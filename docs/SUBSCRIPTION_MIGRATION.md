# Private legacy migration review tool

`scripts/subscription_migration.py` creates an offline SQL review for a **fresh,
unused subscription authority** after the three schema migrations and active
catalogue seed. It never connects to Supabase, imports real members, sends email,
changes the sender backend or edits delivery history. An initialized authority
with member settings, save requests or security requests is refused; this is not
an admin correction or incremental sync tool.

## Inputs and private output

Use a private legacy JSON configuration plus an optional CSV in the existing
member import format. Preserve every legacy `id` exactly. Prepare a separately
reviewed JSON array with one entry per member:

```json
[
  {
    "member_id": "synthetic-legacy-id",
    "user_id": "00000000-0000-0000-0000-000000000001",
    "email": "analyst@example.com",
    "approved": false
  }
]
```

The example is synthetic. Obtain actual UUIDs through the authorized private
Auth inventory and review identity matching and team approval separately.
`approved` is required and never inferred from email verification or subscription
participation. An unapproved imported member is preserved but excluded from the
sender snapshot. Even paused/unapproved records require a verified matching Auth
identity; unresolved identities block the complete import instead of being skipped.

```bash
python scripts/subscription_migration.py \
  --config /private/path/subscriptions.json \
  --identities /private/path/reviewed-identities.json \
  --expected-revision 1 \
  --output /private/path/new-migration-review.sql
```

Optionally add `--members-csv /private/path/members.csv`; its complete roster
replaces the JSON roster in memory only. The source files are never changed.
The output contains private identities/preferences: retain it outside the Git
checkout, public artifacts and Pages. It is created mode 0600 and refuses existing
files/symlinks. Console output contains counts or a sanitized error, not member
values. No credentials are needed for generation.

Unknown nonempty member fields (feedback, legacy scheduling hints, prose content
preferences) stop generation. Resolve their meaning explicitly and retain their
original private export; the tool does not silently drop them. Supported content
preferences must be boolean fields in the JSON roster. Stable IDs, opt-outs,
start dates, personal holdings, groups and the shared delivery policy are retained.

## Review and authorized execution

1. Recheck the actual team's read-only inventory and backups. Read the current
   settings revision privately; do not assume it is still 1. Apply only missing
   schema migrations via the approved route. The tool does not apply migrations.
2. Review the entire private identity map, explicit approvals, policy and SQL.
   Its transaction rechecks the expected settings revision, absence of existing
   authority activity, compatible existing approvals, actual verified Auth emails
   and active catalogue coverage. Bounded lock/statement timeouts fail closed.
3. The generated SQL **ends with ROLLBACK**. In a disposable or explicitly approved
   staging database, execution proves preconditions without retaining member or
   approval changes. It prints counts only. It is still a write transaction during
   rehearsal, so do not run it on the team project without authorization.
4. Only after explicit import authorization and review, change the final ROLLBACK
   to COMMIT in the private reviewed copy and execute through the approved operator
   connection. Record the operator, private file checksum and acceptance evidence
   in the team's private change record. The tool has no automatic `--apply` option.
5. Confirm IDs, opt-outs, approvals and policy using a private service snapshot and
   sender preview against restored archives. Keep `SUBSCRIPTIONS_BACKEND=legacy`
   until the separate source-switch authorization and acceptance are complete.

The whole import commits once or rolls back. Re-running a committed plan fails the
revision/unused-authority guards; it never overwrites later member edits or changes
identities to UUIDs. Do not reset tables or ledgers to bypass these checks. Member
correction and named-operator audit now have a separate local candidate in
[SUBSCRIPTION_ADMINISTRATION.md](SUBSCRIPTION_ADMINISTRATION.md). Incremental
migration remains pending.

## Verification

Python tests cover exact ID/opt-out preservation, lossy/ambiguous maps, duplicate
Auth identities, content types, revision limits, private output and sanitized
errors. `tests/sql/migration_review.py` executes generated SQL against synthetic
Auth users in a fresh disposable PostgreSQL database. It verifies default rollback,
identity/verification/catalogue/revision failures, quoted content, explicit approval
visibility, stable IDs and refusal to overwrite. CI uses a separate test database.
These are local/CI implementation checks, not team-project import acceptance.
