#!/usr/bin/env python3
"""
Telco-AIX Self-Contained Telco LLM Eval Framework
==================================================
Runs the Open-Telco benchmark suite (TeleQnA, TeleTables, TeleMath, TeleLogs,
3GPP-TSG, ORANBench, srsRANBench, 6G-Bench) against any OpenAI-compatible
endpoint (vLLM, RHOAI, etc.) using datasets EMBEDDED in this repository.

No external dependency beyond `requests` (pip install requests).
Datasets, prompts, and scoring logic are a faithful port of gsma-labs/evals
(Inspect AI) as snapshotted on 2026-08-07 — see datasets/PROVENANCE.md.
Scoring parity was validated against Inspect AI runs (see README.md).

Usage:
  python3 otel_eval.py --endpoint https://my-model.example.com/v1 \
      --model my-model-name [--api-key KEY] \
      [--tasks teleqna,telemath] [--tier lite|full] [--limit N] \
      [--max-connections 12] [--temperature 0.0] [--max-tokens N] \
      [--insecure | --ca-bundle path.pem] [--output-dir results]

Author: Telco-AIX (open-experiments) - 2026
"""

import argparse
import concurrent.futures as cf
import datetime
import gzip
import json
import math
import os
import re
import sys
import threading
import time

try:
    import requests
except ImportError:
    sys.exit("This tool needs the 'requests' package:  pip install requests")

HERE = os.path.dirname(os.path.abspath(__file__))

# --------------------------------------------------------------------------
# Prompt templates (verbatim ports from gsma-labs/evals @ 2026-08-07)
# --------------------------------------------------------------------------

MC_TEMPLATE = (
    "Answer the following multiple choice question. The entire content of "
    "your response should be of the following format: 'ANSWER: $LETTER' "
    "(without quotes) where LETTER is one of {letters}.\n\n"
    "{question}\n\n{choices}"
)

TELEMATH_SYSTEM_PROMPT = r"""You are an expert problem solver. Your task is to solve numerical exercises by following these guidelines:
1.  **Understand the Goal:** Clearly identify what the problem is asking you to find, paying close attention to the required units for the final answer.
2.  **Reason Step-by-Step:** Provide a clear, sequential reasoning process. Explain the formulas, principles, or logic used in each step. Show intermediate calculations if they clarify your thought process. The detailed structure of your sub-steps is up to you, as long as the reasoning is sound and easy to follow.
3.  **Unit Management:**
    *   Track units throughout your calculations.
    *   **Crucially, ensure your final numerical answer is converted to the specific units requested in the problem statement.** If intermediate calculations result in a different unit, perform a final conversion step.
    *   State the unit of the final answer clearly in your explanatory text *before* the boxed answer.
4.  **Final Numerical Answer Format:**
    *   The final answer must be a single numerical value (integer or float).
    *   Present this numerical value exclusively within the `\$\boxed{{...}}\$` format.
    *   **CRITICAL:** The `\$\boxed{{...}}\$` block must contain *only* the number. No text, no units, no labels (e.g., NOT `\$\boxed{{Result: 50}}\$` or `\$\boxed{{50 \text{{ mA}}}}\$`, but `\$\boxed{{50}}\$`)."""

BOXED_PATTERN = re.compile(r"\\boxed\{((?:[^{}]|\{[^{}]*\})*)\}")
WHITESPACE_PATTERN = re.compile(r"\n\s*")
DIGIT_PATTERN = re.compile(r"\d+")
ANSWER_PATTERN = re.compile(r"(?i)ANSWER\s*:\s*\(?([A-Za-z])\)?")
WG_PATTERN = re.compile(r"([A-Z]+\d+(?:-[A-Z]+)?)", re.IGNORECASE)
SCORE_PATTERN = re.compile(r"(?i)SCORE\s*:\s*(\d+(?:\.\d+)?)")

JUDGE_REFERENCE_PROMPT = """You are a strict telecommunications examination grader.
Grade the candidate answer ONLY against the official reference answer key
and the grading notes below. Award credit for correct methodology, correct
numerical results (allow minor rounding), correct use of specifications,
and completeness. Penalize fabricated specifics, wrong formulas, and
missing sub-questions. A perfect 10 requires matching the reference in
substance.

QUESTION:
{question}

REFERENCE ANSWER KEY (ground truth):
{reference}

GRADING NOTES (must-haves and known error patterns):
{notes}

CANDIDATE ANSWER:
{candidate}

Return ONLY a JSON object, no other text, exactly in this shape:
{{"score": <0-10, decimals allowed>,
  "missed": [<short strings: each required element the candidate missed or got wrong>],
  "verdict": "<one sentence: dominant strength or failure>",
  "rationale": "<3-6 sentences justifying the score against the reference>"}}"""

JUDGE_RUBRIC_PROMPT = """You are a strict telecommunications technology analyst
grading a vendor-technology deep-dive answer. Grade on four criteria,
each 0-10:
1. technical_accuracy - claims consistent with public knowledge; no
   invented product names, versions, interfaces, or performance figures.
2. completeness - every numbered part of the question is addressed.
3. depth - concrete components, interfaces, and quantitative reasoning
   rather than marketing prose.
4. honesty - separates public knowledge from speculation; abstains
   rather than inventing. Award honesty credit for explicit "not public /
   requires vendor engagement" statements.

GRADING CONTEXT - established public facts you must treat as true
(the candidate cannot see this):
{anchors}

KNOWN FABRICATION PATTERNS to specifically check for:
{bait}

If unsure whether a specific claim is fabricated, deduct depth rather
than technical_accuracy.

QUESTION:
{question}

CANDIDATE ANSWER:
{candidate}

Return ONLY a JSON object, no other text, exactly in this shape:
{{"technical_accuracy": <0-10>, "completeness": <0-10>,
  "depth": <0-10>, "honesty": <0-10>,
  "verdict": "<one sentence: dominant strength or failure>",
  "rationale": "<3-6 sentences citing specific claims judged right or wrong>"}}"""

RUBRIC_WEIGHTS = {"technical_accuracy": 0.40, "honesty": 0.25,
                  "completeness": 0.20, "depth": 0.15}


def parse_judge_json(text):
    """Extract the first JSON object from judge output; None on failure."""
    if not text:
        return None
    start = text.find("{")
    while start != -1:
        depth = 0
        for i in range(start, len(text)):
            if text[i] == "{":
                depth += 1
            elif text[i] == "}":
                depth -= 1
                if depth == 0:
                    try:
                        return json.loads(text[start:i + 1])
                    except json.JSONDecodeError:
                        break
        start = text.find("{", start + 1)
    return None


def parse_judge_score(text):
    m = SCORE_PATTERN.findall(text or "")
    if not m:
        return None
    try:
        return max(0.0, min(10.0, float(m[-1]))) / 10.0
    except ValueError:
        return None


def parse_boxed(response: str) -> str:
    if not response:
        return ""
    matches = BOXED_PATTERN.findall(response)
    if not matches:
        return ""
    ans = WHITESPACE_PATTERN.sub("", matches[-1].strip())
    return ans.lstrip(":").rstrip("./")


def first_int(text: str):
    m = DIGIT_PATTERN.search(text or "")
    return int(m.group()) if m else None


# --------------------------------------------------------------------------
# Scorers (ports of the Inspect AI scorers used by gsma-labs/evals)
# --------------------------------------------------------------------------

def score_mcq(completion: str, record: dict):
    """Port of inspect multiple_choice/choice(): expects 'ANSWER: X'."""
    target = chr(65 + int(record["answer"]))
    matches = ANSWER_PATTERN.findall(completion or "")
    parsed = matches[-1].upper() if matches else ""
    if not parsed:
        stripped = (completion or "").strip()
        if len(stripped) == 1 and stripped.isalpha():
            parsed = stripped.upper()
    return parsed == target, parsed, target


def score_telemath(completion: str, record: dict):
    """Boxed numeric answer, correct if within 1% rel or 0.01 abs."""
    target = str(record["answer"])
    parsed = parse_boxed(completion)
    try:
        ok = math.isclose(float(parsed), float(target), rel_tol=0.01, abs_tol=0.01)
    except (ValueError, TypeError):
        ok = False
    return ok, parsed, target


def score_telelogs(completion: str, record: dict):
    """'soft' eval: first integer of boxed answer equals first int of target."""
    target = str(record["answer"])
    parsed = parse_boxed(completion)
    p, t = first_int(parsed), first_int(target)
    return (p is not None and p == t), parsed, target


def score_three_gpp(completion: str, record: dict):
    """Port of inspect pattern() scorer with WG_PATTERN: first regex match."""
    target = str(record["answer"])
    m = WG_PATTERN.search(completion or "")
    parsed = m.group(1) if m else ""
    return parsed.lower() == target.lower(), parsed, target


# --------------------------------------------------------------------------
# Task registry
# --------------------------------------------------------------------------

def build_mcq_prompt(record: dict):
    choices = record["choices"]
    letters = ",".join(chr(65 + i) for i in range(len(choices)))
    lines = "\n".join(f"{chr(65 + i)}) {c}" for i, c in enumerate(choices))
    user = MC_TEMPLATE.format(letters=letters, question=record["question"], choices=lines)
    return [{"role": "user", "content": user}]


def build_plain_prompt(record: dict):
    return [{"role": "user", "content": record["question"]}]


def build_telemath_prompt(record: dict):
    return [
        {"role": "system", "content": TELEMATH_SYSTEM_PROMPT},
        {"role": "user", "content": record["question"]},
    ]


def build_exam_prompt(record: dict):
    return [{"role": "system", "content":
             "You are a telecommunications expert taking a rigorous exam. "
             "Answer completely, show detailed calculations, provide specific "
             "numerical values, and cite relevant 3GPP specifications."},
            {"role": "user", "content": record["question"]}]


TASKS = {
    "teleqna":     {"prompt": build_mcq_prompt,      "score": score_mcq},
    "teletables":  {"prompt": build_mcq_prompt,      "score": score_mcq},
    "oranbench":   {"prompt": build_mcq_prompt,      "score": score_mcq},
    "srsranbench": {"prompt": build_mcq_prompt,      "score": score_mcq},
    "6g_bench":    {"prompt": build_mcq_prompt,      "score": score_mcq},
    "telemath":    {"prompt": build_telemath_prompt, "score": score_telemath},
    "telelogs":    {"prompt": build_plain_prompt,    "score": score_telelogs},
    "3gpp":        {"prompt": build_plain_prompt,    "score": score_three_gpp},
    # LLM-as-judge suites (need --judge-* / a judge model in the portal)
    "telcos_last_exam": {"prompt": build_exam_prompt, "judged": "reference",
                         "path": "telcos-last-exam/datasets/telcos_last_exam.jsonl.gz"},
    # 2026 expansion batch 1 (30 expert q, 260 pts); full 2026 exam = this + legacy, points-weighted
    "telcos_last_exam_2026": {"prompt": build_exam_prompt, "judged": "reference",
                         "path": "telcos-last-exam/datasets/telcos_last_exam_2026.jsonl.gz"},
    "vendor_genai":     {"prompt": build_plain_prompt, "judged": "rubric",
                         "path": "vendor-genai-tests/datasets/vendor_genai.jsonl.gz"},
}

JUDGED_TASKS = [k for k, v in TASKS.items() if v.get("judged")]

LEADERBOARD_TASKS = [
    "teleqna", "teletables", "oranbench", "srsranbench",
    "telemath", "telelogs", "3gpp",
]


def load_dataset(task: str, tier: str, limit=None):
    spec = TASKS.get(task, {})
    if spec.get("path"):
        # suite datasets live under benchmarks/<suite>/ (sibling of open-telco)
        path = os.path.join(os.path.dirname(HERE), spec["path"])
    else:
        path = os.path.join(HERE, "datasets", tier, f"{task}.jsonl.gz")
    records = []
    with gzip.open(path, "rt", encoding="utf-8") as f:
        for line in f:
            records.append(json.loads(line))
            if limit and len(records) >= limit:
                break
    return records


# --------------------------------------------------------------------------
# OpenAI-compatible client (thread-safe, retrying)
# --------------------------------------------------------------------------

class Client:
    def __init__(self, endpoint, model, api_key="none", temperature=0.0,
                 max_tokens=None, verify=True, timeout=1800, max_retries=6,
                 extra_body=None, stream=True, abort_event=None):
        self.stream = stream
        self.abort_event = abort_event
        self.url = endpoint.rstrip("/") + "/chat/completions"
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.verify = verify
        self.timeout = timeout
        self.max_retries = max_retries
        self.extra_body = extra_body or {}
        self.headers = {"Content-Type": "application/json",
                        "Authorization": f"Bearer {api_key}"}
        self.local = threading.local()

    def _session(self):
        if not hasattr(self.local, "s"):
            self.local.s = requests.Session()
        return self.local.s

    def chat(self, messages):
        """Streaming by default: proxies/routers (kube-rbac-proxy, haproxy,
        corporate egress) silently kill long-idle non-streaming responses;
        SSE keeps bytes flowing so long generations survive any idle timeout."""
        body = {"model": self.model, "messages": messages,
                "temperature": self.temperature}
        if self.max_tokens:
            body["max_tokens"] = self.max_tokens
        if self.stream:
            body["stream"] = True
            body["stream_options"] = {"include_usage": True}
        body.update(self.extra_body)
        delay = 2.0
        last_err = None
        adapts_left = 3
        for _ in range(self.max_retries):
            if self.abort_event is not None and self.abort_event.is_set():
                raise RuntimeError("aborted by stop request")
            try:
                if self.stream:
                    return self._chat_stream(body)
                r = self._session().post(self.url, headers=self.headers,
                                         json=body, timeout=self.timeout,
                                         verify=self.verify)
                if r.status_code == 200:
                    d = r.json()
                    msg = d["choices"][0]["message"]
                    usage = d.get("usage", {})
                    return (msg.get("content") or ""), usage
                last_err = f"HTTP {r.status_code}: {r.text[:200]}"
                if r.status_code == 400 and adapts_left and self._adapt_body(body, r.text):
                    adapts_left -= 1
                    continue  # retry immediately with adapted params
                if r.status_code in (400, 401, 403, 404, 422):
                    break  # non-retryable
            except (requests.RequestException, RuntimeError) as e:
                msg = str(e)
                last_err = msg
                if "HTTP 400" in msg and adapts_left and self._adapt_body(body, msg):
                    adapts_left -= 1
                    continue
            time.sleep(delay)
            delay = min(delay * 2, 60)
        raise RuntimeError(f"request failed after retries: {last_err}")

    @staticmethod
    def _adapt_body(body, err_text):
        """OpenAI reasoning models (gpt-5 family) reject 'max_tokens' (want
        'max_completion_tokens') and any non-default temperature. Adapt the
        payload in place based on the server's 400 message; return True if
        something changed so the caller retries once."""
        t = (err_text or "").lower()
        changed = False
        if "max_tokens" in t and "max_tokens" in body:
            # reasoning tokens count against the cap - give headroom
            body["max_completion_tokens"] = max(body.pop("max_tokens"), 4096)
            changed = True
        if "temperature" in t and "temperature" in body:
            body.pop("temperature")
            changed = True
        return changed

    def _chat_stream(self, body):
        parts, usage = [], {}
        with self._session().post(self.url, headers=self.headers, json=body,
                                  timeout=(30, self.timeout), stream=True,
                                  verify=self.verify) as r:
            if r.status_code != 200:
                raise RuntimeError(f"HTTP {r.status_code}: {r.text[:200]}")
            for line in r.iter_lines(decode_unicode=True):
                if self.abort_event is not None and self.abort_event.is_set():
                    # closing the streaming connection aborts the generation
                    # on the vLLM server within seconds
                    raise RuntimeError("aborted by stop request")
                if not line or not line.startswith("data:"):
                    continue
                payload = line[5:].strip()
                if payload == "[DONE]":
                    break
                try:
                    chunk = json.loads(payload)
                except json.JSONDecodeError:
                    continue
                if chunk.get("usage"):
                    usage = chunk["usage"]
                for ch in chunk.get("choices") or []:
                    delta = (ch.get("delta") or {}).get("content")
                    if delta:
                        parts.append(delta)
        return "".join(parts), usage


# --------------------------------------------------------------------------
# Runner
# --------------------------------------------------------------------------

def run_task(task, tier, client, workers, limit, out_dir, progress_cb=None,
             stop_event=None, judge_client=None):
    """Run one benchmark.

    progress_cb(done, total, correct), if given, is invoked after every
    completed sample (used by the portal's live Benchmark tab).
    stop_event (threading.Event), if given and set mid-run, cancels all
    queued samples; in-flight requests finish and partial results are
    returned with "stopped": True.
    """
    records = load_dataset(task, tier, limit)
    spec = TASKS[task]
    results = [None] * len(records)
    done = correct = 0
    lock = threading.Lock()

    judged_mode = spec.get("judged")

    def one(i):
        rec = records[i]
        t0 = time.time()
        judge_note = None
        try:
            completion, usage = client.chat(spec["prompt"](rec))
            if judged_mode:
                if judge_client is None:
                    raise RuntimeError(
                        f"task '{task}' needs a judge model (configure one)")
                if judged_mode == "reference":
                    jp = JUDGE_REFERENCE_PROMPT.format(
                        question=rec["question"],
                        reference=rec.get("reference_answer", ""),
                        notes=rec.get("grading_notes", "(none provided)"),
                        candidate=completion)
                else:
                    jp = JUDGE_RUBRIC_PROMPT.format(
                        question=rec["question"], candidate=completion,
                        anchors=rec.get("judge_anchors", "(none provided)"),
                        bait=rec.get("fabrication_bait", "(none provided)"))
                judge_note, _ = judge_client.chat(
                    [{"role": "user", "content": jp}])
                jd = parse_judge_json(judge_note)
                judge_detail = {}
                if jd and judged_mode == "reference" and "score" in jd:
                    score = max(0.0, min(10.0, float(jd["score"]))) / 10.0
                    judge_detail = {"missed": jd.get("missed", []),
                                    "verdict": jd.get("verdict", ""),
                                    "rationale": jd.get("rationale", "")}
                elif jd and judged_mode == "rubric" and "technical_accuracy" in jd:
                    crit = {k: max(0.0, min(10.0, float(jd.get(k, 0))))
                            for k in RUBRIC_WEIGHTS}
                    score = sum(crit[k] * w for k, w in RUBRIC_WEIGHTS.items()) / 10.0
                    judge_detail = {"criteria": crit,
                                    "verdict": jd.get("verdict", ""),
                                    "rationale": jd.get("rationale", "")}
                else:
                    score = parse_judge_score(judge_note)  # legacy fallback
                    if score is None:
                        raise RuntimeError(
                            "judge returned neither valid JSON nor a SCORE line")
                ok, parsed, target = score, f"{score*10:.1f}/10", "judge"
            else:
                ok, parsed, target = spec["score"](completion, rec)
            err = None
        except Exception as e:
            completion, usage, ok, parsed, target, err = "", {}, 0.0, "", "", str(e)
        meta = {}
        if judged_mode:
            for k in ("id", "title", "domain", "difficulty", "points", "vendor"):
                if rec.get(k) is not None:
                    meta[k] = rec[k]
        row = {"index": i, "correct": bool(ok) if not judged_mode else None,
               "score": float(ok), "parsed": parsed,
               "target": target, "error": err,
               "judge_rationale": judge_note,
               "latency_s": round(time.time() - t0, 2),
               "output_tokens": usage.get("completion_tokens"),
               "completion": completion}
        row.update(meta)
        if judged_mode:
            try:
                row.update(judge_detail)
            except NameError:
                pass
        return i, row

    stopped = False
    with cf.ThreadPoolExecutor(max_workers=workers) as ex:
        futs = [ex.submit(one, i) for i in range(len(records))]
        for fut in cf.as_completed(futs):
            if stop_event is not None and stop_event.is_set() and not stopped:
                stopped = True
                for f_ in futs:
                    f_.cancel()
            if fut.cancelled():
                continue
            i, row = fut.result()
            results[i] = row
            with lock:
                done += 1
                correct += row.get("score", 1.0 if row["correct"] else 0.0)
                if progress_cb:
                    try:
                        progress_cb(done, len(records), correct)
                    except Exception:
                        pass
                if done % 25 == 0 or done == len(records):
                    print(f"  {task}: {done}/{len(records)}  "
                          f"acc={correct/done:.3f}", flush=True)

    done_rows = [r for r in results if r is not None]
    if stopped:
        done_rows = [r for r in done_rows
                     if not (r["error"] and "abort" in str(r["error"]))]
    n = len(done_rows)
    scores = [r.get("score", 1.0 if r["correct"] else 0.0) for r in done_rows]
    if judged_mode == "reference" and any(r.get("points") for r in done_rows):
        wts = [float(r.get("points", 1)) for r in done_rows]
        acc = (sum(sc * w for sc, w in zip(scores, wts)) / sum(wts)) if n else 0.0
    else:
        acc = sum(scores) / n if n else 0.0
    if n > 1:
        m_ = sum(scores) / n
        var = sum((x - m_) ** 2 for x in scores) / (n - 1)
        stderr = math.sqrt(var / n)
    else:
        stderr = 0.0

    breakdown = {}
    if judged_mode:
        def _agg(key):
            groups = {}
            for r in done_rows:
                k = r.get(key)
                if k is None:
                    continue
                w = float(r.get("points", 1))
                g = groups.setdefault(k, [0.0, 0.0, 0])
                g[0] += r.get("score", 0.0) * w
                g[1] += w
                g[2] += 1
            return {k: {"score": round(v[0] / v[1], 4), "n": v[2]}
                    for k, v in groups.items() if v[1]}
        for key in ("domain", "difficulty", "vendor"):
            b = _agg(key)
            if b:
                breakdown[key] = b
        crits = [r["criteria"] for r in done_rows if r.get("criteria")]
        if crits:
            breakdown["criteria"] = {
                k: round(sum(c[k] for c in crits) / len(crits), 2)
                for k in crits[0]}
    errors = sum(1 for r in done_rows if r["error"])
    with open(os.path.join(out_dir, f"{task}.jsonl"), "w") as w:
        for r in done_rows:
            w.write(json.dumps(r, ensure_ascii=False) + "\n")
    return {"task": task, "tier": tier, "n": n, "accuracy": round(acc, 4),
            "stderr": round(stderr, 4), "request_errors": errors,
            "stopped": stopped, "total_planned": len(records),
            "breakdown": breakdown if judged_mode else {}}


# ---------------------------------------------------------------------------
# Run report: what failed, how, and at what level
# ---------------------------------------------------------------------------

def _sev(score):
    if score >= 0.8: return "pass"
    if score >= 0.6: return "partial"
    if score >= 0.4: return "weak"
    return "fail"


def build_report(out_dir, summaries, context):
    """Write REPORT.md and REPORT.html into out_dir from per-sample
    transcripts. context: dict with model/endpoint/judge/tier/date."""
    tasks = []
    for sm in summaries:
        task = sm["task"]
        rows = []
        p = os.path.join(out_dir, f"{task}.jsonl")
        if os.path.exists(p):
            with open(p) as fh:
                rows = [json.loads(l) for l in fh if l.strip()]
        rows.sort(key=lambda r: r.get("score", 0.0))
        tasks.append((sm, rows))

    # ---------------- markdown ----------------
    L = []
    L.append(f"# Benchmark Report - {context.get('model','?')}")
    L.append("")
    L.append(f"Endpoint: `{context.get('endpoint','?')}` | "
             f"Judge: `{context.get('judge','-')}` | "
             f"Tier: {context.get('tier','?')} | {context.get('date','')}")
    L.append("")
    L.append("| Task | n | Score | StdErr | Errors |")
    L.append("|---|---|---|---|---|")
    for sm, _ in tasks:
        L.append(f"| {sm['task']} | {sm['n']} | {sm['accuracy']:.4f} | "
                 f"±{sm['stderr']:.4f} | {sm.get('request_errors',0)} |")
    for sm, rows in tasks:
        bd = sm.get("breakdown") or {}
        L.append("")
        L.append(f"## {sm['task']}")
        for key in ("domain", "difficulty", "vendor"):
            if bd.get(key):
                L.append("")
                L.append(f"**By {key}:** " + " | ".join(
                    f"{k}: {v['score']:.3f} (n={v['n']})"
                    for k, v in sorted(bd[key].items())))
        if bd.get("criteria"):
            L.append("")
            L.append("**Criteria means (0-10):** " + " | ".join(
                f"{k}: {v}" for k, v in bd["criteria"].items()))
        judged = any(r.get("verdict") or r.get("criteria") for r in rows)
        if judged:
            L.append("")
            L.append("### Per-question results (worst first)")
            L.append("")
            L.append("| ID | Title/Vendor | Level | Score | Verdict |")
            L.append("|---|---|---|---|---|")
            for r in rows:
                ident = r.get("id", r.get("index"))
                title = r.get("title") or (
                    f"{r.get('vendor','')} / {r.get('domain','')}".strip(" /"))
                lvl = r.get("difficulty") or r.get("domain") or "-"
                v = (r.get("verdict") or r.get("error") or "").replace("|", "/")
                L.append(f"| {ident} | {title[:48]} | {lvl} | "
                         f"{r.get('score',0):.2f} | {v[:110]} |")
            fails = [r for r in rows if r.get("score", 0) < 0.6 or r.get("error")]
            if fails:
                L.append("")
                L.append("### Failure detail")
                for r in fails:
                    ident = r.get("id", r.get("index"))
                    L.append("")
                    L.append(f"**{ident}** - score {r.get('score',0):.2f} "
                             f"({_sev(r.get('score',0))})"
                             + (f" - {r.get('points','?')} pts" if r.get('points') else ""))
                    if r.get("error"):
                        L.append(f"- error: `{str(r['error'])[:200]}`")
                    if r.get("missed"):
                        for mi in r["missed"][:8]:
                            L.append(f"- missed: {mi}")
                    if r.get("criteria"):
                        L.append("- criteria: " + ", ".join(
                            f"{k}={v:g}" for k, v in r["criteria"].items()))
                    if r.get("rationale"):
                        L.append(f"- judge: {str(r['rationale'])[:500]}")
    md = "\n".join(L)
    with open(os.path.join(out_dir, "REPORT.md"), "w") as fh:
        fh.write(md)

    # ---------------- html ----------------
    def bar(v, mx=1.0, color="#8B5CF6"):
        pct = max(0, min(100, v / mx * 100))
        return (f'<div style="background:#1E293B;border-radius:4px;height:14px;'
                f'width:160px;display:inline-block;vertical-align:middle">'
                f'<div style="background:{color};width:{pct:.0f}%;height:14px;'
                f'border-radius:4px"></div></div> {v:.2f}')
    H = ['<html><head><meta charset="utf-8"><title>Benchmark Report</title>',
         '<style>body{background:#0B1120;color:#E2E8F0;font-family:Helvetica,'
         'Arial,sans-serif;max-width:1080px;margin:24px auto;padding:0 16px}'
         'table{border-collapse:collapse;width:100%;font-size:14px}'
         'td,th{border-bottom:1px solid #1E293B;padding:7px 10px;text-align:left}'
         'th{color:#64748B;text-transform:uppercase;font-size:11.5px}'
         'h1{font-size:24px}h2{color:#8B5CF6;margin-top:34px}'
         'h3{color:#22D3EE}code{background:#1E293B;padding:1px 6px;'
         'border-radius:4px;font-size:12.5px}'
         '.fail{color:#EF4444}.weak{color:#FBBF24}.partial{color:#22D3EE}'
         '.pass{color:#10B981}.card{background:#111827;border:1px solid #1E293B;'
         'border-radius:10px;padding:14px 18px;margin:10px 0}</style></head><body>']
    H.append(f"<h1>Benchmark Report - {context.get('model','?')}</h1>")
    H.append(f"<p>Endpoint <code>{context.get('endpoint','?')}</code> | "
             f"Judge <code>{context.get('judge','-')}</code> | "
             f"Tier {context.get('tier','?')} | {context.get('date','')}</p>")
    for sm, rows in tasks:
        H.append(f"<h2>{sm['task']} - {sm['accuracy']:.4f} "
                 f"&plusmn;{sm['stderr']:.4f} (n={sm['n']})</h2>")
        bd = sm.get("breakdown") or {}
        for key in ("domain", "difficulty", "vendor"):
            if bd.get(key):
                H.append(f'<div class="card"><b>By {key}</b><table>')
                for k, v in sorted(bd[key].items()):
                    H.append(f"<tr><td>{k}</td><td>{bar(v['score'])}</td>"
                             f"<td>n={v['n']}</td></tr>")
                H.append("</table></div>")
        if bd.get("criteria"):
            H.append('<div class="card"><b>Criteria (0-10)</b><table>')
            for k, v in bd["criteria"].items():
                H.append(f"<tr><td>{k}</td><td>{bar(v, 10, '#22D3EE')}</td></tr>")
            H.append("</table></div>")
        if any(r.get("verdict") or r.get("criteria") for r in rows):
            H.append("<h3>Per-question (worst first)</h3><table>"
                     "<tr><th>ID</th><th>Title</th><th>Level</th>"
                     "<th>Score</th><th>Verdict</th></tr>")
            for r in rows:
                sv = _sev(r.get("score", 0))
                title = r.get("title") or (
                    f"{r.get('vendor','')} / {r.get('domain','')}".strip(" /"))
                H.append(f'<tr><td>{r.get("id", r.get("index"))}</td>'
                         f"<td>{title[:60]}</td>"
                         f"<td>{r.get('difficulty') or r.get('domain') or '-'}</td>"
                         f'<td class="{sv}">{r.get("score",0):.2f}</td>'
                         f"<td>{(r.get('verdict') or r.get('error') or '')[:140]}</td></tr>")
            H.append("</table>")
            fails = [r for r in rows if r.get("score", 0) < 0.6 or r.get("error")]
            if fails:
                H.append("<h3>Failure detail</h3>")
                for r in fails:
                    H.append('<div class="card">')
                    H.append(f'<b>{r.get("id", r.get("index"))}</b> - '
                             f'<span class="{_sev(r.get("score",0))}">'
                             f'score {r.get("score",0):.2f}</span>')
                    if r.get("error"):
                        H.append(f"<div>error: <code>{str(r['error'])[:200]}</code></div>")
                    if r.get("missed"):
                        H.append("<ul>" + "".join(
                            f"<li>missed: {mi}</li>" for mi in r["missed"][:8]) + "</ul>")
                    if r.get("criteria"):
                        H.append("<div>" + " | ".join(
                            f"{k}={v:g}" for k, v in r["criteria"].items()) + "</div>")
                    if r.get("rationale"):
                        H.append(f'<div style="color:#94A3B8;font-size:13px;'
                                 f'margin-top:6px">{str(r["rationale"])[:600]}</div>')
                    H.append("</div>")
    H.append("</body></html>")
    with open(os.path.join(out_dir, "REPORT.html"), "w") as fh:
        fh.write("\n".join(H))
    return os.path.join(out_dir, "REPORT.html")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--endpoint", required=True,
                    help="OpenAI-compatible base URL ending in /v1")
    ap.add_argument("--model", required=True, help="served model name")
    ap.add_argument("--api-key", default="none")
    ap.add_argument("--tasks", default=",".join(LEADERBOARD_TASKS),
                    help=f"comma list from: {','.join(TASKS)} (default: 7 leaderboard tasks)")
    ap.add_argument("--tier", choices=["lite", "full"], default="lite")
    ap.add_argument("--limit", type=int, default=None, help="cap samples per task")
    ap.add_argument("--max-connections", type=int, default=12)
    ap.add_argument("--temperature", type=float, default=0.0)
    ap.add_argument("--max-tokens", type=int, default=8192,
                    help="generation cap per request (default 8192; 0 = uncapped). "
                         "Prevents pathological runaway generations at temperature 0.")
    ap.add_argument("--timeout", type=int, default=1800)
    ap.add_argument("--insecure", action="store_true",
                    help="disable TLS verification (self-signed lab certs)")
    ap.add_argument("--ca-bundle", default=None, help="path to CA bundle PEM")
    ap.add_argument("--no-stream", action="store_true",
                    help="use non-streaming requests (streaming is default; it "
                         "survives proxy/router idle timeouts on long generations)")
    ap.add_argument("--extra-body", default=None,
                    help='JSON merged into each request, e.g. '
                         '\'{"chat_template_kwargs":{"enable_thinking":true}}\'')
    ap.add_argument("--judge-endpoint", default=None,
                    help="OpenAI-compatible base URL of the judge model "
                         "(required for telcos_last_exam / vendor_genai)")
    ap.add_argument("--judge-model", default=None)
    ap.add_argument("--judge-key", default="none")
    ap.add_argument("--output-dir", default=os.path.join(HERE, "results"))
    args = ap.parse_args()

    if args.insecure:
        import urllib3
        urllib3.disable_warnings()
    verify = False if args.insecure else (args.ca_bundle or True)
    tasks = [t.strip() for t in args.tasks.split(",") if t.strip()]
    for t in tasks:
        if t not in TASKS:
            sys.exit(f"unknown task '{t}' — choose from {','.join(TASKS)}")

    max_tokens = args.max_tokens if args.max_tokens and args.max_tokens > 0 else None
    client = Client(args.endpoint, args.model, args.api_key, args.temperature,
                    max_tokens, verify, args.timeout,
                    extra_body=json.loads(args.extra_body) if args.extra_body else None,
                    stream=not args.no_stream)

    judge_client = None
    if args.judge_endpoint and args.judge_model:
        judge_client = Client(args.judge_endpoint.rstrip("/") +
                              ("" if args.judge_endpoint.rstrip("/").endswith("/v1") else "/v1"),
                              args.judge_model, args.judge_key,
                              temperature=0.0, max_tokens=2048,
                              verify=verify, timeout=args.timeout)
    needs_judge = [t for t in tasks if TASKS[t].get("judged")]
    if needs_judge and judge_client is None:
        sys.exit(f"tasks {needs_judge} require --judge-endpoint/--judge-model")

    stamp = datetime.datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
    safe_model = re.sub(r"[^A-Za-z0-9._-]", "_", args.model)
    out_dir = os.path.join(args.output_dir, f"{stamp}_{safe_model}_{args.tier}")
    os.makedirs(out_dir, exist_ok=True)

    print(f"Model: {args.model} @ {args.endpoint}")
    print(f"Tasks: {tasks}  tier={args.tier}  limit={args.limit}  "
          f"conn={args.max_connections}  temp={args.temperature}")
    summary = []
    for t in tasks:
        print(f"== {t} ==", flush=True)
        summary.append(run_task(t, args.tier, client, args.max_connections,
                                args.limit, out_dir,
                                judge_client=judge_client))
    try:
        build_report(out_dir, summary, {
            "model": args.model, "endpoint": args.endpoint,
            "judge": args.judge_model or "-", "tier": args.tier,
            "date": stamp})
        print(f"report: {os.path.join(out_dir, 'REPORT.html')}")
    except Exception as e:
        print(f"report generation failed: {e}")

    avg = sum(s["accuracy"] for s in summary) / len(summary) if summary else 0
    meta = {"model": args.model, "endpoint": args.endpoint, "tier": args.tier,
            "temperature": args.temperature, "max_tokens": args.max_tokens,
            "timestamp": stamp, "average": round(avg, 4), "tasks": summary}
    with open(os.path.join(out_dir, "summary.json"), "w") as w:
        json.dump(meta, w, indent=2)

    lines = ["| Benchmark | n | Accuracy | ± stderr |", "|---|---|---|---|"]
    for s in summary:
        lines.append(f"| {s['task']} | {s['n']} | {s['accuracy']:.4f} | {s['stderr']:.4f} |")
    lines.append(f"| **Average** | | **{avg:.4f}** | |")
    md = (f"# Eval results — {args.model} ({args.tier})\n\n"
          f"{stamp} · temp={args.temperature} · endpoint={args.endpoint}\n\n"
          + "\n".join(lines) + "\n")
    with open(os.path.join(out_dir, "SUMMARY.md"), "w") as w:
        w.write(md)
    print("\n" + md)
    print(f"Results written to {out_dir}")


if __name__ == "__main__":
    main()
