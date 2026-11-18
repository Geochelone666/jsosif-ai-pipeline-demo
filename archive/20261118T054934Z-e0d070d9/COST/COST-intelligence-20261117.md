# COST Intelligence Report

- ticker: **COST**
- Report as_of: **2026-11-17**
- Market data as_of: **2026-11-17**
- Quant sources: https://finance.yahoo.com/quote/COST/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/COST/key-statistics/
- AI analysis snapshot as_of: **2026-11-17**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-18T06:13:52.258172+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 8, 'ai': 11, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **9** exact headline/source/date matches; prior report **20261117T062519Z-6171f6c2/COST** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'directional_claim_without_event_type': 1, 'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 9 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 68.0%; oldest publication 2026-11-11

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 1110.0800 |
| Return 1D (%) | -0.3286 |
| Return 1W (%) | 4.1214 |
| Return 1M (%) | 12.3961 |
| Return YTD (%) | 29.4881 |
| Return 1Y (%) | 22.3580 |
| Annualized volatility (%) | 20.3654 |
| Beta vs SPY | -0.1691 |
| Max drawdown (%) | -18.1993 |
| Sharpe (rf=0) | 1.0966 |
| Downside deviation (rf=0, %) | 13.7435 |
| Sortino (rf=0) | 1.6250 |
| Historical VaR 95% (1D, %) | 2.0802 |
| Historical ES 95% (1D, %) | 2.7374 |
| Correlation vs SPY | -0.1144 |
| Tracking error vs SPY (%) | 25.8628 |
| P/E (trailing) | 53.65 |
| P/B | 13.74 |
| EV/EBITDA | 33.89 |
| Revenue growth (%) | 11.10 |
| Forward P/E (estimate) | 44.33 |
| Gross margin (%) | 12.77 |
| Operating margin (%) | 3.80 |
| Return on equity (%) | 28.40 |
| Free cash flow yield (%) | 1.37 |
| MA50 | 974.0449 |
| Close vs MA50 (%) | 13.9660 |
| MA200 | 974.5598 |
| Close vs MA200 (%) | 13.9058 |
| RSI (14, Wilder) | 75.4437 |
| MACD (12,26) | 37.7197 |
| MACD signal (9) | 32.3262 |
| MACD histogram | 5.3935 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'COST': 284, 'SPY': 284}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 1110.0800 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.3286 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 4.1214 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 12.3961 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 29.4881 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 22.3580 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 20.3654 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 13.7435 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.6250 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.0802 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.7374 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.1144 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 25.8628 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.1691 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -18.1993 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.0966 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 44.3257 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 12.7660 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 3.7970 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 28.4020 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.3728 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 53.6530 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 75.4437 -> Overbought momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 5.3935 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 13.9660 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 13.9058 -> Clearly above the moving-average trend level.

## TAILWINDS

### Costco Stock (COST): Why Mizuho Removed the Big-Box Retailer from Its ‘Top Pick’ List
- Summary: Costco Stock (COST): Why Mizuho Removed the Big-Box Retailer from Its ‘Top Pick’ List
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxOdlVURFpSc0dkWHVKY3M3d0c0WDZWNTh5RHBxbkJ2MDV1Nmh0RGdQV1hNbWtvU2NkMzRobmQ0SlNPbjNMTWlFbjlsVEZKbEhFdXNzRlprcWRJeG9ERDJFcjNFSWJSd3hEdXhsZjdkV28xdnJTSGFVMEt0eWJPRjFtWjdNbG00cXpHVWVpMjVXWGdfbnczSm1hUTBKSG5ZcGkxWWNYSWNDWF9yZnpsYUV3?oc=5>

### Costco’s $30-per-share special dividend means just 3 shares could cover your $65 membership. But there’s a catch
- Summary: Costco’s $30 special dividend could offset membership costs for a few shares, offering a financial benefit to shareholders.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxQNU1XWlFxZWMyYTg0NHd3by15cjhlX3FBQXhnaFpiT2JXRXR2VVRLQmZsbUJVN2Fmd3lJMTdpRUhQNUpNcC1uLUUtYUlnS00yQVZhSVFDWHgtbm9oajE4ZlktcHFvQWZJRVlZZ1hNYmxsQmZaMHFOdHVxZUhIVkN1RmhkY05KaVRsb0lNdFdCVUNkSWI4QmNn?oc=5>

### Jim Cramer says Costco's hefty special dividend signals ‘more gains ahead’
- Summary: Cramer praises special dividend, suggesting future gains.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMie0FVX3lxTE1mem1WV09KMHJEbGxFR0RXanhfVUhVV092TVU2RDRPUUp3Ym93enJSR3htWWV6V1pPb19QRnB5WVlOR0dvVkM0OGQ3SU1ZYk54VWlzUFktdDczWnFDc21MaDJqcFp1b1A3Z001d1BzYzI2N2tXRlZLM2QyTdIBgAFBVV95cUxOQmx1T1pDSkJ5UV9fUTROQUNwTU42VTZPVWRvM3ZORXNlNEV1V1ZiT1MwYVlRQU54cDRoWVhlT1BqcW5hcjZoZnZOMGhvSzRVZlZFY0pwek40TmFXQ1pTT0w1cHFYRFJ0ZzhWUjFnck44RGVtdGx1WXVFZzQtNXgwOQ?oc=5>

### Mizuho raises Costco stock price target to $1,150 on strong sales
- Summary: Mizuho lifts target, citing robust sales.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxOVGE2THhHUElqcTU3WTRTZ1dRZlY0dFJlU3RlV0E5YzRpOTRKTGd5N3dJaEoxamZuU1NPemh6SE16dGhkbVMzOE9ESnhqNWtCc3E5eTR5Ty1LWjdkWXpTdnBic1dNbFdRN1BKV1gtRWt4VnJLMDQxVzRTUTBCRU9DVENqR1E4UTZ3M3JaQWI4ajEyM0s0bGdDcFd4V0xtNE43QWw1SmhNenlkWHU1ZG1lT3RZQW5ia2lPaU5EQnJHTTE?oc=5>

### Costco has surprising response to price adjustments
- Summary: Costco responds positively to price adjustments, potentially boosting sales.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxNZFVtVFdZRXg5WjFZYmw4Ym5QT3lTcnVQLWJabUVjYjVXZkotN2hsVlNoejFOTEF6c0Y4VzFka0NmVFB0NjBsODM5ZTkwdUZjT3lOQVJKM0E3aWpTdUoyQnp4VEExNHhGa3VBT1VBaVRybG1qbkRkV2o0ampNOEVfYmtqRW1KUjdIeDZTNjQ1THV6ZzQ3TXhZVjYyOVJJV0puYVFXeFU4RFVpa19maVE?oc=5>

## HEADWINDS

### “Costco Has Terrible Governance,” Says Lean Startup Author. Its Stock Just Hit a Record
- Summary: Governance concerns raised, potentially harming perception.
- Date: 2026-11-16 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxNWnB6WnliS3RMSzhFdW9BM3AyVV92b2IzSHZ4ZUFjY2FWSjQyQ2dNN1pKcG5NbTdhMDlueExkM0x4WENEVVBobUZLMWtCR2tHMmZuX29ISnRVM194NEkzMXV2bFNxc1VUUW5CcVBueXRGNlVQOVVxOGZ0WEstaHZSMXZGTHl0XzI1anVNOHVoRFhVY1ZoSi1rV3pMRXlFcTI4Sy1pWjhtNmJ4aE1YMGc?oc=5>

### Costco Stock Outlook: Is Wall Street Bullish or Bearish?
- Summary: Uncertain market sentiment, no clear direction.
- Date: 2026-11-16 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxOZllkN082dEhId0dnX3hLazBDT0FKN2poT3NxLVpvbkhkNDl5NjY3ei1YUUpPRmNzOWFJWHhpYUtGcDhFN0w5Vml0VzVxV0hRUk9Wekt2MlNpc05oZmRacVFycWlaV196LXFLUWVjd2NfYWNxTW52VmpBRFJSRzdBLUswX3c4OFdnYzFLZkVPVmI0cHZKOTNkeW9WSXpDZw?oc=5>

### Is Costco Stock Increasing Your Market Risk?
- Summary: Costco stock may elevate market risk for investors.
- Date: 2026-11-17 | Impact: high | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxOZmVoRVEzaVZmR2dJUXBIbmxVZzVBLUd3TW9md1VqZ1AxTWdTcm4xMnVOQTU2dl9yT09mMkcyaGJRbWpId3czN1ppbU51bjVHRGhrU1ZlQnpvb0xCelRSTEdUREoyYlBUUDlMdUxhcFFZSjdzU2VGRjBFeC1kWTlyblZMR1Blc1hhVDVxQ3ZGcVJTd2pyV1BkWko0QjUzcjdqdlE?oc=5>

### What Are Costco Stock Bulls Not Worried About?
- Summary: Bulls express concerns over Costco, indicating potential downside risk.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNN1hkY2p3V3FFb0NZeXpsZjJPV3l0NVZ4X0V1X0ZMZFlTWTN1OHlPVzgybVZPMzVkU0l3aTFoQUg5VDA0VDNQNnc5bHFETUZiMGhmRnkwb0JBeWlMQnR2d2NGZFVmZ1RUVUJiU1BtRTBfNkZVdGpPdEM0Y2kwdXk3TU9tc2pBNHpaSEZ3NHBiUTJLdlRPbXhQbWd2SQ?oc=5>

## CATALYSTS

### Costco Is Paying Out $13 Billion in Special Dividends This Year. Is the Stock a Buy?
- Summary: Costco Is Paying Out $13 Billion in Special Dividends This Year. Is the Stock a Buy?
- Date: 2026-11-15 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxOeElIQXVxNEtIWWJkMXdiQ0hfOUtOelZ5ZGhCV3MzUldkTXNRRlFwa0hYTE5xMTVZTENtRmI0U3dvSGtrcjE4ZmdYRU5sMlB1bGRia3FaWlpmSnh1V1RkeW04TC04ejdxQ2hRMktuM0xmRVphNi1rUWk4VFo4VExyaFhMTzliSzhxRFpWa2VELTVwQXFiS2VwSGt6MHdzQQ?oc=5>

### Costco is benefiting from ‘apocalyptic concerns’ as customers stock up on goods, analysts say
- Summary: Costco is benefiting from ‘apocalyptic concerns’ as customers stock up on goods, analysts say
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizgFBVV95cUxQem9tZXVZeGpsMVdSQXp5dUFaeFplWG1WR25aaVFjSGxRSnJTMENmTWxaQ3p1OEhZeGpHSng0LW1LaTh3cWp2cjJsTzJKN2UxU3J6enBvRmVES21iaFRzbk9Tam9TMnY0eGphOHpJNl81dDVEYlIzYnEtODBRR1AxUlZDOXJhbjFjaWlJTXVGQjZfWG5CaWEyeFVJMnVFdm5oZTlJS2hXeUozVlE2TzZOejdTS3J3MjlodXV0ZkJJaElSQVJLbDR5N3lIUmc5dw?oc=5>

### Costco Hits 52-Week High on Strong Sales and Special Dividend
- Summary: Costco Hits 52-Week High on Strong Sales and Special Dividend
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxQMUpXaW56UjBNc0VnVkd3Q2E4aE1xMjQyTnNLZjlmYW1Dak5yS0NfY0VfaGhEWnRWazJxdV82ZlZPaXJqaGNsaWM4Nnk2emVocVVEQUVyTFJsc2NlRF90czBLdV9WdDhVQ2JXYzJjOHpSVFpDaHBiNURzX0sxakNoMjVhelZRS2pDTXNjYkxpajZseTA?oc=5>

### COST Stock Rises Overnight: Costco’s $30 Special Dividend Has Retail Celebrating ‘Santa Coming Early’
- Summary: COST Stock Rises Overnight: Costco’s $30 Special Dividend Has Retail Celebrating ‘Santa Coming Early’
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxPYU03ekRHaEc0TWl0STFiVExmZnBzd0xRTXdpa2ctc05XeS1qRWlvb3J1NFdaMHVFc2lsLVNkeG1meGZSZTN6MUlLeTRNZFI3c19JeEhWbTlFdFV3MkxJWkt3a05iWVp3ZnZYanZXSTNWV21pLVZ6NTFrT3ZFYmZSOEVFN2pONzdlNHdSOHFYQTJJVzkxeWZQYmZjSlpJMmc?oc=5>

### Costco (COST) Declares $30 Special Dividend And Reauthorizes $4 Billion Buyback
- Summary: Costco (COST) Declares $30 Special Dividend And Reauthorizes $4 Billion Buyback
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNVk1SbzRkY0hkTVlRbk9LWHduY2lLZnJjeUIxU3NvbWVNLWhVZFFJMjNJYUNlSF92N2p5YTY5RFFocmVYSGdKakNybjRTeVZZd250OGg0aWNVVmR6UzFhVHpXRnhVREVmbHJ0RXBVZU5HUVRWelYyRUFxOVhHeHN1QXAxUGxYRVZJSW93OEhjSnJ0V3BGMm9OeURlbk8?oc=5>

### Costco Hits All-Time High Amid $4 Billion Buyback, Special Dividend
- Summary: Costco Hits All-Time High Amid $4 Billion Buyback, Special Dividend
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxNa3JZUXJRekpXSnlWaGt4cmZWTnQwN0FmRjNtRHFzb1VLZnRtZmtuV1hpV0JKamc1OUpIN3VSc3QxYWVZRndEMExETzlycE9wQlVILXdSc1RyTjhaSVVsOWJoLXd1TVV2a0d6Y2RuYXN1eXJGSld4LWpQVUhkUGNrc1ZiMC0tRVNVbi16NW9NTVZ0M25nNVE?oc=5>

### Costco Stocks Rise 1.62% After Record $30 Special Dividend Worth $13.3 Billion
- Summary: Costco Stocks Rise 1.62% After Record $30 Special Dividend Worth $13.3 Billion
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxNNDhKRGlWaVlleFYxdl9yZTJBTGc5Z0plWEp0Zy1sOTdiNGNneDd6bWkxOEtWRUtBN250aU1Ta2FZcEg3WFRNMXl5b1ZDN1NTLU03R3ZSckgxb1BFelRFUGtLMlFrVThxeFRFNUQxdDRNTkJGdFNuSi11WEdiNjh4QWxWbEwzOF9fZXliazd0RXh2Zw?oc=5>

### Does Costco's Special Dividend Offer Enough Reason to Buy the Stock?
- Summary: Costco announced a special dividend, potentially boosting shareholder value and attracting investors.
- Date: 2026-11-13 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxQbUJYejU2QzBORVFWTC1ISnJJRzA3V0RjaFZGRE1oMVhZSi1FQzk3c2VrdENxUjIxNEg3MWdhb09wS3N6ZmtkWDhKYXE0XzVIT0xFYk5NejNnVjVBWXhlTzR5RFFDaGFMMkY4cnlUOWdrTGVqN3VXQ0lGSGdYWUdROEFMUE1yOUh6d3dBRnhxaTVmUGJ0UXpKeXV6RDdtODVjNmc?oc=5>

### Should You Buy Costco Stock for Its Special Dividend?
- Summary: Special dividend could attract investors to Costco stock.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxNNVJxZU9tOXdjNlVWZjN2dHhhaWh3elZHdU1XMk5KeWNDMVhtSFFiTlZ1a1dfUmdOOHVpeEJyZDNOZnpLVHp2Vm9namtNVFpyUzhkUnJmZ1NUNTYwUVliOWFTbmdJdXFCeHc3UzVSMnBSUGZDaUFyeXUtaG45MkNVakx2OWlWTVJpZ1lrcER1M0NLVEpTU1hVSU92SjNlSjg?oc=5>

### Costco Wholesale Corporation (COST) Stock Forecasts
- Summary: Analysts forecast Costco stock performance.
- Date: 2026-11-17 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxPdFVta3FnbkJvNlY3MHVjTElRRG83RWpqTDU0dmpyMTZZUUV5eDRsNHotSmNWTVRucm1KUlJGWnBWWS1FcWxQTHZiVi1BQ1B0b0hjQzFIVWN0OXdoZ0htZnNqbzJXX0o5dnhYRGw3WnhVQmZENkw4VDNoSUJXekhlTjE1ZzVuRlpDdURnbEZRTQ?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **COST** | **53.65** | **13.74** | **33.89** | **11.10** | **491,908,988,928.00 USD** | **22.36** |
| WMT | 46.20 | 10.31 | 24.55 | 5.90 | 1,014,814,212,096.00 USD | 24.91 |
| TGT | 16.65 | 4.06 | 10.04 | 5.30 | 72,473,960,448.00 USD | 86.57 |
| BJ | 24.49 | 6.41 | 14.49 | 15.70 | 14,075,245,568.00 USD | 20.26 |

Peers fetched as_of: 2026-11-17; COST reuses existing data (market data as_of: 2026-11-17); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-09-24
- Next expected earnings: 2026-12-10 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-17

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-K
- Filing date: 2026-10-07
- Revenue (latest available single quarter): 69,597,000,000.00 USD; period 2025-11-24/2026-02-15; fiscal year/reporting period 2026/Q2
- Net income (latest available single quarter): 2,192,000,000.00 USD; period 2026-02-16/2026-05-10; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/909832/000090983226000093/cost-20260830.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMirwFBVV95cUxOdlVURFpSc0dkWHVKY3M3d0c0WDZWNTh5RHBxbkJ2MDV1Nmh0RGdQV1hNbWtvU2NkMzRobmQ0SlNPbjNMTWlFbjlsVEZKbEhFdXNzRlprcWRJeG9ERDJFcjNFSWJSd3hEdXhsZjdkV28xdnJTSGFVMEt0eWJPRjFtWjdNbG00cXpHVWVpMjVXWGdfbnczSm1hUTBKSG5ZcGkxWWNYSWNDWF9yZnpsYUV3?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxQNU1XWlFxZWMyYTg0NHd3by15cjhlX3FBQXhnaFpiT2JXRXR2VVRLQmZsbUJVN2Fmd3lJMTdpRUhQNUpNcC1uLUUtYUlnS00yQVZhSVFDWHgtbm9oajE4ZlktcHFvQWZJRVlZZ1hNYmxsQmZaMHFOdHVxZUhIVkN1RmhkY05KaVRsb0lNdFdCVUNkSWI4QmNn?oc=5
- https://news.google.com/rss/articles/CBMie0FVX3lxTE1mem1WV09KMHJEbGxFR0RXanhfVUhVV092TVU2RDRPUUp3Ym93enJSR3htWWV6V1pPb19QRnB5WVlOR0dvVkM0OGQ3SU1ZYk54VWlzUFktdDczWnFDc21MaDJqcFp1b1A3Z001d1BzYzI2N2tXRlZLM2QyTdIBgAFBVV95cUxOQmx1T1pDSkJ5UV9fUTROQUNwTU42VTZPVWRvM3ZORXNlNEV1V1ZiT1MwYVlRQU54cDRoWVhlT1BqcW5hcjZoZnZOMGhvSzRVZlZFY0pwek40TmFXQ1pTT0w1cHFYRFJ0ZzhWUjFnck44RGVtdGx1WXVFZzQtNXgwOQ?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxOVGE2THhHUElqcTU3WTRTZ1dRZlY0dFJlU3RlV0E5YzRpOTRKTGd5N3dJaEoxamZuU1NPemh6SE16dGhkbVMzOE9ESnhqNWtCc3E5eTR5Ty1LWjdkWXpTdnBic1dNbFdRN1BKV1gtRWt4VnJLMDQxVzRTUTBCRU9DVENqR1E4UTZ3M3JaQWI4ajEyM0s0bGdDcFd4V0xtNE43QWw1SmhNenlkWHU1ZG1lT3RZQW5ia2lPaU5EQnJHTTE?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxNZFVtVFdZRXg5WjFZYmw4Ym5QT3lTcnVQLWJabUVjYjVXZkotN2hsVlNoejFOTEF6c0Y4VzFka0NmVFB0NjBsODM5ZTkwdUZjT3lOQVJKM0E3aWpTdUoyQnp4VEExNHhGa3VBT1VBaVRybG1qbkRkV2o0ampNOEVfYmtqRW1KUjdIeDZTNjQ1THV6ZzQ3TXhZVjYyOVJJV0puYVFXeFU4RFVpa19maVE?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxNWnB6WnliS3RMSzhFdW9BM3AyVV92b2IzSHZ4ZUFjY2FWSjQyQ2dNN1pKcG5NbTdhMDlueExkM0x4WENEVVBobUZLMWtCR2tHMmZuX29ISnRVM194NEkzMXV2bFNxc1VUUW5CcVBueXRGNlVQOVVxOGZ0WEstaHZSMXZGTHl0XzI1anVNOHVoRFhVY1ZoSi1rV3pMRXlFcTI4Sy1pWjhtNmJ4aE1YMGc?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxOZllkN082dEhId0dnX3hLazBDT0FKN2poT3NxLVpvbkhkNDl5NjY3ei1YUUpPRmNzOWFJWHhpYUtGcDhFN0w5Vml0VzVxV0hRUk9Wekt2MlNpc05oZmRacVFycWlaV196LXFLUWVjd2NfYWNxTW52VmpBRFJSRzdBLUswX3c4OFdnYzFLZkVPVmI0cHZKOTNkeW9WSXpDZw?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxOZmVoRVEzaVZmR2dJUXBIbmxVZzVBLUd3TW9md1VqZ1AxTWdTcm4xMnVOQTU2dl9yT09mMkcyaGJRbWpId3czN1ppbU51bjVHRGhrU1ZlQnpvb0xCelRSTEdUREoyYlBUUDlMdUxhcFFZSjdzU2VGRjBFeC1kWTlyblZMR1Blc1hhVDVxQ3ZGcVJTd2pyV1BkWko0QjUzcjdqdlE?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNN1hkY2p3V3FFb0NZeXpsZjJPV3l0NVZ4X0V1X0ZMZFlTWTN1OHlPVzgybVZPMzVkU0l3aTFoQUg5VDA0VDNQNnc5bHFETUZiMGhmRnkwb0JBeWlMQnR2d2NGZFVmZ1RUVUJiU1BtRTBfNkZVdGpPdEM0Y2kwdXk3TU9tc2pBNHpaSEZ3NHBiUTJLdlRPbXhQbWd2SQ?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxOeElIQXVxNEtIWWJkMXdiQ0hfOUtOelZ5ZGhCV3MzUldkTXNRRlFwa0hYTE5xMTVZTENtRmI0U3dvSGtrcjE4ZmdYRU5sMlB1bGRia3FaWlpmSnh1V1RkeW04TC04ejdxQ2hRMktuM0xmRVphNi1rUWk4VFo4VExyaFhMTzliSzhxRFpWa2VELTVwQXFiS2VwSGt6MHdzQQ?oc=5
- https://news.google.com/rss/articles/CBMizgFBVV95cUxQem9tZXVZeGpsMVdSQXp5dUFaeFplWG1WR25aaVFjSGxRSnJTMENmTWxaQ3p1OEhZeGpHSng0LW1LaTh3cWp2cjJsTzJKN2UxU3J6enBvRmVES21iaFRzbk9Tam9TMnY0eGphOHpJNl81dDVEYlIzYnEtODBRR1AxUlZDOXJhbjFjaWlJTXVGQjZfWG5CaWEyeFVJMnVFdm5oZTlJS2hXeUozVlE2TzZOejdTS3J3MjlodXV0ZkJJaElSQVJLbDR5N3lIUmc5dw?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxQMUpXaW56UjBNc0VnVkd3Q2E4aE1xMjQyTnNLZjlmYW1Dak5yS0NfY0VfaGhEWnRWazJxdV82ZlZPaXJqaGNsaWM4Nnk2emVocVVEQUVyTFJsc2NlRF90czBLdV9WdDhVQ2JXYzJjOHpSVFpDaHBiNURzX0sxakNoMjVhelZRS2pDTXNjYkxpajZseTA?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxPYU03ekRHaEc0TWl0STFiVExmZnBzd0xRTXdpa2ctc05XeS1qRWlvb3J1NFdaMHVFc2lsLVNkeG1meGZSZTN6MUlLeTRNZFI3c19JeEhWbTlFdFV3MkxJWkt3a05iWVp3ZnZYanZXSTNWV21pLVZ6NTFrT3ZFYmZSOEVFN2pONzdlNHdSOHFYQTJJVzkxeWZQYmZjSlpJMmc?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNVk1SbzRkY0hkTVlRbk9LWHduY2lLZnJjeUIxU3NvbWVNLWhVZFFJMjNJYUNlSF92N2p5YTY5RFFocmVYSGdKakNybjRTeVZZd250OGg0aWNVVmR6UzFhVHpXRnhVREVmbHJ0RXBVZU5HUVRWelYyRUFxOVhHeHN1QXAxUGxYRVZJSW93OEhjSnJ0V3BGMm9OeURlbk8?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxNa3JZUXJRekpXSnlWaGt4cmZWTnQwN0FmRjNtRHFzb1VLZnRtZmtuV1hpV0JKamc1OUpIN3VSc3QxYWVZRndEMExETzlycE9wQlVILXdSc1RyTjhaSVVsOWJoLXd1TVV2a0d6Y2RuYXN1eXJGSld4LWpQVUhkUGNrc1ZiMC0tRVNVbi16NW9NTVZ0M25nNVE?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxNNDhKRGlWaVlleFYxdl9yZTJBTGc5Z0plWEp0Zy1sOTdiNGNneDd6bWkxOEtWRUtBN250aU1Ta2FZcEg3WFRNMXl5b1ZDN1NTLU03R3ZSckgxb1BFelRFUGtLMlFrVThxeFRFNUQxdDRNTkJGdFNuSi11WEdiNjh4QWxWbEwzOF9fZXliazd0RXh2Zw?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxQbUJYejU2QzBORVFWTC1ISnJJRzA3V0RjaFZGRE1oMVhZSi1FQzk3c2VrdENxUjIxNEg3MWdhb09wS3N6ZmtkWDhKYXE0XzVIT0xFYk5NejNnVjVBWXhlTzR5RFFDaGFMMkY4cnlUOWdrTGVqN3VXQ0lGSGdYWUdROEFMUE1yOUh6d3dBRnhxaTVmUGJ0UXpKeXV6RDdtODVjNmc?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxNNVJxZU9tOXdjNlVWZjN2dHhhaWh3elZHdU1XMk5KeWNDMVhtSFFiTlZ1a1dfUmdOOHVpeEJyZDNOZnpLVHp2Vm9namtNVFpyUzhkUnJmZ1NUNTYwUVliOWFTbmdJdXFCeHc3UzVSMnBSUGZDaUFyeXUtaG45MkNVakx2OWlWTVJpZ1lrcER1M0NLVEpTU1hVSU92SjNlSjg?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxPdFVta3FnbkJvNlY3MHVjTElRRG83RWpqTDU0dmpyMTZZUUV5eDRsNHotSmNWTVRucm1KUlJGWnBWWS1FcWxQTHZiVi1BQ1B0b0hjQzFIVWN0OXdoZ0htZnNqbzJXX0o5dnhYRGw3WnhVQmZENkw4VDNoSUJXekhlTjE1ZzVuRlpDdURnbEZRTQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
