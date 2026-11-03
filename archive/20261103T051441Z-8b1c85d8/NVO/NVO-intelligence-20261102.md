# NVO Intelligence Report

- ticker: **NVO**
- Report as_of: **2026-11-02**
- Market data as_of: **2026-11-02**
- Quant sources: https://finance.yahoo.com/quote/NVO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NVO/key-statistics/
- AI analysis snapshot as_of: **2026-11-02**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-03T05:22:26.633706+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 15, 'rule': 2, 'ai': 3, 'unknown': 0, 'irrelevant': 10})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **7** exact headline/source/date matches; prior report **20261102T041627Z-c84a7052/NVO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 15 unique headlines; 10 named publishers; 0 exact duplicates; 15 HTTPS source links; largest publisher share 40.0%; oldest publication 2026-10-27

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 40.4500 |
| Return 1D (%) | 1.1250 |
| Return 1W (%) | 3.3734 |
| Return 1M (%) | 8.3869 |
| Return YTD (%) | -16.5304 |
| Return 1Y (%) | -14.1340 |
| Annualized volatility (%) | 45.6806 |
| Beta vs SPY | 0.9361 |
| Max drawdown (%) | -43.6699 |
| Sharpe (rf=0) | -0.0877 |
| Downside deviation (rf=0, %) | 34.0486 |
| Sortino (rf=0) | -0.1177 |
| Historical VaR 95% (1D, %) | 3.1076 |
| Historical ES 95% (1D, %) | 7.1341 |
| Correlation vs SPY | 0.2627 |
| Tracking error vs SPY (%) | 44.0833 |
| P/E (trailing) | 9.89 |
| P/B | 5.39 |
| EV/EBITDA | 1.58 |
| Revenue growth (%) | 2.10 |
| Forward P/E (estimate) | 11.76 |
| Gross margin (%) | 81.99 |
| Operating margin (%) | 42.54 |
| Return on equity (%) | 59.81 |
| Free cash flow yield (%) | N/A |
| MA50 | 41.1056 |
| Close vs MA50 (%) | -1.5949 |
| MA200 | 43.3026 |
| Close vs MA200 (%) | -6.5877 |
| RSI (14, Wilder) | 56.8265 |
| MACD (12,26) | -0.2331 |
| MACD signal (9) | -0.5887 |
| MACD histogram | 0.3556 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NVO': 273, 'SPY': 273}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 40.4500 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.1250 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 3.3734 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 8.3869 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -16.5304 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -14.1340 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 45.6806 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 34.0486 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.1177 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.1076 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 7.1341 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2627 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 44.0833 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.9361 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -43.6699 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.0877 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 11.7602 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 81.9870 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 42.5400 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 59.8150 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 9.8900 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 56.8265 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.3556 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -1.5949 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -6.5877 -> Clearly below the moving-average trend level.

## TAILWINDS

### Can Novo Nordisk (NYSE:NVO) Trade Below Fair Value On Earnings?
- Summary: Questioning if NVO trades below fair value based on earnings.
- Date: 2026-10-31 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxOc3ZtQjBQOENCS3Uxb1doRDc5a1l1bTVyRUxuSUN0Y3IxanZHMjJmWVlTTW5oVGR5V3p6YXlKdEc5a1BocUREd25DOHBJTC1jNnRDZGdpbGtzN2xTVmZYdDk4UVNEZXlFSElyTm9PYUJ3UXowV3JCcUlIWV9fWE5PLWx5UHlfZlRDbDBBT1NXcUFIUDVFdWpr?oc=5>

### Novo Nordisk (NVO) Could Be 62% Undervalued On GLP 1 Growth Expectations
- Summary: Analysts suggest Novo Nordisk may be undervalued by 62% based on GLP‑1 growth prospects, indicating potential upside for investors.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi4AFBVV95cUxNTW9IbnQyTkREY1JuNFFFNWllQUpxUnJFQnNjbjBfSlp2aUNUTnBCbTJmdGhCd2oyeDZPa01hV2R5WmhmNFQyNzRSM0d6anhaMUhYOWdpUFJpTXRZTWtJUXZaRmwyUzlJSHRHZW81cmZ6MkFVMTF6OHN3bDZ6RTRHWWpiWm53RXlld2xOLTMxVUxIaE5sRHJobUdWZFNRcll0ellkempJVWRzck0xYWJmWU84OWlUZW9KZWRyRjl5dmpia1dDOV9CX2tJbmpxbFlGSFlleTlWLVFGYXZlc3dSS9IB4AFBVV95cUxNTW9IbnQyTkREY1JuNFFFNWllQUpxUnJFQnNjbjBfSlp2aUNUTnBCbTJmdGhCd2oyeDZPa01hV2R5WmhmNFQyNzRSM0d6anhaMUhYOWdpUFJpTXRZTWtJUXZaRmwyUzlJSHRHZW81cmZ6MkFVMTF6OHN3bDZ6RTRHWWpiWm53RXlld2xOLTMxVUxIaE5sRHJobUdWZFNRcll0ellkempJVWRzck0xYWJmWU84OWlUZW9KZWRyRjl5dmpia1dDOV9CX2tJbmpxbFlGSFlleTlWLVFGYXZlc3dSSw?oc=5>

## HEADWINDS

### Novo Nordisk (CPSE:NOVO B) Stock Looks Cheap Even With Rival Pressure
- Summary: Novo Nordisk (CPSE:NOVO B) Stock Looks Cheap Even With Rival Pressure
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxOd0FrNlVNb2xVTWRmY191SEhMVGJmQWhpOVlfbG11WXFTOTdoUndqd3Fob0l6cEZkSU1oTXdlc3Y0UEo0azF0ZHFwMHRpaXg4NE1WNU5PeWQ4UDhKd2NHOFVYQkZodk1KLUd3OVNGQTEzZlExMnRxemhUVUluNkQ1UWVQMHZRbWxKUTdOUUQwLXhkNG8?oc=5>

## CATALYSTS

### Novo Nordisk Trades at 10 Times Earnings While Buying Back Billions in Stock. Is This the Bottom?
- Summary: Novo Nordisk Trades at 10 Times Earnings While Buying Back Billions in Stock. Is This the Bottom?
- Date: 2026-11-01 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQRkcxLUFGd0VDS2xKVmI4SlZhOHpqT1NjV2VRVGU2ekdvVnVIOWx5cWZLT19HNWdxTXN4Wk11MEVLaVkwN2lVR0tjTXRSNXd5MGxvLVJXb0dPUlhmNHhydDlGSzhvR3lYdzkyYUFiOG9Wb3VndE96R09TVVhySjkyajhBTGNNWHRJLVJxbHA4YmphRHpMT0p5cA?oc=5>

### Novo Nordisk set to report Q3 results as investors watch GLP-1 sales and outlook (NVO:NYSE)
- Summary: Novo Nordisk will release Q3 earnings, focusing on GLP‑1 sales performance and future outlook.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxQa2RjU1ZTM25sSHg5WWJmU0lHaVh4U0NYbk5ZazVPanBuOVMxSHpGUVQyWWNrUGFaUThjd0lYM0pkZlFqWDhYNTA5VVBYNTl6RFJNM216OUVobmZCVTJ0TW5Xb05ORi1mUF9rZUFQTVBoOW1QbXhJUmFfTVlnYzZXZVk3SWFiZVlaNE1Dc1VOSHZXNHg0anJqZjFKaXptdlBZalR1TDVBVEk2VmxDbmVXM2RDb2hHZGVFa2c?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NVO** | **9.89** | **5.39** | **1.58** | **2.10** | **178,412,208,128.00 USD** | **-14.13** |
| LLY | 45.80 | 31.23 | 28.00 | 38.60 | 1,256,832,368,640.00 USD | 64.56 |
| ROG.SW | N/A | N/A | N/A | N/A | N/A unknown currency | N/A |
| SAN.PA | 23.30 | 1.33 | 7.67 | 15.70 | 96,600,276,992.00 EUR | -4.40 |

Peers fetched as_of: 2026-11-02; NVO reuses existing data (market data as_of: 2026-11-02); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-04
- Next expected earnings: 2026-11-04 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-02

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: N/A
- Filing date: N/A
- Revenue (latest available single quarter): N/A
- Net income (latest available single quarter): N/A
- SEC link: N/A

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMilwFBVV95cUxOc3ZtQjBQOENCS3Uxb1doRDc5a1l1bTVyRUxuSUN0Y3IxanZHMjJmWVlTTW5oVGR5V3p6YXlKdEc5a1BocUREd25DOHBJTC1jNnRDZGdpbGtzN2xTVmZYdDk4UVNEZXlFSElyTm9PYUJ3UXowV3JCcUlIWV9fWE5PLWx5UHlfZlRDbDBBT1NXcUFIUDVFdWpr?oc=5
- https://news.google.com/rss/articles/CBMi4AFBVV95cUxNTW9IbnQyTkREY1JuNFFFNWllQUpxUnJFQnNjbjBfSlp2aUNUTnBCbTJmdGhCd2oyeDZPa01hV2R5WmhmNFQyNzRSM0d6anhaMUhYOWdpUFJpTXRZTWtJUXZaRmwyUzlJSHRHZW81cmZ6MkFVMTF6OHN3bDZ6RTRHWWpiWm53RXlld2xOLTMxVUxIaE5sRHJobUdWZFNRcll0ellkempJVWRzck0xYWJmWU84OWlUZW9KZWRyRjl5dmpia1dDOV9CX2tJbmpxbFlGSFlleTlWLVFGYXZlc3dSS9IB4AFBVV95cUxNTW9IbnQyTkREY1JuNFFFNWllQUpxUnJFQnNjbjBfSlp2aUNUTnBCbTJmdGhCd2oyeDZPa01hV2R5WmhmNFQyNzRSM0d6anhaMUhYOWdpUFJpTXRZTWtJUXZaRmwyUzlJSHRHZW81cmZ6MkFVMTF6OHN3bDZ6RTRHWWpiWm53RXlld2xOLTMxVUxIaE5sRHJobUdWZFNRcll0ellkempJVWRzck0xYWJmWU84OWlUZW9KZWRyRjl5dmpia1dDOV9CX2tJbmpxbFlGSFlleTlWLVFGYXZlc3dSSw?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxOd0FrNlVNb2xVTWRmY191SEhMVGJmQWhpOVlfbG11WXFTOTdoUndqd3Fob0l6cEZkSU1oTXdlc3Y0UEo0azF0ZHFwMHRpaXg4NE1WNU5PeWQ4UDhKd2NHOFVYQkZodk1KLUd3OVNGQTEzZlExMnRxemhUVUluNkQ1UWVQMHZRbWxKUTdOUUQwLXhkNG8?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQRkcxLUFGd0VDS2xKVmI4SlZhOHpqT1NjV2VRVGU2ekdvVnVIOWx5cWZLT19HNWdxTXN4Wk11MEVLaVkwN2lVR0tjTXRSNXd5MGxvLVJXb0dPUlhmNHhydDlGSzhvR3lYdzkyYUFiOG9Wb3VndE96R09TVVhySjkyajhBTGNNWHRJLVJxbHA4YmphRHpMT0p5cA?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxQa2RjU1ZTM25sSHg5WWJmU0lHaVh4U0NYbk5ZazVPanBuOVMxSHpGUVQyWWNrUGFaUThjd0lYM0pkZlFqWDhYNTA5VVBYNTl6RFJNM216OUVobmZCVTJ0TW5Xb05ORi1mUF9rZUFQTVBoOW1QbXhJUmFfTVlnYzZXZVk3SWFiZVlaNE1Dc1VOSHZXNHg0anJqZjFKaXptdlBZalR1TDVBVEk2VmxDbmVXM2RDb2hHZGVFa2c?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
