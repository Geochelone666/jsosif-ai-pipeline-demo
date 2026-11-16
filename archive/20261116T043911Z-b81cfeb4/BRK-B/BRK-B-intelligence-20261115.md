# BRK-B Intelligence Report

- ticker: **BRK-B**
- Report as_of: **2026-11-15**
- Market data as_of: **2026-11-13**
- Quant sources: https://finance.yahoo.com/quote/BRK-B/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/BRK-B/key-statistics/
- AI analysis snapshot as_of: **2026-11-15**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-16T04:46:43.826036+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 1, 'ai': 18, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **12** exact headline/source/date matches; prior report **20261115T044154Z-6abfba73/BRK-B** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 8 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 66.67%; oldest publication 2026-11-09

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 592.9400 |
| Return 1D (%) | 0.5273 |
| Return 1W (%) | 3.8624 |
| Return 1M (%) | 13.8977 |
| Return YTD (%) | 17.9628 |
| Return 1Y (%) | 15.5581 |
| Annualized volatility (%) | 15.0285 |
| Beta vs SPY | 0.0766 |
| Max drawdown (%) | -9.4218 |
| Sharpe (rf=0) | 1.0412 |
| Downside deviation (rf=0, %) | 10.0753 |
| Sortino (rf=0) | 1.5531 |
| Historical VaR 95% (1D, %) | 1.4122 |
| Historical ES 95% (1D, %) | 2.0016 |
| Correlation vs SPY | 0.0695 |
| Tracking error vs SPY (%) | 19.5767 |
| P/E (trailing) | 16.60 |
| P/B | 0.00 |
| EV/EBITDA | -2.04 |
| Revenue growth (%) | 11.20 |
| Forward P/E (estimate) | 25.99 |
| Gross margin (%) | 26.60 |
| Operating margin (%) | 26.60 |
| Return on equity (%) | 10.57 |
| Free cash flow yield (%) | 4.17 |
| MA50 | 529.6578 |
| Close vs MA50 (%) | 11.9478 |
| MA200 | 500.4340 |
| Close vs MA200 (%) | 18.4852 |
| RSI (14, Wilder) | 80.9080 |
| MACD (12,26) | 17.8405 |
| MACD signal (9) | 15.0178 |
| MACD histogram | 2.8227 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'BRK-B': 282, 'SPY': 282}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 592.9400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.5273 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 3.8624 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 13.8977 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 17.9628 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 15.5581 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 15.0285 -> Low annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 10.0753 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.5531 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.4122 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.0016 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.0695 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 19.5767 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.0766 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -9.4218 -> Shallow peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.0412 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 25.9872 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 26.6020 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 26.6020 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 10.5740 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 4.1656 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 16.5950 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 80.9080 -> Overbought momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 2.8227 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 11.9478 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 18.4852 -> Clearly above the moving-average trend level.

## TAILWINDS

### Berkshire breaks out to record high with fourth-quarter rally reaching 19%
- Summary: Berkshire’s stock hits record high, rallying 19% in Q4.
- Date: 2026-11-14 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxQbUV4NF9lbkt0WEpneTdsTUFfMDE2dklud1lnVnFPR0YtWGNTck9NbUNJZHk2WWtIeERxXzQ5VWdUTzNDNGRnb2Npd3h0SEp2aVc2VmszQ2lXUjVjZ1lrMEtoSTRYdXJFM0d1TnNNV0ROV1R5VFN5RjJoZjgtWlZBM0lsVnpydV82a1BVQmZibTdaNDA0WFpQMklSaHMwZEtmZ0FhSHM3a0VLQXpwTHFBRHVFMWFaRGZ10gG-AUFVX3lxTE0ycGVWQ2xHWWV0U2xFdWpmbkZiWVhMR2tlQy0wNFlvMXZ0ejlHU0IyNE85Yk0wSjdXODRpSTF4MkZJYXpqMTBSRlZFakhHTjdGSXNpcFZKRHVNcWk0YW5EanM4cW1iYU1oR29PVVYyODUwajRjSjZiR0VFdDdlbWZkUXFXanNTby1fYl9hdkFzVHFKUy1lQXZlUkNzRWNENElhUXBfU0Z1NVdpcXZwM0RVRXpTT3BtQy11QnFGc0E?oc=5>

### Warren Buffett's Berkshire Just Hit a Record High as Nvidia Sank. A 67-Year-Old Who Bought 1,000 Shares in 2016 Can Sell $106,000 of It This Year and Pay 0% on the Gain
- Summary: Berkshire shares reach record high amid Nvidia decline.
- Date: 2026-11-14 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMirwJBVV95cUxNS0JuN2tqU1RoaW8xRHktbXRPUXhJbU8zSWxTZzNDajczQ0E2TkRjMGdnXzloUTlpTmo4MDhLSUxRUHBPaDlIR1NpVHdtbktoRHRuc1YyV3IyemdGb19VaVRISVFpUW5yVFBZSzRERnk4SWNUaEQ4S0c0ZWJJRHA5blJqWDY4alNabFdCU3pVRzgyYU80b05pOTkwX0sxQlh4MmJudkdUV2FyV09wYnRxN3pmSWpUcEVPZy1YY1E2Zk8tSmdHdEdmV2t1dlVKOWRtMkxMaF8wM05yaHQyOWFoVnlMS0V1X21HRTRXTTJmZl8yY2pCMlJocDczbEFJWjdwbmgzNk8wYzgyY2M4czdxV1hVYWFieGJ3RkJmdTctcm9sT2lONzFKTjhEQWk1amM?oc=5>

### Berkshire Hathaway Laid The Blueprint For Right Capital Empire (NYSE:BRK.A)
- Summary: Berkshire outlines a strategic plan for future growth, positioning it as a long-term value play.
- Date: 2026-11-13 | Impact: medium | Horizon: long | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxQVm9ydXRvbkI2eENmbVlqcVBOY3hIaHgtOVQ0U0tuQ3czRUxlWGIxT2ZkQ3Q3emZNR1NZZUNNMU9HYnpuLUdZaDM3alhleXM0SzBjNEFSUlhJMC1mRVJTYV90MFNucnpCY0o3TURYSGJsaXp0bmJYbzg4OHdHNEYwMzQwdE5FYW1TbGpVVjFRNEY5N0h6U2RjOXNPdkl2ZzJnN29WeHFB?oc=5>

### Forget the "Magnificent Seven." Berkshire Hathaway Could Be the Better Long-Term Bet.
- Summary: Opinion piece suggests Berkshire may outperform tech giants over the long term.
- Date: 2026-11-13 | Impact: medium | Horizon: medium | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxPajQ5ZzJXa0RlNXlFNjNDaTNTal95TmV1SlBMdjV0V2tqZjZpSFJEVkxBZXNodzM5ck9VVjNrQ3I5UGlCNWFmQUpJNERyTlNxWm03QVpvdlB0SXlqd0hBUDNvcDVoMEI2bzBwZlp6YXg2SmZPRzQtVHRxTkV5Ui00WlhEZzRUdFpCSm9tbDM4dm5EYnVOQXF3RWxEQ2NOV1hrVktOeGQ4ZWc5dVZ0?oc=5>

### Berkshire Hathaway Stock Trades at Record Levels. CEO Greg Abel Clearly Sees More Room to Run.
- Summary: Berkshire stock hits record levels, CEO Abel signals confidence in growth prospects.
- Date: 2026-11-12 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi0AFBVV95cUxPdWxNZHVCTnhVUE84a1R5MGtQdVZ6WkxDb0tfMTN6aUR3WklyM2RROC1wTU5EYS1xR0FfanBuYkFncmdPQlNKcXNkM0ZZRklzWERSTkVqMWt1RUdqUHBYRE5IQ2tPdXY4VktzNUFQbnNVWHBNbUVGdG9fb3FrVExnY252bkk1MjBmVTlvek5nSjVSX0dadi1sQnJ5c2ctaXdpaVd6WnFjX1k2dnRJM0lZSjR1bG5ZWHRUY1c5Z0F2R1hnS3FjU0ZUUDNaVHExMEE3?oc=5>

## HEADWINDS

### Berkshire’s record high exposes hidden trap in S&P 500 401(k) plans
- Summary: Berkshire’s record high highlights a potential risk for 401(k) investors.
- Date: 2026-11-15 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMie0FVX3lxTFBrQ2xOVE1KellFRnE5a0JYVWhld3NMeVFxX1dEWUU2ZnZWck55WkFiQUlvSC1BWjZ1UGl6S09wV09Cb3VSLTc4N00zNlMzR2d2OFVuUzkwd3FVXzU5Q3NMS0ZocG53TGwwNXBpSXQ5T2Q3NDA0bVpBbXhoaw?oc=5>

### The Stock Market Is Sending a Rare Warning. Here's Warren Buffett's Best Bear Market Advice.
- Summary: Market warning signals potential downside, Buffett’s advice underscores caution.
- Date: 2026-11-15 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxQLXpWWmwyYjBfOVJkVGZvdXJkdHMxMFlZYkFZTjE3Y0dHVTFXamhOX1l6UUJZcTlPbFl3Vm41WXRRZXo2bmI5Q1FtS3Y4UlZNLWFnU0hQd21JdXhDR1RPMDVEcmJEZHg0T3ZCR2dRb1FQR2VBNUpNaElPR1ZIZEdUXzlWLUhNRHg3UmphMGtvcXVqMUswbmlnNzgyOGg3a2M?oc=5>

## CATALYSTS

### Berkshire Hathaway (BRK.A) Stock Fair Value Edges Higher After Split Analyst Revisions
- Summary: Berkshire Hathaway (BRK.A) Stock Fair Value Edges Higher After Split Analyst Revisions
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxOVGJZYUROQlVVN3JGd0N3NVdBaTBZOU9yYUVQakVGa1Nua3pDS1J1N1U2TDJIZmFxUVV6Y1Y1bXNJTS1NcXhZblpGa2Z4RUZob3NWS2x2WDZua1IxNzlJa2trQVpFZkx3MnFCZ2dCZ2hVOFFMeC1rTmJKSWVvRWQ2cHoxcUd0d0MtT0R2NEVOWFREWk1rQlF2Ml9ETVJ1ZTQ?oc=5>

### Berkshire Hathaway’s Greg Abel Bought Back a Record $9.6 Billion of Stock Last Quarter. Here’s Why That Pace Might Not Continue.
- Summary: Record $9.6B stock buyback; future pace uncertain.
- Date: 2026-11-13 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxQZHF3cy1zVVQyOUI5UXA0MnM5SmZ3NEM0RHEtcXlEVnJ2UUhJeGg2dUlNYVJldDRUcE9OSmZjcEtnaFJ3VC0yVEFMTTZfZ296Zl9SQzNBVG84ZWY1VG1mT3BOX2prbEd5cDJKWGZfU3pJTEFkZVdkQmpGYnFQZHhqcElUV0hJVWh0NEcwcnVwTlg0NndTZVRlNHdXdHJDZkxpYUE?oc=5>

### What You Actually Own When You Buy a Share of Berkshire Hathaway
- Summary: Explains the components of a Berkshire Hathaway share, including its underlying assets and voting rights.
- Date: 2026-11-11 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxOMVpuMEJ1b0IyTUJPVE1OakZ0NmhqWVNCQTRILXlWaTZPdmkyQzNrb3lXSGVESFZhY0V2eTdMSXdHdFROUW9qT3dlcUN0UkpiMGYtWDhKYVhlOGVmNFpmSDR2WXp6S0VrUWtreEp5ZkxQMlkzWThxMzFZTlZjVkZVMUNCdEQya1ZsOEFWc0czRDBoNHpiX2R0TUhQb3Rrdw?oc=5>

### Berkshire’s Greg Abel Spent $14.4 Billion on Buffett’s Favorite Stock
- Summary: Berkshire purchased $14.4B of a favored company’s shares, indicating significant capital allocation.
- Date: 2026-11-12 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQM1QyWS1Rd3JOaU5lZHNhVEs4R2pFNE9rQlVVTmdVQ3E0WWt1XzFTTjFaNzdydS04QzJVc1hfYzNfSF8wcHJNTHh0TXNfSFhHQ3pxWlRtY2RaSE12QVZqenkxNUN4SDNVQmVtZktPbHEyOXpnNm5xbV9CMVQ4ZElqMmk5eElOM0RyTENYSWxtMks5dkVJekVleA?oc=5>

### Warren Buffett’s Berkshire Just Bought $600 Million in Lennar Stock as the Housing Market Weakens
- Summary: Acquisition of $600M Lennar shares amid a weakening housing market shows targeted investment.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxNQjYwaGgxSXJtbGwwRFBNNEVxT1FvWWRtVGtkQWZMaWZWUEgzc0pjWFJDVzFPbTV1THk2LXFGQTdiUXBMUGgydl9EU2dlTEtTZWtBaUZwWFhBam12YTFvaU5IaDh1X3RzSFNMbkk0dndiZm5zZ2hKUTRhWkkxZk5maC1oVmxkaWNPdEFyVHJ1dWVsTWxIaWo4OEx0Nk1mRmc?oc=5>

### Berkshire Hathaway Deepens Japan Focus With Fresh Yen Bond Plans
- Summary: Berkshire Hathaway plans new yen-denominated bonds to strengthen Japan exposure.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxQdFlGeUtaNXBLZTZ0b0o0MXk1MU14ZU52S3JlZjROV0tWNHJQQmpfcWcwbFI0U056VHlPOXNST3pGOWFxTXNLRGhnQVdkcnBuRnp0bHFOQWVmTjE3RU9WcEFwSVhDQ1ZSSVp1Mm8zaE9aUEZ0VC13QmNUN3lVTjdQdDJkNWMtejF0Ym1YRUl5aVAzOHN0UW84M2djVHBYWkozMEFqSlV3?oc=5>

### Greg Abel just spent US$9.6 billion buying back Berkshire stock in one quarter — outpacing Buffett's final years
- Summary: Abel’s $9.6B buyback boosts shareholder value and signals confidence.
- Date: 2026-11-15 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMifEFVX3lxTE1qRUVDR1hkZkotczdTRTM5ZlJ6bEstak1QX3FyUEdZV2xsVjA5eDYteWtEUlJJNWZIbGtndGlvVnQtS2U1NXJ2VzNUaGpOWUhXTHVEWGktNXJ6ZktQcHZGWmlBWkUxZmQ5RlpoUXRQZjlaSVc0ZUptVjN3aV8?oc=5>

### What Are Wall Street Analysts' Target Price for Berkshire Hathaway Stock?
- Summary: Analysts discuss target price for Berkshire Hathaway shares.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxQUWlIQkEtV3A5SE9taWtKbUNiU0Zudnp1X3plYmpRY3YyRXNYdFYzVFlOYUFQLUdmY2xodjQ5eDE3T2dnd25jSmcwZGtlZ0JxeV8ydk0zQjBTbHczWlF3THRpVkQ1bVhxdWpvLXBJd0piaUplUHBpcmJZVkVHU0FmY1ZGYWZndFJxMUFoWjYwdHZBSzJKcEZLbm92azJKLTg?oc=5>

### Berkshire Hathaway's Top AI Holding Is Poised to Outperform
- Summary: Berkshire's AI holding expected to outperform market.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxNOWRrX2V6REgxV2JtM3RyQUJjQ0xnSzZNc3UyUVNHZWxIaDFOdFI5UmNaSjRGZHRXWENwSDhCRWxrUjNIYWJ2NHZJZWE1X3JoT0Rkc3loc3BfTmh2amF1RC10Y3JUSFA0VzZsdVRfWUNtMnVaOFBKVzYwcnFyT3dLSmlrNHBZMnd2cjRkWXZ2emV0VGQ1ZmNaVlJPSWhzSDQ?oc=5>

### Warren Buffett's Successor, Greg Abel, Just Bought $9.6 Billion of the Oracle of Omaha's Favorite Stock (No, Not Alphabet!)
- Summary: Greg Abel purchased $9.6B of Berkshire shares.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxPemRfX2I0QTR5M3ViaXh5N3dmR1dJeEt6dWZsRGRaUjliZnpxSHVPOWhTVzlMOEhNTUtWdE1OVEdlSzY4aDFVLUR6QXp1SEVnaTRCSGtmUGNlRDAyTW9WZ09wNWd6UTdoWTFrbHg3R08zc1dyVnMxZ2txdWQ5OEU2Y0laZW9pcGwxLWUzTVVHZHdPODhmbm9JTnFFYU5QVTJraFE?oc=5>

### Warren Buffett's Successor, Greg Abel, Has Nearly $110 Billion Invested in These 2 Tech Stocks
- Summary: Greg Abel invested $110B in tech stocks, not Berkshire.
- Date: 2026-11-12 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxPN29WazVNNTNseGloU2s5UmNaSUZlQzR3Z2lFaEZEeXJndjhwdHhNbVpEcTVGSVUxSXZzdWQ3eG9tNFVDeXgxLXptQi0yd19HQ0kxcUFDVUNiYUVSZzB2QzdvT3NSVFBhUEt3dEdBSGhrTEUydXA1MjJCazJ1WVpHTWpBZkxyZkZHNlpuNUNzLXV0LV8xTmFVU0poZ0k2Y3dnaVE?oc=5>

### Warren Buffett's Rule for Stock Buybacks Is Very Specific. Berkshire Spent a Record $9.6 Billion on Them Last Quarter.
- Summary: Berkshire Hathaway spent a record $9.6 billion on stock buybacks last quarter, reflecting Buffett’s specific buyback policy.
- Date: 2026-11-09 | Impact: high | Horizon: short | Confidence: 1
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxNZ2x4aFRuSTUzYXFaQTc5S3E3N2xiRm9ZU0Npb3Q2RmFYN21JcUxfQld6MUZ0OUQ5ZkNtMzY5MDNXM2FQV0VwSlBWX0NDdi1uemdhdWFzcWVMSF9tUzhmSFA2Yl8xUWVtcUR4X0NrV090V2dTWE9MbjBCZ3VFY1NpOUVpSWNzSTRGTHpZNjVXZ1FqQ1JjU3I1alczTGpBZkswNnc?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **BRK-B** | **16.60** | **0.00** | **-2.04** | **11.20** | **1,259,712,413,696.00 USD** | **15.56** |
| MKL | 14.07 | 1.31 | 8.10 | -11.20 | 24,181,002,240.00 USD | -5.04 |
| FFH.TO | 10.22 | 1.46 | 8.91 | 1.90 | 57,426,022,400.00 CAD | 24.06 |
| L | 15.48 | 1.24 | 8.76 | 1.90 | 22,629,003,264.00 USD | 7.44 |

Peers fetched as_of: 2026-11-15; BRK-B reuses existing data (market data as_of: 2026-11-13); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-07
- Next expected earnings: 2027-03-01 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-15

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-09
- Revenue (latest available single quarter): 105,647,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 22,112,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1067983/000119312526452412/brka-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiuAFBVV95cUxQbUV4NF9lbkt0WEpneTdsTUFfMDE2dklud1lnVnFPR0YtWGNTck9NbUNJZHk2WWtIeERxXzQ5VWdUTzNDNGRnb2Npd3h0SEp2aVc2VmszQ2lXUjVjZ1lrMEtoSTRYdXJFM0d1TnNNV0ROV1R5VFN5RjJoZjgtWlZBM0lsVnpydV82a1BVQmZibTdaNDA0WFpQMklSaHMwZEtmZ0FhSHM3a0VLQXpwTHFBRHVFMWFaRGZ10gG-AUFVX3lxTE0ycGVWQ2xHWWV0U2xFdWpmbkZiWVhMR2tlQy0wNFlvMXZ0ejlHU0IyNE85Yk0wSjdXODRpSTF4MkZJYXpqMTBSRlZFakhHTjdGSXNpcFZKRHVNcWk0YW5EanM4cW1iYU1oR29PVVYyODUwajRjSjZiR0VFdDdlbWZkUXFXanNTby1fYl9hdkFzVHFKUy1lQXZlUkNzRWNENElhUXBfU0Z1NVdpcXZwM0RVRXpTT3BtQy11QnFGc0E?oc=5
- https://news.google.com/rss/articles/CBMirwJBVV95cUxNS0JuN2tqU1RoaW8xRHktbXRPUXhJbU8zSWxTZzNDajczQ0E2TkRjMGdnXzloUTlpTmo4MDhLSUxRUHBPaDlIR1NpVHdtbktoRHRuc1YyV3IyemdGb19VaVRISVFpUW5yVFBZSzRERnk4SWNUaEQ4S0c0ZWJJRHA5blJqWDY4alNabFdCU3pVRzgyYU80b05pOTkwX0sxQlh4MmJudkdUV2FyV09wYnRxN3pmSWpUcEVPZy1YY1E2Zk8tSmdHdEdmV2t1dlVKOWRtMkxMaF8wM05yaHQyOWFoVnlMS0V1X21HRTRXTTJmZl8yY2pCMlJocDczbEFJWjdwbmgzNk8wYzgyY2M4czdxV1hVYWFieGJ3RkJmdTctcm9sT2lONzFKTjhEQWk1amM?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxQVm9ydXRvbkI2eENmbVlqcVBOY3hIaHgtOVQ0U0tuQ3czRUxlWGIxT2ZkQ3Q3emZNR1NZZUNNMU9HYnpuLUdZaDM3alhleXM0SzBjNEFSUlhJMC1mRVJTYV90MFNucnpCY0o3TURYSGJsaXp0bmJYbzg4OHdHNEYwMzQwdE5FYW1TbGpVVjFRNEY5N0h6U2RjOXNPdkl2ZzJnN29WeHFB?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxPajQ5ZzJXa0RlNXlFNjNDaTNTal95TmV1SlBMdjV0V2tqZjZpSFJEVkxBZXNodzM5ck9VVjNrQ3I5UGlCNWFmQUpJNERyTlNxWm03QVpvdlB0SXlqd0hBUDNvcDVoMEI2bzBwZlp6YXg2SmZPRzQtVHRxTkV5Ui00WlhEZzRUdFpCSm9tbDM4dm5EYnVOQXF3RWxEQ2NOV1hrVktOeGQ4ZWc5dVZ0?oc=5
- https://news.google.com/rss/articles/CBMi0AFBVV95cUxPdWxNZHVCTnhVUE84a1R5MGtQdVZ6WkxDb0tfMTN6aUR3WklyM2RROC1wTU5EYS1xR0FfanBuYkFncmdPQlNKcXNkM0ZZRklzWERSTkVqMWt1RUdqUHBYRE5IQ2tPdXY4VktzNUFQbnNVWHBNbUVGdG9fb3FrVExnY252bkk1MjBmVTlvek5nSjVSX0dadi1sQnJ5c2ctaXdpaVd6WnFjX1k2dnRJM0lZSjR1bG5ZWHRUY1c5Z0F2R1hnS3FjU0ZUUDNaVHExMEE3?oc=5
- https://news.google.com/rss/articles/CBMie0FVX3lxTFBrQ2xOVE1KellFRnE5a0JYVWhld3NMeVFxX1dEWUU2ZnZWck55WkFiQUlvSC1BWjZ1UGl6S09wV09Cb3VSLTc4N00zNlMzR2d2OFVuUzkwd3FVXzU5Q3NMS0ZocG53TGwwNXBpSXQ5T2Q3NDA0bVpBbXhoaw?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxQLXpWWmwyYjBfOVJkVGZvdXJkdHMxMFlZYkFZTjE3Y0dHVTFXamhOX1l6UUJZcTlPbFl3Vm41WXRRZXo2bmI5Q1FtS3Y4UlZNLWFnU0hQd21JdXhDR1RPMDVEcmJEZHg0T3ZCR2dRb1FQR2VBNUpNaElPR1ZIZEdUXzlWLUhNRHg3UmphMGtvcXVqMUswbmlnNzgyOGg3a2M?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxOVGJZYUROQlVVN3JGd0N3NVdBaTBZOU9yYUVQakVGa1Nua3pDS1J1N1U2TDJIZmFxUVV6Y1Y1bXNJTS1NcXhZblpGa2Z4RUZob3NWS2x2WDZua1IxNzlJa2trQVpFZkx3MnFCZ2dCZ2hVOFFMeC1rTmJKSWVvRWQ2cHoxcUd0d0MtT0R2NEVOWFREWk1rQlF2Ml9ETVJ1ZTQ?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxQZHF3cy1zVVQyOUI5UXA0MnM5SmZ3NEM0RHEtcXlEVnJ2UUhJeGg2dUlNYVJldDRUcE9OSmZjcEtnaFJ3VC0yVEFMTTZfZ296Zl9SQzNBVG84ZWY1VG1mT3BOX2prbEd5cDJKWGZfU3pJTEFkZVdkQmpGYnFQZHhqcElUV0hJVWh0NEcwcnVwTlg0NndTZVRlNHdXdHJDZkxpYUE?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxOMVpuMEJ1b0IyTUJPVE1OakZ0NmhqWVNCQTRILXlWaTZPdmkyQzNrb3lXSGVESFZhY0V2eTdMSXdHdFROUW9qT3dlcUN0UkpiMGYtWDhKYVhlOGVmNFpmSDR2WXp6S0VrUWtreEp5ZkxQMlkzWThxMzFZTlZjVkZVMUNCdEQya1ZsOEFWc0czRDBoNHpiX2R0TUhQb3Rrdw?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQM1QyWS1Rd3JOaU5lZHNhVEs4R2pFNE9rQlVVTmdVQ3E0WWt1XzFTTjFaNzdydS04QzJVc1hfYzNfSF8wcHJNTHh0TXNfSFhHQ3pxWlRtY2RaSE12QVZqenkxNUN4SDNVQmVtZktPbHEyOXpnNm5xbV9CMVQ4ZElqMmk5eElOM0RyTENYSWxtMks5dkVJekVleA?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxNQjYwaGgxSXJtbGwwRFBNNEVxT1FvWWRtVGtkQWZMaWZWUEgzc0pjWFJDVzFPbTV1THk2LXFGQTdiUXBMUGgydl9EU2dlTEtTZWtBaUZwWFhBam12YTFvaU5IaDh1X3RzSFNMbkk0dndiZm5zZ2hKUTRhWkkxZk5maC1oVmxkaWNPdEFyVHJ1dWVsTWxIaWo4OEx0Nk1mRmc?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxQdFlGeUtaNXBLZTZ0b0o0MXk1MU14ZU52S3JlZjROV0tWNHJQQmpfcWcwbFI0U056VHlPOXNST3pGOWFxTXNLRGhnQVdkcnBuRnp0bHFOQWVmTjE3RU9WcEFwSVhDQ1ZSSVp1Mm8zaE9aUEZ0VC13QmNUN3lVTjdQdDJkNWMtejF0Ym1YRUl5aVAzOHN0UW84M2djVHBYWkozMEFqSlV3?oc=5
- https://news.google.com/rss/articles/CBMifEFVX3lxTE1qRUVDR1hkZkotczdTRTM5ZlJ6bEstak1QX3FyUEdZV2xsVjA5eDYteWtEUlJJNWZIbGtndGlvVnQtS2U1NXJ2VzNUaGpOWUhXTHVEWGktNXJ6ZktQcHZGWmlBWkUxZmQ5RlpoUXRQZjlaSVc0ZUptVjN3aV8?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxQUWlIQkEtV3A5SE9taWtKbUNiU0Zudnp1X3plYmpRY3YyRXNYdFYzVFlOYUFQLUdmY2xodjQ5eDE3T2dnd25jSmcwZGtlZ0JxeV8ydk0zQjBTbHczWlF3THRpVkQ1bVhxdWpvLXBJd0piaUplUHBpcmJZVkVHU0FmY1ZGYWZndFJxMUFoWjYwdHZBSzJKcEZLbm92azJKLTg?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxNOWRrX2V6REgxV2JtM3RyQUJjQ0xnSzZNc3UyUVNHZWxIaDFOdFI5UmNaSjRGZHRXWENwSDhCRWxrUjNIYWJ2NHZJZWE1X3JoT0Rkc3loc3BfTmh2amF1RC10Y3JUSFA0VzZsdVRfWUNtMnVaOFBKVzYwcnFyT3dLSmlrNHBZMnd2cjRkWXZ2emV0VGQ1ZmNaVlJPSWhzSDQ?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxPemRfX2I0QTR5M3ViaXh5N3dmR1dJeEt6dWZsRGRaUjliZnpxSHVPOWhTVzlMOEhNTUtWdE1OVEdlSzY4aDFVLUR6QXp1SEVnaTRCSGtmUGNlRDAyTW9WZ09wNWd6UTdoWTFrbHg3R08zc1dyVnMxZ2txdWQ5OEU2Y0laZW9pcGwxLWUzTVVHZHdPODhmbm9JTnFFYU5QVTJraFE?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxPN29WazVNNTNseGloU2s5UmNaSUZlQzR3Z2lFaEZEeXJndjhwdHhNbVpEcTVGSVUxSXZzdWQ3eG9tNFVDeXgxLXptQi0yd19HQ0kxcUFDVUNiYUVSZzB2QzdvT3NSVFBhUEt3dEdBSGhrTEUydXA1MjJCazJ1WVpHTWpBZkxyZkZHNlpuNUNzLXV0LV8xTmFVU0poZ0k2Y3dnaVE?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxNZ2x4aFRuSTUzYXFaQTc5S3E3N2xiRm9ZU0Npb3Q2RmFYN21JcUxfQld6MUZ0OUQ5ZkNtMzY5MDNXM2FQV0VwSlBWX0NDdi1uemdhdWFzcWVMSF9tUzhmSFA2Yl8xUWVtcUR4X0NrV090V2dTWE9MbjBCZ3VFY1NpOUVpSWNzSTRGTHpZNjVXZ1FqQ1JjU3I1alczTGpBZkswNnc?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
