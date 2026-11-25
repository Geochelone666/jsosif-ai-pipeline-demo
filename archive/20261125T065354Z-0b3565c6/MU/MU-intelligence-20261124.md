# MU Intelligence Report

- ticker: **MU**
- Report as_of: **2026-11-24**
- Market data as_of: **2026-11-24**
- Quant sources: https://finance.yahoo.com/quote/MU/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/MU/key-statistics/
- AI analysis snapshot as_of: **2026-11-24**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-25T06:54:02.451877+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 0, 'ai': 17, 'unknown': 0, 'irrelevant': 7})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **1** exact headline/source/date matches; prior report **20261123T053847Z-45053549/MU** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'directional_claim_without_event_type': 1, 'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 13 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 33.33%; oldest publication 2026-11-20

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 629.7900 |
| Return 1D (%) | -11.0089 |
| Return 1W (%) | -11.5985 |
| Return 1M (%) | -28.2332 |
| Return YTD (%) | 120.8229 |
| Return 1Y (%) | 181.5635 |
| Annualized volatility (%) | 87.2872 |
| Beta vs SPY | 3.4343 |
| Max drawdown (%) | -50.9958 |
| Sharpe (rf=0) | 1.6233 |
| Downside deviation (rf=0, %) | 54.6143 |
| Sortino (rf=0) | 2.5944 |
| Historical VaR 95% (1D, %) | 7.6794 |
| Historical ES 95% (1D, %) | 10.8711 |
| Correlation vs SPY | 0.5884 |
| Tracking error vs SPY (%) | 79.4145 |
| P/E (trailing) | 8.47 |
| P/B | 5.15 |
| EV/EBITDA | 6.20 |
| Revenue growth (%) | 379.30 |
| Forward P/E (estimate) | 3.07 |
| Gross margin (%) | 80.72 |
| Operating margin (%) | 74.59 |
| Return on equity (%) | 88.26 |
| Free cash flow yield (%) | 4.09 |
| MA50 | 901.9156 |
| Close vs MA50 (%) | -30.1720 |
| MA200 | 775.1598 |
| Close vs MA200 (%) | -18.7535 |
| RSI (14, Wilder) | 37.3701 |
| MACD (12,26) | -68.3900 |
| MACD signal (9) | -62.2913 |
| MACD histogram | -6.0987 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'MU': 289, 'SPY': 289}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 629.7900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -11.0089 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -11.5985 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -28.2332 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 120.8229 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 181.5635 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 87.2872 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 54.6143 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 2.5944 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 7.6794 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 10.8711 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5884 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 79.4145 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 3.4343 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -50.9958 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.6233 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 3.0723 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 80.7160 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 74.5860 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 88.2600 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 4.0895 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 8.4729 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 37.3701 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -6.0987 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -30.1720 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -18.7535 -> Clearly below the moving-average trend level.

## TAILWINDS

### Micron (NASDAQ:MU) Stock Soars Nearly 20% as Nvidia’s Comeback Sparks AI Memory Rally
- Summary: Micron shares rise ~20% driven by AI memory demand linked to Nvidia’s resurgence.
- Date: 2026-11-23 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMidkFVX3lxTE1abkg4OTBxMlNfODF3b2VCdy1DOUJjczlRTGFtM0tmSTBQcXI3cklFYTYwaGtPN0ZEUUdfQU4wcGMtVzJ3c3RaM0VLWURBbzM3bTlxYWFCQjFzWXMxcUZVSms4X2Q5VWh2cVRHeUdiNV9NOV9paFE?oc=5>

### Micron Technology jumps 19% as tech stocks soar (MU:NASDAQ)
- Summary: Micron stock surges 19% amid broader tech rally.
- Date: 2026-11-23 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxQbUVwNW5fUTIyNTVENWRMNE02SzdtUlppSWVtVVJ3VkN3NlFEWjVtVl9pOUk1NjRaOUJtSWhIeU01Q1A5blBRalNsS0FGZ0VFbXRsVTNwRmRMUFlQZ2xONV9COG5GZm5CVElfNHotTWhmYjZaXzlSeVFITm1XZ3BMc1BiWXhJcUdoa2JERg?oc=5>

### Why Nvidia Rehiring Jensen Huang Is Making Micron Stock Skyrocket Today
- Summary: Nvidia’s hiring sparks positive sentiment for Micron’s stock.
- Date: 2026-11-23 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxOY0tpblAydUFpam44QV9Od1owS1M4T1BHTGlkYlU3LThpeWh3VTg3YWgyam5jY2pMbTFCUkNYWXlJZm5aRnJWc0h4RGNwTEtubGVHblI2NWtRSUJNS2dQeDI0MTJ4TFhwSDgxRjZRSEI1M1oxQjRaSTlZTXJITldkYS04VXFBYUhLTHFZb0JrU3ZmQzEyQkQ5SE9fMG9aUQ?oc=5>

### Why Micron Stock Is Up Today
- Summary: Micron shares rise, reflecting positive market sentiment.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxPaERiNmxSTXBoZkV2YXktd3BMTGJqeDFFUjMtc1dPZEMwcXpjOVlmeW5HQS1JMkwyM3JxV1pSRzVYUTdsTEwtaXJ6S2R6TVRQcGp4WFpsWnp3cjk5a1JVVmZTYWRuMTBhM0JNdGhJX0dtVjlSRTZ4V2pMb2JDWEhPR2x5TFlrek9aVkM2T3RKOG8?oc=5>

### Micron Technology, Inc. (MU) is Attracting Investor Attention: Here is What You Should Know
- Summary: Investor interest in Micron grows, boosting stock visibility.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxPOGJrYjVsOS1VejkyRzlkTUMzd0FMZXBpODRGWVN1Z1J3b2NSdVVmR0pKUnNWWlpoME9qLXlTcklVMC1tU3RFNk5lWnpRNndweWlBN0dHajNweXNVOUR3RWdTTHBDRXRFVVpETnR2XzdQdjNOQmU4WjVPUXB3ejdBOXhQUkw2bGNHQlpsV05QNlozSk5EV21takpmeU56MDBmamc?oc=5>

### MU: SEC Form DEFA14A filed by Micron Technology Inc.
- Summary: Micron files proxy statement, detailing governance matters.
- Date: 2026-11-24 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxNZTdZVUpfLTlEMVpNSndmcndXMWdUTFBnczBVSmd2Ml9qNmhXZ2lSUkVScUdrT0ljTzR3MGlhSzB1dERCMHNGMVhFaDdJdU95S1Mwc3VITEpFaUptYmtkZFpBdnRjUkxzYWh5QjhRMmQxcmwyR3B3SUc3YlhtNGFVbDIzVjdNeUFDV3ZCMmdHTFZtYldC?oc=5>

## HEADWINDS

### Micron Technology eyes Dell earnings and chip pricing: Can MU avoid deeper declines?
- Summary: Micron concerned about Dell earnings and chip pricing potentially worsening declines.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxPcDhJNnFtdDJhMUR3SXJ4VWdXaWFpSjVxZWlWNGZFZGRFNXVBUWpaTHRRT2FtdHZLa2V6WE1FekloNkw1VHRUVUNiamZrZ3J2LVZ5YTkyNmNOM2hjZzJLR0h6YUVqbzAyTXpVOEhzRmNmTWFzRE0zZ0pLQ0tnYXJOVkk5cHNZVjMwbmRjZDdGSG44WkFBQjZwdTJ3?oc=5>

## CATALYSTS

### Micron Is Down 32% in a Month. Can MU Stock Get Back to $1,000?
- Summary: Micron shares dropped 32% within a month, questioning future recovery prospects.
- Date: 2026-11-20 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxNQ3J3M1QxV2ZsMXItUkt2THBabi1fY0tra0tvZEpTSFl6RzItTjhxcndNSDFOZ3F2M1g0RzA5TFM3eTlvLUw5dXViaGlNU1Q5YnZ2RTR1elc3elNoMzZnWjNsY0FPWjZUakcwN0tQVzQ1Z1N2MUlvRDFZNVJhbGV0UVBsMDdISUpnZmJscG5zWHVzQQ?oc=5>

### Is Micron Technology Stock a Buy at $700?
- Summary: Analyst inquiry on Micron’s valuation at $700.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxPN25CbDJEbTJVNVlOd3Q1bEVndjlGcU85NE03RkVNLVJsZWNGZlNHYW16QjJKMW1NYkV3LU9IcWhDenphdmNCVWd5Q1pyVlYwdzRoa09XQjV6aExveWUyNHBIdlBFSmNOdmg1VGJZMnRrU092YkpGbUZKdzRMNW1MUjI1SVJJZXRvNzFsY2hVZFZlS1ZWOWVKbzQ1bXQ?oc=5>

### Micron: Pounding The Buy Table (Double Upgrade)
- Summary: Analyst upgrades Micron, boosting investor confidence and potentially raising the stock’s valuation.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxPNlFDejB5bGZ3YzVwRzRXTWZqbkJFUV9tbEcyeGhqTTBpZHhsRTNkX1hXQVhDNV96ZHp6WXVDZ1VZZ2JuTjZpRW44Vnc2RVVSd0FLcDJLcEFGLXBUV2c1cHBNYzNRR0dhQmViYnFCSzlSdno2WGJDTU5fNS1UTzIwSlJsUHA4TlE0eGQtYWJn?oc=5>

### Micron Stock Is Counting on a Buyback Bounce. Why It’s No Slam Dunk.
- Summary: Micron’s buyback program may not fully support the stock, limiting upside potential.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMib0FVX3lxTFBpZ3dObUpYUENEWWp5NG43UDdpMlI0ZVdPRUp5clkzTXg1UlhCYVFlem9wYzU2eEV2UENYSXRHZjhTb1kxRlI5MXpvRFJ0dTJ3eElCeU01OGJWRUFvdHM5LV9GZkJiWnlOYW9IMFIxRQ?oc=5>

### Micron’s stock falls as an analyst warns about a future supply glut
- Summary: Analyst cautions of a supply glut could depress Micron’s future earnings, dampening the stock.
- Date: 2026-11-24 | Impact: medium | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxOeFFlMktrdm9XRGNQNzR6SFdtNDFVZjJvZkV2TDFzczB1WGlXMUJTSDlmcjc4RUxTQm1VSFoxeGNzNHdzRTJlMUxEaDhfNWZ1bERkWmEtRTFadnhsSWYwQkhPY3hpUkN6TFNEdnlSTmU3T1VZU2FUX0VqMnJsc2RHNi15cFJXclRWeVF0SVFxeEdLUkpiZVk1VTZfYkVodFpfUjZvTzM1aFhLS1BWSkE?oc=5>

### This Analyst Just Downgraded Micron Stock. Here's Why.
- Summary: An analyst lowered Micron’s rating, citing concerns over earnings and market conditions.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNX0ZTNkdkQjV6ZTRHWkJodzIxQUFJUWxtR3JJd25HSk9CVTlJOEJDdHhwMjBIMU9pWTRsSTNGenZCYndFZ0JWcmNFME9DSERVd1ZpYTg4UWdmeXpNRm9OcG9rN3dJYW1NSzlwby1BVkVfYmNnRElpalpsM25hX2Q0end4bU0xMHo0QWZpbm54WU5OU2o1QVVjWldPcUo?oc=5>

### Why is Micron Technology stock sliding today?
- Summary: Investors question Micron’s recent stock decline amid market volatility and earnings expectations.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxNdFF5MWZQZnNNcXJGcVlRbjlKUUVxdDhGVkR5Q19xQUxVUmxFLUFISG9BWXRxWlFrTVZKeVVVMndwWWhTV0p2QjNuU0prWnllVnVSNGphN3R5WUZCR2NjWkRGWEdjSnZ4YkZFNmFEVTBqTXl6TkQtOU4yb2pYampiRlNuakhWU1J0MGZaeHdQTW5yUjEzY0plSVgxVHZXclI3V2ctWmFlZjNKQQ?oc=5>

### Analyst Cuts Micron Stock Price Target for 12 Months by Over 50%
- Summary: A rating agency slashed Micron’s 12‑month price target by more than half, reflecting weaker outlook.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxQUmRzeDlKNTZQWlFRTTBLSHRwY0lhTmxOZkRQcjFhdDBGc0pUREVfazFRVXVmS2h0M0p4OE91VUtnekVWS2psUmJXOU4zb2xieldrb2JXeTR3QnVGMnUtbVpDYTF5clBiSk9MREQ0aWRadU1nTk00STE0Z2xNR3hEUXpFV3F1RWNOZzY2VzRxTVlvbThXTDFFazdiT3pIWXA3a09J0gHfAUFVX3lxTE5sV2haLWtVaF8yR3VkT0tjYmZQcFZpb0lkRDN5cmVtNjV6UEtzT3JYUDNvVUF4MmRyc2dFajMybjZNOVFrM01uV0drUFloY0F5TEN1ZC1KVGdOOGktM3k5YlVndEZsU1NFV0NKQmpybktpRmZQVW96ck1leGxJcW80MnRCYmJnUmRmNUlrRTltVE9HZXdLVWJUYlRsYktOaXgwTmRtNFBvemlkSGhiTUwxQk9SZVZIZUpJSW1RUjQ2Qkt6VTNGQlhDNkpTOXA2Nk5UekhvT0pxT2JfQlh2Sm8?oc=5>

### Micron Stock: The Earnings Peak Is Nowhere In Sight (NASDAQ:MU)
- Summary: Micron’s earnings outlook remains weak, with analysts projecting no near-term peak. The company’s guidance signals continued pressure on profitability.
- Date: 2026-11-24 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxOWFlyeDJJeXg4SmMwaTdrdXZwc0tHTFFrLWRieFl2UnBnVkFFcFV2dHVncTE1dnRDa1VsSUVNRUo0cnpaTzRKb3FCcDBiS29mRlhnblk4d3NOVGt1UGxWQWw5Z3NmMjBUaHNSejVBWlI4dW5ZdDVPa3kyWFlNMXVqcW91dWRxdjlINm5CMzl6ckRpZ29wRHc?oc=5>

## RISKS

### Micron Just Hit a $700 Ceiling, Caught a Downgrade, and Is Down 10% Today. Is MU a Toxic Stock or a Prime Bargain?
- Summary: Micron’s stock fell 10% after a downgrade, hitting a $700 ceiling. The downgrade reflects concerns over valuation and future performance.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxNX2ZQczZGWkZfbjNvak9BdndhRFE4UzRCNlU2ZGpub3NkRDR2YTdVYjVjVTh5Z0Z0RjRUZFFjV1RmRkxySjRoWnV3VUh5VnYtNlJ1ZW94NmVsaHVHeUN1WTNHV3RCODJqbXFYM2VSWWNTYTRrQWJkN2lkcEVLTWlmNFRiV2J1TjNmUEIzbGhBVUlwSmdaa0Jz?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **MU** | **8.47** | **5.15** | **6.20** | **379.30** | **712,559,034,368.00 USD** | **181.56** |
| WDC | 9.64 | 10.96 | 16.18 | 55.50 | 102,545,866,752.00 USD | 81.85 |
| STX | 25.30 | 32.10 | 19.12 | 61.00 | 110,758,641,664.00 USD | 91.54 |
| NXPI | 18.84 | 4.99 | 12.58 | 19.30 | 60,341,485,568.00 USD | 27.18 |

Peers fetched as_of: 2026-11-24; MU reuses existing data (market data as_of: 2026-11-24); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-09-30
- Next expected earnings: 2026-12-17 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-24

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

- https://news.google.com/rss/articles/CBMidkFVX3lxTE1abkg4OTBxMlNfODF3b2VCdy1DOUJjczlRTGFtM0tmSTBQcXI3cklFYTYwaGtPN0ZEUUdfQU4wcGMtVzJ3c3RaM0VLWURBbzM3bTlxYWFCQjFzWXMxcUZVSms4X2Q5VWh2cVRHeUdiNV9NOV9paFE?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxQbUVwNW5fUTIyNTVENWRMNE02SzdtUlppSWVtVVJ3VkN3NlFEWjVtVl9pOUk1NjRaOUJtSWhIeU01Q1A5blBRalNsS0FGZ0VFbXRsVTNwRmRMUFlQZ2xONV9COG5GZm5CVElfNHotTWhmYjZaXzlSeVFITm1XZ3BMc1BiWXhJcUdoa2JERg?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxOY0tpblAydUFpam44QV9Od1owS1M4T1BHTGlkYlU3LThpeWh3VTg3YWgyam5jY2pMbTFCUkNYWXlJZm5aRnJWc0h4RGNwTEtubGVHblI2NWtRSUJNS2dQeDI0MTJ4TFhwSDgxRjZRSEI1M1oxQjRaSTlZTXJITldkYS04VXFBYUhLTHFZb0JrU3ZmQzEyQkQ5SE9fMG9aUQ?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxPSHNZUG5POXpXZWE1YXZoSXRneHFXM1FSTzctTDZtOGNlemJCZGFTcXotS1A0YXc3bEY2MmZockdvczZHYlpqRUNuWV9mVzdSU3oxUlJ3OHZ2bkhUN2pUeGs2czRldVRhZDFZZmZIVS1pQmtCRkVRc1VEU2hHWGd5c01OM2VGU3hRWjVCeFM0UmtFdHJid3N5M1N6dXFvUS1hZU93M0ZUTC1kWDF6SnVpYzVrZFY?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxPaERiNmxSTXBoZkV2YXktd3BMTGJqeDFFUjMtc1dPZEMwcXpjOVlmeW5HQS1JMkwyM3JxV1pSRzVYUTdsTEwtaXJ6S2R6TVRQcGp4WFpsWnp3cjk5a1JVVmZTYWRuMTBhM0JNdGhJX0dtVjlSRTZ4V2pMb2JDWEhPR2x5TFlrek9aVkM2T3RKOG8?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxPOGJrYjVsOS1VejkyRzlkTUMzd0FMZXBpODRGWVN1Z1J3b2NSdVVmR0pKUnNWWlpoME9qLXlTcklVMC1tU3RFNk5lWnpRNndweWlBN0dHajNweXNVOUR3RWdTTHBDRXRFVVpETnR2XzdQdjNOQmU4WjVPUXB3ejdBOXhQUkw2bGNHQlpsV05QNlozSk5EV21takpmeU56MDBmamc?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxNZTdZVUpfLTlEMVpNSndmcndXMWdUTFBnczBVSmd2Ml9qNmhXZ2lSUkVScUdrT0ljTzR3MGlhSzB1dERCMHNGMVhFaDdJdU95S1Mwc3VITEpFaUptYmtkZFpBdnRjUkxzYWh5QjhRMmQxcmwyR3B3SUc3YlhtNGFVbDIzVjdNeUFDV3ZCMmdHTFZtYldC?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxPcDhJNnFtdDJhMUR3SXJ4VWdXaWFpSjVxZWlWNGZFZGRFNXVBUWpaTHRRT2FtdHZLa2V6WE1FekloNkw1VHRUVUNiamZrZ3J2LVZ5YTkyNmNOM2hjZzJLR0h6YUVqbzAyTXpVOEhzRmNmTWFzRE0zZ0pLQ0tnYXJOVkk5cHNZVjMwbmRjZDdGSG44WkFBQjZwdTJ3?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxNQ3J3M1QxV2ZsMXItUkt2THBabi1fY0tra0tvZEpTSFl6RzItTjhxcndNSDFOZ3F2M1g0RzA5TFM3eTlvLUw5dXViaGlNU1Q5YnZ2RTR1elc3elNoMzZnWjNsY0FPWjZUakcwN0tQVzQ1Z1N2MUlvRDFZNVJhbGV0UVBsMDdISUpnZmJscG5zWHVzQQ?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxPN25CbDJEbTJVNVlOd3Q1bEVndjlGcU85NE03RkVNLVJsZWNGZlNHYW16QjJKMW1NYkV3LU9IcWhDenphdmNCVWd5Q1pyVlYwdzRoa09XQjV6aExveWUyNHBIdlBFSmNOdmg1VGJZMnRrU092YkpGbUZKdzRMNW1MUjI1SVJJZXRvNzFsY2hVZFZlS1ZWOWVKbzQ1bXQ?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxPNlFDejB5bGZ3YzVwRzRXTWZqbkJFUV9tbEcyeGhqTTBpZHhsRTNkX1hXQVhDNV96ZHp6WXVDZ1VZZ2JuTjZpRW44Vnc2RVVSd0FLcDJLcEFGLXBUV2c1cHBNYzNRR0dhQmViYnFCSzlSdno2WGJDTU5fNS1UTzIwSlJsUHA4TlE0eGQtYWJn?oc=5
- https://news.google.com/rss/articles/CBMib0FVX3lxTFBpZ3dObUpYUENEWWp5NG43UDdpMlI0ZVdPRUp5clkzTXg1UlhCYVFlem9wYzU2eEV2UENYSXRHZjhTb1kxRlI5MXpvRFJ0dTJ3eElCeU01OGJWRUFvdHM5LV9GZkJiWnlOYW9IMFIxRQ?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxOeFFlMktrdm9XRGNQNzR6SFdtNDFVZjJvZkV2TDFzczB1WGlXMUJTSDlmcjc4RUxTQm1VSFoxeGNzNHdzRTJlMUxEaDhfNWZ1bERkWmEtRTFadnhsSWYwQkhPY3hpUkN6TFNEdnlSTmU3T1VZU2FUX0VqMnJsc2RHNi15cFJXclRWeVF0SVFxeEdLUkpiZVk1VTZfYkVodFpfUjZvTzM1aFhLS1BWSkE?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNX0ZTNkdkQjV6ZTRHWkJodzIxQUFJUWxtR3JJd25HSk9CVTlJOEJDdHhwMjBIMU9pWTRsSTNGenZCYndFZ0JWcmNFME9DSERVd1ZpYTg4UWdmeXpNRm9OcG9rN3dJYW1NSzlwby1BVkVfYmNnRElpalpsM25hX2Q0end4bU0xMHo0QWZpbm54WU5OU2o1QVVjWldPcUo?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxNdFF5MWZQZnNNcXJGcVlRbjlKUUVxdDhGVkR5Q19xQUxVUmxFLUFISG9BWXRxWlFrTVZKeVVVMndwWWhTV0p2QjNuU0prWnllVnVSNGphN3R5WUZCR2NjWkRGWEdjSnZ4YkZFNmFEVTBqTXl6TkQtOU4yb2pYampiRlNuakhWU1J0MGZaeHdQTW5yUjEzY0plSVgxVHZXclI3V2ctWmFlZjNKQQ?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxQUmRzeDlKNTZQWlFRTTBLSHRwY0lhTmxOZkRQcjFhdDBGc0pUREVfazFRVXVmS2h0M0p4OE91VUtnekVWS2psUmJXOU4zb2xieldrb2JXeTR3QnVGMnUtbVpDYTF5clBiSk9MREQ0aWRadU1nTk00STE0Z2xNR3hEUXpFV3F1RWNOZzY2VzRxTVlvbThXTDFFazdiT3pIWXA3a09J0gHfAUFVX3lxTE5sV2haLWtVaF8yR3VkT0tjYmZQcFZpb0lkRDN5cmVtNjV6UEtzT3JYUDNvVUF4MmRyc2dFajMybjZNOVFrM01uV0drUFloY0F5TEN1ZC1KVGdOOGktM3k5YlVndEZsU1NFV0NKQmpybktpRmZQVW96ck1leGxJcW80MnRCYmJnUmRmNUlrRTltVE9HZXdLVWJUYlRsYktOaXgwTmRtNFBvemlkSGhiTUwxQk9SZVZIZUpJSW1RUjQ2Qkt6VTNGQlhDNkpTOXA2Nk5UekhvT0pxT2JfQlh2Sm8?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxOWFlyeDJJeXg4SmMwaTdrdXZwc0tHTFFrLWRieFl2UnBnVkFFcFV2dHVncTE1dnRDa1VsSUVNRUo0cnpaTzRKb3FCcDBiS29mRlhnblk4d3NOVGt1UGxWQWw5Z3NmMjBUaHNSejVBWlI4dW5ZdDVPa3kyWFlNMXVqcW91dWRxdjlINm5CMzl6ckRpZ29wRHc?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxNX2ZQczZGWkZfbjNvak9BdndhRFE4UzRCNlU2ZGpub3NkRDR2YTdVYjVjVTh5Z0Z0RjRUZFFjV1RmRkxySjRoWnV3VUh5VnYtNlJ1ZW94NmVsaHVHeUN1WTNHV3RCODJqbXFYM2VSWWNTYTRrQWJkN2lkcEVLTWlmNFRiV2J1TjNmUEIzbGhBVUlwSmdaa0Jz?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
