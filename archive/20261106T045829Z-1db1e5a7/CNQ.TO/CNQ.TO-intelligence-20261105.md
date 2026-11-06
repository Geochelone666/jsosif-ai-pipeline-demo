# CNQ.TO Intelligence Report

- ticker: **CNQ.TO**
- Report as_of: **2026-11-05**
- Market data as_of: **2026-11-05**
- Quant sources: https://finance.yahoo.com/quote/CNQ.TO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/CNQ.TO/key-statistics/
- AI analysis snapshot as_of: **2026-11-05**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-06T05:17:34.395108+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 5, 'rule': 1, 'ai': 2, 'unknown': 0, 'irrelevant': 2})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **1** exact headline/source/date matches; prior report **20261105T045846Z-bde0a1fe/CNQ.TO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 5 unique headlines; 3 named publishers; 0 exact duplicates; 5 HTTPS source links; largest publisher share 60.0%; oldest publication 2026-11-04

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 68.4800 |
| Return 1D (%) | -1.0405 |
| Return 1W (%) | -11.1226 |
| Return 1M (%) | -0.6528 |
| Return YTD (%) | 51.5733 |
| Return 1Y (%) | 58.6015 |
| Annualized volatility (%) | 31.7595 |
| Beta vs SPY | -0.5718 |
| Max drawdown (%) | -18.6770 |
| Sharpe (rf=0) | 1.6187 |
| Downside deviation (rf=0, %) | 22.2849 |
| Sortino (rf=0) | 2.3069 |
| Historical VaR 95% (1D, %) | 3.2969 |
| Historical ES 95% (1D, %) | 4.7931 |
| Correlation vs SPY | -0.2454 |
| Tracking error vs SPY (%) | 37.5797 |
| P/E (trailing) | 10.00 |
| P/B | 3.03 |
| EV/EBITDA | 8.30 |
| Revenue growth (%) | 69.50 |
| Forward P/E (estimate) | 11.03 |
| Gross margin (%) | 51.58 |
| Operating margin (%) | 43.09 |
| Return on equity (%) | 26.68 |
| Free cash flow yield (%) | 5.26 |
| MA50 | 71.1872 |
| Close vs MA50 (%) | -3.8030 |
| MA200 | 63.3119 |
| Close vs MA200 (%) | 8.1630 |
| RSI (14, Wilder) | 36.0636 |
| MACD (12,26) | 0.5689 |
| MACD signal (9) | 1.5678 |
| MACD histogram | -0.9990 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'CNQ.TO': 275, 'SPY': 276}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 68.4800 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.0405 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -11.1226 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -0.6528 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 51.5733 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 58.6015 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 31.7595 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 22.2849 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 2.3069 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.2969 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.7931 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.2454 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 37.5797 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.5718 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -18.6770 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.6187 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 11.0288 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 51.5760 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 43.0910 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 26.6850 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 5.2561 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 9.9971 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 36.0636 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.9990 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -3.8030 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 8.1630 -> Clearly above the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

No items in this run

## CATALYSTS

### Canadian Natural Resources Limited Announces Quarterly Dividend
- Summary: Canadian Natural Resources Limited Announces Quarterly Dividend
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxNN1pBd1VDN1VKSzJQaWFwZHlKOEpmUFpod2hDbTAwTDExbUQ1OVl3bE9yOGViZTFDaWVFRWI4cGhBSzVqRlp4em8zVk9kRHJXM241a3VucDVxOFNvY0JqTThtTElEYXFZajN5M3VMR2dkaEVMTjFrNjBHLWxFRm1UMmEydW4wbkZTUldoWE5lWTNoOTNsYUhobQ?oc=5>

### Compared to Estimates, Canadian Natural Resources (CNQ) Q3 Earnings: A Look at Key Metrics
- Summary: CNQ reported Q3 earnings, comparing actual results to analyst estimates, highlighting key financial metrics.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxOUHBZZUpSQVBQRW04ZVA4Tk5uRkZ4TzVmc3ZUYzYyMHJuTlY2azhvUUl1Wlh3Z3c0WTk3ckJFVThmV0ZncFJwT3l6TWUtUWVIZTJsT085cDRpaEdDcVZEYnVhMlNMbkJtZDZqRHcyR2M0bEI1UW1WaUNNZTFvc0p5TU4xUDhGZ1dJY0toLXl1aXR3NFRLZE50SHFkUjd1S1Z2ckUwamVFTzhiT0NxS0Fv?oc=5>

### Earnings Flash (CNQ.TO) Canadian Natural Resources Posts Q3 Adjusted EPS CA$1.65
- Summary: CNQ posted a Q3 adjusted EPS of CA$1.65, indicating profitability for the quarter.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiywFBVV95cUxNU2FpYUZUc004REJET0FWZmJqSm9lV2hiRGltZHdtNFpiVEJ0cUpvdF9sRjRrNXRkSUFBcDVwc1RuS2xBQU5EZnRvZ1dGTTNxN1RyUHRfUEpNTnlfOEU2dHd5X3JoS1NOTkFrS0dldzdZS3FkQ1lhbGVMUWlqQWF3RDhzMzV0cml2WHJnd0tvTjgwZkpab1M4aW05LWFzeldYalpjeGhhaGVmWkRLbDB4d3BqZ0QxOWZvd2EzN050R1NQRnNZXy1zN2dFOA?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **CNQ.TO** | **10.00** | **3.03** | **8.30** | **69.50** | **141,171,523,584.00 CAD** | **58.60** |
| SU.TO | 9.86 | 2.26 | 5.08 | 50.40 | 111,380,938,752.00 CAD | 71.48 |
| IMO.TO | 13.81 | 3.40 | 8.23 | 34.90 | 83,083,517,952.00 CAD | 43.01 |
| CVE.TO | 10.80 | 1.99 | 4.42 | 21.10 | 70,051,799,040.00 CAD | 69.85 |

Peers fetched as_of: 2026-11-05; CNQ.TO reuses existing data (market data as_of: 2026-11-05); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-05
- Next expected earnings: N/A (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-05

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
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

- https://news.google.com/rss/articles/CBMimAFBVV95cUxNN1pBd1VDN1VKSzJQaWFwZHlKOEpmUFpod2hDbTAwTDExbUQ1OVl3bE9yOGViZTFDaWVFRWI4cGhBSzVqRlp4em8zVk9kRHJXM241a3VucDVxOFNvY0JqTThtTElEYXFZajN5M3VMR2dkaEVMTjFrNjBHLWxFRm1UMmEydW4wbkZTUldoWE5lWTNoOTNsYUhobQ?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxOUHBZZUpSQVBQRW04ZVA4Tk5uRkZ4TzVmc3ZUYzYyMHJuTlY2azhvUUl1Wlh3Z3c0WTk3ckJFVThmV0ZncFJwT3l6TWUtUWVIZTJsT085cDRpaEdDcVZEYnVhMlNMbkJtZDZqRHcyR2M0bEI1UW1WaUNNZTFvc0p5TU4xUDhGZ1dJY0toLXl1aXR3NFRLZE50SHFkUjd1S1Z2ckUwamVFTzhiT0NxS0Fv?oc=5
- https://news.google.com/rss/articles/CBMiywFBVV95cUxNU2FpYUZUc004REJET0FWZmJqSm9lV2hiRGltZHdtNFpiVEJ0cUpvdF9sRjRrNXRkSUFBcDVwc1RuS2xBQU5EZnRvZ1dGTTNxN1RyUHRfUEpNTnlfOEU2dHd5X3JoS1NOTkFrS0dldzdZS3FkQ1lhbGVMUWlqQWF3RDhzMzV0cml2WHJnd0tvTjgwZkpab1M4aW05LWFzeldYalpjeGhhaGVmWkRLbDB4d3BqZ0QxOWZvd2EzN050R1NQRnNZXy1zN2dFOA?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
