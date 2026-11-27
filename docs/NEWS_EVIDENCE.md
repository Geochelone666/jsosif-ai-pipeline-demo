# Retrospective news evidence index

`scripts/news_evidence.py` builds a deterministic JSON index, a bounded Markdown
review and a completion manifest from archived RSS items and saved classifications.
It performs no network request, model inference, provider refresh, classification
rewrite, subscription lookup, email or ledger operation.

```sh
python scripts/news_evidence.py --store /path/to/archive --as-of 2026-11-13 \
  --output /path/outside/repository-and-archive/new-news-evidence
```

The result is always `draft_incomplete_evidence`, `delivery_ready: false` and
`retrospective_reconstruction_not_point_in_time`. This is an evidence foundation
for news/catalyst research, not a completed newsletter or event calendar. Existing
member previews continue to report standalone news as an unmet preference.

## Evidence identities and provenance

For each supported stock, select the latest report date at or before the cutoff,
then UTC archive generation timestamp and report ID as deterministic tie-breakers.
Duplicate report identities fail. Generation can postdate the cutoff; selection
does not claim the information was historically available at that cutoff.

Verify the existing snapshot/PDF/Markdown and all tracked source checksums before
projection. Re-read RSS and AI files into bounded retained bytes and check those
bytes again against the expected source hash. Sources without an expected hash
remain explicitly `observed_hash_only`. Missing legacy sources, invalid JSON shapes
and empty feeds have distinct statuses. A failed tracked checksum aborts the build.

An article identity hashes the exact RSS headline, publisher, raw publication
metadata and raw link. Repeated identities within and across stock reports share
one article while preserving each report reference and duplicate count. Differences
in those fields remain separate, even when URLs or titles look similar. This is not
semantic syndication deduplication or independent corroboration.

Only allowlisted fields are projected. Arbitrary AI summaries, reasons, private
configuration and provider fields are excluded. Publication timestamps require an
explicit timezone and normalize to UTC. Missing/invalid/naive values remain unknown;
the report date is never substituted. Future and old timestamps remain visible with
age labels at both the report date and review cutoff. `event_date` is always null:
neither headline dates nor saved calendar/earnings labels establish an event date.

Links must be HTTPS without credentials, fragments, local/IP targets or arbitrary
query strings. Google RSS article links may have the known `oc=5` parameter, which
is removed from the public reference. Rejected links remain null; their original
bytes contribute only to the identity hash. Links are not opened or authenticated.
This is a projection of archive data, not a general privacy scrubber for arbitrary
text embedded in headlines or URL paths.

## Historical predictions, separate from article facts

A saved classification joins only on the full exact RSS identity. A title alone
is insufficient. Each reference preserves distinct saved category/event/sentiment/
method/date values, decision occurrence counts and heuristic review flags. Unknown
enum values are null with flags. Saved summaries and uncalibrated confidence values
are not promoted into article claims. Existing low-confidence review flags may be
retained, but are not probabilities of correctness.

Multiple differing projected decisions are `conflicting`; no winner is selected.
Exact duplicate projected decisions retain a count. `unclassified` and `irrelevant`
are retained when fully matched. Unmatched decisions are counted by saved category;
malformed decisions are separately counted. Wrong ticker/date AI files contribute
no predictions and report an identity mismatch. Missing decisions do not imply
irrelevance. Predictions from different stock reports remain separate contexts.

The Markdown review shows all stock coverage rows plus at most 100 article identities
ordered by publication timestamp, with explicit future/unknown/stale labels and
historical prediction references. This is not a materiality ranking. The JSON
contains every article, per-report prediction and source hash. Markdown escapes
untrusted headline/publisher text; it does not render raw HTML from those fields.

## Output and acceptance

Input limits: 32 MiB archive index, 2 MiB per news source, 500 RSS rows and 1,000
saved decision rows per selected report. Output requires a new directory outside
the source repository and report store; symlink resolution is checked. Files are
created exclusively; `manifest.json` is last and hashes both artifacts. A failed
write can leave an incomplete directory, which must not be treated as published.
Identical inputs produce identical bytes with no wall-clock build timestamp.

The fixed 50-stock archive at cutoff 2026-11-13 contains 695 report RSS references,
692 exact article identities and 98 source versions. There are 248 references
without an exact matched decision. Of 229 unmatched saved decisions, all are legacy
`irrelevant` rows that omitted publisher, publication metadata and URL. They are
counted as gaps rather than joined by title. No inferred event dates are added.
These counts describe that historical fixture, not current news coverage.

Tests cover deterministic selection, exact joining and deduplication, conflicting
predictions, missing/future/UTC publication dates, unsafe links and escaped markup,
tampering including a post-verification source race, legacy integrity disclosures,
bounded inputs, archive immutability, manifest-last failures and CLI behavior.
CI builds this index from offline historical fixtures. Those imported fixtures can
have no retained news sources, so missing-source coverage is expected there; the
separate 50-stock acceptance supplies populated news evidence.

Pending: live source acceptance, verified event dates and calendars, reviewed
materiality/catalyst narratives, standalone news PDFs, explicit member selection,
controlled private links and authorized production delivery. No existing quality,
sender, release, taxonomy or backend defaults change in this increment.
