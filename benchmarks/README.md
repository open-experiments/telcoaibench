# TelcoAIBench Benchmark Suites

All benchmark and evaluation assets of TelcoAIBench live here,
organized by suite. Every suite is self-contained - datasets and scoring
included - so results remain reproducible with nothing but this repository.

| Suite | What it is | How to run |
|---|---|---|
| [`open-telco/`](open-telco/) | **Self-contained Open-Telco eval framework** - the 8 GSMA telecom benchmarks (TeleQnA, TeleTables, TeleMath, TeleLogs, 3GPP-TSG, ORANBench, srsRANBench, 6G-Bench) with lite + full datasets embedded (gzipped JSONL) and a single-file runner. Parity-validated against the official Inspect AI harness (≤1pp on all 7 leaderboard tasks). Includes the 2026-08 leaderboard verification report and claim snapshots. | `cd open-telco && python3 otel_eval.py --endpoint https://<route>/v1 --model <name>` - or use the portal's **Benchmark** tab |
| [`vendor-genai-tests/`](vendor-genai-tests/) | Vendor GenAI deep-dives (Ericsson, Nokia, Mavenir) - **LLM-as-judge benchmark**: rubric-graded (accuracy, completeness, depth, honesty). Embedded dataset plus the original question sheets, hand-graded historical results, and Telco5G reference PDFs. | Portal Benchmark tab (`vendor_genai` + a judge model) or CLI with `--judge-endpoint/--judge-model`; see [README](vendor-genai-tests/README.md) |
| [`telcos-last-exam/`](telcos-last-exam/) | "Telco's Last Exam" - 10 hardest-questions telecom exam with an official answer key - **LLM-as-judge benchmark**: graded 0-10 against the reference key. Embedded dataset plus historical per-model answer sheets. | Portal Benchmark tab (`telcos_last_exam` + a judge model) or CLI with `--judge-endpoint/--judge-model`; see [README](telcos-last-exam/README.md) |
| [`model-reports/`](model-reports/) | Per-model benchmark answer sets and performance reports gathered on this lab (Qwen3-32B, Qwen3-30B-A3B-MoE, Seed-36B perf suite). | See each model's folder |
| [`embeddings/`](embeddings/) | Embeddings model benchmark notes. | See `benchmark.md` |

## Quick start (Open-Telco suite)

```bash
cd open-telco
pip install requests   # only dependency
python3 otel_eval.py --endpoint https://<your-model-route>/v1 --model <served-name>
# lab clusters with self-signed certs: add --insecure (or --ca-bundle <pem>)
```

Or interactively: open the portal's **Benchmark** tab → pick
benchmarks → Run. Live per-task progress and accuracies stream into the UI.

## Judged suites (LLM-as-judge)

`telcos_last_exam` and `vendor_genai` have no deterministic answer scorer -
a **judge model** grades each candidate answer (against the official answer
key, or against a fixed rubric) and emits `SCORE: n/10`. Provision any
OpenAI-compatible endpoint as the judge - a frontier-class model (e.g.
GPT-5, Claude) via an API-key-backed endpoint is recommended for grading
quality. In the portal, provision the judge endpoint like any other target,
then select it in the **Judge model** dropdown. On the CLI, pass
`--judge-endpoint`, `--judge-model`, and `--judge-key`. Always report which
judge was used; scores from different judges are not comparable.

## Reporting discipline

When publishing results from any suite, always record: model **revision hash**,
serving stack + version (e.g. vLLM v0.26.0), quantization/precision,
temperature, dataset tier and sample counts, and the run date. The
`open-telco/reference/` folder shows why: a leaderboard score without a pinned
revision cannot be verified (see the verification report there).
