# Deterministic shared research evidence

`scripts/shared_research_pack.py` builds a reusable evidence package from verified
local report archives. It performs no provider requests, database writes or email
sends. It does not change production workflows or replace the existing site data.

## Build and consume

```sh
python scripts/shared_research_pack.py --store /path/to/archive \
  --as-of 2026-11-13 \
  --boc-capture tests/fixtures/boc_fxusdcad_20261102_20261106.json \
  --output /path/outside/archive/shared-evidence.json
python scripts/shared_research_pack.py --store /path/to/archive \
  --as-of 2026-11-13 \
  --boc-capture tests/fixtures/boc_fxusdcad_20261102_20261106.json \
  --format markdown --output /path/outside/archive/shared-coverage.md
```

The output must be a new file outside the archive. Existing files and symlinks
are not overwritten. The BoC capture is optional. CI builds both formats from
the repository's historical report fixtures and publishes review artifacts.

Python consumers can call `build(root, as_of=..., boc_capture=...)` and
`validate_pack(pack)`. Validation checks fingerprints, identities and references;
it is not provider authentication or a general sanitizer for third-party JSON.
Only the builder performs the allowlisted projection.

## Version 1 contract

- `dataset_id`: SHA-256 of canonical JSON of all remaining fields. There is no
  wall-clock build timestamp; identical selected evidence produces identical JSON.
- `entities`: separate stock, sector, industry, benchmark and macro namespaces.
  Stock identities remain provider symbols with unknown exchange MIC. Research
  sectors are configurable product defaults; Yahoo industry labels are a separate
  taxonomy. Candidate benchmarks retain their proposed status.
- `sources`: content fingerprints, integrity labels and public attribution URLs.
  Snapshot references retain archive paths. Supplemental sources are linked by
  verified content hash; source versions remain distinct.
- `observations`: finite numeric value, unit, currency and separate currency
  source, observation date, optional period start/retrieval time, source reference,
  report-date context and limitations. `observed`, `incomplete` and `missing` are
  distinct states. Zero and negative net income are preserved; nonpositive prices,
  booleans, nonfinite numbers and future observations are rejected.
- `relationships`: sourced coverage, provider industry, peer candidates and
  proposed benchmarks. Provider peer metrics are not normalized rankings.
- `reports`: original version identity, quality and observation references.
  Supplemental evidence does not upgrade report readiness.
- `sectors`: all eight configured groups, coverage gaps, KPI topics and proposed
  benchmarks. Benchmark returns stay missing, KPI status stays not collected,
  and sector brief readiness stays false.

Latest report selection uses report date, normalized generation timestamp and
report ID. Duplicate report IDs fail closed. Original index entries, including
expected source hashes, pass through archive verification. The snapshot is hashed
again from the same bytes parsed. Bad tracked checksums abort the build; optional
missing or malformed sources remain isolated. Legacy sources without expected
hashes retain a build-observed integrity label.

## Source and time limitations

Every observation has `point_in_time_eligible: false`; the package declares
`retrospective_reconstruction_not_point_in_time`. The cutoff selects report and
observation dates, not what an investor could have known at that historical time.
Archive generation time is not provider publication or retrieval time. Unavailable
publication dates, timestamps and vintages remain null.

Stock metrics use a fixed allowlist of saved snapshot values. Price currency is
accepted only from a matching provider symbol and has its own source reference.
Adjustment bases and exact return endpoints are not established by this archive.

FRED includes four known archived series with explicit units. Repeated series IDs
are ambiguous and become missing. Reuse binds both content and report-date context;
one report cannot expose another report's future observation. Vintage, publication
and retrieval evidence is absent, so revisions cannot be ruled out.

SEC extraction accepts only archived quarterly revenue/net income in USD, with
70–110-day periods ending by the report date. Symbol/CIK shape is checked and
Canadian issuers require the explicit existing listing map. No suffix stripping
is used. A latest-filing date is never substituted for a fact's publication date;
fact accession, filing time and retrieval time remain unavailable.

Peer candidates preserve provider-native currencies and units. Duplicated symbols
are excluded, and provider fiscal periods, return endpoints and valuation bases
are not harmonized. They must not be ranked or aggregated as comparable evidence.

BoC capture validation checks the official endpoint, requested window, canonical
payload checksum and existing adapter metadata contract. The capture can postdate
the cutoff: this is retrospective evidence, not a historical vintage. Its checksum
establishes consistency with the capture, not a provider signature. No inferred FX
conversion is performed. Coverage Markdown displays actual macro date ranges.

## Read-only archive acceptance, 2026-11-16

The existing `report-data` branch was inspected at fixed commit
`e705e8be79c14829346a574b3119c4bb2c04b909` (1,373 report versions, 50 symbols).
Only the latest 50 report versions at cutoff 2026-11-13 and their archived sources
were copied to a separate local review store. Delivery state was not extracted
or modified. This acceptance used saved evidence, not new live provider requests.

The package contains 50 stocks across all eight groups, 36 provider industry
labels, 203 source records and 1,409 unique observations: 1,338 observed and 71
missing. All 50 covered stocks have industry labels and three to five provider
peer candidates. The archived reports contain 48 ready and two degraded labels;
these are historical labels, not a current production health assessment.

The optional BoC capture contains only November 2–6 observations, captured on
November 14. It does not imply November 13 macro freshness. The resulting package
ID is `0ad54813047572b5511173d68c467a721bce78fc6e7ac08cef0b3ef051a9f4e9`.

Tests cover deterministic selection, units and zero values, missing currencies,
all tracked source checksum tampering, unknown/private field exclusion, duplicate
identities/peers/FRED series, future dates, malformed cells, SEC issuer and period
checks, BoC capture tampering, package references and safe output creation.

Pending work includes formal listing identities, shared live refresh/cache,
historical publication/vintage evidence, validated benchmark returns, real industry
KPIs and weekly sector briefs. None is activated by this evidence builder.
