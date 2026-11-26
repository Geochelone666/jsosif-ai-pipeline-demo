# Sector Weekly Brief drafts

`scripts/sector_briefs.py` builds eight independent, four-page PDF review drafts
and JSON companions from the verified shared archive evidence. It has no network,
member-config, email, production-workflow or delivery-ledger integration.

```sh
python scripts/sector_briefs.py --store /path/to/archive --as-of 2026-11-13 \
  --boc-capture tests/fixtures/boc_fxusdcad_20261102_20261106.json \
  --output /path/outside/archive/new-sector-briefs
```

The optional BoC capture is the same independently validated capture accepted by
the shared evidence builder. This command does not refresh providers. The date
selects archive evidence; the review window is the trailing seven calendar days,
not a price-return period or an assertion about information available at that time.
Older reports remain visibly outside the review window, with ages in the JSON.

## Four-page template

1. Group-specific stock coverage, provider industry context, historical report
   quality, saved close/currency, observation date and source reference.
2. Macro observations, proposed benchmarks and explicit missing relative returns,
   group-specific KPI research topics, regulation and next-week event gaps.
3. Up to five provider peer candidates per covered stock, with P/E values, dates
   and references. Selection is alphabetical, not a ranking. Fewer than three
   peers remain an explicit gap; more than five retain the full candidate count.
4. Source reference ledger with SHA-256 prefixes and research limitations. Full
   source hashes, attribution URLs and integrity labels remain in the companion.

The seven existing weekly research headings are represented across these pages.
Group identity, coverage, candidate benchmarks and KPI topics reuse the shared
package configuration. Page structure is a fixed version-one layout. The JSON
also retains selected stock metrics/SEC facts and peer P/B, EV/EBITDA, market cap
and saved return observations with original units and source references.

Every output is marked `draft_incomplete_evidence` and `delivery_ready: false`.
Missing benchmark returns, KPIs, verified events and publication/vintage evidence
are never generated from narrative inference. Macro values with conflicting
observations at the latest date are displayed as unavailable. Incomplete numeric
observations are not printed as established facts. Archived quality labels are
preserved but do not authorize sending. Neither sector averages nor FX conversions
are calculated from unaligned prices, fiscal periods or currencies.

## Integrity, reproducibility and safe output

The CLI rebuilds evidence directly from the archive, preserving original expected
hash checks. Each brief ID hashes its entire JSON payload, including source dataset
identity. PDF metadata uses invariant mode; identical inputs and locked runtime
produce identical PDF bytes. Reproduction across different font/rendering/library
versions is not guaranteed; JSON remains canonical and renderer-independent.

Output requires a new directory outside the report store. Existing directories,
files and symlinks are refused. All documents are rendered in an owned staging
directory and checked before exclusive copy. `manifest.json` is written last and
lists each document hash and page check. A failed build has no completed manifest;
the reserved directory may remain and must not be treated as a published bundle.
The builder never deletes a user directory or merges into an existing bundle.

PDF preflight checks exactly four pages, page-specific headings, draft labels,
footers, all covered stocks and all seven template sections. Overflow fails the
bundle rather than silently publishing a fifth page with incorrect numbering.
This structural check is not pixel-level visual proof; rendered-page inspection
is still required before a draft is delivered for review. CI publishes draft
PDF/JSON artifacts for that purpose, not as production reports.

## Acceptance scope

Local tests cover eight-group output, missing evidence, preserved zeros, invalid
currencies, report ages, conflicting macro values, peer truncation, report-context
isolation, duplicate group membership, byte reproducibility, safe directory handling
and failures without a completion manifest. Full regression and real-archive
acceptance are recorded with the external delivery artifacts.

The real review sample is the previously verified 50-stock selection from
`report-data` commit `e705e8be79c14829346a574b3119c4bb2c04b909`, cutoff 2026-11-13.
It is a historical acceptance fixture, not the latest production state. There is
no claim of current freshness on the November 26 development date.

Still pending: validated benchmark observations and industry KPIs, sourced events,
live refresh, analyst acceptance, production attachment delivery and approved
controlled links. Offline member selection, deduplication and MIME-size review are
implemented separately in [MEMBER_ATTACHMENT_PREVIEW.md](MEMBER_ATTACHMENT_PREVIEW.md),
with explicit draft opt-in and no sending. No private research URLs are
published by this builder, and the existing sender remains unchanged.
