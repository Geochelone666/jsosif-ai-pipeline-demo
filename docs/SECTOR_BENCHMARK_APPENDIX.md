# Candidate benchmark appendix for sector drafts

The sector builder optionally appends a fifth page using an already validated
candidate benchmark review. No provider is called. The default four-page mode
and its version-one bundle remain byte-compatible in the locked environment.

```sh
python scripts/sector_briefs.py --store /absolute/archive --as-of 2026-11-13 \
  --boc-capture tests/fixtures/boc_fxusdcad_20261102_20261106.json \
  --benchmark-review /absolute/benchmark-review \
  --output /absolute/new-sector-benchmark-drafts
```

The input is a completed `benchmark_review.py` bundle. Its byte hashes, Markdown
and recomputed calculations are checked before projection. Output must be new
and outside both the report archive and benchmark input.

## Evidence and dates

Version two contains eight five-page PDFs, eight sector JSON companions, a
manifest and one shared `benchmark-review.json`. The manifest binds that shared
file by hash and review identity. It retains the full capture, prices, source
URLs, retrieval times and configuration. Reads are capped at 8 MiB for shared
evidence, 2 MiB per sector companion and the existing PDF limit.

Each companion retains its own sector's pairs, capture/review/configuration
identities, exact price dates, capture time, evidence mode and availability counts.
The review's sector identity, name, coverage and proposed candidate mapping must
match the sector draft. Consumer XLP and XLY remain separate; no sector mean or
ETF blend is calculated. Missing results print N/A with gap codes; full reasons
remain in JSON. Captured source symbols link to retained public history URLs.

Observations beyond the archive cutoff are rejected. Earlier price windows are
allowed as separate historical evidence. If the start predates the seven-day
archive review window, page five explicitly says **OUTSIDE archive review window
- not this week's return**. An inside window is labeled accordingly; neither
label certifies a full trading week. Exact endpoints always remain visible.

Provider retrieval can follow the archive cutoff because this is retrospective.
Adjusted prices may have later revisions; they are not point-in-time evidence or
a certified total-return index. All benchmarks remain proposed, and both
`delivery_ready` and `point_in_time_eligible` remain false. KPI/event gaps and
approved sector benchmarks remain missing even when a pair can be calculated.

Real local acceptance uses CSCO/XLK observations from 2025-10-01 to 2025-10-08
with a 2026-11-13 archive cutoff. Its one comparable pair is explicitly outside
the review window; 58 other pairs remain missing. This is not acceptance of
current weekly relative performance. CI separately labels synthetic fixtures.

## Private preview and verification

`member_attachment_preview.py` accepts both versions. For version two it verifies
the shared retained review, recomputes each sector projection, and checks the
captured PDF's appendix mode, dates, identities and numeric table text. Updating
a local hash cannot make inconsistent derived values valid. A different sector's
appendix cannot be substituted.

The existing content preference and `--include-sector-drafts` gate remain
required. Report-version/age checks, pause/schedule, attachment deduplication,
private output permissions and actual encoded 20 MiB MIME limits still apply.
No sender/ledger integration is added. Shared JSON stays in the review bundle;
it is not silently attached to email or published at a private research URL.

Tests cover taxonomy/date gates, source/scope identity, rehashed tampering,
five-page fit for all 59 synthetic computable pairs including extreme values,
path escapes, PDF appendix substitution, deterministic bytes and preview gates.
CI builds the optional bundle and runs the same member loader. Delivered review
drafts additionally require rendered-page inspection.

Formal listing/MIC checks, benchmark approval, aligned current/full coverage,
FX conversion, KPIs/events, analyst acceptance and authorized production delivery
remain pending. Optional evidence integration does not complete the sector
intelligence phase or the overall 2.0 plan.
