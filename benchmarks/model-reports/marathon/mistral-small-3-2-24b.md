# mistral-small-3-2-24b - TelcoAIBench Marathon Report

**HF repo:** `mistralai/Mistral-Small-3.2-24B-Instruct-2506`  
**Serving:** vLLM v0.26.0 (KServe RawDeployment, 1x RTX PRO 6000 Blackwell 96GB) | args: `--tokenizer-mode=mistral --config-format=mistral --load-format=mistral`  
**Endpoint at test time:** `http://mistral-small-3-2-24b-predictor.gsma-otel2-test.svc.cluster.local:8080`  

## Results

| Suite | Accuracy | StdErr | Samples | Tier | Date |
|---|---|---|---|---|---|
| 3gpp | **0.530** | 0.0502 | 100 | lite | 2026-08-11 |
| 6g_bench | **0.780** | 0.0339 | 150 | lite | 2026-08-11 |
| oranbench | **0.760** | 0.035 | 150 | lite | 2026-08-11 |
| srsranbench | **0.773** | 0.0343 | 150 | lite | 2026-08-11 |
| telelogs | **0.240** | 0.0429 | 100 | lite | 2026-08-11 |
| telemath | **0.390** | 0.049 | 100 | lite | 2026-08-11 |
| teleqna | **0.760** | 0.0135 | 1000 | lite | 2026-08-11 |
| teletables | **0.290** | 0.0456 | 100 | lite | 2026-08-11 |

## Generation behavior

| Suite | Samples | Mean latency (s) | Mean output tokens |
|---|---|---|---|
| 3gpp | 100 | 0.9 | 10 |
| 6g_bench | 150 | 0.7 | 6 |
| oranbench | 150 | 0.3 | 6 |
| srsranbench | 150 | 0.5 | 6 |
| telelogs | 100 | 29.6 | 858 |
| telemath | 100 | 27.1 | 880 |
| teleqna | 1000 | 0.3 | 6 |
| teletables | 100 | 0.3 | 6 |

## Sample misses (first per suite, for audit)

- **3gpp** dataset index 0: expected `SA5`, parsed `SA1` - output: "{"WORKING GROUP": "SA1"}"
- **3gpp** dataset index 2: expected `CT1`, parsed `SA2` - output: "{"WORKING GROUP": "SA2"}"
- **3gpp** dataset index 4: expected `RAN_AH1`, parsed `RAN1` - output: "{"WORKING GROUP": "RAN1"}"
- **6g_bench** dataset index 3: expected `C`, parsed `B` - output: "ANSWER: B"
- **6g_bench** dataset index 4: expected `C`, parsed `B` - output: "ANSWER: B"
- **6g_bench** dataset index 9: expected `B`, parsed `A` - output: "ANSWER: A"
- **oranbench** dataset index 5: expected `A`, parsed `B` - output: "ANSWER: B"
- **oranbench** dataset index 12: expected `C`, parsed `D` - output: "ANSWER: D"
- **oranbench** dataset index 22: expected `C`, parsed `B` - output: "ANSWER: B"
- **srsranbench** dataset index 1: expected `A`, parsed `B` - output: "ANSWER: B"

---
*Per-sample transcripts (full question/answer/verdict JSONL) are archived on the portal state volume under `benchmark-results/`, one directory per suite run, named by model. Scores flow to the [leaderboard](../../docs/data/LEADERBOARD.md) automatically.*
