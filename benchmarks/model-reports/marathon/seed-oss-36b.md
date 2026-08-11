# seed-oss-36b - TelcoAIBench Marathon Report

**HF repo:** `ByteDance-Seed/Seed-OSS-36B-Instruct`  
**Serving:** vLLM v0.26.0 (KServe RawDeployment, 1x RTX PRO 6000 Blackwell 96GB)  
**Endpoint at test time:** `http://seed-oss-36b-predictor.gsma-otel2-test.svc.cluster.local:8080`  

## Results

| Suite | Accuracy | StdErr | Samples | Tier | Date |
|---|---|---|---|---|---|
| oranbench | **0.753** | 0.0353 | 150 | lite | 2026-08-11 |
| srsranbench | **0.813** | 0.0319 | 150 | lite | 2026-08-11 |
| teleqna | **0.770** | 0.0133 | 1000 | lite | 2026-08-11 |
| teletables | **0.380** | 0.0488 | 100 | lite | 2026-08-11 |

## Generation behavior

| Suite | Samples | Mean latency (s) | Mean output tokens |
|---|---|---|---|
| oranbench | 150 | 61.7 | 1250 |
| srsranbench | 150 | 40.3 | 827 |
| teleqna | 1000 | 60.9 | 1228 |
| teletables | 100 | 182.6 | 3570 |

## Sample misses (first per suite, for audit)

- **oranbench** dataset index 5: expected `A`, parsed `B` - output: "<seed:think> Got it, let's try to work through this question. First, I need to remember what O-RU is—Oh, right, O-RU is an Open Radio Unit, part of the Open RAN (O-RAN) architecture. The question is about state transitio..."
- **oranbench** dataset index 8: expected `B`, parsed `A` - output: "<seed:think> Got it, let's try to work through this question. First, I need to remember what R1 DME is in O-RAN. O-RAN has the Near-RT RIC (Real-Time) and Non-RT RIC (Near-Real Time? Wait, no, Near-RT is real-time, Non-R..."
- **oranbench** dataset index 12: expected `C`, parsed `A` - output: "<seed:think> Got it, let's try to work through this question. The question is asking which field is NOT required for the "GuRanUeId" object. First, I need to remember what GuRanUeId typically includes—wait, GuRan probabl..."
- **srsranbench** dataset index 0: expected `A`, parsed `C` - output: "<seed:think> Got it, let's try to work through this question. The question is about the purpose of the lower_phy_controller class. First, I need to remember what each layer in the OSI model does, especially the physical ..."
- **srsranbench** dataset index 1: expected `A`, parsed `C` - output: "<seed:think> Got it, let's try to work through this question. The question is about the purpose of the `generate_ru_sdr_config` function. First, I need to remember what each part of the name means: "generate" suggests cr..."
- **srsranbench** dataset index 9: expected `A`, parsed `C` - output: "<seed:think> Got it, let's try to work through this question. The question is asking for the value of "sib_mapping" in the "sib configuration". First, I need to remember what SIB (System Information Block) mapping means ..."
- **teleqna** dataset index 9: expected `B`, parsed `D` - output: "<seed:think> Got it, let's try to work through this question. The question is about the purpose of the Control and User Plane Separation (CUPS) work item in 3GPP Release 14 for EPC nodes. First, I need to remember what C..."
- **teleqna** dataset index 11: expected `D`, parsed `C` - output: "<seed:think> Got it, let's try to work through this question. The question is about the inputs required for the Nmfaf_3caDataManagement_Fetch service operation in 3GPP Release 18. First, I need to remember what Nmfaf is—..."
- **teleqna** dataset index 12: expected `B`, parsed `D` - output: "<seed:think> Got it, let's try to work through this question. First, I need to remember what ARP means in the context of 3GPP and positioning. ARP stands for "Absolute Radio Frequency Channel Number"—wait, no, wait, actu..."
- **teletables** dataset index 1: expected `B`, parsed `E` - output: "<seed:think> Got it, let's try to work through this question. The question is asking which channel bandwidth has the highest ratio of information bits to binary channel bits per slot. First, I need to remember what those..."

## AI Grid tier fit (measured, MCQ phase)

**Recommended placement: Tier 3 (Region)** - 36B params, 72GB bf16, ~86.4s/answer, ~1718 tokens/answer.
Notes: verbose/slow decode - latency envelope only fits a tier up

| Axis (AIGrid) | Measured accuracy |
|---|---|
| knowledge | 0.779 |
| structured | 0.380 |

*Fitment from measured accuracy, decode speed, verbosity and VRAM - refreshes after the judged pass.*

---
*Per-sample transcripts (full question/answer/verdict JSONL) are archived on the portal state volume under `benchmark-results/`, one directory per suite run, named by model. Scores flow to the [leaderboard](../../docs/data/LEADERBOARD.md) automatically.*
