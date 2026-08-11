# gpt-oss-20b - TelcoAIBench Marathon Report

**HF repo:** `openai/gpt-oss-20b`  
**Serving:** vLLM v0.26.0 (KServe RawDeployment, 1x RTX PRO 6000 Blackwell 96GB)  
**Endpoint at test time:** `http://gpt-oss-20b-predictor.gsma-otel2-test.svc.cluster.local:8080`  

## Results

| Suite | Accuracy | StdErr | Samples | Tier | Date |
|---|---|---|---|---|---|
| 3gpp | **0.280** | 0.0451 | 100 | lite | 2026-08-10 |
| 6g_bench | **0.660** | 0.0388 | 150 | lite | 2026-08-10 |
| oranbench | **0.787** | 0.0336 | 150 | lite | 2026-08-10 |
| srsranbench | **0.787** | 0.0336 | 150 | lite | 2026-08-10 |
| telelogs | **0.410** | 0.0494 | 100 | lite | 2026-08-10 |
| telemath | **0.610** | 0.049 | 100 | lite | 2026-08-10 |
| teleqna | **0.774** | 0.0132 | 1000 | lite | 2026-08-10 |
| teletables | **0.290** | 0.0456 | 100 | lite | 2026-08-10 |

## Generation behavior

| Suite | Samples | Mean latency (s) | Mean output tokens |
|---|---|---|---|
| 3gpp | 100 | 9.6 | 1341 |
| 6g_bench | 150 | 7.3 | 1075 |
| oranbench | 150 | 3.8 | 519 |
| srsranbench | 150 | 2.5 | 367 |
| telelogs | 100 | 20.4 | 2803 |
| telemath | 100 | 12.5 | 1786 |
| teleqna | 1000 | 3.6 | 409 |
| teletables | 100 | 18.7 | 2508 |

## Sample misses (first per suite, for audit)

- **3gpp** dataset index 0: expected `SA5`, parsed `SA1` - output: "{"WORKING GROUP": "SA1"}"
- **3gpp** dataset index 1: expected `RAN4`, parsed `RAN1` - output: "{"WORKING GROUP": "RAN1"}"
- **3gpp** dataset index 3: expected `SA5`, parsed `CT3` - output: "{"WORKING GROUP": "CT3"}"
- **6g_bench** dataset index 3: expected `C`, parsed `B` - output: "ANSWER: B"
- **6g_bench** dataset index 4: expected `C`, parsed `B` - output: "ANSWER: B"
- **6g_bench** dataset index 7: expected `B`, parsed `A` - output: "ANSWER: A"
- **oranbench** dataset index 5: expected `A`, parsed `B` - output: "ANSWER: B"
- **oranbench** dataset index 8: expected `B`, parsed `D` - output: "ANSWER: D"
- **oranbench** dataset index 22: expected `C`, parsed `B` - output: "ANSWER: B"
- **srsranbench** dataset index 0: expected `A`, parsed `C` - output: "ANSWER: C"

## AI Grid tier fit (measured, auto-scored phase)

**Recommended placement: Tier 2 (Provider Edge)** - 20B params, 13GB mxfp4, ~9.8s/answer, ~1351 tokens/answer.
Notes: served quantized (mxfp4)

| Axis (AIGrid) | Measured accuracy |
|---|---|
| knowledge | 0.782 |
| protocol | 0.470 |
| math | 0.610 |
| fault | 0.410 |
| structured | 0.290 |

*Fitment from measured accuracy, decode speed, verbosity and VRAM - refreshes after the judged pass.*

---
*Per-sample transcripts (full question/answer/verdict JSONL) are archived on the portal state volume under `benchmark-results/`, one directory per suite run, named by model. Scores flow to the [leaderboard](../../docs/data/LEADERBOARD.md) automatically.*
