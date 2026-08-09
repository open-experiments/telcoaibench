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
Grade the candidate answer against the official reference answer key.
Award points for correct methodology, correct numerical results (allow minor
rounding), correct use of 3GPP specifications, and completeness. Penalize
fabricated specifics, wrong formulas, and missing sub-questions.
Be strict: a perfect 10 requires matching the reference in substance.

QUESTION:
{question}

REFERENCE ANSWER KEY:
{reference}

CANDIDATE ANSWER:
{candidate}

First give a 3-5 sentence justification, then output the final grade on its
own last line in exactly this format: SCORE: <0-10>"""

JUDGE_RUBRIC_PROMPT = """You are a strict telecommunications technology analyst
grading a vendor-technology deep-dive answer. There is no single reference
answer; grade against this rubric (equal weight):
1. Technical accuracy - claims consistent with public knowledge of the vendor's
   architecture; no fabricated product names, versions, or metrics.
2. Completeness - every numbered section of the request is addressed.
3. Depth - concrete interfaces, components, and quantitative reasoning rather
   than generic marketing language.
4. Honesty - clearly separates publicly known facts from what would require
   vendor engagement; abstains rather than inventing specifics.

QUESTION:
{question}

CANDIDATE ANSWER:
{candidate}

First give a 3-5 sentence justification, then output the final grade on its
own last line in exactly this format: SCORE: <0-10>"""


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
    "sixg_bench":  {"prompt": build_mcq_prompt,      "score": score_mcq},
    "telemath":    {"prompt": build_telemath_prompt, "score": score_telemath},
    "telelogs":    {"prompt": build_plain_prompt,    "score": score_telelogs},
    "three_gpp":   {"prompt": build_plain_prompt,    "score": score_three_gpp},
    # LLM-as-judge suites (need --judge-* / a judge model in the portal)
    "telcos_last_exam": {"prompt": build_exam_prompt, "judged": "reference",
                         "path": "telcos-last-exam/datasets/telcos_last_exam.jsonl.gz"},
    "vendor_genai":     {"prompt": build_plain_prompt, "judged": "rubric",
                         "path": "vendor-genai-tests/datasets/vendor_genai.jsonl.gz"},
}

JUDGED_TASKS = [k for k, v in TASKS.items() if v.get("judged")]

LEADERBOARD_TASKS = [
    "teleqna", "teletables", "oranbench", "srsranbench",
    "telemath", "telelogs", "three_gpp",
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
                if r.status_code in (400, 401, 403, 404, 422):
                    break  # non-retryable
            except (requests.RequestException, RuntimeError) as e:
                last_err = str(e)
            time.sleep(delay)
            delay = min(delay * 2, 60)
        raise RuntimeError(f"request failed after retries: {last_err}")

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
                        candidate=completion)
                else:
                    jp = JUDGE_RUBRIC_PROMPT.format(
                        question=rec["question"], candidate=completion)
                judge_note, _ = judge_client.chat(
                    [{"role": "user", "content": jp}])
                score = parse_judge_score(judge_note)
                if score is None:
                    raise RuntimeError("judge did not return a SCORE line")
                ok, parsed, target = score, f"{score*10:.1f}/10", "judge"
            else:
                ok, parsed, target = spec["score"](completion, rec)
            err = None
        except Exception as e:
            completion, usage, ok, parsed, target, err = "", {}, 0.0, "", "", str(e)
        return i, {"index": i, "correct": bool(ok) if not judged_mode else None,
                   "score": float(ok), "parsed": parsed,
                   "target": target, "error": err,
                   "judge_rationale": judge_note,
                   "latency_s": round(time.time() - t0, 2),
                   "output_tokens": usage.get("completion_tokens"),
                   "completion": completion}

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
    acc = sum(scores) / n if n else 0.0
    if n > 1:
        var = sum((x - acc) ** 2 for x in scores) / (n - 1)
        stderr = math.sqrt(var / n)
    else:
        stderr = 0.0
    errors = sum(1 for r in done_rows if r["error"])
    with open(os.path.join(out_dir, f"{task}.jsonl"), "w") as w:
        for r in done_rows:
            w.write(json.dumps(r, ensure_ascii=False) + "\n")
    return {"task": task, "tier": tier, "n": n, "accuracy": round(acc, 4),
            "stderr": round(stderr, 4), "request_errors": errors,
            "stopped": stopped, "total_planned": len(records)}


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
