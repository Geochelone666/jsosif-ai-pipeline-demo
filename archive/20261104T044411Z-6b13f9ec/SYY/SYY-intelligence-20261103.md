# SYY Intelligence Report

- ticker: **SYY**
- Report as_of: **2026-11-03**
- Market data as_of: **2026-11-03**
- Quant sources: https://finance.yahoo.com/quote/SYY/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/SYY/key-statistics/
- AI analysis snapshot as_of: **2026-11-03**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-04T04:46:35.211902+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 13, 'ai': 5, 'unknown': 0, 'irrelevant': 7})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **7** exact headline/source/date matches; prior report **20261103T051441Z-8b1c85d8/SYY** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 12 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 28.0%; oldest publication 2026-10-27

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 74.1100 |
| Return 1D (%) | -9.3345 |
| Return 1W (%) | -9.9514 |
| Return 1M (%) | -4.3618 |
| Return YTD (%) | 3.4846 |
| Return 1Y (%) | 4.6060 |
| Annualized volatility (%) | 28.8793 |
| Beta vs SPY | 0.1412 |
| Max drawdown (%) | -23.9798 |
| Sharpe (rf=0) | 0.3047 |
| Downside deviation (rf=0, %) | 22.2497 |
| Sortino (rf=0) | 0.3955 |
| Historical VaR 95% (1D, %) | 2.1115 |
| Historical ES 95% (1D, %) | 4.3161 |
| Correlation vs SPY | 0.0626 |
| Tracking error vs SPY (%) | 30.8472 |
| P/E (trailing) | 22.32 |
| P/B | 13.30 |
| EV/EBITDA | 10.86 |
| Revenue growth (%) | 4.70 |
| Forward P/E (estimate) | 13.85 |
| Gross margin (%) | 18.50 |
| Operating margin (%) | 4.84 |
| Return on equity (%) | 77.69 |
| Free cash flow yield (%) | 5.25 |
| MA50 | 79.9954 |
| Close vs MA50 (%) | -7.3571 |
| MA200 | 79.5173 |
| Close vs MA200 (%) | -6.8002 |
| RSI (14, Wilder) | 31.0664 |
| MACD (12,26) | 0.1658 |
| MACD signal (9) | 0.6371 |
| MACD histogram | -0.4713 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'SYY': 274, 'SPY': 274}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 74.1100 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -9.3345 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -9.9514 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -4.3618 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 3.4846 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 4.6060 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 28.8793 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 22.2497 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.3955 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.1115 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.3161 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.0626 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 30.8472 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.1412 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -23.9798 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.3047 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 13.8450 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 18.4960 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 4.8450 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 77.6920 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 5.2502 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 22.3223 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 31.0664 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.4713 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -7.3571 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -6.8002 -> Clearly below the moving-average trend level.

## TAILWINDS

### Sysco Is Almost Tasty Enough For An Upgrade (NYSE:SYY)
- Summary: Sysco Is Almost Tasty Enough For An Upgrade (NYSE:SYY)
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxORnRsbGVmMkQwXzl1c0xMckV5VmVPZlZ1ZXdKaDVJYUlDNkdaelRESE5jRTJGUXRVZ1ZfbUVhYnBMZUNYaldHVzlSS0NqTmNPb05EbWV5Y0FTa2JDc3hFNjNKUWdrNUtEY2EyQVNrLVhCNUVHQmdQMnRaRzA3bDJFdUxjYTlFaW12QXREaQ?oc=5>

### Sysco Q1 Earnings Beat Estimates, Sales Miss Despite Volume Growth
- Summary: Sysco Q1 Earnings Beat Estimates, Sales Miss Despite Volume Growth
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxNOC0wTG1yVzFYYk9ocWZFR3dqMXNURWY0dlowSXprc24xLWxlOTBwRGdHeDllMlFxanc0MkZOdGdlRVQ2dUpYMjhVeFEwTmE4WTNLcVByQXFkZXVRaDltQUV3UTM5cDhoNVNwSnJDc2dtMG15UUVUSVJSdzhWaWVZaWNoZWhqOHQxbmNqcHVOSm1zZXVOS2w1c3I1d2NJaEx5ek9pYWh4Z3JlYkRTZDlfdV94aFBlVmluajNVZTRn?oc=5>

### How Investors May Respond To Sysco (SYY) Los Angeles Strike Ends
- Summary: Strike ends, likely boosting investor confidence and stock performance.
- Date: 2026-10-27 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxOQVFEU1JiUkJwQ0VIemhIdnNpOU9YYmhhbmp2aDAwdXJCeFpIQWZ5ckt5TExHc2EyMmFFLXF3cDJCTGwtWGk4NGEzSXpCQkRfZHh3RHZPSmRyRFloNHZabjJJc05GSTc0aGZLejY5blhSMmZvd2JRcTZkTGVOMTl6QjJOVU1JOXl4ZW1YSUc0YmZhNnlhOExyRFZaMEU?oc=5>

## HEADWINDS

### Sysco retreats 9% on revenue miss, softer sales guidance (SYY:NYSE)
- Summary: Sysco retreats 9% on revenue miss, softer sales guidance (SYY:NYSE)
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxQd2tEc21EVjE2VFZyNlFfUEpNcUhPMmFEeG9rdGVSQjhlVHFaandRWHRNWHNkdF9tdldrSnRVbjNmMGM1SnByZVQ1ZFBDWEJDN1lPaVlYNXdzREpmcEVsYTh5dFhNUkk2RVAxUU9oZ0JGWWszRDRkdFE3b2lQVkk4WGZ4S2lfcnQweDNpZnhsNmlmM2F4ZkpZ?oc=5>

### Sysco (NYSE:SYY) misses Q3 CY2026 sales expectations, stock drops
- Summary: Sysco (NYSE:SYY) misses Q3 CY2026 sales expectations, stock drops
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizwFBVV95cUxNbHFWTGs5b3Vmbm50b2pIYUpYR3VKN05lTXNYM1FGcTYzTU1mUU5uTWl5VERFek91NDJaaVdYV1JCQjNuYlI1ak9QSWQ2ZTBncjExNVkxZ3JDZXhtNFIwWUhaVlZWTjNsTzJBUlZlcEJQMWh1NVlhRmNwS1RQcTU4OGNXRkxNNmdXZDQxcE9zaUE3eVdyRUk5TjRQRG5maFNiMHNZWTNVdEphMW96Y2RsdVE5QnpKRC1HOWRmbTYzQm1Md2RzdUlvZUtTVDFUcWM?oc=5>

### Sysco under pressure on Jetro acquisition costs, FY sales guidance (SYY:NYSE)
- Summary: Sysco under pressure on Jetro acquisition costs, FY sales guidance (SYY:NYSE)
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxPR3dUQkEzV1RZOUJZbUhGOWwwN0VsLXdjdHVGYlNTNjZ2MTBaNlFleFJxa0l2TjlnLWQ5VTh4YXRfaWNGemo1NmJZWktzeGdYdU1INDZnWVhBVlAtcW5BTlp0Rnh5cXJwRTNtdElJTWNjRl9pdThEdG9NeHNmVXg5WjBOa1I3czZnQXVGb2pVOENJOEZoSGR0SlVmNVJJbVFTMFlpTQ?oc=5>

### Why Sysco (SYY) stock is nosediving
- Summary: Sysco shares sharply decline, indicating negative market sentiment.
- Date: 2026-11-03 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxNSzg2bkRLRDRvaGNfeHQzWEkzRU9yRU5GNVhxal91Y3VyVXhrYXVkSGpka0NseEwtMmJzRVZlakQyeHdQSkZnYnY4bmNHNEM5ZEF2RVVYV2l4VWVONDJMUFptSzRwbEExbExNVTh2N1UtbzFfZlluZGhsWkktOFh4Y1pneVpnelhSLXpNTFEwWGpuaS1GQnJraTB3?oc=5>

### Sysco Corp Stock (SYY) Moved Down by 9.80% on Nov 3: Key Drivers Unveiled
- Summary: Sysco shares fell 9.8% on Nov 3, driven by identified factors.
- Date: 2026-11-03 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxNX1FVV1Y1ZjNMRmtuTy1OLXFfVnFKaWQ5Tk1PbG9oTHBER1BHUERRY1hLdU93ZncwNy1vT1hWVjZDMnFKRHpjVVZOb0gxQi1lX1dOYWdCVnZ3VlJ0QXc5MGsxdjl3MUJ0UXdRVW9RNDRVVk9CcnhuV3poa1dQc1BBWUpuYks2ckJtWFE?oc=5>

### Sysco Q1 Earnings: Sales Miss Estimates, Full-Year EPS Outlook Unchanged
- Summary: Q1 sales below estimates; full-year EPS outlook unchanged.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMixgFBVV95cUxOWnZZd1JZRUQxZUYxcm02Z0lpY3FyQ1hCS2NQNW1YRXEzZGZvS3dFdTBVZXZ4c09NcTNRSHg2OHg0cGd4YzhNOWQ0Sy1HVkx3bWZrRVI0NFg0alRvU0U4c0t3Mkl2dmExTUVWYWp0eEk3bjRHZW1GZ29FZmUxWF9NVkNfTmxyMldhdHBSUHJUMlJQWUQwa2M2RzRfOW4xWjdwblNMRU1oM28xaVVVMGk1YUZpME9LVUFfaV84UFAtdlE2V2tZM2c?oc=5>

## CATALYSTS

### Sysco (SYY) Q1 Earnings: Taking a Look at Key Metrics Versus Estimates
- Summary: Sysco (SYY) Q1 Earnings: Taking a Look at Key Metrics Versus Estimates
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxOMUNySDBEYVJoejVEcV9qb2hVbldTcHd4aTFaYnlVdzcwZEJMY1dDUFlWRXVwRDNZQXBVUExwSndoOWk3MGJrZUxXbWNlVElDQklVSndFN0tRSUNhSWNSQWRMM014cU82ckQ4VVNlXzc1NmNpaTJkYnNfazY1ZVZ4UDJ4TjctX09HeVNxU2hkYUFVV012SmZkRg?oc=5>

### Sysco (SYY) Surpasses Q1 Earnings Estimates
- Summary: Sysco (SYY) Surpasses Q1 Earnings Estimates
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNclVQU3VmZFQwQzFsS0RqMzR4TTZhMEFybzJLVElTS2RJM0RmLUFJdDVsdjdtcmR2cEVkakUwcGIyVVc5UXpCQkRpQ01aeGF5dVJoVGFPdUU0NEV5RkphSzhYVTlQWUtxaGhkdENoVHpOdXNBX0RJSmtuWjBPM0hrNHhuSUdDWjB4YWcwbkhLd2RPMEthVFNyakM1TF8?oc=5>

### Sysco Corporation 2027 Q1 - Results - Earnings Call Presentation (NYSE:SYY) 2026-11-03
- Summary: Sysco Corporation 2027 Q1 - Results - Earnings Call Presentation (NYSE:SYY) 2026-11-03
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxPNDEwaW1uQ3ljLXlpNUx4RDBQTHY2TWxVcE5YeGNVN283dGUxX2thbEw4T3FoU1B4UEs2QzZTNlZGTGtSbGxIaV9DbmNyTUY1d1BROGNGb3ZxU2Z0aXNpdjNGZFJZSkF0aWNxdDFDcGc2cEw0OGFObWZoWTNIMTEyelFUOU5sQjJJV0NFUnlwSE8tNUhEMHQzYnNNRmViTFlFYjU0?oc=5>

### SYSCO ($SYY) Releases Q1 2027 Earnings
- Summary: SYSCO ($SYY) Releases Q1 2027 Earnings
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMigwFBVV95cUxOTEJoRXZ5UDk1U21Wa282cmIxb3NRMElQVHZxVW9aemtUUUhtQlR6d1BHbS13RHd0aHlsa3FHX2l0Q2tjRk5UMmhxMWRteGZLSllLb2lxX2luR183TS11NHFuZzV0M0ZxdVJLaV9Lb0FIaWdOUm1yU2ZTT18tVzFna0VEZw?oc=5>

### Sysco Q1 Earnings on the Horizon: Essential Insights for Investors
- Summary: Sysco Q1 Earnings on the Horizon: Essential Insights for Investors
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxPZHZpcnlsSjUwYXhGaE5vN3ZhckJfR05jSWg0YzR2cGVIYlNwTzBadzZPNHdjLXQ4V0Z6dHk1cmNXcXBzUDN3LWtIX3pMSVRqdVZtWDFjSzI5T1pCTlE5Q1V4M2ZLbFdlSFlsM01vYXEtaFB0X0VOdGstV1BmRkppV2Ruc3VhMVRKMG10SDlENHB1dmhvbW1NSnhIaXBqb0o3MGc?oc=5>

### Sysco Earnings Preview: High Debt Levels Overshadow Everything (NYSE:SYY)
- Summary: Sysco Earnings Preview: High Debt Levels Overshadow Everything (NYSE:SYY)
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxOMllybjY0dGtTSEJqNE5sVm84Z3U2OUtFZlkzZVhvTXdwelpPYkNiUzU4dF95VkltejhzcGpTSkZPQUZ4RDIzZERkcW1lV0ViSEZnbXJXQ3V1bXRWa1pmcV9sbm0tbVdUMmZoYkN6d1BXUHRrOWRMbHRqRkdBaUZ6SmJDQm43YUZrNmtPdmJ0NEdVQnNSbkVSNWRSbC1FcVhYSHVVRg?oc=5>

### Sysco earnings: what to look for from SYY
- Summary: Sysco earnings: what to look for from SYY
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxOSHMtaG4ySGl2MTNjVkVlWWIxdkd5QUY4bE13VFJsRkFZclBRSy1YY2tDdHVaNFo1UFFpRXdZdzRjeGp4SXhqTHJBTXZNZ2h2OXNpaXRwLTM3RDl3dlJ4dXFWNU45RTFSQmRsSlYzYmxLR0x1N3hvVThwZFNsTTE3anR2NVFDZHNIanJYWDNHZ0FxT2dXTUtOTFd0TDFMRXc?oc=5>

### Sysco Corporation $SYY Stock: VIRGINIA RETIREMENT SYSTEMS ET Al Lowers Position
- Summary: Sysco Corporation $SYY Stock: VIRGINIA RETIREMENT SYSTEMS ET Al Lowers Position
- Date: 2026-10-31 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1AFBVV95cUxNZk8yMk1mcVozeklUZzZpd1N6WE5VYnVjXzlEU3RKZFNvME9OU3RaampvSWFudXMwdDM0REFlNUZuUFdoUFRuQ3F1eTZIN2tSTld0WVZZaXRIdjlaQ0MxUU5hUERyR0s2aU5kemU2ZGJLNC1mLTdHZnBmWUtqZEpmV3ZnaVdxY0VqWjRheTR5dkh6STRUTW5hSUpnMUUyWUFEeVg0R1A5QTBIQjcwNlZvUkw5cUpnSWR0MHdnbkxRRGNEWEZnbVNjRWctMmRZVGlpU0NyVw?oc=5>

### Sysco (SYY) Earnings Expected to Grow: Should You Buy?
- Summary: Sysco forecasts higher earnings, suggesting potential upside for investors.
- Date: 2026-10-27 | Impact: medium | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxPQW1hNVdrVXZzS0w1OG5NYmhxN3BvdkFTak5UNm53cGdkRkc5a0NzZnIzaE11MGRaQnVlMURGQWJwSmZjNHVobU42V2UwSWxhSHRtb094RE1wLWJ1YmxmS2xJcDBjWHVvUlBqd3NnQ096Y1hlcFQzN2VKRkxMbGFCaTZBZzJFZGtBM05BRFIteTV6d3ZLYS1qMTNfX2FUUQ?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **SYY** | **22.32** | **13.30** | **10.86** | **4.70** | **36,455,743,488.00 USD** | **4.61** |
| USFD | 31.19 | 5.12 | 15.30 | 4.50 | 21,927,282,688.00 USD | 37.53 |
| PFGC | 42.14 | 3.07 | 13.46 | 7.30 | 15,159,063,552.00 USD | -1.50 |
| CHEF | 43.33 | 6.00 | 18.84 | 11.20 | 4,387,579,392.00 USD | 66.25 |

Peers fetched as_of: 2026-11-03; SYY reuses existing data (market data as_of: 2026-11-03); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-03
- Next expected earnings: N/A (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-03

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-K
- Filing date: 2026-08-21
- Revenue (latest available single quarter): 20,519,000,000.00 USD; period 2025-12-28/2026-03-28; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 340,000,000.00 USD; period 2025-12-28/2026-03-28; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/96021/000009602126000033/syy-20260627.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMijAFBVV95cUxORnRsbGVmMkQwXzl1c0xMckV5VmVPZlZ1ZXdKaDVJYUlDNkdaelRESE5jRTJGUXRVZ1ZfbUVhYnBMZUNYaldHVzlSS0NqTmNPb05EbWV5Y0FTa2JDc3hFNjNKUWdrNUtEY2EyQVNrLVhCNUVHQmdQMnRaRzA3bDJFdUxjYTlFaW12QXREaQ?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxNOC0wTG1yVzFYYk9ocWZFR3dqMXNURWY0dlowSXprc24xLWxlOTBwRGdHeDllMlFxanc0MkZOdGdlRVQ2dUpYMjhVeFEwTmE4WTNLcVByQXFkZXVRaDltQUV3UTM5cDhoNVNwSnJDc2dtMG15UUVUSVJSdzhWaWVZaWNoZWhqOHQxbmNqcHVOSm1zZXVOS2w1c3I1d2NJaEx5ek9pYWh4Z3JlYkRTZDlfdV94aFBlVmluajNVZTRn?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxOQVFEU1JiUkJwQ0VIemhIdnNpOU9YYmhhbmp2aDAwdXJCeFpIQWZ5ckt5TExHc2EyMmFFLXF3cDJCTGwtWGk4NGEzSXpCQkRfZHh3RHZPSmRyRFloNHZabjJJc05GSTc0aGZLejY5blhSMmZvd2JRcTZkTGVOMTl6QjJOVU1JOXl4ZW1YSUc0YmZhNnlhOExyRFZaMEU?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxQd2tEc21EVjE2VFZyNlFfUEpNcUhPMmFEeG9rdGVSQjhlVHFaandRWHRNWHNkdF9tdldrSnRVbjNmMGM1SnByZVQ1ZFBDWEJDN1lPaVlYNXdzREpmcEVsYTh5dFhNUkk2RVAxUU9oZ0JGWWszRDRkdFE3b2lQVkk4WGZ4S2lfcnQweDNpZnhsNmlmM2F4ZkpZ?oc=5
- https://news.google.com/rss/articles/CBMizwFBVV95cUxNbHFWTGs5b3Vmbm50b2pIYUpYR3VKN05lTXNYM1FGcTYzTU1mUU5uTWl5VERFek91NDJaaVdYV1JCQjNuYlI1ak9QSWQ2ZTBncjExNVkxZ3JDZXhtNFIwWUhaVlZWTjNsTzJBUlZlcEJQMWh1NVlhRmNwS1RQcTU4OGNXRkxNNmdXZDQxcE9zaUE3eVdyRUk5TjRQRG5maFNiMHNZWTNVdEphMW96Y2RsdVE5QnpKRC1HOWRmbTYzQm1Md2RzdUlvZUtTVDFUcWM?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxPR3dUQkEzV1RZOUJZbUhGOWwwN0VsLXdjdHVGYlNTNjZ2MTBaNlFleFJxa0l2TjlnLWQ5VTh4YXRfaWNGemo1NmJZWktzeGdYdU1INDZnWVhBVlAtcW5BTlp0Rnh5cXJwRTNtdElJTWNjRl9pdThEdG9NeHNmVXg5WjBOa1I3czZnQXVGb2pVOENJOEZoSGR0SlVmNVJJbVFTMFlpTQ?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxNSzg2bkRLRDRvaGNfeHQzWEkzRU9yRU5GNVhxal91Y3VyVXhrYXVkSGpka0NseEwtMmJzRVZlakQyeHdQSkZnYnY4bmNHNEM5ZEF2RVVYV2l4VWVONDJMUFptSzRwbEExbExNVTh2N1UtbzFfZlluZGhsWkktOFh4Y1pneVpnelhSLXpNTFEwWGpuaS1GQnJraTB3?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxNX1FVV1Y1ZjNMRmtuTy1OLXFfVnFKaWQ5Tk1PbG9oTHBER1BHUERRY1hLdU93ZncwNy1vT1hWVjZDMnFKRHpjVVZOb0gxQi1lX1dOYWdCVnZ3VlJ0QXc5MGsxdjl3MUJ0UXdRVW9RNDRVVk9CcnhuV3poa1dQc1BBWUpuYks2ckJtWFE?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxOWnZZd1JZRUQxZUYxcm02Z0lpY3FyQ1hCS2NQNW1YRXEzZGZvS3dFdTBVZXZ4c09NcTNRSHg2OHg0cGd4YzhNOWQ0Sy1HVkx3bWZrRVI0NFg0alRvU0U4c0t3Mkl2dmExTUVWYWp0eEk3bjRHZW1GZ29FZmUxWF9NVkNfTmxyMldhdHBSUHJUMlJQWUQwa2M2RzRfOW4xWjdwblNMRU1oM28xaVVVMGk1YUZpME9LVUFfaV84UFAtdlE2V2tZM2c?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxOMUNySDBEYVJoejVEcV9qb2hVbldTcHd4aTFaYnlVdzcwZEJMY1dDUFlWRXVwRDNZQXBVUExwSndoOWk3MGJrZUxXbWNlVElDQklVSndFN0tRSUNhSWNSQWRMM014cU82ckQ4VVNlXzc1NmNpaTJkYnNfazY1ZVZ4UDJ4TjctX09HeVNxU2hkYUFVV012SmZkRg?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNclVQU3VmZFQwQzFsS0RqMzR4TTZhMEFybzJLVElTS2RJM0RmLUFJdDVsdjdtcmR2cEVkakUwcGIyVVc5UXpCQkRpQ01aeGF5dVJoVGFPdUU0NEV5RkphSzhYVTlQWUtxaGhkdENoVHpOdXNBX0RJSmtuWjBPM0hrNHhuSUdDWjB4YWcwbkhLd2RPMEthVFNyakM1TF8?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxPNDEwaW1uQ3ljLXlpNUx4RDBQTHY2TWxVcE5YeGNVN283dGUxX2thbEw4T3FoU1B4UEs2QzZTNlZGTGtSbGxIaV9DbmNyTUY1d1BROGNGb3ZxU2Z0aXNpdjNGZFJZSkF0aWNxdDFDcGc2cEw0OGFObWZoWTNIMTEyelFUOU5sQjJJV0NFUnlwSE8tNUhEMHQzYnNNRmViTFlFYjU0?oc=5
- https://news.google.com/rss/articles/CBMigwFBVV95cUxOTEJoRXZ5UDk1U21Wa282cmIxb3NRMElQVHZxVW9aemtUUUhtQlR6d1BHbS13RHd0aHlsa3FHX2l0Q2tjRk5UMmhxMWRteGZLSllLb2lxX2luR183TS11NHFuZzV0M0ZxdVJLaV9Lb0FIaWdOUm1yU2ZTT18tVzFna0VEZw?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxPZHZpcnlsSjUwYXhGaE5vN3ZhckJfR05jSWg0YzR2cGVIYlNwTzBadzZPNHdjLXQ4V0Z6dHk1cmNXcXBzUDN3LWtIX3pMSVRqdVZtWDFjSzI5T1pCTlE5Q1V4M2ZLbFdlSFlsM01vYXEtaFB0X0VOdGstV1BmRkppV2Ruc3VhMVRKMG10SDlENHB1dmhvbW1NSnhIaXBqb0o3MGc?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxOMllybjY0dGtTSEJqNE5sVm84Z3U2OUtFZlkzZVhvTXdwelpPYkNiUzU4dF95VkltejhzcGpTSkZPQUZ4RDIzZERkcW1lV0ViSEZnbXJXQ3V1bXRWa1pmcV9sbm0tbVdUMmZoYkN6d1BXUHRrOWRMbHRqRkdBaUZ6SmJDQm43YUZrNmtPdmJ0NEdVQnNSbkVSNWRSbC1FcVhYSHVVRg?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxOSHMtaG4ySGl2MTNjVkVlWWIxdkd5QUY4bE13VFJsRkFZclBRSy1YY2tDdHVaNFo1UFFpRXdZdzRjeGp4SXhqTHJBTXZNZ2h2OXNpaXRwLTM3RDl3dlJ4dXFWNU45RTFSQmRsSlYzYmxLR0x1N3hvVThwZFNsTTE3anR2NVFDZHNIanJYWDNHZ0FxT2dXTUtOTFd0TDFMRXc?oc=5
- https://news.google.com/rss/articles/CBMi1AFBVV95cUxNZk8yMk1mcVozeklUZzZpd1N6WE5VYnVjXzlEU3RKZFNvME9OU3RaampvSWFudXMwdDM0REFlNUZuUFdoUFRuQ3F1eTZIN2tSTld0WVZZaXRIdjlaQ0MxUU5hUERyR0s2aU5kemU2ZGJLNC1mLTdHZnBmWUtqZEpmV3ZnaVdxY0VqWjRheTR5dkh6STRUTW5hSUpnMUUyWUFEeVg0R1A5QTBIQjcwNlZvUkw5cUpnSWR0MHdnbkxRRGNEWEZnbVNjRWctMmRZVGlpU0NyVw?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxPQW1hNVdrVXZzS0w1OG5NYmhxN3BvdkFTak5UNm53cGdkRkc5a0NzZnIzaE11MGRaQnVlMURGQWJwSmZjNHVobU42V2UwSWxhSHRtb094RE1wLWJ1YmxmS2xJcDBjWHVvUlBqd3NnQ096Y1hlcFQzN2VKRkxMbGFCaTZBZzJFZGtBM05BRFIteTV6d3ZLYS1qMTNfX2FUUQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
