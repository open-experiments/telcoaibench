# nemotron-3-5-lightning-30b - TelcoAIBench Marathon Report

**HF repo:** `nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16`  
**Serving:** vLLM v0.26.0 (KServe RawDeployment, 1x RTX PRO 6000 Blackwell 96GB) | args: `--max-model-len=32768 --trust-remote-code`  
**Endpoint at test time:** `http://nemotron-3-5-lightning-30b-predictor.gsma-otel2-test.svc.cluster.local:8080`  

## Results

| Suite | Accuracy | StdErr | Samples | Tier | Date |
|---|---|---|---|---|---|
| 3gpp | **0.080** | 0.0273 | 100 | lite | 2026-08-13 |
| 6g_bench | **0.527** | 0.0409 | 150 | lite | 2026-08-13 |
| oranbench | **0.687** | 0.038 | 150 | lite | 2026-08-13 |
| srsranbench | **0.700** | 0.0375 | 150 | lite | 2026-08-13 |
| telelogs | **0.250** | 0.0435 | 100 | lite | 2026-08-13 |
| telemath | **0.490** | 0.0502 | 100 | lite | 2026-08-13 |
| teleqna | **0.442** | 0.0157 | 1000 | lite | 2026-08-13 |
| teletables | **0.200** | 0.0402 | 100 | lite | 2026-08-13 |

## AI Grid tier fit (measured, auto-scored phase)

**Recommended placement: Tier 2 (Provider Edge)** - 31B params, 63GB bf16 moe(3B act), ~2.7s/answer, ~None tokens/answer.


| Axis (AIGrid) | Measured accuracy |
|---|---|
| knowledge | 0.610 |
| protocol | 0.303 |
| math | 0.490 |
| fault | 0.250 |
| structured | 0.200 |

*Fitment from measured accuracy, decode speed, verbosity and VRAM - refreshes after the judged pass.*

---
*Per-sample transcripts (full question/answer/verdict JSONL) are archived on the portal state volume under `benchmark-results/`, one directory per suite run, named by model. Scores flow to the [leaderboard](../../docs/data/LEADERBOARD.md) automatically.*
