# qwq-32b - TelcoAIBench Marathon Report

**HF repo:** `Qwen/QwQ-32B`  
**Serving:** vLLM v0.26.0 (KServe RawDeployment, 1x RTX PRO 6000 Blackwell 96GB) | args: `--max-model-len=32768`  
**Endpoint at test time:** `http://qwq-32b-predictor.gsma-otel2-test.svc.cluster.local:8080`  

## Results

| Suite | Accuracy | StdErr | Samples | Tier | Date |
|---|---|---|---|---|---|
| 3gpp | **0.160** | 0.0368 | 100 | lite | 2026-08-12 |
| 6g_bench | **0.660** | 0.0388 | 150 | lite | 2026-08-12 |
| oranbench | **0.773** | 0.0343 | 150 | lite | 2026-08-12 |
| srsranbench | **0.820** | 0.0315 | 150 | lite | 2026-08-12 |
| telelogs | **0.540** | 0.0501 | 100 | lite | 2026-08-12 |
| telemath | **0.630** | 0.0485 | 100 | lite | 2026-08-12 |
| teleqna | **0.760** | 0.0135 | 1000 | lite | 2026-08-11 |
| teletables | **0.270** | 0.0446 | 100 | lite | 2026-08-11 |

## Generation behavior

| Suite | Samples | Mean latency (s) | Mean output tokens |
|---|---|---|---|
| 3gpp | 100 | 26.9 | 599 |
| 6g_bench | 150 | 195.3 | 4072 |
| oranbench | 150 | 59.9 | 1318 |
| srsranbench | 150 | 48.1 | 1087 |
| telelogs | 100 | 310.9 | 6220 |
| telemath | 100 | 438.0 | 8702 |
| teleqna | 1000 | 88.0 | 1836 |
| teletables | 100 | 272.8 | 5483 |

## Sample misses (first per suite, for audit)

- **3gpp** dataset index 0: expected `SA5`, parsed `RAN1` - output: "Okay, let's tackle this classification. The user provided a text from a 3GPP document and wants to know which working group it belongs to. The options are a list of CT, RAN, and SA groups.  First, I need to recall what e..."
- **3gpp** dataset index 1: expected `RAN4`, parsed `RAN1` - output: "Okay, let's tackle this classification. The user provided a text snippet from a 3GPP document and wants to know which working group it belongs to. The options are a list of CT, RAN, and SA groups with sub-numbers.  First..."
- **3gpp** dataset index 2: expected `CT1`, parsed `RAN1` - output: "Okay, let's tackle this classification problem. The user wants me to figure out which 3GPP working group the given text belongs to. The options are from the list provided, like RAN1, SA1, etc.  First, I need to understan..."
- **6g_bench** dataset index 3: expected `C`, parsed `B` - output: "Okay, let's tackle this question. Hmm, the scenario is about choosing the best network slice for a UAV in autonomous navigation. The mission needs to continue for at least two more turns unless the risks are too high. Th..."
- **6g_bench** dataset index 4: expected `C`, parsed `B` - output: "Okay, let's tackle this question. Hmm, the UAV is on an mMTC slice right now. The mission needs real-time sensor focus adjustment with max latency of 15ms and at least 5Mbps throughput. The current slice has 25ms latency..."
- **6g_bench** dataset index 7: expected `B`, parsed `` - output: "Okay, let's see. I need to figure out which option is the best here. The question is about a UAV returning under a URLLC slice with certain parameters. The main thing here is the edge load and whether accepting a third-p..."
- **oranbench** dataset index 1: expected `C`, parsed `A` - output: "Okay, so I have this question here about the O-RAN architecture and which interface connects the O-RU's Digital Processing Unit to the O-DU's NPU. Hmm, I remember that O-RAN stands for Open Radio Access Network, right? T..."
- **oranbench** dataset index 8: expected `B`, parsed `A` - output: "Okay, so I have this question about the primary purpose of the R1 DME in O-RAN. Hmm, I need to remember what O-RAN's architecture is like. Let me think. The O-RAN Alliance is pushing for more open and intelligent radio a..."
- **oranbench** dataset index 12: expected `C`, parsed `D` - output: "Okay, so I have this question here about the required fields for the "GuRanUeId" object. The question is asking which one of the options is NOT a required field. Let me think through this step by step.  First, I need to ..."
- **srsranbench** dataset index 1: expected `A`, parsed `C` - output: "Okay, so I have this question here about the purpose of the generate_ru_sdr_config function. The options are A to D. Let me think through this step by step.  First, I need to recall what each of these functions might do...."

## AI Grid tier fit (measured, auto-scored phase)

**Recommended placement: Tier 3 (Region)** - 32B params, 66GB bf16, ~180.0s/answer, ~3664 tokens/answer.
Notes: verbose/slow decode - latency envelope only fits a tier up

| Axis (AIGrid) | Measured accuracy |
|---|---|
| knowledge | 0.784 |
| protocol | 0.410 |
| math | 0.630 |
| fault | 0.540 |
| structured | 0.270 |

*Fitment from measured accuracy, decode speed, verbosity and VRAM - refreshes after the judged pass.*

---
*Per-sample transcripts (full question/answer/verdict JSONL) are archived on the portal state volume under `benchmark-results/`, one directory per suite run, named by model. Scores flow to the [leaderboard](../../../docs/data/LEADERBOARD.md) automatically.*
