# AMD Intelligence Report

- ticker: **AMD**
- Report as_of: **2026-11-01**
- Market data as_of: **2026-10-30**
- Quant sources: https://finance.yahoo.com/quote/AMD/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AMD/key-statistics/
- AI analysis snapshot as_of: **2026-11-01**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-02T04:33:22.290721+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 6, 'ai': 8, 'unknown': 0, 'irrelevant': 11})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **10** exact headline/source/date matches; prior report **20261101T014405Z-e49d1192/AMD** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 16 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 20.0%; oldest publication 2026-10-29

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 504.8000 |
| Return 1D (%) | -10.8789 |
| Return 1W (%) | -2.3201 |
| Return 1M (%) | -17.4840 |
| Return YTD (%) | 135.7116 |
| Return 1Y (%) | 98.0851 |
| Annualized volatility (%) | 69.0333 |
| Beta vs SPY | 3.3070 |
| Max drawdown (%) | -26.4672 |
| Sharpe (rf=0) | 1.3371 |
| Downside deviation (rf=0, %) | 44.0678 |
| Sortino (rf=0) | 2.0946 |
| Historical VaR 95% (1D, %) | 6.0407 |
| Historical ES 95% (1D, %) | 8.5986 |
| Correlation vs SPY | 0.6127 |
| Tracking error vs SPY (%) | 62.0271 |
| P/E (trailing) | 128.78 |
| P/B | 12.26 |
| EV/EBITDA | 85.26 |
| Revenue growth (%) | 50.10 |
| Forward P/E (estimate) | 31.70 |
| Gross margin (%) | 55.72 |
| Operating margin (%) | 17.25 |
| Return on equity (%) | 10.20 |
| Free cash flow yield (%) | 1.07 |
| MA50 | 548.2902 |
| Close vs MA50 (%) | -7.9320 |
| MA200 | 410.4887 |
| Close vs MA200 (%) | 22.9754 |
| RSI (14, Wilder) | 39.6668 |
| MACD (12,26) | -9.0587 |
| MACD signal (9) | -4.0359 |
| MACD histogram | -5.0229 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AMD': 272, 'SPY': 272}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 504.8000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -10.8789 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -2.3201 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -17.4840 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 135.7116 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 98.0851 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 69.0333 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 44.0678 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 2.0946 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 6.0407 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 8.5986 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6127 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 62.0271 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 3.3070 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -26.4672 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.3371 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 31.6970 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 55.7240 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 17.2500 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 10.1960 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.0729 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 128.7755 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 39.6668 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -5.0229 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -7.9320 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 22.9754 -> Clearly above the moving-average trend level.

## TAILWINDS

### AMD Expands AI Footprint With Meta: Can It Outpace NVDA & AVGO?
- Summary: AMD partners with Meta to expand AI capabilities, aiming to compete with Nvidia and Broadcom.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQcUpTZzVzQVN3dHRNS3Q1M2JxMklqTFhsVUxXUmptSEhPZEVFZmR1RzBpR0dKb0xHaHlJR0ZpdVJodnAyVE1XWEFiUHk2a2tmMy05X2FrRjUwR3ItVnBCbmtwM0VEXzBSaWVuSE53U0ZmRnk0Sm02bHhZZGNoZDlFV3VyTl9fNm1OcHVrczJ0OTVHeEVvUkNGOA?oc=5>

## HEADWINDS

### AMD's Stock Slides After Intel Earnings Reveal Two Big Issues
- Summary: AMD's Stock Slides After Intel Earnings Reveal Two Big Issues
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxPQ1dVeFo2WEd5Y29ZMGRMOUhKakNHOTlZYWpjN1piUld4UXEyNXhCSC11cGFmS0l6a0I4WWdJcUk1d1hUSjlST0Y2Q3p6ZmN5aHNBWl9yMFJaNG1WWHJLamxaTDJHcTZoWmVjaHJaTUZlT2RnM0FlTS1yZ2xYZU1BdjJObUVFc2pDS29FclZvOXd6YXVVYlYyZTNhdTRBcTg?oc=5>

### AMD Stocks Drop 11% With a $13 Billion Revenue Test Approaching
- Summary: AMD Stocks Drop 11% With a $13 Billion Revenue Test Approaching
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxPcnVwXzVmcFBWcHRxaUVLN3lqallOWWFIanBvM041QV9PTkV5Y0ZvUTNWWTlKTUw1ZFdQYVNYd01lMkR0VUx4WXM1X3FZcEoyTlBsUHZNcEhkTnpLUTdjTGoyNE5lclI3dlEwbVpEVXlhVmMtX29JMjhfRUY2NjhYR2F3MXhKVWdjcE15TmlwcXUybjJJN2V0MnRCeFF3YjJSN2c?oc=5>

### AMD Stock Fell 11% in a Day Ahead of Its November 3 Report. Here’s Why Intel’s 78% Data Center Jump Matters More to AMD Than Its PC Warning
- Summary: AMD Stock Fell 11% in a Day Ahead of Its November 3 Report. Here’s Why Intel’s 78% Data Center Jump Matters More to AMD Than Its PC Warning
- Date: 2026-10-31 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi8gFBVV95cUxQaXRtV3ZlQUl5Tng1V090RGRYdVJLTV9JVVV1LWV1U19CNE9GWWFOOUtXN0UwNWt2dVQxMVNpOTdVNGpzS180aC1xRVZMRzQyb2VQZElNVmhQUmczRmxFMmY3M0hZUDNQVU9HQnJISlpWc3hKQW50Y3d2akZObGVCWFpnUEZxX2ZnSFlHMjdNcjk3MDNiTFM1dzZtUFdmRW44elcyR0tJN1R3WUN5ZEtyZDNFRERXVGxnczBHbElUUENFbVV2b3U1clZzakN0UGpOVkNjc2x5d1RpTzE4bHZJLXBrMUtuVjAtWVdWZU5TYm1fZw?oc=5>

### Advanced Micro Devices slides 13% as part of tech selloff (AMD:NASDAQ)
- Summary: AMD stock fell 13% amid broader tech selloff, indicating short-term downside pressure.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxPWGV3V2xDR1l0WWdPb1JuRk9WYm81cDQxdFB3NHFXUGZUamIxQzk2MTZ3MFFYSkx1c0VPQTNrT09mdmh5UERtTjZvVTBKRXVPc2NwMHJYMVlfZldGNW9CY2xobXpsTmZjUFRtcDE3dTJwemxHNVRRcU1vcG1uZUZZN1lidjJyWnRXRkVlX2w3ZnVmbEkxcG0yX3FB?oc=5>

## CATALYSTS

### Advanced Micro Devices, Inc. $AMD Stock: Sumitomo Mitsui Trust Group Inc. Lowers Holdings
- Summary: Advanced Micro Devices, Inc. $AMD Stock: Sumitomo Mitsui Trust Group Inc. Lowers Holdings
- Date: 2026-11-01 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi3gFBVV95cUxPUjFKSUQxMWtVa0VTTWlKc3ZXckZvaTM2Q2ctSDJqa1dnb0c4b2l3eU5YSkNwa0tKQ21aOUNYLWZ0UUIzaHZMcVBQNU0tVkQxR2NuYzdUWFV2M3VPMUMyU0laRnR6TXNGNGZiLVNocmxRS0g4MURjdjFDbk1rU3hKSTR3YUJzTDZvYmdfam9OYkNTWE1QU0JhOHBFLUpUOWlhTVFBa2MyaUhod2t1N2FrLVpoVEw0Q2FZcUwzSUMzUXpiRmJPbTRSelRIajEwM1RxWE5HczREeHN3bUdUSlE?oc=5>

### Advanced Micro Devices (AMD) Lands First GSI Deployment Under AI Compute Deal
- Summary: Advanced Micro Devices (AMD) Lands First GSI Deployment Under AI Compute Deal
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxOVGRiNXIyLUNIRGthWXhrRmNyTERCOFc5QjB5ZWplVzlqenBma3VzUWZQZEZrTjBZck5obXVLQTV6Qm9vRVlST1BweVR5TWpPak02LVBRY3lTLVkzYXRYUmhKMWVrNzc5QjE2WnBvWlcxQ2FJWWRiOWVjRFZqTjN4cHZSZnI0S1Rzem9WejR0M0ltWFVhWTBaNEp1a1k?oc=5>

### AMD Earnings Preview: The Bull Case Is Largely Priced In (NASDAQ:AMD)
- Summary: AMD Earnings Preview: The Bull Case Is Largely Priced In (NASDAQ:AMD)
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxON3lGMDBoeWdCeklWb0RtZGxfSHZMb29uUTUxM1Q5dHgxOWxiaWpOak42R0Q2NzVWMXozbmFKWG5UMmlsOTNQai1aT3l6a1o3UzhXeFZKRFpMTWJwbDg3WnZaUS1DbTNDdHR4ZlRxMi1pVE51QktWQ0Vvay0zZW1HUDE5eFZJVlBPS1dhLVV4Ym1jXzdySDB6ZlJmOFk?oc=5>

### Intel, AMD lead semiconductor rout as SOXX drops about 10%
- Summary: AMD shares fall as semiconductor sector declines, reflecting broader market weakness.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxNb1R4bGFvaUxsemtCY0lHd24wVVRUZHJ3bjVWM09JMGRjc20wanA0NU50VUVnYUdGZUJUVHBSTmIyaVFITTI1YVRNSlQxOUNVTDR1bFMtY1pYQlJoTzctclp5U3RTRFVtN1NqOS1CTU9BSFA1NjZIa3ktZWpMLUpyeHltY1RCcVhleEU0Tno0U1daajF2S1E2ek55ZnoyY0hVMnczcFpZNm5rOXRseWFKckxCTWQ5VndqalBB?oc=5>

### What to Expect From AMD’s Q3 Earnings
- Summary: Analysts discuss expectations for AMD's Q3 earnings, focusing on revenue, margins, and guidance.
- Date: 2026-10-31 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMihwFBVV95cUxQS3FlNmJKZmt4TmMtSXRUcmpaUnNoVlotWVdzR0EtcnpqYldWbDNsNUtVaUJGRTR0Y2hHcElQaVZGU2UyR2hla19UaGxBYVFTZXZMbGluai11cXk1R0FDQmpxUG1rekp1RElXMDUzSmdNQkM4Q1hacTAwb3hldVVTTjNMR1ZHMkU?oc=5>

### Cathie Wood’s Latest AMD Move Means Absolutely Nothing
- Summary: Cathie Wood's investment in AMD is highlighted, but analysts suggest it may not impact the company's performance.
- Date: 2026-10-30 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxNZmt6MUc5VnU2S2Jvakw0STNyYUpFWkg5NlVqaC1ZZnJuVGdYbDFnbThOT3k0eExxWk5GdUd6NGlDNUFpUlpsZkFTVG5QQm5vWTZ3ZDhYNXlTWDl2SUdjbHdhS2w1U0RzTkFLUC15VV82OUJvRjVMRC11UHVIQ21LYzM1UFhIWWs5NHpOZlR4TlZlTk8tdnVNNWtid3Aydw?oc=5>

### AMD Earnings Preview: Can Surging AI Sales Calm PC Fears After 11% Stock Drop?
- Summary: The preview examines whether AI sales growth can offset PC market concerns following a recent stock decline.
- Date: 2026-11-01 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxONG4xWmRUZXRPNzhNVlI4T3M4UnQ3R0RfT1hiLUExVWhOQnR4ZkdMVFdNVWVEaTVsbjlpcFcycjVfOUdXQkRYUURfRHhHcE02QXhfal9KZEZMQlRodFRsaUdNQ0h5SU5zbzNmV1ZkN3gzb19UUlhXYnA1d1lCeHkxWmEtOUVPYXlkSVZ2RHJoUXgwLTVxMERDTU5lWEhkWmR6WGE0NkhhUGI?oc=5>

### AMD Stock $504.80: What 3 November Results Must Show
- Summary: Investors look to AMD's November results for key metrics that could influence the stock price.
- Date: 2026-11-01 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxNTERpYmppbDNsWWxFbVFKQ1BtRk8xakxzeVAwcXNHR1lXOWlMVUhTSWcwaGZISU9USVFrV28zUkZDd3dfVjZSZFFSTzF6V0Jhc3U4SnFkc0t1SnFSOHJyNTdBQzBXcmJRRG02U0toQUttMWZibDdpSUpvRVpONU5iQzdDd1RROE93ZzRJZDNXak1Zb0lPM2c1cVAwZk5QTWNONndxMVhYVnE0Q1I4Z0hr?oc=5>

### AMD Has Ripped 170% This Year: Is It Too Late to Buy?
- Summary: The article reviews AMD's year-to-date performance and discusses potential buying opportunities.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxQQnNwWkxWaE01dWV3aW1yRnFpczlwb05JOWVIREZ1dGI0cUNEV0dqdlBJcUJjUlJtcWdSQUhaazk0M2FUaFF0NkJ2aU44QW43SUNpdG9vLWlPbFRsS25xMEtEY2tLVHdCN3VBSzdKajZTQk8za0VoYjBVd1M0UXVZZjhXVHFQVUFadUZVVTJtN0I?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AMD** | **128.78** | **12.26** | **85.26** | **50.10** | **824,073,388,032.00 USD** | **98.09** |
| NVDA | 25.87 | 21.58 | 24.39 | 105.90 | 4,941,441,662,976.00 USD | 1.10 |
| INTC | N/A | 3.04 | 18.84 | 20.90 | 349,514,399,744.00 USD | 63.75 |
| AVGO | 41.64 | 15.62 | 30.46 | 85.50 | 1,556,585,250,816.00 USD | -12.74 |

Peers fetched as_of: 2026-11-01; AMD reuses existing data (market data as_of: 2026-10-30); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-04
- Next expected earnings: 2026-11-03 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-01

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-08-05
- Revenue (latest available single quarter): 1,584,000,000.00 USD; period 2017-07-02/2017-09-30; fiscal year/reporting period 2018/Q3
- Net income (latest available single quarter): 2,297,000,000.00 USD; period 2026-03-29/2026-06-27; fiscal year/reporting period 2026/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/2488/000000248826000123/amd-20260627.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMimAFBVV95cUxQcUpTZzVzQVN3dHRNS3Q1M2JxMklqTFhsVUxXUmptSEhPZEVFZmR1RzBpR0dKb0xHaHlJR0ZpdVJodnAyVE1XWEFiUHk2a2tmMy05X2FrRjUwR3ItVnBCbmtwM0VEXzBSaWVuSE53U0ZmRnk0Sm02bHhZZGNoZDlFV3VyTl9fNm1OcHVrczJ0OTVHeEVvUkNGOA?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxPQ1dVeFo2WEd5Y29ZMGRMOUhKakNHOTlZYWpjN1piUld4UXEyNXhCSC11cGFmS0l6a0I4WWdJcUk1d1hUSjlST0Y2Q3p6ZmN5aHNBWl9yMFJaNG1WWHJLamxaTDJHcTZoWmVjaHJaTUZlT2RnM0FlTS1yZ2xYZU1BdjJObUVFc2pDS29FclZvOXd6YXVVYlYyZTNhdTRBcTg?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxPcnVwXzVmcFBWcHRxaUVLN3lqallOWWFIanBvM041QV9PTkV5Y0ZvUTNWWTlKTUw1ZFdQYVNYd01lMkR0VUx4WXM1X3FZcEoyTlBsUHZNcEhkTnpLUTdjTGoyNE5lclI3dlEwbVpEVXlhVmMtX29JMjhfRUY2NjhYR2F3MXhKVWdjcE15TmlwcXUybjJJN2V0MnRCeFF3YjJSN2c?oc=5
- https://news.google.com/rss/articles/CBMi8gFBVV95cUxQaXRtV3ZlQUl5Tng1V090RGRYdVJLTV9JVVV1LWV1U19CNE9GWWFOOUtXN0UwNWt2dVQxMVNpOTdVNGpzS180aC1xRVZMRzQyb2VQZElNVmhQUmczRmxFMmY3M0hZUDNQVU9HQnJISlpWc3hKQW50Y3d2akZObGVCWFpnUEZxX2ZnSFlHMjdNcjk3MDNiTFM1dzZtUFdmRW44elcyR0tJN1R3WUN5ZEtyZDNFRERXVGxnczBHbElUUENFbVV2b3U1clZzakN0UGpOVkNjc2x5d1RpTzE4bHZJLXBrMUtuVjAtWVdWZU5TYm1fZw?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxPWGV3V2xDR1l0WWdPb1JuRk9WYm81cDQxdFB3NHFXUGZUamIxQzk2MTZ3MFFYSkx1c0VPQTNrT09mdmh5UERtTjZvVTBKRXVPc2NwMHJYMVlfZldGNW9CY2xobXpsTmZjUFRtcDE3dTJwemxHNVRRcU1vcG1uZUZZN1lidjJyWnRXRkVlX2w3ZnVmbEkxcG0yX3FB?oc=5
- https://news.google.com/rss/articles/CBMi3gFBVV95cUxPUjFKSUQxMWtVa0VTTWlKc3ZXckZvaTM2Q2ctSDJqa1dnb0c4b2l3eU5YSkNwa0tKQ21aOUNYLWZ0UUIzaHZMcVBQNU0tVkQxR2NuYzdUWFV2M3VPMUMyU0laRnR6TXNGNGZiLVNocmxRS0g4MURjdjFDbk1rU3hKSTR3YUJzTDZvYmdfam9OYkNTWE1QU0JhOHBFLUpUOWlhTVFBa2MyaUhod2t1N2FrLVpoVEw0Q2FZcUwzSUMzUXpiRmJPbTRSelRIajEwM1RxWE5HczREeHN3bUdUSlE?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxOVGRiNXIyLUNIRGthWXhrRmNyTERCOFc5QjB5ZWplVzlqenBma3VzUWZQZEZrTjBZck5obXVLQTV6Qm9vRVlST1BweVR5TWpPak02LVBRY3lTLVkzYXRYUmhKMWVrNzc5QjE2WnBvWlcxQ2FJWWRiOWVjRFZqTjN4cHZSZnI0S1Rzem9WejR0M0ltWFVhWTBaNEp1a1k?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxON3lGMDBoeWdCeklWb0RtZGxfSHZMb29uUTUxM1Q5dHgxOWxiaWpOak42R0Q2NzVWMXozbmFKWG5UMmlsOTNQai1aT3l6a1o3UzhXeFZKRFpMTWJwbDg3WnZaUS1DbTNDdHR4ZlRxMi1pVE51QktWQ0Vvay0zZW1HUDE5eFZJVlBPS1dhLVV4Ym1jXzdySDB6ZlJmOFk?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxNb1R4bGFvaUxsemtCY0lHd24wVVRUZHJ3bjVWM09JMGRjc20wanA0NU50VUVnYUdGZUJUVHBSTmIyaVFITTI1YVRNSlQxOUNVTDR1bFMtY1pYQlJoTzctclp5U3RTRFVtN1NqOS1CTU9BSFA1NjZIa3ktZWpMLUpyeHltY1RCcVhleEU0Tno0U1daajF2S1E2ek55ZnoyY0hVMnczcFpZNm5rOXRseWFKckxCTWQ5VndqalBB?oc=5
- https://news.google.com/rss/articles/CBMihwFBVV95cUxQS3FlNmJKZmt4TmMtSXRUcmpaUnNoVlotWVdzR0EtcnpqYldWbDNsNUtVaUJGRTR0Y2hHcElQaVZGU2UyR2hla19UaGxBYVFTZXZMbGluai11cXk1R0FDQmpxUG1rekp1RElXMDUzSmdNQkM4Q1hacTAwb3hldVVTTjNMR1ZHMkU?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxNZmt6MUc5VnU2S2Jvakw0STNyYUpFWkg5NlVqaC1ZZnJuVGdYbDFnbThOT3k0eExxWk5GdUd6NGlDNUFpUlpsZkFTVG5QQm5vWTZ3ZDhYNXlTWDl2SUdjbHdhS2w1U0RzTkFLUC15VV82OUJvRjVMRC11UHVIQ21LYzM1UFhIWWs5NHpOZlR4TlZlTk8tdnVNNWtid3Aydw?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxONG4xWmRUZXRPNzhNVlI4T3M4UnQ3R0RfT1hiLUExVWhOQnR4ZkdMVFdNVWVEaTVsbjlpcFcycjVfOUdXQkRYUURfRHhHcE02QXhfal9KZEZMQlRodFRsaUdNQ0h5SU5zbzNmV1ZkN3gzb19UUlhXYnA1d1lCeHkxWmEtOUVPYXlkSVZ2RHJoUXgwLTVxMERDTU5lWEhkWmR6WGE0NkhhUGI?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxNTERpYmppbDNsWWxFbVFKQ1BtRk8xakxzeVAwcXNHR1lXOWlMVUhTSWcwaGZISU9USVFrV28zUkZDd3dfVjZSZFFSTzF6V0Jhc3U4SnFkc0t1SnFSOHJyNTdBQzBXcmJRRG02U0toQUttMWZibDdpSUpvRVpONU5iQzdDd1RROE93ZzRJZDNXak1Zb0lPM2c1cVAwZk5QTWNONndxMVhYVnE0Q1I4Z0hr?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxQQnNwWkxWaE01dWV3aW1yRnFpczlwb05JOWVIREZ1dGI0cUNEV0dqdlBJcUJjUlJtcWdSQUhaazk0M2FUaFF0NkJ2aU44QW43SUNpdG9vLWlPbFRsS25xMEtEY2tLVHdCN3VBSzdKajZTQk8za0VoYjBVd1M0UXVZZjhXVHFQVUFadUZVVTJtN0I?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
