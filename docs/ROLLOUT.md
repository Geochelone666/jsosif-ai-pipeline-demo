# Team rollout checklist

## Collect one row per member

Open the **Members and groups** page or fill `config/members.example.csv` in a
spreadsheet. You can keep it as `.xlsx` using [the Excel template](members.example.xlsx),
or save it as UTF-8 CSV. Examples contain no real member details
and have email participation disabled.

| Column | Meaning | Example |
| --- | --- | --- |
| `id` | Stable member ID; keep it when names or email addresses change | `member-001` |
| `name` | Name used in the greeting | `Example Analyst` |
| `email` | A single bare email address | `analyst@example.com` |
| `groups` | Group IDs separated by semicolons; may be blank with personal holdings | `energy;technology` |
| `tickers` | Personal holdings separated by semicolons; blank inherits group defaults | `CNQ.TO;CSCO` |
| `enabled` | Participation in email delivery | `false` or `true` |
| `timezone` | IANA time zone, not an abbreviation or numeric offset | `America/Toronto` |
| `send_weekday` | Desired weekly delivery day; Monday = 0, Sunday = 6 | `2` |
| `send_time` | Desired local 24-hour time | `09:00` |

Personal holdings replace group defaults when supplied. Duplicate holdings are
combined into one report per stock. A member who opts out of email can still use
the public research website; research collection is independent of participation.
New groups can be created from a complete CSV containing their personal holdings.
To use group defaults without listing personal holdings, define those groups in
the editor or private JSON first. Keep IDs stable to preserve weekly deduplication.

Optional columns retain `preferred_frequency`, `preferred_weekdays`,
`preferred_time`, `content_preferences` and `feedback` from the paper slip.
These are survey responses, not automatic delivery instructions. Confirm one
weekly day and an exact local time before enabling a member. A broad preference
such as "Before 9 AM" belongs in `preferred_time` until the exact `send_time` is
confirmed. Interest in being contacted does not by itself enable recurring email.

## Import and preview privately

The browser editor imports and exports both JSON and CSV. Editing happens in
memory; download changes before closing the page. It does not upload the table
or enable email automatically. The Excel workbook can also be passed directly to the project importer:

```bash
python scripts/subscriptions.py config/subscriptions.local.json \
  --import-excel config/members.local.xlsx
```

For CSV and email previews:

```bash
python scripts/subscriptions.py config/subscriptions.local.json \
  --import-csv config/members.local.csv
python scripts/deliver_weekly.py --config config/subscriptions.local.json \
  --store report-store --preview-all --preview-dir review/weekly
```

The entire roster is validated before replacing the private configuration.
Preview files contain personal information; keep them in the ignored `review/`
directory. Invalid, stale, incomplete or historical-only reports are deferred.
The preview command never contacts SMTP and does not consume a weekly slot.

Check the recipient, greeting, chosen stocks, source dates and PDF attachments.
The body uses the previously tested format:

```text
Hi Example Analyst,

Here are the latest JSOSIF intelligence reports:

- CNQ.TO — YYYY-MM-DD
- CSCO — YYYY-MM-DD

Best,
Tech Team
```

## Configure automation after roster review

1. After importing Excel, use the exported private JSON or save the workbook as
   UTF-8 CSV. Save the CSV as the private GitHub repository secret `MEMBERS_CSV`. Do not
   commit the real table. Existing JSON can instead be stored in
   `SUBSCRIPTIONS_JSON`; if both exist, CSV replaces members and JSON retains
   group defaults, quality policy and report age limits.
2. Configure `Grop_ai_API` (Groq), optional application request/token caps, and
   `SEC_USER_AGENT`. FRED is optional. Check that the daily AI request/token caps can cover
   all requested holdings before they become too old for delivery.
3. Run **Daily production research pipeline** and inspect its report-data branch and site
   artifact. This workflow updates research every day at 19:00 America/Toronto and never
   sends mail. Existing reports are retained with their original dates.
4. Enable GitHub Pages with **GitHub Actions** as the deployment source, then set
   `PAGES_DEPLOY_ENABLED=true` to publish the site. Until enabled, the workflow
   still provides the generated site artifact for review.
5. Configure `GMAIL_USER` and `GMAIL_APP_PASSWORD`. Run **Weekly member PDF
   delivery** manually with confirmation `NO` to inspect due counts. Use the
   local preview command to inspect message bodies before the member's due time.
6. After reviewing the intended roster and previews, set
   `EMAIL_DELIVERY_ENABLED=true` to activate scheduled weekly delivery. A manual
   confirmation of `YES` can also send due messages. Leave the variable false
   while preparing the rollout.

The delivery scanner checks every 15 minutes. It sends at or after the member's
chosen local weekly time, subject to GitHub Actions scheduling delays and fresh
report availability. It is not an exact-minute scheduling service. Accepted
messages are not sent twice in the same local calendar week. Uncertain SMTP
outcomes require reconciliation rather than an automatic duplicate attempt.

Updating the private roster secret takes effect on subsequent runs; no code
change is needed for each new member. Disabling a member stops later deliveries,
but cannot retract email already accepted by SMTP or cancel an in-flight run.

## Website behavior

The site shows latest saved metrics, source dates, quality, and the full report
version history. Readers can inspect quantitative metrics, research sections and
freshness evidence inline, and download the original PDF, JSON or Markdown.
The site checks for a new publication every minute by default and retains the
last loaded view if a check fails. Users can choose five minutes or manual checks.

Browser refresh does not run the research pipeline. The agreed data cadence is
daily research publication, not streaming exchange quotes. Source dates can
precede publication, and degraded or imported reports remain clearly labeled.
No member table, message preview, email address or delivery ledger is published.
The archive retains saved source snapshots; it cannot reconstruct data that was
never collected. Existing historical reports are imported without refreshing them.

## Signup pilot activation

The pilot adds 25 explicitly requested symbols to the original 25 holdings.
Personal tickers still replace group defaults. Sector-only requests use the
original portfolio holdings in that sector; C-Suite with no stocks stays disabled.
Participant names, email addresses and feedback belong only in the private
`SUBSCRIPTIONS_JSON` secret, never in source control or Pages.

An optional member `delivery_start_date` (ISO YYYY-MM-DD in the member's timezone)
prevents activation from catching up a weekly slot whose scheduled date is before
that date. It does not change the selected weekday or local send time. The pilot
starts on 2026-10-22, so elapsed Monday/Tuesday/Wednesday slots start next week.
Existing configurations without this field retain their catch-up behavior.

Collection allows 230 minutes within a 240-minute job to accommodate expanded
coverage and provider retries while leaving time to persist and publish. Missing
or degraded reports still defer the complete member digest; they are never
silently dropped from the requested list. GitHub Actions can delay both nightly
collection and the 15-minute delivery scanner; configured times are due times,
not guaranteed SMTP submission times.

## Recover a slow or interrupted collection

Use **Daily production research pipeline → Run workflow → resume=true** to retry
outstanding holdings for the current Toronto business date. Leave `force=false`.
Resume verifies file hashes, snapshot identity, ready quality and issuer advisories
before reusing a same-day version. Missing, degraded or invalid versions are
collected again. A fully recovered date makes no new provider calls. Use
`force=true` only when all holdings should be collected again; it cannot be
combined with resume. Neither option submits email.

The collector has a 210-minute work budget within the 230-minute collection step.
Each subprocess is bounded by the remaining work budget. On exhaustion it records
`interrupted`, the pending symbols and a recovery reason, leaving time for durable
checkpointing and publication. The always-run finalizer also marks a collector
that crashed or was cancelled as interrupted, but only when its workflow run ID
owns the current attempt. A non-cancelled partial run can publish its saved
reports and interrupted status; strict release/site verification remains red until
all requested evidence is ready. Cancelled jobs retain their checkpoints but do
not deploy a site.

SPY benchmark requests share successful Yahoo or Stooq data only within a single
collection batch. If both providers fail, the failure is reused for five minutes
before another request is allowed. Benchmark metrics remain unavailable during an
outage; no price is invented or carried from an earlier batch. Other holdings
retain their normal provider behavior.

Resume does not delete or rewrite history. If an older archived file is corrupt,
regenerating a current report cannot repair that historical file; restore it from
an intact report-store backup before the site's integrity checks can pass.

The legacy `scripts/scheduler.py` scans only at 09:00 each day. Use the Actions
weekly delivery workflow for members with noon/evening preferences; the legacy
scheduler is not a replacement for that workflow.
