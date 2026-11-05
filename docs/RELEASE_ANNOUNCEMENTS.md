# Verified release announcements

`config/release_announcements.json` is the reviewed source for the website's
What's new page and optional announcements in normal weekly digests. The initial
catalogue is empty. This change does not announce the Supabase portal or any
unverified capability, create a notification schedule or enable email delivery.

## Publication procedure

Add a draft with a stable ID, version, short title, one or two short summary
sentences, kind, audience and a public project link. Example (not a real release):

```json
{
  "schema_version": 1,
  "releases": [{
    "id": "example-release",
    "version": "example-version",
    "title": "Example draft",
    "summary": ["Replace this with a verified member-facing change."],
    "kind": "feature",
    "status": "draft",
    "audience": {"groups": [], "tickers": []},
    "url": "https://geochelone666.github.io/jsosif-ai-pipeline-demo/whats-new.html"
  }]
}
```

Only after the actual feature is deployed and accepted, add timezone-qualified
`deployed_at`, `verified_at`, and `evidence_url` pointing to this repository's
Actions run, then change status to `published` in a reviewed PR. Check the linked
run's deployment and actual HTTP/functional verification; a successful skipped
run or passing unit tests are insufficient. The loader enforces the record's
shape, timestamps and evidence-link origin; it does **not** query GitHub or prove
that the maintainer's deployment declaration is true. Reviewers own that evidence
check. Never put member data, credentials or raw provider error text in a release.

Draft, withdrawn and future-verified records appear neither in the public page nor
in mail. Use `withdrawn` to stop future selection of a problematic announcement;
it cannot recall mail. Keep IDs stable and do not reuse them for different content.
Material corrections need a new reviewed ID and explanation. Preserve old release
records and delivery reservations so audit and deduplication remain meaningful.

Kinds: `feature`, `report_structure`, `data_correction`, `delivery_policy`, and
`maintenance`. Maintenance notes can appear on the website but are excluded from
mail. Empty audience lists target all members; otherwise a matching group OR
subscribed ticker qualifies. Group names in this public catalogue must refer only
to public research teams, never personal roster labels. The website shows all
published release descriptions but omits audience targeting and delivery records.

The public destination is limited to the reviewed project website. Text is escaped
in HTML. The static page works without JavaScript and supports desktop/mobile
navigation from the research homepage. Site builds stage the page alongside the
archive; a malformed catalogue preserves the previous site output.

## Normal weekly mail only

The sender selects at most two relevant, unseen announcements after finding
eligible reports. Each has at most two short summary lines. It renders the same
content in plain text and HTML, retains report attachments and the original
weekly deduplication. Reports that are stale, missing, corrupt or otherwise
ineligible defer the entire digest, including its announcement. Announcement
availability does not create a send, bypass participation or change a due time.

Private preview mode shows the prospective content without recording receipt or
reserving a slot. It may repeat while reviewing. A real send reserves its report
IDs and announcement IDs together in the existing sending reservation, persisted
before SMTP. Publication does not send messages to anyone by itself.

Optional `announcements` and `announcement_recipient` fields extend the existing
reservation. The recipient field is a namespaced hash of the stable member ID;
no raw IDs, emails, names, audience membership or message bodies are added. A
stable hash links announcement history across weeks; use unguessable member IDs
as already required for private identifiers. The site builder never publishes
these ledger fields.

`accepted` means SMTP accepted the digest, not confirmed inbox receipt. `sending`
and `unknown` mean it may have been submitted. All three suppress those
announcement IDs for the same member in later weeks. Existing mailbox-based
reconciliation retains these fields when marking accepted; an explicitly approved
retry removes the original reservation and allows a retry. Do not clear records
to resend an announcement. A checkpoint failure prevents SMTP, and concurrent
sender protection remains the independent delivery-state writer lock/push rule.

## Activation and rollback

Empty catalogues leave existing reservation shapes unchanged. Upgrade all sender
and ledger-reader revisions before adding the first published announcement;
older readers intentionally reject the extended record. Drain older sender jobs
before activation. Production publication and sends still require the existing
approvals. No live catalogue entry or delivery record was created in development.

Once extended reservations exist, do not roll back to a reader that only accepts
the old shape. Disable future announcements by withdrawing entries or using an
empty catalogue while retaining the compatible ledger reader. Preserve every
reservation, including uncertain ones; deleting optional fields would lose
announcement deduplication. Source rollback never requires resetting report-data
or delivery-state.

## Validation

```bash
PYTHONPATH=scripts python -m pytest --import-mode=importlib -q
python scripts/build_site.py --store report-store --output site-build
BROWSER_EXECUTABLE=/path/to/chromium python scripts/browser_smoke.py \
  --site site-build --artifacts review/browser
```

Tests cover publication gating, future dates, evidence/link validation, relevant
audiences, bounded content, legacy and extended ledgers, HTML escaping, previews,
report-quality deferral, pre-SMTP reservation, uncertain outcomes and preservation
of the previous site. Browser checks cover desktop/mobile navigation and overflow.
All test members and release records are synthetic; no real email is submitted.
