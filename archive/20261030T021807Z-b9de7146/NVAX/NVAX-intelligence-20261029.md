# NVAX Intelligence Report

- ticker: **NVAX**
- Report as_of: **2026-10-29**
- Market data as_of: **2026-10-29**
- Quant sources: https://finance.yahoo.com/quote/NVAX/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NVAX/key-statistics/
- AI analysis snapshot as_of: **2026-10-29**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-30T02:31:30.184058+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 9, 'rule': 1, 'ai': 1, 'unknown': 0, 'irrelevant': 7})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **4** exact headline/source/date matches; prior report **20261029T020157Z-688a53f0/NVAX** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 9 unique headlines; 7 named publishers; 0 exact duplicates; 9 HTTPS source links; largest publisher share 33.33%; oldest publication 2026-10-22

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 10.4700 |
| Return 1D (%) | 1.4535 |
| Return 1W (%) | 4.8048 |
| Return 1M (%) | -3.2347 |
| Return YTD (%) | 55.8036 |
| Return 1Y (%) | 24.9403 |
| Annualized volatility (%) | 70.8837 |
| Beta vs SPY | 1.9978 |
| Max drawdown (%) | -34.5844 |
| Sharpe (rf=0) | 0.6568 |
| Downside deviation (rf=0, %) | 41.6096 |
| Sortino (rf=0) | 1.1188 |
| Historical VaR 95% (1D, %) | 5.9349 |
| Historical ES 95% (1D, %) | 7.7057 |
| Correlation vs SPY | 0.3582 |
| Tracking error vs SPY (%) | 67.3838 |
| P/E (trailing) | N/A |
| P/B | -9.05 |
| EV/EBITDA | -12.85 |
| Revenue growth (%) | -76.30 |
| Forward P/E (estimate) | N/A |
| Gross margin (%) | -2.56 |
| Operating margin (%) | -89.61 |
| Return on equity (%) | N/A |
| Free cash flow yield (%) | 8.88 |
| MA50 | 10.4264 |
| Close vs MA50 (%) | 0.4182 |
| MA200 | 9.2852 |
| Close vs MA200 (%) | 12.7601 |
| RSI (14, Wilder) | 47.8403 |
| MACD (12,26) | -0.1282 |
| MACD signal (9) | 0.1093 |
| MACD histogram | -0.2375 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NVAX': 271, 'SPY': 271}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 10.4700 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.4535 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 4.8048 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -3.2347 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 55.8036 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 24.9403 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 70.8837 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 41.6096 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.1188 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 5.9349 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 7.7057 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.3582 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 67.3838 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.9978 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -34.5844 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.6568 -> Modest risk-adjusted return.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: -2.5580 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: -89.6080 -> No interpretation rule is available for this metric.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 8.8822 -> No interpretation rule is available for this metric.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 47.8403 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.2375 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 0.4182 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 12.7601 -> Clearly above the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

### Novavax (NVAX) Stock Falls Amid Market Uptick: What Investors Need to Know
- Summary: Novavax (NVAX) Stock Falls Amid Market Uptick: What Investors Need to Know
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxOX01Na1ozU085VFhKMlVzUndqOEVXdURuYTh0b2djRU9vc2VybXJfa1F6SGZjcUh1YnJMdkVHMmVXbDFtc09nN1FleTUtYWxpSHU0SERIOFpTUV91ZFlqNnBoaXNHWWg3ZUlrTHhNZjY1LVpBVVJfVExocVBLbDduY2I4aWozeDdMd2U5emxmMzRHcDZpcW1MZUpB?oc=5>

## CATALYSTS

### A flu-COVID vaccine trial in people 60 and older brings Novavax $125 million
- Summary: Novavax reports $125 million from a flu-COVID vaccine trial targeting seniors, indicating progress in product development and potential revenue boost.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxPemwxNE1GcXZ2cDRpVHFXbXNvb0hTd2lZUlZLc0dpZlBDUmNEeXFHZVdUNjJyU2J1MVlMXzY3THZhei11azhCY0dvS3ZZNVU4ZHEzSFRNc2lCdmhiSDFod1JsTzZjckpueVp6ZVRKWU5WcFNKaGRyMUx2NnpVMEZRUGdWOURGdF95OGtIZmQ3d2lTVVM0SWNPY2ZZVWp3Y2FOWkVLTW5QZ0N4bFMwSWY0ZHcza1RtbTFy?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NVAX** | **N/A** | **-9.05** | **-12.85** | **-76.30** | **1,726,981,760.00 USD** | **24.94** |
| MRNA | N/A | 13.15 | -38.76 | 2.10 | 88,933,785,600.00 USD | 801.86 |
| BNTX | N/A | 1.12 | -6.69 | -59.50 | 22,389,843,968.00 USD | -13.76 |
| GSK | 16.96 | 3.88 | N/A | 4.00 | 97,531,125,760.00 USD | 9.74 |

Peers fetched as_of: 2026-10-29; NVAX reuses existing data (market data as_of: 2026-10-29); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-06
- Next expected earnings: 2026-11-05 (yfinance; expected dates may change)

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
- Filing date: 2026-08-06
- Revenue (latest available single quarter): 56,698,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- Net income (latest available single quarter): -53,387,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/1000694/000100069426000018/nvax-20260630.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMimgFBVV95cUxOX01Na1ozU085VFhKMlVzUndqOEVXdURuYTh0b2djRU9vc2VybXJfa1F6SGZjcUh1YnJMdkVHMmVXbDFtc09nN1FleTUtYWxpSHU0SERIOFpTUV91ZFlqNnBoaXNHWWg3ZUlrTHhNZjY1LVpBVVJfVExocVBLbDduY2I4aWozeDdMd2U5emxmMzRHcDZpcW1MZUpB?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxPemwxNE1GcXZ2cDRpVHFXbXNvb0hTd2lZUlZLc0dpZlBDUmNEeXFHZVdUNjJyU2J1MVlMXzY3THZhei11azhCY0dvS3ZZNVU4ZHEzSFRNc2lCdmhiSDFod1JsTzZjckpueVp6ZVRKWU5WcFNKaGRyMUx2NnpVMEZRUGdWOURGdF95OGtIZmQ3d2lTVVM0SWNPY2ZZVWp3Y2FOWkVLTW5QZ0N4bFMwSWY0ZHcza1RtbTFy?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
