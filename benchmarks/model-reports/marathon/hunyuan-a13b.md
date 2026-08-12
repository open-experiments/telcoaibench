# hunyuan-a13b - TelcoAIBench Marathon Report

**HF repo:** `tencent/Hunyuan-A13B-Instruct-FP8`  
**Serving:** vLLM v0.26.0 (KServe RawDeployment, 1x RTX PRO 6000 Blackwell 96GB) | args: `--trust-remote-code --max-model-len=32768`  
**Endpoint at test time:** `http://hunyuan-a13b-predictor.gsma-otel2-test.svc.cluster.local:8080`  

## Results

| Suite | Accuracy | StdErr | Samples | Tier | Date |
|---|---|---|---|---|---|
| 3gpp | **0.200** | 0.0402 | 100 | lite | 2026-08-12 |
| 6g_bench | **0.660** | 0.0388 | 150 | lite | 2026-08-12 |
| oranbench | **0.687** | 0.038 | 150 | lite | 2026-08-12 |
| srsranbench | **0.767** | 0.0346 | 150 | lite | 2026-08-12 |
| telelogs | **0.270** | 0.0446 | 100 | lite | 2026-08-12 |
| telemath | **0.480** | 0.0502 | 100 | lite | 2026-08-12 |
| teleqna | **0.733** | 0.014 | 1000 | lite | 2026-08-12 |
| teletables | **0.380** | 0.0488 | 100 | lite | 2026-08-12 |

## Generation behavior

| Suite | Samples | Mean latency (s) | Mean output tokens |
|---|---|---|---|
| 3gpp | 100 | 18.3 | 411 |
| 6g_bench | 150 | 115.7 | 3124 |
| oranbench | 150 | 41.5 | 1150 |
| srsranbench | 150 | 28.6 | 810 |
| telelogs | 100 | 146.7 | 3779 |
| telemath | 100 | 185.3 | 4960 |
| teleqna | 1000 | 39.8 | 1105 |
| teletables | 100 | 118.3 | 3230 |

## Sample misses (first per suite, for audit)

- **3gpp** dataset index 0: expected `SA5`, parsed `RAN1` - output: "<think> Okay, let's try to figure out which 3GPP working group this text belongs to. First, I need to recall what each working group does. The text is about Non-Public Networks (NPN) and Stand-alone Non-Public Networks (..."
- **3gpp** dataset index 1: expected `RAN4`, parsed `n78` - output: "<think> Okay, let's try to figure out which 3GPP working group this text belongs to. First, I need to look at the content of the text. The text talks about a band combination, interference analysis, insertion loss, and M..."
- **3gpp** dataset index 2: expected `CT1`, parsed `RAN1` - output: "<think> Okay, let's tackle this classification. The user wants me to figure out which 3GPP working group this text belongs to. First, I need to look at the content of the text.   The text talks about EPC (Evolved Packet ..."
- **6g_bench** dataset index 2: expected `C`, parsed `B` - output: "<think> Okay, let's try to work through this problem. So the question is about a UAV at turn 9 on final approach. The options are about whether to maintain autonomy, delay downgrade, immediately downgrade, or switch to e..."
- **6g_bench** dataset index 3: expected `C`, parsed `B` - output: "<think> Okay, let's try to work through this problem. So the question is about a UAV that needs to decide which network slice to use for the next two turns, considering various factors. Let's break down the information g..."
- **6g_bench** dataset index 4: expected `C`, parsed `B` - output: "<think> Okay, let's try to work through this problem step by step. First, I need to understand the requirements of the mission. The UAV is doing real-time sensor focus adjustment, which needs a maximum tolerable latency ..."
- **oranbench** dataset index 2: expected `A`, parsed `D` - output: "<think> Okay, let's tackle this question about the Underlay Network in O-RAN. First, I need to remember what O-RAN stands for. Oh right, Open Radio Access Network. It's an open architecture for radio access networks, aim..."
- **oranbench** dataset index 8: expected `B`, parsed `D` - output: "<think> Okay, let's tackle this question about the R1 DME in O-RAN. First, I need to remember what O-RAN is. O-RAN stands for Open Radio Access Network, which is an open standard for next-generation wireless networks. It..."
- **oranbench** dataset index 12: expected `C`, parsed `A` - output: "<think> Okay, let's try to figure out this question. The question is asking which of the options is NOT a required field for the "GuRanUeId" object. The options are A to D, each with different identifiers.  First, I need..."
- **srsranbench** dataset index 0: expected `A`, parsed `C` - output: "<think> Okay, let's tackle this question. The question is about the purpose of the lower_phy_controller class. I need to figure out which option correctly describes its function.  First, I should recall what a lower PHY ..."

## AI Grid tier fit (measured, auto-scored phase)

**Recommended placement: Tier 4 (Core DC)** - 80B params, 81GB fp8 moe(13B act), ~86.8s/answer, ~2321 tokens/answer.
Notes: verbose/slow decode - latency envelope only fits a tier up; served quantized (fp8 moe(13B act))

| Axis (AIGrid) | Measured accuracy |
|---|---|
| knowledge | 0.729 |
| protocol | 0.430 |
| math | 0.480 |
| fault | 0.270 |
| structured | 0.380 |

*Fitment from measured accuracy, decode speed, verbosity and VRAM - refreshes after the judged pass.*

---
*Per-sample transcripts (full question/answer/verdict JSONL) are archived on the portal state volume under `benchmark-results/`, one directory per suite run, named by model. Scores flow to the [leaderboard](../../docs/data/LEADERBOARD.md) automatically.*
