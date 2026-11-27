# Private member attachment review

`scripts/member_attachment_preview.py` prepares private `.eml` files and a
`review.json` selection record from an offline member configuration, verified
stock archive and optional sector, macro and news draft bundles. It has no send mode, network
request, subscription-authority call, ledger read/write or production integration.
Every record has `delivery_ready: false`; the subject says REVIEW ONLY / DO NOT SEND.

```sh
python scripts/member_attachment_preview.py --config /private/members.json \
  --store /path/to/report-store --sector-bundle /path/to/sector-drafts \
  --at 2026-11-14T06:00:00Z --include-sector-drafts \
  --output /private/new-review-directory
```

The review time must be explicit and timezone-aware. It controls historical
eligibility; it does not assert current member consent or current data freshness.
Use a securely obtained offline configuration. This tool must not be treated as
proof of authorization to send, or as a substitute for the sender's fresh authority
check, reservation, uncertain-outcome handling and schedule/consent checks.

## Selection semantics

- Reuse existing member validation, timezone schedule, report-age/quality gates,
  report advisories and original archive/source checksums.
- Enabled members are considered only when due. `--preview-all` bypasses schedule
  and delivery-start-date checks for review; it never bypasses pause.
- Nonempty personal tickers override group holdings, matching the current sender.
  Otherwise use the deduplicated union of group holdings. Private group names or
  IDs are not assumed to equal the research taxonomy.
- Stock PDFs remain the base digest. A missing/ineligible required stock defers
  the entire member preview, rather than silently omitting that holding.
- `content_preferences.sector_brief` must be explicitly true to select sectors
  covering those effective holdings. Missing/false preferences add none. Several
  stocks in one sector add that sector once.
- Current sector artifacts are drafts. They additionally require the explicit
  `--include-sector-drafts` review switch; otherwise the plan lists the unmet
  request. Drafts must fit the report-age window and match the selected stock
  report version IDs. A mismatch is disclosed, not silently mixed.
- `macro_overview` can independently select a verified standalone macro draft via
  `--macro-bundle` and `--include-macro-drafts`. It requires its own explicit true
  preference, age checks and matching stock report IDs/dates/snapshot hashes.
  The sector draft switch cannot enable it. Missing or rejected macro drafts are
  disclosed as gaps. See [MACRO_OVERVIEW.md](MACRO_OVERVIEW.md).
- `news_catalysts` requires its own explicit preference and `--include-news-drafts`
  with `--news-bundle`. Age and stock ID/date/snapshot hashes must match. It adds
  one news draft; default scope is archive-wide. `--news-scope selected-stocks`
  projects it using effective holdings, with private scope metadata and no new
  relevance inference; see SCOPED_NEWS_PREVIEW.md and NEWS_REVIEW.md.
  Missing or ineligible news remains an unmet request.
  Macro context embedded in a sector document is not claimed to satisfy a standalone
  macro subscription. Selecting a sector document selects its whole contents.
- Unknown preference names and nonboolean values fail closed, including legacy
  configs not previously subjected to the backend's stricter preference checks.
- Final attachments are deduplicated by PDF SHA-256 per member. When multiple
  logical references share bytes, their identities remain in the selection record.
  No cross-member, cross-week or prior-delivery deduplication is claimed.

## Integrity and size handling

The optional bundle must contain all eight completed draft records, valid filename
identities, full PDF/JSON checksums, companion fingerprints, the same dataset/date,
and coverage matching the current configured research taxonomy. Captured PDF bytes
are structurally checked and retained for MIME assembly, avoiding a later unchecked
file read. Stock PDF bytes are rehashed after original archive verification.
Duplicate archive report identities fail closed. Checksums establish local artifact
consistency, not publisher identity or production acceptance.

Input reads are bounded: member configuration and each sector JSON at 2 MiB,
the growing archive index at 32 MiB, and individual PDFs at 20 MiB. An oversized
input fails explicitly rather than being partially parsed or attached.

The exact SMTP-policy MIME byte length is checked against the existing **20 MiB**
message cap, including headers, base64 expansion and boundaries. A review exceeding
the cap writes a `deferred_size` plan but no `.eml`. It does not truncate attachments
or invent a public link. The record explicitly states that link fallback requires
an approved access-control design. Pure Python tests may use a lower cap; a higher
cap is rejected. There is no CLI option to raise it.

Messages use a deterministic boundary and Message-ID for identical review inputs,
which permits byte-level reproduction. These are preview identities, not delivery
idempotency keys. No `From` header or SMTP credentials are added.

## Private output and failure behavior

The CLI requires a new directory outside the report store, sector/macro/news bundles and source
repository. Directory mode is 0700 and every file is created exclusively with mode
0600. Existing directories, files and symlinks are never overwritten. `review.json`
is written last; a directory without it is incomplete. Logs contain no member
names, IDs, addresses, holdings or message bodies. The review record uses hashed
member/period keys; this is an identifier convention, not an anonymization promise.
The `.eml` files contain recipient information and must remain private.

No existing `sending`, `unknown`, accepted-delivery record or budget reservation is
consulted or changed. Consequently an offline preview can be produced for a member
whose real weekly delivery has already occurred or is uncertain. Never pass these
previews to SMTP or infer that they are safe to send.

## Validation and remaining work

Tests exercise overlapping holdings, personal overrides, separate recipients,
explicit content consent, pause/schedule behavior, draft opt-in, version/future-date
rejection, unsupported content, checksums and altered coverage, MIME boundary/size
limits, retained bytes, private file modes, no network or input/ledger mutation,
and deterministic output. Real-archive acceptance uses synthetic members only.

Still pending: complete/live-accepted sector, macro and news intelligence,
authorized sender integration with fresh authority and ledger gates,
controlled private downloads, expiry/access checks, and end-to-end team acceptance.
This candidate does not enable these features in production.
