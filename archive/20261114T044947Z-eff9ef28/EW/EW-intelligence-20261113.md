# EW Intelligence Report

- ticker: **EW**
- Report as_of: **2026-11-13**
- Market data as_of: **2026-11-13**
- Quant sources: https://finance.yahoo.com/quote/EW/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/EW/key-statistics/
- AI analysis snapshot as_of: **2026-11-13**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-14T04:56:38.389631+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 12, 'rule': 5, 'ai': 3, 'unknown': 0, 'irrelevant': 4})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **4** exact headline/source/date matches; prior report **20261113T045636Z-34122c9a/EW** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 12 unique headlines; 6 named publishers; 0 exact duplicates; 12 HTTPS source links; largest publisher share 50.0%; oldest publication 2026-11-08

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 107.1500 |
| Return 1D (%) | 1.2760 |
| Return 1W (%) | 4.9050 |
| Return 1M (%) | 25.6597 |
| Return YTD (%) | 25.6892 |
| Return 1Y (%) | 24.4339 |
| Annualized volatility (%) | 25.6156 |
| Beta vs SPY | 0.5513 |
| Max drawdown (%) | -13.1855 |
| Sharpe (rf=0) | 0.9845 |
| Downside deviation (rf=0, %) | 16.8821 |
| Sortino (rf=0) | 1.4937 |
| Historical VaR 95% (1D, %) | 2.5317 |
| Historical ES 95% (1D, %) | 3.1155 |
| Correlation vs SPY | 0.2934 |
| Tracking error vs SPY (%) | 25.2405 |
| P/E (trailing) | 61.58 |
| P/B | 5.68 |
| EV/EBITDA | 27.58 |
| Revenue growth (%) | 10.50 |
| Forward P/E (estimate) | 31.64 |
| Gross margin (%) | 78.02 |
| Operating margin (%) | 28.82 |
| Return on equity (%) | 9.33 |
| Free cash flow yield (%) | 1.86 |
| MA50 | 90.4242 |
| Close vs MA50 (%) | 18.4970 |
| MA200 | 86.3349 |
| Close vs MA200 (%) | 24.1097 |
| RSI (14, Wilder) | 80.2762 |
| MACD (12,26) | 4.8196 |
| MACD signal (9) | 3.5911 |
| MACD histogram | 1.2285 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'EW': 282, 'SPY': 282}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 107.1500 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.2760 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 4.9050 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 25.6597 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 25.6892 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 24.4339 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 25.6156 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 16.8821 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.4937 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.5317 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.1155 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2934 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 25.2405 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.5513 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -13.1855 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.9845 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 31.6412 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 78.0180 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 28.8180 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 9.3330 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.8590 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 61.5805 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 80.2762 -> Overbought momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 1.2285 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 18.4970 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 24.1097 -> Clearly above the moving-average trend level.

## TAILWINDS

### Edwards Lifesciences (NYSE:EW) Sets New 12-Month High on Analyst Upgrade
- Summary: Edwards Lifesciences (NYSE:EW) Sets New 12-Month High on Analyst Upgrade
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiygFBVV95cUxQQmxMbFhlaEdNV1JXcGlSQU1jQ3h2ZFJvbXhKdUNock9sVTlVWEs3TjdDVjA5T085S1dlbVdiRHVCanQ5ajd6R0Z4U3pGd0lNWlkxOEtydEFBdDFqQ2kwLWlYZHFqYTFobWt3ZTQza1EwcU82MGNVNEoxX1ZpNVpzQkpyTzBPVno1MnRFQWxLRDBDaktOZHpBaVNnaE9wUWw0UDBGLUhmZmw1MjNtUTlUNFJ1bGtFOGFhZ1BfXzBOck9OMGRhZXJXSG5R?oc=5>

### Edwards Lifesciences (NYSE:EW) Stock Rating Upgraded by Wall Street Zen
- Summary: Edwards Lifesciences (NYSE:EW) Stock Rating Upgraded by Wall Street Zen
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiywFBVV95cUxOeXdrdC1rODh0Q05aajZZVjJELTRSaFd1RTBQOVNTSmFfR3RLQy1kcTVlWDVjdFd4X1FpR29SWXEyMUxVSFBNclRWZ05mcDRaTU1ZUXBBYlJiVW9XM1FRVXVMdlFYYWwza0Jub19weGpfTFRpU0MxbW5IdzFWZ1ktckQ2UzZLRmxoN3RiN1NwcEZBTmZKQTV0NFhlOFdCdnJnc2FwTnkxdjh6UmJJTGtaNU9EUjI4NUliQUljR25LdEhWenRZWUZkV00wNA?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Edwards Lifesciences Corporation $EW Stock Sold by Russell Investments Group Ltd.
- Summary: Edwards Lifesciences Corporation $EW Stock Sold by Russell Investments Group Ltd.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1wFBVV95cUxOT28tTzZZbXpzYnhUempPekhwTWlodmhmLUtJQ2U1WGJpTGdiRXp6NkFTTGhkS1M0T1ZOZk1SSmdUa0RCQ0RWWnZIZUVvcHIyd09tRE9GUjdyb2NnS05WM053RUdWVHJlSTg0cXhxWkFiM2NIUVRpSlFIN3VvWXhMTG1VMDJyTzg4LVBfSkxWQnJ1X200eDJmN2VheWd6QlJlZmJGWFVKRDV3cG1PS3ZXM0tkX0U5UzBfNmxfcmZVNmhhYkdtdl9teE9IQ3lrZk05ZDB5bDBoWQ?oc=5>

### Edwards Lifesciences Corporation $EW Stock Sold by Lockheed Martin Investment Management Co.
- Summary: Edwards Lifesciences Corporation $EW Stock Sold by Lockheed Martin Investment Management Co.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi5gFBVV95cUxPODJwRzl1eERGT1daZzJlS0I5WmJ4bHl1NllYNXBRYkd4Z3prNnV3Q1hDWXBlMkltWVlsY19tVFZ1ZmQzT3czWW14TENyWkhJbEFZTWtobTY5eUs5RFNCMk85T0VrSlJlTlRITnhvV0FNZUQ5aW5GZ1JCdG1mbXI3cUphNGNKamNIUmNuV0dKYk5QbWE4ZDl2bmItbjJacGQ1ZnhLQlR0WHp3cWQ0d2ZoM1FHM1Y5WllEWk1MenF4T0tOdFNWUVJJUmpvZkx1NzQydVNWcXU1ZTBWSS1pVkhXN09zUVVjZw?oc=5>

### Edwards Lifesciences (NYSE:EW) Given New $121.00 Price Target at TD Cowen
- Summary: Edwards Lifesciences (NYSE:EW) Given New $121.00 Price Target at TD Cowen
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiywFBVV95cUxNRXlYX3BxUFRPdmhBNmRYcVprNzQyVGowU2Fzb2hBMHoxS0VzakVWSUlVOHVqRmt2SlpHSGRmLVpEU2VhcFdOTFgzYmI4RFZUeXZiUUp0ZUZnYmNUMktLR0RpdWZ5ZEotM3c4cTV0YnJvLXY5cThtNUxKZUxTS1NCbC1IekpoWE5KWlRoVDNmbTFEYWk5YVVsWC16Mm5veUhMNG9jSVp4b1JxcVl1S1A2WGlOd295RHN6YzZabWtza1NHSFhJWENLNlA5QQ?oc=5>

### Edwards Lifesciences stock rating maintained at Buy by TD Cowen
- Summary: TD Cowen keeps Edwards Lifesciences buy rating, signaling confidence in the company’s prospects.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxQZlNMWExmNGZDc09BUkU1MjE3dHlrdFlMb0JkWnZnY01Db011Wl9iUDV0SGhOdDNBcWhrOHByNWFrMW1zcjZnRnVwVG1IZUlUUXZKOXBzVExrN0Y1b0pud01TYUh2MWRPdkxFNWhaYTduaVkwbFNNc1czY0JUY210WmNNeklQNlJoMk5TMktnMzZmODZwLThiRnlDNkY3WktQdFhCeXBOR1J5WVFZS0k2OE9leTFyNnM1NXVadnJwTVc?oc=5>

### Edwards Lifesciences Corporation $EW Stake Trimmed by Candriam S.C.A.
- Summary: Candriam S.C.A. reduced its stake in Edwards Lifesciences, reflecting a portfolio rebalancing.
- Date: 2026-11-09 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxPSUlNa3FJdnZtWWtjSkZydFY5aExEbFRSeWtmcmc5eEVJZTJjU3BCRjd4UndrdFBBWUVOVlZkblVhVTdnbXZTb25jN3RrNG9lQkV5d2NNZFhLM3E0UXJla05iYkU0WjdJZEJuOUxwNy1rOEg1TU5acndJNzVqLXBnanNlTnByTXZmRkpURkpVZFh6NWU2UnVtZDR3YUMzV1NwNHM1TDVUN3RTOGExeWxwTlc1MXkwRzBHY1d1MENLeWtBOUpB?oc=5>

### Is Edwards Lifesciences (EW) Fully Priced On Raised Guidance And Clinical Trial Wins?
- Summary: Edwards Lifesciences may be fully priced on new guidance and successful clinical trials, potentially boosting investor confidence.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0wFBVV95cUxPU0p6M0E0aHNSLTZ6d0tmRXhPejBqVXY5TENhVzhSTFM4c2ZMamFKaWNQakdZU3BuVlNBWEk2ai10M2V5R1ZwNFNoTjVjeUtOak1FaHFXZzJ4eE1uTUNLYk5mdWtKLUk4WVpyTlMtMkN6aFlwd3NMUHJoYS1IU3N6MWFzaXNZS0tTSnB1dXM2NVdUQlJSWnhOaVltSmIyOEwwQUhTS0podm1KMk5WWEk3VG1PaW5tY3dYbkJ2M1VnQlJ1ZmdRbGRsT01qVkNYQmRhWlV30gHYAUFVX3lxTFBBZXVBb3BDeEprcGl2VkUxR1hjR01PSG9VUXVQS3AzSGwxdmtGR0ZiblhMZ3hjYzIzSUlmV2xidkV2eE9XZ0pWNVlacGJaQjJyZ1pVaHpQOXh2SDJ2TXRxWjJVLUx1S0lLWHdGcGZQUHdxSEJhX0lGU05neXlkaGVGWXZGY2ZuZzctSXJWUmwtWWFqQkZhbWZIRkt2YnNoQ3FKZU9rd21KaEdERmZkV3JqYzZYZTZJMTREeUdfSTl5eGVmdnlndmt0YmRTOEhhVTZVMEd5Qld2NQ?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **EW** | **61.58** | **5.68** | **27.58** | **10.50** | **61,611,249,664.00 USD** | **24.43** |
| MDT | 24.79 | 2.62 | 14.58 | 13.70 | 131,572,129,792.00 USD | 10.54 |
| BSX | 18.63 | 2.51 | 13.62 | 1.40 | 64,269,643,776.00 USD | -57.76 |
| ABT | 40.04 | 3.68 | 18.82 | 14.50 | 187,950,301,184.00 USD | -13.96 |

Peers fetched as_of: 2026-11-13; EW reuses existing data (market data as_of: 2026-11-13); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-04
- Next expected earnings: 2027-02-09 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-13

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-04
- Revenue (latest available single quarter): 1,715,500,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 307,500,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1099800/000109980026000054/ew-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiygFBVV95cUxQQmxMbFhlaEdNV1JXcGlSQU1jQ3h2ZFJvbXhKdUNock9sVTlVWEs3TjdDVjA5T085S1dlbVdiRHVCanQ5ajd6R0Z4U3pGd0lNWlkxOEtydEFBdDFqQ2kwLWlYZHFqYTFobWt3ZTQza1EwcU82MGNVNEoxX1ZpNVpzQkpyTzBPVno1MnRFQWxLRDBDaktOZHpBaVNnaE9wUWw0UDBGLUhmZmw1MjNtUTlUNFJ1bGtFOGFhZ1BfXzBOck9OMGRhZXJXSG5R?oc=5
- https://news.google.com/rss/articles/CBMiywFBVV95cUxOeXdrdC1rODh0Q05aajZZVjJELTRSaFd1RTBQOVNTSmFfR3RLQy1kcTVlWDVjdFd4X1FpR29SWXEyMUxVSFBNclRWZ05mcDRaTU1ZUXBBYlJiVW9XM1FRVXVMdlFYYWwza0Jub19weGpfTFRpU0MxbW5IdzFWZ1ktckQ2UzZLRmxoN3RiN1NwcEZBTmZKQTV0NFhlOFdCdnJnc2FwTnkxdjh6UmJJTGtaNU9EUjI4NUliQUljR25LdEhWenRZWUZkV00wNA?oc=5
- https://news.google.com/rss/articles/CBMi1wFBVV95cUxOT28tTzZZbXpzYnhUempPekhwTWlodmhmLUtJQ2U1WGJpTGdiRXp6NkFTTGhkS1M0T1ZOZk1SSmdUa0RCQ0RWWnZIZUVvcHIyd09tRE9GUjdyb2NnS05WM053RUdWVHJlSTg0cXhxWkFiM2NIUVRpSlFIN3VvWXhMTG1VMDJyTzg4LVBfSkxWQnJ1X200eDJmN2VheWd6QlJlZmJGWFVKRDV3cG1PS3ZXM0tkX0U5UzBfNmxfcmZVNmhhYkdtdl9teE9IQ3lrZk05ZDB5bDBoWQ?oc=5
- https://news.google.com/rss/articles/CBMi5gFBVV95cUxPODJwRzl1eERGT1daZzJlS0I5WmJ4bHl1NllYNXBRYkd4Z3prNnV3Q1hDWXBlMkltWVlsY19tVFZ1ZmQzT3czWW14TENyWkhJbEFZTWtobTY5eUs5RFNCMk85T0VrSlJlTlRITnhvV0FNZUQ5aW5GZ1JCdG1mbXI3cUphNGNKamNIUmNuV0dKYk5QbWE4ZDl2bmItbjJacGQ1ZnhLQlR0WHp3cWQ0d2ZoM1FHM1Y5WllEWk1MenF4T0tOdFNWUVJJUmpvZkx1NzQydVNWcXU1ZTBWSS1pVkhXN09zUVVjZw?oc=5
- https://news.google.com/rss/articles/CBMiywFBVV95cUxNRXlYX3BxUFRPdmhBNmRYcVprNzQyVGowU2Fzb2hBMHoxS0VzakVWSUlVOHVqRmt2SlpHSGRmLVpEU2VhcFdOTFgzYmI4RFZUeXZiUUp0ZUZnYmNUMktLR0RpdWZ5ZEotM3c4cTV0YnJvLXY5cThtNUxKZUxTS1NCbC1IekpoWE5KWlRoVDNmbTFEYWk5YVVsWC16Mm5veUhMNG9jSVp4b1JxcVl1S1A2WGlOd295RHN6YzZabWtza1NHSFhJWENLNlA5QQ?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxQZlNMWExmNGZDc09BUkU1MjE3dHlrdFlMb0JkWnZnY01Db011Wl9iUDV0SGhOdDNBcWhrOHByNWFrMW1zcjZnRnVwVG1IZUlUUXZKOXBzVExrN0Y1b0pud01TYUh2MWRPdkxFNWhaYTduaVkwbFNNc1czY0JUY210WmNNeklQNlJoMk5TMktnMzZmODZwLThiRnlDNkY3WktQdFhCeXBOR1J5WVFZS0k2OE9leTFyNnM1NXVadnJwTVc?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxPSUlNa3FJdnZtWWtjSkZydFY5aExEbFRSeWtmcmc5eEVJZTJjU3BCRjd4UndrdFBBWUVOVlZkblVhVTdnbXZTb25jN3RrNG9lQkV5d2NNZFhLM3E0UXJla05iYkU0WjdJZEJuOUxwNy1rOEg1TU5acndJNzVqLXBnanNlTnByTXZmRkpURkpVZFh6NWU2UnVtZDR3YUMzV1NwNHM1TDVUN3RTOGExeWxwTlc1MXkwRzBHY1d1MENLeWtBOUpB?oc=5
- https://news.google.com/rss/articles/CBMi0wFBVV95cUxPU0p6M0E0aHNSLTZ6d0tmRXhPejBqVXY5TENhVzhSTFM4c2ZMamFKaWNQakdZU3BuVlNBWEk2ai10M2V5R1ZwNFNoTjVjeUtOak1FaHFXZzJ4eE1uTUNLYk5mdWtKLUk4WVpyTlMtMkN6aFlwd3NMUHJoYS1IU3N6MWFzaXNZS0tTSnB1dXM2NVdUQlJSWnhOaVltSmIyOEwwQUhTS0podm1KMk5WWEk3VG1PaW5tY3dYbkJ2M1VnQlJ1ZmdRbGRsT01qVkNYQmRhWlV30gHYAUFVX3lxTFBBZXVBb3BDeEprcGl2VkUxR1hjR01PSG9VUXVQS3AzSGwxdmtGR0ZiblhMZ3hjYzIzSUlmV2xidkV2eE9XZ0pWNVlacGJaQjJyZ1pVaHpQOXh2SDJ2TXRxWjJVLUx1S0lLWHdGcGZQUHdxSEJhX0lGU05neXlkaGVGWXZGY2ZuZzctSXJWUmwtWWFqQkZhbWZIRkt2YnNoQ3FKZU9rd21KaEdERmZkV3JqYzZYZTZJMTREeUdfSTl5eGVmdnlndmt0YmRTOEhhVTZVMEd5Qld2NQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
