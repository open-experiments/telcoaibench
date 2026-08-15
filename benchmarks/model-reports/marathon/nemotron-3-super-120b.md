# nemotron-3-super-120b - TelcoAIBench Marathon Report

**HF repo:** `nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-FP8`  
**Serving:** vLLM v0.26.0 (KServe RawDeployment, 1x RTX PRO 6000 Blackwell 96GB) | args: `--max-model-len=32768 --trust-remote-code --tensor-parallel-size=2`  
**Endpoint at test time:** `http://nemotron-3-super-120b-predictor.gsma-otel2-test.svc.cluster.local:8080`  

## Results

| Suite | Accuracy | StdErr | Samples | Tier | Date |
|---|---|---|---|---|---|
| 3gpp | **0.370** | 0.0485 | 100 | lite | 2026-08-13 |
| 6g_bench | **0.453** | 0.0408 | 150 | lite | 2026-08-13 |
| oranbench | **0.787** | 0.0336 | 150 | lite | 2026-08-13 |
| srsranbench | **0.800** | 0.0328 | 150 | lite | 2026-08-13 |
| telelogs | **0.580** | 0.0496 | 100 | lite | 2026-08-13 |
| telemath | **0.690** | 0.0465 | 100 | lite | 2026-08-13 |
| teleqna | **0.798** | 0.0127 | 1000 | lite | 2026-08-13 |
| teletables | **0.180** | 0.0386 | 100 | lite | 2026-08-13 |

## AI Grid tier fit (measured, auto-scored phase)

**Recommended placement: Tier 4 (Core DC)** - 124B params, 124GB fp8 moe(12B act), ~4.2s/answer, ~None tokens/answer.
Notes: served quantized (fp8 moe(12B act))

| Axis (AIGrid) | Measured accuracy |
|---|---|
| knowledge | 0.795 |
| protocol | 0.412 |
| math | 0.690 |
| fault | 0.580 |
| structured | 0.180 |

*Fitment from measured accuracy, decode speed, verbosity and VRAM - refreshes after the judged pass.*

---
*Per-sample transcripts (full question/answer/verdict JSONL) are archived on the portal state volume under `benchmark-results/`, one directory per suite run, named by model. Scores flow to the [leaderboard](../../../docs/data/LEADERBOARD.md) automatically.*
