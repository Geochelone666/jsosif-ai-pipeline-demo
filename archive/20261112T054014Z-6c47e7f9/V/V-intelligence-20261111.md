# V Intelligence Report

- ticker: **V**
- Report as_of: **2026-11-11**
- Market data as_of: **2026-11-11**
- Quant sources: https://finance.yahoo.com/quote/V/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/V/key-statistics/
- AI analysis snapshot as_of: **2026-11-11**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-12T05:50:59.167509+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 16, 'rule': 3, 'ai': 5, 'unknown': 0, 'irrelevant': 8})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **5** exact headline/source/date matches; prior report **20261111T043601Z-d14951e6/V** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 16 unique headlines; 10 named publishers; 0 exact duplicates; 16 HTTPS source links; largest publisher share 18.75%; oldest publication 2026-11-05

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 425.5500 |
| Return 1D (%) | 0.6028 |
| Return 1W (%) | -2.3438 |
| Return 1M (%) | 10.6078 |
| Return YTD (%) | 22.2942 |
| Return 1Y (%) | 26.7991 |
| Annualized volatility (%) | 22.9248 |
| Beta vs SPY | 0.3363 |
| Max drawdown (%) | -17.1805 |
| Sharpe (rf=0) | 1.1535 |
| Downside deviation (rf=0, %) | 14.1375 |
| Sortino (rf=0) | 1.8705 |
| Historical VaR 95% (1D, %) | 1.8026 |
| Historical ES 95% (1D, %) | 2.7901 |
| Correlation vs SPY | 0.2014 |
| Tracking error vs SPY (%) | 24.2333 |
| P/E (trailing) | 34.35 |
| P/B | 22.20 |
| EV/EBITDA | 24.77 |
| Revenue growth (%) | 13.20 |
| Forward P/E (estimate) | 24.83 |
| Gross margin (%) | 97.68 |
| Operating margin (%) | 66.31 |
| Return on equity (%) | 63.51 |
| Free cash flow yield (%) | 2.64 |
| MA50 | 387.8976 |
| Close vs MA50 (%) | 9.7068 |
| MA200 | 344.8275 |
| Close vs MA200 (%) | 23.4095 |
| RSI (14, Wilder) | 65.0878 |
| MACD (12,26) | 11.0992 |
| MACD signal (9) | 11.0889 |
| MACD histogram | 0.0103 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'V': 280, 'SPY': 280}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 425.5500 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.6028 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -2.3438 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 10.6078 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 22.2942 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 26.7991 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 22.9248 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 14.1375 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.8705 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.8026 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.7901 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2014 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 24.2333 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.3363 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -17.1805 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.1535 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 24.8273 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 97.6780 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 66.3070 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 63.5070 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.6428 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 34.3462 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 65.0878 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.0103 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 9.7068 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 23.4095 -> Clearly above the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

### Visa Stock Drops 3.8%, Shedding Nearly $28 Billion in One Session
- Summary: Visa Stock Drops 3.8%, Shedding Nearly $28 Billion in One Session
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMifkFVX3lxTE5fT1NLR3lPeDJtLWNPQkQzM1Y2eEUweWx5Y3BPZHJfeXFCQVhWOW5JUHcycmRjNmlwWDhGRU4wVFRmbVZTU3ZLdEhaU2VVcHNtUWlZTEJnUk9rRlk2di1iamJnbmdONGtVSjBvOFRJNk5iV2ZMR0NSZmdBb2gzQQ?oc=5>

### Visa (NYSE:V) Stock Falls 3.3% - Here's Why
- Summary: Visa (NYSE:V) Stock Falls 3.3% - Here's Why
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQUEpYckR2d0x3OXIwaXhxajhOQ0Z6RzZ5VjNHM19GTDBsVTZ2YlMzMGNzRXR3TUYtcjJqeVNTcUFhbUdZZl9JdnhVeVpNMEdEZWtHQ1F6MlIxeVRDQTI2VkFscm9UbWF3Y19uOU9DXzJ3azNSVEFaTUJUQmI4M0lZWjZkV243ZHRoWTJlZlhIM21LNTBrZHBhRWhabVI?oc=5>

## CATALYSTS

### Visa (V) Stock Price Stalls After Q4 Earnings Beat
- Summary: Visa (V) Stock Price Stalls After Q4 Earnings Beat
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxQRmYzcXpPN1dXRkl4M2ZBOWhmR3QxVUZwR2hTTlpLRjczMnJ1Q1BybWpGT0VvYVBvSHNlZk5IUlQzYkVYdllLVXViSGVhS2dHbXUxZE1wVmkzanV6SXNrZTVwbGtiT0hYZC01ZVN6MDBIcUV5NV85WHI0bXJ6Z1laNS1mcGRJel9TQ2U5UGlxaV9RVGEzSGV6S1F5eVg2dnptQnNqSzBnZ0JOMXcxcEhYOHhUUTRiTlhubjIyY9IBwgFBVV95cUxQakl0U1FCSGgtcG5LVFJhcE5GOVZrVDdfZG1qNFpwekFuclhDSDZHYWFFX0VkeXAwdUx0NnBfUHRZM1o4MG5odVR6c0NqbFZFTmRSeWZpTV9NVWRUd3dyTzNvR29uZHQ0X2s2TU1Eb21VcFB1TGFVTXZHaWEyZy1YaWNiLXBHUWJvLU9qUE5PM1Vnd2NxMWdwMmZZTFJxN3pwZXlnMDBvVEpuWndHNm5GSUtHekJXVnk0S09wbFlEQkNkQQ?oc=5>

### The Dates That Matter Most For Visa Stock
- Summary: Key dates for Visa stock performance highlighted.
- Date: 2026-11-10 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxQamVyZEYyY3hfT3VNT0FDRVJNWjFfdTJ2S1J6XzkweXRZY3dVSTJJNFVSVHB2OTNpR1FycVFpdXRFR1V1bGtjSC1WY2ZjLXBydGxSX0haam83NFhnV0QteTNiZmlYQk1zS3ZDQlR4Um9PbVZwUDYxQTdkZnF2M3dOVlNwcEgwcktVV2t2MGNtRjVOdExISVJnM1JZSXlES0ND?oc=5>

### Visa (V) Stock Could Be Reasonable With Excess Returns Intact
- Summary: Speculation that Visa stock may remain attractive with excess returns intact.
- Date: 2026-11-10 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxPamgyTVlJR1Rza3hGS3VHejlSczNrQ2J0cndUSVM4cDlsQ0xsNWNkdzdtUVo5ZkZQOTJkSVZNNHcwWUkxMUNQQ0hrTmxCZU1wdUV6OHlla1VoTTlDZmRxTUhZTFhfbF8yMTVCTTVNYjEwR2d4clpoTzFHZkZ3aUhQeDVoZlJVOGxnWEtqZEVOdFUzLTJKekdoSDNB?oc=5>

### Insider trades: Netflix, Intel, Visa among notable names (V:NYSE)
- Summary: Insider trading activity involving Visa noted.
- Date: 2026-11-07 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxPU1FaN0dLTS0xR2F6NmtmajJrblZBaHV2MGFEbURkU0x5Si1Jd2RadThjZWxIYjVwM0sxcHBsWGdtN2UwWHJvbGNvTkJzUkFLNkU5SXVESGNBWHZDUlZVSFR1QlF4R21yU3JUT25MUWNBLXBkSHVsdnBoTjVaMWpZVTBmV01JclZ6RWk4WlFIbFR1QlJNV1E?oc=5>

### Citigroup Issues Positive Forecast for Visa (NYSE:V) Stock Price
- Summary: Citigroup forecasts a positive outlook for Visa stock.
- Date: 2026-11-10 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxQS0JsRjVsMzh1UG55eVFlaHpwaWJTam5DQjVZUFo3dG1SVUpFWU1CRHBLV1JLSkZhSm5kTEd4MGZrdmFKQ0ZzNlBSODdpcjgxa3FzNTJzOEFUQlJXUmxtVlF5ZGR1blc0c0J4bElpS1hkcDZiNXF6TC1UVnhBV3UzcHkzcVJtLTk3T2NvUF9zU29UZFQ1SE1xU0txQnNtd0piQ05YR1FEc2kxbG9LZEJfMFFFckNnTWtrY0xGdmFvZklFQQ?oc=5>

### AI failed 42.8% of shopping test runs, Visa finds
- Summary: Visa reports AI test failures in shopping scenarios, indicating challenges in AI integration.
- Date: 2026-11-05 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxQQ0x3UVNPbUo2OFN1TnczU3BId1QxYm5oQ1hRZEhjdkVjLWtxNElKTGRkNXJMSEd3ZVlVdmdtVTRKeXBVYUtTbnBqdm1MVU1PUDBhZm9ONmxGbm1ENEYwTGFIZTlPa3lGS0JIWEd4WWh3d2ZvX1BTclFwZmNSNC1nWVFnWlJYYWVyTVpRQWdDOEZhZHBfemc5dDZ4U2Y1ZlppUkxtbWptQWd3OS1aTnFDQzV1aDVhZGhoLVE?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **V** | **34.35** | **22.20** | **24.77** | **13.20** | **793,991,184,384.00 USD** | **26.80** |
| MA | 34.58 | 85.33 | 25.58 | 14.00 | 575,612,190,720.00 USD | 19.10 |
| PYPL | 11.22 | 2.56 | 8.19 | 2.00 | 49,407,553,536.00 USD | -10.77 |
| AXP | 18.22 | 6.06 | N/A | 11.30 | 216,662,048,768.00 USD | -11.73 |

Peers fetched as_of: 2026-11-11; V reuses existing data (market data as_of: 2026-11-11); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-27
- Next expected earnings: 2027-01-26 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-11

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-K
- Filing date: 2026-11-05
- Revenue (latest available single quarter): 5,840,000,000.00 USD; period 2019-04-01/2019-06-30; fiscal year/reporting period 2019/Q3
- Net income (latest available single quarter): 5,628,000,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1403161/000140316126000134/v-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMifkFVX3lxTE5fT1NLR3lPeDJtLWNPQkQzM1Y2eEUweWx5Y3BPZHJfeXFCQVhWOW5JUHcycmRjNmlwWDhGRU4wVFRmbVZTU3ZLdEhaU2VVcHNtUWlZTEJnUk9rRlk2di1iamJnbmdONGtVSjBvOFRJNk5iV2ZMR0NSZmdBb2gzQQ?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQUEpYckR2d0x3OXIwaXhxajhOQ0Z6RzZ5VjNHM19GTDBsVTZ2YlMzMGNzRXR3TUYtcjJqeVNTcUFhbUdZZl9JdnhVeVpNMEdEZWtHQ1F6MlIxeVRDQTI2VkFscm9UbWF3Y19uOU9DXzJ3azNSVEFaTUJUQmI4M0lZWjZkV243ZHRoWTJlZlhIM21LNTBrZHBhRWhabVI?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxQRmYzcXpPN1dXRkl4M2ZBOWhmR3QxVUZwR2hTTlpLRjczMnJ1Q1BybWpGT0VvYVBvSHNlZk5IUlQzYkVYdllLVXViSGVhS2dHbXUxZE1wVmkzanV6SXNrZTVwbGtiT0hYZC01ZVN6MDBIcUV5NV85WHI0bXJ6Z1laNS1mcGRJel9TQ2U5UGlxaV9RVGEzSGV6S1F5eVg2dnptQnNqSzBnZ0JOMXcxcEhYOHhUUTRiTlhubjIyY9IBwgFBVV95cUxQakl0U1FCSGgtcG5LVFJhcE5GOVZrVDdfZG1qNFpwekFuclhDSDZHYWFFX0VkeXAwdUx0NnBfUHRZM1o4MG5odVR6c0NqbFZFTmRSeWZpTV9NVWRUd3dyTzNvR29uZHQ0X2s2TU1Eb21VcFB1TGFVTXZHaWEyZy1YaWNiLXBHUWJvLU9qUE5PM1Vnd2NxMWdwMmZZTFJxN3pwZXlnMDBvVEpuWndHNm5GSUtHekJXVnk0S09wbFlEQkNkQQ?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxQamVyZEYyY3hfT3VNT0FDRVJNWjFfdTJ2S1J6XzkweXRZY3dVSTJJNFVSVHB2OTNpR1FycVFpdXRFR1V1bGtjSC1WY2ZjLXBydGxSX0haam83NFhnV0QteTNiZmlYQk1zS3ZDQlR4Um9PbVZwUDYxQTdkZnF2M3dOVlNwcEgwcktVV2t2MGNtRjVOdExISVJnM1JZSXlES0ND?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxPamgyTVlJR1Rza3hGS3VHejlSczNrQ2J0cndUSVM4cDlsQ0xsNWNkdzdtUVo5ZkZQOTJkSVZNNHcwWUkxMUNQQ0hrTmxCZU1wdUV6OHlla1VoTTlDZmRxTUhZTFhfbF8yMTVCTTVNYjEwR2d4clpoTzFHZkZ3aUhQeDVoZlJVOGxnWEtqZEVOdFUzLTJKekdoSDNB?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxPU1FaN0dLTS0xR2F6NmtmajJrblZBaHV2MGFEbURkU0x5Si1Jd2RadThjZWxIYjVwM0sxcHBsWGdtN2UwWHJvbGNvTkJzUkFLNkU5SXVESGNBWHZDUlZVSFR1QlF4R21yU3JUT25MUWNBLXBkSHVsdnBoTjVaMWpZVTBmV01JclZ6RWk4WlFIbFR1QlJNV1E?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxQS0JsRjVsMzh1UG55eVFlaHpwaWJTam5DQjVZUFo3dG1SVUpFWU1CRHBLV1JLSkZhSm5kTEd4MGZrdmFKQ0ZzNlBSODdpcjgxa3FzNTJzOEFUQlJXUmxtVlF5ZGR1blc0c0J4bElpS1hkcDZiNXF6TC1UVnhBV3UzcHkzcVJtLTk3T2NvUF9zU29UZFQ1SE1xU0txQnNtd0piQ05YR1FEc2kxbG9LZEJfMFFFckNnTWtrY0xGdmFvZklFQQ?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxQQ0x3UVNPbUo2OFN1TnczU3BId1QxYm5oQ1hRZEhjdkVjLWtxNElKTGRkNXJMSEd3ZVlVdmdtVTRKeXBVYUtTbnBqdm1MVU1PUDBhZm9ONmxGbm1ENEYwTGFIZTlPa3lGS0JIWEd4WWh3d2ZvX1BTclFwZmNSNC1nWVFnWlJYYWVyTVpRQWdDOEZhZHBfemc5dDZ4U2Y1ZlppUkxtbWptQWd3OS1aTnFDQzV1aDVhZGhoLVE?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
