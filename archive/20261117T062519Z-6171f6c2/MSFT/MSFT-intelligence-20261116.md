# MSFT Intelligence Report

- ticker: **MSFT**
- Report as_of: **2026-11-16**
- Market data as_of: **2026-11-16**
- Quant sources: https://finance.yahoo.com/quote/MSFT/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/MSFT/key-statistics/
- AI analysis snapshot as_of: **2026-11-16**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-17T06:34:25.855808+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 4, 'ai': 17, 'unknown': 0, 'irrelevant': 4})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **9** exact headline/source/date matches; prior report **20261116T043911Z-b81cfeb4/MSFT** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 16 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 32.0%; oldest publication 2026-11-13

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 517.9900 |
| Return 1D (%) | -1.1243 |
| Return 1W (%) | -4.9873 |
| Return 1M (%) | -2.0905 |
| Return YTD (%) | 7.7863 |
| Return 1Y (%) | 2.3662 |
| Annualized volatility (%) | 34.0343 |
| Beta vs SPY | 1.0035 |
| Max drawdown (%) | -30.0352 |
| Sharpe (rf=0) | 0.2518 |
| Downside deviation (rf=0, %) | 21.7619 |
| Sortino (rf=0) | 0.3938 |
| Historical VaR 95% (1D, %) | 2.8549 |
| Historical ES 95% (1D, %) | 4.1000 |
| Correlation vs SPY | 0.4059 |
| Tracking error vs SPY (%) | 31.1043 |
| P/E (trailing) | 27.03 |
| P/B | 8.18 |
| EV/EBITDA | 19.04 |
| Revenue growth (%) | 18.80 |
| Forward P/E (estimate) | 21.41 |
| Gross margin (%) | 67.66 |
| Operating margin (%) | 47.10 |
| Return on equity (%) | 34.22 |
| Free cash flow yield (%) | 0.08 |
| MA50 | 519.3630 |
| Close vs MA50 (%) | -0.2644 |
| MA200 | 440.9438 |
| Close vs MA200 (%) | 17.4730 |
| RSI (14, Wilder) | 46.3741 |
| MACD (12,26) | 1.0099 |
| MACD signal (9) | 3.2864 |
| MACD histogram | -2.2765 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'MSFT': 283, 'SPY': 283}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 517.9900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.1243 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -4.9873 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -2.0905 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 7.7863 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 2.3662 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 34.0343 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 21.7619 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.3938 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.8549 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.1000 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4059 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 31.1043 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.0035 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -30.0352 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.2518 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 21.4073 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 67.6570 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 47.1040 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 34.2210 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 0.0778 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 27.0350 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 46.3741 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -2.2765 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -0.2644 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 17.4730 -> Clearly above the moving-average trend level.

## TAILWINDS

### Microsoft Corporation (MSFT) is Attracting Investor Attention: Here is What You Should Know
- Summary: Microsoft draws investor interest, potentially boosting demand for its shares.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxQNHdZOGRjaEJQWVQ5Tm9NMklaaGwyWHRFX3VYLU0xMmpBbVI2anJxTjZoQXI0eGpOVno3c3BRS1Z2a0kxSWFVRFFuNzU4WGdWNDl3S3RRb0lYeVhLVEY4aHF2aTNYNXFKbWxFU3ZvUU93WUlZT3hwVlQzQzgtR21EX0FkOTh2N0pMUXlhaWlaVUdqbHZTTGVkdzR5a0tDa2l5dDBDdXR6NC03TFJYLXJNUA?oc=5>

### Microsoft: Azure Accelerates And Cash Conversion Becomes The Test (NASDAQ:MSFT)
- Summary: Azure growth boosts cash conversion, signaling strong cloud performance.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxQWHVqMGZtQ1hFMURfLTdmMXg1RXUyQVVvckZqc3BMbEE1YWVMSjhlNlU5MDZVc1FjWGJyQXdoeXlzN1REenRsWmJTWWhadVNON3BHMnpSVTdHU2xQYWk3VENySm01YTJfOUJ6REg3WWtIZmhWLVB3cGNRNVF2U0l1WFNudXRVRE1zNjhHRWpRV2gwSVBzVkluVHRRRzFNeTZUcHkwZFFuUDI?oc=5>

## HEADWINDS

### Microsoft Stock (NASDAQ:MSFT) Slips as Massive Outlook Outage Post-Mortem Begins
- Summary: Microsoft Stock (NASDAQ:MSFT) Slips as Massive Outlook Outage Post-Mortem Begins
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxPY2ZBT0k0ZkJ2N1Utb2k5RjIyWnp0SzNQQnhITVdET1Awa09pWmtyekJrekxqVXJaVzAwZkRDTmpaaWVyWGpJdGZ2Qi1ZTnNTeW9rRmtZd0lPdUY1WnNIcnFrZmdlODYxQ3lYbVJubjdUdElYOE04M09ZM0NrNGd5NWNEb0lXRXViaXNHMXhDSklLanN4Wi1QZXJHMWdIUk1MVktTbHdWdDJoWFk?oc=5>

### Microsoft Stock Falls as Outage Tests Its Copilot Push
- Summary: Microsoft Stock Falls as Outage Tests Its Copilot Push
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxQX19ZTTZXQk1LYXpjVmJvTDY4dVY2VUpmc3pOS3R4TS11WU1WSkpOMHJNNHRnVDhpMTNmdWhHN204QkFFYmtLWnBRWlkwaGNrQ0dfVVZlb1oxV1dieTdHS1hxNWpWSmRkWmNKU3A0OHdVbnc4YzNhejgweGZtd2pqeHhhYTlzdE5fWkFN?oc=5>

### Microsoft Stock Drops as Global Outage Cripples Outlook, Teams and Copilot
- Summary: Microsoft Stock Drops as Global Outage Cripples Outlook, Teams and Copilot
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxQTFM2V2hLWVoxbk1yckIxNUlkekhjeU5xUkFUXzY4eVRMbEU3enJFX1J2X2pTTWxtVTNPVnFMT3hCYVlVcjA0ZUxrODdoS2cxRzU0Y3lXb2tWSF9iZmUzZDZpMVpvMTNvbXlZZGE1dF8xWVMxenhhbEZLRDBHdmtsV09fVUpBMHpsaWNzSw?oc=5>

### Why the Microsoft Outage Came at the Worst Possible Time for the Stock
- Summary: An outage coincides with a stock dip, hurting investor sentiment.
- Date: 2026-11-14 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMigAFBVV95cUxQRUtKYTY3Q0wwdDR0WDQ0NlBVV0xsZVEzM0J5aDVUd1hrX2VBOXFTbks4Z2JFZFF6RG9TNjVIb3ZNRl9KRUJvNGxnYlgzQzBKbWVYWDFuU3F2X2VBdU5UWVo1OWVFOHpUX0E3RHNmNXBJQTE0dVU2R0dUS3pvVWhGNQ?oc=5>

### ‘SaaSpocalypse’ Fears Hit Microsoft Stock Again. Don’t Rush to Buy the Dip.
- Summary: Continued SaaS concerns pressure MSFT shares.
- Date: 2026-11-13 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxNaGtTRGVaNHpadHlTY1NJQy1mQXpJQ1ZOaFVrY3Z3eU15STMxeE5fbXFuTi1VLWlqdmFYd0xyZ1pBaE1oSE41WC1zWVc4TW04S2s2bDlVMlVHZWZubi1iNFVuRnBUcFV5UXh0WlBoWmQ3Q0lGY3otcWk3eXBSUHRzQi00SEZIcHh3dXc2MEdGdXJWYmpGNTNVMm1BbEdfSTB2STNKTWcyRQ?oc=5>

### The Microsoft outage didn’t lose your email — here’s what it does mean for you
- Summary: Microsoft experienced a service outage affecting email, but no data loss occurred. Users may face temporary disruptions.
- Date: 2026-11-14 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxPT0U5d29Od01qNm5mUGY0WU5hdTN5eTV1M3ZxMUNiMXhzWGZtZWdlOExJZ1ZCLURsTGwxQ1p4OFBRX3hyZGNQN2Jfd2FGRUl6UG1kMzBDYjVTU2J1WnQ3QzdadzQ3ZU9zaEdPUG1XbUhNdmkyc1ktNVVsVW5XUjJBTGpUb3RsbVdaRkpvYVliQl9JWHhrU1Jab0hwVmhGOEZNbFY3NWFyME42bjVpNFZZSXZJS2FwM2ZGZVdzTjI1bUM?oc=5>

### Microsoft Stock Under Fire After Worldwide Blackout
- Summary: Worldwide blackout led to stock under fire.
- Date: 2026-11-13 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxOZHZqMll0OWUzZkFWN1BEY1VZWlZoTE45ZXJaX0NHQWNuZU90bEt3VzVqUzR4NE1tY29SbkxhdVFHTDUwT09kQm9aVmMwZzYwOHBRS3JBcl92MDJQUFJYYlJ4ZjF2RUJhd0ljSFk4TUJZOXZPczB2bFB3S3ZEaDVNS1FDZ0RvYnRVYzE2VmVVWXJFTnBvWGtySXdaYzAybzNZQ2F0VURXMUdpemgzQ1hJ?oc=5>

### Microsoft (MSFT) Is One of NVIDIA’s Biggest Customers, and a Growing Rival
- Summary: Microsoft’s dual role as NVIDIA customer and competitor may create strategic tension.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxQUWl6NDdVVHVoUnJ0TVJBaDRMWW1mX0U2M29TQ2xTbksyaXFWSDI0bldFYTBYOGdPcmN6bWFwSDhjZFpad3RDOFE1SFJ6azJaUDlLN05adEI4TlJfRlJxTW1kWWtqLWs2TjJIeUFVWWlTdUlHMUdfUVI0UzN0UVYySm9UYzM0aGtOTmZPYld3X2lrc3N1Q2RTaTVrbjVwT0E?oc=5>

### Service outage resolution sees Microsoft stock consolidate near $524.98 resistance
- Summary: Service outage resolution leads to stock consolidation near resistance level.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiiAFBVV95cUxQbGlSYXgxbVRod2l2ZDRQczM5Q081VnZvTm1IMzFLM2dKNDc5NFhBY0poN2pnVW5PbFRRSG1SU2w3OUpDS2tObEk1QzBwNWJzMnlBOXcwUDRzOFZwd2M2ellrQmJzS3FFbEV2WHRhMjRxVU95WEtzZHhEc2ZEYlpIb3hIaFRsSkJF?oc=5>

## CATALYSTS

### Microsoft (MSFT) Strikes AI Deal That Broadens Its Chip Supplier Base
- Summary: Microsoft (MSFT) Strikes AI Deal That Broadens Its Chip Supplier Base
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxOX3prYWZxNFJ4T3VWLVVoT0NaUHRrbXg2UkFsX0RYQlRqQ1I3SXByUkVtckxqT1hJbi1Kc3lLUDRKX3loMTdaRVFyTzUxUHN6aVlmUDVIOVVvYVZRQmJYWHRXTUdxdC1Tek5jQ3owWHEzN2JxeTZnYXdkU3gxYm1VSXlWeEhvUmNxd3pjSzk3bnI1Nkpwa2MzRXR3?oc=5>

### Microsoft (MSFT) stock price forecast: Wall Street analysts see 22% upside
- Summary: Analysts project a 22% upside for MSFT shares, indicating bullish outlook.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxQYXJNSTlyS19oSERrUGpmR2pyQ0F4Y1FDZ0hqY0d5R2c4U1o3QlBaRnVJOHZOSmFqMW1kNGYwSGZhY0lZMU4zN3JTZlBzWVFtdWlXSFpYUGE0VWlZVHlwbzVOM1BlQUVjdzJ0alZIc0pXV2dPOXZrN0hxSlE4aEpFTWtlUlpSVFl2MGNsRHQxOHBubVBkbFY0N1VuT05UZw?oc=5>

### Microsoft Ignite Starts Nov. 17. Will Microsoft Update Its Paid Copilot Seat Count?
- Summary: Upcoming Ignite event may introduce new Copilot pricing, impacting product strategy.
- Date: 2026-11-15 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxPdlBJMGRieWdXY3ZYdHJ4WVhhWjlPTWtkN0RrUGNZZVkzUFVGaGtvckpNV3FaS3FYajdrYkE1amlHQ2gtMm10UGo5MFVNM1pqb2VDb0F4aTl6UGhHeldlTEhfejMyOFZ6ZUNhYkpPZTl3WElyNUhldTBxNWFyNjNUazJ2Zm9lWllLeUhtMXFDeUlDd2otaThJNWlDRS1CU0JwN2t6a2hfRXV3Q3o1cENqMVlwcFpLWDBRTmNmZFVFWkM?oc=5>

### Microsoft (MSFT) Unveiled An Enterprise AI Agent Platform
- Summary: Launch of new AI agent platform signals product expansion.
- Date: 2026-11-13 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxPRnJHaU82ZVRoTzZHSVNNT2VVRHZFanRraE0zeFEySnhNMVZfX1lJYUd1SkpDc3pzQ3ZlbUZma1JVb0szc0EzVmFjeFNLWndua0o4U09sWWswMUIzaGJ6Y2k0dVRieURrdFpZYXNsS2Ruc2VBckZJeEdUQlFURjVYeDJ2ZmlqTU00N1JJUlMxN0sxdmdvbFNUVmFfZVJIZFJfRjZv?oc=5>

### Corvex exits Microsoft, raises holdings in Amazon.com, cuts stake in Walt Disney (MSFT:NASDAQ)
- Summary: Shareholder Corvex exits MSFT, increasing Amazon stake, impacting MSFT ownership dynamics.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxQYmVQUUROcXJfcGFPazRSZkExNWVYc25WaVpfNk5HT21rbG5yY3pTU01lSXB4OGZyZVFuaktNNUJvemxIVmI5enlZUzJtdHp6Zy1GUjFXQ3cxeXlBaTJPM1FkZzdhLWJJcUZFa0JQVUQyUXRleGRLSWFILTdSSnBlTUttYTZHaEhtTGtOY2t5eEJ1SG9udnpweS1DOUJQQ3RiRl9pY2R5YWdKLW91ZWRhRGpOZGVWQQ?oc=5>

### Microsoft Stocks Move Lower as $1 Billion Anthropic Bet Precedes Ignite
- Summary: Microsoft's $1B bet with Anthropic ahead of Ignite causes stock dip.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiygFBVV95cUxNOVoybWdIQ2tHakc1SFItZW9rY0dwOTlKZUlnNElFTnBIWHJJd25YQ0dUcTBSTnA4VjZPRGMxMmJ4QmdnTmdGTmhqemMxdlpQX0t0aHIzTmN5aG51Z3AyV2pOSkR6X09pbllPVHFRRlpHQ290THlERmktQnhsOVdrbVlxSnBRcUg0cjNXaDlHdE9xRG1Cc0RRWGYxdl94VkIxbXZ0WkNXb1BmOFptODcxbWRkT3FfQmJzR0RsNFN4WXYwZ0V6Z1JnZU9R?oc=5>

## RISKS

### Microsoft Service Outage Gives Software Giant Black Eye
- Summary: The outage tarnishes Microsoft’s reputation, raising concerns about reliability and customer trust.
- Date: 2026-11-13 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxPVERZREpDa055TVUzUktQNXhoTVE4LXQxTm0zMmFSdTR0cDBGeTFESHhETEl0c3UwbjNianF4ZEUtR2FvRXV1NktGMzJLOG83clczNXNfRm5MVE56emE0bjZLeC0xTmczRXdFVGcwN1lPdTB6S0VTUkd6M0VhaUJiZDZXWGFnNFh3MTFsODZHUFc?oc=5>

### Microsoft continues to restore Outlook email after outage, rules out ‘cyber or AI’ agents
- Summary: Microsoft is working to restore Outlook email services after an outage, dismissing cyber or AI agent causes.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2wFBVV95cUxQVW1TSGtQZ1h4RV92RXpiUTFLbjFhem5OYjZHa2RRd1JnUWtLb0lCS296aGxRVV9CYVNQaVNmZ0QwVGpRYVQ3elpKVlVPWWF2N0NHXzdCTE9YOHl2dXd3VldzaGNfb0ZIMTZLalVwR3lGMG5wZW16YU5NdEczMVN0eUM5c0xLUkVrQTBUU1ktbk1GQkVsX1BPbTI0UldXQWdMTGE3REpfMThId0xFcW9yODNReVNZS2ktLVFhOEdXcEFFUDlBa2RrUlFqcjZyQjBXZV92RGc0dUNhWGc?oc=5>

### Microsoft Extends Email Timeout Window To 48 Hours – Highlights Recovery Progress Across Asia-Pacific Infrastructure
- Summary: Microsoft extended Outlook timeout to 48 hours, showing recovery progress in Asia-Pacific infrastructure.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxPLXVrb3F0MDQ5OHNkRUZkRkpFVVlzcjRMcUZWcHJZMGhTN3E2VEgyTE4xcWxUeS1hUVFueW1xMUdVUHJWVk9TOXFxcGt1d1Ewdkl3OFZiazFmT1JhcnRfb0JHQTJOdXJLUklaLWQ3S2o5dUoxYndFYmhWUXY0dzVzYUtianJNREIzT3lCNEwwc0VOZERjd0dCdGlYdlZxMWYz?oc=5>

### Has Microsoft Stock Become A Different Bet?
- Summary: Investor uncertainty about Microsoft’s valuation raises risk concerns.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxPenQ0X1kweC0yd1FQelFMQXdjMjFMbklTbWxMOXRzb056WElTbVZzVS0wUmVlVHVzYmNmUnlqSktuV1pON3ZwU2RabWpDV001clNIYW1fWDNSbEUtUkFDdHcyUHVpb3lxWFBQQ2c2bFF0VWxaczB6eklrZkZwSHd5YktyV1g3Q3p0SDZzVW5PcFl4TnZwbHBzMzFkb0lQampwWElEZ0FB?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **MSFT** | **27.03** | **8.18** | **19.04** | **18.80** | **3,846,694,502,400.00 USD** | **2.37** |
| ORCL | 18.67 | 5.83 | 14.45 | 29.60 | 371,287,851,008.00 USD | -45.85 |
| GOOGL | 14.82 | 5.29 | 18.28 | 24.70 | 3,488,053,460,992.00 USD | 2.91 |
| AMZN | 20.84 | 4.54 | 16.21 | 12.10 | 2,787,086,172,160.00 USD | 9.83 |

Peers fetched as_of: 2026-11-16; MSFT reuses existing data (market data as_of: 2026-11-16); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-28
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-16

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-28
- Revenue (latest available single quarter): 19,953,000,000.00 USD; period 2010-10-01/2010-12-31; fiscal year/reporting period 2011/Q2
- Net income (latest available single quarter): 36,629,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2027/Q1
- SEC link: https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/msft-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMisAFBVV95cUxQNHdZOGRjaEJQWVQ5Tm9NMklaaGwyWHRFX3VYLU0xMmpBbVI2anJxTjZoQXI0eGpOVno3c3BRS1Z2a0kxSWFVRFFuNzU4WGdWNDl3S3RRb0lYeVhLVEY4aHF2aTNYNXFKbWxFU3ZvUU93WUlZT3hwVlQzQzgtR21EX0FkOTh2N0pMUXlhaWlaVUdqbHZTTGVkdzR5a0tDa2l5dDBDdXR6NC03TFJYLXJNUA?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxQWHVqMGZtQ1hFMURfLTdmMXg1RXUyQVVvckZqc3BMbEE1YWVMSjhlNlU5MDZVc1FjWGJyQXdoeXlzN1REenRsWmJTWWhadVNON3BHMnpSVTdHU2xQYWk3VENySm01YTJfOUJ6REg3WWtIZmhWLVB3cGNRNVF2U0l1WFNudXRVRE1zNjhHRWpRV2gwSVBzVkluVHRRRzFNeTZUcHkwZFFuUDI?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxPY2ZBT0k0ZkJ2N1Utb2k5RjIyWnp0SzNQQnhITVdET1Awa09pWmtyekJrekxqVXJaVzAwZkRDTmpaaWVyWGpJdGZ2Qi1ZTnNTeW9rRmtZd0lPdUY1WnNIcnFrZmdlODYxQ3lYbVJubjdUdElYOE04M09ZM0NrNGd5NWNEb0lXRXViaXNHMXhDSklLanN4Wi1QZXJHMWdIUk1MVktTbHdWdDJoWFk?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxQX19ZTTZXQk1LYXpjVmJvTDY4dVY2VUpmc3pOS3R4TS11WU1WSkpOMHJNNHRnVDhpMTNmdWhHN204QkFFYmtLWnBRWlkwaGNrQ0dfVVZlb1oxV1dieTdHS1hxNWpWSmRkWmNKU3A0OHdVbnc4YzNhejgweGZtd2pqeHhhYTlzdE5fWkFN?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxQTFM2V2hLWVoxbk1yckIxNUlkekhjeU5xUkFUXzY4eVRMbEU3enJFX1J2X2pTTWxtVTNPVnFMT3hCYVlVcjA0ZUxrODdoS2cxRzU0Y3lXb2tWSF9iZmUzZDZpMVpvMTNvbXlZZGE1dF8xWVMxenhhbEZLRDBHdmtsV09fVUpBMHpsaWNzSw?oc=5
- https://news.google.com/rss/articles/CBMigAFBVV95cUxQRUtKYTY3Q0wwdDR0WDQ0NlBVV0xsZVEzM0J5aDVUd1hrX2VBOXFTbks4Z2JFZFF6RG9TNjVIb3ZNRl9KRUJvNGxnYlgzQzBKbWVYWDFuU3F2X2VBdU5UWVo1OWVFOHpUX0E3RHNmNXBJQTE0dVU2R0dUS3pvVWhGNQ?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxNaGtTRGVaNHpadHlTY1NJQy1mQXpJQ1ZOaFVrY3Z3eU15STMxeE5fbXFuTi1VLWlqdmFYd0xyZ1pBaE1oSE41WC1zWVc4TW04S2s2bDlVMlVHZWZubi1iNFVuRnBUcFV5UXh0WlBoWmQ3Q0lGY3otcWk3eXBSUHRzQi00SEZIcHh3dXc2MEdGdXJWYmpGNTNVMm1BbEdfSTB2STNKTWcyRQ?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxPT0U5d29Od01qNm5mUGY0WU5hdTN5eTV1M3ZxMUNiMXhzWGZtZWdlOExJZ1ZCLURsTGwxQ1p4OFBRX3hyZGNQN2Jfd2FGRUl6UG1kMzBDYjVTU2J1WnQ3QzdadzQ3ZU9zaEdPUG1XbUhNdmkyc1ktNVVsVW5XUjJBTGpUb3RsbVdaRkpvYVliQl9JWHhrU1Jab0hwVmhGOEZNbFY3NWFyME42bjVpNFZZSXZJS2FwM2ZGZVdzTjI1bUM?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxOZHZqMll0OWUzZkFWN1BEY1VZWlZoTE45ZXJaX0NHQWNuZU90bEt3VzVqUzR4NE1tY29SbkxhdVFHTDUwT09kQm9aVmMwZzYwOHBRS3JBcl92MDJQUFJYYlJ4ZjF2RUJhd0ljSFk4TUJZOXZPczB2bFB3S3ZEaDVNS1FDZ0RvYnRVYzE2VmVVWXJFTnBvWGtySXdaYzAybzNZQ2F0VURXMUdpemgzQ1hJ?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxQUWl6NDdVVHVoUnJ0TVJBaDRMWW1mX0U2M29TQ2xTbksyaXFWSDI0bldFYTBYOGdPcmN6bWFwSDhjZFpad3RDOFE1SFJ6azJaUDlLN05adEI4TlJfRlJxTW1kWWtqLWs2TjJIeUFVWWlTdUlHMUdfUVI0UzN0UVYySm9UYzM0aGtOTmZPYld3X2lrc3N1Q2RTaTVrbjVwT0E?oc=5
- https://news.google.com/rss/articles/CBMiiAFBVV95cUxQbGlSYXgxbVRod2l2ZDRQczM5Q081VnZvTm1IMzFLM2dKNDc5NFhBY0poN2pnVW5PbFRRSG1SU2w3OUpDS2tObEk1QzBwNWJzMnlBOXcwUDRzOFZwd2M2ellrQmJzS3FFbEV2WHRhMjRxVU95WEtzZHhEc2ZEYlpIb3hIaFRsSkJF?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxOX3prYWZxNFJ4T3VWLVVoT0NaUHRrbXg2UkFsX0RYQlRqQ1I3SXByUkVtckxqT1hJbi1Kc3lLUDRKX3loMTdaRVFyTzUxUHN6aVlmUDVIOVVvYVZRQmJYWHRXTUdxdC1Tek5jQ3owWHEzN2JxeTZnYXdkU3gxYm1VSXlWeEhvUmNxd3pjSzk3bnI1Nkpwa2MzRXR3?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxQYXJNSTlyS19oSERrUGpmR2pyQ0F4Y1FDZ0hqY0d5R2c4U1o3QlBaRnVJOHZOSmFqMW1kNGYwSGZhY0lZMU4zN3JTZlBzWVFtdWlXSFpYUGE0VWlZVHlwbzVOM1BlQUVjdzJ0alZIc0pXV2dPOXZrN0hxSlE4aEpFTWtlUlpSVFl2MGNsRHQxOHBubVBkbFY0N1VuT05UZw?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxPdlBJMGRieWdXY3ZYdHJ4WVhhWjlPTWtkN0RrUGNZZVkzUFVGaGtvckpNV3FaS3FYajdrYkE1amlHQ2gtMm10UGo5MFVNM1pqb2VDb0F4aTl6UGhHeldlTEhfejMyOFZ6ZUNhYkpPZTl3WElyNUhldTBxNWFyNjNUazJ2Zm9lWllLeUhtMXFDeUlDd2otaThJNWlDRS1CU0JwN2t6a2hfRXV3Q3o1cENqMVlwcFpLWDBRTmNmZFVFWkM?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxPRnJHaU82ZVRoTzZHSVNNT2VVRHZFanRraE0zeFEySnhNMVZfX1lJYUd1SkpDc3pzQ3ZlbUZma1JVb0szc0EzVmFjeFNLWndua0o4U09sWWswMUIzaGJ6Y2k0dVRieURrdFpZYXNsS2Ruc2VBckZJeEdUQlFURjVYeDJ2ZmlqTU00N1JJUlMxN0sxdmdvbFNUVmFfZVJIZFJfRjZv?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxQYmVQUUROcXJfcGFPazRSZkExNWVYc25WaVpfNk5HT21rbG5yY3pTU01lSXB4OGZyZVFuaktNNUJvemxIVmI5enlZUzJtdHp6Zy1GUjFXQ3cxeXlBaTJPM1FkZzdhLWJJcUZFa0JQVUQyUXRleGRLSWFILTdSSnBlTUttYTZHaEhtTGtOY2t5eEJ1SG9udnpweS1DOUJQQ3RiRl9pY2R5YWdKLW91ZWRhRGpOZGVWQQ?oc=5
- https://news.google.com/rss/articles/CBMiygFBVV95cUxNOVoybWdIQ2tHakc1SFItZW9rY0dwOTlKZUlnNElFTnBIWHJJd25YQ0dUcTBSTnA4VjZPRGMxMmJ4QmdnTmdGTmhqemMxdlpQX0t0aHIzTmN5aG51Z3AyV2pOSkR6X09pbllPVHFRRlpHQ290THlERmktQnhsOVdrbVlxSnBRcUg0cjNXaDlHdE9xRG1Cc0RRWGYxdl94VkIxbXZ0WkNXb1BmOFptODcxbWRkT3FfQmJzR0RsNFN4WXYwZ0V6Z1JnZU9R?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxPVERZREpDa055TVUzUktQNXhoTVE4LXQxTm0zMmFSdTR0cDBGeTFESHhETEl0c3UwbjNianF4ZEUtR2FvRXV1NktGMzJLOG83clczNXNfRm5MVE56emE0bjZLeC0xTmczRXdFVGcwN1lPdTB6S0VTUkd6M0VhaUJiZDZXWGFnNFh3MTFsODZHUFc?oc=5
- https://news.google.com/rss/articles/CBMi2wFBVV95cUxQVW1TSGtQZ1h4RV92RXpiUTFLbjFhem5OYjZHa2RRd1JnUWtLb0lCS296aGxRVV9CYVNQaVNmZ0QwVGpRYVQ3elpKVlVPWWF2N0NHXzdCTE9YOHl2dXd3VldzaGNfb0ZIMTZLalVwR3lGMG5wZW16YU5NdEczMVN0eUM5c0xLUkVrQTBUU1ktbk1GQkVsX1BPbTI0UldXQWdMTGE3REpfMThId0xFcW9yODNReVNZS2ktLVFhOEdXcEFFUDlBa2RrUlFqcjZyQjBXZV92RGc0dUNhWGc?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxPLXVrb3F0MDQ5OHNkRUZkRkpFVVlzcjRMcUZWcHJZMGhTN3E2VEgyTE4xcWxUeS1hUVFueW1xMUdVUHJWVk9TOXFxcGt1d1Ewdkl3OFZiazFmT1JhcnRfb0JHQTJOdXJLUklaLWQ3S2o5dUoxYndFYmhWUXY0dzVzYUtianJNREIzT3lCNEwwc0VOZERjd0dCdGlYdlZxMWYz?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxPenQ0X1kweC0yd1FQelFMQXdjMjFMbklTbWxMOXRzb056WElTbVZzVS0wUmVlVHVzYmNmUnlqSktuV1pON3ZwU2RabWpDV001clNIYW1fWDNSbEUtUkFDdHcyUHVpb3lxWFBQQ2c2bFF0VWxaczB6eklrZkZwSHd5YktyV1g3Q3p0SDZzVW5PcFl4TnZwbHBzMzFkb0lQampwWElEZ0FB?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
