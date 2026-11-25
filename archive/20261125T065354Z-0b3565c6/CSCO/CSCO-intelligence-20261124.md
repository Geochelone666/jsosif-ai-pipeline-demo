# CSCO Intelligence Report

- ticker: **CSCO**
- Report as_of: **2026-11-24**
- Market data as_of: **2026-11-24**
- Quant sources: https://finance.yahoo.com/quote/CSCO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/CSCO/key-statistics/
- AI analysis snapshot as_of: **2026-11-24**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-25T07:07:52.441224+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 23, 'rule': 5, 'ai': 17, 'unknown': 0, 'irrelevant': 1})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **8** exact headline/source/date matches; prior report **20261124T081701Z-6c335e3d/CSCO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **6**; {'directional_claim_without_event_type': 5, 'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 23 unique headlines; 10 named publishers; 2 exact duplicates; 23 HTTPS source links; largest publisher share 26.09%; oldest publication 2026-11-17

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 93.9900 |
| Return 1D (%) | -2.9029 |
| Return 1W (%) | -1.1776 |
| Return 1M (%) | -11.7465 |
| Return YTD (%) | 24.2763 |
| Return 1Y (%) | 25.5641 |
| Annualized volatility (%) | 37.9878 |
| Beta vs SPY | 1.3077 |
| Max drawdown (%) | -29.7448 |
| Sharpe (rf=0) | 0.7919 |
| Downside deviation (rf=0, %) | 26.5702 |
| Sortino (rf=0) | 1.1321 |
| Historical VaR 95% (1D, %) | 3.2126 |
| Historical ES 95% (1D, %) | 5.6237 |
| Correlation vs SPY | 0.5148 |
| Tracking error vs SPY (%) | 32.8909 |
| P/E (trailing) | 25.00 |
| P/B | 7.17 |
| EV/EBITDA | 18.66 |
| Revenue growth (%) | 24.40 |
| Forward P/E (estimate) | 15.52 |
| Gross margin (%) | 64.07 |
| Operating margin (%) | 27.17 |
| Return on equity (%) | 30.38 |
| Free cash flow yield (%) | 2.81 |
| MA50 | 105.5651 |
| Close vs MA50 (%) | -10.9649 |
| MA200 | 102.2074 |
| Close vs MA200 (%) | -8.0399 |
| RSI (14, Wilder) | 41.0380 |
| MACD (12,26) | -3.5664 |
| MACD signal (9) | -3.4136 |
| MACD histogram | -0.1528 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'CSCO': 289, 'SPY': 289}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 93.9900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -2.9029 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -1.1776 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -11.7465 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 24.2763 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 25.5641 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 37.9878 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 26.5702 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.1321 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.2126 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.6237 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5148 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 32.8909 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.3077 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -29.7448 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.7919 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 15.5180 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 64.0740 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 27.1720 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 30.3800 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.8094 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 24.9973 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 41.0380 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.1528 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -10.9649 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -8.0399 -> Clearly below the moving-average trend level.

## TAILWINDS

### Why Did Cisco Stock Jump?
- Summary: Analysis of factors contributing to recent Cisco stock price increase.
- Date: 2026-11-24 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxNblpEQURxbGlHZkNyTVVzNGpzQkhGQlJDYUpoend5OGJzY1F3M1JFeDVMQkxZYjE1VkFXbmRjUzlNOHFmZDhvSVoySFltcjZJSmlRcGdtMEtPTXZfWEFYYlNVVXRvbTNURE44dmJVNmIxU3BiQnBtVTN3c3REYTVBc3ZrNTVKcVE5RGczWmxR?oc=5>

### Cisco to Participate in December Events with the Financial Community
- Summary: Cisco will attend December financial community events, potentially boosting investor relations.
- Date: 2026-11-24 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxPNmtuOUl5ZWxWV19vSUg2TE9VZWYzMjFFMFhrZFhRT2xWYU9FMzExMDBhVkxCWWdaWVhJdm83cXltQWVSa3FjTnp5ck8zbTZvNndrYW1Gc3BOb1MtRnUyVmlnYXVycXBwNTV3by03OEZhSldmUExpSENoVHktdWVIaHd3WFIySlE1RTBCNjFnWG9YWXJtblExak0xZDdzaWR3bEJPTVcyTUtHRjdIdGJ6Wg?oc=5>

### Will Cisco stock hold $88.93 support as seller pressure weighs?
- Summary: Questioning Cisco stock's ability to maintain support level amid selling pressure.
- Date: 2026-11-24 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxONTczX1B4MUxpQ2tyQkY0bXF0aV9HX3RURDNIaDY5bXo4aWVqTkd0Wm1xSUQ2dlBTNlU1dEM2RE94c1dUMVNReHZHRlBpckg2NXhHcEVSVk1TUjVzNmJaekZwVmpwb0Ytam5JLTFpLXlwNnYtallBMldhUklubDZFVjFkdkJQcXJiUXRn?oc=5>

### Cisco Systems Inc Stock (CSCO) Moved Down by 3.99% on Nov 24: Facts Behind the Movement
- Summary: Explores reasons for Cisco's 3.99% decline on Nov 24.
- Date: 2026-11-24 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxQd0xJckRWTHZOX1B1S3ZGQ2tURkU4a2RNTE9ZdWV3dXZVdnlPTmhSd0NtTmJyVmNSSFhBVTRVVFJfR0JoS20zOVVjYUNTZ0pRRkRFRWVxb3BOQk1mZnlXOEswZG81bWw5dGRkQ0gyYmY4bXVXZzQyYmc0RGlvOFdqWGtPMm1OejVTc0lv?oc=5>

### Analysts Offer Insights on Technology Companies: Cisco Systems (CSCO) and JetAI (JTAI)
- Summary: Analysts discuss Cisco and JetAI, providing market insights.
- Date: 2026-11-24 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi-gFBVV95cUxNLURSVFg2SFZXZXROWUZmcVlnVGxWREpWSFNEVk03alpYWUpXRmZPV2R2UXhscGVmZjJYWGptYWxOdEQtQXY0am1SempYR3Flc0NVSWhIVHhET2h0dndqRmlpU3IyMjE4WlNtRmgzSmFTS1E0U05aYVdqeUVRX25YTHlRRUdNTDhYM3l4N0dScTdycjR6UDd6MTJJMHZSNFd6ZEQxWGgyejFSdDZpX1JlbVR6YXlFNWctTjBMRnNGSXdJeU1iX0sxSWgycFFiUkJ1enJJUEZtRlRfYzd4RmhsdVRSZU1CcTB3T0hCZTNkYV96S1NwekdDX3pn?oc=5>

### Cisco (CSCO) Stock Still Looks Cheap Despite Its 118% Run
- Summary: Stock perceived as undervalued, suggesting potential upside.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxPYjJJTmVsSVM2Y3ROQmh3REJfZDBfSGE2R2wzQjFyT0tjYVlmRkI5RWdZSktRYzhvSTE1d3BBVFBHV1I2VnZuNTZsd09lVkI3ZmNjcDIxc0VQWnlfMHktM0dORDdsNlliM3RLQS1SMW40M0x1eFBacXdWVWE5SnBOUkdtSWJwa0dtMXZhOExuZTRvMHVpbUtkdVZ4bWZTYVNxam1FdkdKSTZhbDNNR3VfWTZ3ajlUekloZC1oNmpTMNIBxAFBVV95cUxNSDVBRjFLNnEtUWpzMV9sbGJmRmRCZ0VhMTJJNEdhYnh5WFVyams1TVdBcnVsVEZfVndEcXk4RmxfZTNLbDF0SXFreWNpZTNsVlIwS1dnWVhVSWVPWEFQNEh6aXkwUkl6M3c2cWwySjRpUHBLS184OV94SG9ld1FSMDFncU81dkJNZ2o5N2l2Vm11VkMyZzBxWEhiSEdSMXFJd3dBaHVqYWU2R0ZjaEk2OEFoNXN6TkwwVWtuVUlXbk5GMk54?oc=5>

## HEADWINDS

### Cisco Stock Fell 15.5% Despite Its Strongest Growth in 15 Years. Is the Dividend Safe?
- Summary: Cisco Stock Fell 15.5% Despite Its Strongest Growth in 15 Years. Is the Dividend Safe?
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixgFBVV95cUxOLW5SV3lqa1B5SE1SMHZhUDhKaWNlaG5fUnZvNk00NHU1eHU4bVdxWXVFZDQ2bmtpOVRwUUp1SXg1dnB4S2h6WFdYWmJxODJLOTFacmtoLXFPam1TUTRCdDlpN0FEcElWS1dHMFFRWUd0NjN3b0JUQ2lXcTh1dmhmcHpLbzlDQWlzX0VZMnRBNVpEY3JCSXlIazVqTzBuWVp4azJ2QXFUSXFtNkRlQzdPdWc0alhIVlpFTGVyNEx4b0JQWHo3NWc?oc=5>

### Cisco Systems, Inc. (CSCO) Posted Record $17.3 Billion Revenue, but Margins Slipped: Is the Stock Still Worth Buying?
- Summary: Cisco Systems, Inc. (CSCO) Posted Record $17.3 Billion Revenue, but Margins Slipped: Is the Stock Still Worth Buying?
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxQazVldGNaeWhMdGxVX3lmZlJjRHh5OE91TFUzUGhzYXJjUDB6aXh4Y0hITjZMREZPTmZ0UmYwRGxzY0VoSlRVWlF2UmVCeHZ2NWlIbEtja3V3RHhNNmtoYlBTcjNQQ3pXQm5zNXdUYnZuY2hGeXNPbHVCUDBDSDEzQTdhbXBSWDRyeHZ6dzl4QlQwNEVES0lQVlZB?oc=5>

### Cisco Systems (NASDAQ:CSCO) Stock Falls 2.9% - Here's What Happened
- Summary: Cisco Systems (NASDAQ:CSCO) Stock Falls 2.9% - Here's What Happened
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxPWHdPM2dzUW1NdlRaOTRNd3UwU3ptbU5ubTM2OXJZYzlYdTlqd21EZmctOXZGSlRNOEl4czFCT0RzSFkwZXFCYU5kM2JsMEZOVl84NkM1eGktcXhSWkxKMzJoYUNJbkNJRlZ4akhEV0tPSjZoZ2RYSThTQ0FhSktjU201NngyQXhKXy1HNzlieEk5NUxMcWx1WjNjbmQ1TFB2RmRqS19lNFhuUURfNVNaeWNoTG1rdDlEWFFrTQ?oc=5>

### Cisco Slides as Tech Pullback and Profit-Taking Weigh on Shares
- Summary: Cisco Slides as Tech Pullback and Profit-Taking Weigh on Shares
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxPR09qVGkwR0hzSmJlSFBHa080TEt2cHhSSjhsSXF6R1RtV0ZULWJWN01tRXJpM0tnczNKeGJVS2xFUU9vZTNjRkZsTnlJMTBKOFZSUkFTeldtdkdzQ1NDZHhYVGxOSmVOdy1LN20yaVNJV2EwSEdqRTg2YzlmWDJjWWRFNGM0SUFBMXdXMzdGelBRNGpRendGVFkwa1k?oc=5>

### Cisco insider share sales: Can CSCO avoid deeper losses?
- Summary: Insider share sales may signal declining confidence, potentially impacting stock negatively.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxQWUdpdXY2TlhoRDBwTWNzZU9Nb3plYWFHZ1JXSEdhejlUOHVMd0ZVQklBc1p0dHRjT0lpYWdUMWZmc0QwSS1XNFN2eU1ibnpFM2ZTNzhkeS1JbmpiN3dPcTZ6c0x6emtYVlFqNXRHRWZkMGw5ZEJGb0puN1k2RlJySEZmcXlWTExHR1Q4NjNTaw?oc=5>

### Cisco Systems Inc Stock (CSCO) Moved Down by 3.10% on Nov 20: A Full Analysis
- Summary: Stock fell 3.10%, indicating a short-term negative market reaction.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxPbVRIOElDNVBrZkR1MHZrcDNvVXIyT0lObnNwcTVQR3Z1dHA3VHFGdVNvLUpGN21pZTJUVDFMMzZiNnJZME9NbTRsU0lBZTdUSHVsYVFOSGZuMFNaWldXenU1cFhRVDUwTjhTYlpzd2hGOHU3STRxUS1wR09jS0wwdkRyYUdqTnlOZllV?oc=5>

### Cisco ordered to address Expressway vulnerability: CSCO rally loses momentum
- Summary: Regulatory order may dampen investor sentiment and affect stock momentum.
- Date: 2026-11-23 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxPYjRubFp6SVhqLUlRbU1tSVZNdjdkYmZ4ak5uRW05MEtvUHBVNFVrUmhwNUZndXFpMjNJZW9QdllfRDNRNC1CTVRSby1FQ2pxVXU2bERwTTJCeGl3X3d2XzRmQ1Y0YU42OWJQejByOXZzc2xlYktLcGROUVBlWmtwTGZ6UVBHbmlhd0Z3?oc=5>

## CATALYSTS

### Cisco (CSCO) Stock Gets Fair Value Trim As Analysts Cut Targets After Strong Q1
- Summary: Cisco (CSCO) Stock Gets Fair Value Trim As Analysts Cut Targets After Strong Q1
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxOd0psSW1iRElNXzlmeTI0QTZrM1J1UU5QaUJnS1J4NXFMYzhMM2dvb3dxeG5zSHRFTG5IRkhPTklXMy1vM01GaDBRSlRYNjQxM3E2aEZtYXlyTEdRR0x3STNMMUlyQ1A4aWNERVNQTW1RazVaZUc2WFJ2UjY1eVVUanA2U3ZGMXZITlRJOVRNeF9QTzhJaHc?oc=5>

### Can Cisco Stock Hit $120?
- Summary: Speculation on whether Cisco stock can reach $120.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxQTlB1aWlkZlVUd1pFYkpGVzhlaDUtWEs1MHhyZlVQUkV4bkRjdWRLbmdLME1McGRvNDIwMFgtVkVqcUhHOGhocDZsX2l5SExvTW1iY3pGRzRNamVFcDZWZ2xuREN6aTN4Sm9tcEp2M3RDRmhfbUdlZXhBS0RFREcwZGJjVmN0Z0g1TnFRSg?oc=5>

### Cisco’s CEO Just Sold $27 Million of Stock in 3 Days
- Summary: Cisco CEO sold $27M of shares over three days.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxObk1wZmhoMzladm0wOVlmakNfWXdhTWN1ZHZ2WmFfVzN0OTVBWVpvMW1vY290c1hyalBfMS1vcGVzWXNidFFlUGtZSjJ6UXpnQ1JyNktMVEg3RklqdnYzZ1o3cEpETlRpUXRNNUdoUmJfY21QQXczRGpWU280c3FTRUZqR1U0elNSSGRvWHBpb3M?oc=5>

### How Investors May Respond To Cisco Stock After Earnings Beat
- Summary: Earnings beat may boost investor sentiment and drive stock upward.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxOMHZiWHc0TlV6cUxOTTNTbDQzdkczcWFEZ2RELUhIaG1vbDhjcFJreXZleXRmc0Q3UHNqbm84SW9pZlIwdmY2Z0xLcUt5RXd2c2RQT3NCREI2RmdmRGthaUJhU3pTd09NZUg0RllpZ3hVNmFGZlRBbVAwZ2ltajRiQ1lYQmFwMmFBSHNqSDl1WmtXbmtmRWZtOUVFNkFiYXM?oc=5>

### Cisco Drops 7% Post Earnings: Should You Buy the Stock on the Dip?
- Summary: Cisco’s earnings miss caused a 7% drop, prompting investors to consider buying at the dip.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxOR2gxQW9fU2tUZlVfZ3k0RGw2UF9KWjAwVGVFUFU4c2R1VE5PWERjTkMtNnF6OUNQNjYtQzhsN1RrUFU0OHU1MjJaeS0wYUdIdlY1TmVpajRVZWh1TWhrNG82OWRmeHBaZzg2dEREcGFOc01mVE4tR2ZPUWtGc1dkRmM3dVlJTjNXaHpENFhzUXEzN29SOGdv?oc=5>

### Cisco Systems Inc Stock (CSCO) Moved Up by 6.44% on Nov 23: Key Drivers Unveiled
- Summary: Cisco shares rose 6.44% on Nov 23, driven by key factors.
- Date: 2026-11-23 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxOdEUwVkdOckx1ZUhBUVhfc1VpWk1jckhFYmFkc2ZkamNlOTlMdy14ZE8xX1BsN1Z4eENlRHJESFBHckNkd3FDUEVjLUNWUlBOdlJ1M0MxaEVfdWI4bGFCLUM5U2N1cVIxMGNQYUtvcVZneUIzc3BuanE4MmRpeGRVak9BN1NJTzdfcU1B?oc=5>

### What Did Cisco’s Quarter Change For Its Stock?
- Summary: Cisco’s latest quarterly results and their impact on the stock price.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxPZkpSempEOHAyWU5QVVlKUGw2Zl81RHBKRnBGT3ljMmQ5Q21VazV1azg0ZzdUek5zZHQ0MVZfRkJGVWNzQXpHUkk5dVVZMENON3JuYWJsQ3RDVlVqNS1FeGp1dUprLUFWSnUxd0xDdFg2dUJmZ2tXVU9HS2RyaHJKeEVVTmZULUpoUVlDZzVjNHVNMGVfNTRiOC11OG5sbkhEVzhZODRlMlg?oc=5>

### Cisco Systems (CSCO) Lifted Its Outlook, Is It Still 38% Undervalued?
- Summary: Outlook upgrade could support higher valuation expectations.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxOUzlpX21FUGR4U0FIZGN5RnBBTFV1OS1mc2lBZXd1TGR4V0hMaGtXTGstOEcxSmhfOVpKUDR3S1ZOV1I1WnAxUFBJS1p6X2JxTy1PVVM2VzJIY3RZRkk0OThkeXJXUWJOVHllamc3UVFENjZmNTlUZkhQNHdpeDEtS1o3QUVwTlZKOTZpY2hQZDV2VFFRZUdBRXMxVHRhaTg?oc=5>

### Cisco Beat Revenue at 18% Growth and $9.3B AI Orders — So Why Did the Stock Plunge 9% to $112?
- Summary: Earnings beat but stock fell, indicating market overreaction.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi3AFBVV95cUxObzFNNUtsdDh5Z0ZjZmN0R1lhUFppN0lpaWNQcWp4dDB4Z3ZOQWNSLWhlMTZsWXdaU2trdXpsbzFOc2VOeUdyRXQ3a2dyTGcxQVF0NUw2VXI0SEdBT05SUjZ4XzIzT2s2NDljNVhjVldlODZBbnltOEg0Y2w0OVNabkRralU3S2h1R2h2Y2RDOXlaejBoNjJhVENfaVBNX2lHb2VrSnB4NnllWDNpM3RQZ2ZZNjZjS1hQbFVGUG1JdW9KS0o3bFdia1M3bG1pUnBIQlZRLTFZSU4tRFdt?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **CSCO** | **25.00** | **7.17** | **18.66** | **24.40** | **370,550,702,080.00 USD** | **25.56** |
| ANET | 45.19 | 12.95 | 37.44 | 58.50 | 212,959,100,928.00 USD | 37.97 |
| FFIV | 25.31 | 4.49 | 18.11 | 13.30 | 18,041,337,856.00 USD | 34.19 |
| HPE | 20.72 | 2.01 | 11.31 | 33.70 | 53,350,809,600.00 USD | 94.00 |

Peers fetched as_of: 2026-11-24; CSCO reuses existing data (market data as_of: 2026-11-24); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-12
- Next expected earnings: 2027-02-10 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-24

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-17
- Revenue (latest available single quarter): 12,844,000,000.00 USD; period 2018-04-29/2018-07-28; fiscal year/reporting period 2018/FY
- Net income (latest available single quarter): 4,552,000,000.00 USD; period 2026-07-26/2026-10-24; fiscal year/reporting period 2027/Q1
- SEC link: https://www.sec.gov/Archives/edgar/data/858877/000085887726000185/csco-20261024.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMijgFBVV95cUxNblpEQURxbGlHZkNyTVVzNGpzQkhGQlJDYUpoend5OGJzY1F3M1JFeDVMQkxZYjE1VkFXbmRjUzlNOHFmZDhvSVoySFltcjZJSmlRcGdtMEtPTXZfWEFYYlNVVXRvbTNURE44dmJVNmIxU3BiQnBtVTN3c3REYTVBc3ZrNTVKcVE5RGczWmxR?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxPNmtuOUl5ZWxWV19vSUg2TE9VZWYzMjFFMFhrZFhRT2xWYU9FMzExMDBhVkxCWWdaWVhJdm83cXltQWVSa3FjTnp5ck8zbTZvNndrYW1Gc3BOb1MtRnUyVmlnYXVycXBwNTV3by03OEZhSldmUExpSENoVHktdWVIaHd3WFIySlE1RTBCNjFnWG9YWXJtblExak0xZDdzaWR3bEJPTVcyTUtHRjdIdGJ6Wg?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxONTczX1B4MUxpQ2tyQkY0bXF0aV9HX3RURDNIaDY5bXo4aWVqTkd0Wm1xSUQ2dlBTNlU1dEM2RE94c1dUMVNReHZHRlBpckg2NXhHcEVSVk1TUjVzNmJaekZwVmpwb0Ytam5JLTFpLXlwNnYtallBMldhUklubDZFVjFkdkJQcXJiUXRn?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxQd0xJckRWTHZOX1B1S3ZGQ2tURkU4a2RNTE9ZdWV3dXZVdnlPTmhSd0NtTmJyVmNSSFhBVTRVVFJfR0JoS20zOVVjYUNTZ0pRRkRFRWVxb3BOQk1mZnlXOEswZG81bWw5dGRkQ0gyYmY4bXVXZzQyYmc0RGlvOFdqWGtPMm1OejVTc0lv?oc=5
- https://news.google.com/rss/articles/CBMi-gFBVV95cUxNLURSVFg2SFZXZXROWUZmcVlnVGxWREpWSFNEVk03alpYWUpXRmZPV2R2UXhscGVmZjJYWGptYWxOdEQtQXY0am1SempYR3Flc0NVSWhIVHhET2h0dndqRmlpU3IyMjE4WlNtRmgzSmFTS1E0U05aYVdqeUVRX25YTHlRRUdNTDhYM3l4N0dScTdycjR6UDd6MTJJMHZSNFd6ZEQxWGgyejFSdDZpX1JlbVR6YXlFNWctTjBMRnNGSXdJeU1iX0sxSWgycFFiUkJ1enJJUEZtRlRfYzd4RmhsdVRSZU1CcTB3T0hCZTNkYV96S1NwekdDX3pn?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxPYjJJTmVsSVM2Y3ROQmh3REJfZDBfSGE2R2wzQjFyT0tjYVlmRkI5RWdZSktRYzhvSTE1d3BBVFBHV1I2VnZuNTZsd09lVkI3ZmNjcDIxc0VQWnlfMHktM0dORDdsNlliM3RLQS1SMW40M0x1eFBacXdWVWE5SnBOUkdtSWJwa0dtMXZhOExuZTRvMHVpbUtkdVZ4bWZTYVNxam1FdkdKSTZhbDNNR3VfWTZ3ajlUekloZC1oNmpTMNIBxAFBVV95cUxNSDVBRjFLNnEtUWpzMV9sbGJmRmRCZ0VhMTJJNEdhYnh5WFVyams1TVdBcnVsVEZfVndEcXk4RmxfZTNLbDF0SXFreWNpZTNsVlIwS1dnWVhVSWVPWEFQNEh6aXkwUkl6M3c2cWwySjRpUHBLS184OV94SG9ld1FSMDFncU81dkJNZ2o5N2l2Vm11VkMyZzBxWEhiSEdSMXFJd3dBaHVqYWU2R0ZjaEk2OEFoNXN6TkwwVWtuVUlXbk5GMk54?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxOLW5SV3lqa1B5SE1SMHZhUDhKaWNlaG5fUnZvNk00NHU1eHU4bVdxWXVFZDQ2bmtpOVRwUUp1SXg1dnB4S2h6WFdYWmJxODJLOTFacmtoLXFPam1TUTRCdDlpN0FEcElWS1dHMFFRWUd0NjN3b0JUQ2lXcTh1dmhmcHpLbzlDQWlzX0VZMnRBNVpEY3JCSXlIazVqTzBuWVp4azJ2QXFUSXFtNkRlQzdPdWc0alhIVlpFTGVyNEx4b0JQWHo3NWc?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxNWVh6MU8tWllnenNJUHZSZ0MwMDNKSE9IaVF5VXdJb3VhVzBucXI3ZDMySUhCUmRIQ0pWSHM4VWROMjFndmF6RElkV3J1aWRRckNfNGVobXNKQWtTWW8zdjJzcnZwWFA1NlRmQXJMVUVTSW9NRy1qbHhyVURZN25QMEZnOHExWl9vUWkwSy1Bcw?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxQazVldGNaeWhMdGxVX3lmZlJjRHh5OE91TFUzUGhzYXJjUDB6aXh4Y0hITjZMREZPTmZ0UmYwRGxzY0VoSlRVWlF2UmVCeHZ2NWlIbEtja3V3RHhNNmtoYlBTcjNQQ3pXQm5zNXdUYnZuY2hGeXNPbHVCUDBDSDEzQTdhbXBSWDRyeHZ6dzl4QlQwNEVES0lQVlZB?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxPWHdPM2dzUW1NdlRaOTRNd3UwU3ptbU5ubTM2OXJZYzlYdTlqd21EZmctOXZGSlRNOEl4czFCT0RzSFkwZXFCYU5kM2JsMEZOVl84NkM1eGktcXhSWkxKMzJoYUNJbkNJRlZ4akhEV0tPSjZoZ2RYSThTQ0FhSktjU201NngyQXhKXy1HNzlieEk5NUxMcWx1WjNjbmQ1TFB2RmRqS19lNFhuUURfNVNaeWNoTG1rdDlEWFFrTQ?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxPR09qVGkwR0hzSmJlSFBHa080TEt2cHhSSjhsSXF6R1RtV0ZULWJWN01tRXJpM0tnczNKeGJVS2xFUU9vZTNjRkZsTnlJMTBKOFZSUkFTeldtdkdzQ1NDZHhYVGxOSmVOdy1LN20yaVNJV2EwSEdqRTg2YzlmWDJjWWRFNGM0SUFBMXdXMzdGelBRNGpRendGVFkwa1k?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxQWUdpdXY2TlhoRDBwTWNzZU9Nb3plYWFHZ1JXSEdhejlUOHVMd0ZVQklBc1p0dHRjT0lpYWdUMWZmc0QwSS1XNFN2eU1ibnpFM2ZTNzhkeS1JbmpiN3dPcTZ6c0x6emtYVlFqNXRHRWZkMGw5ZEJGb0puN1k2RlJySEZmcXlWTExHR1Q4NjNTaw?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxPbVRIOElDNVBrZkR1MHZrcDNvVXIyT0lObnNwcTVQR3Z1dHA3VHFGdVNvLUpGN21pZTJUVDFMMzZiNnJZME9NbTRsU0lBZTdUSHVsYVFOSGZuMFNaWldXenU1cFhRVDUwTjhTYlpzd2hGOHU3STRxUS1wR09jS0wwdkRyYUdqTnlOZllV?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxPYjRubFp6SVhqLUlRbU1tSVZNdjdkYmZ4ak5uRW05MEtvUHBVNFVrUmhwNUZndXFpMjNJZW9QdllfRDNRNC1CTVRSby1FQ2pxVXU2bERwTTJCeGl3X3d2XzRmQ1Y0YU42OWJQejByOXZzc2xlYktLcGROUVBlWmtwTGZ6UVBHbmlhd0Z3?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxOd0psSW1iRElNXzlmeTI0QTZrM1J1UU5QaUJnS1J4NXFMYzhMM2dvb3dxeG5zSHRFTG5IRkhPTklXMy1vM01GaDBRSlRYNjQxM3E2aEZtYXlyTEdRR0x3STNMMUlyQ1A4aWNERVNQTW1RazVaZUc2WFJ2UjY1eVVUanA2U3ZGMXZITlRJOVRNeF9QTzhJaHc?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxQTlB1aWlkZlVUd1pFYkpGVzhlaDUtWEs1MHhyZlVQUkV4bkRjdWRLbmdLME1McGRvNDIwMFgtVkVqcUhHOGhocDZsX2l5SExvTW1iY3pGRzRNamVFcDZWZ2xuREN6aTN4Sm9tcEp2M3RDRmhfbUdlZXhBS0RFREcwZGJjVmN0Z0g1TnFRSg?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxObk1wZmhoMzladm0wOVlmakNfWXdhTWN1ZHZ2WmFfVzN0OTVBWVpvMW1vY290c1hyalBfMS1vcGVzWXNidFFlUGtZSjJ6UXpnQ1JyNktMVEg3RklqdnYzZ1o3cEpETlRpUXRNNUdoUmJfY21QQXczRGpWU280c3FTRUZqR1U0elNSSGRvWHBpb3M?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxPdDNIY29LZWFpZ1lHNHBiTmdBVHN1NmkxM05pWTVOdEZuSTNGeFJVaFVwLS1FZE9PU1k5QWEtRm95UjMtUlpKTmU0VkRpMDBUbVptQ0RDRmJGR0x6c1J5amNCZnpkbURheE9lUDNGTVU0OW5UeWtwREdpVVR6eDgxTmJERS12Y2xGdFU2OXhPQXNLMHY0M1FpRVBn?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxOMHZiWHc0TlV6cUxOTTNTbDQzdkczcWFEZ2RELUhIaG1vbDhjcFJreXZleXRmc0Q3UHNqbm84SW9pZlIwdmY2Z0xLcUt5RXd2c2RQT3NCREI2RmdmRGthaUJhU3pTd09NZUg0RllpZ3hVNmFGZlRBbVAwZ2ltajRiQ1lYQmFwMmFBSHNqSDl1WmtXbmtmRWZtOUVFNkFiYXM?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxOR2gxQW9fU2tUZlVfZ3k0RGw2UF9KWjAwVGVFUFU4c2R1VE5PWERjTkMtNnF6OUNQNjYtQzhsN1RrUFU0OHU1MjJaeS0wYUdIdlY1TmVpajRVZWh1TWhrNG82OWRmeHBaZzg2dEREcGFOc01mVE4tR2ZPUWtGc1dkRmM3dVlJTjNXaHpENFhzUXEzN29SOGdv?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxOdEUwVkdOckx1ZUhBUVhfc1VpWk1jckhFYmFkc2ZkamNlOTlMdy14ZE8xX1BsN1Z4eENlRHJESFBHckNkd3FDUEVjLUNWUlBOdlJ1M0MxaEVfdWI4bGFCLUM5U2N1cVIxMGNQYUtvcVZneUIzc3BuanE4MmRpeGRVak9BN1NJTzdfcU1B?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxPZkpSempEOHAyWU5QVVlKUGw2Zl81RHBKRnBGT3ljMmQ5Q21VazV1azg0ZzdUek5zZHQ0MVZfRkJGVWNzQXpHUkk5dVVZMENON3JuYWJsQ3RDVlVqNS1FeGp1dUprLUFWSnUxd0xDdFg2dUJmZ2tXVU9HS2RyaHJKeEVVTmZULUpoUVlDZzVjNHVNMGVfNTRiOC11OG5sbkhEVzhZODRlMlg?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxOUzlpX21FUGR4U0FIZGN5RnBBTFV1OS1mc2lBZXd1TGR4V0hMaGtXTGstOEcxSmhfOVpKUDR3S1ZOV1I1WnAxUFBJS1p6X2JxTy1PVVM2VzJIY3RZRkk0OThkeXJXUWJOVHllamc3UVFENjZmNTlUZkhQNHdpeDEtS1o3QUVwTlZKOTZpY2hQZDV2VFFRZUdBRXMxVHRhaTg?oc=5
- https://news.google.com/rss/articles/CBMi3AFBVV95cUxObzFNNUtsdDh5Z0ZjZmN0R1lhUFppN0lpaWNQcWp4dDB4Z3ZOQWNSLWhlMTZsWXdaU2trdXpsbzFOc2VOeUdyRXQ3a2dyTGcxQVF0NUw2VXI0SEdBT05SUjZ4XzIzT2s2NDljNVhjVldlODZBbnltOEg0Y2w0OVNabkRralU3S2h1R2h2Y2RDOXlaejBoNjJhVENfaVBNX2lHb2VrSnB4NnllWDNpM3RQZ2ZZNjZjS1hQbFVGUG1JdW9KS0o3bFdia1M3bG1pUnBIQlZRLTFZSU4tRFdt?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
