# Team Supabase subscription authority — Phase 1 foundation

Status: implementation for review, disabled by default. The team will provision
Supabase. No project, real user, auth email, roster migration or live sender switch
has been created by this change. The existing members.html remains a local roster editor. The new subscriptions.html
implements the authenticated portal against the RPCs, but defaults to disabled
and has only passed isolated browser tests so far.

## Implemented contract

Before applying anything to the team project, run `supabase/preflight_readonly.sql`
in its SQL Editor and review all returned metadata. It reads aggregate Auth/Storage
counts without selecting member identities or credentials. A Dashboard reporting
no public tables does not establish that all schemas are empty.

The candidate migration in `supabase/migrations` assumes Supabase-managed
`auth.users`, `auth.uid()` and standard roles. Preferences live in the unexposed
`subscription_private` schema. A member can read only their own row through RLS;
there are no member INSERT/UPDATE/DELETE table grants. Writes go through
`save_my_subscription(p_preferences, p_expected_version, p_request_id)` with the
verified identity derived server-side and an explicit team approval. Email
confirmation alone does not grant access, even when Auth signup is enabled. An
administrator must add the verified user UUID to the private `approved_members`
table through a reviewed server-side operation. Members cannot approve themselves.
Removing approval blocks preference reads/writes and excludes that member from
subsequent sender snapshots; preserve their settings and sending history. The client cannot choose a member ID,
email or another user's ID. Email comes exclusively from verified Auth records.

`get_my_subscription()` returns preferences, version and update time, or null for
a new member. The save RPC returns the new version/update time. A new member uses
expected version 0. Each save uses a fresh UUID request ID; a transport retry uses
the same ID and identical payload/version. Reusing an ID with different input
fails. A stale version fails, so clients must reload and review the current values
before resubmitting rather than overwriting someone else's changes silently.

Supported preferences: name, email participation, known groups/active securities,
IANA timezone, weekday (Monday=0), HH:MM, optional start date and the boolean
`sector_brief`, `macro_overview`, `news_catalysts` content preferences. Content
preferences are stored for the next development stages; they do not imply that
Sector/Macro reports are generated or attached yet. Unsupported symbols are
rejected; the requested-security onboarding queue is still to be implemented.

`subscription_snapshot()` is executable only by the server service role. One
statement exports verified Auth emails, stable member IDs, preferences and policy
from a consistent database view, with schema version, revision and generation time.
It contains private data: never upload its output to Pages, artifacts or either
public state branch. Server credentials must never enter browser configuration.

## Python/Actions integration

The default `SUBSCRIPTIONS_BACKEND=legacy` preserves existing JSON/CSV loading.
Only an approved explicit switch to `supabase` selects the new authority:

| Setting | Location | Purpose |
| --- | --- | --- |
| `SUBSCRIPTIONS_BACKEND` | Actions variable | `legacy` (default) or `supabase` |
| `SUBSCRIPTIONS_SUPABASE_URL` | Actions variable | Exact HTTPS project URL ending in `.supabase.co` |
| `SUBSCRIPTIONS_SERVICE_KEY` | Actions secret | Server-side Supabase secret key or legacy service-role JWT for the RPC |

Both daily research and weekly delivery use `prepare_subscriptions.py`. In
Supabase mode the loader ignores legacy secrets, validates the returned schema,
member configuration and timestamp, and writes a mode-0600 local snapshot.
Network, credential, schema or size errors stop the job; there is no fallback to
an old Secret. HTTP redirects are rejected and TLS validation remains enabled.
Both legacy service-role JWTs and new `sb_secret_` server keys are supported by
the adapter. Opaque secret keys are sent only in `apikey`, not as JWT Bearer tokens;
new Publishable keys are rejected for private snapshots. Validate the actual key
route on the team project before activation. Custom Supabase domains remain unsupported.

Immediately before each real delivery reservation, the sender rechecks authority
revision and configuration digest. An opt-out, email change, edit or outage aborts
before that reservation/SMTP call. Earlier accepted sends in the run retain their
ledger entries. Restart with a fresh snapshot after resolving the cause; normal
weekly deduplication still applies. Any member's edit conservatively invalidates
the full frozen snapshot. This is bounded fail-closed behavior, not a distributed
transaction with SMTP: a change after the final check cannot retract a submission
already in flight. The UI must describe pause as stopping future submissions.

Preview mode uses the frozen snapshot without SMTP or a send reservation. A
preview is not evidence that a future send will use the same configuration.
`report-data` and `delivery-state` remain independent; reservation formats and
existing weekly member IDs are unchanged.

## Team project preparation and cutover (not executed)

1. Confirm team ownership, hosting region, data handling/access policy and backup
   retention. Configure Supabase Auth email verification, allowed redirect URLs,
   email change confirmation/security notifications and rate limits. Verify actual
   JWT/session handling in staging; local SQL tests emulate identity claims only.
2. Apply the migration once to the approved project and load the reviewed
   `supabase/seed_securities.sql` catalogue. Expose only public RPCs to PostgREST;
   do not add `subscription_private` to exposed schemas. Configure private policy
   and known groups in the singleton settings row; increment its revision with
   administrative policy changes. Python validates all exported policy/groups.
3. Before opening registration, stage the private JSON/CSV migration. Match each
   legacy member to a verified Auth identity using an administrator-reviewed map;
   copy the existing member `id` into `member_id` exactly and separately approve
   the verified user UUID in `approved_members`. Do not replace it with an
   Auth UUID for migrated members: that would bypass old weekly reservations.
   Import preferences/policies through a reviewed server-side migration and verify
   counts, disabled states, start dates and IDs without printing member values.
   An automated importer/admin portal is not included in this foundation.
4. Build and test the authenticated settings page against staging: signup, login,
   session expiration, cross-user denial, retries, version conflicts, email changes,
   opt-out and settings read-back. Do not enable the existing portal announcement
   until these flows actually work. The database RPCs alone are not the portal.
5. Validate a service snapshot with `prepare_subscriptions.py` and run the actual
   sender in preview mode against a restored archive/independent ledger. Verify
   a pause/config edit blocks reservation and preserves all prior sends.
6. Obtain explicit approval for the production source switch. Stop/drain any old
   sender using a legacy snapshot before switching; update both workflows together.
   Keep an encrypted/private recovery export. Legacy JSON/CSV is recovery-only,
   not an actively maintained second authority. Never reset the delivery ledger.

Rollback after member edits requires a reviewed fresh export back to legacy
format, preserving member IDs and current opt-outs. Do not point the sender at
stale pre-migration Secrets. Source rollback before activation simply leaves the
legacy workflow in place. Preserve both persistent branches in either case.

## Reproducible validation

Python regressions (standard locked Python 3.12 environment):

```bash
PYTHONPATH=scripts python -m pytest --import-mode=importlib -q
```

Database regressions require a fresh disposable PostgreSQL 17 database and a
privileged test connection configured through the normal PG* environment variables:

```bash
psql -X -v ON_ERROR_STOP=1 -f tests/sql/subscription_authority.sql
python tests/sql/concurrent_subscriptions.py
```

The SQL fixture creates synthetic Auth users/roles and applies the real migration.
It checks anonymous/unverified denial, RLS isolation, forbidden direct writes,
server-controlled email, active-security validation, idempotency, version conflicts,
pause/export agreement and stable migrated IDs. Two concurrent connections then
prove one stale writer is rejected. Use a fresh database for each run; the fixture
must never run against a real Supabase project. CI runs it in its own PostgreSQL
service. Python tests exercise private files, authenticated requests, stale snapshots,
no legacy fallback, email/opt-out changes and failure before ledger mutation/SMTP.

## Remaining 2.0 stages

Phase 1 still needs actual hosted authentication/email-change acceptance,
reviewed roster migration/admin correction, security acceptance on the actual
Supabase project, unsupported-security requests and deployed release announcements.
Phase 2 then establishes shared Sector/Macro/Peer data; sector briefs depend on
those verified sources. Keep the existing report integrity, quota and email gates
throughout. No live capability is announced by this foundation.

## Configuration handoff follow-up

The team's Dashboard handoff reports a Production project, no public tables and
conflicting Auth counts. Do not classify it as empty or run migrations until the
read-only inventory is reviewed. The supplied Publishable key is not a service
credential. Development cloud variables and GitHub Actions settings must be
configured separately; keep `SUBSCRIPTIONS_BACKEND=legacy` until approved cutover.
The current exact redirect targets the research homepage; add the precise verified
portal callback only when its implementation is ready. An open Auth signup switch
does not bypass the database's explicit team-approval requirement.

## Browser portal candidate

The build always includes subscriptions.html and subscriptions.js, with a disabled
portal-config.json by default. The current deployment workflows do not enable it.
For staging only, supply `--portal-config /private/path/portal-public.json` to the
site builder, containing exactly `enabled: true`, the HTTPS Supabase `url`, and a
`publishable_key` starting with sb_publishable_. No service/secret key is accepted.
Apply the second subscription_options migration after the authority migration.
It returns active tickers and group options only to approved authenticated members.

The browser requests email codes, verifies them with Auth and calls own-member
RPCs with the returned session. Tokens live only in memory and expire locally
within one hour; there is no localStorage/sessionStorage persistence. Reloading
the page requires sign-in again. Preferences use expected versions and retained
request IDs for ambiguous retries. Version conflicts require an explicit reload.
Email change requests go to Auth, not preference rows; real secure double-confirmation
behavior must be verified on the team project. The exact callback must be added
to the project's allowlist before live email-change acceptance.

Do not advertise the portal as launched based on mock tests. Run
`BROWSER_EXECUTABLE=/path/to/chromium python scripts/subscription_browser_smoke.py
--site site-build` for isolated tests; every Auth/RPC request in this test is
intercepted, and no real email or database mutation occurs.
