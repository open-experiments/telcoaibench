# otel2-llm-31b-it - TelcoAIBench Marathon Report

**Serving:** vLLM v0.26.0 (KServe RawDeployment, 1x RTX PRO 6000 Blackwell 96GB)  
**Endpoint at test time:** `https://otel2-llm-31b-it-gsma-otel2-test.apps.venice.narlabs.io`  

## Results

| Suite | Accuracy | StdErr | Samples | Tier | Date |
|---|---|---|---|---|---|
| 3gpp | **0.610** | 0.049 | 100 | lite | 2026-08-10 |
| 6g_bench | **0.653** | 0.039 | 150 | lite | 2026-08-10 |
| oranbench | **0.787** | 0.0336 | 150 | lite | 2026-08-10 |
| srsranbench | **0.840** | 0.03 | 150 | lite | 2026-08-10 |
| telcos_last_exam | **0.587** | 0.034 | 30 | lite | 2026-08-10 |
| telelogs | **0.470** | 0.0502 | 100 | lite | 2026-08-10 |
| telemath | **0.560** | 0.0499 | 100 | lite | 2026-08-10 |
| teleqna | **0.795** | 0.0128 | 1000 | lite | 2026-08-10 |
| teletables | **0.290** | 0.0456 | 100 | lite | 2026-08-10 |
| vendor_genai | **0.476** | 0.0444 | 24 | lite | 2026-08-10 |

## Generation behavior

| Suite | Samples | Mean latency (s) | Mean output tokens |
|---|---|---|---|
| 3gpp | 100 | 1.3 | 9 |
| 6g_bench | 150 | 12.9 | 275 |
| oranbench | 150 | 4.7 | 106 |
| srsranbench | 150 | 4.6 | 104 |
| telcos_last_exam | 30 | 77.0 | 1374 |
| telelogs | 100 | 27.5 | 512 |
| telemath | 100 | 36.3 | 806 |
| teleqna | 1000 | 4.7 | 106 |
| teletables | 100 | 26.4 | 597 |
| vendor_genai | 24 | 97.4 | 1930 |

## Sample misses (first per suite, for audit)

- **3gpp** dataset index 0: expected `SA5`, parsed `SA2` - output: "{"WORKING GROUP": "SA2"}"
- **3gpp** dataset index 4: expected `RAN_AH1`, parsed `RAN1` - output: "{"WORKING GROUP": "RAN1"}"
- **3gpp** dataset index 5: expected `SA1`, parsed `SA6` - output: "{"WORKING GROUP": "SA6"}"
- **6g_bench** dataset index 3: expected `C`, parsed `B` - output: "The correct answer is based on minimizing maximum regret under uncertainty over the next two turns, especially given the current high edge load on mMTC and the need to maintain safe autonomous navigation in icing conditi..."
- **6g_bench** dataset index 4: expected `C`, parsed `B` - output: "To determine the correct slice for the UAV, we must evaluate the mission requirements against the performance characteristics of the available slices under the projected conditions.  1.  **Mission Requirements:**     *  ..."
- **6g_bench** dataset index 7: expected `B`, parsed `C` - output: "To determine the correct course of action, we must evaluate the impact of accepting the third-party request on the edge load and the risk of violating the SLA.  1. **Current State**:    - Edge load: 0.41    - SLA limit: ..."
- **oranbench** dataset index 3: expected `C`, parsed `` - output: "The correct answer is C) 3. Ongoing data transfer between the Application Test Server and Test UE or UE emulator.  In the context of validating the user plane downlink data forwarding function during an Inter-Master Node..."
- **oranbench** dataset index 8: expected `B`, parsed `A` - output: "The primary purpose of the R1 DME (Data Management Entity) in O-RAN is to provide a standardized interface for rApps to publish data. This allows for consistent data management and interoperability within the O-RAN archi..."
- **oranbench** dataset index 11: expected `D`, parsed `B` - output: "The correct answer is based on the behavior defined for RIC Service CONTROL requests in the context of timer expiration. When a valid Call Process ID is received after the Time to Wait timer expires, the E2 Node is unabl..."
- **srsranbench** dataset index 1: expected `A`, parsed `C` - output: "The function name `generate_ru_sdr_config` suggests that its purpose is to create or generate a configuration related to RU SDR. Among the given options, option C directly aligns with this interpretation, as it involves ..."

## AI Grid tier fit (measured, auto-scored phase)

**Recommended placement: Tier 2 (Provider Edge)** - 31B params, 62GB bf16, ~14.8s/answer, ~314 tokens/answer.


| Axis (AIGrid) | Measured accuracy |
|---|---|
| knowledge | 0.807 |
| protocol | 0.632 |
| math | 0.560 |
| fault | 0.470 |
| structured | 0.290 |

*Fitment from measured accuracy, decode speed, verbosity and VRAM - refreshes after the judged pass.*

---
*Per-sample transcripts (full question/answer/verdict JSONL) are archived on the portal state volume under `benchmark-results/`, one directory per suite run, named by model. Scores flow to the [leaderboard](../../../docs/data/LEADERBOARD.md) automatically.*
