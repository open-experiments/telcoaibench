# qwen3-6-27b - TelcoAIBench Marathon Report

**HF repo:** `Qwen/Qwen3.6-27B`  
**Serving:** vLLM v0.26.0 (KServe RawDeployment, 1x RTX PRO 6000 Blackwell 96GB)  
**Endpoint at test time:** `http://qwen3-6-27b-predictor.gsma-otel2-test.svc.cluster.local:8080`  

## Results

| Suite | Accuracy | StdErr | Samples | Tier | Date |
|---|---|---|---|---|---|
| 3gpp | **0.080** | 0.0273 | 100 | lite | 2026-08-11 |
| 6g_bench | **0.693** | 0.0378 | 150 | lite | 2026-08-11 |
| oranbench | **0.800** | 0.0328 | 150 | lite | 2026-08-11 |
| srsranbench | **0.827** | 0.031 | 150 | lite | 2026-08-11 |
| telelogs | **0.050** | 0.0219 | 100 | lite | 2026-08-11 |
| telemath | **0.270** | 0.0446 | 100 | lite | 2026-08-11 |
| teleqna | **0.814** | 0.0123 | 1000 | lite | 2026-08-11 |
| teletables | **0.320** | 0.0469 | 100 | lite | 2026-08-11 |

## Generation behavior

| Suite | Samples | Mean latency (s) | Mean output tokens |
|---|---|---|---|
| 3gpp | 100 | 54.5 | 1431 |
| 6g_bench | 150 | 108.4 | 2832 |
| oranbench | 150 | 50.1 | 1330 |
| srsranbench | 150 | 46.6 | 1236 |
| telelogs | 100 | 662.5 | 16287 |
| telemath | 100 | 456.4 | 11537 |
| teleqna | 1000 | 42.2 | 1119 |
| teletables | 100 | 122.3 | 3228 |

## Sample misses (first per suite, for audit)

- **3gpp** dataset index 0: expected `SA5`, parsed `CT1` - output: "Here's a thinking process:  1.  **Analyze User Input:**    - **Role:** Distinguished expert in telecommunication domain, skilled in understanding and classifying 3GPP technical documents.    - **Task:** Classify the prov..."
- **3gpp** dataset index 1: expected `RAN4`, parsed `CT1` - output: "Here's a thinking process:  1.  **Analyze User Input:**    - **Role:** Distinguished expert in telecommunication domain, skilled in understanding and classifying 3GPP technical documents.    - **Task:** Classify the prov..."
- **3gpp** dataset index 3: expected `SA5`, parsed `CT1` - output: "Here's a thinking process:  1.  **Analyze User Input:**    - **Role:** Distinguished expert in telecommunication domain, skilled in understanding and classifying 3GPP technical documents.    - **Task:** Classify the prov..."
- **6g_bench** dataset index 3: expected `C`, parsed `B` - output: "The user wants me to answer a multiple-choice question based on a provided scenario.  **Scenario Analysis:** - **Turn:** 6 - **UAV State:** Autonomous navigation enabled, speed 18.0 mps, altitude 20.0 m. - **Environment:..."
- **6g_bench** dataset index 4: expected `C`, parsed `B` - output: "The user wants me to answer a multiple-choice question based on a specific scenario involving a UAV and network slices.  **Scenario Analysis:** 1.  **Current State:**     *   Slice: mMTC     *   Latency: 25ms     *   Jit..."
- **6g_bench** dataset index 5: expected `C`, parsed `A` - output: "The user wants me to answer a multiple-choice question based on a specific scenario involving an AI scheduler, network slices (mMTC, URLLC, eMBB), UAV flight parameters, and regret minimization.  **Scenario Breakdown:** ..."
- **oranbench** dataset index 11: expected `D`, parsed `C` - output: "The user wants to identify the correct behavior of an E2 Node when it receives a RIC Service CONTROL request with a valid Call Process ID after the associated Time to Wait timer has expired.  1.  **Analyze the context**:..."
- **oranbench** dataset index 19: expected `D`, parsed `C` - output: "The user wants to identify the protocol used for external user to group mapping in NETCONF endpoints based on "provided requirements". Since no specific document or context is provided in the prompt, I need to infer the ..."
- **oranbench** dataset index 22: expected `C`, parsed `B` - output: "The user wants to identify the primary goal of the O-RAN ALLIANCE Test and Integration Focus Group (TIFG) from the given options.  1.  **Analyze the question:** The question asks for the primary goal of the O-RAN ALLIANC..."
- **srsranbench** dataset index 0: expected `A`, parsed `B` - output: "The user wants to identify the purpose of the `lower_phy_controller` class from a multiple-choice question.  1.  **Analyze the question:** "What is the purpose of the lower_phy_controller class?" 2.  **Context:** This lo..."

---
*Per-sample transcripts (full question/answer/verdict JSONL) are archived on the portal state volume under `benchmark-results/`, one directory per suite run, named by model. Scores flow to the [leaderboard](../../docs/data/LEADERBOARD.md) automatically.*
