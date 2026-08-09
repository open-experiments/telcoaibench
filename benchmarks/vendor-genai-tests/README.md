# Vendor GenAI Tests

Deep-dive vendor-technology questions (Ericsson, Nokia, Mavenir) probing
whether a model can reason about real vendor architectures - components,
interfaces, dimensioning - without inventing product names, versions, or
metrics.

Originally manual prompt-based tests with hand-graded results, now also a
**runnable LLM-as-judge benchmark**: the candidate model answers each
vendor question and a judge model grades against a fixed rubric (technical
accuracy, completeness, depth, honesty about what is not public), emitting
a 0-10 score per answer. Scores are reported as a 0-1 average with sample
stderr.

## Layout

```
vendor-genai-tests/
├── datasets/
│   └── vendor_genai.jsonl.gz    # machine-readable question set, embedded
├── source-tests/                # original question sheets
│   ├── Ericsson-GenAI-Test.txt
│   ├── Nokia-GenAI-Test.txt
│   └── Mavenir-GenAI-Test.txt
├── historical-results/          # hand-graded runs from the manual era
│   ├── Ericsson-GenAI-Test-Result.md
│   ├── Nokia-GenAI-Test-Result.md
│   ├── Mavenir-GenAI-Test-Result.md
│   └── report_1_qwen3_q*.md     # per-question Qwen3 answer reports
└── reference/                   # background material
    ├── benchmark_detailed_description.md
    ├── Telco5G-GenAI-BenchM-01.pdf
    └── Telco5G-GenAI-BenchM-02.pdf
```

## How to run

From the portal: open the **Benchmark** tab, select `vendor_genai`,
provision a judge with the **Provision judge model** form (endpoint URL +
API key + model name - a frontier-class judge gives the most reliable
rubric grading), pick it in the **Judge model** dropdown, then Run.

From the CLI (same engine):

```bash
cd benchmarks/open-telco
python3 otel_eval.py \
  --endpoint https://<candidate-route>/v1 --model <candidate-name> \
  --tasks vendor_genai \
  --judge-endpoint https://api.openai.com/v1 --judge-model gpt-5 \
  --judge-key $OPENAI_API_KEY
```

## Grading notes

There is no single reference answer; the rubric rewards models that
separate publicly known facts from what would require vendor engagement
and abstain rather than fabricate. Use the same judge (model + revision)
across candidates and report it with the scores.
