# eurollm-22b - TelcoAIBench Marathon Report

**HF repo:** `utter-project/EuroLLM-22B-Instruct-2512`  
**Serving:** vLLM v0.26.0 (KServe RawDeployment, 1x RTX PRO 6000 Blackwell 96GB) | args: `--max-model-len=32768`  
**Endpoint at test time:** `http://eurollm-22b-predictor.gsma-otel2-test.svc.cluster.local:8080`  

## Results

| Suite | Accuracy | StdErr | Samples | Tier | Date |
|---|---|---|---|---|---|
| 3gpp | **0.210** | 0.0409 | 100 | lite | 2026-08-12 |
| 6g_bench | **0.693** | 0.0378 | 150 | lite | 2026-08-12 |
| oranbench | **0.707** | 0.0373 | 150 | lite | 2026-08-12 |
| srsranbench | **0.720** | 0.0368 | 150 | lite | 2026-08-12 |
| telelogs | **0.140** | 0.0349 | 100 | lite | 2026-08-12 |
| telemath | **0.200** | 0.0402 | 100 | lite | 2026-08-12 |
| teleqna | **0.682** | 0.0147 | 1000 | lite | 2026-08-12 |
| teletables | **0.260** | 0.0441 | 100 | lite | 2026-08-12 |

## Generation behavior

| Suite | Samples | Mean latency (s) | Mean output tokens |
|---|---|---|---|
| 3gpp | 100 | 1.0 | 15 |
| 6g_bench | 150 | 0.7 | 6 |
| oranbench | 150 | 0.3 | 6 |
| srsranbench | 150 | 0.6 | 6 |
| telelogs | 100 | 50.1 | 1418 |
| telemath | 100 | 57.5 | 1709 |
| teleqna | 1000 | 0.3 | 6 |
| teletables | 100 | 0.3 | 6 |

## Sample misses (first per suite, for audit)

- **3gpp** dataset index 0: expected `SA5`, parsed `SA3` - output: "{"WORKING GROUP": "SA3"}"
- **3gpp** dataset index 1: expected `RAN4`, parsed `RAN1` - output: "{"WORKING GROUP": "RAN1"}"
- **3gpp** dataset index 2: expected `CT1`, parsed `SA3` - output: "{"WORKING GROUP": "SA3"}"
- **6g_bench** dataset index 0: expected `A`, parsed `D` - output: "ANSWER: D"
- **6g_bench** dataset index 2: expected `C`, parsed `B` - output: "ANSWER: B"
- **6g_bench** dataset index 3: expected `C`, parsed `B` - output: "ANSWER: B"
- **oranbench** dataset index 1: expected `C`, parsed `A` - output: "ANSWER: A"
- **oranbench** dataset index 8: expected `B`, parsed `A` - output: "ANSWER: A"
- **oranbench** dataset index 12: expected `C`, parsed `A` - output: "ANSWER: A"
- **srsranbench** dataset index 0: expected `A`, parsed `C` - output: "ANSWER: C"

---
*Per-sample transcripts (full question/answer/verdict JSONL) are archived on the portal state volume under `benchmark-results/`, one directory per suite run, named by model. Scores flow to the [leaderboard](../../../docs/data/LEADERBOARD.md) automatically.*
