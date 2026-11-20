# AMZN Intelligence Report

- ticker: **AMZN**
- Report as_of: **2026-11-19**
- Market data as_of: **2026-11-19**
- Quant sources: https://finance.yahoo.com/quote/AMZN/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AMZN/key-statistics/
- AI analysis snapshot as_of: **2026-11-19**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-20T06:01:54.899701+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 22, 'rule': 6, 'ai': 11, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **7** exact headline/source/date matches; prior report **20261119T054856Z-9eb86811/AMZN** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'low_uncalibrated_model_confidence': 2}
- RSS source audit (metadata only, not article fact-checking): 22 unique headlines; 9 named publishers; 3 exact duplicates; 22 HTTPS source links; largest publisher share 31.82%; oldest publication 2026-11-13

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 257.3700 |
| Return 1D (%) | -3.8732 |
| Return 1W (%) | -3.7653 |
| Return 1M (%) | -1.9356 |
| Return YTD (%) | 11.5025 |
| Return 1Y (%) | 15.5732 |
| Annualized volatility (%) | 34.1611 |
| Beta vs SPY | 1.3148 |
| Max drawdown (%) | -19.6419 |
| Sharpe (rf=0) | 0.5924 |
| Downside deviation (rf=0, %) | 20.9381 |
| Sortino (rf=0) | 0.9665 |
| Historical VaR 95% (1D, %) | 3.0783 |
| Historical ES 95% (1D, %) | 4.0530 |
| Correlation vs SPY | 0.5350 |
| Tracking error vs SPY (%) | 29.1915 |
| P/E (trailing) | 20.81 |
| P/B | 4.53 |
| EV/EBITDA | 16.19 |
| Revenue growth (%) | 12.10 |
| Forward P/E (estimate) | 23.56 |
| Gross margin (%) | 51.37 |
| Operating margin (%) | 13.09 |
| Return on equity (%) | 27.42 |
| Free cash flow yield (%) | -1.25 |
| MA50 | 255.2312 |
| Close vs MA50 (%) | 0.8380 |
| MA200 | 245.0299 |
| Close vs MA200 (%) | 5.0362 |
| RSI (14, Wilder) | 48.9661 |
| MACD (12,26) | 2.2498 |
| MACD signal (9) | 2.2465 |
| MACD histogram | 0.0033 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AMZN': 286, 'SPY': 286}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 257.3700 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -3.8732 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -3.7653 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -1.9356 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 11.5025 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 15.5732 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 34.1611 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 20.9381 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.9665 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.0783 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.0530 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5350 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 29.1915 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.3148 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -19.6419 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.5924 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 23.5556 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 51.3740 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 13.0870 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 27.4160 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: -1.2480 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 20.8060 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 48.9661 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.0033 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 0.8380 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 5.0362 -> Clearly above the moving-average trend level.

## TAILWINDS

### Amazon Stock Moves Higher: What's Going On?
- Summary: Amazon Stock Moves Higher: What's Going On?
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxOd3EzOU9yRkc4NDAwWmxwN0dpeF9DdHJpNFpmN1hfV2poTUZkY21xcW1jNXAyR1BIU3NDZnpPQ0M3Z2NYMG1xeTAzRXpwTUplOTB5SHZ0R2xtNjNmajRrVWxCTVl0ZGpiUEtnS1FRRFpIMUE2dFlYZUo2WXFEVXNkM1JEYU1DdW5vS05YbXdwcW10dWJwS0ltdDVQd0xBLXVfOENXRUdn?oc=5>

### Amazon.com (NASDAQ:AMZN) Stock Jumps 3.8% - Here's Why
- Summary: Amazon.com (NASDAQ:AMZN) Stock Jumps 3.8% - Here's Why
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxNY3FYSHN1WVd5R2I5T0lTUXhrMmhMRVhwZ0FiTEZGTHRmaF92aHF2LUFpLVpWSXpUM2ZKYXdmbWRZUkp1MkV4aDluQzZSNncxTURrcmF2bU8xTWRFNzE2NU15WU1jVkRFY2NWeDFDekVQRjBHdi1tODg4SUtwR1pkajcwVmNjYmVEUFVteUVqOEk5elBpUkt4TjBVVEdFc0dTVm9qQ1lHN0MtQQ?oc=5>

### Amazon makes major investments in renewable energy projects in India (AMZN:NASDAQ)
- Summary: Amazon is investing heavily in renewable energy projects in India, supporting sustainability and reducing operational costs.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxPTkpLSzFzQVZ5V0xHYmhnVE5HSU1fMEZ5SVZjc2ZTLThtWHFfMDI3dWNiNkl5emt2TnhoUVRZd0dzM0ROS2VpWmxpcGw2SC1HQm5CVVNqUUhZRlFjLTFGb0FTN2VKUTMyODd5X3hfVzBjWmxieTB6NjE3c1QwMWVmYU05WnNzR0g3eEctY3RUMENMdERlYVdMUzZERm5wRzVjaDlvMTRxSGljQQ?oc=5>

### AMZN Stock Rebounds Despite UBS Downgrade, as Amazon Anthropic Investment Could Be Worth $150B
- Summary: Amazon stock rebounds amid UBS downgrade; Anthropic investment potentially worth $150B.
- Date: 2026-11-19 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi0AFBVV95cUxNRFE4NV9tYjU4UzVEM1gwRTZhc3lyNlFxN2oycE5pdUY0WUJob1h4aVNUTVp4UkdJNHNvbmtNVVFiSmFiSThRTUkyNHR1dkdnYkxsU0plR3V2M2I3RzJuSFkwOGNxOS15cUhSSmYySWhHVTFmS2hlTkdxQ2xNQWJCX2drYzRsdGQwQ2N6UU5HZnJIMzFBeXVWZUc4T3U5RXVYRnA1TEM5SWU3WVBIQVdkOXJtNWF0ZG5ROGQwZkhRVXp2QThoc3VlR1VBcVdDa09y?oc=5>

### The Amazon Kindle begins its 20th year of upending the bookstore model (AMZN:NASDAQ)
- Summary: Amazon’s Kindle celebrates 20 years, continuing to disrupt traditional bookstores.
- Date: 2026-11-19 | Impact: medium | Horizon: long | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxQMENycjlaSV9FRXRpTkNqM09GYVZKZ3FOQlFNM0xDTGZ2TUJLN0t4R0txOGcybHVOYnJQbXpHa1NUQmp3OFM1Y0kyUWE0MEZjYlphUDRMM1VydTR3WXEzOEFOcFY5QktKTDRLUlNtLTZ2dWJfTTc3WE5MZDExOFlLZ1VxWlkySC1QTlJrY0dFb2ZHVUZvWF9QVVZhYm04VW9lZ192WnpoajBmMEVy?oc=5>

## HEADWINDS

### Amazon.com (NASDAQ:AMZN) Stock Falls 3.9% - Here's What Happened
- Summary: Amazon.com (NASDAQ:AMZN) Stock Falls 3.9% - Here's What Happened
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxOSzU4aVNRUDd2aEJiRHFaRUZ4NHoycXBPUkVmQUtudmFMSkhWT3R3MDhpMHowRUhENmhJSnVJeU4xdTdSNFp3SkJWcGpZVHVTMHFERmNmNWFsVi1UWEdEc2pUTVFxbHA0VnlOSzhqLVJZYy1XdVZDNHZNeWRpYUluN0pRZUpGRVZhYUhxRUtrRWxSZ0ZCUW9Bdzg3ZlBOSFRGRjg3dzVxTTdqRldaQjN0dVFuQll5WFU?oc=5>

### Will Amazon stock avoid deeper losses amid overbought warning and weak momentum?
- Summary: Amazon stock may face deeper losses due to overbought warning and weak momentum.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxOdWVNdkhlSWIxTzZFeU16ZC1MV3NENEtiME1BVDA4WWx4NWRqeG5EaU9KdnlvWnZSV0F4VUV4cG1lWldPMHF5TGF2WW0tOXhsdE8wbU4wVWZhNnJEdlI0TjY5OURGeFBvZ3VBZXJid3ZNeVVvd1R3RkZJcVY1YW5JVWRyLV9VN1d2cE5MNndlaFFSQQ?oc=5>

### New York City legislation could upend Amazon's delivery model (AMZN:NASDAQ)
- Summary: NYC legislation could disrupt Amazon's delivery model.
- Date: 2026-11-19 | Impact: high | Horizon: medium | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxQMm14N0pvX2NlNEJxQW5UZWJqX3pyQVVoNzJZdGpFTG9WeWZUTVNtTnZRZWZ5SkxPUVNMQ2EwM3I5SFllM042QVhXd0c3a3JuM2ozeTVlX2JnTk9mT1VDNkdBVExxZnF2UFRqYjJTUmx5bDRfLWFfM1FEZEQ2UkM5V2R6N19Ibm1TS294Z3M4cFhIVEMwckwxN05qSG9QSkE?oc=5>

### Rocket failure destroys 40 Amazon satellites, threatening broadband rollout (AMZN:NASDAQ)
- Summary: A rocket failure destroyed 40 Amazon satellites, jeopardizing broadband plans.
- Date: 2026-11-15 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxPWDhBeDRCZ21nOExrVzluVTk3dWpYQlE2VGgtSVUyRFdXSUI0VVJybVNQTms5V2czZjNtRE1QZ0xTM2NwUWwyUmNsSS10dm5CVE5PeGJ1QVl2djlXNFI2NVhKN0F6YVVfdEF1aE1lWUw2ZFEyT1B5VWM4WVF6VUVncDVfSGE0bzA2RjZrSjdwX3ZlSDhISVRQT2Vzc3pFZlVKVFNmRDNJaG5vcGxVTjhZX2h3?oc=5>

## CATALYSTS

### Amazon (AMZN) Stock Trades Below Fair Value As Its 82% Run Continues
- Summary: Amazon (AMZN) Stock Trades Below Fair Value As Its 82% Run Continues
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxQUUtfMDhmNWV5dFk3RkdyTDhlTi1NZ2U1QmVMXzBhWmZwWHlGWktLSk1kbUFJUTVEUjYybDFxT2NJMjFRa2lySmw2bkVSdXFtcnpxaEFsbWF1MEhPX3FVLUxFSXAyTmM4LXJwVUVSS29KTWtxejlYYjZVejNGTW9FbXpmUFBzRE53Yi11TnBUVnAyYTBLNllfQ2E2OA?oc=5>

### Amazon.com, Inc. $AMZN Stock Acquired by Virtue Capital Management LLC
- Summary: Amazon.com, Inc. $AMZN Stock Acquired by Virtue Capital Management LLC
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixgFBVV95cUxOb2VZTGRQNTR3Y042NDIxMDB1cVZKOWhMZ2ZFY2p2WEZvVjZlOTZieDkwN185eDJaWFhia1hlSE9rX0RmemQ4ZmhJanNaRGVwVUFQWmV0aXhHZmF2WENiLWR4SVZwOWktWXZYVjc1c1BqdlFyQzBpWDBPWEljRnRSdVZyOUI2aE9kcm10Ymhhc0JhbHhnQUtSMkZ1V1RIVVdUWWd3NWo5UHZ1QXdCTkRoelAxQUIxblI5VmNqLXpGTzduVmt0LVE?oc=5>

### Amazon.com, Inc. $AMZN Stock: Greenleaf Trust Reduces Holdings
- Summary: Amazon.com, Inc. $AMZN Stock: Greenleaf Trust Reduces Holdings
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxPN1doVGpYYU1fR3JrU05FdXZ1OHZ5NEpkWENiM1dFaWhGa05hMktZVkRzR2I0OUpINlA3R216RG9oQlg4SUF0YnZEdGJ3TzdSZi1kYzMwUmVLYi1kNHRWbTNEZGJSeWMwRUdnVjNGMWlSZ1BFVDYxZmFMU2hraDRkZ1RtOVNYQklSVGx0VDFzR0NMXzBKSlJaQl9KOEhBUURGZjl3SkR3dDFsTDUwMnM2Slgza2EwcXFzUUE?oc=5>

### What Could Lift Amazon Stock From Here?
- Summary: Speculative piece on factors that could boost Amazon's stock performance.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.5
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxPdnhpdEhzanE4RkFZb3FsR1hjYl93aktwY3hjV0NCQ1EtQzBBbDRMSzgzYjZoVEdKS2c1ZWU0RTRoMVd5Si1pSlR5R0VaOXQwRVByX1YzdUhLV1djN2ZoSmF1OTAycm5kanF1Y014ZXBSbVp0Q3Nqd0RmWjdJaEFtM3ptUDZsT25temNOTEY3YncxMU1SOHpzSU5fU0JNbjRT?oc=5>

### Anthropic’s New IPO Filing Shows Amazon, Google Will Own Over A Quarter Of The Claude Maker
- Summary: Amazon will own over 25% of Anthropic after its IPO filing, indicating a significant partnership and potential AI collaboration.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxNWnBIQWE0a2JUME11UzNpeTZUa0lqOEg0aFNMT05BV29YVldtdzNISHM1OWtrdHZsYkRHc2xTZmFjekh4dTltVEpROVRsZlFjcW8xR21QZ2t2aXpNcHNpb2QyU0lkdU5aZXV6bFVkdXNES09NRnh2MHJTeER1R2hud3o1UWdkSmR5ZnZoQmpRQjhvQk5nTlZtVnBMS1FGUDA?oc=5>

### Amazon looks to take a bigger bite out of the food delivery market (AMZN:NASDAQ)
- Summary: Amazon plans to expand its food delivery services.
- Date: 2026-11-17 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxPOUpacmFTc2V0a2tyZ1AwUjBtUHlLczh1NDc5WnBvSW5vU1owWVlkTXRVdFlTQlBsWXN5NExwRFluS3hWUzMyT0N4VWNIWUF3aVZZZ0xwSGJsT1hNRGhkSk0wbWQtUy1jeUJ1T2VqdFkwRThUcXUtSUZvSm1TN2J5aXBtbTdFVjRZUEk5T1VlMFdITm5jMFphTzhZdTB6NVRfSUlNRWhYUQ?oc=5>

### Amazon and Alphabet Will Own Over 28% of Anthropic After Its IPO. Here’s What That Means for Their Stocks.
- Summary: Amazon and Alphabet jointly acquire majority stake in Anthropic post-IPO, signaling strategic partnership and potential AI collaboration.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxOYU1Lcy0yRzhtLVRmZ003M0VQVVJTbUF3ZEFXMVItd3JjdElrZVdYalkzWjNsVXNvaDkzcHYtZHBEWnRVREw5T2YzaHZNUEQtRVJEeVVWUlE0WDUwMF9PXy1zS05FMFlaS0Myc3ZCVHFWVmVsYXd0VXBHQl9qOXhXMFFNQm9iaWUtbjl4VW9ZUFg1Y3VnSWIwZHl6c2dscnNUMWhFRklQZGc?oc=5>

## RISKS

### Amazon: The Age Of Inference (And Big E-Commerce Profits) (NASDAQ:AMZN)
- Summary: Amazon's inference tech promises growth but may face execution risk.
- Date: 2026-11-16 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxNQnRLX2xlM3NNZ3ctbTl3OF9OdlRwYktiRHBTeUN1bjZNRG0yTFBYaGw5OTdaVXRHcEVrMWt6WlRJWXpLT05xVEJoSFJnUEgxSDg0R1pmYXFMMWlYX2U2QU5kWlZtTUx0eWpWVjFxSnNaNWhRS0tIWUdOUkRkZk5td2dRanFxR1ZyNklUS2hpUXJKS1hT?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AMZN** | **20.81** | **4.53** | **16.19** | **12.10** | **2,782,977,327,104.00 USD** | **15.57** |
| WMT | 45.67 | 10.19 | 24.52 | 5.90 | 999,969,390,592.00 USD | 26.33 |
| MSFT | 26.01 | 7.87 | 18.33 | 18.80 | 3,700,472,676,352.00 USD | 3.34 |
| GOOGL | 14.24 | 5.08 | 17.55 | 24.70 | 3,352,081,989,632.00 USD | -6.64 |

Peers fetched as_of: 2026-11-19; AMZN reuses existing data (market data as_of: 2026-11-19); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-29
- Next expected earnings: 2027-02-04 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-19

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-30
- Revenue (latest available single quarter): 201,944,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 20,685,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMipgFBVV95cUxOd3EzOU9yRkc4NDAwWmxwN0dpeF9DdHJpNFpmN1hfV2poTUZkY21xcW1jNXAyR1BIU3NDZnpPQ0M3Z2NYMG1xeTAzRXpwTUplOTB5SHZ0R2xtNjNmajRrVWxCTVl0ZGpiUEtnS1FRRFpIMUE2dFlYZUo2WXFEVXNkM1JEYU1DdW5vS05YbXdwcW10dWJwS0ltdDVQd0xBLXVfOENXRUdn?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxOMlZzcndHVHcxM3A0VFVKY2NVZUhMejNRLXJJVjZBV1RiR3o1cXk3c28xcnRNbjAtTl8wUmtsUVFxc1RUZGxtNzVza3Y5cmNoZTF5dExRNUNuWnRSV0RFU1BFaFVxeHd2VHljbW5iUTVQMFR2QmR6VDN0Q1VLazNjZXRwVU81b0M2MHVXY3AydVpXb1FXQTBiMnpQLXBrR1MxQTVXZUJn?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxNY3FYSHN1WVd5R2I5T0lTUXhrMmhMRVhwZ0FiTEZGTHRmaF92aHF2LUFpLVpWSXpUM2ZKYXdmbWRZUkp1MkV4aDluQzZSNncxTURrcmF2bU8xTWRFNzE2NU15WU1jVkRFY2NWeDFDekVQRjBHdi1tODg4SUtwR1pkajcwVmNjYmVEUFVteUVqOEk5elBpUkt4TjBVVEdFc0dTVm9qQ1lHN0MtQQ?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxPTkpLSzFzQVZ5V0xHYmhnVE5HSU1fMEZ5SVZjc2ZTLThtWHFfMDI3dWNiNkl5emt2TnhoUVRZd0dzM0ROS2VpWmxpcGw2SC1HQm5CVVNqUUhZRlFjLTFGb0FTN2VKUTMyODd5X3hfVzBjWmxieTB6NjE3c1QwMWVmYU05WnNzR0g3eEctY3RUMENMdERlYVdMUzZERm5wRzVjaDlvMTRxSGljQQ?oc=5
- https://news.google.com/rss/articles/CBMi0AFBVV95cUxNRFE4NV9tYjU4UzVEM1gwRTZhc3lyNlFxN2oycE5pdUY0WUJob1h4aVNUTVp4UkdJNHNvbmtNVVFiSmFiSThRTUkyNHR1dkdnYkxsU0plR3V2M2I3RzJuSFkwOGNxOS15cUhSSmYySWhHVTFmS2hlTkdxQ2xNQWJCX2drYzRsdGQwQ2N6UU5HZnJIMzFBeXVWZUc4T3U5RXVYRnA1TEM5SWU3WVBIQVdkOXJtNWF0ZG5ROGQwZkhRVXp2QThoc3VlR1VBcVdDa09y?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxQMENycjlaSV9FRXRpTkNqM09GYVZKZ3FOQlFNM0xDTGZ2TUJLN0t4R0txOGcybHVOYnJQbXpHa1NUQmp3OFM1Y0kyUWE0MEZjYlphUDRMM1VydTR3WXEzOEFOcFY5QktKTDRLUlNtLTZ2dWJfTTc3WE5MZDExOFlLZ1VxWlkySC1QTlJrY0dFb2ZHVUZvWF9QVVZhYm04VW9lZ192WnpoajBmMEVy?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxOSzU4aVNRUDd2aEJiRHFaRUZ4NHoycXBPUkVmQUtudmFMSkhWT3R3MDhpMHowRUhENmhJSnVJeU4xdTdSNFp3SkJWcGpZVHVTMHFERmNmNWFsVi1UWEdEc2pUTVFxbHA0VnlOSzhqLVJZYy1XdVZDNHZNeWRpYUluN0pRZUpGRVZhYUhxRUtrRWxSZ0ZCUW9Bdzg3ZlBOSFRGRjg3dzVxTTdqRldaQjN0dVFuQll5WFU?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxOdWVNdkhlSWIxTzZFeU16ZC1MV3NENEtiME1BVDA4WWx4NWRqeG5EaU9KdnlvWnZSV0F4VUV4cG1lWldPMHF5TGF2WW0tOXhsdE8wbU4wVWZhNnJEdlI0TjY5OURGeFBvZ3VBZXJid3ZNeVVvd1R3RkZJcVY1YW5JVWRyLV9VN1d2cE5MNndlaFFSQQ?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxQMm14N0pvX2NlNEJxQW5UZWJqX3pyQVVoNzJZdGpFTG9WeWZUTVNtTnZRZWZ5SkxPUVNMQ2EwM3I5SFllM042QVhXd0c3a3JuM2ozeTVlX2JnTk9mT1VDNkdBVExxZnF2UFRqYjJTUmx5bDRfLWFfM1FEZEQ2UkM5V2R6N19Ibm1TS294Z3M4cFhIVEMwckwxN05qSG9QSkE?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxPWDhBeDRCZ21nOExrVzluVTk3dWpYQlE2VGgtSVUyRFdXSUI0VVJybVNQTms5V2czZjNtRE1QZ0xTM2NwUWwyUmNsSS10dm5CVE5PeGJ1QVl2djlXNFI2NVhKN0F6YVVfdEF1aE1lWUw2ZFEyT1B5VWM4WVF6VUVncDVfSGE0bzA2RjZrSjdwX3ZlSDhISVRQT2Vzc3pFZlVKVFNmRDNJaG5vcGxVTjhZX2h3?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxQUUtfMDhmNWV5dFk3RkdyTDhlTi1NZ2U1QmVMXzBhWmZwWHlGWktLSk1kbUFJUTVEUjYybDFxT2NJMjFRa2lySmw2bkVSdXFtcnpxaEFsbWF1MEhPX3FVLUxFSXAyTmM4LXJwVUVSS29KTWtxejlYYjZVejNGTW9FbXpmUFBzRE53Yi11TnBUVnAyYTBLNllfQ2E2OA?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxOb2VZTGRQNTR3Y042NDIxMDB1cVZKOWhMZ2ZFY2p2WEZvVjZlOTZieDkwN185eDJaWFhia1hlSE9rX0RmemQ4ZmhJanNaRGVwVUFQWmV0aXhHZmF2WENiLWR4SVZwOWktWXZYVjc1c1BqdlFyQzBpWDBPWEljRnRSdVZyOUI2aE9kcm10Ymhhc0JhbHhnQUtSMkZ1V1RIVVdUWWd3NWo5UHZ1QXdCTkRoelAxQUIxblI5VmNqLXpGTzduVmt0LVE?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxPN1doVGpYYU1fR3JrU05FdXZ1OHZ5NEpkWENiM1dFaWhGa05hMktZVkRzR2I0OUpINlA3R216RG9oQlg4SUF0YnZEdGJ3TzdSZi1kYzMwUmVLYi1kNHRWbTNEZGJSeWMwRUdnVjNGMWlSZ1BFVDYxZmFMU2hraDRkZ1RtOVNYQklSVGx0VDFzR0NMXzBKSlJaQl9KOEhBUURGZjl3SkR3dDFsTDUwMnM2Slgza2EwcXFzUUE?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxPdnhpdEhzanE4RkFZb3FsR1hjYl93aktwY3hjV0NCQ1EtQzBBbDRMSzgzYjZoVEdKS2c1ZWU0RTRoMVd5Si1pSlR5R0VaOXQwRVByX1YzdUhLV1djN2ZoSmF1OTAycm5kanF1Y014ZXBSbVp0Q3Nqd0RmWjdJaEFtM3ptUDZsT25temNOTEY3YncxMU1SOHpzSU5fU0JNbjRT?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxNWnBIQWE0a2JUME11UzNpeTZUa0lqOEg0aFNMT05BV29YVldtdzNISHM1OWtrdHZsYkRHc2xTZmFjekh4dTltVEpROVRsZlFjcW8xR21QZ2t2aXpNcHNpb2QyU0lkdU5aZXV6bFVkdXNES09NRnh2MHJTeER1R2hud3o1UWdkSmR5ZnZoQmpRQjhvQk5nTlZtVnBMS1FGUDA?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxPOUpacmFTc2V0a2tyZ1AwUjBtUHlLczh1NDc5WnBvSW5vU1owWVlkTXRVdFlTQlBsWXN5NExwRFluS3hWUzMyT0N4VWNIWUF3aVZZZ0xwSGJsT1hNRGhkSk0wbWQtUy1jeUJ1T2VqdFkwRThUcXUtSUZvSm1TN2J5aXBtbTdFVjRZUEk5T1VlMFdITm5jMFphTzhZdTB6NVRfSUlNRWhYUQ?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxOYU1Lcy0yRzhtLVRmZ003M0VQVVJTbUF3ZEFXMVItd3JjdElrZVdYalkzWjNsVXNvaDkzcHYtZHBEWnRVREw5T2YzaHZNUEQtRVJEeVVWUlE0WDUwMF9PXy1zS05FMFlaS0Myc3ZCVHFWVmVsYXd0VXBHQl9qOXhXMFFNQm9iaWUtbjl4VW9ZUFg1Y3VnSWIwZHl6c2dscnNUMWhFRklQZGc?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxQaV9WVUdzMk5hM0tDU1FaeFB0dkpRenRRaUFFWWdFaVZCVUdpT3hVc3cxeWZfeTlQNjVBVHJjRzdxS1dsclRZeHBIblVhQWkzMEliOU5vUzVFODgtQUI3VHJjVnVVZGd4V1lnNUVvWVdBc0hzUW5wX1JlZ2FMV0hVOXViZEFfTE1WcDFpVE1ySXRrZkVGRk5F?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxNQnRLX2xlM3NNZ3ctbTl3OF9OdlRwYktiRHBTeUN1bjZNRG0yTFBYaGw5OTdaVXRHcEVrMWt6WlRJWXpLT05xVEJoSFJnUEgxSDg0R1pmYXFMMWlYX2U2QU5kWlZtTUx0eWpWVjFxSnNaNWhRS0tIWUdOUkRkZk5td2dRanFxR1ZyNklUS2hpUXJKS1hT?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
