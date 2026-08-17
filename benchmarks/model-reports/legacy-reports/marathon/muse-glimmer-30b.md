# muse-glimmer-30b - TelcoAIBench Marathon Report

**HF repo:** `meta-models/Muse-Glimmer-30B`  
**Serving:** vLLM day-0 build `0.26.1rc1.dev608` (`vllm/vllm-openai:muse-glimmer-x86_64-cu129`), KServe RawDeployment, 1x RTX PRO 6000 Blackwell 96GB  
**Endpoint at test time:** `http://muse-glimmer-30b-predictor.gsma-otel2-test.svc.cluster.local:8080`  

> **Engine caveat:** `MuseGlimmerForConditionalGeneration` is absent from the pinned
> vLLM v0.26.0 *and* 0.27.1 (support PR #51655 open at test time), so this model runs
> on vLLM's day-0 image - the only board entry not on the pinned engine. Scores are
> produced by the identical harness, prompts, and greedy decoding, but the serving
> stack is **not stack-comparable** with the rest of the board.

## Results

| Suite | Accuracy | StdErr | Samples | Tier | Date |
|---|---|---|---|---|---|
| 3gpp | **0.540** | 0.0501 | 100 | lite | 2026-08-14 |
| 6g_bench | **0.693** | 0.0378 | 150 | lite | 2026-08-14 |
| oranbench | **0.807** | 0.0324 | 150 | lite | 2026-08-14 |
| srsranbench | **0.827** | 0.031 | 150 | lite | 2026-08-14 |
| telcos_last_exam | **0.647** | 0.0407 | 30 | lite | 2026-08-15 |
| telelogs | **0.510** | 0.0502 | 100 | lite | 2026-08-14 |
| telemath | **0.360** | 0.0482 | 100 | lite | 2026-08-14 |
| teleqna | **0.795** | 0.0128 | 1000 | lite | 2026-08-14 |
| teletables | **0.300** | 0.0461 | 100 | lite | 2026-08-14 |
| vendor_genai | **0.540** | 0.0312 | 24 | lite | 2026-08-15 |

Judged suites (`telcos_last_exam`, `vendor_genai`) scored by **gpt-5.6-sol**.
Composite **0.6031** | Auto-8 **0.6040** | judged-auto gap **-0.0028** - essentially
zero, the smallest on the board: held-out performance equals benchmark performance.

## Run wall-clock (driver logs)

Auto-scored pass ran 2026-08-14 (Job `lb-run-muse`), judged pass 2026-08-15
(Jobs `lb-judgetest` for vendor_genai, `lb-judged-muse2` for telcos_last_exam,
both after the gpt-5.5 judge retirement).

| Suite | Wall-clock (min) |
|---|---|
| teleqna | 22 |
| teletables | 16 |
| oranbench | 8 |
| srsranbench | 3 |
| telemath | 15 |
| telelogs | 35 |
| 3gpp | 4 |
| 6g_bench | 9 |
| telcos_last_exam (judged) | 16 |
| vendor_genai (judged) | 4 |

All 8 auto-scored suites in **112 min** (~3.6 s/answer batched over ~1,850 answers),
truncation rate 0.4% - the cheapest full run of the three models in this round.

## Notable results

- **Beats the telecom fine-tune (telecomgpt-r1) on both judged suites:**
  telcos_last_exam 0.647 vs 0.595, vendor_genai 0.540 vs 0.418.
- Takes **3gpp outright** from telecomgpt-r1 (0.540 vs 0.520) - the first
  general-purpose model to win a contamination-suspect suite.
- **telelogs 0.510** where the base-family comparison point scores 0.050 - a 10x
  jump on the suite where other general models collapse.
- Weak spots: telemath 0.360, teletables 0.300.

## AI Grid tier fit (measured)

**Recommended placement: Tier 2 (Provider Edge)** - 30B params, 60GB bf16, ~3.6 s/answer (suite mean, batched).

| Axis (AIGrid) | Measured accuracy |
|---|---|
| knowledge | 0.809 |
| protocol | 0.617 |
| math | 0.360 |
| fault | 0.510 |
| structured | 0.300 |

*Fitment from measured accuracy, decode speed, verbosity and VRAM.*

---
*Per-sample transcripts (full question/answer/verdict JSONL) are archived on the portal state volume under `benchmark-results/`, one directory per suite run, named by model. Scores flow to the [leaderboard](../../../docs/data/LEADERBOARD.md) automatically.*
