# CSCO Intelligence Report

- ticker: **CSCO**
- Report as_of: **2026-10-25**
- Market data as_of: **2026-10-23**
- Quant sources: https://finance.yahoo.com/quote/CSCO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/CSCO/key-statistics/
- AI analysis snapshot as_of: **2026-10-25**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-26T01:20:16.937102+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 3, 'ai': 11, 'unknown': 0, 'irrelevant': 10})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **0** exact headline/source/date matches; prior report **N/A** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 12 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 16.67%; oldest publication 2026-10-19

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 106.5000 |
| Return 1D (%) | 1.5349 |
| Return 1W (%) | -0.8288 |
| Return 1M (%) | 0.4537 |
| Return YTD (%) | 40.8174 |
| Return 1Y (%) | 54.3641 |
| Annualized volatility (%) | 35.3598 |
| Beta vs SPY | 1.1028 |
| Max drawdown (%) | -18.6996 |
| Sharpe (rf=0) | 1.4103 |
| Downside deviation (rf=0, %) | 23.9362 |
| Sortino (rf=0) | 2.0834 |
| Historical VaR 95% (1D, %) | 2.9026 |
| Historical ES 95% (1D, %) | 4.9273 |
| Correlation vs SPY | 0.3975 |
| Tracking error vs SPY (%) | 32.4721 |
| P/E (trailing) | 31.98 |
| P/B | 8.36 |
| EV/EBITDA | 23.34 |
| Revenue growth (%) | 17.60 |
| Forward P/E (estimate) | 18.94 |
| Gross margin (%) | 64.52 |
| Operating margin (%) | 27.72 |
| Return on equity (%) | 27.32 |
| Free cash flow yield (%) | 2.66 |
| MA50 | 109.9381 |
| Close vs MA50 (%) | -3.1273 |
| MA200 | 99.6344 |
| Close vs MA200 (%) | 6.8908 |
| RSI (14, Wilder) | 42.1330 |
| MACD (12,26) | -1.0589 |
| MACD signal (9) | -0.1628 |
| MACD histogram | -0.8961 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'CSCO': 267, 'SPY': 267}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 106.5000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.5349 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -0.8288 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 0.4537 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 40.8174 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 54.3641 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 35.3598 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 23.9362 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 2.0834 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.9026 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.9273 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.3975 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 32.4721 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.1028 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -18.6996 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.4103 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 18.9433 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 64.5240 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 27.7190 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 27.3190 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.6633 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 31.9820 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 42.1330 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.8961 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -3.1273 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 6.8908 -> Clearly above the moving-average trend level.

## TAILWINDS

### How AI Networking Expansion Will Impact Cisco (CSCO) Stock
- Summary: Cisco's AI networking expansion is expected to positively influence its stock performance by enhancing product offerings and market competitiveness.
- Date: 2026-10-22 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxOQ1B3ZFk3cEEzOXUwUWFkWHZyTVJZTjBSRzBXMHRlenJlak5NT0d2NTI4eURwNFVibDlOVTJUdW9OZG02Z1AyLWpDd0JET3RvMGtsZVRmdGdTTElPNEVCejJEalFJVWFpMlhYNGZJZXNNbEpINVpSRWZKMFVuSUxLVXhiSXNMMS1ramRtVDF0anV5RE4tYl9nVXRPd1dKei1wdHdEdXM0cVVpdUZtb0pNMnZKamZJbEV6c0RtTnF4Y3RDZ9IBxwFBVV95cUxObXYyaXpPVjlFNlNDeW1SQ2VscTVueEN2ajFmZldPVHNKNVBqMWpEWUZ6Z1BXS2hZeWxSaW1HMmV6RXpYZXNPbC16MHBWMWtGU2dQalliZnBrYm8wS3NtY0tqekhCQUNOQkRoWTNFSTl4blpLaVV6T0lHZmJGZW5ubzJ0MlFISUVwN3plWG5hWmlTWFVncXlzUnhsTG5tQWVOYjRWNmNJMXNER29EblVGWVdXZ3BfT2tuQUItUEdJLUpfMXRUU2tR?oc=5>

## HEADWINDS

### CSCO Stock Slips After-Hours Even As AI Equipment Demand Drives Q4 Beat
- Summary: CSCO Stock Slips After-Hours Even As AI Equipment Demand Drives Q4 Beat
- Date: 2026-10-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0AFBVV95cUxPLUpSR2NDbTBTb0p2R0ZCRUFGclBpbVk2Vjdhay1QdWlTTG1NeHdTUExiQjBSVVJSSmszMFlrMkRCdkJJdFNGbGJneWR1Nm9oUUtHblE1alkxYXJNSURKY1RkaERRUmJ6VEtMdFZFSUlScDc0X0JiVkJGSUw3T1ZjaGlkLWxKblBtcmhxUXVpRjNMd0ozdE1fLUZrd3ZQaXhvcWNXWUY3bFpCdFpDLVNIRm1CQ3djVjRkX0JiMmhybmJFc1RtVmJDVjA3XzNLOHdT?oc=5>

### Cisco Systems (NASDAQ:CSCO) Stock Price Down 2.2% - What's Next?
- Summary: Cisco Systems (NASDAQ:CSCO) Stock Price Down 2.2% - What's Next?
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxOeGQ1SWhBNndSeDFMVkd0MnM2Z3Vkb29nUS1MNlJ1aGdRVy1mdTBITWhCNlowdHRoRzI3Sk1NREdjMEItRWtrZmZ2OEd4TUw2em91R0g5TVA3R0R4Y05CWnBoTXp2MG5xMlNsQXJzUEZXdmZsZXZBRW1WMXdGNUNzVzBVQzh1bmZqOGVTX2k4WGtuekRaV3c3aWVkNzc0eW9XaTJkSWRZV2JvMUt5YTJtUlJXbDBpUVk?oc=5>

### Here's Why Cisco Systems (CSCO) Fell More Than Broader Market
- Summary: Cisco's stock decline outpaced the broader market due to specific negative factors affecting investor sentiment and company performance.
- Date: 2026-10-22 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxOd0tuclZqb2tZSGdkdUU3eDM0czVTV2VmZ0JNcUlzOVBKUTNMZ0RIYmpGZEtHUTgxSlVTSU9PQTd6SFA4VGItcUk0RVJPNzRWZnlrNWlzTjYtZVBfZmVNNFhhbmFUMjRVNjlLbmNhclYzbnprLVpSbkhmdzBDZFhRVGFabFMyTU9IaTZGcHFYVFVqbnA3cjJWUw?oc=5>

## CATALYSTS

### Cisco Systems, Inc. $CSCO Shares Acquired by Robeco Schweiz AG
- Summary: Cisco Systems, Inc. $CSCO Shares Acquired by Robeco Schweiz AG
- Date: 2026-10-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxOeGJtNi1HNTVYczhIME1LYURXdmN1dEdJRFlBQmZNUENtVGYxZ1RqMjY5MzJzZ0FoanFCTVRCR1FpWHNIV2FCblVEeE0wYXJDdkJsS2lJTDZJZnRDSjlsTjBjcGRmcjRVRURTUllKdjR3SjNESXB2aWN5b3FueFdlYm5KUGNpb3BVbkJNQlgwSS1jWkVWclFrcFpXOUJ4VEdKYlNTei13NWFFd0dZSGE2SlJKVjlMYzdxTUxHeQ?oc=5>

### Cisco Beat Revenue at 18% Growth and $9.3B AI Orders — So Why Did the Stock Plunge 9% to $112?
- Summary: Cisco reported strong revenue growth and AI orders, yet the stock fell 9%.
- Date: 2026-10-25 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi3AFBVV95cUxObzFNNUtsdDh5Z0ZjZmN0R1lhUFppN0lpaWNQcWp4dDB4Z3ZOQWNSLWhlMTZsWXdaU2trdXpsbzFOc2VOeUdyRXQ3a2dyTGcxQVF0NUw2VXI0SEdBT05SUjZ4XzIzT2s2NDljNVhjVldlODZBbnltOEg0Y2w0OVNabkRralU3S2h1R2h2Y2RDOXlaejBoNjJhVENfaVBNX2lHb2VrSnB4NnllWDNpM3RQZ2ZZNjZjS1hQbFVGUG1JdW9KS0o3bFdia1M3bG1pUnBIQlZRLTFZSU4tRFdt?oc=5>

### Did AI Networking Expansion Just Shift Cisco's (CSCO) Investment Narrative?
- Summary: Cisco's AI networking expansion may alter investor perception, potentially boosting demand for its networking solutions.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxOQW5kYV9YR1ptZTJpOEV4VDhCdXBERFI0TWtCd2oxSGhXTFlnZm5FZktyOFNFUmRuQ0VJYzQ2RTBEX29uRUVzellhV2ZmWld2dEhVS3BxWmd5NnhVZndSUER5ODVXbTJrQnJ5RUpCRUNYQXZScHNTOHB0WFdZaGtpakdSTDZLcTFVd1I3aVZES2RjZ0RsQ3d5Qm1lN1M?oc=5>

### How Much Of Cisco Stock’s Rise Did The Business Earn?
- Summary: Examines how Cisco’s earnings contributed to its recent stock price increase, highlighting financial performance and investor perception.
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxOdHdLRzNuWVpWcEhOa2dBZjc3NW13ek9zSVlpQ19DTWoyTGNHd1ZxRUpVcGVKZGE2TGN5bWVSVUdhTG1IWHhMVFI0N3JJM3JMSmd5Snc1TV9xNjhGYklQT05CbDVqVktnZndYV09aMFBMMEdFaHN6UGU0QmJTdUZZTGxJcUxtS0YxTVNfMkRWdDhCa2NOeDVYQnRUdFF0ckZZbzNObEV1MHk0eWRYQXVRb3RB?oc=5>

### Cisco: Don't Throw In The Towel Just Yet (Earnings Preview) (NASDAQ:CSCO)
- Summary: Cisco anticipates earnings that may exceed expectations, suggesting potential upside.
- Date: 2026-10-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQNDMwU25XTnVZNjVyVTJsZk5IeXpiT01NRkJHdE9Eb3Q2X2xvVnlkMUZWNXF4T0lqYUQ5REhQWE1JcmtzRThBazlRVV84cmF4RmhjY2l1NDdIN09XTzdieGxxcTFKd3BGM2stNlBPdEduNkhSNUpKZDcxQTdrRUR6Q25tTlVsdzRtYTBQMnh0cWhISGZXd1NfdVV0YWY?oc=5>

### Cisco's Dip Yet To Improve Its Overbought AI Story - Initiate Hold (NASDAQ:CSCO)
- Summary: Analyst recommends hold, noting Cisco's dip and overbought AI narrative.
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxQVko2MWlxTl9raDdPSlQtRFd6VDRaVW52Y3I4Nzg3eVVGbmJYeF9oOFFPTmJFQkhYNC1UMERSWTBuNnZUNkFoR3RzRkZ3aWk4eHJfNFFnTUpma0NGTk9FOHJlWjJpQ0M0b2xWRE5XR2JzTm16S2g4bDRNWGdsOF96Z2d5TkZBMU5zQzZfTXZLN09hbEV0c2lLall4N3RtM285UGkzbjhlYw?oc=5>

### Cisco (CSCO) Stock Looks Undervalued Based On Future Cash Flow
- Summary: Analysts suggest Cisco’s stock is undervalued relative to projected cash flows, indicating potential upside for investors.
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxQUjl1bF9NbzFoSlQyX3JFaUV5b29Ja09VRHRvNm4wMnh4WGRfN1IzX0wtM3dtU0JsVXVRZGE2Xzg1cDhKT3h4Snc4eFQzQl9FSzRpVUJpZVlJZjN4U1BrM2IwcUlTZm91SzN5eXVjODJCV3pLdGpnSUFHa0owaUxSbWNVRUJZWkJuZzBTMGdtemlxSE91bnNwQmI0cmpGblNxRmlUMEdLU1plZm91bWZuLXlGM0M0MTZuc1QtTVJKSGhxNnZDcThV0gHMAUFVX3lxTE5WZDNjMzlvQWZ4eHp4ajB5dHN6NG9IWkJNdWRQUGpIUDMteGw1Y3JIRVBzZTA1V2pfX1BTQW9NbG1RVUE2bjNBRXkzR2ZCWUdLenpzRUtVUWJRU2xUR2pMZVhtLXM3Q2s4SzlENUdISVhPbnhNRUFucm9NRU1qYmdkdDFOVV8ybG44azdJVjlEcmJZaVA5MVA5d2hZSXZSaTJVY1VsTDJMb2NxaGM3RmE1MTA4WFdpY1ctdncxZ2tCb3pkeWdzZlFiX2R1Ng?oc=5>

### Cisco Systems, Inc. $CSCO Stock: Atlatl Advisers LLC Boosts Stake
- Summary: Atlatl Advisers LLC increased its stake in Cisco, signaling confidence and potentially supporting the stock price.
- Date: 2026-10-24 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxOMG1yRlJSYlltTUhhWEhHVkFrTnAzbTJWWE5FdElGS1BoUUd5RlpXOUotTm1GUG1veFZ2ejVxYk9nZ1lUTlRoeVotSE9teE84dTkwSnE5ek9jSElmVWE0QnZtcURJLU4zOWp4WXBPWm1VTFAwaExqbVI4cnlJVUVRcDcxVXRhUXdRSEl5WHJIYUdwN3Rpam5qSUdCODRydXlHVXNVdVBQbktRZ25SWUJQVmtUQ0h5UXJldExBcnR3MA?oc=5>

## RISKS

### Wells Fargo (WF), Cisco (CSCO), Marvell (MRVL) join objections to OKX-ICE tokenized stock plans
- Summary: Cisco joined a lawsuit against tokenized stock plans, potentially facing regulatory scrutiny.
- Date: 2026-10-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizAFBVV95cUxNekc1MnU3Uktka3JVcEpxem1xS0UxaGZVQzcwQTVBWHNQd01PUHNJMzdBa3Y4UFB6SkVlRTljOHJzYnZIS045eklhNlFtTDJFd3llSXJBS0x5VFNialdLMm5CVDhSTTBVa1lkcmxab1ZoQVZ0ZUhTZXl5ZWs0T0FFZUxIT0pvcmh1TjRLVUxGdG9Dd1JjQjVYdmRmaEdSdnl0Nk55aWxmMU5uX0NaN1hyU1g5NjJEOXoycGJWRzV1VXE1VGppS3lHOWd1TDc?oc=5>

### Cisco: Fundamental Fair Value, But Here's Where Major Technical Support Appears (Downgrade)
- Summary: Analysts downgrade Cisco, citing technical support concerns that could pressure the stock.
- Date: 2026-10-19 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMixgFBVV95cUxOOTNSa2ZfQjYyU0Q1NUZ1MTE4d2ZFTkZSODFuVDV5MFZiRnJHckk0MGZhYlVxUmVhZ2VsQXBLR2U3TEVkTVFaNlF4d0RmVlBPUTFqNWJRcE9BMWRLdWt6dmZhVEQxTmJkRHc5XzdfZnJQWm9EdFJ5cXZHMThRMXRiU0J6TnNPSzZEV0VobDFYZ2k1T05VMDk0eTh1cHVEdTM1bTQyeHBaYnNxZm9KYTlBazdWdzc0cWNPdnppN1pnQnBHVW0zVGc?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **CSCO** | **31.98** | **8.36** | **23.34** | **17.60** | **419,885,514,752.00 USD** | **54.36** |
| ANET | 58.63 | 14.69 | 43.98 | 37.70 | 217,397,297,152.00 USD | 12.84 |
| FFIV | 36.29 | 6.71 | 26.47 | 10.90 | 25,789,153,280.00 USD | 50.87 |
| HPE | 29.22 | 2.84 | 12.98 | 33.70 | 75,253,981,184.00 USD | 148.87 |

Peers fetched as_of: 2026-10-25; CSCO reuses existing data (market data as_of: 2026-10-23); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-12
- Next expected earnings: 2026-11-12 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-25

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-K
- Filing date: 2026-09-02
- Revenue (latest available single quarter): 12,844,000,000.00 USD; period 2018-04-29/2018-07-28; fiscal year/reporting period 2018/FY
- Net income (latest available single quarter): 3,373,000,000.00 USD; period 2026-01-25/2026-04-25; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/858877/000085887726000132/csco-20260725.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiwgFBVV95cUxOQ1B3ZFk3cEEzOXUwUWFkWHZyTVJZTjBSRzBXMHRlenJlak5NT0d2NTI4eURwNFVibDlOVTJUdW9OZG02Z1AyLWpDd0JET3RvMGtsZVRmdGdTTElPNEVCejJEalFJVWFpMlhYNGZJZXNNbEpINVpSRWZKMFVuSUxLVXhiSXNMMS1ramRtVDF0anV5RE4tYl9nVXRPd1dKei1wdHdEdXM0cVVpdUZtb0pNMnZKamZJbEV6c0RtTnF4Y3RDZ9IBxwFBVV95cUxObXYyaXpPVjlFNlNDeW1SQ2VscTVueEN2ajFmZldPVHNKNVBqMWpEWUZ6Z1BXS2hZeWxSaW1HMmV6RXpYZXNPbC16MHBWMWtGU2dQalliZnBrYm8wS3NtY0tqekhCQUNOQkRoWTNFSTl4blpLaVV6T0lHZmJGZW5ubzJ0MlFISUVwN3plWG5hWmlTWFVncXlzUnhsTG5tQWVOYjRWNmNJMXNER29EblVGWVdXZ3BfT2tuQUItUEdJLUpfMXRUU2tR?oc=5
- https://news.google.com/rss/articles/CBMi0AFBVV95cUxPLUpSR2NDbTBTb0p2R0ZCRUFGclBpbVk2Vjdhay1QdWlTTG1NeHdTUExiQjBSVVJSSmszMFlrMkRCdkJJdFNGbGJneWR1Nm9oUUtHblE1alkxYXJNSURKY1RkaERRUmJ6VEtMdFZFSUlScDc0X0JiVkJGSUw3T1ZjaGlkLWxKblBtcmhxUXVpRjNMd0ozdE1fLUZrd3ZQaXhvcWNXWUY3bFpCdFpDLVNIRm1CQ3djVjRkX0JiMmhybmJFc1RtVmJDVjA3XzNLOHdT?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxOeGQ1SWhBNndSeDFMVkd0MnM2Z3Vkb29nUS1MNlJ1aGdRVy1mdTBITWhCNlowdHRoRzI3Sk1NREdjMEItRWtrZmZ2OEd4TUw2em91R0g5TVA3R0R4Y05CWnBoTXp2MG5xMlNsQXJzUEZXdmZsZXZBRW1WMXdGNUNzVzBVQzh1bmZqOGVTX2k4WGtuekRaV3c3aWVkNzc0eW9XaTJkSWRZV2JvMUt5YTJtUlJXbDBpUVk?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxOd0tuclZqb2tZSGdkdUU3eDM0czVTV2VmZ0JNcUlzOVBKUTNMZ0RIYmpGZEtHUTgxSlVTSU9PQTd6SFA4VGItcUk0RVJPNzRWZnlrNWlzTjYtZVBfZmVNNFhhbmFUMjRVNjlLbmNhclYzbnprLVpSbkhmdzBDZFhRVGFabFMyTU9IaTZGcHFYVFVqbnA3cjJWUw?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxOeGJtNi1HNTVYczhIME1LYURXdmN1dEdJRFlBQmZNUENtVGYxZ1RqMjY5MzJzZ0FoanFCTVRCR1FpWHNIV2FCblVEeE0wYXJDdkJsS2lJTDZJZnRDSjlsTjBjcGRmcjRVRURTUllKdjR3SjNESXB2aWN5b3FueFdlYm5KUGNpb3BVbkJNQlgwSS1jWkVWclFrcFpXOUJ4VEdKYlNTei13NWFFd0dZSGE2SlJKVjlMYzdxTUxHeQ?oc=5
- https://news.google.com/rss/articles/CBMi3AFBVV95cUxObzFNNUtsdDh5Z0ZjZmN0R1lhUFppN0lpaWNQcWp4dDB4Z3ZOQWNSLWhlMTZsWXdaU2trdXpsbzFOc2VOeUdyRXQ3a2dyTGcxQVF0NUw2VXI0SEdBT05SUjZ4XzIzT2s2NDljNVhjVldlODZBbnltOEg0Y2w0OVNabkRralU3S2h1R2h2Y2RDOXlaejBoNjJhVENfaVBNX2lHb2VrSnB4NnllWDNpM3RQZ2ZZNjZjS1hQbFVGUG1JdW9KS0o3bFdia1M3bG1pUnBIQlZRLTFZSU4tRFdt?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxOQW5kYV9YR1ptZTJpOEV4VDhCdXBERFI0TWtCd2oxSGhXTFlnZm5FZktyOFNFUmRuQ0VJYzQ2RTBEX29uRUVzellhV2ZmWld2dEhVS3BxWmd5NnhVZndSUER5ODVXbTJrQnJ5RUpCRUNYQXZScHNTOHB0WFdZaGtpakdSTDZLcTFVd1I3aVZES2RjZ0RsQ3d5Qm1lN1M?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxOdHdLRzNuWVpWcEhOa2dBZjc3NW13ek9zSVlpQ19DTWoyTGNHd1ZxRUpVcGVKZGE2TGN5bWVSVUdhTG1IWHhMVFI0N3JJM3JMSmd5Snc1TV9xNjhGYklQT05CbDVqVktnZndYV09aMFBMMEdFaHN6UGU0QmJTdUZZTGxJcUxtS0YxTVNfMkRWdDhCa2NOeDVYQnRUdFF0ckZZbzNObEV1MHk0eWRYQXVRb3RB?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQNDMwU25XTnVZNjVyVTJsZk5IeXpiT01NRkJHdE9Eb3Q2X2xvVnlkMUZWNXF4T0lqYUQ5REhQWE1JcmtzRThBazlRVV84cmF4RmhjY2l1NDdIN09XTzdieGxxcTFKd3BGM2stNlBPdEduNkhSNUpKZDcxQTdrRUR6Q25tTlVsdzRtYTBQMnh0cWhISGZXd1NfdVV0YWY?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxQVko2MWlxTl9raDdPSlQtRFd6VDRaVW52Y3I4Nzg3eVVGbmJYeF9oOFFPTmJFQkhYNC1UMERSWTBuNnZUNkFoR3RzRkZ3aWk4eHJfNFFnTUpma0NGTk9FOHJlWjJpQ0M0b2xWRE5XR2JzTm16S2g4bDRNWGdsOF96Z2d5TkZBMU5zQzZfTXZLN09hbEV0c2lLall4N3RtM285UGkzbjhlYw?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxQUjl1bF9NbzFoSlQyX3JFaUV5b29Ja09VRHRvNm4wMnh4WGRfN1IzX0wtM3dtU0JsVXVRZGE2Xzg1cDhKT3h4Snc4eFQzQl9FSzRpVUJpZVlJZjN4U1BrM2IwcUlTZm91SzN5eXVjODJCV3pLdGpnSUFHa0owaUxSbWNVRUJZWkJuZzBTMGdtemlxSE91bnNwQmI0cmpGblNxRmlUMEdLU1plZm91bWZuLXlGM0M0MTZuc1QtTVJKSGhxNnZDcThV0gHMAUFVX3lxTE5WZDNjMzlvQWZ4eHp4ajB5dHN6NG9IWkJNdWRQUGpIUDMteGw1Y3JIRVBzZTA1V2pfX1BTQW9NbG1RVUE2bjNBRXkzR2ZCWUdLenpzRUtVUWJRU2xUR2pMZVhtLXM3Q2s4SzlENUdISVhPbnhNRUFucm9NRU1qYmdkdDFOVV8ybG44azdJVjlEcmJZaVA5MVA5d2hZSXZSaTJVY1VsTDJMb2NxaGM3RmE1MTA4WFdpY1ctdncxZ2tCb3pkeWdzZlFiX2R1Ng?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxOMG1yRlJSYlltTUhhWEhHVkFrTnAzbTJWWE5FdElGS1BoUUd5RlpXOUotTm1GUG1veFZ2ejVxYk9nZ1lUTlRoeVotSE9teE84dTkwSnE5ek9jSElmVWE0QnZtcURJLU4zOWp4WXBPWm1VTFAwaExqbVI4cnlJVUVRcDcxVXRhUXdRSEl5WHJIYUdwN3Rpam5qSUdCODRydXlHVXNVdVBQbktRZ25SWUJQVmtUQ0h5UXJldExBcnR3MA?oc=5
- https://news.google.com/rss/articles/CBMizAFBVV95cUxNekc1MnU3Uktka3JVcEpxem1xS0UxaGZVQzcwQTVBWHNQd01PUHNJMzdBa3Y4UFB6SkVlRTljOHJzYnZIS045eklhNlFtTDJFd3llSXJBS0x5VFNialdLMm5CVDhSTTBVa1lkcmxab1ZoQVZ0ZUhTZXl5ZWs0T0FFZUxIT0pvcmh1TjRLVUxGdG9Dd1JjQjVYdmRmaEdSdnl0Nk55aWxmMU5uX0NaN1hyU1g5NjJEOXoycGJWRzV1VXE1VGppS3lHOWd1TDc?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxOOTNSa2ZfQjYyU0Q1NUZ1MTE4d2ZFTkZSODFuVDV5MFZiRnJHckk0MGZhYlVxUmVhZ2VsQXBLR2U3TEVkTVFaNlF4d0RmVlBPUTFqNWJRcE9BMWRLdWt6dmZhVEQxTmJkRHc5XzdfZnJQWm9EdFJ5cXZHMThRMXRiU0J6TnNPSzZEV0VobDFYZ2k1T05VMDk0eTh1cHVEdTM1bTQyeHBaYnNxZm9KYTlBazdWdzc0cWNPdnppN1pnQnBHVW0zVGc?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
