# Measured Evidence for AI Grid Tier Placement

*Support material for "Telco AI Grid: Serving, Governing, & Monetizing AI" (Haiby, Mufti, Nar, Sharma).*
*Source: TelcoAIBench marathon, 2026-08-10/11 - identical harness, prompts, greedy decoding, vLLM v0.26.0,*
*1x RTX PRO 6000 Blackwell 96GB per model. Per-question transcripts archived; AUTO-SCORED phase snapshot.*

> **Snapshot note (2026-08-15):** the tables below are the 13-model snapshot this pack was
> written against. The board has since grown to 31 ranked models (judged pass complete,
> judge `gpt-5.6-sol`) - the maintained fitment for every model lives in
> [`docs/data/tierfit.json`](../../../docs/data/tierfit.json) and each model's
> [marathon report](./). The measurements and conclusions below are unchanged.

The article's placement principle - *"tier choice should rest on measured accuracy, latency, and cost
for the target workload rather than parameter count alone"* - is directly observable in this data:

## Table 1. Measured tier fitment (13 models benchmarked to date)

| Model | Params | Weights (as served) | Composite | ~s/answer | ~tokens/answer | Measured tier fit |
|---|---|---|---|---|---|---|
| telecomgpt-r1 | 27B | 55GB bf16 | 0.751 | 24.1 | 623 | Tier 2 - Provider Edge |
| seed-oss-36b | 36B | 72GB bf16 | 0.679 | 86.4 | 1718 | Tier 3 - Region |
| gemma4-31b-it-base | 31B | 62GB bf16 | 0.646 | 15.9 | 334 | Tier 2 - Provider Edge |
| gpt-oss-120b | 117B | 63GB mxfp4 | 0.605 | 6.6 | 546 | Tier 3 - Region |
| otel2-llm-31b-it | 31B | 62GB bf16 | 0.599 | 14.8 | 314 | Tier 2 - Provider Edge |
| magistral-small-2509 | 24B | 48GB bf16 | 0.575 | - | - | Tier 2 - Provider Edge |
| gpt-oss-20b | 20B | 13GB mxfp4 | 0.575 | 9.8 | 1351 | Tier 2 - Provider Edge |
| mistral-small-3-2-24b | 24B | 48GB bf16 | 0.565 | 7.5 | 222 | Tier 2 - Provider Edge |
| qwen3-6-35b-a3b | 35B | 72GB bf16 moe(3B act) | 0.530 | 67.1 | 4750 | Tier 3 - Region |
| glm-4-5-air | 106B | 63GB awq-4bit moe(12B act) | 0.501 | 73.4 | 3123 | Tier 4 - Core DC |
| qwen3-6-27b | 27B | 56GB bf16 | 0.482 | 192.9 | 4875 | Tier 3 - Region |
| otel-llm-20b-it | 20B | 42GB bf16 (fp32 ckpt) | 0.462 | 23.2 | 1457 | Tier 2 - Provider Edge |
| nemotron-3-nano-30b | 30B | 63GB bf16 moe(3B act) | 0.454 | 58.8 | 3907 | Tier 3 - Region |

## Findings the tier envelopes predict - and the measurements confirm

1. **Parameter count misleads placement.** qwen3-6-27b (27B, Tier-2-sized) measures ~193s/answer on
   fault-analysis workloads - 10x the token spend of its MoE sibling - and only fits a Region-tier
   latency envelope. Size said Tier 2; measurement says Tier 3.
2. **Quantized MoE breaks the size-tier correlation upward.** gpt-oss-120b (117B) serves from 63GB MXFP4
   at ~6.6s/answer and 0.605 composite: Region-tier capability on a single provider-edge GPU budget.
3. **The reasoning tax is quantifiable.** magistral vs mistral (same 24B base): +0.010 composite for ~2x
   tokens/answer - a per-tier cost/accuracy trade the gateway's router can price explicitly.
4. **Domain tuning beats scale at the same tier.** telecomgpt-r1 (27B, Tier 2 fit) outscores every
   larger general model on the board - right-model-right-tier in one row.
5. **Deployment reality gates placement before accuracy does.** An FP32-packaged 20B checkpoint required
   140GB host RAM to load (3 failed deploys); AWQ-quantized MoE decode measured ~73s/answer despite
   fitting VRAM. Both invisible to parameter-count planning; both measured here.

*Full per-model reports with per-suite accuracy, generation behavior, and audit transcripts:*
*github.com/open-experiments/telcoaibench - benchmarks/model-reports/marathon/*
