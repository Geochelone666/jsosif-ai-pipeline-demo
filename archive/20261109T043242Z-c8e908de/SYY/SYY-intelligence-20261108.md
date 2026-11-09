# SYY Intelligence Report

- ticker: **SYY**
- Report as_of: **2026-11-08**
- Market data as_of: **2026-11-06**
- Quant sources: https://finance.yahoo.com/quote/SYY/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/SYY/key-statistics/
- AI analysis snapshot as_of: **2026-11-08**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-09T04:39:11.224354+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 21, 'rule': 7, 'ai': 11, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **11** exact headline/source/date matches; prior report **20261108T041758Z-43fb2458/SYY** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 21 unique headlines; 12 named publishers; 0 exact duplicates; 21 HTTPS source links; largest publisher share 19.05%; oldest publication 2026-11-02

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 76.8600 |
| Return 1D (%) | 2.1531 |
| Return 1W (%) | -7.2859 |
| Return 1M (%) | -0.7618 |
| Return YTD (%) | 7.3246 |
| Return 1Y (%) | 8.4727 |
| Annualized volatility (%) | 29.2875 |
| Beta vs SPY | 0.2164 |
| Max drawdown (%) | -23.9798 |
| Sharpe (rf=0) | 0.4289 |
| Downside deviation (rf=0, %) | 22.3565 |
| Sortino (rf=0) | 0.5619 |
| Historical VaR 95% (1D, %) | 2.1606 |
| Historical ES 95% (1D, %) | 4.3236 |
| Correlation vs SPY | 0.1001 |
| Tracking error vs SPY (%) | 31.0146 |
| P/E (trailing) | 20.44 |
| P/B | 9.35 |
| EV/EBITDA | 11.08 |
| Revenue growth (%) | 2.80 |
| Forward P/E (estimate) | 14.27 |
| Gross margin (%) | 18.54 |
| Operating margin (%) | 3.96 |
| Return on equity (%) | 58.74 |
| Free cash flow yield (%) | 6.36 |
| MA50 | 79.6278 |
| Close vs MA50 (%) | -3.4759 |
| MA200 | 79.5353 |
| Close vs MA200 (%) | -3.3636 |
| RSI (14, Wilder) | 42.4996 |
| MACD (12,26) | -0.6826 |
| MACD signal (9) | 0.0876 |
| MACD histogram | -0.7702 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'SYY': 277, 'SPY': 277}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 76.8600 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 2.1531 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -7.2859 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -0.7618 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 7.3246 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 8.4727 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 29.2875 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 22.3565 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.5619 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.1606 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.3236 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.1001 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 31.0146 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.2164 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -23.9798 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.4289 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 14.2736 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 18.5430 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 3.9640 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 58.7360 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 6.3633 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 20.4415 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 42.4996 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.7702 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -3.4759 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -3.3636 -> Slightly below the moving-average trend level.

## TAILWINDS

### Sysco Is Almost Tasty Enough For An Upgrade (NYSE:SYY)
- Summary: Sysco Is Almost Tasty Enough For An Upgrade (NYSE:SYY)
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxORnRsbGVmMkQwXzl1c0xMckV5VmVPZlZ1ZXdKaDVJYUlDNkdaelRESE5jRTJGUXRVZ1ZfbUVhYnBMZUNYaldHVzlSS0NqTmNPb05EbWV5Y0FTa2JDc3hFNjNKUWdrNUtEY2EyQVNrLVhCNUVHQmdQMnRaRzA3bDJFdUxjYTlFaW12QXREaQ?oc=5>

### Sysco Q1 Earnings Beat Estimates, Sales Miss Despite Volume Growth
- Summary: Sysco Q1 Earnings Beat Estimates, Sales Miss Despite Volume Growth
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxOSV9zYURQUWNqRWIyaXlibWROSFdYRWFuQXN2ZnltM29ST1BqR1N0MGt3VGRIOUMzVXA2VTVNUm1XS3JWaXVZWVRUVEVEMkVIeEl5bXhNQ1FuWTZ1S3hwcjEyRlBDNWM1UkxIZ211TGV0d1hqNDZocURlY2o2amtrZmltS0R6RWNIWmt1ZW9zOHpfdVlWRHRCVmJGZnNVUQ?oc=5>

## HEADWINDS

### Sysco under pressure on Jetro acquisition costs, FY sales guidance (SYY:NYSE)
- Summary: Sysco under pressure on Jetro acquisition costs, FY sales guidance (SYY:NYSE)
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxPR3dUQkEzV1RZOUJZbUhGOWwwN0VsLXdjdHVGYlNTNjZ2MTBaNlFleFJxa0l2TjlnLWQ5VTh4YXRfaWNGemo1NmJZWktzeGdYdU1INDZnWVhBVlAtcW5BTlp0Rnh5cXJwRTNtdElJTWNjRl9pdThEdG9NeHNmVXg5WjBOa1I3czZnQXVGb2pVOENJOEZoSGR0SlVmNVJJbVFTMFlpTQ?oc=5>

### Sysco (NYSE:SYY) misses Q3 CY2026 sales expectations, stock drops
- Summary: Sysco (NYSE:SYY) misses Q3 CY2026 sales expectations, stock drops
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizwFBVV95cUxNbHFWTGs5b3Vmbm50b2pIYUpYR3VKN05lTXNYM1FGcTYzTU1mUU5uTWl5VERFek91NDJaaVdYV1JCQjNuYlI1ak9QSWQ2ZTBncjExNVkxZ3JDZXhtNFIwWUhaVlZWTjNsTzJBUlZlcEJQMWh1NVlhRmNwS1RQcTU4OGNXRkxNNmdXZDQxcE9zaUE3eVdyRUk5TjRQRG5maFNiMHNZWTNVdEphMW96Y2RsdVE5QnpKRC1HOWRmbTYzQm1Md2RzdUlvZUtTVDFUcWM?oc=5>

### Why Sysco (SYY) stock is nosediving
- Summary: Sysco shares are falling sharply, indicating a negative market reaction.
- Date: 2026-11-03 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxOM0tscmdreEd1bkdmMzAxMGUzWjZPNUJFd0plTzdULUNqdzlIS1hqRDRJd2NMNkI0VHotNTJUZk9sLVpxTEc0cEt1WGNkWDZwd1duR25TakozYzV0VVhZaUEwTWpOMGpBRjlveXVFcFdNRDJpejFCTXpCejVKWV9YUHFLMlZxeFRWMHZ6ZFVTVFdseU05Qk9HbjZDNVRCNGVtOEtyVnNOc0xMdw?oc=5>

### Sysco Corp Stock (SYY) Moved Down by 9.80% on Nov 3: Key Drivers Unveiled
- Summary: Sysco shares fell 9.8% on Nov 3, driven by identified factors.
- Date: 2026-11-03 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxNX1FVV1Y1ZjNMRmtuTy1OLXFfVnFKaWQ5Tk1PbG9oTHBER1BHUERRY1hLdU93ZncwNy1vT1hWVjZDMnFKRHpjVVZOb0gxQi1lX1dOYWdCVnZ3VlJ0QXc5MGsxdjl3MUJ0UXdRVW9RNDRVVk9CcnhuV3poa1dQc1BBWUpuYks2ckJtWFE?oc=5>

### Sysco Q1 Earnings: Sales Miss Estimates, Full-Year EPS Outlook Unchanged
- Summary: Q1 sales below estimates; full-year EPS outlook unchanged.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMixgFBVV95cUxOWnZZd1JZRUQxZUYxcm02Z0lpY3FyQ1hCS2NQNW1YRXEzZGZvS3dFdTBVZXZ4c09NcTNRSHg2OHg0cGd4YzhNOWQ0Sy1HVkx3bWZrRVI0NFg0alRvU0U4c0t3Mkl2dmExTUVWYWp0eEk3bjRHZW1GZ29FZmUxWF9NVkNfTmxyMldhdHBSUHJUMlJQWUQwa2M2RzRfOW4xWjdwblNMRU1oM28xaVVVMGk1YUZpME9LVUFfaV84UFAtdlE2V2tZM2c?oc=5>

## CATALYSTS

### Sysco (SYY) Surpasses Q1 Earnings Estimates
- Summary: Sysco (SYY) Surpasses Q1 Earnings Estimates
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNclVQU3VmZFQwQzFsS0RqMzR4TTZhMEFybzJLVElTS2RJM0RmLUFJdDVsdjdtcmR2cEVkakUwcGIyVVc5UXpCQkRpQ01aeGF5dVJoVGFPdUU0NEV5RkphSzhYVTlQWUtxaGhkdENoVHpOdXNBX0RJSmtuWjBPM0hrNHhuSUdDWjB4YWcwbkhLd2RPMEthVFNyakM1TF8?oc=5>

### Sysco (SYY) Q1 Earnings: Taking a Look at Key Metrics Versus Estimates
- Summary: Sysco (SYY) Q1 Earnings: Taking a Look at Key Metrics Versus Estimates
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxOMUNySDBEYVJoejVEcV9qb2hVbldTcHd4aTFaYnlVdzcwZEJMY1dDUFlWRXVwRDNZQXBVUExwSndoOWk3MGJrZUxXbWNlVElDQklVSndFN0tRSUNhSWNSQWRMM014cU82ckQ4VVNlXzc1NmNpaTJkYnNfazY1ZVZ4UDJ4TjctX09HeVNxU2hkYUFVV012SmZkRg?oc=5>

### SYSCO ($SYY) Releases Q1 2027 Earnings
- Summary: SYSCO ($SYY) Releases Q1 2027 Earnings
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMigwFBVV95cUxOTEJoRXZ5UDk1U21Wa282cmIxb3NRMElQVHZxVW9aemtUUUhtQlR6d1BHbS13RHd0aHlsa3FHX2l0Q2tjRk5UMmhxMWRteGZLSllLb2lxX2luR183TS11NHFuZzV0M0ZxdVJLaV9Lb0FIaWdOUm1yU2ZTT18tVzFna0VEZw?oc=5>

### Sysco (SYY) Reports Strong Q1 Performance Amid Inflation and Sup
- Summary: Sysco reports robust Q1 earnings, indicating strong performance despite inflationary pressures.
- Date: 2026-11-03 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxNUnYxSWMtX19HdGZEYjVzcGxzRWRfcHp2dV8wVkFlMjBPLWpGcjNMUEFPb0d6Uk81WC1HaGx6cmtzM21sWm1uZFFKVEdvVHlNdnN0ZG8xXzhocnZBXzM5ZnJ3bjhaRHZQVmNXUjVIdEwxTTZBLUFPUDlFblI2cklMNks4aDkxY1J5UEpuOHNjU0p4Zk5lUGZaRjBLTVQyR2FhX0JCVDl0cWxtWlJHWjNYNDdTdk0wVUdnMnN1aG93?oc=5>

### Sysco (SYY) Reports 2.7% U.S. Local Growth and AI-Driven Cost Sa
- Summary: Announces 2.7% U.S. local growth and AI‑driven cost savings, reflecting recent earnings results.
- Date: 2026-11-03 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxNenpzN2NBeFNqX3BGUW5yNTFrQTltQngwT0psa19iWFJfUEZKMDJXd3VrLVNkZE1BdDJJOUMwVll3Z21JajlBR0R1eHVTc3FubWo4NDRGeFF3UHlRbkZQWUpUUG9ZZjJEXzFOME9JOHg3NkZpdEl4d0RMZXBWRm0yZG9hV1ByRXBMR0gwVEFjOVJ4NEQ3QUNUUjdmTktwZTY5NjJYdmJzaEluVXVGTWc?oc=5>

### What Sysco (SYY)'s CFO Appointment Means For Shareholders
- Summary: Sysco's new CFO appointment may influence shareholder value and company strategy.
- Date: 2026-11-07 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxQc2dpdWY4UUZ2aVhvYzRicWNBQjUwV1NDMmxJaG9rbFRPcmRuZExmQTVvTWZ1LXVTVFR4MElSckh1WTBHenhiZnBBRzNrSU84dUMyWk5DNmRiNzkzX2x6b2l5aWMtMnJQcHQ5NkVmZjZfdHpIRG0zRlVuRW80ZGd3eTU2SlN0ZXVHWmRwbmNQbGg2WjhHQmJJWWNEMF9jTG9Yd1JVbjkwQ3FQNTRNU3JacllLMnFQV3E3NllSRDV1MzhNamPSAcgBQVVfeXFMTm9qRTBYM3pYUjdDbDF3cUVCUTNmSTlaR2hzTFlMbjRFVjUwVWpFQzlCcHBxelRMM1Nod01VT0Y4Tk9QS09ESGJsaV9RSjlNSkswWlB5a29TSVFsYUpOYmJNM1pCTXJfZmlXSENseFBsd3Z0a1czdUlVQi1YWG9Ld2lNUmU4WmRCLVg0V0JZN1FzUTRRVGtqQVp4Wm1jR0doS3gwM0swLThYZ2k5SUF6SlRreFJjdzV6NUZ3RXM4dVNLQm1pVzVyc04?oc=5>

### A 9% to 11% target for adjusted earnings per share growth remains at Sysco.
- Summary: Sysco maintains a 9%-11% adjusted EPS growth target for the upcoming period.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxQUnMxaTltdWhGX3hFUkNfVXluN1dRSEtEWWM0Y3QzQjNfUlNvaHdpbG9CNVM5WVJhRlEySEM1M196NV9XSnRwU2ZHMU5CT0w0MXA1S3hyZmxGQlROUTJILTdpdWM5d0VqbDM5VWlCcXd0SUhOQWMyd1BBRi1ReEdieW9IQ09ibTBMLTZDWGNlMUhsMXIyb1FGTkVXcnRWZ0xDbGZ0ZktmNm5ldTBHSGNLV2I0aERMS0gwRTkw?oc=5>

### Can Sysco (NYSE:SYY) Sustain Its Dividend Amid Acquisition Debt?
- Summary: Questions Sysco’s ability to maintain dividends given its acquisition debt load.
- Date: 2026-11-04 | Impact: medium | Horizon: medium | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxPT3IzYTFMUHJOOHMtNzFUMUtCdDVWUXBMdkN0dmRmdG5Cc05JMkxrSnZMZk85NzNvYktfWkxHeHlwMkR2N3JWNWNVVWJ1bE5rSk5lbUthOWRKWFpHRlRVendCcGtlODRiWDZBRUVRdVI0MUxLcUItX1RaVlFPcHZWd3NYWS1HSFdNM0tSZnJ2WjJ0N3NkdU9HRmVmU3AzdlNjenpCaWtDUQ?oc=5>

### Sysco (SYY) Could Be 15% Undervalued Following Earnings And CFO Appointment
- Summary: Sysco may be undervalued; earnings outlook and new CFO appointment suggest potential upside.
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiywFBVV95cUxNV2VGQ0VabE5BeEFMUnlCR3ZqZ1VIekhfZFJLbjhoeWhKR09KYU0zX0ZNXzZSNzBvRkF0aHl6TWhNdE9JdTg5cVgyQ0thcXY1a0hNZWdEeWFFdW9uVmd2N2hJY2lNZXlYTVgwMFE2WE13UUQ2djc1N3F3ZkxWWGotZ01pYjF5ZGtqcWpxVmRwdjJxbFprTXBvWHhnMUdXQXE4Z2pldlo5aGpNMlNwTEdGTmE0d3hINXBnVl91MVpFVFhtbVFfcXFUUnZvZ9IB0AFBVV95cUxQcFhBZlhpUVVWZDZaa0xadTlLMExlMGl0czZKcUh5T2dnQ0dPUElIMTFFV2x0OWF2bktBTUZ5elYwNC1OYUhGT2JIMHR0OW0zMGhUakkyWFA5aUdWQXVCd2tfQnZYUVZXendfM2VsaTk1X09UX0pONnJoLXVrbVhtMkhvT2RTdlVHS1dPakFjVE1LZDNHSmdsYWVrNHVyV3RlMG04NURFaVVJSGZPeld1WjNvX3ItZFhGZUYtcVNRNlNZUVNtSWdHYkwzc1ZpenNr?oc=5>

### Sysco Corporation (SYY) Stock Forecasts
- Summary: Analysts predict future stock performance for Sysco.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxPR0ROZ1BrMndnS0c2RHZkLU1meWF1SV9xVDJ4X3Vjc2g5cUJBLThqb3l4ZmtsdTBsd0FLeFNkazM3ODhjVy1ac3N0UXB3SUZtRFlxTS1ZaElHXzQ2bkx4OGVvVk12QmpSV0w1OUt2VDZaaG90MjE0TlF4WG85WmxzZEg1SFdSNHprVG5zMw?oc=5>

## RISKS

### Sysco Investigation Notice: SueWallSt Notifies Investors of Pending Investigation Into Sysco (SYY)
- Summary: Investigation notice signals potential legal scrutiny for Sysco.
- Date: 2026-11-04 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi5gFBVV95cUxQM1lEVzUzcFd2UXFzZVhkcEZ3U3FMXzgzN0pFcjdxempod3J1TkYwd0UzTXlWaUs3SGUwYWNrZFJhSEEtcXJYMlhqbEdzenBkTFktRHVZVEhETEFjVGUtZUlzR2V1VWktaE15d3pCa1JGazhXb0tOXzBrbXJuemRDTW1YYlJ5Sjc2bWFQaXllZzNKekNNaHgyUlJqUDIzY2ItVm5zTjVkZGx2S21vSWZuR1JfUFRYdVY5ZVFrS1c5S3dTT01mMnNuSkpLV0pHNXNZeVBIUjV4WWFxT1lsQkZTYVR0NE1kQQ?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **SYY** | **20.44** | **9.35** | **11.08** | **2.80** | **37,835,931,648.00 USD** | **8.47** |
| USFD | 29.80 | 5.28 | 14.81 | 2.10 | 22,901,170,176.00 USD | 49.40 |
| PFGC | 42.83 | 3.32 | 14.08 | 5.50 | 16,961,837,056.00 USD | 13.19 |
| CHEF | 44.54 | 6.17 | N/A | 11.20 | 4,510,144,512.00 USD | 63.01 |

Peers fetched as_of: 2026-11-08; SYY reuses existing data (market data as_of: 2026-11-06); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-03
- Next expected earnings: 2027-02-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-08

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-04
- Revenue (latest available single quarter): 21,744,000,000.00 USD; period 2026-06-28/2026-09-26; fiscal year/reporting period 2027/Q1
- Net income (latest available single quarter): 526,000,000.00 USD; period 2026-06-28/2026-09-26; fiscal year/reporting period 2027/Q1
- SEC link: https://www.sec.gov/Archives/edgar/data/96021/000009602126000050/syy-20260926.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMijAFBVV95cUxORnRsbGVmMkQwXzl1c0xMckV5VmVPZlZ1ZXdKaDVJYUlDNkdaelRESE5jRTJGUXRVZ1ZfbUVhYnBMZUNYaldHVzlSS0NqTmNPb05EbWV5Y0FTa2JDc3hFNjNKUWdrNUtEY2EyQVNrLVhCNUVHQmdQMnRaRzA3bDJFdUxjYTlFaW12QXREaQ?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxOSV9zYURQUWNqRWIyaXlibWROSFdYRWFuQXN2ZnltM29ST1BqR1N0MGt3VGRIOUMzVXA2VTVNUm1XS3JWaXVZWVRUVEVEMkVIeEl5bXhNQ1FuWTZ1S3hwcjEyRlBDNWM1UkxIZ211TGV0d1hqNDZocURlY2o2amtrZmltS0R6RWNIWmt1ZW9zOHpfdVlWRHRCVmJGZnNVUQ?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxPR3dUQkEzV1RZOUJZbUhGOWwwN0VsLXdjdHVGYlNTNjZ2MTBaNlFleFJxa0l2TjlnLWQ5VTh4YXRfaWNGemo1NmJZWktzeGdYdU1INDZnWVhBVlAtcW5BTlp0Rnh5cXJwRTNtdElJTWNjRl9pdThEdG9NeHNmVXg5WjBOa1I3czZnQXVGb2pVOENJOEZoSGR0SlVmNVJJbVFTMFlpTQ?oc=5
- https://news.google.com/rss/articles/CBMizwFBVV95cUxNbHFWTGs5b3Vmbm50b2pIYUpYR3VKN05lTXNYM1FGcTYzTU1mUU5uTWl5VERFek91NDJaaVdYV1JCQjNuYlI1ak9QSWQ2ZTBncjExNVkxZ3JDZXhtNFIwWUhaVlZWTjNsTzJBUlZlcEJQMWh1NVlhRmNwS1RQcTU4OGNXRkxNNmdXZDQxcE9zaUE3eVdyRUk5TjRQRG5maFNiMHNZWTNVdEphMW96Y2RsdVE5QnpKRC1HOWRmbTYzQm1Md2RzdUlvZUtTVDFUcWM?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxOM0tscmdreEd1bkdmMzAxMGUzWjZPNUJFd0plTzdULUNqdzlIS1hqRDRJd2NMNkI0VHotNTJUZk9sLVpxTEc0cEt1WGNkWDZwd1duR25TakozYzV0VVhZaUEwTWpOMGpBRjlveXVFcFdNRDJpejFCTXpCejVKWV9YUHFLMlZxeFRWMHZ6ZFVTVFdseU05Qk9HbjZDNVRCNGVtOEtyVnNOc0xMdw?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxNX1FVV1Y1ZjNMRmtuTy1OLXFfVnFKaWQ5Tk1PbG9oTHBER1BHUERRY1hLdU93ZncwNy1vT1hWVjZDMnFKRHpjVVZOb0gxQi1lX1dOYWdCVnZ3VlJ0QXc5MGsxdjl3MUJ0UXdRVW9RNDRVVk9CcnhuV3poa1dQc1BBWUpuYks2ckJtWFE?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxOWnZZd1JZRUQxZUYxcm02Z0lpY3FyQ1hCS2NQNW1YRXEzZGZvS3dFdTBVZXZ4c09NcTNRSHg2OHg0cGd4YzhNOWQ0Sy1HVkx3bWZrRVI0NFg0alRvU0U4c0t3Mkl2dmExTUVWYWp0eEk3bjRHZW1GZ29FZmUxWF9NVkNfTmxyMldhdHBSUHJUMlJQWUQwa2M2RzRfOW4xWjdwblNMRU1oM28xaVVVMGk1YUZpME9LVUFfaV84UFAtdlE2V2tZM2c?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNclVQU3VmZFQwQzFsS0RqMzR4TTZhMEFybzJLVElTS2RJM0RmLUFJdDVsdjdtcmR2cEVkakUwcGIyVVc5UXpCQkRpQ01aeGF5dVJoVGFPdUU0NEV5RkphSzhYVTlQWUtxaGhkdENoVHpOdXNBX0RJSmtuWjBPM0hrNHhuSUdDWjB4YWcwbkhLd2RPMEthVFNyakM1TF8?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxOMUNySDBEYVJoejVEcV9qb2hVbldTcHd4aTFaYnlVdzcwZEJMY1dDUFlWRXVwRDNZQXBVUExwSndoOWk3MGJrZUxXbWNlVElDQklVSndFN0tRSUNhSWNSQWRMM014cU82ckQ4VVNlXzc1NmNpaTJkYnNfazY1ZVZ4UDJ4TjctX09HeVNxU2hkYUFVV012SmZkRg?oc=5
- https://news.google.com/rss/articles/CBMigwFBVV95cUxOTEJoRXZ5UDk1U21Wa282cmIxb3NRMElQVHZxVW9aemtUUUhtQlR6d1BHbS13RHd0aHlsa3FHX2l0Q2tjRk5UMmhxMWRteGZLSllLb2lxX2luR183TS11NHFuZzV0M0ZxdVJLaV9Lb0FIaWdOUm1yU2ZTT18tVzFna0VEZw?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxNUnYxSWMtX19HdGZEYjVzcGxzRWRfcHp2dV8wVkFlMjBPLWpGcjNMUEFPb0d6Uk81WC1HaGx6cmtzM21sWm1uZFFKVEdvVHlNdnN0ZG8xXzhocnZBXzM5ZnJ3bjhaRHZQVmNXUjVIdEwxTTZBLUFPUDlFblI2cklMNks4aDkxY1J5UEpuOHNjU0p4Zk5lUGZaRjBLTVQyR2FhX0JCVDl0cWxtWlJHWjNYNDdTdk0wVUdnMnN1aG93?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxNenpzN2NBeFNqX3BGUW5yNTFrQTltQngwT0psa19iWFJfUEZKMDJXd3VrLVNkZE1BdDJJOUMwVll3Z21JajlBR0R1eHVTc3FubWo4NDRGeFF3UHlRbkZQWUpUUG9ZZjJEXzFOME9JOHg3NkZpdEl4d0RMZXBWRm0yZG9hV1ByRXBMR0gwVEFjOVJ4NEQ3QUNUUjdmTktwZTY5NjJYdmJzaEluVXVGTWc?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxQc2dpdWY4UUZ2aVhvYzRicWNBQjUwV1NDMmxJaG9rbFRPcmRuZExmQTVvTWZ1LXVTVFR4MElSckh1WTBHenhiZnBBRzNrSU84dUMyWk5DNmRiNzkzX2x6b2l5aWMtMnJQcHQ5NkVmZjZfdHpIRG0zRlVuRW80ZGd3eTU2SlN0ZXVHWmRwbmNQbGg2WjhHQmJJWWNEMF9jTG9Yd1JVbjkwQ3FQNTRNU3JacllLMnFQV3E3NllSRDV1MzhNamPSAcgBQVVfeXFMTm9qRTBYM3pYUjdDbDF3cUVCUTNmSTlaR2hzTFlMbjRFVjUwVWpFQzlCcHBxelRMM1Nod01VT0Y4Tk9QS09ESGJsaV9RSjlNSkswWlB5a29TSVFsYUpOYmJNM1pCTXJfZmlXSENseFBsd3Z0a1czdUlVQi1YWG9Ld2lNUmU4WmRCLVg0V0JZN1FzUTRRVGtqQVp4Wm1jR0doS3gwM0swLThYZ2k5SUF6SlRreFJjdzV6NUZ3RXM4dVNLQm1pVzVyc04?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxQUnMxaTltdWhGX3hFUkNfVXluN1dRSEtEWWM0Y3QzQjNfUlNvaHdpbG9CNVM5WVJhRlEySEM1M196NV9XSnRwU2ZHMU5CT0w0MXA1S3hyZmxGQlROUTJILTdpdWM5d0VqbDM5VWlCcXd0SUhOQWMyd1BBRi1ReEdieW9IQ09ibTBMLTZDWGNlMUhsMXIyb1FGTkVXcnRWZ0xDbGZ0ZktmNm5ldTBHSGNLV2I0aERMS0gwRTkw?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxPT3IzYTFMUHJOOHMtNzFUMUtCdDVWUXBMdkN0dmRmdG5Cc05JMkxrSnZMZk85NzNvYktfWkxHeHlwMkR2N3JWNWNVVWJ1bE5rSk5lbUthOWRKWFpHRlRVendCcGtlODRiWDZBRUVRdVI0MUxLcUItX1RaVlFPcHZWd3NYWS1HSFdNM0tSZnJ2WjJ0N3NkdU9HRmVmU3AzdlNjenpCaWtDUQ?oc=5
- https://news.google.com/rss/articles/CBMiywFBVV95cUxNV2VGQ0VabE5BeEFMUnlCR3ZqZ1VIekhfZFJLbjhoeWhKR09KYU0zX0ZNXzZSNzBvRkF0aHl6TWhNdE9JdTg5cVgyQ0thcXY1a0hNZWdEeWFFdW9uVmd2N2hJY2lNZXlYTVgwMFE2WE13UUQ2djc1N3F3ZkxWWGotZ01pYjF5ZGtqcWpxVmRwdjJxbFprTXBvWHhnMUdXQXE4Z2pldlo5aGpNMlNwTEdGTmE0d3hINXBnVl91MVpFVFhtbVFfcXFUUnZvZ9IB0AFBVV95cUxQcFhBZlhpUVVWZDZaa0xadTlLMExlMGl0czZKcUh5T2dnQ0dPUElIMTFFV2x0OWF2bktBTUZ5elYwNC1OYUhGT2JIMHR0OW0zMGhUakkyWFA5aUdWQXVCd2tfQnZYUVZXendfM2VsaTk1X09UX0pONnJoLXVrbVhtMkhvT2RTdlVHS1dPakFjVE1LZDNHSmdsYWVrNHVyV3RlMG04NURFaVVJSGZPeld1WjNvX3ItZFhGZUYtcVNRNlNZUVNtSWdHYkwzc1ZpenNr?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxPR0ROZ1BrMndnS0c2RHZkLU1meWF1SV9xVDJ4X3Vjc2g5cUJBLThqb3l4ZmtsdTBsd0FLeFNkazM3ODhjVy1ac3N0UXB3SUZtRFlxTS1ZaElHXzQ2bkx4OGVvVk12QmpSV0w1OUt2VDZaaG90MjE0TlF4WG85WmxzZEg1SFdSNHprVG5zMw?oc=5
- https://news.google.com/rss/articles/CBMi5gFBVV95cUxQM1lEVzUzcFd2UXFzZVhkcEZ3U3FMXzgzN0pFcjdxempod3J1TkYwd0UzTXlWaUs3SGUwYWNrZFJhSEEtcXJYMlhqbEdzenBkTFktRHVZVEhETEFjVGUtZUlzR2V1VWktaE15d3pCa1JGazhXb0tOXzBrbXJuemRDTW1YYlJ5Sjc2bWFQaXllZzNKekNNaHgyUlJqUDIzY2ItVm5zTjVkZGx2S21vSWZuR1JfUFRYdVY5ZVFrS1c5S3dTT01mMnNuSkpLV0pHNXNZeVBIUjV4WWFxT1lsQkZTYVR0NE1kQQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
