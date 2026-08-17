# TelecomGPT-R1: Their Claims vs. Our Measurements

**Their claim** (model card, KU-DFI/TelecomGPT-R1): *89.6% average on the
GSMA Open Telco Leaderboard, #1 across all models open or closed.*
**Our measurement** (TelcoAIBench marathon, 2026-08-11): composite
**0.7507** over 8 suites — #1 on our board too, but ~14 points below
their claimed average on the comparable 7-suite subset (our mean over
the 7 GSMA leaderboard tasks: **0.755**).

Both agree the model is the strongest telecom entrant tested. The gap in
absolute numbers comes from concrete, identifiable protocol differences.

## Side-by-side

| Suite | Our score | Their claim (radar) | Note |
|---|---|---|---|
| teleqna | 0.902 | "1.0 normalized" (= leaderboard best) | close in spirit |
| teletables | **0.360** | "1.0 normalized" | **different protocol - see #1** |
| oranbench | 0.940 | >= 0.94 tier | consistent |
| srsranbench | 0.953 | "1.0 normalized" | consistent |
| telemath | 0.620 | >= 0.94 tier | gap - see #3/#4 |
| telelogs | 0.990 | "1.0 normalized" | consistent |
| 3gpp | **0.520** | "1.0 normalized" | gap - see #3/#4 |
| 6g_bench | 0.720 | n/a | not a GSMA leaderboard task |

## What they did differently

**1. TeleTables: they attach the table to the prompt (admitted).** Their
footnote: *"On TeleTables, we follow the original paper's evaluation
protocol by attaching the table content directly to the prompt."* The
GSMA harness (and ours, parity-validated to <=1pp) asks the question
**without** the table - that is the whole point of the suite as the
leaderboard runs it. With the table attached the task collapses to
reading comprehension. This is why *every* model on our board sits at
0.28-0.39 on teletables while their radar shows leaderboard-best.
This one protocol choice is worth roughly +8 points of their average.

**2. Bespoke system prompt.** Their quickstart evaluates with a custom
persona prompt ("You are TelecomGPT-R1... Reason step-by-step over 3GPP
standards, RAN logs, RF and network derivations"). Our harness uses the
official leaderboard prompt for every model identically - no per-model
prompt engineering. Reasoning-primed system prompts reliably lift
telemath/3gpp-style multi-step tasks.

**3. Serving stack and decoding unknowns.** They verified on
`transformers 5.3-dev + vllm 0.19.1` with optional fast-path kernels
(`flash-linear-attention`, `causal-conv1d` - the base is a Qwen3.5
linear-attention hybrid); their example decodes with
`max_new_tokens=2048`. We serve on vLLM 0.26.0, greedy (temperature 0),
16384-token answer budget, identical settings for all 24 models.
Their decoding parameters (temperature, sampling, retries, n-best)
are not disclosed; the paper is "coming soon."

**4. Task set and aggregation.** Their 89.6% averages the 7 GSMA
leaderboard tasks. Our composite spans 8 suites including 6g_bench
(0.720), and our board reserves the judged suites (Telco's Last Exam,
vendor deep-dives) for the top-5 pass.

**5. Self-reported vs. measured.** Their number is a self-evaluation
presented as a leaderboard result; ours is a pinned, reproducible run
(vLLM version, dtype, prompts, transcripts all archived). This is
precisely the reproducibility gap our 2026-08 verification report
documented across telecom leaderboard claims.

## The contamination question

The model is telecom-*trained* on a 158,915-example corpus built from
"standards documents, Q&A seeds and glossaries, logs, math papers" -
source families that overlap the public benchmarks' own source material.
Scoring 0.99 on telelogs and 0.95 on srsranbench is consistent either
with genuine domain skill or with benchmark-adjacent training data.
The discriminator is our **unpublished judged suites** (Telco's Last
Exam, vendor GenAI deep-dives): a contaminated model typically craters
there while a genuinely capable one holds. TelecomGPT-R1 is in the
top-5, so the judged pass will answer this directly.

## Bottom line

Directionally, our marathon *confirms* their headline: TelecomGPT-R1 is
the best telecom-domain model we have measured, #1 on our board by a
clear margin. The 89.6%-vs-75.5% delta decomposes into an easier
TeleTables protocol (+~8 pts), per-model prompt engineering, undisclosed
decoding settings, and self-evaluation vs. pinned reproduction. Our
number is the one we can defend: same harness, same prompts, same
serving stack for all 24 models, transcripts on disk.

*Generated 2026-08-11 from the TelcoAIBench marathon archive and the
KU-DFI/TelecomGPT-R1 model card (retrieved same day).*
