# Research data dictionary and evidence policy

This project produces **historical, source-grounded research**, not trading signals.
All timestamps below describe distinct objects and should not be conflated.

| Category | Input / derived source | Core dimensions | Limitations |
| --- | --- | --- | --- |
| Daily price history | Yahoo Finance adjusted close, Stooq fallback | Close, 1D/1W/1M/YTD/1Y returns, 50/200 day averages, RSI, MACD | Missing history N/A; Stooq availability depends on listing; vendor adjustments need spot checks |
| Risk statistics | Existing price history plus SPY observations | Volatility, beta, drawdown, Sharpe, Sortino, downside deviation, historical VaR/ES, correlation, tracking error | Trailing calendar-year sample, 252-day scaling; date-aligned returns only; native currencies, no portfolio FX conversion |
| Company fundamentals | Existing yfinance company info snapshot | Trailing/forward P/E, P/B, EV/EBITDA, revenue growth, gross/operating margins, ROE, FCF yield | Vendor-reported periods may differ, estimates may change; currency equality required for FCF yield |
| RSS headline observation | Google News RSS results | Headline, named publisher, link, publication date, RSS fetch status | News coverage is non-exhaustive; a headline does not prove the underlying claim |
| Headline classification | Deterministic rules + optionally Groq/Gemini | Tailwind/headwind/catalyst/risk, source metadata, class method, unresolved and irrelevant counts, actual models used | AI is not a fact checker; unknown items are excluded and block complete readiness |
| RSS breadth/freshness audit | Pure functions of fetched RSS items | Unique publishers, dominant publisher share, publisher HHI, duplicates, HTTPS link coverage, oldest/newest publication date | Metadata completeness/diversity are proxies, not independent corroboration |
| Earnings and comparables | yfinance/secondary market sources | Expected/report dates, peer valuation and growth | Expected dates may shift; comparisons can mix fiscal periods and currencies |
| Regulatory fundamentals | SEC EDGAR where issuer identity is verified | Filing identity, source fields, revenue, income | Coverage varies by issuer and domicile; never silently substitute another company |
| Macro context | FRED observations | Observed series value, release/observation date, units | Historical observations may be stale, revised, discontinued or unavailable |

## Data-quality gate

A daily report is **ready** only with eligible dated market observations and
complete reconciled RSS classification evidence. The per-report snapshot
records classification counters, coverage percentage, provenance and limitations.
A fetch error, stale ticker identity, unresolved headline, counter mismatch or
source outage must **not** be silently filled in.

The public archive uses immutable report versions and sha256 checksums.
Generated and emailed timestamps are *not* evidence that all source dates match
the business date. Quality metadata should be read before making any research
claim. The weekly mailer uses separately persisted delivery state and unique
member/week keys to avoid blind retries.

## Interpreting the new source breadth metrics

- `unique_publishers` is the count of nonblank case-normalized RSS publisher names.
- `publisher_hhi` is the sum of squared shares **among headlines with known
  publishers**; smaller values indicate more even publisher distribution, not
  higher truthfulness or independence.
- `largest_publisher_share_pct` similarly uses only named publishers.
- `https_link_headlines` counts URLs with an HTTPS scheme and a hostname;
  this validates syntax only, **not** accessibility, article content or safety.
- `oldest_headline_age_days` compares UTC publication dates to the report's
  business date; malformed and future dates are reported separately.
- `duplicates_excluded` counts exact repeated headline strings; near-duplicate
  stories are not automatically collapsed.

All these are deterministic, inexpensive calculations over fetched headlines.
They do not send additional requests or change the release gate by themselves.
