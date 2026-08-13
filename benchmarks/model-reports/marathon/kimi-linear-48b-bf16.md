# kimi-linear-48b-bf16 - TelcoAIBench Marathon Report

**HF repo:** `moonshotai/Kimi-Linear-48B-A3B-Instruct`  
**Serving:** vLLM v0.26.0 (KServe RawDeployment, 1x RTX PRO 6000 Blackwell 96GB) | args: `--max-model-len=32768 --trust-remote-code --tensor-parallel-size=2`  
**Endpoint at test time:** `http://kimi-linear-48b-bf16-predictor.gsma-otel2-test.svc.cluster.local:8080`  

## Results

| Suite | Accuracy | StdErr | Samples | Tier | Date |
|---|---|---|---|---|---|
| 3gpp | **0.330** | 0.0473 | 100 | lite | 2026-08-13 |
| 6g_bench | **0.233** | 0.0346 | 150 | lite | 2026-08-13 |
| oranbench | **0.547** | 0.0408 | 150 | lite | 2026-08-13 |
| srsranbench | **0.760** | 0.035 | 150 | lite | 2026-08-13 |
| telelogs | **0.040** | 0.0197 | 100 | lite | 2026-08-13 |
| telemath | **0.360** | 0.0482 | 100 | lite | 2026-08-13 |
| teleqna | **0.672** | 0.0149 | 1000 | lite | 2026-08-13 |
| teletables | **0.040** | 0.0197 | 100 | lite | 2026-08-13 |

## AI Grid tier fit (measured, auto-scored phase)

**Recommended placement: Tier 2 (Provider Edge)** - 48B params, 97GB bf16 moe(3B act), ~2.3s/answer, ~None tokens/answer.


| Axis (AIGrid) | Measured accuracy |
|---|---|
| knowledge | 0.660 |
| protocol | 0.282 |
| math | 0.360 |
| fault | 0.040 |
| structured | 0.040 |

*Fitment from measured accuracy, decode speed, verbosity and VRAM - refreshes after the judged pass.*

## Quantisation control: did we benchmark Kimi, or a quantiser?

This run exists to answer one question. The marathon's first Kimi-Linear
entry used `nm-testing/Kimi-Linear-48B-A3B-Instruct-FP8-DYNAMIC` - an FP8
quantisation published by a third party, **not** Moonshot's release - and
it scored poorly. Attributing that to "Kimi" would have been unsound, so
that entry was removed from the board and the official bf16 weights were
run here under identical conditions (same suites, same prompts, same vLLM
0.26.0, same greedy decoding; bf16 needs 97GB so it runs tensor-parallel
across both GPUs).

| Suite | FP8 (third-party) | bf16 (official) | delta |
|---|---|---|---|
| teleqna | 0.663 | **0.672** | +0.009 |
| teletables | 0.100 | 0.040 | -0.060 |
| oranbench | 0.553 | 0.547 | -0.006 |
| srsranbench | 0.800 | 0.760 | -0.040 |
| telemath | 0.360 | 0.360 | 0.000 |
| telelogs | 0.070 | 0.040 | -0.030 |
| 3gpp | 0.360 | 0.330 | -0.030 |
| 6g_bench | 0.187 | **0.233** | +0.046 |
| **mean** | **0.387** | **0.373** | **-0.014** |

**Result: the quantisation hypothesis is rejected.** Every per-suite
delta is within run-to-run noise, the deltas fall on both sides of zero,
and the official bf16 weights are marginally *worse* on average. FP8-
dynamic quantisation did not cost this model anything measurable on the
telecom suites - its weak showing is the model, not the build.

Two things follow. First, removing the third-party entry was still the
right call: a leaderboard should name what it actually served, and the
provenance was wrong regardless of the outcome. Second, the conclusion
about Kimi-Linear on telecom stands unchanged, and now rests on
Moonshot's own weights.

*Caveat: this is a single paired run per suite, not a repeated-seed study.
It is strong enough to reject a large quantisation penalty; it cannot
resolve differences of a few points.*

---
*Per-sample transcripts (full question/answer/verdict JSONL) are archived on the portal state volume under `benchmark-results/`, one directory per suite run, named by model. Scores flow to the [leaderboard](../../docs/data/LEADERBOARD.md) automatically.*
