# TelcoAIBench 2026 Track

In-house AUTO-SCORED suites widening the benchmark beyond the frozen
[GSMA-parity suites](../open-telco/) - see the [track design](../2026-track-design.md).
The GSMA-parity suites remain untouched and runnable 1:1; this track is scored on its
own board (Marathon #02 onward, "2026 Functional Track" tab on the site).

## Suites

| Suite | Status | Scope |
|---|---|---|
| `rel19_bench` | **batch 1 frozen 2026-08-16** (52 q) | Rel-18/19 & 6G-readiness functional knowhow: capability limits, mechanisms, release availability, spec-to-function mapping, operational scenarios |
| `ntn_bench` | planned | NTN & private networks |
| `netapi_bench` | planned | Network APIs & monetization (CAMARA/TMF) |
| `aiops_bench` | planned | AI-RAN & autonomous operations |

## Method

- Questions authored from primary 3GPP/ETSI sources (portal records, TS/TR, official
  feature articles), SME-reviewed in three redline rounds, and **pilot-screened against
  live models** to remove non-discriminating items. Design rule: functional knowhow for
  operational model selection (AI-RAN, AIOps, Transport, Packet, IMS, VAS, Regulatory,
  OSS/BSS) - no archival trivia.
- **Two fixed answer orderings** (`_A`/`_B` files, seeds in `MANIFEST.json`); a model's
  score is the mean of both runs. This bounds LLM choice-ordering sensitivity, which we
  measured at up to ~7 points on a single shuffle.
- Scoring: same parity-validated MCQ parser as open-telco (`ANSWER: X`), greedy, temp 0.
- Per-question provenance (source + rationale) in `rel19-bench-batch1-provenance.md`.

## Running

```bash
cd ../open-telco
# copy a frozen shuffle over the dataset name, then:
python3 otel_eval.py --endpoint https://<route>/v1 --model <name> --tasks rel19_bench --tier lite
```
(Harness task registration for the 2026 suites lands with the next portal update.)
