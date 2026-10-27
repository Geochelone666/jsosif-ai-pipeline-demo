# TMC Intelligence Report

- ticker: **TMC**
- Report as_of: **2026-10-26**
- Market data as_of: **2026-10-26**
- Quant sources: https://finance.yahoo.com/quote/TMC/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/TMC/key-statistics/
- AI analysis snapshot as_of: **2026-10-26**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-27T02:10:42.804473+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 6, 'rule': 2, 'ai': 4, 'unknown': 0})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **0** exact headline/source/date matches; prior report **N/A** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 6 unique headlines; 6 named publishers; 1 exact duplicates; 6 HTTPS source links; largest publisher share 16.67%; oldest publication 2026-10-22

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 2.3900 |
| Return 1D (%) | -1.6461 |
| Return 1W (%) | -8.7786 |
| Return 1M (%) | -39.1857 |
| Return YTD (%) | -61.2642 |
| Return 1Y (%) | -66.4797 |
| Annualized volatility (%) | 90.5695 |
| Beta vs SPY | 3.4330 |
| Max drawdown (%) | -74.6822 |
| Sharpe (rf=0) | -0.7287 |
| Downside deviation (rf=0, %) | 61.7082 |
| Sortino (rf=0) | -1.0695 |
| Historical VaR 95% (1D, %) | 8.7111 |
| Historical ES 95% (1D, %) | 11.6409 |
| Correlation vs SPY | 0.4820 |
| Tracking error vs SPY (%) | 85.1723 |
| P/E (trailing) | N/A |
| P/B | -37.94 |
| EV/EBITDA | -4.65 |
| Revenue growth (%) | N/A |
| Forward P/E (estimate) | N/A |
| Gross margin (%) | 0.00 |
| Operating margin (%) | 0.00 |
| Return on equity (%) | -1123.19 |
| Free cash flow yield (%) | 1.97 |
| MA50 | 3.7826 |
| Close vs MA50 (%) | -36.8159 |
| MA200 | 4.9896 |
| Close vs MA200 (%) | -52.1001 |
| RSI (14, Wilder) | 21.8755 |
| MACD (12,26) | -0.4059 |
| MACD signal (9) | -0.3651 |
| MACD histogram | -0.0408 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'TMC': 268, 'SPY': 268}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 2.3900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.6461 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -8.7786 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -39.1857 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -61.2642 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -66.4797 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 90.5695 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 61.7082 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -1.0695 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 8.7111 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 11.6409 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4820 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 85.1723 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 3.4330 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -74.6822 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.7287 -> Negative risk-adjusted return.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 0.0000 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 0.0000 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: -1123.1911 -> Adjusted price fell over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.9713 -> No interpretation rule is available for this metric.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 21.8755 -> Oversold momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.0408 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -36.8159 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -52.1001 -> Clearly below the moving-average trend level.

## TAILWINDS

### TMC Stock Gains On NOAA Compliance Ruling In A Boost To US Critical Metals Push
- Summary: TMC Stock Gains On NOAA Compliance Ruling In A Boost To US Critical Metals Push
- Date: 2026-10-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxPU2VKTTZTaFFpRGRTM2xzQlphMnVwbWFUNVdqVGx2R2dwa2dmNGxPRzRUUWQwMXZocEVkMzBLcnNJcDZxaTBkaFk0U3FWSFNMUms4aTk0XzFkdlZKUWFub0NHRFlvY0E4NHJVWUd4VWUzSVhUSG45VEhNd3hWUXpyTTE3dGliSWpDV2xqU2l1djJsUmZiZnpOdWMtZ19lLTlxMXkzWGFMdjlxbkZvTGZyV0pyeWNkalFISkF4UU9sQkVWV1dF?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### The Metals Company Trades at $2.65. Analysts See It at $10. Here's What Would Need to Go Right for It to Close That Gap.
- Summary: The Metals Company Trades at $2.65. Analysts See It at $10. Here's What Would Need to Go Right for It to Close That Gap.
- Date: 2026-10-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxPRERZUHVZemxqckRSS3BMMHlSNnk1cEJDX1p5X0xDWk1nSm4wcWRNREE0Mzg2bVFUend2b1pLYjlpVHFudjdhQUdnbmZ3VzZITTdIOWZsRkM3R3NYNHZoSEJfVFQ2Q3M3Tl9qa21wQi1vQ20zMEJtSWJUM0pOY1p2Ni1ITjR4UHcyNVQxM2JuaEZVQkU?oc=5>

### TMC stock hits 52-week low at 2.47 USD
- Summary: TMC shares fell to a 52‑week low of $2.47, indicating a sharp decline in market value.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQNkZTMU9GUHh3UlJuYXhyUGVTenRKYk9sVGphalg4ZGFDZE1ib21vMGROQXp5cF96VU1MT0hPUUJQeXl0RlFOUVU2LTNQTi1xbF91NDM2MjZaVjJZaEdVVnU1a1FILWt1NTJjRVZfOEVVWFNyZm5ZbzFScXlnODNQcWFfcGRJZ2F0d2xYTC1aSmRsVVZscVdnUA?oc=5>

### TMC the metals company Inc. Estimates – NASDAQ:TMC
- Summary: TMC released its latest earnings estimates, providing guidance on future financial performance.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMid0FVX3lxTE41Tjdla1dFSGpDNHcxZUZ3M0t4MFhBNG0ybUJoZS1ZSVpQWWoxdFI4d0hJUHFPREFjZVhyZW1vZ19lSkhxdUdfVlNBajJhbVZXT2xlSnpFOWxweFlFRDFUWDZ1akJZaDVVWFRlNlhobE9WUm9vdnRz?oc=5>

### What's Behind TMC the Metals Company (NASDAQ:TMC) Penny Stock's Decline This Month
- Summary: Analysis explains factors contributing to TMC's penny stock decline during the month.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxQNlZTTkM2b2N3SFl3dDNzMkxhaFh6ajlMVlE3Q2FROTBya1BHWjZMS0E0Zk9FUHZidWpVQWR5Q1ppU2JiT1FFSm1uQmU3dDRnU1dWQkoyLTVWVjQyYzVLelR1Mm81WTVfWnNkM0NLNFVILWhBczVueDNGRi1oVFhCVjNiOWNXaVl6SUFOZVRySGlfOG1VSzFuV0pHbGlVRm5JelJrekpsVlM0T245NTZtVS12bVE?oc=5>

### TMC stock hits 52-week low at 2.47 USD By Investing.com
- Summary: Investing.com reports TMC shares at a 52‑week low of $2.47, reflecting a significant drop.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxQb2tlQWlWWmNDWmtMS0lZY0F1b3EyTms1VHloaEhROTB1bXNPWml0cG1hcC1JTThYbzAtc1pCMU93bjFKOEtBT1hlWmpDVEJZZXotOHE3Y3JxS1EyY0ZxMTQwVlAxdkdPNWJOdVp1RWF4VzdmVjVSOHEyenpjdXAxVndkSmZqYVAxeDZqRngwUl9YMWdDU3FFQXVWVU5xdw?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **TMC** | **N/A** | **-37.94** | **-4.65** | **N/A** | **1,054,313,856.00 USD** | **-66.48** |
| MP | N/A | 3.41 | 162.65 | 119.70 | 6,673,466,368.00 USD | -47.08 |
| LAC | N/A | 0.52 | -24.82 | N/A | 733,346,752.00 USD | -69.94 |
| VALE | 24.00 | 1.31 | 1.76 | 6.40 | 51,069,153,280.00 USD | 13.90 |

Peers fetched as_of: 2026-10-26; TMC reuses existing data (market data as_of: 2026-10-26); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-13
- Next expected earnings: 2026-11-12 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-26

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-08-13
- Revenue (latest available single quarter): 410,000.00 USD; period 2024-04-01/2024-06-30; fiscal year/reporting period 2024/Q2
- Net income (latest available single quarter): -60,123,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/1798562/000110465926096051/tmc-20260630x10q.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMixAFBVV95cUxPU2VKTTZTaFFpRGRTM2xzQlphMnVwbWFUNVdqVGx2R2dwa2dmNGxPRzRUUWQwMXZocEVkMzBLcnNJcDZxaTBkaFk0U3FWSFNMUms4aTk0XzFkdlZKUWFub0NHRFlvY0E4NHJVWUd4VWUzSVhUSG45VEhNd3hWUXpyTTE3dGliSWpDV2xqU2l1djJsUmZiZnpOdWMtZ19lLTlxMXkzWGFMdjlxbkZvTGZyV0pyeWNkalFISkF4UU9sQkVWV1dF?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxPRERZUHVZemxqckRSS3BMMHlSNnk1cEJDX1p5X0xDWk1nSm4wcWRNREE0Mzg2bVFUend2b1pLYjlpVHFudjdhQUdnbmZ3VzZITTdIOWZsRkM3R3NYNHZoSEJfVFQ2Q3M3Tl9qa21wQi1vQ20zMEJtSWJUM0pOY1p2Ni1ITjR4UHcyNVQxM2JuaEZVQkU?oc=5
- https://news.google.com/rss/articles/CBMiekFVX3lxTE8zaG13RUZfYVk4ekVzaDFuLUxGaXdaZkQwSnVqYXppY05NMUJRejhndTlvd2VVWVhEMTV1SkpDaHRFN1llVGtrTDRia05pUGYtYkVadlNlRWFobE9UVHVYeGctYzUwUXNNQlExV2ZlN0htbWdUUE5KS0d3?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQNkZTMU9GUHh3UlJuYXhyUGVTenRKYk9sVGphalg4ZGFDZE1ib21vMGROQXp5cF96VU1MT0hPUUJQeXl0RlFOUVU2LTNQTi1xbF91NDM2MjZaVjJZaEdVVnU1a1FILWt1NTJjRVZfOEVVWFNyZm5ZbzFScXlnODNQcWFfcGRJZ2F0d2xYTC1aSmRsVVZscVdnUA?oc=5
- https://news.google.com/rss/articles/CBMid0FVX3lxTE41Tjdla1dFSGpDNHcxZUZ3M0t4MFhBNG0ybUJoZS1ZSVpQWWoxdFI4d0hJUHFPREFjZVhyZW1vZ19lSkhxdUdfVlNBajJhbVZXT2xlSnpFOWxweFlFRDFUWDZ1akJZaDVVWFRlNlhobE9WUm9vdnRz?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxQNlZTTkM2b2N3SFl3dDNzMkxhaFh6ajlMVlE3Q2FROTBya1BHWjZMS0E0Zk9FUHZidWpVQWR5Q1ppU2JiT1FFSm1uQmU3dDRnU1dWQkoyLTVWVjQyYzVLelR1Mm81WTVfWnNkM0NLNFVILWhBczVueDNGRi1oVFhCVjNiOWNXaVl6SUFOZVRySGlfOG1VSzFuV0pHbGlVRm5JelJrekpsVlM0T245NTZtVS12bVE?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxQb2tlQWlWWmNDWmtMS0lZY0F1b3EyTms1VHloaEhROTB1bXNPWml0cG1hcC1JTThYbzAtc1pCMU93bjFKOEtBT1hlWmpDVEJZZXotOHE3Y3JxS1EyY0ZxMTQwVlAxdkdPNWJOdVp1RWF4VzdmVjVSOHEyenpjdXAxVndkSmZqYVAxeDZqRngwUl9YMWdDU3FFQXVWVU5xdw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
