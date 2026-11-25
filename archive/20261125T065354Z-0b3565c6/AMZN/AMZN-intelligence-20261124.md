# AMZN Intelligence Report

- ticker: **AMZN**
- Report as_of: **2026-11-24**
- Market data as_of: **2026-11-24**
- Quant sources: https://finance.yahoo.com/quote/AMZN/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AMZN/key-statistics/
- AI analysis snapshot as_of: **2026-11-24**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-25T07:01:38.510285+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 12, 'ai': 11, 'unknown': 0, 'irrelevant': 2})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **3** exact headline/source/date matches; prior report **20261124T081701Z-6c335e3d/AMZN** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 14 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 24.0%; oldest publication 2026-11-19

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 252.2900 |
| Return 1D (%) | -1.2138 |
| Return 1W (%) | -2.1715 |
| Return 1M (%) | 1.7298 |
| Return YTD (%) | 9.3016 |
| Return 1Y (%) | 11.4946 |
| Annualized volatility (%) | 34.3898 |
| Beta vs SPY | 1.2389 |
| Max drawdown (%) | -19.6419 |
| Sharpe (rf=0) | 0.4858 |
| Downside deviation (rf=0, %) | 21.2254 |
| Sortino (rf=0) | 0.7871 |
| Historical VaR 95% (1D, %) | 3.2202 |
| Historical ES 95% (1D, %) | 4.1300 |
| Correlation vs SPY | 0.5387 |
| Tracking error vs SPY (%) | 29.1919 |
| P/E (trailing) | 20.40 |
| P/B | 4.45 |
| EV/EBITDA | 15.89 |
| Revenue growth (%) | 12.10 |
| Forward P/E (estimate) | 23.09 |
| Gross margin (%) | 51.37 |
| Operating margin (%) | 13.09 |
| Return on equity (%) | 27.42 |
| Free cash flow yield (%) | -1.27 |
| MA50 | 255.1464 |
| Close vs MA50 (%) | -1.1195 |
| MA200 | 245.5938 |
| Close vs MA200 (%) | 2.7266 |
| RSI (14, Wilder) | 46.5132 |
| MACD (12,26) | 0.0620 |
| MACD signal (9) | 1.3779 |
| MACD histogram | -1.3159 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AMZN': 289, 'SPY': 289}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 252.2900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.2138 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -2.1715 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 1.7298 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 9.3016 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 11.4946 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 34.3898 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 21.2254 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.7871 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.2202 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.1300 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5387 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 29.1919 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.2389 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -19.6419 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.4858 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 23.0906 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 51.3740 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 13.0870 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 27.4160 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: -1.2731 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 20.3953 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 46.5132 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -1.3159 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -1.1195 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 2.7266 -> Slightly above the moving-average trend level.

## TAILWINDS

### Amazon Stock Pops: What's Going On? - Amazon.com (NASDAQ:AMZN)
- Summary: Amazon Stock Pops: What's Going On? - Amazon.com (NASDAQ:AMZN)
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxPZzNaYkdqazhvS254MUt3MjVTaFcxNzV6Q2NGYlZ2eHdaUm9XS3FyTkR5WkRHX3A1SjBEQ1QtY0djSC1iTUdpRkl2bUZudFRwM2ZUcDV1eHRhRVJObXNpRFBaYjMwZDdnNWhmdkVwZkpCa0xCRWtMNkZpX2xQLXg1eENFUjV6YXROaEQ2SlhJMk9KSVZhUGJKaw?oc=5>

### Amazon stock declines while higher inflation and Fed signals boost Treasury yields
- Summary: Amazon stock declines while higher inflation and Fed signals boost Treasury yields
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihAFBVV95cUxQdWwxTW5IUFNRc01yMjBHeldQeDhUeUJjUC1idHF0bVJmWE04UkJkbWJyT1hiZmppWUd1NGpua1kzZl85bXRIMTFOZVh3VEZaMWl5cktCS1M3VEF3UXpFbjI5b21TWjMyOVZoZUlfQkVSU0tDTGlJNmVHOXRmLXA2clN4eXE?oc=5>

### Amazon Makes AI Chip Move; Stock Climbs Alongside Nvidia Relief Rally
- Summary: Amazon Makes AI Chip Move; Stock Climbs Alongside Nvidia Relief Rally
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihAFBVV95cUxONGNWcWFkazVXMUhqYkdVOXN3UUJFbVppRWw4RUZaVFA1ci1TLWlXUk5xOG1pUWJ0X1VKZEN4SVRpYUpzbVlsSnVhVW1fM3dDdGp3NHFiMXVraHVvUXZBOUExZy0yVWdscE5wZWNUd256d1U0bzh6b0Uwell0NXRqekVVOEo?oc=5>

### Amazon.com (NASDAQ:AMZN) Stock Jumps 3.5% After Analyst Upgrade
- Summary: Amazon.com (NASDAQ:AMZN) Stock Jumps 3.5% After Analyst Upgrade
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxQdEFnQ1liWFJrVDBPTkV4Umt0SEw3V3FvWDZoeTRZczNlYTlKLXBZM2dNVThEcXRkUm9KV0ZCTUFQTVJFWnhqcVk2NWQ5V2ZsbzZBUldEbTg0b0o2VDlCRklDNUlFRHk4X2RwRGZOa1ZOcnpfZmpONEtoU3ViZWVGTTh6RGJzSENlNW9QOXptcmEwQ3NmdmxydGtEdXp2Z3RUYlRJLWI2a3BzUmg0Z01xY3I4akVmWElWbWc?oc=5>

### Amazon (AMZN) and Big Tech Are Spending Heavily on AI – Here’s Why Investors Aren’t Panicking
- Summary: Amazon’s significant AI investment is viewed positively, with investors remaining calm.
- Date: 2026-11-20 | Impact: medium | Horizon: medium | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxOMXdBQUpoQ2EwOFVBdW5HQWtaTXdVVTJqbjJZczdqRFZJdDJ3bHMzQmVQU2RVTF9ISmNxcFRXV2VJeWdDNURIZ0duc2pTX0lVZmE4WTREb3NaQmIyM1JfMzBqNFpENlBjTEhoVlZPc3I1bHdkVFowWEkyWXFib1hDbWF6bUJKS2pobVg1OW5pZFZqUElibGNJVQ?oc=5>

### Amazon.com Inc Stock (AMZN) Moved Up by 3.71% on Nov 23: A Full Analysis
- Summary: Amazon shares rose 3.71% on Nov 23, indicating a positive market reaction.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxOYUI4dW4yVFZLUmNocWJ3SmJ4MFhaTGRrcFVqd2ZUak1sdDYwSlR6YkJjUHkya1FaQzlmQkduYVRDYkhKa0w1ZHBvYkFSZXlLOGNlVmxLcjdMclgxaUlZTi11VmJwYUpuUXVuWU13WVE3UFhPRjgyek1MTkNUckhHMkd6cVVfNGoxc3Vn?oc=5>

### Amazon Is Reportedly Paying $7.5 Billion for Decart’s AI Chip Software
- Summary: Amazon acquires Decart’s AI chip software for $7.5B, expanding its AI capabilities.
- Date: 2026-11-24 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxQLXVIRDFZWk96UXRyLWRvTUJxU2ZZMUdvSExoSk9keXF3ZWx4RTdtSDZPMFJjWTUySjZqUC1SZ0llWXNaVFJuMDVKNlNvOFlsRXRiZXM3N2t3RXM0UnZ5RnlPU3N6VnJYY2dRd1djVXhsYVAyRlg0TVJaczBIMkxYdmlJaE1pcnR3MTZ2VUFrTjRxTWE2RUdzdEhVeXlFZ2FBSmoxOVdiTld1ZkF0NDdxaVFR?oc=5>

## HEADWINDS

### Amazon.com (NASDAQ:AMZN) Stock Price Down 1.2% - What's Next?
- Summary: Amazon.com (NASDAQ:AMZN) Stock Price Down 1.2% - What's Next?
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxNVGpZZGtHTnFvVjdEUjNmbHJ2YnlPUTdxcGFtRUlJb2ZQRjZBb2ZKWEoycXNKNGFlaFNxckd5LTlyeUZwWjdPcVVVZXJWN3NwMXFhTHJpYXlnWWdzTEI3eGVLeDFnOXMxZUFuandKMUp2Z3FoYTRvX2tBTTVJdnRiYmlYeW9LR0Vzb2RrcnZMcXVkM0t2QXEyY1U5SndPUUJ5T0YxbWxrWmVFbXJvV25GTU9n?oc=5>

### Amazon Stock (AMZN) Falls 3.9% After Anthropic IPO Debut (Nov 19)
- Summary: Amazon Stock (AMZN) Falls 3.9% After Anthropic IPO Debut (Nov 19)
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMigAFBVV95cUxOejFaODVKV0NVTXhtWFRJTjNhVmh5SFhiRl85T3VIYm1hUWZJeUF4RENfNFlQc2NLN2NBUFROSk9aRE8wN3dsdUNrTFJHR0h2NDZGTTczNld3NVRsRlBYY1lldHYxckZnODF5TTZHRm12Qk5RNThEVWxhZWVFYlpNbQ?oc=5>

### Stock Market Today, Nov. 20: Amazon Shares Slide on AI and Mega-Cap Tech Sell-Off
- Summary: Amazon shares fell amid AI concerns and a broader tech sell-off.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxOZ3Q4VjNVRWVxOW90cDAtdDVDc1V0eXZGZ3gxbHhCQlhGUC1aTFNqTmtrU055TklQUjZreGR5NkRHU1FvblFOajBsWnVncTVhVnA3NTEzaWlQUFh0UjZMR0FDa2pINmlZSnItYmtHMDJ4TnhRclBFbnJzVXFvalg2UEJhQlZkTmJMQnc1dkJ2MVF5dTBFM3RYY3VBanF1blJOYzUxbGF2cHhvY2FBV3hXcURYb0VWamxSZVRxN3BWSGZoQWtqMEtaaWJ6SFFXNjBjbmtvOVFB?oc=5>

## CATALYSTS

### Amazon (AMZN) Stock Trades Below Fair Value As Its 82% Run Continues
- Summary: Amazon (AMZN) Stock Trades Below Fair Value As Its 82% Run Continues
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxQUUtfMDhmNWV5dFk3RkdyTDhlTi1NZ2U1QmVMXzBhWmZwWHlGWktLSk1kbUFJUTVEUjYybDFxT2NJMjFRa2lySmw2bkVSdXFtcnpxaEFsbWF1MEhPX3FVLUxFSXAyTmM4LXJwVUVSS29KTWtxejlYYjZVejNGTW9FbXpmUFBzRE53Yi11TnBUVnAyYTBLNllfQ2E2OA?oc=5>

### Amazon Leo launches 36 satellites aboard Ariane 6 rocket (AMZN:NASDAQ)
- Summary: Amazon Leo launches 36 satellites aboard Ariane 6 rocket (AMZN:NASDAQ)
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxNLTd2Tk05V0RoMjVLOFROaFNwUDFiMXN0RTZCSGlocGJQb1hTb09pam1wckZwT0RaQmpxSVFrSUNVNmJOUDdRSHRmUUc5N0FTYXRxWDFOeExNdmk1a3VPQWhSNFJ0ajBtUDZ4SzJhZ05ZS25hdGRHbzBCYklCTTNPWUZsLTRUVUNkVWRGRDNzNkVMXzJSSkRjZ3N3?oc=5>

### Amazon nearing $7.5B deal to buy AI start-up Decart: FT
- Summary: Amazon nearing $7.5B deal to buy AI start-up Decart: FT
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxPeWc2UVNPUkd5Zkphdnk2U0VVcnpReDhobWoyNEtSemI4cUhlMDBpZGhiTm51TWpORk1YQ3dBS1g3YzN1TlN6aFQ1azRPZ19wYWhEQnpkSy1rSGhocjk2V3MwYXN6cjVTQm0za2NiTGNxWUJXUDhJNUtfTHNyZkVRRGVwbGE1dDBQc1E?oc=5>

### Amazon (AMZN) Stock Trades Below Fair Value With AI Cash Flow In Focus
- Summary: Amazon (AMZN) Stock Trades Below Fair Value With AI Cash Flow In Focus
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxNcWlDUlo1X0dLWE1CbGY1dUg4cXRPaDgtRFRHN1JWRGxOTktkbzFRV1VTWnQ1VmMzUDUwTWloa2l5RVdtU0FuZC1kbHR1X2N4bEdHMHg4TEZ2bGV6LTM0d2FvVFg4emU5RjlJbHRXOXhReFBUbEZQREZfeHNFclBlcFNnQzlaLW13czBwbUVSakJrUG14eG9OUS1lY2lFMFBXOGZTZzdNZHFVXy1xQWVidEM5Rm5oYndMVnB3YTFIZkJxdlXSAcgBQVVfeXFMTkQzTnB5bEJNOHNlbjJVOFpVbFVzQXdQb0lxV19wQWp4OE5SU3hSQnFmMWM0dmZvU1hHeWh4cWZ6a1N6WU1EbXFHNW9LOVlXZmFEaDB3M2F3Y3ZrN0dKcklScDBWSEZxUWlmR2xfekdGbEQyN1pVNEdtMkhPOFd2UkZHVHBnalVhZkJublJoQkdueWd0LVMxWFhmWm9NUDJIRjVVUHRZYjJIRlJpUWFUU2NmeGE1bnE3VWJxWHl2cGtOa1JVQ2tQbkY?oc=5>

### Amazon Stock Rises 4% After Announcing Acquisition of AI Startup Decart AI
- Summary: Amazon Stock Rises 4% After Announcing Acquisition of AI Startup Decart AI
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxOeGZMRDlrbE1hb21mc28zX0JxOFNacFNmWVNYZzJ3cnVOeWd0TTdMNlJ0RGNxT1FRSkdvNEdqSi1fN2NueW9yeEdGaUxmNVNyd052SWZoSTl6QTA4WmNIWDQ5eWVDUWl4TW1sYU1PRHV0MU1iNFBJY05DSWNzdTNwbmRaZ0xiR2xpUE8zNnd5R2VNaWpTTFlucWVfR1dYcm1zZUU3WnhKTFI5V2M?oc=5>

### Amazon (NASDAQ:AMZN) Takes Aim at Nvidia With Reported $7.5 Billion AI Technology Deal
- Summary: Amazon (NASDAQ:AMZN) Takes Aim at Nvidia With Reported $7.5 Billion AI Technology Deal
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMib0FVX3lxTE1zdE5xTF90UGhzTWsyQ05ybnVzaElJWW96MmF2QlYzZ01VUWV3MFdac0NsNUx1aEV1UUNCQ0tTc2NHamVoUnQtTVh2U1gzYVNjbXhZOFpxakZycDNkYzFlOHFVWl92Rlg5NHRpa0o2WQ?oc=5>

### At $260 a share, Amazon (AMZN) CFO Brian T. Olsavsky sold 6,172 shares under a trading plan.
- Summary: CFO Brian Olsavsky sold 6,172 shares, a routine insider transaction.
- Date: 2026-11-24 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxPcTA3bGtvUVR5ajVwRVJMSFBqbTF4V0lzeFMxWl9KMU1Mb2szbVNuUWI3elZlY0pkZE44aVp1YWZ1TXV5SFdqZ2VHMG4yR1Zoa05qd2YxMHpyQ0xjRDlEcDRWRjc4UkhLeHh3d3hHRW1WYXJXV2JqNHRZbkZ4Vld5ZlNheEhldzEwcVp2X2E5UzNFc3lzQmF0eDlUaTlnWlJuQTRCZ3J3UUYwZ3JN?oc=5>

### After converting stock units into 18,176 shares, Amazon (AMZN) executive Matthew S. Garman sold 14,541 shares.
- Summary: Executive Matthew Garman sold 14,541 shares after converting units, a standard insider sale.
- Date: 2026-11-24 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxQSjJnV0lQcXdpMHFaNmZsdHhZVXdLM19xb3Y5ZF9TaWVmc0JQQ01yMW5nMWFhSTlWVEpwV29BeUdnNXhxRUVTQm1BdU9XQmJITktzbVBKVlhmaTRTSWFuZnB4bEIyUk41YTZ3VkJhdHkxZFYwUXFEXzBNWklXSjBnV1ZrdWE4ckRZSFdOZFhNWm5FVXNneFZuSHoyTkJyQ1FSYi10eG9LVlhaUXR4?oc=5>

### After converting 50,000 stock units, Amazon (AMZN) CEO Andrew Jassy sold shares in nine trades.
- Summary: CEO Andrew Jassy sold shares after converting stock units.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxQWjEzdDFnSGFrblowa1hZRmtXN1I0RGRyNUVOSUlKN3QtOGRnSnBDekY5NlI4SlZBVzdGNUZLdW5HeGxYckc5c2Q5RktTUjVkcy1HV2VaZmlLUnRGTTZIeU9VMHJpNm1NcUhrM2JGVW5kVU5xMWNWdk1PT2NPTkxOVTlxTDJxcDJxc0NTbVhyNEQ5d1BvZHZvUHBldDJtODZUb0tPUnFhZ0ZVWHBW?oc=5>

### After converting stock awards, Amazon (AMZN) SVP David Zapolsky sold 15,430 shares.
- Summary: Amazon SVP David Zapolsky sold 15,430 shares after converting stock awards.
- Date: 2026-11-24 | Impact: low | Horizon: short | Confidence: 1
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxPUTN5d2pob1FUeWI1YWlOTUI5WHZ1Q2ZoYno2Mm1GalRJcWNpVFdJazNzWVBmRFpiMmlia2tKZmV1ejY4UnFfMW9Vb25xMzZDeTN4WVc4aVNTLWJVWV9NTC1saWg0U3BRQ2VXb05OT2xCRVNmZmlod1BFY3VBcnlGb25FeUpTUXdNMTVEd3ljelppNVF1eW9yaWhnTUxzbjJlcHd2RUdhNGhBcVpL?oc=5>

### Three stock awards gave Douglas Herrington 15,905 Amazon (AMZN) shares. He later sold 6,362 shares.
- Summary: Douglas Herrington received 15,905 shares and sold 6,362 shares.
- Date: 2026-11-24 | Impact: low | Horizon: short | Confidence: 1
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxOSHJyU2VpUzZjYVBDR3pIa3c2cVh0Y1JlQjdockc5UE50Ni1GSFRDUHZ5bk5yNEEyUWRMZ2VuTXdtY19SQ2VPT3g2dG5jMDV1YW1ScHYxaFFSY0JvVkxaMndSb0FIeTFFcXBLZ3BrMVhyTGR4d2Utbl9oNk5pbElaV2puaTV0QXFXU240eC1WOUNPR1ctdWJCQXFLeXlQZDdRVC1Lb0NBeE5XSnkz?oc=5>

### Amazon (AMZN) VP Shelley Reynolds sold 2,343 shares in 10 trades under a preset plan.
- Summary: Amazon VP Shelley Reynolds sold 2,343 shares in 10 trades.
- Date: 2026-11-24 | Impact: low | Horizon: short | Confidence: 1
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxOZWZ2SllZMFliVDdiTWdocnJsd1pjM2NKdFF2aXV1d2tGelF3ZFV3WHZjSDFmdFlXc2JZRmp6WmwzMVkzbUlHZlIwTzFRU2gyUG5fUmFrWnZLa3BRU2FaeXFETngycm1sWW82TUdsckk3RkdaODVhZGVSNWkwNVY2eVNSNGE0MU4zWGFtaXV3WGdzTXNZUUF6OHJqWmNmVWp0N3dhaHBaUHk2d1Nn?oc=5>

## RISKS

### FAA probes Amazon delivery drone crash in Michigan near Detroit (AMZN:NASDAQ)
- Summary: FAA investigating Amazon drone crash.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxOeFVtMWpScDBVZnhzMnVXQWNmcmlWRGtSSUVIeWhvRXloUGVSdE1vSE9lTUNlbVBJR1JtYjhPaVRSeHNOV093NDg0aF9vQ3lPTTdFYmpidm5zbURJNmtFNUJFN1ZISllDeFFBemQ3ZXhDQUhsTFdNYXo5aE9ONTVOVV8zT1M3OHhNZXd5Mm1qRG8xajNPbHNjRGRGVHNmbnFnX0F3?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AMZN** | **20.40** | **4.45** | **15.89** | **12.10** | **2,728,046,362,624.00 USD** | **11.49** |
| WMT | 47.94 | 10.70 | 23.08 | 5.20 | 1,052,933,423,104.00 USD | 28.22 |
| MSFT | 25.89 | 7.83 | 18.25 | 18.80 | 3,684,357,898,240.00 USD | 5.54 |
| GOOGL | 14.57 | 5.20 | 17.97 | 24.70 | 3,430,640,517,120.00 USD | -12.18 |

Peers fetched as_of: 2026-11-24; AMZN reuses existing data (market data as_of: 2026-11-24); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-29
- Next expected earnings: 2027-02-04 (yfinance; expected dates may change)

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
- Filing date: 2026-10-30
- Revenue (latest available single quarter): 201,944,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 20,685,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMimAFBVV95cUxPZzNaYkdqazhvS254MUt3MjVTaFcxNzV6Q2NGYlZ2eHdaUm9XS3FyTkR5WkRHX3A1SjBEQ1QtY0djSC1iTUdpRkl2bUZudFRwM2ZUcDV1eHRhRVJObXNpRFBaYjMwZDdnNWhmdkVwZkpCa0xCRWtMNkZpX2xQLXg1eENFUjV6YXROaEQ2SlhJMk9KSVZhUGJKaw?oc=5
- https://news.google.com/rss/articles/CBMihAFBVV95cUxQdWwxTW5IUFNRc01yMjBHeldQeDhUeUJjUC1idHF0bVJmWE04UkJkbWJyT1hiZmppWUd1NGpua1kzZl85bXRIMTFOZVh3VEZaMWl5cktCS1M3VEF3UXpFbjI5b21TWjMyOVZoZUlfQkVSU0tDTGlJNmVHOXRmLXA2clN4eXE?oc=5
- https://news.google.com/rss/articles/CBMihAFBVV95cUxONGNWcWFkazVXMUhqYkdVOXN3UUJFbVppRWw4RUZaVFA1ci1TLWlXUk5xOG1pUWJ0X1VKZEN4SVRpYUpzbVlsSnVhVW1fM3dDdGp3NHFiMXVraHVvUXZBOUExZy0yVWdscE5wZWNUd256d1U0bzh6b0Uwell0NXRqekVVOEo?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxQdEFnQ1liWFJrVDBPTkV4Umt0SEw3V3FvWDZoeTRZczNlYTlKLXBZM2dNVThEcXRkUm9KV0ZCTUFQTVJFWnhqcVk2NWQ5V2ZsbzZBUldEbTg0b0o2VDlCRklDNUlFRHk4X2RwRGZOa1ZOcnpfZmpONEtoU3ViZWVGTTh6RGJzSENlNW9QOXptcmEwQ3NmdmxydGtEdXp2Z3RUYlRJLWI2a3BzUmg0Z01xY3I4akVmWElWbWc?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxOMXdBQUpoQ2EwOFVBdW5HQWtaTXdVVTJqbjJZczdqRFZJdDJ3bHMzQmVQU2RVTF9ISmNxcFRXV2VJeWdDNURIZ0duc2pTX0lVZmE4WTREb3NaQmIyM1JfMzBqNFpENlBjTEhoVlZPc3I1bHdkVFowWEkyWXFib1hDbWF6bUJKS2pobVg1OW5pZFZqUElibGNJVQ?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxOYUI4dW4yVFZLUmNocWJ3SmJ4MFhaTGRrcFVqd2ZUak1sdDYwSlR6YkJjUHkya1FaQzlmQkduYVRDYkhKa0w1ZHBvYkFSZXlLOGNlVmxLcjdMclgxaUlZTi11VmJwYUpuUXVuWU13WVE3UFhPRjgyek1MTkNUckhHMkd6cVVfNGoxc3Vn?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxQLXVIRDFZWk96UXRyLWRvTUJxU2ZZMUdvSExoSk9keXF3ZWx4RTdtSDZPMFJjWTUySjZqUC1SZ0llWXNaVFJuMDVKNlNvOFlsRXRiZXM3N2t3RXM0UnZ5RnlPU3N6VnJYY2dRd1djVXhsYVAyRlg0TVJaczBIMkxYdmlJaE1pcnR3MTZ2VUFrTjRxTWE2RUdzdEhVeXlFZ2FBSmoxOVdiTld1ZkF0NDdxaVFR?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxNVGpZZGtHTnFvVjdEUjNmbHJ2YnlPUTdxcGFtRUlJb2ZQRjZBb2ZKWEoycXNKNGFlaFNxckd5LTlyeUZwWjdPcVVVZXJWN3NwMXFhTHJpYXlnWWdzTEI3eGVLeDFnOXMxZUFuandKMUp2Z3FoYTRvX2tBTTVJdnRiYmlYeW9LR0Vzb2RrcnZMcXVkM0t2QXEyY1U5SndPUUJ5T0YxbWxrWmVFbXJvV25GTU9n?oc=5
- https://news.google.com/rss/articles/CBMigAFBVV95cUxOejFaODVKV0NVTXhtWFRJTjNhVmh5SFhiRl85T3VIYm1hUWZJeUF4RENfNFlQc2NLN2NBUFROSk9aRE8wN3dsdUNrTFJHR0h2NDZGTTczNld3NVRsRlBYY1lldHYxckZnODF5TTZHRm12Qk5RNThEVWxhZWVFYlpNbQ?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxOZ3Q4VjNVRWVxOW90cDAtdDVDc1V0eXZGZ3gxbHhCQlhGUC1aTFNqTmtrU055TklQUjZreGR5NkRHU1FvblFOajBsWnVncTVhVnA3NTEzaWlQUFh0UjZMR0FDa2pINmlZSnItYmtHMDJ4TnhRclBFbnJzVXFvalg2UEJhQlZkTmJMQnc1dkJ2MVF5dTBFM3RYY3VBanF1blJOYzUxbGF2cHhvY2FBV3hXcURYb0VWamxSZVRxN3BWSGZoQWtqMEtaaWJ6SFFXNjBjbmtvOVFB?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxQUUtfMDhmNWV5dFk3RkdyTDhlTi1NZ2U1QmVMXzBhWmZwWHlGWktLSk1kbUFJUTVEUjYybDFxT2NJMjFRa2lySmw2bkVSdXFtcnpxaEFsbWF1MEhPX3FVLUxFSXAyTmM4LXJwVUVSS29KTWtxejlYYjZVejNGTW9FbXpmUFBzRE53Yi11TnBUVnAyYTBLNllfQ2E2OA?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxNLTd2Tk05V0RoMjVLOFROaFNwUDFiMXN0RTZCSGlocGJQb1hTb09pam1wckZwT0RaQmpxSVFrSUNVNmJOUDdRSHRmUUc5N0FTYXRxWDFOeExNdmk1a3VPQWhSNFJ0ajBtUDZ4SzJhZ05ZS25hdGRHbzBCYklCTTNPWUZsLTRUVUNkVWRGRDNzNkVMXzJSSkRjZ3N3?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxPeWc2UVNPUkd5Zkphdnk2U0VVcnpReDhobWoyNEtSemI4cUhlMDBpZGhiTm51TWpORk1YQ3dBS1g3YzN1TlN6aFQ1azRPZ19wYWhEQnpkSy1rSGhocjk2V3MwYXN6cjVTQm0za2NiTGNxWUJXUDhJNUtfTHNyZkVRRGVwbGE1dDBQc1E?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxNcWlDUlo1X0dLWE1CbGY1dUg4cXRPaDgtRFRHN1JWRGxOTktkbzFRV1VTWnQ1VmMzUDUwTWloa2l5RVdtU0FuZC1kbHR1X2N4bEdHMHg4TEZ2bGV6LTM0d2FvVFg4emU5RjlJbHRXOXhReFBUbEZQREZfeHNFclBlcFNnQzlaLW13czBwbUVSakJrUG14eG9OUS1lY2lFMFBXOGZTZzdNZHFVXy1xQWVidEM5Rm5oYndMVnB3YTFIZkJxdlXSAcgBQVVfeXFMTkQzTnB5bEJNOHNlbjJVOFpVbFVzQXdQb0lxV19wQWp4OE5SU3hSQnFmMWM0dmZvU1hHeWh4cWZ6a1N6WU1EbXFHNW9LOVlXZmFEaDB3M2F3Y3ZrN0dKcklScDBWSEZxUWlmR2xfekdGbEQyN1pVNEdtMkhPOFd2UkZHVHBnalVhZkJublJoQkdueWd0LVMxWFhmWm9NUDJIRjVVUHRZYjJIRlJpUWFUU2NmeGE1bnE3VWJxWHl2cGtOa1JVQ2tQbkY?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxOeGZMRDlrbE1hb21mc28zX0JxOFNacFNmWVNYZzJ3cnVOeWd0TTdMNlJ0RGNxT1FRSkdvNEdqSi1fN2NueW9yeEdGaUxmNVNyd052SWZoSTl6QTA4WmNIWDQ5eWVDUWl4TW1sYU1PRHV0MU1iNFBJY05DSWNzdTNwbmRaZ0xiR2xpUE8zNnd5R2VNaWpTTFlucWVfR1dYcm1zZUU3WnhKTFI5V2M?oc=5
- https://news.google.com/rss/articles/CBMib0FVX3lxTE1zdE5xTF90UGhzTWsyQ05ybnVzaElJWW96MmF2QlYzZ01VUWV3MFdac0NsNUx1aEV1UUNCQ0tTc2NHamVoUnQtTVh2U1gzYVNjbXhZOFpxakZycDNkYzFlOHFVWl92Rlg5NHRpa0o2WQ?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxPcTA3bGtvUVR5ajVwRVJMSFBqbTF4V0lzeFMxWl9KMU1Mb2szbVNuUWI3elZlY0pkZE44aVp1YWZ1TXV5SFdqZ2VHMG4yR1Zoa05qd2YxMHpyQ0xjRDlEcDRWRjc4UkhLeHh3d3hHRW1WYXJXV2JqNHRZbkZ4Vld5ZlNheEhldzEwcVp2X2E5UzNFc3lzQmF0eDlUaTlnWlJuQTRCZ3J3UUYwZ3JN?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxQSjJnV0lQcXdpMHFaNmZsdHhZVXdLM19xb3Y5ZF9TaWVmc0JQQ01yMW5nMWFhSTlWVEpwV29BeUdnNXhxRUVTQm1BdU9XQmJITktzbVBKVlhmaTRTSWFuZnB4bEIyUk41YTZ3VkJhdHkxZFYwUXFEXzBNWklXSjBnV1ZrdWE4ckRZSFdOZFhNWm5FVXNneFZuSHoyTkJyQ1FSYi10eG9LVlhaUXR4?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxQWjEzdDFnSGFrblowa1hZRmtXN1I0RGRyNUVOSUlKN3QtOGRnSnBDekY5NlI4SlZBVzdGNUZLdW5HeGxYckc5c2Q5RktTUjVkcy1HV2VaZmlLUnRGTTZIeU9VMHJpNm1NcUhrM2JGVW5kVU5xMWNWdk1PT2NPTkxOVTlxTDJxcDJxc0NTbVhyNEQ5d1BvZHZvUHBldDJtODZUb0tPUnFhZ0ZVWHBW?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxPUTN5d2pob1FUeWI1YWlOTUI5WHZ1Q2ZoYno2Mm1GalRJcWNpVFdJazNzWVBmRFpiMmlia2tKZmV1ejY4UnFfMW9Vb25xMzZDeTN4WVc4aVNTLWJVWV9NTC1saWg0U3BRQ2VXb05OT2xCRVNmZmlod1BFY3VBcnlGb25FeUpTUXdNMTVEd3ljelppNVF1eW9yaWhnTUxzbjJlcHd2RUdhNGhBcVpL?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxOSHJyU2VpUzZjYVBDR3pIa3c2cVh0Y1JlQjdockc5UE50Ni1GSFRDUHZ5bk5yNEEyUWRMZ2VuTXdtY19SQ2VPT3g2dG5jMDV1YW1ScHYxaFFSY0JvVkxaMndSb0FIeTFFcXBLZ3BrMVhyTGR4d2Utbl9oNk5pbElaV2puaTV0QXFXU240eC1WOUNPR1ctdWJCQXFLeXlQZDdRVC1Lb0NBeE5XSnkz?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxOZWZ2SllZMFliVDdiTWdocnJsd1pjM2NKdFF2aXV1d2tGelF3ZFV3WHZjSDFmdFlXc2JZRmp6WmwzMVkzbUlHZlIwTzFRU2gyUG5fUmFrWnZLa3BRU2FaeXFETngycm1sWW82TUdsckk3RkdaODVhZGVSNWkwNVY2eVNSNGE0MU4zWGFtaXV3WGdzTXNZUUF6OHJqWmNmVWp0N3dhaHBaUHk2d1Nn?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxOeFVtMWpScDBVZnhzMnVXQWNmcmlWRGtSSUVIeWhvRXloUGVSdE1vSE9lTUNlbVBJR1JtYjhPaVRSeHNOV093NDg0aF9vQ3lPTTdFYmpidm5zbURJNmtFNUJFN1ZISllDeFFBemQ3ZXhDQUhsTFdNYXo5aE9ONTVOVV8zT1M3OHhNZXd5Mm1qRG8xajNPbHNjRGRGVHNmbnFnX0F3?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
