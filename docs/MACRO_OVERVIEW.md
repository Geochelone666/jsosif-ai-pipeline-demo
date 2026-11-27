# Standalone macro overview draft

`scripts/macro_overview.py` produces an independent two-page PDF, a versioned JSON
companion and a completion manifest from the verified shared evidence package.
It performs no provider refresh, member lookup, email or production activation.

```sh
python scripts/macro_overview.py --store /path/to/archive --as-of 2026-11-13 \
  --boc-capture tests/fixtures/boc_fxusdcad_20261102_20261106.json \
  --output /path/to/new-macro-bundle
```

Page one shows four configured FRED series and BoC FXUSDCAD with unit, actual
observation date, age relative to the cutoff and evidence status. It also shows
up to five latest dated BoC observations. Page two records source/version counts,
hash prefixes, retrieval limitations and full companion identity. Histories and
source hashes are retained in JSON; no forecast, causality or inferred FX conversion
is added. Missing BoC capture remains explicit rather than hiding that series.

## Evidence selection

All macro evidence in the selected stock archive package is considered once per
observation identity. Different source versions and report contexts remain distinct.
Per series/date, agreeing numeric records produce an observed value; contradictory
values produce `conflicting`; mixed available/missing records produce `incomplete`;
no usable value produces `missing`. Only `observed` carries a summary value.

The latest **dated** record determines the headline, including when it is missing.
There is no fallback to an older good value. Undated missing records remain separately
referenced, without inventing a date. Source age is cutoff minus observation date,
not a promise of freshness. Small nonzero values are not formatted as zero.

The package is always `draft_incomplete_evidence`, `delivery_ready: false`, and
retrospective. Publication times and historical vintages are unavailable. BoC capture
time can postdate the report cutoff and is retained without claiming historical
availability. Every observation keeps `point_in_time_eligible: false`.

The overview fingerprint covers its complete payload. Validation reuses the shared
evidence contract for references, units/dates/statuses and source fingerprints,
then recomputes the summary to detect altered derived values. Only known series
and their expected units are accepted. Stock report IDs, dates and snapshot hashes
are included as lineage; no stock/private source fields are copied into the macro
observation section. Checksums establish consistency, not publisher authentication.

## Private member review

```sh
python scripts/member_attachment_preview.py --config /private/members.json \
  --store /path/to/archive --macro-bundle /path/to/macro-bundle \
  --at 2026-11-14T06:00:00Z --include-macro-drafts \
  --output /private/new-review-directory
```

The member must explicitly request `macro_overview: true`. A separate macro draft
switch is mandatory; sector preference and `--include-sector-drafts` cannot enable
the macro attachment. The macro cutoff must fit the configured report-age window,
and each selected stock's report ID, date and snapshot hash must match its lineage.
Mismatch, absence or disabled draft review appears as a gap. The full draft remains
ineligible for sending, including when those preview gates pass.

One macro PDF is added per member and included in the existing per-member content
deduplication and actual encoded 20 MiB MIME budget. Verified bytes are retained for
assembly. Pause/schedule rules, private 0700/0600 output, no-authority/no-ledger
semantics remain unchanged. News drafts require a separate preference and switch;
see NEWS_REVIEW.md. No direct send mode exists.

## Output and acceptance

The new bundle directory must be outside the report store. Existing paths are
refused. PDF structure is checked before writing; the completion manifest is last.
It validates two pages, dates, draft labels, footers and all five configured series.
Invariant PDF metadata enables byte-identical rebuilds with the locked runtime.
Visual rendering still requires inspection; structural checks are not visual proof.
CI builds and uploads the draft from historical fixtures.

The real acceptance fixture uses the previously verified 50-stock selection at
cutoff 2026-11-13: nine macro records, two source versions, five BoC dates and three
available FRED series; NAPM remains missing. BoC's latest observation is seven days
before the cutoff, the available FRED dates are 43 days before it. This is not a
claim of current November 26 data. The delivery evidence records PDF review, full
regression, deterministic rebuilds and synthetic-member MIME acceptance.

Live refresh, additional series, revised-data/vintage handling, current-data team
acceptance and authorized production distribution remain pending. Independent news
review drafts and private attachment opt-in are described in NEWS_REVIEW.md.
