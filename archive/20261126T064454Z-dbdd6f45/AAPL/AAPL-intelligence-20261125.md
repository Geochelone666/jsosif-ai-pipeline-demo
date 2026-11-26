# AAPL Intelligence Report

- ticker: **AAPL**
- Report as_of: **2026-11-25**
- Market data as_of: **2026-11-25**
- Quant sources: https://finance.yahoo.com/quote/AAPL/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AAPL/key-statistics/
- AI analysis snapshot as_of: **2026-11-25**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-26T07:03:04.813721+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 8, 'ai': 11, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **6** exact headline/source/date matches; prior report **20261125T065354Z-0b3565c6/AAPL** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **3**; {'low_uncalibrated_model_confidence': 3}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 9 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 37.5%; oldest publication 2026-11-18

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

### Apple Inc. $AAPL Stock Position Raised by Bank Julius Baer & Co. Ltd Zurich
- Summary: Bank Julius Baer increases its Apple holdings, signaling confidence in the company.
- Date: 2026-11-25 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMiywFBVV95cUxOSkZpQ0dDQ0UyZEItc0JFT3dSTHpBYmlHV0lGeUx1aFU2cW9LS3JsOFJPQ0huYkNHMmlBUUIwV3k4MzBfMFJudHp3bDJGUXFmbXUxVUlSNmpTcHRMZk5jMU1MbmswM2kwZjRHd2tOLUs0QW53SkhjMWlJLU1Eekl2UmV2Q21rbFlpVGJIOGt6aHE4SXc3azVPcGVaU25selZUdGQ4cGxKaU1wTHRqY0xOYUplTlFHZ280T0R6dUVHYUdTY0NhTndBN0VzVQ?oc=5>

## HEADWINDS

### Apple (AAPL) Stock Could Be 33% Overvalued On Fresh Service Outage Concerns
- Summary: Service outage worries may depress Apple’s valuation, signaling potential short‑term downside.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxPcW1UV2NiYVZ2ZmxTbDc1dVoxblRuVWpUSlFHdWlaRXhzMmFUWFoxRHY2c2hMTEFyNmdrbUwwTHU0YUswM1VDMF9XZGVpbUhEaHRhSEwzdXZxaFFVVlNUWEJhNU5MTXRvY2tVd1FVbldtX0JfYUlyRG94MTh6WnEyWHF6Nl9mRkszMGJ4SW5mOWZDOTBK?oc=5>

### AAPL Stock Alert: Samsung Could Win a Bigger Apple Memory Deal
- Summary: Samsung may secure a larger memory deal, posing a competitive threat to Apple.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxQUG1OQlUtTVFmOHM1eXZOOHVhWDlSaGJzcGhkQ2JWUExCbGNmalR6Z1ZoR1lQQjZ3cnY5elc2dU9RbmF2YjF1UkhPc3o0d0FmQ3NvRGp3RE5pMWVsOW1uZzNjakFaR3J3ZnNsVkdMb29BMUs4R3M0YlpxT3VwSGExWk9JOVZFbFM1NVFOQm5qTkZqX0VMQUc5SFZkWE85VV9GVENSWXJ3Nm5YTXREY2RYRVJuRk90eDRVLTNlYmt3?oc=5>

### Apple Inc. $AAPL Stock: Trek Financial LLC Trims Position
- Summary: Trek Financial reduces its Apple stake, indicating potential concerns.
- Date: 2026-11-25 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxQMURLZmdNNVVjcW8yRzl0N1A5WFpfbGVNdm5sQzVHNkw0TmMwY1lEQXUwUXpJUkZLZWU3dTFtcnkwel9Jc3lHRTdRMC03T0RleDBONXFycmVyTW9wcXQ0N1ZteXRSU2VMV1E0R1R0Zk4ybk5CR1R6TFRSRmxmSk5vQUZuMnlYdjAxbUljSU1BTlhYX1c1ZkdWanpjMWMyV2VZWWRuc2VnX0VFSFFtS2VJblJaRUNVdw?oc=5>

### Apple Inc. $AAPL Stock Holdings Cut by MeadowBrook Investment Advisors LLC
- Summary: MeadowBrook cuts Apple holdings, reflecting possible doubts.
- Date: 2026-11-25 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMizgFBVV95cUxQWENxVXkzVUxNYlBXWjkxbWVBRktNQWwwTHJKT0x3OHVMdEFxZGNiTnV1S1R3eDlxcDhlZF9yRHRySUp0cWVMWS1Bcm5qWWY3M0YyTm5KaFFOZWV2dGx3ZEJZQ1VMTjEwZTZwU2U2cm1YVC10X29STFNjbmxScU5DRVpCeXhwbDA0amRfTTdNcmctY3FhbGp4U19hd3B0d09ZNWtJaS1BV3p1eFR3VGdYUFp0Vm1RdFJTcDZfU3FaME1jQkw1THlqMmJURU1Qdw?oc=5>

## CATALYSTS

### Apple Stock Has 3 Things Going for It in 2027. Here’s My Price Target
- Summary: Apple Stock Has 3 Things Going for It in 2027. Here’s My Price Target
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxPSUhjckIzQThzNXJUVXhqNzRLVUp1eEhsY1p2VDVNTGhOblRmOFJxXzRKV09wZkFhbmF1U3JIaEsxclB4Y0Fwc0RiajhCMGJDanpSbEVZdGg1SlhaNy1VNGxaTWJKU1RnUmdPSFMxdkxSYkFXb2F3azV3TGdlVVhDT1pmQldxVklzTXJiR3E2bVppNkQzeVE?oc=5>

### Apple Inc. (AAPL) Delivered Strong Results: Why Investors Are Watching Its Next Move Closely
- Summary: Apple Inc. (AAPL) Delivered Strong Results: Why Investors Are Watching Its Next Move Closely
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxPLTlCTmhMLXRPNjhlZnU1Q2Z0V3VwR3FTR0haUlBObWNOWjdWM3luWnhwWWNfNnhxVXlrT1kwMlVpdEYySEFMMkxTbi1sR0Nza19XS2tQUjFkWHQ4V3dzT1VIQTFyVzRPU2RZd2Q1N2hENkxuN09TU3llRWRjMVZCZGNlbzFOXzBJbDZ0QXlQbHZfLUoybUl3N2VDQlU?oc=5>

### Apple Nears a Rare Long-Term DRAM Supply Deal With Samsung Electronics. What This Means for AAPL Stock.
- Summary: Apple Nears a Rare Long-Term DRAM Supply Deal With Samsung Electronics. What This Means for AAPL Stock.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxQZTAzU2dvbVdZTzN2Smttc1pjc3lsSW5qWTdldDFETUFxNmx4Y2Z1RkZSNG5EcXR0bFlueDdLY2Y4cWxfdGxiYktmeWVDODhnclQ5eEpWZVZRVHlJZjhkalNMVlk1UUpKaW9IS3NRN3RVcnF1MHhEbnVaZWdQaThJRjdud3VSSGkxREdfWHVTelZxSGdXTXc?oc=5>

### Apple Inc. $AAPL Stock Purchased by One Way Holdings LLC
- Summary: Apple Inc. $AAPL Stock Purchased by One Way Holdings LLC
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxPbmlUcHp3RmVRODJuRVBwX2VIeWhyOTJuazNWSjF4V0UyNUNMcmVWNTJXT1IzRlEtUm5xNW1ycnEwc3RXN2hzQXhpWmp3bV9zZ0xRb2xKa2l6MnVua0pvUTV3aHdpOUpmTmg1UGxxUnR6MEZjRnkxTWV3WUE4Ul9oQkJtTDF3ckJVM0FWVDdQanVsVU91RnhzT184UWx3UlMtVkJiOGJqeFJUZHVJVEg3aWlRUVNwdw?oc=5>

### Apple Inc. $AAPL Stock: Greenleaf Trust Reduces Stake
- Summary: Apple Inc. $AAPL Stock: Greenleaf Trust Reduces Stake
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxPNF9oS1JPeE8yTDVTNVpFQk9JRzY5bHgwMHZCLUJNU080VHNuSU15RkluWVJtbVNuMkNldlZMVnZ4UWJPX3JGRWxlbDZRMXdUOVZuTi1hVy1OdEN6WEpQQ2hNbWJ5V0piQ21KVy1wZVd3d1RmZXNnNnVjdHJIdkQ1cmE4TnFrdkxBS2ItMzF4LUx2NlZQdWxiVnFEdml2VWxWMHg0X1UwbHFKUE1DdXpObA?oc=5>

### Apple Inc. $AAPL Stock: Welch Group LLC Reduces Stake
- Summary: Apple Inc. $AAPL Stock: Welch Group LLC Reduces Stake
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxOYVdnNTNMMGw2R1JZSjJFTEE3MWU5emIxMnhNOG1ycE92bE83YlNmb2FjZDN4bDU1allWQ2tYUndkamtOamMyWUFQNFN3U3RlbTJMR2llb3JmRWJhN1Ria0lqU2lPMnd6UW1mOVcyV2xRalJWM2Q4cmZhUXpKeDJsZy1sQXA0a1RwcjQ0RC1fVFlwX202dU9tMkFQazBzNG9qZFFDTFpmb0tyT1lfMGh0bA?oc=5>

### Apple Inc. $AAPL Stock Acquired by Dala Group LLC
- Summary: Apple Inc. $AAPL Stock Acquired by Dala Group LLC
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxPZi05TDV3clE2TFBGZzQ3SmNwMlVKbWtWVlM0Qm40ZmRxT1N1MUF1a1VXYUtzNDVWY2pMdVUzaHljZGJOcEdjRl9zaFFnYlJzX28zeWxqZ01QdEhNVTBqWFlwWnFqMGVtZlNQTUgtOE9TLWNMYjk3OFlPc0xSVFZHd0xkN2tPSXo5U1NZVDZsWjhhUVo2Z1ZyVUtGNGU2QjlZWTlsekdzelRwSjVU?oc=5>

### Apple Inc. $AAPL Stock Bought by Investment Partners LTD.
- Summary: Apple Inc. $AAPL Stock Bought by Investment Partners LTD.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxNV0MyNHFRQXdJLXFlX0p2SGxBYnJvM3hueDNPV1Vha0tTZzhIbUNldnJPZUN6cUxHa2hnN29QbldsMWtMTlVYSVVHczkzNGM1Q1pWN1FaQXNTeDZ2TVNlckIxR3gyTDJJNzA2Skd4czNJZGFFaGNGRUdDdlczR3pGTk5XUi11dFM1bUJ6U1RvM1hSVm9mMHhQNWdURDctSzg5VjRvS001dXQwM3hjSjY3S3h0OEpldw?oc=5>

### Apple Is Now Worth Over $5 Trillion Without Betting Big on AI Data Centers. AAPL Stock Now Trades Near Wall Street’s Targets.
- Summary: Apple’s market cap surpasses $5 trillion; stock trades near analyst targets, indicating bullish sentiment.
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi-AFBVV95cUxNRXVwb1laS1Btbm1iTjFsMEg3OGRxd2I4MDBheXBhTmpLTnBpLVpFaGZCdmVabEZnS3FWREh5WDAxcW1KVGpOVFB5NzltWnAyakRibjhhckdQM3BpcVRtSTdHckRoY2RtRFdmZG82T3NlY0xkLS1MczU4b29KQXFXVGdXSjNHMUxBT0NoZmRSb0tuYTdCOEZYWWhGRW8xbUVOTlhkZjJFVGhOUEVaQVptUW05eW1UalZBeG9wRUhLVXljWlVFU0JLc0dkVm1aZjM5OHJEWlVuUmFUd1FJNW1Rdi1UdDN5YlRER0JMZnVpaGNvSVUyRUx5ZA?oc=5>

### AAPL Stock Alert: What to Know as Apple Develops AI Agent to Compete With Muse
- Summary: Apple’s new AI agent launch could boost product portfolio and market share.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxQekFPM3ZncUc5OWU5R3NERDJHalhFbE9WNURJNUNmc3RnelpCTW9OcHNHcXZuTDMxVGtMbWkwUnM3WDBCSHVYalU4dnhzWFY4NW10dGJROGVEOE5KNXNIUjJUY1ltN1A3SHJTZE9XS0ZUQTNUT0c5S1BVUzJGRDlzVlVuZkV4YUNNTHFxZVhmai05QUcwdmc?oc=5>

### Can Wearables & Mac Revenues Add Fresh Momentum to Apple Stock Ahead?
- Summary: Speculation that increased wearables and Mac revenue could boost Apple’s stock performance.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi6AFBVV95cUxPenFLZ1gzQTQxOW1kMXQyeHhxWU5yV2loaFlSQjRWajZGcWtsZXYzQlhseUtHcF9LUUh5ZFhTSkxZWUtIN3I3Rk1oakZJYmpRbGNWUXBmbUZJLXI4Q3dYREdlV01fTjdwT29PM2RhRXVncklOOEU2MVpKZHJDbTlFTzBXT0dSQjJDeDJfbnNQVW5JTG5nUERjR0YxVUp2UW4wMnpYelRrcUNhdGY4Z0xiVEM4TTREeUl1VFJJb3V0ZG82MHQ2aVUwWXBjTVdONWpxVVpEYkVVYjVEUXFxMUo4eDlhVFhPVVpF?oc=5>

### Is Apple (AAPL) Above Fair Value As ETF Buying Returns?
- Summary: Questioning whether Apple’s valuation exceeds fair value amid ETF buying activity.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxOVkFWM051XzB5b0RCeFhPQm5iUTNIWlZvNFZ2VzUwSnlVQXVzTDBSZkVPUU1ZeDRheTdIa3lBWmwzV0JqWFBpcjFJQjhpSHkwY1V1SEZXQmVaYmJHdmIxcUNnMmxzRDZYWlExQ05JN0ZpSU0xeEItMjFwY0xnMUgzejg2VnRpRkZab0dFUWp5T2hFZk5IMmVj?oc=5>

### ANT, META Stock Slip After-Hours Amid Reports That Apple Is Working On Its Own AI Agent
- Summary: Apple develops its own AI agent, potentially boosting future capabilities.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi4AFBVV95cUxQeTJ6NFlTUEVrSzlSZ2Q1UVNDakdTR2NkM3JuSHVVbkFfX3BWNnUyTE9pY1MwbTRDdmpndEoxOHRTeVR1TWdZb05PelJPd1FVVzZzMTdLbVNBeldwb2o0UGZTS0t2dUF0UUswZ3ozTWptalJwM3pRQXlDSXJQNjFnRG1IV1BJSWVHZjRBX2x2MUdHVzN1anNaXzhuWVVGbkVUQ3BpN2lya2x5V2diTHNHekNrTV9Ic0xMVUozS1ZhblgxWjkxdHBqYkFON3I5YWdKZXNjS2JHRk1aMW1ta2xuRA?oc=5>

### Apple: $136 Billion Of Free Cash Flow Without The AI CapEx Bill (NASDAQ:AAPL)
- Summary: Apple reports $136B free cash flow, excluding AI capital expenditures, indicating strong liquidity and potential for future investments.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxPTGhlNjVzYXh4MXk0NlRMNnpKMGhmMDJKYXJ3a1FRbzhFZ08zZzJvN3ZhZGVTN05wWnpILV9lX0M2ZFAyWTFEb3ZpTFJVTVJ4OHRjZklzcS1Xd29nUHlxQVFXUVcwUHRQR2wwRW5oTk1OM2JOTUhLenJ1NjJ6VDkybEhEZi1FSlBkd3pJaDAyZUp0bkFFTDVmbVJ2ejNnaEN1Skw3bQ?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AAPL** | **39.60** | **46.10** | **30.35** | **11.70** | **5,167,353,167,872.00 USD** | **28.83** |
| MSFT | 25.57 | 7.73 | 18.03 | 18.80 | 3,638,315,450,368.00 USD | 3.56 |
| GOOGL | 14.26 | 5.09 | 17.58 | 24.70 | 3,357,491,331,072.00 USD | -15.34 |
| SONY | 21.26 | 3.08 | 0.30 | 10.30 | 166,046,941,184.00 USD | -0.38 |

Peers fetched as_of: 2026-11-25; AAPL reuses existing data (market data as_of: 2026-11-25); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-02
- Next expected earnings: 2027-01-28 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-25

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

- https://news.google.com/rss/articles/CBMiywFBVV95cUxOSkZpQ0dDQ0UyZEItc0JFT3dSTHpBYmlHV0lGeUx1aFU2cW9LS3JsOFJPQ0huYkNHMmlBUUIwV3k4MzBfMFJudHp3bDJGUXFmbXUxVUlSNmpTcHRMZk5jMU1MbmswM2kwZjRHd2tOLUs0QW53SkhjMWlJLU1Eekl2UmV2Q21rbFlpVGJIOGt6aHE4SXc3azVPcGVaU25selZUdGQ4cGxKaU1wTHRqY0xOYUplTlFHZ280T0R6dUVHYUdTY0NhTndBN0VzVQ?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxPcW1UV2NiYVZ2ZmxTbDc1dVoxblRuVWpUSlFHdWlaRXhzMmFUWFoxRHY2c2hMTEFyNmdrbUwwTHU0YUswM1VDMF9XZGVpbUhEaHRhSEwzdXZxaFFVVlNUWEJhNU5MTXRvY2tVd1FVbldtX0JfYUlyRG94MTh6WnEyWHF6Nl9mRkszMGJ4SW5mOWZDOTBK?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxQUG1OQlUtTVFmOHM1eXZOOHVhWDlSaGJzcGhkQ2JWUExCbGNmalR6Z1ZoR1lQQjZ3cnY5elc2dU9RbmF2YjF1UkhPc3o0d0FmQ3NvRGp3RE5pMWVsOW1uZzNjakFaR3J3ZnNsVkdMb29BMUs4R3M0YlpxT3VwSGExWk9JOVZFbFM1NVFOQm5qTkZqX0VMQUc5SFZkWE85VV9GVENSWXJ3Nm5YTXREY2RYRVJuRk90eDRVLTNlYmt3?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxQMURLZmdNNVVjcW8yRzl0N1A5WFpfbGVNdm5sQzVHNkw0TmMwY1lEQXUwUXpJUkZLZWU3dTFtcnkwel9Jc3lHRTdRMC03T0RleDBONXFycmVyTW9wcXQ0N1ZteXRSU2VMV1E0R1R0Zk4ybk5CR1R6TFRSRmxmSk5vQUZuMnlYdjAxbUljSU1BTlhYX1c1ZkdWanpjMWMyV2VZWWRuc2VnX0VFSFFtS2VJblJaRUNVdw?oc=5
- https://news.google.com/rss/articles/CBMizgFBVV95cUxQWENxVXkzVUxNYlBXWjkxbWVBRktNQWwwTHJKT0x3OHVMdEFxZGNiTnV1S1R3eDlxcDhlZF9yRHRySUp0cWVMWS1Bcm5qWWY3M0YyTm5KaFFOZWV2dGx3ZEJZQ1VMTjEwZTZwU2U2cm1YVC10X29STFNjbmxScU5DRVpCeXhwbDA0amRfTTdNcmctY3FhbGp4U19hd3B0d09ZNWtJaS1BV3p1eFR3VGdYUFp0Vm1RdFJTcDZfU3FaME1jQkw1THlqMmJURU1Qdw?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxPSUhjckIzQThzNXJUVXhqNzRLVUp1eEhsY1p2VDVNTGhOblRmOFJxXzRKV09wZkFhbmF1U3JIaEsxclB4Y0Fwc0RiajhCMGJDanpSbEVZdGg1SlhaNy1VNGxaTWJKU1RnUmdPSFMxdkxSYkFXb2F3azV3TGdlVVhDT1pmQldxVklzTXJiR3E2bVppNkQzeVE?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxNd3Q4bDB2UEZPeThmaDdXeHBJNm8wcUU3ZzJmeWFTZTItV3lCeVVqQ1Bpanp6R3Y1SzlYZTN1M05PdGV6SFZBWU5JLWtvdGtfMlBGMHNMa1NwemRheFJPaVRUa09rQ3pJNVlxMGxWYkw0QzlDRXNGeU5jQXRjRHBHQ0toeTYtNTBQM1VOem9XeGNsUkxCUE0tanRpdHVJVDF0S21LcjVZWE9NY1hGRzQxVQ?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxPLTlCTmhMLXRPNjhlZnU1Q2Z0V3VwR3FTR0haUlBObWNOWjdWM3luWnhwWWNfNnhxVXlrT1kwMlVpdEYySEFMMkxTbi1sR0Nza19XS2tQUjFkWHQ4V3dzT1VIQTFyVzRPU2RZd2Q1N2hENkxuN09TU3llRWRjMVZCZGNlbzFOXzBJbDZ0QXlQbHZfLUoybUl3N2VDQlU?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxQZTAzU2dvbVdZTzN2Smttc1pjc3lsSW5qWTdldDFETUFxNmx4Y2Z1RkZSNG5EcXR0bFlueDdLY2Y4cWxfdGxiYktmeWVDODhnclQ5eEpWZVZRVHlJZjhkalNMVlk1UUpKaW9IS3NRN3RVcnF1MHhEbnVaZWdQaThJRjdud3VSSGkxREdfWHVTelZxSGdXTXc?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxPbmlUcHp3RmVRODJuRVBwX2VIeWhyOTJuazNWSjF4V0UyNUNMcmVWNTJXT1IzRlEtUm5xNW1ycnEwc3RXN2hzQXhpWmp3bV9zZ0xRb2xKa2l6MnVua0pvUTV3aHdpOUpmTmg1UGxxUnR6MEZjRnkxTWV3WUE4Ul9oQkJtTDF3ckJVM0FWVDdQanVsVU91RnhzT184UWx3UlMtVkJiOGJqeFJUZHVJVEg3aWlRUVNwdw?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxPNF9oS1JPeE8yTDVTNVpFQk9JRzY5bHgwMHZCLUJNU080VHNuSU15RkluWVJtbVNuMkNldlZMVnZ4UWJPX3JGRWxlbDZRMXdUOVZuTi1hVy1OdEN6WEpQQ2hNbWJ5V0piQ21KVy1wZVd3d1RmZXNnNnVjdHJIdkQ1cmE4TnFrdkxBS2ItMzF4LUx2NlZQdWxiVnFEdml2VWxWMHg0X1UwbHFKUE1DdXpObA?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxOYVdnNTNMMGw2R1JZSjJFTEE3MWU5emIxMnhNOG1ycE92bE83YlNmb2FjZDN4bDU1allWQ2tYUndkamtOamMyWUFQNFN3U3RlbTJMR2llb3JmRWJhN1Ria0lqU2lPMnd6UW1mOVcyV2xRalJWM2Q4cmZhUXpKeDJsZy1sQXA0a1RwcjQ0RC1fVFlwX202dU9tMkFQazBzNG9qZFFDTFpmb0tyT1lfMGh0bA?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxPZi05TDV3clE2TFBGZzQ3SmNwMlVKbWtWVlM0Qm40ZmRxT1N1MUF1a1VXYUtzNDVWY2pMdVUzaHljZGJOcEdjRl9zaFFnYlJzX28zeWxqZ01QdEhNVTBqWFlwWnFqMGVtZlNQTUgtOE9TLWNMYjk3OFlPc0xSVFZHd0xkN2tPSXo5U1NZVDZsWjhhUVo2Z1ZyVUtGNGU2QjlZWTlsekdzelRwSjVU?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxNV0MyNHFRQXdJLXFlX0p2SGxBYnJvM3hueDNPV1Vha0tTZzhIbUNldnJPZUN6cUxHa2hnN29QbldsMWtMTlVYSVVHczkzNGM1Q1pWN1FaQXNTeDZ2TVNlckIxR3gyTDJJNzA2Skd4czNJZGFFaGNGRUdDdlczR3pGTk5XUi11dFM1bUJ6U1RvM1hSVm9mMHhQNWdURDctSzg5VjRvS001dXQwM3hjSjY3S3h0OEpldw?oc=5
- https://news.google.com/rss/articles/CBMi-AFBVV95cUxNRXVwb1laS1Btbm1iTjFsMEg3OGRxd2I4MDBheXBhTmpLTnBpLVpFaGZCdmVabEZnS3FWREh5WDAxcW1KVGpOVFB5NzltWnAyakRibjhhckdQM3BpcVRtSTdHckRoY2RtRFdmZG82T3NlY0xkLS1MczU4b29KQXFXVGdXSjNHMUxBT0NoZmRSb0tuYTdCOEZYWWhGRW8xbUVOTlhkZjJFVGhOUEVaQVptUW05eW1UalZBeG9wRUhLVXljWlVFU0JLc0dkVm1aZjM5OHJEWlVuUmFUd1FJNW1Rdi1UdDN5YlRER0JMZnVpaGNvSVUyRUx5ZA?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxQekFPM3ZncUc5OWU5R3NERDJHalhFbE9WNURJNUNmc3RnelpCTW9OcHNHcXZuTDMxVGtMbWkwUnM3WDBCSHVYalU4dnhzWFY4NW10dGJROGVEOE5KNXNIUjJUY1ltN1A3SHJTZE9XS0ZUQTNUT0c5S1BVUzJGRDlzVlVuZkV4YUNNTHFxZVhmai05QUcwdmc?oc=5
- https://news.google.com/rss/articles/CBMi6AFBVV95cUxPenFLZ1gzQTQxOW1kMXQyeHhxWU5yV2loaFlSQjRWajZGcWtsZXYzQlhseUtHcF9LUUh5ZFhTSkxZWUtIN3I3Rk1oakZJYmpRbGNWUXBmbUZJLXI4Q3dYREdlV01fTjdwT29PM2RhRXVncklOOEU2MVpKZHJDbTlFTzBXT0dSQjJDeDJfbnNQVW5JTG5nUERjR0YxVUp2UW4wMnpYelRrcUNhdGY4Z0xiVEM4TTREeUl1VFJJb3V0ZG82MHQ2aVUwWXBjTVdONWpxVVpEYkVVYjVEUXFxMUo4eDlhVFhPVVpF?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxOVkFWM051XzB5b0RCeFhPQm5iUTNIWlZvNFZ2VzUwSnlVQXVzTDBSZkVPUU1ZeDRheTdIa3lBWmwzV0JqWFBpcjFJQjhpSHkwY1V1SEZXQmVaYmJHdmIxcUNnMmxzRDZYWlExQ05JN0ZpSU0xeEItMjFwY0xnMUgzejg2VnRpRkZab0dFUWp5T2hFZk5IMmVj?oc=5
- https://news.google.com/rss/articles/CBMi4AFBVV95cUxQeTJ6NFlTUEVrSzlSZ2Q1UVNDakdTR2NkM3JuSHVVbkFfX3BWNnUyTE9pY1MwbTRDdmpndEoxOHRTeVR1TWdZb05PelJPd1FVVzZzMTdLbVNBeldwb2o0UGZTS0t2dUF0UUswZ3ozTWptalJwM3pRQXlDSXJQNjFnRG1IV1BJSWVHZjRBX2x2MUdHVzN1anNaXzhuWVVGbkVUQ3BpN2lya2x5V2diTHNHekNrTV9Ic0xMVUozS1ZhblgxWjkxdHBqYkFON3I5YWdKZXNjS2JHRk1aMW1ta2xuRA?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxPTGhlNjVzYXh4MXk0NlRMNnpKMGhmMDJKYXJ3a1FRbzhFZ08zZzJvN3ZhZGVTN05wWnpILV9lX0M2ZFAyWTFEb3ZpTFJVTVJ4OHRjZklzcS1Xd29nUHlxQVFXUVcwUHRQR2wwRW5oTk1OM2JOTUhLenJ1NjJ6VDkybEhEZi1FSlBkd3pJaDAyZUp0bkFFTDVmbVJ2ejNnaEN1Skw3bQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
