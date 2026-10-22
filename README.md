# JSOSIF research reports

Quantitative metrics, recent headline research, PDF reports, a versioned website,
and one personalized weekly email per participating member. The active universe
contains 25 holdings in `scripts/universe.py`.

Reports support analyst research preparation. Check source dates and missing data;
they are not investment advice. News summaries use RSS headlines, not full articles.

## Manual member and group entry

Open `docs/members.html` locally, or choose **Members and groups** on the report site.
The browser editor provides a member table with names, email addresses, groups,
personal ticker lists, participation, time zones and weekly delivery times. Import
an existing JSON or UTF-8 CSV to edit it, then download `subscriptions.local.json`
or `members.local.csv`. CSV and Excel templates are available from the editor. The downloadable Excel
workbook also preserves the original paper-form survey answers. All editing stays in that browser page;
it does not upload the roster or enable delivery. Save the download before closing
the page and use it as the private configuration below.

Copy `config/subscriptions.example.json` to **ignored**
`config/subscriptions.local.json`. Enter groups and their ticker lists, then members:

- `id`: a stable member identifier; keep it when changing their email/name.
- `name`, `email`: the personal greeting and delivery address.
- `groups`: group IDs used for team membership and default stock lists.
- `tickers`: optional personal stock list. A nonempty list replaces group defaults;
  leave it empty to inherit the union of selected groups. At least a group or
  personal holding is required. Only the 25 supported holdings are accepted.
- `enabled`: participation switch, a JSON boolean.
- `timezone`: IANA zone such as `America/Toronto`.
- `send_weekday`: Monday = 0 through Sunday = 6.
- `send_time`: local 24-hour `HH:MM`.

You can manually fill a CSV using `config/members.example.csv`, with group IDs
and personal tickers separated by semicolons, then import it:

```bash
python scripts/subscriptions.py config/subscriptions.local.json --import-csv config/members.local.csv
```

A completed Excel workbook can be imported directly, without converting it first:

```bash
python scripts/subscriptions.py config/subscriptions.local.json --import-excel config/members.local.xlsx
```

Use the `Members` sheet in [the Excel template](docs/members.example.xlsx), or a
single-sheet workbook with the same column headers. Native Excel time cells are
supported. Formula cells are rejected; the importer never evaluates them.

This replaces the configuration's member list only after validating the entire input,
using an atomic file replacement with owner-only permissions. A complete CSV can
create the JSON configuration from scratch. New groups derive their stock lists
from the personal holdings entered for that group. Existing group lists and
freshness settings are preserved. Header-only files are rejected. Use `true`/`false`
or `yes`/`no` for participation; weekday numbers run from Monday = 0 to Sunday = 6.
Optional `preferred_frequency`, `preferred_weekdays`, `preferred_time`,
`content_preferences` and `feedback` columns retain the original paper survey.
They do not override the reviewed `send_weekday`, `send_time` or `enabled` values.
The pilot remains weekly even if a survey response asks for daily reports.
All example members are disabled and use example.com addresses. Actual member
files must stay private; do not commit them to this public repository.

## Generate and retain reports

```bash
python -m pip install -r requirements.txt
python scripts/refresh_reports.py --store report-store --config config/subscriptions.local.json
python scripts/build_site.py --store report-store --output site-build
```

Production AI uses **Groq**. Set the repository Secret `Grop_ai_API`; the daily
workflow maps it to `GROQ_API_KEY` and explicitly sets `AI_PROVIDER=groq`.
The default model is `openai/gpt-oss-20b`. Local request and token application
caps are configurable with `GROQ_RPD`, `GROQ_RPM`, `GROQ_TPD`, and `GROQ_TPM`.
These caps are not the provider's published allowances. Verify account limits in
Groq Console. Quota exhaustion degrades AI evidence without suppressing market
collection. See [v1 launch and operations](docs/V1_LAUNCH.md) for configuration,
policy evidence, acceptance checks and recovery. Gemini remains available for
explicit standalone compatibility through `AI_PROVIDER=gemini`.

## Weekly personalized delivery

```bash
python scripts/deliver_weekly.py --config config/subscriptions.local.json --store report-store
```

Default mode shows preview counts and never consumes the weekly send slot.
To inspect actual `.eml` messages before the scheduled time, use:

```bash
python scripts/deliver_weekly.py --config config/subscriptions.local.json --store report-store \
  --preview-all --preview-dir review/weekly
```

This includes enabled members only, checks report quality and freshness, writes
private previews outside the public archive, and does not contact SMTP or reserve
a weekly slot. Preview flags cannot be combined with `--send`. Historical-only
archives still defer delivery previews; they do not masquerade as fresh reports.
For enabled members whose local weekly time has passed, it selects the newest
qualifying report for every subscribed ticker. One email includes all PDFs, a
personal greeting, the report list and the `Best, / Tech Team` sign-off.
This is the same short cover-note format as the previously tested email; the
detailed analysis stays in the PDF attachments. Multiple groups still
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
Before delivery or site publication, archive files must match their hashes,
filenames, snapshot contract, ticker, report date and quality label. All three
files must belong to the same archived version, and the PDF must have a PDF header.
An invalid archive is deferred for delivery; a failed site build preserves the
previous output. The snapshot release check rejects an empty reports directory.

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
- `Grop_ai_API` (Groq), optional `FRED_API_KEY`.
- `GMAIL_USER` and `GMAIL_APP_PASSWORD` for delivery.

Set repository **Variables**:

- Optional `GROQ_RPD`, `GROQ_RPM`, `GROQ_TPD`, `GROQ_TPM`: application caps.
- `SEC_USER_AGENT`: organization plus contact email.
- Optional `GROQ_MODEL`; daily collection targets 19:00 America/Toronto.
- `EMAIL_DELIVERY_ENABLED=true` enables scheduled mail scans.
- `PAGES_DEPLOY_ENABLED=true` enables website publication after Pages is
  configured to deploy with **GitHub Actions** in repository settings.

`Refresh research archive` runs after typical market closing times, Monday–Friday
at 22:17 UTC. It collects only the union of enabled members' stocks; without
`SUBSCRIPTIONS_JSON`, it collects the full 25-stock universe. It never sends mail.
`Weekly member PDF delivery` checks due members every 15 minutes at offset minutes.
Manual runs default to preview; type `YES` in the confirmation input to send.
Both workflows accept the private `MEMBERS_CSV` repository secret directly.
`SUBSCRIPTIONS_JSON` remains supported for existing group defaults and report
policies. If both are set, CSV replaces the members while preserving those
defaults and policies. Neither roster is written to the public site or logs.
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
PYTHONPATH=scripts python -m pytest --import-mode=importlib -q
```

This matches CI: it also collects the archived experiment tests under
`verification/`. Pass `tests scripts` to run only the current pipeline suites.

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


## Rollout from the team spreadsheet

See [the rollout checklist](docs/ROLLOUT.md) for collection fields, CSV import,
private preview, automation settings, and the website's daily update behavior.
The public workspace shows latest saved metrics, per-source dates and quality,
plus every historical version. Use **Read research** or **Inspect** to view a
version's quantitative table, research sections and freshness evidence inline.
The browser checks for a new publication every minute by default; readers can
choose five minutes or manual refresh. Polling does not initiate API calls or
convert daily research snapshots into streaming quotes.
