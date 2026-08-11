# magistral-small-2509 - TelcoAIBench Marathon Report

**HF repo:** `mistralai/Magistral-Small-2509`  
**Serving:** vLLM v0.26.0 (KServe RawDeployment, 1x RTX PRO 6000 Blackwell 96GB) | args: `--tokenizer-mode=mistral --config-format=mistral --load-format=mistral`  
**Endpoint at test time:** `http://magistral-small-2509-predictor.gsma-otel2-test.svc.cluster.local:8080`  

## Results

| Suite | Accuracy | StdErr | Samples | Tier | Date |
|---|---|---|---|---|---|
| 3gpp | **0.510** | 0.0502 | 100 | lite | 2026-08-11 |
| 6g_bench | **0.767** | 0.0346 | 150 | lite | 2026-08-11 |
| oranbench | **0.760** | 0.035 | 150 | lite | 2026-08-11 |
| srsranbench | **0.787** | 0.0336 | 150 | lite | 2026-08-11 |
| telelogs | **0.280** | 0.0451 | 100 | lite | 2026-08-11 |
| telemath | **0.470** | 0.0502 | 100 | lite | 2026-08-11 |
| teleqna | **0.749** | 0.0137 | 1000 | lite | 2026-08-11 |
| teletables | **0.280** | 0.0451 | 100 | lite | 2026-08-11 |

---
*Per-sample transcripts (full question/answer/verdict JSONL) are archived on the portal state volume under `benchmark-results/`, one directory per suite run, named by model. Scores flow to the [leaderboard](../../docs/data/LEADERBOARD.md) automatically.*
