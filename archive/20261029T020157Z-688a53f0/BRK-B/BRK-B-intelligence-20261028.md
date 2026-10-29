# BRK-B Intelligence Report

- ticker: **BRK-B**
- Report as_of: **2026-10-28**
- Market data as_of: **2026-10-28**
- Quant sources: https://finance.yahoo.com/quote/BRK-B/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/BRK-B/key-statistics/
- AI analysis snapshot as_of: **2026-10-28**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-29T02:12:44.137045+00:00**
- AI status: **Partial: 1 headline remains unclassified and excluded from research conclusions**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 19, 'rule': 3, 'ai': 13, 'unknown': 1, 'irrelevant': 2})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **4** exact headline/source/date matches; prior report **20261028T015717Z-533e470c/BRK-B** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 19 unique headlines; 5 named publishers; 6 exact duplicates; 19 HTTPS source links; largest publisher share 63.16%; oldest publication 2026-10-21

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 540.3400 |
| Return 1D (%) | -0.4880 |
| Return 1W (%) | 0.2505 |
| Return 1M (%) | 7.4042 |
| Return YTD (%) | 7.4983 |
| Return 1Y (%) | 12.2341 |
| Annualized volatility (%) | 14.6775 |
| Beta vs SPY | -0.0418 |
| Max drawdown (%) | -9.4218 |
| Sharpe (rf=0) | 0.8629 |
| Downside deviation (rf=0, %) | 10.0919 |
| Sortino (rf=0) | 1.2550 |
| Historical VaR 95% (1D, %) | 1.4122 |
| Historical ES 95% (1D, %) | 2.0016 |
| Correlation vs SPY | -0.0362 |
| Tracking error vs SPY (%) | 19.7553 |
| P/E (trailing) | 13.66 |
| P/B | 0.00 |
| EV/EBITDA | -1.79 |
| Revenue growth (%) | 10.00 |
| Forward P/E (estimate) | 24.09 |
| Gross margin (%) | 30.33 |
| Operating margin (%) | 32.56 |
| Return on equity (%) | 12.12 |
| Free cash flow yield (%) | 6.22 |
| MA50 | 513.3526 |
| Close vs MA50 (%) | 5.2571 |
| MA200 | 495.2633 |
| Close vs MA200 (%) | 9.1016 |
| RSI (14, Wilder) | 65.3225 |
| MACD (12,26) | 9.8440 |
| MACD signal (9) | 8.1471 |
| MACD histogram | 1.6969 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'BRK-B': 270, 'SPY': 270}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 540.3400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.4880 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 0.2505 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 7.4042 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 7.4983 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 12.2341 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 14.6775 -> Low annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 10.0919 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.2550 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.4122 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.0016 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.0362 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 19.7553 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.0418 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -9.4218 -> Shallow peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.8629 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 24.0885 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 30.3320 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 32.5610 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 12.1200 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 6.2224 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 13.6587 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 65.3225 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 1.6969 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 5.2571 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 9.1016 -> Clearly above the moving-average trend level.

## TAILWINDS

### Berkshire shares shake the Buffett blues with new all-time highs
- Summary: Berkshire shares shake the Buffett blues with new all-time highs
- Date: 2026-10-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMif0FVX3lxTFBDUGVaejRDVUljZ2dXVkZibE43eVJuTlpLUnRlWlpXeERSYlFtd291bEJSdWJKb2NOZ29mY0xEWWE4RHIzVGM1ZkxxempDRTl3Q09wWXpfcGRyS3p6ZkxDRVFSRndXTFBlRVRMVDJqUHJTVDdYVUhldVBJVklnRWPSAYQBQVVfeXFMUFlBMEVBeGdQbnZCdHNhSG9ldTZZai1GOUpIamhNOXBPX3hBTVc4MjZUQmpTZVYyZ1lHcWR6WWpRWS01SDg2cGF5SkNyb3lyMWNkSllkY1I3clVxdVliYWZHQ3hnV2Vka2xiSzdULXZxVWQ1RHpvTDVDSlVPUTZpaFJ4U0pC?oc=5>

### Berkshire Hathaway B (BRK.B) Increases Despite Market Slip: Here's What You Need to Know
- Summary: Berkshire Hathaway shares rise even as broader market slips, indicating resilience.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxQX01PWk9DUFBveTAzMDFDMjFyeEpMNWVHLXgzaGVtRENkRWt4WW0ySkstLWVwaEVQd0tORi00aUhEaFYtQThfYUVzbkJDQW1wNWhFc3ROcEtJU3cyRFlWbThBUnBaMElIM2JiRkhvcXJvbXVXczJvaEFad0p1U1RPMF9FZGlVd09zQmVJZklSeFUtU05UQnc?oc=5>

### 10 Stocks Warren Buffett and His Successor, Greg Abel, Plan to Hold Forever
- Summary: Long-term holdings suggest stability and confidence in selected companies.
- Date: 2026-10-28 | Impact: medium | Horizon: long | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxOYUxValdVdG15cGprNExqMFhpU1VqQVQwbnpDZnd6Wi1ySkVBU1RKT2ZuV0UwQThwZGY5NW1abkMzZm40VGN5YmJ3aUl0b0dCTEJkRlExcjd0SGdrU29wWmxuYlBuakJKaFNiWnJldGVWLWZZTVUweVVEd3ZISTU2eXowRS16VnFQUDkxZmdYUmtkYnBGUXlHVU9ORUNmR2NHb2FZTDZBRk9NczJVcjhTQVl0LVBUNFU?oc=5>

### Berkshire Hathaway Stock Rose 10 Days in a Row in October for the First Time Since 2018. Here's What History Says Comes Next.
- Summary: Stock rose 10 consecutive days, first time since 2018, indicating positive momentum.
- Date: 2026-10-25 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxOZkFuMWpmT3otRzRPaEpoM0xlaUFNU2Y0cjYyZXYxRVJtZlRKVFl0Z3ZyQXpxdDVCSXp3X3hfZmFRY3NCaHlqVFgzSUNseWdvLXhIQWdyUnFfdlNkb3hqZVFqOTFhb19DdVpPc3lBaVBWdm9LZkhOTks0QkNEcThfSnY5a2hRUTFYdVNlbVQzUHd0OFdHTldXOTFuRXpiUQ?oc=5>

### Berkshire Finally Topped Its Pre-Buffett-Exit Peak
- Summary: Stock reached its pre-Buffett peak, signaling strong performance.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxNZV96cW9STksxZ0hjWFNDbDZTWXVicUhzeFdQaVo0eXZSUmx2clZ4MGxmd3hiOUtkcUoyZzFQVW5jc2VPUlpMeDNWdENpS0FtRXA3bEc3cWdLbm0tVDl1WGdMQWNLNnNvS0dVRGY2ejRvUUpiTHZhalRSLTN4ZElsRGFNNi1lX0R4aXhTLTMzWEZuVU1jLXNkR29SbDRuYmJjakU0?oc=5>

## HEADWINDS

### Warren Buffett's Berkshire Stock Flashes Strong Warning
- Summary: Stock issued a strong warning, signaling potential downside risk.
- Date: 2026-10-26 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxPa1BxSVZNc1FGSHVGeFNsazl3dnBCY2RvbkFmdTdPaF9tUzV1R0xvRGE2WFJPTkVtZ0xuLTR4T3F6cW9TYzRqbWFjcnV3X3ZHbHIyVlVySWZaWENrOFdYZUN6MEJXUmtOdENETFV4OWlNMXoxUjQzOXhuYk1lVTFNbE1kaFV4LWM4Ql9HZGhlVW1LejN4ZTUyT05QM0pCUHk3REVvWlNCbw?oc=5>

### ETFs Are Net Sellers of Berkshire Hathaway (BRK.B) on Oct. 23
- Summary: ETFs sold Berkshire shares, indicating short‑term selling pressure.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxNSFlBamNJYld5NmUwa2VCa09WSnVYRG9HVWtxWGpWcEdhNmw4eVF6UkFybnNiaUpFT1p2RGtodmZlZGxleHVESnNlckNGUnJCbnh1dm5GWFFsUWJ5OTRxVkhoSGRpb1dYVFFfT3RMY0NjSjVQOGpYTnlDYVg0QTROVDl1T0tTRDlWUEwwNkJ1czA2V0w3dFMtOVBNZUFwTjVTWmc?oc=5>

### Is Berkshire Hathaway Stock a Buy Near Its All-Time High?
- Summary: High price may deter new investors, indicating potential overvaluation.
- Date: 2026-10-27 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxOcHQ5LXhDTDB0czloZWlqRTdncFROSEZJc1ZTcXdTcGJ2V0Y5TlY2dlZPbmc3dlk3blZ0VWpRa1dUemtGWmR0WFRvcDVqQUUyUDd5LTM4QXhCVnhfLVpEeGFxLUxaOUdJcjhKZDcxT0dwVi1Rd2NmdktWZGFoN3FKUjgtaUxwSmw2U3pvV0duMk1pUG4wZWx5d3lvMmQ0czA?oc=5>

### Berkshire Hathaway: Is the Stock Still a Safe Buy Without Warren Buffett?
- Summary: Uncertainty about leadership may reduce perceived safety.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxOb3d2TFVQVlNMSXVKOU5rcWplYlNOdVV5WVdDMWlIQ3pJeXRtZ1RJakpmZTdOMi00aFJKWlcxeXZ6WW8xYk9BV0lxRzJwOUdVaDgyQTZzeHRtblpfRnF5OGpndFN3ZU9pbXpGT1J2WjZDS3NLREhoWXlXcjR1Rk1GVVBxazdsWGpnSVZFZmRFb0NiM01USTZyWDJKUC1TMWlCV1E?oc=5>

## CATALYSTS

### Berkshire Likely Has a Loss on Its Big Alphabet Stake After Earnings Miss
- Summary: Berkshire Likely Has a Loss on Its Big Alphabet Stake After Earnings Miss
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxQY29SaUxydzVyYTB4S2pIX09vSFhMNEhFSDIwYUVhR2QwdTFvbDA3Q1V0RkhUVkVEWWpvUnZmNmtYaGhSXzNuLTJDSHdidG9ZZ3RyWGtlMTc0c0pMbWpwZ2VCdGJBU0NVVndMNldyV2JjTlliaWpOdDJFMkkzMjZwMTdBbjB0dGhJTlcw?oc=5>

### Berkshire Hathaway (BRK.A) After Buffett’s Warning Looks Undervalued On Fair Value Narrative
- Summary: Berkshire Hathaway (BRK.A) After Buffett’s Warning Looks Undervalued On Fair Value Narrative
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxQcXdMQ28xZUpSZlVVU2pqalJVcFRoSWtNVXlRSU1DV2EzaUhvYXNURzlMZFRqZnU2X3lJbzFDRWJXR1cya0tpQUlJallDcHc4eUxHT3RZU1BwdVF5NTMxbUNfd0N2ZUY1SkdSV0JTTWtWMWNFTEtzcW80Sm5ra2dXRURYUmdJRXVwT3VicG5VXzI0U2VlSjAxeDV1cVpSQjhjQTBWcWJ3?oc=5>

### Berkshire Hathaway (BRK-B) Starts Spending Its Cash, but Is 24 Times Earnings Fair?
- Summary: Berkshire begins cash outlays, raising questions on valuation and spending strategy.
- Date: 2026-10-21 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQcjBSTEFUWUxMNFBQUmFMME5sWHUzbkdUY0RVNURhSUdLamhVYjVxX3pEd0d6Q0NHOUlJOTZvSEoxYjAxcVdSRnhidDNfa0VzMU5DaVdia0c4ZTMzUWdBc1NWS0hrTVFqdDZfTlBlYTlPeExrdW5ibVdvWGdwUVoxN2NEOENKQjFyMjV3NG9PYUVYR09wOTZGQWJrV3o?oc=5>

### Berkshire to Report Q3 Earnings: Time to Buy, Hold or Sell the Stock?
- Summary: Upcoming Q3 earnings release may influence investment decisions.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxQY0FxV3JTZVdPUVJZWFJvc1RnN19HTngwWkRHaERsMVQyeEdDaGNJZ3BSa3duTVV2YkFSYk43UkJNYmVYdWs3UDBfc181a2NvQUxLYmY1VDEtNTVscjZ0SFlJWmNac28tRUU0RThPTThjMmJtM1FSOXZvZEcxU3hsN3hMRnZyaEoyVHBISXFKZ19UV2VLS2E3VlNZeXNQY3M?oc=5>

### Warren Buffett's Successor, Greg Abel, Has 32% of Berkshire Hathaway's $364 Billion Portfolio Invested in 3 Unstoppable AI Stocks
- Summary: Greg Abel has allocated a significant portion of Berkshire’s portfolio to three AI stocks, indicating a strategic shift toward technology investments.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi6gFBVV95cUxPb2szY1FfR0FCYlV0N29iSWg5bndSdFdfTWNBazJoSC00Mi16RDFTa3pPaFNSTDU3elBINGRwZEprOHY4VWx0cE82a1BkeEIyZWdFbmFNYnRwWDVkVDN5WnZVcFhpbUJzSlVhYWIzb19mUjBzNkNFbTUxQWtFVjB2U2tNNXNrRVFlSlhGeEpZN29nODRTSmtpR0xub0kwX09QUXlIVXZrQ1NIcjhVWTUtenFBbzNxVFI0TS0ySDlpcVdOVkhJd2I2ZnlENEdrdGZrb1VKX19oTVh3Y3pYYm5sS2diTW12Z09SeEE?oc=5>

### Berkshire Hathaway Started Buying Back Its Own Stock Again This Year. Should You Buy It at a Record High?
- Summary: Berkshire Hathaway has resumed share buybacks this year, signaling confidence in its valuation and potential upside for shareholders.
- Date: 2026-10-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi3wFBVV95cUxOa0dobzY5aWRZMU5ZSnB1OVlCazNWYWdtWXJ1ZWRhNFZKV01zVUtPa3ZqNTBBSjNHSmpqWnpKb2UzdnNCTlB3SklYNnlzYUJKRTRQcEVoelFHQmhaQ2hNR2pnbnlhaUpZWWVLdGVPeGJCcWF5aHN3ckQtSlc5LTJjVlFWYnoySG92Q1U3dW9kMC10TnZHWkFXbGI3U3VkMXVwbXB1UGdjWHRRakdvc09idG1vdHp3bjhJQVdPQjJRaW1WT0lLcTJMREViWnZoR3VuQTE3bzNWQU92QkdlMTRN?oc=5>

## RISKS

### Warren Buffett's Successor, Greg Abel, Has 58.9% of Berkshire Hathaway's Portfolio Invested in Just 5 Stocks. Here's My Top Pick for November.
- Summary: Concentration in few stocks increases portfolio risk.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxPUmZMUVlpeVVKRjQtbjNfUjQ2SEl4VmN6RDhFV1VGdnM4RXBLdkE0d1RHR0dwcW96Mm42T2gzanFpX3NmNXJpM2JEQXRldUVUcTRtbExXT0Q3T094TUpSdFZBNHFWbFNOaE9IUnhhZDFCb0FudFF0b0RqcExUYWVmWUhfdVRXY1dOMkZqREZIWk02dVMxQzRDLVE1SS1id0RfZHc?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **BRK-B** | **13.66** | **0.00** | **-1.79** | **10.00** | **1,156,711,186,432.00 USD** | **12.23** |
| MKL | 10.24 | 1.20 | 6.40 | 12.70 | 22,856,499,200.00 USD | 0.37 |
| FFH.TO | 8.77 | 1.35 | 7.88 | -0.50 | 55,156,965,376.00 CAD | 6.93 |
| L | 13.60 | 1.18 | 8.03 | 3.90 | 22,527,932,416.00 USD | 12.28 |

Peers fetched as_of: 2026-10-28; BRK-B reuses existing data (market data as_of: 2026-10-28); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-08
- Next expected earnings: 2026-11-07 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-28

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-08-10
- Revenue (latest available single quarter): 101,808,000,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- Net income (latest available single quarter): 25,667,000,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/1067983/000119312526341032/brka-20260630.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMif0FVX3lxTFBDUGVaejRDVUljZ2dXVkZibE43eVJuTlpLUnRlWlpXeERSYlFtd291bEJSdWJKb2NOZ29mY0xEWWE4RHIzVGM1ZkxxempDRTl3Q09wWXpfcGRyS3p6ZkxDRVFSRndXTFBlRVRMVDJqUHJTVDdYVUhldVBJVklnRWPSAYQBQVVfeXFMUFlBMEVBeGdQbnZCdHNhSG9ldTZZai1GOUpIamhNOXBPX3hBTVc4MjZUQmpTZVYyZ1lHcWR6WWpRWS01SDg2cGF5SkNyb3lyMWNkSllkY1I3clVxdVliYWZHQ3hnV2Vka2xiSzdULXZxVWQ1RHpvTDVDSlVPUTZpaFJ4U0pC?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxQX01PWk9DUFBveTAzMDFDMjFyeEpMNWVHLXgzaGVtRENkRWt4WW0ySkstLWVwaEVQd0tORi00aUhEaFYtQThfYUVzbkJDQW1wNWhFc3ROcEtJU3cyRFlWbThBUnBaMElIM2JiRkhvcXJvbXVXczJvaEFad0p1U1RPMF9FZGlVd09zQmVJZklSeFUtU05UQnc?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxOYUxValdVdG15cGprNExqMFhpU1VqQVQwbnpDZnd6Wi1ySkVBU1RKT2ZuV0UwQThwZGY5NW1abkMzZm40VGN5YmJ3aUl0b0dCTEJkRlExcjd0SGdrU29wWmxuYlBuakJKaFNiWnJldGVWLWZZTVUweVVEd3ZISTU2eXowRS16VnFQUDkxZmdYUmtkYnBGUXlHVU9ORUNmR2NHb2FZTDZBRk9NczJVcjhTQVl0LVBUNFU?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxOS1hLX0Mwd0pQMDdTZk45cXpEazRuU0tlbDdsN3QwNjhYaGUtVEdkYTU3ajdIeHZiVWpHV2RvRm5KZWVUbmRWQUhYc3BGaHVuU0RNVWRzOVhjV1NURmFYM19maWhRMm8yTEJGcmxVeHl2NDZKZ3Nkck0tT0xBd0xtZFZoUDktQzkxaENON2ppRTkzLWJZLUVGLTlLVUxJWHJ1?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxOZkFuMWpmT3otRzRPaEpoM0xlaUFNU2Y0cjYyZXYxRVJtZlRKVFl0Z3ZyQXpxdDVCSXp3X3hfZmFRY3NCaHlqVFgzSUNseWdvLXhIQWdyUnFfdlNkb3hqZVFqOTFhb19DdVpPc3lBaVBWdm9LZkhOTks0QkNEcThfSnY5a2hRUTFYdVNlbVQzUHd0OFdHTldXOTFuRXpiUQ?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxQMW9rUmp4RnlObFJ3NWlmVk40d0ZPZ0gzbHlwNG5la1RLZ2xFNENxbXBsamw5dXZnTjd4NjBDanM1WTQtS3pueGNicXhMd3pNN2syRHBUYnJVR0JJc25SVmdHU2kwTWVxbm1WX2c1RDk3RkJWNmVqSFhsQWNsa1QwcGxDNV9lNGpEMUJjQTZnQzZxb28ya2cw?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxNZV96cW9STksxZ0hjWFNDbDZTWXVicUhzeFdQaVo0eXZSUmx2clZ4MGxmd3hiOUtkcUoyZzFQVW5jc2VPUlpMeDNWdENpS0FtRXA3bEc3cWdLbm0tVDl1WGdMQWNLNnNvS0dVRGY2ejRvUUpiTHZhalRSLTN4ZElsRGFNNi1lX0R4aXhTLTMzWEZuVU1jLXNkR29SbDRuYmJjakU0?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxPa1BxSVZNc1FGSHVGeFNsazl3dnBCY2RvbkFmdTdPaF9tUzV1R0xvRGE2WFJPTkVtZ0xuLTR4T3F6cW9TYzRqbWFjcnV3X3ZHbHIyVlVySWZaWENrOFdYZUN6MEJXUmtOdENETFV4OWlNMXoxUjQzOXhuYk1lVTFNbE1kaFV4LWM4Ql9HZGhlVW1LejN4ZTUyT05QM0pCUHk3REVvWlNCbw?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxNSFlBamNJYld5NmUwa2VCa09WSnVYRG9HVWtxWGpWcEdhNmw4eVF6UkFybnNiaUpFT1p2RGtodmZlZGxleHVESnNlckNGUnJCbnh1dm5GWFFsUWJ5OTRxVkhoSGRpb1dYVFFfT3RMY0NjSjVQOGpYTnlDYVg0QTROVDl1T0tTRDlWUEwwNkJ1czA2V0w3dFMtOVBNZUFwTjVTWmc?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxOcHQ5LXhDTDB0czloZWlqRTdncFROSEZJc1ZTcXdTcGJ2V0Y5TlY2dlZPbmc3dlk3blZ0VWpRa1dUemtGWmR0WFRvcDVqQUUyUDd5LTM4QXhCVnhfLVpEeGFxLUxaOUdJcjhKZDcxT0dwVi1Rd2NmdktWZGFoN3FKUjgtaUxwSmw2U3pvV0duMk1pUG4wZWx5d3lvMmQ0czA?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQdHFQcG1TREVKanV4RWZlNksyZUswYkhleXdQaGE2WFFlaFRNMVlnRzVaaVBfUk14bGk1SWJYck16OC1QMzd6X2NsYmlsTG1VQkxWcm9aSlFWdXd0WndrV1BFWGpZbExFWmdEb0pfNXRIQjY3UzE2UVdRNlV0U2xiSDhSTFAzNWFaT2pRbFkxV2RSQno3enR5dw?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxOb3d2TFVQVlNMSXVKOU5rcWplYlNOdVV5WVdDMWlIQ3pJeXRtZ1RJakpmZTdOMi00aFJKWlcxeXZ6WW8xYk9BV0lxRzJwOUdVaDgyQTZzeHRtblpfRnF5OGpndFN3ZU9pbXpGT1J2WjZDS3NLREhoWXlXcjR1Rk1GVVBxazdsWGpnSVZFZmRFb0NiM01USTZyWDJKUC1TMWlCV1E?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxOLUQ4NkFrUFJ4ZUJKMXd4ZktjTXc5WFUyVUl0UGFnS0x0QUNLM0VhQ08zZnFMT05oa2RNVnk3MDhrMUdoemJCaUJsS0RrMVZRTWRYd3RybUVMNV9yRmc2SklYaGhON2t2d05XQUp6UDBlWlFaenU4MWJ2TE1Cc0FVNDhqaF9KbndLU3JFS3dQNUN1QUozRjJxQWNEREN3NEd2Rm1WcXVZLVVQcktfemlWc21jcmk?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxQY29SaUxydzVyYTB4S2pIX09vSFhMNEhFSDIwYUVhR2QwdTFvbDA3Q1V0RkhUVkVEWWpvUnZmNmtYaGhSXzNuLTJDSHdidG9ZZ3RyWGtlMTc0c0pMbWpwZ2VCdGJBU0NVVndMNldyV2JjTlliaWpOdDJFMkkzMjZwMTdBbjB0dGhJTlcw?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxQcXdMQ28xZUpSZlVVU2pqalJVcFRoSWtNVXlRSU1DV2EzaUhvYXNURzlMZFRqZnU2X3lJbzFDRWJXR1cya0tpQUlJallDcHc4eUxHT3RZU1BwdVF5NTMxbUNfd0N2ZUY1SkdSV0JTTWtWMWNFTEtzcW80Sm5ra2dXRURYUmdJRXVwT3VicG5VXzI0U2VlSjAxeDV1cVpSQjhjQTBWcWJ3?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQcjBSTEFUWUxMNFBQUmFMME5sWHUzbkdUY0RVNURhSUdLamhVYjVxX3pEd0d6Q0NHOUlJOTZvSEoxYjAxcVdSRnhidDNfa0VzMU5DaVdia0c4ZTMzUWdBc1NWS0hrTVFqdDZfTlBlYTlPeExrdW5ibVdvWGdwUVoxN2NEOENKQjFyMjV3NG9PYUVYR09wOTZGQWJrV3o?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxQY0FxV3JTZVdPUVJZWFJvc1RnN19HTngwWkRHaERsMVQyeEdDaGNJZ3BSa3duTVV2YkFSYk43UkJNYmVYdWs3UDBfc181a2NvQUxLYmY1VDEtNTVscjZ0SFlJWmNac28tRUU0RThPTThjMmJtM1FSOXZvZEcxU3hsN3hMRnZyaEoyVHBISXFKZ19UV2VLS2E3VlNZeXNQY3M?oc=5
- https://news.google.com/rss/articles/CBMi6gFBVV95cUxPb2szY1FfR0FCYlV0N29iSWg5bndSdFdfTWNBazJoSC00Mi16RDFTa3pPaFNSTDU3elBINGRwZEprOHY4VWx0cE82a1BkeEIyZWdFbmFNYnRwWDVkVDN5WnZVcFhpbUJzSlVhYWIzb19mUjBzNkNFbTUxQWtFVjB2U2tNNXNrRVFlSlhGeEpZN29nODRTSmtpR0xub0kwX09QUXlIVXZrQ1NIcjhVWTUtenFBbzNxVFI0TS0ySDlpcVdOVkhJd2I2ZnlENEdrdGZrb1VKX19oTVh3Y3pYYm5sS2diTW12Z09SeEE?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxQQ2FVRFAtN1pJYVVKTGNYYTYxajZ0Y3BXT1cyb3VRRkV3TEZtV21WS0VOWDFOMjhabFlMZVA5QVh3MVhzZTNROFM3SlRFQWFibTU1TnBWU3YxLVNSdFZ0UU5jSExwVDh0MHpzNTdDTGNpWHl3Z1Q2azdidnNfZlhJZkpuRGpHS2tBbDczWU5hZjdsSUZITWp5NGNrUTQyZDlo?oc=5
- https://news.google.com/rss/articles/CBMi3wFBVV95cUxOa0dobzY5aWRZMU5ZSnB1OVlCazNWYWdtWXJ1ZWRhNFZKV01zVUtPa3ZqNTBBSjNHSmpqWnpKb2UzdnNCTlB3SklYNnlzYUJKRTRQcEVoelFHQmhaQ2hNR2pnbnlhaUpZWWVLdGVPeGJCcWF5aHN3ckQtSlc5LTJjVlFWYnoySG92Q1U3dW9kMC10TnZHWkFXbGI3U3VkMXVwbXB1UGdjWHRRakdvc09idG1vdHp3bjhJQVdPQjJRaW1WT0lLcTJMREViWnZoR3VuQTE3bzNWQU92QkdlMTRN?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxPUmZMUVlpeVVKRjQtbjNfUjQ2SEl4VmN6RDhFV1VGdnM4RXBLdkE0d1RHR0dwcW96Mm42T2gzanFpX3NmNXJpM2JEQXRldUVUcTRtbExXT0Q3T094TUpSdFZBNHFWbFNOaE9IUnhhZDFCb0FudFF0b0RqcExUYWVmWUhfdVRXY1dOMkZqREZIWk02dVMxQzRDLVE1SS1id0RfZHc?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
