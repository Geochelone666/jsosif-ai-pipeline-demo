# TSM Intelligence Report

- ticker: **TSM**
- Report as_of: **2026-11-09**
- Market data as_of: **2026-11-09**
- Quant sources: https://finance.yahoo.com/quote/TSM/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/TSM/key-statistics/
- AI analysis snapshot as_of: **2026-11-09**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-10T05:52:16.672801+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 23, 'rule': 1, 'ai': 14, 'unknown': 0, 'irrelevant': 8})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **7** exact headline/source/date matches; prior report **20261109T043242Z-c8e908de/TSM** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'short_term_price_move_in_structural_risks': 1}
- RSS source audit (metadata only, not article fact-checking): 23 unique headlines; 13 named publishers; 2 exact duplicates; 23 HTTPS source links; largest publisher share 30.43%; oldest publication 2026-11-04

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 388.6200 |
| Return 1D (%) | 3.5105 |
| Return 1W (%) | -2.5111 |
| Return 1M (%) | -14.2706 |
| Return YTD (%) | 28.8873 |
| Return 1Y (%) | 37.0796 |
| Annualized volatility (%) | 41.6796 |
| Beta vs SPY | 2.1557 |
| Max drawdown (%) | -27.3158 |
| Sharpe (rf=0) | 0.8985 |
| Downside deviation (rf=0, %) | 28.7717 |
| Sortino (rf=0) | 1.3016 |
| Historical VaR 95% (1D, %) | 4.2435 |
| Historical ES 95% (1D, %) | 5.7594 |
| Correlation vs SPY | 0.7082 |
| Tracking error vs SPY (%) | 33.4128 |
| P/E (trailing) | 25.19 |
| P/B | 74.17 |
| EV/EBITDA | 3.58 |
| Revenue growth (%) | 50.90 |
| Forward P/E (estimate) | 16.62 |
| Gross margin (%) | 65.85 |
| Operating margin (%) | 58.66 |
| Return on equity (%) | 41.85 |
| Free cash flow yield (%) | N/A |
| MA50 | 430.8157 |
| Close vs MA50 (%) | -9.7944 |
| MA200 | 400.3110 |
| Close vs MA200 (%) | -2.9205 |
| RSI (14, Wilder) | 41.2619 |
| MACD (12,26) | -15.3515 |
| MACD signal (9) | -10.3653 |
| MACD histogram | -4.9862 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'TSM': 278, 'SPY': 278}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 388.6200 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 3.5105 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -2.5111 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -14.2706 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 28.8873 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 37.0796 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 41.6796 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 28.7717 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.3016 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.2435 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.7594 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.7082 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 33.4128 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 2.1557 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -27.3158 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.8985 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 16.6181 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 65.8460 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 58.6550 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 41.8550 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 25.1860 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 41.2619 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -4.9862 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -9.7944 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -2.9205 -> Slightly below the moving-average trend level.

## TAILWINDS

### TSMC Stocks Rise 4.68% as Taiwan Curbs Short Selling, Deploys Stabilization Fund
- Summary: TSMC Stocks Rise 4.68% as Taiwan Curbs Short Selling, Deploys Stabilization Fund
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1AFBVV95cUxQZXJkcmI1STJVajA1Z3JPVEpsdzVLOFNUb2k3NktqV3g5RDB3SHBfdTNWUmtadFlZMjVEMUxRTVlTSVplQUM4ZG44OFYydWduTGxGblpTVXJoSG8tc3I5VzNvMGhRTlBxY01HYzBrc0c2OGxuYlpFQnh0YkczRFpmd2ZfUzBVUHNKVkNVX3I3SGpmY3QxTG8waXRPUE43N1VJYVhIaFFzbXBZRUE0Q2FlWmVwQ0ZtZmVsNGZrVTVYanhlZGM3NmNVbWxmZktmb2ZaY1RUaA?oc=5>

### Taiwan Semiconductor Manufacturing Co Ltd Stock (TSM) Opened Up by 3.14% on Nov 9: Drivers Behind the Movement
- Summary: TSM shares rose 3.14% on Nov 9, driven by market sentiment and positive news flow.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxNb2JBUHY4RzJnUTJHV0N3bDUtUUZEMWg5eU1wVjFMal9wTXlFRXp6cWMzb2d4Q3dOdzVzSmxzX0g0MjU1ZThLYW9LVkRRaWVVU0x6aXBFVF9nZVdvVUZENTNVUjhoX3RJbTdYem5HMmFKNXRyWl83dWdHTGJ0WWhkbVZpRjhXTzZzR3c?oc=5>

### TSM Stock at 21x After a 30% Chip Sell-Off [2026]
- Summary: TSM shares trade at 21x after a 30% chip sell-off, indicating a valuation shift.
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMigwFBVV95cUxOX1FqWGlaSkMzLUctRzBxaV92YzNySE9mQmFHVjhsS2FIVkVpQ0pkZkU1czBKLUtJQ0pMSGRkd08yT1o3N2ZXR1RWdnZPT0VackxCSlRNMXdNUTY2VVVkRmNzWUNqTEF2M0VCM0dibFFMVzdXNy01MUM1U3dLdmpFcGxaUQ?oc=5>

### 11 ETFs Add to Taiwan Semiconductor (TSM) on Thursday
- Summary: Eleven ETFs increased holdings in TSM, boosting demand.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiAFBVV95cUxNMHJOYWdmOVlwd0VLU0JpNVNsNzRuc0plSjM5ZTZwNjVUTW5vWlh4QkJFdmtzeXI2ai1oS3ZpWUxrSENnVHU0U2IwQjBiYW52a3l2UF9qRU1QMVppaWNtbkp2MHB3T2lwalR6bDc0Q3ZIUDdpVmdWUXFIZjRvVmxqdlJndUNPRTV2?oc=5>

### Taiwan Semiconductor Stocks Jump 7.45% as Taiwan Slashes Short Selling After Rout
- Summary: TSM shares surged 7.45% following a short-selling ban.
- Date: 2026-11-06 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxOS0JicUZndUVVYzJoazZmczNMOUNOVFNjSEVDTlNvT3hobFZERHc3N3BPVVE4MENVX0hUTkMwS0NULWxPOXl1Yi13UU9QUmtmcnZtZjF3ZHkwS2Z6VkRBLXdyLUtTYWNkdUxQTWpQLU56SklLYVltUVlUYWFEQTRRYTFWRlY0aEVIenhr?oc=5>

## HEADWINDS

### TSMC Sinks 10%, UMC Down 16% as Chip Rout Deepens After Democrats’ Midterm Wins
- Summary: TSM stock falls 10% during chip rout post‑midterms.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxNcmtKWTVlcVpNd3cyUm50T3VoNG5tbjB0NUI3QWhkS2tZVEY1dFZzak9lWmU5UjBJRUtleUp5dlR1R0g3bTdlOWQ4ajhKaTZzbk9BSzhTWGF6c1FPUDJUU1JES0Z0S01uZkN1XzFWRmN5Q1p5Y1NwSTR5bHFZeVhJS2hweDEtcFNmM09HSUxWT0Q?oc=5>

### TSMC Stocks Move Lower as November Sales Data Face a $53.3 Billion Quarterly Hurdle
- Summary: TSMC shares fell due to sales data challenges, indicating a short-term market decline.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNN21ieWNIWmt1ZzdET1pneEZqX0hEbTRkSE1MTUlLbDhHYUhTRlVhM1lQbEFuSVl4YVA3Mko3YjJWREduclIyT3NUV1RuSXhSbTdwV0xZbFgxLTZoTk8wSG40ejRxUlZpRGJTc2VOV1pQUHpPcjA5dmEzTlJPMUJneUNCNzBUbHFsbzByWEJwbFU2T013d1pyRXplY3M?oc=5>

## CATALYSTS

### Nvidia vs. Taiwan Semiconductor: The AI Revolution Is Big Enough for Both. Here's the Better Buy.
- Summary: Recommends TSM as a better investment over Nvidia.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxPTDNYN2cxV2pHRDRoZm0tUEFobGpnYzBKMUtlbUgwMFF1TklfMU9ZbkpFQnZCamZYVXY4dWFpTVRWUFhmczRvSi1TRnpNOUlpMlZGNnRQaWNpYzBzY1VqaVhUeVBpR0tYOXpuTGlZejhkVlZ5d18takN1ZGdTSkV5MHFTZm1FYVdNYUl0NW9RS3JMMWVJc3MwWA?oc=5>

### TSMC’s AI Opportunity Is Expanding. Here’s the Question That Matters for Its Stock Price
- Summary: Explores TSMC's growing AI prospects and their impact on stock valuation.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiyAFBVV95cUxQTE91N3lqQmhwTnRpMEdqcC1WTFk1blNhSzZHVHRZOUd3dGhUNEU5TGFWZUxVb3FmNWJKazVvY095RS1nV0tGWWdJR0ZPYWxFT2MycURzeXN6aEpkeENCcFYwYXVUSjRqbS1sMl9GQWtSdGZySXdjQ0tXb1dOTmxoZXo5RGlTX016bGhxSTFoYk9VS3pnaEdDc2FMa3J5THNmNDNrVkpLSGdKOEs2ZjJ4ODVqeEUydFdtQUpZdmN1aVlXdWI2THZDZw?oc=5>

### TSMC rises on report of potential push into advanced memory for Nvidia
- Summary: TSM shares rise due to potential advanced memory push for Nvidia.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNRGNTQTdxUFhhMmJMcEpnNUcwdldseWVRTmIyREZtblRncFM3cld4Y2VISnRhWW9rVDdPVHMwaDNVVFNsRjZTZmxaRXZhcm1idmk0NGZPTjlwMHJCdWwxSTBidVh5Vy1ZTjlfeDNBUjQzSDQwV1kweUlJMDdVeV9IVnRteEVsRTBhNmVfUVBUT1FqamRSN1F4RGswdXU?oc=5>

### Taiwan Semiconductor (TSM) Sees $146.2 Million in Net ETF Buying on Nov. 3
- Summary: Net ETF buying of $146.2M indicates institutional confidence in TSM.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxOTHZJQ3FxWHdoRHdCWW50TmE3bzNNVGpiVDFKenBjZEdfWHpWaU16QlFCWmZaejVIcDFlNnFFY0tCQ19vZXczbURkd0p0M3h5YktDRWxhbk94R0Qwd3lldGdlazcwbzdwY1NibnRtdFJRdFhidmJnY1BUMG42VnBYZmFLclZYY0hDbDcyYUlNRGMxWUxPVnNHME9uMVFzNEk?oc=5>

### Taiwan Semiconductor Manufactur (TSM) Stock Forecasts
- Summary: Provides stock forecast for TSM.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxQU241b0xoOWFLMWx3UzJKT0FhNjR5RXJGbFY5LWxjVzFoM2Ezdm03U3hfRVh3LThvRzJyVWJjVW5nWG16RkN0a2p3LVJLR0JFTEtLVUpBWTVuWThuNUV2R3RtWnV2aHU1cUFrT25uZXllb1dzc3VVdkxEZF9FTzlGRUw2XzVjX2c5N0JRSw?oc=5>

### TSMC: Celebrating The Opportunity Presented (NYSE:TSM)
- Summary: TSMC announces a positive outlook and celebrates new opportunities.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxOenhRWWdtanc1S3MxdnR1VjZCaER5OUkxX1AwX3BPRXpRVlptUy03M2syZVpPaWh4Y2dmNVVxNkd2YXlrcjdiaW95Z2tTdW1yV0l5VXhvbjlKRjFSdzJwOEJ4bnFQdkRwc3Yxdm04YUFPaURiUE9VX3ZkVHBENlcxMFBhem85d3I0ajZZ?oc=5>

### Taiwan Semiconductor Wants to Enter Into Advanced Memory Production
- Summary: TSM plans to expand into advanced memory manufacturing, potentially boosting its product portfolio and market position.
- Date: 2026-11-09 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxPczRaLXVBWl83bUZxN1Y4U1ZrTkxGYVk3akdIQklXRHE0NERGNkdOUlZNaFpYZ1NoYzlTX1BDMXlSOVowUUJxa3hEVEdtQzBCemtoZEVKUWNzT1gwTmpMVlN6Mjd1SU1fZ1JHWDkyNDdxTW1PZGUzVkVqNHhJbFJ1UE0xdEwtMXZKaWZFWkJWZFZVMGdHZGlKSUs3QVd6M0lrSW10azNjZWdRXzRyVFdMdA?oc=5>

## RISKS

### What Is Going on With Taiwan Semiconductor Stock on Monday?
- Summary: Inquiry about TSM stock movement on Monday.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxNdlVNUlBPLXliejk5cW53UXNqT0FxZTBBUnQ1ZlhjS2dldDZGSjl2QUsyT3BGY2Q3OGRkUWw3VmV1TFgxVU05eGdJRXZRckQ0ZXU0di1nMGdoYzhJX3YzWGxVcGIxbm9FR0Z2bEpQenM4bkhsNkcydFVCLUtOeHVMd1htQ0ZuV185SVV4bTgzM2l5YjlONURuc0FyWHN2NFpyS2hSdDJyMm8yRE5TWGVZcg?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **TSM** | **25.19** | **74.17** | **3.58** | **50.90** | **2,015,567,544,320.00 USD** | **37.08** |
| UMC | 14.05 | 2.57 | -0.29 | 25.60 | 37,341,052,928.00 USD | 104.48 |
| GFS | 115.74 | 1.89 | 10.87 | 12.50 | 22,582,249,472.00 USD | 19.34 |
| INTC | N/A | 2.74 | 17.16 | 20.90 | 315,551,547,392.00 USD | 55.70 |

Peers fetched as_of: 2026-11-09; TSM reuses existing data (market data as_of: 2026-11-09); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-15
- Next expected earnings: 2027-01-14 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-09

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: N/A
- Filing date: N/A
- Revenue (latest available single quarter): N/A
- Net income (latest available single quarter): N/A
- SEC link: N/A

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMi1AFBVV95cUxQZXJkcmI1STJVajA1Z3JPVEpsdzVLOFNUb2k3NktqV3g5RDB3SHBfdTNWUmtadFlZMjVEMUxRTVlTSVplQUM4ZG44OFYydWduTGxGblpTVXJoSG8tc3I5VzNvMGhRTlBxY01HYzBrc0c2OGxuYlpFQnh0YkczRFpmd2ZfUzBVUHNKVkNVX3I3SGpmY3QxTG8waXRPUE43N1VJYVhIaFFzbXBZRUE0Q2FlWmVwQ0ZtZmVsNGZrVTVYanhlZGM3NmNVbWxmZktmb2ZaY1RUaA?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxNb2JBUHY4RzJnUTJHV0N3bDUtUUZEMWg5eU1wVjFMal9wTXlFRXp6cWMzb2d4Q3dOdzVzSmxzX0g0MjU1ZThLYW9LVkRRaWVVU0x6aXBFVF9nZVdvVUZENTNVUjhoX3RJbTdYem5HMmFKNXRyWl83dWdHTGJ0WWhkbVZpRjhXTzZzR3c?oc=5
- https://news.google.com/rss/articles/CBMigwFBVV95cUxOX1FqWGlaSkMzLUctRzBxaV92YzNySE9mQmFHVjhsS2FIVkVpQ0pkZkU1czBKLUtJQ0pMSGRkd08yT1o3N2ZXR1RWdnZPT0VackxCSlRNMXdNUTY2VVVkRmNzWUNqTEF2M0VCM0dibFFMVzdXNy01MUM1U3dLdmpFcGxaUQ?oc=5
- https://news.google.com/rss/articles/CBMiiAFBVV95cUxNMHJOYWdmOVlwd0VLU0JpNVNsNzRuc0plSjM5ZTZwNjVUTW5vWlh4QkJFdmtzeXI2ai1oS3ZpWUxrSENnVHU0U2IwQjBiYW52a3l2UF9qRU1QMVppaWNtbkp2MHB3T2lwalR6bDc0Q3ZIUDdpVmdWUXFIZjRvVmxqdlJndUNPRTV2?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxOS0JicUZndUVVYzJoazZmczNMOUNOVFNjSEVDTlNvT3hobFZERHc3N3BPVVE4MENVX0hUTkMwS0NULWxPOXl1Yi13UU9QUmtmcnZtZjF3ZHkwS2Z6VkRBLXdyLUtTYWNkdUxQTWpQLU56SklLYVltUVlUYWFEQTRRYTFWRlY0aEVIenhr?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxNcmtKWTVlcVpNd3cyUm50T3VoNG5tbjB0NUI3QWhkS2tZVEY1dFZzak9lWmU5UjBJRUtleUp5dlR1R0g3bTdlOWQ4ajhKaTZzbk9BSzhTWGF6c1FPUDJUU1JES0Z0S01uZkN1XzFWRmN5Q1p5Y1NwSTR5bHFZeVhJS2hweDEtcFNmM09HSUxWT0Q?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNN21ieWNIWmt1ZzdET1pneEZqX0hEbTRkSE1MTUlLbDhHYUhTRlVhM1lQbEFuSVl4YVA3Mko3YjJWREduclIyT3NUV1RuSXhSbTdwV0xZbFgxLTZoTk8wSG40ejRxUlZpRGJTc2VOV1pQUHpPcjA5dmEzTlJPMUJneUNCNzBUbHFsbzByWEJwbFU2T013d1pyRXplY3M?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxPTDNYN2cxV2pHRDRoZm0tUEFobGpnYzBKMUtlbUgwMFF1TklfMU9ZbkpFQnZCamZYVXY4dWFpTVRWUFhmczRvSi1TRnpNOUlpMlZGNnRQaWNpYzBzY1VqaVhUeVBpR0tYOXpuTGlZejhkVlZ5d18takN1ZGdTSkV5MHFTZm1FYVdNYUl0NW9RS3JMMWVJc3MwWA?oc=5
- https://news.google.com/rss/articles/CBMiyAFBVV95cUxQTE91N3lqQmhwTnRpMEdqcC1WTFk1blNhSzZHVHRZOUd3dGhUNEU5TGFWZUxVb3FmNWJKazVvY095RS1nV0tGWWdJR0ZPYWxFT2MycURzeXN6aEpkeENCcFYwYXVUSjRqbS1sMl9GQWtSdGZySXdjQ0tXb1dOTmxoZXo5RGlTX016bGhxSTFoYk9VS3pnaEdDc2FMa3J5THNmNDNrVkpLSGdKOEs2ZjJ4ODVqeEUydFdtQUpZdmN1aVlXdWI2THZDZw?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNRGNTQTdxUFhhMmJMcEpnNUcwdldseWVRTmIyREZtblRncFM3cld4Y2VISnRhWW9rVDdPVHMwaDNVVFNsRjZTZmxaRXZhcm1idmk0NGZPTjlwMHJCdWwxSTBidVh5Vy1ZTjlfeDNBUjQzSDQwV1kweUlJMDdVeV9IVnRteEVsRTBhNmVfUVBUT1FqamRSN1F4RGswdXU?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxOTHZJQ3FxWHdoRHdCWW50TmE3bzNNVGpiVDFKenBjZEdfWHpWaU16QlFCWmZaejVIcDFlNnFFY0tCQ19vZXczbURkd0p0M3h5YktDRWxhbk94R0Qwd3lldGdlazcwbzdwY1NibnRtdFJRdFhidmJnY1BUMG42VnBYZmFLclZYY0hDbDcyYUlNRGMxWUxPVnNHME9uMVFzNEk?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxQU241b0xoOWFLMWx3UzJKT0FhNjR5RXJGbFY5LWxjVzFoM2Ezdm03U3hfRVh3LThvRzJyVWJjVW5nWG16RkN0a2p3LVJLR0JFTEtLVUpBWTVuWThuNUV2R3RtWnV2aHU1cUFrT25uZXllb1dzc3VVdkxEZF9FTzlGRUw2XzVjX2c5N0JRSw?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxOenhRWWdtanc1S3MxdnR1VjZCaER5OUkxX1AwX3BPRXpRVlptUy03M2syZVpPaWh4Y2dmNVVxNkd2YXlrcjdiaW95Z2tTdW1yV0l5VXhvbjlKRjFSdzJwOEJ4bnFQdkRwc3Yxdm04YUFPaURiUE9VX3ZkVHBENlcxMFBhem85d3I0ajZZ?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxPczRaLXVBWl83bUZxN1Y4U1ZrTkxGYVk3akdIQklXRHE0NERGNkdOUlZNaFpYZ1NoYzlTX1BDMXlSOVowUUJxa3hEVEdtQzBCemtoZEVKUWNzT1gwTmpMVlN6Mjd1SU1fZ1JHWDkyNDdxTW1PZGUzVkVqNHhJbFJ1UE0xdEwtMXZKaWZFWkJWZFZVMGdHZGlKSUs3QVd6M0lrSW10azNjZWdRXzRyVFdMdA?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxOc082T1J0TU5FN2owTXl4YWZYVkNDdzJHWkZHeFhZYm0yQVd1RnBsZXF2TUg5c0d3d0k4Umc0elpXRDYyMWJDaWJ6dWVIbFNSUFYwZ1dkN2pfZmNtTW9yVkVRQkdSb1Zlalg0dmhqUFhYOFlhenl6N2lnc2lVY19FZ01Xakc0NjBuZWY5Z3RR?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxNdlVNUlBPLXliejk5cW53UXNqT0FxZTBBUnQ1ZlhjS2dldDZGSjl2QUsyT3BGY2Q3OGRkUWw3VmV1TFgxVU05eGdJRXZRckQ0ZXU0di1nMGdoYzhJX3YzWGxVcGIxbm9FR0Z2bEpQenM4bkhsNkcydFVCLUtOeHVMd1htQ0ZuV185SVV4bTgzM2l5YjlONURuc0FyWHN2NFpyS2hSdDJyMm8yRE5TWGVZcg?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
