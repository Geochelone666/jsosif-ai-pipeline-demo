# Shared research foundation — configurable defaults

The team requested that development propose the research groups. The eight
product defaults in config/research_teams.json cover the current 50-symbol
universe exactly once: Financials, Technology, Healthcare, Energy, Industrials,
Consumer, Materials, and Communications/Media. Consumer combines staples and
discretionary companies. These are configurable research group defaults, not a
claim about the fund's formal organization or investment mandate.

Each template names coverage, candidate benchmark ETFs, sector-specific KPI
research topics and seven sections for a future weekly brief. Candidate benchmarks
are explicitly proposed, not active/validated observations. Consumer has separate
XLP/XLY candidates; no arbitrary blended benchmark is computed. KPI topics are
not assumed to apply to every issuer: bank NIM is not a Visa metric; production
volume is not evidence for a pre-production issuer. Missing data remains missing.

research_data.PriceObservation binds an instrument to an observation date,
positive finite price, currency, timezone-aware retrieval time, HTTPS source and
explicit adjustment basis. relative_performance compares the same exact endpoints
only when currencies and documented price bases match. It does not forward-fill,
invent FX conversions, infer causality or fetch providers. Output separates
percentage returns from relative percentage points and exposes source URLs.

This contract is not a deployed sector dashboard or completed data collector.
Further work must bind observations to verified provider adapters and source
hashes, add shared caches, validate benchmark listings/calendars/FX, select macro
series, and supply real company-specific KPI evidence. The existing stock report
archive is preserved throughout. Eight-group configuration is not automatically
written to team Supabase or existing private member preferences.

Public source references must be HTTPS without credentials, query strings or
fragments. Store a public attribution URL rather than a credential-bearing API
request URL; adapters retain request parameters privately as appropriate.

## Archive-backed workspace

Site builds now create research-data.json and the research.html/js view. The
workspace reuses latest verified stock snapshots and projects only allowlisted
peer/FRED fields. It does not fetch providers. Eight sector filters show coverage,
report quality/advisories and source dates. The comparison page shows original
saved metric values and provider peers, not normalized rankings. Macro observations
retain series dates/units and public FRED attribution; unavailable sources stay missing.

Supplemental source files are not covered by the original report-index expected
hashes. Their provenance explicitly says the hash was observed at build, not
verified against an original expectation. They never upgrade report readiness.
Reads are bounded and parsed/hashed from the same bytes. Macro projections are
shared by source hash AND report-date context, so future observations for an older
report cannot be made available by reuse. Corrupt optional sources are isolated;
a bad verified report still fails the whole site build and preserves prior output.

inputs_digest fingerprints selected snapshot/source inputs and team templates for
reproducible source selection, not a guarantee that underlying providers were
correct. Source retrieval/publication timestamps absent from old files remain
unavailable. Private source fields, credentials and member configuration are never
copied into this public dataset. Stock metrics remain the already-public verified
snapshot payload. Provider fiscal periods and currencies can differ.

Test with `python scripts/research_browser_smoke.py --site site-build` using the
same Chromium installation as other browser checks. Real shared provider caches,
Bank of Canada adapters, historical charts, calendars, validated sector returns,
industry KPI observations and weekly briefs remain subsequent delivery work.
