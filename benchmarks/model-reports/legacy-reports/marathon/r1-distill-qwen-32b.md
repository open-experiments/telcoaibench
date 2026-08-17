# r1-distill-qwen-32b - TelcoAIBench Marathon Report

**HF repo:** `deepseek-ai/DeepSeek-R1-Distill-Qwen-32B`  
**Serving:** vLLM v0.26.0 (KServe RawDeployment, 1x RTX PRO 6000 Blackwell 96GB)  
**Endpoint at test time:** `http://r1-distill-qwen-32b-predictor.gsma-otel2-test.svc.cluster.local:8080`  

## Results

| Suite | Accuracy | StdErr | Samples | Tier | Date |
|---|---|---|---|---|---|
| 3gpp | **0.250** | 0.0435 | 100 | lite | 2026-08-12 |
| 6g_bench | **0.600** | 0.0401 | 150 | lite | 2026-08-12 |
| oranbench | **0.727** | 0.0365 | 150 | lite | 2026-08-12 |
| srsranbench | **0.800** | 0.0328 | 150 | lite | 2026-08-12 |
| telelogs | **0.320** | 0.0469 | 100 | lite | 2026-08-12 |
| telemath | **0.470** | 0.0502 | 100 | lite | 2026-08-12 |
| teleqna | **0.739** | 0.0139 | 1000 | lite | 2026-08-12 |
| teletables | **0.300** | 0.0461 | 100 | lite | 2026-08-12 |

## Generation behavior

| Suite | Samples | Mean latency (s) | Mean output tokens |
|---|---|---|---|
| 3gpp | 100 | 16.7 | 368 |
| 6g_bench | 150 | 251.3 | 5064 |
| oranbench | 150 | 88.8 | 1873 |
| srsranbench | 150 | 51.0 | 1144 |
| telelogs | 100 | 94.8 | 1936 |
| telemath | 100 | 304.5 | 6057 |
| teleqna | 1000 | 87.3 | 1809 |
| teletables | 100 | 318.5 | 6262 |

## Sample misses (first per suite, for audit)

- **3gpp** dataset index 0: expected `SA5`, parsed `SA1` - output: "Okay, so I need to classify this text into one of the 3GPP working groups. The text is about Non-Public Networks (NPN) and Stand-alone Non-Public Networks (SNPN) in the context of 5G systems. It mentions things like netw..."
- **3gpp** dataset index 1: expected `RAN4`, parsed `n78` - output: "Okay, so I need to classify this text into one of the 3GPP working groups. Let me start by understanding what the text is about. The text mentions "band combination, interference analysis, insertion loss and MSD between ..."
- **3gpp** dataset index 3: expected `SA5`, parsed `CT1` - output: "Okay, so I need to classify this text into one of the 3GPP working groups. Let me start by understanding the content of the text.   The text mentions things like "NS PM flow between NFVO and NM," "PM-MAMO-VNF WID," "VNF ..."
- **6g_bench** dataset index 3: expected `C`, parsed `` - output: "Okay, so I've got this multiple-choice question about UAV navigation and network slicing. Hmm, let me try to break it down. I'm a bit rusty on this, but I'll think it through.  The question is about a UAV that's just ena..."
- **6g_bench** dataset index 4: expected `C`, parsed `B` - output: "Okay, so I've got this question about UAVs and network slices. Hmm, I'm a bit rusty on this, but let me try to think it through.  The question is about choosing the right network slice for a UAV mission. The UAV is curre..."
- **6g_bench** dataset index 5: expected `C`, parsed `` - output: "Okay, so I've got this multiple-choice question about network scheduling for a UAV, and I'm a bit new to this, but I'll try to think it through. Let me read the question again and break it down.  The scenario is at turn ..."
- **oranbench** dataset index 1: expected `C`, parsed `A` - output: "Okay, so I've got this question about O-RAN architecture and the interfaces between different units. Hmm, I'm a bit rusty on this, but let me think it through.  The question is asking what interface connects the O-RU's D..."
- **oranbench** dataset index 8: expected `B`, parsed `A` - output: "Okay, so I've got this multiple-choice question about the O-RAN architecture, specifically about the R1 DME. Hmm, I'm a bit rusty on this, but let me think it through.  I remember that O-RAN stands for Open Radio Access ..."
- **oranbench** dataset index 12: expected `C`, parsed `` - output: "Okay, so I've got this question about the "GuRanUeId" object and which field isn't required. Hmm, I'm a bit rusty on this, but let me think it through.  Wait, I remember that in 5G, the GuRanUeId is used for identifying ..."
- **srsranbench** dataset index 0: expected `A`, parsed `C` - output: "Okay, so I've got this multiple-choice question about the lower_phy_controller class. Hmm, I'm a bit rusty on this, but let me think it through.  The question is asking about the purpose of the lower_phy_controller. The ..."

## AI Grid tier fit (measured, auto-scored phase)

**Recommended placement: Tier 3 (Region)** - 32B params, 66GB bf16, ~151.6s/answer, ~3064 tokens/answer.
Notes: verbose/slow decode - latency envelope only fits a tier up

| Axis (AIGrid) | Measured accuracy |
|---|---|
| knowledge | 0.755 |
| protocol | 0.425 |
| math | 0.470 |
| fault | 0.320 |
| structured | 0.300 |

*Fitment from measured accuracy, decode speed, verbosity and VRAM - refreshes after the judged pass.*

---
*Per-sample transcripts (full question/answer/verdict JSONL) are archived on the portal state volume under `benchmark-results/`, one directory per suite run, named by model. Scores flow to the [leaderboard](../../../docs/data/LEADERBOARD.md) automatically.*
