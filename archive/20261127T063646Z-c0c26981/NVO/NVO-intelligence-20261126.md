# NVO Intelligence Report

- ticker: **NVO**
- Report as_of: **2026-11-26**
- Market data as_of: **2026-11-25**
- Quant sources: https://finance.yahoo.com/quote/NVO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NVO/key-statistics/
- AI analysis snapshot as_of: **2026-11-26**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-27T06:38:09.439302+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 15, 'rule': 2, 'ai': 5, 'unknown': 0, 'irrelevant': 8})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **11** exact headline/source/date matches; prior report **20261126T064454Z-dbdd6f45/NVO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 15 unique headlines; 8 named publishers; 0 exact duplicates; 15 HTTPS source links; largest publisher share 33.33%; oldest publication 2026-11-20

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 40.9700 |
| Return 1D (%) | 1.6373 |
| Return 1W (%) | 3.9057 |
| Return 1M (%) | 4.9168 |
| Return YTD (%) | -15.4574 |
| Return 1Y (%) | -8.5948 |
| Annualized volatility (%) | 45.0446 |
| Beta vs SPY | 0.9133 |
| Max drawdown (%) | -43.6699 |
| Sharpe (rf=0) | 0.0295 |
| Downside deviation (rf=0, %) | 33.6003 |
| Sortino (rf=0) | 0.0396 |
| Historical VaR 95% (1D, %) | 3.1053 |
| Historical ES 95% (1D, %) | 6.9779 |
| Correlation vs SPY | 0.3027 |
| Tracking error vs SPY (%) | 42.9507 |
| P/E (trailing) | 10.35 |
| P/B | 5.52 |
| EV/EBITDA | 1.48 |
| Revenue growth (%) | 5.60 |
| Forward P/E (estimate) | 11.66 |
| Gross margin (%) | 83.33 |
| Operating margin (%) | 50.78 |
| Return on equity (%) | 58.38 |
| Free cash flow yield (%) | N/A |
| MA50 | 39.4418 |
| Close vs MA50 (%) | 3.8746 |
| MA200 | 42.1736 |
| Close vs MA200 (%) | -2.8538 |
| RSI (14, Wilder) | 54.6016 |
| MACD (12,26) | -0.0002 |
| MACD signal (9) | 0.0489 |
| MACD histogram | -0.0490 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NVO': 290, 'SPY': 290}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 40.9700 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.6373 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 3.9057 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 4.9168 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -15.4574 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -8.5948 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 45.0446 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 33.6003 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.0396 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.1053 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 6.9779 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.3027 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 42.9507 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.9133 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -43.6699 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.0295 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 11.6643 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 83.3330 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 50.7790 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 58.3840 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 10.3460 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 54.6016 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.0490 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 3.8746 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -2.8538 -> Slightly below the moving-average trend level.

## TAILWINDS

### Novo Nordisk stock advances as weak momentum tempers recent gains
- Summary: Novo Nordisk stock advances as weak momentum tempers recent gains
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxPMk1tMTY4QmtJRGpxWllQZTZRNlpIeDN5enNfdDk3c043TVpTTlRsbEZjU0EwRVJFaktPX0ZkVm1mdjlXZ0FOd2JCbXlXdE5WTDJmWTR5c2tqa1h0cUswTUJZVGJONHBVMHV3LUF2UXJNM3hROWNVN0p4WXVLektDNFRueWxoc1VkQjZsSQ?oc=5>

### Novo Nordisk (NYSE: NVO) Trades At A Decade-Low Valuation Even As Its Wegovy Pill Dominates Oral GLP-1 Market
- Summary: Low valuation coupled with Wegovy market dominance signals potential upside.
- Date: 2026-11-22 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi6wFBVV95cUxPUkItU0xjMHAtejlZR1oybGZSOVhMd1VhRHZqS2pPSGx0ZmxzT1hRSHFZQ0tqVFNJeTVDaER1eXgxeTk5Slp5a05oZUhvc0xubm9TZ1Q1U0tTdnBwb1ROeklqQWZOSTIwaGhYckpCSHVSRmRSTXVLNUd3WE1acGJYcnZwMkRleWc2TWk2dEZjUmxScFB5aDlZY0xhTkpjN0tuZXFBazRXRzJjSHdqNjlvYy11Q2NUcnJjZUJ4VUIwbS03aWtrQTZDNTlYTWY5ekdoTm5MN1J6dUNXQ2pUN213Z1NBYWJRZm8wLUZJ?oc=5>

### Novo Nordisk (NYSE: NVO) Targets Underserved Pediatric Patients As Weekly Sogroya Clears FDA Hurdle
- Summary: Novo Nordisk announces Sogroya FDA clearance, targeting underserved pediatric patients, indicating product expansion and potential revenue growth.
- Date: 2026-11-24 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMi3gFBVV95cUxPcm1NaWN5SEV1VVFwdHhCaXMzNndhcVlnNTltZmx0anN2QURxejJqSnlfczEtNjNSZDhDMjdKaTcweFNaeUp1VDhyckpGX0xmVEp1RGlDSWFHWDlPNFJsM2t5UnNIRGlEaFFHWnVmRC0weTk1bFpMSDdydEEzMVhKNld4anUtdGhUMEw2TE4tR2dvNjBwNWxZaFNxT2tGaVdDRGtsU1hZbkh2cjRDdmRKdTBGSzA0czl1dXJ1bmhLaTJWZmw1VE9zT0hGLXQ4QS0yMlAxeTgteWxJUGl2UFE?oc=5>

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

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NVO** | **10.35** | **5.52** | **1.48** | **5.60** | **180,523,859,968.00 USD** | **-8.59** |
| LLY | 45.19 | 30.81 | 27.64 | 38.60 | 1,240,112,955,392.00 USD | 26.19 |
| ROG.SW | N/A | N/A | N/A | N/A | N/A unknown currency | N/A |
| SAN.PA | 28.16 | 1.63 | 8.99 | 15.70 | 118,655,926,272.00 EUR | 19.98 |

Peers fetched as_of: 2026-11-26; NVO reuses existing data (market data as_of: 2026-11-25); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-04
- Next expected earnings: 2027-02-03 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-26

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

- https://news.google.com/rss/articles/CBMijAFBVV95cUxPMk1tMTY4QmtJRGpxWllQZTZRNlpIeDN5enNfdDk3c043TVpTTlRsbEZjU0EwRVJFaktPX0ZkVm1mdjlXZ0FOd2JCbXlXdE5WTDJmWTR5c2tqa1h0cUswTUJZVGJONHBVMHV3LUF2UXJNM3hROWNVN0p4WXVLektDNFRueWxoc1VkQjZsSQ?oc=5
- https://news.google.com/rss/articles/CBMi6wFBVV95cUxPUkItU0xjMHAtejlZR1oybGZSOVhMd1VhRHZqS2pPSGx0ZmxzT1hRSHFZQ0tqVFNJeTVDaER1eXgxeTk5Slp5a05oZUhvc0xubm9TZ1Q1U0tTdnBwb1ROeklqQWZOSTIwaGhYckpCSHVSRmRSTXVLNUd3WE1acGJYcnZwMkRleWc2TWk2dEZjUmxScFB5aDlZY0xhTkpjN0tuZXFBazRXRzJjSHdqNjlvYy11Q2NUcnJjZUJ4VUIwbS03aWtrQTZDNTlYTWY5ekdoTm5MN1J6dUNXQ2pUN213Z1NBYWJRZm8wLUZJ?oc=5
- https://news.google.com/rss/articles/CBMi3gFBVV95cUxPcm1NaWN5SEV1VVFwdHhCaXMzNndhcVlnNTltZmx0anN2QURxejJqSnlfczEtNjNSZDhDMjdKaTcweFNaeUp1VDhyckpGX0xmVEp1RGlDSWFHWDlPNFJsM2t5UnNIRGlEaFFHWnVmRC0weTk1bFpMSDdydEEzMVhKNld4anUtdGhUMEw2TE4tR2dvNjBwNWxZaFNxT2tGaVdDRGtsU1hZbkh2cjRDdmRKdTBGSzA0czl1dXJ1bmhLaTJWZmw1VE9zT0hGLXQ4QS0yMlAxeTgteWxJUGl2UFE?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxOcjB1NlROdkt0RnhrUUZpSHBHSUJqX2paVVNHNVlCdTdpS3I3WGlxSUZ2UUc4dVB6ek1LSFNtNEhiMTU3YWFyZ1BRU0g5LVlBY1dkN1ZnNUJsY01zTTRTV0gxSzM1WHcwTlo0TDduM21adGw0OUtpQ3FQeEp0TWhhOEktY1Utc0FWYUFaS09HNHo?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxNLXVhN29zLTItTC1tUV92bzRNdEdxdG9HR3dXNmdvdldlMGo4dW5nZjQwZHhkUHRjd0NaQllZMXlCUXRBZzk1eVpiZ3NEREp6WlVRWS1NN19TaEozaF9KbDVMendub2RVRERpb3g1MldwNzR4THdRQTFESWl1bm1pcGJKZndYejBQYUlyeA?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxNejZkQ0NRNVZJNmdTUjVEZmQtZkxSVlFKM2Z4WUdRaXJaLUY2Q21QN2NBSDc5WllXOTNNaVBTcmhpb1lJbWpUaENCNnY2UWotdHJrb1FFVWpsczE0ejBjd3VocFplRkNJUGlGbVlkemlzcl9rU3ViOHZBc1gtNy00blJ5cmdVX24zcm5PS00wbFF1SURHMjB0VWxab2ZJU3Ez?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxNd3ZTQzZNNUFpT0x5cXpTSldFMG1wVnJQejZQcWJQSzFBUkVMTUM2VGFDcHFJT0RLUWp0T3lhTHAxaEVnZWxFNXJFUHZNWjhRQVI1M0hmcTlqRzZzdXNsMmZNVi1vQmRENlZUT1F2MzQ3SW9BaEpBQzhWN0FnbTVBODY5RGUwYlA2SHhVWTJTMG02QQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
