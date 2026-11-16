# Named administrator corrections — local candidate

This candidate adds verified, explicitly authorized Auth administrators and a
private inspect/review/apply CLI. It has not been installed on the team project.
It does not send mail, switch the sender backend or publish the portal. A hosted
admin page and real Supabase session acceptance remain pending.

## Migration and authority

Apply `202611150001_subscription_administration.sql` **after** the authority,
options and security-request migrations, only through the separately authorized
migration route. Earlier installations apply only this missing migration; do not
rerun older installation scripts. The transaction creates private administrator
membership and audit tables, extracts the existing preference checks into one
shared validator, and replaces the member save RPC with equivalent validation
plus a post-lock approval recheck. Member subscriptions, IDs, Auth emails, source
archives and delivery ledgers are preserved.

A database operator must separately review each real administrator's verified
Auth UUID and insert it into `subscription_private.administrators`. No member RPC,
CLI plan or service-key function can grant administrator membership. Empty admin
membership is the default. Normal approved team membership does not grant admin
access. Unverified or revoked administrators cannot inspect, correct or retry.

All new private tables have RLS and explicit grants replacing project defaults.
Authenticated users have no direct table access. The service role has read-only
access to these tables and cannot call the admin RPCs; they require a real verified
Auth administrator identity. The privileged database owner remains a trusted
operator and can bypass application restrictions. This is not tamper-proof audit
against the database owner.

## RPC contract

- `get_admin_subscription(p_user_id)` reads one account by exact Auth UUID,
  including its current preferences, stable member ID, version, approval state,
  verified-email state, allowed groups/tickers and the verified operator UUID.
- `correct_admin_subscription(...)` requires target UUID, desired approval,
  expected member version and approval, request UUID, a nonblank reason, expected
  operator UUID, and either complete desired preferences or SQL null to preserve
  preferences. The operator is derived from Auth; the expected operator prevents
  a plan being silently applied by a different administrator.
- `get_admin_subscription_history(p_user_id)` returns at most the latest 50
  private events for that account. Each records actual operator UUID, target,
  request UUID, reason, before/after state and database time. History is not exposed
  to members or public site assets. A complete archival audit export remains an
  operator task, not this bounded interactive view.

Corrections never change `member_id`, Auth identity/email, catalogue securities or
administrator membership. Preferences use exactly the same validator as self-service
saves, including active securities, known groups, schedules and boolean content
preferences. Only existing subscription rows can receive preference corrections.
For a new verified user, an approval-only change is supported; the user then saves
their own subscription, or a separately reviewed legacy migration preserves their
old ID. Approval alone does not create a subscription or opt someone into mail.

Reapproval preserves the current pause setting. Unverified targets cannot be
approved or edited, but their existing approval can be revoked. No-op corrections
are refused. Each accepted operation updates the sender settings revision, and
existing member rows receive a new version even for approval-only changes. The
audit event and state changes commit together. Member/admin concurrent edits
serialize through the existing settings lock and reject stale expected versions.

An exact retry with the same actor/request UUID and identical input returns the
original result without another write or audit event. Changed input with that ID
fails. The receipt describes that original operation; it is not proof the account
has remained unchanged since. Revoked administrators cannot retrieve retry results.
Administrator revocation waits for already-running operations holding their role
lock; it blocks subsequent calls, not operations already authorized in flight.

## Private CLI workflow

Configure `SUBSCRIPTIONS_SUPABASE_URL`, the public
`SUBSCRIPTIONS_PUBLISHABLE_KEY`, and a short-lived `SUBSCRIPTIONS_ADMIN_TOKEN`
through a secure local environment/session mechanism. The token must belong to a
verified administrator; a service key is not a replacement. Tokens remain in
process memory/environment and are not written to plans, receipts or console.
Do not paste tokens into chat, CLI arguments, source files or public artifacts.

1. After authorization to inspect the account, read its private current state:

   ```bash
   python scripts/subscription_admin.py inspect \
     --user-id 00000000-0000-0000-0000-000000000001 \
     --output /private/path/new-inspection.json
   ```

   The UUID is synthetic. History is read separately after the state; it is
   supplementary context, not an atomic snapshot with the versioned state.

2. Prepare a correction **offline** from the private inspection. Write the reason
   in a private UTF-8 file. To revoke approval without changing preferences:

   ```bash
   python scripts/subscription_admin.py prepare \
     --inspection /private/path/new-inspection.json --approval revoke \
     --reason-file /private/path/reason.txt --output /private/path/new-plan.json
   ```

   For preferences, add `--preferences /private/path/desired-preferences.json`;
   the file must contain the full desired preference object. Approval defaults
   to `keep`; use `approve` or `revoke` explicitly to change it. Review the entire
   plan, including desired participation, schedules, expected state, target,
   operator and reason. Server validation remains authoritative at application.

3. Only after actual mutation authorization, explicitly apply that reviewed plan:

   ```bash
   python scripts/subscription_admin.py apply --plan /private/path/new-plan.json \
     --receipt /private/path/new-receipt.json
   ```

   There is no automatic apply during prepare and no automatic network retry.
   Application rejects a different project URL or operator. A private `unconfirmed`
   receipt is reserved before dispatch. A lost response leaves it unconfirmed:
   retain the original plan, inspect privately, and if retrying use the same plan
   with a new receipt filename. Do not generate a new request ID to retry an
   uncertain outcome. A version/approval conflict instead requires a fresh
   inspection and newly reviewed correction.

Outputs are new mode-0600 files and refuse overwrite/symlinks. Keep them outside
the checkout, public artifacts, report-data and Pages. API calls use bounded
response sizes/timeouts, the existing redirect-rejecting transport, and sanitized
errors. A confirmed receipt is a database RPC result, not email-delivery evidence.

## Verification and remaining acceptance

The standard SQL fixture now applies all four migrations and tests normal member
contracts plus administrator isolation, inherited privileges, unverified/revoked
denial, shared validation, immutable IDs, version/approval conflicts, exact retries,
approval-only behavior, opt-out preservation and named audit records. Additional
concurrent tests prove one-writer behavior, one event for concurrent exact retries,
and rejection of both a queued member save and an old request replay after revocation.
A disposable negative-control database without the post-lock approval guard fails
this concurrency regression, while the final migration passes it.

CLI tests use synthetic HTTP/RPC responses and private temporary files, including
lost-response receipts, exact retry identity, project binding and credential/error
handling. No real account was inspected or changed. Real Auth/JWT acceptance,
operator onboarding, permission review, backup/restore and end-to-end sender
read-back remain required before enabling this workflow on the team project.
