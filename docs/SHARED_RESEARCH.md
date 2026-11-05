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
