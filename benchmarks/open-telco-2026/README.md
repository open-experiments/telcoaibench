# TelcoAIBench 2026 Track

In-house AUTO-SCORED suites widening the benchmark beyond the frozen
[GSMA-parity suites](../open-telco/) - see the [track design](../2026-track-design.md).
The GSMA-parity suites remain untouched and runnable 1:1; this track is scored on its
own board (Marathon #02 onward, "2026 Functional Track" tab on the site).

## Suites

| Suite | Status | Scope |
|---|---|---|
| `rel19_bench` | **batch 1 frozen 2026-08-16** (52 q) | Rel-18/19 & 6G-readiness functional knowhow: capability limits, mechanisms, release availability, spec-to-function mapping, operational scenarios |
| `ntn_bench` | **batch 1 frozen 2026-08-16** (45 q) | NTN (NR-NTN/IoT-NTN, D2D, spectrum, orbits) & private networks (SNPN/PNI-NPN, CAG, onboarding, deployment models) |
| `netapi_bench` | **batch 1 frozen 2026-08-16** (38 q) | CAMARA/Open Gateway API mechanics, NEF/CAPIF exposure architecture, ecosystem roles (CAMARA/GSMA/TMF), monetization structure, incl. a post-cutoff 1Q26-report precision block |
| `aiops_bench` | **batch 1 frozen 2026-08-17** (60 q) | AIOps & autonomous networks: autonomy levels (human-participation basis, scenario-scoped L4), intent management, NWDAF, RIC control loops, AI-RAN taxonomy, agentic operations, classification/prediction/dynamic-scaling tasks, incl. a post-cutoff 2026-state precision block (TM Forum survey, NGMN Agentic AI publication) |

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
- Per-question provenance (source + rationale) in the per-suite `*-batch1-provenance.md` docs.

## Running

```bash
cd ../open-telco
# copy a frozen shuffle over the dataset name, then:
python3 otel_eval.py --endpoint https://<route>/v1 --model <name> --tasks rel19_bench --tier lite
```
(Harness task registration for the 2026 suites lands with the next portal update.)
