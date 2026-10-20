# JSOSIF v1.0.0 launch and operations

## Release contract

- Python 3.12 with `requirements.lock`; CI and scheduled workflows use that runtime.
- One automatic research collection per Toronto business date, including weekends.
  The target time is 19:00 America/Toronto. Two UTC triggers cover daylight saving
  time, but the gate selects only one and the collector rejects duplicate dates.
  GitHub Actions can delay execution; this is not an exact-minute service.
- Every configured holding gets its market and non-AI collection independently
  of AI quota. Quota planning limits AI calls only. Missing credentials,
  insufficient quota, empty news or failed extraction are explicitly degraded.
- The site is published after the daily run and retains every archived version.
  `health.json` and the page banner expose partial, degraded and failed updates.
  A new publication timestamp never claims that an old source is fresh.
- Weekly member email remains separately gated. It requires fresh eligible
  reports and explicit participation, uses the approved short body and PDFs,
  and does not blindly retry an uncertain SMTP submission.

## Required GitHub settings

Use repository Settings → Secrets and variables → Actions. Never put keys in
source files, PR descriptions, issue comments or chat.

| Setting | Type | Purpose |
| --- | --- | --- |
| `Grop_ai_API` | Secret | Existing Groq key, mapped to `GROQ_API_KEY` in Actions |
| `GROQ_MODEL` | Optional variable | Defaults to `openai/gpt-oss-20b`; verify account availability |
| `GROQ_RPD`, `GROQ_RPM` | Optional variables | Application request caps, defaults 100/day and 10/minute |
| `GROQ_TPD`, `GROQ_TPM` | Optional variables | Application token caps, defaults 100,000/day and 5,000/minute |
| `SEC_USER_AGENT` | Optional variable | Organization/contact override; otherwise derive a real contact identity from `GMAIL_USER` |
| `PAGES_DEPLOY_ENABLED` | Variable: `true` | Enable the Pages deployment step |
| `SUBSCRIPTIONS_JSON` or `MEMBERS_CSV` | Secret | Private roster and research choices |
| `GMAIL_USER`, `GMAIL_APP_PASSWORD` | Secrets | Gmail authentication/delivery; the sender address can also supply the SEC contact |
| `EMAIL_DELIVERY_ENABLED` | Variable | Leave false until the roster and email previews are reviewed |
| `FRED_API_KEY` | Optional secret | FRED macro source; otherwise explicitly unavailable |

Without a roster, collection covers the 25 configured holdings. A roster controls
the research universe, but opting out of email does not stop website research.
Without a real SEC identity, no placeholder requests are made; SEC fields are
explicitly unavailable. Configure it before claiming the filing integration works.

Enable GitHub Pages using **GitHub Actions** as the deployment source. Allow the
`github-pages` environment to deploy from the intended source branch. The
workflow needs contents write, Pages write and OIDC permissions. Git authentication
alone does not prove that repository administration or Pages deployment is allowed.

## First live acceptance

1. Install pinned dependencies in Python 3.12:

   ```bash
   python -m pip install -r requirements-dev.txt
   PYTHONPATH=scripts python -m pytest --import-mode=importlib -q
   ```

2. Run **Groq API contract check** manually in Actions to use the existing
   repository Secret directly. Alternatively provide API credentials securely
   in the runtime used for testing. GitHub
   Secrets do not automatically enter a separate development environment.
   Execute one small authenticated AI contract check:

   ```bash
   python scripts/probe_ai.py
   ```

   It makes one request and reports status, model and usage; it does not print
   the key or raw response. Do not repeatedly probe after a quota/access error
   until the configuration or diagnosis changes.

3. Run **Daily production research pipeline** manually. Normal runs are
   idempotent for the local date. Enable `force` only for an explicit recovery
   after correcting a failure or changing quota/configuration.
4. Require all expected reports for the date to pass the strict release check:

   ```bash
   python scripts/check_release.py --store report-store --require-ready
   ```

   A degraded pipeline can still publish honest, usable market updates, but its
   strict workflow check fails until mandatory market/news evidence is ready.
   A historical-only archive cannot pass this acceptance check.
5. Verify the deployed site, `index.json`, `health.json`, one current PDF and an
   old archived PDF. Confirm the business date, expected/updated counts, quality
   and per-source timestamps. Verify that member data and previews are absent.
6. Before enabling email, import the reviewed roster and generate private
   `--preview-all --preview-dir review/weekly` messages. A real send requires
   explicit authorization and valid Gmail credentials; SMTP acceptance is not
   proof of inbox delivery.

## Failure and recovery

The source workflow and weekly sender share the `jsosif-report-data` concurrency
group. Local collectors also lock their shared source directory. An explicit
`--force` rerun archives new versions rather than overwriting old reports.
Do not delete `report-data`, reset it to an old source commit, or force-push it.

The collector pushes an initial run checkpoint, each completed ticker and the
final outcome when run with `--persist-git`. Each AI request reservation is
also pushed before the HTTP call. A failed push prevents that operation; an
interrupted job therefore has a recoverable status instead of silent success.
Check the run summary and `index.json:last_attempt` for failed stage names and
timeout categories. Do not assume that an interrupted `running` state completed.

Automatic runs attempt a business date once. After correcting the cause, use an
explicit recovery run. The prior valid versions remain available throughout.
The pipeline has per-stage timeouts and a two-hour job ceiling. A failed ticker
does not prevent the remaining holdings from being collected.

`report-data` is the durable store for immutable report files, source snapshots,
quota counters and hashed delivery reservations. Delivery records contain no
names or addresses. Every daily publication also uploads a compressed backup of
the persisted Git tree, retained as an Actions artifact for 30 days. This backup
retention does not delete Git history or archived reports.

Recover on a clean machine by cloning the `report-data` branch into a separate
store directory, checking integrity, and rebuilding the site with the current
application code. Retain the delivery ledger and API reservations during recovery;
restoring reports without them can permit duplicate sends or quota overspending.

## What counts as launched

Merged code, passing offline tests, a seeded historical store and generated site
artifacts are separate milestones. A live v1 requires a successful authenticated
AI check, full current-day collection, a strict release check, an actual Pages
deployment and a verified public response. Email activation is separate and can
remain off until the team roster has been collected. Never describe these external
checks as passed merely because the code is ready or the archive exists.

## Groq limits and policy evidence

The production workflow explicitly selects Groq and sends the existing
`Grop_ai_API` Secret only to `api.groq.com`. Standalone clients accept
`GROQ_API_KEY`; Gemini remains an optional explicit compatibility provider.
Never put a Groq key into a Gemini credential binding.

The local caps above are conservative application defaults, **not Groq plan
allowances**. The request/token ledger uses UTC dates for the application's daily
budget; this does not assert Groq's reset timezone. Input reservation uses a
conservative UTF-8 byte bound plus completion allowance. Minute request/token caps
use a rolling window, not an average spacing estimate. Successful calls reconcile
reported token usage; failed calls retain their reservation. Headlines are batched
five at a time, so one stock can require several requests. Budget exhaustion leaves
market collection running and marks affected AI evidence unavailable.

The client uses JSON object mode and a bounded completion, times out after 60
seconds, and retries connection errors, 408, 409, 429 and server errors at most
three total attempts. It honors Retry-After, including HTTP dates. Long retry
windows are persisted and deferred rather than retried early. Credentials and
provider error bodies are excluded from application errors and usage files.

Official sources checked on 2026-10-19:

- [Groq Python client](https://github.com/groq/groq-python): authentication,
  error classes, timeout and retry behavior.
- [Official request types](https://github.com/groq/groq-python/blob/main/src/groq/types/chat/completion_create_params.py):
  `openai/gpt-oss-20b`, `response_format` and `max_completion_tokens`.
- [Rate limits](https://console.groq.com/docs/rate-limits) and
  [account limits](https://console.groq.com/settings/limits): verify the actual
  model/account request and token limits before enabling full-volume collection.
- [Groq privacy policy](https://groq.com/privacy-policy/) and
  [terms](https://groq.com/terms-of-use/): review the current account's applicable
  data terms before sending private material.

The official SDK source was reachable during development; the documentation and
policy websites were blocked by the environment's outbound proxy. Consequently,
no account-specific allowance, retention guarantee or policy approval is claimed.
Only public headlines and the public stock symbol are sent for classification;
the member roster and email addresses are not included in AI prompts.

## Repeatable launch rehearsal

The offline suite includes a full 25-holding, 30-member, three-timezone rehearsal
across two simulated weeks. It imports a real `.xlsx` workbook, generates actual
Markdown/JSON/PDF artifacts, checks 29 personalized previews and the opt-out,
repeats delivery to check deduplication, rejects expired reports without reserving
slots, updates all holdings for the next week, preserves 50 report versions, and
checks that an uncertain SMTP result remains visible without automatic resubmission.
The external research sources and email transport are synthetic in this rehearsal;
it does not establish that real API calls or inbox delivery work.

Run the same tests used by CI:

```bash
python -m pip install -r requirements-dev.txt
PYTHONPATH=scripts python -m pytest --import-mode=importlib -q
```

Browser acceptance is now a separate CI job. It checks historical report reading,
filter/refresh behavior, CSV import/export, preservation after rejected imports,
and mobile overflow. All member data used by the browser check is synthetic.
For a local run against a generated site:

```bash
python -m pip install -r requirements-browser.txt
python -m playwright install chromium
python scripts/browser_smoke.py --site site-build --artifacts review/browser
```

To use an existing Chromium installation, set `BROWSER_EXECUTABLE` to its path.
Browser artifacts stay outside the public site. The deployed-site verifier checks
the expected business date, coverage, matching publication metadata, every current
Markdown/JSON/PDF hash, and one older PDF when historical versions exist:

```bash
python scripts/check_site.py --url https://OWNER.github.io/REPOSITORY/ --require-ready
```

Both verification CLIs default to today's **Toronto** date. Specify
`--business-date YYYY-MM-DD` when inspecting an earlier run or a delayed scheduled
publication. A healthy old archive cannot pass as today's successful update.

## Finish external acceptance before importing the real roster

**Live launch acceptance (no email delivery)** runs after its workflow or check
script merges into `main`, and can also be dispatched manually. It uses the
repository Secrets directly, so copying credentials into a development workspace
is unnecessary for this path. It independently checks one authenticated Groq JSON
request, market history, RSS, SEC, Gmail STARTTLS/login, the automation switches and the deployed site.
Gmail authentication submits no email envelope, recipients or message body.
The workflow uploads a sanitized `live-launch-acceptance` JSON artifact even if
one check fails. A failed check does not hide the remaining check results.

Set `PUBLIC_SITE_URL` only if Pages uses a custom address. Otherwise the workflow
uses the normal owner/repository Pages address. Run the daily pipeline and deploy
first; an old or historical-only site must fail the live acceptance check. If the
acceptance workflow starts before the first daily deployment, rerun it afterwards.
No roster is required for these checks. Each authenticated AI probe consumes one
real API request; this is a manually repeatable check, not a periodic quota probe.

A successful live acceptance establishes integration access and public deployment,
not a guarantee of future provider availability or inbox placement. Before enabling
weekly email, import the reviewed roster and inspect the personalized `.eml` files.
Once `EMAIL_DELIVERY_ENABLED=true`, new members are picked up by subsequent scans;
new holdings enter the next daily collection. A member without eligible reports
waits without consuming the weekly slot. Do not change member IDs between imports,
because IDs define durable weekly delivery identity.

Due deliveries blocked by missing or invalid reports fail the sending workflow
instead of silently reporting success. Their unreserved slots remain retryable.
Uncertain or interrupted submissions continue to report a reconciliation requirement
on later scans, and never submit another message until explicitly reconciled.
Report age uses Toronto calendar dates; member scheduling still uses each member's
own IANA timezone.

The v1 research universe contains the 25 configured holdings in `scripts/universe.py`.
Unsupported symbols are rejected on import; supporting new companies requires an
explicit universe/data-source update before roster activation. FRED is optional;
missing macro data is labelled unavailable. Streaming quotes, online self-service
signup and a database-backed member portal are outside this daily pilot's scope.


After validating integrations and confirming that old test members are removed,
production switches can be armed before the formal roster arrives. With
`EMAIL_DELIVERY_ENABLED=true`, a missing, empty or entirely opted-out roster leaves
the weekly job idle without SMTP authentication or delivery. An invalid roster
fails validation. A later valid enabled roster is picked up automatically. Keep
`PAGES_DEPLOY_ENABLED=true` so future daily runs continue to publish. Live acceptance
requires both switches to be armed before reporting `ready_for_roster=true`.


## Post-merge live diagnostics

The live account model directory was queried during the 2026-10-19 follow-up.
It offered `openai/gpt-oss-20b` and `openai/gpt-oss-120b` among the known public
candidates; the previous default model was unavailable. Production now defaults
to the smaller 20b model and requests low reasoning effort. Explicit `GROQ_MODEL`
configuration still takes precedence. API requests identify the application with
`User-Agent: JSOSIF/1.0`. Safe check annotations expose status codes and known
provider error codes without raw responses, credentials or addresses.

If the normal job logs or artifacts cannot be downloaded, inspect the run's
**Live acceptance** annotations. The same states appear in the job summary.
Select the optional `research_smoke` input when manually dispatching live launch
acceptance to generate one real CSCO report and PDF in a temporary store. The
isolated run uploads `isolated-real-research-preview`; it neither publishes the
website nor writes to `report-data` and never sends email. It consumes real source
and AI requests and is intended for explicit acceptance, not periodic polling.
A successful isolated report is separate from a full daily production deployment.

## Full-portfolio acceptance and quiet-news days

The isolated research check accepts `smoke_ticker=ALL` to collect every configured
holding without publishing or changing `report-data`. It uses the same collector,
source stages, report renderer and strict integrity check as production. Progress
notices appear after each five holdings. The final notice includes per-holding
classification counts and sanitized source-failure categories.

Groq classifications use a strict JSON schema with the requested listing symbol
as the only valid ticker value. Explicit irrelevant-headline decisions need a
matching input headline and a nonblank reason; they are retained in the archived
AI source JSON. Unexplained or malformed results remain unclassified. The model
must not replace Toronto or Paris symbols with unrelated or alternative listings.

A successful RSS query with no recent headlines is a quiet observation, not a
source outage. Reports explicitly say that no AI classification was performed.
A successful AI review that finds no relevant company development is also stated
explicitly. Failed fetches, incorrect identities, unresolved news without usable
analysis and provider failures continue to prevent strict readiness. These states
must not be collapsed into a generic claim that AI analysis was available.

Each API attempt still pushes its conservative reservation before HTTP. Successful
usage reconciliation is written locally and included in the next reservation or
ticker checkpoint; a crash before that push retains the larger remote reservation.
This reduces archive push frequency without allowing a crash to erase consumption.
Transient store push failures receive bounded retries of the same commit. Conflicts,
authorization failures and repository-policy rejections fail without a force push.

A manual collection before 19:00 Toronto does not consume that date's evening
scheduled slot. The evening refresh archives another version; later automatic
repeats remain idempotent. Both attempts consume the configured API budget, and
recovery never resets usage counters. Live acceptance before 19:00 checks the last
expected evening publication and accepts a newer same-day manual publication;
explicit `--business-date` verification remains exact.

## Internal inbox acceptance without a member roster

The **Internal email acceptance** workflow is manual-only and runs from `main`.
Its default `PREVIEW` mode validates a five-PDF cover note against fresh eligible
reports for CNQ.TO, CSCO, JPM, BMO.TO and COST. The only recipient is `GMAIL_USER`;
there is no recipient input. The synthetic greeting, public attachment names and
cover note are safe to review in the run output. Address headers stay in the
runner's temporary preview directory and are deleted without artifact upload.

Real inbox testing requires an explicit `SEND_ONE_TO_SELF` selection and separate
user authorization. It uses the same weekly sender, integrity checks and durable
ledger as team delivery. An accepted or uncertain submission will not be blindly
repeated in the same local week. The internal member ID is fixed and no real
member roster or global email switch is changed. There is no schedule trigger.
SMTP acceptance still needs a human confirmation that the message reached the
inbox. Leave `EMAIL_DELIVERY_ENABLED` false throughout internal acceptance.
