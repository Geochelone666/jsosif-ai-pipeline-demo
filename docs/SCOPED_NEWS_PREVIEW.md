# News drafts scoped to selected stocks

The private preview can filter a verified news bundle by effective stock selection.
Personal tickers override group holdings; otherwise the deduplicated group union is
used. This is a local review option, not a server preference or production switch.

```sh
python scripts/member_attachment_preview.py --config /private/members.json \
  --store /path/to/archive --news-bundle /path/to/news-draft \
  --at 2026-11-14T06:00:00Z --include-news-drafts --news-scope selected-stocks \
  --output /private/new-review-directory
```

`news_catalysts: true`, the news draft switch, selected report ID/date/snapshot
matching and age checks are still required. Scope selection cannot bypass pause,
schedule, quality or missing reports. Default `--news-scope archive` preserves the
version-one full-archive artifacts and messages for identical inputs.

## Evidence projection

From the validated, captured companion retain only selected stock reports, their
referenced articles and RSS/AI source records. Remove unselected report contexts,
classifications and unused sources. Shared article identities remain one record
with separate selected-stock references. No ticker search, model or provider call
is made. A shared headline can still mention other companies; original text stays
intact. Archived report association is not independent proof of headline relevance.

Recompute the newest-eight chronology inside the scope, retaining unknown/future
publication metadata in JSON. There is no quota or story guarantee per holding.
Empty feeds and missing requested reports remain explicit; unselected stocks are
outside scope rather than mislabeled missing.

Scoped companions and evidence use schema **2**, canonical sorted tickers and
parent review/index fingerprints. Full-archive schema **1** is unchanged. Validators
bind scope to taxonomy, coverage, retained references, counts, chronology and stock
lineage. A scoped input may be narrowed but cannot be widened. Parent fingerprints
are provenance references, not signatures or authorization for external bundles.

No member ID, name, email or private group name enters the PDF or companion. Stock
selections can still be private: scoped bundles use 0700 directories and 0600 files,
with fingerprint prefixes in filenames. Private preview records retain the scope
and parent identity. MIME messages attach only the PDF, not the JSON companion.

Identical stock sets within one preview invocation share one in-memory PDF render.
There is no persistent cache or cross-member message reuse. Recipients still have
separate MIME messages. Captured verified evidence is used even if input paths
later change. Scoped PDFs participate in per-member SHA-256 deduplication and the
actual encoded 20 MiB cap. No public link or sending path is added.

## Standalone private scope review

```sh
python scripts/news_review.py --store /path/to/archive --as-of 2026-11-13 \
  --tickers CSCO JPM --output /private/new-scoped-news-bundle
```

The CLI first verifies the archive, then projects the requested scope. Empty or
unsupported ticker sets fail. Missing requested reports are visible in standalone
drafts; member previews still require every selected stock report. The four-page
layout labels scope on every page and lists only requested stocks on its coverage
page. Every result remains retrospective, `delivery_ready: false`, with unknown
event dates and no point-in-time eligibility.

CI uploads only a hard-coded public fixture scope, never member input. Tests cover
scope isolation, shared references, order/duplicate normalization, rehashed tampering,
no widening, empty/large layouts, private round-trips, personal overrides/group
unions, render reuse, recipient isolation, retained bytes, consent/pause, MIME caps
and CLI behavior. Historical acceptance uses synthetic members and compares default
archive-mode bytes with the prior delivery.

Live sources, verified calendars, materiality review, controlled private access and
authorized production distribution remain pending.
