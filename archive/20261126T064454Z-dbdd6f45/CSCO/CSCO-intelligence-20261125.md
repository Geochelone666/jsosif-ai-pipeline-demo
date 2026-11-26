# CSCO Intelligence Report

- ticker: **CSCO**
- Report as_of: **2026-11-25**
- Market data as_of: **2026-11-25**
- Quant sources: https://finance.yahoo.com/quote/CSCO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/CSCO/key-statistics/
- AI analysis snapshot as_of: **2026-11-25**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-26T07:10:38.720883+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 6, 'ai': 17, 'unknown': 0, 'irrelevant': 1})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **9** exact headline/source/date matches; prior report **20261125T065354Z-0b3565c6/CSCO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **4**; {'directional_claim_without_event_type': 3, 'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 12 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 16.67%; oldest publication 2026-11-18

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 94.2000 |
| Return 1D (%) | 0.2234 |
| Return 1W (%) | -3.0665 |
| Return 1M (%) | -11.5493 |
| Return YTD (%) | 24.5540 |
| Return 1Y (%) | 25.7127 |
| Annualized volatility (%) | 37.9879 |
| Beta vs SPY | 1.3118 |
| Max drawdown (%) | -29.7448 |
| Sharpe (rf=0) | 0.7950 |
| Downside deviation (rf=0, %) | 26.5702 |
| Sortino (rf=0) | 1.1366 |
| Historical VaR 95% (1D, %) | 3.2126 |
| Historical ES 95% (1D, %) | 5.6237 |
| Correlation vs SPY | 0.5156 |
| Tracking error vs SPY (%) | 32.8807 |
| P/E (trailing) | 25.05 |
| P/B | 7.18 |
| EV/EBITDA | 18.70 |
| Revenue growth (%) | 24.40 |
| Forward P/E (estimate) | 15.57 |
| Gross margin (%) | 64.07 |
| Operating margin (%) | 27.17 |
| Return on equity (%) | 30.38 |
| Free cash flow yield (%) | 2.80 |
| MA50 | 105.3027 |
| Close vs MA50 (%) | -10.5436 |
| MA200 | 102.2525 |
| Close vs MA200 (%) | -7.8751 |
| RSI (14, Wilder) | 41.3892 |
| MACD (12,26) | -3.4856 |
| MACD signal (9) | -3.4280 |
| MACD histogram | -0.0576 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'CSCO': 290, 'SPY': 290}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 94.2000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.2234 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -3.0665 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -11.5493 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 24.5540 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 25.7127 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 37.9879 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 26.5702 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.1366 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.2126 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.6237 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5156 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 32.8807 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.3118 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -29.7448 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.7950 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 15.5719 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 64.0740 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 27.1720 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 30.3800 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.8031 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 25.0532 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 41.3892 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.0576 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -10.5436 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -7.8751 -> Clearly below the moving-average trend level.

## TAILWINDS

### Cisco Systems (NASDAQ:CSCO) Stock Jumps 6.8% - Here's Why
- Summary: Cisco Systems (NASDAQ:CSCO) Stock Jumps 6.8% - Here's Why
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxQaHZ4VHhKWW9SaGUtMjY3elhGSzlrX2ZMUWwwNURmcUJpR0hwVnZaM1ItT1RhR0FiQVBVWW1ubUZJc2k1bHF1SGlmaEJsazNMMGxEWWlPdHN0UnltcTBpRllHTzFOTWdXd2xvUzdobWxNaEljSF9DcFlDcDF6YnhTNDliQ0ktcVpNT3JtNUJjY0xMTU14MHA2WWtFZEhqazdlR1Y3WDFMUmhJdC1PeHU0?oc=5>

### Why Did Cisco Stock Jump?
- Summary: Analysis of factors contributing to recent Cisco stock price increase.
- Date: 2026-11-24 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxNblpEQURxbGlHZkNyTVVzNGpzQkhGQlJDYUpoend5OGJzY1F3M1JFeDVMQkxZYjE1VkFXbmRjUzlNOHFmZDhvSVoySFltcjZJSmlRcGdtMEtPTXZfWEFYYlNVVXRvbTNURE44dmJVNmIxU3BiQnBtVTN3c3REYTVBc3ZrNTVKcVE5RGczWmxR?oc=5>

### Cisco to Participate in December Events with the Financial Community
- Summary: Cisco will attend December financial community events, potentially boosting investor relations.
- Date: 2026-11-24 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxPNmtuOUl5ZWxWV19vSUg2TE9VZWYzMjFFMFhrZFhRT2xWYU9FMzExMDBhVkxCWWdaWVhJdm83cXltQWVSa3FjTnp5ck8zbTZvNndrYW1Gc3BOb1MtRnUyVmlnYXVycXBwNTV3by03OEZhSldmUExpSENoVHktdWVIaHd3WFIySlE1RTBCNjFnWG9YWXJtblExak0xZDdzaWR3bEJPTVcyTUtHRjdIdGJ6Wg?oc=5>

### Cisco (CSCO) Stock Still Looks Cheap Despite Its 118% Run
- Summary: Stock perceived as undervalued, suggesting potential upside.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxPYjJJTmVsSVM2Y3ROQmh3REJfZDBfSGE2R2wzQjFyT0tjYVlmRkI5RWdZSktRYzhvSTE1d3BBVFBHV1I2VnZuNTZsd09lVkI3ZmNjcDIxc0VQWnlfMHktM0dORDdsNlliM3RLQS1SMW40M0x1eFBacXdWVWE5SnBOUkdtSWJwa0dtMXZhOExuZTRvMHVpbUtkdVZ4bWZTYVNxam1FdkdKSTZhbDNNR3VfWTZ3ajlUekloZC1oNmpTMNIBxAFBVV95cUxNSDVBRjFLNnEtUWpzMV9sbGJmRmRCZ0VhMTJJNEdhYnh5WFVyams1TVdBcnVsVEZfVndEcXk4RmxfZTNLbDF0SXFreWNpZTNsVlIwS1dnWVhVSWVPWEFQNEh6aXkwUkl6M3c2cWwySjRpUHBLS184OV94SG9ld1FSMDFncU81dkJNZ2o5N2l2Vm11VkMyZzBxWEhiSEdSMXFJd3dBaHVqYWU2R0ZjaEk2OEFoNXN6TkwwVWtuVUlXbk5GMk54?oc=5>

### Cisco Systems Inc Stock (CSCO) Moved Down by 3.99% on Nov 24: Facts Behind the Movement
- Summary: Explores reasons for Cisco's 3.99% decline on Nov 24.
- Date: 2026-11-24 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxQd0xJckRWTHZOX1B1S3ZGQ2tURkU4a2RNTE9ZdWV3dXZVdnlPTmhSd0NtTmJyVmNSSFhBVTRVVFJfR0JoS20zOVVjYUNTZ0pRRkRFRWVxb3BOQk1mZnlXOEswZG81bWw5dGRkQ0gyYmY4bXVXZzQyYmc0RGlvOFdqWGtPMm1OejVTc0lv?oc=5>

### Cisco (CSCO) Stock May Be 29% Undervalued As AI Security News Builds
- Summary: Analysts suggest CSCO may be undervalued by 29% amid growing AI security demand.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxOYWQwYmJ5a2plUENjZmVDMFFoemhxWnRHYTd1Um5xamxIbHM1TGJfVEdXaWJycFluY1A4NUhEM2FqNVgyQnQ1YUtiVUs2VHBESkk1UHFUOWJUZU92cVUwSXc1VEN1aHF4ODFnOGxhWnhReDlxdzN1R1NyeGJ1Vk5Dd3BteDZEbzBrSlJTbWpPN0s5dw?oc=5>

### Cisco Gains From AI Networking Boom: Can It Outpace HPE & ANET?
- Summary: CSCO could surpass competitors in AI networking, boosting its growth prospects.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxNUVZHa2h5enhncnBlMmo2dU4wMWdudEF2NHQ5YzhLYndHVXp1MHZ6Zk5sVkltWGc2V2NKa1c0U2Zlblo1NDF2MWlLSW43cXM3d2JSQ095c0NpeXBUWnJvU0ZrOEZVSjJjVUlXZkZKalV0YkdNdGkxWGdZOTAwZmZDbHJkM3FKY0prdHZGb0x1Q3Y2ZjhyOUlKRndzeGNkZHNJY0xrRlFXTFo2M3VXNmlTTVduZFVGQQ?oc=5>

### Cisco: Its $22 Billion AI Supply Bet Looks Worth Taking
- Summary: CSCO’s $22B AI supply investment is seen as a strategic win.
- Date: 2026-11-19 | Impact: medium | Horizon: medium | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxPRVVEN2VyeUR1UFJzOXczaW1IQ1dfOTBzWEsyc2YycmZZUTR6YVgtUmw3Q2dZQ3pGNWZhU294VWd1ZnYzV0Mtc180ancyUENfVHhnM1QwZ1BJRkNEZUVkZjhENm9CbGFpY0hhcHRwOWhoYmIzMmpfZzZ5YUpEQjF4REYyNzlBbkxfdzNUV3dUdHFXbm8wRVRtUVJB?oc=5>

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

### Cisco Systems Inc Stock (CSCO) Moved Down by 3.10% on Nov 20: A Full Analysis
- Summary: Stock fell 3.10%, indicating a short-term negative market reaction.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxPbVRIOElDNVBrZkR1MHZrcDNvVXIyT0lObnNwcTVQR3Z1dHA3VHFGdVNvLUpGN21pZTJUVDFMMzZiNnJZME9NbTRsU0lBZTdUSHVsYVFOSGZuMFNaWldXenU1cFhRVDUwTjhTYlpzd2hGOHU3STRxUS1wR09jS0wwdkRyYUdqTnlOZllV?oc=5>

### Cisco’s CEO Just Sold $27 Million of Stock in 3 Days
- Summary: CEO’s large stock sale raises concerns about internal confidence.
- Date: 2026-11-19 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxObk1wZmhoMzladm0wOVlmakNfWXdhTWN1ZHZ2WmFfVzN0OTVBWVpvMW1vY290c1hyalBfMS1vcGVzWXNidFFlUGtZSjJ6UXpnQ1JyNktMVEg3RklqdnYzZ1o3cEpETlRpUXRNNUdoUmJfY21QQXczRGpWU280c3FTRUZqR1U0elNSSGRvWHBpb3M?oc=5>

### Cisco Drops 7% Post Earnings: Should You Buy the Stock on the Dip?
- Summary: CSCO fell 7% after earnings, signaling short-term weakness.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi4gFBVV95cUxNYWlDR0hJcFBncjRXeW94SElVQVNEN1EzdnVRSHNZc2RkM3RiZDQ5NVltSGJMYk9yWFc0U1g5Vk5qUkdxVTdEcmJWNmppV1dJSTUxcmkyYVpJeThfYVQ4eWdCeW94bHRIbk5CT1hFS19RcGQxejdfQWpUWHotUG8tZm4xNTBTVFhoak9MZURzY1ZSXy1WbHdUc3A2bVFGTTF5MEgwdmd1dzllRHVEcmhrRDhWWnpzUGJlU2RmMFpjVGgwU2YwZndYbHBNLW9YOXFjRUlZd2pLR2JGV1dOU3ZxakdR?oc=5>

## CATALYSTS

### Cisco Systems, Inc. (CSCO) - What Are Analysts Saying About This Stock?
- Summary: Cisco Systems, Inc. (CSCO) - What Are Analysts Saying About This Stock?
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxPM3ZtdUpuUWJsTHIycGc5Zks1dGpGcjNfbjBjZGNyWEwwRWFseXBXMjg5eXVTNnpNekxrVXJleXpUNHhQWXQxQ2thbGRrbU5lWDZkRG5PZkN5UWJLeDVjcS1iTjk1bk5ZU3lUcHlza0d4VkN5NjVWWWxveGk0NWZ5X3p2Uk1SeHhtTm1GZnBSZHB0MzE4ZEdKTW4yUmJRZW0zRHNjN0I5RThrSVJZbEJFNEh6Y01hOUNfOEFqUXAzZHdEbWhCOW9j?oc=5>

### Can Cisco Stock Hit $120?
- Summary: Speculation on whether Cisco stock can reach $120.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxQTlB1aWlkZlVUd1pFYkpGVzhlaDUtWEs1MHhyZlVQUkV4bkRjdWRLbmdLME1McGRvNDIwMFgtVkVqcUhHOGhocDZsX2l5SExvTW1iY3pGRzRNamVFcDZWZ2xuREN6aTN4Sm9tcEp2M3RDRmhfbUdlZXhBS0RFREcwZGJjVmN0Z0g1TnFRSg?oc=5>

### How Investors May Respond To Cisco Stock After Earnings Beat
- Summary: Earnings beat may boost investor sentiment and drive stock upward.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxOMHZiWHc0TlV6cUxOTTNTbDQzdkczcWFEZ2RELUhIaG1vbDhjcFJreXZleXRmc0Q3UHNqbm84SW9pZlIwdmY2Z0xLcUt5RXd2c2RQT3NCREI2RmdmRGthaUJhU3pTd09NZUg0RllpZ3hVNmFGZlRBbVAwZ2ltajRiQ1lYQmFwMmFBSHNqSDl1WmtXbmtmRWZtOUVFNkFiYXM?oc=5>

### Cisco Systems Inc Stock (CSCO) Moved Up by 6.44% on Nov 23: Key Drivers Unveiled
- Summary: Cisco shares rose 6.44% on Nov 23, driven by key factors.
- Date: 2026-11-23 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxOdEUwVkdOckx1ZUhBUVhfc1VpWk1jckhFYmFkc2ZkamNlOTlMdy14ZE8xX1BsN1Z4eENlRHJESFBHckNkd3FDUEVjLUNWUlBOdlJ1M0MxaEVfdWI4bGFCLUM5U2N1cVIxMGNQYUtvcVZneUIzc3BuanE4MmRpeGRVak9BN1NJTzdfcU1B?oc=5>

### AI Revenue Target Could Be A Big Moment For Cisco Stock (CSCO)
- Summary: Cisco’s projected AI revenue could boost investor confidence and drive stock performance.
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxQMTdVWXJXZVV6SEJjNTl1c3RUNU1KaDBNandHbjNobHVjajR1Z0VOT3B5cUhueFlDdnN2ZklTTTV6QWp0Y3FFazdHZEwyRmV5Wm1kOURvQ2NkY2VWU19ISjB5clA0eEV6YjdHQldlRXBkVXlfbGw5dzF4cjhXZk9EZkxwYjVkMHNZcS1WY2dPTnNZR3A0MF9VVWZHRFd2bl9aNTdpUXNjRnhuOTRRUXp1TVNEbVM2SGZWN21LQnBqRzBodFZVZ0o4?oc=5>

### Why Analysts Are Suddenly Talking About This Forgotten Tech Stock
- Summary: Analysts are re-evaluating Cisco’s potential, sparking renewed interest.
- Date: 2026-11-18 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxObUVGbm1yZThIOHppbXJNN1NIUHFPM1BnM1hDWXhpOVVPMUZmOHVaVU1lWWptay1wenVIN05BS2xUOU5aZm51OEkwaW9fcTVYV1piODRKbXowazdNcTFJLU50S0JVMnNSQlQ1QTJOWEpES2tZZEZHdFk0Uzk4UXhFUFRueXdyUng5bU04VUpYYmN6SnhtOHY2YjNjTldLOWxwVFFlaWYzMFBqUEFEX0E?oc=5>

### A new Cisco-OpenAI tool can protect systems while teams work on a fix.
- Summary: Cisco and OpenAI collaborate on a tool enhancing system protection during fixes.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxPMFpXbU5jSk5sYzdFRGhDU2p2X0puVjVxbEpMWVBmVlBETzJSYWs5RmRvMWF2OFpKcEFkQ2QyT0pSMEVnT25JdlNVNkRxNE05MjBoMy00ZURxdlctemo3YWFOSlpKM1ZEdTQ5c3J6d2EzOERrNVlDOXUtb1YyeEd3YUFiOUZjbXd2d2E2N2syR0szV3VYM24xRTdvUk1LQVo0UkNRTHFNOXpfZFhsZkNXU29yajBHQkhhc0lLalY3aw?oc=5>

### Cisco (CSCO) Stock Can Q1 Results Sustain The AI Rebound?
- Summary: Investors question if Q1 earnings will maintain the AI-driven stock rally.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxQNzl3YVozazZGRThYdDlEWklreDVRS2hzUnNDcXFDZUpjNUxjbm1adFNaTWtRSWRVYkUtSzFxZ1U0RVFCNnJpZnZQYzhubUZYYnRSNjZYWEVsZjZncm5kQ0xpSDVwWFdoaDNiWl9XUmQ1RTQ4LTJ5bkJFLWRMeUpremluV3Q0TUVVdkhwMkVXd1AyWGRPQVBySHYwTVFyeGxPN01mSTVQSW5FUHlReDFSTllQTFFXTnRXTXhWaFExMNIBxAFBVV95cUxPQWVFV253MkNwaVBQdU96ZVoyTW4zN0NDNUNvWjBjMnJCZTZ4czE4bEc4MWZzbDlNZl9saFNkZllxMXZYUVdNTmpxanFWUzNGeldqNFFmUjEwQXptQlZ0dGQtaHhFRko1ckZmYTF5Q3B1WTNWR3ljU1J5QzBZTGV6ZHZDeURHTGliMDVNbjJqT2gtNnVkeENDVGRMYWcwQTR0NHM2UXM1Ql83TndpVlZmeXFjTGVEd2NYMnQ1V2dDWnFrOXBZ?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **CSCO** | **25.05** | **7.18** | **18.70** | **24.40** | **371,378,585,600.00 USD** | **25.71** |
| ANET | 43.97 | 12.60 | 36.35 | 58.50 | 207,185,362,944.00 USD | 31.15 |
| FFIV | 25.32 | 4.50 | 18.12 | 13.30 | 18,051,586,048.00 USD | 32.10 |
| HPE | 13.30 | 1.95 | 7.94 | 50.30 | 53,719,117,824.00 USD | 94.55 |

Peers fetched as_of: 2026-11-25; CSCO reuses existing data (market data as_of: 2026-11-25); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-12
- Next expected earnings: 2027-02-10 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-25

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

- https://news.google.com/rss/articles/CBMirwFBVV95cUxQaHZ4VHhKWW9SaGUtMjY3elhGSzlrX2ZMUWwwNURmcUJpR0hwVnZaM1ItT1RhR0FiQVBVWW1ubUZJc2k1bHF1SGlmaEJsazNMMGxEWWlPdHN0UnltcTBpRllHTzFOTWdXd2xvUzdobWxNaEljSF9DcFlDcDF6YnhTNDliQ0ktcVpNT3JtNUJjY0xMTU14MHA2WWtFZEhqazdlR1Y3WDFMUmhJdC1PeHU0?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxNblpEQURxbGlHZkNyTVVzNGpzQkhGQlJDYUpoend5OGJzY1F3M1JFeDVMQkxZYjE1VkFXbmRjUzlNOHFmZDhvSVoySFltcjZJSmlRcGdtMEtPTXZfWEFYYlNVVXRvbTNURE44dmJVNmIxU3BiQnBtVTN3c3REYTVBc3ZrNTVKcVE5RGczWmxR?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxPNmtuOUl5ZWxWV19vSUg2TE9VZWYzMjFFMFhrZFhRT2xWYU9FMzExMDBhVkxCWWdaWVhJdm83cXltQWVSa3FjTnp5ck8zbTZvNndrYW1Gc3BOb1MtRnUyVmlnYXVycXBwNTV3by03OEZhSldmUExpSENoVHktdWVIaHd3WFIySlE1RTBCNjFnWG9YWXJtblExak0xZDdzaWR3bEJPTVcyTUtHRjdIdGJ6Wg?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxPYjJJTmVsSVM2Y3ROQmh3REJfZDBfSGE2R2wzQjFyT0tjYVlmRkI5RWdZSktRYzhvSTE1d3BBVFBHV1I2VnZuNTZsd09lVkI3ZmNjcDIxc0VQWnlfMHktM0dORDdsNlliM3RLQS1SMW40M0x1eFBacXdWVWE5SnBOUkdtSWJwa0dtMXZhOExuZTRvMHVpbUtkdVZ4bWZTYVNxam1FdkdKSTZhbDNNR3VfWTZ3ajlUekloZC1oNmpTMNIBxAFBVV95cUxNSDVBRjFLNnEtUWpzMV9sbGJmRmRCZ0VhMTJJNEdhYnh5WFVyams1TVdBcnVsVEZfVndEcXk4RmxfZTNLbDF0SXFreWNpZTNsVlIwS1dnWVhVSWVPWEFQNEh6aXkwUkl6M3c2cWwySjRpUHBLS184OV94SG9ld1FSMDFncU81dkJNZ2o5N2l2Vm11VkMyZzBxWEhiSEdSMXFJd3dBaHVqYWU2R0ZjaEk2OEFoNXN6TkwwVWtuVUlXbk5GMk54?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxQd0xJckRWTHZOX1B1S3ZGQ2tURkU4a2RNTE9ZdWV3dXZVdnlPTmhSd0NtTmJyVmNSSFhBVTRVVFJfR0JoS20zOVVjYUNTZ0pRRkRFRWVxb3BOQk1mZnlXOEswZG81bWw5dGRkQ0gyYmY4bXVXZzQyYmc0RGlvOFdqWGtPMm1OejVTc0lv?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxOYWQwYmJ5a2plUENjZmVDMFFoemhxWnRHYTd1Um5xamxIbHM1TGJfVEdXaWJycFluY1A4NUhEM2FqNVgyQnQ1YUtiVUs2VHBESkk1UHFUOWJUZU92cVUwSXc1VEN1aHF4ODFnOGxhWnhReDlxdzN1R1NyeGJ1Vk5Dd3BteDZEbzBrSlJTbWpPN0s5dw?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxNUVZHa2h5enhncnBlMmo2dU4wMWdudEF2NHQ5YzhLYndHVXp1MHZ6Zk5sVkltWGc2V2NKa1c0U2Zlblo1NDF2MWlLSW43cXM3d2JSQ095c0NpeXBUWnJvU0ZrOEZVSjJjVUlXZkZKalV0YkdNdGkxWGdZOTAwZmZDbHJkM3FKY0prdHZGb0x1Q3Y2ZjhyOUlKRndzeGNkZHNJY0xrRlFXTFo2M3VXNmlTTVduZFVGQQ?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxPRVVEN2VyeUR1UFJzOXczaW1IQ1dfOTBzWEsyc2YycmZZUTR6YVgtUmw3Q2dZQ3pGNWZhU294VWd1ZnYzV0Mtc180ancyUENfVHhnM1QwZ1BJRkNEZUVkZjhENm9CbGFpY0hhcHRwOWhoYmIzMmpfZzZ5YUpEQjF4REYyNzlBbkxfdzNUV3dUdHFXbm8wRVRtUVJB?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxOLW5SV3lqa1B5SE1SMHZhUDhKaWNlaG5fUnZvNk00NHU1eHU4bVdxWXVFZDQ2bmtpOVRwUUp1SXg1dnB4S2h6WFdYWmJxODJLOTFacmtoLXFPam1TUTRCdDlpN0FEcElWS1dHMFFRWUd0NjN3b0JUQ2lXcTh1dmhmcHpLbzlDQWlzX0VZMnRBNVpEY3JCSXlIazVqTzBuWVp4azJ2QXFUSXFtNkRlQzdPdWc0alhIVlpFTGVyNEx4b0JQWHo3NWc?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxNWVh6MU8tWllnenNJUHZSZ0MwMDNKSE9IaVF5VXdJb3VhVzBucXI3ZDMySUhCUmRIQ0pWSHM4VWROMjFndmF6RElkV3J1aWRRckNfNGVobXNKQWtTWW8zdjJzcnZwWFA1NlRmQXJMVUVTSW9NRy1qbHhyVURZN25QMEZnOHExWl9vUWkwSy1Bcw?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxQazVldGNaeWhMdGxVX3lmZlJjRHh5OE91TFUzUGhzYXJjUDB6aXh4Y0hITjZMREZPTmZ0UmYwRGxzY0VoSlRVWlF2UmVCeHZ2NWlIbEtja3V3RHhNNmtoYlBTcjNQQ3pXQm5zNXdUYnZuY2hGeXNPbHVCUDBDSDEzQTdhbXBSWDRyeHZ6dzl4QlQwNEVES0lQVlZB?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxPWHdPM2dzUW1NdlRaOTRNd3UwU3ptbU5ubTM2OXJZYzlYdTlqd21EZmctOXZGSlRNOEl4czFCT0RzSFkwZXFCYU5kM2JsMEZOVl84NkM1eGktcXhSWkxKMzJoYUNJbkNJRlZ4akhEV0tPSjZoZ2RYSThTQ0FhSktjU201NngyQXhKXy1HNzlieEk5NUxMcWx1WjNjbmQ1TFB2RmRqS19lNFhuUURfNVNaeWNoTG1rdDlEWFFrTQ?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxPR09qVGkwR0hzSmJlSFBHa080TEt2cHhSSjhsSXF6R1RtV0ZULWJWN01tRXJpM0tnczNKeGJVS2xFUU9vZTNjRkZsTnlJMTBKOFZSUkFTeldtdkdzQ1NDZHhYVGxOSmVOdy1LN20yaVNJV2EwSEdqRTg2YzlmWDJjWWRFNGM0SUFBMXdXMzdGelBRNGpRendGVFkwa1k?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxPbVRIOElDNVBrZkR1MHZrcDNvVXIyT0lObnNwcTVQR3Z1dHA3VHFGdVNvLUpGN21pZTJUVDFMMzZiNnJZME9NbTRsU0lBZTdUSHVsYVFOSGZuMFNaWldXenU1cFhRVDUwTjhTYlpzd2hGOHU3STRxUS1wR09jS0wwdkRyYUdqTnlOZllV?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxObk1wZmhoMzladm0wOVlmakNfWXdhTWN1ZHZ2WmFfVzN0OTVBWVpvMW1vY290c1hyalBfMS1vcGVzWXNidFFlUGtZSjJ6UXpnQ1JyNktMVEg3RklqdnYzZ1o3cEpETlRpUXRNNUdoUmJfY21QQXczRGpWU280c3FTRUZqR1U0elNSSGRvWHBpb3M?oc=5
- https://news.google.com/rss/articles/CBMi4gFBVV95cUxNYWlDR0hJcFBncjRXeW94SElVQVNEN1EzdnVRSHNZc2RkM3RiZDQ5NVltSGJMYk9yWFc0U1g5Vk5qUkdxVTdEcmJWNmppV1dJSTUxcmkyYVpJeThfYVQ4eWdCeW94bHRIbk5CT1hFS19RcGQxejdfQWpUWHotUG8tZm4xNTBTVFhoak9MZURzY1ZSXy1WbHdUc3A2bVFGTTF5MEgwdmd1dzllRHVEcmhrRDhWWnpzUGJlU2RmMFpjVGgwU2YwZndYbHBNLW9YOXFjRUlZd2pLR2JGV1dOU3ZxakdR?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxPM3ZtdUpuUWJsTHIycGc5Zks1dGpGcjNfbjBjZGNyWEwwRWFseXBXMjg5eXVTNnpNekxrVXJleXpUNHhQWXQxQ2thbGRrbU5lWDZkRG5PZkN5UWJLeDVjcS1iTjk1bk5ZU3lUcHlza0d4VkN5NjVWWWxveGk0NWZ5X3p2Uk1SeHhtTm1GZnBSZHB0MzE4ZEdKTW4yUmJRZW0zRHNjN0I5RThrSVJZbEJFNEh6Y01hOUNfOEFqUXAzZHdEbWhCOW9j?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxQTlB1aWlkZlVUd1pFYkpGVzhlaDUtWEs1MHhyZlVQUkV4bkRjdWRLbmdLME1McGRvNDIwMFgtVkVqcUhHOGhocDZsX2l5SExvTW1iY3pGRzRNamVFcDZWZ2xuREN6aTN4Sm9tcEp2M3RDRmhfbUdlZXhBS0RFREcwZGJjVmN0Z0g1TnFRSg?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxOMHZiWHc0TlV6cUxOTTNTbDQzdkczcWFEZ2RELUhIaG1vbDhjcFJreXZleXRmc0Q3UHNqbm84SW9pZlIwdmY2Z0xLcUt5RXd2c2RQT3NCREI2RmdmRGthaUJhU3pTd09NZUg0RllpZ3hVNmFGZlRBbVAwZ2ltajRiQ1lYQmFwMmFBSHNqSDl1WmtXbmtmRWZtOUVFNkFiYXM?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxOdEUwVkdOckx1ZUhBUVhfc1VpWk1jckhFYmFkc2ZkamNlOTlMdy14ZE8xX1BsN1Z4eENlRHJESFBHckNkd3FDUEVjLUNWUlBOdlJ1M0MxaEVfdWI4bGFCLUM5U2N1cVIxMGNQYUtvcVZneUIzc3BuanE4MmRpeGRVak9BN1NJTzdfcU1B?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxQMTdVWXJXZVV6SEJjNTl1c3RUNU1KaDBNandHbjNobHVjajR1Z0VOT3B5cUhueFlDdnN2ZklTTTV6QWp0Y3FFazdHZEwyRmV5Wm1kOURvQ2NkY2VWU19ISjB5clA0eEV6YjdHQldlRXBkVXlfbGw5dzF4cjhXZk9EZkxwYjVkMHNZcS1WY2dPTnNZR3A0MF9VVWZHRFd2bl9aNTdpUXNjRnhuOTRRUXp1TVNEbVM2SGZWN21LQnBqRzBodFZVZ0o4?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxObUVGbm1yZThIOHppbXJNN1NIUHFPM1BnM1hDWXhpOVVPMUZmOHVaVU1lWWptay1wenVIN05BS2xUOU5aZm51OEkwaW9fcTVYV1piODRKbXowazdNcTFJLU50S0JVMnNSQlQ1QTJOWEpES2tZZEZHdFk0Uzk4UXhFUFRueXdyUng5bU04VUpYYmN6SnhtOHY2YjNjTldLOWxwVFFlaWYzMFBqUEFEX0E?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxPMFpXbU5jSk5sYzdFRGhDU2p2X0puVjVxbEpMWVBmVlBETzJSYWs5RmRvMWF2OFpKcEFkQ2QyT0pSMEVnT25JdlNVNkRxNE05MjBoMy00ZURxdlctemo3YWFOSlpKM1ZEdTQ5c3J6d2EzOERrNVlDOXUtb1YyeEd3YUFiOUZjbXd2d2E2N2syR0szV3VYM24xRTdvUk1LQVo0UkNRTHFNOXpfZFhsZkNXU29yajBHQkhhc0lLalY3aw?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxQNzl3YVozazZGRThYdDlEWklreDVRS2hzUnNDcXFDZUpjNUxjbm1adFNaTWtRSWRVYkUtSzFxZ1U0RVFCNnJpZnZQYzhubUZYYnRSNjZYWEVsZjZncm5kQ0xpSDVwWFdoaDNiWl9XUmQ1RTQ4LTJ5bkJFLWRMeUpremluV3Q0TUVVdkhwMkVXd1AyWGRPQVBySHYwTVFyeGxPN01mSTVQSW5FUHlReDFSTllQTFFXTnRXTXhWaFExMNIBxAFBVV95cUxPQWVFV253MkNwaVBQdU96ZVoyTW4zN0NDNUNvWjBjMnJCZTZ4czE4bEc4MWZzbDlNZl9saFNkZllxMXZYUVdNTmpxanFWUzNGeldqNFFmUjEwQXptQlZ0dGQtaHhFRko1ckZmYTF5Q3B1WTNWR3ljU1J5QzBZTGV6ZHZDeURHTGliMDVNbjJqT2gtNnVkeENDVGRMYWcwQTR0NHM2UXM1Ql83TndpVlZmeXFjTGVEd2NYMnQ1V2dDWnFrOXBZ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
