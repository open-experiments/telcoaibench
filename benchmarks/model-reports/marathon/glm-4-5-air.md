# glm-4-5-air - TelcoAIBench Marathon Report

**HF repo:** `cpatonn/GLM-4.5-Air-AWQ-4bit`  
**Serving:** vLLM v0.26.0 (KServe RawDeployment, 1x RTX PRO 6000 Blackwell 96GB) | args: `--max-model-len=32768`  
**Endpoint at test time:** `http://glm-4-5-air-predictor.gsma-otel2-test.svc.cluster.local:8080`  

## Results

| Suite | Accuracy | StdErr | Samples | Tier | Date |
|---|---|---|---|---|---|
| 3gpp | **0.150** | 0.0359 | 100 | lite | 2026-08-11 |
| 6g_bench | **0.640** | 0.0393 | 150 | lite | 2026-08-11 |
| oranbench | **0.720** | 0.0368 | 150 | lite | 2026-08-11 |
| srsranbench | **0.747** | 0.0356 | 150 | lite | 2026-08-11 |
| telelogs | **0.410** | 0.0494 | 100 | lite | 2026-08-11 |
| telemath | **0.300** | 0.0461 | 100 | lite | 2026-08-11 |
| teleqna | **0.769** | 0.0133 | 1000 | lite | 2026-08-10 |
| teletables | **0.270** | 0.0446 | 100 | lite | 2026-08-10 |

## Generation behavior

| Suite | Samples | Mean latency (s) | Mean output tokens |
|---|---|---|---|
| 3gpp | 100 | 10.5 | 500 |
| 6g_bench | 150 | 93.5 | 4085 |
| oranbench | 150 | 29.8 | 1403 |
| srsranbench | 150 | 23.5 | 1115 |
| telelogs | 100 | 136.0 | 5531 |
| telemath | 100 | 162.6 | 6589 |
| teleqna | 380 | 28.4 | 1327 |
| teletables | 100 | 103.1 | 4435 |

## Sample misses (first per suite, for audit)

- **3gpp** dataset index 0: expected `SA5`, parsed `CT1` - output: "<think>Alright, let's tackle this problem step by step. The user wants me to classify a given text excerpt into one of the specified 3GPP working groups. The options are: CT1, CT3, CT4, CT6, RAN1, RAN2, RAN3, RAN4, RAN5,..."
- **3gpp** dataset index 1: expected `RAN4`, parsed `CT1` - output: "<think>Alright, let's tackle this problem. I need to classify the given text into one of the 3GPP working groups. The options are: CT1, CT3, CT4, CT6, RAN1, RAN2, RAN3, RAN4, RAN5, RAN_AH1, SA1, SA2, SA3, SA4, SA5, SA6. ..."
- **3gpp** dataset index 3: expected `SA5`, parsed `CT1` - output: "<think>Alright, let's tackle this problem step by step. The user wants me to classify a given text into one of the 3GPP working groups based on the provided list. The list includes groups like CT1, CT3, RAN1, SA1, etc.  ..."
- **6g_bench** dataset index 4: expected `C`, parsed `B` - output: "<think>First, I need to understand the current situation. The UAV is on an mMTC slice with:  - Latency: 25ms  - Jitter: 8ms  - Loss: 1.2%  - Throughput: 1.5Mbps  - Edge load: 0.75  The mission requires real-time sensor f..."
- **6g_bench** dataset index 7: expected `B`, parsed `` - output: "<think>First, I need to understand the scenario. The UAV is returning under a URLLC slice with specific parameters: 7ms latency, 0.8ms jitter, 0.01% loss, 125Mbps throughput, and 0.41 edge load. A third-party request com..."
- **6g_bench** dataset index 9: expected `B`, parsed `A` - output: "<think>First, I need to understand the question. It's about a UAV agent that's currently on an eMBB slice with certain metrics: latency 35ms, jitter 12ms, loss 0.8%, throughput 95Mbps, and edge load 0.85. It's carrying t..."
- **oranbench** dataset index 1: expected `C`, parsed `A` - output: "<think>First, the question is: "What interface connects the O-RU's Digital Processing Unit to the O-DU's NPU in an integrated O-RAN architecture?" The options are:  A) Ethernet  B) USB  C) PCIe  D) SATA  I need to recall..."
- **oranbench** dataset index 8: expected `B`, parsed `D` - output: "<think>First, I need to understand what the R1 DME is in O-RAN. O-RAN stands for Open Radio Access Network, and it's an initiative to make RAN components more open and interoperable. The R1 interface is part of the O-RAN..."
- **oranbench** dataset index 12: expected `C`, parsed `A` - output: "<think>First, the question is: "Which of the following is NOT a required field for the 'GuRanUeId' object in the provided context?" But there's no provided context given in the query. That might be a problem. Let me read..."
- **srsranbench** dataset index 0: expected `A`, parsed `C` - output: "<think>First, the question is: "What is the purpose of the lower_phy_controller class?" And there are four options:  A) 1. It provides a start and stop methods for the lower physical layer.  B) 2. It manages the synchron..."

---
*Per-sample transcripts (full question/answer/verdict JSONL) are archived on the portal state volume under `benchmark-results/`, one directory per suite run, named by model. Scores flow to the [leaderboard](../../docs/data/LEADERBOARD.md) automatically.*
