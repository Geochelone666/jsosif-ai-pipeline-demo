# GIS Intelligence Report

- ticker: **GIS**
- Report as_of: **2026-11-10**
- Market data as_of: **2026-11-10**
- Quant sources: https://finance.yahoo.com/quote/GIS/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/GIS/key-statistics/
- AI analysis snapshot as_of: **2026-11-10**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-11T04:39:23.231413+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 7, 'rule': 1, 'ai': 2, 'unknown': 0, 'irrelevant': 4})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **0** exact headline/source/date matches; prior report **N/A** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 7 unique headlines; 6 named publishers; 0 exact duplicates; 7 HTTPS source links; largest publisher share 28.57%; oldest publication 2026-11-05

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 34.6000 |
| Return 1D (%) | -0.8028 |
| Return 1W (%) | 1.5258 |
| Return 1M (%) | 9.1908 |
| Return YTD (%) | -20.4578 |
| Return 1Y (%) | -19.9759 |
| Annualized volatility (%) | 30.8081 |
| Beta vs SPY | -0.3782 |
| Max drawdown (%) | -33.2524 |
| Sharpe (rf=0) | -0.5731 |
| Downside deviation (rf=0, %) | 21.5210 |
| Sortino (rf=0) | -0.8205 |
| Historical VaR 95% (1D, %) | 2.9959 |
| Historical ES 95% (1D, %) | 3.8866 |
| Correlation vs SPY | -0.1678 |
| Tracking error vs SPY (%) | 35.7407 |
| P/E (trailing) | N/A |
| P/B | 2.48 |
| EV/EBITDA | 9.28 |
| Revenue growth (%) | -2.80 |
| Forward P/E (estimate) | 10.98 |
| Gross margin (%) | 33.73 |
| Operating margin (%) | 15.24 |
| Return on equity (%) | -10.49 |
| Free cash flow yield (%) | 7.04 |
| MA50 | 34.2657 |
| Close vs MA50 (%) | 0.9755 |
| MA200 | 36.0143 |
| Close vs MA200 (%) | -3.9270 |
| RSI (14, Wilder) | 52.2581 |
| MACD (12,26) | 0.4222 |
| MACD signal (9) | 0.2138 |
| MACD histogram | 0.2083 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'GIS': 279, 'SPY': 279}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 34.6000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.8028 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 1.5258 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 9.1908 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -20.4578 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -19.9759 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 30.8081 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 21.5210 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.8205 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.9959 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.8866 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.1678 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 35.7407 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.3782 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -33.2524 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.5731 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 10.9763 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 33.7280 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 15.2430 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: -10.4950 -> Adjusted price fell over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 7.0411 -> No interpretation rule is available for this metric.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 52.2581 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.2083 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 0.9755 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -3.9270 -> Slightly below the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

No items in this run

## CATALYSTS

### General Mills Has Paid Uninterrupted Dividends for 127 Years. Here's the Yearly Payout on $5,000.
- Summary: General Mills Has Paid Uninterrupted Dividends for 127 Years. Here's the Yearly Payout on $5,000.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQUjd6MW5mZk1jZDh2el9pQXdobkVEVnpRcHdfMmxrajlZaENXWHQwSnVQNWRiYnExb1o3ZTRlZnRVdnRXQTJwNjJ1UUM1X3loQlI5TnBvLTEwUjVMYjc5ZU1Ma2hieWtrS2pNc3R6alQ0dTBnNkwzeXB4NENDdnd6OWUzNHUtRlNLQURzRmI1QVZkU1lvSi12Rw?oc=5>

### General Mills separates businesses to sharpen focus and resource allocation (GIS:NYSE)
- Summary: General Mills is restructuring its business units to improve focus and resource allocation.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxOZGVCV3U4T0lTSlM4RGgzYW1FT0pySFNJb3NsbVBESHBmajg1Z0xvTTRsTjA0Rm44ZFMyVFZ5NWltZTBLSlF2bW5ZNlBybTNoTG4tRVFQSTZJaElBTHFSY3d5SFRWOUNXZnNpOXhEWkFER3E3eHFsdTlnTGdGWGNabmlQb2h4MU1OaFpNM0dFZmhzSHZEYWV2bXFFd2lhdUxEMTdmOWZaa3RWTFFjVFpSaU9vWQ?oc=5>

### General Mills evaluating selling Häagen-Dazs business outside of North America - WSJ (GIS:NYSE)
- Summary: General Mills is considering divesting its Häagen-Dazs brand outside North America, potentially reshaping its portfolio and focus.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxOTUlWUkVIaXp1dDd6TEEwR1lkZWd2NkMxTGxzcWRVMkNVUUxmNS0xaEZzd1R6azNQR3VYYW0tRHJ4aGVOXzRxZTRCVHZoZ3RZaFUtWEZsbDY5WmhMQ29SWFpqVTZuMjZRWXVXa2MzUEM2V29tSDlhQVlXM3dkWmR4LTBBZHhzQWx6aGdrMk5aRTVVYUFENm9DLVV2TTdMTjNWYVAwdW5qcFJXLUpyVnNfeGVRaWczeXVKb015ZzRlQQ?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **GIS** | **N/A** | **2.48** | **9.28** | **-2.80** | **18,500,173,824.00 USD** | **-19.98** |
| KHC | N/A | 0.80 | 8.32 | -2.00 | 28,696,014,848.00 USD | 6.23 |
| CPB | 17.24 | 1.75 | 8.70 | -7.90 | 6,737,121,792.00 USD | -21.56 |
| SJM | 62.43 | 2.48 | 9.35 | 5.00 | 14,271,578,112.00 USD | 29.75 |

Peers fetched as_of: 2026-11-10; GIS reuses existing data (market data as_of: 2026-11-10); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-09-23
- Next expected earnings: 2026-12-23 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-10

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-09-23
- Revenue (latest available single quarter): 4,389,500,000.00 USD; period 2026-06-01/2026-08-30; fiscal year/reporting period 2027/Q1
- Net income (latest available single quarter): 397,000,000.00 USD; period 2026-06-01/2026-08-30; fiscal year/reporting period 2027/Q1
- SEC link: https://www.sec.gov/Archives/edgar/data/40704/000162828026063201/gis-20260830.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMimAFBVV95cUxQUjd6MW5mZk1jZDh2el9pQXdobkVEVnpRcHdfMmxrajlZaENXWHQwSnVQNWRiYnExb1o3ZTRlZnRVdnRXQTJwNjJ1UUM1X3loQlI5TnBvLTEwUjVMYjc5ZU1Ma2hieWtrS2pNc3R6alQ0dTBnNkwzeXB4NENDdnd6OWUzNHUtRlNLQURzRmI1QVZkU1lvSi12Rw?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxOZGVCV3U4T0lTSlM4RGgzYW1FT0pySFNJb3NsbVBESHBmajg1Z0xvTTRsTjA0Rm44ZFMyVFZ5NWltZTBLSlF2bW5ZNlBybTNoTG4tRVFQSTZJaElBTHFSY3d5SFRWOUNXZnNpOXhEWkFER3E3eHFsdTlnTGdGWGNabmlQb2h4MU1OaFpNM0dFZmhzSHZEYWV2bXFFd2lhdUxEMTdmOWZaa3RWTFFjVFpSaU9vWQ?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxOTUlWUkVIaXp1dDd6TEEwR1lkZWd2NkMxTGxzcWRVMkNVUUxmNS0xaEZzd1R6azNQR3VYYW0tRHJ4aGVOXzRxZTRCVHZoZ3RZaFUtWEZsbDY5WmhMQ29SWFpqVTZuMjZRWXVXa2MzUEM2V29tSDlhQVlXM3dkWmR4LTBBZHhzQWx6aGdrMk5aRTVVYUFENm9DLVV2TTdMTjNWYVAwdW5qcFJXLUpyVnNfeGVRaWczeXVKb015ZzRlQQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
