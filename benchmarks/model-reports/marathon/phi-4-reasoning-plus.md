# phi-4-reasoning-plus - TelcoAIBench Marathon Report

**HF repo:** `microsoft/Phi-4-reasoning-plus`  
**Serving:** vLLM v0.26.0 (KServe RawDeployment, 1x RTX PRO 6000 Blackwell 96GB) | args: `--max-model-len=32768 --override-generation-config={"repetition_penalty": 1.3}`  
**Endpoint at test time:** `http://phi-4-reasoning-plus-predictor.gsma-otel2-test.svc.cluster.local:8080`  

## Results

| Suite | Accuracy | StdErr | Samples | Tier | Date |
|---|---|---|---|---|---|
| 3gpp | **0.090** | 0.0288 | 100 | lite | 2026-08-12 |
| 6g_bench | **0.720** | 0.0368 | 150 | lite | 2026-08-12 |
| oranbench | **0.760** | 0.035 | 150 | lite | 2026-08-12 |
| srsranbench | **0.793** | 0.0332 | 150 | lite | 2026-08-12 |
| telelogs | **0.380** | 0.0488 | 100 | lite | 2026-08-12 |
| telemath | **0.000** | 0.0 | 100 | lite | 2026-08-12 |
| teleqna | **0.722** | 0.0142 | 1000 | lite | 2026-08-12 |
| teletables | **0.310** | 0.0465 | 100 | lite | 2026-08-12 |

## Generation behavior

| Suite | Samples | Mean latency (s) | Mean output tokens |
|---|---|---|---|
| 3gpp | 100 | 81.3 | 3573 |
| 6g_bench | 150 | 43.9 | 2024 |
| oranbench | 150 | 32.7 | 1509 |
| srsranbench | 150 | 36.4 | 1655 |
| telelogs | 100 | 166.8 | 6667 |
| telemath | 100 | 248.7 | 9545 |
| teleqna | 1000 | 48.5 | 2093 |
| teletables | 100 | 97.0 | 4237 |

## Sample misses (first per suite, for audit)

- **3gpp** dataset index 0: expected `SA5`, parsed `CT1` - output: "<think>We have been given instructions:  "As a distinguished expert in telecommunications domain ... classification task." We need to output result in JSON object like { "WORKING_GROUP": "<name>" } where <name> must come..."
- **3gpp** dataset index 1: expected `RAN4`, parsed `CT1` - output: "<think>We have been asked classification task with instructions:  "As a distinguished expert in telecommunications domain ... please help user to classify text into one of these three Gpp working groups." We must choose ..."
- **3gpp** dataset index 3: expected `SA5`, parsed `CT1` - output: "<think>We have been given instructions:  "As a distinguished expert in telecommunications domain... classification task." We must output result with JSON object containing key WORKING_GROUP mapping value equals chosen wo..."
- **6g_bench** dataset index 4: expected `C`, parsed `B` - output: "<think>We have problem statement:  "UAV is currently operating under mMTC slice with parameters: latency=25 ms, jitter = 8ms loss rate=1.2% throughput=1.5 Mbps  edge load=0.75  Mission requirements require "real time sen..."
- **6g_bench** dataset index 7: expected `B`, parsed `A` - output: "<think>We have problem statement:  "UAV returns under URLLC slice with parameters:  - Latency = 7 ms  - Jitter=0.8 ms,  - Loss rate=0.01%  - Throughput=125 Mbps   - Edge Load=0.41  Third party request comes to offload co..."
- **6g_bench** dataset index 13: expected `C`, parsed `B` - output: "<think>We have multi-turn scenario described:  The problem statement: "At turn 5 the UAV captures a high-resolution thermal image while on an eMBB slice with latency 200ms, jitter 50ms, loss 5%, throughput=200Mbps, and e..."
- **oranbench** dataset index 12: expected `C`, parsed `D` - output: "<think>We have been asked: ``` Question text:  "Answer the following multiple-choice question. The entire content of your answer must follow this exact formatting:  `ANSWER: $LETTER`  Where letter is among {A, B, C, D}. ..."
- **oranbench** dataset index 22: expected `C`, parsed `B` - output: "<think>We have been asked "what's the primary goal" with options provided:  The answer choices: Option A says: "To develop and maintain the O-RAN interface specifications." Option B states: "to conduct interoperability t..."
- **oranbench** dataset index 28: expected `B`, parsed `D` - output: "<think>We have query "which type of queue is recommended for transporting PTP packets in O-RAN" with options: Option A: Strict priority queue. Option B: Guaranteed Bandwidth Queue, Option C: both strict-priority & GBW qu..."
- **srsranbench** dataset index 1: expected `A`, parsed `C` - output: "<think>We have been asked "what's the answer?" with instructions: Answer must follow exactly this output formatting: "ANSWER: $LETTER" without additional text or explanation? But we need to check what does it ask:  The p..."

## AI Grid tier fit (measured, auto-scored phase)

**Recommended placement: Tier 3 (Region)** - 14B params, 29GB bf16, ~94.4s/answer, ~3912 tokens/answer.
Notes: verbose/slow decode - latency envelope only fits a tier up

| Axis (AIGrid) | Measured accuracy |
|---|---|
| knowledge | 0.758 |
| protocol | 0.405 |
| math | 0.000 |
| fault | 0.380 |
| structured | 0.310 |

*Fitment from measured accuracy, decode speed, verbosity and VRAM - refreshes after the judged pass.*

## Serving accommodation & measured caveats

**Repetition-penalty accommodation (documented deviation).** Under the
harness's uniform greedy decoding (temperature 0), phi-4-reasoning-plus
degenerates into unterminated repetition loops: on the first teleqna
attempt 307/333 answers hit the 16,384-token cap (mean 15,276 tokens),
e.g. endlessly repeating "I'll produce answer in the required format."
Probes showed repetition_penalty 1.1 and 1.2 do not break the loop;
**1.3 terminates cleanly**. The model was therefore served with a
server-side default `repetition_penalty=1.3`
(`--override-generation-config`), the only per-model sampling
accommodation in the marathon. Prompts, temperature, and the rest of the
harness remained identical to all other models. All recorded scores are
from runs under this setting.

**telemath 0.000 - format-compliance failure, not a knowledge failure.**
The model frequently derives the correct numerical value but ends in
prose and emitted the required `\boxed{}` block in only 1/100 answers,
so nothing parses. Endpoint probes at repetition_penalty 1.15 AND 1.3
both drop `\boxed{}` once reasoning exceeds ~10k tokens - instruction
drift over long generations, independent of the accommodation. Peers
(qwq-32b, seed-oss-36b) hold the format on identical prompts. Takeaway
for AI Grid placement: a model that cannot hold an output contract over
long reasoning is a poor fit for machine-parsed pipelines at any tier,
whatever its raw problem-solving ability.

---
*Per-sample transcripts (full question/answer/verdict JSONL) are archived on the portal state volume under `benchmark-results/`, one directory per suite run, named by model. Scores flow to the [leaderboard](../../docs/data/LEADERBOARD.md) automatically.*
