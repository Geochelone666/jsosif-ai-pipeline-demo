# Cached candidate-benchmark captures

`benchmark_cache.py` wraps the standalone collector with an **exact-batch** cache
and a durable local adapter-call budget. It is not connected to production jobs,
email, existing price caches, budget reservations or delivery ledgers.

```sh
python scripts/benchmark_cache.py --symbols CSCO XLK \
  --start 2025-10-01 --end 2025-10-08 \
  --cache /absolute/work/benchmark-cache --daily-limit 20 \
  --output /absolute/review/first-capture
python scripts/benchmark_cache.py --symbols XLK CSCO \
  --start 2025-10-01 --end 2025-10-08 \
  --cache /absolute/work/benchmark-cache --daily-limit 20 \
  --output /absolute/review/second-capture
python scripts/benchmark_review.py --capture /absolute/review/second-capture \
  --output /absolute/review/candidate-review
```

The cache directory must be new on first use, with an existing parent, outside
the repository. Subsequent calls use that same dedicated owner-only directory.
The output must always be new, outside both repository and cache. macOS/Linux
local filesystems with POSIX `flock` are supported; network filesystems and
multi-host coordination are not validated.

## Identity, evidence and expiry

Keys bind the sorted unique symbol set, inclusive window, provider, installed
yfinance version, adapter contract version, daily interval, adjustment basis and
provider/injected mode. Request order and duplicates do not cause another fetch.
Different windows, provider versions or symbol sets require separate captures.
Overlapping batches do **not** reuse individual series: this preserves the prior
single-batch evidence contract without merging different retrieval vintages.

A cache hit returns the exact retained capture. Its retrieval timestamps and
capture ID stay unchanged, and the existing bundle writer produces identical
JSON/manifest bytes. The CLI prints a separate operational JSON receipt to stdout
with access time, cache key, hit status, reservation day, units used and policy.
That receipt is not a newly retrieved price observation or a signed provider
attestation. The standard price bundle format is unchanged.

Complete observed endpoints have a one-hour TTL, measured from batch finish.
A batch with a missing endpoint, empty observations or any failed instrument has
a five-minute negative TTL. Successful series in such a batch are retained;
expiry refreshes the whole batch within the remaining budget. No stale fallback
is returned when quota or validation prevents refresh. Fixed cooldowns do not
claim to implement provider `Retry-After` handling, which yfinance does not expose
through this adapter contract.

## Reservations, concurrency and failures

One budget unit reserves **one unique symbol passed to the adapter**, not one
HTTP request, dollar, token or successful response. yfinance can make internal
cookie/metadata/retry requests. The wrapper is not a hard network-request quota.
The default daily limit is 20 units; the first invocation pins the chosen limit
(1–1000) in its SQLite settings. A later caller with a different limit fails,
including on a would-be cache hit. This release has no automatic policy migration.

All keys and processes sharing a cache directory share its budget. The wrapper
atomically commits the whole batch reservation before the first provider call.
The UTC **reservation day** determines the charge, including a batch that finishes
after midnight. A new UTC day has its own allowance, with older rows retained.
Moving the clock backwards fails rather than resurrecting older daily allowance.

Per-key locks suppress duplicate concurrent fetches. Short global state locks and
SQLite transactions arbitrate different keys competing for the same quota. A
busy lock times out (default five seconds) without issuing a provider call.
Success atomically binds the cache entry and completed reservation to its capture
ID. Failure, interruption, process death or a failed cache write never refunds
units. An unfinished reservation blocks retry for five minutes; after that, a
new attempt still needs fresh budget, and the original reservation stays recorded.

Invalid/oversized cached evidence can be replaced only after another reservation.
Missing/corrupt state databases, missing settings/tables, schema/policy mismatch,
unsafe symlinks or failed integrity checks stop collection. State is never
silently recreated in an existing cache directory. Preserve the directory for
inspection; do not delete it or create another directory to bypass the allowance.
No automatic pruning or reset is provided. These guarantees assume trusted local
filesystem ownership; manual database edits or deletion cannot be authenticated.

This allowance is scoped to this wrapper and cache directory. The original
standalone collector, other cache directories, BoC collection and production
budgets are independent. Unified provider-wide budgets, per-instrument reuse,
retry-header handling and controlled operational policy changes remain pending.

## Acceptance

`tests/test_benchmark_cache.py` covers TTL boundaries, failure isolation, exact
evidence reuse, cross-key quota, midnight rollover, clock rollback, metadata-key
separation, corrupt-entry recovery, corrupt-state refusal, symlinks, lock timeout,
failed writes, separate-process contention and abrupt process death.

CI also runs `tests/benchmark_cache_acceptance.py`: the explicit synthetic fixture
requires two adapter calls, then a reordered request is served from cache with
identical output bytes; another key is denied at the pinned two-unit limit.
Only synthetic public evidence and receipts are uploaded, not the cache database.
Real-source/cache acceptance is recorded separately in local delivery artifacts.
All downstream candidate reviews remain retrospective, proposed and unready for
delivery; this cache does not establish approved benchmarks or current coverage.
