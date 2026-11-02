# VRTX Intelligence Report

- ticker: **VRTX**
- Report as_of: **2026-11-01**
- Market data as_of: **2026-10-30**
- Quant sources: https://finance.yahoo.com/quote/VRTX/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/VRTX/key-statistics/
- AI analysis snapshot as_of: **2026-11-01**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-02T04:32:09.968441+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 12, 'rule': 2, 'ai': 5, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **7** exact headline/source/date matches; prior report **20261101T014405Z-e49d1192/VRTX** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'directional_claim_without_event_type': 1, 'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 12 unique headlines; 6 named publishers; 0 exact duplicates; 12 HTTPS source links; largest publisher share 50.0%; oldest publication 2026-10-26

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 558.8800 |
| Return 1D (%) | 3.4963 |
| Return 1W (%) | 6.6707 |
| Return 1M (%) | 6.8993 |
| Return YTD (%) | 23.2751 |
| Return 1Y (%) | 33.1015 |
| Annualized volatility (%) | 29.3714 |
| Beta vs SPY | 0.4502 |
| Max drawdown (%) | -15.2113 |
| Sharpe (rf=0) | 1.1228 |
| Downside deviation (rf=0, %) | 17.8438 |
| Sortino (rf=0) | 1.8482 |
| Historical VaR 95% (1D, %) | 2.6839 |
| Historical ES 95% (1D, %) | 3.4058 |
| Correlation vs SPY | 0.1960 |
| Tracking error vs SPY (%) | 29.6472 |
| P/E (trailing) | 32.55 |
| P/B | 6.99 |
| EV/EBITDA | 26.62 |
| Revenue growth (%) | 12.50 |
| Forward P/E (estimate) | 27.37 |
| Gross margin (%) | 54.96 |
| Operating margin (%) | 38.05 |
| Return on equity (%) | 23.54 |
| Free cash flow yield (%) | 1.86 |
| MA50 | 523.2144 |
| Close vs MA50 (%) | 6.8166 |
| MA200 | 479.2140 |
| Close vs MA200 (%) | 16.6243 |
| RSI (14, Wilder) | 67.6523 |
| MACD (12,26) | 6.6102 |
| MACD signal (9) | 1.5814 |
| MACD histogram | 5.0288 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'VRTX': 272, 'SPY': 272}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 558.8800 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 3.4963 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 6.6707 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 6.8993 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 23.2751 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 33.1015 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 29.3714 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 17.8438 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.8482 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.6839 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.4058 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.1960 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 29.6472 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.4502 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -15.2113 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.1228 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 27.3710 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 54.9570 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 38.0550 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 23.5430 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.8551 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 32.5498 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 67.6523 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 5.0288 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 6.8166 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 16.6243 -> Clearly above the moving-average trend level.

## TAILWINDS

### Here is What to Know Beyond Why Vertex Pharmaceuticals Incorporated (VRTX) is a Trending Stock
- Summary: General information about Vertex’s trending status.
- Date: 2026-10-28 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxQQVdrekpkclVkTF93RUxySVd2Tm0tYmJibzdpUUNLdlZuZTlwM1A3NWxjcWpxbkNaOEhBUkVSaTcyOVdSd3Zvd29xT3dFMXpYb0N4eEl0MkN0U25BdERES0ZpbG5tTVdOemQxc0lwaVBOVjI3WTB5aERPbndUYWVqMVpzRW1rQnoyVlo4N2VrbzhIZHlXQk9YZExXQnBtMjJFZ0VrUzZR?oc=5>

### Vertex Pharmaceuticals (VRTX) Stock Could Stay Below Fair Value Despite Its 173% Run
- Summary: Predicts VRTX stock may remain undervalued.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMi7AFBVV95cUxPaHpyVVgwQjlCOElOZjJKN3ZLbHJVVV9MMFVoVF8xVWFmUVVzOGlDem9FMnNDek9uSVFKRWd6RGRzTWRRNXFYd0xLQXNjcldEQS1UQ2N6c0NGV2ZobUNOaEVvMFhyZ0ZxU2x2c0psbUdtTi1XY2hvb3VLSFBnQk9JZXdGS1ZfeFdCcE5yVGlTS3JDYlJQS0lPcW13U0JqdkI4eEdIN243dW1QLUpnWU1SaDNNeVFHX2dSZ2lSeGJLYnVOOXdzOGdvbnJvak5jai1nWHJDVmstY2JWSjJWa2VxTkhOMExCVUp5cGdiZNIB8gFBVV95cUxORVdwSVByZlRQa3ZpVVhVVFFRbDIyQ0dMYmdRT3BOTE41RnQ0V0dRdDZNdEFIYmkyRnJzdWwyV3BDUzJFTkhkQUtydzVNYnVJRl9lTUZLU1pZR3hfOVBXVWVYMERTS1M0bDdJdVFfMk1uaU05dkl5ZFRRV2pSTW1wZlpEZlJkeDJWeWE4NGM1TFhaUWQwVHBpajBqVkx0dFltbFpvZzlTeG9nTUFFdWNnOHNLcUpEOGxvUXEtSm56VXliU29SVHl2aHlzQUc0U0JpcWluN1VXSzRRYUM1di1jREd2RkRhX3NLaTlFS1JkVzR2QQ?oc=5>

## HEADWINDS

### Vertex Pharmaceuticals (VRTX) Stock Sinks As Market Gains: Here's Why
- Summary: Stock price decline amid broader market gains indicates negative sentiment for the company.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxPOEVKaXlSbjNjRTEwSDRGODcyR0VTV1B3bmZPbU45ejBOZ0E0RERDRmdwVVBySUZkN0NmOWxjQS10QWNyOVhWWTZJaE5VSWppZVhDMnhGSUs3bFZtUHhSLUlHbVRuOEo1bmdCTkk2cENuV1doMGZmTXJ4cXozMXo4S25MeHB5V3JqVlBnVXlRM19kbTlMdno5SVlTQUgwSXRPZjI5Q0szQQ?oc=5>

## CATALYSTS

### Vertex Pharmaceuticals (VRTX) Set to Report Q3 Earnings on Novem
- Summary: Vertex Pharmaceuticals (VRTX) Set to Report Q3 Earnings on Novem
- Date: 2026-11-01 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxNMUcySXV6cmhUVzl1X0tzWTNKbFNfaERVQzMxQ2JTbWxXX0ZrQW5rTHlBWGNMWTFCLXBKQzhWSWtBTnZFOHd6TzJqcmpBZDFWb3dtb0pZT2RuSDNKY2hhb0NSYnBYTUZZblBULXpEMm1Rd3dOMGVpN1BKUWs3S296YmZEX0pBRnVwVEE4UDZFWDJCdnAySzZyX20zZE15ZGhkYjhscjZYN3FVQQ?oc=5>

### Vertex Pharmaceuticals earnings: what to look for from VRTX
- Summary: Vertex Pharmaceuticals earnings: what to look for from VRTX
- Date: 2026-11-01 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxOd0N4VUVaYjRYaHphMkxPZEZjSkZJdFBTQ1BzYUVpcVVoRVZILXpmNWxkU1BqcWxPQkZLT21JLUhHNWFSalRWQjJpVEJSSWRsM3RjTER3SUdCWmxhWE1BMFJtZzVBWnZEaUNYUWtlOVJjVE5GUHZvam9veERwSlJXcjh1YnBDTEZqQkY0WjVwdzVyVXk4MG1YUjdmYi1uenpsbVRpbUtITmtIQUNnMWcxSG1UalJTeXF4WU93?oc=5>

### Ahead of Vertex (VRTX) Q3 Earnings: Get Ready With Wall Street Estimates for Key Metrics
- Summary: Upcoming Q3 earnings estimates.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxQdXJROFhGNXJCQTZoUDlrdDJoU2FieHZidWZmNTY0X2I3WVRoVDYtaEY4ZnhUdTc4VEpmekVJTlh1V3ZFeVd4VjcwdVdhZkpiaDlXdXlxc2ZfQ1NsUm43cl9oRTlONXVyYkp3Z0hXbE9zOG5EdThfM3F4amhWM0RyUHFwN3M5bGVxcUR3R3R4NUxKVG5KSDZVMmhn?oc=5>

### Vertex Pharmaceuticals (VRTX) Earnings Expected to Grow: Should You Buy?
- Summary: Anticipated earnings growth may boost investor interest and stock performance.
- Date: 2026-10-26 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxPLWpRMzlmMXJhdl90d0llcXVVOFJEMlQ5ZXhJaGlhajlJVlZUeG0yVGZwU3JObzFtMTJIVE00ZUdwWXd5YWZBRm5qWGJwTkU3em9YNXFkSXVsYmJTemVBb1JMQnZXRmRUSXczMHhfLWYyRDhNWEF0LWVKaEZ1X01oODkySEgwSTN6bWQtMmluRUx0ZTNXOXZFOVFTT3VyYnRNSXB6bXBnYV9UV3V1YXJ3?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **VRTX** | **32.55** | **6.99** | **26.62** | **12.50** | **141,654,245,376.00 USD** | **33.10** |
| REGN | 20.51 | 2.78 | 15.32 | 36.30 | 95,988,236,288.00 USD | 42.60 |
| BIIB | 109.79 | 1.98 | 13.32 | 10.60 | 37,490,163,712.00 USD | 69.52 |
| AMGN | 28.94 | 21.55 | 17.10 | 9.50 | 251,939,930,112.00 USD | 64.02 |

Peers fetched as_of: 2026-11-01; VRTX reuses existing data (market data as_of: 2026-10-30); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-03
- Next expected earnings: 2026-11-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-01

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-08-04
- Revenue (latest available single quarter): 640,799,000.00 USD; period 2018-01-01/2018-03-31; fiscal year/reporting period 2018/Q1
- Net income (latest available single quarter): 1,099,800,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/875320/000087532026000259/vrtx-20260630.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMipgFBVV95cUxQQVdrekpkclVkTF93RUxySVd2Tm0tYmJibzdpUUNLdlZuZTlwM1A3NWxjcWpxbkNaOEhBUkVSaTcyOVdSd3Zvd29xT3dFMXpYb0N4eEl0MkN0U25BdERES0ZpbG5tTVdOemQxc0lwaVBOVjI3WTB5aERPbndUYWVqMVpzRW1rQnoyVlo4N2VrbzhIZHlXQk9YZExXQnBtMjJFZ0VrUzZR?oc=5
- https://news.google.com/rss/articles/CBMi7AFBVV95cUxPaHpyVVgwQjlCOElOZjJKN3ZLbHJVVV9MMFVoVF8xVWFmUVVzOGlDem9FMnNDek9uSVFKRWd6RGRzTWRRNXFYd0xLQXNjcldEQS1UQ2N6c0NGV2ZobUNOaEVvMFhyZ0ZxU2x2c0psbUdtTi1XY2hvb3VLSFBnQk9JZXdGS1ZfeFdCcE5yVGlTS3JDYlJQS0lPcW13U0JqdkI4eEdIN243dW1QLUpnWU1SaDNNeVFHX2dSZ2lSeGJLYnVOOXdzOGdvbnJvak5jai1nWHJDVmstY2JWSjJWa2VxTkhOMExCVUp5cGdiZNIB8gFBVV95cUxORVdwSVByZlRQa3ZpVVhVVFFRbDIyQ0dMYmdRT3BOTE41RnQ0V0dRdDZNdEFIYmkyRnJzdWwyV3BDUzJFTkhkQUtydzVNYnVJRl9lTUZLU1pZR3hfOVBXVWVYMERTS1M0bDdJdVFfMk1uaU05dkl5ZFRRV2pSTW1wZlpEZlJkeDJWeWE4NGM1TFhaUWQwVHBpajBqVkx0dFltbFpvZzlTeG9nTUFFdWNnOHNLcUpEOGxvUXEtSm56VXliU29SVHl2aHlzQUc0U0JpcWluN1VXSzRRYUM1di1jREd2RkRhX3NLaTlFS1JkVzR2QQ?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxPOEVKaXlSbjNjRTEwSDRGODcyR0VTV1B3bmZPbU45ejBOZ0E0RERDRmdwVVBySUZkN0NmOWxjQS10QWNyOVhWWTZJaE5VSWppZVhDMnhGSUs3bFZtUHhSLUlHbVRuOEo1bmdCTkk2cENuV1doMGZmTXJ4cXozMXo4S25MeHB5V3JqVlBnVXlRM19kbTlMdno5SVlTQUgwSXRPZjI5Q0szQQ?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxNMUcySXV6cmhUVzl1X0tzWTNKbFNfaERVQzMxQ2JTbWxXX0ZrQW5rTHlBWGNMWTFCLXBKQzhWSWtBTnZFOHd6TzJqcmpBZDFWb3dtb0pZT2RuSDNKY2hhb0NSYnBYTUZZblBULXpEMm1Rd3dOMGVpN1BKUWs3S296YmZEX0pBRnVwVEE4UDZFWDJCdnAySzZyX20zZE15ZGhkYjhscjZYN3FVQQ?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxOd0N4VUVaYjRYaHphMkxPZEZjSkZJdFBTQ1BzYUVpcVVoRVZILXpmNWxkU1BqcWxPQkZLT21JLUhHNWFSalRWQjJpVEJSSWRsM3RjTER3SUdCWmxhWE1BMFJtZzVBWnZEaUNYUWtlOVJjVE5GUHZvam9veERwSlJXcjh1YnBDTEZqQkY0WjVwdzVyVXk4MG1YUjdmYi1uenpsbVRpbUtITmtIQUNnMWcxSG1UalJTeXF4WU93?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxQdXJROFhGNXJCQTZoUDlrdDJoU2FieHZidWZmNTY0X2I3WVRoVDYtaEY4ZnhUdTc4VEpmekVJTlh1V3ZFeVd4VjcwdVdhZkpiaDlXdXlxc2ZfQ1NsUm43cl9oRTlONXVyYkp3Z0hXbE9zOG5EdThfM3F4amhWM0RyUHFwN3M5bGVxcUR3R3R4NUxKVG5KSDZVMmhn?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxPLWpRMzlmMXJhdl90d0llcXVVOFJEMlQ5ZXhJaGlhajlJVlZUeG0yVGZwU3JObzFtMTJIVE00ZUdwWXd5YWZBRm5qWGJwTkU3em9YNXFkSXVsYmJTemVBb1JMQnZXRmRUSXczMHhfLWYyRDhNWEF0LWVKaEZ1X01oODkySEgwSTN6bWQtMmluRUx0ZTNXOXZFOVFTT3VyYnRNSXB6bXBnYV9UV3V1YXJ3?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
