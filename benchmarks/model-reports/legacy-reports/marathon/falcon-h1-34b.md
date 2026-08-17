# falcon-h1-34b - TelcoAIBench Marathon Report

**HF repo:** `tiiuae/Falcon-H1-34B-Instruct`  
**Serving:** vLLM v0.26.0 (KServe RawDeployment, 1x RTX PRO 6000 Blackwell 96GB)  
**Endpoint at test time:** `http://falcon-h1-34b-predictor.gsma-otel2-test.svc.cluster.local:8080`  

## Results

| Suite | Accuracy | StdErr | Samples | Tier | Date |
|---|---|---|---|---|---|
| 3gpp | **0.290** | 0.0456 | 100 | lite | 2026-08-12 |
| 6g_bench | **0.727** | 0.0365 | 150 | lite | 2026-08-12 |
| oranbench | **0.780** | 0.0339 | 150 | lite | 2026-08-12 |
| srsranbench | **0.773** | 0.0343 | 150 | lite | 2026-08-12 |
| telelogs | **0.220** | 0.0416 | 100 | lite | 2026-08-12 |
| telemath | **0.510** | 0.0502 | 100 | lite | 2026-08-12 |
| teleqna | **0.771** | 0.0133 | 1000 | lite | 2026-08-12 |
| teletables | **0.340** | 0.0476 | 100 | lite | 2026-08-12 |

## Generation behavior

| Suite | Samples | Mean latency (s) | Mean output tokens |
|---|---|---|---|
| 3gpp | 100 | 1.6 | 11 |
| 6g_bench | 150 | 1.0 | 4 |
| oranbench | 150 | 0.5 | 4 |
| srsranbench | 150 | 0.5 | 4 |
| telelogs | 100 | 41.1 | 768 |
| telemath | 100 | 37.9 | 794 |
| teleqna | 1000 | 0.9 | 4 |
| teletables | 100 | 0.5 | 4 |

## Sample misses (first per suite, for audit)

- **3gpp** dataset index 0: expected `SA5`, parsed `SA3` - output: "{"WORKING GROUP": "SA3"}"
- **3gpp** dataset index 1: expected `RAN4`, parsed `RAN1` - output: "{"WORKING GROUP": "RAN1"}"
- **3gpp** dataset index 2: expected `CT1`, parsed `SA3` - output: "{"WORKING GROUP": "SA3"}"
- **6g_bench** dataset index 2: expected `C`, parsed `B` - output: "ANSWER: B"
- **6g_bench** dataset index 3: expected `C`, parsed `B` - output: "ANSWER: B"
- **6g_bench** dataset index 5: expected `C`, parsed `A` - output: "ANSWER: A"
- **oranbench** dataset index 2: expected `A`, parsed `B` - output: "ANSWER: B"
- **oranbench** dataset index 8: expected `B`, parsed `C` - output: "ANSWER: C"
- **oranbench** dataset index 22: expected `C`, parsed `B` - output: "ANSWER: B"
- **srsranbench** dataset index 0: expected `A`, parsed `C` - output: "ANSWER: C"

## AI Grid tier fit (measured, auto-scored phase)

**Recommended placement: Tier 2 (Provider Edge)** - 34B params, 67GB bf16, ~10.5s/answer, ~199 tokens/answer.


| Axis (AIGrid) | Measured accuracy |
|---|---|
| knowledge | 0.775 |
| protocol | 0.508 |
| math | 0.510 |
| fault | 0.220 |
| structured | 0.340 |

*Fitment from measured accuracy, decode speed, verbosity and VRAM - refreshes after the judged pass.*

---
*Per-sample transcripts (full question/answer/verdict JSONL) are archived on the portal state volume under `benchmark-results/`, one directory per suite run, named by model. Scores flow to the [leaderboard](../../../docs/data/LEADERBOARD.md) automatically.*
