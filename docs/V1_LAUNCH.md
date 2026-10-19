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
| `GROQ_MODEL` | Optional variable | Defaults to `llama-3.1-8b-instant`; verify account availability |
| `GROQ_RPD`, `GROQ_RPM` | Optional variables | Application request caps, defaults 100/day and 10/minute |
| `GROQ_TPD`, `GROQ_TPM` | Optional variables | Application token caps, defaults 100,000/day and 5,000/minute |
| `SEC_USER_AGENT` | Variable | Organization and real contact email for SEC requests |
| `PAGES_DEPLOY_ENABLED` | Variable: `true` | Enable the Pages deployment step |
| `SUBSCRIPTIONS_JSON` or `MEMBERS_CSV` | Secret | Private roster and research choices |
| `GMAIL_USER`, `GMAIL_APP_PASSWORD` | Secrets | Required only for real email delivery |
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
conservative UTF-8 byte bound plus completion allowance. Successful calls reconcile
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
  `llama-3.1-8b-instant`, `response_format` and `max_completion_tokens`.
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
