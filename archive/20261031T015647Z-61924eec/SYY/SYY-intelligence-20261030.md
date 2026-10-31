# SYY Intelligence Report

- ticker: **SYY**
- Report as_of: **2026-10-30**
- Market data as_of: **2026-10-30**
- Quant sources: https://finance.yahoo.com/quote/SYY/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/SYY/key-statistics/
- AI analysis snapshot as_of: **2026-10-30**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-31T02:03:51.131133+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 11, 'rule': 4, 'ai': 4, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **2** exact headline/source/date matches; prior report **20261030T021807Z-b9de7146/SYY** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 11 unique headlines; 6 named publishers; 0 exact duplicates; 11 HTTPS source links; largest publisher share 36.36%; oldest publication 2026-10-23

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 82.9000 |
| Return 1D (%) | 0.4605 |
| Return 1W (%) | 1.8803 |
| Return 1M (%) | 7.0940 |
| Return YTD (%) | 15.7586 |
| Return 1Y (%) | 14.1935 |
| Annualized volatility (%) | 27.3340 |
| Beta vs SPY | 0.1485 |
| Max drawdown (%) | -23.9798 |
| Sharpe (rf=0) | 0.6273 |
| Downside deviation (rf=0, %) | 20.2333 |
| Sortino (rf=0) | 0.8474 |
| Historical VaR 95% (1D, %) | 2.1089 |
| Historical ES 95% (1D, %) | 3.7604 |
| Correlation vs SPY | 0.0695 |
| Tracking error vs SPY (%) | 29.3618 |
| P/E (trailing) | 22.65 |
| P/B | 14.88 |
| EV/EBITDA | 11.79 |
| Revenue growth (%) | 4.70 |
| Forward P/E (estimate) | 15.39 |
| Gross margin (%) | 18.50 |
| Operating margin (%) | 4.84 |
| Return on equity (%) | 77.69 |
| Free cash flow yield (%) | 4.69 |
| MA50 | 80.2138 |
| Close vs MA50 (%) | 3.3488 |
| MA200 | 79.5114 |
| Close vs MA200 (%) | 4.2618 |
| RSI (14, Wilder) | 59.6376 |
| MACD (12,26) | 0.9295 |
| MACD signal (9) | 0.7317 |
| MACD histogram | 0.1978 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'SYY': 272, 'SPY': 272}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 82.9000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.4605 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 1.8803 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 7.0940 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 15.7586 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 14.1935 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 27.3340 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 20.2333 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.8474 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.1089 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.7604 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.0695 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 29.3618 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.1485 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -23.9798 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.6273 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 15.3923 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 18.4960 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 4.8450 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 77.6920 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 4.6935 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 22.6503 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 59.6376 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.1978 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 3.3488 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 4.2618 -> Slightly above the moving-average trend level.

## TAILWINDS

### Sysco (SYY) Stock May Look Reasonable As Its 34% Run Continues
- Summary: Sysco’s stock continues a 34% run, suggesting potential value for investors.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiygFBVV95cUxONE9XTDdrQVZHa2RabTFUQ21rZnh5WW5JRm15NTJJNjdjNENaQ0x6bF9JSm02aDRDMFEwQmJRcEV6Q1J3YlYyMU1aT2VKSEpOeHdhTklEZmRzajdjOEdIampQSzdMdE1DTHE2eUJsYjJlbXpMRWgzcHFhdTRkMGg4QnU3Nzd2NFJIbGNGM3h2RUdIRUV1M3BBMF9CTm9CblRtUjRQdDkycFFLeG9BM1o3Zm42VTY5WmNPb0lYWmZyallMSTdJMjYxeUNB0gHPAUFVX3lxTE1mYXVvbVFFaTJWZ2xxZmJwRnlyclBKRVNubFBNYWRVRXF1a05OTFFsa29SWi03ekpNM1VXZlJRUmgtQVR0WjN2ZksxRTlPV0dzYlRzWjhfRERBWV8yMzVFS19tczloVGlIUEwtZUZVTjV3LVFVMTV2VGI5clRPN1lpQTdCRkRfYjlKOWs2aWJmVDg4VDlmN1ZUTjFIMERvdW45azFvWk4yMHVxenhYX2E3bUVlSS1ZMEZvTkdQTjBlVlluamJoWVdOcWhoWnQ4MA?oc=5>

### How Investors May Respond To Sysco (SYY) Los Angeles Strike Ends
- Summary: Strike ends, likely boosting investor confidence and stock performance.
- Date: 2026-10-27 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxOQVFEU1JiUkJwQ0VIemhIdnNpOU9YYmhhbmp2aDAwdXJCeFpIQWZ5ckt5TExHc2EyMmFFLXF3cDJCTGwtWGk4NGEzSXpCQkRfZHh3RHZPSmRyRFloNHZabjJJc05GSTc0aGZLejY5blhSMmZvd2JRcTZkTGVOMTl6QjJOVU1JOXl4ZW1YSUc0YmZhNnlhOExyRFZaMEU?oc=5>

## HEADWINDS

### Sysco Corp (SYY) Stock Down 3.1% -- Now Undervalued? GF Score: 8
- Summary: Recent 3.1% decline signals short‑term downside pressure.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxPajJiUGFnczdqMUZtT0dpV1gxWnhrVm54YTc5amZDbWtfYWZ6YmI2UDJkVElVc2MxbTc2bkFPRmtnb1k3Uy1hNDV4eW5HRWpEbWN3UHdKdDJSaHZ2czgzWGFMdXJfUlp0RWVMQmZ1alBYTEhEZWc0NzhNNlhwS1RUSFlOMk9Ldk5abV9kREdOY2FuQU5heUlSUHpBalJsb1E?oc=5>

## CATALYSTS

### Sysco Earnings Preview: High Debt Levels Overshadow Everything (NYSE:SYY)
- Summary: Sysco Earnings Preview: High Debt Levels Overshadow Everything (NYSE:SYY)
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxOMllybjY0dGtTSEJqNE5sVm84Z3U2OUtFZlkzZVhvTXdwelpPYkNiUzU4dF95VkltejhzcGpTSkZPQUZ4RDIzZERkcW1lV0ViSEZnbXJXQ3V1bXRWa1pmcV9sbm0tbVdUMmZoYkN6d1BXUHRrOWRMbHRqRkdBaUZ6SmJDQm43YUZrNmtPdmJ0NEdVQnNSbkVSNWRSbC1FcVhYSHVVRg?oc=5>

### Sysco Corporation $SYY Stock Sold by Mondrian Investment Partners LTD
- Summary: Sysco Corporation $SYY Stock Sold by Mondrian Investment Partners LTD
- Date: 2026-10-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiyAFBVV95cUxNVXJRbHh1VnJrbGJGNmVUVjBRbEcwZElFZk15azN2SUtZdW5UcmZiRGpsZ2VXbmhrQ2ZUYUhzSzVZbjdwRk5nOGtVY1BwenkwNzc0NTRUWHJjR0s5akE5amtPLXh6LUgxZEx3LWl2YXdYSDNpVFJGV1hWMldjanZoMl8tVk5KS044ZkZoWllXZ2FMYlhyc0ZMbHJ5TVR5eUFCMVZRWjBWWWl6VEZyT0laeFU3akphVjRkSGMwZkVhamRlRUI2NlUxQQ?oc=5>

### Sysco Corporation $SYY Stock Purchased by Robeco Institutional Asset Management B.V.
- Summary: Sysco Corporation $SYY Stock Purchased by Robeco Institutional Asset Management B.V.
- Date: 2026-10-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2gFBVV95cUxQOWxvZU5OYXVLQmhIV2tGZnViOHo1bUZhbGVfc09tUTNfMmFCS2FfV1Q3ck1vQTV3N3ZVb0lfM3lvaU9JQVZpNlktbmlWVXhKODFHU2Y3eEZtWU13Z3M5NGM1T2p5NkE2QUgxLXNnYjMtVUJMeGRhdVVqXzl0LU91NkpXZnhSdjFyZ1gzSmRDekR1Z2FsWmZwTWZWLVU5eFZtdDdyTWt4bnByUWFva3FuTEpfZmtoMnJwaTBIRXgtVUdWcjVxdjBUbzNTMUdydFpjOXMxMENka29tUQ?oc=5>

### Sysco Corporation $SYY Stock Sold by Investment House LLC
- Summary: Sysco Corporation $SYY Stock Sold by Investment House LLC
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxPaWd0N05GZFNkMUE3TWhnMi1OSnFVYUtuMEVyT2gzcWRxNnRhSkFWMG8tbGtuSG03Z080bTFfYTBHZFFrVF9ra2R5bUYwWEZRZVNqWVRiRDNIZ3RHZlA1b243bmdGS2g4NUgzYzJjeVZEcXVOZU0tMVpyVFRaYzdVcnU0REUyTG1MODVEU1ZHN19KNE03UlVVa0VVcFlKbGgtalVEcFFSQWlLcndsZzIzQmZQbDRnNnBY?oc=5>

### Sysco (SYY) Earnings Expected to Grow: Should You Buy?
- Summary: Sysco forecasts higher earnings, suggesting potential upside for investors.
- Date: 2026-10-27 | Impact: medium | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxPQW1hNVdrVXZzS0w1OG5NYmhxN3BvdkFTak5UNm53cGdkRkc5a0NzZnIzaE11MGRaQnVlMURGQWJwSmZjNHVobU42V2UwSWxhSHRtb094RE1wLWJ1YmxmS2xJcDBjWHVvUlBqd3NnQ096Y1hlcFQzN2VKRkxMbGFCaTZBZzJFZGtBM05BRFIteTV6d3ZLYS1qMTNfX2FUUQ?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **SYY** | **22.65** | **14.88** | **11.79** | **4.70** | **40,779,665,408.00 USD** | **14.19** |
| USFD | 31.88 | 5.24 | 15.57 | 4.50 | 22,414,026,752.00 USD | 41.45 |
| PFGC | 43.25 | 3.16 | 13.69 | 7.30 | 15,558,028,288.00 USD | 2.03 |
| CHEF | 44.73 | 6.19 | 19.35 | 11.20 | 4,530,137,600.00 USD | 73.80 |

Peers fetched as_of: 2026-10-30; SYY reuses existing data (market data as_of: 2026-10-30); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-04
- Next expected earnings: 2026-11-03 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-30

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
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

- https://news.google.com/rss/articles/CBMiygFBVV95cUxONE9XTDdrQVZHa2RabTFUQ21rZnh5WW5JRm15NTJJNjdjNENaQ0x6bF9JSm02aDRDMFEwQmJRcEV6Q1J3YlYyMU1aT2VKSEpOeHdhTklEZmRzajdjOEdIampQSzdMdE1DTHE2eUJsYjJlbXpMRWgzcHFhdTRkMGg4QnU3Nzd2NFJIbGNGM3h2RUdIRUV1M3BBMF9CTm9CblRtUjRQdDkycFFLeG9BM1o3Zm42VTY5WmNPb0lYWmZyallMSTdJMjYxeUNB0gHPAUFVX3lxTE1mYXVvbVFFaTJWZ2xxZmJwRnlyclBKRVNubFBNYWRVRXF1a05OTFFsa29SWi03ekpNM1VXZlJRUmgtQVR0WjN2ZksxRTlPV0dzYlRzWjhfRERBWV8yMzVFS19tczloVGlIUEwtZUZVTjV3LVFVMTV2VGI5clRPN1lpQTdCRkRfYjlKOWs2aWJmVDg4VDlmN1ZUTjFIMERvdW45azFvWk4yMHVxenhYX2E3bUVlSS1ZMEZvTkdQTjBlVlluamJoWVdOcWhoWnQ4MA?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxOQVFEU1JiUkJwQ0VIemhIdnNpOU9YYmhhbmp2aDAwdXJCeFpIQWZ5ckt5TExHc2EyMmFFLXF3cDJCTGwtWGk4NGEzSXpCQkRfZHh3RHZPSmRyRFloNHZabjJJc05GSTc0aGZLejY5blhSMmZvd2JRcTZkTGVOMTl6QjJOVU1JOXl4ZW1YSUc0YmZhNnlhOExyRFZaMEU?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxPajJiUGFnczdqMUZtT0dpV1gxWnhrVm54YTc5amZDbWtfYWZ6YmI2UDJkVElVc2MxbTc2bkFPRmtnb1k3Uy1hNDV4eW5HRWpEbWN3UHdKdDJSaHZ2czgzWGFMdXJfUlp0RWVMQmZ1alBYTEhEZWc0NzhNNlhwS1RUSFlOMk9Ldk5abV9kREdOY2FuQU5heUlSUHpBalJsb1E?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxOMllybjY0dGtTSEJqNE5sVm84Z3U2OUtFZlkzZVhvTXdwelpPYkNiUzU4dF95VkltejhzcGpTSkZPQUZ4RDIzZERkcW1lV0ViSEZnbXJXQ3V1bXRWa1pmcV9sbm0tbVdUMmZoYkN6d1BXUHRrOWRMbHRqRkdBaUZ6SmJDQm43YUZrNmtPdmJ0NEdVQnNSbkVSNWRSbC1FcVhYSHVVRg?oc=5
- https://news.google.com/rss/articles/CBMiyAFBVV95cUxNVXJRbHh1VnJrbGJGNmVUVjBRbEcwZElFZk15azN2SUtZdW5UcmZiRGpsZ2VXbmhrQ2ZUYUhzSzVZbjdwRk5nOGtVY1BwenkwNzc0NTRUWHJjR0s5akE5amtPLXh6LUgxZEx3LWl2YXdYSDNpVFJGV1hWMldjanZoMl8tVk5KS044ZkZoWllXZ2FMYlhyc0ZMbHJ5TVR5eUFCMVZRWjBWWWl6VEZyT0laeFU3akphVjRkSGMwZkVhamRlRUI2NlUxQQ?oc=5
- https://news.google.com/rss/articles/CBMi2gFBVV95cUxQOWxvZU5OYXVLQmhIV2tGZnViOHo1bUZhbGVfc09tUTNfMmFCS2FfV1Q3ck1vQTV3N3ZVb0lfM3lvaU9JQVZpNlktbmlWVXhKODFHU2Y3eEZtWU13Z3M5NGM1T2p5NkE2QUgxLXNnYjMtVUJMeGRhdVVqXzl0LU91NkpXZnhSdjFyZ1gzSmRDekR1Z2FsWmZwTWZWLVU5eFZtdDdyTWt4bnByUWFva3FuTEpfZmtoMnJwaTBIRXgtVUdWcjVxdjBUbzNTMUdydFpjOXMxMENka29tUQ?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxPaWd0N05GZFNkMUE3TWhnMi1OSnFVYUtuMEVyT2gzcWRxNnRhSkFWMG8tbGtuSG03Z080bTFfYTBHZFFrVF9ra2R5bUYwWEZRZVNqWVRiRDNIZ3RHZlA1b243bmdGS2g4NUgzYzJjeVZEcXVOZU0tMVpyVFRaYzdVcnU0REUyTG1MODVEU1ZHN19KNE03UlVVa0VVcFlKbGgtalVEcFFSQWlLcndsZzIzQmZQbDRnNnBY?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxPQW1hNVdrVXZzS0w1OG5NYmhxN3BvdkFTak5UNm53cGdkRkc5a0NzZnIzaE11MGRaQnVlMURGQWJwSmZjNHVobU42V2UwSWxhSHRtb094RE1wLWJ1YmxmS2xJcDBjWHVvUlBqd3NnQ096Y1hlcFQzN2VKRkxMbGFCaTZBZzJFZGtBM05BRFIteTV6d3ZLYS1qMTNfX2FUUQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
