# Telco's Last Exam

A hardest-questions telecommunications exam: 30 deep questions (10
legacy + 20 v2) spanning 8 domains - RF/RAN, Core & Protocols,
Transport & Fronthaul, Timing & Sync, Security, OAM & Performance,
Cloud-Native, and Economics - across three difficulty tiers
(foundation / advanced / expert), 246 points total. Each question
carries a machine-verified reference answer and judge grading notes
(must-haves, acceptable variations, known error patterns).

Originally a manual exam (models answer, humans grade), it is now also a
**runnable LLM-as-judge benchmark**: the candidate model answers each
question, then a judge model grades the answer against the official
reference key on a 0-10 scale (strict grading: methodology, numerical
results, 3GPP citations, completeness). Scores are reported as a 0-1
average with sample stderr.

## 2026 expansion

The 2026 track adds `telcos_last_exam_2026`: **+30 expert questions, 260 points**
(source of truth: [`exam-2026.md`](exam-2026.md)) — new domains IMS & Voice, OSS/BSS,
Regulatory Services, AI & Autonomous Ops, NTN, Energy & Sustainability, plus expert
deepeners in the legacy domains. The legacy 30-question exam stays frozen 1:1; the full
2026 exam is both tasks combined, points-weighted (506 points total).

### Batch-1 marathon results (judge: gpt-5.6-sol, 2026-08-17)

| # | Model | Points-weighted | Mean/question |
|---|---|---|---|
| 1 | muse-glimmer-30b | **0.6842** | 0.6823 |
| 2 | gemma4-31b-it-base | **0.6808** | 0.6783 |
| 3 | otel2-llm-31b-it | **0.6488** | 0.6440 |
| 4 | qwen3-8-27b | **0.5823** | 0.5797 |
| 5 | qwen3-6-35b-a3b | **0.5778** | 0.5723 |
| 6 | telecomgpt-r1 | **0.5658** | 0.5610 |
| 7 | qwq-32b | **0.5080** | 0.5020 |
| 8 | gpt-oss-120b | **0.5073** | 0.5013 |
| 9 | seed-oss-36b | **0.5006** | 0.4960 |
| 10 | nemotron-3-super-120b | **0.4894** | 0.4840 |

All 10 board models, 30 questions each, zero request/judge errors. Hardest domains across the field: Timing & Sync (0.35), Regulatory Services (0.38); easiest: Energy & Sustainability (0.82), Cloud-Native (0.79). Shown on the 2026 board tab as the `Exam-2026 · judged` column (informational — not in the composite until the judged track completes).

## Layout

```
telcos-last-exam/
├── exam.md                      # legacy 10 questions (kept verbatim)
├── answers.md                   # legacy answer key
├── exam-v2.md                   # v2 source of truth: 20 new questions + answers + grading notes
├── exam-2026.md                 # 2026 expansion source of truth: 30 expert questions (batch 1)
├── datasets/
│   ├── telcos_last_exam.jsonl.gz       # machine-readable exam (question + reference), embedded
│   └── telcos_last_exam_2026.jsonl.gz  # 2026 expansion batch 1 (30 q, 260 pts)
└── model-answers/               # historical per-model answer sheets (manual era)
    ├── chatgpt-5-answers.md
    ├── qwen3-30b-a3b-fp8-answers.md
    └── qwen3-32b-answers.md
```

## How to run

From the portal: open the **Benchmark** tab, select `telcos_last_exam`,
provision a judge with the **Provision judge model** form (endpoint URL +
API key + model name - a frontier-class model such as GPT-5 or Claude
gives the most reliable grading), pick it in the **Judge model** dropdown,
then Run.

From the CLI (same engine):

```bash
cd benchmarks/open-telco
python3 otel_eval.py \
  --endpoint https://<candidate-route>/v1 --model <candidate-name> \
  --tasks telcos_last_exam \
  --judge-endpoint https://api.openai.com/v1 --judge-model gpt-5 \
  --judge-key $OPENAI_API_KEY
```

## Grading notes

The judge sees the question, the reference answer key, and the candidate
answer, and returns structured JSON: a 0-10 score, the list of required
elements the candidate missed, a one-line verdict, and a rationale.
Task scores are points-weighted; runs report per-domain and
per-difficulty breakdowns plus a downloadable per-question failure
report (REPORT.md / REPORT.html). Judge choice matters: a stronger judge is stricter and more
consistent. For comparable numbers across models, always use the same
judge (same model, same revision) and report it alongside the scores.
