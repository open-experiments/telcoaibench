# seed-oss-36b - TelcoAIBench Marathon Report

**HF repo:** `ByteDance-Seed/Seed-OSS-36B-Instruct`  
**Serving:** vLLM v0.26.0 (KServe RawDeployment, 1x RTX PRO 6000 Blackwell 96GB)  
**Endpoint at test time:** `http://seed-oss-36b-predictor.gsma-otel2-test.svc.cluster.local:8080`  

## Results

| Suite | Accuracy | StdErr | Samples | Tier | Date |
|---|---|---|---|---|---|
| 3gpp | **0.310** | 0.0465 | 100 | lite | 2026-08-11 |
| 6g_bench | **0.673** | 0.0384 | 150 | lite | 2026-08-11 |
| oranbench | **0.753** | 0.0353 | 150 | lite | 2026-08-11 |
| srsranbench | **0.813** | 0.0319 | 150 | lite | 2026-08-11 |
| telelogs | **0.540** | 0.0501 | 100 | lite | 2026-08-11 |
| telemath | **0.520** | 0.0502 | 100 | lite | 2026-08-11 |
| teleqna | **0.770** | 0.0133 | 1000 | lite | 2026-08-11 |
| teletables | **0.380** | 0.0488 | 100 | lite | 2026-08-11 |

## Generation behavior

| Suite | Samples | Mean latency (s) | Mean output tokens |
|---|---|---|---|
| 3gpp | 100 | 37.0 | 745 |
| 6g_bench | 150 | 177.5 | 3494 |
| oranbench | 150 | 61.7 | 1250 |
| srsranbench | 150 | 40.3 | 827 |
| telelogs | 100 | 440.2 | 7936 |
| telemath | 100 | 579.4 | 10169 |
| teleqna | 1000 | 60.9 | 1228 |
| teletables | 100 | 182.6 | 3570 |

## Sample misses (first per suite, for audit)

- **3gpp** dataset index 0: expected `SA5`, parsed `SA1` - output: "<seed:think> Got it, let's tackle this problem. First, I need to remember what each 3GPP working group does. The user provided a list, so let's recall the key ones related to the text.  The text is talking about Non-Publ..."
- **3gpp** dataset index 2: expected `CT1`, parsed `SA1` - output: "<seed:think> Got it, let's tackle this problem. First, I need to remember what each 3GPP working group does. The user provided a list, so let's recall the key ones related to the text.  The text is talking about EPC (Evo..."
- **3gpp** dataset index 3: expected `SA5`, parsed `SA1` - output: "<seed:think> Got it, let's tackle this problem. First, I need to remember what each 3GPP working group does. The user provided a list, so let's recall the key ones related to the text.  The text mentions a lot about "PM"..."
- **6g_bench** dataset index 3: expected `C`, parsed `B` - output: "<seed:think> Got it, let's try to work through this question step by step. First, I need to remember what the question is asking: the mission needs to continue for at least the next two turns unless worst-case risks exce..."
- **6g_bench** dataset index 4: expected `C`, parsed `B` - output: "<seed:think> Got it, let's try to work through this problem step by step. First, I need to remember what each slice is for—mMTC is machine-type communication (like lots of low-power devices), URLLC is ultra-reliable low-..."
- **6g_bench** dataset index 7: expected `B`, parsed `A` - output: "<seed:think> Got it, let's try to work through this problem step by step. First, I need to make sure I understand all the details given, then look at each option to see which makes sense.  First, let's list out the key i..."
- **oranbench** dataset index 5: expected `A`, parsed `B` - output: "<seed:think> Got it, let's try to work through this question. First, I need to remember what O-RU is—Oh, right, O-RU is an Open Radio Unit, part of the Open RAN (O-RAN) architecture. The question is about state transitio..."
- **oranbench** dataset index 8: expected `B`, parsed `A` - output: "<seed:think> Got it, let's try to work through this question. First, I need to remember what R1 DME is in O-RAN. O-RAN has the Near-RT RIC (Real-Time) and Non-RT RIC (Near-Real Time? Wait, no, Near-RT is real-time, Non-R..."
- **oranbench** dataset index 12: expected `C`, parsed `A` - output: "<seed:think> Got it, let's try to work through this question. The question is asking which field is NOT required for the "GuRanUeId" object. First, I need to remember what GuRanUeId typically includes—wait, GuRan probabl..."
- **srsranbench** dataset index 0: expected `A`, parsed `C` - output: "<seed:think> Got it, let's try to work through this question. The question is about the purpose of the lower_phy_controller class. First, I need to remember what each layer in the OSI model does, especially the physical ..."

## AI Grid tier fit (measured, auto-scored phase)

**Recommended placement: Tier 3 (Region)** - 36B params, 72GB bf16, ~197.4s/answer, ~3652 tokens/answer.
Notes: verbose/slow decode - latency envelope only fits a tier up

| Axis (AIGrid) | Measured accuracy |
|---|---|
| knowledge | 0.779 |
| protocol | 0.492 |
| math | 0.520 |
| fault | 0.540 |
| structured | 0.380 |

*Fitment from measured accuracy, decode speed, verbosity and VRAM - refreshes after the judged pass.*

---
*Per-sample transcripts (full question/answer/verdict JSONL) are archived on the portal state volume under `benchmark-results/`, one directory per suite run, named by model. Scores flow to the [leaderboard](../../docs/data/LEADERBOARD.md) automatically.*
