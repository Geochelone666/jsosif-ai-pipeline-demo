# SPGI Intelligence Report

- ticker: **SPGI**
- Report as_of: **2026-11-02**
- Market data as_of: **2026-11-02**
- Quant sources: https://finance.yahoo.com/quote/SPGI/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/SPGI/key-statistics/
- AI analysis snapshot as_of: **2026-11-02**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-03T05:25:10.393898+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 23, 'rule': 8, 'ai': 9, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **8** exact headline/source/date matches; prior report **20261102T041627Z-c84a7052/SPGI** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 23 unique headlines; 12 named publishers; 2 exact duplicates; 23 HTTPS source links; largest publisher share 47.83%; oldest publication 2026-10-26

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 475.1700 |
| Return 1D (%) | 1.8476 |
| Return 1W (%) | 5.4410 |
| Return 1M (%) | 23.0150 |
| Return YTD (%) | -3.2268 |
| Return 1Y (%) | 4.0047 |
| Annualized volatility (%) | 30.7507 |
| Beta vs SPY | 0.3145 |
| Max drawdown (%) | -28.4781 |
| Sharpe (rf=0) | 0.2187 |
| Downside deviation (rf=0, %) | 22.9904 |
| Sortino (rf=0) | 0.2925 |
| Historical VaR 95% (1D, %) | 2.8767 |
| Historical ES 95% (1D, %) | 4.6345 |
| Correlation vs SPY | 0.1311 |
| Tracking error vs SPY (%) | 31.7269 |
| P/E (trailing) | 27.87 |
| P/B | 6.99 |
| EV/EBITDA | 18.37 |
| Revenue growth (%) | 6.80 |
| Forward P/E (estimate) | 23.54 |
| Gross margin (%) | 70.99 |
| Operating margin (%) | 48.21 |
| Return on equity (%) | 17.88 |
| Free cash flow yield (%) | 4.38 |
| MA50 | 422.3631 |
| Close vs MA50 (%) | 12.5027 |
| MA200 | 415.5583 |
| Close vs MA200 (%) | 14.3450 |
| RSI (14, Wilder) | 79.9499 |
| MACD (12,26) | 14.9102 |
| MACD signal (9) | 10.4675 |
| MACD histogram | 4.4427 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'SPGI': 273, 'SPY': 273}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 475.1700 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.8476 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 5.4410 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 23.0150 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -3.2268 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 4.0047 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 30.7507 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 22.9904 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.2925 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.8767 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.6345 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.1311 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 31.7269 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.3145 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -28.4781 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.2187 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 23.5430 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 70.9940 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 48.2060 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 17.8760 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 4.3839 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 27.8692 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 79.9499 -> Overbought momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 4.4427 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 12.5027 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 14.3450 -> Clearly above the moving-average trend level.

## TAILWINDS

### SPGI Stock Outlook Improves as S&P Global Raises 2026 Guidance
- Summary: SPGI Stock Outlook Improves as S&P Global Raises 2026 Guidance
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxONEZJNlgxVUhTazVVR3NHVTNfV0tKelhFSDlpNHluZGtpWmthMUtSNVBpVDIzMTBnNjF3Rm50ZzJidGlpQlZqcXRXOHBjQzZsUWZmNTNpVV9URFpiek1IaldPeGJBckJlU0Z5dG9JS1JUTnBSUnNFNkNNdzB0SjRKT2RnYkdjWF9fdG0weWtlV1poZ182Y0lZTWRKdXZKN1JIYy1z0gGoAUFVX3lxTE91UlpfZFIzNERRaWNtTGpOVnVMNWNfb3BHQVBwRGZpYzNlYkFBSjV1VUVaTlE5MGlDU1VTMkdEc0ZzTGZtaTVHTl9pOEF1anpDQUhHVkNmZWxTbG85YUsyQkxGUjhPTlZpMzRHc21XUzNiMTNZaS15VGZmdjBoelMxNzQ5UFJISk4xUXpMLW1OX25yOGxmS2lhWk9BSFBvSUozUTZpaXhTdg?oc=5>

### S&P Global (SPGI) Shares Rise After Q3 Beat and Strategic Review Announcement
- Summary: S&P Global (SPGI) Shares Rise After Q3 Beat and Strategic Review Announcement
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxOUWlZcTU2dkNSNE1yNU9QY3lQVDBtajVPWmVJNEM4R04tcU1kN2hzaFNkaThfWnROU2NyVmdXUXBTYUhQY0NEeU1YelB3Z1lzLUYtWk1oSnJQdmFUY1Q1WFF6OEpyaHVMX1FVYjRjd3liaFRwVVNIUk53ejFGdmZUN291Q1d2WldyQmRaNW0xTjlBMXhlOVBzeGJ4Z0RQb3hnWlZYLU5NakRhSG8ySW92cDhwTQ?oc=5>

### S&P Global (SPGI) Stock Looks Fully Priced Despite Strong Excess Returns
- Summary: Stock appears fully priced, indicating market confidence.
- Date: 2026-10-27 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxNZkJOcnNoTVNDRElhOU9KUkcxOTYtbVFYY0JDTXNXbGpIaW9kRmt3SVo0OS1kdHpCdUNydGdUMUpQYTlMaFZpUkZVTE11WW96c2Z1UVZGOGgwT1FxTldCUmxFQW44UE93czlNTnY3dmhMSkprVlEyR3RCdDBwWk96QnBuVFBuaE91QXljODVDUWdhcEdW?oc=5>

### S&P Global Inc. stock outperforms competitors on strong trading day
- Summary: SPGI shares rise, outperforming peers amid robust trading activity.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi3AFBVV95cUxNLUsyVGQ1YjFENU9NV3l6Umh0V0ZkYkN4Mk9QSk1mWnJRaTZiSnhVNVYyaVk4Q1Q1MXk1UVdzM1Fsbl9SRURGQ2RqS3ExQURSTFg0czFKM0h0LTVhamlMbGRJMWMwRjRlUG1BS2hucklyQjhZWUI4eERCZzFod0FWOVFqMEVvYmdBR3dQY29KRWlpZWxQMU9haW5zeTB6NU1NWFZ4dXR0MURSMWs2YUtpenZja0xmUHRsVFprX2UwdkpJSDJtLUNubFZxbU1tNjdEM2p1eEZlc2VUNDJW?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### S&P Global confirms strategic review of Capital IQ, data businesses; Q3 earnings beat (SPGI:NYSE)
- Summary: S&P Global confirms strategic review of Capital IQ, data businesses; Q3 earnings beat (SPGI:NYSE)
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxNZ2NVLUdkWW8yY0g0VmQzNlY5T0NDVjdGa2pqRnBWNllLUDBFVVNRUGxpd3c0X09ncThWVUF0Wk9ORUgyUTJzUjNHdnRCb0dvVE94VzJjd2NYYzBWX3kxWlRneVZoRUt2aUo0RkVoX2duNWlZdkRKd2tUOFVERU1EUHdWVnBPcDBraHB5aGRkRTd5TlRKTUYtdGVfWnRNZDdhcExPYk1VVHBiYmE4dHVZZWpNZGdaUWlPb2RtUA?oc=5>

### S&P Global Earnings Ahead: What Past Reactions Say About The Stock
- Summary: S&P Global Earnings Ahead: What Past Reactions Say About The Stock
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxNbXJWVmtSY3V4LW1XTk92RlFlc1FuN2JPMUpyVzRzcmNyUWl2aHIxS1BNSmNYdmVxbzJ3UjlUdDBHN21vOFBsX244ay1rSU93S3p4WlN6YkZpU0xmcU8wMWNSUGRmTUp6ZGZ4UnBId3czNmc1dzBJdUx3SV9fUlFxYl90cXhSME9CeUdtN2owN0ljZ0RDN3ZRQQ?oc=5>

### S&P Global Beats Q3 Earnings on Indices & Market Intelligence
- Summary: S&P Global Beats Q3 Earnings on Indices & Market Intelligence
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxNbFpONkFnZXFFTHdhU0dqbVFrQ3IxYkRwVFZGWmk5Y0tUb0VhWEJiWEpCbU5jN2xPRi0zeVVKT2J5MU9nclpKemlVeGJpTnVvSF9Uam9EV2ZhdFpJM005YXl3QU5Senphb0x1aFV1ZXhSaGVBOHd4NGN4dnhHYml4dkFwdlQ5a2p6V3YtaXVRbkttX1R2eEE?oc=5>

### S&P Global (SPGI) Q3 Earnings and Revenues Surpass Estimates
- Summary: S&P Global (SPGI) Q3 Earnings and Revenues Surpass Estimates
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxNYWZJa0ZHSEZ1RnJIWjFCa2ZLSXVEbUVlWVZkZGdMRHRUOEh4c193UXNWZ1l4WDBvQllhQXgzbmV0MnJ6QVpEWUFVT0ZCRUxZNkFhbG8wcHFoT1g1U0JhMEoyQVNBT0M3SzBSbS1rbTFodWpzZ3lzVU1udFRjdXY4WTlkbFE1ZmNmQ3hVb21MbC1iMlNp?oc=5>

### S&P Global (SPGI) Reports Q3 Earnings: What Key Metrics Have to Say
- Summary: S&P Global (SPGI) Reports Q3 Earnings: What Key Metrics Have to Say
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxQRWRhQVJacHhlWjNRUUZIR2pUVTQwQTZDREI2MTJxWF8yUVhRR3hGZzJ2V0EwVFNnUHlFanZBeGdMYU50WHBubTJ3SVJIWS1zX0JEX2Z5SERFMzVnVWdWalVLa2h1TGZ6SHRjUHVCWWxrSW1jLTJHb1BZUmlpRnc5VHRDdEtsNS1rT29KeTIzaXRrbTQ?oc=5>

### S&P Global (SPGI) to report earnings tomorrow: here is what to expect
- Summary: S&P Global (SPGI) to report earnings tomorrow: here is what to expect
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxQcnMyOV9rOGtfWFhyYjRPZkNzaHhMSDBsNnN3MWJsejZ4RnhaeU5LUHpOVzNwc2RERWdoUUtGYWlId0JPaEVaV0JITW1QcWdvYkt1a0VfWlFRYW16YWppLXVaNkcwMzRHdWx1QnJYdGE1TWw5R2lIVTQyVnVFQjVjRktXd1lUUVNRRnNyanRUaVR5NEp0d24yWGJB?oc=5>

### S&P Global: Three Times A Charm?
- Summary: Analysis of S&P Global's recent performance and potential future earnings.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMihwFBVV95cUxQd001cnZQZGhEV280cjlBb0ppRktWVTZDVUdvYjF1LXVmdUpsZ1V0eml4WTBmM0NZVDVUdXZLYkYtNjN1aktMc0tINmVfRkhJQ0t0X2s3TDJtMC1mN3prU0JpYWpnMGdxOUhXMVZxWm1RTkhSZDd3dnFMSGl5RHlDVWQ4Q2d4bk0?oc=5>

### S&P Global (SPGI) Stock Faces Q3 Earnings Puzzle After Guidance Lift
- Summary: SPGI’s guidance lift creates earnings uncertainty, raising questions about future profitability.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxNQ3d6ZEw2NXY4Y0JEQy1QazBTYjNuRjlTYWtBNFFodTJ6bjNXalRCdlZ0VkZfVTNuNmtzTndiOFd1U202Ul9zWW5KM3lBdG9wWXNmWEEwbVpGTURvMG1OeU4wRjZ4aG80WTM1SE9kbkxXWEZYVm5iT0Jrdms0QTRXTi1lcDd0ZUFHcFgtclg0MF9SSDZy?oc=5>

### SPGI Q3 deep dive: strategic review and AI drive business evolution
- Summary: SPGI's Q3 review highlights strategic initiatives and AI integration driving business evolution.
- Date: 2026-10-31 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxNdnhRYzhvMTJyQzE0a0NXVUN6aFlqczc4VzhSQzd0YVRiRlB6YmZMQWFIaDlSclB3T0FHSmlYTEhxRjctTTVGWldpQTdKTlV0NHk4Z01KajU4THVGSEVRZmE5SlhwMjhMLTdtWUNteW9uVHlKYVhrYlVVN1RndzRjTzVBcXZZMjBvdzNaZDk5SUFXX0k2Wm5n?oc=5>

### S&P Global Inc. (SPGI) Stock Forecasts
- Summary: Forecasts for S&P Global's stock performance based on earnings projections.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxNdVdISHpmUjBoYUhidWVHakF1ZDV5ZXhrM241eU4zTEFEbE9GR0xQRlFueUd5TjJEb0FEdjJVOUlNLU5TMTdrOGlrd0NKbkFGZXVMeU5vUENzcXlNMlhkdlRBR094RS1NcmczOXNqTnF5MHJaVE93VGwwT3BBOGdlUDBTNWJERFRfbVh1VQ?oc=5>

### S&P Global Reports Third Quarter Results; Announces Strategic Review for Capital IQ and Associated Data Businesses
- Summary: SPGI releases Q3 results and announces strategic review of Capital IQ and Associated Data.
- Date: 2026-10-27 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxPS1RxWGVmczhnMUdrRkJwMjM0dmMyZ3ZMZUhrSEtoekk2TEpuajhxSU52eU85TXJqQ2lTdmZlb1lFVVZPYjJsWWVab1RRWUduZDdaZFFQVkNWcDJpRDNNajNZbENnQmFtcmVnSG1zcjQ5TzBzZ0FzelpfUUhPZXdVaUxnd1ZfU3hRYi1qcWhSakZjanNPOTR5WUFVSQ?oc=5>

### S&P Global starts review for Capital IQ and related data business
- Summary: Internal review of Capital IQ and related data business.
- Date: 2026-10-27 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxNUTlPSHg5RWh2UEZuY2lDSmF1Z0Z3UkVscm42OHFKRjRlZ21MemFjNVF1ZmNwaVVHVDgwTW9hd29kRHhLMGpKQU9sV0xubG5JdGs5SEdqTkJiWkJwN1QwWmlCZnFNTHJtc2dNNjVyN2k5LTVrX0c1NDdpUlVxZXNJQ1VzREt1SUsxTGd5MVhfV3o2TWlHbkFQVVBQT0NQcVQ4UEI5Y0pyaThEYTZDOWU4SUxkU2w1Wjl2R1l2aTdBTExNLWN5azhz?oc=5>

### 5 must-read analyst questions from S&P Global’s Q3 earnings call
- Summary: Analysts posed key questions during SPGI’s Q3 earnings call, highlighting areas of focus for investors.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxNRkhSalE2SlJmTWZQZ3ZTLXVvY2ppdEhtbFRhS2ZaWXhvV1ljMU85MmVtY2ZKTzd2ZGIwS2xBZDJ4amtwVldoTmN4alhFeTE2c1FTd3NJZmJTVnZ0QmF2aUpBN3dzTlBrOVRoTm9Sc3E3TTByWEhRczFHTDdqVlBBSDF2STMtbmhDUTdPZUJWeDRJQkxXNHp1UTlB?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **SPGI** | **27.87** | **6.99** | **18.37** | **6.80** | **137,751,789,568.00 USD** | **4.00** |
| MCO | 30.87 | 26.70 | 23.07 | 0.80 | 87,250,034,688.00 USD | 6.27 |
| MSCI | 33.70 | -15.15 | 25.86 | 12.40 | 46,325,170,176.00 USD | 9.82 |
| FDS | 23.59 | 6.05 | 14.88 | 6.30 | 12,123,665,408.00 USD | 31.15 |

Peers fetched as_of: 2026-11-02; SPGI reuses existing data (market data as_of: 2026-11-02); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-27
- Next expected earnings: 2027-02-09 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-02

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-28
- Revenue (latest available single quarter): 1,567,000,000.00 USD; period 2018-01-01/2018-03-31; fiscal year/reporting period 2018/Q1
- Net income (latest available single quarter): 1,240,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/64040/000006404026000058/spgi-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiowFBVV95cUxONEZJNlgxVUhTazVVR3NHVTNfV0tKelhFSDlpNHluZGtpWmthMUtSNVBpVDIzMTBnNjF3Rm50ZzJidGlpQlZqcXRXOHBjQzZsUWZmNTNpVV9URFpiek1IaldPeGJBckJlU0Z5dG9JS1JUTnBSUnNFNkNNdzB0SjRKT2RnYkdjWF9fdG0weWtlV1poZ182Y0lZTWRKdXZKN1JIYy1z0gGoAUFVX3lxTE91UlpfZFIzNERRaWNtTGpOVnVMNWNfb3BHQVBwRGZpYzNlYkFBSjV1VUVaTlE5MGlDU1VTMkdEc0ZzTGZtaTVHTl9pOEF1anpDQUhHVkNmZWxTbG85YUsyQkxGUjhPTlZpMzRHc21XUzNiMTNZaS15VGZmdjBoelMxNzQ5UFJISk4xUXpMLW1OX25yOGxmS2lhWk9BSFBvSUozUTZpaXhTdg?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxOUWlZcTU2dkNSNE1yNU9QY3lQVDBtajVPWmVJNEM4R04tcU1kN2hzaFNkaThfWnROU2NyVmdXUXBTYUhQY0NEeU1YelB3Z1lzLUYtWk1oSnJQdmFUY1Q1WFF6OEpyaHVMX1FVYjRjd3liaFRwVVNIUk53ejFGdmZUN291Q1d2WldyQmRaNW0xTjlBMXhlOVBzeGJ4Z0RQb3hnWlZYLU5NakRhSG8ySW92cDhwTQ?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxNZkJOcnNoTVNDRElhOU9KUkcxOTYtbVFYY0JDTXNXbGpIaW9kRmt3SVo0OS1kdHpCdUNydGdUMUpQYTlMaFZpUkZVTE11WW96c2Z1UVZGOGgwT1FxTldCUmxFQW44UE93czlNTnY3dmhMSkprVlEyR3RCdDBwWk96QnBuVFBuaE91QXljODVDUWdhcEdW?oc=5
- https://news.google.com/rss/articles/CBMi3AFBVV95cUxNLUsyVGQ1YjFENU9NV3l6Umh0V0ZkYkN4Mk9QSk1mWnJRaTZiSnhVNVYyaVk4Q1Q1MXk1UVdzM1Fsbl9SRURGQ2RqS3ExQURSTFg0czFKM0h0LTVhamlMbGRJMWMwRjRlUG1BS2hucklyQjhZWUI4eERCZzFod0FWOVFqMEVvYmdBR3dQY29KRWlpZWxQMU9haW5zeTB6NU1NWFZ4dXR0MURSMWs2YUtpenZja0xmUHRsVFprX2UwdkpJSDJtLUNubFZxbU1tNjdEM2p1eEZlc2VUNDJW?oc=5
- https://news.google.com/rss/articles/CBMi3AFBVV95cUxNeHY0eGlnUThSMlJZcmNqSS1ndXQtaURUUHhpMWVyUVVfdmFrMm1xci1QUWNDenFEY3FEZGdpRXRyRVhQTlBMdmstdjZkMi1rekVXWEl1aXRMQnJFTXFVVEQ3ZGpsVFFhYWpMTDBfZXBuUWthTEt2WXNCQU9xU1R5LTcxdlNKUGJISzlLcVB3aTUyU3ZjMVhkVE9CN1FlSDdpUlFkVXNaZGEwNUc3MTAyNUJwVGhsRFRhOGc2YjQwOTBWMmhmWWUxYVdFWDhuZkZ0ZmNia0tZXzZtSkQt?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxNZ2NVLUdkWW8yY0g0VmQzNlY5T0NDVjdGa2pqRnBWNllLUDBFVVNRUGxpd3c0X09ncThWVUF0Wk9ORUgyUTJzUjNHdnRCb0dvVE94VzJjd2NYYzBWX3kxWlRneVZoRUt2aUo0RkVoX2duNWlZdkRKd2tUOFVERU1EUHdWVnBPcDBraHB5aGRkRTd5TlRKTUYtdGVfWnRNZDdhcExPYk1VVHBiYmE4dHVZZWpNZGdaUWlPb2RtUA?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxNbXJWVmtSY3V4LW1XTk92RlFlc1FuN2JPMUpyVzRzcmNyUWl2aHIxS1BNSmNYdmVxbzJ3UjlUdDBHN21vOFBsX244ay1rSU93S3p4WlN6YkZpU0xmcU8wMWNSUGRmTUp6ZGZ4UnBId3czNmc1dzBJdUx3SV9fUlFxYl90cXhSME9CeUdtN2owN0ljZ0RDN3ZRQQ?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxNbFpONkFnZXFFTHdhU0dqbVFrQ3IxYkRwVFZGWmk5Y0tUb0VhWEJiWEpCbU5jN2xPRi0zeVVKT2J5MU9nclpKemlVeGJpTnVvSF9Uam9EV2ZhdFpJM005YXl3QU5Senphb0x1aFV1ZXhSaGVBOHd4NGN4dnhHYml4dkFwdlQ5a2p6V3YtaXVRbkttX1R2eEE?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxNYWZJa0ZHSEZ1RnJIWjFCa2ZLSXVEbUVlWVZkZGdMRHRUOEh4c193UXNWZ1l4WDBvQllhQXgzbmV0MnJ6QVpEWUFVT0ZCRUxZNkFhbG8wcHFoT1g1U0JhMEoyQVNBT0M3SzBSbS1rbTFodWpzZ3lzVU1udFRjdXY4WTlkbFE1ZmNmQ3hVb21MbC1iMlNp?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxQRWRhQVJacHhlWjNRUUZIR2pUVTQwQTZDREI2MTJxWF8yUVhRR3hGZzJ2V0EwVFNnUHlFanZBeGdMYU50WHBubTJ3SVJIWS1zX0JEX2Z5SERFMzVnVWdWalVLa2h1TGZ6SHRjUHVCWWxrSW1jLTJHb1BZUmlpRnc5VHRDdEtsNS1rT29KeTIzaXRrbTQ?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxQcnMyOV9rOGtfWFhyYjRPZkNzaHhMSDBsNnN3MWJsejZ4RnhaeU5LUHpOVzNwc2RERWdoUUtGYWlId0JPaEVaV0JITW1QcWdvYkt1a0VfWlFRYW16YWppLXVaNkcwMzRHdWx1QnJYdGE1TWw5R2lIVTQyVnVFQjVjRktXd1lUUVNRRnNyanRUaVR5NEp0d24yWGJB?oc=5
- https://news.google.com/rss/articles/CBMihwFBVV95cUxQd001cnZQZGhEV280cjlBb0ppRktWVTZDVUdvYjF1LXVmdUpsZ1V0eml4WTBmM0NZVDVUdXZLYkYtNjN1aktMc0tINmVfRkhJQ0t0X2s3TDJtMC1mN3prU0JpYWpnMGdxOUhXMVZxWm1RTkhSZDd3dnFMSGl5RHlDVWQ4Q2d4bk0?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxNQ3d6ZEw2NXY4Y0JEQy1QazBTYjNuRjlTYWtBNFFodTJ6bjNXalRCdlZ0VkZfVTNuNmtzTndiOFd1U202Ul9zWW5KM3lBdG9wWXNmWEEwbVpGTURvMG1OeU4wRjZ4aG80WTM1SE9kbkxXWEZYVm5iT0Jrdms0QTRXTi1lcDd0ZUFHcFgtclg0MF9SSDZy?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxNdnhRYzhvMTJyQzE0a0NXVUN6aFlqczc4VzhSQzd0YVRiRlB6YmZMQWFIaDlSclB3T0FHSmlYTEhxRjctTTVGWldpQTdKTlV0NHk4Z01KajU4THVGSEVRZmE5SlhwMjhMLTdtWUNteW9uVHlKYVhrYlVVN1RndzRjTzVBcXZZMjBvdzNaZDk5SUFXX0k2Wm5n?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxNdVdISHpmUjBoYUhidWVHakF1ZDV5ZXhrM241eU4zTEFEbE9GR0xQRlFueUd5TjJEb0FEdjJVOUlNLU5TMTdrOGlrd0NKbkFGZXVMeU5vUENzcXlNMlhkdlRBR094RS1NcmczOXNqTnF5MHJaVE93VGwwT3BBOGdlUDBTNWJERFRfbVh1VQ?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxPS1RxWGVmczhnMUdrRkJwMjM0dmMyZ3ZMZUhrSEtoekk2TEpuajhxSU52eU85TXJqQ2lTdmZlb1lFVVZPYjJsWWVab1RRWUduZDdaZFFQVkNWcDJpRDNNajNZbENnQmFtcmVnSG1zcjQ5TzBzZ0FzelpfUUhPZXdVaUxnd1ZfU3hRYi1qcWhSakZjanNPOTR5WUFVSQ?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxNUTlPSHg5RWh2UEZuY2lDSmF1Z0Z3UkVscm42OHFKRjRlZ21MemFjNVF1ZmNwaVVHVDgwTW9hd29kRHhLMGpKQU9sV0xubG5JdGs5SEdqTkJiWkJwN1QwWmlCZnFNTHJtc2dNNjVyN2k5LTVrX0c1NDdpUlVxZXNJQ1VzREt1SUsxTGd5MVhfV3o2TWlHbkFQVVBQT0NQcVQ4UEI5Y0pyaThEYTZDOWU4SUxkU2w1Wjl2R1l2aTdBTExNLWN5azhz?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxNRkhSalE2SlJmTWZQZ3ZTLXVvY2ppdEhtbFRhS2ZaWXhvV1ljMU85MmVtY2ZKTzd2ZGIwS2xBZDJ4amtwVldoTmN4alhFeTE2c1FTd3NJZmJTVnZ0QmF2aUpBN3dzTlBrOVRoTm9Sc3E3TTByWEhRczFHTDdqVlBBSDF2STMtbmhDUTdPZUJWeDRJQkxXNHp1UTlB?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxPSHVJZ2VpRmtOMEEzdjE2OWJoaHhlUFQ4NENJNVloTkpiYUt0d3FoMGkxVTRORjNKZVR1M1I2SnpZcUUyLXlOZjFxTDRjQ1dNYzRxS1Vmd01OT1lqM2xYa1R6WGFfLVo5M2s4LTB4QWZBQ2l0LW1YZmhaYk1XUDdPLXkzZHBfeU5kaUtIUXYwR3NoalFfemFod1ZFR3U3cm1CRzJTS0QwNGotLThWcFl2ZnF5TXBxSGlnZTFocm1nRTNtWFk?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
