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

## Generation behavior

| Suite | Samples | Mean latency (s) | Mean output tokens |
|---|---|---|---|
| 3gpp | 100 | 0.9 | 10 |
| 6g_bench | 150 | 0.7 | 6 |
| oranbench | 150 | 0.4 | 6 |
| srsranbench | 150 | 0.6 | 6 |
| telelogs | 100 | 30.0 | 868 |
| telemath | 100 | 47.6 | 1447 |
| teleqna | 1000 | 0.3 | 6 |
| teletables | 100 | 0.3 | 6 |

## Sample misses (first per suite, for audit)

- **3gpp** dataset index 0: expected `SA5`, parsed `SA1` - output: "{"WORKING GROUP": "SA1"}"
- **3gpp** dataset index 2: expected `CT1`, parsed `SA2` - output: "{"WORKING GROUP": "SA2"}"
- **3gpp** dataset index 4: expected `RAN_AH1`, parsed `RAN1` - output: "{"WORKING GROUP": "RAN1"}"
- **6g_bench** dataset index 1: expected `A`, parsed `C` - output: "ANSWER: C"
- **6g_bench** dataset index 4: expected `C`, parsed `B` - output: "ANSWER: B"
- **6g_bench** dataset index 5: expected `C`, parsed `A` - output: "ANSWER: A"
- **oranbench** dataset index 1: expected `C`, parsed `A` - output: "ANSWER: A"
- **oranbench** dataset index 8: expected `B`, parsed `A` - output: "ANSWER: A"
- **oranbench** dataset index 12: expected `C`, parsed `D` - output: "ANSWER: D"
- **srsranbench** dataset index 1: expected `A`, parsed `C` - output: "ANSWER: C"

## AI Grid tier fit (measured, MCQ phase)

**Recommended placement: Tier 2 (Provider Edge)** - 24B params, 48GB bf16, ~Nones/answer, ~None tokens/answer.


| Axis (AIGrid) | Measured accuracy |
|---|---|
| knowledge | 0.765 |
| protocol | 0.638 |
| math | 0.470 |
| fault | 0.280 |
| structured | 0.280 |

*Fitment from measured accuracy, decode speed, verbosity and VRAM - refreshes after the judged pass.*

---
*Per-sample transcripts (full question/answer/verdict JSONL) are archived on the portal state volume under `benchmark-results/`, one directory per suite run, named by model. Scores flow to the [leaderboard](../../docs/data/LEADERBOARD.md) automatically.*
