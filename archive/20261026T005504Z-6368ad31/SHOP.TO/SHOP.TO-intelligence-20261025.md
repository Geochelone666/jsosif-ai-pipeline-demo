# SHOP.TO Intelligence Report

- ticker: **SHOP.TO**
- Report as_of: **2026-10-25**
- Market data as_of: **2026-10-23**
- Quant sources: https://finance.yahoo.com/quote/SHOP.TO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/SHOP.TO/key-statistics/
- AI analysis snapshot as_of: **2026-10-25**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-26T00:58:39.823212+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 2, 'rule': 1, 'ai': 0, 'unknown': 0, 'irrelevant': 1})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **0** exact headline/source/date matches; prior report **N/A** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 2 unique headlines; 2 named publishers; 0 exact duplicates; 2 HTTPS source links; largest publisher share 50.0%; oldest publication 2026-10-19

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 236.2400 |
| Return 1D (%) | -0.0719 |
| Return 1W (%) | -1.4476 |
| Return 1M (%) | 17.8489 |
| Return YTD (%) | 6.8959 |
| Return 1Y (%) | 1.1691 |
| Annualized volatility (%) | 57.5136 |
| Beta vs SPY | 1.7590 |
| Max drawdown (%) | -47.6553 |
| Sharpe (rf=0) | 0.3070 |
| Downside deviation (rf=0, %) | 40.0307 |
| Sortino (rf=0) | 0.4411 |
| Historical VaR 95% (1D, %) | 6.0443 |
| Historical ES 95% (1D, %) | 7.6952 |
| Correlation vs SPY | 0.3879 |
| Tracking error vs SPY (%) | 54.3601 |
| P/E (trailing) | 115.24 |
| P/B | 17.10 |
| EV/EBITDA | 124.92 |
| Revenue growth (%) | 33.70 |
| Forward P/E (estimate) | 68.53 |
| Gross margin (%) | 47.77 |
| Operating margin (%) | 17.55 |
| Return on equity (%) | 15.54 |
| Free cash flow yield (%) | N/A |
| MA50 | 211.2150 |
| Close vs MA50 (%) | 11.8481 |
| MA200 | 180.2041 |
| Close vs MA200 (%) | 31.0958 |
| RSI (14, Wilder) | 57.6183 |
| MACD (12,26) | 10.6751 |
| MACD signal (9) | 11.6769 |
| MACD histogram | -1.0018 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'SHOP.TO': 266, 'SPY': 267}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 236.2400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.0719 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -1.4476 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 17.8489 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 6.8959 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 1.1691 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 57.5136 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 40.0307 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.4411 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 6.0443 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 7.6952 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.3879 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 54.3601 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.7590 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -47.6553 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.3070 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 68.5294 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 47.7650 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 17.5550 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 15.5430 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 115.2390 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 57.6183 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -1.0018 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 11.8481 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 31.0958 -> Clearly above the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

No items in this run

## CATALYSTS

### Shopify is still kicking butt, this analyst says
- Summary: Shopify is still kicking butt, this analyst says
- Date: 2026-10-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxQVzNuUXFoT1FvZnFGb2VPb0swZ19MNVZNRTY5WGZqS004cGRXLUdTVllyT3BfSVVYb2RDdkI4UEoza2V1ZDd5VnR0OHcyb1F2ZmJVcE80c3YwV1pUeUNzN1lPcXJrYV9PR19FMDR5TDRhM2kwcGJTLVl1Z1daR2liR1pkUG5QRDdKS0p2bXlpONIBlAFBVV95cUxNVVVjdl9qNEFGbHl6SDBWUTBfalVCZjVRWk1JTlJGMU8yc0RDXzNTQXVfYURxUVBCdnJjYmhvb3NHNFIwMG9zZDFxTEtYb2RYMnZUVTdVMlRIRnI0UTdiLVpYeU9yc1k4REhmLUNjbWNsQjRMbGowWl9BVExyWXNyQVRtcGZFU0E0NHZJRGRiVV94RUZW?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **SHOP.TO** | **115.24** | **17.10** | **124.92** | **33.70** | **306,557,943,808.00 CAD** | **1.17** |
| WIX | N/A | -2.02 | -31.11 | 14.90 | 3,429,149,184.00 USD | -41.58 |
| CRM | 22.74 | 5.33 | 18.26 | 10.80 | 204,573,114,368.00 USD | -1.71 |
| GDDY | 16.78 | 2,128.11 | 12.27 | 6.60 | 14,284,594,176.00 USD | -14.83 |

Peers fetched as_of: 2026-10-25; SHOP.TO reuses existing data (market data as_of: 2026-10-23); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-05
- Next expected earnings: 2026-11-03 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-25

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: N/A
- Filing date: N/A
- Revenue (latest available single quarter): N/A
- Net income (latest available single quarter): N/A
- SEC link: N/A

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMijwFBVV95cUxQVzNuUXFoT1FvZnFGb2VPb0swZ19MNVZNRTY5WGZqS004cGRXLUdTVllyT3BfSVVYb2RDdkI4UEoza2V1ZDd5VnR0OHcyb1F2ZmJVcE80c3YwV1pUeUNzN1lPcXJrYV9PR19FMDR5TDRhM2kwcGJTLVl1Z1daR2liR1pkUG5QRDdKS0p2bXlpONIBlAFBVV95cUxNVVVjdl9qNEFGbHl6SDBWUTBfalVCZjVRWk1JTlJGMU8yc0RDXzNTQXVfYURxUVBCdnJjYmhvb3NHNFIwMG9zZDFxTEtYb2RYMnZUVTdVMlRIRnI0UTdiLVpYeU9yc1k4REhmLUNjbWNsQjRMbGowWl9BVExyWXNyQVRtcGZFU0E0NHZJRGRiVV94RUZW?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
