# TMC Intelligence Report

- ticker: **TMC**
- Report as_of: **2026-11-12**
- Market data as_of: **2026-11-12**
- Quant sources: https://finance.yahoo.com/quote/TMC/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/TMC/key-statistics/
- AI analysis snapshot as_of: **2026-11-12**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-13T04:58:24.424678+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 10, 'rule': 2, 'ai': 4, 'unknown': 0, 'irrelevant': 4})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **4** exact headline/source/date matches; prior report **20261112T054014Z-6c47e7f9/TMC** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'directional_claim_without_event_type': 1}
- RSS source audit (metadata only, not article fact-checking): 10 unique headlines; 10 named publishers; 1 exact duplicates; 10 HTTPS source links; largest publisher share 10.0%; oldest publication 2026-11-09

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 2.3000 |
| Return 1D (%) | -6.3136 |
| Return 1W (%) | 11.1111 |
| Return 1M (%) | -20.1389 |
| Return YTD (%) | -62.7229 |
| Return 1Y (%) | -59.2199 |
| Annualized volatility (%) | 94.2876 |
| Beta vs SPY | 3.4872 |
| Max drawdown (%) | -78.0720 |
| Sharpe (rf=0) | -0.4906 |
| Downside deviation (rf=0, %) | 63.0196 |
| Sortino (rf=0) | -0.7340 |
| Historical VaR 95% (1D, %) | 8.8909 |
| Historical ES 95% (1D, %) | 11.8344 |
| Correlation vs SPY | 0.5080 |
| Tracking error vs SPY (%) | 88.1085 |
| P/E (trailing) | N/A |
| P/B | -36.51 |
| EV/EBITDA | -4.46 |
| Revenue growth (%) | N/A |
| Forward P/E (estimate) | N/A |
| Gross margin (%) | 0.00 |
| Operating margin (%) | 0.00 |
| Return on equity (%) | -1123.19 |
| Free cash flow yield (%) | 2.05 |
| MA50 | 3.2473 |
| Close vs MA50 (%) | -29.1719 |
| MA200 | 4.6419 |
| Close vs MA200 (%) | -50.4513 |
| RSI (14, Wilder) | 38.8706 |
| MACD (12,26) | -0.2480 |
| MACD signal (9) | -0.2885 |
| MACD histogram | 0.0406 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'TMC': 281, 'SPY': 281}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 2.3000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -6.3136 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 11.1111 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -20.1389 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -62.7229 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -59.2199 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 94.2876 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 63.0196 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.7340 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 8.8909 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 11.8344 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5080 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 88.1085 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 3.4872 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -78.0720 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.4906 -> Negative risk-adjusted return.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 0.0000 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 0.0000 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: -1123.1911 -> Adjusted price fell over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.0484 -> No interpretation rule is available for this metric.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 38.8706 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.0406 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -29.1719 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -50.4513 -> Clearly below the moving-average trend level.

## TAILWINDS

### TMC Receives NOAA Letter on Seabed Permit Application Certification
- Summary: TMC received a NOAA letter confirming certification of its seabed permit application, supporting its expansion plans.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxNWnBteDlONHNON0RqVmhlVnduVjBrTlJ2Mm1uYV9jT2FrTTJ5VWFEbjg0TWsyVW9hV2ZGMjRiN1A3dnhkcnJOVVNkeVVma1hwa2tOXzFMTGg3M05CVFhKUjFpZTlWOVF5LXhNNlIyQUl3NHhsbHc2U2ZDby1wWUxKMmdWZW9MR1dFMVVTQ0VtRjlSbl9DS3R1dWJmWkZ2VG40LUJRcTMzUzAyVk1OQmNDV0hKZTVJWmM1dFRZ?oc=5>

## HEADWINDS

### NOAA to decide on TMC the metals Co Inc. permit application by mid-December
- Summary: NOAA will decide on TMC's permit by mid‑December, potentially delaying operations.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMizwFBVV95cUxPMUs3TUlOM2x1WjRNcUtxaVdMTTBiTjhLY05YOTNCb0xjNFNmUmVfNWc4bXEtQlRRQkVCQjRlR3B5YzdjdE5qdzBULVFCYXhFRWlkYl9NbW9SRjFDMDdDWWozaXM0UWl1WHhGYnYzanFMUXloanhUTzJYMTEzRWJSVDU0OXdhOXpNUzQwdEhEYnpHcW94REJsYUxUUE13eDJ0WjhpVURnS1Q3Njd1OHRlNXU3RUU2NWlJVDl0VUsybC1uSlRBQ1BuMkNPcENZUWM?oc=5>

## CATALYSTS

### TMC the metals company faces earnings test as NOAA decision looms
- Summary: TMC the metals company faces earnings test as NOAA decision looms
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxQTkoxanZaM3FMX1l4alBlX0RCNmpXV3FlaW9iLVI4OGU4YlZDYVJBZFp0MGVrdGNPemdRQzg2Q0F2RFpIdU9SaGZ0bjhtZW1HTHI1dWVrQUZlWDFPOFJJRFNaSDFtWFJnalIxeUJBVFN0OG1SZkgxS1lYV19feWxoNGNEdmIwcjh2SG1WaVpEWVNFTllaWjNUS0k4elVud3dsdnFBYjk5WTYxTjNrVDJhcHdpbU5FTGlPZXVwb1RIM210dUgz?oc=5>

### The Metals Company (TMC) Set to Report Q3 Earnings Amid Continued Losses and Strategic Progress
- Summary: The Metals Company (TMC) Set to Report Q3 Earnings Amid Continued Losses and Strategic Progress
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizAFBVV95cUxPcHRuVDYwOEh3aGFrZzR0TmFvdTd2UEpGMERFa0V1Z1ZXWG5Yb0FiOWoxN1o0alF6S0ZfaWFLOGlpT29XanlVcVBDLTdkWDVENWVNMWtYRGZXSzAwRG5vMUVJbEdTSFVRZjJCT29Kbk9WNjRVTEVhZEhFU1BncHFhdWdualFMRnRncUhqUUhVMF9MeUFMNkZjOFhkM1ZqVG1PLXplbnU2UDRBWVVmSWFHVHMzSzdCZ3RVbEhYZnBycS1YREF0OEhVc3NLN2s?oc=5>

### TMC: TMC the metals company Inc. filed SEC Form 8-K: Regulation FD Disclosure, Financial Statements and Exhibits
- Summary: SEC filing discloses financial statements and exhibits.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxPeHdGQldEN3F1Z2ZEWlBoQkFGWEJBUkNNUmwyNFJRWmRZbjJ1UHhzekp5UTNrX3NkSVZJQzRzdWROYUllODlJa1NQQ0JIaDkwYVd0dmJEZmVOd0lRbU1NNXdKYzNzS21KMnhrVEhVclNFX3lMc0RDZzUxNG9DZ1VoVUFoVUJpSC1CODNSdnRZRTRnQUtNN3k4X1JQYW1iUFp5?oc=5>

### TMC The Metals Company Q3 Loss Narrows
- Summary: TMC's Q3 loss narrowed, indicating improved profitability.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxQRFlJTEZfOGE1dWxTRzFsTnhWaUJSdjE1NlZtaHFDMVI2Y2doaVYwRGhmd0JuS0JVd2hFRDhNX28wYUZpMC02MWo1cUVBc1dRMjA1Z0hHNHJkVHdac3E5QXhLWHpnYjd0WlVsblJuRzVkSzRzZ2pMM1NyR3EwU0V4UmFBZ0lhdTlFM3VsVWY0NUpoVldoZVE?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **TMC** | **N/A** | **-36.51** | **-4.46** | **N/A** | **1,014,611,584.00 USD** | **-59.22** |
| MP | N/A | 3.42 | 108.07 | 190.90 | 6,676,135,424.00 USD | -37.29 |
| LAC | N/A | 0.48 | -22.74 | N/A | 591,760,000.00 USD | -66.53 |
| VALE | 70.50 | 1.24 | 1.95 | -3.90 | 48,005,013,504.00 USD | -2.12 |

Peers fetched as_of: 2026-11-12; TMC reuses existing data (market data as_of: 2026-11-12); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-13
- Next expected earnings: 2026-11-12 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-12

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-12
- Revenue (latest available single quarter): 410,000.00 USD; period 2024-04-01/2024-06-30; fiscal year/reporting period 2024/Q2
- Net income (latest available single quarter): -28,361,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1798562/000162828026073463/tmc-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiuwFBVV95cUxNWnBteDlONHNON0RqVmhlVnduVjBrTlJ2Mm1uYV9jT2FrTTJ5VWFEbjg0TWsyVW9hV2ZGMjRiN1A3dnhkcnJOVVNkeVVma1hwa2tOXzFMTGg3M05CVFhKUjFpZTlWOVF5LXhNNlIyQUl3NHhsbHc2U2ZDby1wWUxKMmdWZW9MR1dFMVVTQ0VtRjlSbl9DS3R1dWJmWkZ2VG40LUJRcTMzUzAyVk1OQmNDV0hKZTVJWmM1dFRZ?oc=5
- https://news.google.com/rss/articles/CBMizwFBVV95cUxPMUs3TUlOM2x1WjRNcUtxaVdMTTBiTjhLY05YOTNCb0xjNFNmUmVfNWc4bXEtQlRRQkVCQjRlR3B5YzdjdE5qdzBULVFCYXhFRWlkYl9NbW9SRjFDMDdDWWozaXM0UWl1WHhGYnYzanFMUXloanhUTzJYMTEzRWJSVDU0OXdhOXpNUzQwdEhEYnpHcW94REJsYUxUUE13eDJ0WjhpVURnS1Q3Njd1OHRlNXU3RUU2NWlJVDl0VUsybC1uSlRBQ1BuMkNPcENZUWM?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxQTkoxanZaM3FMX1l4alBlX0RCNmpXV3FlaW9iLVI4OGU4YlZDYVJBZFp0MGVrdGNPemdRQzg2Q0F2RFpIdU9SaGZ0bjhtZW1HTHI1dWVrQUZlWDFPOFJJRFNaSDFtWFJnalIxeUJBVFN0OG1SZkgxS1lYV19feWxoNGNEdmIwcjh2SG1WaVpEWVNFTllaWjNUS0k4elVud3dsdnFBYjk5WTYxTjNrVDJhcHdpbU5FTGlPZXVwb1RIM210dUgz?oc=5
- https://news.google.com/rss/articles/CBMizAFBVV95cUxPcHRuVDYwOEh3aGFrZzR0TmFvdTd2UEpGMERFa0V1Z1ZXWG5Yb0FiOWoxN1o0alF6S0ZfaWFLOGlpT29XanlVcVBDLTdkWDVENWVNMWtYRGZXSzAwRG5vMUVJbEdTSFVRZjJCT29Kbk9WNjRVTEVhZEhFU1BncHFhdWdualFMRnRncUhqUUhVMF9MeUFMNkZjOFhkM1ZqVG1PLXplbnU2UDRBWVVmSWFHVHMzSzdCZ3RVbEhYZnBycS1YREF0OEhVc3NLN2s?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxPeHdGQldEN3F1Z2ZEWlBoQkFGWEJBUkNNUmwyNFJRWmRZbjJ1UHhzekp5UTNrX3NkSVZJQzRzdWROYUllODlJa1NQQ0JIaDkwYVd0dmJEZmVOd0lRbU1NNXdKYzNzS21KMnhrVEhVclNFX3lMc0RDZzUxNG9DZ1VoVUFoVUJpSC1CODNSdnRZRTRnQUtNN3k4X1JQYW1iUFp5?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxQRFlJTEZfOGE1dWxTRzFsTnhWaUJSdjE1NlZtaHFDMVI2Y2doaVYwRGhmd0JuS0JVd2hFRDhNX28wYUZpMC02MWo1cUVBc1dRMjA1Z0hHNHJkVHdac3E5QXhLWHpnYjd0WlVsblJuRzVkSzRzZ2pMM1NyR3EwU0V4UmFBZ0lhdTlFM3VsVWY0NUpoVldoZVE?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
