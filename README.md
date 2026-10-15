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

## Team email distribution

`config/team_recipients.json` maps each teammate to one holding. Generate one
multipart email per teammate from existing reports:

```bash
python3 scripts/distribute_team_reports.py --dry-run
```

Previews are written to ignored `review/team/`. The default report date is the
latest date available for every assigned holding; use `--date YYYYMMDD` to select
a specific snapshot. This command does not refresh reports or schedule daily runs.
The complete batch is validated before delivery. Actual sending requires explicit
Lucas approval, `JSOSIF_APPROVED_SEND=1`, `--send`, and the existing local
`config/gmail.json` credentials. A transport failure stops the batch; check which
messages were sent before retrying to avoid duplicates. Never commit credentials.
