# jsosif-ai-pipeline-demo

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/Geochelone666/jsosif-ai-pipeline-demo)

A working demo of a dual-pipeline investment intelligence setup: **quant metrics + AI research**, merged into one report per ticker. Built to answer one question for the JSOSIF tech team: *can we automate the repetitive data-gathering that sector teams do every week?*

This is a prototype to validate the architecture, not a production system. If the team agrees on the direction, it gets rebuilt properly with a real intelligence database and broader asset coverage.

## Try it in one click

No local setup needed — open it in GitHub Codespaces and everything (Python 3.12 + dependencies) is preinstalled:

1. Click **Code → Codespaces → Create codespace** (or the badge above).
2. Wait for the container to build, then run:
   ```bash
   REPORT_AS_OF=2026-10-05 python3 scripts/validate_phase1.py
   ```
   This offline check validates the committed snapshots: all six reports contain the required sections and their numbers match the ticker JSON data.
3. Open `reports/NVDA-intelligence-20261005.md` to see a finished intelligence report.

## How it works

Two branches feed into one report. First branch: market data comes from yfinance and goes through Python quant metrics. Second branch: news RSS goes to Gemini, which extracts and classifies items into tailwinds, headwinds, catalysts, and risks. Both branches merge into a single `{TICKER}-intelligence-*.md` report.

- **Quant**: 1D/1W/1M/YTD/1Y returns, annualized volatility, beta vs SPY, max drawdown, Sharpe, P/E, P/B, EV/EBITDA, revenue growth, MA50/MA200, RSI(14), MACD. Cross-checked against raw CSV with independent recomputation.
- **AI research**: Google News RSS (25 headlines) → Gemini structured extraction into tailwinds / headwinds / catalysts / risks, each with an English summary, date, impact, horizon, and confidence. Headlines link back to their RSS source URLs. Clear headlines are classified locally by rules; only ambiguous ones go to the model.
- **Free sources only**: yfinance, Google News RSS, SEC EDGAR, FRED (optional key). No paid APIs.

## Repo layout

```
├── README.md               # this file
├── INDEX.md                # report links and per-ticker summaries (start here)
├── requirements.txt
├── .devcontainer/          # GitHub Codespaces config
├── scripts/                # pipeline code
│   ├── quant.py            # market data + metrics → data/{ticker}-quant.json
│   ├── ai_extract.py       # RSS fetch + Gemini extraction → data/{ticker}-ai-intel.json
│   ├── comparables.py / earnings.py / fred.py / edgar.py
│   ├── regenerate_report.py# assembles the Markdown report
│   ├── run_phase1.py       # runs all six tickers in sequence
│   ├── validate_phase1.py  # offline validation of reports vs snapshots
│   └── data_utils.py       # shared paths + JSON helpers
├── data/                   # committed pipeline outputs (per-ticker JSON + CSVs)
├── reports/                # finished intelligence reports (*-intelligence-*.md)
├── docs/                   # dashboard mockup, screenshots, team docs
└── verification/           # extraction-method experiments and results
```

## Run it

```bash
pip install -r requirements.txt
python3 scripts/fred.py  # once, or reuse the existing data/fred.json snapshot
for ticker in NVDA MSFT AAPL GOOGL AMZN TSLA; do
    python3 scripts/quant.py --ticker "$ticker"
    python3 scripts/ai_extract.py --ticker "$ticker"
    python3 scripts/comparables.py --ticker "$ticker"
    python3 scripts/earnings.py --ticker "$ticker"
    python3 scripts/edgar.py --ticker "$ticker"
    python3 scripts/regenerate_report.py --ticker "$ticker"
done
```

All six ticker scripts default to NVDA when `--ticker` is omitted. Outputs land in `data/` (lowercase ticker JSON files, e.g. `data/msft-quant.json`) and reports in `reports/` (uppercase names, e.g. `reports/MSFT-intelligence-20261005.md`). Shared macro data stays in `data/fred.json`. AI calls are spaced at least 20 seconds apart; failed requests retry once after 90 seconds, then the AI sections show N/A.

AI extraction requires the Gemini CLI configured at the absolute `CLI` path in `scripts/ai_extract.py`; set `GEMINI_CLI` to override it for your environment. Report generation reuses local JSON snapshots and does not fetch data.

## Validate local reports

After generating the reports, or directly against the committed snapshots, run:

```bash
REPORT_AS_OF=2026-10-05 python3 scripts/validate_phase1.py
```

This offline check uses only the Python standard library. It checks that all six reports contain the required sections and that their quantitative table values match the ticker JSON snapshots at the expected precision. When GOOGL verification data is available, it also independently recomputes the 1Y return from `data/GOOGL-yfinance.csv`; otherwise that check is recorded as unavailable.

A successful run rewrites `INDEX.md` with report links and summaries and `data/phase1-validation.json` with the results. Missing files or failed assertions stop the script with a nonzero exit status.

## Six-asset dashboard

Open [`docs/index.html`](docs/index.html) in a browser for the six-asset dashboard covering NVDA, MSFT, AAPL, GOOGL, AMZN and TSLA. The page uses an embedded data snapshot. Rerunning the pipeline does not automatically refresh it; regenerate or update the embedded snapshot in `docs/index.html` to see new data on the dashboard.

## Intelligence page prototype

A static mockup of the future dashboard Intelligence page (open `docs/intelligence-mockup.html` in a browser). The mockup currently shows NVDA, MSFT and AAPL; all six ticker reports are in [`reports/`](reports/).

![Intelligence page prototype](docs/intelligence-nvda-desktop.png)

## Limitations

- Supports NVDA, MSFT, AAPL, GOOGL, AMZN and TSLA. Latest market refresh: 2026-10-05 (intraday); see [INDEX.md](INDEX.md). News and other non-market sections retain their existing snapshots.
- `REPORT_AS_OF=2026-10-05` selects the market cutoff and report date for `scripts/quant.py`, `scripts/regenerate_report.py` and `scripts/validate_phase1.py`.
- Free-tier data: delayed quotes, RSS coverage not guaranteed, AI items need human review.
- Free-tier Gemini grounding (`google_search` tool) returned 429 in the original run — the demo works around it with RSS + plain-text extraction.
- Not investment advice.

## Rule-first extraction

`scripts/ai_extract.py` classifies clear headlines locally and sends only ambiguous headlines to the Flash-Lite CLI. RSS metadata remains authoritative. Existing report fields are retained; additive `extraction_method` values are `rule`, `ai`, or `unknown`. Unresolved items are retained in `unclassified`, with counts in `extraction_stats`. Rule summaries copy the headline; impact and horizon use conservative defaults.

Run the unit tests from `scripts/`:

```bash
cd scripts && python3 -m unittest -v test_ai_extract test_data_utils test_rule_opt_v2
```

See [verification results](../verification/rule-first/RESULTS.md). Current fixture rule coverage is 27.9%, below the 70% goal; historical AI category agreement is not ground-truth accuracy.
