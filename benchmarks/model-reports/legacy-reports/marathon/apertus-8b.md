# apertus-8b - TelcoAIBench Marathon Report

**HF repo:** `swiss-ai/Apertus-8B-Instruct-2509`  
**Serving:** vLLM v0.26.0 (KServe RawDeployment, 1x RTX PRO 6000 Blackwell 96GB)  
**Endpoint at test time:** `http://apertus-8b-predictor.gsma-otel2-test.svc.cluster.local:8080`  

## Results

| Suite | Accuracy | StdErr | Samples | Tier | Date |
|---|---|---|---|---|---|
| 3gpp | **0.240** | 0.0429 | 100 | lite | 2026-08-12 |
| 6g_bench | **0.447** | 0.0407 | 150 | lite | 2026-08-12 |
| oranbench | **0.587** | 0.0403 | 150 | lite | 2026-08-12 |
| srsranbench | **0.747** | 0.0356 | 150 | lite | 2026-08-12 |
| telelogs | **0.100** | 0.0302 | 100 | lite | 2026-08-12 |
| telemath | **0.110** | 0.0314 | 100 | lite | 2026-08-12 |
| teleqna | **0.633** | 0.0152 | 1000 | lite | 2026-08-12 |
| teletables | **0.220** | 0.0416 | 100 | lite | 2026-08-12 |

## Generation behavior

| Suite | Samples | Mean latency (s) | Mean output tokens |
|---|---|---|---|
| 3gpp | 100 | 0.3 | 11 |
| 6g_bench | 150 | 0.2 | 3 |
| oranbench | 150 | 0.1 | 6 |
| srsranbench | 150 | 0.1 | 6 |
| telelogs | 100 | 10.1 | 764 |
| telemath | 100 | 29.0 | 2121 |
| teleqna | 1000 | 0.2 | 5 |
| teletables | 100 | 0.4 | 6 |

## Sample misses (first per suite, for audit)

- **3gpp** dataset index 0: expected `SA5`, parsed `RAN1` - output: "{"WORKING GROUP": "RAN1"}"
- **3gpp** dataset index 1: expected `RAN4`, parsed `RAN1` - output: "{"WORKING GROUP": "RAN1"}"
- **3gpp** dataset index 2: expected `CT1`, parsed `RAN1` - output: "{"WORKING GROUP": "RAN1"}"
- **6g_bench** dataset index 0: expected `A`, parsed `D` - output: "D"
- **6g_bench** dataset index 1: expected `A`, parsed `B` - output: "B"
- **6g_bench** dataset index 2: expected `C`, parsed `B` - output: "B"
- **oranbench** dataset index 2: expected `A`, parsed `B` - output: "ANSWER: B"
- **oranbench** dataset index 3: expected `C`, parsed `A` - output: "ANSWER: A"
- **oranbench** dataset index 5: expected `A`, parsed `B` - output: "ANSWER: B"
- **srsranbench** dataset index 2: expected `A`, parsed `C` - output: "ANSWER: C"

## AI Grid tier fit (measured, auto-scored phase)

**Recommended placement: Tier 1 (User Edge)** - 8B params, 16GB bf16, ~5.0s/answer, ~365 tokens/answer.


| Axis (AIGrid) | Measured accuracy |
|---|---|
| knowledge | 0.655 |
| protocol | 0.343 |
| math | 0.110 |
| fault | 0.100 |
| structured | 0.220 |

*Fitment from measured accuracy, decode speed, verbosity and VRAM - refreshes after the judged pass.*

---
*Per-sample transcripts (full question/answer/verdict JSONL) are archived on the portal state volume under `benchmark-results/`, one directory per suite run, named by model. Scores flow to the [leaderboard](../../../docs/data/LEADERBOARD.md) automatically.*
