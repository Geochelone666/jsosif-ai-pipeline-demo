# JSOSIF research reports

Quantitative metrics, recent headline research, PDF reports, a versioned website,
and one personalized weekly email per participating member. The active universe
contains 25 holdings in `scripts/universe.py`.

Reports support analyst research preparation. Check source dates and missing data;
they are not investment advice. News summaries use RSS headlines, not full articles.

## Manual member and group entry

Open `docs/members.html` locally, or choose **成员与小组配置** on the report site.
The browser form supports group stock lists, multiple members, participation,
time zones and weekly delivery times. Import an existing JSON to edit it, then
download `subscriptions.local.json`. All editing stays in that browser page;
it does not upload the roster or enable delivery. Save the download before closing
the page and use it as the private configuration below.

Copy `config/subscriptions.example.json` to **ignored**
`config/subscriptions.local.json`. Enter groups and their ticker lists, then members:

- `id`: a stable member identifier; keep it when changing their email/name.
- `name`, `email`, `groups`: one or more group IDs; overlapping tickers are deduplicated.
- `enabled`: participation switch, a JSON boolean.
- `timezone`: IANA zone such as `America/Toronto`.
- `send_weekday`: Monday = 0 through Sunday = 6.
- `send_time`: local 24-hour `HH:MM`.

You can manually fill a CSV using `config/members.example.csv`, with group IDs
separated by semicolons, then import it:

```bash
python scripts/subscriptions.py config/subscriptions.local.json --import-csv config/members.local.csv
```

This replaces the configuration's member list after validating the entire input.
All example members are disabled and use example.com addresses. Actual member
files must stay private; do not commit them to this public repository.

## Generate and retain reports

```bash
python -m pip install -r requirements.txt
python scripts/refresh_reports.py --store report-store --config config/subscriptions.local.json
python scripts/build_site.py --store report-store --output site-build
```

Configure `GEMINI_API_KEY`, actual project quotas `GEMINI_RPD` and `GEMINI_RPM`,
and `SEC_USER_AGENT` (organization and real contact email). `FRED_API_KEY` is
optional. `GEMINI_MODEL` defaults to `gemini-3.5-flash-lite`. An explicitly supplied
`GEMINI_CLI` remains available for standalone compatibility; GitHub uses the
portable REST client and no home-directory credentials.

`--interval-days` defaults to 1 and controls the minimum calendar-day interval
between successful refresh batches. `--force` bypasses the interval, but never
bypasses provider-side or locally tracked API quotas. All stages share one UTC
business date, including runs that cross midnight.

The planner uses 80% of configured Gemini RPD, subtracts attempts already made
in the same Pacific quota day, and reserves three attempts per ticker. A repeated
manual run cannot plan against the same requests again. If a daily batch cannot cover every subscribed stock, it rotates the
least-recently updated stocks across days. `refresh_plan` in the archive index
reports the conservative number of collection days for a full rotation (weekday
schedules can make the calendar duration longer). It is a planning estimate,
not a guarantee of provider capacity. RPM is enforced per attempt; HTTP 429/5xx
use bounded retries. Actual token quotas still apply at the provider; token usage
is captured in per-ticker Gemini envelopes. Other applications sharing the same
project also consume the published quota.

If a rotation takes longer than your weekly delivery or freshness requirements,
increase the available quota, reduce the stock list or adjust the requirements;
the application defers an incomplete/stale digest instead of mislabeling it fresh.
Yahoo/RSS have no fixed guaranteed capacity established by this project. Start
with one collection batch per trading day and inspect observed failures.

Every archived version includes immutable MD, JSON, PDF and the source snapshots.
Same-day reruns receive separate run IDs. Each file has a SHA-256 integrity check.
Price history is reused only within the current collection batch; later batches
fetch again so an earlier provisional daily bar cannot mask the closing price.
Existing saved Markdown is migrated by `scripts/import_history.py` before the
first refresh. It preserves the original text/date, renders a historical PDF
without reading today's mutable data snapshots, and marks these versions
`historical`. Import is idempotent, and historical versions are excluded from
weekly delivery even when degraded reports are allowed. Only new collections
carry fresh source snapshots; historical imports cannot reconstruct missing inputs.
Source freshness and degraded news are visible in the snapshot and site. Market
data older than four calendar days is marked degraded; this conservative bound
may need adjustment for exceptional exchange closures. Peers display their own
listing currencies; this project does not convert values to USD.

## Weekly personalized delivery

```bash
python scripts/deliver_weekly.py --config config/subscriptions.local.json --store report-store
```

Default mode shows preview counts and never consumes the weekly send slot.
For enabled members whose local weekly time has passed, it selects the newest
qualifying report for every subscribed ticker. One email includes all PDFs, a
personal greeting, attachment introduction and good wishes. Multiple groups still
produce at most one email per member per local Monday–Sunday week.

For the repeated fall-back hour, a configured time uses its first occurrence.
A nonexistent spring-forward time moves forward by the DST gap (for example,
02:30 becomes 03:30 when the clock skips an hour). Due checks compare UTC instants,
so the repeated hour cannot undo an already due delivery.

Actual delivery requires `--send`, `JSOSIF_APPROVED_SEND=1`, `GMAIL_USER`, and
`GMAIL_APP_PASSWORD`. A local ignored `config/gmail.json` remains supported for
legacy usage. Scheduled delivery does not regenerate reports.

`max_report_age_days` defaults to 4. Zero means a report dated today in UTC and generated
within the last 24 hours; positive values bound both the UTC report date and elapsed
generation age. The member editor canonicalizes time zone names before export.
Degraded reports are blocked unless the
private configuration explicitly sets `allow_degraded: true`. Missing/old reports
defer the whole member digest and are retried by later scans within the same week.
Both the report date and its generation time must satisfy the age bound, so
repackaging old content does not make it eligible for weekly mail.
The encoded email is capped at 20 MiB to leave room below common SMTP limits.

The sender records a `sending` reservation durably before contacting SMTP.
Accepted messages are not sent again that week. An ambiguous transport failure
is marked `unknown` and is not automatically retried: check the sender mailbox,
then explicitly resolve it using `scripts/delivery_state.py`. Reconciliation uses
the same lock as sending, so concurrent edits cannot overwrite delivery state. SMTP acceptance is
not proof of inbox delivery. State contains hashed member/week keys, timestamps
and report IDs, but no email addresses, names or email bodies. Keep IDs stable;
use random IDs if even guessed identifiers would be sensitive.

## GitHub automation and Pages

Set repository **Secrets**:

- `SUBSCRIPTIONS_JSON`: contents of the private subscription configuration.
- `GEMINI_API_KEY`, optional `FRED_API_KEY`.
- `GMAIL_USER` and `GMAIL_APP_PASSWORD` for delivery.

Set repository **Variables**:

- `GEMINI_RPD`, `GEMINI_RPM`: actual model/project limits from AI Studio.
- `SEC_USER_AGENT`: organization plus contact email.
- Optional `GEMINI_MODEL`, `REPORT_INTERVAL_DAYS` (default 1).
- `EMAIL_DELIVERY_ENABLED=true` enables scheduled mail scans.
- `PAGES_DEPLOY_ENABLED=true` enables website publication after Pages is
  configured to deploy with **GitHub Actions** in repository settings.

`Refresh research archive` runs after typical market closing times, Monday–Friday
at 22:17 UTC. It collects only the union of enabled members' stocks; without
`SUBSCRIPTIONS_JSON`, it collects the full 25-stock universe. It never sends mail.
`Weekly member PDF delivery` checks due members every 15 minutes at offset minutes.
Manual runs default to preview; type `YES` in the confirmation input to send.
GitHub schedules can be delayed or dropped, so delivery is best-effort within the
remaining local week. It does not guarantee minute-exact arrival. A durable
external scheduler is needed if strict arrival deadlines are required.

Both workflows serialize through the same concurrency group and use the
`report-data` branch as the persistent store. Successful report versions and quota
state are pushed even when another stock fails. The sender pushes its reservation
before SMTP and its result afterwards. A failed push blocks delivery. The branch
is initialized only after an explicit remote check proves it is absent; connection
failures never initialize over unknown state. Do not delete or rewrite this branch.
Back it up as the report archive grows; it is not a substitute for an independent backup.

Publication runs only after the store has been persisted successfully. The site
builder stages and validates all files before replacing its previous output; a
missing store or corrupt report preserves the last good site.

The Pages build copies only indexed report files, never private configuration,
delivery state, quota state or credentials. It shows latest reports, a stock/date/
quality filter, all historical versions and PDF/JSON/MD downloads. The browser
rechecks the index every five minutes; new data appears after the next successful
refresh/deployment, not as a streaming market feed. These report files and the
report-data branch are public in a public repository. Private group reports require
a separate authenticated hosting/storage design. Confirm data redistribution rights
for team/public use before publishing provider data.

## Tests and legacy commands

```bash
python -m pip install -r requirements-dev.txt
PYTHONPATH=scripts python -m pytest --import-mode=importlib tests scripts -q
```

The offline CI runs on pushes and PRs. Tests cover news date boundaries, provider
usage/errors, subscriptions, DST, weekly deduplication, uncertain SMTP outcomes,
durability before send, stale/corrupt reports, immutable history and private-state
exclusion from the site. Browser configuration validation is checked against the
Python importer using Node. No test sends real email.
Each successful CI run also provides a `research-site-preview` artifact containing
the site, configuration form and PDFs generated from the existing saved history.
It uses no live APIs or member credentials; the artifact expires after 14 days
and is a review preview, not the permanent report store.

`run_phase1.py`, `run_all.py`, `distribute_team_reports.py` and `scheduler.py` remain
legacy entry points for compatibility. Use the new refresh/delivery workflows for
subscriptions and weekly idempotency; do not run the legacy daily daemon alongside
them. The former one-time test sending schedule has been removed. Legacy recipient
configuration now contains example addresses instead of actual members.
