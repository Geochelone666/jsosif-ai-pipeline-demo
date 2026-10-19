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
2. Configure `GEMINI_API_KEY`, actual `GEMINI_RPD`/`GEMINI_RPM`, and
   `SEC_USER_AGENT`. FRED is optional. Check that the quota rotation can refresh
   all requested holdings before they become too old for delivery.
3. Run **Refresh research archive** and inspect its report-data branch and site
   artifact. This workflow updates research on workdays at 22:17 UTC and never
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
workday research publication, not streaming exchange quotes. Source dates can
precede publication, and degraded or imported reports remain clearly labeled.
No member table, message preview, email address or delivery ledger is published.
The archive retains saved source snapshots; it cannot reconstruct data that was
never collected. Existing historical reports are imported without refreshing them.
