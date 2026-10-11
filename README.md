# JSOSIF investment intelligence demo

The active universe contains these 25 holdings, in portfolio order:

CNQ.TO, CSCO, JPM, BMO.TO, COST, V, JWEL.TO, VRTX, ENB, PFE, CP.TO, ATD.TO, SCHW, ACN, J, XYL, PEP, NTR.TO, DIS, MG.TO, OTEX.TO, GIS, NVO, MC.PA, AMTM.

`scripts/universe.py` is the shared pipeline universe. All ticker scripts default to CNQ.TO. Exchange suffixes are preserved in filenames and data requests.

The `prompts/` directory contains the 25 `*-ai-prompt.txt` templates with empty headline lists; add sourced headlines before using them. No news, prices, or reports have been fabricated or fetched for the new holdings. Existing data, reports, and verification fixtures are historical artifacts of the previous universe.

## Run

```bash
pip install -r requirements.txt
python3 scripts/run_phase1.py
python3 scripts/validate_phase1.py
```

The pipeline writes per-ticker snapshots to `data/` and reports to `reports/`. It reuses `data/fred.json`; macro refresh is optional. AI extraction requires a configured Gemini CLI (`GEMINI_CLI`). SEC issuer mappings are resolved from the SEC ticker directory; unavailable mappings are recorded as N/A. Sector peer lists in `scripts/comparables.py` are empty pending configuration. International listings never use the US Stooq fallback.

Open `docs/index.html` or `docs/intelligence-mockup.html` for the 25-holding dashboard.

## Offline checks

```bash
cd scripts
python3 -m unittest -v test_ai_extract test_data_utils test_rule_opt_v2
```

Free source coverage is not guaranteed. AI items need human review. This demo is not investment advice.

Run the full offline pytest suite (including archived verification tests) from the repo root with `PYTHONPATH=scripts .venv/bin/python -m pytest --import-mode=importlib -q`; importlib mode avoids duplicate archived test-module names.

## Explicit assumptions (registry v1)

`scripts/assumptions.py` records statements, rationale, and optional predicates: `prices-adjusted-close` (provider adjustments may be revised), `prices-lookback-start` (fixed 2025-10-02, not rolling), `stooq-us-only` (dot denotes international), `prices-normalized-index` (naive midnight), `prices-trading-calendar` (no gap detection), `prices-currency-usd` (no currency verification), `prices-minimum-history`, `phase1-artifacts-exist`, `fred-shared-freshness` (shared snapshot, no age bound), `supported-ticker`, and `report-as-of-date` (real YYYY-MM-DD, not future).

The minimum is one usable positive finite ticker close; short histories retain existing N/A metrics and an unavailable SPY still yields N/A beta. Empty ticker histories and missing required report artifacts exit 2 with a human-readable violation. `check_all(context)` returns check results or raises `AssumptionViolation` carrying all results in `.results`; absent evidence is `uncheckable`, never `ok`. Quant JSON and report metadata sidecars (`reports/<TICKER>-intelligence-<DATE>.json`) record `assumptions_version` and `assumptions_checked`, including failures. Artifact existence does not validate contents or freshness; report preflight runs before Markdown is written.
