# Production review — 2026-10-23 Toronto

This is a point-in-time review, not a deployment certification. Source main was
`c4d0cb81aed7553f98d952bd30c24b4b5ea1e6cc`; the read-only report-data snapshot was
`19ab6475dd24e09595a563dc24df767733dda204`.

## Findings and priority

| Priority | Classification | Finding and evidence |
| --- | --- | --- |
| P0 | Confirmed Problem | Latest stored attempt for 2026-10-23 generated 50/50 reports but is `degraded`. V, VRTX and XYL snapshots report `Groq application daily budget exhausted`. Strict `check_release.check(..., require_ready=True)` rejects this date. This is an application budget limit; it does not establish a provider outage or the account's actual allowance. |
| P0 | Confirmed Problem | Before this fix, `build_site.build` copied the entire archive index, including unknown nested metadata, into the public site. A regression injecting synthetic member/credential data reproduced disclosure in index.json. No actual production disclosure was observed. The fix projects explicit public metadata fields, checks public value types and preserves immutable report bytes. |
| P0 | Already Resolved | PR #13 separated sender persistence and concurrency from research, introduced guarded migration and fails before SMTP on stale writers. Reviewed merge `8545cfd` and independent-delivery regressions; this is code/test evidence, not proof of production migration. |
| P0 | Already Resolved | PR #14 corrected sender backup staging paths (`ec66a18`). PR #15 added aggregate deferral reasons (`d20b136`). Both are present in current main; do not reimplement them. |
| P0 | Not Verified | Issue #16 contents, latest PR discussion, Actions scheduling, job logs, artifacts, live acceptance and Pages HTTP responses: API/Pages requests returned proxy 403. Stored workflow ID `40047255413` identifies the latest attempt but does not prove its Actions conclusion or deployment. |
| P1 | Potential Risk | health.json exposes counts taken from the last attempt but lacks explicit ready/missing/recovery counts. `last_complete_refresh` also advances for degraded runs; it means completed collection, not full source readiness. Do not interpret it as last strict success. |
| P1 | Potential Risk | GitHub cron/runner availability is best effort. The historical scheduling gaps documented in V1_ACCEPTANCE.md were not independently rechecked during this review. An external scheduler requires separate approval. |
| P2 | Not Verified | Current real AI/source authentication, account limits, SMTP login, inbox delivery and factual accuracy beyond the saved source/snapshot contracts require external verification. No API credentials were available; no live calls or sends were attempted. |

## Validation and recovery evidence

The exported production snapshot contains 273 versions (25 historical, 40 degraded,
208 ready across all dates). Archive contract/hash/PDF checks found no integrity
errors; strict daily acceptance fails solely for the three degraded holdings and
the degraded run status. Older degraded history remains preserved and visible.

A read-only `reusable_reports` evaluation returns 47 reusable ready same-day
reports and exactly V, VRTX and XYL pending. After checking the UTC application
budget and provider retry window, an authorized operator can use the current daily
workflow with `resume=true`, `force=false` and the intended business date. Do not
increase caps without verifying account allowances. No recovery workflow was
triggered here: a successful daily completion can trigger enabled member delivery.

Chromium smoke checks against a locally rebuilt copy of all 273 production
versions passed: report reading, filters, refresh, member CSV/JSON round trips,
start dates, rejected-import preservation and mobile layout, with no JS errors.
Synthetic members only; no actual roster was read or published. Local browser
success does not establish public deployment success.

The privacy regression first failed against main. The change also covers nested
hash metadata and malformed public values, preserving the previous site on error.
Public operational details not consumed by the website (raw failures, quota plans,
workflow IDs and per-stage maps) stay in the private operational index. Adding a
new public field now requires an explicit schema change and review. This boundary
covers index metadata; report content remains the existing validated public
research payload and must never contain private configuration.

## Remaining external acceptance

Read Issue #16 and recent Actions/PR records once read-only API access is available.
Verify migration and validated backup artifacts on both persistent branches.
After budget recovery, require a strict 50-holding release check, actual Pages
publication and HTTP hash verification for the intended Toronto date. Inspect
weekly delivery summaries without dispatching real sends. SMTP acceptance and
inbox placement remain separate outcomes. Keep these checks **Pending External
Verification** until direct evidence is available.

No production configuration, persistent branch, archived version or delivery
record was modified. No email, deployment, paid service or recovery dispatch was
initiated. This branch must be reviewed and merged before its code can affect
production; rolling back source does not require changing either state branch.
