# ATD.TO Intelligence Report

- ticker: **ATD.TO**
- Report as_of: **2026-11-24**
- Market data as_of: **2026-11-24**
- Quant sources: https://finance.yahoo.com/quote/ATD.TO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/ATD.TO/key-statistics/
- AI analysis snapshot as_of: **2026-11-24**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-25T07:02:53.997568+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 7, 'rule': 1, 'ai': 5, 'unknown': 0, 'irrelevant': 1})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **0** exact headline/source/date matches; prior report **N/A** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 7 unique headlines; 6 named publishers; 0 exact duplicates; 7 HTTPS source links; largest publisher share 28.57%; oldest publication 2026-11-17

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 84.5000 |
| Return 1D (%) | 1.1007 |
| Return 1W (%) | 1.0161 |
| Return 1M (%) | 1.4041 |
| Return YTD (%) | 13.6027 |
| Return 1Y (%) | 20.4050 |
| Annualized volatility (%) | 26.3193 |
| Beta vs SPY | 0.1374 |
| Max drawdown (%) | -17.5708 |
| Sharpe (rf=0) | 0.8374 |
| Downside deviation (rf=0, %) | 15.3958 |
| Sortino (rf=0) | 1.4316 |
| Historical VaR 95% (1D, %) | 2.2683 |
| Historical ES 95% (1D, %) | 2.9356 |
| Correlation vs SPY | 0.0779 |
| Tracking error vs SPY (%) | 29.4708 |
| P/E (trailing) | 17.57 |
| P/B | 3.31 |
| EV/EBITDA | 14.00 |
| Revenue growth (%) | 25.10 |
| Forward P/E (estimate) | 16.77 |
| Gross margin (%) | 18.24 |
| Operating margin (%) | 5.88 |
| Return on equity (%) | 19.61 |
| Free cash flow yield (%) | N/A |
| MA50 | 80.9728 |
| Close vs MA50 (%) | 4.3560 |
| MA200 | 82.5342 |
| Close vs MA200 (%) | 2.3818 |
| RSI (14, Wilder) | 57.6255 |
| MACD (12,26) | 0.4130 |
| MACD signal (9) | 0.3952 |
| MACD histogram | 0.0178 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'ATD.TO': 288, 'SPY': 289}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 84.5000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.1007 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 1.0161 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 1.4041 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 13.6027 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 20.4050 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 26.3193 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 15.3958 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.4316 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.2683 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.9356 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.0779 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 29.4708 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.1374 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -17.5708 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.8374 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 16.7699 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 18.2380 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 5.8820 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 19.6150 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 17.5676 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 57.6255 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.0178 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 4.3560 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 2.3818 -> Slightly above the moving-average trend level.

## TAILWINDS

### Alimentation Couche-Tard (TSE:ATD) Stock Price Expected to Rise, National Bank Financial Analyst Says
- Summary: Analyst forecasts a rise in ATD.TO stock price.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi8gFBVV95cUxQMWo2MlZNR2VDM1dETl9PRk1YSnFwUzJCWkNQSy1xaEs0b3FfMGtzS2tpQVFYcS1OSHYwZlhsVDlfQ0E1QnF3NUVwb0ZNZkF2WUtkYW0tX09ybjVENi01bmlqZkh3RlJvajB5SDJpRHNRaG5kdWZpQW42YlZtYVpzV1pyaU1SUUxPRnh5VHdTeTJDX3RlVk9laVdZd2ROQmVvMUpmRE5tSER6eVFMd21Db2NyTmxlRGlaMzBobWI3YXRTNk1Dbmc0NmZnWUJ0bi1rV0dGOVNad3hnZHJlYWZfcmVra2N6OWQyc2RIM2FCOFpfZw?oc=5>

### Alimentation Couche-Tard (TSE:ATD) Stock Price Breaks Above 200-Day Moving Average - What's Next?
- Summary: ATD.TO stock surpasses 200‑day moving average, indicating bullish momentum.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi5gFBVV95cUxOampoZzBpQ3BsX3B3UFkxZWpvQ20wY2ZDdGVnMi1ZQk1mQWVxS2oxZ0RNQko0U21BRzhIdzhwNkpqc0VLWHo5UGZRRjRPQTNMZXJFRjBfT1ByVXdfcUtsRlBhZEhTS3NCM01FSGhDYXRvODhpNlNKVWlKZ3JHUnYxeEl3OWYxcmE5LUFmNmJNNWdJbm5CV2dZMWNiQks1azBRMC1Oek1iMU1waXJXaUs3dnV3VDRtVUxYZ25oTnAzNU9wVHIwSTBVQUc1ZTZkSFhsOHdSMWVsS2N1T3phUGFYVEp1NmQ3dw?oc=5>

## HEADWINDS

### Couche Tard (TSX:ATD) Stock Looks Below Fair Value Despite A 72% Run
- Summary: ATD.TO stock trades below fair value, suggesting potential downside.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi7AFBVV95cUxOWGFkVFNySzZOQVlrMUFkWHNlSS1ISm5FVWlVTElZUWZNOTFzR0pzZFJPaFRReHlQdE1yUU1TbVJtcUx5cDd2YkdnbFMyZmtkNTA4ZHc1Y3NfRFlnRXFiRkMtODlVRGVOQm1HY3FIMHZqWVl2aTFBTW9nWUYzREs5QmU4RHNTZUpfZzhBX1ExY0xTSE1kd1ZBcUpLcUJxdHc4VHc1R085UFBjWHQ4Qi1Na2kyWkZSYkdpOTJoUEQ1OFBMTVRWRTRWa2RzU0NFd0tJNUtldk9MU2FjbG1CSXVXdC1oYXZYLUhsdkZzOdIB8gFBVV95cUxNSU5sVk1iWEZTOEN1SXRSRlVRTDdJdlh4aks5ckRmcTJLNkZyUWNqLTVJQzUxbk9qb3o3XzFvRjJFOWNOTFJSTkJ0MVBhNEw2ckttTGs3Q2E3WkNKeHhiaDkxNno1TG1ZWXBIMkNEUV9RMTBxOENYaVMyV0I3VXhOWEc3NFlEOHJEUnlKVHhQYk1ZN3BHVjZpRjNOOUR0TkhfMGFMSjNUUDBaMUpjQW1CdF81OXlnR1ZObC1hbllucUp0cG1fQTdOTlpmQlJFQlZBYjBrWWtUeEs3Sl96bzJZSDIxSFlxMVFlTGprY3poT0JJUQ?oc=5>

## CATALYSTS

### Alimentation Couche-Tard Q2FY27 Results: Adj. EPS $0.84 beats estimate
- Summary: Alimentation Couche-Tard Q2FY27 Results: Adj. EPS $0.84 beats estimate
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxPOUxZQ1JxRVdEVGQ2Yktjalg5SnVZTEhfSE1vd25KOE9ONV9QMEI4ZmxEOUtzT21QdUtCYlEzRGtycy1DNUJ4dEhGUFB4OXRwS1lTTktkbWF1ckRVcUVCNVJ3Wm83M1Y3bDNMZ3Q2V1BwZ2xhMVp0ZFplLVhsUUxzVGlfWFVxaDRsVUdzRVM1MUZFT1hSV0xmcmk2aURQZG1JcUtBcG5mYlZVbGtO?oc=5>

### Couche-Tard earns US$691.3M second-quarter profit, down from US$740.6M last year
- Summary: ATD.TO reported Q2 profit of US$691.3M, slightly lower than last year.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMifkFVX3lxTFB5VnFJTHVMZkVjTkNEbTRLSzlwOTVWZF9BU0hmSVNlcHhUVVhYY2JockVJcVhzNFZrakpxUkphcVlIaWxTbUFaZWxDQ19GWVB4WTlTWGYtMlJUVnFPdDVwOHV1SzM5alRBd0ZJal91YnJvcmtpcDNmSklsVGRrQQ?oc=5>

### Couche-Tard Reports Fiscal 2027 Second-Quarter Results
- Summary: ATD.TO released fiscal 2027 Q2 results, indicating financial performance.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxNQjVTLWhvdUxpa3N1MDZQQS1qa05kWmRQTFdNVm52U0otYVdlYk0zMU5hNUlPVFVDeGxFcDBjU180dDRsTHYxbzA5bGVUdllaenpRdXRxdWxiZTdMNWp5dFgxT01aVF9FeUxseThaQjZIUGwyQUM4MVFmRmlVd2pFTHdUZ0ZlNnRLdy1WajZRRzZDNFlMSmExMjZaTHZZS2t2VXRRMzVydEZMUQ?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **ATD.TO** | **17.57** | **3.31** | **14.00** | **25.10** | **77,567,844,352.00 CAD** | **20.40** |
| CASY | 33.09 | 6.21 | 17.74 | 24.30 | 25,392,375,808.00 USD | 27.46 |
| MUSA | 14.36 | 11.64 | 9.21 | 39.30 | 9,237,832,704.00 USD | 39.76 |
| SUN | 10.96 | 1.23 | 6.87 | 198.90 | 11,952,979,968.00 USD | 21.99 |

Peers fetched as_of: 2026-11-24; ATD.TO reuses existing data (market data as_of: 2026-11-24); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-24
- Next expected earnings: N/A (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-24

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

- https://news.google.com/rss/articles/CBMi8gFBVV95cUxQMWo2MlZNR2VDM1dETl9PRk1YSnFwUzJCWkNQSy1xaEs0b3FfMGtzS2tpQVFYcS1OSHYwZlhsVDlfQ0E1QnF3NUVwb0ZNZkF2WUtkYW0tX09ybjVENi01bmlqZkh3RlJvajB5SDJpRHNRaG5kdWZpQW42YlZtYVpzV1pyaU1SUUxPRnh5VHdTeTJDX3RlVk9laVdZd2ROQmVvMUpmRE5tSER6eVFMd21Db2NyTmxlRGlaMzBobWI3YXRTNk1Dbmc0NmZnWUJ0bi1rV0dGOVNad3hnZHJlYWZfcmVra2N6OWQyc2RIM2FCOFpfZw?oc=5
- https://news.google.com/rss/articles/CBMi5gFBVV95cUxOampoZzBpQ3BsX3B3UFkxZWpvQ20wY2ZDdGVnMi1ZQk1mQWVxS2oxZ0RNQko0U21BRzhIdzhwNkpqc0VLWHo5UGZRRjRPQTNMZXJFRjBfT1ByVXdfcUtsRlBhZEhTS3NCM01FSGhDYXRvODhpNlNKVWlKZ3JHUnYxeEl3OWYxcmE5LUFmNmJNNWdJbm5CV2dZMWNiQks1azBRMC1Oek1iMU1waXJXaUs3dnV3VDRtVUxYZ25oTnAzNU9wVHIwSTBVQUc1ZTZkSFhsOHdSMWVsS2N1T3phUGFYVEp1NmQ3dw?oc=5
- https://news.google.com/rss/articles/CBMi7AFBVV95cUxOWGFkVFNySzZOQVlrMUFkWHNlSS1ISm5FVWlVTElZUWZNOTFzR0pzZFJPaFRReHlQdE1yUU1TbVJtcUx5cDd2YkdnbFMyZmtkNTA4ZHc1Y3NfRFlnRXFiRkMtODlVRGVOQm1HY3FIMHZqWVl2aTFBTW9nWUYzREs5QmU4RHNTZUpfZzhBX1ExY0xTSE1kd1ZBcUpLcUJxdHc4VHc1R085UFBjWHQ4Qi1Na2kyWkZSYkdpOTJoUEQ1OFBMTVRWRTRWa2RzU0NFd0tJNUtldk9MU2FjbG1CSXVXdC1oYXZYLUhsdkZzOdIB8gFBVV95cUxNSU5sVk1iWEZTOEN1SXRSRlVRTDdJdlh4aks5ckRmcTJLNkZyUWNqLTVJQzUxbk9qb3o3XzFvRjJFOWNOTFJSTkJ0MVBhNEw2ckttTGs3Q2E3WkNKeHhiaDkxNno1TG1ZWXBIMkNEUV9RMTBxOENYaVMyV0I3VXhOWEc3NFlEOHJEUnlKVHhQYk1ZN3BHVjZpRjNOOUR0TkhfMGFMSjNUUDBaMUpjQW1CdF81OXlnR1ZObC1hbllucUp0cG1fQTdOTlpmQlJFQlZBYjBrWWtUeEs3Sl96bzJZSDIxSFlxMVFlTGprY3poT0JJUQ?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxPOUxZQ1JxRVdEVGQ2Yktjalg5SnVZTEhfSE1vd25KOE9ONV9QMEI4ZmxEOUtzT21QdUtCYlEzRGtycy1DNUJ4dEhGUFB4OXRwS1lTTktkbWF1ckRVcUVCNVJ3Wm83M1Y3bDNMZ3Q2V1BwZ2xhMVp0ZFplLVhsUUxzVGlfWFVxaDRsVUdzRVM1MUZFT1hSV0xmcmk2aURQZG1JcUtBcG5mYlZVbGtO?oc=5
- https://news.google.com/rss/articles/CBMifkFVX3lxTFB5VnFJTHVMZkVjTkNEbTRLSzlwOTVWZF9BU0hmSVNlcHhUVVhYY2JockVJcVhzNFZrakpxUkphcVlIaWxTbUFaZWxDQ19GWVB4WTlTWGYtMlJUVnFPdDVwOHV1SzM5alRBd0ZJal91YnJvcmtpcDNmSklsVGRrQQ?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxNQjVTLWhvdUxpa3N1MDZQQS1qa05kWmRQTFdNVm52U0otYVdlYk0zMU5hNUlPVFVDeGxFcDBjU180dDRsTHYxbzA5bGVUdllaenpRdXRxdWxiZTdMNWp5dFgxT01aVF9FeUxseThaQjZIUGwyQUM4MVFmRmlVd2pFTHdUZ0ZlNnRLdy1WajZRRzZDNFlMSmExMjZaTHZZS2t2VXRRMzVydEZMUQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
