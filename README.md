# TelcoAIBench — Telco AI Portal & Benchmark Suite

**🎥 Demo Video**: [Watch on YouTube](https://youtu.be/UQB1T-ThQBk) · **📖 Article**: [Read on Medium](https://medium.com/open-5g-hypercore/episode-xxix-the-prompt-engineering-how-to-make-a-toddler-act-talk-nice-83e9aab2e3b9)

**TelcoAIBench** is a GenAI workbench for telecom professionals: a **web portal** for expert AI
conversations, embeddings, and live model observability — plus a fully
**self-contained telco benchmark suite** that measures any model you plug in,
from the CLI or straight from the portal UI.

Everything runs against **any OpenAI-compatible endpoint** (vLLM,
RHOAI/KServe, TGI, SaaS). Point it at your model with two environment
variables and you have a chat portal, a metrics dashboard, and a
leaderboard-grade eval harness — no source edits, no external data
dependencies.

---

## The Portal, Tab by Tab

### 💬 Chat — expert telco conversations

![Chat tab](images/tab-chat.png)

Multi-persona chat with telecom-specialized system prompts (Telco Expert,
Network Expert, Cloud/Storage Experts, intent classification, or your own).
Persistent sessions survive browser refreshes and can be shared by ID.
Auto-streaming kicks in for large contexts; temperature, token limits, and
prompt overrides adjust live. File upload (txt/md/csv/json/py/pdf) feeds
documents into the conversation.

### 📝 Prompt Manager — persona engineering

![Prompt Manager tab](images/tab-prompts.png)

Create, edit, and persist system-prompt personas (`system_prompts.json`)
without touching code — load an existing persona, refine it, save, and it is
immediately available in the Chat tab.

### 🧬 Embeddings Generation

![Embeddings tab](images/tab-embeddings.png)

Generate embeddings against a configured embeddings endpoint and experiment
with in-memory semantic search over your own text.

### 📊 Observability — live vLLM metrics

![Observability tab](images/tab-observability.png)

A dual-API dashboard polling the model server's `/metrics`: request rates and
latency, token throughput, GPU cache utilization, health status, efficiency
analysis, and diagnostics for both the chat and embeddings endpoints —
with Plotly visualizations and configurable collection intervals.

### 🏆 Benchmark — leaderboard-grade evals, one click

![Benchmark tab running](images/tab-benchmark-live.png)

Select any subset of the **8 embedded Open-Telco benchmarks** — TeleQnA,
TeleTables, TeleMath, TeleLogs, 3GPP-TSG, ORANBench, srsRANBench, 6G-Bench —
pick the dataset tier (lite = leaderboard default, or full), sample limit,
parallelism, and token cap, and watch results stream in live: per-task
progress and running accuracy update every ~2 seconds.

![Benchmark tab complete](images/tab-benchmark-done.png)

When the run completes you get accuracy ± stderr per benchmark, the overall
average, the exact model/endpoint/configuration used, and per-sample
transcripts for auditing. The same engine is scriptable from the CLI (below).

---

## Quick Start

### 1. Serve a model

Any OpenAI-compatible server works. Example with vLLM:

```bash
vllm serve <your-model> --port 8080
```

### 2. Point the portal at it (env vars — no source edits)

```bash
pip install 'gradio>=5,<6' && pip install -r requirements-v2.txt

export SME_API_ENDPOINT="https://my-model-route.apps.mylab"   # base URL, no /v1
export SME_MODEL_NAME="my-served-model-name"
export SME_USE_TOKEN_AUTH="false"      # or true + SME_API_TOKEN="..."
export SME_TLS_VERIFY="false"          # lab clusters with self-signed certs

python sme-web-ui-v2.py                # portal on :30180, login admin/minad
```

All settings: `SME_API_ENDPOINT`, `SME_MODEL_NAME`, `SME_API_TOKEN`,
`SME_USE_TOKEN_AUTH`, `SME_TLS_VERIFY`, `SME_ADMIN_USERNAME`,
`SME_ADMIN_PASSWORD`, and embeddings equivalents
(`SME_EMBEDDINGS_ENDPOINT` / `SME_EMBEDDINGS_MODEL` / `SME_EMBEDDINGS_TOKEN`).
Anything unset falls back to the `Config` defaults in `sme-web-ui-v2.py`.

### 3. (Optional) Deploy on Kubernetes / OpenShift

The portal is a single Python process — a minimal Deployment that clones this
repo, pip-installs, and sets the `SME_*` env vars is all it takes; add a
Service + Route/Ingress on port 30180. The Benchmark tab works out of the box
since the datasets ship inside the repo.

---

## Benchmarks & Evals

All benchmark assets are consolidated under [`benchmarks/`](benchmarks/README.md):

| Suite | What it is |
|---|---|
| [`benchmarks/open-telco/`](benchmarks/open-telco/) | **Self-contained Open-Telco eval framework** — 8 GSMA telecom benchmarks with lite + full datasets embedded (gzipped JSONL, ~4.5MB) and a single-file runner (stdlib + `requests`). Scoring parity-validated against the official Inspect AI harness (≤1pp on all 7 leaderboard tasks). Includes the 2026-08 leaderboard verification report, claim snapshots, and reference results. |
| [`benchmarks/vendor-genai-tests/`](benchmarks/vendor-genai-tests/) | Original vendor GenAI test sets (Ericsson / Nokia / Mavenir) with graded results + Telco5G benchmark reports. |
| [`benchmarks/telcos-last-exam/`](benchmarks/telcos-last-exam/) | Hardest-questions telco exam with per-model answer sheets. |
| [`benchmarks/model-reports/`](benchmarks/model-reports/) | Per-model benchmark answers and performance reports collected on this lab. |
| [`benchmarks/embeddings/`](benchmarks/embeddings/) | Embeddings model benchmark notes. |

Run from the CLI (identical engine to the portal tab):

```bash
cd benchmarks/open-telco
python3 otel_eval.py --endpoint https://<model-route>/v1 --model <name>
# self-signed lab certs: add --insecure   ·   full datasets: --tier full
```

**Reproducibility discipline**: always record the model revision hash, serving
stack + version, precision, temperature, dataset tier, and date with any
published number — the verification report in
`benchmarks/open-telco/reference/` documents exactly why.

---

## Repository Layout

```
telcoaibench/
├── sme-web-ui-v2.py        # The portal (Gradio) — all tabs incl. 🏆 Benchmark
├── system_prompts.json     # Expert persona definitions
├── requirements-v2.txt     # Python dependencies (pin gradio <6)
├── benchmarks/             # All benchmark & eval assets (see benchmarks/README.md)
│   ├── open-telco/         #   embedded eval framework: runner + datasets + reports
│   ├── vendor-genai-tests/ #   Ericsson / Nokia / Mavenir + Telco5G
│   ├── telcos-last-exam/   #   telco exam + per-model answers
│   ├── model-reports/      #   per-model results & perf reports
│   └── embeddings/         #   embeddings benchmark
├── archive/                # Legacy v1 application
├── images/                 # Screenshots (this README) & docs imagery
└── README.md
```

## Architecture Notes

Single-file app (`sme-web-ui-v2.py`) with clean separations:

- **Config** — env-var-driven connection settings (pluggable endpoint)
- **ChatClient** — OpenAI-compatible HTTP client with smart streaming,
  retries, and timeout handling
- **SessionManager** — file-backed persistent sessions (24h retention)
- **MetricsCollector** — `/metrics` polling, archival, and Plotly dashboards
- **ChatInterface** — the Gradio UI, including the Benchmark tab which
  imports `benchmarks/open-telco/otel_eval.py` directly (streaming transport,
  8k default token cap, per-sample transcripts)

Benchmark engine design highlights: SSE streaming by default (survives
proxy/router idle timeouts on long generations), deterministic scoring ported
1:1 from the official harness, zero network dependencies for datasets.

---

*TelcoAIBench graduated from the `telco-sme` experiment in
[Telco-AIX](https://github.com/open-experiments/Telco-AIX), where its full
development history lives. Contributions welcome.*
