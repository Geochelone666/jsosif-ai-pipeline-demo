# PFE Intelligence Report

- ticker: **PFE**
- Report as_of: **2026-11-07**
- Market data as_of: **2026-11-06**
- Quant sources: https://finance.yahoo.com/quote/PFE/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/PFE/key-statistics/
- AI analysis snapshot as_of: **2026-11-07**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-08T04:28:44.722610+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 11, 'ai': 11, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **13** exact headline/source/date matches; prior report **20261107T043155Z-acc5f41d/PFE** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 10 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 36.0%; oldest publication 2026-11-02

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 29.3900 |
| Return 1D (%) | -0.2037 |
| Return 1W (%) | -2.2965 |
| Return 1M (%) | 8.4332 |
| Return YTD (%) | 25.9367 |
| Return 1Y (%) | 28.4121 |
| Annualized volatility (%) | 21.6777 |
| Beta vs SPY | 0.2729 |
| Max drawdown (%) | -15.7243 |
| Sharpe (rf=0) | 1.2665 |
| Downside deviation (rf=0, %) | 14.0672 |
| Sortino (rf=0) | 1.9517 |
| Historical VaR 95% (1D, %) | 2.1427 |
| Historical ES 95% (1D, %) | 2.6741 |
| Correlation vs SPY | 0.1706 |
| Tracking error vs SPY (%) | 23.5225 |
| P/E (trailing) | 41.99 |
| P/B | 1.88 |
| EV/EBITDA | 8.70 |
| Revenue growth (%) | -0.40 |
| Forward P/E (estimate) | 10.01 |
| Gross margin (%) | 74.90 |
| Operating margin (%) | 33.38 |
| Return on equity (%) | 4.47 |
| Free cash flow yield (%) | 7.76 |
| MA50 | 28.3374 |
| Close vs MA50 (%) | 3.7144 |
| MA200 | 26.0880 |
| Close vs MA200 (%) | 12.6571 |
| RSI (14, Wilder) | 53.5209 |
| MACD (12,26) | 0.4662 |
| MACD signal (9) | 0.5154 |
| MACD histogram | -0.0492 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'PFE': 277, 'SPY': 277}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 29.3900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.2037 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -2.2965 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 8.4332 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 25.9367 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 28.4121 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 21.6777 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 14.0672 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.9517 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.1427 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.6741 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.1706 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 23.5225 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.2729 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -15.7243 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.2665 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 10.0067 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 74.8980 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 33.3840 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 4.4680 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 7.7645 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 41.9857 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 53.5209 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.0492 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 3.7144 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 12.6571 -> Clearly above the moving-average trend level.

## TAILWINDS

### Pfizer hikes full-year outlook on new product growth, taps company veteran as new CFO
- Summary: Pfizer hikes full-year outlook on new product growth, taps company veteran as new CFO
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMickFVX3lxTFBfVElSNTY2SkVSU0NJOUpBalpLNVRMUThqV3ZTb1RwcVhkWndyUHdFTTFJZVNhWXJOWDRXckVMVHVRdU1TLTFGdlNBbmMtM0JDdzlSbEVwanJrUElJT1huRGhsdUJDa3JZUGtxRm8tcjJ0UdIBd0FVX3lxTE5sX2ZVWW5pM29Fc2RUZ2lhLV9uM2RidDdWLXFGRkhhcnhpQ0NfVjBpVFBPbDloZU9HdXVhaF9nZXFrUTR1eVEtLU9uWUhNaXNKSmJmV2J3MUNybnVnVkFPU19QeWZ5QUJPdmFHbExqbFFoNHVFbEF3?oc=5>

### Pfizer Beats Expectations in Q3 and Raises Its Guidance. Is the Stock Due for a Big Rally?
- Summary: Pfizer Beats Expectations in Q3 and Raises Its Guidance. Is the Stock Due for a Big Rally?
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNa0N3bkQxVDFoY0lwZmlQQWlfcFVaX3ByU3lnZE5WbjBRRlg1c1lTaE1TV3c1NlRZdkVaVlhNeXduQkF4OWVkQ3p0amhWd2w2czdib3NmNjdDMHgxMlZteVhUZ0hXTmNGR29LSXltbEltaXlwSW9RbXFsXzdENHVveFE4dU1JZ19ZMjMyOERhSWNIejAyQjM5UVdCN2o?oc=5>

### Pfizer (PFE) Q3 Earnings Rebuild Confidence As New Drugs Gain Ground
- Summary: Pfizer (PFE) Q3 Earnings Rebuild Confidence As New Drugs Gain Ground
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxNdGlHb0hXbkJuS1BabHRTakp0TVN4SURLT1dZeDI5dVlHRXRLQXhWNkViNVRZekNlRFJHdUJlRmNfTnE0RjVlcHNQelJZMGh1cHdvRWlFeXFNMHIyZ2NwYmlVR0RhUEY1aU0xSTBkemh0V3pRaklCMTBMN2tyQ1pZR1Zyb1JPN3I5b2dVUG1FVjY5RWk4Q3c?oc=5>

### Pfizer hikes 2026 outlook: names new CFO (PFE:NYSE)
- Summary: Pfizer hikes 2026 outlook: names new CFO (PFE:NYSE)
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMigwFBVV95cUxNOTF4c0NpeDNqUzhrd3BxcDRpVE5YbnRPRnNaRmNDOHczYml3Z3NBZVo5d1hwMnpxREpGMXlINzctcE9HdFpNa3gxXzJsMTBQSzdmZDlwZzVVQmN3VkpYMWgtbXNpWnJncW9HdHlGZl9YeXZvRGVobWtMR0s1Z29vYXdvNA?oc=5>

### What Is Pfizer (PFE) Signaling With Its Viagra Playbook For Obesity Drugs?
- Summary: Pfizer’s strategy to repurpose its Viagra platform for obesity treatments signals potential new revenue streams.
- Date: 2026-11-06 | Impact: high | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0wFBVV95cUxOTHd6WU5DQTJYRmlGVXNXTFBtWGVGY2pMeDdwRjg2UHhMQkU4cHFGb1JTMkxMM2Q1eXhTZE8xZHVBQ2RqdjNJWE5yU0pRNkdYVU1aUjdWSmF2b2Q1bDV1SWI1b3ZybmhXUm8yaDVuTEdwM0lEZnlyNXFDN0JuZWFoODVZbkRCalhYOEtEZXBYUFBYaTZWMG1fSVpMVl9ESU5kRHpFY0FMRy1xZ283bUl2OG5TUjlaLWR5eHVqdTl4Y1dUNlJrMGVPR2M0eEdkeWtPWWg00gHYAUFVX3lxTE5kcG9NVG1QbVJKN1BvOThzanRPS2l0dHNYdElIak5zempyMW8tbmZRUkZORW5ubm1nVm0zNnhlVlpuV2gzYjh4Qk5MbGpBRlVPNElOcTFGZXFuWklsa25XR0c2akZZb2duNHpJdzdOUkVTdWRqbUVxYWlSSS1VQW1fTWVIcWtBTkxFdldsek1fSXNQLTZXUnNvcmlBQ0xadDItUEcxdndpeVExdzlNYWdCV1NKLUplYjJEZHBLa25JQlFsVFRzX0g4UnRSMXYxWnhwYWdNcEo2TQ?oc=5>

## HEADWINDS

### Pfizer (PFE) Q3 Results Contrast Profit Rebound With Margin Pressure
- Summary: Pfizer (PFE) Q3 Results Contrast Profit Rebound With Margin Pressure
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0wFBVV95cUxPalM1eTlURTd1NWRhQjBGWm4yeU0tREI1WkZiT3dqNXBqQWVES3hkSzBKTlNzZW9WLUJkSWJSN3k5N1lkTlpRZ1NidTJ5Z0ZRSHlHT05tMlpZV09lMHl2elRpMlFPZV9OdDZQanc1ZTZtZjFuTVRuSHVORXFKTXdkWUdrX0lkaGh2UVJzcWJtbWs3NlhaM0dzS3BPSFJJQ3Ewa2hiU1JuUzFiYjlMa2dmZWdwOGNDVklIbVdTVkJhQTdsWTlSb2RKeUZnUjBkLWxqeDFv0gHYAUFVX3lxTFBpTDBuX0pxekZXNlVERG1Wd0lxMTBrMThRSWN1Yy1wUFFUTUhDTTkxSk85b3ZBTHhDbFFwY0tveEl3ZER3QmpSM0dkMzV2UWZ0ekxCWnRfRU5NbE01N2g4TkRUSHA0LUNEcnhKQ0l6bW1fMFlrUTYtVmNyaURHY0Y2eXgtMTg5Q0tqcERyOTFZREE3WEdGUWNVQTh4RTBaWHNuMFNCaGNkM2dmTHRqZkhDN0JDUGNxZXpZbE5rU0V4OHFVamx1U3lpdS1TTGpMRVo5a1o0OHk0Sg?oc=5>

## CATALYSTS

### Pfizer (PFE) Surpasses Q3 Earnings and Revenue Estimates
- Summary: Pfizer (PFE) Surpasses Q3 Earnings and Revenue Estimates
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxOS1dDV1BleUNJdDB3S2F0cDltMmZXc0xnR2E3UWxPOG5ZOTJKT1cwMG9SdVp0UVU1dTZma1FUc1RCZmVEX3FzXy1VN3M0RHoxeFRUVk9vbjR3d05GemR0cTRtVmdBYnEtcDB3LXJKZTd5MHFJUzZFdFJCQ3FXNGlfNFNjRDh4MUdjTVQ3UFA2ZVNCbGFPQk1nVVpkdndyQQ?oc=5>

### Stocks making the biggest moves premarket: Pfizer, Apple, Palantir, Zebra Technologies & more
- Summary: Stocks making the biggest moves premarket: Pfizer, Apple, Palantir, Zebra Technologies & more
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxQQU9uNE1qbFRtYXJFRjhneHc1S2NySmYtc0RWaGU0blFtd2R3aTZZN3V2dHdHRHJHajBTbjV3LVdZZ0RrMjJNd0RUWU1XUl9uWGNQNE52NUxld2Y3dndwZDExU19UcXF1TzBrOFNBaFpNX2tROVQ5UnBoZmdiR3NTZDEwTnRmaFlnR1g5NWhmWlgyakdVMzVKVU4xcUcxZw?oc=5>

### Pfizer (PFE) Reports Q3 Earnings: What Key Metrics Have to Say
- Summary: Pfizer (PFE) Reports Q3 Earnings: What Key Metrics Have to Say
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNY2RxSEZsZk5UWW5Pd2ZVN2VOdENOT004RVZTLWp4allaejhEY3U4ZGpiMC1Ec2YtY3M5U1JRd0ZNVmpMRWxTblo3Vl9qN3JlY2JSX25pR1Z4b3RFV0hlZFRZUEhNR2dXRkVyLTg0dVRJWW51UldrY0g2bHQyQS1ObkUzR0NFV0hLTFhNa2xXZUstWExGVFBFUnJkMA?oc=5>

### Pfizer Q3 preview: Analysts look to obesity pipeline amid diverging growth expectations (PFE:NYSE)
- Summary: Pfizer Q3 preview: Analysts look to obesity pipeline amid diverging growth expectations (PFE:NYSE)
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxOaVA1cGtvS25jb25FMnNKX0VyUGk5UVljVjVpZndtMVFWQ01ZRWtvNVpvSFBRdVpDU0lZend5ZVhLbVk0VlVuNk9vSnRHaDRCOVVIcU9uTWhxWUx4RVRNWkhaWnRHVUFZenk3SHU1Tk5PQmtoWnpCMTV4cVp3MnU0SHlqZTNfLU1IMjlHM3ZGbEdpWG11OEZ2RmtkR1pPNHBPMHBtQVhmTlBTcHRiN2hTUHB0Y0VyVXByTjJZeGZqVE56UQ?oc=5>

### PFIZER ($PFE) Releases Q3 2026 Earnings
- Summary: PFIZER ($PFE) Releases Q3 2026 Earnings
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihAFBVV95cUxNTF9QOEpKdW5XeVk3V1dqSzRvay1ueGtWUnJyU1h0aGJ6ay1lelpLV2NpUDcyOGNKZktXa0taLXdGWngxTEhMSkVKMUhiald1Z0JKaUVPblIwNjA0eUlTV0puZGhuR0hrdUdIZ25CSjQ3bzF4b2c0d0EtbWh2MTNyR2FuV1E?oc=5>

### Pfizer (PFE) Reports Q3 Earnings Tomorrow — Here’s Why Wall Street Remains Split
- Summary: Pfizer (PFE) Reports Q3 Earnings Tomorrow — Here’s Why Wall Street Remains Split
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxPWUN6OU0xMTFqbFZfLVEwYjJrc2lESDJhaHV1ZXA4MEwwd1hzVlRmMEFoUkhoazA1UDk1QTlLRmlSNmVpTkF4RnZZaWVxSFp2aFp6d1NxRDd2amc5cG92MEhVZlFwdV9URWZWS0Rod0FLZXU1ZFlxQkNVQnB5V1ZEbWM0VVh4eUxldXdiaWNYUWpsbndSUHhGaldQTjUxcWJ0TENzSDEyS1Q?oc=5>

### Pfizer (PFE) Stock Looks Attractive for Income Investors
- Summary: Income investors find Pfizer’s stock appealing due to dividend yield and stable earnings.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxPQ2pCSkNOWGtCR09IaXRTWXhrcFN4NGRWNmViaklVUXA4dmFuelE0cjRaR3VNQUVDNXFEa0VscWdmaW5HQ0tXQjJwSlN4YkJldnpWMVg5R1BpYUhMaks3TmRrcVZ6Nk4wVkRRLXpnRUhFazdQOEJhMVFaOXN6R29INFYyZFZQSGk4cDR2c3pzdFVNb0lxMUVrVGJn?oc=5>

### What Could Send Pfizer Stock Soaring?
- Summary: Speculation on factors that could boost Pfizer’s stock price.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxNbmZ2UWVhQnFxckMwRkc4MzZ1c0o0STlHaFowd2ZxZnVhZEtIS09ZLUEwU1Z2d2pSeWxWdXZlNlRxcTFxOXQ0MGg2WXpSVVRCYmdHRzYzR2YxVHhEaEZhbUEyd0tTOUg2VEJxMG1RaWJHaDZvRjBqUjBnMU51QWRMWXMtMGZrQmJfX2NuN2dBMkFfOTFGRU5PVVN5UHRqWkk?oc=5>

### What to expect from Pfizer’s (PFE) Q3 earnings
- Summary: Anticipated Q3 earnings details and guidance for Pfizer.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxPN1Itd1VZUGl5dVBWVmhjS29zWk1FbmdRaFhwWVBPcjRTOWtTbzVHNmFPeThRTGZqaE95VDB4YmNnRHUzTlNUclVtM3V2Tkp1S2lCeVVKX3BhSGhsdVN3Rm1Vd1Nmb1NlQldUb0ZqUXY5RG5uZGZmaUt4TXR5b3RzSGlrVXMyRDlFVms5YmFyTzFvcmNx?oc=5>

### Pfizer (PFE) Names Cecile Guegan Permanent Chief Financial Officer
- Summary: Pfizer appoints new permanent CFO, Cecile Guegan.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxPSFV5UkkzQ1dXSmdiZzlMU1lrZlVwR19kc1puUVJ1N3pPcVduc19iREE0ZU04TFJLNVczclVBb3pKYXhNNGpLdTJZZWN1RmNBblA5WjRPYnh0ZWg1aWlNWHI0b2ZsbktJU1RaZmRnczViT0NWRmpqNkE1blNOMWRWY0NwY0ZDdl9XX01hZ09FbklEVUhnVXN3VUFNMA?oc=5>

### Pfizer, Inc. (PFE) Stock Forecasts
- Summary: Analysts’ projections for Pfizer’s future stock performance.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiiAFBVV95cUxQV09Ia1VhZXBEWFF3Y0ZrYUNtUk9maWh4cjBzN19FbVc1WFRrTDFxME4yRWdkN1U2VVF2T2YtaGltZjZZamJfLVFrWmJGUE4tM2VIYzF3OVVWcFZvbk4wT2RlbHFvc1dVQjh4NGp4RjRSS3lwRG5rWU9nTExMR2FFTTJtT0IwWWxO?oc=5>

### Pfizer: The Portfolio Transformation Is Gaining Momentum (NYSE:PFE)
- Summary: Pfizer is actively reshaping its product portfolio, indicating strategic focus on high-growth areas.
- Date: 2026-11-05 | Impact: medium | Horizon: medium | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxPWkhFWVJuMGRVSDktTlZ2VG16SVkxd2hDZ3ZpMmNzbjJpRG1uMk5wRzNlNWhKT0RPZlY0TTY3czZMZy1yc3ltdzMtcURXTUxDbjlWLVJESXFHWkNJVHJWZGhYNU5mSU5TcEprU3ZCNGlqaUhQVXVtWGR5VnNJTU41aVVhZUh1RjlsSW41SkhDQ3VwTGs4NUtVYU13R0U?oc=5>

### Pfizer Appoints Cecile Guegan as Chief Financial Officer
- Summary: Pfizer names Cecile Guegan CFO, signaling leadership change.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi1wFBVV95cUxNM2RaZ2JjaGEyWnVEMEZHOGlISlMxWWdtOVJaZGs4TTFOTzdZWWRBTlhoOXQ4OGJsdWFqY25Lb3I2b2ZkSWJvd1piU2JBZXdHMnFTZzIxNXgxUy1Gd0ZnLWlkZXdTYXBBVGxxa3RhQUFnUVF1TmUyZUpnQ3NYOHA1NnpadklrdnNSQlZVdUVjNzNaTlRDZVdtZjV6Z05NREEtNVJOTGZwSHctMTNfMmV2di1CRGdVNUxnTFhyVGJDc3FZOWRKOU5VaW1Pc0hWdlUzQmhicUVVOA?oc=5>

### Pfizer Q3: The Street Is Pricing In Too Much Deceleration For This 5.7% Yield (NYSE:PFE)
- Summary: Market expects slower growth, affecting Q3 earnings outlook.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxOOHAyM3o1eVlzNVJKd2NBdnhsZXJuZXBBdjhSQUEtZllhNUs4WVY0aW5acGllSDBELWZuaWljMUtfWUZkdmZ1cC1icnN4Uzh6QWV5cUk5MWc4c0lFclBkRU0xNklod2hRdGtyVVZBLWVIY2dkSG1zSkFINTc2WVZDRmJ5Q0R3REZCaTlaZVU0X0U0cXlyZWpnT3hNZU5yUGVscFV5cUt5SEpMQklOTmxveFFQOTJhWVZycDJGdEZwS193QQ?oc=5>

### Pfizer (NYSE:PFE) reports strong Q3 2026, full-year outlook slightly exceeds expectations
- Summary: Pfizer reports robust Q3 results and better-than-expected full-year outlook.
- Date: 2026-11-03 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMi4AFBVV95cUxQNGRoVWpzRFYzcFdpQTRhdVlTRkhya0RfMy0tejhsVHpZb29aVjFUVU5oM01iMVRPb3pzSGI2ZjVWNTc1QmRrWVpzSDFFNlhGMGh4VWdVYTVuNE9SWEpZUmtEY0xYWFVOcjVHbDQwMnRndVNrN3p3QmtLTi1aTWJvZHoyLTR6cjkxSXV3RktMTks1TXp4cEVubU55TFZJY1VuSUhid05WX3lZWG14OHBLWmppckc0Mjh0SUhDNVdQLXdMWkh1anpSMW1mQjRERHYxUmFsWEV2bTR1Z0lMUkJHcw?oc=5>

### Pfizer (PFE) Appoints Cecile Guegan As Permanent Chief Financial Officer
- Summary: Pfizer names Cecile Guegan as its new permanent CFO, signaling a leadership change in the finance department.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 1
- Sources: <https://news.google.com/rss/articles/CBMi0wFBVV95cUxOUDZGMV9URS15Q3VFbUJwXzZkS0pSMEM2elJ4RGktNmo2dnNQM0xsTk02Uk1IMlBHV3ZQRllPdl81ZU0wVE51d1dDdXZOT3pWdlhuZ0cwM2tPU0pSeUFuR1VwSi16dFZVX3dpX1dpRGZwTldhdlF1cDQyTi1yemJkQTV4d0dmQkl6R1F0VXNyejc2eHVpMFlPaDByeGl2SXdSY2x4Z0NBeFYtOTdlVTQxS0tiYU5uclRzUWVJNEpuMHh2anQtOVQ1b3VBblZXdnpLc3E40gHYAUFVX3lxTFBxcXh6RUJUd0U4em9NX05fbi1GbEM0RTJ1WnpEbFJZRnBRSm82S3l4N2FTTXFCZS1PbGlLbkFqeFdTaE1QRmVVODFzbFRzLURMRmlnR0NPNVRsTUNYZWNFUHZxRk1NOWZzQkFoblZmaFlfaG05c0x1dUh1V003S19ZUDZqbW1yNjhRWjFEZk1ma3FBU0gzTjJnTVVYMThESDFvLS1oNGs5ZWhsLTdRRF9sakhZeFFSZGVqelFZSVJ3ZmRqd2V1UWZiQXh5amRDQmZRZGxzem90Qg?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **PFE** | **41.99** | **1.88** | **8.70** | **-0.40** | **167,518,699,520.00 USD** | **28.41** |
| MRK | 148.21 | 8.06 | 13.77 | 4.70 | 361,725,493,248.00 USD | 76.08 |
| JNJ | 41.92 | 8.16 | 20.07 | 5.90 | 664,947,261,440.00 USD | 51.06 |
| LLY | 43.95 | 29.96 | 26.90 | 38.60 | 1,206,068,707,328.00 USD | 45.35 |

Peers fetched as_of: 2026-11-07; PFE reuses existing data (market data as_of: 2026-11-06); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-03
- Next expected earnings: 2027-02-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-07

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-03
- Revenue (latest available single quarter): 16,583,000,000.00 USD; period 2026-06-29/2026-09-27; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 3,242,000,000.00 USD; period 2026-06-29/2026-09-27; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/78003/000007800326000127/pfe-20260927.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMickFVX3lxTFBfVElSNTY2SkVSU0NJOUpBalpLNVRMUThqV3ZTb1RwcVhkWndyUHdFTTFJZVNhWXJOWDRXckVMVHVRdU1TLTFGdlNBbmMtM0JDdzlSbEVwanJrUElJT1huRGhsdUJDa3JZUGtxRm8tcjJ0UdIBd0FVX3lxTE5sX2ZVWW5pM29Fc2RUZ2lhLV9uM2RidDdWLXFGRkhhcnhpQ0NfVjBpVFBPbDloZU9HdXVhaF9nZXFrUTR1eVEtLU9uWUhNaXNKSmJmV2J3MUNybnVnVkFPU19QeWZ5QUJPdmFHbExqbFFoNHVFbEF3?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNa0N3bkQxVDFoY0lwZmlQQWlfcFVaX3ByU3lnZE5WbjBRRlg1c1lTaE1TV3c1NlRZdkVaVlhNeXduQkF4OWVkQ3p0amhWd2w2czdib3NmNjdDMHgxMlZteVhUZ0hXTmNGR29LSXltbEltaXlwSW9RbXFsXzdENHVveFE4dU1JZ19ZMjMyOERhSWNIejAyQjM5UVdCN2o?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxNdGlHb0hXbkJuS1BabHRTakp0TVN4SURLT1dZeDI5dVlHRXRLQXhWNkViNVRZekNlRFJHdUJlRmNfTnE0RjVlcHNQelJZMGh1cHdvRWlFeXFNMHIyZ2NwYmlVR0RhUEY1aU0xSTBkemh0V3pRaklCMTBMN2tyQ1pZR1Zyb1JPN3I5b2dVUG1FVjY5RWk4Q3c?oc=5
- https://news.google.com/rss/articles/CBMigwFBVV95cUxNOTF4c0NpeDNqUzhrd3BxcDRpVE5YbnRPRnNaRmNDOHczYml3Z3NBZVo5d1hwMnpxREpGMXlINzctcE9HdFpNa3gxXzJsMTBQSzdmZDlwZzVVQmN3VkpYMWgtbXNpWnJncW9HdHlGZl9YeXZvRGVobWtMR0s1Z29vYXdvNA?oc=5
- https://news.google.com/rss/articles/CBMi0wFBVV95cUxOTHd6WU5DQTJYRmlGVXNXTFBtWGVGY2pMeDdwRjg2UHhMQkU4cHFGb1JTMkxMM2Q1eXhTZE8xZHVBQ2RqdjNJWE5yU0pRNkdYVU1aUjdWSmF2b2Q1bDV1SWI1b3ZybmhXUm8yaDVuTEdwM0lEZnlyNXFDN0JuZWFoODVZbkRCalhYOEtEZXBYUFBYaTZWMG1fSVpMVl9ESU5kRHpFY0FMRy1xZ283bUl2OG5TUjlaLWR5eHVqdTl4Y1dUNlJrMGVPR2M0eEdkeWtPWWg00gHYAUFVX3lxTE5kcG9NVG1QbVJKN1BvOThzanRPS2l0dHNYdElIak5zempyMW8tbmZRUkZORW5ubm1nVm0zNnhlVlpuV2gzYjh4Qk5MbGpBRlVPNElOcTFGZXFuWklsa25XR0c2akZZb2duNHpJdzdOUkVTdWRqbUVxYWlSSS1VQW1fTWVIcWtBTkxFdldsek1fSXNQLTZXUnNvcmlBQ0xadDItUEcxdndpeVExdzlNYWdCV1NKLUplYjJEZHBLa25JQlFsVFRzX0g4UnRSMXYxWnhwYWdNcEo2TQ?oc=5
- https://news.google.com/rss/articles/CBMi0wFBVV95cUxPalM1eTlURTd1NWRhQjBGWm4yeU0tREI1WkZiT3dqNXBqQWVES3hkSzBKTlNzZW9WLUJkSWJSN3k5N1lkTlpRZ1NidTJ5Z0ZRSHlHT05tMlpZV09lMHl2elRpMlFPZV9OdDZQanc1ZTZtZjFuTVRuSHVORXFKTXdkWUdrX0lkaGh2UVJzcWJtbWs3NlhaM0dzS3BPSFJJQ3Ewa2hiU1JuUzFiYjlMa2dmZWdwOGNDVklIbVdTVkJhQTdsWTlSb2RKeUZnUjBkLWxqeDFv0gHYAUFVX3lxTFBpTDBuX0pxekZXNlVERG1Wd0lxMTBrMThRSWN1Yy1wUFFUTUhDTTkxSk85b3ZBTHhDbFFwY0tveEl3ZER3QmpSM0dkMzV2UWZ0ekxCWnRfRU5NbE01N2g4TkRUSHA0LUNEcnhKQ0l6bW1fMFlrUTYtVmNyaURHY0Y2eXgtMTg5Q0tqcERyOTFZREE3WEdGUWNVQTh4RTBaWHNuMFNCaGNkM2dmTHRqZkhDN0JDUGNxZXpZbE5rU0V4OHFVamx1U3lpdS1TTGpMRVo5a1o0OHk0Sg?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxOS1dDV1BleUNJdDB3S2F0cDltMmZXc0xnR2E3UWxPOG5ZOTJKT1cwMG9SdVp0UVU1dTZma1FUc1RCZmVEX3FzXy1VN3M0RHoxeFRUVk9vbjR3d05GemR0cTRtVmdBYnEtcDB3LXJKZTd5MHFJUzZFdFJCQ3FXNGlfNFNjRDh4MUdjTVQ3UFA2ZVNCbGFPQk1nVVpkdndyQQ?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxQQU9uNE1qbFRtYXJFRjhneHc1S2NySmYtc0RWaGU0blFtd2R3aTZZN3V2dHdHRHJHajBTbjV3LVdZZ0RrMjJNd0RUWU1XUl9uWGNQNE52NUxld2Y3dndwZDExU19UcXF1TzBrOFNBaFpNX2tROVQ5UnBoZmdiR3NTZDEwTnRmaFlnR1g5NWhmWlgyakdVMzVKVU4xcUcxZw?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNY2RxSEZsZk5UWW5Pd2ZVN2VOdENOT004RVZTLWp4allaejhEY3U4ZGpiMC1Ec2YtY3M5U1JRd0ZNVmpMRWxTblo3Vl9qN3JlY2JSX25pR1Z4b3RFV0hlZFRZUEhNR2dXRkVyLTg0dVRJWW51UldrY0g2bHQyQS1ObkUzR0NFV0hLTFhNa2xXZUstWExGVFBFUnJkMA?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxOaVA1cGtvS25jb25FMnNKX0VyUGk5UVljVjVpZndtMVFWQ01ZRWtvNVpvSFBRdVpDU0lZend5ZVhLbVk0VlVuNk9vSnRHaDRCOVVIcU9uTWhxWUx4RVRNWkhaWnRHVUFZenk3SHU1Tk5PQmtoWnpCMTV4cVp3MnU0SHlqZTNfLU1IMjlHM3ZGbEdpWG11OEZ2RmtkR1pPNHBPMHBtQVhmTlBTcHRiN2hTUHB0Y0VyVXByTjJZeGZqVE56UQ?oc=5
- https://news.google.com/rss/articles/CBMihAFBVV95cUxNTF9QOEpKdW5XeVk3V1dqSzRvay1ueGtWUnJyU1h0aGJ6ay1lelpLV2NpUDcyOGNKZktXa0taLXdGWngxTEhMSkVKMUhiald1Z0JKaUVPblIwNjA0eUlTV0puZGhuR0hrdUdIZ25CSjQ3bzF4b2c0d0EtbWh2MTNyR2FuV1E?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxPWUN6OU0xMTFqbFZfLVEwYjJrc2lESDJhaHV1ZXA4MEwwd1hzVlRmMEFoUkhoazA1UDk1QTlLRmlSNmVpTkF4RnZZaWVxSFp2aFp6d1NxRDd2amc5cG92MEhVZlFwdV9URWZWS0Rod0FLZXU1ZFlxQkNVQnB5V1ZEbWM0VVh4eUxldXdiaWNYUWpsbndSUHhGaldQTjUxcWJ0TENzSDEyS1Q?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxPQ2pCSkNOWGtCR09IaXRTWXhrcFN4NGRWNmViaklVUXA4dmFuelE0cjRaR3VNQUVDNXFEa0VscWdmaW5HQ0tXQjJwSlN4YkJldnpWMVg5R1BpYUhMaks3TmRrcVZ6Nk4wVkRRLXpnRUhFazdQOEJhMVFaOXN6R29INFYyZFZQSGk4cDR2c3pzdFVNb0lxMUVrVGJn?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxNbmZ2UWVhQnFxckMwRkc4MzZ1c0o0STlHaFowd2ZxZnVhZEtIS09ZLUEwU1Z2d2pSeWxWdXZlNlRxcTFxOXQ0MGg2WXpSVVRCYmdHRzYzR2YxVHhEaEZhbUEyd0tTOUg2VEJxMG1RaWJHaDZvRjBqUjBnMU51QWRMWXMtMGZrQmJfX2NuN2dBMkFfOTFGRU5PVVN5UHRqWkk?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxPN1Itd1VZUGl5dVBWVmhjS29zWk1FbmdRaFhwWVBPcjRTOWtTbzVHNmFPeThRTGZqaE95VDB4YmNnRHUzTlNUclVtM3V2Tkp1S2lCeVVKX3BhSGhsdVN3Rm1Vd1Nmb1NlQldUb0ZqUXY5RG5uZGZmaUt4TXR5b3RzSGlrVXMyRDlFVms5YmFyTzFvcmNx?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxPSFV5UkkzQ1dXSmdiZzlMU1lrZlVwR19kc1puUVJ1N3pPcVduc19iREE0ZU04TFJLNVczclVBb3pKYXhNNGpLdTJZZWN1RmNBblA5WjRPYnh0ZWg1aWlNWHI0b2ZsbktJU1RaZmRnczViT0NWRmpqNkE1blNOMWRWY0NwY0ZDdl9XX01hZ09FbklEVUhnVXN3VUFNMA?oc=5
- https://news.google.com/rss/articles/CBMiiAFBVV95cUxQV09Ia1VhZXBEWFF3Y0ZrYUNtUk9maWh4cjBzN19FbVc1WFRrTDFxME4yRWdkN1U2VVF2T2YtaGltZjZZamJfLVFrWmJGUE4tM2VIYzF3OVVWcFZvbk4wT2RlbHFvc1dVQjh4NGp4RjRSS3lwRG5rWU9nTExMR2FFTTJtT0IwWWxO?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxPWkhFWVJuMGRVSDktTlZ2VG16SVkxd2hDZ3ZpMmNzbjJpRG1uMk5wRzNlNWhKT0RPZlY0TTY3czZMZy1yc3ltdzMtcURXTUxDbjlWLVJESXFHWkNJVHJWZGhYNU5mSU5TcEprU3ZCNGlqaUhQVXVtWGR5VnNJTU41aVVhZUh1RjlsSW41SkhDQ3VwTGs4NUtVYU13R0U?oc=5
- https://news.google.com/rss/articles/CBMi1wFBVV95cUxNM2RaZ2JjaGEyWnVEMEZHOGlISlMxWWdtOVJaZGs4TTFOTzdZWWRBTlhoOXQ4OGJsdWFqY25Lb3I2b2ZkSWJvd1piU2JBZXdHMnFTZzIxNXgxUy1Gd0ZnLWlkZXdTYXBBVGxxa3RhQUFnUVF1TmUyZUpnQ3NYOHA1NnpadklrdnNSQlZVdUVjNzNaTlRDZVdtZjV6Z05NREEtNVJOTGZwSHctMTNfMmV2di1CRGdVNUxnTFhyVGJDc3FZOWRKOU5VaW1Pc0hWdlUzQmhicUVVOA?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxOOHAyM3o1eVlzNVJKd2NBdnhsZXJuZXBBdjhSQUEtZllhNUs4WVY0aW5acGllSDBELWZuaWljMUtfWUZkdmZ1cC1icnN4Uzh6QWV5cUk5MWc4c0lFclBkRU0xNklod2hRdGtyVVZBLWVIY2dkSG1zSkFINTc2WVZDRmJ5Q0R3REZCaTlaZVU0X0U0cXlyZWpnT3hNZU5yUGVscFV5cUt5SEpMQklOTmxveFFQOTJhWVZycDJGdEZwS193QQ?oc=5
- https://news.google.com/rss/articles/CBMi4AFBVV95cUxQNGRoVWpzRFYzcFdpQTRhdVlTRkhya0RfMy0tejhsVHpZb29aVjFUVU5oM01iMVRPb3pzSGI2ZjVWNTc1QmRrWVpzSDFFNlhGMGh4VWdVYTVuNE9SWEpZUmtEY0xYWFVOcjVHbDQwMnRndVNrN3p3QmtLTi1aTWJvZHoyLTR6cjkxSXV3RktMTks1TXp4cEVubU55TFZJY1VuSUhid05WX3lZWG14OHBLWmppckc0Mjh0SUhDNVdQLXdMWkh1anpSMW1mQjRERHYxUmFsWEV2bTR1Z0lMUkJHcw?oc=5
- https://news.google.com/rss/articles/CBMi0wFBVV95cUxOUDZGMV9URS15Q3VFbUJwXzZkS0pSMEM2elJ4RGktNmo2dnNQM0xsTk02Uk1IMlBHV3ZQRllPdl81ZU0wVE51d1dDdXZOT3pWdlhuZ0cwM2tPU0pSeUFuR1VwSi16dFZVX3dpX1dpRGZwTldhdlF1cDQyTi1yemJkQTV4d0dmQkl6R1F0VXNyejc2eHVpMFlPaDByeGl2SXdSY2x4Z0NBeFYtOTdlVTQxS0tiYU5uclRzUWVJNEpuMHh2anQtOVQ1b3VBblZXdnpLc3E40gHYAUFVX3lxTFBxcXh6RUJUd0U4em9NX05fbi1GbEM0RTJ1WnpEbFJZRnBRSm82S3l4N2FTTXFCZS1PbGlLbkFqeFdTaE1QRmVVODFzbFRzLURMRmlnR0NPNVRsTUNYZWNFUHZxRk1NOWZzQkFoblZmaFlfaG05c0x1dUh1V003S19ZUDZqbW1yNjhRWjFEZk1ma3FBU0gzTjJnTVVYMThESDFvLS1oNGs5ZWhsLTdRRF9sakhZeFFSZGVqelFZSVJ3ZmRqd2V1UWZiQXh5amRDQmZRZGxzem90Qg?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
