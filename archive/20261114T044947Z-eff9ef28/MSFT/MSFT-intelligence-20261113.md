# MSFT Intelligence Report

- ticker: **MSFT**
- Report as_of: **2026-11-13**
- Market data as_of: **2026-11-13**
- Quant sources: https://finance.yahoo.com/quote/MSFT/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/MSFT/key-statistics/
- AI analysis snapshot as_of: **2026-11-13**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-14T05:01:19.576254+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 8, 'ai': 12, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **3** exact headline/source/date matches; prior report **20261113T045636Z-34122c9a/MSFT** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'short_term_price_move_in_structural_risks': 1}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 17 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 28.0%; oldest publication 2026-11-11

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 523.8800 |
| Return 1D (%) | 0.1683 |
| Return 1W (%) | -1.2683 |
| Return 1M (%) | -3.6011 |
| Return YTD (%) | 9.0120 |
| Return 1Y (%) | 4.9475 |
| Annualized volatility (%) | 33.9772 |
| Beta vs SPY | 1.0093 |
| Max drawdown (%) | -30.4041 |
| Sharpe (rf=0) | 0.3093 |
| Downside deviation (rf=0, %) | 21.6957 |
| Sortino (rf=0) | 0.4844 |
| Historical VaR 95% (1D, %) | 2.8530 |
| Historical ES 95% (1D, %) | 4.1000 |
| Correlation vs SPY | 0.4050 |
| Tracking error vs SPY (%) | 31.0663 |
| P/E (trailing) | 27.30 |
| P/B | 8.27 |
| EV/EBITDA | 19.25 |
| Revenue growth (%) | 18.80 |
| Forward P/E (estimate) | 21.66 |
| Gross margin (%) | 67.66 |
| Operating margin (%) | 47.10 |
| Return on equity (%) | 34.22 |
| Free cash flow yield (%) | 0.08 |
| MA50 | 518.9972 |
| Close vs MA50 (%) | 0.9408 |
| MA200 | 440.4917 |
| Close vs MA200 (%) | 18.9307 |
| RSI (14, Wilder) | 48.8235 |
| MACD (12,26) | 2.0258 |
| MACD signal (9) | 3.8555 |
| MACD histogram | -1.8297 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'MSFT': 282, 'SPY': 282}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 523.8800 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.1683 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -1.2683 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -3.6011 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 9.0120 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 4.9475 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 33.9772 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 21.6957 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.4844 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.8530 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.1000 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4050 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 31.0663 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.0093 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -30.4041 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.3093 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 21.6569 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 67.6570 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 47.1040 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 34.2210 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 0.0770 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 27.2996 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 48.8235 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -1.8297 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 0.9408 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 18.9307 -> Clearly above the moving-average trend level.

## TAILWINDS

### Microsoft Stock (MSFT) Climbs Despite a Major Service Outage
- Summary: Microsoft Stock (MSFT) Climbs Despite a Major Service Outage
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxPaDFlYVFZNElsTEdDYXN6ZnNjR19Wb2pJMzJBSU9QeGg0bGg4MzlvLU4tUjd6NEE5aG5COUFKNFVoY2YwNkFYc3hZbEltMjR3QkEyMFF5cHl5ekJxdXBpSzZPQndrNHF1bjlZY1dPMUlTc20wWm9JRklUc0dsYU5KZGt1Y2xxY2dCc2lEXzJSTmV1UQ?oc=5>

### Microsoft Is Off Its Record High. Next Week Could See the Stock Reignited.
- Summary: Microsoft Is Off Its Record High. Next Week Could See the Stock Reignited.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMidkFVX3lxTE83cmJyRlBjMDBWU21ycUZoMzJTZXRiYml1RVpnRHZ6emprSmNFNUVIYk5oYm45VUJXdkJHSm5DVm5lamdUQjZ3QVl2UTcyRzZvc0lsWE9sWGFFeE52VUE2TlBJUExqandxbktlcjNiU01XNGRCbHc?oc=5>

## HEADWINDS

### MSFT Stock Slides Pre-Market as the Microsoft 365 Outage Hitting Outlook, Teams and Copilot Runs Into Day Two
- Summary: MSFT Stock Slides Pre-Market as the Microsoft 365 Outage Hitting Outlook, Teams and Copilot Runs Into Day Two
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMic0FVX3lxTE1jb2RGT2llS3RNLXJnQzNrTFBYTU9iUjJQSkhnUVNaeGZBZ1dQM3M0NjVROHdUZl9HN0o0ZXlJTWVYUFdLWHJ1VkQ0bUxTak81eDVqZzZLWXNxOU10dVBxdlNuS2ZQYlFfZ3o1WWU5dnhNYkU?oc=5>

### Microsoft stock slips as global outage knocks out Outlook, Teams, and Copilot
- Summary: Microsoft stock slips as global outage knocks out Outlook, Teams, and Copilot
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihgFBVV95cUxOZy1KS2lPYjZlU3hyNXhSMVlZdlEzTDZYaHhYbUJRMnhFVEpZWURSOHNWaW5mYk12Uko3b3haR1Vjd0xOUVNXWk5Kb19fRnFfYVJjaU02M1F6dWo5M1dnMUFxeGQ4NVdXUnlGa1ZJVXlxMF9yNVhMbmFNdFE1eGlzcnRRTDM4UQ?oc=5>

### Microsoft (NASDAQ:MSFT) Stock Falls as Global Outage Hits Outlook, Teams and Copilot
- Summary: Microsoft (NASDAQ:MSFT) Stock Falls as Global Outage Hits Outlook, Teams and Copilot
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMifkFVX3lxTFBjc0JoR1g3Zmthcmx5N0tIQ0NORnZkVmZWblRjV00wc1JSY21fUUdya3B3cGVqaWQ3QVZoc0VYY2VxdklDTWJhZmg1S2JUMk00MVpFcUM0cjA5U3p4Q0NCQ1d6ak5LVWw5amVZdXNZM2g3ZFNWVXJ3dXEzNDcxUQ?oc=5>

### Microsoft Stock Falls as Outage Tests Its Copilot Push
- Summary: Microsoft Stock Falls as Outage Tests Its Copilot Push
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxQX19ZTTZXQk1LYXpjVmJvTDY4dVY2VUpmc3pOS3R4TS11WU1WSkpOMHJNNHRnVDhpMTNmdWhHN204QkFFYmtLWnBRWlkwaGNrQ0dfVVZlb1oxV1dieTdHS1hxNWpWSmRkWmNKU3A0OHdVbnc4YzNhejgweGZtd2pqeHhhYTlzdE5fWkFN?oc=5>

### Microsoft Stock Drops as Global Outage Cripples Outlook, Teams and Copilot
- Summary: Microsoft Stock Drops as Global Outage Cripples Outlook, Teams and Copilot
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxQTFM2V2hLWVoxbk1yckIxNUlkekhjeU5xUkFUXzY4eVRMbEU3enJFX1J2X2pTTWxtVTNPVnFMT3hCYVlVcjA0ZUxrODdoS2cxRzU0Y3lXb2tWSF9iZmUzZDZpMVpvMTNvbXlZZGE1dF8xWVMxenhhbEZLRDBHdmtsV09fVUpBMHpsaWNzSw?oc=5>

### Azure Grew 48%, Yet Griffin Securities Downgraded Microsoft (MSFT). Here’s the Catch
- Summary: Azure Grew 48%, Yet Griffin Securities Downgraded Microsoft (MSFT). Here’s the Catch
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxPWTNUbVRXMnF2WU1sMW9vbFRLNFg4VUhFUzNZcTBJUUM3V1ZQT1BfWExkbDF6Z1c5LUdvUUZobko2Ykg1eU5aZUlaS3ZPZFJRdG1fYVpZVU1wYlVNYTNaU25henhkc1I3WHAwMDhZeGtSU3FuUGUtLW94Y2dYSDNLTldXWnRQWHBOUy00Qk9fYVA0Q3ZR?oc=5>

## CATALYSTS

### Microsoft Stocks Decline 2.5% as $1 Billion Anthropic Stake Tests Partner-Rival Balance
- Summary: Microsoft announced a $1B stake in Anthropic, testing its partnership and rivalry balance.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxPd2NEVEtyeThmMlBlejQ5YS0xdkVsTnhiczZRSkY2VUlWSFc1ZmhNek0tTVU5THZvZjdGbW5JWF9rSWFkanM3WkxyTlp6NDhWTHJwcGlzWFdGLXlIcXBOcndpVDlOQTZCanZOZ2VsNFdkMUdKOXZhUDlrS1lNUE9OakVMRVZnQVozTkdtYkFEM3Z3SnBQcjlFSw?oc=5>

### Microsoft (MSFT) stock price forecast: Wall Street analysts see 22% upside
- Summary: Analysts project a 22% upside for MSFT shares, indicating bullish outlook.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxQYXJNSTlyS19oSERrUGpmR2pyQ0F4Y1FDZ0hqY0d5R2c4U1o3QlBaRnVJOHZOSmFqMW1kNGYwSGZhY0lZMU4zN3JTZlBzWVFtdWlXSFpYUGE0VWlZVHlwbzVOM1BlQUVjdzJ0alZIc0pXV2dPOXZrN0hxSlE4aEpFTWtlUlpSVFl2MGNsRHQxOHBubVBkbFY0N1VuT05UZw?oc=5>

### Microsoft Corporation (MSFT) is Attracting Investor Attention: Here is What You Should Know
- Summary: MSFT draws investor focus, highlighting potential growth and stability.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxQNHdZOGRjaEJQWVQ5Tm9NMklaaGwyWHRFX3VYLU0xMmpBbVI2anJxTjZoQXI0eGpOVno3c3BRS1Z2a0kxSWFVRFFuNzU4WGdWNDl3S3RRb0lYeVhLVEY4aHF2aTNYNXFKbWxFU3ZvUU93WUlZT3hwVlQzQzgtR21EX0FkOTh2N0pMUXlhaWlaVUdqbHZTTGVkdzR5a0tDa2l5dDBDdXR6NC03TFJYLXJNUA?oc=5>

### Bill Ackman says Microsoft's position is 'really, really strong' as Anthropic pushes into enterprise software
- Summary: Analyst Bill Ackman praises Microsoft’s strong position amid Anthropic’s enterprise push.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi_gFBVV95cUxNNGxyVmFIZ0htSkxiTFBTemhQZEkyYmsxck9NZTIza0J6WEF6ZWVvSVFKQ2I3SktOc3VqNi01NVRUZ3FONU5LSWhkeUNjcFI5bFJXRTJLZkdheHdUUjllWHk3Qm9YZlNmVVU0dzZYN3JTY2NrSW9ld29HV3UwTWVEa003bDhLdEtFMkFZVHl1a3ktbm1CVGphb3F4UVViRWFwWjlIR3VlMjE3MTZkQnFZOGtHLWFNNzVoVDNuczNTM1JTY0RNTXhERHhGejZKa3FXbWt0QXUtYklzMGhPMzFLWDI1bHJhN1A3dlJFcnNQazlPZXpib0E3S2JyRDVNZw?oc=5>

### Microsoft: No Outage In The Growth Story, Hiking My Target (NASDAQ:MSFT)
- Summary: Microsoft analyst raises target, dismisses outage concerns, signals growth optimism.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxNRDVtc1I4MDNyU3BPNTRWNnZPMmw5eTN1SkYzNFprRXJqelVINVFkeU1kTXdldTZvN25vUS1VNXo3RUFQNEZBbzlVYU5wWmVsQnZLRy1Tc09Fd1NDUGFTY1o2RlVFMS01YWctTEFLVkkzTkRGbXFfRVEtcDBJMzg2UkhDUTV5b1hOVmJwaEtoN29YanNoTjJiTFpXNkVzQQ?oc=5>

## RISKS

### Microsoft points to ‘broad recovery and stability’ after widespread Outlook outage
- Summary: Microsoft acknowledges widespread Outlook outage, citing recovery and stability.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0gFBVV95cUxQN3JfTWdHazZ1d0hZM2RZaktTendJdWFRVDNEVEs1a3VqY19GUF9oZW1zUTN4aUlPV0wzZUhsRDBST250bHl3VHMxTzRqb2QzSG1FWDBlNk1Yc0lmNmJvTTJEMmhRZmQ3RFNLUDQ2U3U3bTZHNC1ZTExHLUlGcjN3ak15OTZkTDV0aEVOTEp0Skw5dGtRbGZUcjhHOUowWjlMVUpPbnB2R2FkOFdvVEp3TnEzMHlPSEVERTZHRkkwMFVSMWlDUmVTRHdfRkZZM253OVE?oc=5>

### Microsoft Stock Under Fire After Worldwide Blackout
- Summary: Global blackout triggers negative sentiment toward Microsoft stock.
- Date: 2026-11-13 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxOZHZqMll0OWUzZkFWN1BEY1VZWlZoTE45ZXJaX0NHQWNuZU90bEt3VzVqUzR4NE1tY29SbkxhdVFHTDUwT09kQm9aVmMwZzYwOHBRS3JBcl92MDJQUFJYYlJ4ZjF2RUJhd0ljSFk4TUJZOXZPczB2bFB3S3ZEaDVNS1FDZ0RvYnRVYzE2VmVVWXJFTnBvWGtySXdaYzAybzNZQ2F0VURXMUdpemgzQ1hJ?oc=5>

### Microsoft Stock in Focus as Massive 365 Outage Hits Outlook, Teams and Copilot: What Investors Should Know
- Summary: Massive 365 outage impacts Outlook, Teams, Copilot, affecting investor outlook.
- Date: 2026-11-13 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi-AFBVV95cUxOV18yQk1JR3FWeWVZRlgxZmRNWDRFQXZoMDB5N0UyR3pLTGVNcTZDdEJYZmI3RlhZeHRrYmR6NHpRMksxTUJoSV9DU0s1cUxsRmFveF80aUhXOG1MRXV0RnVpTWZvWHB0TnozbTU3ZWxkdmJIejNhOFZrVER4cHRmbEN5VnZsejlYRVVwRk9fNjJCTGRrNEJuQkJ2SU5MZUhrQjFJODdGdzdWb0VqMWF1NHhJYmRySWZiZnVzS1RBYl82WTZhZUprN2tfZ0Nkc1ZRdjBZbU1xVTRwLTlValMzUkNZUTc5eXMwMGo5eVpINV9kZDI3dzUzbg?oc=5>

### Microsoft (MSFT) Sees $360.6 Million in Net ETF Buying on Nov. 11
- Summary: Microsoft experiences significant net ETF buying, indicating positive market interest.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxPWmdKX2VHelFFazNocWt6TDZUNTJoNGZRbnloaVV6QWZ2WWt3T2ZHNm5BSEdrT25hcXlucURMQ1hWRXVZc3VHa2xZSlpjY2RpTWFPaGN4NGp2S2REeXV0aW9zcHp6eGNxN3lBZVl3U2FnQ3NxdnZVVmx6NzV0bGZUbDlzdTJXTWNTWTlrU205bXUyNllS?oc=5>

### Microsoft updates on outage disrupting Outlook email, Teams, and Copilot for users
- Summary: Microsoft reports outage affecting Outlook, Teams, Copilot, posing operational risk.
- Date: 2026-11-13 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMizAFBVV95cUxNSXRGTzRHWGVubjllRE1ILWQ2R0NMNU1fcFNQTlZhU0U3eHYxZ21DN0JPZElYSWxXb1ZTRnBlMHItR3o4Q2w0ZE5MN0c5SlZtUXhxYkt3ekVRdkdVTFBwLW5vakJHbHM2QUxMVVdqV29UMW1aN1NUa0VCR2I1aUZ2TWNrQWdsbmhSY0QwMkRaX3Q4dEtEOXRScmJSUEgybUxsWm9MbFdSeXhRaXM5RWdLVVdLV3Y5aG1ZUC0wRTJ6djVTbGI0OExFRXFSMkc?oc=5>

### Why Microsoft Outage Is the Worst Possible Timing for the Stock
- Summary: Microsoft's service outage coincides with a critical period, potentially affecting investor confidence and stock performance.
- Date: 2026-11-13 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMigAFBVV95cUxQRUtKYTY3Q0wwdDR0WDQ0NlBVV0xsZVEzM0J5aDVUd1hrX2VBOXFTbks4Z2JFZFF6RG9TNjVIb3ZNRl9KRUJvNGxnYlgzQzBKbWVYWDFuU3F2X2VBdU5UWVo1OWVFOHpUX0E3RHNmNXBJQTE0dVU2R0dUS3pvVWhGNQ?oc=5>

### Microsoft Service Outage Gives Software Giant Black Eye
- Summary: The outage tarnishes Microsoft’s reputation, raising concerns about reliability and customer trust.
- Date: 2026-11-13 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxPVERZREpDa055TVUzUktQNXhoTVE4LXQxTm0zMmFSdTR0cDBGeTFESHhETEl0c3UwbjNianF4ZEUtR2FvRXV1NktGMzJLOG83clczNXNfRm5MVE56emE0bjZLeC0xTmczRXdFVGcwN1lPdTB6S0VTUkd6M0VhaUJiZDZXWGFnNFh3MTFsODZHUFc?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **MSFT** | **27.30** | **8.27** | **19.25** | **18.80** | **3,890,434,801,664.00 USD** | **4.95** |
| ORCL | 19.93 | 6.13 | 15.00 | 29.60 | 390,804,701,184.00 USD | -41.62 |
| GOOGL | 15.60 | 5.51 | 19.08 | 24.70 | 3,636,196,016,128.00 USD | 6.45 |
| AMZN | 21.63 | 4.70 | 16.73 | 12.10 | 2,883,431,432,192.00 USD | 12.24 |

Peers fetched as_of: 2026-11-13; MSFT reuses existing data (market data as_of: 2026-11-13); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-28
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-13

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

- https://news.google.com/rss/articles/CBMikgFBVV95cUxPaDFlYVFZNElsTEdDYXN6ZnNjR19Wb2pJMzJBSU9QeGg0bGg4MzlvLU4tUjd6NEE5aG5COUFKNFVoY2YwNkFYc3hZbEltMjR3QkEyMFF5cHl5ekJxdXBpSzZPQndrNHF1bjlZY1dPMUlTc20wWm9JRklUc0dsYU5KZGt1Y2xxY2dCc2lEXzJSTmV1UQ?oc=5
- https://news.google.com/rss/articles/CBMidkFVX3lxTE83cmJyRlBjMDBWU21ycUZoMzJTZXRiYml1RVpnRHZ6emprSmNFNUVIYk5oYm45VUJXdkJHSm5DVm5lamdUQjZ3QVl2UTcyRzZvc0lsWE9sWGFFeE52VUE2TlBJUExqandxbktlcjNiU01XNGRCbHc?oc=5
- https://news.google.com/rss/articles/CBMic0FVX3lxTE1jb2RGT2llS3RNLXJnQzNrTFBYTU9iUjJQSkhnUVNaeGZBZ1dQM3M0NjVROHdUZl9HN0o0ZXlJTWVYUFdLWHJ1VkQ0bUxTak81eDVqZzZLWXNxOU10dVBxdlNuS2ZQYlFfZ3o1WWU5dnhNYkU?oc=5
- https://news.google.com/rss/articles/CBMihgFBVV95cUxOZy1KS2lPYjZlU3hyNXhSMVlZdlEzTDZYaHhYbUJRMnhFVEpZWURSOHNWaW5mYk12Uko3b3haR1Vjd0xOUVNXWk5Kb19fRnFfYVJjaU02M1F6dWo5M1dnMUFxeGQ4NVdXUnlGa1ZJVXlxMF9yNVhMbmFNdFE1eGlzcnRRTDM4UQ?oc=5
- https://news.google.com/rss/articles/CBMifkFVX3lxTFBjc0JoR1g3Zmthcmx5N0tIQ0NORnZkVmZWblRjV00wc1JSY21fUUdya3B3cGVqaWQ3QVZoc0VYY2VxdklDTWJhZmg1S2JUMk00MVpFcUM0cjA5U3p4Q0NCQ1d6ak5LVWw5amVZdXNZM2g3ZFNWVXJ3dXEzNDcxUQ?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxQX19ZTTZXQk1LYXpjVmJvTDY4dVY2VUpmc3pOS3R4TS11WU1WSkpOMHJNNHRnVDhpMTNmdWhHN204QkFFYmtLWnBRWlkwaGNrQ0dfVVZlb1oxV1dieTdHS1hxNWpWSmRkWmNKU3A0OHdVbnc4YzNhejgweGZtd2pqeHhhYTlzdE5fWkFN?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxQTFM2V2hLWVoxbk1yckIxNUlkekhjeU5xUkFUXzY4eVRMbEU3enJFX1J2X2pTTWxtVTNPVnFMT3hCYVlVcjA0ZUxrODdoS2cxRzU0Y3lXb2tWSF9iZmUzZDZpMVpvMTNvbXlZZGE1dF8xWVMxenhhbEZLRDBHdmtsV09fVUpBMHpsaWNzSw?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxPWTNUbVRXMnF2WU1sMW9vbFRLNFg4VUhFUzNZcTBJUUM3V1ZQT1BfWExkbDF6Z1c5LUdvUUZobko2Ykg1eU5aZUlaS3ZPZFJRdG1fYVpZVU1wYlVNYTNaU25henhkc1I3WHAwMDhZeGtSU3FuUGUtLW94Y2dYSDNLTldXWnRQWHBOUy00Qk9fYVA0Q3ZR?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxPd2NEVEtyeThmMlBlejQ5YS0xdkVsTnhiczZRSkY2VUlWSFc1ZmhNek0tTVU5THZvZjdGbW5JWF9rSWFkanM3WkxyTlp6NDhWTHJwcGlzWFdGLXlIcXBOcndpVDlOQTZCanZOZ2VsNFdkMUdKOXZhUDlrS1lNUE9OakVMRVZnQVozTkdtYkFEM3Z3SnBQcjlFSw?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxQYXJNSTlyS19oSERrUGpmR2pyQ0F4Y1FDZ0hqY0d5R2c4U1o3QlBaRnVJOHZOSmFqMW1kNGYwSGZhY0lZMU4zN3JTZlBzWVFtdWlXSFpYUGE0VWlZVHlwbzVOM1BlQUVjdzJ0alZIc0pXV2dPOXZrN0hxSlE4aEpFTWtlUlpSVFl2MGNsRHQxOHBubVBkbFY0N1VuT05UZw?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxQNHdZOGRjaEJQWVQ5Tm9NMklaaGwyWHRFX3VYLU0xMmpBbVI2anJxTjZoQXI0eGpOVno3c3BRS1Z2a0kxSWFVRFFuNzU4WGdWNDl3S3RRb0lYeVhLVEY4aHF2aTNYNXFKbWxFU3ZvUU93WUlZT3hwVlQzQzgtR21EX0FkOTh2N0pMUXlhaWlaVUdqbHZTTGVkdzR5a0tDa2l5dDBDdXR6NC03TFJYLXJNUA?oc=5
- https://news.google.com/rss/articles/CBMi_gFBVV95cUxNNGxyVmFIZ0htSkxiTFBTemhQZEkyYmsxck9NZTIza0J6WEF6ZWVvSVFKQ2I3SktOc3VqNi01NVRUZ3FONU5LSWhkeUNjcFI5bFJXRTJLZkdheHdUUjllWHk3Qm9YZlNmVVU0dzZYN3JTY2NrSW9ld29HV3UwTWVEa003bDhLdEtFMkFZVHl1a3ktbm1CVGphb3F4UVViRWFwWjlIR3VlMjE3MTZkQnFZOGtHLWFNNzVoVDNuczNTM1JTY0RNTXhERHhGejZKa3FXbWt0QXUtYklzMGhPMzFLWDI1bHJhN1A3dlJFcnNQazlPZXpib0E3S2JyRDVNZw?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxNRDVtc1I4MDNyU3BPNTRWNnZPMmw5eTN1SkYzNFprRXJqelVINVFkeU1kTXdldTZvN25vUS1VNXo3RUFQNEZBbzlVYU5wWmVsQnZLRy1Tc09Fd1NDUGFTY1o2RlVFMS01YWctTEFLVkkzTkRGbXFfRVEtcDBJMzg2UkhDUTV5b1hOVmJwaEtoN29YanNoTjJiTFpXNkVzQQ?oc=5
- https://news.google.com/rss/articles/CBMi0gFBVV95cUxQN3JfTWdHazZ1d0hZM2RZaktTendJdWFRVDNEVEs1a3VqY19GUF9oZW1zUTN4aUlPV0wzZUhsRDBST250bHl3VHMxTzRqb2QzSG1FWDBlNk1Yc0lmNmJvTTJEMmhRZmQ3RFNLUDQ2U3U3bTZHNC1ZTExHLUlGcjN3ak15OTZkTDV0aEVOTEp0Skw5dGtRbGZUcjhHOUowWjlMVUpPbnB2R2FkOFdvVEp3TnEzMHlPSEVERTZHRkkwMFVSMWlDUmVTRHdfRkZZM253OVE?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxOZHZqMll0OWUzZkFWN1BEY1VZWlZoTE45ZXJaX0NHQWNuZU90bEt3VzVqUzR4NE1tY29SbkxhdVFHTDUwT09kQm9aVmMwZzYwOHBRS3JBcl92MDJQUFJYYlJ4ZjF2RUJhd0ljSFk4TUJZOXZPczB2bFB3S3ZEaDVNS1FDZ0RvYnRVYzE2VmVVWXJFTnBvWGtySXdaYzAybzNZQ2F0VURXMUdpemgzQ1hJ?oc=5
- https://news.google.com/rss/articles/CBMi-AFBVV95cUxOV18yQk1JR3FWeWVZRlgxZmRNWDRFQXZoMDB5N0UyR3pLTGVNcTZDdEJYZmI3RlhZeHRrYmR6NHpRMksxTUJoSV9DU0s1cUxsRmFveF80aUhXOG1MRXV0RnVpTWZvWHB0TnozbTU3ZWxkdmJIejNhOFZrVER4cHRmbEN5VnZsejlYRVVwRk9fNjJCTGRrNEJuQkJ2SU5MZUhrQjFJODdGdzdWb0VqMWF1NHhJYmRySWZiZnVzS1RBYl82WTZhZUprN2tfZ0Nkc1ZRdjBZbU1xVTRwLTlValMzUkNZUTc5eXMwMGo5eVpINV9kZDI3dzUzbg?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxPWmdKX2VHelFFazNocWt6TDZUNTJoNGZRbnloaVV6QWZ2WWt3T2ZHNm5BSEdrT25hcXlucURMQ1hWRXVZc3VHa2xZSlpjY2RpTWFPaGN4NGp2S2REeXV0aW9zcHp6eGNxN3lBZVl3U2FnQ3NxdnZVVmx6NzV0bGZUbDlzdTJXTWNTWTlrU205bXUyNllS?oc=5
- https://news.google.com/rss/articles/CBMizAFBVV95cUxNSXRGTzRHWGVubjllRE1ILWQ2R0NMNU1fcFNQTlZhU0U3eHYxZ21DN0JPZElYSWxXb1ZTRnBlMHItR3o4Q2w0ZE5MN0c5SlZtUXhxYkt3ekVRdkdVTFBwLW5vakJHbHM2QUxMVVdqV29UMW1aN1NUa0VCR2I1aUZ2TWNrQWdsbmhSY0QwMkRaX3Q4dEtEOXRScmJSUEgybUxsWm9MbFdSeXhRaXM5RWdLVVdLV3Y5aG1ZUC0wRTJ6djVTbGI0OExFRXFSMkc?oc=5
- https://news.google.com/rss/articles/CBMigAFBVV95cUxQRUtKYTY3Q0wwdDR0WDQ0NlBVV0xsZVEzM0J5aDVUd1hrX2VBOXFTbks4Z2JFZFF6RG9TNjVIb3ZNRl9KRUJvNGxnYlgzQzBKbWVYWDFuU3F2X2VBdU5UWVo1OWVFOHpUX0E3RHNmNXBJQTE0dVU2R0dUS3pvVWhGNQ?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxPVERZREpDa055TVUzUktQNXhoTVE4LXQxTm0zMmFSdTR0cDBGeTFESHhETEl0c3UwbjNianF4ZEUtR2FvRXV1NktGMzJLOG83clczNXNfRm5MVE56emE0bjZLeC0xTmczRXdFVGcwN1lPdTB6S0VTUkd6M0VhaUJiZDZXWGFnNFh3MTFsODZHUFc?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
