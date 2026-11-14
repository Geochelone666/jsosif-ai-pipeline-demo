# Security request queue

Implemented locally for the existing personal repository and team Supabase
architecture. No team database migration, portal deployment or real request has
been performed. The default portal remains disabled.

## Deployment order

Apply `202611110001_security_requests.sql` after the authority and options
migrations, through the reviewed migration route. The new portal requires all
three migrations. Do not rerun the authority migration against an already
initialized project. The queue migration is transactional and preserves existing
subscriptions, settings revisions, securities, report archives and delivery ledgers.

The portal allows an approved, email-verified member to submit a provider ticker,
a four-character exchange MIC and a short reason. MIC syntax is checked; actual
exchange/listing identity is a reviewer responsibility. Each member has one request
per normalized ticker/MIC pair, with at most 20 pending or reviewing requests.
Repeating a request returns its original identity, reason and state, including
when a previous response was lost. Resolved requests remain visible; resubmission
does not reopen or edit them. A future appeal workflow can be added separately.

Members can read only their own requests. Approval revocation prevents subsequent
reads and submissions. Review notes are member-visible and rendered as plain text.
Neither requests nor an `available` decision add anything to a subscription.
The member must select an active ticker and save preferences separately.

## Backend review

A privileged operator can inspect the private queue using the team's reviewed SQL
connection or SQL Editor. These are operational examples, not setup commands to
run automatically, and must not be put in public site assets:

```sql
select id, ticker, exchange_mic, reason, status, version, created_at
from subscription_private.security_requests
where status in ('pending', 'reviewing')
order by created_at, id;
```

Use `public.review_security_request(p_id, p_expected_version, p_status, p_note)`
through a server-only service credential or the authorized SQL connection. Supply
the actual UUID and version from the reviewed row. Valid decisions are `reviewing`,
`rejected` or `available`; pending and reviewing requests can be resolved directly.
Resolved requests cannot be edited or reopened. A stale review fails; an exact
retry of the last accepted decision returns the same result. Every accepted review
adds one append-only audit row via this RPC. Member credentials cannot execute it
or read review history. The service role receives read access to queue/audit tables
and execute access to the review RPC, not direct mutation grants on these tables.

Before selecting `available`, the operator must check:

- Exact company, listing, exchange MIC, provider symbol and reporting currency.
- Source availability, freshness, required coverage and report quality gates.
- Expected collection cost and the existing quota/reservation policies.
- Independently approved addition to the canonical active-security catalogue and
  research coverage configuration, with normal pipeline acceptance.

The RPC enforces that the ticker already exists in the active catalogue. It does
not prove listing/MIC identity, provider quality or budget acceptance; those remain
manual gates until the validated onboarding workflow is implemented. It never
inserts a security or changes member preferences. Keep the reason for rejection
or the remaining review steps in the member-visible note (maximum 1,000 characters).
The audit records decision/version/time, not an individual operator identity when
operators share a service credential; named-operator administration remains pending.

## Verification

`tests/sql/subscription_authority.sql` includes the queue's migration and isolation,
validation, quota, retry, review audit, stale-version, non-activation and revocation
checks. Run only in a fresh disposable PostgreSQL database. Then run
`tests/sql/concurrent_subscriptions.py` in that same database for competing updates,
request quotas and duplicate retries. CI already invokes both entry points.

`subscription_browser_smoke.py` checks submission after a simulated lost response,
progress refresh, unknown-stock rejection, unchanged subscription settings, plain
text rendering of review notes, clearing request data on logout and discarding
responses that arrive after session expiry. All Auth/RPC
responses are synthetic; no live email or Supabase requests are made.

## Recovery and local acceptance — 2026-11-14

The cloud workspace was unavailable locally and the queue branch had never been
pushed. The two added SQL files and inspected edit scripts were recovered from
the previous chat's recorded changes on top of `de4dede`; this is recovered source,
not a claim that the old working directory was copied. The final cloud browser
run had failed because advancing one hour also fired the 20-second request timeout.

The regression now uses a one-second synthetic session and advances 1,001 ms.
Late successful, conflict and network-error responses leave the account cleared;
sign-in works afterwards. Removing the response guard from a disposable site
copy reproduces the reopened-account failure. Table grants also explicitly revoke
inherited service-role mutations before granting read/review access; the SQL fixture
tests permissive defaults. CI retains subscription and shared-research screenshots.

Local acceptance: 1,065 Python tests and 57 subtests; PostgreSQL 17 isolation,
review and concurrent quota/retry checks; mocked Chrome portal checks; a site
build from 25 repository historical samples. These results do not establish real
Supabase authentication, migration, email delivery or production acceptance.
