# nemotron-3-nano-30b - TelcoAIBench Marathon Report

**HF repo:** `nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16`  
**Serving:** vLLM v0.26.0 (KServe RawDeployment, 1x RTX PRO 6000 Blackwell 96GB)  
**Endpoint at test time:** `http://nemotron-3-nano-30b-predictor.gsma-otel2-test.svc.cluster.local:8080`  

## Results

| Suite | Accuracy | StdErr | Samples | Tier | Date |
|---|---|---|---|---|---|
| 3gpp | **0.270** | 0.0446 | 100 | lite | 2026-08-10 |
| 6g_bench | **0.573** | 0.0405 | 150 | lite | 2026-08-10 |
| oranbench | **0.667** | 0.0386 | 150 | lite | 2026-08-10 |
| srsranbench | **0.700** | 0.0375 | 150 | lite | 2026-08-10 |
| telelogs | **0.000** | 0.0 | 100 | lite | 2026-08-10 |
| telemath | **0.620** | 0.0488 | 100 | lite | 2026-08-10 |
| teleqna | **0.718** | 0.0142 | 1000 | lite | 2026-08-10 |
| teletables | **0.080** | 0.0273 | 100 | lite | 2026-08-10 |

## Generation behavior

| Suite | Samples | Mean latency (s) | Mean output tokens |
|---|---|---|---|
| 3gpp | 100 | 10.1 | 735 |
| 6g_bench | 150 | 68.6 | 4583 |
| oranbench | 150 | 47.8 | 3186 |
| srsranbench | 150 | 27.3 | 1825 |
| telelogs | 100 | 122.4 | 8192 |
| telemath | 100 | 52.1 | 3397 |
| teleqna | 1000 | 29.4 | 1901 |
| teletables | 100 | 112.4 | 7441 |

## Sample misses (first per suite, for audit)

- **3gpp** dataset index 0: expected `SA5`, parsed `CT1` - output: "We need to classify the text into one of the listed working groups. The text is about Non-Public Networks (NPN), SNPN, definitions, concepts. Likely related to SA (Service & System Aspects?) Or maybe RAN? Let's see the w..."
- **3gpp** dataset index 1: expected `RAN4`, parsed `RAN3` - output: "We need to classify the text into one of the listed working groups. The text is about band combination, interference analysis, insertion loss, MSD between certain bands, DC configuration, etc. This seems related to NR (N..."
- **3gpp** dataset index 3: expected `SA5`, parsed `SA3` - output: "We need to classify the text into one of the listed working groups. The text mentions "PM-MAMO-VNF WID", "VNF related VR PM use case", "reference point for clause 6.1.3 Requirements for Ve-Vnfm-em", "performance Threshol..."
- **6g_bench** dataset index 3: expected `C`, parsed `T` - output: "We need to parse the question. It's a multiple-choice question with scenario about UAV autonomous navigation at turn 6. There are network slices: mMTC, URLLC, eMBB. The question: "Given uncertainty across the next two tu..."
- **6g_bench** dataset index 4: expected `C`, parsed `B` - output: "We need to answer a multiple choice about which option should be selected given the scenario. The question provides details: The UAV is currently operating under mMTC slice with latency 25ms, jitter 8ms, loss 1.2%, throu..."
- **6g_bench** dataset index 5: expected `C`, parsed `` - output: "We need to parse the question. It's a multiple-choice question with four options A, B, C, D. The question: "Under worst case jitter and load, which scheduler reconfiguration should be selected to minimize maximum regret ..."
- **oranbench** dataset index 5: expected `A`, parsed `` - output: "We need to answer a multiple choice about O-RU transitions to the FREERUN state. The question: "When an O-RU transitions to the FREERUN state, what is the only possible state for both tx-array-carrier and rx-array-carrie..."
- **oranbench** dataset index 8: expected `B`, parsed `A` - output: "We need to answer a multiple choice about O-RAN R1 DME (Data Management Entity) primary purpose. Options:  A) To provide a standardized interface for rApps to publish data. B) To hide the identity of data consumers from ..."
- **oranbench** dataset index 12: expected `C`, parsed `` - output: "We need to parse the question: "Which of the following is NOT a required field for the 'GuRanUeId' object in the provided context?" They have options: A) 1. globalGnbId, B) 2. ranUeId, C) 3. plmnId, D) 4. gnbId.  We need..."
- **srsranbench** dataset index 1: expected `A`, parsed `` - output: "We need to answer a multiple choice about purpose of the `generate_ru_sdr_config` function. The question: "What is the purpose of the `generate_ru_sdr_config` function?" Options: A) To convert a RU SDR application unit c..."

## AI Grid tier fit (measured, auto-scored phase)

**Recommended placement: Tier 3 (Region)** - 30B params, 63GB bf16 moe(3B act), ~58.8s/answer, ~3907 tokens/answer.
Notes: verbose/slow decode - latency envelope only fits a tier up

| Axis (AIGrid) | Measured accuracy |
|---|---|
| knowledge | 0.695 |
| protocol | 0.422 |
| math | 0.620 |
| fault | 0.000 |
| structured | 0.080 |

*Fitment from measured accuracy, decode speed, verbosity and VRAM - refreshes after the judged pass.*

---
*Per-sample transcripts (full question/answer/verdict JSONL) are archived on the portal state volume under `benchmark-results/`, one directory per suite run, named by model. Scores flow to the [leaderboard](../../../docs/data/LEADERBOARD.md) automatically.*
