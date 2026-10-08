# JSOSIF investment intelligence demo

The active universe contains these 25 holdings, in portfolio order:

CNQ.TO, CSCO, JPM, BMO.TO, COST, V, JWEL.TO, VRTX, ENB, PFE, CP.TO, ATD.TO, SCHW, ACN, J, XYL, PEP, NTR.TO, DIS, MG.TO, OTEX.TO, GIS, NVO, MC.PA, AMTM.

`scripts/universe.py` is the shared pipeline universe. All ticker scripts default to CNQ.TO. Exchange suffixes are preserved in filenames and data requests.

The root `*-ai-prompt.txt` files are templates with empty headline lists; add sourced headlines before using them. No news, prices, or reports have been fabricated or fetched for the new holdings. Existing data, reports, and verification fixtures are historical artifacts of the previous universe.

## Run

```bash
pip install -r requirements.txt
python3 scripts/run_phase1.py
python3 scripts/validate_phase1.py
python3 build-mockup.py
```

The pipeline writes per-ticker snapshots to `data/` and reports to `reports/`. It reuses `data/fred.json`; macro refresh is optional. AI extraction requires a configured Gemini CLI (`GEMINI_CLI`). SEC issuer mappings are resolved from the SEC ticker directory; unavailable mappings are recorded as N/A. Sector peer lists in `scripts/comparables.py` are empty pending configuration. International listings never use the US Stooq fallback.

Open `docs/index.html` or `docs/intelligence-mockup.html` for the 25-holding dashboard. New holdings initially show unavailable data. Run `build-mockup.py` after refreshing snapshots to update both pages.

## Offline checks

```bash
cd scripts
python3 -m unittest -v test_ai_extract test_data_utils test_rule_opt_v2
```

Free source coverage is not guaranteed. AI items need human review. This demo is not investment advice.
