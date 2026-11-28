# NVO Intelligence Report

- ticker: **NVO**
- Report as_of: **2026-11-27**
- Market data as_of: **2026-11-27**
- Quant sources: https://finance.yahoo.com/quote/NVO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NVO/key-statistics/
- AI analysis snapshot as_of: **2026-11-27**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-28T06:29:25.635618+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 12, 'rule': 3, 'ai': 5, 'unknown': 0, 'irrelevant': 4})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **7** exact headline/source/date matches; prior report **20261127T063646Z-c0c26981/NVO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 12 unique headlines; 6 named publishers; 2 exact duplicates; 12 HTTPS source links; largest publisher share 50.0%; oldest publication 2026-11-20

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 41.0700 |
| Return 1D (%) | 0.2441 |
| Return 1W (%) | 8.5933 |
| Return 1M (%) | 6.2064 |
| Return YTD (%) | -15.2510 |
| Return 1Y (%) | -11.4755 |
| Annualized volatility (%) | 44.9778 |
| Beta vs SPY | 0.8942 |
| Max drawdown (%) | -43.6699 |
| Sharpe (rf=0) | -0.0729 |
| Downside deviation (rf=0, %) | 33.6675 |
| Sortino (rf=0) | -0.0974 |
| Historical VaR 95% (1D, %) | 3.1068 |
| Historical ES 95% (1D, %) | 6.9779 |
| Correlation vs SPY | 0.2986 |
| Tracking error vs SPY (%) | 42.9546 |
| P/E (trailing) | 10.37 |
| P/B | 5.53 |
| EV/EBITDA | 1.48 |
| Revenue growth (%) | 5.60 |
| Forward P/E (estimate) | 11.69 |
| Gross margin (%) | 83.33 |
| Operating margin (%) | 50.78 |
| Return on equity (%) | 58.38 |
| Free cash flow yield (%) | N/A |
| MA50 | 39.3994 |
| Close vs MA50 (%) | 4.2402 |
| MA200 | 42.1468 |
| Close vs MA200 (%) | -2.5549 |
| RSI (14, Wilder) | 55.0504 |
| MACD (12,26) | 0.0819 |
| MACD signal (9) | 0.0555 |
| MACD histogram | 0.0265 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NVO': 291, 'SPY': 291}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 41.0700 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.2441 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 8.5933 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 6.2064 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -15.2510 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -11.4755 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 44.9778 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 33.6675 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.0974 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.1068 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 6.9779 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2986 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 42.9546 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.8942 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -43.6699 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.0729 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 11.6927 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 83.3330 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 50.7790 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 58.3840 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 10.3712 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 55.0504 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.0265 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 4.2402 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -2.5549 -> Slightly below the moving-average trend level.

## TAILWINDS

### Novo Nordisk stock rises as buyer support drives momentum higher
- Summary: Novo Nordisk stock rises as buyer support drives momentum higher
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxOdUFicUo2TTNlNkxRLS1IMFJIYTBqalR2cWluRmtEQW1vUlZLSlZjMlZScE42VGRsbUlrQ1dsXzRfNzQ0ZWxjNlpjOXVxamR4anZLZGlpd2FjempBamRJV3BxVE9MVlJPY0R0bXV0US02MmFGTmhaaWNqZDNtR1hqWDJ2LVFoNDZjTlBIaw?oc=5>

### Novo Nordisk stock advances as weak momentum tempers recent gains
- Summary: Novo Nordisk stock advances as weak momentum tempers recent gains
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxPMk1tMTY4QmtJRGpxWllQZTZRNlpIeDN5enNfdDk3c043TVpTTlRsbEZjU0EwRVJFaktPX0ZkVm1mdjlXZ0FOd2JCbXlXdE5WTDJmWTR5c2tqa1h0cUswTUJZVGJONHBVMHV3LUF2UXJNM3hROWNVN0p4WXVLektDNFRueWxoc1VkQjZsSQ?oc=5>

### Novo Nordisk (NYSE: NVO) Trades At A Decade-Low Valuation Even As Its Wegovy Pill Dominates Oral GLP-1 Market
- Summary: Low valuation coupled with Wegovy market dominance signals potential upside.
- Date: 2026-11-22 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi6wFBVV95cUxPUkItU0xjMHAtejlZR1oybGZSOVhMd1VhRHZqS2pPSGx0ZmxzT1hRSHFZQ0tqVFNJeTVDaER1eXgxeTk5Slp5a05oZUhvc0xubm9TZ1Q1U0tTdnBwb1ROeklqQWZOSTIwaGhYckpCSHVSRmRSTXVLNUd3WE1acGJYcnZwMkRleWc2TWk2dEZjUmxScFB5aDlZY0xhTkpjN0tuZXFBazRXRzJjSHdqNjlvYy11Q2NUcnJjZUJ4VUIwbS03aWtrQTZDNTlYTWY5ekdoTm5MN1J6dUNXQ2pUN213Z1NBYWJRZm8wLUZJ?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Novo Nordisk stock gains more than 2% after FDA greenlights SOGROYA and repurchase plan advances
- Summary: Novo Nordisk stock gains more than 2% after FDA greenlights SOGROYA and repurchase plan advances
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxOcjB1NlROdkt0RnhrUUZpSHBHSUJqX2paVVNHNVlCdTdpS3I3WGlxSUZ2UUc4dVB6ek1LSFNtNEhiMTU3YWFyZ1BRU0g5LVlBY1dkN1ZnNUJsY01zTTRTV0gxSzM1WHcwTlo0TDduM21adGw0OUtpQ3FQeEp0TWhhOEktY1Utc0FWYUFaS09HNHo?oc=5>

### Novo Nordisk wins FDA Sogroya indication: NVO gains momentum
- Summary: FDA approval of Sogroya expands Novo Nordisk’s product portfolio, boosting market confidence.
- Date: 2026-11-25 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxNLXVhN29zLTItTC1tUV92bzRNdEdxdG9HR3dXNmdvdldlMGo4dW5nZjQwZHhkUHRjd0NaQllZMXlCUXRBZzk1eVpiZ3NEREp6WlVRWS1NN19TaEozaF9KbDVMendub2RVRERpb3g1MldwNzR4THdRQTFESWl1bm1pcGJKZndYejBQYUlyeA?oc=5>

### Novo Nordisk: The Wegovy Pill Opportunity Is Just Beginning (NYSE:NVO)
- Summary: Novo Nordisk highlights expanding Wegovy market potential, signaling growth prospects.
- Date: 2026-11-23 | Impact: medium | Horizon: medium | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxNejZkQ0NRNVZJNmdTUjVEZmQtZkxSVlFKM2Z4WUdRaXJaLUY2Q21QN2NBSDc5WllXOTNNaVBTcmhpb1lJbWpUaENCNnY2UWotdHJrb1FFVWpsczE0ejBjd3VocFplRkNJUGlGbVlkemlzcl9rU3ViOHZBc1gtNy00blJ5cmdVX24zcm5PS00wbFF1SURHMjB0VWxab2ZJU3Ez?oc=5>

### Will Novo Nordisk stock hold $35.78 support amid persistent downward momentum?
- Summary: Analysts question NVO's ability to maintain $35.78 support amid declining trend.
- Date: 2026-11-23 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxNd3ZTQzZNNUFpT0x5cXpTSldFMG1wVnJQejZQcWJQSzFBUkVMTUM2VGFDcHFJT0RLUWp0T3lhTHAxaEVnZWxFNXJFUHZNWjhRQVI1M0hmcTlqRzZzdXNsMmZNVi1vQmRENlZUT1F2MzQ3SW9BaEpBQzhWN0FnbTVBODY5RGUwYlA2SHhVWTJTMG02QQ?oc=5>

### Forget the Headlines: Novo Nordisk's (NVO) 4.6% Dividend Yield Is the Real Story for Patient Investors
- Summary: Novo Nordisk announces a 4.6% dividend yield, highlighting shareholder returns.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxNek1PY1YtNFZIWnlLTmNXWHdKbWJENkN5UWE0MmhYRWpINzUwY2tralIyOWQxX2pLRU44LUdxUF92aHNFLVFKdzl0ckk0dTVhdWZtaFdmYy03bll3SW41TWlMSHR1Z2xydHU1dWwwN0QtYzRJN3ZnUGRyeGl2Ty1VcC1mQkJScGo0eDFNUE9wcW5qbE0tQTNrSg?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NVO** | **10.37** | **5.53** | **1.48** | **5.60** | **180,964,474,880.00 USD** | **-11.48** |
| LLY | 45.19 | 30.81 | 27.64 | 38.60 | 1,240,255,561,728.00 USD | 26.85 |
| ROG.SW | N/A | N/A | N/A | N/A | N/A unknown currency | N/A |
| SAN.PA | 28.22 | 1.61 | 8.90 | 15.70 | 117,239,209,984.00 EUR | 21.02 |

Peers fetched as_of: 2026-11-27; NVO reuses existing data (market data as_of: 2026-11-27); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-04
- Next expected earnings: 2027-02-03 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-27

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
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

- https://news.google.com/rss/articles/CBMijAFBVV95cUxOdUFicUo2TTNlNkxRLS1IMFJIYTBqalR2cWluRmtEQW1vUlZLSlZjMlZScE42VGRsbUlrQ1dsXzRfNzQ0ZWxjNlpjOXVxamR4anZLZGlpd2FjempBamRJV3BxVE9MVlJPY0R0bXV0US02MmFGTmhaaWNqZDNtR1hqWDJ2LVFoNDZjTlBIaw?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxPMk1tMTY4QmtJRGpxWllQZTZRNlpIeDN5enNfdDk3c043TVpTTlRsbEZjU0EwRVJFaktPX0ZkVm1mdjlXZ0FOd2JCbXlXdE5WTDJmWTR5c2tqa1h0cUswTUJZVGJONHBVMHV3LUF2UXJNM3hROWNVN0p4WXVLektDNFRueWxoc1VkQjZsSQ?oc=5
- https://news.google.com/rss/articles/CBMi6wFBVV95cUxPUkItU0xjMHAtejlZR1oybGZSOVhMd1VhRHZqS2pPSGx0ZmxzT1hRSHFZQ0tqVFNJeTVDaER1eXgxeTk5Slp5a05oZUhvc0xubm9TZ1Q1U0tTdnBwb1ROeklqQWZOSTIwaGhYckpCSHVSRmRSTXVLNUd3WE1acGJYcnZwMkRleWc2TWk2dEZjUmxScFB5aDlZY0xhTkpjN0tuZXFBazRXRzJjSHdqNjlvYy11Q2NUcnJjZUJ4VUIwbS03aWtrQTZDNTlYTWY5ekdoTm5MN1J6dUNXQ2pUN213Z1NBYWJRZm8wLUZJ?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxOcjB1NlROdkt0RnhrUUZpSHBHSUJqX2paVVNHNVlCdTdpS3I3WGlxSUZ2UUc4dVB6ek1LSFNtNEhiMTU3YWFyZ1BRU0g5LVlBY1dkN1ZnNUJsY01zTTRTV0gxSzM1WHcwTlo0TDduM21adGw0OUtpQ3FQeEp0TWhhOEktY1Utc0FWYUFaS09HNHo?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxNLXVhN29zLTItTC1tUV92bzRNdEdxdG9HR3dXNmdvdldlMGo4dW5nZjQwZHhkUHRjd0NaQllZMXlCUXRBZzk1eVpiZ3NEREp6WlVRWS1NN19TaEozaF9KbDVMendub2RVRERpb3g1MldwNzR4THdRQTFESWl1bm1pcGJKZndYejBQYUlyeA?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxNejZkQ0NRNVZJNmdTUjVEZmQtZkxSVlFKM2Z4WUdRaXJaLUY2Q21QN2NBSDc5WllXOTNNaVBTcmhpb1lJbWpUaENCNnY2UWotdHJrb1FFVWpsczE0ejBjd3VocFplRkNJUGlGbVlkemlzcl9rU3ViOHZBc1gtNy00blJ5cmdVX24zcm5PS00wbFF1SURHMjB0VWxab2ZJU3Ez?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxNd3ZTQzZNNUFpT0x5cXpTSldFMG1wVnJQejZQcWJQSzFBUkVMTUM2VGFDcHFJT0RLUWp0T3lhTHAxaEVnZWxFNXJFUHZNWjhRQVI1M0hmcTlqRzZzdXNsMmZNVi1vQmRENlZUT1F2MzQ3SW9BaEpBQzhWN0FnbTVBODY5RGUwYlA2SHhVWTJTMG02QQ?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxNek1PY1YtNFZIWnlLTmNXWHdKbWJENkN5UWE0MmhYRWpINzUwY2tralIyOWQxX2pLRU44LUdxUF92aHNFLVFKdzl0ckk0dTVhdWZtaFdmYy03bll3SW41TWlMSHR1Z2xydHU1dWwwN0QtYzRJN3ZnUGRyeGl2Ty1VcC1mQkJScGo0eDFNUE9wcW5qbE0tQTNrSg?oc=5
- https://news.google.com/rss/articles/CBMijAJBVV95cUxPaXVTR0FQeXB1OElrWnlZS0JOdTJRWkJFVTk5TU1rYmYzR19VTkpvUjFRbWhPeWtSZEQyMUV0VHlVQU40eXBKRk5hcDlJdHNlaHJXM0dJQXo5YklrcDRVV0hBWThqSFJaWHhJd0RHTjZXd1oxYlJIdDJqbHpqeXI2Z0M3M0FVVDE2T0xuOVdVTy1FMjQ0MGJYRHJLWXRjTFpaVXBGMzVoaW01NGJNUnJDYXRpVnF4SmpkWWFIYWZVMTdmZDlRcWswQnlaTnRmeUhZalZqek8zc01MT3pzajlfOFBnU3E4QTc4YlZGdExCU3RzeXo1SjFwMlo0bjlSTXNvdEUyNEFHX0tqWEJQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
