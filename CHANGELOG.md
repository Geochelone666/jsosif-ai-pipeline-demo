# Changelog

## Unreleased — 2026-10-22

### Fixed
- Public site indexes now export an explicit metadata schema, excluding unknown
  top-level and nested operational fields. Invalid public metadata preserves the
  previous site; original archive files remain unchanged.
- `fred.py`: a `config/fred.json` that is not a JSON object, or has a null
  `api_key`, no longer crashes the shared FRED stage; it falls back to
  `FRED_API_KEY`.
- A corrupt SEC ticker cache or shared price cache no longer blocks SEC data or
  price collection; both are refetched and now written atomically.
- `send_ledger.py --list` skips undecodable lines instead of failing.
- `build_review_bundle.py --sector` works on a fresh clone via the tracked
  `config/sectors.json` when `data/<ticker>-info.json` has not been generated.

### Changed
- `data/` is no longer tracked: it is the per-run working directory and holds
  the send ledger with recipient addresses. Back up local `data/` before pulling
  if you run the pipeline on a machine with an older checkout.
- Test fixtures and docstrings use `example.com` addresses only.
- Dependencies: certifi 2026.10.19 (PYSEC-2026-4320), pytest 9.0.3
  (PYSEC-2026-1845).

### Added
- Offline tests for the SEC EDGAR collector (identity requirement, retry policy, as-of period selection, revenue fallback, failure tolerance).
- `prepare_store.py` falls back to a portable orphan-worktree setup on Git older than 2.42; the full test suite now passes on Git 2.34. Added offline tests for `prepare_store` and `bundle_reports`.
- Offline tests for the FRED and peer-comparables collectors.
- README: environment variable reference; test command now matches CI.
