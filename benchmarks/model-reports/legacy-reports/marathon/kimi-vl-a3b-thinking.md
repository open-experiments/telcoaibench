# kimi-vl-a3b-thinking - TelcoAIBench Marathon Report

**HF repo:** `moonshotai/Kimi-VL-A3B-Thinking-2506`  
**Serving:** vLLM v0.26.0 (KServe RawDeployment, 1x RTX PRO 6000 Blackwell 96GB) | args: `--max-model-len=32768 --trust-remote-code`  
**Endpoint at test time:** `http://kimi-vl-a3b-thinking-predictor.gsma-otel2-test.svc.cluster.local:8080`  

## Results

| Suite | Accuracy | StdErr | Samples | Tier | Date |
|---|---|---|---|---|---|
| 3gpp | **0.110** | 0.0314 | 100 | lite | 2026-08-12 |
| 6g_bench | **0.113** | 0.026 | 150 | lite | 2026-08-13 |
| oranbench | **0.627** | 0.0396 | 150 | lite | 2026-08-12 |
| srsranbench | **0.673** | 0.0384 | 150 | lite | 2026-08-12 |
| telelogs | **0.090** | 0.0288 | 100 | lite | 2026-08-12 |
| telemath | **0.210** | 0.0409 | 100 | lite | 2026-08-12 |
| teleqna | **0.647** | 0.0151 | 1000 | lite | 2026-08-12 |
| teletables | **0.090** | 0.0288 | 100 | lite | 2026-08-12 |

## Generation behavior

| Suite | Samples | Mean latency (s) | Mean output tokens |
|---|---|---|---|
| 3gpp | 100 | 16.7 | 1374 |
| oranbench | 150 | 52.2 | 3917 |
| srsranbench | 150 | 46.2 | 3508 |
| telelogs | 100 | 140.4 | 10199 |
| telemath | 100 | 148.8 | 10332 |
| teleqna | 1000 | 49.8 | 3692 |
| teletables | 100 | 182.5 | 13084 |

## Sample misses (first per suite, for audit)

- **3gpp** dataset index 0: expected `SA5`, parsed `CT1` - output: "◁think▷Okay, let's see. I need to classify this text into one of the 3GPP working groups listed. The text is about Non-Public Networks (NPN) and Stand-alone Non-Public Networks (SNPN), including their definitions and con..."
- **3gpp** dataset index 1: expected `RAN4`, parsed `CT1` - output: "◁think▷Okay, let's see. The user wants me to classify this text into a 3GPP working group. The options are CT1, CT3, CT4, CT6, RAN1, RAN2, RAN3, RAN4, RAN5, RAN_AH1, SA1, SA2, SA3, SA4, SA5, SA6.  First, I need to unders..."
- **3gpp** dataset index 3: expected `SA5`, parsed `CT1` - output: "◁think▷Okay, let's tackle this classification. The user wants me to determine which 3GPP working group the given text belongs to. The options are CT1, CT3, CT4, CT6, RAN1, RAN2, RAN3, RAN4, RAN5, RAN_AH1, SA1, SA2, SA3, ..."
- **oranbench** dataset index 5: expected `A`, parsed `` - output: "◁think▷Okay, so I need to figure out this O-RU FREERUN state question. Let me think. The question is about what the tx-array-carrier and rx-array-carrier states are when the O-RU is in FREERUN. The options are A to D, wi..."
- **oranbench** dataset index 6: expected `D`, parsed `` - output: "◁think▷Okay, so I need to figure out which option is the abbreviation for Key Performance Indicator in the context of O-RAN. Let me think. I remember that O-RAN has a lot of specific terms and acronyms. The question is a..."
- **oranbench** dataset index 8: expected `B`, parsed `A` - output: "◁think▷Okay, so I need to figure out the primary purpose of the R1 DME in O-RAN. Let me start by recalling what I know about O-RAN architecture. O-RAN is the Open Radio Access Network, which is an initiative to make the ..."
- **srsranbench** dataset index 0: expected `A`, parsed `C` - output: "◁think▷Okay, so I need to figure out what the purpose of the lower_phy_controller class is. The question gives four options, A to D. Let me think about each option.  First, I remember that in networking or communication ..."
- **srsranbench** dataset index 1: expected `A`, parsed `C` - output: "◁think▷Okay, so I need to figure out what the purpose of the generate_ru_sdr_config function is. The options are A, B, C, D. Let me think.  The question is about the function's purpose. The options are a bit confusing. L..."
- **srsranbench** dataset index 2: expected `A`, parsed `C` - output: "◁think▷Okay, so I need to figure out what the purpose of the gtpu_demux_ctrl class is. The options are A, B, C, D. Let me think.   First, I remember that GTP-U stands for GPRS Tunneling Protocol for User Plane. It's used..."
- **telelogs** dataset index 0: expected `C6`, parsed `` - output: "◁think▷Okay, let's try to figure out why the throughput dropped below 600Mbps in certain road sections. The user provided a list of 8 potential root causes, and I need to pick the most likely one based on the given data...."

## AI Grid tier fit (measured, auto-scored phase)

**Recommended placement: Tier 3 (Region)** - 16B params, 32GB bf16 moe(3B act), ~90.9s/answer, ~6586 tokens/answer.
Notes: verbose/slow decode - latency envelope only fits a tier up

| Axis (AIGrid) | Measured accuracy |
|---|---|
| knowledge | 0.649 |
| protocol | 0.112 |
| math | 0.210 |
| fault | 0.090 |
| structured | 0.090 |

*Fitment from measured accuracy, decode speed, verbosity and VRAM - refreshes after the judged pass.*

---
*Per-sample transcripts (full question/answer/verdict JSONL) are archived on the portal state volume under `benchmark-results/`, one directory per suite run, named by model. Scores flow to the [leaderboard](../../../docs/data/LEADERBOARD.md) automatically.*
