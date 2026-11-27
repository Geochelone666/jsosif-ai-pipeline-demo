# Standalone news review draft and private attachment preview

`scripts/news_review.py` builds a four-page PDF, a complete JSON companion and a
manifest from the verified news evidence index. It makes no provider/model call,
does not rewrite historical classifications and never enables production sending.

```sh
python scripts/news_review.py --store /path/to/archive --as-of 2026-11-13 \
  --output /path/outside/repository-and-archive/new-news-draft
```

## Review layout and evidence

1. Archive/source counts, missing/conflicting predictions, publication metadata gaps
   and explicit limitations, with evidence and companion fingerprints.
2. The first four dated RSS identities at or before the cutoff, newest first.
3. The next four eligible identities, or an explicit absence message.
4. All 50 configured stocks, with per-stock reference and prediction-gap counts;
   missing/malformed RSS and absent reports have distinct markers.

This is an archive-wide chronology, not a personalized selection or importance
ranking. A member's holdings need not occur among the eight displayed stories.
Future/undated metadata is excluded from that bounded chronology but retained in
the companion. Older dated news may appear with its actual age; no current-news
readiness is claimed. Full original headlines, links, source hashes, all report
contexts and saved predictions remain in JSON. Source links are clickable HTTPS
references, not independent claim verification.

PDF text uses ASCII display normalization. Long headlines/publisher labels and
prediction context are explicitly marked `[shortened]`; JSON remains complete.
Publication timestamps never become event dates. Every artifact is retrospective,
`draft_incomplete_evidence`, `delivery_ready: false`, and ineligible for point-in-time
backtesting. A saved catalyst or calendar classification does not establish a
verified catalyst, earnings date, causal explanation or investment recommendation.

The companion retains the entire news index and its fingerprint, plus deterministic
selection, coverage totals and stock snapshot lineage. The validator checks source
identities/references, publication fields and ages, draft claims, exact coverage,
prediction metadata and count accounting, then recomputes the selection and summary.
Checksums provide consistency, not publisher authentication. Original RSS identity
hashes cannot be reconstructed from the sanitized projection; validating those
against source bytes remains the archive builder's responsibility.

## Separate private news opt-in

```sh
python scripts/member_attachment_preview.py --config /private/members.json \
  --store /path/to/archive --news-bundle /path/to/news-draft \
  --at 2026-11-14T06:00:00Z --include-news-drafts \
  --output /private/new-review-directory
```

Both `content_preferences.news_catalysts: true` and `--include-news-drafts` are
required. Sector/macro switches do not enable news. A missing draft, stale/future
cutoff, mismatched selected stock report ID/date/snapshot hash or disabled news
switch leaves a gap. The preview attaches at most one full archive-wide news PDF,
disclosed in its message body; it does not promise holdings-filtered news coverage.

The PDF is checked using captured, bounded bytes and those same bytes are attached.
News participates in per-member SHA-256 deduplication and the actual SMTP-encoded
20 MiB limit, including base64 overhead. Exceeding the limit writes no `.eml` and
does not invent a public download link. Existing personal holdings overrides,
pause/schedule/report-quality rules, private output modes and no-ledger semantics
remain in force. No live authority, member import or email operation is performed.

## Output, testing and remaining acceptance

Output requires a new directory outside the archive and source repository. JSON
is bounded at 8 MiB and PDF at 20 MiB; artifacts are prepared and structurally
checked before exclusive writes. The manifest is written last. Four pages, draft
labels, cutoff, page numbers and selected evidence references are checked. Identical
inputs and locked PDF runtime produce byte-identical artifacts. Structural checks
do not replace rendering and visual inspection.

Tests cover selection and retained future/unknown evidence, rehashed metadata and
summary tampering, source references, wrong manifest/paths, deterministic builds,
long escaped text, empty coverage, bounded outputs, manifest-last failures, private
CLI output, independent consent, lineages, age gates, retained bytes and MIME caps.
CI builds/uploads the draft alongside the existing offline artifacts.

Live sources and current-data acceptance, human review of catalyst materiality,
verified event calendars, personalized news selection, controlled private downloads,
fresh-authority sender integration and production delivery remain pending. Preparing
a draft attachment does not complete those goals or authorize a real send.
