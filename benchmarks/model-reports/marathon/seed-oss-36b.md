# seed-oss-36b - TelcoAIBench Marathon Report

**HF repo:** `ByteDance-Seed/Seed-OSS-36B-Instruct`  
**Serving:** vLLM v0.26.0 (KServe RawDeployment, 1x RTX PRO 6000 Blackwell 96GB)  
**Endpoint at test time:** `http://seed-oss-36b-predictor.gsma-otel2-test.svc.cluster.local:8080`  

## Results

| Suite | Accuracy | StdErr | Samples | Tier | Date |
|---|---|---|---|---|---|
| oranbench | **0.753** | 0.0353 | 150 | lite | 2026-08-11 |
| srsranbench | **0.813** | 0.0319 | 150 | lite | 2026-08-11 |
| telemath | **0.520** | 0.0502 | 100 | lite | 2026-08-11 |
| teleqna | **0.770** | 0.0133 | 1000 | lite | 2026-08-11 |
| teletables | **0.380** | 0.0488 | 100 | lite | 2026-08-11 |

## AI Grid tier fit (measured, MCQ phase)

**Recommended placement: Tier 3 (Region)** - 36B params, 72GB bf16, ~86.4s/answer, ~1718 tokens/answer.
Notes: verbose/slow decode - latency envelope only fits a tier up

| Axis (AIGrid) | Measured accuracy |
|---|---|
| knowledge | 0.779 |
| math | 0.520 |
| structured | 0.380 |

*Fitment from measured accuracy, decode speed, verbosity and VRAM - refreshes after the judged pass.*

---
*Per-sample transcripts (full question/answer/verdict JSONL) are archived on the portal state volume under `benchmark-results/`, one directory per suite run, named by model. Scores flow to the [leaderboard](../../docs/data/LEADERBOARD.md) automatically.*
