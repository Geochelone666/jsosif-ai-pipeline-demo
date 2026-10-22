# Changelog

## Unreleased — 2026-10-22

### Fixed
- `fred.py`: a `config/fred.json` that is not a JSON object, or has a null
  `api_key`, no longer crashes the shared FRED stage; it falls back to
  `FRED_API_KEY`.
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
- Offline tests for the FRED and peer-comparables collectors.
- README: environment variable reference; test command now matches CI.
