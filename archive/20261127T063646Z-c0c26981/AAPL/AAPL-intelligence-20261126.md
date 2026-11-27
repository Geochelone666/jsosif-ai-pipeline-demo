# AAPL Intelligence Report

- ticker: **AAPL**
- Report as_of: **2026-11-26**
- Market data as_of: **2026-11-25**
- Quant sources: https://finance.yahoo.com/quote/AAPL/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AAPL/key-statistics/
- AI analysis snapshot as_of: **2026-11-26**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-27T06:43:15.867944+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 22, 'rule': 5, 'ai': 11, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **11** exact headline/source/date matches; prior report **20261126T064454Z-dbdd6f45/AAPL** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 22 unique headlines; 12 named publishers; 1 exact duplicates; 22 HTTPS source links; largest publisher share 18.18%; oldest publication 2026-11-19

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 355.5800 |
| Return 1D (%) | 0.4265 |
| Return 1W (%) | 0.8881 |
| Return 1M (%) | 2.3352 |
| Return YTD (%) | 31.2509 |
| Return 1Y (%) | 28.8294 |
| Annualized volatility (%) | 24.9493 |
| Beta vs SPY | 0.5716 |
| Max drawdown (%) | -13.7985 |
| Sharpe (rf=0) | 1.1445 |
| Downside deviation (rf=0, %) | 16.9835 |
| Sortino (rf=0) | 1.6814 |
| Historical VaR 95% (1D, %) | 2.0034 |
| Historical ES 95% (1D, %) | 3.4742 |
| Correlation vs SPY | 0.3421 |
| Tracking error vs SPY (%) | 24.3010 |
| P/E (trailing) | 39.60 |
| P/B | 46.10 |
| EV/EBITDA | 30.35 |
| Revenue growth (%) | 11.70 |
| Forward P/E (estimate) | 33.63 |
| Gross margin (%) | 48.79 |
| Operating margin (%) | 33.01 |
| Return on equity (%) | 142.26 |
| Free cash flow yield (%) | 2.04 |
| MA50 | 342.8382 |
| Close vs MA50 (%) | 3.7166 |
| MA200 | 303.9591 |
| Close vs MA200 (%) | 16.9828 |
| RSI (14, Wilder) | 58.0431 |
| MACD (12,26) | 3.0298 |
| MACD signal (9) | 3.1569 |
| MACD histogram | -0.1271 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AAPL': 290, 'SPY': 290}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 355.5800 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.4265 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 0.8881 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 2.3352 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 31.2509 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 28.8294 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 24.9493 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 16.9835 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.6814 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.0034 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.4742 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.3421 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 24.3010 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.5716 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -13.7985 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.1445 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 33.6318 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 48.7860 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 33.0100 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 142.2570 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.0447 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 39.5969 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 58.0431 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.1271 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 3.7166 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 16.9828 -> Clearly above the moving-average trend level.

## TAILWINDS

### Apple Enters the AI Agent Race as It Takes on OpenAI, Anthropic, and Meta. What That Means for AAPL Stock.
- Summary: Apple launches AI agent initiative, competing with OpenAI, Anthropic, Meta.
- Date: 2026-11-26 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi3wFBVV95cUxQYXdfa3Bna1FYMHFuMy1haFR5VzUwdDBta2xLbzU3UnhnTlZVQ1JETWFKT0ZORGNDeVQyNEF5dHQ0X3loYXNlVktodi1xMHR6eTdUdGVxSnhMS1NJN0lXZnBuQTdWRGVoN3ctYkk0Y0hXSkpfLUhEQXY4N0dxcUpyQkRsYkU4NWhMVDNmMjQ0a0xXdmdCWktWaVhBYlZUd2hSNzBoOWtCTWloa1RscW9KcEdBZms1YUxlRktHM0VveVhYS0VnMDVKaGx2TzA5QkJYeTlUSENUOTV3bjZNTG5F?oc=5>

### Apple Inc. $AAPL Stock: Summit Wealth Group LLC Co. Grows Stake
- Summary: Summit Wealth Group increases stake in Apple.
- Date: 2026-11-26 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxPU0JGZmFHUXlXeWdYU0xHc1JZRVdZbnE0Ym9mcWVNWWRKTWdwQjh1ZmJGMVBnMFVDWE9nb2sxNGJJYVNINnNyNVRNNm9lN0RKNEJxZ3l6Q0xodm90QWlBZXRHZUZhclpEWGkzaWJoNXMzaEFlWjgzVzIxc0dtYkxhSTdJem92ZGpqUWxiX0FoSlZXXy16Zmk4b0MxcXc2bUpkSTBQTkZyY2ltMUU5V2haZUVoVFdERThpNDZjbw?oc=5>

### How Apple Avoided the Stock Market Crash With 31% Gains
- Summary: Apple stock gained 31% during market downturn.
- Date: 2026-11-26 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMib0FVX3lxTE56MDRwbDVnRVZwbGEybFlQZjZLOEdCNGdRMTBhMlhkY0pNLWJaUnFIWEZlQl8yTmw1aU1GS1BZamY2WTM3YUZyX0RDSVNXVXZpcGtDOFVHNS1BVjlIOGIxb2ZMVUxSQk1ETDFzQU01cw?oc=5>

## HEADWINDS

### Apple Stock Defies AI Selloff: Is It the Market's Safe Haven?
- Summary: Apple Stock Defies AI Selloff: Is It the Market's Safe Haven?
- Date: 2026-11-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiaEFVX3lxTE82a01DUHNCbGVoR3dxYWlCa2c3ZXNUdVFkVmV2MkFYWV9kVExUeDhFRWthMUJhOG1qOElLZjAzV3I2SFlwbk5LbFF1ZHpxV2gzSjZyVFo5N3hVc21YSzV1d0F0enFpd0c2?oc=5>

### Apple (AAPL) Stock Could Be 33% Overvalued On Fresh Service Outage Concerns
- Summary: Service outage worries may depress Apple’s valuation, signaling potential short‑term downside.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxPcW1UV2NiYVZ2ZmxTbDc1dVoxblRuVWpUSlFHdWlaRXhzMmFUWFoxRHY2c2hMTEFyNmdrbUwwTHU0YUswM1VDMF9XZGVpbUhEaHRhSEwzdXZxaFFVVlNUWEJhNU5MTXRvY2tVd1FVbldtX0JfYUlyRG94MTh6WnEyWHF6Nl9mRkszMGJ4SW5mOWZDOTBK?oc=5>

### A trust’s proposed sale of 55,000 Apple (AAPL) shares traces back to restricted stock.
- Summary: Trust proposes sale of 55,000 Apple shares.
- Date: 2026-11-25 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxOc20yelR6REZ6dzFqWU9ONDVsN1BIT0RsRk05M1BhVmRpVkRWWEFHVG56Mnl6YTBzLUU5bjhxeWxPYnhuVktlczZKUmhFV0pGSFJqOWZzWXo2MlBkWUIzeE5ib1o4d21PVXg3a2UxTXR1UXk3MGhWRlVOZFktcWxsMGg5Z2tKTTU3ZkRURTZOMA?oc=5>

## CATALYSTS

### Apple Stock Has 3 Things Going for It in 2027. Here’s My Price Target
- Summary: Apple Stock Has 3 Things Going for It in 2027. Here’s My Price Target
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxNd3Q4bDB2UEZPeThmaDdXeHBJNm8wcUU3ZzJmeWFTZTItV3lCeVVqQ1Bpanp6R3Y1SzlYZTN1M05PdGV6SFZBWU5JLWtvdGtfMlBGMHNMa1NwemRheFJPaVRUa09rQ3pJNVlxMGxWYkw0QzlDRXNGeU5jQXRjRHBHQ0toeTYtNTBQM1VOem9XeGNsUkxCUE0tanRpdHVJVDF0S21LcjVZWE9NY1hGRzQxVQ?oc=5>

### Apple Inc. (AAPL) Delivered Strong Results: Why Investors Are Watching Its Next Move Closely
- Summary: Apple Inc. (AAPL) Delivered Strong Results: Why Investors Are Watching Its Next Move Closely
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxPLTlCTmhMLXRPNjhlZnU1Q2Z0V3VwR3FTR0haUlBObWNOWjdWM3luWnhwWWNfNnhxVXlrT1kwMlVpdEYySEFMMkxTbi1sR0Nza19XS2tQUjFkWHQ4V3dzT1VIQTFyVzRPU2RZd2Q1N2hENkxuN09TU3llRWRjMVZCZGNlbzFOXzBJbDZ0QXlQbHZfLUoybUl3N2VDQlU?oc=5>

### Apple Inc. $AAPL Stock Sold by Harold Davidson & Associates Inc.
- Summary: Apple Inc. $AAPL Stock Sold by Harold Davidson & Associates Inc.
- Date: 2026-11-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxPS2xqYWIyVE5xbzZOeUEzRGV3eFVlcjVhTGFVUi15V0haTGZfRUdXRDF6TkhkaTY2YVBKeXhfd2h3RFdXVGgzcTlXZnV3OGRqcEYxeW9MU0UwRnFxNkRjbFFFZEJrd1NqOGRJdEdFeFlORVo4S05HNVNZam1pUXhydHBRNVIyMDhvRldLWkhYN3lKNnRTVEcxLXBDcXFNaDZRdk9qRC1CeVpub1JGaTRQc3RsU3NLYmYxVEhyUQ?oc=5>

### Apple Inc. $AAPL Stock Bought by Gerber Kawasaki Wealth & Investment Management
- Summary: Apple Inc. $AAPL Stock Bought by Gerber Kawasaki Wealth & Investment Management
- Date: 2026-11-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0gFBVV95cUxQMUFXWFNqdEhFdFVBdnNFMzcwU05Tc3dHZ0M2OGtVSC1COXlFNmh0a2p5Zk9YRHNmMVIySnFqTjQzbTZtUFdDUlFBUktrZ0pxT3RzdW1IQ2RiTnhsYjR2SDRZaXo4R1JwSEJvblBNRTZuQzItWWFpNXh0TlRUUnFqNGpZcmxleE1LNTRUMlZQSS1JMmpZV3R0VFpWYkVreC1xcFhJWWdONWhEMUlHMTlydzBocDJQUW9ES2hXYXNQajRQMzE3ZHYyaTJXWE1kWFViZ3c?oc=5>

### Can Wearables & Mac Revenues Add Fresh Momentum to Apple Stock Ahead?
- Summary: Speculation that increased wearables and Mac revenue could boost Apple’s stock performance.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi6AFBVV95cUxPenFLZ1gzQTQxOW1kMXQyeHhxWU5yV2loaFlSQjRWajZGcWtsZXYzQlhseUtHcF9LUUh5ZFhTSkxZWUtIN3I3Rk1oakZJYmpRbGNWUXBmbUZJLXI4Q3dYREdlV01fTjdwT29PM2RhRXVncklOOEU2MVpKZHJDbTlFTzBXT0dSQjJDeDJfbnNQVW5JTG5nUERjR0YxVUp2UW4wMnpYelRrcUNhdGY4Z0xiVEM4TTREeUl1VFJJb3V0ZG82MHQ2aVUwWXBjTVdONWpxVVpEYkVVYjVEUXFxMUo4eDlhVFhPVVpF?oc=5>

### Apple Is Now Worth Over $5 Trillion Without Betting Big on AI Data Centers. AAPL Stock Now Trades Near Wall Street’s Targets.
- Summary: Apple’s market cap surpasses $5 trillion; stock trades near analyst targets, indicating bullish sentiment.
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi-AFBVV95cUxNRXVwb1laS1Btbm1iTjFsMEg3OGRxd2I4MDBheXBhTmpLTnBpLVpFaGZCdmVabEZnS3FWREh5WDAxcW1KVGpOVFB5NzltWnAyakRibjhhckdQM3BpcVRtSTdHckRoY2RtRFdmZG82T3NlY0xkLS1MczU4b29KQXFXVGdXSjNHMUxBT0NoZmRSb0tuYTdCOEZYWWhGRW8xbUVOTlhkZjJFVGhOUEVaQVptUW05eW1UalZBeG9wRUhLVXljWlVFU0JLc0dkVm1aZjM5OHJEWlVuUmFUd1FJNW1Rdi1UdDN5YlRER0JMZnVpaGNvSVUyRUx5ZA?oc=5>

### Is Apple (AAPL) Above Fair Value As ETF Buying Returns?
- Summary: Questioning whether Apple’s valuation exceeds fair value amid ETF buying activity.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxOVkFWM051XzB5b0RCeFhPQm5iUTNIWlZvNFZ2VzUwSnlVQXVzTDBSZkVPUU1ZeDRheTdIa3lBWmwzV0JqWFBpcjFJQjhpSHkwY1V1SEZXQmVaYmJHdmIxcUNnMmxzRDZYWlExQ05JN0ZpSU0xeEItMjFwY0xnMUgzejg2VnRpRkZab0dFUWp5T2hFZk5IMmVj?oc=5>

### AAPL Stock Alert: What to Know as Apple Develops AI Agent to Compete With Muse
- Summary: Apple’s new AI agent launch could boost product portfolio and market share.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxQekFPM3ZncUc5OWU5R3NERDJHalhFbE9WNURJNUNmc3RnelpCTW9OcHNHcXZuTDMxVGtMbWkwUnM3WDBCSHVYalU4dnhzWFY4NW10dGJROGVEOE5KNXNIUjJUY1ltN1A3SHJTZE9XS0ZUQTNUT0c5S1BVUzJGRDlzVlVuZkV4YUNNTHFxZVhmai05QUcwdmc?oc=5>

### Apple: $136 Billion Of Free Cash Flow Without The AI CapEx Bill (NASDAQ:AAPL)
- Summary: Apple reports $136B free cash flow, excluding AI capital expenditures, indicating strong liquidity and potential for future investments.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxPTGhlNjVzYXh4MXk0NlRMNnpKMGhmMDJKYXJ3a1FRbzhFZ08zZzJvN3ZhZGVTN05wWnpILV9lX0M2ZFAyWTFEb3ZpTFJVTVJ4OHRjZklzcS1Xd29nUHlxQVFXUVcwUHRQR2wwRW5oTk1OM2JOTUhLenJ1NjJ6VDkybEhEZi1FSlBkd3pJaDAyZUp0bkFFTDVmbVJ2ejNnaEN1Skw3bQ?oc=5>

### ANT, META Stock Slip After-Hours Amid Reports That Apple Is Working On Its Own AI Agent
- Summary: Apple develops its own AI agent, potentially boosting future capabilities.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi4AFBVV95cUxQeTJ6NFlTUEVrSzlSZ2Q1UVNDakdTR2NkM3JuSHVVbkFfX3BWNnUyTE9pY1MwbTRDdmpndEoxOHRTeVR1TWdZb05PelJPd1FVVzZzMTdLbVNBeldwb2o0UGZTS0t2dUF0UUswZ3ozTWptalJwM3pRQXlDSXJQNjFnRG1IV1BJSWVHZjRBX2x2MUdHVzN1anNaXzhuWVVGbkVUQ3BpN2lya2x5V2diTHNHekNrTV9Ic0xMVUozS1ZhblgxWjkxdHBqYkFON3I5YWdKZXNjS2JHRk1aMW1ta2xuRA?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AAPL** | **39.60** | **46.10** | **30.35** | **11.70** | **5,167,353,167,872.00 USD** | **28.83** |
| MSFT | 25.57 | 7.73 | 18.03 | 18.80 | 3,638,315,450,368.00 USD | 3.56 |
| GOOGL | 14.26 | 5.09 | 17.58 | 24.70 | 3,357,491,331,072.00 USD | -15.34 |
| SONY | 21.26 | 3.08 | 0.30 | 10.30 | 166,046,941,184.00 USD | -0.38 |

Peers fetched as_of: 2026-11-26; AAPL reuses existing data (market data as_of: 2026-11-25); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-02
- Next expected earnings: 2027-01-28 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-26

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-K
- Filing date: 2026-11-03
- Revenue (latest available single quarter): 62,900,000,000.00 USD; period 2018-07-01/2018-09-29; fiscal year/reporting period 2018/FY
- Net income (latest available single quarter): 29,789,000,000.00 USD; period 2026-03-29/2026-06-27; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/320193/000032019326000026/aapl-20260926.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMi3wFBVV95cUxQYXdfa3Bna1FYMHFuMy1haFR5VzUwdDBta2xLbzU3UnhnTlZVQ1JETWFKT0ZORGNDeVQyNEF5dHQ0X3loYXNlVktodi1xMHR6eTdUdGVxSnhMS1NJN0lXZnBuQTdWRGVoN3ctYkk0Y0hXSkpfLUhEQXY4N0dxcUpyQkRsYkU4NWhMVDNmMjQ0a0xXdmdCWktWaVhBYlZUd2hSNzBoOWtCTWloa1RscW9KcEdBZms1YUxlRktHM0VveVhYS0VnMDVKaGx2TzA5QkJYeTlUSENUOTV3bjZNTG5F?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxPU0JGZmFHUXlXeWdYU0xHc1JZRVdZbnE0Ym9mcWVNWWRKTWdwQjh1ZmJGMVBnMFVDWE9nb2sxNGJJYVNINnNyNVRNNm9lN0RKNEJxZ3l6Q0xodm90QWlBZXRHZUZhclpEWGkzaWJoNXMzaEFlWjgzVzIxc0dtYkxhSTdJem92ZGpqUWxiX0FoSlZXXy16Zmk4b0MxcXc2bUpkSTBQTkZyY2ltMUU5V2haZUVoVFdERThpNDZjbw?oc=5
- https://news.google.com/rss/articles/CBMib0FVX3lxTE56MDRwbDVnRVZwbGEybFlQZjZLOEdCNGdRMTBhMlhkY0pNLWJaUnFIWEZlQl8yTmw1aU1GS1BZamY2WTM3YUZyX0RDSVNXVXZpcGtDOFVHNS1BVjlIOGIxb2ZMVUxSQk1ETDFzQU01cw?oc=5
- https://news.google.com/rss/articles/CBMiaEFVX3lxTE82a01DUHNCbGVoR3dxYWlCa2c3ZXNUdVFkVmV2MkFYWV9kVExUeDhFRWthMUJhOG1qOElLZjAzV3I2SFlwbk5LbFF1ZHpxV2gzSjZyVFo5N3hVc21YSzV1d0F0enFpd0c2?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxPcW1UV2NiYVZ2ZmxTbDc1dVoxblRuVWpUSlFHdWlaRXhzMmFUWFoxRHY2c2hMTEFyNmdrbUwwTHU0YUswM1VDMF9XZGVpbUhEaHRhSEwzdXZxaFFVVlNUWEJhNU5MTXRvY2tVd1FVbldtX0JfYUlyRG94MTh6WnEyWHF6Nl9mRkszMGJ4SW5mOWZDOTBK?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxOc20yelR6REZ6dzFqWU9ONDVsN1BIT0RsRk05M1BhVmRpVkRWWEFHVG56Mnl6YTBzLUU5bjhxeWxPYnhuVktlczZKUmhFV0pGSFJqOWZzWXo2MlBkWUIzeE5ib1o4d21PVXg3a2UxTXR1UXk3MGhWRlVOZFktcWxsMGg5Z2tKTTU3ZkRURTZOMA?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxNd3Q4bDB2UEZPeThmaDdXeHBJNm8wcUU3ZzJmeWFTZTItV3lCeVVqQ1Bpanp6R3Y1SzlYZTN1M05PdGV6SFZBWU5JLWtvdGtfMlBGMHNMa1NwemRheFJPaVRUa09rQ3pJNVlxMGxWYkw0QzlDRXNGeU5jQXRjRHBHQ0toeTYtNTBQM1VOem9XeGNsUkxCUE0tanRpdHVJVDF0S21LcjVZWE9NY1hGRzQxVQ?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxPSUhjckIzQThzNXJUVXhqNzRLVUp1eEhsY1p2VDVNTGhOblRmOFJxXzRKV09wZkFhbmF1U3JIaEsxclB4Y0Fwc0RiajhCMGJDanpSbEVZdGg1SlhaNy1VNGxaTWJKU1RnUmdPSFMxdkxSYkFXb2F3azV3TGdlVVhDT1pmQldxVklzTXJiR3E2bVppNkQzeVE?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxPLTlCTmhMLXRPNjhlZnU1Q2Z0V3VwR3FTR0haUlBObWNOWjdWM3luWnhwWWNfNnhxVXlrT1kwMlVpdEYySEFMMkxTbi1sR0Nza19XS2tQUjFkWHQ4V3dzT1VIQTFyVzRPU2RZd2Q1N2hENkxuN09TU3llRWRjMVZCZGNlbzFOXzBJbDZ0QXlQbHZfLUoybUl3N2VDQlU?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxPS2xqYWIyVE5xbzZOeUEzRGV3eFVlcjVhTGFVUi15V0haTGZfRUdXRDF6TkhkaTY2YVBKeXhfd2h3RFdXVGgzcTlXZnV3OGRqcEYxeW9MU0UwRnFxNkRjbFFFZEJrd1NqOGRJdEdFeFlORVo4S05HNVNZam1pUXhydHBRNVIyMDhvRldLWkhYN3lKNnRTVEcxLXBDcXFNaDZRdk9qRC1CeVpub1JGaTRQc3RsU3NLYmYxVEhyUQ?oc=5
- https://news.google.com/rss/articles/CBMi0gFBVV95cUxQMUFXWFNqdEhFdFVBdnNFMzcwU05Tc3dHZ0M2OGtVSC1COXlFNmh0a2p5Zk9YRHNmMVIySnFqTjQzbTZtUFdDUlFBUktrZ0pxT3RzdW1IQ2RiTnhsYjR2SDRZaXo4R1JwSEJvblBNRTZuQzItWWFpNXh0TlRUUnFqNGpZcmxleE1LNTRUMlZQSS1JMmpZV3R0VFpWYkVreC1xcFhJWWdONWhEMUlHMTlydzBocDJQUW9ES2hXYXNQajRQMzE3ZHYyaTJXWE1kWFViZ3c?oc=5
- https://news.google.com/rss/articles/CBMi6AFBVV95cUxPenFLZ1gzQTQxOW1kMXQyeHhxWU5yV2loaFlSQjRWajZGcWtsZXYzQlhseUtHcF9LUUh5ZFhTSkxZWUtIN3I3Rk1oakZJYmpRbGNWUXBmbUZJLXI4Q3dYREdlV01fTjdwT29PM2RhRXVncklOOEU2MVpKZHJDbTlFTzBXT0dSQjJDeDJfbnNQVW5JTG5nUERjR0YxVUp2UW4wMnpYelRrcUNhdGY4Z0xiVEM4TTREeUl1VFJJb3V0ZG82MHQ2aVUwWXBjTVdONWpxVVpEYkVVYjVEUXFxMUo4eDlhVFhPVVpF?oc=5
- https://news.google.com/rss/articles/CBMi-AFBVV95cUxNRXVwb1laS1Btbm1iTjFsMEg3OGRxd2I4MDBheXBhTmpLTnBpLVpFaGZCdmVabEZnS3FWREh5WDAxcW1KVGpOVFB5NzltWnAyakRibjhhckdQM3BpcVRtSTdHckRoY2RtRFdmZG82T3NlY0xkLS1MczU4b29KQXFXVGdXSjNHMUxBT0NoZmRSb0tuYTdCOEZYWWhGRW8xbUVOTlhkZjJFVGhOUEVaQVptUW05eW1UalZBeG9wRUhLVXljWlVFU0JLc0dkVm1aZjM5OHJEWlVuUmFUd1FJNW1Rdi1UdDN5YlRER0JMZnVpaGNvSVUyRUx5ZA?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxOVkFWM051XzB5b0RCeFhPQm5iUTNIWlZvNFZ2VzUwSnlVQXVzTDBSZkVPUU1ZeDRheTdIa3lBWmwzV0JqWFBpcjFJQjhpSHkwY1V1SEZXQmVaYmJHdmIxcUNnMmxzRDZYWlExQ05JN0ZpSU0xeEItMjFwY0xnMUgzejg2VnRpRkZab0dFUWp5T2hFZk5IMmVj?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxQekFPM3ZncUc5OWU5R3NERDJHalhFbE9WNURJNUNmc3RnelpCTW9OcHNHcXZuTDMxVGtMbWkwUnM3WDBCSHVYalU4dnhzWFY4NW10dGJROGVEOE5KNXNIUjJUY1ltN1A3SHJTZE9XS0ZUQTNUT0c5S1BVUzJGRDlzVlVuZkV4YUNNTHFxZVhmai05QUcwdmc?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxPTGhlNjVzYXh4MXk0NlRMNnpKMGhmMDJKYXJ3a1FRbzhFZ08zZzJvN3ZhZGVTN05wWnpILV9lX0M2ZFAyWTFEb3ZpTFJVTVJ4OHRjZklzcS1Xd29nUHlxQVFXUVcwUHRQR2wwRW5oTk1OM2JOTUhLenJ1NjJ6VDkybEhEZi1FSlBkd3pJaDAyZUp0bkFFTDVmbVJ2ejNnaEN1Skw3bQ?oc=5
- https://news.google.com/rss/articles/CBMi4AFBVV95cUxQeTJ6NFlTUEVrSzlSZ2Q1UVNDakdTR2NkM3JuSHVVbkFfX3BWNnUyTE9pY1MwbTRDdmpndEoxOHRTeVR1TWdZb05PelJPd1FVVzZzMTdLbVNBeldwb2o0UGZTS0t2dUF0UUswZ3ozTWptalJwM3pRQXlDSXJQNjFnRG1IV1BJSWVHZjRBX2x2MUdHVzN1anNaXzhuWVVGbkVUQ3BpN2lya2x5V2diTHNHekNrTV9Ic0xMVUozS1ZhblgxWjkxdHBqYkFON3I5YWdKZXNjS2JHRk1aMW1ta2xuRA?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
