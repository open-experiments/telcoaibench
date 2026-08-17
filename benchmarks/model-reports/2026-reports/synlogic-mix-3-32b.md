# synlogic-mix-3-32b — 2026 Test Suite Report Card

**Track:** 2026 Test Suite · 6G Within (AUTO-SCORED) · **Origin:** China · **Legacy Test Benchmark rank:** #None

Composite (equal-weight mean of 4 AUTO-SCORED suites, 195 questions, each scored on two frozen answer shuffles): **0.8692** · Exam-2026 judged score (informational): **0.4468**

| Suite | Questions | Shuffle A | Shuffle B | Mean |
|---|---|---|---|---|
| Rel-19-Bench | 52 | 0.8269 | 0.7885 | **0.8077** |
| NTN-Bench | 45 | 0.8889 | 0.8222 | **0.8556** |
| NetAPI-Bench | 38 | 0.8421 | 0.8684 | **0.8553** |
| AIOps-Bench | 60 | 0.9500 | 0.9667 | **0.9583** |
| **Composite (AUTO-SCORED)** | **195** | | | **0.8692** |
| Exam-2026 (judged, 30q/260pts) | 30 | | | 0.4468 |

## Methodology

Each suite is frozen as two fixed answer-order shuffles (seeds and SHA-256 in the suite [MANIFEST](../../open-telco-2026/datasets/lite/MANIFEST.json)); every model sees identical orderings and the reported score is the mean of the two runs, neutralizing answer-position sensitivity (measured up to ~7 points on a single ordering). Scoring: exact-match `ANSWER: X` extraction, temperature 0.0, max 8192 output tokens, streaming, 6 concurrent connections. Serving: KServe RawDeployment on OpenShift (cluster `venice`, 2× RTX PRO 6000 96GB), the pinned vLLM v0.26.0 CUDA 12.9 image, weights from cluster PVCs.

**Serving note:** RL reasoning-tuned; at temp 0 answers ultra-tersely (~5 tokens) on MCQ.

## Suite provenance

Question sets are in-house authored functional-knowhow items (capability mechanisms, release availability, spec-to-function mapping, operational scenarios), pilot-screened on two live models and SME-reviewed before freeze. See per-suite provenance docs under [`benchmarks/open-telco-2026/`](../../open-telco-2026/).

*Generated 2026-08-17 · TelcoAIBench 2026 track, batch 1 (Marathon #02)*
