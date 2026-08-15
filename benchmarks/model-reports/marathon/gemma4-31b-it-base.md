# gemma4-31b-it-base - TelcoAIBench Marathon Report

**Serving:** vLLM v0.26.0 (KServe RawDeployment, 1x RTX PRO 6000 Blackwell 96GB)  
**Endpoint at test time:** `https://gemma4-31b-it-base-gsma-otel2-test.apps.venice.narlabs.io`  

## Results

| Suite | Accuracy | StdErr | Samples | Tier | Date |
|---|---|---|---|---|---|
| 3gpp | **0.470** | 0.0502 | 100 | lite | 2026-08-10 |
| 6g_bench | **0.693** | 0.0378 | 150 | lite | 2026-08-10 |
| oranbench | **0.827** | 0.031 | 150 | lite | 2026-08-10 |
| srsranbench | **0.820** | 0.0315 | 150 | lite | 2026-08-10 |
| telcos_last_exam | **0.662** | 0.0336 | 30 | lite | 2026-08-10 |
| telelogs | **0.530** | 0.0502 | 100 | lite | 2026-08-10 |
| telemath | **0.680** | 0.0469 | 100 | lite | 2026-08-10 |
| teleqna | **0.806** | 0.0125 | 1000 | lite | 2026-08-10 |
| teletables | **0.390** | 0.049 | 100 | lite | 2026-08-10 |
| vendor_genai | **0.592** | 0.0348 | 24 | lite | 2026-08-10 |

## Generation behavior

| Suite | Samples | Mean latency (s) | Mean output tokens |
|---|---|---|---|
| 3gpp | 100 | 1.4 | 9 |
| 6g_bench | 150 | 19.0 | 409 |
| oranbench | 150 | 4.0 | 87 |
| srsranbench | 150 | 3.0 | 64 |
| telcos_last_exam | 30 | 80.5 | 1463 |
| telelogs | 100 | 41.6 | 804 |
| telemath | 100 | 41.1 | 917 |
| teleqna | 1000 | 4.4 | 98 |
| teletables | 100 | 12.7 | 289 |
| vendor_genai | 24 | 42.4 | 630 |

## Sample misses (first per suite, for audit)

- **3gpp** dataset index 0: expected `SA5`, parsed `SA2` - output: "{"WORKING GROUP": "SA2"}"
- **3gpp** dataset index 4: expected `RAN_AH1`, parsed `RAN1` - output: "{"WORKING GROUP": "RAN1"}"
- **3gpp** dataset index 5: expected `SA1`, parsed `SA2` - output: "{"WORKING GROUP": "SA2"}"
- **6g_bench** dataset index 3: expected `C`, parsed `B` - output: "To determine the best course of action, we must evaluate the risks associated with each network slice based on the provided data and the objective of minimizing maximum regret over the next two turns.  1.  **mMTC (Curren..."
- **6g_bench** dataset index 4: expected `C`, parsed `B` - output: "To determine the correct slice, we must evaluate the mission requirements against the performance of the available slices under the projected edge load.  **1. Mission Requirements:** *   Maximum tolerable latency: 15ms *..."
- **6g_bench** dataset index 7: expected `B`, parsed `A` - output: "To determine the correct action, we evaluate the edge load constraints and the risks associated with the request.  1.  **Current State:** Edge load = 0.41. 2.  **SLA Limit:** Edge load $\le$ 0.95. 3.  **Immediate Impact ..."
- **oranbench** dataset index 8: expected `B`, parsed `A` - output: "The R1 interface in the O-RAN architecture connects the Non-RT RIC to the Near-RT RIC. Within this context, the Data Management Entity (DME) serves as a standardized mechanism to manage the exchange of data. Specifically..."
- **oranbench** dataset index 11: expected `D`, parsed `B` - output: "The correct answer is based on the O-RAN E2 interface specifications regarding the RIC Service CONTROL procedure. When a CONTROL request is received with a Call Process ID that was previously used, but the associated "Ti..."
- **oranbench** dataset index 12: expected `C`, parsed `D` - output: "Based on standard 3GPP specifications for the `GuRanUeId` (Global RAN UE Identifier) structure, the object typically consists of the `plmnId`, the `gnbId` (or `globalGnbId`), and the `ranUeId`. However, in the context of..."
- **srsranbench** dataset index 2: expected `A`, parsed `C` - output: "The `gtpu_demux_ctrl` class is typically designed to act as the control interface for the GTP-U demultiplexer, managing how incoming GTP-U packets are steered or handled based on the Tunnel Endpoint Identifier (TEID).  A..."

## AI Grid tier fit (measured, auto-scored phase)

**Recommended placement: Tier 2 (Provider Edge)** - 31B params, 62GB bf16, ~15.9s/answer, ~334 tokens/answer.


| Axis (AIGrid) | Measured accuracy |
|---|---|
| knowledge | 0.818 |
| protocol | 0.582 |
| math | 0.680 |
| fault | 0.530 |
| structured | 0.390 |

*Fitment from measured accuracy, decode speed, verbosity and VRAM - refreshes after the judged pass.*

---
*Per-sample transcripts (full question/answer/verdict JSONL) are archived on the portal state volume under `benchmark-results/`, one directory per suite run, named by model. Scores flow to the [leaderboard](../../../docs/data/LEADERBOARD.md) automatically.*
