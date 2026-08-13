# kimi-dev-72b - TelcoAIBench Marathon Report

**HF repo:** `abhishekchohan/Kimi-Dev-72B-AWQ`  
**Serving:** vLLM v0.26.0 (KServe RawDeployment, 1x RTX PRO 6000 Blackwell 96GB) | args: `--max-model-len=32768`  
**Endpoint at test time:** `http://kimi-dev-72b-predictor.gsma-otel2-test.svc.cluster.local:8080`  

## Results

| Suite | Accuracy | StdErr | Samples | Tier | Date |
|---|---|---|---|---|---|
| 3gpp | **0.300** | 0.0461 | 100 | lite | 2026-08-12 |
| 6g_bench | **0.607** | 0.04 | 150 | lite | 2026-08-12 |
| oranbench | **0.740** | 0.0359 | 150 | lite | 2026-08-12 |
| srsranbench | **0.820** | 0.0315 | 150 | lite | 2026-08-12 |
| telelogs | **0.340** | 0.0476 | 100 | lite | 2026-08-12 |
| telemath | **0.420** | 0.0496 | 100 | lite | 2026-08-12 |
| teleqna | **0.767** | 0.0134 | 1000 | lite | 2026-08-12 |
| teletables | **0.320** | 0.0469 | 100 | lite | 2026-08-12 |

## Generation behavior

| Suite | Samples | Mean latency (s) | Mean output tokens |
|---|---|---|---|
| 3gpp | 100 | 25.7 | 806 |
| 6g_bench | 150 | 83.6 | 2402 |
| oranbench | 150 | 21.4 | 709 |
| srsranbench | 150 | 24.4 | 791 |
| telelogs | 100 | 108.3 | 3023 |
| telemath | 100 | 230.1 | 6134 |
| teleqna | 1000 | 35.5 | 1049 |
| teletables | 100 | 98.4 | 2869 |

## Sample misses (first per suite, for audit)

- **3gpp** dataset index 0: expected `SA5`, parsed `SA2` - output: "◁think▷Okay, let's try to figure out which 3GPP working group this text belongs to. The user provided a list of working groups, so I need to match the content to one of them.  First, the text mentions Non-Public Networks..."
- **3gpp** dataset index 1: expected `RAN4`, parsed `RAN1` - output: "◁think▷Okay, let's try to figure out which 3GPP working group this text belongs to. The user provided a list of working groups, so I need to match the content to one of them.  The text mentions "band combination", "inter..."
- **3gpp** dataset index 3: expected `SA5`, parsed `CT1` - output: "◁think▷Okay, let's try to figure out which 3GPP working group this text belongs to. The user provided a list of working groups, so I need to match the content to one of them.  Looking at the text, it mentions things like..."
- **6g_bench** dataset index 4: expected `C`, parsed `B` - output: "◁think▷Okay, let's tackle this problem. The user is asking which slice the UAV should switch to based on the current requirements and projected conditions.  First, the current situation: the UAV is on mMTC with 25ms late..."
- **6g_bench** dataset index 5: expected `C`, parsed `B` - output: "◁think▷Okay, let's try to figure out which scheduler reconfiguration is best here. The problem is about minimizing maximum regret under worst-case conditions. The user provided several options, each with their own trade-..."
- **6g_bench** dataset index 7: expected `B`, parsed `` - output: "◁think▷Okay, let's try to figure out the best answer here. The problem is about deciding whether to accept a compute offload request from a third party. The UAV is returning under a URLLC slice with certain parameters, a..."
- **oranbench** dataset index 8: expected `B`, parsed `D` - output: "◁think▷Okay, let's tackle this question. The user is asking about the primary purpose of the R1 DME (Data Management Entity) in O-RAN. The options given are:  A) To provide a standardized interface for rApps to publish d..."
- **oranbench** dataset index 22: expected `C`, parsed `B` - output: "◁think▷Okay, let's see. The user is asking about the primary goal of the O-RAN ALLIANCE Test and Integration Focus Group (TIFG). The options are:  A) To develop and maintain the O-RAN interface specifications. B) To cond..."
- **oranbench** dataset index 25: expected `B`, parsed `A` - output: "◁think▷Okay, let's tackle this problem. The user is asking about the maximum acceptable relative time error between the O-DU and O-RU for S-plane measurement signals in O-RAN. The options given are 1.5 µs, 3 µs, 10 µs, a..."
- **srsranbench** dataset index 0: expected `A`, parsed `C` - output: "◁think▷Okay, let's try to figure out the purpose of the lower_phy_controller class based on the given options.   First, the name "lower_phy_controller" suggests it's responsible for controlling the lower physical layer. ..."

## AI Grid tier fit (measured, auto-scored phase)

**Recommended placement: Tier 4 (Core DC)** - 73B params, 40GB awq-4bit, ~78.4s/answer, ~2222 tokens/answer.
Notes: verbose/slow decode - latency envelope only fits a tier up; served quantized (awq-4bit)

| Axis (AIGrid) | Measured accuracy |
|---|---|
| knowledge | 0.776 |
| protocol | 0.453 |
| math | 0.420 |
| fault | 0.340 |
| structured | 0.320 |

*Fitment from measured accuracy, decode speed, verbosity and VRAM - refreshes after the judged pass.*

---
*Per-sample transcripts (full question/answer/verdict JSONL) are archived on the portal state volume under `benchmark-results/`, one directory per suite run, named by model. Scores flow to the [leaderboard](../../docs/data/LEADERBOARD.md) automatically.*
