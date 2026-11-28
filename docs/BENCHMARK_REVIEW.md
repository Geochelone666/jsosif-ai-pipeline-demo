# Candidate benchmark price evidence

`benchmark_prices.py` is an explicit, bounded collector for supported stocks and
configured candidate ETFs. `benchmark_review.py` consumes its retained bundle
offline and builds a JSON/Markdown review across the eight product-default groups.
An optional exact-batch cache and local adapter-call allowance are available via
`benchmark_cache.py`; see [BENCHMARK_CACHE.md](BENCHMARK_CACHE.md).
These tools are independent of the production collectors, scheduler, report
archive, email sender and delivery ledger. They do not activate a benchmark or
attach returns to sector briefs. Every review has `delivery_ready: false` and
`point_in_time_eligible: false`.

## Collect and review

Use the locked Python environment. Both destinations must be new directories
outside the repository, with existing parent directories. Review output cannot
be inside its capture input. Existing files are never overwritten.

```sh
python scripts/benchmark_prices.py --symbols CSCO XLK \
  --start 2025-10-01 --end 2025-10-08 --output /absolute/review/prices
python scripts/benchmark_review.py --capture /absolute/review/prices \
  --output /absolute/review/benchmark-review
```

Only the first command requests prices. Each unique requested symbol is passed
once to yfinance history, using daily adjusted prices, no repair, no actions,
explicit inclusive endpoints and a 15-second request timeout. yfinance may make
additional internal requests for cookies/metadata or retries; this is not an
HTTP-request quota or a hard batch wall-clock limit. Windows are positive and at
most 366 days. The end must precede both UTC capture day and exchange-local
retrieval day; this conservative check does not certify an exchange calendar.
The installed yfinance 1.7.0 supports per-call `raise_errors=True` with a
deprecation warning. It is retained to isolate failures without changing global
provider configuration. Provider exceptions are replaced with fixed gap codes.

The adapter verifies provider-reported symbol, native currency, equity/ETF type,
exchange timezone and price dates. It rejects zero, negative, infinite and
duplicate observations. Null adjusted prices remain null. A failed instrument
does not discard successful instruments. Captured metadata is an allowlisted
projection; arbitrary provider fields and exception text are not retained.

Capture output contains `prices.json` and a manifest written last. `capture_id`
binds the canonical retained evidence; the manifest also hashes actual JSON
bytes. Input reads are bounded (8 MiB per data file, 64 KiB per manifest), and
paths cannot escape their bundle. These hashes prove internal consistency, not
provider authenticity. Capture timestamps describe retrieval, not historical
availability; adjusted prices may be revised after the observation date.

## Comparison contract

The review retains the full capture, the normalized group configuration and its
fingerprint, and per-pair references to captured series. It covers all 50 stocks,
eight groups and 59 stock/candidate pairs, including explicit gaps when only a
subset was collected. Consumer stocks get separate XLP and XLY rows.

- Both series need actual observations on the same exact start and end dates.
  No forward fill, interpolation or calendar substitution is performed.
- Prices must share a native currency and documented `adjusted_close` basis.
  Candidate currency must also match its proposed configuration. CAD/EUR stocks
  against USD candidates remain missing until separately validated FX evidence
  and a conversion methodology exist.
- Each price return is `(end / start - 1) * 100`, in percent. The difference is
  stock return minus candidate return, in **percentage points**, not percent.
  This is an adjusted-price calculation, not a certified total-return index.
- No sector mean, portfolio return, ETF blend, benchmark approval or investment
  conclusion is inferred from available pairs. Individual computability does
  not make the weekly sector brief ready.

The review validator recomputes every derived field, count and fingerprint from
the retained capture and **the current checked-out configuration**. Use the same
code/configuration revision to reproduce or validate an older review. A changed
configuration requires a newly built review. Bundle loading also checks Markdown
against the recomputed rendering, so rehashing a misleading table is insufficient.

## Verification and remaining work

`tests/test_benchmark_review.py` exercises endpoint and currency gaps, separate
Consumer candidates, provider failure isolation, timezone conversion, adapter
flags, canonical identities, rehashed inconsistencies, bounded reads, symlink
escapes, new-output guards and byte-identical offline builds. The committed
`tests/fixtures/benchmark_prices_synthetic` is **synthetic**, with artificial
100→110 / 100→105 prices, `capture_mode: injected_fetcher` and
`provider_version: synthetic-test`. Its Markdown explicitly labels injected
fixtures; actual CLI collection uses `capture_mode: provider`. Its Yahoo URLs
exercise the source contract; they do not attribute invented observations to
Yahoo. CI only consumes that fixture and makes no benchmark-provider calls.

Real-source acceptance is a separate local artifact: CSCO and XLK, historical
2025-10-01 through 2025-10-08, six observations each. A successful limited capture
does not validate every instrument or establish production data readiness.
Formal listing/MIC verification, benchmark selection review, unified provider-wide
refresh budgets and per-instrument cache reuse, FX conversion, corporate-action methodology, current/full coverage,
production integration and point-in-time/backtest eligibility remain pending.
An optional sector appendix is implemented in
[SECTOR_BENCHMARK_APPENDIX.md](SECTOR_BENCHMARK_APPENDIX.md).
