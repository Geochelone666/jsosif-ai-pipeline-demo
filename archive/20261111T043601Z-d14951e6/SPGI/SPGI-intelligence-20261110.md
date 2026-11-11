# SPGI Intelligence Report

- ticker: **SPGI**
- Report as_of: **2026-11-10**
- Market data as_of: **2026-11-10**
- Quant sources: https://finance.yahoo.com/quote/SPGI/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/SPGI/key-statistics/
- AI analysis snapshot as_of: **2026-11-10**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-11T04:47:36.766636+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 12, 'rule': 2, 'ai': 8, 'unknown': 0, 'irrelevant': 2})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **5** exact headline/source/date matches; prior report **20261110T055129Z-abd33250/SPGI** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'directional_claim_without_event_type': 1}
- RSS source audit (metadata only, not article fact-checking): 12 unique headlines; 6 named publishers; 0 exact duplicates; 12 HTTPS source links; largest publisher share 41.67%; oldest publication 2026-11-04

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 473.3800 |
| Return 1D (%) | 0.4861 |
| Return 1W (%) | 1.5772 |
| Return 1M (%) | 16.0757 |
| Return YTD (%) | -3.5914 |
| Return 1Y (%) | 2.2219 |
| Annualized volatility (%) | 30.9503 |
| Beta vs SPY | 0.3535 |
| Max drawdown (%) | -28.4781 |
| Sharpe (rf=0) | 0.2276 |
| Downside deviation (rf=0, %) | 23.0728 |
| Sortino (rf=0) | 0.3053 |
| Historical VaR 95% (1D, %) | 2.8749 |
| Historical ES 95% (1D, %) | 4.6345 |
| Correlation vs SPY | 0.1561 |
| Tracking error vs SPY (%) | 31.8227 |
| P/E (trailing) | 28.14 |
| P/B | 6.96 |
| EV/EBITDA | 18.31 |
| Revenue growth (%) | 6.80 |
| Forward P/E (estimate) | 23.46 |
| Gross margin (%) | 70.99 |
| Operating margin (%) | 48.21 |
| Return on equity (%) | 17.88 |
| Free cash flow yield (%) | 4.40 |
| MA50 | 426.6696 |
| Close vs MA50 (%) | 10.9477 |
| MA200 | 414.6626 |
| Close vs MA200 (%) | 14.1603 |
| RSI (14, Wilder) | 66.8386 |
| MACD (12,26) | 15.2944 |
| MACD signal (9) | 14.3303 |
| MACD histogram | 0.9640 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'SPGI': 279, 'SPY': 279}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 473.3800 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.4861 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 1.5772 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 16.0757 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -3.5914 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 2.2219 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 30.9503 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 23.0728 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.3053 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.8749 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.6345 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.1561 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 31.8227 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.3535 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -28.4781 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.2276 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 23.4629 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 70.9940 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 48.2060 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 17.8760 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 4.4005 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 28.1439 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 66.8386 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.9640 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 10.9477 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 14.1603 -> Clearly above the moving-average trend level.

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

### S&P Global (SPGI) Stock Trades At A Premium To Its Earnings Power
- Summary: S&P Global (SPGI) Stock Trades At A Premium To Its Earnings Power
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxQSkk4Z0g1VkNPLUhfbm9CQ3hxSWNlMnVQMndvemY2S1F0bUdmdVJMczl1R0lpcVU5RGg0bU9ZVjA5U05Vb1o2RWRLU2JXUU5QdGd1MXZxOHZzdklCdW81ZzhpcHBpeWVvbGk4eGoyY3dqTHhFTW84Mlk2Z3JZZk04SXNYLV9BU3pORWotR3M2aVlIYlZ0anc?oc=5>

### S&P Global (SPGI) Is Reviewing A Separation Of Capital IQ
- Summary: S&P Global is evaluating a separation of its Capital IQ unit, potentially restructuring ownership and operations.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxQZ3lTZHM1bDZHRHVhZzlGTXBpYkZSX1JQTzF6WVJPR0toek9mVks0MWRrSkxxZ1FCZlVXSW5TUjBGMnZueXRObWxHYVBHN3FBQ29kMFVGbTN0bXJzUEhpZlIzTDdNQnktLXNWMFZ0VUkxMG8zMkg2MlNtVThPVG96dnFGNkswVlRwY2x6VEZfbFpRVlRUMlpncm1XS3NVWWFl?oc=5>

### S&P Global (SPGI) Could Be 10% Below Fair Value Following Strong Q3 Earnings
- Summary: SPGI may trade below fair value after strong Q3 earnings, indicating a potential market undervaluation.
- Date: 2026-11-07 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxPdVZSellIY2RuUnExVUVOeDFlWUdFbE1PZGJSbFAxdm1NekdiWUxwMy11cUpRa2xCUG93NVhSQ0E2MWJZTVhtWFBUQl9Yc1lkS25VSDc4aHJYaXRXaHdKblFxUE1KZm1LN0pPTDN2MnlFcEFfNFJtX3R0cXNEUnZ1di11SHRwanoyZ2tlbUtONU8?oc=5>

### S&P Global Inc. (SPGI) Stock Forecasts
- Summary: Analysts provide stock forecasts for S&P Global, offering price targets and outlooks.
- Date: 2026-11-09 | Impact: low | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxNdEg3bnBiQmpvVE5oZDNQcjc1UVRzMDJvdHBfTlhoaWk4S1RZdXFVeGtCQzB6VmZqSE94TG53S0p0Q1hpRjZzcnBnNGN0R2ZGZHJSTFBLWTBUSUt3OS0xbFI3eS1EVEw5RXZ0STVuWlZ5YTBTdklBMGtJU1Q1SFVEMG9keGRzc05KVGRkbA?oc=5>

### Earnings Outlook Lift Could Be A Game Changer For S&P Global (SPGI)
- Summary: Positive earnings outlook could significantly boost SPGI’s future performance.
- Date: 2026-11-07 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxQb2dDRDc1Nm5Ud2ZYTlVNVjlXbHBZZkdoOVVSUU9HTXBUbDFkSjJQZDJoOVRrX1A5TjFpeExXNWlheVlIMTJFZ1F0YS1xRzJzcEtFWHhKQlp6Z0NfOGFNV0FmSjI1emE0VjVqMFVjMXJ5clJGdTBMOU5DNHBRRFlyWnRnUFNXWHNXLXVGUmJ3U3NvWXlFVE5MZUlzZ2Z2RU0xSXFueHdlZDdpZVZyeGRxQWc4YU5iWXh6bG1uRmMzVkRRSTZrR0VrTUxmQjJpZmR0YlBZTklR0gHbAUFVX3lxTE54cktiU0gxT3pNSldzU0cyek9BU2p3ZFdJM0NzdFp5TEZlT2J6NEZfMldrREVILThXdUNuaHF4dVhaWjIwNi1rOFVkcWhLMl9fTjduZ2Zja1M5UUd5NjVaZGZBRFZ6Y2d3b05rSDE0RXZZcHNUTzVNNXprMlpkdXowTHZfY1BzU0Y1TGx5SHhBV2hkYkN6eENxdVJUaDZEV0R3WHdYSWp0bndaN3FmRW1vU0Z1TXQ2Sm1mZnEyRnpzZjNnQV9nVHd2enBmY24wdGxSSzlpSHRubGlBNA?oc=5>

### S&P Global: The Strong Index Division Hides A Change (NYSE:SPGI)
- Summary: Internal division change at S&P Global.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNZ0ZNaUZNWmdQQjR1NHo3U0dVY1pHZ0dwVHZCYnFWaW5NNXBxS3NndjFRRDRVZVdIa280RDZ1aGJ4R3NFRVBDM3BXNGUxTnJJYTFka0lRanBjVzBMa3YzSG9PcWpBbnJEOVB5eFd4VDBrMzJra3hHQkl2NHo3TWRyQlptOVNKUHlOX0Z1M0hIakRpZFlQOWRCVlFld2g?oc=5>

### S&P Global (SPGI) Opened a Strategic Review of Capital IQ. Here’s What CEO Martina Cheung Said
- Summary: Strategic review of Capital IQ division.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxQa3JvVl9SN05Ib2d5SWx2VXFKUl93aGluS1Z0eDBKNFlUMlhDMmJfcXdEb2VIUVhYaTNZSmZtV0ljVHhDWkJKbnR4NUVYVXVVSVNURmVJTExHSFV4ZGp6MUlCTVZRRUJkV1NZRTEzbVJZTTZncHhGLUR6X3d0S0IyYTdLY2FpV3NybjVWWFN1endqbFo2R2hHRGRn?oc=5>

### Is S&P Global (SPGI) Stock Starting To Look Pricey Now?
- Summary: Market perception of SPGI stock price.
- Date: 2026-11-10 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiywFBVV95cUxNLUlMWHFxdjMwZkRiZTQ5RGI5aVphSGN4Zk9VOTk3amc2dnNsdEcwRGE1WFk5cmRsRVFuN21zR05UWDdGLWZaZ240YmFNR0VvdXMtX1JoTHZXRXJjdkk3LTJteWZHbGJmNXNJT0Y1YkpJS2laclZRU1piTTJpenV3MVlIWmtiWjNZMU5saFUtZlFYeWlNV3kxRmVhbjNjU1Q0R1VlbkxnNmFSMk1sUHBZcnJnOFdNQUwwUVRUU2xpekFnellWWVhCU3ZwNNIB0AFBVV95cUxQOFl3VXlXUkVCbWMxWXFEQlcySmFldndHektGaHFMYVpjSUQ3Z056YVd3RmFsMzBWOGdOckVFcGZjYTg0X1E1RWk4OWJ3TG5TYTVCblQ2SWk5OEZNMmVoSE5EUFVUNE9Bc3Azc2hfQThQZTVVc1ZHWUtZZWZWbnM3UFQ2UEFZUjlHR043UnBLYlg1OE1Vem5FMFRiWVJ0cmxFNXhVWUpEaW9SRkJxejNFVUY1WkwycEdJelNLVXV5Ui1ERGFzSGJfV1I1UzA0VEJr?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **SPGI** | **28.14** | **6.96** | **18.31** | **6.80** | **137,232,867,328.00 USD** | **2.22** |
| MCO | 31.16 | 26.95 | 23.27 | 0.80 | 88,058,699,776.00 USD | 6.23 |
| MSCI | 34.74 | -15.61 | 26.55 | 12.40 | 47,753,719,808.00 USD | 15.48 |
| FDS | 22.37 | 5.74 | 14.18 | 6.30 | 11,497,273,344.00 USD | 25.17 |

Peers fetched as_of: 2026-11-10; SPGI reuses existing data (market data as_of: 2026-11-10); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-27
- Next expected earnings: 2027-02-09 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-10

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

- https://news.google.com/rss/articles/CBMiqgFBVV95cUxNY0NSSEM0anBJYWg2TkduT0Q0TmE0cFJlZ0dudUpYNVZaOFdRY1VJd1lWeS1COFROVWdVeE4tMzNwTTdLcUthWFJZVEFjS3JtWXNWUEtmOUFldlhic0dfTW1ZYW5QaWdCWG5ZSGlaX2lNNklCSFdBSm14aXVTNEIzSWtVRDRXLXdGMVhISU1VVzBxX3g2bGZTR2UtcmExaS1VVS13S3pNWGpvQQ?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxQd3dFNUo5YTJMdzdlV0pENWgtYTdxNElxU00xdUxfMGZ0WTBMdjJlekR0TEd1VEZXQ1ZFbXJURmlsRGFzS0dsNm1oVzFLM2Z0clpjYmdoRFh6YWVrQjhMNHh3ODdoTHc5ZFBvcHNON254RUtjbHZMTTdFampXU0x5Zm8zVWpyMkZ0ME5yTlZiT0FKc2Va?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxQSkk4Z0g1VkNPLUhfbm9CQ3hxSWNlMnVQMndvemY2S1F0bUdmdVJMczl1R0lpcVU5RGg0bU9ZVjA5U05Vb1o2RWRLU2JXUU5QdGd1MXZxOHZzdklCdW81ZzhpcHBpeWVvbGk4eGoyY3dqTHhFTW84Mlk2Z3JZZk04SXNYLV9BU3pORWotR3M2aVlIYlZ0anc?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxQZ3lTZHM1bDZHRHVhZzlGTXBpYkZSX1JQTzF6WVJPR0toek9mVks0MWRrSkxxZ1FCZlVXSW5TUjBGMnZueXRObWxHYVBHN3FBQ29kMFVGbTN0bXJzUEhpZlIzTDdNQnktLXNWMFZ0VUkxMG8zMkg2MlNtVThPVG96dnFGNkswVlRwY2x6VEZfbFpRVlRUMlpncm1XS3NVWWFl?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxPdVZSellIY2RuUnExVUVOeDFlWUdFbE1PZGJSbFAxdm1NekdiWUxwMy11cUpRa2xCUG93NVhSQ0E2MWJZTVhtWFBUQl9Yc1lkS25VSDc4aHJYaXRXaHdKblFxUE1KZm1LN0pPTDN2MnlFcEFfNFJtX3R0cXNEUnZ1di11SHRwanoyZ2tlbUtONU8?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxNdEg3bnBiQmpvVE5oZDNQcjc1UVRzMDJvdHBfTlhoaWk4S1RZdXFVeGtCQzB6VmZqSE94TG53S0p0Q1hpRjZzcnBnNGN0R2ZGZHJSTFBLWTBUSUt3OS0xbFI3eS1EVEw5RXZ0STVuWlZ5YTBTdklBMGtJU1Q1SFVEMG9keGRzc05KVGRkbA?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxQb2dDRDc1Nm5Ud2ZYTlVNVjlXbHBZZkdoOVVSUU9HTXBUbDFkSjJQZDJoOVRrX1A5TjFpeExXNWlheVlIMTJFZ1F0YS1xRzJzcEtFWHhKQlp6Z0NfOGFNV0FmSjI1emE0VjVqMFVjMXJ5clJGdTBMOU5DNHBRRFlyWnRnUFNXWHNXLXVGUmJ3U3NvWXlFVE5MZUlzZ2Z2RU0xSXFueHdlZDdpZVZyeGRxQWc4YU5iWXh6bG1uRmMzVkRRSTZrR0VrTUxmQjJpZmR0YlBZTklR0gHbAUFVX3lxTE54cktiU0gxT3pNSldzU0cyek9BU2p3ZFdJM0NzdFp5TEZlT2J6NEZfMldrREVILThXdUNuaHF4dVhaWjIwNi1rOFVkcWhLMl9fTjduZ2Zja1M5UUd5NjVaZGZBRFZ6Y2d3b05rSDE0RXZZcHNUTzVNNXprMlpkdXowTHZfY1BzU0Y1TGx5SHhBV2hkYkN6eENxdVJUaDZEV0R3WHdYSWp0bndaN3FmRW1vU0Z1TXQ2Sm1mZnEyRnpzZjNnQV9nVHd2enBmY24wdGxSSzlpSHRubGlBNA?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNZ0ZNaUZNWmdQQjR1NHo3U0dVY1pHZ0dwVHZCYnFWaW5NNXBxS3NndjFRRDRVZVdIa280RDZ1aGJ4R3NFRVBDM3BXNGUxTnJJYTFka0lRanBjVzBMa3YzSG9PcWpBbnJEOVB5eFd4VDBrMzJra3hHQkl2NHo3TWRyQlptOVNKUHlOX0Z1M0hIakRpZFlQOWRCVlFld2g?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxQa3JvVl9SN05Ib2d5SWx2VXFKUl93aGluS1Z0eDBKNFlUMlhDMmJfcXdEb2VIUVhYaTNZSmZtV0ljVHhDWkJKbnR4NUVYVXVVSVNURmVJTExHSFV4ZGp6MUlCTVZRRUJkV1NZRTEzbVJZTTZncHhGLUR6X3d0S0IyYTdLY2FpV3NybjVWWFN1endqbFo2R2hHRGRn?oc=5
- https://news.google.com/rss/articles/CBMiywFBVV95cUxNLUlMWHFxdjMwZkRiZTQ5RGI5aVphSGN4Zk9VOTk3amc2dnNsdEcwRGE1WFk5cmRsRVFuN21zR05UWDdGLWZaZ240YmFNR0VvdXMtX1JoTHZXRXJjdkk3LTJteWZHbGJmNXNJT0Y1YkpJS2laclZRU1piTTJpenV3MVlIWmtiWjNZMU5saFUtZlFYeWlNV3kxRmVhbjNjU1Q0R1VlbkxnNmFSMk1sUHBZcnJnOFdNQUwwUVRUU2xpekFnellWWVhCU3ZwNNIB0AFBVV95cUxQOFl3VXlXUkVCbWMxWXFEQlcySmFldndHektGaHFMYVpjSUQ3Z056YVd3RmFsMzBWOGdOckVFcGZjYTg0X1E1RWk4OWJ3TG5TYTVCblQ2SWk5OEZNMmVoSE5EUFVUNE9Bc3Azc2hfQThQZTVVc1ZHWUtZZWZWbnM3UFQ2UEFZUjlHR043UnBLYlg1OE1Vem5FMFRiWVJ0cmxFNXhVWUpEaW9SRkJxejNFVUY1WkwycEdJelNLVXV5Ui1ERGFzSGJfV1I1UzA0VEJr?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
