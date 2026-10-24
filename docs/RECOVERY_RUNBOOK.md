# Research and delivery recovery

Use current main, Python 3.12 and locked dependencies. Begin with read-only
inspection. Never reset either persistent branch, force-push, erase usage
reservations, or treat a new publication timestamp as fresh source evidence.
Commands below inspect a separately restored local archive; they do not authorize
production dispatches, sends or state edits.

## Determine what failed

Check the Actions job outcome, its summary and the stored `index.json:last_attempt`.
Record the Toronto business date, expected holdings, failed stage/category,
pending and degraded holdings, and the workflow run ID. A green skipped job does
not establish business completion. A running/interrupted stored attempt is not a
completed collection. Retain the failing run URL for diagnosis.

Run the strict archive check against the intended date:

```bash
python scripts/check_release.py --store /path/to/report-store \
  --business-date YYYY-MM-DD --require-ready
```

`health.json` counts the latest verified, nonhistorical report per expected ticker
for that date: `updated = ready + degraded`; `missing = expected - updated`.
Issuer advisories count as degraded. `failed` is a last-attempt outcome and may
overlap missing. `pending` is the union of missing/degraded/failed holdings and
the recorded pending list, restricted to expected holdings. An older report or
multiple versions cannot inflate current coverage. `last_attempt_at` and
`finished_at` are collection times; `published_at` is when the local site was built.
None proves Pages deployment, backup completion, SMTP submission or inbox delivery.
`last_complete_refresh` in the operational index also advances for degraded
collections; it is not a last strict-success timestamp.

## Research timeout, network errors or partial completion

1. Preserve the report-data branch and latest backup. Inspect `failures` and
   `stage_seconds` in the operational index. Distinguish stage timeout, shared
   prerequisite failure, budget exhaustion and persistence failure.
2. For transient provider/transport failures, check configured credentials,
   allowed destinations, provider availability and Retry-After. Do not weaken
   quality checks or repeatedly run probes that consume quota.
3. After correcting the cause, an authorized operator can dispatch the daily
   workflow with `resume=true`, `force=false` for the intended business date.
   The collector verifies same-day source quality, identity, hashes and PDF before
   reuse. Use the CLI's `--business-date` when recovering an earlier date; manual
   workflow dispatch otherwise selects its current Toronto date.
4. Recheck strict coverage. Resume archives new versions and retains history;
   `force` recomputes all holdings and is unnecessary for ordinary partial recovery.

The daily workflow has a work budget inside its step/job timeout. Its always-run
finalizer records an interrupted state only for its owned attempt. Cancellation
retains checkpoints and does not deploy. A completed daily workflow can trigger
an enabled member scan: obtain approval before using a production dispatch where
that side effect is not already authorized. Do not dispatch automatically during
an audit.

## Groq budget, HTTP 429 or invalid AI JSON

Inspect the sanitized error and UTC application-day usage state. Application caps
are not the provider's published allowances. Wait for the relevant budget window
and persisted Retry-After before an authorized resume; verify account limits
before changing caps. Keep durable request/token reservations. Never clear
`state/api-usage.json` to obtain more calls. Missing classifications remain
unclassified; failed AI work must not be rewritten as irrelevant news. Existing
bounded schema/coverage retries still consume the shared budget.

## Cache failure

Current SEC/price collectors refetch malformed caches and write atomically.
Identify the specific cache and error first. If a cache is still unusable, preserve
a copy outside the store before repairing that cache in an approved recovery.
Do not replace the whole state directory: it also contains quota and migration
state. Never delete report versions or sending history to repair a cache.

## Git persistence conflict

`concurrent_writer`, `repository_policy` and `authorization` are not automatic
transport retries. Stop the stale writer; retain its local commit. Fetch and
inspect both histories in a separate recovery checkout. Reconcile immutable
versions and retain all API/delivery reservations before any reviewed normal
fast-forward update. Do not force-push, silently rebase a sender reservation, or
retry SMTP after a failed persistence checkpoint. Transient transport failures
already have bounded retries; continuing failure needs investigation.

## Corrupt archive, PDF or failed site publication

A hash/contract/PDF failure blocks site replacement. Keep the last good site.
Compare the exact corrupt path with an intact report-data Git revision and its
backup. Restore reviewed original bytes from trusted history; generating a new
current report does not repair old immutable files. Validate the whole archive
before rebuilding. A renderer failure must not create a ready report.

For Pages errors, inspect build, upload, deployment and post-deployment checks
separately. Check Pages settings/permissions and the intended business date before
redeploying approved persisted state. Do not recollect all holdings to fix hosting.
After deployment, run:

```bash
python scripts/check_site.py --url https://OWNER.github.io/REPOSITORY/ \
  --business-date YYYY-MM-DD --require-ready
```

This checks actual public hashes/coverage; local build success is insufficient.
Confirm backup artifact creation/download and retention independently. A summary
or `health.json` cannot prove that a backup exists or is restorable.

## Delivery-state failure or sending/unknown

Follow [the guarded cutover and recovery contract](DELIVERY_SCHEDULING.md).
Preserve both branches and validated backups. Missing/corrupt ledger or migration
markers must fail closed, never become empty sending history. Current-main
preview mode can inspect due/deferred counts without SMTP; private `.eml` previews
must stay outside both stores and outside the public site.

A persisted `sending` reservation may already have reached SMTP. `unknown` is
also ambiguous. Neither is safe to resend automatically. An authorized operator
must inspect actual mailbox/transport evidence before using `delivery_state.py`
under its shared sender lock. Its `accepted` and `retry` resolutions change durable
behavior; they require explicit approval and preservation of the prior state.
Never choose retry solely because the workflow failed or the recipient has not
confirmed arrival. SMTP acceptance and inbox placement are different evidence.
