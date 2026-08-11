# telecomgpt-r1 - TelcoAIBench Marathon Report

**HF repo:** `KU-DFI/TelecomGPT-R1`  
**Serving:** vLLM v0.26.0 (KServe RawDeployment, 1x RTX PRO 6000 Blackwell 96GB)  
**Endpoint at test time:** `http://telecomgpt-r1-predictor.gsma-otel2-test.svc.cluster.local:8080`  

## Results

| Suite | Accuracy | StdErr | Samples | Tier | Date |
|---|---|---|---|---|---|
| 3gpp | **0.520** | 0.0502 | 100 | lite | 2026-08-11 |
| 6g_bench | **0.720** | 0.0368 | 150 | lite | 2026-08-11 |
| oranbench | **0.940** | 0.0195 | 150 | lite | 2026-08-11 |
| srsranbench | **0.953** | 0.0173 | 150 | lite | 2026-08-11 |
| telelogs | **0.990** | 0.01 | 100 | lite | 2026-08-11 |
| telemath | **0.620** | 0.0488 | 100 | lite | 2026-08-11 |
| teleqna | **0.902** | 0.0094 | 1000 | lite | 2026-08-11 |
| teletables | **0.360** | 0.0482 | 100 | lite | 2026-08-11 |

## Generation behavior

| Suite | Samples | Mean latency (s) | Mean output tokens |
|---|---|---|---|
| 3gpp | 100 | 8.2 | 196 |
| 6g_bench | 150 | 24.1 | 629 |
| oranbench | 150 | 19.2 | 510 |
| srsranbench | 150 | 21.0 | 559 |
| telelogs | 100 | 23.0 | 514 |
| telemath | 100 | 52.6 | 1391 |
| teleqna | 1000 | 16.5 | 425 |
| teletables | 100 | 28.4 | 766 |

## Sample misses (first per suite, for audit)

- **3gpp** dataset index 1: expected `RAN4`, parsed `n78` - output: "The text discusses a specific band combination (3A-5A-7A-7A and n78A-n257A), interference analysis, insertion loss, and MSD (Maximum Sensitivity Degradation). It references TR 37.863 and TR 37.864, which are technical re..."
- **3gpp** dataset index 4: expected `RAN_AH1`, parsed `AH1` - output: "The text describes the physical layer transmission chain for user plane data, including transport channel multiplexing, CRC, channel coding (convolutional, turbo), interleaving, and rate matching. This is a high-level ov..."
- **3gpp** dataset index 5: expected `SA1`, parsed `SA6` - output: "The text discusses interworking requirements between MCPTT (Mission Critical Push-To-Talk) service and TETRA systems. It specifies functional requirements like group calls, emergency calls, encryption, overrides, regroup..."
- **6g_bench** dataset index 3: expected `C`, parsed `B` - output: "The UAV is in autonomous navigation under icing conditions with wind, requiring reliable control links. The current mMTC slice has high latency (50 ms) and edge load (0.75), which risks command responsiveness degradation..."
- **6g_bench** dataset index 5: expected `C`, parsed `A` - output: "The current network slice is mMTC with latency 22.0 ms, jitter 7.5 ms, loss 0.6%, throughput 1.0 Mbps, and edge load 0.88. The UAV is at 100% battery, flying at 22.0 mps, altitude 30-150 m, wind 8.5 mps. Earlier turns us..."
- **6g_bench** dataset index 9: expected `B`, parsed `A` - output: "The mission requires continuous thermal imaging at 300m range with 640x512 resolution, which demands sufficient throughput and low latency to maintain real-time operation. The current eMBB slice provides 95Mbps throughpu..."
- **oranbench** dataset index 11: expected `D`, parsed `A` - output: "When a RIC Service CONTROL request is received with a valid Call Process ID after the associated Time to Wait timer has expired, the E2 Node is expected to handle the situation based on the protocol specifications. The T..."
- **oranbench** dataset index 28: expected `B`, parsed `D` - output: "In O-RAN, when physical layer time stamping is used for Precision Time Protocol (PTP), the timing accuracy is determined at the hardware level (PHY) rather than relying on software processing delays within the network st..."
- **oranbench** dataset index 40: expected `C`, parsed `D` - output: "The question asks about a specific handover scenario where the E2 node must invoke several procedures: Handover Preparation for UE Mobility Management, Bearer Context Modification, UE Context Modification, and RRC Messag..."
- **srsranbench** dataset index 5: expected `D`, parsed `A` - output: "The user is asking for the functionality of a specific function `amplitude_controller_scaling_impl::process`.  1.  **Analyze the function name:** `amplitude_controller_scaling_impl::process`.     *   `amplitude_controlle..."

---
*Per-sample transcripts (full question/answer/verdict JSONL) are archived on the portal state volume under `benchmark-results/`, one directory per suite run, named by model. Scores flow to the [leaderboard](../../docs/data/LEADERBOARD.md) automatically.*
