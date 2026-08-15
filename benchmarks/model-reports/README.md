# Model Reports - Leaderboard Proof Points

Every ranked model on the [TelcoAIBench leaderboard](../../docs/data/LEADERBOARD.md) is
backed by a **marathon report** in [`marathon/`](marathon/): per-suite scores with stderr,
sample counts and dates, generation behavior, first-miss audit samples, and measured
[AI Grid tier fit](../../docs/data/tierfit.json). Per-sample transcripts (question /
answer / verdict JSONL) are archived on the portal state volume under `benchmark-results/`.

AUTO-SCORED suites are machine-scored; `telcos_last_exam` and `vendor_genai` are
LLM-as-judge suites (judge: `gpt-5.6-sol` since 2026-08-15; see
[lessons-learned](../../docs/lessons-learned.md) on the `gpt-5.5` retirement).

## Index (board order)

| Rank | Model | Composite (10) | Auto-8 | Coverage | Runs | Report |
|---|---|---|---|---|---|---|
| 1 | telecomgpt-r1 | **0.6802** | 0.7507 | 100% | 1 | [report](marathon/telecomgpt-r1.md) |
| 2 | gemma4-31b-it-base | **0.6459** | 0.6520 | 100% | 1 | [report](marathon/gemma4-31b-it-base.md) |
| 3 | muse-glimmer-30b | **0.6031** | 0.6040 | 100% | 1 | [report](marathon/muse-glimmer-30b.md) |
| 4 | otel2-llm-31b-it | **0.5993** | 0.6256 | 100% | 1 | [report](marathon/otel2-llm-31b-it.md) |
| 5 | qwen3-8-27b | **0.5909** | 0.6590 | 100% | best of 3 | [report](marathon/qwen3-8-27b.md) |
| 6 | gpt-oss-120b | **0.5601** | 0.6049 | 100% | 1 | [report](marathon/gpt-oss-120b.md) |
| 7 | seed-oss-36b | **0.5456** | 0.5950 | 100% | 1 | [report](marathon/seed-oss-36b.md) |
| 8 | nemotron-3-super-120b | **0.5456** | 0.5822 | 100% | 1 | [report](marathon/nemotron-3-super-120b.md) |
| 9 | qwq-32b | **0.5304** | 0.5767 | 100% | 1 | [report](marathon/qwq-32b.md) |
| 10 | qwen3-6-35b-a3b | **0.5284** | 0.5303 | 100% | 1 | [report](marathon/qwen3-6-35b-a3b.md) |
| 11 | mistral-small-3-2-24b | **0.5235** | 0.5654 | 100% | 1 | [report](marathon/mistral-small-3-2-24b.md) |
| 12 | magistral-small-2509 | **0.5208** | 0.5753 | 100% | 1 | [report](marathon/magistral-small-2509.md) |
| 13 | falcon-h1-34b | **0.5137** | 0.5514 | 100% | 1 | [report](marathon/falcon-h1-34b.md) |
| 14 | kimi-dev-72b | **0.5020** | 0.5392 | 100% | 1 | [report](marathon/kimi-dev-72b.md) |
| 15 | qwen3-6-27b | **0.4983** | 0.4818 | 100% | 1 | [report](marathon/qwen3-6-27b.md) |
| 16 | glm-4-5-air | **0.4820** | 0.5007 | 100% | 1 | [report](marathon/glm-4-5-air.md) |
| 17 | exaone-4-0-32b | **0.4755** | 0.5298 | 100% | 1 | [report](marathon/exaone-4-0-32b.md) |
| 18 | r1-distill-qwen-32b | **0.4754** | 0.5257 | 100% | 1 | [report](marathon/r1-distill-qwen-32b.md) |
| 19 | hunyuan-a13b | **0.4536** | 0.5221 | 100% | 1 | [report](marathon/hunyuan-a13b.md) |
| 20 | phi-4-reasoning-plus | **0.4392** | 0.4719 | 100% | 1 | [report](marathon/phi-4-reasoning-plus.md) |
| 21 | otel-llm-20b-it | **0.4287** | 0.4615 | 100% | 1 | [report](marathon/otel-llm-20b-it.md) |
| 22 | nemotron-3-nano-30b | **0.4252** | 0.4535 | 100% | 1 | [report](marathon/nemotron-3-nano-30b.md) |
| | **provisional - judged suites not yet run, ranked on Auto-8 alone** | | | | | |
| 23 | gpt-oss-20b | - | 0.5747 | 70% | 1 | [report](marathon/gpt-oss-20b.md) |
| 24 | granite-4-0-h-small | - | 0.4925 | 70% | 1 | [report](marathon/granite-4-0-h-small.md) |
| 25 | lfm2-5-2-6b | - | 0.4751 | 70% | 1 | [report](marathon/lfm2-5-2-6b.md) |
| 26 | eurollm-22b | - | 0.4515 | 70% | 1 | [report](marathon/eurollm-22b.md) |
| 27 | nemotron-3-5-lightning-30b | - | 0.4219 | 70% | 1 | [report](marathon/nemotron-3-5-lightning-30b.md) |
| 28 | apertus-8b | - | 0.3854 | 70% | 1 | [report](marathon/apertus-8b.md) |
| 29 | kimi-linear-48b-bf16 | - | 0.3727 | 70% | 1 | [report](marathon/kimi-linear-48b-bf16.md) |
| 30 | eurollm-9b | - | 0.3653 | 70% | 1 | [report](marathon/eurollm-9b.md) |
| 31 | kimi-vl-a3b-thinking | - | 0.3200 | 70% | 1 | [report](marathon/kimi-vl-a3b-thinking.md) |

Cross-model evidence: [aigrid-evidence-pack.md](marathon/aigrid-evidence-pack.md) (measured
tier-fitment tables) and [telecomgpt-r1-claims-review.md](marathon/telecomgpt-r1-claims-review.md)
(fine-tune claims vs measurements).

## Historical (pre-leaderboard)

[`pre-marathon/`](pre-marathon/) holds reports from before the unified marathon harness -
different hardware, prompts, and scoring; **not comparable** with board numbers:
`Qwen3-30B-A3B-MoE/` (domain Q&A answer sets), `Qwen3-32B/` (notes),
`Seed-36B-performance/` (standalone perf test suite + results).

Suite-scoped historical artifacts stay inside their suites for reproducibility:
[`telcos-last-exam/model-answers/`](../telcos-last-exam/model-answers/) and
[`vendor-genai-tests/historical-results/`](../vendor-genai-tests/historical-results/).
