# phi-4-mini — 2026 Test Suite Report Card

**Track:** 2026 Test Suite · 6G Within (AUTO-SCORED) · **Origin:** USA · **Legacy Test Benchmark rank:** new

Composite (equal-weight mean of 4 AUTO-SCORED suites, 195 questions, each scored on two frozen answer shuffles): **0.7859** · Exam-2026 judged score (informational): **0.2482**

| Suite | Questions | Shuffle A | Shuffle B | Mean |
|---|---|---|---|---|
| Rel-19-Bench | 52 | 0.7115 | 0.6923 | **0.7019** |
| NTN-Bench | 45 | 0.7778 | 0.8000 | **0.7889** |
| NetAPI-Bench | 38 | 0.7105 | 0.8947 | **0.8026** |
| AIOps-Bench | 60 | 0.8333 | 0.8667 | **0.8500** |
| **Composite (AUTO-SCORED)** | **195** | | | **0.7859** |
| Exam-2026 (judged, 30q/260pts) | 30 | | | 0.2482 |
| Vendor-2026 (judged, 24 cells) | 24 | | | 0.1754 |

## Methodology

Each suite is frozen as two fixed answer-order shuffles (seeds and SHA-256 in the suite [MANIFEST](../../open-telco-2026/datasets/lite/MANIFEST.json)); every model sees identical orderings and the reported score is the mean of the two runs, neutralizing answer-position sensitivity (measured up to ~7 points on a single ordering). Scoring: exact-match `ANSWER: X` extraction, temperature 0.0, max 8192 output tokens, streaming, 6 concurrent connections. Serving: KServe RawDeployment on OpenShift (cluster `venice`, 2× RTX PRO 6000 96GB), the pinned vLLM v0.26.0 CUDA 12.9 image, weights from cluster PVCs.

**Serving note:** 3.8B User-Edge model, MIT license; standard serving on the pinned engine.

## Suite provenance

Question sets are in-house authored functional-knowhow items (capability mechanisms, release availability, spec-to-function mapping, operational scenarios), pilot-screened on two live models and SME-reviewed before freeze. See per-suite provenance docs under [`benchmarks/open-telco-2026/`](../../open-telco-2026/).

*Generated 2026-08-18 · TelcoAIBench 2026 track, batch 1 (Marathon #02)*
