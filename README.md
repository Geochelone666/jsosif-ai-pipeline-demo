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

## Built-in daily scheduler

Run the foreground daemon in a persistent terminal or under a process supervisor;
no external cron is needed. Keep the process and machine running:

```bash
JSOSIF_APPROVED_SEND=1 python3 scripts/scheduler.py --daemon
```

It sleeps until the next 09:00 `America/Toronto`, adjusting for daylight saving
time, then runs `distribute_team_reports.py --send` with the current Python
interpreter. Existing Gmail credentials and send approval are still required.
It distributes existing reports; it does not refresh them. Missed runs while the
process is stopped are not replayed. Starting at exactly 09:00 schedules tomorrow.

`--once` sends immediately; `--dry-run` only prints the next run and elapsed
seconds without sending or creating files. These modes are mutually exclusive.
Logs rotate at `logs/scheduler.log`; use `--log-file` to override. A shared
`logs/distribution.lock` prevents simultaneous sends by scheduler instances,
including `--once`; use the same `--lock-file` for all instances. Direct manual
calls to the distribution script do not participate in this lock. The persistent
lock file is released by the OS when its owner exits; do not delete it while
running. Failed sends are logged and the daemon continues with the next day's
run, without automatically retrying a potentially partially sent batch. Child
output is suppressed to keep credentials and recipient data out of scheduler logs.
