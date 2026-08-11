# qwen3-6-27b - TelcoAIBench Marathon Report

**HF repo:** `Qwen/Qwen3.6-27B`  
**Serving:** vLLM v0.26.0 (KServe RawDeployment, 1x RTX PRO 6000 Blackwell 96GB)  
**Endpoint at test time:** `http://qwen3-6-27b-predictor.gsma-otel2-test.svc.cluster.local:8080`  

## Results

| Suite | Accuracy | StdErr | Samples | Tier | Date |
|---|---|---|---|---|---|
| oranbench | **0.800** | 0.0328 | 150 | lite | 2026-08-11 |
| srsranbench | **0.827** | 0.031 | 150 | lite | 2026-08-11 |
| telemath | **0.270** | 0.0446 | 100 | lite | 2026-08-11 |
| teleqna | **0.814** | 0.0123 | 1000 | lite | 2026-08-11 |
| teletables | **0.320** | 0.0469 | 100 | lite | 2026-08-11 |

## Generation behavior

| Suite | Samples | Mean latency (s) | Mean output tokens |
|---|---|---|---|
| oranbench | 150 | 50.1 | 1330 |
| srsranbench | 150 | 46.6 | 1236 |
| telemath | 3 | 264.7 | 6880 |
| teleqna | 1000 | 42.2 | 1119 |
| teletables | 100 | 122.3 | 3228 |

## Sample misses (first per suite, for audit)

- **oranbench** dataset index 11: expected `D`, parsed `C` - output: "The user wants to identify the correct behavior of an E2 Node when it receives a RIC Service CONTROL request with a valid Call Process ID after the associated Time to Wait timer has expired.  1.  **Analyze the context**:..."
- **oranbench** dataset index 19: expected `D`, parsed `C` - output: "The user wants to identify the protocol used for external user to group mapping in NETCONF endpoints based on "provided requirements". Since no specific document or context is provided in the prompt, I need to infer the ..."
- **oranbench** dataset index 22: expected `C`, parsed `B` - output: "The user wants to identify the primary goal of the O-RAN ALLIANCE Test and Integration Focus Group (TIFG) from the given options.  1.  **Analyze the question:** The question asks for the primary goal of the O-RAN ALLIANC..."
- **srsranbench** dataset index 0: expected `A`, parsed `B` - output: "The user wants to identify the purpose of the `lower_phy_controller` class from a multiple-choice question.  1.  **Analyze the question:** "What is the purpose of the lower_phy_controller class?" 2.  **Context:** This lo..."
- **srsranbench** dataset index 6: expected `C`, parsed `B` - output: "The user wants to identify the purpose of the `deallocate` function in the `polar_deallocator_impl` class.  1.  **Analyze the question:** The question asks about a specific function `deallocate` in a specific class `pola..."
- **srsranbench** dataset index 14: expected `A`, parsed `C` - output: "The user wants to identify what the `channel_precoder_avx512` class implements based on the provided options.  1.  **Analyze the class name:** `channel_precoder_avx512`     *   `channel_precoder`: Indicates it's related ..."
- **telemath** dataset index 5: expected `28.803717234923226`, parsed `{28.8}` - output: "Here's a thinking process to solve the problem:  1.  **Understand the Goal:** The objective is to calculate the required receive antenna gain ($G_r$) in decibels (dB) at the cell boundary.  2.  **Identify the Given Infor..."
- **telemath** dataset index 6: expected `0.5`, parsed `{0.5}` - output: "Here's a thinking process to solve the problem:  1.  **Understand the Goal:** The objective is to find the steady-state probability that the robot is "out of order" (broken/under repair).  2.  **Analyze the System:**    ..."
- **teleqna** dataset index 9: expected `B`, parsed `C` - output: "The user wants to identify the purpose of the "Control and User Plane Separation of EPC nodes" work item in 3GPP Release 14.  1.  **Analyze the question:** The question asks for the specific purpose of a 3GPP Release 14 ..."
- **teleqna** dataset index 11: expected `D`, parsed `A` - output: "The user wants to identify the inputs for the `Nmfaf_3caDataManagement_Fetch` service operation in 3GPP Release 18.  1.  **Identify the Service:** `Nmfaf_3caDataManagement` is the service provided by the MFAF (Multi-acce..."

---
*Per-sample transcripts (full question/answer/verdict JSONL) are archived on the portal state volume under `benchmark-results/`, one directory per suite run, named by model. Scores flow to the [leaderboard](../../docs/data/LEADERBOARD.md) automatically.*
