# granite-4-0-h-small - TelcoAIBench Marathon Report

**HF repo:** `ibm-granite/granite-4.0-h-small`  
**Serving:** vLLM v0.26.0 (KServe RawDeployment, 1x RTX PRO 6000 Blackwell 96GB)  
**Endpoint at test time:** `http://granite-4-0-h-small-predictor.gsma-otel2-test.svc.cluster.local:8080`  

## Results

| Suite | Accuracy | StdErr | Samples | Tier | Date |
|---|---|---|---|---|---|
| 3gpp | **0.300** | 0.0461 | 100 | lite | 2026-08-12 |
| 6g_bench | **0.687** | 0.038 | 150 | lite | 2026-08-12 |
| oranbench | **0.733** | 0.0362 | 150 | lite | 2026-08-12 |
| srsranbench | **0.680** | 0.0382 | 150 | lite | 2026-08-12 |
| telelogs | **0.250** | 0.0435 | 100 | lite | 2026-08-12 |
| telemath | **0.330** | 0.0473 | 100 | lite | 2026-08-12 |
| teleqna | **0.690** | 0.0146 | 1000 | lite | 2026-08-12 |
| teletables | **0.270** | 0.0446 | 100 | lite | 2026-08-12 |

## Generation behavior

| Suite | Samples | Mean latency (s) | Mean output tokens |
|---|---|---|---|
| 3gpp | 100 | 0.6 | 11 |
| 6g_bench | 150 | 0.4 | 5 |
| oranbench | 150 | 0.3 | 5 |
| srsranbench | 150 | 0.3 | 5 |
| telelogs | 100 | 23.7 | 774 |
| telemath | 100 | 28.7 | 1088 |
| teleqna | 1000 | 0.7 | 5 |
| teletables | 100 | 0.6 | 18 |

## Sample misses (first per suite, for audit)

- **3gpp** dataset index 1: expected `RAN4`, parsed `RAN5` - output: "{"WORKING GROUP": "RAN5"}"
- **3gpp** dataset index 2: expected `CT1`, parsed `SA4` - output: "{"WORKING GROUP": "SA4"}"
- **3gpp** dataset index 4: expected `RAN_AH1`, parsed `RAN1` - output: "{"WORKING GROUP": "RAN1"}"
- **6g_bench** dataset index 0: expected `A`, parsed `C` - output: "ANSWER: C"
- **6g_bench** dataset index 3: expected `C`, parsed `D` - output: "ANSWER: D"
- **6g_bench** dataset index 4: expected `C`, parsed `B` - output: "ANSWER: B"
- **oranbench** dataset index 8: expected `B`, parsed `A` - output: "ANSWER: A"
- **oranbench** dataset index 12: expected `C`, parsed `D` - output: "ANSWER: D"
- **oranbench** dataset index 22: expected `C`, parsed `B` - output: "ANSWER: B"
- **srsranbench** dataset index 0: expected `A`, parsed `C` - output: "ANSWER: C"

## AI Grid tier fit (measured, auto-scored phase)

**Recommended placement: Tier 2 (Provider Edge)** - 32B params, 64GB bf16, ~6.9s/answer, ~238 tokens/answer.


| Axis (AIGrid) | Measured accuracy |
|---|---|
| knowledge | 0.701 |
| protocol | 0.493 |
| math | 0.330 |
| fault | 0.250 |
| structured | 0.270 |

*Fitment from measured accuracy, decode speed, verbosity and VRAM - refreshes after the judged pass.*

---
*Per-sample transcripts (full question/answer/verdict JSONL) are archived on the portal state volume under `benchmark-results/`, one directory per suite run, named by model. Scores flow to the [leaderboard](../../../docs/data/LEADERBOARD.md) automatically.*
