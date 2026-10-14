# JSOSIF investment intelligence demo

Pipeline that builds a standardized pre-research snapshot for each holding:
quantitative metrics (yfinance) + AI-extracted news (RSS + Gemini), assembled
into per-ticker Markdown reports and a dashboard mockup.

This is a demo, not investment advice. AI items need human review.

The active universe has 25 holdings (`scripts/universe.py`); ticker scripts
default to CNQ.TO. The `prompts/` templates have empty headline lists — add
sourced headlines before using them. Reports under `reports/` are historical
snapshots of the previous universe; new reports have not been fetched.

## Run

```bash
pip install -r requirements.txt
python3 scripts/run_phase1.py
python3 scripts/validate_phase1.py
```

Reports go to `reports/`; per-ticker data to `data/`. AI extraction needs a
configured Gemini CLI (`GEMINI_CLI`). Open `docs/index.html` for the dashboard.

## Tests

```bash
cd scripts
python3 -m unittest -v test_ai_extract test_data_utils test_rule_opt_v2
```

Full offline suite (including archived verification tests) from the repo root:

```bash
PYTHONPATH=scripts .venv/bin/python -m pytest --import-mode=importlib -q
```

Metric edge cases (short histories, missing SPY, zero volatility, etc.) map to
`ok` / `undefined` / `insufficient` with a reason recorded in `metric_notes`;
see `scripts/assumptions.py` and `scripts/quant.py` for details. RSS fetch
failures are retried with backoff and recorded as `failed` in `ai-intel.json`
without breaking the quant side.

Config: `JSOSIF_CONFIG` JSON, `config.json`, or `JSOSIF_<KEY>` env vars
(env > file > defaults).
