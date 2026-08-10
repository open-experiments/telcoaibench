# Vendor GenAI Tests

Deep-dive vendor-technology questions - a 6-vendor x 4-domain matrix
(24 questions): Ericsson, Nokia, Mavenir, Samsung Networks, Rakuten
Symphony, and Cisco, each across RAN, Core, OSS/AI, and Cloud-native.
Every question follows the same 5-part structure and carries judge
anchors (durable public facts used as grading context) plus known
fabrication-bait patterns. Three questions are deliberate honesty
traps that reward models for saying a vendor does not play in a
domain.

Originally manual prompt-based tests with hand-graded results, now also a
**runnable LLM-as-judge benchmark**: the candidate model answers each
vendor question and a judge model returns structured JSON with four 0-10
criteria - technical_accuracy, completeness, depth, honesty - weighted
0.40/0.20/0.15/0.25 into the overall score so confident fabrication is
punished hardest. Runs report per-vendor, per-domain and per-criterion
breakdowns plus a downloadable per-question failure report.

## Layout

```
vendor-genai-tests/
├── vendor-genai-v2.md           # v2 source of truth: matrix, anchors, rubric
├── datasets/
│   └── vendor_genai.jsonl.gz    # 24 records: question + judge_anchors + fabrication_bait
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
