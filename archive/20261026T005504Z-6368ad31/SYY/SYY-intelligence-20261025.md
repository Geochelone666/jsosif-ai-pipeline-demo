# SYY Intelligence Report

- ticker: **SYY**
- Report as_of: **2026-10-25**
- Market data as_of: **2026-10-23**
- Quant sources: https://finance.yahoo.com/quote/SYY/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/SYY/key-statistics/
- AI analysis snapshot as_of: **2026-10-25**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-26T00:59:51.896635+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 7, 'rule': 3, 'ai': 0, 'unknown': 0, 'irrelevant': 4})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **0** exact headline/source/date matches; prior report **N/A** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 7 unique headlines; 6 named publishers; 0 exact duplicates; 7 HTTPS source links; largest publisher share 28.57%; oldest publication 2026-10-22

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 81.3700 |
| Return 1D (%) | -3.0963 |
| Return 1W (%) | -1.0338 |
| Return 1M (%) | 6.2349 |
| Return YTD (%) | 13.6222 |
| Return 1Y (%) | 7.0556 |
| Annualized volatility (%) | 27.5775 |
| Beta vs SPY | 0.1444 |
| Max drawdown (%) | -23.9798 |
| Sharpe (rf=0) | 0.3891 |
| Downside deviation (rf=0, %) | 20.5518 |
| Sortino (rf=0) | 0.5221 |
| Historical VaR 95% (1D, %) | 2.1115 |
| Historical ES 95% (1D, %) | 3.8061 |
| Correlation vs SPY | 0.0667 |
| Tracking error vs SPY (%) | 29.5986 |
| P/E (trailing) | 22.23 |
| P/B | 14.61 |
| EV/EBITDA | 11.63 |
| Revenue growth (%) | 4.70 |
| Forward P/E (estimate) | 15.22 |
| Gross margin (%) | 18.50 |
| Operating margin (%) | 4.84 |
| Return on equity (%) | 77.69 |
| Free cash flow yield (%) | 4.78 |
| MA50 | 80.1613 |
| Close vs MA50 (%) | 1.5078 |
| MA200 | 79.2920 |
| Close vs MA200 (%) | 2.6207 |
| RSI (14, Wilder) | 54.3635 |
| MACD (12,26) | 0.8773 |
| MACD signal (9) | 0.3709 |
| MACD histogram | 0.5064 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'SYY': 267, 'SPY': 267}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 81.3700 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -3.0963 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -1.0338 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 6.2349 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 13.6222 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 7.0556 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 27.5775 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 20.5518 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.5221 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.1115 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.8061 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.0667 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 29.5986 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.1444 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -23.9798 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.3891 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 15.2213 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 18.4960 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 4.8450 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 77.6920 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 4.7818 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 22.2322 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 54.3635 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.5064 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 1.5078 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 2.6207 -> Slightly above the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

### Sysco Corporation (SYY) Falls 3.10% to $81.37, Testing the Middle of Its Trading Range - Quote Data
- Summary: Sysco Corporation (SYY) Falls 3.10% to $81.37, Testing the Middle of Its Trading Range - Quote Data
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxOdmN2MGE4WEljTmcybDQ3Nk92UEZKdGV3MGN2Xy1zcjhZbTM1dU8wVURiVTBvYy1jSV9xVXRHRHJXV2ctaEtnSGU0Q3ZvSV9GZnRFU0FLNEFKejFWYm5fZmxoVkozT19iaVFYRnV6YXkyZDYza3JfOGRwRFlSRHV4R0JSYm5FRnV6Um9raDlvUnhQZFBJdUdhRENIaTk3QnhFbllqSmFoLUM2VGc2Z0VlYmtYandwaENkWGZpSUxCT0JGdw?oc=5>

## CATALYSTS

### Sysco Corporation $SYY Stock Sold by Mondrian Investment Partners LTD
- Summary: Sysco Corporation $SYY Stock Sold by Mondrian Investment Partners LTD
- Date: 2026-10-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiyAFBVV95cUxNVXJRbHh1VnJrbGJGNmVUVjBRbEcwZElFZk15azN2SUtZdW5UcmZiRGpsZ2VXbmhrQ2ZUYUhzSzVZbjdwRk5nOGtVY1BwenkwNzc0NTRUWHJjR0s5akE5amtPLXh6LUgxZEx3LWl2YXdYSDNpVFJGV1hWMldjanZoMl8tVk5KS044ZkZoWllXZ2FMYlhyc0ZMbHJ5TVR5eUFCMVZRWjBWWWl6VEZyT0laeFU3akphVjRkSGMwZkVhamRlRUI2NlUxQQ?oc=5>

### Sysco Corporation $SYY Stock Purchased by Robeco Institutional Asset Management B.V.
- Summary: Sysco Corporation $SYY Stock Purchased by Robeco Institutional Asset Management B.V.
- Date: 2026-10-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2gFBVV95cUxQOWxvZU5OYXVLQmhIV2tGZnViOHo1bUZhbGVfc09tUTNfMmFCS2FfV1Q3ck1vQTV3N3ZVb0lfM3lvaU9JQVZpNlktbmlWVXhKODFHU2Y3eEZtWU13Z3M5NGM1T2p5NkE2QUgxLXNnYjMtVUJMeGRhdVVqXzl0LU91NkpXZnhSdjFyZ1gzSmRDekR1Z2FsWmZwTWZWLVU5eFZtdDdyTWt4bnByUWFva3FuTEpfZmtoMnJwaTBIRXgtVUdWcjVxdjBUbzNTMUdydFpjOXMxMENka29tUQ?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **SYY** | **22.23** | **14.61** | **11.63** | **4.70** | **40,027,037,696.00 USD** | **7.06** |
| USFD | 31.05 | 5.10 | 15.24 | 4.50 | 21,829,933,056.00 USD | 33.06 |
| PFGC | 41.36 | 3.02 | 13.29 | 7.30 | 14,876,333,056.00 USD | -6.93 |
| CHEF | 50.42 | 6.66 | 19.70 | 12.90 | 4,319,489,024.00 USD | 80.19 |

Peers fetched as_of: 2026-10-25; SYY reuses existing data (market data as_of: 2026-10-23); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-04
- Next expected earnings: 2026-11-03 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-25

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

- https://news.google.com/rss/articles/CBMiwgFBVV95cUxOdmN2MGE4WEljTmcybDQ3Nk92UEZKdGV3MGN2Xy1zcjhZbTM1dU8wVURiVTBvYy1jSV9xVXRHRHJXV2ctaEtnSGU0Q3ZvSV9GZnRFU0FLNEFKejFWYm5fZmxoVkozT19iaVFYRnV6YXkyZDYza3JfOGRwRFlSRHV4R0JSYm5FRnV6Um9raDlvUnhQZFBJdUdhRENIaTk3QnhFbllqSmFoLUM2VGc2Z0VlYmtYandwaENkWGZpSUxCT0JGdw?oc=5
- https://news.google.com/rss/articles/CBMiyAFBVV95cUxNVXJRbHh1VnJrbGJGNmVUVjBRbEcwZElFZk15azN2SUtZdW5UcmZiRGpsZ2VXbmhrQ2ZUYUhzSzVZbjdwRk5nOGtVY1BwenkwNzc0NTRUWHJjR0s5akE5amtPLXh6LUgxZEx3LWl2YXdYSDNpVFJGV1hWMldjanZoMl8tVk5KS044ZkZoWllXZ2FMYlhyc0ZMbHJ5TVR5eUFCMVZRWjBWWWl6VEZyT0laeFU3akphVjRkSGMwZkVhamRlRUI2NlUxQQ?oc=5
- https://news.google.com/rss/articles/CBMi2gFBVV95cUxQOWxvZU5OYXVLQmhIV2tGZnViOHo1bUZhbGVfc09tUTNfMmFCS2FfV1Q3ck1vQTV3N3ZVb0lfM3lvaU9JQVZpNlktbmlWVXhKODFHU2Y3eEZtWU13Z3M5NGM1T2p5NkE2QUgxLXNnYjMtVUJMeGRhdVVqXzl0LU91NkpXZnhSdjFyZ1gzSmRDekR1Z2FsWmZwTWZWLVU5eFZtdDdyTWt4bnByUWFva3FuTEpfZmtoMnJwaTBIRXgtVUdWcjVxdjBUbzNTMUdydFpjOXMxMENka29tUQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
