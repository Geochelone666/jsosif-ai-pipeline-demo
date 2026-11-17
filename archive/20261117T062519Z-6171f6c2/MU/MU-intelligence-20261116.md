# MU Intelligence Report

- ticker: **MU**
- Report as_of: **2026-11-16**
- Market data as_of: **2026-11-16**
- Quant sources: https://finance.yahoo.com/quote/MU/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/MU/key-statistics/
- AI analysis snapshot as_of: **2026-11-16**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-17T06:35:09.622991+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 21, 'rule': 0, 'ai': 14, 'unknown': 0, 'irrelevant': 7})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **8** exact headline/source/date matches; prior report **20261116T043911Z-b81cfeb4/MU** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **4**; {'directional_claim_without_event_type': 1, 'low_uncalibrated_model_confidence': 1, 'positive_sentiment_in_headwinds': 1, 'short_term_price_move_in_structural_risks': 1}
- RSS source audit (metadata only, not article fact-checking): 21 unique headlines; 8 named publishers; 4 exact duplicates; 21 HTTPS source links; largest publisher share 38.1%; oldest publication 2026-11-13

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 719.0200 |
| Return 1D (%) | -7.6178 |
| Return 1W (%) | -1.9273 |
| Return 1M (%) | -18.1853 |
| Return YTD (%) | 152.1096 |
| Return 1Y (%) | 191.6326 |
| Annualized volatility (%) | 84.7342 |
| Beta vs SPY | 3.4414 |
| Max drawdown (%) | -45.8952 |
| Sharpe (rf=0) | 1.7181 |
| Downside deviation (rf=0, %) | 53.1323 |
| Sortino (rf=0) | 2.7400 |
| Historical VaR 95% (1D, %) | 7.3472 |
| Historical ES 95% (1D, %) | 10.3774 |
| Correlation vs SPY | 0.5591 |
| Tracking error vs SPY (%) | 77.8773 |
| P/E (trailing) | 9.67 |
| P/B | 5.88 |
| EV/EBITDA | 7.12 |
| Revenue growth (%) | 379.30 |
| Forward P/E (estimate) | 3.46 |
| Gross margin (%) | 80.72 |
| Operating margin (%) | 74.59 |
| Return on equity (%) | 88.26 |
| Free cash flow yield (%) | 3.58 |
| MA50 | 937.7412 |
| Close vs MA50 (%) | -23.3243 |
| MA200 | 766.9389 |
| Close vs MA200 (%) | -6.2481 |
| RSI (14, Wilder) | 38.0104 |
| MACD (12,26) | -57.1404 |
| MACD signal (9) | -54.3019 |
| MACD histogram | -2.8385 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'MU': 283, 'SPY': 283}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 719.0200 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -7.6178 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -1.9273 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -18.1853 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 152.1096 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 191.6326 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 84.7342 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 53.1323 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 2.7400 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 7.3472 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 10.3774 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5591 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 77.8773 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 3.4414 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -45.8952 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.7181 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 3.4608 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 80.7160 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 74.5860 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 88.2600 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 3.5820 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 9.6733 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 38.0104 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -2.8385 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -23.3243 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -6.2481 -> Clearly below the moving-average trend level.

## TAILWINDS

### Micron Stock (MU) Forecast – Why Are Analysts Bullish Despite Ongoing Volatility?
- Summary: Analysts remain optimistic about Micron’s future, citing strong demand and potential upside despite market volatility.
- Date: 2026-11-14 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxNV1J2alhFSlhSeFc5cG9KRWZ3R0hGd013SC1hc3lFcjRNVE8tdnpyc2lnS0FSUDJ6Qzc1SWhtUk5QZ2pkX3V0U0R1U3h3WWNOMENqUjJYdlkxSmdOYlVfcEluQ3phV1NUNjVCS3pHNkN1QWx0Nnp3ZFBVbXZmcmp0dEYxT1F5YXEtMlNmZmhzVWZxSmhYa010dUx3SHFPSVZxOEFma2xDa0JxZzdNeG9KVnljSW4?oc=5>

### Micron Technology (MU): Does a Low Earnings Multiple Understate Its AI Opportunity?
- Summary: Analysis questions if low earnings multiple undervalues Micron’s AI prospects.
- Date: 2026-11-14 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQRmFxb0NFNGNaVzBRdzExcGJ6a2Jremg4N1JFQk1lRHlQME04V3NnQ2ZocVlBR2RkeVpVWmwzQ3BaVmZSZjhrTFZZTndQSTJNR2hieUtXSzdaNUdraVFlU3ZUNllBRFpNTUtTZUFJeTg3TTdIWGtib0ZKZmROZGk1NHVSeERfLXZoOHNGNmY1TTlqZGpVWjl2Sg?oc=5>

### What Bernstein Sees in Micron (MU) After the Memory Selloff
- Summary: Bernstein analysis following Micron’s recent selloff, discussing potential recovery and valuation.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxPdUdkNlU1SG9TdmdNNU9IQW1tZl9lLVBFR1QzNUdUQVl4TzVxY3NfY3VLQW1BWmhpWDNlTjlTUC1rUTlXbEFXYUdmS0dMWHJkOUR0NTR1RXc0X3pGb1VPY0FJSjc5ZU5XbFRTMEJQQXFHaFpPMHZ3a2t0Vmo5c2w1a0FDc2JXZ3RqZlVid1pELVJ3T09OVERoOUhJUnQ?oc=5>

### Micron Technology (MU) Has More Than 75% Of 2027 Output Committed
- Summary: Micron secured over 75% of 2027 output, indicating strong demand.
- Date: 2026-11-14 | Impact: high | Horizon: long | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxNU1J4THBrTkV3M19WbEtScExWeGVyeUtlOGdEZHB5WE95NVo1dlBrMlp1b1JFXzBnQnd0Q3ZSaXFlNGdYWGJKYjhlaGMtS3NtOHEySFBqWVBSaVZFV0dRaG1qY19pZDgtc2N0R3pGd0R0VG1GdnlyX1RRajFrU1dpdTRNajE4amplYk5ubkF2WWV5WWc?oc=5>

### Is It Too Late to Buy Micron Stock?
- Summary: Questioning optimal timing for Micron investment.
- Date: 2026-11-14 | Impact: low | Horizon: short | Confidence: 0.5
- Sources: <https://news.google.com/rss/articles/CBMigwFBVV95cUxOTE1UT2VEX281LUxZd1BjS1ZTYU9wQmpvdnVqQjUyRk1MUjVXTm1tRjhkRFI3MDVjT3c5dFBYNDl2MU5zQnd0X0RqODdXbEJSNnA3NnpFdGFKRWVEcTBwMmcxOE4wREU1ajdGRHUwSjg2RFhFTVU2Z19XUTBTYlVGd3RuUQ?oc=5>

## HEADWINDS

### Micron Technology Inc Stock (MU) Opened Down by 5.60% on Nov 16: Facts Behind the Movement
- Summary: Micron’s stock opened 5.6% lower on Nov 16, driven by market factors.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiAFBVV95cUxQRjF2MVk3WHJETEkzNnVzLUhtb1JubUJMZGpucTYwdFVva1JBN1p2aVlsM3hMTXBpRnd2M1RaVUFTczNWTG9XWFhxU3g2dDdCLXdyVUpQdWlXaEpQZzd0R0M0cXBuTUN0SktmS3pLUUMxbVQ0MUhnUGtaYjRxbG0xaHdsSlhZU1pY?oc=5>

### What's Going On With Micron Technology Stock Monday?
- Summary: Investors question Micron’s recent stock decline, seeking explanations for the downturn.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxOOENST1M1UlNIcFJqOHhNUzdFWV9lT2dXNU5Xc2E2WEpRdHA3YWxQZHFxNHRGaU51c3prVFhzeHhOVEpjN2lJdjZXeVE1eGVBbG82ZkdWbGxRWkQteDZUcUF5aHliSzkzVW5lVW1rZEJIcXo4Zi1jR0hnd2Rid3l2MXRBcTJsOEdNdVRLQUNLSU5TWjRKdWhtRU1FcnpUWHZkdXVPcW1FOHI?oc=5>

### Why Micron Stock Keeps Going Down
- Summary: Analysis highlights factors contributing to Micron’s persistent share price decline.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxNcE9tT1dYdmpyZ3d5T0RiZm84UllQWHJOU1JKZEN0eGNBUjVYZlQ3RUdDQTRQaUJqWndzLWpURWs0bFZ1V2gxSFFrUVpBekZjSUFUY1Q2NGlDOFR5Tk5PNTU4ZzV6QWN5blA0aWFkM240c1AzOTBlMG5ieWxkVjFjU3Fna0M3ZzBVQ0NwRHlKZU9sVjJSeHZvLQ?oc=5>

### Should You Really Buy Micron Stock Right Now? Wall Street Has a Clear Answer for Investors.
- Summary: Wall Street advises caution, suggesting current conditions are unfavorable for buying Micron shares.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxPQWRhOEp3TjNfUXJlMDREcDhuTWlfSEhTblRTZGRFTzVQbC1YTGxpdWxFR1FYY2U4WVV6UFlwcGVrM0JfZXNGSHhrSmYxQWVNMV8ydFVDaHNXUmFTb25wWUtaS3ViWGZDUVU4OVN0MW1EbWFlN05Ga3EtQVgwaVhhaTFycEp6ZUlWYzhKaFRDZFI1eFJLb2hv?oc=5>

### Why Micron Stock Is a Screaming Buy Before Year-End
- Summary: Contrasting view claims Micron’s stock is undervalued and a strong buy before year-end.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxQd1NSV2x5ckRwbXRXdGVULTJldFZkWC1lNmlFZ1ZBZVNkRThxMklXQzNvV1NfTWd2M0FWeGpMMGxncDZVbWlvZDZQUjdVZk8xVEVzVE5tYkZJc3JSQnJvTmhNTDVpYWcxSTBTWmxCMUVzcjN4c0RqOXUwZHZtTXZldDhpQUE2VDlvMlFrbmh0YnA2SmZTZ2NDNTFn?oc=5>

### Micron Is Down 20% in a Month. What Will It Take to Get MU Stock Back to $1,000?
- Summary: Explores what actions or conditions could reverse Micron’s 20% monthly decline.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxQRG90Z3ZXaHhwb050bTI2cmlubU9XTVk0YUlrZ0lBLUxMUDQ5SlZ0UXBUVml4VGhLN21veURwaThVSzRZT2pibGVXMkNuVWxPTkV5VmNuQXB0WVJKVm9oSzg4RlJqRGFDejA1R1FHTlhYVF9zVVd2eXpjUGFyM01STFVKY0JwajdBRW1yc0YzLUpnQQ?oc=5>

## CATALYSTS

### DRAM Just Got More Expensive Than AI Memory. Here’s Why Micron Could Soar in 2027
- Summary: Higher DRAM prices could boost Micron’s long‑term earnings.
- Date: 2026-11-15 | Impact: high | Horizon: long | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxOQWFVdTN3S2tEZzRVbHFTckQwdU1CSkg4VmtkcV9GM2F6UWE5RENEYVlFTmh0M1BscUV1emV0eVNZbmhQdjYyV0JGUGF6OXAydldtakpxdUd1dFdFTndvMkVZY0pTcVNMVjZWVkRHN2R2VXZEVWl1OGdQOFFmandKOXBNeXc5emthSDFITnZ2RU9EN2N1T1Jzeg?oc=5>

### Micron MU Stock Returns Toward $700 Support as Memory-Sector Risks Return
- Summary: Micron’s stock moves toward $700 support amid memory‑sector risk resurgence.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxPRHdfdjdWVXV4WWxXNHdJZ2Z3S0IzNWJ3NUZNRVlMZktoV2xRVnRXSzdGeGdNWEVzaEFORkhkNzg1Q1pXNm4zTi1FYjBWdld1SXNjaFdmcnlqcTQ3SVE2NzE3S1BtbGUzSEhWQ0VHWTMyelR5cFRybm81cENRdnJ1Ulp4Z1ZRRTBfS2FfMGE3cTRFd1FuQ0l6aVhzYmNpenRWYy1TSEladjRYaEZsT3pmVkdSWmg4Zw?oc=5>

## RISKS

### Why Micron Stock Dove Today
- Summary: Micron shares fell today, indicating short-term downside pressure.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiekFVX3lxTE5ua2lEMDdzTnFrazZhY0hiTk5IVkhPSWJrSGRXUkhlbU8wRlJDcVJ6Wlk4Ui1fUWs0SUNyd1ZMSWlqTDB2M09QaFdtd3luZ0pYR2gwcko2eGJ0dEIzcmVzRTBFb2VCNVQ3d2tjMnJsLUFVR2hqMlo3cGRn?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **MU** | **9.67** | **5.88** | **7.12** | **379.30** | **813,515,931,648.00 USD** | **191.63** |
| WDC | 9.88 | 11.24 | 16.60 | 55.50 | 105,158,631,424.00 USD | 78.33 |
| STX | 26.17 | 33.20 | 19.75 | 61.00 | 114,550,988,800.00 USD | 94.39 |
| NXPI | 20.00 | 5.30 | 13.27 | 19.30 | 64,069,349,376.00 USD | 31.24 |

Peers fetched as_of: 2026-11-16; MU reuses existing data (market data as_of: 2026-11-16); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-09-30
- Next expected earnings: 2026-12-23 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-16

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

- https://news.google.com/rss/articles/CBMitAFBVV95cUxNV1J2alhFSlhSeFc5cG9KRWZ3R0hGd013SC1hc3lFcjRNVE8tdnpyc2lnS0FSUDJ6Qzc1SWhtUk5QZ2pkX3V0U0R1U3h3WWNOMENqUjJYdlkxSmdOYlVfcEluQ3phV1NUNjVCS3pHNkN1QWx0Nnp3ZFBVbXZmcmp0dEYxT1F5YXEtMlNmZmhzVWZxSmhYa010dUx3SHFPSVZxOEFma2xDa0JxZzdNeG9KVnljSW4?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQRmFxb0NFNGNaVzBRdzExcGJ6a2Jremg4N1JFQk1lRHlQME04V3NnQ2ZocVlBR2RkeVpVWmwzQ3BaVmZSZjhrTFZZTndQSTJNR2hieUtXSzdaNUdraVFlU3ZUNllBRFpNTUtTZUFJeTg3TTdIWGtib0ZKZmROZGk1NHVSeERfLXZoOHNGNmY1TTlqZGpVWjl2Sg?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxPdUdkNlU1SG9TdmdNNU9IQW1tZl9lLVBFR1QzNUdUQVl4TzVxY3NfY3VLQW1BWmhpWDNlTjlTUC1rUTlXbEFXYUdmS0dMWHJkOUR0NTR1RXc0X3pGb1VPY0FJSjc5ZU5XbFRTMEJQQXFHaFpPMHZ3a2t0Vmo5c2w1a0FDc2JXZ3RqZlVid1pELVJ3T09OVERoOUhJUnQ?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxNU1J4THBrTkV3M19WbEtScExWeGVyeUtlOGdEZHB5WE95NVo1dlBrMlp1b1JFXzBnQnd0Q3ZSaXFlNGdYWGJKYjhlaGMtS3NtOHEySFBqWVBSaVZFV0dRaG1qY19pZDgtc2N0R3pGd0R0VG1GdnlyX1RRajFrU1dpdTRNajE4amplYk5ubkF2WWV5WWc?oc=5
- https://news.google.com/rss/articles/CBMigwFBVV95cUxOTE1UT2VEX281LUxZd1BjS1ZTYU9wQmpvdnVqQjUyRk1MUjVXTm1tRjhkRFI3MDVjT3c5dFBYNDl2MU5zQnd0X0RqODdXbEJSNnA3NnpFdGFKRWVEcTBwMmcxOE4wREU1ajdGRHUwSjg2RFhFTVU2Z19XUTBTYlVGd3RuUQ?oc=5
- https://news.google.com/rss/articles/CBMiiAFBVV95cUxQRjF2MVk3WHJETEkzNnVzLUhtb1JubUJMZGpucTYwdFVva1JBN1p2aVlsM3hMTXBpRnd2M1RaVUFTczNWTG9XWFhxU3g2dDdCLXdyVUpQdWlXaEpQZzd0R0M0cXBuTUN0SktmS3pLUUMxbVQ0MUhnUGtaYjRxbG0xaHdsSlhZU1pY?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxOOENST1M1UlNIcFJqOHhNUzdFWV9lT2dXNU5Xc2E2WEpRdHA3YWxQZHFxNHRGaU51c3prVFhzeHhOVEpjN2lJdjZXeVE1eGVBbG82ZkdWbGxRWkQteDZUcUF5aHliSzkzVW5lVW1rZEJIcXo4Zi1jR0hnd2Rid3l2MXRBcTJsOEdNdVRLQUNLSU5TWjRKdWhtRU1FcnpUWHZkdXVPcW1FOHI?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxNcE9tT1dYdmpyZ3d5T0RiZm84UllQWHJOU1JKZEN0eGNBUjVYZlQ3RUdDQTRQaUJqWndzLWpURWs0bFZ1V2gxSFFrUVpBekZjSUFUY1Q2NGlDOFR5Tk5PNTU4ZzV6QWN5blA0aWFkM240c1AzOTBlMG5ieWxkVjFjU3Fna0M3ZzBVQ0NwRHlKZU9sVjJSeHZvLQ?oc=5
- https://news.google.com/rss/articles/CBMiggFBVV95cUxNbDNBMXhZQXJyaUJfbWp4eFc1dmtSbklvMU1NbUlDdlZzRXVOd3RERUFhOTlyVXFNcDZlZVhWeFBxNEdrU3U4UWtWUUw3YnVwRDBjR0FsaXJGYVhmLWlNWlpoR3doRFY4bG4wSFFCT2w1V092YWljVktqckVoajZNZnB3?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxPQWRhOEp3TjNfUXJlMDREcDhuTWlfSEhTblRTZGRFTzVQbC1YTGxpdWxFR1FYY2U4WVV6UFlwcGVrM0JfZXNGSHhrSmYxQWVNMV8ydFVDaHNXUmFTb25wWUtaS3ViWGZDUVU4OVN0MW1EbWFlN05Ga3EtQVgwaVhhaTFycEp6ZUlWYzhKaFRDZFI1eFJLb2hv?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxNN2xuSWtLWEFOY0R2TFc4U0M0YjV0WUF6WUloTVNVTWlXNHYtNlRDUnJKelRVZ1JOc1hTTGV4Z2VWTWNQdHFvN1ZWcDlJQV91cTV4SEc0MHRsalVpV21jTXhrMmN5emw2Z3hFaGdDVEVCRk9jNGY3SXhYMjBqQ0p3eklfUC02WVFocGpqazE4NlZ1OG9QamtZ?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxQd1NSV2x5ckRwbXRXdGVULTJldFZkWC1lNmlFZ1ZBZVNkRThxMklXQzNvV1NfTWd2M0FWeGpMMGxncDZVbWlvZDZQUjdVZk8xVEVzVE5tYkZJc3JSQnJvTmhNTDVpYWcxSTBTWmxCMUVzcjN4c0RqOXUwZHZtTXZldDhpQUE2VDlvMlFrbmh0YnA2SmZTZ2NDNTFn?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxPM3hpcF8waGhWQUV0WGRKUnBMdzRnb0hydEItT3ZTMGhlUDB2UG1iUHhFWVZMX0k4VnZXdGJpYXJiREpmcS1RbHdaVXJUMEJ6QzJxb1lsdWgteF9ZeDc0X3hHWHJrZlNPYTZBMUo2RzQ4d2pDc3NTdmxUREdOMi1nd2pZMDVWZTlicjVHb3RhTnlGclN0MG9IZFNpUQ?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxQRG90Z3ZXaHhwb050bTI2cmlubU9XTVk0YUlrZ0lBLUxMUDQ5SlZ0UXBUVml4VGhLN21veURwaThVSzRZT2pibGVXMkNuVWxPTkV5VmNuQXB0WVJKVm9oSzg4RlJqRGFDejA1R1FHTlhYVF9zVVd2eXpjUGFyM01STFVKY0JwajdBRW1yc0YzLUpnQQ?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxNelVwdm5oMDVMRW1lazFacTZYZXpVTHNKQXNQbjBoREsyUkpBVHVDbnJWM2dHTXdYQTZmVG9hUDR5NjV0c2FoWVFsaExLRXRBUWlGTUhBV0taQkRMbTQtZmpNbzR1TGxaUFNfWHgyM3NyMnU2VWxPTTRpRW0zczEwUm9vMm1Kc2ViMTZBM2MxeVZDQmxTQWR0T0ZRa3pFSmVVS29NczJHQTAzaVZSMUhITTZibjhNamFlQ2pr?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxOQWFVdTN3S2tEZzRVbHFTckQwdU1CSkg4VmtkcV9GM2F6UWE5RENEYVlFTmh0M1BscUV1emV0eVNZbmhQdjYyV0JGUGF6OXAydldtakpxdUd1dFdFTndvMkVZY0pTcVNMVjZWVkRHN2R2VXZEVWl1OGdQOFFmandKOXBNeXc5emthSDFITnZ2RU9EN2N1T1Jzeg?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxPRHdfdjdWVXV4WWxXNHdJZ2Z3S0IzNWJ3NUZNRVlMZktoV2xRVnRXSzdGeGdNWEVzaEFORkhkNzg1Q1pXNm4zTi1FYjBWdld1SXNjaFdmcnlqcTQ3SVE2NzE3S1BtbGUzSEhWQ0VHWTMyelR5cFRybm81cENRdnJ1Ulp4Z1ZRRTBfS2FfMGE3cTRFd1FuQ0l6aVhzYmNpenRWYy1TSEladjRYaEZsT3pmVkdSWmg4Zw?oc=5
- https://news.google.com/rss/articles/CBMiekFVX3lxTE5ua2lEMDdzTnFrazZhY0hiTk5IVkhPSWJrSGRXUkhlbU8wRlJDcVJ6Wlk4Ui1fUWs0SUNyd1ZMSWlqTDB2M09QaFdtd3luZ0pYR2gwcko2eGJ0dEIzcmVzRTBFb2VCNVQ3d2tjMnJsLUFVR2hqMlo3cGRn?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
