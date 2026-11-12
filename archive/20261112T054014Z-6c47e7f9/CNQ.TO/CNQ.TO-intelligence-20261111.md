# CNQ.TO Intelligence Report

- ticker: **CNQ.TO**
- Report as_of: **2026-11-11**
- Market data as_of: **2026-11-11**
- Quant sources: https://finance.yahoo.com/quote/CNQ.TO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/CNQ.TO/key-statistics/
- AI analysis snapshot as_of: **2026-11-11**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-12T05:56:48.015468+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 11, 'rule': 4, 'ai': 2, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **1** exact headline/source/date matches; prior report **20261111T043601Z-d14951e6/CNQ.TO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 11 unique headlines; 4 named publishers; 0 exact duplicates; 11 HTTPS source links; largest publisher share 45.45%; oldest publication 2026-11-05

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 69.6900 |
| Return 1D (%) | 1.8860 |
| Return 1W (%) | 0.7081 |
| Return 1M (%) | -1.5678 |
| Return YTD (%) | 54.2515 |
| Return 1Y (%) | 60.0879 |
| Annualized volatility (%) | 31.7684 |
| Beta vs SPY | -0.5805 |
| Max drawdown (%) | -18.6770 |
| Sharpe (rf=0) | 1.6478 |
| Downside deviation (rf=0, %) | 22.2676 |
| Sortino (rf=0) | 2.3509 |
| Historical VaR 95% (1D, %) | 3.2969 |
| Historical ES 95% (1D, %) | 4.7931 |
| Correlation vs SPY | -0.2516 |
| Tracking error vs SPY (%) | 37.7392 |
| P/E (trailing) | 10.48 |
| P/B | 3.04 |
| EV/EBITDA | 7.03 |
| Revenue growth (%) | 34.40 |
| Forward P/E (estimate) | 11.12 |
| Gross margin (%) | 52.92 |
| Operating margin (%) | 30.67 |
| Return on equity (%) | 32.38 |
| Free cash flow yield (%) | 8.59 |
| MA50 | 71.2137 |
| Close vs MA50 (%) | -2.1396 |
| MA200 | 63.7243 |
| Close vs MA200 (%) | 9.3617 |
| RSI (14, Wilder) | 42.1847 |
| MACD (12,26) | -0.6866 |
| MACD signal (9) | 0.3846 |
| MACD histogram | -1.0713 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'CNQ.TO': 279, 'SPY': 280}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 69.6900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.8860 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 0.7081 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -1.5678 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 54.2515 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 60.0879 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 31.7684 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 22.2676 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 2.3509 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.2969 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.7931 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.2516 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 37.7392 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.5805 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -18.6770 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.6478 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 11.1180 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 52.9160 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 30.6740 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 32.3850 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 8.5863 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 10.4797 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 42.1847 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -1.0713 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -2.1396 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 9.3617 -> Clearly above the moving-average trend level.

## TAILWINDS

### Canadian Natural Resources (CNQ) Beats Q3 Earnings and Revenue Estimates
- Summary: Canadian Natural Resources (CNQ) Beats Q3 Earnings and Revenue Estimates
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxOQUQ4Rk5rRlVrNDhhX0tIQjRDQ1RrM0tUVkluNC1kdjdQWjdsZ0htNGFobERoZ3kwZmQ2Wlk2ZUVKZWFXMG41VlVaZ3cwZ1pIbl9KTXlHOWJOZkpZT25wN0NsaWVxYThHeGw5amNRRWhTemtvdi1rOEFldEdMa1hhNDFfLU9Td0dLYnV6S1dIMnEyaU1OWXZ1X2VmWDZMMGhVX0I0?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Canadian Natural Resources (TSX:CNQ) Q3 Results Mask A One Off Profit Boost
- Summary: Canadian Natural Resources (TSX:CNQ) Q3 Results Mask A One Off Profit Boost
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxOOUswNjRsMlRNM2pJbVc5WDFSTm51cmdOenM5NmxpQlAtMGM3WHAxNlNoOTFDZktVNjIyVktIeXlxcnk0X0JIQ2xzSkV5bllSNE8tbE1OZnhqZWJJN1RmT2stOC1VZWU1azFvVjIxMUhHOVdYVVl0dkJodjFxdDlldTBucmF1RlFqX2pSU3BqRXVXRGEtRkp6cTZocGd2aUVB?oc=5>

### Canadian Natural Resources Q3 Earnings Call Highlights
- Summary: Canadian Natural Resources Q3 Earnings Call Highlights
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxOTms1ZVFtX2FqMGg1UXNVYWRPWmQ2MXBPZ3BDOTNrY3JLdnNPZmNQMUZQS2VZTU13TTRkZE9PcjdxNWxmdmlmSDRWMzVSZTNaQWNEeXVTa2p6NGF0ckFXVDNKcmo0UkdfU1dHMmlNV0R4VFA3NXhoeWtWTHBzaXA5dXhzRTdLZnJhYkZlY3pQTW5ROVRZR0wwcjNMSQ?oc=5>

### Canadian Natural Resources stock shifts cash flow to buybacks
- Summary: Canadian Natural Resources stock shifts cash flow to buybacks
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxQSnZmUjM3b0REWjhzTDFNMHdwcllrWmxkSnVvRXJCd1BZOHJWRXNWekdXd251ckVYd01qdGFRZUlDUHR0a1hLYmkyeXUzVjFuT3FNY0d0OHZudmNaLUxfbWpheUJKU1p4blFyRTdIMGdsUXlET1gtcGdhcl9uWUh3OEw4OFBLUFk2VHd6VEFaRlhReWVwTnUwSUg1QnhfdW12a3pyemFKSWF1UkF4elBYRWl3UDRhU3paRjlsLVNnNTlTQQ?oc=5>

### How Earnings And Buybacks Will Impact Canadian Natural Resources Stock Investors
- Summary: Discusses how earnings and buybacks could affect CNQ investors.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxPLXRydHlQUnZjaDdTWVFNaDh0Wl9xbjVHajdURWZYT1hXVEhLSHZyS1ROVUZncFpOdVA2OEFuSHNnbG8tZ215MTlfQ0hnT1p4eGlWeElncEVyakF2LXExSkZtMENBRkZwLW52eUYzbmR3Q2dQeWhtMTZ6ZjlSckQ4YUxiSjJzc0xLSldzX3Zta1M0ekxTa0J2NUMtaWRkUy1uSmdpNW9vakpsUQ?oc=5>

### Compared to Estimates, Canadian Natural Resources (CNQ) Q3 Earnings: A Look at Key Metrics
- Summary: CNQ reports Q3 earnings, comparing actuals to estimates, highlighting key financial metrics.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxOUHBZZUpSQVBQRW04ZVA4Tk5uRkZ4TzVmc3ZUYzYyMHJuTlY2azhvUUl1Wlh3Z3c0WTk3ckJFVThmV0ZncFJwT3l6TWUtUWVIZTJsT085cDRpaEdDcVZEYnVhMlNMbkJtZDZqRHcyR2M0bEI1UW1WaUNNZTFvc0p5TU4xUDhGZ1dJY0toLXl1aXR3NFRLZE50SHFkUjd1S1Z2ckUwamVFTzhiT0NxS0Fv?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **CNQ.TO** | **10.48** | **3.04** | **7.03** | **34.40** | **141,828,210,688.00 CAD** | **60.09** |
| SU.TO | 10.66 | 2.29 | 5.15 | 50.40 | 113,061,724,160.00 CAD | 64.05 |
| IMO.TO | 14.78 | 3.48 | 8.43 | 34.90 | 85,132,050,432.00 CAD | 36.70 |
| CVE.TO | 8.62 | 2.08 | 4.60 | 21.10 | 73,214,623,744.00 CAD | 62.32 |

Peers fetched as_of: 2026-11-11; CNQ.TO reuses existing data (market data as_of: 2026-11-11); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-05
- Next expected earnings: 2027-03-04 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-11

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
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

- https://news.google.com/rss/articles/CBMiowFBVV95cUxOQUQ4Rk5rRlVrNDhhX0tIQjRDQ1RrM0tUVkluNC1kdjdQWjdsZ0htNGFobERoZ3kwZmQ2Wlk2ZUVKZWFXMG41VlVaZ3cwZ1pIbl9KTXlHOWJOZkpZT25wN0NsaWVxYThHeGw5amNRRWhTemtvdi1rOEFldEdMa1hhNDFfLU9Td0dLYnV6S1dIMnEyaU1OWXZ1X2VmWDZMMGhVX0I0?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxOOUswNjRsMlRNM2pJbVc5WDFSTm51cmdOenM5NmxpQlAtMGM3WHAxNlNoOTFDZktVNjIyVktIeXlxcnk0X0JIQ2xzSkV5bllSNE8tbE1OZnhqZWJJN1RmT2stOC1VZWU1azFvVjIxMUhHOVdYVVl0dkJodjFxdDlldTBucmF1RlFqX2pSU3BqRXVXRGEtRkp6cTZocGd2aUVB?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxOTms1ZVFtX2FqMGg1UXNVYWRPWmQ2MXBPZ3BDOTNrY3JLdnNPZmNQMUZQS2VZTU13TTRkZE9PcjdxNWxmdmlmSDRWMzVSZTNaQWNEeXVTa2p6NGF0ckFXVDNKcmo0UkdfU1dHMmlNV0R4VFA3NXhoeWtWTHBzaXA5dXhzRTdLZnJhYkZlY3pQTW5ROVRZR0wwcjNMSQ?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxQSnZmUjM3b0REWjhzTDFNMHdwcllrWmxkSnVvRXJCd1BZOHJWRXNWekdXd251ckVYd01qdGFRZUlDUHR0a1hLYmkyeXUzVjFuT3FNY0d0OHZudmNaLUxfbWpheUJKU1p4blFyRTdIMGdsUXlET1gtcGdhcl9uWUh3OEw4OFBLUFk2VHd6VEFaRlhReWVwTnUwSUg1QnhfdW12a3pyemFKSWF1UkF4elBYRWl3UDRhU3paRjlsLVNnNTlTQQ?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxPLXRydHlQUnZjaDdTWVFNaDh0Wl9xbjVHajdURWZYT1hXVEhLSHZyS1ROVUZncFpOdVA2OEFuSHNnbG8tZ215MTlfQ0hnT1p4eGlWeElncEVyakF2LXExSkZtMENBRkZwLW52eUYzbmR3Q2dQeWhtMTZ6ZjlSckQ4YUxiSjJzc0xLSldzX3Zta1M0ekxTa0J2NUMtaWRkUy1uSmdpNW9vakpsUQ?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxOUHBZZUpSQVBQRW04ZVA4Tk5uRkZ4TzVmc3ZUYzYyMHJuTlY2azhvUUl1Wlh3Z3c0WTk3ckJFVThmV0ZncFJwT3l6TWUtUWVIZTJsT085cDRpaEdDcVZEYnVhMlNMbkJtZDZqRHcyR2M0bEI1UW1WaUNNZTFvc0p5TU4xUDhGZ1dJY0toLXl1aXR3NFRLZE50SHFkUjd1S1Z2ckUwamVFTzhiT0NxS0Fv?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
