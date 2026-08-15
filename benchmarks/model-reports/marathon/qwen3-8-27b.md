# qwen3-8-27b - TelcoAIBench Marathon Report

**HF repo:** `Qwen/Qwen3.8-27B`  
**Serving:** vLLM v0.26.0 (KServe RawDeployment, 1x RTX PRO 6000 Blackwell 96GB)  
**Endpoint at test time:** `http://qwen3-8-27b-predictor.gsma-otel2-test.svc.cluster.local:8080`  

> **Config note:** board scores are **best of 3 serving configs**; the winning run
> used the golden config - **reasoning disabled** via
> `chat_template_kwargs: {"enable_thinking": false}` - which is Pareto-dominant on
> this workload: +0.043 Auto-8 *and* 6.9x faster wall-clock than thinking-on.
> Full sweep in [docs/lessons-learned.md](../../../docs/lessons-learned.md).

## Results

| Suite | Accuracy | StdErr | Samples | Tier | Date | Runs |
|---|---|---|---|---|---|---|
| 3gpp | **0.340** | 0.0476 | 100 | lite | 2026-08-15 | 2 |
| 6g_bench | **0.807** | 0.0324 | 150 | lite | 2026-08-15 | 2 |
| oranbench | **0.787** | 0.0336 | 150 | lite | 2026-08-15 | 3 |
| srsranbench | **0.887** | 0.026 | 150 | lite | 2026-08-14 | 3 |
| telcos_last_exam | **0.513** | 0.0341 | 30 | lite | 2026-08-15 | 1 |
| telelogs | **0.610** | 0.049 | 100 | lite | 2026-08-15 | 2 |
| telemath | **0.720** | 0.0451 | 100 | lite | 2026-08-15 | 2 |
| teleqna | **0.812** | 0.0124 | 1000 | lite | 2026-08-15 | 3 |
| teletables | **0.310** | 0.0465 | 100 | lite | 2026-08-14 | 3 |
| vendor_genai | **0.332** | 0.0196 | 24 | lite | 2026-08-15 | 1 |

Judged suites (`telcos_last_exam`, `vendor_genai`) scored by **gpt-5.6-sol**.
Composite **0.5909** | Auto-8 **0.6590** | judged-auto gap **-0.2238**.

## Generation behavior (golden config, loadprofile on idle engine)

| conc | TTFT p50 | e2e p95 | answers/min |
|---|---|---|---|
| 1 | 0.08s | 17.0s | 11.4 |
| 8 | 0.13s | 15.8s | 30.5 |
| 32 | 0.32s | 16.5s | 116.6 |
| 64 | 0.52s | 20.7s | 184.8 |

Mean output tokens **141** (vs 1,654 thinking-on - 12x reduction); aggregate
throughput 435 tok/s at conc 64 and still climbing - the saturation knee is
above 64 and unmeasured. Full-set truncation rate 2.5% (a 12-sample smoke had
suggested 17% - see lessons-learned on small samples).

## Run wall-clock (driver logs)

Auto-scored passes 2026-08-14/15 (Jobs `lb-run-qwen` thinking-on, `lb-v1-nothink`
golden config); judged pass 2026-08-15 (Job `lb-judged-qwen`, thinking off).

| Suite | thinking-on (min) | golden config (min) |
|---|---|---|
| teleqna | 59 | <1 |
| teletables | 40 | 5 |
| oranbench | 15 | <1 |
| srsranbench | 13 | <1 |
| telemath | 29 | 9 |
| telelogs | 51 | 16 |
| 3gpp | 12 | <1 |
| 6g_bench | 17 | 4 |
| telcos_last_exam (judged) | - | 10 |
| vendor_genai (judged) | - | 4 |

## Notable results

- **Best Auto-8 among general-purpose models** (0.6590): beats telecomgpt-r1 on
  telemath (0.720 vs 0.620) and 6g_bench (0.807 vs 0.720), and posts +0.129 Auto-8
  over its own base family (qwen3-6-27b) - a real generation-over-generation gain.
- **Collapses on the held-out judged suites** (vendor_genai 0.332,
  telcos_last_exam 0.513). The -0.224 judged-auto gap is statistically
  indistinguishable from telecomgpt-r1's -0.232 - the contamination-suspect
  signature. Verified not to be a best-of-N artifact: the clean single-config
  comparison gives -0.2184.
- teletables 0.210 under thinking-on was a serving artifact (35% of answers hit
  the 16k token cap mid-reasoning and scored 0); the golden config scores 0.310,
  level with the base family.

## AI Grid tier fit (measured)

**Recommended placement: Tier 2 (Provider Edge)** - 27B params, 56GB bf16, ~3 s/answer p50 (idle engine, conc 32-64, thinking off).

| Axis (AIGrid) | Measured accuracy |
|---|---|
| knowledge | 0.828 |
| protocol | 0.573 |
| math | 0.720 |
| fault | 0.610 |
| structured | 0.310 |

*Fitment from measured accuracy, decode speed, verbosity and VRAM.*

---
*Per-sample transcripts (full question/answer/verdict JSONL) are archived on the portal state volume under `benchmark-results/`, one directory per suite run, named by model. Scores flow to the [leaderboard](../../../docs/data/LEADERBOARD.md) automatically.*
