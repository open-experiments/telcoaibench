# exaone-4-0-32b - TelcoAIBench Marathon Report

**HF repo:** `LGAI-EXAONE/EXAONE-4.0-32B`  
**Serving:** vLLM v0.26.0 (KServe RawDeployment, 1x RTX PRO 6000 Blackwell 96GB)  
**Endpoint at test time:** `http://exaone-4-0-32b-predictor.gsma-otel2-test.svc.cluster.local:8080`  

## Results

| Suite | Accuracy | StdErr | Samples | Tier | Date |
|---|---|---|---|---|---|
| 3gpp | **0.280** | 0.0451 | 100 | lite | 2026-08-11 |
| 6g_bench | **0.673** | 0.0384 | 150 | lite | 2026-08-11 |
| oranbench | **0.760** | 0.035 | 150 | lite | 2026-08-11 |
| srsranbench | **0.833** | 0.0305 | 150 | lite | 2026-08-11 |
| telelogs | **0.180** | 0.0386 | 100 | lite | 2026-08-11 |
| telemath | **0.450** | 0.05 | 100 | lite | 2026-08-11 |
| teleqna | **0.742** | 0.0138 | 1000 | lite | 2026-08-11 |
| teletables | **0.320** | 0.0469 | 100 | lite | 2026-08-11 |

## AI Grid tier fit (measured, MCQ phase)

**Recommended placement: Tier 2 (Provider Edge)** - 32B params, 64GB bf16, ~Nones/answer, ~None tokens/answer.


| Axis (AIGrid) | Measured accuracy |
|---|---|
| knowledge | 0.778 |
| protocol | 0.477 |
| math | 0.450 |
| fault | 0.180 |
| structured | 0.320 |

*Fitment from measured accuracy, decode speed, verbosity and VRAM - refreshes after the judged pass.*

---
*Per-sample transcripts (full question/answer/verdict JSONL) are archived on the portal state volume under `benchmark-results/`, one directory per suite run, named by model. Scores flow to the [leaderboard](../../docs/data/LEADERBOARD.md) automatically.*
