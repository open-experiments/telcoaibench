# Golden Serving Config — Findings & Lessons Learned

**Scope:** three "hottest open models" evaluated on TelcoAIBench, plus a serving-config
sweep aimed at accuracy *and* latency.
**Cluster:** venice / `gsma-otel2-test`, 2× RTX PRO 6000 96GB, vLLM v0.26.0-cu129 (UBI-based
serving image), KServe RawDeployment.
**Date:** 2026-08-15

---

## 1. The headline: reasoning is pure cost on this workload

For `qwen3-8-27b`, disabling the model's reasoning block via
`chat_template_kwargs.enable_thinking=false` is **Pareto-dominant** — it wins on
accuracy *and* on every latency measure simultaneously. This is unusual and worth
stating plainly, because the normal expectation is a tradeoff.

### Accuracy

| config | Auto-8 |
|---|---|
| thinking on, 16k budget (parity) | 0.6106 |
| **thinking off, 16k budget** | **0.6536** |
| thinking on, 32k budget | ~0.61 (flat) |

**+0.0430 composite** from turning reasoning off.

### Latency — in-cluster, idle engine, streaming, greedy

| conc | think-on TTFT p50 | think-off TTFT p50 | think-on e2e p95 | **think-off e2e p95** | think-on ans/min | **think-off ans/min** |
|---|---|---|---|---|---|---|
| 1 | 0.09s | 0.08s | 158.6s | **17.0s** | 1.4 | **11.4** |
| 4 | 0.13s | 0.10s | 333.9s | **14.8s** | 0.7 | **16.3** |
| 8 | 0.20s | 0.13s | 171.0s | **15.8s** | 1.3 | **30.5** |
| 16 | 0.28s | 0.16s | 627.7s | **16.1s** | 1.5 | **59.8** |
| 32 | 0.53s | 0.32s | 650.5s | **16.5s** | 5.3 | **116.6** |
| 64 | 1.01s | 0.52s | 235.1s | **20.7s** | 7.6 | **184.8** |

Aggregate throughput: 29 → **435 tok/s** (think-off, conc 1 → 64) versus 29 → 210 (think-on).
Mean output tokens per answer: **141 vs 1,654** — a 12× reduction.

### Recommended golden config

```
--max-model-len=65536 --gpu-memory-utilization=0.92 --max-num-seqs=64
--tensor-parallel-size=1 --disable-custom-all-reduce
```
with **`chat_template_kwargs: {"enable_thinking": false}`** sent per request, at
**concurrency 32–64**.

- p50 latency ~3s, p95 ~17–21s, TTFT ~0.3–0.5s
- 117–185 answers/min on a single 96GB card
- Throughput was still climbing at 64 (266 → 435 tok/s from 32 → 64), so the
  saturation knee is **above 64** and remains unmeasured.

---

## 2. Why reasoning-on is disqualifying for a served product

The p50 is fine at every concurrency level (7–10s). The problem is the tail:
**p95 runs 20–70× p50, peaking at 10.5 minutes for a single answer.**

This is not queueing. TTFT stays under 0.6s even at 32-way, so the engine is
responsive throughout — it is per-request decode behaviour. A minority of prompts
send the model into thousands of tokens of self-talk; mean output swings
1,288 → 4,218 tokens depending purely on which prompts land in a batch.

**No amount of capacity fixes this.** Adding GPUs reduces queueing, not spiral length.

The same mechanism corrupted the benchmark itself: on `teletables`, **35% of answers
hit the 16k token cap mid-reasoning and scored 0**, producing an apparent accuracy of
0.210. With reasoning off the same model scores 0.310 — level with base Qwen3.6's
0.320. **The "weakness" was an artifact of the serving config, not the model.**

---

## 3. Model findings

### Final board (composite = Auto-8 suites ×1, telcos_last_exam ×2, vendor_genai ×1.5)

| | Auto-8 | Judged | **Composite** | gap (judged−auto) |
|---|---|---|---|---|
| telecomgpt-r1 (telecom fine-tune) | 0.7506 | 0.5191 | **0.6802** | −0.2315 |
| **muse-glimmer-30b** | 0.6040 | 0.6012 | **0.6031** | **−0.0028** |
| **qwen3-8-27b** | 0.6590 | 0.4352 | **0.5909** | −0.2238 |
| qwen3-6-27b (base family) | 0.4818 | 0.5359 | 0.4982 | +0.0541 |

### Qwen3.8-27B — strong on paper, weak when held out
- Beats TelecomGPT-R1 on `telemath` (0.720 vs 0.620) and `6g_bench` (0.807 vs 0.720).
- Gains **+0.129 Auto-8 over its own base family** (Qwen3.6-27B) — a real
  generation-over-generation improvement.
- But **collapses on judged suites**: `vendor_genai` 0.332, `telcos_last_exam` 0.513.
- Its **−0.224 judged-vs-auto gap is statistically indistinguishable from
  TelecomGPT-R1's −0.232** — the signature we have been calling contamination-suspect.
- Verified this is *not* an artifact of best-of-N retention: the clean single-config
  comparison (thinking off on both halves) gives −0.2184.

### Muse-Glimmer-30B — the standout
- **Beats the telecom fine-tune on both judged suites**: `telcos_last_exam` 0.647 vs
  0.595, `vendor_genai` 0.540 vs 0.418.
- **Judged−auto gap of −0.003 — essentially zero.** Held-out performance equals
  benchmark performance. No other model on this board comes close to that.
- Takes `3gpp` outright from TelecomGPT-R1 (0.540 vs 0.520) — the first general-purpose
  model to win a contamination-suspect suite.
- `telelogs` 0.510 vs base-family 0.050 — a 10× jump on the suite where every other
  general model collapses.
- Cheap to run: 112 min for all 8 suites vs Qwen3.8's 236, and 0.4% truncation vs 5%.

### MiniMax-H3 — not benchmarkable
`pipeline_tag: image-text-to-video`, `library_name: minimax-h3`, diffusers with an audio
VAE and separate text encoder. It generates video with synchronised audio and has **no
chat-completions interface**. Category mismatch, not a serving difficulty. Dropped.

---

## 4. Infrastructure & harness lessons

### 4.1 `gpt-5.5` as judge is silently broken
Both judged suites returned **exactly 0.000 across every sample**. Diagnosed by swapping
only the judge on an otherwise identical run:

| judge | vendor_genai (24 samples) |
|---|---|
| `gpt-5.5` | **0.000** |
| `gpt-5.6-sol` | **0.540** |

The judged code path wraps each sample in `try/except` that scores 0.0 on any exception,
so a failing judge is indistinguishable from a model that answers everything wrong.
**Action taken:** `gpt-5.5` retired; `gpt-5.6-sol` is the judge going forward.
**Action outstanding:** the harness should fail loudly on a uniform-zero judged suite
rather than recording it as a score.

### 4.2 The portal's model list was hardcoded
`models_init()` seeded the registry from env vars and a JSON file, then never reconciled
against the cluster. Torn-down models kept their cards; a model that *was* serving had no
card at all. Replaced with **KServe InferenceService discovery** (namespace-scoped
read-only RBAC): adopts what is serving, retires what is not, leaves external endpoints
like OpenAI alone. Card metadata (engine version, context length) is now probed rather
than printed as a literal — the previous UI labelled `api.openai.com` as "vLLM".

### 4.3 Per-model engine override
`mk_runtime` hardcoded the pinned vLLM image, so a model whose architecture the pinned
engine cannot load could only be recorded as *unservable* — which is how `ling-3-0-flash`
ended up on the board. Now takes a per-model `image` override.
Muse Glimmer runs on vLLM's day-0 build (`0.26.1rc1.dev608`) because
`MuseGlimmerForConditionalGeneration` is absent from the registry at both 0.26.0 and
0.27.1 (support PR #51655 still open).
**Consistency item:** `ling-3-0-flash` was excluded under a rule we no longer follow and
should be revisited.

### 4.4 Best-of-N retention is invisible by default
Leaderboard retention keeps the better of two runs for the same model. Running N config
variants therefore produces a best-of-N score on a board where every other model got one
run. `attempts` was already recorded but never displayed; added a **`Runs` column** that
renders "best of N".
**Still open:** the column shows the run *count*, not that the winning run used a
different sampling config. Publishing Qwen3.8's best-of-3 needs a config footnote, not
just a count.

### 4.5 Live progress is per-session
Gradio holds generator state per browser session, so a run started by the in-cluster
driver shows "Idle" in every other tab. Observability (server-side polling) and the
Leaderboard (shared PVC) are cross-session; the Benchmark tab is not.
**Outstanding:** persist per-run progress to the shared PVC and render from it.

---

## 5. Methodology notes

- **Suite wall-clock is not latency.** The benchmark harness reports throughput under its
  own concurrency. A sizing decision needs per-request latency at a known concurrency,
  measured on an idle engine. These differ by an order of magnitude.
- **Small-sample truncation rates mislead.** A 12-sample smoke put Qwen3.8's truncation at
  17% (±11%); the full 1,000-sample run put it at 2.5%. Acting on the smoke number would
  have meant raising the token budget for the wrong reason.
- **Screen for uniform failure before trusting any score.** Both a 0.000 judged suite and a
  0.210 auto suite looked like model quality and were not.
- **The judged suites are where the money is.** Auto-8 ranking put Qwen3.8 above Muse
  Glimmer; the composite reverses it. Any claim based on auto-scored suites alone would
  have been wrong.

---
