# qwen3-6-27b - TelcoAIBench Marathon Report

**HF repo:** `Qwen/Qwen3.6-27B`  
**Serving:** vLLM v0.26.0 (KServe RawDeployment, 1x RTX PRO 6000 Blackwell 96GB)  
**Endpoint at test time:** `http://qwen3-6-27b-predictor.gsma-otel2-test.svc.cluster.local:8080`  

## Results

| Suite | Accuracy | StdErr | Samples | Tier | Date |
|---|---|---|---|---|---|
| teleqna | **0.814** | 0.0123 | 1000 | lite | 2026-08-11 |

## Generation behavior

| Suite | Samples | Mean latency (s) | Mean output tokens |
|---|---|---|---|
| teleqna | 1000 | 42.2 | 1119 |

## Sample misses (first per suite, for audit)

- **teleqna** dataset index 9: expected `B`, parsed `C` - output: "The user wants to identify the purpose of the "Control and User Plane Separation of EPC nodes" work item in 3GPP Release 14.  1.  **Analyze the question:** The question asks for the specific purpose of a 3GPP Release 14 ..."
- **teleqna** dataset index 11: expected `D`, parsed `A` - output: "The user wants to identify the inputs for the `Nmfaf_3caDataManagement_Fetch` service operation in 3GPP Release 18.  1.  **Identify the Service:** `Nmfaf_3caDataManagement` is the service provided by the MFAF (Multi-acce..."
- **teleqna** dataset index 14: expected `B`, parsed `D` - output: "The user wants to identify the additional functions supported by the eNB in the case of SIPTO@LN (Selected IP Traffic Offload at Local Network) with a collocated L-GW (Local Gateway) according to 3GPP Release 17.  1.  **..."

---
*Per-sample transcripts (full question/answer/verdict JSONL) are archived on the portal state volume under `benchmark-results/`, one directory per suite run, named by model. Scores flow to the [leaderboard](../../docs/data/LEADERBOARD.md) automatically.*
