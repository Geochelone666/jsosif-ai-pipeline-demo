# NVDA Intelligence Report

- ticker: **NVDA**
- Report as_of: **2026-10-28**
- Market data as_of: **2026-10-28**
- Quant sources: https://finance.yahoo.com/quote/NVDA/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NVDA/key-statistics/
- AI analysis snapshot as_of: **2026-10-28**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-29T02:24:37.505699+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 7, 'ai': 9, 'unknown': 0, 'irrelevant': 8})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **3** exact headline/source/date matches; prior report **20261028T015717Z-533e470c/NVDA** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 7 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 50.0%; oldest publication 2026-10-26

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 215.3800 |
| Return 1D (%) | -1.1746 |
| Return 1W (%) | -2.9689 |
| Return 1M (%) | -5.8901 |
| Return YTD (%) | 15.7555 |
| Return 1Y (%) | 7.3949 |
| Annualized volatility (%) | 37.2869 |
| Beta vs SPY | 1.9244 |
| Max drawdown (%) | -20.2144 |
| Sharpe (rf=0) | 0.3772 |
| Downside deviation (rf=0, %) | 25.2933 |
| Sortino (rf=0) | 0.5560 |
| Historical VaR 95% (1D, %) | 3.7736 |
| Historical ES 95% (1D, %) | 4.5600 |
| Correlation vs SPY | 0.6556 |
| Tracking error vs SPY (%) | 30.5063 |
| P/E (trailing) | 27.54 |
| P/B | 22.71 |
| EV/EBITDA | 25.67 |
| Revenue growth (%) | 105.90 |
| Forward P/E (estimate) | 13.53 |
| Gross margin (%) | 74.67 |
| Operating margin (%) | 66.24 |
| Return on equity (%) | 117.21 |
| Free cash flow yield (%) | 0.80 |
| MA50 | 221.9971 |
| Close vs MA50 (%) | -2.9807 |
| MA200 | 203.8411 |
| Close vs MA200 (%) | 5.6607 |
| RSI (14, Wilder) | 43.8843 |
| MACD (12,26) | -2.6585 |
| MACD signal (9) | -1.5322 |
| MACD histogram | -1.1264 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NVDA': 270, 'SPY': 270}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 215.3800 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.1746 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -2.9689 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -5.8901 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 15.7555 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 7.3949 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 37.2869 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 25.2933 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.5560 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.7736 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.5600 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6556 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 30.5063 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.9244 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -20.2144 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.3772 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 13.5335 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 74.6740 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 66.2370 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 117.2110 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 0.8039 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 27.5422 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 43.8843 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -1.1264 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -2.9807 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 5.6607 -> Clearly above the moving-average trend level.

## TAILWINDS

### NVIDIA (NASDAQ:NVDA) Stock Price Up 2.4% - What's Next?
- Summary: NVIDIA (NASDAQ:NVDA) Stock Price Up 2.4% - What's Next?
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxOd3QtUS1INzUwaDdYUktGRWF2NUlfa2xfQWVYT1VBZFM2c0c5TTlqWTZfWjduOWp1Wlg3NmxKdzRFYk5BSVdKRzN2OUJIcnZwZlB1S1VFelBkdG5sTFQ1dXpscjRKZVl2Z1QzNWIyS1dZdUt3a1JTVVhMYzJCLUpPdGJJVGNzd3M2SnFqTGtKaEtDcWRabzBzNXZFcEhpenlxWFF3bEtaUmlQcGc?oc=5>

### NVDA Stock Ticks Higher Overnight: a16z Data Shows GPU Rental Prices Rising Sharply, Even For Older Chips
- Summary: NVDA Stock Ticks Higher Overnight: a16z Data Shows GPU Rental Prices Rising Sharply, Even For Older Chips
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxNVzhIbU14cHlhdjlKTUNmTkpxbXBMTXRHb2U5Wk1rMVg0dEhwX216VVJmUEhfT3l5SUtKZVB0ZU91QklIdERHMDRzSXhmcExnMmJxSUxNMUhJNmpYdEN4bUFMTXlwbjY4WjRENmZyR0JfQWMwTWxramtEVi0teDZWOUVMTUVFRjJSTGg2NjJ6eTVXYmFxWllIT1BQeHFGemM?oc=5>

### Nvidia (NVDA) Surpasses Market Returns: Some Facts Worth Knowing
- Summary: NVDA outperformed market returns, indicating strong performance.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxQdnNyZ1g4R2pVdTJTQW1HNE53cGJLSDVBbGFTUWZlOFd0akxCQUJ6SzBwWVVlaDFYZjlLdXA3TktObUZrdnJRX1lCcEFnbDBvZTliYUVCeC1OUDMtVGxhT2pvVWxnYm05UUhEUnRER1NGbFVLZmhWVG8wYVcxQ3hKRHdjdnNkMkRGWFFuRjBFRjdUeE5oU1drR3oxV2tyUUFCcExN?oc=5>

### ETFs Are Buying NVIDIA (NVDA) on Thursday
- Summary: ETFs are purchasing NVDA shares, indicating increased institutional demand.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxQRDhlSHItazZid1JpaGpGOVJSb0tMUENleERVZEVyX3pMaklPcXJwRDBqQlFVcTRBTzZ5ZXM4ZEMzRWdHS2oyaV8yNUFBeFFqU0l2UDZCd0s2THhnMUJkMGRfeWpNb2tJVjZaLXNmblNDdWlaczJPTjQwYkVsTzRaeVN0MlgzcG5ob3U5V05raGowQ2hGRVEzMjJQNTVnUQ?oc=5>

### Buy 10 Shares of Nvidia Today? Here’s What Different 2030 Scenarios Could Look Like
- Summary: Analyst scenarios for Nvidia’s 2030 performance, offering long-term outlooks.
- Date: 2026-10-28 | Impact: low | Horizon: long | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxQLUR6RDFYc3VSb0h3U1ZFQXZCM01lN2w4enRTVGFuekVwT1NneHhxR0tGZHJSeUk1bTVwckZxQlBTU3hYcDdUY28wOVBzekd6Z0Qtby0xbXM4STBjdzJQTUFFaTBJZ3JrS3JKbmV1OVJOZEdCU0pDUkpMLUhyVnZBWkllUERMTzUwenlUMm5CLUp0RHZ3SWU5OGxPZmJiRmJQLThNbUpkeTBhYVlESW5HZzZtZlF5TWt2UHo0Y0tJX2pQR00?oc=5>

### Prediction: This Will Be Nvidia's Stock Price by the End of 2027
- Summary: Forecast of Nvidia’s 2027 stock price, providing speculative guidance.
- Date: 2026-10-28 | Impact: low | Horizon: long | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxOSE5kLWtkeHlacEVIVWdjYWQxMy1neTRiWVZCNFdJUFBFZTZmWUZQT0ROcS1hbWotcG96UU9pSklPQ3pqa1cwZUdsbHE3N0dsT2pjU2oyT1JmVkRyMDBiZFV2akthMnpQazFxck9MbmxpYjRSU2xpVXUzWDRwcU5NTkhOUDRKczZ0d25RQ1ZSQjZnbjQ1MjdmYg?oc=5>

### NVIDIA (NVDA) Analyst Ratings, Stock Forecast and Price Target
- Summary: Compilation of analyst ratings and price targets for Nvidia.
- Date: 2026-10-28 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxOWGJWb3NoNzZMS2s1SnByZUZyR1RnSFBLN1huOVJBdzJBbG9idXhoN3RTR3lwb2o1ZDV6OWZTUHRVVmVuVG5DcnllOER3cU42eEJtRmNNZHdIUnZJdDZJTHdqa2xEOGpkV2t2LUp1TGZRN3dFY1hqWmJPbnZFcVJ3bFlxZjQxdnQxU19rWVdZdEtXUlJFeVJmMU9yNFJSR1NXSkU1X2huUEktcEVHNDlWOFRuZHFBWkRv?oc=5>

## HEADWINDS

### Nvidia Stock Is Down 12% From Its High. Here's What History Says Happens Next.
- Summary: Nvidia Stock Is Down 12% From Its High. Here's What History Says Happens Next.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihwFBVV95cUxPcEZla1VqXzQxakdfSk52MkVWQ191TzRxSDJpSi1JMU5jUkZiNTYxQi1xeG92dnhHUDFsWjhBejM1dXNUTUs4WmVvZHFtTUw0bUh0bHVuN0hwUFJvcGdNb2FRZmRoaEtRbHd1aS1BYS11NmU3cXltVm9iZEd0N29IWVZxal9XZjg?oc=5>

## CATALYSTS

### Nvidia Stock $216: SpaceX $40B GPU Deal, Bull $243
- Summary: Nvidia Stock $216: SpaceX $40B GPU Deal, Bull $243
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxOT2ZzTjNmanRRMnAxOW5GZTR0Y2hPU1NtZ29TOElBa3BfTHVlR2pCUzQ5UTBkRGtyeHhNWkhpZUlKZDN2UnRVdG1wNzdHeUhoakNhbmFaSkhBeF9vY1ZLajNLWk9mQmVSYXJjbldsYUIwYS1ycnplSnQtZ1lvVlZYV0RMcjdueXgtOUd5aEQzVER3bHh0c21MUWl6RGJzRkxfNjlmOWZsRjJpMWY0Mnp4b2NPWGJ1UjlNbm1vbQ?oc=5>

### NVDA Stock Edges Down On DOJ Interest In $12.9 Billion Hugging Face Acquisition
- Summary: NVDA Stock Edges Down On DOJ Interest In $12.9 Billion Hugging Face Acquisition
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxPNnRxUGd1QjJiYWlRWTlWd2lyWDN1eW5YSWFyYkJYWnhlMGMtY3VobFJIUW1qcXg0Nkh4U0hwZ0phV2VjNnZVYlQxbkRydWxZMEtaWGRNOTVOZC0wME5GOXVHSkdKZllPRTRaWkIzMGh5eXBwd1JuWml2SUg5Z0ozV3l2UUFiVTZLMmNBMTQtX19RcXB5?oc=5>

### Nvidia (NASDAQ:NVDA) to Invest $3 Billion in Meta (NASDAQ:META) Share Offering as AI Partnership Expands
- Summary: Nvidia (NASDAQ:NVDA) to Invest $3 Billion in Meta (NASDAQ:META) Share Offering as AI Partnership Expands
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxPa3p2ZDNFSE9sdnIwSWVWN1hTX2JaUzV0am9lNlNzS3VKbEpBbDRaWjRORlVOUjNSam9jdjF1anE1eVkzZlFUWTc5X0Y4VHJqaVd2anVKS09CQWNVSHliMUFkNERSbU1sOTZ2OUxOSW8tVmZlVEhrNjYwLUhUZVFVLVpxUmFkaXdyMVhlYU5jVk45NEY1VXc?oc=5>

### Nvidia to invest $3 billion in Meta, expand partnership on Muse
- Summary: Nvidia to invest $3 billion in Meta, expand partnership on Muse
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxPWFVwN1hfQVhaWm9LZkY0bERYY0JtOVBtR2dSSHV4T1c0eU91TjN6WXAwTHNvZmhnQlpkUENkSGhYT21aNWlBWjM0dXNFSHp5andOeTlKRzhDN3NremU5QzhTdDlRMThvMGZFck02ZnUtRWIybmloSTJPVnktWlVSRWdOZ1c3QWY3bk1GVUN1YWx4aExfRnJ4b2VtNlFia0wtVWNQZE5mcl9Ld2JUT3g5X1FRT1lYSUVpVWc?oc=5>

### Nvidia May Actually Raise Its 70% Growth Guide In November
- Summary: Nvidia may lift its 70% growth forecast, boosting investor expectations.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxOMzkwNDNBX2JDYk1SOUF2YVlkdEx4U05naHhkV0xLZzNfWmNYd2M1bGVCOU0ySTQwNjVzbFFBTEZNVDMzSENyalpMU2FXMFZEN2YzVTNzT093WExtSlJnald4Ny1PdWtKWS1QMmQ0WVNDOTlPVVJadlg0VERoUXNYcnRjVWJ0N0JsU3BXZ0p3UG5ueG9LZG5nTU1VVzltR3NkWjVtZUtRY095UQ?oc=5>

### SK Hynix, Nvidia and Micron send one clear message to investors with their stocks off the highs
- Summary: NVDA stock fell from recent highs, signaling investor caution.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi7wFBVV95cUxOOG1VS2oyRGs5WkYxbmREb0l6WTJ4TTB3cm9lM2VZTVRTOGt3QmpQQ2hoc2ZHV3htd1JPMWFSd0VmWVY3UVRYZzhOLWtuSWU1Ry1ha1NWOGxDcnI2WEJEQXdiZmpMN042Vi11NmZlckRYVUlUdWEwc0hiYnFLdi1lN2pTYlRJWEREY3ByTTJ6bjdXWVJvbDNEVVB0SzhsRWpuNU53NklQeGVRQ2RYUEJQT2dKZDMtQWN0Z3hZem94RzVOdFpQOTNMc0hlR1J3MDVaUmllUDg0b3ZKZWVHWUVmMjRzbzJ5dF9ONVdtY1pvOA?oc=5>

### Nvidia: Risk Building, Earnings Revisions Can Turn Negative (NASDAQ:NVDA)
- Summary: NVDA warns that risk building and earnings revisions could become negative.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxQMmRBanZIT29hZVU4TWVSWENzU2NzbkNHNHNPb0dWX0xtLWVPaS1qQ3FEcDQ0ejdCbWhkUDh5YWt5aWFBank3dHhLZXNYTnFqWEpzT0Z3a2dwbGxta2gwak4tNEYzUDBKcnUxSS04MzdDVHNhczBid3BzTDZnTkVXS1JTcm9VTEpaUUp2dnZMOGVlOGh5Yk9MRERSTDBOVUE?oc=5>

### NVDA Stock Alert: What to Know as Nvidia Invests $3 Billion in Meta
- Summary: NVIDIA invests $3B in Meta, strengthening partnership and expanding AI collaboration.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxON0JPdEc2MXNVR1UzZF8tZk00UERCQTF2RnkwU3Q0QTNXcDJ5MmtNeF94dmpoZXVTWFRydkUwb1UySkU5dEtSQ1NweGRVTUN0V2FDQU14QUIzU3Zfa2JZRTlLSks4Zm1LVWxiN1FnTzd4ZXdrZEF1VnhEeWF0LTMtWDZrNTBlSmJ1YUJ4a1dfZXAtOTBJZnJ0Yw?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NVDA** | **27.54** | **22.71** | **25.67** | **105.90** | **5,200,780,722,176.00 USD** | **7.39** |
| AMD | 142.82 | 14.04 | 97.83 | 50.10 | 944,288,825,344.00 USD | 124.19 |
| AVGO | 44.93 | 16.85 | 32.81 | 85.50 | 1,679,410,724,864.00 USD | -4.97 |
| INTC | N/A | 5.50 | 30.78 | 25.40 | 504,981,618,688.00 USD | 130.03 |

Peers fetched as_of: 2026-10-28; NVDA reuses existing data (market data as_of: 2026-10-28); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-26
- Next expected earnings: 2026-11-17 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-28

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-08-26
- Revenue (latest available single quarter): 96,221,000,000.00 USD; period 2026-04-27/2026-07-26; fiscal year/reporting period 2027/Q2
- Net income (latest available single quarter): 59,688,000,000.00 USD; period 2026-04-27/2026-07-26; fiscal year/reporting period 2027/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiqwFBVV95cUxOd3QtUS1INzUwaDdYUktGRWF2NUlfa2xfQWVYT1VBZFM2c0c5TTlqWTZfWjduOWp1Wlg3NmxKdzRFYk5BSVdKRzN2OUJIcnZwZlB1S1VFelBkdG5sTFQ1dXpscjRKZVl2Z1QzNWIyS1dZdUt3a1JTVVhMYzJCLUpPdGJJVGNzd3M2SnFqTGtKaEtDcWRabzBzNXZFcEhpenlxWFF3bEtaUmlQcGc?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxNVzhIbU14cHlhdjlKTUNmTkpxbXBMTXRHb2U5Wk1rMVg0dEhwX216VVJmUEhfT3l5SUtKZVB0ZU91QklIdERHMDRzSXhmcExnMmJxSUxNMUhJNmpYdEN4bUFMTXlwbjY4WjRENmZyR0JfQWMwTWxramtEVi0teDZWOUVMTUVFRjJSTGg2NjJ6eTVXYmFxWllIT1BQeHFGemM?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxQdnNyZ1g4R2pVdTJTQW1HNE53cGJLSDVBbGFTUWZlOFd0akxCQUJ6SzBwWVVlaDFYZjlLdXA3TktObUZrdnJRX1lCcEFnbDBvZTliYUVCeC1OUDMtVGxhT2pvVWxnYm05UUhEUnRER1NGbFVLZmhWVG8wYVcxQ3hKRHdjdnNkMkRGWFFuRjBFRjdUeE5oU1drR3oxV2tyUUFCcExN?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxQRDhlSHItazZid1JpaGpGOVJSb0tMUENleERVZEVyX3pMaklPcXJwRDBqQlFVcTRBTzZ5ZXM4ZEMzRWdHS2oyaV8yNUFBeFFqU0l2UDZCd0s2THhnMUJkMGRfeWpNb2tJVjZaLXNmblNDdWlaczJPTjQwYkVsTzRaeVN0MlgzcG5ob3U5V05raGowQ2hGRVEzMjJQNTVnUQ?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxQLUR6RDFYc3VSb0h3U1ZFQXZCM01lN2w4enRTVGFuekVwT1NneHhxR0tGZHJSeUk1bTVwckZxQlBTU3hYcDdUY28wOVBzekd6Z0Qtby0xbXM4STBjdzJQTUFFaTBJZ3JrS3JKbmV1OVJOZEdCU0pDUkpMLUhyVnZBWkllUERMTzUwenlUMm5CLUp0RHZ3SWU5OGxPZmJiRmJQLThNbUpkeTBhYVlESW5HZzZtZlF5TWt2UHo0Y0tJX2pQR00?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxOSE5kLWtkeHlacEVIVWdjYWQxMy1neTRiWVZCNFdJUFBFZTZmWUZQT0ROcS1hbWotcG96UU9pSklPQ3pqa1cwZUdsbHE3N0dsT2pjU2oyT1JmVkRyMDBiZFV2akthMnpQazFxck9MbmxpYjRSU2xpVXUzWDRwcU5NTkhOUDRKczZ0d25RQ1ZSQjZnbjQ1MjdmYg?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxQOUV6dVd5UU1ESWo2WjBmR3NMTWNiTUxmUmxacl9FWTQ0aTM3aW94UUUyZk5oSWtaSUgxX2RSajlXbkFLQURzUEo4c3NEcURDRlZ2cV9TbDQwTVZpX29TQUFyYU1QaWNCQnZXZlB5aktJSmdjNDJMZm9DcUczVXdQZTlMMXkyVkYxV0duRlFKSWtqVHhqZTV6WFhfUVhtMDBh?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxOWGJWb3NoNzZMS2s1SnByZUZyR1RnSFBLN1huOVJBdzJBbG9idXhoN3RTR3lwb2o1ZDV6OWZTUHRVVmVuVG5DcnllOER3cU42eEJtRmNNZHdIUnZJdDZJTHdqa2xEOGpkV2t2LUp1TGZRN3dFY1hqWmJPbnZFcVJ3bFlxZjQxdnQxU19rWVdZdEtXUlJFeVJmMU9yNFJSR1NXSkU1X2huUEktcEVHNDlWOFRuZHFBWkRv?oc=5
- https://news.google.com/rss/articles/CBMihwFBVV95cUxPcEZla1VqXzQxakdfSk52MkVWQ191TzRxSDJpSi1JMU5jUkZiNTYxQi1xeG92dnhHUDFsWjhBejM1dXNUTUs4WmVvZHFtTUw0bUh0bHVuN0hwUFJvcGdNb2FRZmRoaEtRbHd1aS1BYS11NmU3cXltVm9iZEd0N29IWVZxal9XZjg?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxOT2ZzTjNmanRRMnAxOW5GZTR0Y2hPU1NtZ29TOElBa3BfTHVlR2pCUzQ5UTBkRGtyeHhNWkhpZUlKZDN2UnRVdG1wNzdHeUhoakNhbmFaSkhBeF9vY1ZLajNLWk9mQmVSYXJjbldsYUIwYS1ycnplSnQtZ1lvVlZYV0RMcjdueXgtOUd5aEQzVER3bHh0c21MUWl6RGJzRkxfNjlmOWZsRjJpMWY0Mnp4b2NPWGJ1UjlNbm1vbQ?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxPNnRxUGd1QjJiYWlRWTlWd2lyWDN1eW5YSWFyYkJYWnhlMGMtY3VobFJIUW1qcXg0Nkh4U0hwZ0phV2VjNnZVYlQxbkRydWxZMEtaWGRNOTVOZC0wME5GOXVHSkdKZllPRTRaWkIzMGh5eXBwd1JuWml2SUg5Z0ozV3l2UUFiVTZLMmNBMTQtX19RcXB5?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxPa3p2ZDNFSE9sdnIwSWVWN1hTX2JaUzV0am9lNlNzS3VKbEpBbDRaWjRORlVOUjNSam9jdjF1anE1eVkzZlFUWTc5X0Y4VHJqaVd2anVKS09CQWNVSHliMUFkNERSbU1sOTZ2OUxOSW8tVmZlVEhrNjYwLUhUZVFVLVpxUmFkaXdyMVhlYU5jVk45NEY1VXc?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxPWFVwN1hfQVhaWm9LZkY0bERYY0JtOVBtR2dSSHV4T1c0eU91TjN6WXAwTHNvZmhnQlpkUENkSGhYT21aNWlBWjM0dXNFSHp5andOeTlKRzhDN3NremU5QzhTdDlRMThvMGZFck02ZnUtRWIybmloSTJPVnktWlVSRWdOZ1c3QWY3bk1GVUN1YWx4aExfRnJ4b2VtNlFia0wtVWNQZE5mcl9Ld2JUT3g5X1FRT1lYSUVpVWc?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxOMzkwNDNBX2JDYk1SOUF2YVlkdEx4U05naHhkV0xLZzNfWmNYd2M1bGVCOU0ySTQwNjVzbFFBTEZNVDMzSENyalpMU2FXMFZEN2YzVTNzT093WExtSlJnald4Ny1PdWtKWS1QMmQ0WVNDOTlPVVJadlg0VERoUXNYcnRjVWJ0N0JsU3BXZ0p3UG5ueG9LZG5nTU1VVzltR3NkWjVtZUtRY095UQ?oc=5
- https://news.google.com/rss/articles/CBMi7wFBVV95cUxOOG1VS2oyRGs5WkYxbmREb0l6WTJ4TTB3cm9lM2VZTVRTOGt3QmpQQ2hoc2ZHV3htd1JPMWFSd0VmWVY3UVRYZzhOLWtuSWU1Ry1ha1NWOGxDcnI2WEJEQXdiZmpMN042Vi11NmZlckRYVUlUdWEwc0hiYnFLdi1lN2pTYlRJWEREY3ByTTJ6bjdXWVJvbDNEVVB0SzhsRWpuNU53NklQeGVRQ2RYUEJQT2dKZDMtQWN0Z3hZem94RzVOdFpQOTNMc0hlR1J3MDVaUmllUDg0b3ZKZWVHWUVmMjRzbzJ5dF9ONVdtY1pvOA?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxQMmRBanZIT29hZVU4TWVSWENzU2NzbkNHNHNPb0dWX0xtLWVPaS1qQ3FEcDQ0ejdCbWhkUDh5YWt5aWFBank3dHhLZXNYTnFqWEpzT0Z3a2dwbGxta2gwak4tNEYzUDBKcnUxSS04MzdDVHNhczBid3BzTDZnTkVXS1JTcm9VTEpaUUp2dnZMOGVlOGh5Yk9MRERSTDBOVUE?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxON0JPdEc2MXNVR1UzZF8tZk00UERCQTF2RnkwU3Q0QTNXcDJ5MmtNeF94dmpoZXVTWFRydkUwb1UySkU5dEtSQ1NweGRVTUN0V2FDQU14QUIzU3Zfa2JZRTlLSks4Zm1LVWxiN1FnTzd4ZXdrZEF1VnhEeWF0LTMtWDZrNTBlSmJ1YUJ4a1dfZXAtOTBJZnJ0Yw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
