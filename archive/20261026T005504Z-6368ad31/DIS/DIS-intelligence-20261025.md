# DIS Intelligence Report

- ticker: **DIS**
- Report as_of: **2026-10-25**
- Market data as_of: **2026-10-23**
- Quant sources: https://finance.yahoo.com/quote/DIS/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/DIS/key-statistics/
- AI analysis snapshot as_of: **2026-10-25**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-26T01:23:32.601598+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 12, 'rule': 0, 'ai': 8, 'unknown': 0, 'irrelevant': 4})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **0** exact headline/source/date matches; prior report **N/A** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 12 unique headlines; 7 named publishers; 0 exact duplicates; 12 HTTPS source links; largest publisher share 33.33%; oldest publication 2026-10-18

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 112.5200 |
| Return 1D (%) | -0.5392 |
| Return 1W (%) | 1.7452 |
| Return 1M (%) | 8.7570 |
| Return YTD (%) | -0.3409 |
| Return 1Y (%) | 0.9903 |
| Annualized volatility (%) | 26.8746 |
| Beta vs SPY | 0.6198 |
| Max drawdown (%) | -20.2451 |
| Sharpe (rf=0) | 0.1713 |
| Downside deviation (rf=0, %) | 19.1831 |
| Sortino (rf=0) | 0.2399 |
| Historical VaR 95% (1D, %) | 2.4075 |
| Historical ES 95% (1D, %) | 3.7715 |
| Correlation vs SPY | 0.2940 |
| Tracking error vs SPY (%) | 26.1402 |
| P/E (trailing) | 23.20 |
| P/B | 1.77 |
| EV/EBITDA | 11.54 |
| Revenue growth (%) | 6.80 |
| Forward P/E (estimate) | 15.01 |
| Gross margin (%) | 37.59 |
| Operating margin (%) | 19.30 |
| Return on equity (%) | 8.01 |
| Free cash flow yield (%) | 2.50 |
| MA50 | 106.8952 |
| Close vs MA50 (%) | 5.2620 |
| MA200 | 103.0807 |
| Close vs MA200 (%) | 9.1572 |
| RSI (14, Wilder) | 66.4920 |
| MACD (12,26) | 1.9352 |
| MACD signal (9) | 1.3415 |
| MACD histogram | 0.5936 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'DIS': 267, 'SPY': 267}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 112.5200 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.5392 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 1.7452 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 8.7570 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -0.3409 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 0.9903 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 26.8746 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 19.1831 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.2399 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.4075 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.7715 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2940 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 26.1402 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.6198 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -20.2451 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.1713 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 15.0102 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 37.5950 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 19.3010 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 8.0100 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.5016 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 23.2000 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 66.4920 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.5936 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 5.2620 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 9.1572 -> Clearly above the moving-average trend level.

## TAILWINDS

### DIS Stock Gains Nearly 2% — Why Wells Fargo Says Disney Could Jump 40% If It Exits Streaming
- Summary: Wells Fargo predicts a 40% jump if Disney exits streaming, driving a 2% stock gain.
- Date: 2026-10-24 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi5wFBVV95cUxQaUpXbXBqR0p6UXVpS3Z3cTlJNEJ0UlFGa2tvOFNORTNYLVkzdVF0TkNJamxITl9pMkk5ZHVyZndTQjVQRk8xVmg5c2hBdVZhYVNCOExzWWt3SF9EWFNfOHh2cHRDWDZrWE9hZ2VKRWJjLWRqVUNyR095ODhSSkRWRkd1YUxqVEowRXVQSk51ak1mNm84X05kT0R4Yk9MUkpWOWs5OEVhQ183aTA1QjViTmJzRmxwVldnbDhCQjNpSmxkZzlMSkVqcjlfeTBjV2xwS0ZSWFg3NFVRVjltazBZQ01yaVpGc3M?oc=5>

### Walt Disney (DIS) Rises As Market Takes a Dip: Key Facts
- Summary: Disney stock rises as market dips, indicating a positive market move.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQZGhWalpQSjhncTE1ZEsyRy1KTHNXQ18yX0FRNlV6ekUyM1l1TzVOYUlfVFNiaFc3a256TFFVY3lwWXo4VGl5UElMalZYb3FMNHRDWjNZQWpBV3p4aVdpUmV4V1VzZlUyM1VHNEdaTlpMY3k2N3lESEpkb1ZVRWVlWkR5QTBLQ1JIYWNTTHRJV3pxanYwTi1NcA?oc=5>

### Disney (DIS) Stock Looks Reasonably Priced After A 43% Gain
- Summary: Stock appears fairly priced following a 43% gain.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxQOEdDdXl2bGNjMmg5WEs1T0I2RjE1V1lrdlpTR1hfYmYxa0EwT3NxN1lOUTdmVmpwc0tRRnVZcUI4QUV5dko3RGhnTmxkc1N4d3hFMTQ1UmpkM2xCSVVJUlA1b1NXSnpQUHZpUGFJSU53blZwVjl3QlJCczk2SkpkSmFYOUFycUdUWmQzTmpvZ0ItQ0ZRZ21JVk9MNS1fRWM?oc=5>

## HEADWINDS

### If Park Visitors Pull Back, What Happens To Your Disney Stock?
- Summary: Potential decline in park visitors could negatively affect Disney stock.
- Date: 2026-10-22 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxPZ1RNTXN0U2dhM3RNaFM3b0lZMkgyVmlLMTRUVVlBOFZxZG93RjJ1aWRtLUJtLVd3dEFXYTdBX0hsYmlRbWpFMXQtRmNIcUV2UDdFcHVCd1lIR28taEhGWjF4d0tEb2ktcWl6ZExHSWROcXpHTEpDUmJkakZCT0ZFSEZ6M3dXUm1QSGVVRVE0M1VVb19QOG1hWnQ3bUpVNzdZQ25HZUZUVDZjOFM1N3poT3N5ejd6cUNoWi00Sg?oc=5>

### The Walt Disney Company $DIS Stock Holdings Lessened by Prime Capital Investment Advisors LLC
- Summary: Prime Capital reduced Disney holdings.
- Date: 2026-10-22 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMi6AFBVV95cUxOaGh3SUVLS3MzejhVU085TEIwNFVIUU9laUZ5UWtEY01xcS13RHdyWkRVN3kyaDRRMWVLQzNNUGFoWTZ0enI2Nnp2bnBUTVItUUR0ZXJXbjdfWFo3Tm81a3FScmFHZ0U4eFlUeDZaUnFwRjhKQ0RoLUhNZWdjbTZmTzRMVjU5VzlhQmRUYV9fUGt6YTBiaUNBR1ljUzlvZng3djNzaVgxM3kxaTlrWkcwQmlKdXlxdWhkOTNwTU94VFEwZXFTSVc0Xy1zOVhRUE1jQXc4a2t0S05LdFVndXlXdlphbkxSZENt?oc=5>

## CATALYSTS

### AI Hiring Push Might Change The Case For Investing In Disney (DIS)
- Summary: AI hiring initiative could alter investment outlook.
- Date: 2026-10-18 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxQMDlabnlyY0VZOFhsSHZYNVVOVENOWnowLWRjeXgzUFRBYTdGNWcyYThWeDBzUE5pb2NiUXd2eTlNUktGVm5HQW81VG9iYVBURURzQ2R1Q2Vhb04xMHJvVVhNa2RYZFB1cUZnRV9tSTFsSHN4bS1sUnRrTDJFeGRvLUdNU29ZaExwT1FKek5jTDh6OW83RVVV?oc=5>

### Disney (DIS) Stock May Be Near Fair Value Despite AI Asset Bid
- Summary: Disney stock appears near fair value amid AI asset bid concerns.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxPR1h5SUU0LXFib0pMaUxjOE9VR0Z1ZDhhWUhycl9YYXFlV2s1Ml80bHhBWm9oRllXTVNGNEoxUkVabW50VjVvaEx1dTgxZUIxdEkyamllVkE5QjM2Qmh1bVJNR3NnZW12YllJNGE5VEZhUDJ3dVFudGVjd2hTSmtBaUVoWnJjNXYzcWxTamxobG5pX3Z4Tlh6VWR2eFpNZkhaWUlYLTkxZFVNYXNKWDBtWnlLV1J5SmR0U3RsOUR3Qk04Z9IBxwFBVV95cUxNeGhLcHdfSmNlRFhESm16X3pkUmVIUEhpZVVsNzRjWWR5UGNsREJnZVU4TGRtVmtyZW5vNV9za054aVAtTHkzaEVfdWp1QmVSV2pPd1R6NVNiZjdHV0RwV182U3JfSldqQ3FSQXFyQlFZVXZET0ctQ0NxRDRibnViZHlpWUNXR1ZBdm9MVU9WeUFfbTdwdktOS3I5WjJjdXFFMUN0cFh6Y2R5U3l0QzNNdExuWkxsUEw5ajJ5eDVmazVha2dOVkpB?oc=5>

### Skydance Rises 5% as Steep Post-Merger Slide Pauses; Disney Gains 2%, Netflix Slips
- Summary: Disney shares up 2% following Skydance rally.
- Date: 2026-10-20 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxOdWxiN2xCcHc3eVhrakhMaEV2eENPdVpaTzVJalNWMjBsTVp4UnpPVFdsTnV2YVY3R0JwTzNRSlRtV2JmUEZzZHZQR0V0d0NkSGplWlhoSy0tWVVid3luUkl3UXJoZnljc19OTlMxWHFkLUMwa0UxOGJFY1Zyek5ibmFER2NBQWhIY2ljV0ZwQm9jbEpGSENNZ3JkSFN2MGRHckxaem11MTlqeVhjMk1USUtZbUt4MGVlRnYwQ2hKbGo?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **DIS** | **23.20** | **1.77** | **11.54** | **6.80** | **194,286,796,800.00 USD** | **0.99** |
| NFLX | 19.03 | 9.23 | 17.53 | 11.80 | 274,195,415,040.00 USD | -40.87 |
| WBD | N/A | 2.36 | 13.79 | -11.20 | 77,595,885,568.00 USD | N/A |
| PSKY | N/A | 0.93 | 7.95 | 0.90 | 10,992,190,464.00 USD | N/A |

Peers fetched as_of: 2026-10-25; DIS reuses existing data (market data as_of: 2026-10-23); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-05
- Next expected earnings: 2026-11-17 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-25

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-08-05
- Revenue (latest available single quarter): 25,248,000,000.00 USD; period 2026-03-29/2026-06-27; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 2,638,000,000.00 USD; period 2026-03-29/2026-06-27; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1744489/000174448926000057/dis-20260627.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMi5wFBVV95cUxQaUpXbXBqR0p6UXVpS3Z3cTlJNEJ0UlFGa2tvOFNORTNYLVkzdVF0TkNJamxITl9pMkk5ZHVyZndTQjVQRk8xVmg5c2hBdVZhYVNCOExzWWt3SF9EWFNfOHh2cHRDWDZrWE9hZ2VKRWJjLWRqVUNyR095ODhSSkRWRkd1YUxqVEowRXVQSk51ak1mNm84X05kT0R4Yk9MUkpWOWs5OEVhQ183aTA1QjViTmJzRmxwVldnbDhCQjNpSmxkZzlMSkVqcjlfeTBjV2xwS0ZSWFg3NFVRVjltazBZQ01yaVpGc3M?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQZGhWalpQSjhncTE1ZEsyRy1KTHNXQ18yX0FRNlV6ekUyM1l1TzVOYUlfVFNiaFc3a256TFFVY3lwWXo4VGl5UElMalZYb3FMNHRDWjNZQWpBV3p4aVdpUmV4V1VzZlUyM1VHNEdaTlpMY3k2N3lESEpkb1ZVRWVlWkR5QTBLQ1JIYWNTTHRJV3pxanYwTi1NcA?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxQOEdDdXl2bGNjMmg5WEs1T0I2RjE1V1lrdlpTR1hfYmYxa0EwT3NxN1lOUTdmVmpwc0tRRnVZcUI4QUV5dko3RGhnTmxkc1N4d3hFMTQ1UmpkM2xCSVVJUlA1b1NXSnpQUHZpUGFJSU53blZwVjl3QlJCczk2SkpkSmFYOUFycUdUWmQzTmpvZ0ItQ0ZRZ21JVk9MNS1fRWM?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxPZ1RNTXN0U2dhM3RNaFM3b0lZMkgyVmlLMTRUVVlBOFZxZG93RjJ1aWRtLUJtLVd3dEFXYTdBX0hsYmlRbWpFMXQtRmNIcUV2UDdFcHVCd1lIR28taEhGWjF4d0tEb2ktcWl6ZExHSWROcXpHTEpDUmJkakZCT0ZFSEZ6M3dXUm1QSGVVRVE0M1VVb19QOG1hWnQ3bUpVNzdZQ25HZUZUVDZjOFM1N3poT3N5ejd6cUNoWi00Sg?oc=5
- https://news.google.com/rss/articles/CBMi6AFBVV95cUxOaGh3SUVLS3MzejhVU085TEIwNFVIUU9laUZ5UWtEY01xcS13RHdyWkRVN3kyaDRRMWVLQzNNUGFoWTZ0enI2Nnp2bnBUTVItUUR0ZXJXbjdfWFo3Tm81a3FScmFHZ0U4eFlUeDZaUnFwRjhKQ0RoLUhNZWdjbTZmTzRMVjU5VzlhQmRUYV9fUGt6YTBiaUNBR1ljUzlvZng3djNzaVgxM3kxaTlrWkcwQmlKdXlxdWhkOTNwTU94VFEwZXFTSVc0Xy1zOVhRUE1jQXc4a2t0S05LdFVndXlXdlphbkxSZENt?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxQMDlabnlyY0VZOFhsSHZYNVVOVENOWnowLWRjeXgzUFRBYTdGNWcyYThWeDBzUE5pb2NiUXd2eTlNUktGVm5HQW81VG9iYVBURURzQ2R1Q2Vhb04xMHJvVVhNa2RYZFB1cUZnRV9tSTFsSHN4bS1sUnRrTDJFeGRvLUdNU29ZaExwT1FKek5jTDh6OW83RVVV?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxPR1h5SUU0LXFib0pMaUxjOE9VR0Z1ZDhhWUhycl9YYXFlV2s1Ml80bHhBWm9oRllXTVNGNEoxUkVabW50VjVvaEx1dTgxZUIxdEkyamllVkE5QjM2Qmh1bVJNR3NnZW12YllJNGE5VEZhUDJ3dVFudGVjd2hTSmtBaUVoWnJjNXYzcWxTamxobG5pX3Z4Tlh6VWR2eFpNZkhaWUlYLTkxZFVNYXNKWDBtWnlLV1J5SmR0U3RsOUR3Qk04Z9IBxwFBVV95cUxNeGhLcHdfSmNlRFhESm16X3pkUmVIUEhpZVVsNzRjWWR5UGNsREJnZVU4TGRtVmtyZW5vNV9za054aVAtTHkzaEVfdWp1QmVSV2pPd1R6NVNiZjdHV0RwV182U3JfSldqQ3FSQXFyQlFZVXZET0ctQ0NxRDRibnViZHlpWUNXR1ZBdm9MVU9WeUFfbTdwdktOS3I5WjJjdXFFMUN0cFh6Y2R5U3l0QzNNdExuWkxsUEw5ajJ5eDVmazVha2dOVkpB?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxOdWxiN2xCcHc3eVhrakhMaEV2eENPdVpaTzVJalNWMjBsTVp4UnpPVFdsTnV2YVY3R0JwTzNRSlRtV2JmUEZzZHZQR0V0d0NkSGplWlhoSy0tWVVid3luUkl3UXJoZnljc19OTlMxWHFkLUMwa0UxOGJFY1Zyek5ibmFER2NBQWhIY2ljV0ZwQm9jbEpGSENNZ3JkSFN2MGRHckxaem11MTlqeVhjMk1USUtZbUt4MGVlRnYwQ2hKbGo?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
