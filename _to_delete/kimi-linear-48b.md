# kimi-linear-48b - TelcoAIBench Marathon Report

**HF repo:** `nm-testing/Kimi-Linear-48B-A3B-Instruct-FP8-DYNAMIC`  
**Serving:** vLLM v0.26.0 (KServe RawDeployment, 1x RTX PRO 6000 Blackwell 96GB) | args: `--max-model-len=32768 --trust-remote-code`  
**Endpoint at test time:** `http://kimi-linear-48b-predictor.gsma-otel2-test.svc.cluster.local:8080`  

## Results

| Suite | Accuracy | StdErr | Samples | Tier | Date |
|---|---|---|---|---|---|
| 3gpp | **0.360** | 0.0482 | 100 | lite | 2026-08-12 |
| 6g_bench | **0.187** | 0.0319 | 150 | lite | 2026-08-12 |
| oranbench | **0.553** | 0.0407 | 150 | lite | 2026-08-12 |
| srsranbench | **0.800** | 0.0328 | 150 | lite | 2026-08-12 |
| telelogs | **0.070** | 0.0256 | 100 | lite | 2026-08-12 |
| telemath | **0.360** | 0.0482 | 100 | lite | 2026-08-12 |
| teleqna | **0.663** | 0.015 | 1000 | lite | 2026-08-12 |
| teletables | **0.100** | 0.0302 | 100 | lite | 2026-08-12 |

## Generation behavior

| Suite | Samples | Mean latency (s) | Mean output tokens |
|---|---|---|---|
| 3gpp | 100 | 0.3 | 6 |
| 6g_bench | 150 | 140.1 | 13556 |
| oranbench | 150 | 67.9 | 6504 |
| srsranbench | 150 | 20.0 | 1923 |
| telelogs | 100 | 144.0 | 14022 |
| telemath | 100 | 85.9 | 8357 |
| teleqna | 1000 | 39.8 | 3655 |
| teletables | 100 | 147.4 | 14012 |

## Sample misses (first per suite, for audit)

- **3gpp** dataset index 0: expected `SA5`, parsed `SA3` - output: "{"SA3"}"
- **3gpp** dataset index 1: expected `RAN4`, parsed `RAN3` - output: "{"RAN3"}"
- **3gpp** dataset index 2: expected `CT1`, parsed `SA2` - output: "SA2"
- **6g_bench** dataset index 1: expected `A`, parsed `` - output: "We need to parse the problem. It's a multiple choice question about a UAV operating under dust conditions, with network slice switched to mMTC (massive Machine Type Communication) with certain latency, jitter, packet los..."
- **6g_bench** dataset index 2: expected `C`, parsed `` - output: "We need to answer a multiple choice question about a UAV (unmanned aerial vehicle) scenario. The question: "At turn 9 the UAV is on final approach at altitude 50.0 within policy bounds of 15.0 to 120.0 while moving at 18..."
- **6g_bench** dataset index 3: expected `C`, parsed `` - output: "We need to parse the problem. It's a multiple choice question about UAV navigation, network slices, edge load, latency, etc. The question: "Given uncertainty across the next two turns and the need to minimize maximum reg..."
- **oranbench** dataset index 0: expected `C`, parsed `` - output: "We need to answer a multiple choice question: "Which of the following hardware components is responsible for monitoring the hardware status of an O-DU8?" Options: A) 1. Accelerator, B) 2. Baseboard, C) 3. Management Cont..."
- **oranbench** dataset index 1: expected `C`, parsed `` - output: "We need to answer a multiple choice question: "What interface connects the O-RU's Digital Processing Unit to the O-DU's NPU in an integrated O-RAN architecture?" Options: A) Ethernet, B) USB, C) PCIe, D) SATA.  We need t..."
- **oranbench** dataset index 5: expected `A`, parsed `` - output: "We need to answer a multiple choice question about O-RU (Open Radio Unit) transitioning to FREERUN state, and what is the only possible state for both tx-array-carrier and rx-array-carrier.  We need to recall the O-RU st..."
- **srsranbench** dataset index 0: expected `A`, parsed `` - output: "We need to answer a multiple choice question: "What is the purpose of the lower_phy_controller class?" Options:  A) 1. It provides a start and stop methods for the lower physical layer. B) 2. It manages the synchronizati..."

## AI Grid tier fit (measured, auto-scored phase)

**Recommended placement: Tier 3 (Region)** - 48B params, 49GB fp8 moe(3B act), ~80.7s/answer, ~7754 tokens/answer.
Notes: verbose/slow decode - latency envelope only fits a tier up; served quantized (fp8 moe(3B act))

| Axis (AIGrid) | Measured accuracy |
|---|---|
| knowledge | 0.672 |
| protocol | 0.273 |
| math | 0.360 |
| fault | 0.070 |
| structured | 0.100 |

*Fitment from measured accuracy, decode speed, verbosity and VRAM - refreshes after the judged pass.*

## Serving accommodations & an important caveat

**This run measured a third-party quantisation, not Moonshot's release.**
The weights benchmarked here are
`nm-testing/Kimi-Linear-48B-A3B-Instruct-FP8-DYNAMIC`, an FP8 dynamic
quantisation published by a third party - **not**
`moonshotai/Kimi-Linear-48B-A3B-Instruct`. The official bf16 release is
~97GB and does not fit a single 96GB card, so it is being run separately
as `kimi-linear-48b-bf16` on two GPUs (tensor-parallel) as a control.
Until that control lands, these scores should be read as "this FP8 build
of Kimi-Linear", not as a verdict on the model family.

**Two serving accommodations were required to run it at all:**

1. `--trust-remote-code` - the repo ships a custom tokenizer class.
2. **A patch to `tokenization_kimi.py`.** The shipped file does
   `from transformers.models.gpt2.tokenization_gpt2 import
   bytes_to_unicode`, a symbol that no longer exists in the transformers
   version inside vLLM 0.26; serving crashed with `ImportError` on every
   start. The function was inlined into the model's own tokenizer file on
   the weights volume. No model weights or generation settings were
   touched - this only makes the tokenizer importable.

Without both, the model fails to serve; two earlier attempts were
recorded as serving failures before the patch.

---
*Per-sample transcripts (full question/answer/verdict JSONL) are archived on the portal state volume under `benchmark-results/`, one directory per suite run, named by model. Scores flow to the [leaderboard](../../docs/data/LEADERBOARD.md) automatically.*
