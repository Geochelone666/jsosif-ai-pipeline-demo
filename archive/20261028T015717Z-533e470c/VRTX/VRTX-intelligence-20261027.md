# VRTX Intelligence Report

- ticker: **VRTX**
- Report as_of: **2026-10-27**
- Market data as_of: **2026-10-27**
- Quant sources: https://finance.yahoo.com/quote/VRTX/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/VRTX/key-statistics/
- AI analysis snapshot as_of: **2026-10-27**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-28T02:13:40.161195+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 20, 'rule': 1, 'ai': 9, 'unknown': 0, 'irrelevant': 10})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **11** exact headline/source/date matches; prior report **20261027T014607Z-b66f6bd5/VRTX** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'directional_claim_without_event_type': 2}
- RSS source audit (metadata only, not article fact-checking): 20 unique headlines; 9 named publishers; 0 exact duplicates; 20 HTTPS source links; largest publisher share 30.0%; oldest publication 2026-10-20

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 521.0300 |
| Return 1D (%) | 0.6841 |
| Return 1W (%) | 1.2397 |
| Return 1M (%) | -0.9806 |
| Return YTD (%) | 14.9263 |
| Return 1Y (%) | 24.0046 |
| Annualized volatility (%) | 29.1144 |
| Beta vs SPY | 0.4940 |
| Max drawdown (%) | -15.2113 |
| Sharpe (rf=0) | 0.8858 |
| Downside deviation (rf=0, %) | 17.8860 |
| Sortino (rf=0) | 1.4419 |
| Historical VaR 95% (1D, %) | 2.6839 |
| Historical ES 95% (1D, %) | 3.4058 |
| Correlation vs SPY | 0.2155 |
| Tracking error vs SPY (%) | 29.1478 |
| P/E (trailing) | 29.74 |
| P/B | 6.52 |
| EV/EBITDA | 24.74 |
| Revenue growth (%) | 12.50 |
| Forward P/E (estimate) | 25.52 |
| Gross margin (%) | 54.96 |
| Operating margin (%) | 38.05 |
| Return on equity (%) | 23.54 |
| Free cash flow yield (%) | 1.99 |
| MA50 | 523.0532 |
| Close vs MA50 (%) | -0.3868 |
| MA200 | 477.8951 |
| Close vs MA200 (%) | 9.0260 |
| RSI (14, Wilder) | 53.4005 |
| MACD (12,26) | 1.3345 |
| MACD signal (9) | -1.2992 |
| MACD histogram | 2.6337 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'VRTX': 269, 'SPY': 269}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 521.0300 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.6841 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 1.2397 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -0.9806 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 14.9263 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 24.0046 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 29.1144 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 17.8860 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.4419 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.6839 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.4058 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2155 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 29.1478 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.4940 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -15.2113 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.8858 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 25.5178 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 54.9570 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 38.0550 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 23.5430 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.9899 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 29.7392 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 53.4005 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 2.6337 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -0.3868 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 9.0260 -> Clearly above the moving-average trend level.

## TAILWINDS

### Vertex Pharmaceuticals (VRTX) Outpaces Stock Market Gains: What You Should Know
- Summary: Vertex Pharmaceuticals (VRTX) Outpaces Stock Market Gains: What You Should Know
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxOUFgyYVJvNnAxN1I1bmZmcnZIQXIzVC1uNlZGUzZqR3ozSEEtYnV3T1p4ZG1TRGRhRUhRY1NJZllOUzBqTjVRUmdNelBKMV9BZ1dtcUk2bng3NlJFdjlEV0ZIUEg2TVFuZUNJZHFCQXRmNFVza2FidlZOLXZhbEFlM3QyY2pMNTJKLVJ5Z3A0T2VzLUs3Y19zVWtHWURmMnVXSzd5cWVDUEt1Njg?oc=5>

### Vertex Pharmaceuticals Gets 96% of Product Sales From Treatments for 1 Disease. Here's Why That's About to Change.
- Summary: Diversification of product sales expected to reduce reliance on a single disease, boosting revenue stability.
- Date: 2026-10-24 | Impact: high | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxNVlJHemhWaVI4enI0cXRkMTZncnRaMEN3Und6NndBTHFoQ1FaOUZseFZBTmNJaDZUVzd1MHdkd1dPYmd3WDR6M2M3X1BrZ0ZSb053blZYNUpQMWtKTnBack9wdFRNX3g1TnNvTHN3UTVWUGtIQmp1RHFVRDEtX014Tkx0ZDZ6bTMxT3NrTHJXVV9wdkdpSkNBSw?oc=5>

### Vertex Pharmaceuticals (VRTX) Posts Positive Phase 3 Results For Povetacicept
- Summary: Positive Phase 3 results for Povetacicept indicate strong clinical progress.
- Date: 2026-10-25 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxNZHJ3T19LVjBFdDc3RUxicks1UUFqdjlYNEZDZ19CNmRZeWdJc0tjbkZiNjY5NlZCSlhUaUtWSzNKbEhValJ1aWtiS2h6SzlyN3hVNzgzMlNzNTVPRzNXZTFlV1BPUHB3U1dUZy1IMWM4c3dDQ2k2bk5mZkd6VDUtazd5aUZVMGpjUTMtVW9reDk4aTBIcWFvUWNxLUFmN2lBR0FDOG1R?oc=5>

### Vertex Pharmaceuticals Incorpor (VRTX) Stock Forecasts
- Summary: Forecasts predict future stock performance for Vertex.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxQc0VzMGtueUtMc3NJN09ZTVpOUTJSaHY1WmdrV3VCTzQ1V0lnVVhFX2ZId2VSV1ZtcTN2aG4zN1pRVVVuSGx6STFzRExxY1lQaGxSN0F0Sm42QTNvMERLRFhZN2ZjdmJrdWlETFpZYThPbVpvYldjYTFZMDdwNDFpS0VsX0lqblM4RUFsYg?oc=5>

### Vertex Pharmaceuticals’ New Drugs Are Gaining Ground. Is That Enough for Investors?
- Summary: Discusses market acceptance of Vertex’s new drugs and investor implications.
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxOQmV1bzlLNFA2T2R0aTY0WEdKYTdWVmZycTFZcXkycjFQS3JVTDBfaEFLTzhlV0ZyZUpQdnV0cW1ubG5TdGx3WXJMZ2FZX0N5VmFhSmVwUTdNbEo2dExlNTliNXBnOFB1MkphcDBTTC1KNVpUd0RBejFtSXM1ME5SQkV6cDV0QVg0b1VfSTh3N2N1WHRYSWEyQlNkb240QThqOTBnVW5fWQ?oc=5>

### Is Vertex Pharmaceuticals (VRTX) A Bargain After Its Phase 3 Kidney Trial Win?
- Summary: Phase 3 kidney trial success suggests undervaluation and potential upside.
- Date: 2026-10-25 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi7AFBVV95cUxQZG5hRkFwbDdac3BTellXczFoU3QxVG5vbGlua09JYzlDTVZlV1l1aENQNjV3blp6WWRQazdwSV9GLWVJRUJnVnNEdTNqTl9zLU1wc3NIS3RfeXJ0OUgyNHhILWFBdTVVVzFMOU1qeGJicDRTa1pNMmtrVTZxcnJreDhKa0RiS0Q0WDRwbDBXN2thT1o3NlpzZW5xQVh0bnJaRWVmb3dCam9PdjRlanpyUnNVV3FkU2MxZU0zd3hyRlRHQ0Rlckk2UzFpNm5MWjlaUUVOTHlpMkhnb1hYN2otYU5KVnBWaGxNVjlqa9IB8gFBVV95cUxNSlRkeFoxU2Q0T0hhTGZLVEVrdlIzWW9fZW9JcnJ3SnlTREE5ejIyVW9mb0tmWVZ0NG1xZUxiaTZMUlVrck90RUlXbHByWE9uWlVZVTFiV1JoWjZXc0JvWVFkQXp4bWRTdjFyQWtRSHF0NWNaa2c4dWlOVkhGSm9POGxFTDdhTDZZenc3c3pDeURBaU5YZjBPOVpHOGhpN3BPWDVJUFZ0M1FTaWxXYlAydW9aLVV0UFk4T3BTZ1h2bllEY2ZLNHlqMzhlb0ZZRmtXamN5Qmg0ZnRxWUliSVY5NGVCS1lMWFIxX0FRQ3dlUXVSZw?oc=5>

## HEADWINDS

### Vertex Pharmaceuticals (VRTX) Stock Sinks As Market Gains: Here's Why
- Summary: Stock price decline amid broader market gains indicates negative sentiment for the company.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxPOEVKaXlSbjNjRTEwSDRGODcyR0VTV1B3bmZPbU45ejBOZ0E0RERDRmdwVVBySUZkN0NmOWxjQS10QWNyOVhWWTZJaE5VSWppZVhDMnhGSUs3bFZtUHhSLUlHbVRuOEo1bmdCTkk2cENuV1doMGZmTXJ4cXozMXo4S25MeHB5V3JqVlBnVXlRM19kbTlMdno5SVlTQUgwSXRPZjI5Q0szQQ?oc=5>

## CATALYSTS

### Vertex Pharmaceuticals (VRTX) Earnings Expected to Grow: Should You Buy?
- Summary: Positive earnings outlook signals potential upside for investors.
- Date: 2026-10-26 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxNX0gxQ2xmS0ktZHc5cWNrVW45OGJ4c2taeUFOZkpncmk3NHpVUGJZMXhPLWhXcm1Fc2hXYTh2RVdSdS1LbUwzcXQzVWlPVF9UN1BvWFNRb0xZNXlRVDN1OW8yYllta1kwRjBoSGpIVFhIendxeDMwRTdjcW5nRWxFZjFxWG1LWGpUYXZzOU1jaHdzS3puSXdCY2VR?oc=5>

### Kidney Trial Win Could Be A Game Changer For Vertex Pharmaceuticals (VRTX)
- Summary: Successful kidney trial could expand product portfolio and revenue.
- Date: 2026-10-26 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi7AFBVV95cUxNRjY1MTFrN0lZLXdzNVBJRW4tY2VtQUowMDllMWlIOV9pS1QxUWF6R3h1dVRxUktwa0xkVk1UaGFvbnktX1RXUGtwel9hWDFaRzJpNGxJd1E1Q2JMZmFvdmhsd1pncjJ2UG1FVUVjX0w0Vy15YV9NaW1Id3ZldGg5NmctNmppdTAwSUZ1bFB2NUx5QTgtT05xclBTbDdCMDR5WHp3LXZhNnJiRWg5aV9uNlBGUU5raFF0aTdoTUFpRDZKeksyNlRoa1doOXVlQmVielNjZmxyRGQwVXBoUlFaSUFLREY3cEJ6bE1aZdIB8gFBVV95cUxOdnlmaTJPM2VXamFoN2JQSjAwV05YNEhrQmROXzUwdWdMWURqaUY4RjhXZ1dldmJiR3EwaDNXWGgtMWh0aUhkWlplVXFKY0VxTXgxSHdsZUNFcG5Fb0JCWE9Pd0M1RnJfd2lVMGd0d3A3Ql9keVNKWkNUa3VodnVZVjZpWmFkd0xvNWx5LTFzbk4tTkdDM0tsSHFMNWt3UWlqQVBtazBuOUxoVXNZeEprZ2cyLXRLNGo5a3RBeFlVbGRQTTJrZFFuS2lld2t2TkJ5TW9BRkJzWVpRNHlrbWFlOURKaWEzd0QycEplSmxiVS05Zw?oc=5>

### Vertex Pharmaceuticals Incorporated Estimates – NASDAQ:VRTX
- Summary: Company releases earnings estimates for upcoming period.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMieEFVX3lxTE5GOHRJNC1Yems2S1BMVXZEWWhWU0hpMHVPTm1YenpFbmZyVERKNmZZbHB2dHNCUDBDZFZRZ0lWV0gzQ2VzZjdiM05uNFdwUURxTG15N1YxRl9yNU9xUUFSMmdSN1I1aksxNkcxWXZiNmUyN2VqMkZ0dw?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **VRTX** | **29.74** | **6.52** | **24.74** | **12.50** | **132,060,758,016.00 USD** | **24.00** |
| REGN | 20.18 | 2.58 | 16.20 | 16.70 | 84,021,567,488.00 USD | 40.15 |
| BIIB | 44.57 | 1.98 | 13.22 | 3.40 | 37,341,868,032.00 USD | 68.01 |
| AMGN | 27.82 | 20.72 | 16.53 | 9.50 | 242,176,114,688.00 USD | 58.12 |

Peers fetched as_of: 2026-10-27; VRTX reuses existing data (market data as_of: 2026-10-27); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-03
- Next expected earnings: 2026-11-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-27

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-08-04
- Revenue (latest available single quarter): 640,799,000.00 USD; period 2018-01-01/2018-03-31; fiscal year/reporting period 2018/Q1
- Net income (latest available single quarter): 1,099,800,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/875320/000087532026000259/vrtx-20260630.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiqwFBVV95cUxOUFgyYVJvNnAxN1I1bmZmcnZIQXIzVC1uNlZGUzZqR3ozSEEtYnV3T1p4ZG1TRGRhRUhRY1NJZllOUzBqTjVRUmdNelBKMV9BZ1dtcUk2bng3NlJFdjlEV0ZIUEg2TVFuZUNJZHFCQXRmNFVza2FidlZOLXZhbEFlM3QyY2pMNTJKLVJ5Z3A0T2VzLUs3Y19zVWtHWURmMnVXSzd5cWVDUEt1Njg?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxNVlJHemhWaVI4enI0cXRkMTZncnRaMEN3Und6NndBTHFoQ1FaOUZseFZBTmNJaDZUVzd1MHdkd1dPYmd3WDR6M2M3X1BrZ0ZSb053blZYNUpQMWtKTnBack9wdFRNX3g1TnNvTHN3UTVWUGtIQmp1RHFVRDEtX014Tkx0ZDZ6bTMxT3NrTHJXVV9wdkdpSkNBSw?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxNZHJ3T19LVjBFdDc3RUxicks1UUFqdjlYNEZDZ19CNmRZeWdJc0tjbkZiNjY5NlZCSlhUaUtWSzNKbEhValJ1aWtiS2h6SzlyN3hVNzgzMlNzNTVPRzNXZTFlV1BPUHB3U1dUZy1IMWM4c3dDQ2k2bk5mZkd6VDUtazd5aUZVMGpjUTMtVW9reDk4aTBIcWFvUWNxLUFmN2lBR0FDOG1R?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxQc0VzMGtueUtMc3NJN09ZTVpOUTJSaHY1WmdrV3VCTzQ1V0lnVVhFX2ZId2VSV1ZtcTN2aG4zN1pRVVVuSGx6STFzRExxY1lQaGxSN0F0Sm42QTNvMERLRFhZN2ZjdmJrdWlETFpZYThPbVpvYldjYTFZMDdwNDFpS0VsX0lqblM4RUFsYg?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxOQmV1bzlLNFA2T2R0aTY0WEdKYTdWVmZycTFZcXkycjFQS3JVTDBfaEFLTzhlV0ZyZUpQdnV0cW1ubG5TdGx3WXJMZ2FZX0N5VmFhSmVwUTdNbEo2dExlNTliNXBnOFB1MkphcDBTTC1KNVpUd0RBejFtSXM1ME5SQkV6cDV0QVg0b1VfSTh3N2N1WHRYSWEyQlNkb240QThqOTBnVW5fWQ?oc=5
- https://news.google.com/rss/articles/CBMi7AFBVV95cUxQZG5hRkFwbDdac3BTellXczFoU3QxVG5vbGlua09JYzlDTVZlV1l1aENQNjV3blp6WWRQazdwSV9GLWVJRUJnVnNEdTNqTl9zLU1wc3NIS3RfeXJ0OUgyNHhILWFBdTVVVzFMOU1qeGJicDRTa1pNMmtrVTZxcnJreDhKa0RiS0Q0WDRwbDBXN2thT1o3NlpzZW5xQVh0bnJaRWVmb3dCam9PdjRlanpyUnNVV3FkU2MxZU0zd3hyRlRHQ0Rlckk2UzFpNm5MWjlaUUVOTHlpMkhnb1hYN2otYU5KVnBWaGxNVjlqa9IB8gFBVV95cUxNSlRkeFoxU2Q0T0hhTGZLVEVrdlIzWW9fZW9JcnJ3SnlTREE5ejIyVW9mb0tmWVZ0NG1xZUxiaTZMUlVrck90RUlXbHByWE9uWlVZVTFiV1JoWjZXc0JvWVFkQXp4bWRTdjFyQWtRSHF0NWNaa2c4dWlOVkhGSm9POGxFTDdhTDZZenc3c3pDeURBaU5YZjBPOVpHOGhpN3BPWDVJUFZ0M1FTaWxXYlAydW9aLVV0UFk4T3BTZ1h2bllEY2ZLNHlqMzhlb0ZZRmtXamN5Qmg0ZnRxWUliSVY5NGVCS1lMWFIxX0FRQ3dlUXVSZw?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxPOEVKaXlSbjNjRTEwSDRGODcyR0VTV1B3bmZPbU45ejBOZ0E0RERDRmdwVVBySUZkN0NmOWxjQS10QWNyOVhWWTZJaE5VSWppZVhDMnhGSUs3bFZtUHhSLUlHbVRuOEo1bmdCTkk2cENuV1doMGZmTXJ4cXozMXo4S25MeHB5V3JqVlBnVXlRM19kbTlMdno5SVlTQUgwSXRPZjI5Q0szQQ?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxNX0gxQ2xmS0ktZHc5cWNrVW45OGJ4c2taeUFOZkpncmk3NHpVUGJZMXhPLWhXcm1Fc2hXYTh2RVdSdS1LbUwzcXQzVWlPVF9UN1BvWFNRb0xZNXlRVDN1OW8yYllta1kwRjBoSGpIVFhIendxeDMwRTdjcW5nRWxFZjFxWG1LWGpUYXZzOU1jaHdzS3puSXdCY2VR?oc=5
- https://news.google.com/rss/articles/CBMi7AFBVV95cUxNRjY1MTFrN0lZLXdzNVBJRW4tY2VtQUowMDllMWlIOV9pS1QxUWF6R3h1dVRxUktwa0xkVk1UaGFvbnktX1RXUGtwel9hWDFaRzJpNGxJd1E1Q2JMZmFvdmhsd1pncjJ2UG1FVUVjX0w0Vy15YV9NaW1Id3ZldGg5NmctNmppdTAwSUZ1bFB2NUx5QTgtT05xclBTbDdCMDR5WHp3LXZhNnJiRWg5aV9uNlBGUU5raFF0aTdoTUFpRDZKeksyNlRoa1doOXVlQmVielNjZmxyRGQwVXBoUlFaSUFLREY3cEJ6bE1aZdIB8gFBVV95cUxOdnlmaTJPM2VXamFoN2JQSjAwV05YNEhrQmROXzUwdWdMWURqaUY4RjhXZ1dldmJiR3EwaDNXWGgtMWh0aUhkWlplVXFKY0VxTXgxSHdsZUNFcG5Fb0JCWE9Pd0M1RnJfd2lVMGd0d3A3Ql9keVNKWkNUa3VodnVZVjZpWmFkd0xvNWx5LTFzbk4tTkdDM0tsSHFMNWt3UWlqQVBtazBuOUxoVXNZeEprZ2cyLXRLNGo5a3RBeFlVbGRQTTJrZFFuS2lld2t2TkJ5TW9BRkJzWVpRNHlrbWFlOURKaWEzd0QycEplSmxiVS05Zw?oc=5
- https://news.google.com/rss/articles/CBMieEFVX3lxTE5GOHRJNC1Yems2S1BMVXZEWWhWU0hpMHVPTm1YenpFbmZyVERKNmZZbHB2dHNCUDBDZFZRZ0lWV0gzQ2VzZjdiM05uNFdwUURxTG15N1YxRl9yNU9xUUFSMmdSN1I1aksxNkcxWXZiNmUyN2VqMkZ0dw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
