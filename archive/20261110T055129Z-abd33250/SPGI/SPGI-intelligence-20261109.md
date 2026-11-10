# SPGI Intelligence Report

- ticker: **SPGI**
- Report as_of: **2026-11-09**
- Market data as_of: **2026-11-09**
- Quant sources: https://finance.yahoo.com/quote/SPGI/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/SPGI/key-statistics/
- AI analysis snapshot as_of: **2026-11-09**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-10T06:15:11.154353+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 8, 'rule': 1, 'ai': 7, 'unknown': 0})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **3** exact headline/source/date matches; prior report **20261109T043242Z-c8e908de/SPGI** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'directional_claim_without_event_type': 1}
- RSS source audit (metadata only, not article fact-checking): 8 unique headlines; 5 named publishers; 0 exact duplicates; 8 HTTPS source links; largest publisher share 50.0%; oldest publication 2026-11-04

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 471.0900 |
| Return 1D (%) | 0.7033 |
| Return 1W (%) | -0.8586 |
| Return 1M (%) | 15.5142 |
| Return YTD (%) | -4.0577 |
| Return 1Y (%) | 1.1987 |
| Annualized volatility (%) | 31.0089 |
| Beta vs SPY | 0.3549 |
| Max drawdown (%) | -28.4781 |
| Sharpe (rf=0) | 0.2122 |
| Downside deviation (rf=0, %) | 23.1189 |
| Sortino (rf=0) | 0.2847 |
| Historical VaR 95% (1D, %) | 2.8767 |
| Historical ES 95% (1D, %) | 4.6345 |
| Correlation vs SPY | 0.1567 |
| Tracking error vs SPY (%) | 31.8744 |
| P/E (trailing) | 28.14 |
| P/B | 6.93 |
| EV/EBITDA | 18.23 |
| Revenue growth (%) | 6.80 |
| Forward P/E (estimate) | 23.35 |
| Gross margin (%) | 70.99 |
| Operating margin (%) | 48.21 |
| Return on equity (%) | 17.88 |
| Free cash flow yield (%) | 4.42 |
| MA50 | 425.9188 |
| Close vs MA50 (%) | 10.6056 |
| MA200 | 414.8102 |
| Close vs MA200 (%) | 13.5676 |
| RSI (14, Wilder) | 65.8864 |
| MACD (12,26) | 15.5450 |
| MACD signal (9) | 14.0893 |
| MACD histogram | 1.4557 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'SPGI': 278, 'SPY': 278}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 471.0900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.7033 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -0.8586 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 15.5142 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -4.0577 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 1.1987 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 31.0089 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 23.1189 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.2847 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.8767 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.6345 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.1567 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 31.8744 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.3549 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -28.4781 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.2122 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 23.3494 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 70.9940 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 48.2060 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 17.8760 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 4.4218 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 28.1416 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 65.8864 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 1.4557 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 10.6056 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 13.5676 -> Clearly above the moving-average trend level.

## TAILWINDS

### S&P Global Inc (SPGI) Stock Up 3.4% and Still Undervalued -- GF Score: 94/100
- Summary: S&P Global Inc (SPGI) Stock Up 3.4% and Still Undervalued -- GF Score: 94/100
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxNY0NSSEM0anBJYWg2TkduT0Q0TmE0cFJlZ0dudUpYNVZaOFdRY1VJd1lWeS1COFROVWdVeE4tMzNwTTdLcUthWFJZVEFjS3JtWXNWUEtmOUFldlhic0dfTW1ZYW5QaWdCWG5ZSGlaX2lNNklCSFdBSm14aXVTNEIzSWtVRDRXLXdGMVhISU1VVzBxX3g2bGZTR2UtcmExaS1VVS13S3pNWGpvQQ?oc=5>

### S&P Global Inc. (SPGI) Remains a Key Player in Financial Markets: Is Its Competitive Edge Underestimated?
- Summary: Highlights SPGI’s strong market position and suggests its competitive advantage may be undervalued.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxQd3dFNUo5YTJMdzdlV0pENWgtYTdxNElxU00xdUxfMGZ0WTBMdjJlekR0TEd1VEZXQ1ZFbXJURmlsRGFzS0dsNm1oVzFLM2Z0clpjYmdoRFh6YWVrQjhMNHh3ODdoTHc5ZFBvcHNON254RUtjbHZMTTdFampXU0x5Zm8zVWpyMkZ0ME5yTlZiT0FKc2Va?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### S&P Global (SPGI) Could Be 10% Below Fair Value Following Strong Q3 Earnings
- Summary: SPGI may trade below fair value after strong Q3 earnings, indicating a potential market undervaluation.
- Date: 2026-11-07 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxPdVZSellIY2RuUnExVUVOeDFlWUdFbE1PZGJSbFAxdm1NekdiWUxwMy11cUpRa2xCUG93NVhSQ0E2MWJZTVhtWFBUQl9Yc1lkS25VSDc4aHJYaXRXaHdKblFxUE1KZm1LN0pPTDN2MnlFcEFfNFJtX3R0cXNEUnZ1di11SHRwanoyZ2tlbUtONU8?oc=5>

### Earnings Outlook Lift Could Be A Game Changer For S&P Global (SPGI)
- Summary: Positive earnings outlook could significantly boost SPGI’s future performance.
- Date: 2026-11-07 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxQb2dDRDc1Nm5Ud2ZYTlVNVjlXbHBZZkdoOVVSUU9HTXBUbDFkSjJQZDJoOVRrX1A5TjFpeExXNWlheVlIMTJFZ1F0YS1xRzJzcEtFWHhKQlp6Z0NfOGFNV0FmSjI1emE0VjVqMFVjMXJ5clJGdTBMOU5DNHBRRFlyWnRnUFNXWHNXLXVGUmJ3U3NvWXlFVE5MZUlzZ2Z2RU0xSXFueHdlZDdpZVZyeGRxQWc4YU5iWXh6bG1uRmMzVkRRSTZrR0VrTUxmQjJpZmR0YlBZTklR0gHbAUFVX3lxTE54cktiU0gxT3pNSldzU0cyek9BU2p3ZFdJM0NzdFp5TEZlT2J6NEZfMldrREVILThXdUNuaHF4dVhaWjIwNi1rOFVkcWhLMl9fTjduZ2Zja1M5UUd5NjVaZGZBRFZ6Y2d3b05rSDE0RXZZcHNUTzVNNXprMlpkdXowTHZfY1BzU0Y1TGx5SHhBV2hkYkN6eENxdVJUaDZEV0R3WHdYSWp0bndaN3FmRW1vU0Z1TXQ2Sm1mZnEyRnpzZjNnQV9nVHd2enBmY24wdGxSSzlpSHRubGlBNA?oc=5>

### S&P Global (SPGI) Is Reviewing A Separation Of Capital IQ
- Summary: S&P Global is evaluating a separation of its Capital IQ unit, potentially restructuring ownership and operations.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxQZ3lTZHM1bDZHRHVhZzlGTXBpYkZSX1JQTzF6WVJPR0toek9mVks0MWRrSkxxZ1FCZlVXSW5TUjBGMnZueXRObWxHYVBHN3FBQ29kMFVGbTN0bXJzUEhpZlIzTDdNQnktLXNWMFZ0VUkxMG8zMkg2MlNtVThPVG96dnFGNkswVlRwY2x6VEZfbFpRVlRUMlpncm1XS3NVWWFl?oc=5>

### The Secret Billionaire Backing S&P Global (SPGI) Alongside Bill Ackman
- Summary: A private billionaire is backing S&P Global alongside Bill Ackman, indicating potential investment interest.
- Date: 2026-11-07 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxQdXBQNEJZVmgzWV9hMVpqSmJDTnRvS29xYmpEVGFITjM2ZEs0MW8zUGZfODYzcnpXWUhvemQwSDJ0QzY4RzE0SlljYlNEbkdqeV80d1ZPeGdfNWdMc0RLeTdYdV9LUXpkN2pLYTFCYnZPUjdmTU1jOTNFMm1DZUVoNGtWMUN4NW5sMUhiUURScWxJOURiNVRnYWlydGZKWjZKVlE?oc=5>

### S&P Global Inc. (SPGI) Stock Forecasts
- Summary: Analysts provide stock forecasts for S&P Global, offering price targets and outlooks.
- Date: 2026-11-09 | Impact: low | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxNdEg3bnBiQmpvVE5oZDNQcjc1UVRzMDJvdHBfTlhoaWk4S1RZdXFVeGtCQzB6VmZqSE94TG53S0p0Q1hpRjZzcnBnNGN0R2ZGZHJSTFBLWTBUSUt3OS0xbFI3eS1EVEw5RXZ0STVuWlZ5YTBTdklBMGtJU1Q1SFVEMG9keGRzc05KVGRkbA?oc=5>

### Analysts Offer Insights on Financial Companies: S&P Global (SPGI) and Western Union (WU)
- Summary: Analysts discuss S&P Global and Western Union, providing market insights and potential investment considerations.
- Date: 2026-11-06 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi-wFBVV95cUxPQjRPSG5yUGhXeWxndDVKZnBYelZHMERSa09NYlpJZkFacUFIcm1vSnc2NF83dWZnRXg4ZXR1Umk5VGtYUEIzb3h0NnZhdV9OLVpBa3YwNU1oZ2ZEZktkWUl2UXRWTEFfZ09MRy13LVNPMHpqalBWQXBlcjlaNmpXYTljZVNYLVFiNXYzZ2NIdUxxbWhWTTFicTU3cGlqQ21IUXU0eGxRX1p6bjVrLXBoT2N5NzZLTEpORmUtb0dKMm0tb3dBaFI3MmZZTG56amtFLTluRXl1dzlweDlFdDg0SDk4eFVnTTE2YkNwWmRsU0UzbmpvblRlVjRMdw?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **SPGI** | **28.14** | **6.93** | **18.23** | **6.80** | **136,568,987,648.00 USD** | **1.20** |
| MCO | 31.18 | 26.97 | 23.28 | 0.80 | 88,122,499,072.00 USD | 5.64 |
| MSCI | 34.19 | -15.37 | 26.18 | 12.40 | 46,996,914,176.00 USD | 12.50 |
| FDS | 22.42 | 5.75 | 14.21 | 6.30 | 11,523,373,056.00 USD | 26.65 |

Peers fetched as_of: 2026-11-09; SPGI reuses existing data (market data as_of: 2026-11-09); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-27
- Next expected earnings: 2027-02-09 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-09

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
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

- https://news.google.com/rss/articles/CBMiqgFBVV95cUxNY0NSSEM0anBJYWg2TkduT0Q0TmE0cFJlZ0dudUpYNVZaOFdRY1VJd1lWeS1COFROVWdVeE4tMzNwTTdLcUthWFJZVEFjS3JtWXNWUEtmOUFldlhic0dfTW1ZYW5QaWdCWG5ZSGlaX2lNNklCSFdBSm14aXVTNEIzSWtVRDRXLXdGMVhISU1VVzBxX3g2bGZTR2UtcmExaS1VVS13S3pNWGpvQQ?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxQd3dFNUo5YTJMdzdlV0pENWgtYTdxNElxU00xdUxfMGZ0WTBMdjJlekR0TEd1VEZXQ1ZFbXJURmlsRGFzS0dsNm1oVzFLM2Z0clpjYmdoRFh6YWVrQjhMNHh3ODdoTHc5ZFBvcHNON254RUtjbHZMTTdFampXU0x5Zm8zVWpyMkZ0ME5yTlZiT0FKc2Va?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxPdVZSellIY2RuUnExVUVOeDFlWUdFbE1PZGJSbFAxdm1NekdiWUxwMy11cUpRa2xCUG93NVhSQ0E2MWJZTVhtWFBUQl9Yc1lkS25VSDc4aHJYaXRXaHdKblFxUE1KZm1LN0pPTDN2MnlFcEFfNFJtX3R0cXNEUnZ1di11SHRwanoyZ2tlbUtONU8?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxQb2dDRDc1Nm5Ud2ZYTlVNVjlXbHBZZkdoOVVSUU9HTXBUbDFkSjJQZDJoOVRrX1A5TjFpeExXNWlheVlIMTJFZ1F0YS1xRzJzcEtFWHhKQlp6Z0NfOGFNV0FmSjI1emE0VjVqMFVjMXJ5clJGdTBMOU5DNHBRRFlyWnRnUFNXWHNXLXVGUmJ3U3NvWXlFVE5MZUlzZ2Z2RU0xSXFueHdlZDdpZVZyeGRxQWc4YU5iWXh6bG1uRmMzVkRRSTZrR0VrTUxmQjJpZmR0YlBZTklR0gHbAUFVX3lxTE54cktiU0gxT3pNSldzU0cyek9BU2p3ZFdJM0NzdFp5TEZlT2J6NEZfMldrREVILThXdUNuaHF4dVhaWjIwNi1rOFVkcWhLMl9fTjduZ2Zja1M5UUd5NjVaZGZBRFZ6Y2d3b05rSDE0RXZZcHNUTzVNNXprMlpkdXowTHZfY1BzU0Y1TGx5SHhBV2hkYkN6eENxdVJUaDZEV0R3WHdYSWp0bndaN3FmRW1vU0Z1TXQ2Sm1mZnEyRnpzZjNnQV9nVHd2enBmY24wdGxSSzlpSHRubGlBNA?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxQZ3lTZHM1bDZHRHVhZzlGTXBpYkZSX1JQTzF6WVJPR0toek9mVks0MWRrSkxxZ1FCZlVXSW5TUjBGMnZueXRObWxHYVBHN3FBQ29kMFVGbTN0bXJzUEhpZlIzTDdNQnktLXNWMFZ0VUkxMG8zMkg2MlNtVThPVG96dnFGNkswVlRwY2x6VEZfbFpRVlRUMlpncm1XS3NVWWFl?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxQdXBQNEJZVmgzWV9hMVpqSmJDTnRvS29xYmpEVGFITjM2ZEs0MW8zUGZfODYzcnpXWUhvemQwSDJ0QzY4RzE0SlljYlNEbkdqeV80d1ZPeGdfNWdMc0RLeTdYdV9LUXpkN2pLYTFCYnZPUjdmTU1jOTNFMm1DZUVoNGtWMUN4NW5sMUhiUURScWxJOURiNVRnYWlydGZKWjZKVlE?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxNdEg3bnBiQmpvVE5oZDNQcjc1UVRzMDJvdHBfTlhoaWk4S1RZdXFVeGtCQzB6VmZqSE94TG53S0p0Q1hpRjZzcnBnNGN0R2ZGZHJSTFBLWTBUSUt3OS0xbFI3eS1EVEw5RXZ0STVuWlZ5YTBTdklBMGtJU1Q1SFVEMG9keGRzc05KVGRkbA?oc=5
- https://news.google.com/rss/articles/CBMi-wFBVV95cUxPQjRPSG5yUGhXeWxndDVKZnBYelZHMERSa09NYlpJZkFacUFIcm1vSnc2NF83dWZnRXg4ZXR1Umk5VGtYUEIzb3h0NnZhdV9OLVpBa3YwNU1oZ2ZEZktkWUl2UXRWTEFfZ09MRy13LVNPMHpqalBWQXBlcjlaNmpXYTljZVNYLVFiNXYzZ2NIdUxxbWhWTTFicTU3cGlqQ21IUXU0eGxRX1p6bjVrLXBoT2N5NzZLTEpORmUtb0dKMm0tb3dBaFI3MmZZTG56amtFLTluRXl1dzlweDlFdDg0SDk4eFVnTTE2YkNwWmRsU0UzbmpvblRlVjRMdw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
