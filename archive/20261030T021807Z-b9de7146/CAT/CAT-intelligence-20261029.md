# CAT Intelligence Report

- ticker: **CAT**
- Report as_of: **2026-10-29**
- Market data as_of: **2026-10-29**
- Quant sources: https://finance.yahoo.com/quote/CAT/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/CAT/key-statistics/
- AI analysis snapshot as_of: **2026-10-29**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-30T02:20:50.635950+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 13, 'ai': 11, 'unknown': 0})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **3** exact headline/source/date matches; prior report **20261029T020157Z-688a53f0/CAT** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'negative_sentiment_in_tailwinds': 1}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 10 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 54.17%; oldest publication 2026-10-26

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 647.3900 |
| Return 1D (%) | -9.2503 |
| Return 1W (%) | -7.8290 |
| Return 1M (%) | -21.4979 |
| Return YTD (%) | 13.9692 |
| Return 1Y (%) | 11.5126 |
| Annualized volatility (%) | 40.0527 |
| Beta vs SPY | 1.8801 |
| Max drawdown (%) | -38.9489 |
| Sharpe (rf=0) | 0.4730 |
| Downside deviation (rf=0, %) | 28.1036 |
| Sortino (rf=0) | 0.6741 |
| Historical VaR 95% (1D, %) | 4.0469 |
| Historical ES 95% (1D, %) | 5.5327 |
| Correlation vs SPY | 0.5966 |
| Tracking error vs SPY (%) | 34.0340 |
| P/E (trailing) | 27.87 |
| P/B | 14.13 |
| EV/EBITDA | 20.72 |
| Revenue growth (%) | 24.00 |
| Forward P/E (estimate) | 19.87 |
| Gross margin (%) | 29.71 |
| Operating margin (%) | 22.18 |
| Return on equity (%) | 56.97 |
| Free cash flow yield (%) | 1.70 |
| MA50 | 785.4196 |
| Close vs MA50 (%) | -17.5740 |
| MA200 | 806.6852 |
| Close vs MA200 (%) | -19.7469 |
| RSI (14, Wilder) | 26.6373 |
| MACD (12,26) | -33.6869 |
| MACD signal (9) | -26.5371 |
| MACD histogram | -7.1499 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'CAT': 271, 'SPY': 271}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 647.3900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -9.2503 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -7.8290 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -21.4979 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 13.9692 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 11.5126 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 40.0527 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 28.1036 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.6741 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.0469 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.5327 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5966 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 34.0340 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.8801 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -38.9489 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.4730 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 19.8676 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 29.7130 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 22.1830 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 56.9720 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.6966 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 27.8687 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 26.6373 -> Oversold momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -7.1499 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -17.5740 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -19.7469 -> Clearly below the moving-average trend level.

## TAILWINDS

### Caterpillar earnings beat by $0.17, revenue topped estimates
- Summary: Caterpillar earnings beat by $0.17, revenue topped estimates
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxONDVqbmdBdkpRNjZxbkJneVFadnFfX0JsUFhPT2E4NnhxcGNhVEc1UndNekl0TXhITW1zNzZ2ckdCb1pkLTZXT2ZUa2tpLTZibjZzVEtGZUxjVWhPdG52MTFxcVNpa0FxX0pBaGpSZUhRbWlOdDVwSEltY3M5NW4xRERQLUJJV1pWaHVWSDlrSk8xV0Y1d3BZUGFIVlZfN09pSHVjWVVtNG0?oc=5>

### Caterpillar (CAT) Q3 Earnings and Revenues Beat Estimates
- Summary: Caterpillar (CAT) Q3 Earnings and Revenues Beat Estimates
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxQRnRUZTFxQVcyNTNWM3V0MURNUjIxN0N2b2NnbDZGUU00cW5Cbm1WMWlOVE5DbWxmb2xvb1VSSUV6VTlVSGxseVhzU2NrS0ZRVDYxODBDcWJybTJoSlAyMFc2QUlDTjJFaWV5STNlWEZYOUw0MW1pTDdoLTJ0bF9YSkRJYUpPZTFETjZIT2VLT1lFcUg3a2RaQkVRSjFLTWwzUUxV?oc=5>

### Why is Caterpillar stock sliding today?
- Summary: Stock price decline noted, no company action cited.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxNSU95Smtjel92QjROdWFpM0pUTzFaUVhWRExBR1VmaDVlUF9nenFxNnc0RGpUbnF2bzhrQzhOZjNuRzh5M1NsNEZrd1pJRXRkYjBYeWJHWkdMOXA5TEJlVDBEeDNUbGM2Rm9kOU90Z2FKRTNaSV9zRV9MbU9pNC1Gd1JTeUFka3ViRENvVzNXSXRwYjc1MlpVSEhhT2tPUUJJaUE?oc=5>

### Caterpillar: Q3 Earnings Snapshot
- Summary: Q3 earnings reported, details not provided.
- Date: 2026-10-29 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxQUnlROWdTSTFOYmlFelh1TUtXaGg1YnI2dF9ta2RwQV83REcwQjZOMU5PMlhjM1dRcGg2RERKMWc4YzhURU9hTGtLOFpvajdodlJIVUJjdEVrc2tsbVZ1TkZNVm44cml4SmJSaklxb21fa1RKQzR2MFcyMEFJV19zVWgzTWJvbUtPOGFtRFJicHdJY3Nvd25UYmdpSDF5UQ?oc=5>

### Caterpillar Sales Jump on Growing AI Demand, But Wall Street Wanted More
- Summary: Sales increased due to AI demand, analysts sought higher guidance.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxOLVlpcFIzZ3pMMDZyanJZTXlqM1BxbzhjbE9VVEZBLWJqNVZDYnpZVjZhWVFwX2Z1QkVLNnlFc1hvVzM5blBhS2ZlODU3RlhEOUE4N3FGNU9lNFg0bFlod1Btai1uVVJLTXJoMmFiZlNRd29qZ21ZUlVwRTB5NG5LZ2tTem1FS3lpUEotSk5NTnhKMzdWOTZUWEY5YkRHdF9v?oc=5>

## HEADWINDS

### Caterpillar slides on Q3 earnings
- Summary: Caterpillar slides on Q3 earnings
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiggFBVV95cUxPbmpIV2p3MlljeUpvMFNCWFZ2SEd3ZU50R1JIQ3Roc1dndlQtR25zYjdCbDBoTXN0Q2VQZ0RwTjNESDd3ajNfcjlTTE8yTmZmd2ZtR3pUbzdJY2ZDQ0t0T2hWeGdlcVVYZzVOSktub2JsMnc4TEg3akVLVFVuQTVWYjB3?oc=5>

### Caterpillar’s stock is sinking. Here’s what that means for the Dow.
- Summary: Caterpillar’s stock is sinking. Here’s what that means for the Dow.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxNcTFJRWVHOUlkMlFXbFRrZ0xsSEZ1X2V1THprS3B5M2x3dUdnSEltSG5wZE93RDdCM2M4SjBlcDl4SFk5aG1FVjBNN3VFUjd5MG0tbEFIZWtIYzlscUVPaklaZGhIOW9saWYwSzFpNWkyd3o0UDB4LW9Pandpakt3VmlyLXljci1RS1lrcDJFWmliMmI0dWIwNEM4aGNfbHE5b1c1X3ZGRzNOOXI5NmZVNmgzSlVFY3ZJazZXaDB3MHhaUQ?oc=5>

### Caterpillar stock sinks after earnings: here's the case for buying
- Summary: Caterpillar stock sinks after earnings: here's the case for buying
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxOZGlQZHBxOU5KU2lhZDZSbTZld29ZU2dfNjJQWnZMWnQ1cEoxTVZrQi1PMGZBUVdud2ZkdXdDYVRqNjdMODctZ1R0YjBHaGk4ZlA4bHZnbTV3UUVIdjdHbDk3QWxsWkdOdlIwWXlwbDVWb3d2d1o1RUtlTHZWVy1FTmVHUGtIQ2ktNmt0OUN2TVIwTEFOS29jNURoaTVXNWFOVjBvVXllQ245MmhtaUk2aEFNRllabE1HUzQ3RDJUQQ?oc=5>

### Caterpillar Drops 7% as Moderate Sales Outlook Overshadows Beat; Deere Sits Out the Selloff, PACCAR Dips
- Summary: Caterpillar Drops 7% as Moderate Sales Outlook Overshadows Beat; Deere Sits Out the Selloff, PACCAR Dips
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxQZkstZEtWT3BFVzJLX09qbTFrX1k2dzRCLUxWbWh4U2otN1daVDE4SmduZkc0VFNmUzBUcG1fY0NFc21kUDMtR1NCVnFtNjdtRktBOVlFQW5wWnN1TWJoUWZVODZDRXZrY1ZWM1JVMlY2NEpJMW1pVDhQNElheDFKaDFvckk3TE12cnA2bkpDSG1vdUNTV01WM2QxM3lwbXZf?oc=5>

### Caterpillar Revenue Miss, Outlook Dig Hole For Dow Jones Industrial Average
- Summary: Revenue miss signals weaker performance, negatively impacting market outlook.
- Date: 2026-10-29 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxNRk54ajQ4MHcydlBCcGgtb21UekZtYnFXdVJGVF91d1ZwSjJqYUsxaXlZUWhoMFJaekV5QjlvU2tlTThoS0w3aUpIRzJqVkRoeDg2VUQzaGRjNmM3dnpzQUZVUE81czY2VUxseEVwZU5KQVJBbURuY3RRUDY3N2ZNaUpsY3kzMGFwcjRlaDBaRTRXOTdXTG9DYk93?oc=5>

### Why Is Caterpillar Stock Sinking Thursday? - Caterpillar (NYSE:CAT)
- Summary: Stock decline indicates investor concern over recent performance.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiygFBVV95cUxPUEl6amRQTlBpS0lYYjBuM2Z5cWJWeFBfYi11dkZtNC16Wi1mYkl1cVE2Ukk3ZXlBSHFIYy01bW5Na1RUblZQV1p5cU1OSDBweFpibUg4LXpkSFJGNXpUejNHbDlSVms4RTlzM2E1SXJDX3FTWW1ob0ZkLWVHaWMtU3lnTC14WkFvV0s3RGljVDZLOXNoZGlIT21WOFNVTnc5eWpsUy1yTkxPczZYM21UZGI2cU9tU0VZMVpRLVFPUDE2emZHaFM3Qll3?oc=5>

### Why Caterpillar (CAT) shares are falling today
- Summary: Shares falling today reflect market reaction to recent news.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxPMEVrQWc4M293b0pxWUxDYVRtb05YOHAyWFZqcDZCOGd5R3hzVGZuRjBPYmFndDBYenFFc0N3bl9URVlPYVdnMTdxR3A2YzJhTVJBckFyd3RIVEY1SFNsUDdyaVdZTTB4bjdtMFdVYnJjcGJCSU44dXV3QkJkUWRwYUdsR2t4dzhDZFk5T2NBUTdMT3dBeGtpSW5ESHlGR1V5?oc=5>

### Caterpillar Stock Slumps 9% Despite Q3 Earnings Beat As Revenue Falls Short Of Estimates
- Summary: Revenue miss outweighs earnings beat, causing a sharp stock drop.
- Date: 2026-10-29 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxOQlhocGZIRndSYzQ1dTJlZUYzVmpZdVRXYlF6QzZnc095NU5DNkY1WWJpMlkxZUx6dkM3U1lhYWIzSTBPTHNnUThaTTZKRGJ0S0g5QU9IYkF2Z2kwa3FvdG1HUnA1YlZHdzFPZjZXODVFQWFfbFkxaHFRVDZQX2xpbEFmRkFkYWZ4NGd3UnJodDhNZzVUUkxBdDJVelFUTDRZ?oc=5>

## CATALYSTS

### Caterpillar Stock Dives Over 7% as Analysts Cut CAT Price Targets After Earnings
- Summary: Caterpillar Stock Dives Over 7% as Analysts Cut CAT Price Targets After Earnings
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxOUWx4S1ZIcFRvc00wTldHaENCZTVJSnItdDdhbHBDX1p5NEZZSEU2dFRXNUkwdGlwTld6U0RFNElqUWttU0VUZUR6cVF3dmgxUE1TYkpBZ1IxZC1kRHlMa0kxb3lzZTJoT2NuZG14blpFMkl3SUVjZmwyZDhzUEcwd3FHTVcyYkpCRlFBanRpSTB0aHVBY0NHVHpZOHJtblNzMVZINW1DbVF1blRx?oc=5>

### Caterpillar, the Dow's best stock of 2026, is unraveling — and an earnings beat couldn't stop it
- Summary: Caterpillar, the Dow's best stock of 2026, is unraveling — and an earnings beat couldn't stop it
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi4gFBVV95cUxPQk5icEllSDRCZkxZWk9JRDNoLWtacDBFWVh6QjZxcUpIa1VIbXBxa3pSbV9lc2JzejN3aEQ3THloSWp2TzQzeGJZcDAtZFU4WXlQWjhrNS1OVFU2ZkZBT0QyMG5JRHVaTjdJbmxoakpFWUNqbGNKRkxPbEMxUVF6LXgyelNZVlN4YUJHTUd3cTVSSVVjVE9ZTkpPSlNCdkNYX1VjSkdSenNxYmtSekx4eFVqU3Z5QU9SekNDUmpSZXdWelFOektIQlljclZWUlhOdmpkajJpRkFhOUh2TWVBc0ln?oc=5>

### Caterpillar shares slump 10% despite earnings beat amid rapid AI buildout
- Summary: Caterpillar shares slump 10% despite earnings beat amid rapid AI buildout
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxORmZTQVpMQ0FFQnJFeGxTUlRWWjlHUHpYclVVSzBXWFBtV2ZONkpYWWl0elE3OEtacDdDR3p0bXVNblRLNUtzZGQySThCVEFYWlBtZjdmWGRUWjh5azZhSkp5bHd2aEkxUzlXa0VYVGlWNjZUMVNzSkVBQ1A5amc5OUJiZzFSbDBsbzI2NF93RnV4UjBSRndaMVFjWEFvVVJGNFNSSDFjQzNyZw?oc=5>

### Caterpillar (CAT) Q3 Earnings: How Key Metrics Compare to Wall Street Estimates
- Summary: Caterpillar (CAT) Q3 Earnings: How Key Metrics Compare to Wall Street Estimates
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNTlFvcnJ2OFNOdGFRcGw5SG1IZVIycHJMd2hxMkFVZUQtcHJCeW5sYmxXNEtCNVN2b3habXFlbGVSUXdkZFZYOUJLLVN1bk0zWUZTeWZsRUo4MU5zeFh2UFJwNUxTOEtFMlZrY3pkZFliTGh5eS1QR3VFWmdHa3BPWUJ1NXEzLUN5YzFGZFpoSUhMelhxU2V6Z3gxY3E?oc=5>

### Caterpillar Inc. Q3 2026 Earnings Call Summary
- Summary: Caterpillar Inc. Q3 2026 Earnings Call Summary
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxOMkJveTdPZVhNRXo2VHRrQVdGSnZOOU5yQll4Wkp4T3BadTAycUhIS0JLQmtTSEJOUzFfSkVFZlpidGJpNF9YVzVrbUNkbEhTM283Z1lDUk9qc1lFbUdnVkNkbUZoeTZ1T1F2aUdWb1NrNnRBbE01anJWUmpLYnNPcnFFRjJFU2QzZUVfT2t2UEJfVVZJRGNVWXN5WVF2UQ?oc=5>

### Caterpillar Inc (CAT) (Q3 2026) Earnings Call Highlights: Record $20. ...
- Summary: Caterpillar Inc (CAT) (Q3 2026) Earnings Call Highlights: Record $20. ...
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxNc2pJTGs5Q0dqdkFseTc3RC1lMGgwdEVEaEtZdTFiZjZ1WUx5QklBbW5OSXJKcHhEUG5SOHhWQmVNY0hzRUpjc3pyckNoYnlUOHVuN3RFdlNXbkZpcFFCRzJWOVNvdUhia0VzeGI5dEcwVzlCd0JNTmx5el9HQi02U09FUTF1VlBHSGZpZUxyU09DZTJ0R293?oc=5>

### Caterpillar earnings: what to look for from CAT
- Summary: Caterpillar earnings: what to look for from CAT
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxPemNZNTRhaF82ZzBVWlItSDA2VnhjUVdIblNFa3BCVGZlbVR0QUhMZzlFN21YaGdNNUY1WVRrUE9uSF9iYVN1Z2tVMzBLV1J5a0tjci0zNmhvb19fd0p3LU1Neno2XzlSWVhaTUFtbGE1bWxUbk9fN1hBeGJYZnJlZ2NtUWZvdlY2ckRzRm9SRWd6UEFqS1FQY0xn?oc=5>

### Dear Caterpillar Stock Fans, Mark Your Calendars for October 29
- Summary: Upcoming event on October 29, likely earnings or guidance.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxQc1ZHR1lneTJYUC1xZkdaOHdKMVdIT3gzNlctZEliZHJmWGh2bVJ0UVlQbW41d3M4NThYRjNOV0V2VEFIal90SndCT3dZZExJUjdLS1RxX2tMQ3V3bE9MZHdOQVRBSjVpUVJCR1JiSm5ZY3FoMXF5OV9sV3lOZ1JvSmsyX0Q4VjJ6dzJLNW4tdDF2UkR3aVNvUGtvVDAtVUxXbFNuZldubThVUQ?oc=5>

### Caterpillar Set to Report Q3 Earnings: Buy, Sell or Hold the Stock?
- Summary: Caterpillar will announce Q3 earnings, potentially influencing stock valuation.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxQMUFqOFpQTDhPdlFBajh6SDRjQkdiSERCTnhyeEc1LXo4a3BMV3hjaXFtcGtZS01iQVR5YkM3UkZkS2stcjU4ZGh3T1dpdk1wZVFValBuWU44cThnLVFQclQ4VWFrb0d1UGZzbUlBclVRc3djd1A2NjlJaXNlRXhJNzRjaG51aTBrVXNXajdMeDFkWkhjUzdLQmF0cU44QzNF?oc=5>

### Caterpillar (CAT) Stock May Be 20% Undervalued Following Backlog Questions
- Summary: Analysis suggests potential undervaluation due to backlog concerns.
- Date: 2026-10-28 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxNamg4bGJCNnJ2bkNBa0JFTGZfZFVrU0JsbEN0RE5vUXBQcGZOYU1lV1I2TzBkTDF1VDhWM2lOTkRfb0xNY21mT0FaSHFuWEpqTTBtM3JCbHRaMmJHZ0ZoWGlLVjViS0VTTWJvc1AyS3NkLUxibHBQMUVOaF9kUlgzWDVvOFllMWVJT1RSb003QXRrWUxUaWRPSg?oc=5>

### Cat Financial Announces Second-Quarter 2026 Results
- Summary: Release of Q2 2026 financial results provides new data for investors.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxQR2tlUVVCbVQ2U1BMMnc0NDZOaTFUTWhvdWJETVo0RW5kazlZaE9ydkdRbmpNdnhVS2FkM2ZGekFIZk5UYml6X1lXOU9SS2RaVVBvVUJyYkZFNGtWX1B6dzI0X2tfN2ktZW9YQXhYWWlMTGtpWGNlREFZZEw1ZDE2bDdqQk5obHh5cnNLNy0xZngxbGNWR093aDFn?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **CAT** | **27.87** | **14.13** | **20.72** | **24.00** | **297,588,916,224.00 USD** | **11.51** |
| DE | 36.69 | 6.36 | 27.40 | 4.90 | 177,952,768,000.00 USD | 40.98 |
| CNH | 45.16 | 1.80 | 36.97 | 2.00 | 18,156,111,872.00 USD | 7.34 |
| CMI | 26.47 | 5.55 | 15.29 | 9.40 | 71,314,333,696.00 USD | 19.11 |

Peers fetched as_of: 2026-10-29; CAT reuses existing data (market data as_of: 2026-10-29); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-29
- Next expected earnings: N/A (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-29

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-08-05
- Revenue (latest available single quarter): 20,543,000,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- Net income (latest available single quarter): 1,141,000,000.00 USD; period 2011-07-01/2011-09-30; fiscal year/reporting period 2011/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/18230/000001823026000046/cat-20260630.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiqAFBVV95cUxONDVqbmdBdkpRNjZxbkJneVFadnFfX0JsUFhPT2E4NnhxcGNhVEc1UndNekl0TXhITW1zNzZ2ckdCb1pkLTZXT2ZUa2tpLTZibjZzVEtGZUxjVWhPdG52MTFxcVNpa0FxX0pBaGpSZUhRbWlOdDVwSEltY3M5NW4xRERQLUJJV1pWaHVWSDlrSk8xV0Y1d3BZUGFIVlZfN09pSHVjWVVtNG0?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxQRnRUZTFxQVcyNTNWM3V0MURNUjIxN0N2b2NnbDZGUU00cW5Cbm1WMWlOVE5DbWxmb2xvb1VSSUV6VTlVSGxseVhzU2NrS0ZRVDYxODBDcWJybTJoSlAyMFc2QUlDTjJFaWV5STNlWEZYOUw0MW1pTDdoLTJ0bF9YSkRJYUpPZTFETjZIT2VLT1lFcUg3a2RaQkVRSjFLTWwzUUxV?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxNSU95Smtjel92QjROdWFpM0pUTzFaUVhWRExBR1VmaDVlUF9nenFxNnc0RGpUbnF2bzhrQzhOZjNuRzh5M1NsNEZrd1pJRXRkYjBYeWJHWkdMOXA5TEJlVDBEeDNUbGM2Rm9kOU90Z2FKRTNaSV9zRV9MbU9pNC1Gd1JTeUFka3ViRENvVzNXSXRwYjc1MlpVSEhhT2tPUUJJaUE?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxQUnlROWdTSTFOYmlFelh1TUtXaGg1YnI2dF9ta2RwQV83REcwQjZOMU5PMlhjM1dRcGg2RERKMWc4YzhURU9hTGtLOFpvajdodlJIVUJjdEVrc2tsbVZ1TkZNVm44cml4SmJSaklxb21fa1RKQzR2MFcyMEFJV19zVWgzTWJvbUtPOGFtRFJicHdJY3Nvd25UYmdpSDF5UQ?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxOLVlpcFIzZ3pMMDZyanJZTXlqM1BxbzhjbE9VVEZBLWJqNVZDYnpZVjZhWVFwX2Z1QkVLNnlFc1hvVzM5blBhS2ZlODU3RlhEOUE4N3FGNU9lNFg0bFlod1Btai1uVVJLTXJoMmFiZlNRd29qZ21ZUlVwRTB5NG5LZ2tTem1FS3lpUEotSk5NTnhKMzdWOTZUWEY5YkRHdF9v?oc=5
- https://news.google.com/rss/articles/CBMiggFBVV95cUxPbmpIV2p3MlljeUpvMFNCWFZ2SEd3ZU50R1JIQ3Roc1dndlQtR25zYjdCbDBoTXN0Q2VQZ0RwTjNESDd3ajNfcjlTTE8yTmZmd2ZtR3pUbzdJY2ZDQ0t0T2hWeGdlcVVYZzVOSktub2JsMnc4TEg3akVLVFVuQTVWYjB3?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxNcTFJRWVHOUlkMlFXbFRrZ0xsSEZ1X2V1THprS3B5M2x3dUdnSEltSG5wZE93RDdCM2M4SjBlcDl4SFk5aG1FVjBNN3VFUjd5MG0tbEFIZWtIYzlscUVPaklaZGhIOW9saWYwSzFpNWkyd3o0UDB4LW9Pandpakt3VmlyLXljci1RS1lrcDJFWmliMmI0dWIwNEM4aGNfbHE5b1c1X3ZGRzNOOXI5NmZVNmgzSlVFY3ZJazZXaDB3MHhaUQ?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxOZGlQZHBxOU5KU2lhZDZSbTZld29ZU2dfNjJQWnZMWnQ1cEoxTVZrQi1PMGZBUVdud2ZkdXdDYVRqNjdMODctZ1R0YjBHaGk4ZlA4bHZnbTV3UUVIdjdHbDk3QWxsWkdOdlIwWXlwbDVWb3d2d1o1RUtlTHZWVy1FTmVHUGtIQ2ktNmt0OUN2TVIwTEFOS29jNURoaTVXNWFOVjBvVXllQ245MmhtaUk2aEFNRllabE1HUzQ3RDJUQQ?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxQZkstZEtWT3BFVzJLX09qbTFrX1k2dzRCLUxWbWh4U2otN1daVDE4SmduZkc0VFNmUzBUcG1fY0NFc21kUDMtR1NCVnFtNjdtRktBOVlFQW5wWnN1TWJoUWZVODZDRXZrY1ZWM1JVMlY2NEpJMW1pVDhQNElheDFKaDFvckk3TE12cnA2bkpDSG1vdUNTV01WM2QxM3lwbXZf?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxNRk54ajQ4MHcydlBCcGgtb21UekZtYnFXdVJGVF91d1ZwSjJqYUsxaXlZUWhoMFJaekV5QjlvU2tlTThoS0w3aUpIRzJqVkRoeDg2VUQzaGRjNmM3dnpzQUZVUE81czY2VUxseEVwZU5KQVJBbURuY3RRUDY3N2ZNaUpsY3kzMGFwcjRlaDBaRTRXOTdXTG9DYk93?oc=5
- https://news.google.com/rss/articles/CBMiygFBVV95cUxPUEl6amRQTlBpS0lYYjBuM2Z5cWJWeFBfYi11dkZtNC16Wi1mYkl1cVE2Ukk3ZXlBSHFIYy01bW5Na1RUblZQV1p5cU1OSDBweFpibUg4LXpkSFJGNXpUejNHbDlSVms4RTlzM2E1SXJDX3FTWW1ob0ZkLWVHaWMtU3lnTC14WkFvV0s3RGljVDZLOXNoZGlIT21WOFNVTnc5eWpsUy1yTkxPczZYM21UZGI2cU9tU0VZMVpRLVFPUDE2emZHaFM3Qll3?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxPMEVrQWc4M293b0pxWUxDYVRtb05YOHAyWFZqcDZCOGd5R3hzVGZuRjBPYmFndDBYenFFc0N3bl9URVlPYVdnMTdxR3A2YzJhTVJBckFyd3RIVEY1SFNsUDdyaVdZTTB4bjdtMFdVYnJjcGJCSU44dXV3QkJkUWRwYUdsR2t4dzhDZFk5T2NBUTdMT3dBeGtpSW5ESHlGR1V5?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxOTDVlem1BYlZ5ZjM3Mk13TTdhMGFNcVRJWDQwZ3huQ0d0MEItSC1kWmVNbUlHUkZfV0FPSGhIOVFFTVl2NEM4UFlvUU15NTRwdXNfUUFUN2x4djNDYzg4Vkt4Z0ZlcDRFejQ4NzMwbllmMEZsX3cwNU5hOUhYZkRFOFp6cGtBMHNFMUFyOVlwdl9HTWdFNDB3YnZ2Z2lOR0JYM0tKczFoUUo?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxOQlhocGZIRndSYzQ1dTJlZUYzVmpZdVRXYlF6QzZnc095NU5DNkY1WWJpMlkxZUx6dkM3U1lhYWIzSTBPTHNnUThaTTZKRGJ0S0g5QU9IYkF2Z2kwa3FvdG1HUnA1YlZHdzFPZjZXODVFQWFfbFkxaHFRVDZQX2xpbEFmRkFkYWZ4NGd3UnJodDhNZzVUUkxBdDJVelFUTDRZ?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxOUWx4S1ZIcFRvc00wTldHaENCZTVJSnItdDdhbHBDX1p5NEZZSEU2dFRXNUkwdGlwTld6U0RFNElqUWttU0VUZUR6cVF3dmgxUE1TYkpBZ1IxZC1kRHlMa0kxb3lzZTJoT2NuZG14blpFMkl3SUVjZmwyZDhzUEcwd3FHTVcyYkpCRlFBanRpSTB0aHVBY0NHVHpZOHJtblNzMVZINW1DbVF1blRx?oc=5
- https://news.google.com/rss/articles/CBMi4gFBVV95cUxPQk5icEllSDRCZkxZWk9JRDNoLWtacDBFWVh6QjZxcUpIa1VIbXBxa3pSbV9lc2JzejN3aEQ3THloSWp2TzQzeGJZcDAtZFU4WXlQWjhrNS1OVFU2ZkZBT0QyMG5JRHVaTjdJbmxoakpFWUNqbGNKRkxPbEMxUVF6LXgyelNZVlN4YUJHTUd3cTVSSVVjVE9ZTkpPSlNCdkNYX1VjSkdSenNxYmtSekx4eFVqU3Z5QU9SekNDUmpSZXdWelFOektIQlljclZWUlhOdmpkajJpRkFhOUh2TWVBc0ln?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxORmZTQVpMQ0FFQnJFeGxTUlRWWjlHUHpYclVVSzBXWFBtV2ZONkpYWWl0elE3OEtacDdDR3p0bXVNblRLNUtzZGQySThCVEFYWlBtZjdmWGRUWjh5azZhSkp5bHd2aEkxUzlXa0VYVGlWNjZUMVNzSkVBQ1A5amc5OUJiZzFSbDBsbzI2NF93RnV4UjBSRndaMVFjWEFvVVJGNFNSSDFjQzNyZw?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNTlFvcnJ2OFNOdGFRcGw5SG1IZVIycHJMd2hxMkFVZUQtcHJCeW5sYmxXNEtCNVN2b3habXFlbGVSUXdkZFZYOUJLLVN1bk0zWUZTeWZsRUo4MU5zeFh2UFJwNUxTOEtFMlZrY3pkZFliTGh5eS1QR3VFWmdHa3BPWUJ1NXEzLUN5YzFGZFpoSUhMelhxU2V6Z3gxY3E?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxOMkJveTdPZVhNRXo2VHRrQVdGSnZOOU5yQll4Wkp4T3BadTAycUhIS0JLQmtTSEJOUzFfSkVFZlpidGJpNF9YVzVrbUNkbEhTM283Z1lDUk9qc1lFbUdnVkNkbUZoeTZ1T1F2aUdWb1NrNnRBbE01anJWUmpLYnNPcnFFRjJFU2QzZUVfT2t2UEJfVVZJRGNVWXN5WVF2UQ?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxNc2pJTGs5Q0dqdkFseTc3RC1lMGgwdEVEaEtZdTFiZjZ1WUx5QklBbW5OSXJKcHhEUG5SOHhWQmVNY0hzRUpjc3pyckNoYnlUOHVuN3RFdlNXbkZpcFFCRzJWOVNvdUhia0VzeGI5dEcwVzlCd0JNTmx5el9HQi02U09FUTF1VlBHSGZpZUxyU09DZTJ0R293?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxPemNZNTRhaF82ZzBVWlItSDA2VnhjUVdIblNFa3BCVGZlbVR0QUhMZzlFN21YaGdNNUY1WVRrUE9uSF9iYVN1Z2tVMzBLV1J5a0tjci0zNmhvb19fd0p3LU1Neno2XzlSWVhaTUFtbGE1bWxUbk9fN1hBeGJYZnJlZ2NtUWZvdlY2ckRzRm9SRWd6UEFqS1FQY0xn?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxQc1ZHR1lneTJYUC1xZkdaOHdKMVdIT3gzNlctZEliZHJmWGh2bVJ0UVlQbW41d3M4NThYRjNOV0V2VEFIal90SndCT3dZZExJUjdLS1RxX2tMQ3V3bE9MZHdOQVRBSjVpUVJCR1JiSm5ZY3FoMXF5OV9sV3lOZ1JvSmsyX0Q4VjJ6dzJLNW4tdDF2UkR3aVNvUGtvVDAtVUxXbFNuZldubThVUQ?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxQMUFqOFpQTDhPdlFBajh6SDRjQkdiSERCTnhyeEc1LXo4a3BMV3hjaXFtcGtZS01iQVR5YkM3UkZkS2stcjU4ZGh3T1dpdk1wZVFValBuWU44cThnLVFQclQ4VWFrb0d1UGZzbUlBclVRc3djd1A2NjlJaXNlRXhJNzRjaG51aTBrVXNXajdMeDFkWkhjUzdLQmF0cU44QzNF?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxNamg4bGJCNnJ2bkNBa0JFTGZfZFVrU0JsbEN0RE5vUXBQcGZOYU1lV1I2TzBkTDF1VDhWM2lOTkRfb0xNY21mT0FaSHFuWEpqTTBtM3JCbHRaMmJHZ0ZoWGlLVjViS0VTTWJvc1AyS3NkLUxibHBQMUVOaF9kUlgzWDVvOFllMWVJT1RSb003QXRrWUxUaWRPSg?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxQR2tlUVVCbVQ2U1BMMnc0NDZOaTFUTWhvdWJETVo0RW5kazlZaE9ydkdRbmpNdnhVS2FkM2ZGekFIZk5UYml6X1lXOU9SS2RaVVBvVUJyYkZFNGtWX1B6dzI0X2tfN2ktZW9YQXhYWWlMTGtpWGNlREFZZEw1ZDE2bDdqQk5obHh5cnNLNy0xZngxbGNWR093aDFn?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
