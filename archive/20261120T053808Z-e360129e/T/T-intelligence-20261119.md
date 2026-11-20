# T Intelligence Report

- ticker: **T**
- Report as_of: **2026-11-19**
- Market data as_of: **2026-11-19**
- Quant sources: https://finance.yahoo.com/quote/T/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/T/key-statistics/
- AI analysis snapshot as_of: **2026-11-19**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-20T05:53:25.521254+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 12, 'rule': 2, 'ai': 6, 'unknown': 0, 'irrelevant': 4})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **4** exact headline/source/date matches; prior report **20261118T054934Z-e0d070d9/T** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 12 unique headlines; 7 named publishers; 0 exact duplicates; 12 HTTPS source links; largest publisher share 25.0%; oldest publication 2026-11-12

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 21.8500 |
| Return 1D (%) | -0.4556 |
| Return 1W (%) | -1.4878 |
| Return 1M (%) | -5.8190 |
| Return YTD (%) | -7.8401 |
| Return 1Y (%) | -9.4083 |
| Annualized volatility (%) | 28.6613 |
| Beta vs SPY | -0.3306 |
| Max drawdown (%) | -28.8854 |
| Sharpe (rf=0) | -0.2014 |
| Downside deviation (rf=0, %) | 21.9912 |
| Sortino (rf=0) | -0.2625 |
| Historical VaR 95% (1D, %) | 2.8546 |
| Historical ES 95% (1D, %) | 4.6484 |
| Correlation vs SPY | -0.1603 |
| Tracking error vs SPY (%) | 33.7995 |
| P/E (trailing) | 11.68 |
| P/B | 1.38 |
| EV/EBITDA | 7.29 |
| Revenue growth (%) | 5.30 |
| Forward P/E (estimate) | 8.42 |
| Gross margin (%) | 59.74 |
| Operating margin (%) | 22.59 |
| Return on equity (%) | 11.61 |
| Free cash flow yield (%) | 8.13 |
| MA50 | 23.1767 |
| Close vs MA50 (%) | -5.7245 |
| MA200 | 24.3211 |
| Close vs MA200 (%) | -10.1604 |
| RSI (14, Wilder) | 44.0722 |
| MACD (12,26) | -0.2222 |
| MACD signal (9) | -0.3571 |
| MACD histogram | 0.1349 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'T': 286, 'SPY': 286}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 21.8500 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.4556 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -1.4878 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -5.8190 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -7.8401 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -9.4083 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 28.6613 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 21.9912 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.2625 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.8546 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.6484 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.1603 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 33.7995 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.3306 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -28.8854 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.2014 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 8.4174 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 59.7420 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 22.5930 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 11.6130 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 8.1266 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 11.6845 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 44.0722 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.1349 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -5.7245 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -10.1604 -> Clearly below the moving-average trend level.

## TAILWINDS

### Could AT&T Be The Value Stock For Your Portfolio?
- Summary: Analyst opinion that AT&T may be a value investment for portfolios.
- Date: 2026-11-12 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxPMy1qLUZsZVBUcDZ2UkRvelROOUFjUTZYM3dVajNvejlJOWNfZWd6QnpSTEVxUGRlUzY0LXNUaktXN2xjRmUtTVFxQW9ZM0JiYXNvN1F3bEFvZC1rc3Z3OGxBT0d6cy1DWGFwUGl1SlVXR1h1Q1E2R0dsaklnS3hPaHVqSHFfWk44M0ppM3U2RVpIT25VbDJNT19n?oc=5>

### AT&T (T) Stock Looks Reasonable On Its 62% Three Year Run
- Summary: Assessment of AT&T's stock performance over three years.
- Date: 2026-11-15 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxNeWlWTVNHb1JxQ3c0amtDcjNhZDlwTXFPd25YeXk0YUVhYlBCS3VDdXNlb2d1WUZqOS1mY2s4SThiMzhMUDJxUTJvOFRjdDZSa2xpOHl2b0Z3REEtb24zRlJZWUtqd1RYTVRxQ0c3SzFBNzgzWktqQ1RjX2NJNzVwZmNpQy00UHpVQmllcnNZWTJWYVNOYzZMeEppel9xc0FLemU0ajdLaXdoUk92OHfSAbMBQVVfeXFMTmxmZzB2LURENGF6VkxKbkt5SUgwdFUwMEJzZHJ6aHI5d3FzQ0Q1Vm0xLUZSd3QzQUluZmJxVi0zMzMtSTlDZUhvclY0ZzFtQVRPelJjQ0swb0xpSE5TbWFZZ2RmSVB4ZVVoaC1NNE5ZSHhsSHlTb28tRlliMERpOFlFQ0N2LTZQbXpvLWRZQ0h1VFJ3dzVPOHhyejBhVmVBUnBwdjIxM1RwRjRBLXRXdTZfSzA?oc=5>

### AT&T will connect U.S. Soccer’s new center, where men’s and women’s teams will train at one site for the first time.
- Summary: AT&T to connect new U.S. Soccer training center.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxOdEgyMkxYUU05LVdLNUY3UnUtQlFyMTM4LVhqMTBaTEROaHBRcl90dlJ2RDB4ZGNOSllxY3FLWFBDb3VaeDB5dHBrWmFRWDJJVlRRalo3RnZEZlRKVmpFdnlqTDQyREtiSVBrLUFsemljU1U0bDlxTE5KaHduSDJxblBlejl4dDJfQTdlREpGd3ByaDVhWWNYeTRiN2Z6NG9haEpIbVQydnpCZ0FrUlNIWTQ4T20tb3c?oc=5>

## HEADWINDS

### AT&T Inc. (T) Stock: Slips Despite Renewed Partnership Supporting 27 U.S. National Teams
- Summary: AT&T Inc. (T) Stock: Slips Despite Renewed Partnership Supporting 27 U.S. National Teams
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxOQkhIX01xQnUyVWVMZnpmN19WZmVsY0hQRUxmNHJQbTh2Y0ZHN01jSXNwdXpqcFpsMkxNbUtEeTRFcnUxd3ZucE45bmNKN056Vld4b3drNkpMV2VScU5ZbkJMWGhYOFhrV0tEb0pFR2RUNDM3bjZVTmVlM1lwWGVfTDByLWh2blluZld4OW10NmFWYXRzT1g1cm5tVzJybzRscFRxaEh2NE9tQQ?oc=5>

### AT&T stock slips to EUR 19.98, down 0.60% before Xetra
- Summary: AT&T stock slips to EUR 19.98, down 0.60% before Xetra
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxNQy03NWdOYmVwbG10SG4tUGlyLTBhekVkWXBMcWdlYW13WVpLXzU4LWUtUGI3OWVsbG9JWGZtZFNKZ2JnVW1mYThqaC01MUtIWTdoaGNpcXVEUUYyNVRkWFRpVEtlVlgyeDdiYWtfaVdNLUFiZ2lLT244R3Z4WXl0NWwyR2tWRDAtWlBzOTVoZHlHbWRMemlyQnhVU0YyNXVNb19lanRtcXVIOE43dHBZ?oc=5>

### FAA Chief Warns System ‘Will Continue to Break.’ AT&T, Verizon, and Lumen Could Be Big Winners
- Summary: FAA warns system failures; AT&T may benefit.
- Date: 2026-11-15 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxPRDM4NHJ3U1I1RVJxY3JTOVFZWVk2Q1p2cEQxREh1YVpkUFlHOVI4TVplWDE5bVQ3ZGM0MExOcUtjR3IwdjVYM2pXVXVDLTRjdS16OXZFR2FKdU5MY1dpYzFreU1UODR6bUZ6V2hibVFnZXVzODA2djFxSkZLNVI2b0NsRXVzc0NpWkNGSVpzZmxBRGJQMnBFTFRMQ2s?oc=5>

## CATALYSTS

### Clean Execution Lifted AT&T (T) in Q3
- Summary: AT&T's Q3 earnings improved due to clean execution.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxNOG8zdFF2YjExaGFJamFKLUJ0MmQ3SzJLeW8tUnFwOThVREh4NzllWWhuQmtUU05MakRIWkVtRDl0VmVpSnotbkczaC1FcE5CdGFlSGIxNndkN0JDcFlaSUhHeno3U1M4RExJTkZUVFE1VVZ1NDh1YVg0RVdqZjU3X3lXakN0cTByQlhFNl84bWRqN1ZlZ1E?oc=5>

### AT&T stock: Microsoft bundle expands small-business AI reach
- Summary: AT&T partners with Microsoft to bundle AI services for small businesses, potentially boosting revenue and market presence.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxOQndWSmMwVFd3aGMtZGdtZkltSGRQRThFemFRR2RObnVjTzNLckZ0bXlMTTNDX3J0bmo2M2Z4SkM2eVE5MjU4cF9lVzdpN1lVMXo1cVpjaVZGUHR2UnlVUHFSempxdDYxWjV3X0NaTm94Y05Wb3FJMmZ1cWZVLXRiVU1heXN0STNSaDFqSVRaY0RLREltRndFNnV1X0JMVWs0dktGRG5DSXVmZGhMZzc1QTFJLXdnWXhPaEFpWFJEMA?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **T** | **11.68** | **1.38** | **7.29** | **5.30** | **147,191,955,456.00 USD** | **-9.41** |
| VZ | 11.67 | 1.79 | 7.33 | 1.50 | 189,573,939,200.00 USD | 18.44 |
| TMUS | 15.81 | 3.07 | 8.07 | 7.40 | 172,163,563,520.00 USD | -21.44 |
| BCE | 11.53 | 1.33 | 7.35 | 2.20 | 19,890,776,064.00 USD | -1.39 |

Peers fetched as_of: 2026-11-19; T reuses existing data (market data as_of: 2026-11-19); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-21
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-19

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-21
- Revenue (latest available single quarter): 32,322,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 891,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/732717/000073271726000372/t-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMimgFBVV95cUxPMy1qLUZsZVBUcDZ2UkRvelROOUFjUTZYM3dVajNvejlJOWNfZWd6QnpSTEVxUGRlUzY0LXNUaktXN2xjRmUtTVFxQW9ZM0JiYXNvN1F3bEFvZC1rc3Z3OGxBT0d6cy1DWGFwUGl1SlVXR1h1Q1E2R0dsaklnS3hPaHVqSHFfWk44M0ppM3U2RVpIT25VbDJNT19n?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxNeWlWTVNHb1JxQ3c0amtDcjNhZDlwTXFPd25YeXk0YUVhYlBCS3VDdXNlb2d1WUZqOS1mY2s4SThiMzhMUDJxUTJvOFRjdDZSa2xpOHl2b0Z3REEtb24zRlJZWUtqd1RYTVRxQ0c3SzFBNzgzWktqQ1RjX2NJNzVwZmNpQy00UHpVQmllcnNZWTJWYVNOYzZMeEppel9xc0FLemU0ajdLaXdoUk92OHfSAbMBQVVfeXFMTmxmZzB2LURENGF6VkxKbkt5SUgwdFUwMEJzZHJ6aHI5d3FzQ0Q1Vm0xLUZSd3QzQUluZmJxVi0zMzMtSTlDZUhvclY0ZzFtQVRPelJjQ0swb0xpSE5TbWFZZ2RmSVB4ZVVoaC1NNE5ZSHhsSHlTb28tRlliMERpOFlFQ0N2LTZQbXpvLWRZQ0h1VFJ3dzVPOHhyejBhVmVBUnBwdjIxM1RwRjRBLXRXdTZfSzA?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxOdEgyMkxYUU05LVdLNUY3UnUtQlFyMTM4LVhqMTBaTEROaHBRcl90dlJ2RDB4ZGNOSllxY3FLWFBDb3VaeDB5dHBrWmFRWDJJVlRRalo3RnZEZlRKVmpFdnlqTDQyREtiSVBrLUFsemljU1U0bDlxTE5KaHduSDJxblBlejl4dDJfQTdlREpGd3ByaDVhWWNYeTRiN2Z6NG9haEpIbVQydnpCZ0FrUlNIWTQ4T20tb3c?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxOQkhIX01xQnUyVWVMZnpmN19WZmVsY0hQRUxmNHJQbTh2Y0ZHN01jSXNwdXpqcFpsMkxNbUtEeTRFcnUxd3ZucE45bmNKN056Vld4b3drNkpMV2VScU5ZbkJMWGhYOFhrV0tEb0pFR2RUNDM3bjZVTmVlM1lwWGVfTDByLWh2blluZld4OW10NmFWYXRzT1g1cm5tVzJybzRscFRxaEh2NE9tQQ?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxNQy03NWdOYmVwbG10SG4tUGlyLTBhekVkWXBMcWdlYW13WVpLXzU4LWUtUGI3OWVsbG9JWGZtZFNKZ2JnVW1mYThqaC01MUtIWTdoaGNpcXVEUUYyNVRkWFRpVEtlVlgyeDdiYWtfaVdNLUFiZ2lLT244R3Z4WXl0NWwyR2tWRDAtWlBzOTVoZHlHbWRMemlyQnhVU0YyNXVNb19lanRtcXVIOE43dHBZ?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxPRDM4NHJ3U1I1RVJxY3JTOVFZWVk2Q1p2cEQxREh1YVpkUFlHOVI4TVplWDE5bVQ3ZGM0MExOcUtjR3IwdjVYM2pXVXVDLTRjdS16OXZFR2FKdU5MY1dpYzFreU1UODR6bUZ6V2hibVFnZXVzODA2djFxSkZLNVI2b0NsRXVzc0NpWkNGSVpzZmxBRGJQMnBFTFRMQ2s?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxNOG8zdFF2YjExaGFJamFKLUJ0MmQ3SzJLeW8tUnFwOThVREh4NzllWWhuQmtUU05MakRIWkVtRDl0VmVpSnotbkczaC1FcE5CdGFlSGIxNndkN0JDcFlaSUhHeno3U1M4RExJTkZUVFE1VVZ1NDh1YVg0RVdqZjU3X3lXakN0cTByQlhFNl84bWRqN1ZlZ1E?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxOQndWSmMwVFd3aGMtZGdtZkltSGRQRThFemFRR2RObnVjTzNLckZ0bXlMTTNDX3J0bmo2M2Z4SkM2eVE5MjU4cF9lVzdpN1lVMXo1cVpjaVZGUHR2UnlVUHFSempxdDYxWjV3X0NaTm94Y05Wb3FJMmZ1cWZVLXRiVU1heXN0STNSaDFqSVRaY0RLREltRndFNnV1X0JMVWs0dktGRG5DSXVmZGhMZzc1QTFJLXdnWXhPaEFpWFJEMA?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
