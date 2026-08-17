# TelcoAIBench 2026 Track — Design

**Status:** approved 2026-08-16 · auto-scored track delivered (195q frozen, Marathon #02
complete) · exam-2026 delivered (21-model judged marathon) · vendor-genai-2026 frozen, marathon in progress.

## Why

Field feedback on the original suites: outdated in spots and too shallow — strong models
cluster near the top, and coverage misses the domains where operators actually deploy
LLMs today. The 2026 track widens the benchmark in **both dimensions**:

- **Horizontal** — new subject areas: Rel-18/19 & 6G readiness, NTN & private networks,
  network-API exposure (CAMARA/Open Gateway), AIOps & autonomous networks; for the exam,
  new domains IMS & Voice, OSS/BSS, Regulatory Services, AI & Autonomous Ops, NTN, Energy.
- **Vertical** — harder, deeper questions in each area: functional knowhow for
  operational model selection (AI-RAN, AIOps for RAN, Transport, Packet Network, IMS,
  VAS, Regulatory Services, OSS/BSS), never archival trivia.

**GSMA-parity invariant:** the legacy [open-telco](open-telco/) suites remain untouched
and runnable 1:1. The 2026 track is additive, scored on its own board tab
("2026 Test Suite · 6G Within"); the legacy board stays as "Legacy Test Benchmarks".

## Components

### 1. AUTO-SCORED suites (delivered — [open-telco-2026/](open-telco-2026/))

| Suite | Size | Scope |
|---|---|---|
| `rel19_bench` | 52q | Rel-18/19 & 6G-readiness: capability limits, mechanisms, release availability, spec-to-function mapping |
| `ntn_bench` | 45q | NTN (NR-NTN/IoT-NTN, D2D, spectrum, orbits) & private networks (SNPN/PNI-NPN) |
| `netapi_bench` | 38q | CAMARA/Open Gateway mechanics, NEF/CAPIF exposure, ecosystem roles, monetization structure |
| `aiops_bench` | 60q | Autonomy levels, intent management, NWDAF, RIC loops, agentic ops, classification/prediction/scaling |

195 questions total. Question-design rules: functional knowhow only; capability numbers,
mechanisms, release availability, NOT-form, multi-element joins, counterintuitive-correct
scenarios; training-saturated domains get post-cutoff date-stamped precision blocks from
official reports.

### 2. Judged-suite expansions (in progress)

- **`telcos_last_exam` 2026 expansion** — +30 expert questions (30 → 60; 246 → ~506
  points): new domains IMS & Voice, OSS/BSS, Regulatory Services, AI & Autonomous Ops,
  NTN, Energy & Sustainability, plus expert deepeners in the legacy 8 domains. Same
  format: worked reference answer + judge grading notes per question.
- **`vendor_genai` 2026 expansion** — 8 vendors × 6 domains = 48 scenarios: adds
  **Huawei** and **ZTE** to the vendor set, and **Transport/IP** and **Security** to the
  domain set.
- Judge: the portal-provisioned judge model (`gpt-5.6-sol`), one consistent judge per
  published board snapshot.

## Pipeline (every suite)

1. **Draft** — authored from primary sources (3GPP/ETSI/CAMARA/TM Forum/NGMN/O-RAN).
2. **Pilot-screen** on two live models — removes non-discriminating or broken items;
   both-wrong-same-pick triggers a key re-verification against the source.
3. **SME review** — redline rounds; corrections applied verbatim.
4. **Freeze** — two fixed answer-order shuffles (`_A`/`_B`, seeds + SHA-256 in
   `MANIFEST.json`); score = mean of both runs. Measured choice-ordering sensitivity:
   up to ~7 points on a single shuffle — the two-shuffle mean bounds it.
5. **Marathon** — all board models on the identical pinned serving stack, two models at
   a time (one per GPU), JSON-verified serving swaps.
6. **Publish** — board column + per-model [report cards](model-reports/2026-reports/),
   frozen datasets + provenance in the suite folder, one git patch per delivery.

## Board

Two tabs: **Legacy Test Benchmarks** (unchanged composite) and **2026 Test Suite ·
6G Within** (equal-weight mean across the 2026 suites, per-suite columns, origin,
legacy-rank Δ). Data: [`docs/data/marathon02.json`](../docs/data/marathon02.json).
