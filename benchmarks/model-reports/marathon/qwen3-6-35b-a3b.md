# qwen3-6-35b-a3b - TelcoAIBench Marathon Report

**HF repo:** `Qwen/Qwen3.6-35B-A3B`  
**Serving:** vLLM v0.26.0 (KServe RawDeployment, 1x RTX PRO 6000 Blackwell 96GB)  
**Endpoint at test time:** `http://qwen3-6-35b-a3b-predictor.gsma-otel2-test.svc.cluster.local:8080`  

## Results

| Suite | Accuracy | StdErr | Samples | Tier | Date |
|---|---|---|---|---|---|
| 3gpp | **0.080** | 0.0273 | 100 | lite | 2026-08-11 |
| 6g_bench | **0.727** | 0.0365 | 150 | lite | 2026-08-11 |
| oranbench | **0.827** | 0.031 | 150 | lite | 2026-08-11 |
| srsranbench | **0.807** | 0.0324 | 150 | lite | 2026-08-11 |
| telelogs | **0.150** | 0.0359 | 100 | lite | 2026-08-11 |
| telemath | **0.510** | 0.0502 | 100 | lite | 2026-08-11 |
| teleqna | **0.812** | 0.0124 | 1000 | lite | 2026-08-11 |
| teletables | **0.330** | 0.0473 | 100 | lite | 2026-08-11 |

## Generation behavior

| Suite | Samples | Mean latency (s) | Mean output tokens |
|---|---|---|---|
| 3gpp | 100 | 28.1 | 2033 |
| 6g_bench | 150 | 30.4 | 2273 |
| oranbench | 150 | 17.7 | 1270 |
| srsranbench | 150 | 14.0 | 998 |
| telelogs | 100 | 222.6 | 15687 |
| telemath | 100 | 164.0 | 11472 |
| teleqna | 1000 | 13.5 | 932 |
| teletables | 100 | 46.8 | 3337 |

## Sample misses (first per suite, for audit)

- **3gpp** dataset index 0: expected `SA5`, parsed `CT1` - output: "Here's a thinking process:  1.  **Analyze User Input:**    - **Role:** Distinguished expert in telecommunications, skilled in classifying 3GPP technical documents.    - **Task:** Classify the provided text into one of th..."
- **3gpp** dataset index 1: expected `RAN4`, parsed `CT1` - output: "Here's a thinking process:  1.  **Analyze User Input:**    - **Role:** Distinguished expert in telecommunications, skilled in classifying 3GPP technical documents.    - **Task:** Classify the provided text into one of th..."
- **3gpp** dataset index 3: expected `SA5`, parsed `CT1` - output: "Here's a thinking process:  1.  **Analyze User Input:**    - **Role:** Distinguished expert in telecommunications, skilled in 3GPP technical documents.    - **Task:** Classify the provided text into one of the specified ..."
- **6g_bench** dataset index 4: expected `C`, parsed `B` - output: "Here's a thinking process:  1.  **Analyze User Input:**    - **Current State:** UAV on mMTC slice.      - Latency: 25ms      - Jitter: 8ms      - Loss: 1.2%      - Throughput: 1.5 Mbps      - Edge load: 0.75    - **Missi..."
- **6g_bench** dataset index 5: expected `C`, parsed `A` - output: "The question asks to select the best scheduler reconfiguration option to minimize maximum regret over the next three turns, given specific conditions and constraints. Let's analyze the given information: - Current state ..."
- **6g_bench** dataset index 9: expected `B`, parsed `A` - output: "Here's a thinking process:  1.  **Analyze User Input:**    - **Current State:** UAV on eMBB slice.      - Latency: 35ms      - Jitter: 12ms      - Loss: 0.8%      - Throughput: 95Mbps      - Edge load: 0.85      - Payloa..."
- **oranbench** dataset index 5: expected `A`, parsed `B` - output: "The question asks about the state of `tx-array-carrier` and `rx-array-carrier` when an O-RU (Open Radio Unit) transitions to the `FREERUN` state. This relates to the O-RAN specifications, specifically the O-RU Management..."
- **oranbench** dataset index 8: expected `B`, parsed `A` - output: "The user wants to identify the primary purpose of the R1 DME (Data Management Entity) in O-RAN from the given options.  1.  **Analyze the question:** "What is the primary purpose of the R1 DME (Data Management Entity) in..."
- **oranbench** dataset index 12: expected `C`, parsed `D` - output: "The user wants to identify which of the given options is NOT a required field for the "GuRanUeId" object in a specific context. The context seems to be related to 5G/NR (New Radio) or 3GPP specifications, specifically re..."
- **srsranbench** dataset index 0: expected `A`, parsed `C` - output: "The user wants to identify the purpose of the `lower_phy_controller` class from a multiple-choice question. The options are: A) 1. It provides a start and stop methods for the lower physical layer. B) 2. It manages the s..."

## AI Grid tier fit (measured, auto-scored phase)

**Recommended placement: Tier 3 (Region)** - 35B params, 72GB bf16 moe(3B act), ~67.1s/answer, ~4750 tokens/answer.
Notes: verbose/slow decode - latency envelope only fits a tier up

| Axis (AIGrid) | Measured accuracy |
|---|---|
| knowledge | 0.815 |
| protocol | 0.403 |
| math | 0.510 |
| fault | 0.150 |
| structured | 0.330 |

*Fitment from measured accuracy, decode speed, verbosity and VRAM - refreshes after the judged pass.*

---
*Per-sample transcripts (full question/answer/verdict JSONL) are archived on the portal state volume under `benchmark-results/`, one directory per suite run, named by model. Scores flow to the [leaderboard](../../docs/data/LEADERBOARD.md) automatically.*
