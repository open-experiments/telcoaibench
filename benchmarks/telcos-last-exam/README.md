# Telco's Last Exam

A hardest-questions telecommunications exam: 10 deep, multi-part questions
spanning RF link budgets, 3GPP protocol internals, transport, timing, and
system design - each with a detailed reference answer key.

Originally a manual exam (models answer, humans grade), it is now also a
**runnable LLM-as-judge benchmark**: the candidate model answers each
question, then a judge model grades the answer against the official
reference key on a 0-10 scale (strict grading: methodology, numerical
results, 3GPP citations, completeness). Scores are reported as a 0-1
average with sample stderr.

## Layout

```
telcos-last-exam/
├── exam.md                      # the 10 questions (source of truth)
├── answers.md                   # official reference answer key
├── datasets/
│   └── telcos_last_exam.jsonl.gz  # machine-readable exam (question + reference), embedded
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
answer, and must justify its grade before emitting a final `SCORE: n/10`
line. Judge choice matters: a stronger judge is stricter and more
consistent. For comparable numbers across models, always use the same
judge (same model, same revision) and report it alongside the scores.
