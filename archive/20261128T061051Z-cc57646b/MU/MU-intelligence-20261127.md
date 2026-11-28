# MU Intelligence Report

- ticker: **MU**
- Report as_of: **2026-11-27**
- Market data as_of: **2026-11-27**
- Quant sources: https://finance.yahoo.com/quote/MU/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/MU/key-statistics/
- AI analysis snapshot as_of: **2026-11-27**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-28T06:26:54.893768+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 1, 'ai': 16, 'unknown': 0, 'irrelevant': 8})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **11** exact headline/source/date matches; prior report **20261127T063646Z-c0c26981/MU** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 9 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 40.0%; oldest publication 2026-11-24

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 646.9500 |
| Return 1D (%) | 7.6008 |
| Return 1W (%) | 8.8207 |
| Return 1M (%) | -30.3426 |
| Return YTD (%) | 126.8397 |
| Return 1Y (%) | 181.2841 |
| Annualized volatility (%) | 87.8482 |
| Beta vs SPY | 3.4650 |
| Max drawdown (%) | -50.9958 |
| Sharpe (rf=0) | 1.5912 |
| Downside deviation (rf=0, %) | 54.9123 |
| Sortino (rf=0) | 2.5456 |
| Historical VaR 95% (1D, %) | 7.6856 |
| Historical ES 95% (1D, %) | 10.8711 |
| Correlation vs SPY | 0.5925 |
| Tracking error vs SPY (%) | 79.8695 |
| P/E (trailing) | 8.70 |
| P/B | 5.29 |
| EV/EBITDA | 6.37 |
| Revenue growth (%) | 379.30 |
| Forward P/E (estimate) | 3.16 |
| Gross margin (%) | 80.72 |
| Operating margin (%) | 74.59 |
| Return on equity (%) | 88.26 |
| Free cash flow yield (%) | 3.97 |
| MA50 | 888.8046 |
| Close vs MA50 (%) | -27.2112 |
| MA200 | 777.4857 |
| Close vs MA200 (%) | -16.7895 |
| RSI (14, Wilder) | 40.3263 |
| MACD (12,26) | -70.3737 |
| MACD signal (9) | -65.4622 |
| MACD histogram | -4.9115 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'MU': 291, 'SPY': 291}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 646.9500 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 7.6008 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 8.8207 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -30.3426 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 126.8397 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 181.2841 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 87.8482 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 54.9123 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 2.5456 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 7.6856 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 10.8711 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5925 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 79.8695 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 3.4650 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -50.9958 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.5912 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 3.1560 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 80.7160 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 74.5860 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 88.2600 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 3.9687 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 8.7038 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 40.3263 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -4.9115 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -27.2112 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -16.7895 -> Clearly below the moving-average trend level.

## TAILWINDS

### Why Is Micron Technology Stock Surging Today?
- Summary: Micron’s stock price rises today, indicating positive market sentiment.
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxOMDM2VUo4OEx2NGdYWjVmUUVmNkx4NWc0Q2lTQmhfQmdqUzMzSjFqSXpLdTY3VFNrNlZUTGlHdzZWU0lIWi1pNGpBb3kyMEw5c2ltQ1FUb1RqVjJnWjZlRFdYUFBSVERkQ05LV0ViVS04bFBvMmxueGtrSW5FcmlRTkRncnFZblFjT2Fud1lrbFVGZFhGdThZUDFKNWJOOG0zNFE?oc=5>

### Why Is Micron Stock Jumping Today?
- Summary: Micron’s shares jump today, reflecting favorable market conditions.
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxNc2tBak9GbGducUhqek1hTEwzWU9Yd3ctRVdvamd6R2NJX0ZrZGhrUUMyVmVDeVhnNVlodzVFZFgyc1NKSGUyTkEzOHRTTTJQWGZTWnZhV245OG5JSGk5Y0JaWjNGUWhLLWxjUDlzRGRpZnNwbHM3MUhmWmtzVjR1RzBTTXlMZkdjSjRzalA3VQ?oc=5>

### Micron: 3.9x Earnings Is Insane (NASDAQ:MU)
- Summary: Micron reports earnings 3.9x higher than expected, indicating strong profitability.
- Date: 2026-11-27 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMie0FVX3lxTE1vN3lPN3E2NXNlLVJsbG1US1lCd1doa21VcEI5ckZ2Q1pVaGkxbVd2QWYzbkJ4NHlZTUtwT25sTHlSSjdjc2pSVlFfS05IN3lXc3NFRW95bGZzOGhSbVJDX0tMdVpRRnVPTEdYNER3YUxYckluRGlpU3BkTQ?oc=5>

### Micron Technology (MU) Products Are Exempt From New US Tariffs
- Summary: Micron’s products are exempt from new U.S. tariffs, reducing potential cost pressures and supporting sales stability.
- Date: 2026-11-26 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxNT0lyUFVtNWVHZ3g3a2NlRk8yX0FWUnVtVGxGWndjUmNaak1OY1E3N1A2ejNLVXlHMkVEU3VZbzc3Z3dCWDJoaERSRnZXTlA5Yy1RZWw0dERzak5hX1VHbHNBUnZrd2hldTRLcDJyckJvbXh3OEpCRFl4ZS1uVHAzbFRSRWUtemR3T0l3RnZIRlpZeTVPQjFuRVd6a1JuQmxVZ0Nz?oc=5>

## HEADWINDS

### MU Stock Downgraded, Price Target Cut By Almost $1,000: BNP Paribas Flags 2028 Hyperscaler Capacity Risks
- Summary: MU Stock Downgraded, Price Target Cut By Almost $1,000: BNP Paribas Flags 2028 Hyperscaler Capacity Risks
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxQN2xTTnFhTGcyQ1JESmtFRG5LWUhxYjQ4S2lsT2otYjhObS1EZ3dhbGJjSmJGX3RwUVQtc01vTG1KTk50d2dxckluZktQU3FHUlZOYzYzdXhyMkVMdlV2cmdzN2xmdUdfaVhoUzdrZmFJanlEbXB2bVQ4QzZrUnZZYWlLVVBMRk8ydi02R3lPS1pEZDJIdVhoRXFZME5IQQ?oc=5>

### Micron Stock: The Earnings Peak Is Nowhere In Sight (NASDAQ:MU)
- Summary: Earnings outlook appears weak, no peak expected soon.
- Date: 2026-11-24 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxOWFlyeDJJeXg4SmMwaTdrdXZwc0tHTFFrLWRieFl2UnBnVkFFcFV2dHVncTE1dnRDa1VsSUVNRUo0cnpaTzRKb3FCcDBiS29mRlhnblk4d3NOVGt1UGxWQWw5Z3NmMjBUaHNSejVBWlI4dW5ZdDVPa3kyWFlNMXVqcW91dWRxdjlINm5CMzl6ckRpZ29wRHc?oc=5>

### Micron Stock Falls as UBS Cuts Price Target, BNP Paribas Downgrade Weighs
- Summary: Stock decline following analyst downgrades.
- Date: 2026-11-25 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMizgFBVV95cUxOcm5uSzFucTZkd1dyRWJzTGRZYWZQLUhhQXJyUUZsWTh5VEVpUjlBVVVnMkl4bWdyc1ZLZ1I2eVFTQzQ5NGV5eE5GMTl4VnlvcnhKY2phSTRZSlltWVdVVGVSWHVWYWxfZEJqYkN4OXZmcWRjcVQxLVFHZ0lodXdqNHhIWnFRSFE3dGZJUWhLQU1tOXNVNnZJdDVQd2ZhV19TNkZSVGtEVmsybEk4OW9TQS1qWVZYZngydVR3cTRwMGluRDRVX0dEMi16RUVBZw?oc=5>

### What Is Going on With Micron Tech Stock on Wednesday?
- Summary: Questions about Micron's current market performance.
- Date: 2026-11-25 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxQS25kX3lFaktpdXJYNUw0SFdDV3lHUjdiX2xZSUxoUDlKYUJYNFFrY1dpbXh4VW9VN1I2TWZ0djRYT2Vnem43NlhRZXF1Vkl5aEFBeDdtWTNOWVBtOHpoMTJSNFVXbUNEUmRLWkpIaVlOV0RXUnFfbUlXNTFYUmgyaXZjUlVMMmJqSk5VOWVVc1pRUzVtaHVyTUFoSUNaak1JbmpaT1Njd1BwN2FVeThtcDFETndkUQ?oc=5>

### Why Micron Stock Just Dropped Again
- Summary: Micron shares fell again, indicating a negative market reaction.
- Date: 2026-11-25 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxQWkpQcm91R3l5eFo3OVEtQ2lXN2I2WmVhZmFFZ0hvN2RTZ2hWd1dwNDRveEEtQzBFV1hCLWZiUE1JNklNeVNIRUUwbTdvUklvNlNyWkFGT2VQSG5ia2k5QjNGeG5lQWJGdjVMRUZiQ1h6UE91OURpVUR6bDFUNjZ3SnVvNXp4M1Q4dzFjZmU3Yno2WkZzamd4aVl3?oc=5>

### Micron Stock Is Jumping but There’s Bad News on Memory Prices
- Summary: Stock gains offset by negative memory price outlook, hurting prospects.
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMidkFVX3lxTE03a3R5bkdkT2gwM2wxcVVqVFgzaVEwUmF6bXUyNk9xSGxJRGFaV1lWRE5KT1BDVlpQMHVnaU95c3ljeUdsbE9IdVVKTnZiZ2V1eHphdnBHd2ZTS0VZUkZnSU50cWs5UHRZMENNNzEtZDEwQjNBYXc?oc=5>

### Micron Technology declines 11% as AI stocks drop (MU:NASDAQ)
- Summary: Micron shares fall 11% amid broader AI stock sell‑off.
- Date: 2026-11-25 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxQYVhjd2ZXSC1VdWw4QTBBbUd3Zy0ydEE5Wnd2WGNvazFGb3gyZUZKdXRuYzJJbFZ2QlFWZlJtQ2t1S3VDYWF1UW10TUdxLVFwejN1bWNPWi1Pc0lDR2syTTJyU3BoSlBqTG9SWEV1dWI5YkpSWnc1elp1ejlDa3pLMzJkUDZMclpvZkRTWkF3?oc=5>

### Micron: The Selloff Creates A Compelling Value Opportunity(NASDAQ:MU)
- Summary: Market selloff pressures Micron shares, presenting a buying opportunity for value investors.
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxNOUltdTEtcG0ydENZTDJnN0dWb3k2bndGR1FhLUU2d0F3THA2RWJzU3ZVUHJZZ3lBbmEtMDZ6ZW5JT0FLSlpMUmVJaUIxSkR4S2FBY3NVcmZIc1ZWVjl2bUJJLUhzUWxJV2g1dU5ORnFYM2ZXTjI2Y3lva09wSFo2U2Z6c0dES3lCY05IZ2dtWkhQOWlrdi10Rk5kd28wSVli?oc=5>

### Micron Technology Shares See Sharp Correction as Market Weighs Storage Chip Supply-Demand Rhythm
- Summary: Micron shares fell sharply as the market reassessed storage chip supply-demand dynamics, indicating potential short-term price pressure.
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiyAFBVV95cUxNcl8zWEdXeDF1ekJ5Z1k2LXVSVXVnZTdzWUMzclFoU2RTbXJzcWJCWHp2X19WemJ3TDRMb25Jcm4yMGZiMWFxcDk3TmloX2oxQXAwbDRBQ0U0OHB2VHl1RFhUQy1IQURXSzBNeDMtQlktOXdKZ0plc1EtYk9KQ0RHZzltZkdKVWltZlVIYmI0c0tJUWpuTkt4Nl9kUFY3N1V2NnluX0ZDVlc1OHMzWmVBV2JQYTlqa3BweUh5WVo5Qmg4LXVUUU1sTA?oc=5>

## CATALYSTS

### Micron Technology (MU) Dropped, So What Is Drawing Attention Now?
- Summary: Micron’s recent decline prompts analysis of underlying factors affecting its market trajectory.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxONEhmZjdQYXZtRENTeXQ5QVhoTlU5QjlPTlBsTzA1eGFtWmJLQl8xSkx3YlJiVzg4THJ6VF9fWjFyTnZPVGJObUZkVEhJZzdFdzMxd1JfYkRhTWQ2S2Z3T1pUTHJjeGotQjFOc0xCZlJjUUMxZllVV3J1aDF6NENwSUZiUnBEbVdNTE5raHBmc19Gams3cmtPMUdQeEFzRXRSdFNz?oc=5>

### MU Stock Alert: What to Know as Micron Reveals Surprising Spending Increase
- Summary: Micron announced higher spending, suggesting increased investment plans.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxQWWgwRmxaQm4tRHVtY1FnUElyZFZNTk15dG05S1hlWmo5aTZZVUZSRHBjb0lIS0FBZktDZXRoUTEwZkllVUd2Rzl3SFU2Y2poeFM4cUNPWmxXVmc5ZHRYSHNpUzRDSUt1TWRxa2xwTlJyMlRYTUN0ZU02SkhoRzNlVWVQVkRQT0FTcDBzZnZlUXlMYmxESWhIbkVIODRZU3Q4NUtYMmNfaVd1VGVOaTA3LWxtYnJGNV9pVGc?oc=5>

### Micron (MU) Has Secured $32 Billion in Customer Commitments. Here’s Why That Matters
- Summary: Micron secured $32B in customer commitments, boosting revenue prospects and signaling strong demand.
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxOamM0M051dndpNkFXREREWHBBdTF2a1RHSGotakFUQlpxNFhhRXRzOTBtdVZfXzBLMDgxdGdqNXZycnhKNzA1R1p0RzEyS212Y1poRTFUeHN5TmlTUmdyMFdza2FzQTVtSjVVTWt0TmJlc2I0ZmZ2MU5halRYbTZHbVVQazRpZndCelRkbkc4NlA4QlVlalNWLQ?oc=5>

## RISKS

### Micron Just Hit a $700 Ceiling, Caught a Downgrade, and Is Down 10% Today. Is MU a Toxic Stock or a Prime Bargain?
- Summary: Micron’s stock fell 10% after a downgrade, hitting a $700 ceiling. The downgrade reflects concerns over valuation and future performance.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxNX2ZQczZGWkZfbjNvak9BdndhRFE4UzRCNlU2ZGpub3NkRDR2YTdVYjVjVTh5Z0Z0RjRUZFFjV1RmRkxySjRoWnV3VUh5VnYtNlJ1ZW94NmVsaHVHeUN1WTNHV3RCODJqbXFYM2VSWWNTYTRrQWJkN2lkcEVLTWlmNFRiV2J1TjNmUEIzbGhBVUlwSmdaa0Jz?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **MU** | **8.70** | **5.29** | **6.37** | **379.30** | **734,245,748,736.00 USD** | **181.28** |
| WDC | 10.27 | 11.69 | 17.26 | 55.50 | 109,343,563,776.00 USD | 85.53 |
| STX | 26.73 | 33.91 | 20.18 | 61.00 | 116,998,111,232.00 USD | 88.29 |
| NXPI | 19.92 | 5.28 | 13.22 | 19.30 | 63,817,297,920.00 USD | 32.98 |

Peers fetched as_of: 2026-11-27; MU reuses existing data (market data as_of: 2026-11-27); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-09-30
- Next expected earnings: 2026-12-17 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-27

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-K
- Filing date: 2026-10-09
- Revenue (latest available single quarter): 8,440,000,000.00 USD; period 2018-06-01/2018-08-30; fiscal year/reporting period 2018/FY
- Net income (latest available single quarter): 28,243,000,000.00 USD; period 2026-02-27/2026-05-28; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/723125/000072312526000023/mu-20260903.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiogFBVV95cUxOMDM2VUo4OEx2NGdYWjVmUUVmNkx4NWc0Q2lTQmhfQmdqUzMzSjFqSXpLdTY3VFNrNlZUTGlHdzZWU0lIWi1pNGpBb3kyMEw5c2ltQ1FUb1RqVjJnWjZlRFdYUFBSVERkQ05LV0ViVS04bFBvMmxueGtrSW5FcmlRTkRncnFZblFjT2Fud1lrbFVGZFhGdThZUDFKNWJOOG0zNFE?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxNc2tBak9GbGducUhqek1hTEwzWU9Yd3ctRVdvamd6R2NJX0ZrZGhrUUMyVmVDeVhnNVlodzVFZFgyc1NKSGUyTkEzOHRTTTJQWGZTWnZhV245OG5JSGk5Y0JaWjNGUWhLLWxjUDlzRGRpZnNwbHM3MUhmWmtzVjR1RzBTTXlMZkdjSjRzalA3VQ?oc=5
- https://news.google.com/rss/articles/CBMie0FVX3lxTE1vN3lPN3E2NXNlLVJsbG1US1lCd1doa21VcEI5ckZ2Q1pVaGkxbVd2QWYzbkJ4NHlZTUtwT25sTHlSSjdjc2pSVlFfS05IN3lXc3NFRW95bGZzOGhSbVJDX0tMdVpRRnVPTEdYNER3YUxYckluRGlpU3BkTQ?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxNT0lyUFVtNWVHZ3g3a2NlRk8yX0FWUnVtVGxGWndjUmNaak1OY1E3N1A2ejNLVXlHMkVEU3VZbzc3Z3dCWDJoaERSRnZXTlA5Yy1RZWw0dERzak5hX1VHbHNBUnZrd2hldTRLcDJyckJvbXh3OEpCRFl4ZS1uVHAzbFRSRWUtemR3T0l3RnZIRlpZeTVPQjFuRVd6a1JuQmxVZ0Nz?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxQN2xTTnFhTGcyQ1JESmtFRG5LWUhxYjQ4S2lsT2otYjhObS1EZ3dhbGJjSmJGX3RwUVQtc01vTG1KTk50d2dxckluZktQU3FHUlZOYzYzdXhyMkVMdlV2cmdzN2xmdUdfaVhoUzdrZmFJanlEbXB2bVQ4QzZrUnZZYWlLVVBMRk8ydi02R3lPS1pEZDJIdVhoRXFZME5IQQ?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxOWFlyeDJJeXg4SmMwaTdrdXZwc0tHTFFrLWRieFl2UnBnVkFFcFV2dHVncTE1dnRDa1VsSUVNRUo0cnpaTzRKb3FCcDBiS29mRlhnblk4d3NOVGt1UGxWQWw5Z3NmMjBUaHNSejVBWlI4dW5ZdDVPa3kyWFlNMXVqcW91dWRxdjlINm5CMzl6ckRpZ29wRHc?oc=5
- https://news.google.com/rss/articles/CBMizgFBVV95cUxOcm5uSzFucTZkd1dyRWJzTGRZYWZQLUhhQXJyUUZsWTh5VEVpUjlBVVVnMkl4bWdyc1ZLZ1I2eVFTQzQ5NGV5eE5GMTl4VnlvcnhKY2phSTRZSlltWVdVVGVSWHVWYWxfZEJqYkN4OXZmcWRjcVQxLVFHZ0lodXdqNHhIWnFRSFE3dGZJUWhLQU1tOXNVNnZJdDVQd2ZhV19TNkZSVGtEVmsybEk4OW9TQS1qWVZYZngydVR3cTRwMGluRDRVX0dEMi16RUVBZw?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxQS25kX3lFaktpdXJYNUw0SFdDV3lHUjdiX2xZSUxoUDlKYUJYNFFrY1dpbXh4VW9VN1I2TWZ0djRYT2Vnem43NlhRZXF1Vkl5aEFBeDdtWTNOWVBtOHpoMTJSNFVXbUNEUmRLWkpIaVlOV0RXUnFfbUlXNTFYUmgyaXZjUlVMMmJqSk5VOWVVc1pRUzVtaHVyTUFoSUNaak1JbmpaT1Njd1BwN2FVeThtcDFETndkUQ?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxQWkpQcm91R3l5eFo3OVEtQ2lXN2I2WmVhZmFFZ0hvN2RTZ2hWd1dwNDRveEEtQzBFV1hCLWZiUE1JNklNeVNIRUUwbTdvUklvNlNyWkFGT2VQSG5ia2k5QjNGeG5lQWJGdjVMRUZiQ1h6UE91OURpVUR6bDFUNjZ3SnVvNXp4M1Q4dzFjZmU3Yno2WkZzamd4aVl3?oc=5
- https://news.google.com/rss/articles/CBMidkFVX3lxTE03a3R5bkdkT2gwM2wxcVVqVFgzaVEwUmF6bXUyNk9xSGxJRGFaV1lWRE5KT1BDVlpQMHVnaU95c3ljeUdsbE9IdVVKTnZiZ2V1eHphdnBHd2ZTS0VZUkZnSU50cWs5UHRZMENNNzEtZDEwQjNBYXc?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxQYVhjd2ZXSC1VdWw4QTBBbUd3Zy0ydEE5Wnd2WGNvazFGb3gyZUZKdXRuYzJJbFZ2QlFWZlJtQ2t1S3VDYWF1UW10TUdxLVFwejN1bWNPWi1Pc0lDR2syTTJyU3BoSlBqTG9SWEV1dWI5YkpSWnc1elp1ejlDa3pLMzJkUDZMclpvZkRTWkF3?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxNOUltdTEtcG0ydENZTDJnN0dWb3k2bndGR1FhLUU2d0F3THA2RWJzU3ZVUHJZZ3lBbmEtMDZ6ZW5JT0FLSlpMUmVJaUIxSkR4S2FBY3NVcmZIc1ZWVjl2bUJJLUhzUWxJV2g1dU5ORnFYM2ZXTjI2Y3lva09wSFo2U2Z6c0dES3lCY05IZ2dtWkhQOWlrdi10Rk5kd28wSVli?oc=5
- https://news.google.com/rss/articles/CBMiyAFBVV95cUxNcl8zWEdXeDF1ekJ5Z1k2LXVSVXVnZTdzWUMzclFoU2RTbXJzcWJCWHp2X19WemJ3TDRMb25Jcm4yMGZiMWFxcDk3TmloX2oxQXAwbDRBQ0U0OHB2VHl1RFhUQy1IQURXSzBNeDMtQlktOXdKZ0plc1EtYk9KQ0RHZzltZkdKVWltZlVIYmI0c0tJUWpuTkt4Nl9kUFY3N1V2NnluX0ZDVlc1OHMzWmVBV2JQYTlqa3BweUh5WVo5Qmg4LXVUUU1sTA?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxONEhmZjdQYXZtRENTeXQ5QVhoTlU5QjlPTlBsTzA1eGFtWmJLQl8xSkx3YlJiVzg4THJ6VF9fWjFyTnZPVGJObUZkVEhJZzdFdzMxd1JfYkRhTWQ2S2Z3T1pUTHJjeGotQjFOc0xCZlJjUUMxZllVV3J1aDF6NENwSUZiUnBEbVdNTE5raHBmc19Gams3cmtPMUdQeEFzRXRSdFNz?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxQWWgwRmxaQm4tRHVtY1FnUElyZFZNTk15dG05S1hlWmo5aTZZVUZSRHBjb0lIS0FBZktDZXRoUTEwZkllVUd2Rzl3SFU2Y2poeFM4cUNPWmxXVmc5ZHRYSHNpUzRDSUt1TWRxa2xwTlJyMlRYTUN0ZU02SkhoRzNlVWVQVkRQT0FTcDBzZnZlUXlMYmxESWhIbkVIODRZU3Q4NUtYMmNfaVd1VGVOaTA3LWxtYnJGNV9pVGc?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxOamM0M051dndpNkFXREREWHBBdTF2a1RHSGotakFUQlpxNFhhRXRzOTBtdVZfXzBLMDgxdGdqNXZycnhKNzA1R1p0RzEyS212Y1poRTFUeHN5TmlTUmdyMFdza2FzQTVtSjVVTWt0TmJlc2I0ZmZ2MU5halRYbTZHbVVQazRpZndCelRkbkc4NlA4QlVlalNWLQ?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxNX2ZQczZGWkZfbjNvak9BdndhRFE4UzRCNlU2ZGpub3NkRDR2YTdVYjVjVTh5Z0Z0RjRUZFFjV1RmRkxySjRoWnV3VUh5VnYtNlJ1ZW94NmVsaHVHeUN1WTNHV3RCODJqbXFYM2VSWWNTYTRrQWJkN2lkcEVLTWlmNFRiV2J1TjNmUEIzbGhBVUlwSmdaa0Jz?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
