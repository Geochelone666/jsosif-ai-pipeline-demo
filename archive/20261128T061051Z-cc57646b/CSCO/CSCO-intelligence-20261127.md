# CSCO Intelligence Report

- ticker: **CSCO**
- Report as_of: **2026-11-27**
- Market data as_of: **2026-11-27**
- Quant sources: https://finance.yahoo.com/quote/CSCO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/CSCO/key-statistics/
- AI analysis snapshot as_of: **2026-11-27**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-28T06:19:37.664641+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 10, 'ai': 11, 'unknown': 0, 'irrelevant': 4})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **9** exact headline/source/date matches; prior report **20261127T063646Z-c0c26981/CSCO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'directional_claim_without_event_type': 1, 'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 12 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 16.0%; oldest publication 2026-11-23

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 97.0400 |
| Return 1D (%) | 3.0149 |
| Return 1W (%) | 7.0609 |
| Return 1M (%) | -12.8748 |
| Return YTD (%) | 28.3091 |
| Return 1Y (%) | 29.9284 |
| Annualized volatility (%) | 38.1585 |
| Beta vs SPY | 1.3207 |
| Max drawdown (%) | -29.7448 |
| Sharpe (rf=0) | 0.8527 |
| Downside deviation (rf=0, %) | 26.6213 |
| Sortino (rf=0) | 1.2222 |
| Historical VaR 95% (1D, %) | 3.2248 |
| Historical ES 95% (1D, %) | 5.6237 |
| Correlation vs SPY | 0.5199 |
| Tracking error vs SPY (%) | 32.9499 |
| P/E (trailing) | 25.81 |
| P/B | 7.40 |
| EV/EBITDA | 19.24 |
| Revenue growth (%) | 24.40 |
| Forward P/E (estimate) | 16.02 |
| Gross margin (%) | 64.07 |
| Operating margin (%) | 27.17 |
| Return on equity (%) | 30.38 |
| Free cash flow yield (%) | 2.72 |
| MA50 | 105.0472 |
| Close vs MA50 (%) | -7.6225 |
| MA200 | 102.3156 |
| Close vs MA200 (%) | -5.1562 |
| RSI (14, Wilder) | 46.0671 |
| MACD (12,26) | -3.1560 |
| MACD signal (9) | -3.3736 |
| MACD histogram | 0.2176 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'CSCO': 291, 'SPY': 291}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 97.0400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 3.0149 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 7.0609 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -12.8748 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 28.3091 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 29.9284 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 38.1585 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 26.6213 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.2222 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.2248 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.6237 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5199 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 32.9499 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.3207 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -29.7448 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.8527 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 16.0215 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 64.0740 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 27.1720 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 30.3800 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.7211 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 25.8085 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 46.0671 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.2176 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -7.6225 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -5.1562 -> Clearly below the moving-average trend level.

## TAILWINDS

### Cisco (CSCO) Upgraded to Strong Buy: Here's Why
- Summary: Cisco (CSCO) Upgraded to Strong Buy: Here's Why
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNSl9EeTdhSHRCdWxoeHExUDVzY242ZnVIczFmQm5iOFRlNGRXdUdMcTUxWllQd3I2MlBQcERObEpsaGJ1dnRTV1lMaklQZi1nUFhsb251OUNTMndyTWFpR1VRTVJiT3J4M0VNYTd5X0JxeTRNWHYzaU42bVZLaEY1MFJSOUtsbFZNTkIxSkdsNmotMmdfeWM5aER2QQ?oc=5>

### Cisco Systems Inc Stock (CSCO) Moved Up by 3.04% on Nov 27: What Investors Need To Know
- Summary: Cisco Systems Inc Stock (CSCO) Moved Up by 3.04% on Nov 27: What Investors Need To Know
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxPeVdES3JpTV9uZUx1M1Nta2hIYjNkOWc4bHgtRFJYTG1vRlg1ZEZUbS1kb1ZFOGk0cDdIbTJ0MmN2dGdZaWJ3dXhxc3JiejlBQnJXamxrc0RjWVJxTHFldmdnWDkwZWlHTV9rWUZ3OFVLSmFvM3YyUHQwcmNMVi10cElYeHBnU3RIQWxV?oc=5>

### Cisco Systems (NASDAQ:CSCO) Shares Up 3.1% - Here's Why
- Summary: Cisco Systems (NASDAQ:CSCO) Shares Up 3.1% - Here's Why
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxNc18yM2ZlYVBYcEtPRTRHTE5TQ05STHR4YllRV3YzeVdOdktWeG1uNlBQYTE2dTlyb1JiTGZWWlVfUXNIUzNGZXlNckk1TDA0VnJsS2dLUTFzWGZiODJNTHZsS1VVVWVXRlA0dGwtVTNMdkwxVHlRVnpISVFDV0dZLUg1WFlrZWM2MHFjLWVLSVpCTlZXVFZlQlc2NXNSdkZ3aUFXUlI4clQ5Nk5q?oc=5>

### Cisco Systems Inc Stock (CSCO) Moved Up by 6.44% on Nov 23: Key Drivers Unveiled
- Summary: Cisco Systems Inc Stock (CSCO) Moved Up by 6.44% on Nov 23: Key Drivers Unveiled
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxOdEUwVkdOckx1ZUhBUVhfc1VpWk1jckhFYmFkc2ZkamNlOTlMdy14ZE8xX1BsN1Z4eENlRHJESFBHckNkd3FDUEVjLUNWUlBOdlJ1M0MxaEVfdWI4bGFCLUM5U2N1cVIxMGNQYUtvcVZneUIzc3BuanE4MmRpeGRVak9BN1NJTzdfcU1B?oc=5>

### Cisco Systems (NASDAQ:CSCO) Stock Jumps 6.8% - Here's Why
- Summary: Cisco Systems (NASDAQ:CSCO) Stock Jumps 6.8% - Here's Why
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxQaHZ4VHhKWW9SaGUtMjY3elhGSzlrX2ZMUWwwNURmcUJpR0hwVnZaM1ItT1RhR0FiQVBVWW1ubUZJc2k1bHF1SGlmaEJsazNMMGxEWWlPdHN0UnltcTBpRllHTzFOTWdXd2xvUzdobWxNaEljSF9DcFlDcDF6YnhTNDliQ0ktcVpNT3JtNUJjY0xMTU14MHA2WWtFZEhqazdlR1Y3WDFMUmhJdC1PeHU0?oc=5>

### Cisco Systems Inc (CSCO) Shares Surge 3.0% -- What GF Score of 9
- Summary: Cisco Systems Inc (CSCO) Shares Surge 3.0% -- What GF Score of 9
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxPV0lfeGFGZVBUNWE0MzlhSjR1NXhwV25uTEZuRHZSSS1HU1NWU29aMmZMNEZ5WmlnenF3bzE0QlNkOVowaE9odWJwNGdNUy13bDZzMVVwR1RneDFzVzdQeEJDUlJfa2ptWURsQ1dpUUhyeDBnR0RQNkZTMzVMS1hEdzZqeHExaTBuT2QzVC0wX2VjTzBLWC03UEdsSzU3OXBoRU9SY0J0Q1ExdFVOd0pKQ0pqbw?oc=5>

### Why Did Cisco Stock Jump?
- Summary: Analysis of factors contributing to recent Cisco stock price increase.
- Date: 2026-11-24 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxNblpEQURxbGlHZkNyTVVzNGpzQkhGQlJDYUpoend5OGJzY1F3M1JFeDVMQkxZYjE1VkFXbmRjUzlNOHFmZDhvSVoySFltcjZJSmlRcGdtMEtPTXZfWEFYYlNVVXRvbTNURE44dmJVNmIxU3BiQnBtVTN3c3REYTVBc3ZrNTVKcVE5RGczWmxR?oc=5>

### Cisco (CSCO) Stock May Be 29% Undervalued As AI Security News Builds
- Summary: Analysts suggest CSCO may be undervalued by 29% amid growing AI security demand.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxOYWQwYmJ5a2plUENjZmVDMFFoemhxWnRHYTd1Um5xamxIbHM1TGJfVEdXaWJycFluY1A4NUhEM2FqNVgyQnQ1YUtiVUs2VHBESkk1UHFUOWJUZU92cVUwSXc1VEN1aHF4ODFnOGxhWnhReDlxdzN1R1NyeGJ1Vk5Dd3BteDZEbzBrSlJTbWpPN0s5dw?oc=5>

### Cisco (CSCO) Stock Still Looks Cheap Despite Its 118% Run
- Summary: Stock perceived as undervalued, suggesting potential upside.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxPYjJJTmVsSVM2Y3ROQmh3REJfZDBfSGE2R2wzQjFyT0tjYVlmRkI5RWdZSktRYzhvSTE1d3BBVFBHV1I2VnZuNTZsd09lVkI3ZmNjcDIxc0VQWnlfMHktM0dORDdsNlliM3RLQS1SMW40M0x1eFBacXdWVWE5SnBOUkdtSWJwa0dtMXZhOExuZTRvMHVpbUtkdVZ4bWZTYVNxam1FdkdKSTZhbDNNR3VfWTZ3ajlUekloZC1oNmpTMNIBxAFBVV95cUxNSDVBRjFLNnEtUWpzMV9sbGJmRmRCZ0VhMTJJNEdhYnh5WFVyams1TVdBcnVsVEZfVndEcXk4RmxfZTNLbDF0SXFreWNpZTNsVlIwS1dnWVhVSWVPWEFQNEh6aXkwUkl6M3c2cWwySjRpUHBLS184OV94SG9ld1FSMDFncU81dkJNZ2o5N2l2Vm11VkMyZzBxWEhiSEdSMXFJd3dBaHVqYWU2R0ZjaEk2OEFoNXN6TkwwVWtuVUlXbk5GMk54?oc=5>

### 50 ETFs Add to Cisco (CSCO) Holdings on Nov. 25
- Summary: Fifty ETFs increased their Cisco holdings, indicating growing institutional confidence in the company.
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxNbFE1bDIwV3BpQ3BkWU9XN2Z0cGtaenJWQVBaTVlQbDhzYW9vbF8wZFprVWFfTWhZVnVxZ0hsTHdYcjRSUG41cUlIZ19JNlNoUkVSM2p1QTlQZnY1Q0NyTlNocXFyZ2xfeWhuaXdzMnFGRUo3eEFzU21MT2V5LWNFOC1jNFNKSzNNR05n?oc=5>

## HEADWINDS

### Cisco Systems Inc Stock (CSCO) Moved Down by 3.99% on Nov 24: Facts Behind the Movement
- Summary: Cisco Systems Inc Stock (CSCO) Moved Down by 3.99% on Nov 24: Facts Behind the Movement
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxQd0xJckRWTHZOX1B1S3ZGQ2tURkU4a2RNTE9ZdWV3dXZVdnlPTmhSd0NtTmJyVmNSSFhBVTRVVFJfR0JoS20zOVVjYUNTZ0pRRkRFRWVxb3BOQk1mZnlXOEswZG81bWw5dGRkQ0gyYmY4bXVXZzQyYmc0RGlvOFdqWGtPMm1OejVTc0lv?oc=5>

### Cisco Systems (NASDAQ:CSCO) Stock Falls 2.9% - Here's What Happened
- Summary: Cisco Systems (NASDAQ:CSCO) Stock Falls 2.9% - Here's What Happened
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxPWHdPM2dzUW1NdlRaOTRNd3UwU3ptbU5ubTM2OXJZYzlYdTlqd21EZmctOXZGSlRNOEl4czFCT0RzSFkwZXFCYU5kM2JsMEZOVl84NkM1eGktcXhSWkxKMzJoYUNJbkNJRlZ4akhEV0tPSjZoZ2RYSThTQ0FhSktjU201NngyQXhKXy1HNzlieEk5NUxMcWx1WjNjbmQ1TFB2RmRqS19lNFhuUURfNVNaeWNoTG1rdDlEWFFrTQ?oc=5>

### Cisco Slides as Tech Pullback and Profit-Taking Weigh on Shares
- Summary: Cisco Slides as Tech Pullback and Profit-Taking Weigh on Shares
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxPR09qVGkwR0hzSmJlSFBHa080TEt2cHhSSjhsSXF6R1RtV0ZULWJWN01tRXJpM0tnczNKeGJVS2xFUU9vZTNjRkZsTnlJMTBKOFZSUkFTeldtdkdzQ1NDZHhYVGxOSmVOdy1LN20yaVNJV2EwSEdqRTg2YzlmWDJjWWRFNGM0SUFBMXdXMzdGelBRNGpRendGVFkwa1k?oc=5>

## CATALYSTS

### Cisco Systems, Inc. (CSCO) - What Are Analysts Saying About This Stock?
- Summary: Cisco Systems, Inc. (CSCO) - What Are Analysts Saying About This Stock?
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxPM3ZtdUpuUWJsTHIycGc5Zks1dGpGcjNfbjBjZGNyWEwwRWFseXBXMjg5eXVTNnpNekxrVXJleXpUNHhQWXQxQ2thbGRrbU5lWDZkRG5PZkN5UWJLeDVjcS1iTjk1bk5ZU3lUcHlza0d4VkN5NjVWWWxveGk0NWZ5X3p2Uk1SeHhtTm1GZnBSZHB0MzE4ZEdKTW4yUmJRZW0zRHNjN0I5RThrSVJZbEJFNEh6Y01hOUNfOEFqUXAzZHdEbWhCOW9j?oc=5>

### Can Cisco Stock Hit $120?
- Summary: Speculation on whether Cisco stock can reach $120.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxQTlB1aWlkZlVUd1pFYkpGVzhlaDUtWEs1MHhyZlVQUkV4bkRjdWRLbmdLME1McGRvNDIwMFgtVkVqcUhHOGhocDZsX2l5SExvTW1iY3pGRzRNamVFcDZWZ2xuREN6aTN4Sm9tcEp2M3RDRmhfbUdlZXhBS0RFREcwZGJjVmN0Z0g1TnFRSg?oc=5>

### A new Cisco-OpenAI tool can protect systems while teams work on a fix.
- Summary: Cisco and OpenAI collaborate on a tool enhancing system protection during fixes.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxPMFpXbU5jSk5sYzdFRGhDU2p2X0puVjVxbEpMWVBmVlBETzJSYWs5RmRvMWF2OFpKcEFkQ2QyT0pSMEVnT25JdlNVNkRxNE05MjBoMy00ZURxdlctemo3YWFOSlpKM1ZEdTQ5c3J6d2EzOERrNVlDOXUtb1YyeEd3YUFiOUZjbXd2d2E2N2syR0szV3VYM24xRTdvUk1LQVo0UkNRTHFNOXpfZFhsZkNXU29yajBHQkhhc0lLalY3aw?oc=5>

### What Drove the Fastest Revenue Growth in Years at Cisco (NASDAQ:CSCO)?
- Summary: Analyst inquiry into Cisco's rapid revenue growth, exploring underlying drivers.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxQN1RXZlp0Ny1lYVFuS2ZIWm8xWnMxYzY1anZ0NzFwXzlMLVhjMFczUHpzbkhyY2U2N3pZRWlRRFhWajR2enNpRVdtOG1SaEE1Q1pxVF8tbWZPUXlibFY4ZlJreWdMMlRfVjNQc2RTbHBaYTdmUzE5UnV3cTlnRTRySC1paEh0VEstNlN0ZTgxdGRtVXdnRi1CanBhdzZXOVlYQW1Kc0M2aERQbWl1X3ow?oc=5>

### Cisco Short Interest Rises After Q1 2027 Results
- Summary: Short interest increased following Q1 2027 earnings, indicating investor skepticism.
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxNeVhfNTU2R1FUVFhEQks5Mm9HaWFCQ3JtRE1ZUDF5Z25tdGVScUZEWjhfc3VhQ1hmM1BMTVdrZUluZlZVMXB5ck00NmJRSWxiUUhZZXFkNUtwR1l2bjJJc2JIbjEtQ1hzX2hnb2ppbXBFd1BENjRNTmhYT0FhamxRWHItcXFYT3FtaWZ2TUJrbTE0LUJkSjZfV0NpMnJIZ1RMNEhKbFFsd3pQQnNLZk5TRE40c1A?oc=5>

### Wall Street Analysts Think Cisco (CSCO) Is a Good Investment: Is It?
- Summary: Analysts view Cisco favorably, suggesting potential upside for investors.
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxOb3lsQ2pZR1JLWVN1VC03SGctNHJfektxR082RHY5V1NkN0d4TjBneWFPTFdsYTNCNG40OGFYRVVOWGhHSFllNE5INEJIYmFHRnB0NjVQdEFDUkFHdlYyS0lQcGR1R2VlU2lVbFV2cms1S0EzbHN3czZHX0FhZlkzMVZ2Wnc0aXluN2VYOU5xY3BHWktmVEN6cE4yY3k1Zw?oc=5>

### Cisco Gains From AI Networking Boom: Can It Outpace HPE & ANET?
- Summary: Cisco benefits from AI networking surge, potentially surpassing competitors.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxOVEtaUG52NHllNGUzWHNWRy1qLVNUMTR3RlVXVHdWTUVfbFZyUkJuamU5V0w5NjQ2ZktWQ2d5QlllNUFrX3RPcGFRWnZlSHplcFptSTBtcFRJWWtJS3c4UmVGM2d6b2RmRWRpWi1DQzlVOTBvQVJRRnVPb3AxZFFYWHZTNmhJZDhmWFgzekF3QUxuemZkWVVYSV93?oc=5>

### Cisco Systems (CSCO) Stock Price Prediction: Record earnings meet a fragile rebound in Cisco shares
- Summary: Predicted stock rebound amid record earnings, though fragile market conditions persist.
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxQMHRpTkY4OV9acTBmckR3YXYyMWd5VUVJbDdRaldmVnNDT25FWngxYzJENHZuVkU4My05OHZ1UVZKVTFrZzVxUWFiOEl4NWdTZXRtU2R0ZWRSZFc1bUZCaDZBWjlaalcxUzRoWW5KXzl6TkJoa08wMW14RkExU2pxVVNDYjh5WGlXa2kxVlEtc3hHQ0FKb1A3WEtCZXd5bmM?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **CSCO** | **25.81** | **7.40** | **19.24** | **24.40** | **382,575,181,824.00 USD** | **29.93** |
| ANET | 46.84 | 13.42 | 38.91 | 58.50 | 220,754,296,832.00 USD | 36.88 |
| FFIV | 25.79 | 4.58 | 18.48 | 13.30 | 18,382,385,152.00 USD | 35.53 |
| HPE | 13.93 | 2.04 | 8.24 | 50.30 | 56,272,158,720.00 USD | 102.19 |

Peers fetched as_of: 2026-11-27; CSCO reuses existing data (market data as_of: 2026-11-27); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-12
- Next expected earnings: 2027-02-10 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-27

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

- https://news.google.com/rss/articles/CBMimwFBVV95cUxNSl9EeTdhSHRCdWxoeHExUDVzY242ZnVIczFmQm5iOFRlNGRXdUdMcTUxWllQd3I2MlBQcERObEpsaGJ1dnRTV1lMaklQZi1nUFhsb251OUNTMndyTWFpR1VRTVJiT3J4M0VNYTd5X0JxeTRNWHYzaU42bVZLaEY1MFJSOUtsbFZNTkIxSkdsNmotMmdfeWM5aER2QQ?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxPeVdES3JpTV9uZUx1M1Nta2hIYjNkOWc4bHgtRFJYTG1vRlg1ZEZUbS1kb1ZFOGk0cDdIbTJ0MmN2dGdZaWJ3dXhxc3JiejlBQnJXamxrc0RjWVJxTHFldmdnWDkwZWlHTV9rWUZ3OFVLSmFvM3YyUHQwcmNMVi10cElYeHBnU3RIQWxV?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxNc18yM2ZlYVBYcEtPRTRHTE5TQ05STHR4YllRV3YzeVdOdktWeG1uNlBQYTE2dTlyb1JiTGZWWlVfUXNIUzNGZXlNckk1TDA0VnJsS2dLUTFzWGZiODJNTHZsS1VVVWVXRlA0dGwtVTNMdkwxVHlRVnpISVFDV0dZLUg1WFlrZWM2MHFjLWVLSVpCTlZXVFZlQlc2NXNSdkZ3aUFXUlI4clQ5Nk5q?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxOdEUwVkdOckx1ZUhBUVhfc1VpWk1jckhFYmFkc2ZkamNlOTlMdy14ZE8xX1BsN1Z4eENlRHJESFBHckNkd3FDUEVjLUNWUlBOdlJ1M0MxaEVfdWI4bGFCLUM5U2N1cVIxMGNQYUtvcVZneUIzc3BuanE4MmRpeGRVak9BN1NJTzdfcU1B?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxQaHZ4VHhKWW9SaGUtMjY3elhGSzlrX2ZMUWwwNURmcUJpR0hwVnZaM1ItT1RhR0FiQVBVWW1ubUZJc2k1bHF1SGlmaEJsazNMMGxEWWlPdHN0UnltcTBpRllHTzFOTWdXd2xvUzdobWxNaEljSF9DcFlDcDF6YnhTNDliQ0ktcVpNT3JtNUJjY0xMTU14MHA2WWtFZEhqazdlR1Y3WDFMUmhJdC1PeHU0?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxPV0lfeGFGZVBUNWE0MzlhSjR1NXhwV25uTEZuRHZSSS1HU1NWU29aMmZMNEZ5WmlnenF3bzE0QlNkOVowaE9odWJwNGdNUy13bDZzMVVwR1RneDFzVzdQeEJDUlJfa2ptWURsQ1dpUUhyeDBnR0RQNkZTMzVMS1hEdzZqeHExaTBuT2QzVC0wX2VjTzBLWC03UEdsSzU3OXBoRU9SY0J0Q1ExdFVOd0pKQ0pqbw?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxNblpEQURxbGlHZkNyTVVzNGpzQkhGQlJDYUpoend5OGJzY1F3M1JFeDVMQkxZYjE1VkFXbmRjUzlNOHFmZDhvSVoySFltcjZJSmlRcGdtMEtPTXZfWEFYYlNVVXRvbTNURE44dmJVNmIxU3BiQnBtVTN3c3REYTVBc3ZrNTVKcVE5RGczWmxR?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxOYWQwYmJ5a2plUENjZmVDMFFoemhxWnRHYTd1Um5xamxIbHM1TGJfVEdXaWJycFluY1A4NUhEM2FqNVgyQnQ1YUtiVUs2VHBESkk1UHFUOWJUZU92cVUwSXc1VEN1aHF4ODFnOGxhWnhReDlxdzN1R1NyeGJ1Vk5Dd3BteDZEbzBrSlJTbWpPN0s5dw?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxPYjJJTmVsSVM2Y3ROQmh3REJfZDBfSGE2R2wzQjFyT0tjYVlmRkI5RWdZSktRYzhvSTE1d3BBVFBHV1I2VnZuNTZsd09lVkI3ZmNjcDIxc0VQWnlfMHktM0dORDdsNlliM3RLQS1SMW40M0x1eFBacXdWVWE5SnBOUkdtSWJwa0dtMXZhOExuZTRvMHVpbUtkdVZ4bWZTYVNxam1FdkdKSTZhbDNNR3VfWTZ3ajlUekloZC1oNmpTMNIBxAFBVV95cUxNSDVBRjFLNnEtUWpzMV9sbGJmRmRCZ0VhMTJJNEdhYnh5WFVyams1TVdBcnVsVEZfVndEcXk4RmxfZTNLbDF0SXFreWNpZTNsVlIwS1dnWVhVSWVPWEFQNEh6aXkwUkl6M3c2cWwySjRpUHBLS184OV94SG9ld1FSMDFncU81dkJNZ2o5N2l2Vm11VkMyZzBxWEhiSEdSMXFJd3dBaHVqYWU2R0ZjaEk2OEFoNXN6TkwwVWtuVUlXbk5GMk54?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxNbFE1bDIwV3BpQ3BkWU9XN2Z0cGtaenJWQVBaTVlQbDhzYW9vbF8wZFprVWFfTWhZVnVxZ0hsTHdYcjRSUG41cUlIZ19JNlNoUkVSM2p1QTlQZnY1Q0NyTlNocXFyZ2xfeWhuaXdzMnFGRUo3eEFzU21MT2V5LWNFOC1jNFNKSzNNR05n?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxQd0xJckRWTHZOX1B1S3ZGQ2tURkU4a2RNTE9ZdWV3dXZVdnlPTmhSd0NtTmJyVmNSSFhBVTRVVFJfR0JoS20zOVVjYUNTZ0pRRkRFRWVxb3BOQk1mZnlXOEswZG81bWw5dGRkQ0gyYmY4bXVXZzQyYmc0RGlvOFdqWGtPMm1OejVTc0lv?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxPWHdPM2dzUW1NdlRaOTRNd3UwU3ptbU5ubTM2OXJZYzlYdTlqd21EZmctOXZGSlRNOEl4czFCT0RzSFkwZXFCYU5kM2JsMEZOVl84NkM1eGktcXhSWkxKMzJoYUNJbkNJRlZ4akhEV0tPSjZoZ2RYSThTQ0FhSktjU201NngyQXhKXy1HNzlieEk5NUxMcWx1WjNjbmQ1TFB2RmRqS19lNFhuUURfNVNaeWNoTG1rdDlEWFFrTQ?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxPR09qVGkwR0hzSmJlSFBHa080TEt2cHhSSjhsSXF6R1RtV0ZULWJWN01tRXJpM0tnczNKeGJVS2xFUU9vZTNjRkZsTnlJMTBKOFZSUkFTeldtdkdzQ1NDZHhYVGxOSmVOdy1LN20yaVNJV2EwSEdqRTg2YzlmWDJjWWRFNGM0SUFBMXdXMzdGelBRNGpRendGVFkwa1k?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxPM3ZtdUpuUWJsTHIycGc5Zks1dGpGcjNfbjBjZGNyWEwwRWFseXBXMjg5eXVTNnpNekxrVXJleXpUNHhQWXQxQ2thbGRrbU5lWDZkRG5PZkN5UWJLeDVjcS1iTjk1bk5ZU3lUcHlza0d4VkN5NjVWWWxveGk0NWZ5X3p2Uk1SeHhtTm1GZnBSZHB0MzE4ZEdKTW4yUmJRZW0zRHNjN0I5RThrSVJZbEJFNEh6Y01hOUNfOEFqUXAzZHdEbWhCOW9j?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxQTlB1aWlkZlVUd1pFYkpGVzhlaDUtWEs1MHhyZlVQUkV4bkRjdWRLbmdLME1McGRvNDIwMFgtVkVqcUhHOGhocDZsX2l5SExvTW1iY3pGRzRNamVFcDZWZ2xuREN6aTN4Sm9tcEp2M3RDRmhfbUdlZXhBS0RFREcwZGJjVmN0Z0g1TnFRSg?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxPMFpXbU5jSk5sYzdFRGhDU2p2X0puVjVxbEpMWVBmVlBETzJSYWs5RmRvMWF2OFpKcEFkQ2QyT0pSMEVnT25JdlNVNkRxNE05MjBoMy00ZURxdlctemo3YWFOSlpKM1ZEdTQ5c3J6d2EzOERrNVlDOXUtb1YyeEd3YUFiOUZjbXd2d2E2N2syR0szV3VYM24xRTdvUk1LQVo0UkNRTHFNOXpfZFhsZkNXU29yajBHQkhhc0lLalY3aw?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxQN1RXZlp0Ny1lYVFuS2ZIWm8xWnMxYzY1anZ0NzFwXzlMLVhjMFczUHpzbkhyY2U2N3pZRWlRRFhWajR2enNpRVdtOG1SaEE1Q1pxVF8tbWZPUXlibFY4ZlJreWdMMlRfVjNQc2RTbHBaYTdmUzE5UnV3cTlnRTRySC1paEh0VEstNlN0ZTgxdGRtVXdnRi1CanBhdzZXOVlYQW1Kc0M2aERQbWl1X3ow?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxNeVhfNTU2R1FUVFhEQks5Mm9HaWFCQ3JtRE1ZUDF5Z25tdGVScUZEWjhfc3VhQ1hmM1BMTVdrZUluZlZVMXB5ck00NmJRSWxiUUhZZXFkNUtwR1l2bjJJc2JIbjEtQ1hzX2hnb2ppbXBFd1BENjRNTmhYT0FhamxRWHItcXFYT3FtaWZ2TUJrbTE0LUJkSjZfV0NpMnJIZ1RMNEhKbFFsd3pQQnNLZk5TRE40c1A?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxOb3lsQ2pZR1JLWVN1VC03SGctNHJfektxR082RHY5V1NkN0d4TjBneWFPTFdsYTNCNG40OGFYRVVOWGhHSFllNE5INEJIYmFHRnB0NjVQdEFDUkFHdlYyS0lQcGR1R2VlU2lVbFV2cms1S0EzbHN3czZHX0FhZlkzMVZ2Wnc0aXluN2VYOU5xY3BHWktmVEN6cE4yY3k1Zw?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxOVEtaUG52NHllNGUzWHNWRy1qLVNUMTR3RlVXVHdWTUVfbFZyUkJuamU5V0w5NjQ2ZktWQ2d5QlllNUFrX3RPcGFRWnZlSHplcFptSTBtcFRJWWtJS3c4UmVGM2d6b2RmRWRpWi1DQzlVOTBvQVJRRnVPb3AxZFFYWHZTNmhJZDhmWFgzekF3QUxuemZkWVVYSV93?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxQMHRpTkY4OV9acTBmckR3YXYyMWd5VUVJbDdRaldmVnNDT25FWngxYzJENHZuVkU4My05OHZ1UVZKVTFrZzVxUWFiOEl4NWdTZXRtU2R0ZWRSZFc1bUZCaDZBWjlaalcxUzRoWW5KXzl6TkJoa08wMW14RkExU2pxVVNDYjh5WGlXa2kxVlEtc3hHQ0FKb1A3WEtCZXd5bmM?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
