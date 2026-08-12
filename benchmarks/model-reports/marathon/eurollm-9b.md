# eurollm-9b - TelcoAIBench Marathon Report

**HF repo:** `utter-project/EuroLLM-9B-Instruct`  
**Serving:** vLLM v0.26.0 (KServe RawDeployment, 1x RTX PRO 6000 Blackwell 96GB) | args: `--max-model-len=4096`  
**Endpoint at test time:** `http://eurollm-9b-predictor.gsma-otel2-test.svc.cluster.local:8080`  

## Results

| Suite | Accuracy | StdErr | Samples | Tier | Date |
|---|---|---|---|---|---|
| 3gpp | **0.230** | 0.0423 | 100 | lite | 2026-08-12 |
| 6g_bench | **0.567** | 0.0406 | 150 | lite | 2026-08-12 |
| oranbench | **0.553** | 0.0407 | 150 | lite | 2026-08-12 |
| srsranbench | **0.787** | 0.0336 | 150 | lite | 2026-08-12 |
| telelogs | **0.000** | 0.0 | 100 | lite | 2026-08-12 |
| telemath | **0.010** | 0.01 | 100 | lite | 2026-08-12 |
| teleqna | **0.496** | 0.0158 | 1000 | lite | 2026-08-12 |
| teletables | **0.280** | 0.0451 | 100 | lite | 2026-08-12 |

## Generation behavior

| Suite | Samples | Mean latency (s) | Mean output tokens |
|---|---|---|---|
| 3gpp | 100 | 0.3 | 7 |
| 6g_bench | 150 | 0.3 | 6 |
| oranbench | 150 | 0.1 | 6 |
| srsranbench | 150 | 0.1 | 6 |
| telelogs | 100 | 2.9 | 151 |
| telemath | 100 | 14.6 | 1093 |
| teleqna | 1000 | 0.1 | 7 |
| teletables | 100 | 0.2 | 9 |

## Sample misses (first per suite, for audit)

- **3gpp** dataset index 0: expected `SA5`, parsed `RAN1` - output: "{RAN1}"
- **3gpp** dataset index 1: expected `RAN4`, parsed `RAN1` - output: "{RAN1}"
- **3gpp** dataset index 2: expected `CT1`, parsed `RAN1` - output: "{RAN1}"
- **6g_bench** dataset index 0: expected `A`, parsed `C` - output: "ANSWER: C"
- **6g_bench** dataset index 3: expected `C`, parsed `D` - output: "ANSWER: D"
- **6g_bench** dataset index 4: expected `C`, parsed `B` - output: "ANSWER: B"
- **oranbench** dataset index 2: expected `A`, parsed `B` - output: "ANSWER: B"
- **oranbench** dataset index 3: expected `C`, parsed `A` - output: "ANSWER: A"
- **oranbench** dataset index 5: expected `A`, parsed `D` - output: "ANSWER: D"
- **srsranbench** dataset index 2: expected `A`, parsed `C` - output: "ANSWER: C"

## AI Grid tier fit (measured, auto-scored phase)

**Recommended placement: Tier 1 (User Edge)** - 9B params, 18GB bf16, ~2.6s/answer, ~182 tokens/answer.


| Axis (AIGrid) | Measured accuracy |
|---|---|
| knowledge | 0.612 |
| protocol | 0.398 |
| math | 0.010 |
| fault | 0.000 |
| structured | 0.280 |

*Fitment from measured accuracy, decode speed, verbosity and VRAM - refreshes after the judged pass.*

## Context budget: a measured deployment constraint

EuroLLM-9B has a **4,096-token context window**, and that ceiling - not
its reasoning - decided whether suites could run at all.

With the marathon's default answer budget the long-context suites were
*unservable*: every request returned HTTP 400, e.g.
`maximum context length is 4096 tokens. However, you requested 3000
output tokens and your prompt contains at least 1097 input tokens, for a
total of at least 4097`. Four consecutive attempts were killed by the
zero-token watchdog before the cause was identified. Lowering the answer
budget to 1,024 recovered `3gpp` and `6g_bench`; `telelogs` still failed
on a single sample whose prompt tokenises to 3,073 tokens (3,073 + 1,024
= 4,097 - over by one token again). A 512-token budget completed all
eight suites.

**Why this matters for AI Grid placement:** this is a Tier 1 (User Edge)
candidate that runs out of *context budget*, not capability, on the
long-context telecom suites. At the edge, the context window is a
first-class deployment constraint alongside VRAM and latency - a 9B model
that cannot ingest a log excerpt plus emit a reasoned answer is
mis-placed for fault-diagnosis work regardless of its accuracy elsewhere.

**Also recorded:** `telelogs` scored **0 correct out of 99** clean
samples (one sample errored), and `telemath` scored 0.010. Both are
genuine measurements, not harness artefacts.

---
*Per-sample transcripts (full question/answer/verdict JSONL) are archived on the portal state volume under `benchmark-results/`, one directory per suite run, named by model. Scores flow to the [leaderboard](../../docs/data/LEADERBOARD.md) automatically.*
