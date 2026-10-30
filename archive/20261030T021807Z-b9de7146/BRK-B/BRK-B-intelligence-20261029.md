# BRK-B Intelligence Report

- ticker: **BRK-B**
- Report as_of: **2026-10-29**
- Market data as_of: **2026-10-29**
- Quant sources: https://finance.yahoo.com/quote/BRK-B/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/BRK-B/key-statistics/
- AI analysis snapshot as_of: **2026-10-29**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-30T02:18:14.273744+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 21, 'rule': 5, 'ai': 10, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **4** exact headline/source/date matches; prior report **20261028T015717Z-533e470c/BRK-B** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 21 unique headlines; 7 named publishers; 4 exact duplicates; 21 HTTPS source links; largest publisher share 66.67%; oldest publication 2026-10-24

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 541.9600 |
| Return 1D (%) | 0.2998 |
| Return 1W (%) | -0.9159 |
| Return 1M (%) | 7.8849 |
| Return YTD (%) | 7.8206 |
| Return 1Y (%) | 13.9146 |
| Annualized volatility (%) | 14.6273 |
| Beta vs SPY | -0.0425 |
| Max drawdown (%) | -9.4218 |
| Sharpe (rf=0) | 0.9674 |
| Downside deviation (rf=0, %) | 10.0225 |
| Sortino (rf=0) | 1.4119 |
| Historical VaR 95% (1D, %) | 1.4122 |
| Historical ES 95% (1D, %) | 2.0016 |
| Correlation vs SPY | -0.0369 |
| Tracking error vs SPY (%) | 19.7287 |
| P/E (trailing) | 13.63 |
| P/B | 0.00 |
| EV/EBITDA | -1.79 |
| Revenue growth (%) | 10.00 |
| Forward P/E (estimate) | 24.16 |
| Gross margin (%) | 30.33 |
| Operating margin (%) | 32.56 |
| Return on equity (%) | 12.12 |
| Free cash flow yield (%) | 6.20 |
| MA50 | 514.1994 |
| Close vs MA50 (%) | 5.3988 |
| MA200 | 495.4969 |
| Close vs MA200 (%) | 9.3771 |
| RSI (14, Wilder) | 66.4415 |
| MACD (12,26) | 9.6072 |
| MACD signal (9) | 8.4391 |
| MACD histogram | 1.1681 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'BRK-B': 271, 'SPY': 271}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 541.9600 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.2998 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -0.9159 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 7.8849 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 7.8206 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 13.9146 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 14.6273 -> Low annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 10.0225 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.4119 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.4122 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.0016 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.0369 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 19.7287 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.0425 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -9.4218 -> Shallow peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.9674 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 24.1607 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 30.3320 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 32.5610 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 12.1200 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 6.2038 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 13.6308 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 66.4415 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 1.1681 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 5.3988 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 9.3771 -> Clearly above the moving-average trend level.

## TAILWINDS

### Berkshire Is at All-Time Highs. How to Play the Stock From Here.
- Summary: Berkshire Is at All-Time Highs. How to Play the Stock From Here.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxNb0ZWcmxwUW4zVTlmZkQ3aEREMEVIZ29QOTY1UTFka01yc0prY2lMTFdQZ1JkSVVEUzNEeTRKYUVJemtxTlRreGo1UlNvVG5oOEN5WER0YUkwYWFfNlFoNDFZck1RZmNKcnZkSF95bE8wckdxZ05aQXJPaUJQd0t6dzhGV01CT0QzZ1loRmlEaFBTX0k3RnZOcWY0VmVkaEJ6dWVGX2pOSFFxdw?oc=5>

### Berkshire shares shake the Buffett blues with new all-time highs
- Summary: Berkshire shares shake the Buffett blues with new all-time highs
- Date: 2026-10-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMif0FVX3lxTFBDUGVaejRDVUljZ2dXVkZibE43eVJuTlpLUnRlWlpXeERSYlFtd291bEJSdWJKb2NOZ29mY0xEWWE4RHIzVGM1ZkxxempDRTl3Q09wWXpfcGRyS3p6ZkxDRVFSRndXTFBlRVRMVDJqUHJTVDdYVUhldVBJVklnRWPSAYQBQVVfeXFMUFlBMEVBeGdQbnZCdHNhSG9ldTZZai1GOUpIamhNOXBPX3hBTVc4MjZUQmpTZVYyZ1lHcWR6WWpRWS01SDg2cGF5SkNyb3lyMWNkSllkY1I3clVxdVliYWZHQ3hnV2Vka2xiSzdULXZxVWQ1RHpvTDVDSlVPUTZpaFJ4U0pC?oc=5>

### Berkshire Hathaway (BRK.B) Gains Momentum As Valuation Still Looks In Focus
- Summary: Berkshire’s valuation remains attractive, driving momentum in its stock.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNS3EtUEZPZUlYeU9nbjVBS2NfYmlVVTlnOWtCWXhEcjF1cjVOMlZyU1RmOXNHNE15cE5BVVMxNjBDNHduMHF3eEtmZEpvbjJENkUtSjk4aVJmT3RYR0ZmQllZUE5iNXpPejkxdVUzNVlCRlQyNFRlVFh3Mk9LYUR0RDRCX1lSbXhFcDk4Z3dQY3hteFdXMDVlQXo1aw?oc=5>

## HEADWINDS

### Warren Buffett's Berkshire Stock Flashes Strong Warning
- Summary: Stock issued a strong warning, signaling potential downside risk.
- Date: 2026-10-26 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxPa1BxSVZNc1FGSHVGeFNsazl3dnBCY2RvbkFmdTdPaF9tUzV1R0xvRGE2WFJPTkVtZ0xuLTR4T3F6cW9TYzRqbWFjcnV3X3ZHbHIyVlVySWZaWENrOFdYZUN6MEJXUmtOdENETFV4OWlNMXoxUjQzOXhuYk1lVTFNbE1kaFV4LWM4Ql9HZGhlVW1LejN4ZTUyT05QM0pCUHk3REVvWlNCbw?oc=5>

### ETFs Are Net Sellers of Berkshire Hathaway (BRK.B) on Oct. 23
- Summary: ETFs sold Berkshire shares, indicating short‑term selling pressure.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxNSFlBamNJYld5NmUwa2VCa09WSnVYRG9HVWtxWGpWcEdhNmw4eVF6UkFybnNiaUpFT1p2RGtodmZlZGxleHVESnNlckNGUnJCbnh1dm5GWFFsUWJ5OTRxVkhoSGRpb1dYVFFfT3RMY0NjSjVQOGpYTnlDYVg0QTROVDl1T0tTRDlWUEwwNkJ1czA2V0w3dFMtOVBNZUFwTjVTWmc?oc=5>

### Berkshire Hathaway: Is the Stock Still a Safe Buy Without Warren Buffett?
- Summary: Uncertainty about Berkshire’s safety post-Buffett raises concerns.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxOb3d2TFVQVlNMSXVKOU5rcWplYlNOdVV5WVdDMWlIQ3pJeXRtZ1RJakpmZTdOMi00aFJKWlcxeXZ6WW8xYk9BV0lxRzJwOUdVaDgyQTZzeHRtblpfRnF5OGpndFN3ZU9pbXpGT1J2WjZDS3NLREhoWXlXcjR1Rk1GVVBxazdsWGpnSVZFZmRFb0NiM01USTZyWDJKUC1TMWlCV1E?oc=5>

## CATALYSTS

### Berkshire Likely Has a Loss on Its Big Alphabet Stake After Earnings Miss
- Summary: Berkshire Likely Has a Loss on Its Big Alphabet Stake After Earnings Miss
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxQY29SaUxydzVyYTB4S2pIX09vSFhMNEhFSDIwYUVhR2QwdTFvbDA3Q1V0RkhUVkVEWWpvUnZmNmtYaGhSXzNuLTJDSHdidG9ZZ3RyWGtlMTc0c0pMbWpwZ2VCdGJBU0NVVndMNldyV2JjTlliaWpOdDJFMkkzMjZwMTdBbjB0dGhJTlcw?oc=5>

### Berkshire Hathaway Earnings Preview: What to Expect
- Summary: Berkshire Hathaway Earnings Preview: What to Expect
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxPbU9hWk1jaGdJWUpaT1U0cEVRb2NyNk5aQmtsMi1qc1lTV29lOC03RnRLYjl2MXF1QVBGV2lkenpTS3VYcC1iVllXWFQ0ejJCWUx0aEpaZXhjTk5SWTZrd3RVQlZ1V2Nnd1Rxcm9yYXdFUUZFd0l6bUFaNzFEdWRhcGxUWFktcXFjSUM2VDFCS2VwWUpidVFSNHR3?oc=5>

### Berkshire Hathaway (BRK.A) After Buffett’s Warning Looks Undervalued On Fair Value Narrative
- Summary: Berkshire Hathaway (BRK.A) After Buffett’s Warning Looks Undervalued On Fair Value Narrative
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxQcXdMQ28xZUpSZlVVU2pqalJVcFRoSWtNVXlRSU1DV2EzaUhvYXNURzlMZFRqZnU2X3lJbzFDRWJXR1cya0tpQUlJallDcHc4eUxHT3RZU1BwdVF5NTMxbUNfd0N2ZUY1SkdSV0JTTWtWMWNFTEtzcW80Sm5ra2dXRURYUmdJRXVwT3VicG5VXzI0U2VlSjAxeDV1cVpSQjhjQTBWcWJ3?oc=5>

### What Could Berkshire Hathaway (BRK.B) Gain From An Early AI Funding Round?
- Summary: Speculation on potential benefits from early AI funding for Berkshire Hathaway.
- Date: 2026-10-24 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxNZEw2bVhaMGVVc0FlS1RMOEtGWUNjVUMzZEZjeVhNNExOQUxqZThIOGZHNi1QTDVCaFc0OWpvQkF1OFprRWFKVUJTRnFyeS14MVZaZDVMdy1PYU00N01zd1diM3FVRXdaeElHamRwR09BM0NQVWFCVHBtdHk5d2l1aVFzVTlRWHZ1TG1YeEU2cFU0cXFNVzg2NHVB?oc=5>

### Berkshire Hathaway Trades Above its 50-SMA: Time to Buy the Stock?
- Summary: Analyst question on buying Berkshire stock above 50-SMA.
- Date: 2026-10-28 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxPVjQ2a1IyOTFTa005bm1Od1RqTHVOaDhMcE1PbHQyM1FJRXdBXzB2ZUN6dUY0bHJ3TXMxVDJUQmkyQklqbkwydzNTOU5mMF9UWEF6SE44Y3Blb0hreFVhclZBcnNwa1FidDloSDRMaHVQdkFzX1NHMTJIMVh5OFByWUZxUWdiZTdMN25DYU9xNThQTFlvcFVuV2JLaWlDeGowMm84Wm4zcEs?oc=5>

### Berkshire to Report Q3 Earnings: Time to Buy, Hold or Sell the Stock?
- Summary: Upcoming Q3 earnings announcement for Berkshire.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxQY0FxV3JTZVdPUVJZWFJvc1RnN19HTngwWkRHaERsMVQyeEdDaGNJZ3BSa3duTVV2YkFSYk43UkJNYmVYdWs3UDBfc181a2NvQUxLYmY1VDEtNTVscjZ0SFlJWmNac28tRUU0RThPTThjMmJtM1FSOXZvZEcxU3hsN3hMRnZyaEoyVHBISXFKZ19UV2VLS2E3VlNZeXNQY3M?oc=5>

### Berkshire Hathaway (BRK.B) stock price forecast: insurance businesses hold $359 bn in cash
- Summary: Large cash reserves in insurance units could support future growth.
- Date: 2026-10-29 | Impact: medium | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxNNFBxTEo5Q1doT1VNaTcyakVXSzFVaFRra3A4NXA1SUNnTjBRbFFzQUJCUU4yNmJ3ZU1iVDdEazkzMDd2eWhrQ2JDWVNCU2l5bzhmZm9BSjlyTlZ4OUlPT0FHZEhwQjVlMFVkcWJwdkJNajB5MzRDSk5vNExSVW5mQ0FCeUwwekV4RWFibG04WmhHb21ZeGxJWmlTeFBlRVZxRk5JdzlNVk42T1RhcDVkUEk3c0Y2QVQxZDdCUDdYZmdpd2s?oc=5>

### Warren Buffett's $48 Billion American Express Stake Has Been a Huge Winner. The Latest Results Say the Streak Is Far From Over.
- Summary: Buffett’s AmEx stake continues to perform well, boosting Berkshire’s returns.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxNY0Y1YzJaSTc3OHdpX0tuRlFUNGlPNkthbzFPUTZBNklmcmp3S3Z3TFhZd0JMbUh0SzYtSkd4RVRXU3dNUnl4eG9WOGVhcVhKZmNHWFdhQ0dBazZjMGQxU2JoU0VkTm4zZFU1bVl5UEpveFZoNDJUS3BHQ1ItOEhfbDBIMHQzVVR1c1J6UDB2VW9rSGdsUHh4aERsLTg2WHZFSXc?oc=5>

### Berkshire Hathaway Stock Rose 10 Days in a Row in October for the First Time Since 2018. Here's What History Says Comes Next.
- Summary: Berkshire Hathaway shares surged for 10 consecutive days in October, a first since 2018, indicating potential bullish momentum.
- Date: 2026-10-25 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxOZkFuMWpmT3otRzRPaEpoM0xlaUFNU2Y0cjYyZXYxRVJtZlRKVFl0Z3ZyQXpxdDVCSXp3X3hfZmFRY3NCaHlqVFgzSUNseWdvLXhIQWdyUnFfdlNkb3hqZVFqOTFhb19DdVpPc3lBaVBWdm9LZkhOTks0QkNEcThfSnY5a2hRUTFYdVNlbVQzUHd0OFdHTldXOTFuRXpiUQ?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **BRK-B** | **13.63** | **0.00** | **-1.79** | **10.00** | **1,160,179,089,408.00 USD** | **13.91** |
| MKL | 13.29 | 1.26 | 6.40 | 12.70 | 23,134,404,608.00 USD | 2.24 |
| FFH.TO | 8.88 | 1.37 | 7.98 | -0.50 | 55,973,761,024.00 CAD | 11.91 |
| L | 13.69 | 1.19 | 8.12 | 3.90 | 22,832,531,456.00 USD | 14.47 |

Peers fetched as_of: 2026-10-29; BRK-B reuses existing data (market data as_of: 2026-10-29); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-08
- Next expected earnings: 2026-11-07 (yfinance; expected dates may change)

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
- Filing date: 2026-08-10
- Revenue (latest available single quarter): 101,808,000,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- Net income (latest available single quarter): 25,667,000,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/1067983/000119312526341032/brka-20260630.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiqgFBVV95cUxNb0ZWcmxwUW4zVTlmZkQ3aEREMEVIZ29QOTY1UTFka01yc0prY2lMTFdQZ1JkSVVEUzNEeTRKYUVJemtxTlRreGo1UlNvVG5oOEN5WER0YUkwYWFfNlFoNDFZck1RZmNKcnZkSF95bE8wckdxZ05aQXJPaUJQd0t6dzhGV01CT0QzZ1loRmlEaFBTX0k3RnZOcWY0VmVkaEJ6dWVGX2pOSFFxdw?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxOTlpyQ1JrbEZGTVV3Q0cyOFpjVV9Dd1ZqSFFvNEJUakRnUjhpYnRaU3FhZER5blR0ZmIxUkVyVGdQTVAxcDcyQmxfRlpIOVp0eVpibjUxN3A3TGNTNWR1WVkySFVqa05teGNTaHY1OFV3YncwWkw4WUlDRXZ2NUtXbnJfald1MFR2WFBtYXhGM3VSeXJIalNKajhtbDY?oc=5
- https://news.google.com/rss/articles/CBMif0FVX3lxTFBDUGVaejRDVUljZ2dXVkZibE43eVJuTlpLUnRlWlpXeERSYlFtd291bEJSdWJKb2NOZ29mY0xEWWE4RHIzVGM1ZkxxempDRTl3Q09wWXpfcGRyS3p6ZkxDRVFSRndXTFBlRVRMVDJqUHJTVDdYVUhldVBJVklnRWPSAYQBQVVfeXFMUFlBMEVBeGdQbnZCdHNhSG9ldTZZai1GOUpIamhNOXBPX3hBTVc4MjZUQmpTZVYyZ1lHcWR6WWpRWS01SDg2cGF5SkNyb3lyMWNkSllkY1I3clVxdVliYWZHQ3hnV2Vka2xiSzdULXZxVWQ1RHpvTDVDSlVPUTZpaFJ4U0pC?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNS3EtUEZPZUlYeU9nbjVBS2NfYmlVVTlnOWtCWXhEcjF1cjVOMlZyU1RmOXNHNE15cE5BVVMxNjBDNHduMHF3eEtmZEpvbjJENkUtSjk4aVJmT3RYR0ZmQllZUE5iNXpPejkxdVUzNVlCRlQyNFRlVFh3Mk9LYUR0RDRCX1lSbXhFcDk4Z3dQY3hteFdXMDVlQXo1aw?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxPa1BxSVZNc1FGSHVGeFNsazl3dnBCY2RvbkFmdTdPaF9tUzV1R0xvRGE2WFJPTkVtZ0xuLTR4T3F6cW9TYzRqbWFjcnV3X3ZHbHIyVlVySWZaWENrOFdYZUN6MEJXUmtOdENETFV4OWlNMXoxUjQzOXhuYk1lVTFNbE1kaFV4LWM4Ql9HZGhlVW1LejN4ZTUyT05QM0pCUHk3REVvWlNCbw?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxNSFlBamNJYld5NmUwa2VCa09WSnVYRG9HVWtxWGpWcEdhNmw4eVF6UkFybnNiaUpFT1p2RGtodmZlZGxleHVESnNlckNGUnJCbnh1dm5GWFFsUWJ5OTRxVkhoSGRpb1dYVFFfT3RMY0NjSjVQOGpYTnlDYVg0QTROVDl1T0tTRDlWUEwwNkJ1czA2V0w3dFMtOVBNZUFwTjVTWmc?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxOb3d2TFVQVlNMSXVKOU5rcWplYlNOdVV5WVdDMWlIQ3pJeXRtZ1RJakpmZTdOMi00aFJKWlcxeXZ6WW8xYk9BV0lxRzJwOUdVaDgyQTZzeHRtblpfRnF5OGpndFN3ZU9pbXpGT1J2WjZDS3NLREhoWXlXcjR1Rk1GVVBxazdsWGpnSVZFZmRFb0NiM01USTZyWDJKUC1TMWlCV1E?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxQY29SaUxydzVyYTB4S2pIX09vSFhMNEhFSDIwYUVhR2QwdTFvbDA3Q1V0RkhUVkVEWWpvUnZmNmtYaGhSXzNuLTJDSHdidG9ZZ3RyWGtlMTc0c0pMbWpwZ2VCdGJBU0NVVndMNldyV2JjTlliaWpOdDJFMkkzMjZwMTdBbjB0dGhJTlcw?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxPbU9hWk1jaGdJWUpaT1U0cEVRb2NyNk5aQmtsMi1qc1lTV29lOC03RnRLYjl2MXF1QVBGV2lkenpTS3VYcC1iVllXWFQ0ejJCWUx0aEpaZXhjTk5SWTZrd3RVQlZ1V2Nnd1Rxcm9yYXdFUUZFd0l6bUFaNzFEdWRhcGxUWFktcXFjSUM2VDFCS2VwWUpidVFSNHR3?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxQcXdMQ28xZUpSZlVVU2pqalJVcFRoSWtNVXlRSU1DV2EzaUhvYXNURzlMZFRqZnU2X3lJbzFDRWJXR1cya0tpQUlJallDcHc4eUxHT3RZU1BwdVF5NTMxbUNfd0N2ZUY1SkdSV0JTTWtWMWNFTEtzcW80Sm5ra2dXRURYUmdJRXVwT3VicG5VXzI0U2VlSjAxeDV1cVpSQjhjQTBWcWJ3?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxNZEw2bVhaMGVVc0FlS1RMOEtGWUNjVUMzZEZjeVhNNExOQUxqZThIOGZHNi1QTDVCaFc0OWpvQkF1OFprRWFKVUJTRnFyeS14MVZaZDVMdy1PYU00N01zd1diM3FVRXdaeElHamRwR09BM0NQVWFCVHBtdHk5d2l1aVFzVTlRWHZ1TG1YeEU2cFU0cXFNVzg2NHVB?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxPVjQ2a1IyOTFTa005bm1Od1RqTHVOaDhMcE1PbHQyM1FJRXdBXzB2ZUN6dUY0bHJ3TXMxVDJUQmkyQklqbkwydzNTOU5mMF9UWEF6SE44Y3Blb0hreFVhclZBcnNwa1FidDloSDRMaHVQdkFzX1NHMTJIMVh5OFByWUZxUWdiZTdMN25DYU9xNThQTFlvcFVuV2JLaWlDeGowMm84Wm4zcEs?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxQYVgtNWNPbmtVb3NFZ2hraFRULUNXZk1tMFpOUlluREw5MHZ1RklSQU4wODFxSkFUWGNNNGpVS25xMzRkU2dnZ2tjU2hIYnZqTkhibUdHckdYcEJ4UXd5NjZ1TFUwZzkxMHl6THhIX0Z4eEhSd3ctaFNFZHNpM3JMV2VwM3FhMFo1dXlDcC1uT0pIdVgxcEdiNGF6NnE2YjhJ?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxQY0FxV3JTZVdPUVJZWFJvc1RnN19HTngwWkRHaERsMVQyeEdDaGNJZ3BSa3duTVV2YkFSYk43UkJNYmVYdWs3UDBfc181a2NvQUxLYmY1VDEtNTVscjZ0SFlJWmNac28tRUU0RThPTThjMmJtM1FSOXZvZEcxU3hsN3hMRnZyaEoyVHBISXFKZ19UV2VLS2E3VlNZeXNQY3M?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxNNFBxTEo5Q1doT1VNaTcyakVXSzFVaFRra3A4NXA1SUNnTjBRbFFzQUJCUU4yNmJ3ZU1iVDdEazkzMDd2eWhrQ2JDWVNCU2l5bzhmZm9BSjlyTlZ4OUlPT0FHZEhwQjVlMFVkcWJwdkJNajB5MzRDSk5vNExSVW5mQ0FCeUwwekV4RWFibG04WmhHb21ZeGxJWmlTeFBlRVZxRk5JdzlNVk42T1RhcDVkUEk3c0Y2QVQxZDdCUDdYZmdpd2s?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxNY0Y1YzJaSTc3OHdpX0tuRlFUNGlPNkthbzFPUTZBNklmcmp3S3Z3TFhZd0JMbUh0SzYtSkd4RVRXU3dNUnl4eG9WOGVhcVhKZmNHWFdhQ0dBazZjMGQxU2JoU0VkTm4zZFU1bVl5UEpveFZoNDJUS3BHQ1ItOEhfbDBIMHQzVVR1c1J6UDB2VW9rSGdsUHh4aERsLTg2WHZFSXc?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxOZkFuMWpmT3otRzRPaEpoM0xlaUFNU2Y0cjYyZXYxRVJtZlRKVFl0Z3ZyQXpxdDVCSXp3X3hfZmFRY3NCaHlqVFgzSUNseWdvLXhIQWdyUnFfdlNkb3hqZVFqOTFhb19DdVpPc3lBaVBWdm9LZkhOTks0QkNEcThfSnY5a2hRUTFYdVNlbVQzUHd0OFdHTldXOTFuRXpiUQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
