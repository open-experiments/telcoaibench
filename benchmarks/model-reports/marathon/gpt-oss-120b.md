# gpt-oss-120b - TelcoAIBench Marathon Report

**HF repo:** `openai/gpt-oss-120b`  
**Serving:** vLLM v0.26.0 (KServe RawDeployment, 1x RTX PRO 6000 Blackwell 96GB) | args: `--max-model-len=32768`  
**Endpoint at test time:** `http://gpt-oss-120b-predictor.gsma-otel2-test.svc.cluster.local:8080`  

## Results

| Suite | Accuracy | StdErr | Samples | Tier | Date |
|---|---|---|---|---|---|
| 3gpp | **0.300** | 0.0461 | 100 | lite | 2026-08-10 |
| 6g_bench | **0.660** | 0.0388 | 150 | lite | 2026-08-10 |
| oranbench | **0.793** | 0.0332 | 150 | lite | 2026-08-10 |
| srsranbench | **0.847** | 0.0295 | 150 | lite | 2026-08-10 |
| telelogs | **0.480** | 0.0502 | 100 | lite | 2026-08-10 |
| telemath | **0.660** | 0.0476 | 100 | lite | 2026-08-10 |
| teleqna | **0.809** | 0.0124 | 1000 | lite | 2026-08-10 |
| teletables | **0.290** | 0.0456 | 100 | lite | 2026-08-10 |

## Generation behavior

| Suite | Samples | Mean latency (s) | Mean output tokens |
|---|---|---|---|
| 3gpp | 100 | 3.1 | 253 |
| 6g_bench | 150 | 7.9 | 675 |
| oranbench | 150 | 2.5 | 199 |
| srsranbench | 150 | 2.1 | 169 |
| telelogs | 100 | 16.1 | 1332 |
| telemath | 100 | 13.2 | 1115 |
| teleqna | 1000 | 3.0 | 196 |
| teletables | 100 | 5.1 | 433 |

## Sample misses (first per suite, for audit)

- **3gpp** dataset index 0: expected `SA5`, parsed `SA2` - output: "{"WORKING GROUP": "SA2"}"
- **3gpp** dataset index 1: expected `RAN4`, parsed `RAN2` - output: "{"WORKING GROUP": "RAN2"}"
- **3gpp** dataset index 2: expected `CT1`, parsed `SA2` - output: "{"WORKING GROUP": "SA2"}"
- **6g_bench** dataset index 4: expected `C`, parsed `B` - output: "ANSWER: B"
- **6g_bench** dataset index 7: expected `B`, parsed `A` - output: "ANSWER: A"
- **6g_bench** dataset index 9: expected `B`, parsed `A` - output: "ANSWER: A"
- **oranbench** dataset index 8: expected `B`, parsed `A` - output: "ANSWER: A"
- **oranbench** dataset index 19: expected `D`, parsed `A` - output: "ANSWER: A"
- **oranbench** dataset index 22: expected `C`, parsed `B` - output: "ANSWER: B"
- **srsranbench** dataset index 0: expected `A`, parsed `C` - output: "ANSWER: C"

---
*Per-sample transcripts (full question/answer/verdict JSONL) are archived on the portal state volume under `benchmark-results/`, one directory per suite run, named by model. Scores flow to the [leaderboard](../../docs/data/LEADERBOARD.md) automatically.*
