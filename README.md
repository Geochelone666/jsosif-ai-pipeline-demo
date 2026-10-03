# jsosif-ai-pipeline-demo

A single-asset demo of a dual-pipeline investment intelligence setup: **quant metrics + AI research**, merged into one report.

Built for [JSOSIF](https://www.uwindsor.ca) (John Simpson Odette Student Investment Fund) dev team discussion. This is a prototype to validate the architecture, not a production system.

## How it works

```
Market APIs (yfinance) ──→ Python metrics ──┐
                                            ├─→ NVDA-intelligence-*.md
News RSS ──→ Gemini extract / classify ─────┘
```

- **Quant**: 1D/1W/1M/YTD/1Y returns, annualized volatility, beta vs SPY, max drawdown, Sharpe, P/E, P/B, EV/EBITDA, revenue growth, MA50/MA200, RSI(14), MACD. Cross-checked against raw CSV with independent recomputation.
- **AI research**: Google News RSS (25 headlines) → Gemini structured extraction into tailwinds / headwinds / catalysts / risks, each with date, impact, horizon, confidence, and source URLs.
- **Free sources only**: yfinance, Google News RSS, SEC EDGAR, FRED (optional key). No paid APIs.

## Repo contents

| File | What |
|---|---|
| `NVDA-intelligence-20261003.md` | The generated demo report (start here) |
| `quant.py` | Market data + metrics → `quant.json` |
| `ai_extract.py` | RSS fetch + Gemini extraction → `ai-intel.json` |
| `comparables.py` / `earnings.py` / `fred.py` / `edgar.py` | Peer comps, earnings calendar, macro (FRED), latest SEC filing |
| `regenerate_report.py` | Assembles the Markdown report |

## Run it

```bash
python3 quant.py        # quant metrics
python3 ai_extract.py   # AI extraction (needs Gemini API key via env)
python3 regenerate_report.py
```

## Limitations

- Single asset (NVDA), one-off local run.
- Free-tier data: delayed quotes, RSS coverage not guaranteed, AI items need human review.
- Free-tier Gemini grounding (`google_search` tool) returns 429 — the demo works around it with RSS + plain-text extraction.
- Not investment advice.

## Status

Prototype for architecture discussion. If the team agrees on the direction, this gets rebuilt properly with a real intelligence database and multi-asset support.
