# TMC Intelligence Report

- ticker: **TMC**
- Report as_of: **2026-10-29**
- Market data as_of: **2026-10-29**
- Quant sources: https://finance.yahoo.com/quote/TMC/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/TMC/key-statistics/
- AI analysis snapshot as_of: **2026-10-29**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-30T02:36:02.261796+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 6, 'rule': 1, 'ai': 3, 'unknown': 0, 'irrelevant': 2})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **0** exact headline/source/date matches; prior report **N/A** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'short_term_price_move_in_structural_risks': 2}
- RSS source audit (metadata only, not article fact-checking): 6 unique headlines; 6 named publishers; 0 exact duplicates; 6 HTTPS source links; largest publisher share 16.67%; oldest publication 2026-10-22

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 2.8400 |
| Return 1D (%) | 1.4286 |
| Return 1W (%) | 14.9798 |
| Return 1M (%) | -24.0642 |
| Return YTD (%) | -53.9708 |
| Return 1Y (%) | -58.7209 |
| Annualized volatility (%) | 91.6918 |
| Beta vs SPY | 3.4678 |
| Max drawdown (%) | -74.6822 |
| Sharpe (rf=0) | -0.5167 |
| Downside deviation (rf=0, %) | 61.5650 |
| Sortino (rf=0) | -0.7695 |
| Historical VaR 95% (1D, %) | 8.7111 |
| Historical ES 95% (1D, %) | 11.6409 |
| Correlation vs SPY | 0.4807 |
| Tracking error vs SPY (%) | 86.3048 |
| P/E (trailing) | N/A |
| P/B | -45.08 |
| EV/EBITDA | -5.62 |
| Revenue growth (%) | N/A |
| Forward P/E (estimate) | N/A |
| Gross margin (%) | 0.00 |
| Operating margin (%) | 0.00 |
| Return on equity (%) | -1123.19 |
| Free cash flow yield (%) | 1.66 |
| MA50 | 3.7172 |
| Close vs MA50 (%) | -23.5984 |
| MA200 | 4.9225 |
| Close vs MA200 (%) | -42.3060 |
| RSI (14, Wilder) | 41.5528 |
| MACD (12,26) | -0.3083 |
| MACD signal (9) | -0.3511 |
| MACD histogram | 0.0428 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'TMC': 271, 'SPY': 271}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 2.8400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.4286 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 14.9798 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -24.0642 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -53.9708 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -58.7209 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 91.6918 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 61.5650 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.7695 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 8.7111 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 11.6409 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4807 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 86.3048 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 3.4678 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -74.6822 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.5167 -> Negative risk-adjusted return.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 0.0000 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 0.0000 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: -1123.1911 -> Adjusted price fell over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.6589 -> No interpretation rule is available for this metric.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 41.5528 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.0428 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -23.5984 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -42.3060 -> Clearly below the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

No items in this run

## CATALYSTS

### The Metals Company Trades at $2.65. Analysts See It at $10. Here's What Would Need to Go Right for It to Close That Gap.
- Summary: The Metals Company Trades at $2.65. Analysts See It at $10. Here's What Would Need to Go Right for It to Close That Gap.
- Date: 2026-10-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxPRERZUHVZemxqckRSS3BMMHlSNnk1cEJDX1p5X0xDWk1nSm4wcWRNREE0Mzg2bVFUend2b1pLYjlpVHFudjdhQUdnbmZ3VzZITTdIOWZsRkM3R3NYNHZoSEJfVFQ2Q3M3Tl9qa21wQi1vQ20zMEJtSWJUM0pOY1p2Ni1ITjR4UHcyNVQxM2JuaEZVQkU?oc=5>

### USA Rare Earth Soars 13%, Critical Metals Up 12%, TMC Up 11% as Critical Minerals Stocks Rally
- Summary: TMC shares rise 11% amid critical minerals rally.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxNVS16UEVvajlvV2I5eFRIcDBNa3dvekw1QXN4VUhvYlFIanIwVzBwU2VpWXlqMDByMWwtSkszYTZUai1xSzB5TXdyTWJ5a0MzTXZYVzNfMzFKb211VnNDMmtLVkZCOHF3SGh6Q1FsSlJFdy15S19sWVNwcTktcFd6RTJVTi1lYm5JRnVTdEczTldDQzA3aVdEd1R3elFtZDVrX1ExZEYyUk85SDBmYzNZOVBrOXFrQQ?oc=5>

## RISKS

### TMC stock hits 52-week low at 2.47 USD
- Summary: TMC shares fall to 52‑week low.
- Date: 2026-10-22 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQNkZTMU9GUHh3UlJuYXhyUGVTenRKYk9sVGphalg4ZGFDZE1ib21vMGROQXp5cF96VU1MT0hPUUJQeXl0RlFOUVU2LTNQTi1xbF91NDM2MjZaVjJZaEdVVnU1a1FILWt1NTJjRVZfOEVVWFNyZm5ZbzFScXlnODNQcWFfcGRJZ2F0d2xYTC1aSmRsVVZscVdnUA?oc=5>

### TMC stock hits 52-week low at 2.47 USD By Investing.com
- Summary: TMC shares fall to 52‑week low.
- Date: 2026-10-22 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxOLWM1enFRaVM1NE8xaW9ZSS1PQTN4WjEwNW1uYUlhTm5qS3l4TzNVaHJVMEV3X3UydmVOTWZCc2FiSGpZQTc5RTVfSTh4Q1pJMkRucEhhWFBzbzBBLXI2QzNPa25rNnB5ZDJxMUJ5MGlWdkU1dVdHWHZjME1Cd3VJMlRCS3VkVm51aVEyUG5hN1d2U2lySUtFZTRwSGJDZw?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **TMC** | **N/A** | **-45.08** | **-5.62** | **N/A** | **1,252,824,704.00 USD** | **-58.72** |
| MP | N/A | 3.79 | 180.91 | 119.70 | 7,416,150,016.00 USD | -35.23 |
| LAC | N/A | 0.54 | -25.43 | N/A | 773,281,536.00 USD | -62.96 |
| VALE | 22.36 | 1.22 | 1.71 | 6.40 | 47,579,426,816.00 USD | 2.35 |

Peers fetched as_of: 2026-10-29; TMC reuses existing data (market data as_of: 2026-10-29); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-13
- Next expected earnings: 2026-11-12 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-29

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

- https://news.google.com/rss/articles/CBMikwFBVV95cUxPRERZUHVZemxqckRSS3BMMHlSNnk1cEJDX1p5X0xDWk1nSm4wcWRNREE0Mzg2bVFUend2b1pLYjlpVHFudjdhQUdnbmZ3VzZITTdIOWZsRkM3R3NYNHZoSEJfVFQ2Q3M3Tl9qa21wQi1vQ20zMEJtSWJUM0pOY1p2Ni1ITjR4UHcyNVQxM2JuaEZVQkU?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxNVS16UEVvajlvV2I5eFRIcDBNa3dvekw1QXN4VUhvYlFIanIwVzBwU2VpWXlqMDByMWwtSkszYTZUai1xSzB5TXdyTWJ5a0MzTXZYVzNfMzFKb211VnNDMmtLVkZCOHF3SGh6Q1FsSlJFdy15S19sWVNwcTktcFd6RTJVTi1lYm5JRnVTdEczTldDQzA3aVdEd1R3elFtZDVrX1ExZEYyUk85SDBmYzNZOVBrOXFrQQ?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQNkZTMU9GUHh3UlJuYXhyUGVTenRKYk9sVGphalg4ZGFDZE1ib21vMGROQXp5cF96VU1MT0hPUUJQeXl0RlFOUVU2LTNQTi1xbF91NDM2MjZaVjJZaEdVVnU1a1FILWt1NTJjRVZfOEVVWFNyZm5ZbzFScXlnODNQcWFfcGRJZ2F0d2xYTC1aSmRsVVZscVdnUA?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxOLWM1enFRaVM1NE8xaW9ZSS1PQTN4WjEwNW1uYUlhTm5qS3l4TzNVaHJVMEV3X3UydmVOTWZCc2FiSGpZQTc5RTVfSTh4Q1pJMkRucEhhWFBzbzBBLXI2QzNPa25rNnB5ZDJxMUJ5MGlWdkU1dVdHWHZjME1Cd3VJMlRCS3VkVm51aVEyUG5hN1d2U2lySUtFZTRwSGJDZw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
