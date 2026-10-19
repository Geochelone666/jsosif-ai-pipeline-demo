# V1 prelaunch acceptance evidence

Recorded on 2026-10-19. This document distinguishes simulated business checks from
real external integration and deployment acceptance.

| Check | Evidence | Result |
| --- | --- | --- |
| Full offline regression | Python 3.12, pinned development dependencies, `PYTHONPATH=scripts python -m pytest --import-mode=importlib -q` | 703 passed |
| Full portfolio rehearsal | 25 holdings, 30 synthetic Excel members, three timezones, two simulated weeks; external source stages and SMTP replaced with fixtures | Passed |
| Personalized messages | 29 private previews, five attachments for the first member, individual choices, one opted-out member, no real SMTP submission | Passed |
| Delivery recovery | Duplicate scans, expired reports, an uncertain submission and later scans that continue to flag reconciliation | Passed |
| Historical retention | Two simulated collections retained 50 versions and original hashes | Passed |
| Remote archive recovery | Fresh clone of `report-data`; all 25 pre-existing historical versions verified | Passed |
| Browser acceptance | Chromium: history inspector, filters, refresh, CSV import/export, invalid-import preservation and mobile layout; no JavaScript errors | Passed |
| Public-site verification | Real local HTTP server: expected date, publication metadata, coverage and file hashes; broken PDFs and stale publications rejected | Passed |
| Workflow structure | All five workflow YAML files parsed; branch review still precedes GitHub execution | Passed locally |
| Runtime dependencies | `pip check` in the pinned environment | Passed |
| Authenticated Groq and source access | Current development runtime has no injected Groq key and has not applied saved source-domain configuration | Not verified here |
| Gmail authentication | No Gmail credentials in the current runtime; the new live workflow authenticates without submitting a message | Not verified here |
| Current-day production collection | Restored remote store had historical reports only and no recorded daily attempt | Not passed |
| Public Pages deployment | Requires a current successful production collection and deployed HTTP verification | Not verified here |
| Inbox placement | No real email was sent during this acceptance work | Not tested |

## Fixes covered by this update

- Report freshness uses Toronto dates while member delivery uses each member's
  own timezone. UTC midnight no longer rejects a same-day Toronto report.
- Due deliveries without eligible reports fail visibly and leave their slots
  retryable. Uncertain or interrupted submissions remain visible on later scans
  without automatic resubmission.
- Release verification requires the expected daily date and a complete strict
  run; a healthy historical store cannot stand in for today's successful update.
- Deployment verifies real HTTP responses and hashes after Pages reports success.
- Provider credentials never follow redirects. Groq pacing across UTC midnight
  charges the correct application day. A persistence failure after a successful
  HTTP response does not trigger another API call.
- Invalid AI summaries remain unclassified; batched Groq responses are normalized
  before merging, using the same schema checks as single batches.
- Offline tests isolate live credentials. CI includes the report-compatibility
  checks and a repeatable desktop/mobile browser job.
- Empty or entirely opted-out rosters leave the weekly workflow idle. Invalid
  private configuration cannot enable delivery.

## Remaining acceptance sequence

1. Merge the hardening change and require the offline and browser CI checks.
2. Check the automatically started **Live launch acceptance (no email delivery)**
   artifact. It makes one real Groq request and independently checks sources,
   Gmail login, production switches and the deployed site. No roster is needed.
3. Correct only the blocked settings. Run **Daily production research pipeline**
   and inspect its strict acceptance result and deployed verification. Use `force`
   only to recover an already attempted date after correcting its cause.
4. After reviewing and removing any old test roster, arm
   `PAGES_DEPLOY_ENABLED=true` and `EMAIL_DELIVERY_ENABLED=true`, then rerun live
   acceptance. A missing or empty roster remains idle.
5. Import the reviewed formal Excel roster, inspect private previews and update
   the repository's private roster Secret. Subsequent scans use enabled members'
   settings automatically; new holdings enter the next daily collection.

See [V1 launch and operations](V1_LAUNCH.md) for settings, commands, recovery and
scope. Do not describe this release as waiting only for member information until
the real integration and deployment checks have passed.
