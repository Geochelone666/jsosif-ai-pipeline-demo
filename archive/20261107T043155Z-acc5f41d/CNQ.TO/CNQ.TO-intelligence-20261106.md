# CNQ.TO Intelligence Report

- ticker: **CNQ.TO**
- Report as_of: **2026-11-06**
- Market data as_of: **2026-11-06**
- Quant sources: https://finance.yahoo.com/quote/CNQ.TO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/CNQ.TO/key-statistics/
- AI analysis snapshot as_of: **2026-11-06**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-07T04:41:29.004300+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 14, 'rule': 5, 'ai': 6, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **4** exact headline/source/date matches; prior report **20261106T045829Z-1db1e5a7/CNQ.TO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 14 unique headlines; 7 named publishers; 0 exact duplicates; 14 HTTPS source links; largest publisher share 35.71%; oldest publication 2026-11-03

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 68.5000 |
| Return 1D (%) | 0.0292 |
| Return 1W (%) | -12.6498 |
| Return 1M (%) | 0.0292 |
| Return YTD (%) | 51.6175 |
| Return 1Y (%) | 60.6826 |
| Annualized volatility (%) | 31.7256 |
| Beta vs SPY | -0.5849 |
| Max drawdown (%) | -18.6770 |
| Sharpe (rf=0) | 1.6614 |
| Downside deviation (rf=0, %) | 22.2487 |
| Sortino (rf=0) | 2.3691 |
| Historical VaR 95% (1D, %) | 3.2969 |
| Historical ES 95% (1D, %) | 4.7931 |
| Correlation vs SPY | -0.2505 |
| Tracking error vs SPY (%) | 37.5807 |
| P/E (trailing) | 10.10 |
| P/B | 3.00 |
| EV/EBITDA | 7.19 |
| Revenue growth (%) | 34.40 |
| Forward P/E (estimate) | 10.57 |
| Gross margin (%) | 52.92 |
| Operating margin (%) | 32.27 |
| Return on equity (%) | 32.38 |
| Free cash flow yield (%) | 7.89 |
| MA50 | 71.1909 |
| Close vs MA50 (%) | -3.7798 |
| MA200 | 63.4126 |
| Close vs MA200 (%) | 8.0226 |
| RSI (14, Wilder) | 36.1408 |
| MACD (12,26) | 0.1092 |
| MACD signal (9) | 1.2761 |
| MACD histogram | -1.1669 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'CNQ.TO': 276, 'SPY': 277}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 68.5000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.0292 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -12.6498 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 0.0292 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 51.6175 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 60.6826 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 31.7256 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 22.2487 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 2.3691 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.2969 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.7931 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.2505 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 37.5807 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.5849 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -18.6770 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.6614 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 10.5664 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 52.9160 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 32.2680 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 32.3850 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 7.8931 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 10.1032 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 36.1408 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -1.1669 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -3.7798 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 8.0226 -> Clearly above the moving-average trend level.

## TAILWINDS

### Canadian Natural Resources (CNQ) Beats Q3 Earnings and Revenue Estimates
- Summary: Canadian Natural Resources (CNQ) Beats Q3 Earnings and Revenue Estimates
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxOQUQ4Rk5rRlVrNDhhX0tIQjRDQ1RrM0tUVkluNC1kdjdQWjdsZ0htNGFobERoZ3kwZmQ2Wlk2ZUVKZWFXMG41VlVaZ3cwZ1pIbl9KTXlHOWJOZkpZT25wN0NsaWVxYThHeGw5amNRRWhTemtvdi1rOEFldEdMa1hhNDFfLU9Td0dLYnV6S1dIMnEyaU1OWXZ1X2VmWDZMMGhVX0I0?oc=5>

### Canadian Natural Resources Q3 Adjusted Net Earnings Rise
- Summary: Canadian Natural Resources Q3 Adjusted Net Earnings Rise
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxOWXpoZ1NxMzB4eE93bjFKczFldkZPMGRwbjFYNEluT1g2bHZ2VmFDUnBPT0RURDlNSlZWX1I4Q0VwdzJaZGFuWEJOa1dpNXFjRTRwakNfMTY2VVkwSmtkUnZhbXpYZWVtcXNMREV3MW0xSjR3bWdhcGdDX0FqMzV2aUZ6SUdGZFdoSXRxTG9mRkRWNWh6bjF6UlpxRFp5VVd6d2pkUGtR?oc=5>

## HEADWINDS

### Canadian Natural Resources Ltd. stock falls Thursday, still outperforms market
- Summary: Canadian Natural Resources Ltd. stock falls Thursday, still outperforms market
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0gFBVV95cUxOTWp6VDF3WFhmRUxTTjdfMnRTSDVjZGNfalA0M2hsVklFUU05blFEQk1hMWRxaWtlR0dtdGk5dlBSZDc0Y1F4OFg0eHItN3V5VUtCdzNVUFMtVEktRWpnSzN3WV9sV1F1V2sxaVo5bnhQRkdjaWFQYW9DWXNTdVJ0THNLd1RHSUFhTmRyWmc5QUdIZWdaZGJ4Y1pwOEI4ZDFKRFhzdzlZN1FqQTRMZ2d2UDRRcTNBOXIwWWxRUEwyTzhkRmdocWVIYjFKck96cjZOMWc?oc=5>

## CATALYSTS

### Canadian Natural Resources Q3 Earnings Call Highlights
- Summary: Canadian Natural Resources Q3 Earnings Call Highlights
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxOTms1ZVFtX2FqMGg1UXNVYWRPWmQ2MXBPZ3BDOTNrY3JLdnNPZmNQMUZQS2VZTU13TTRkZE9PcjdxNWxmdmlmSDRWMzVSZTNaQWNEeXVTa2p6NGF0ckFXVDNKcmo0UkdfU1dHMmlNV0R4VFA3NXhoeWtWTHBzaXA5dXhzRTdLZnJhYkZlY3pQTW5ROVRZR0wwcjNMSQ?oc=5>

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

### Canadian Natural Earnings: Debt Target Hit; 100% of Free Cash to Shareholders
- Summary: CNQ reports earnings, hitting debt target and returning all free cash to shareholders.
- Date: 2026-11-05 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxNdTQzUm1TWjFtbzA0R0U0cEx4aFJVMnRleHVadUNXUEpBdG5zcGNSbzNHOUdKbWQzMGdJR0RHQzA1ekc0VEVVUWNvY0hLelhTWF9pUTdndXgyUmRVNTVIZ3hTeEJtbFoxamE3R0FIdENJazlZeEkzdzd1NmFjaG9wZGpoY3ZSd295UWJ0TFV0aUowRXBtcW12WnlGdVJqVWhkT3IxRl9fQl9scGg5ZlhwUGR3?oc=5>

### Canadian Natural: Strong Results, 10%+ Yield (NYSE:CNQ)
- Summary: CNQ announces strong earnings with over 10% dividend yield.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxObE5BUzF4RmJVVWw2MllIQ0VjalBzTjdYYVF4OTh4MzJGcV9TYTFWaXJVbEpBNXNDaFBGQllLS0N6eTB0VGRpeTBiNUVaT21EZzJWQTdqTnpPNk1mdGVuNllPbkh2QUpuRm1BSm5sUTBrU2JsS1l6dkNtbTVMemY0NjVhQWhqV0p4OFh5VEdUcXVkaVN4OG1uTWxn?oc=5>

### Canadian Natural Declares C$0.625 Quarterly Dividend
- Summary: CNQ declares a quarterly dividend of C$0.625 per share.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxNNE03LWZ4WmlDVnFIYVlKdHBMQ1JxeFc3RVEzYm9LMVllaUwxc0NrRkFMdDhhU2YwVXZCQ1Q5b1hWSC1HY0VJQUU5emtXclZXZTUtLVZQa2ZPWFFSTmYwUGo0V01wRVZMRkRGYUJ5YkZibEthckR5bFZoR200bkVEaG1CbHZOMGZLMEFmOWFSVk5EY1E4bVJjU0tNWHNDY2EzQVN4S3JB?oc=5>

### Canadian Natural to Report Q3 Earnings: What's in the Offing?
- Summary: CNQ will report Q3 earnings, providing guidance on future performance.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxOc2ExQk9HcFc0YW84czdFZ0pWX1p1QWw2OFN4WHhzMVN4WW1yZmFOTjlRWVc2b3BmRzBZckJ5UXR3ckVEbWktSHdMb0ZzZk56eS1sWmhpaWQ2d0dCZ1dnRWZ3VUs5Q1lqZ0EtLTlUZDQwMHhrM1ZMajFWbjdDNTBYbVJGZmpHX0FoMHRWUlRvblBXN0k5T0w0?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **CNQ.TO** | **10.10** | **3.00** | **7.19** | **34.40** | **141,212,745,728.00 CAD** | **60.68** |
| SU.TO | 10.32 | 2.26 | 5.09 | 50.40 | 111,783,870,464.00 CAD | 68.90 |
| IMO.TO | 14.05 | 3.41 | 8.26 | 34.90 | 83,390,324,736.00 CAD | 40.23 |
| CVE.TO | 10.79 | 1.99 | 4.42 | 21.10 | 70,015,655,936.00 CAD | 67.19 |

Peers fetched as_of: 2026-11-06; CNQ.TO reuses existing data (market data as_of: 2026-11-06); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-05
- Next expected earnings: 2027-03-04 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-06

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
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

- https://news.google.com/rss/articles/CBMiowFBVV95cUxOQUQ4Rk5rRlVrNDhhX0tIQjRDQ1RrM0tUVkluNC1kdjdQWjdsZ0htNGFobERoZ3kwZmQ2Wlk2ZUVKZWFXMG41VlVaZ3cwZ1pIbl9KTXlHOWJOZkpZT25wN0NsaWVxYThHeGw5amNRRWhTemtvdi1rOEFldEdMa1hhNDFfLU9Td0dLYnV6S1dIMnEyaU1OWXZ1X2VmWDZMMGhVX0I0?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxOWXpoZ1NxMzB4eE93bjFKczFldkZPMGRwbjFYNEluT1g2bHZ2VmFDUnBPT0RURDlNSlZWX1I4Q0VwdzJaZGFuWEJOa1dpNXFjRTRwakNfMTY2VVkwSmtkUnZhbXpYZWVtcXNMREV3MW0xSjR3bWdhcGdDX0FqMzV2aUZ6SUdGZFdoSXRxTG9mRkRWNWh6bjF6UlpxRFp5VVd6d2pkUGtR?oc=5
- https://news.google.com/rss/articles/CBMi0gFBVV95cUxOTWp6VDF3WFhmRUxTTjdfMnRTSDVjZGNfalA0M2hsVklFUU05blFEQk1hMWRxaWtlR0dtdGk5dlBSZDc0Y1F4OFg0eHItN3V5VUtCdzNVUFMtVEktRWpnSzN3WV9sV1F1V2sxaVo5bnhQRkdjaWFQYW9DWXNTdVJ0THNLd1RHSUFhTmRyWmc5QUdIZWdaZGJ4Y1pwOEI4ZDFKRFhzdzlZN1FqQTRMZ2d2UDRRcTNBOXIwWWxRUEwyTzhkRmdocWVIYjFKck96cjZOMWc?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxOTms1ZVFtX2FqMGg1UXNVYWRPWmQ2MXBPZ3BDOTNrY3JLdnNPZmNQMUZQS2VZTU13TTRkZE9PcjdxNWxmdmlmSDRWMzVSZTNaQWNEeXVTa2p6NGF0ckFXVDNKcmo0UkdfU1dHMmlNV0R4VFA3NXhoeWtWTHBzaXA5dXhzRTdLZnJhYkZlY3pQTW5ROVRZR0wwcjNMSQ?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxNN1pBd1VDN1VKSzJQaWFwZHlKOEpmUFpod2hDbTAwTDExbUQ1OVl3bE9yOGViZTFDaWVFRWI4cGhBSzVqRlp4em8zVk9kRHJXM241a3VucDVxOFNvY0JqTThtTElEYXFZajN5M3VMR2dkaEVMTjFrNjBHLWxFRm1UMmEydW4wbkZTUldoWE5lWTNoOTNsYUhobQ?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxOUHBZZUpSQVBQRW04ZVA4Tk5uRkZ4TzVmc3ZUYzYyMHJuTlY2azhvUUl1Wlh3Z3c0WTk3ckJFVThmV0ZncFJwT3l6TWUtUWVIZTJsT085cDRpaEdDcVZEYnVhMlNMbkJtZDZqRHcyR2M0bEI1UW1WaUNNZTFvc0p5TU4xUDhGZ1dJY0toLXl1aXR3NFRLZE50SHFkUjd1S1Z2ckUwamVFTzhiT0NxS0Fv?oc=5
- https://news.google.com/rss/articles/CBMiywFBVV95cUxNU2FpYUZUc004REJET0FWZmJqSm9lV2hiRGltZHdtNFpiVEJ0cUpvdF9sRjRrNXRkSUFBcDVwc1RuS2xBQU5EZnRvZ1dGTTNxN1RyUHRfUEpNTnlfOEU2dHd5X3JoS1NOTkFrS0dldzdZS3FkQ1lhbGVMUWlqQWF3RDhzMzV0cml2WHJnd0tvTjgwZkpab1M4aW05LWFzeldYalpjeGhhaGVmWkRLbDB4d3BqZ0QxOWZvd2EzN050R1NQRnNZXy1zN2dFOA?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxNdTQzUm1TWjFtbzA0R0U0cEx4aFJVMnRleHVadUNXUEpBdG5zcGNSbzNHOUdKbWQzMGdJR0RHQzA1ekc0VEVVUWNvY0hLelhTWF9pUTdndXgyUmRVNTVIZ3hTeEJtbFoxamE3R0FIdENJazlZeEkzdzd1NmFjaG9wZGpoY3ZSd295UWJ0TFV0aUowRXBtcW12WnlGdVJqVWhkT3IxRl9fQl9scGg5ZlhwUGR3?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxObE5BUzF4RmJVVWw2MllIQ0VjalBzTjdYYVF4OTh4MzJGcV9TYTFWaXJVbEpBNXNDaFBGQllLS0N6eTB0VGRpeTBiNUVaT21EZzJWQTdqTnpPNk1mdGVuNllPbkh2QUpuRm1BSm5sUTBrU2JsS1l6dkNtbTVMemY0NjVhQWhqV0p4OFh5VEdUcXVkaVN4OG1uTWxn?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxNNE03LWZ4WmlDVnFIYVlKdHBMQ1JxeFc3RVEzYm9LMVllaUwxc0NrRkFMdDhhU2YwVXZCQ1Q5b1hWSC1HY0VJQUU5emtXclZXZTUtLVZQa2ZPWFFSTmYwUGo0V01wRVZMRkRGYUJ5YkZibEthckR5bFZoR200bkVEaG1CbHZOMGZLMEFmOWFSVk5EY1E4bVJjU0tNWHNDY2EzQVN4S3JB?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxOc2ExQk9HcFc0YW84czdFZ0pWX1p1QWw2OFN4WHhzMVN4WW1yZmFOTjlRWVc2b3BmRzBZckJ5UXR3ckVEbWktSHdMb0ZzZk56eS1sWmhpaWQ2d0dCZ1dnRWZ3VUs5Q1lqZ0EtLTlUZDQwMHhrM1ZMajFWbjdDNTBYbVJGZmpHX0FoMHRWUlRvblBXN0k5T0w0?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
