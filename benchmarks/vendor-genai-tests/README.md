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

## 2026 expansion

The 2026 track adds `vendor_genai_2026`: **24 new matrix cells** completing an
**8-vendor x 6-domain grid** (48 cells with the legacy 24, kept 1:1) — **Huawei** and
**ZTE** across all six domains, and the six legacy vendors across the two new domains
(**Transport/IP**, **Security**). Same 5-part structure, judge anchors, fabrication
baits and rubric weights; five honesty traps (M-E, S-E, R-E, S-F, R-F) reward stating
that a vendor does not play in a domain. Source of truth:
[`vendor-genai-2026.md`](vendor-genai-2026.md).

### 2026-expansion marathon results (judge: gpt-5.6-sol, 2026-08-18)

| # | Model | Score |
|---|---|---|
| 1 | gemma4-31b-it-base | **0.4279** |
| 2 | muse-glimmer-30b | **0.4208** |
| 3 | otel2-llm-31b-it | **0.3325** |
| 4 | synlogic-mix-3-32b | **0.3160** |
| 5 | nemotron-3-5-lightning-30b | **0.3088** |
| 6 | llama31-nemotron-70b | **0.2944** |
| 7 | nemotron-3-super-120b | **0.2919** |
| 8 | qwen3-8-27b | **0.2875** |
| 9 | falcon-h1-34b | **0.2796** |
| 10 | qwen3-6-35b-a3b | **0.2750** |
| 11 | qwq-32b | **0.2660** |
| 12 | telecomgpt-r1 | **0.2656** |
| 13 | mistral-small-3-2-24b | **0.2652** |
| 14 | seed-oss-36b | **0.2548** |
| 15 | qwen3-5-9b-base | **0.2454** |
| 16 | gpt-oss-120b | **0.2354** |
| 17 | glm-4-7-flash | **0.2194** |
| 18 | nemotron-cascade-2-30b | **0.2135** |
| 19 | lfm2-5-8b-a1b | **0.2060** |
| 20 | lfm2-5-vl-3b | **0.1996** |
| 21 | lfm2-5-2-6b-base | **0.1550** |

All 21 board models, 24 cells each, zero judge errors. The honesty-weighted rubric compresses scores hard: no model exceeds 0.43 - fabricated product names and invented market claims dominate the losses, and the five honesty traps reward the rare model that states a vendor does not play in a domain.

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
