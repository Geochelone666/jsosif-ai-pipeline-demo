# GIS Intelligence Report

- ticker: **GIS**
- Report as_of: **2026-11-17**
- Market data as_of: **2026-11-17**
- Quant sources: https://finance.yahoo.com/quote/GIS/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/GIS/key-statistics/
- AI analysis snapshot as_of: **2026-11-17**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-18T05:51:09.910112+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 21, 'rule': 5, 'ai': 7, 'unknown': 0, 'irrelevant': 9})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **11** exact headline/source/date matches; prior report **20261116T043911Z-b81cfeb4/GIS** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 21 unique headlines; 11 named publishers; 0 exact duplicates; 21 HTTPS source links; largest publisher share 28.57%; oldest publication 2026-11-10

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 34.6800 |
| Return 1D (%) | -1.5891 |
| Return 1W (%) | 0.2312 |
| Return 1M (%) | 4.6785 |
| Return YTD (%) | -20.2739 |
| Return 1Y (%) | -21.0716 |
| Annualized volatility (%) | 31.0609 |
| Beta vs SPY | -0.3891 |
| Max drawdown (%) | -33.2524 |
| Sharpe (rf=0) | -0.6105 |
| Downside deviation (rf=0, %) | 21.6813 |
| Sortino (rf=0) | -0.8746 |
| Historical VaR 95% (1D, %) | 2.9959 |
| Historical ES 95% (1D, %) | 3.8866 |
| Correlation vs SPY | -0.1726 |
| Tracking error vs SPY (%) | 36.0900 |
| P/E (trailing) | N/A |
| P/B | 2.49 |
| EV/EBITDA | 9.29 |
| Revenue growth (%) | -2.80 |
| Forward P/E (estimate) | 11.02 |
| Gross margin (%) | 33.73 |
| Operating margin (%) | 15.62 |
| Return on equity (%) | -10.49 |
| Free cash flow yield (%) | 7.02 |
| MA50 | 33.8404 |
| Close vs MA50 (%) | 2.4810 |
| MA200 | 35.8052 |
| Close vs MA200 (%) | -3.1424 |
| RSI (14, Wilder) | 52.3029 |
| MACD (12,26) | 0.2682 |
| MACD signal (9) | 0.2513 |
| MACD histogram | 0.0169 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'GIS': 284, 'SPY': 284}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 34.6800 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.5891 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 0.2312 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 4.6785 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -20.2739 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -21.0716 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 31.0609 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 21.6813 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.8746 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.9959 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.8866 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.1726 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 36.0900 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.3891 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -33.2524 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.6105 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 11.0200 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 33.7280 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 15.6240 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: -10.4950 -> Adjusted price fell over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 7.0248 -> No interpretation rule is available for this metric.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 52.3029 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.0169 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 2.4810 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -3.1424 -> Slightly below the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

### General Mills downgraded by Piper Sandler with a new price target
- Summary: General Mills downgraded by Piper Sandler with a new price target
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxNbDF6TU1Ka2t5WlRSUVZhd0JIX2h5QURYdWs4Wkd1WUVDUEQyQnJuaTNyekpGLUlPc3BqSGE5bDdBbDU0aHQtQm5KdXNaRER6bmFmZVVMYk1iUHZtblBzbGwyYzhURkNIX2NhZnJuRUU5MzRMSTJONnpYb0preWU1RzFJWUM1bmFuREJISjRic3RXd2FzZlk2THh5WWpyWXc5c2t3?oc=5>

### General Mills (NYSE:GIS) Downgraded by Piper Sandler to "Neutral"
- Summary: General Mills (NYSE:GIS) Downgraded by Piper Sandler to "Neutral"
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxQX0g3UWJVcFRpZGEwZzY1RU9XUDJtV3pUUmtad1pIaXEwMTVOVzZ6WnhBLVZVVWdoeENDMDA3Ujc3cE1oSUJGZ0tXQkUtNVMyV1NLOHRuVm9kb0F4ODh2dkhFb2Rvc2tUOENWTE55RTFVRVpyVDJ3eTExT1lqaUl5VjV2bmFYYnl3SFc1YXdsVFZMR0pQXzhabzVHcFdCX1EtTTVobGlZU2NqVnl4Zk9SUUdNbkZVbkNaZG8xeVJiYk8?oc=5>

## CATALYSTS

### General Mills Quarterly Dividend Declared
- Summary: General Mills Quarterly Dividend Declared
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxPem4xWWlNbzFQVURSU3d3VFB2MWtlNkVlaVFRM0tDel9JSlpQcTdxamJGa1JUSVJXTDhmU2lhRUNzRWFTUk5OeFA5eHFycWQ0bFZYMXMzX1l4alYtZHJ4bXU5X252N1gwUUJEeWtZdmgyMlE1aEFwUkFmTmNXZXlRS0V2cjZDZ1Z0OUlJVUd5ZlNvc2tXQWg2VmdHdzU3M3V4S1FxeWZoREJGUQ?oc=5>

### General Mills is on watch after Piper Sandler warns of a potential dividend cut (GIS:NYSE)
- Summary: General Mills is on watch after Piper Sandler warns of a potential dividend cut (GIS:NYSE)
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxOY1FUYmJWalRhdWtFN0RnNDlKbGJnYW5NQVpDY1A3QWJLcnZCSGtpd0tZZlg2TzNfX2pPU0ZsSVQ3UWtRaHRlT2w2SVNtTEFDdnNRMlhxN1Bnb1liZkZ1b0huVlBoMVhwX1BlUXJWWnRuYVhYdG0zX0JIeDNURUNkUXJiQzl3UzVlNXZvZWw4NkZocExlMjBESHNYb3dxZThzNFpzaF85NTR4RHF3SEpoR1AwclhCeVR0?oc=5>

### General Mills or Coca-Cola: I Can Only Pick One Dividend Stock for the Next 10 Years. Here’s Mine
- Summary: General Mills or Coca-Cola: I Can Only Pick One Dividend Stock for the Next 10 Years. Here’s Mine
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxPSXF1akZ4cWFDa1ZHM1RiUmJCeWdWaXpwWkNsYXlBckJaYXQxTE4zVUZXTU04MHVvelk2a3RQX3Rhc0d5WHhxS0JpaFZLWFhoS1Z5U3NuOUU0LWp5eVBxV3hIYkttcy1NZ0ZseGJqRHJSN3M0a1dXd2Y1RUVqalhhRm5XSW9KQ19aOXdEakZmdk95dEVKbFhSUjY5Nm5ubmpvQVJLM0N0WEIwc3J6eUFyeDN6VVprajVkYUoyZnVR?oc=5>

### How Investors May Respond To General Mills (GIS) Dividend Cut Risk
- Summary: Dividend cut risk may prompt investor reaction.
- Date: 2026-11-14 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxPQXBCVXhBREV4d0JOQ1BIaTNRRnRvaUlpMVBmMUtQWUN0U1VjXzB3VnF0eE1FVU1MT3pnVWYxc3hYUld6cldFNFI0NG9kSEltRDNjbUFLWkZraDFWWTc5bkpPOUx4aDN4b1Q3WVVpMHpkQzZaR2lrQ0pBZk9pY1poZDJKaWJaSDVHdktSSTdkUzVTWGhfQm5XVXpBVDBXeGdBVnc?oc=5>

### Are Wall Street Analysts Predicting General Mills Stock Will Climb or Sink?
- Summary: Analysts discuss potential price movement for GIS.
- Date: 2026-11-15 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxPNDVQRHh1MUZQeEo4OE5KWUZHUGIyUlBSVFM3dlJrbWhoMk8xOTdlY1JBSFlkX1gzN2VuMWVmMjZwMHVvTl9hM0JVZWVBVUhkQWJHbWYtUUJqQ0N3ZTFfWllRVEJ4Y1pKd1MzMUhOc0lSenN3Vk1jdzM0MFFmM042R1NWdTZwWE5ETXNXRXU4NmgyNjBNMnYxMmJiQW1MMTctTEVHT3BxTQ?oc=5>

### Does Three Segment Reorganization Change The Bull Case For General Mills (GIS)?
- Summary: General Mills' three‑segment reorganization may alter investor perception, potentially impacting valuation and strategic focus.
- Date: 2026-11-15 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2gFBVV95cUxPdUJZQ3RkQzhxZVJUbW9xWHNUN25rTmJSeHRWWElTdktVVV9oVG9xVEtPZFdqU0xOT0JRejQxMnFxUHBzcmlMcEZUMTZYdW9maS1nYjF1QlA0TjRrUWVpTndQUEQ4Z3BicFlxcnlaSC0xNDFpcE9xVFl5ZmgtajgxbS1xbG5NNTI5a1NKV3FzWXhIR3BrM2lmNmNwYWc4WENhSmxJTHVJNmtUV0x3SDdUblJ6QXY1al9RNV9ZRzktRlZmdVBGSEptbjA4NlRTbmppZE5kTUtKRVd6QdIB3wFBVV95cUxOQnNvNkhSVVJxbWlzRVdiYkI5WnNZRVhNeDRRam9UVEs5RE1aNmxlVDc2UXB1RWEwZG9oZzlOdGRiYVJBQXVuQXJYVWR1YjRPZTVydW50Qk14UG11dDRLUHB6YUI5RWpmNXJNS1MwaUtHODZkMGhMVUpnSkkwVnVCckN4amZZekhTZ1pWeC1LcEc3UlBtLXhuTnNEVEQ2Y3BuR0thdlkySElOWWNPbnA0dGM2Qk1IcXNseXVodWxiV0dydEdwRlFjYnhTQjhJblJuWjlwUnRZeFdUZXJnUkRR?oc=5>

### Better High-Yield Dividend Stock: General Mills vs. Comcast
- Summary: General Mills offers higher dividend yield than Comcast.
- Date: 2026-11-10 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxOVkxJMlVxMllYdXE2VGYxRnNXbWxiVVpaSGlERUdRaEN1SXNONGxYMkZITUpGRTRhZjlqZEpmb2twUG42akhsSXhvWklfUTJ1MUxmLThCMzRrYnpiMkFDRkZjcXcyd2Q5anlreXVWSXYtejdFRm13VnBYUkE3dS1lSFFKU0FTalZvd1Vj?oc=5>

### General Mills will put marketing, sales and consumer insights in one new function
- Summary: General Mills consolidates marketing, sales, and consumer insights into a single function to streamline operations.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxOWjcxNlBweGxRLWNRNjlWU2dEVmJ2QnpmdFBwckY4bnFHQWFSdndmd1B4c2s2ckpLM3VtNWdoS3JKdEF6VVR4XzV3UTF4bWl3NHF0Mjhhb3M1R2NWVkJkTVVIdGpuRW55cjZJMVA3b0tqZWNoUk5rdDJJM3gzTm1xLUdhZm92cG5iY3l2dnNYTXVKVGZTdmxQZ29JSXB6bXVTTkRYa3FqWjktOWhEQnNhRmg3NTI5UQ?oc=5>

## RISKS

### Why Is General Mills (NYSE:GIS) Gaining Attention After Results?
- Summary: Post‑results attention could signal earnings impact.
- Date: 2026-11-14 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxNb1JtQ3BwSUhmcGI3emNORnRLUkFuMFBIMzhFZzFHSWhPeDQ3ZjdSdjdHSF9leEFtb1Byd3ZLZG4tYU1nX2REVjZ0Mm10Mlp2X2ltTHFjS1FNbk9vVzNtdlIySG8tc2RHVEJXWEMtbC1HODJHV05tNXdKZUNIRVRneHVsdUZiZjB6UHhZZTFhdHRuZXllcE5fVXhHSzRLS0Y5OU1lMk5UWQ?oc=5>

### Piper Sandler Flags a Risk at General Mills (GIS)
- Summary: Piper Sandler identifies a risk factor for General Mills, potentially affecting investor perception and valuation.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxPSW9tc0xtUVJGSmZZaUZ5WE9WVGllWXhWQS1JZXNCaGl3bUJzRHFER0p6Nk9NQWFHZ0xHYkFiVndRZVZsT0dRWVdPYy1JRlJiMDl6VUE1Tll4YnQxbkRQM0NiODZzdjlQWnFvZWJIQjRDZ0J6WGl2dUl1c2pTdGZNVWNPT2w5NEo2a2c4VS1ZNFA3WktqQ2FSdk9WblQ1Zw?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **GIS** | **N/A** | **2.49** | **9.29** | **-2.80** | **18,542,950,400.00 USD** | **-21.07** |
| KHC | N/A | 0.83 | 8.51 | -2.00 | 29,725,945,856.00 USD | 9.55 |
| CPB | 17.86 | 1.83 | 8.88 | -7.90 | 7,049,393,152.00 USD | -18.36 |
| SJM | 62.36 | 2.48 | 9.34 | 5.00 | 14,254,485,504.00 USD | 30.21 |

Peers fetched as_of: 2026-11-17; GIS reuses existing data (market data as_of: 2026-11-17); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-09-23
- Next expected earnings: 2026-12-23 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-17

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

- https://news.google.com/rss/articles/CBMiowFBVV95cUxNbDF6TU1Ka2t5WlRSUVZhd0JIX2h5QURYdWs4Wkd1WUVDUEQyQnJuaTNyekpGLUlPc3BqSGE5bDdBbDU0aHQtQm5KdXNaRER6bmFmZVVMYk1iUHZtblBzbGwyYzhURkNIX2NhZnJuRUU5MzRMSTJONnpYb0preWU1RzFJWUM1bmFuREJISjRic3RXd2FzZlk2THh5WWpyWXc5c2t3?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxQX0g3UWJVcFRpZGEwZzY1RU9XUDJtV3pUUmtad1pIaXEwMTVOVzZ6WnhBLVZVVWdoeENDMDA3Ujc3cE1oSUJGZ0tXQkUtNVMyV1NLOHRuVm9kb0F4ODh2dkhFb2Rvc2tUOENWTE55RTFVRVpyVDJ3eTExT1lqaUl5VjV2bmFYYnl3SFc1YXdsVFZMR0pQXzhabzVHcFdCX1EtTTVobGlZU2NqVnl4Zk9SUUdNbkZVbkNaZG8xeVJiYk8?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxPem4xWWlNbzFQVURSU3d3VFB2MWtlNkVlaVFRM0tDel9JSlpQcTdxamJGa1JUSVJXTDhmU2lhRUNzRWFTUk5OeFA5eHFycWQ0bFZYMXMzX1l4alYtZHJ4bXU5X252N1gwUUJEeWtZdmgyMlE1aEFwUkFmTmNXZXlRS0V2cjZDZ1Z0OUlJVUd5ZlNvc2tXQWg2VmdHdzU3M3V4S1FxeWZoREJGUQ?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxOY1FUYmJWalRhdWtFN0RnNDlKbGJnYW5NQVpDY1A3QWJLcnZCSGtpd0tZZlg2TzNfX2pPU0ZsSVQ3UWtRaHRlT2w2SVNtTEFDdnNRMlhxN1Bnb1liZkZ1b0huVlBoMVhwX1BlUXJWWnRuYVhYdG0zX0JIeDNURUNkUXJiQzl3UzVlNXZvZWw4NkZocExlMjBESHNYb3dxZThzNFpzaF85NTR4RHF3SEpoR1AwclhCeVR0?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxPSXF1akZ4cWFDa1ZHM1RiUmJCeWdWaXpwWkNsYXlBckJaYXQxTE4zVUZXTU04MHVvelk2a3RQX3Rhc0d5WHhxS0JpaFZLWFhoS1Z5U3NuOUU0LWp5eVBxV3hIYkttcy1NZ0ZseGJqRHJSN3M0a1dXd2Y1RUVqalhhRm5XSW9KQ19aOXdEakZmdk95dEVKbFhSUjY5Nm5ubmpvQVJLM0N0WEIwc3J6eUFyeDN6VVprajVkYUoyZnVR?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxPQXBCVXhBREV4d0JOQ1BIaTNRRnRvaUlpMVBmMUtQWUN0U1VjXzB3VnF0eE1FVU1MT3pnVWYxc3hYUld6cldFNFI0NG9kSEltRDNjbUFLWkZraDFWWTc5bkpPOUx4aDN4b1Q3WVVpMHpkQzZaR2lrQ0pBZk9pY1poZDJKaWJaSDVHdktSSTdkUzVTWGhfQm5XVXpBVDBXeGdBVnc?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxPNDVQRHh1MUZQeEo4OE5KWUZHUGIyUlBSVFM3dlJrbWhoMk8xOTdlY1JBSFlkX1gzN2VuMWVmMjZwMHVvTl9hM0JVZWVBVUhkQWJHbWYtUUJqQ0N3ZTFfWllRVEJ4Y1pKd1MzMUhOc0lSenN3Vk1jdzM0MFFmM042R1NWdTZwWE5ETXNXRXU4NmgyNjBNMnYxMmJiQW1MMTctTEVHT3BxTQ?oc=5
- https://news.google.com/rss/articles/CBMi2gFBVV95cUxPdUJZQ3RkQzhxZVJUbW9xWHNUN25rTmJSeHRWWElTdktVVV9oVG9xVEtPZFdqU0xOT0JRejQxMnFxUHBzcmlMcEZUMTZYdW9maS1nYjF1QlA0TjRrUWVpTndQUEQ4Z3BicFlxcnlaSC0xNDFpcE9xVFl5ZmgtajgxbS1xbG5NNTI5a1NKV3FzWXhIR3BrM2lmNmNwYWc4WENhSmxJTHVJNmtUV0x3SDdUblJ6QXY1al9RNV9ZRzktRlZmdVBGSEptbjA4NlRTbmppZE5kTUtKRVd6QdIB3wFBVV95cUxOQnNvNkhSVVJxbWlzRVdiYkI5WnNZRVhNeDRRam9UVEs5RE1aNmxlVDc2UXB1RWEwZG9oZzlOdGRiYVJBQXVuQXJYVWR1YjRPZTVydW50Qk14UG11dDRLUHB6YUI5RWpmNXJNS1MwaUtHODZkMGhMVUpnSkkwVnVCckN4amZZekhTZ1pWeC1LcEc3UlBtLXhuTnNEVEQ2Y3BuR0thdlkySElOWWNPbnA0dGM2Qk1IcXNseXVodWxiV0dydEdwRlFjYnhTQjhJblJuWjlwUnRZeFdUZXJnUkRR?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxOVkxJMlVxMllYdXE2VGYxRnNXbWxiVVpaSGlERUdRaEN1SXNONGxYMkZITUpGRTRhZjlqZEpmb2twUG42akhsSXhvWklfUTJ1MUxmLThCMzRrYnpiMkFDRkZjcXcyd2Q5anlreXVWSXYtejdFRm13VnBYUkE3dS1lSFFKU0FTalZvd1Vj?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxOWjcxNlBweGxRLWNRNjlWU2dEVmJ2QnpmdFBwckY4bnFHQWFSdndmd1B4c2s2ckpLM3VtNWdoS3JKdEF6VVR4XzV3UTF4bWl3NHF0Mjhhb3M1R2NWVkJkTVVIdGpuRW55cjZJMVA3b0tqZWNoUk5rdDJJM3gzTm1xLUdhZm92cG5iY3l2dnNYTXVKVGZTdmxQZ29JSXB6bXVTTkRYa3FqWjktOWhEQnNhRmg3NTI5UQ?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxNb1JtQ3BwSUhmcGI3emNORnRLUkFuMFBIMzhFZzFHSWhPeDQ3ZjdSdjdHSF9leEFtb1Byd3ZLZG4tYU1nX2REVjZ0Mm10Mlp2X2ltTHFjS1FNbk9vVzNtdlIySG8tc2RHVEJXWEMtbC1HODJHV05tNXdKZUNIRVRneHVsdUZiZjB6UHhZZTFhdHRuZXllcE5fVXhHSzRLS0Y5OU1lMk5UWQ?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxPSW9tc0xtUVJGSmZZaUZ5WE9WVGllWXhWQS1JZXNCaGl3bUJzRHFER0p6Nk9NQWFHZ0xHYkFiVndRZVZsT0dRWVdPYy1JRlJiMDl6VUE1Tll4YnQxbkRQM0NiODZzdjlQWnFvZWJIQjRDZ0J6WGl2dUl1c2pTdGZNVWNPT2w5NEo2a2c4VS1ZNFA3WktqQ2FSdk9WblQ1Zw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
