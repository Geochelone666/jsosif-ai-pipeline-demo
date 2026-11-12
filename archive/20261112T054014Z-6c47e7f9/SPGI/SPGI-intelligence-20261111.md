# SPGI Intelligence Report

- ticker: **SPGI**
- Report as_of: **2026-11-11**
- Market data as_of: **2026-11-11**
- Quant sources: https://finance.yahoo.com/quote/SPGI/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/SPGI/key-statistics/
- AI analysis snapshot as_of: **2026-11-11**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-12T05:49:21.085029+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 11, 'rule': 1, 'ai': 5, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **7** exact headline/source/date matches; prior report **20261111T043601Z-d14951e6/SPGI** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 11 unique headlines; 6 named publishers; 0 exact duplicates; 11 HTTPS source links; largest publisher share 27.27%; oldest publication 2026-11-04

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 475.1100 |
| Return 1D (%) | 0.3655 |
| Return 1W (%) | -1.3660 |
| Return 1M (%) | 16.4999 |
| Return YTD (%) | -3.2390 |
| Return 1Y (%) | 1.7936 |
| Annualized volatility (%) | 30.9427 |
| Beta vs SPY | 0.3521 |
| Max drawdown (%) | -28.4781 |
| Sharpe (rf=0) | 0.2139 |
| Downside deviation (rf=0, %) | 23.0728 |
| Sortino (rf=0) | 0.2869 |
| Historical VaR 95% (1D, %) | 2.8749 |
| Historical ES 95% (1D, %) | 4.6345 |
| Correlation vs SPY | 0.1562 |
| Tracking error vs SPY (%) | 31.8311 |
| P/E (trailing) | 28.28 |
| P/B | 6.99 |
| EV/EBITDA | 18.37 |
| Revenue growth (%) | 6.80 |
| Forward P/E (estimate) | 23.55 |
| Gross margin (%) | 70.99 |
| Operating margin (%) | 44.09 |
| Return on equity (%) | 17.88 |
| Free cash flow yield (%) | 4.38 |
| MA50 | 427.3676 |
| Close vs MA50 (%) | 11.1713 |
| MA200 | 414.5639 |
| Close vs MA200 (%) | 14.6048 |
| RSI (14, Wilder) | 67.5749 |
| MACD (12,26) | 15.0617 |
| MACD signal (9) | 14.4766 |
| MACD histogram | 0.5851 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'SPGI': 280, 'SPY': 280}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 475.1100 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.3655 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -1.3660 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 16.4999 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -3.2390 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 1.7936 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 30.9427 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 23.0728 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.2869 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.8749 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.6345 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.1562 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 31.8311 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.3521 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -28.4781 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.2139 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 23.5486 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 70.9940 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 44.0930 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 17.8760 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 4.3844 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 28.2804 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 67.5749 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.5851 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 11.1713 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 14.6048 -> Clearly above the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

No items in this run

## CATALYSTS

### S&P Global (SPGI) Stock Trades At A Premium To Its Earnings Power
- Summary: S&P Global (SPGI) Stock Trades At A Premium To Its Earnings Power
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxQSkk4Z0g1VkNPLUhfbm9CQ3hxSWNlMnVQMndvemY2S1F0bUdmdVJMczl1R0lpcVU5RGg0bU9ZVjA5U05Vb1o2RWRLU2JXUU5QdGd1MXZxOHZzdklCdW81ZzhpcHBpeWVvbGk4eGoyY3dqTHhFTW84Mlk2Z3JZZk04SXNYLV9BU3pORWotR3M2aVlIYlZ0anc?oc=5>

### S&P Global: The Strong Index Division Hides A Change (NYSE:SPGI)
- Summary: Internal division change at S&P Global.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNZ0ZNaUZNWmdQQjR1NHo3U0dVY1pHZ0dwVHZCYnFWaW5NNXBxS3NndjFRRDRVZVdIa280RDZ1aGJ4R3NFRVBDM3BXNGUxTnJJYTFka0lRanBjVzBMa3YzSG9PcWpBbnJEOVB5eFd4VDBrMzJra3hHQkl2NHo3TWRyQlptOVNKUHlOX0Z1M0hIakRpZFlQOWRCVlFld2g?oc=5>

### S&P Global (SPGI) Is Reviewing A Separation Of Capital IQ
- Summary: S&P Global is evaluating a separation of its Capital IQ unit, potentially restructuring ownership and operations.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxQZ3lTZHM1bDZHRHVhZzlGTXBpYkZSX1JQTzF6WVJPR0toek9mVks0MWRrSkxxZ1FCZlVXSW5TUjBGMnZueXRObWxHYVBHN3FBQ29kMFVGbTN0bXJzUEhpZlIzTDdNQnktLXNWMFZ0VUkxMG8zMkg2MlNtVThPVG96dnFGNkswVlRwY2x6VEZfbFpRVlRUMlpncm1XS3NVWWFl?oc=5>

### S&P Global (SPGI) Could Be 10% Below Fair Value Following Strong Q3 Earnings
- Summary: SPGI may trade below fair value after strong Q3 earnings, indicating a potential market undervaluation.
- Date: 2026-11-07 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxPdVZSellIY2RuUnExVUVOeDFlWUdFbE1PZGJSbFAxdm1NekdiWUxwMy11cUpRa2xCUG93NVhSQ0E2MWJZTVhtWFBUQl9Yc1lkS25VSDc4aHJYaXRXaHdKblFxUE1KZm1LN0pPTDN2MnlFcEFfNFJtX3R0cXNEUnZ1di11SHRwanoyZ2tlbUtONU8?oc=5>

### Is S&P Global (SPGI) Stock Starting To Look Pricey Now?
- Summary: Market perception of SPGI stock price.
- Date: 2026-11-10 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiywFBVV95cUxNLUlMWHFxdjMwZkRiZTQ5RGI5aVphSGN4Zk9VOTk3amc2dnNsdEcwRGE1WFk5cmRsRVFuN21zR05UWDdGLWZaZ240YmFNR0VvdXMtX1JoTHZXRXJjdkk3LTJteWZHbGJmNXNJT0Y1YkpJS2laclZRU1piTTJpenV3MVlIWmtiWjNZMU5saFUtZlFYeWlNV3kxRmVhbjNjU1Q0R1VlbkxnNmFSMk1sUHBZcnJnOFdNQUwwUVRUU2xpekFnellWWVhCU3ZwNNIB0AFBVV95cUxQOFl3VXlXUkVCbWMxWXFEQlcySmFldndHektGaHFMYVpjSUQ3Z056YVd3RmFsMzBWOGdOckVFcGZjYTg0X1E1RWk4OWJ3TG5TYTVCblQ2SWk5OEZNMmVoSE5EUFVUNE9Bc3Azc2hfQThQZTVVc1ZHWUtZZWZWbnM3UFQ2UEFZUjlHR043UnBLYlg1OE1Vem5FMFRiWVJ0cmxFNXhVWUpEaW9SRkJxejNFVUY1WkwycEdJelNLVXV5Ui1ERGFzSGJfV1I1UzA0VEJr?oc=5>

### Earnings Outlook Lift Could Be A Game Changer For S&P Global (SPGI)
- Summary: Positive earnings outlook could significantly boost SPGI’s future performance.
- Date: 2026-11-07 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxQb2dDRDc1Nm5Ud2ZYTlVNVjlXbHBZZkdoOVVSUU9HTXBUbDFkSjJQZDJoOVRrX1A5TjFpeExXNWlheVlIMTJFZ1F0YS1xRzJzcEtFWHhKQlp6Z0NfOGFNV0FmSjI1emE0VjVqMFVjMXJ5clJGdTBMOU5DNHBRRFlyWnRnUFNXWHNXLXVGUmJ3U3NvWXlFVE5MZUlzZ2Z2RU0xSXFueHdlZDdpZVZyeGRxQWc4YU5iWXh6bG1uRmMzVkRRSTZrR0VrTUxmQjJpZmR0YlBZTklR0gHbAUFVX3lxTE54cktiU0gxT3pNSldzU0cyek9BU2p3ZFdJM0NzdFp5TEZlT2J6NEZfMldrREVILThXdUNuaHF4dVhaWjIwNi1rOFVkcWhLMl9fTjduZ2Zja1M5UUd5NjVaZGZBRFZ6Y2d3b05rSDE0RXZZcHNUTzVNNXprMlpkdXowTHZfY1BzU0Y1TGx5SHhBV2hkYkN6eENxdVJUaDZEV0R3WHdYSWp0bndaN3FmRW1vU0Z1TXQ2Sm1mZnEyRnpzZjNnQV9nVHd2enBmY24wdGxSSzlpSHRubGlBNA?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **SPGI** | **28.28** | **6.99** | **18.37** | **6.80** | **137,734,389,760.00 USD** | **1.79** |
| MCO | 31.42 | 27.17 | 23.45 | 0.80 | 88,786,329,600.00 USD | 5.35 |
| MSCI | 34.98 | -15.72 | 26.72 | 12.40 | 47,299,395,584.00 USD | 14.83 |
| FDS | 22.98 | 5.90 | 14.53 | 6.30 | 11,811,174,400.00 USD | 25.53 |

Peers fetched as_of: 2026-11-11; SPGI reuses existing data (market data as_of: 2026-11-11); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-27
- Next expected earnings: 2027-02-09 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-11

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
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

- https://news.google.com/rss/articles/CBMilgFBVV95cUxQSkk4Z0g1VkNPLUhfbm9CQ3hxSWNlMnVQMndvemY2S1F0bUdmdVJMczl1R0lpcVU5RGg0bU9ZVjA5U05Vb1o2RWRLU2JXUU5QdGd1MXZxOHZzdklCdW81ZzhpcHBpeWVvbGk4eGoyY3dqTHhFTW84Mlk2Z3JZZk04SXNYLV9BU3pORWotR3M2aVlIYlZ0anc?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNZ0ZNaUZNWmdQQjR1NHo3U0dVY1pHZ0dwVHZCYnFWaW5NNXBxS3NndjFRRDRVZVdIa280RDZ1aGJ4R3NFRVBDM3BXNGUxTnJJYTFka0lRanBjVzBMa3YzSG9PcWpBbnJEOVB5eFd4VDBrMzJra3hHQkl2NHo3TWRyQlptOVNKUHlOX0Z1M0hIakRpZFlQOWRCVlFld2g?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxQZ3lTZHM1bDZHRHVhZzlGTXBpYkZSX1JQTzF6WVJPR0toek9mVks0MWRrSkxxZ1FCZlVXSW5TUjBGMnZueXRObWxHYVBHN3FBQ29kMFVGbTN0bXJzUEhpZlIzTDdNQnktLXNWMFZ0VUkxMG8zMkg2MlNtVThPVG96dnFGNkswVlRwY2x6VEZfbFpRVlRUMlpncm1XS3NVWWFl?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxPdVZSellIY2RuUnExVUVOeDFlWUdFbE1PZGJSbFAxdm1NekdiWUxwMy11cUpRa2xCUG93NVhSQ0E2MWJZTVhtWFBUQl9Yc1lkS25VSDc4aHJYaXRXaHdKblFxUE1KZm1LN0pPTDN2MnlFcEFfNFJtX3R0cXNEUnZ1di11SHRwanoyZ2tlbUtONU8?oc=5
- https://news.google.com/rss/articles/CBMiywFBVV95cUxNLUlMWHFxdjMwZkRiZTQ5RGI5aVphSGN4Zk9VOTk3amc2dnNsdEcwRGE1WFk5cmRsRVFuN21zR05UWDdGLWZaZ240YmFNR0VvdXMtX1JoTHZXRXJjdkk3LTJteWZHbGJmNXNJT0Y1YkpJS2laclZRU1piTTJpenV3MVlIWmtiWjNZMU5saFUtZlFYeWlNV3kxRmVhbjNjU1Q0R1VlbkxnNmFSMk1sUHBZcnJnOFdNQUwwUVRUU2xpekFnellWWVhCU3ZwNNIB0AFBVV95cUxQOFl3VXlXUkVCbWMxWXFEQlcySmFldndHektGaHFMYVpjSUQ3Z056YVd3RmFsMzBWOGdOckVFcGZjYTg0X1E1RWk4OWJ3TG5TYTVCblQ2SWk5OEZNMmVoSE5EUFVUNE9Bc3Azc2hfQThQZTVVc1ZHWUtZZWZWbnM3UFQ2UEFZUjlHR043UnBLYlg1OE1Vem5FMFRiWVJ0cmxFNXhVWUpEaW9SRkJxejNFVUY1WkwycEdJelNLVXV5Ui1ERGFzSGJfV1I1UzA0VEJr?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxQb2dDRDc1Nm5Ud2ZYTlVNVjlXbHBZZkdoOVVSUU9HTXBUbDFkSjJQZDJoOVRrX1A5TjFpeExXNWlheVlIMTJFZ1F0YS1xRzJzcEtFWHhKQlp6Z0NfOGFNV0FmSjI1emE0VjVqMFVjMXJ5clJGdTBMOU5DNHBRRFlyWnRnUFNXWHNXLXVGUmJ3U3NvWXlFVE5MZUlzZ2Z2RU0xSXFueHdlZDdpZVZyeGRxQWc4YU5iWXh6bG1uRmMzVkRRSTZrR0VrTUxmQjJpZmR0YlBZTklR0gHbAUFVX3lxTE54cktiU0gxT3pNSldzU0cyek9BU2p3ZFdJM0NzdFp5TEZlT2J6NEZfMldrREVILThXdUNuaHF4dVhaWjIwNi1rOFVkcWhLMl9fTjduZ2Zja1M5UUd5NjVaZGZBRFZ6Y2d3b05rSDE0RXZZcHNUTzVNNXprMlpkdXowTHZfY1BzU0Y1TGx5SHhBV2hkYkN6eENxdVJUaDZEV0R3WHdYSWp0bndaN3FmRW1vU0Z1TXQ2Sm1mZnEyRnpzZjNnQV9nVHd2enBmY24wdGxSSzlpSHRubGlBNA?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
