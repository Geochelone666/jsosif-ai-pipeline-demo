# J Intelligence Report

- ticker: **J**
- Report as_of: **2026-10-27**
- Market data as_of: **2026-10-27**
- Quant sources: https://finance.yahoo.com/quote/J/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/J/key-statistics/
- AI analysis snapshot as_of: **2026-10-27**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-28T02:25:04.075499+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 9, 'rule': 3, 'ai': 3, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **4** exact headline/source/date matches; prior report **20261027T014607Z-b66f6bd5/J** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 9 unique headlines; 4 named publishers; 0 exact duplicates; 9 HTTPS source links; largest publisher share 66.67%; oldest publication 2026-10-22

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 148.3400 |
| Return 1D (%) | 0.8155 |
| Return 1W (%) | 6.2075 |
| Return 1M (%) | 7.2053 |
| Return YTD (%) | 12.9090 |
| Return 1Y (%) | -6.8817 |
| Annualized volatility (%) | 32.6441 |
| Beta vs SPY | 0.7648 |
| Max drawdown (%) | -33.0387 |
| Sharpe (rf=0) | -0.0548 |
| Downside deviation (rf=0, %) | 24.3937 |
| Sortino (rf=0) | -0.0733 |
| Historical VaR 95% (1D, %) | 3.0123 |
| Historical ES 95% (1D, %) | 5.1035 |
| Correlation vs SPY | 0.2976 |
| Tracking error vs SPY (%) | 31.3080 |
| P/E (trailing) | 49.28 |
| P/B | 5.32 |
| EV/EBITDA | 19.14 |
| Revenue growth (%) | 34.50 |
| Forward P/E (estimate) | 18.01 |
| Gross margin (%) | 22.07 |
| Operating margin (%) | 7.39 |
| Return on equity (%) | 8.00 |
| Free cash flow yield (%) | 3.72 |
| MA50 | 143.2817 |
| Close vs MA50 (%) | 3.5303 |
| MA200 | 133.1384 |
| Close vs MA200 (%) | 11.4179 |
| RSI (14, Wilder) | 63.9085 |
| MACD (12,26) | 1.3211 |
| MACD signal (9) | 0.2582 |
| MACD histogram | 1.0629 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'J': 269, 'SPY': 269}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 148.3400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.8155 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 6.2075 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 7.2053 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 12.9090 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -6.8817 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 32.6441 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 24.3937 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.0733 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.0123 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.1035 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2976 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 31.3080 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.7648 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -33.0387 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.0548 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 18.0092 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 22.0670 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 7.3870 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 7.9980 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 3.7190 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 49.2824 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 63.9085 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 1.0629 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 3.5303 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 11.4179 -> Clearly above the moving-average trend level.

## TAILWINDS

### 10,300 Jacobs Solutions Inc. $J Shares Bought by Oakmont Investment Advisors Inc.
- Summary: Oakmont Investment Advisors purchased 10,300 shares of Jacobs Solutions, indicating investor interest.
- Date: 2026-10-22 | Impact: low | Horizon: short | Confidence: 1
- Sources: <https://news.google.com/rss/articles/CBMi1AFBVV95cUxQOTl5czh5NTlHRUZyY2lQekNWNXFDZXE3cUo2QzBuWHRxOFdCb2RWNlBFMW13LXhfdVB2QzRQVk12YlYySFlhR0N1NFJyaXZCMHdaZ2Rhc18taUpOREpza3VaU1o1NGhMLTNIUnp0dm5KM0c2UHBwYlU3MUg3SzJQLWNIX3hqUEVmN3EzUVlQU1dWcC1iaGstRWVvMk5SYmo0NnNhdlJNWHlPTTdtR3dPbm80OXd6dk1LdGFUUGJNS2N0MmhFd3lFTE1sM2dwRTVUZVo1dQ?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Jacobs Solutions Inc. $J Stock Sold by Robeco Institutional Asset Management B.V.
- Summary: Jacobs Solutions Inc. $J Stock Sold by Robeco Institutional Asset Management B.V.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1AFBVV95cUxNN3A4MnJ4RzhIZGNPX3Z6VkNwZVBlOWJTeVhOZGJ6bWxZdElRSkdlUE51LUIzdVVlazNycExuVjRrVTJfMnJxclJMcEdITC05NXo1bUMzWm9MdVhZX2pMeGZ1U3VGUjNxQU5QNXFGYTktVmRzc1ltQ0dpWnI4QnNOZ01SUWpjcExPUXNMWW9jMHQ1TTdQZUZUMWJsVldQUnowdkRlXzdSc21mVUQ1clVNdXBoY3B5VjBJbTdPa3VVR0lDdzlYbnpNdl85Q1RLeE9obEtpbA?oc=5>

### Jacobs Solutions (NYSE:J) Given New $188.00 Price Target at Citigroup
- Summary: Jacobs Solutions (NYSE:J) Given New $188.00 Price Target at Citigroup
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixgFBVV95cUxNVWt3SXc0OUxPa0gwSUhvTC1yamtETGZZVkxLczZHRUxYbjA1UFdyNHdzbGZvM2VvTy1jaU5jeldfZ2xuT3Q0Mk1IRWJUUTZHUGZXLXZLOS1EeTNsOEt4dWhrYkpHRkhiY1FQbDBNdXZENjJuQzBZcUpnRGQ0WGlINHpvS2tYWkdoUzdtQktNakswQ2JaZTVwSVBEdUdUTFMydWFhemxLaTMtVFdjU0xaWU5iWDU2RlZmb3FlaVJvcm9hOVQwX3c?oc=5>

### Jacobs Solutions (J) Dividend Yield 2026, Date & History $J
- Summary: Jacobs Solutions (J) Dividend Yield 2026, Date & History $J
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiX0FVX3lxTE9vMUpBU3NHZWV3TEx3S0VURVlnQkFMN3hlX05GeFVMNGxLZldLN1hFcmI0cWNETFNYQVlGZk9KellUMF9CdjVzNWVJQmF5UFg3MHhKQi1KbDc5c09oMHA0?oc=5>

### Robeco Schweiz AG Sells 64,534 Shares of Jacobs Solutions Inc. $J
- Summary: Robeco Schweiz AG sold 64,534 shares of Jacobs Solutions, indicating a market move.
- Date: 2026-10-25 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxORVVXOFRnS3J1bVdsZXZ4U2lQZVZCMkNxUlpLUWJCekltTmxuUW94OW9zSEJkQTJKdTRlM2tXbHdWOFJfeVh6TDNoQkEzV1FZSloxeDQzZnYzUHlKcmhYVTlkWkU4UllTaERfT1hYdnhfbGE0dzN1WE1kbjEtQXByLXljcHc4MkhfZVJhUFZFZjhLLWEwOS1wTmVjMTFHTnI5cWZxaHBtWWNKNFNHV0lRVTUtUFhFWVYtRDBXVTFpVlM?oc=5>

### Valen Private Capital LLC Acquires New Holdings in Jacobs Solutions Inc. $J
- Summary: Valen Private Capital LLC purchased new holdings in Jacobs Solutions, reflecting a market move.
- Date: 2026-10-25 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizwFBVV95cUxPMWJFRGtPSGFBNTdzV2tOdF9wRHRldDVjZkNfQ2RqN1pVQnZ1NE42ZVh0enZGc0lheGE1eXNKNFlkMk14ekxDd2FsUUEzWXVUUlRHMkVJand3dWpySXlFaFFDTXRJQUZ5TnJCMEVMZlRHLVJ1MWhmb19qVGk4V083aEd1RG5VSE5EeXNGZ2JZaDk2QS1BU01rWHY2eGswUGFUQ3FSZ1d1X3Rzc1NySWVOcjVBcDgzUTNIZHA1TGRWR2s0ZV9jSG9TTmxlS0E4SDg?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **J** | **49.28** | **5.32** | **19.14** | **34.50** | **17,361,506,304.00 USD** | **-6.88** |
| ACM | 21.67 | 3.61 | 11.20 | -14.20 | 7,918,690,816.00 USD | -52.81 |
| FLR | N/A | 2.33 | -18.46 | 8.80 | 6,173,487,616.00 USD | -4.82 |
| KBR | 12.08 | 3.10 | 11.21 | 1.60 | 5,071,705,600.00 USD | -6.54 |

Peers fetched as_of: 2026-10-27; J reuses existing data (market data as_of: 2026-10-27); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-04
- Next expected earnings: 2026-11-23 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-27

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-08-04
- Revenue (latest available single quarter): 4,142,644,000.00 USD; period 2018-06-30/2018-09-28; fiscal year/reporting period 2018/FY
- Net income (latest available single quarter): 136,553,000.00 USD; period 2026-03-28/2026-06-26; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/52988/000162828026052573/jec-20260626.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMi1AFBVV95cUxQOTl5czh5NTlHRUZyY2lQekNWNXFDZXE3cUo2QzBuWHRxOFdCb2RWNlBFMW13LXhfdVB2QzRQVk12YlYySFlhR0N1NFJyaXZCMHdaZ2Rhc18taUpOREpza3VaU1o1NGhMLTNIUnp0dm5KM0c2UHBwYlU3MUg3SzJQLWNIX3hqUEVmN3EzUVlQU1dWcC1iaGstRWVvMk5SYmo0NnNhdlJNWHlPTTdtR3dPbm80OXd6dk1LdGFUUGJNS2N0MmhFd3lFTE1sM2dwRTVUZVo1dQ?oc=5
- https://news.google.com/rss/articles/CBMi1AFBVV95cUxNN3A4MnJ4RzhIZGNPX3Z6VkNwZVBlOWJTeVhOZGJ6bWxZdElRSkdlUE51LUIzdVVlazNycExuVjRrVTJfMnJxclJMcEdITC05NXo1bUMzWm9MdVhZX2pMeGZ1U3VGUjNxQU5QNXFGYTktVmRzc1ltQ0dpWnI4QnNOZ01SUWpjcExPUXNMWW9jMHQ1TTdQZUZUMWJsVldQUnowdkRlXzdSc21mVUQ1clVNdXBoY3B5VjBJbTdPa3VVR0lDdzlYbnpNdl85Q1RLeE9obEtpbA?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxNVWt3SXc0OUxPa0gwSUhvTC1yamtETGZZVkxLczZHRUxYbjA1UFdyNHdzbGZvM2VvTy1jaU5jeldfZ2xuT3Q0Mk1IRWJUUTZHUGZXLXZLOS1EeTNsOEt4dWhrYkpHRkhiY1FQbDBNdXZENjJuQzBZcUpnRGQ0WGlINHpvS2tYWkdoUzdtQktNakswQ2JaZTVwSVBEdUdUTFMydWFhemxLaTMtVFdjU0xaWU5iWDU2RlZmb3FlaVJvcm9hOVQwX3c?oc=5
- https://news.google.com/rss/articles/CBMiX0FVX3lxTE9vMUpBU3NHZWV3TEx3S0VURVlnQkFMN3hlX05GeFVMNGxLZldLN1hFcmI0cWNETFNYQVlGZk9KellUMF9CdjVzNWVJQmF5UFg3MHhKQi1KbDc5c09oMHA0?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxORVVXOFRnS3J1bVdsZXZ4U2lQZVZCMkNxUlpLUWJCekltTmxuUW94OW9zSEJkQTJKdTRlM2tXbHdWOFJfeVh6TDNoQkEzV1FZSloxeDQzZnYzUHlKcmhYVTlkWkU4UllTaERfT1hYdnhfbGE0dzN1WE1kbjEtQXByLXljcHc4MkhfZVJhUFZFZjhLLWEwOS1wTmVjMTFHTnI5cWZxaHBtWWNKNFNHV0lRVTUtUFhFWVYtRDBXVTFpVlM?oc=5
- https://news.google.com/rss/articles/CBMizwFBVV95cUxPMWJFRGtPSGFBNTdzV2tOdF9wRHRldDVjZkNfQ2RqN1pVQnZ1NE42ZVh0enZGc0lheGE1eXNKNFlkMk14ekxDd2FsUUEzWXVUUlRHMkVJand3dWpySXlFaFFDTXRJQUZ5TnJCMEVMZlRHLVJ1MWhmb19qVGk4V083aEd1RG5VSE5EeXNGZ2JZaDk2QS1BU01rWHY2eGswUGFUQ3FSZ1d1X3Rzc1NySWVOcjVBcDgzUTNIZHA1TGRWR2s0ZV9jSG9TTmxlS0E4SDg?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
