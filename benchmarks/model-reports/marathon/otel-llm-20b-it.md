# otel-llm-20b-it - TelcoAIBench Marathon Report

**HF repo:** `farbodtavakkoli/OTel-LLM-20B-IT`  
**Serving:** vLLM v0.26.0 (KServe RawDeployment, 1x RTX PRO 6000 Blackwell 96GB) | args: `--dtype=bfloat16 --max-model-len=32768`  
**Endpoint at test time:** `http://otel-llm-20b-it-predictor.gsma-otel2-test.svc.cluster.local:8080`  

## Results

| Suite | Accuracy | StdErr | Samples | Tier | Date |
|---|---|---|---|---|---|
| 3gpp | **0.270** | 0.0446 | 100 | lite | 2026-08-11 |
| 6g_bench | **0.680** | 0.0382 | 150 | lite | 2026-08-11 |
| oranbench | **0.747** | 0.0356 | 150 | lite | 2026-08-11 |
| srsranbench | **0.713** | 0.037 | 150 | lite | 2026-08-11 |
| telelogs | **0.270** | 0.0446 | 100 | lite | 2026-08-11 |
| telemath | **0.030** | 0.0171 | 100 | lite | 2026-08-11 |
| teleqna | **0.712** | 0.0143 | 1000 | lite | 2026-08-11 |
| teletables | **0.270** | 0.0446 | 100 | lite | 2026-08-11 |

## Generation behavior

| Suite | Samples | Mean latency (s) | Mean output tokens |
|---|---|---|---|
| 3gpp | 100 | 2.3 | 234 |
| 6g_bench | 150 | 2.3 | 205 |
| oranbench | 150 | 6.1 | 474 |
| srsranbench | 150 | 0.2 | 14 |
| telelogs | 100 | 79.3 | 4758 |
| telemath | 100 | 57.7 | 3489 |
| teleqna | 1000 | 1.7 | 103 |
| teletables | 100 | 36.1 | 2382 |

## Sample misses (first per suite, for audit)

- **3gpp** dataset index 0: expected `SA5`, parsed `SA1` - output: "{"WORKING GROUP": "SA1"}"
- **3gpp** dataset index 1: expected `RAN4`, parsed `RAN1` - output: "{"WORKING GROUP": "RAN1"}"
- **3gpp** dataset index 2: expected `CT1`, parsed `RAN4` - output: "{"WORKING GROUP": "RAN4"}"
- **6g_bench** dataset index 3: expected `C`, parsed `B` - output: "ANSWER: B"
- **6g_bench** dataset index 5: expected `C`, parsed `A` - output: "ANSWER: A"
- **6g_bench** dataset index 9: expected `B`, parsed `` - output: ""
- **oranbench** dataset index 1: expected `C`, parsed `A` - output: "ANSWER: A"
- **oranbench** dataset index 5: expected `A`, parsed `B` - output: "ANSWER: B"
- **oranbench** dataset index 8: expected `B`, parsed `C` - output: "ANSWER: C"
- **srsranbench** dataset index 0: expected `A`, parsed `C` - output: "ANSWER: C"

## AI Grid tier fit (measured, MCQ phase)

**Recommended placement: Tier 2 (Provider Edge)** - 20B params, 42GB bf16 (fp32 ckpt), ~23.2s/answer, ~1457 tokens/answer.


| Axis (AIGrid) | Measured accuracy |
|---|---|
| knowledge | 0.724 |
| protocol | 0.475 |
| math | 0.030 |
| fault | 0.270 |
| structured | 0.270 |

*Fitment from measured accuracy, decode speed, verbosity and VRAM - refreshes after the judged pass.*

---
*Per-sample transcripts (full question/answer/verdict JSONL) are archived on the portal state volume under `benchmark-results/`, one directory per suite run, named by model. Scores flow to the [leaderboard](../../docs/data/LEADERBOARD.md) automatically.*
