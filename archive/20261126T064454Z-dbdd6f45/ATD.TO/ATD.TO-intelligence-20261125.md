# ATD.TO Intelligence Report

- ticker: **ATD.TO**
- Report as_of: **2026-11-25**
- Market data as_of: **2026-11-25**
- Quant sources: https://finance.yahoo.com/quote/ATD.TO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/ATD.TO/key-statistics/
- AI analysis snapshot as_of: **2026-11-25**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-26T07:06:37.641986+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 7, 'rule': 2, 'ai': 4, 'unknown': 0, 'irrelevant': 1})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **2** exact headline/source/date matches; prior report **20261125T065354Z-0b3565c6/ATD.TO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 7 unique headlines; 6 named publishers; 0 exact duplicates; 7 HTTPS source links; largest publisher share 28.57%; oldest publication 2026-11-18

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 85.3000 |
| Return 1D (%) | 0.9467 |
| Return 1W (%) | 2.7711 |
| Return 1M (%) | 2.3641 |
| Return YTD (%) | 14.6782 |
| Return 1Y (%) | 15.8605 |
| Annualized volatility (%) | 25.8839 |
| Beta vs SPY | 0.1165 |
| Max drawdown (%) | -17.5708 |
| Sharpe (rf=0) | 0.6979 |
| Downside deviation (rf=0, %) | 15.3958 |
| Sortino (rf=0) | 1.1734 |
| Historical VaR 95% (1D, %) | 2.2683 |
| Historical ES 95% (1D, %) | 2.9356 |
| Correlation vs SPY | 0.0670 |
| Tracking error vs SPY (%) | 29.2258 |
| P/E (trailing) | 17.73 |
| P/B | 3.34 |
| EV/EBITDA | 14.00 |
| Revenue growth (%) | 25.10 |
| Forward P/E (estimate) | 16.93 |
| Gross margin (%) | 18.24 |
| Operating margin (%) | 5.88 |
| Return on equity (%) | 19.61 |
| Free cash flow yield (%) | N/A |
| MA50 | 81.0854 |
| Close vs MA50 (%) | 5.1977 |
| MA200 | 82.5664 |
| Close vs MA200 (%) | 3.3107 |
| RSI (14, Wilder) | 59.9716 |
| MACD (12,26) | 0.5777 |
| MACD signal (9) | 0.4317 |
| MACD histogram | 0.1460 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'ATD.TO': 289, 'SPY': 290}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 85.3000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.9467 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 2.7711 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 2.3641 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 14.6782 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 15.8605 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 25.8839 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 15.3958 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.1734 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.2683 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.9356 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.0670 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 29.2258 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.1165 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -17.5708 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.6979 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 16.9286 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 18.2380 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 5.8820 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 19.6150 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 17.7339 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 59.9716 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.1460 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 5.1977 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 3.3107 -> Slightly above the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

### Alimentation Couche-Tard falls 3.45% in Thursday's session
- Summary: Alimentation Couche-Tard falls 3.45% in Thursday's session
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxOMVdPVE9UaHlCWEdOUGpVRmR4S0hGeHd0cXJELV9NN0tGakh1TERGUGdKdV9yYlREX1o5RkgzUWJtRy1xaTVlSWNoa2l2TGg4aFhTMlBxZlRvb0p3aVJUcUNCa3BhWUd1OV9jODFsblhzUWZtT2RqWF92aURuMl9vdG8xVlF4ZjNtaFVuRmJMSGY3bkk?oc=5>

## CATALYSTS

### Alimentation Couche-Tard Q2 2027 Earnings Call Transcript
- Summary: Alimentation Couche-Tard Q2 2027 Earnings Call Transcript
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxPMkhoLWR6V05peWk5c29DYVRsX0Q2LUFTZHpHNjJBSURJMmJ2NlYzZlBVQ2FNQTdkd2xjaGcxZWt3alN2b1ZOeklQVXprQXd0QU9zd1dtcU1USi02VkxwSVlubE5mSDlvU05EUHE4R3h4QXZBSGlBbkF0d0lyMm04RlVyVDJfMEpQUF9kcTdBeVJIbTZ5WWhGQ00xV1ZiQlJs?oc=5>

### Couche-Tard earns US$691.3M second-quarter profit, down from US$740.6M last year
- Summary: ATD.TO reported Q2 profit of US$691.3M, slightly lower than last year.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMifkFVX3lxTFB5VnFJTHVMZkVjTkNEbTRLSzlwOTVWZF9BU0hmSVNlcHhUVVhYY2JockVJcVhzNFZrakpxUkphcVlIaWxTbUFaZWxDQ19GWVB4WTlTWGYtMlJUVnFPdDVwOHV1SzM5alRBd0ZJal91YnJvcmtpcDNmSklsVGRrQQ?oc=5>

### Couche-Tard Reports Fiscal 2027 Second-Quarter Results
- Summary: ATD.TO released fiscal 2027 Q2 results, indicating financial performance.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxNQjVTLWhvdUxpa3N1MDZQQS1qa05kWmRQTFdNVm52U0otYVdlYk0zMU5hNUlPVFVDeGxFcDBjU180dDRsTHYxbzA5bGVUdllaenpRdXRxdWxiZTdMNWp5dFgxT01aVF9FeUxseThaQjZIUGwyQUM4MVFmRmlVd2pFTHdUZ0ZlNnRLdy1WajZRRzZDNFlMSmExMjZaTHZZS2t2VXRRMzVydEZMUQ?oc=5>

### Alimentation Couche-Tard (TSX: ATD) to report second-quarter results
- Summary: Company will release Q2 earnings, providing insight into performance and guidance.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxQOUkzbXdySEVsNVlzdHk0N0hNQkt0a2hLUml0akV4SndqaXNRbFE3dXo3NFk5RWFxb010emlNTTZoWHF2Q1pRQURPZXNWWnEwUWRXWGJCRGNMZHBWLVlxSnFPT2hvSkF6akJXUGRlcFNlM0xqbGhOdTkwVVo1MEl2WThXdnNLUEhYWUlKZ0tQN3BmZw?oc=5>

### Alimentation Couche Tard (TSX:ATD) Could Be 40% Undervalued On Zabka Deal Closing In December
- Summary: Potential undervaluation highlighted for upcoming Zabka acquisition closing.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxPR29jZklSR3ZOZ3VsNnhiQTY3SVlsb0c0OGFkeFlTUklmanNzUXJMYUg3ZDlFY3B5bUxCa3JseE5hVXZXR3RoWlcwQUNsNFREOFpFM2RDR0Z2cTRETlR5N1NmN0VlWEhCeXN2T3N0RTNGSTNJT1ZDVnQ1TmtmNnpyS2dieHNPSXJhRTU1NHpPaVRXWGFZMW9fSTVLMzd3UQ?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **ATD.TO** | **17.73** | **3.34** | **14.00** | **25.10** | **78,302,216,192.00 CAD** | **15.86** |
| CASY | 33.63 | 6.31 | 18.01 | 24.30 | 25,807,806,464.00 USD | 23.90 |
| MUSA | 14.45 | 11.72 | 9.26 | 39.30 | 9,299,915,776.00 USD | 36.52 |
| SUN | 10.35 | 1.22 | 6.83 | 198.90 | 11,775,870,976.00 USD | 19.71 |

Peers fetched as_of: 2026-11-25; ATD.TO reuses existing data (market data as_of: 2026-11-25); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-24
- Next expected earnings: 2027-03-16 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-25

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

- https://news.google.com/rss/articles/CBMikwFBVV95cUxOMVdPVE9UaHlCWEdOUGpVRmR4S0hGeHd0cXJELV9NN0tGakh1TERGUGdKdV9yYlREX1o5RkgzUWJtRy1xaTVlSWNoa2l2TGg4aFhTMlBxZlRvb0p3aVJUcUNCa3BhWUd1OV9jODFsblhzUWZtT2RqWF92aURuMl9vdG8xVlF4ZjNtaFVuRmJMSGY3bkk?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxPMkhoLWR6V05peWk5c29DYVRsX0Q2LUFTZHpHNjJBSURJMmJ2NlYzZlBVQ2FNQTdkd2xjaGcxZWt3alN2b1ZOeklQVXprQXd0QU9zd1dtcU1USi02VkxwSVlubE5mSDlvU05EUHE4R3h4QXZBSGlBbkF0d0lyMm04RlVyVDJfMEpQUF9kcTdBeVJIbTZ5WWhGQ00xV1ZiQlJs?oc=5
- https://news.google.com/rss/articles/CBMifkFVX3lxTFB5VnFJTHVMZkVjTkNEbTRLSzlwOTVWZF9BU0hmSVNlcHhUVVhYY2JockVJcVhzNFZrakpxUkphcVlIaWxTbUFaZWxDQ19GWVB4WTlTWGYtMlJUVnFPdDVwOHV1SzM5alRBd0ZJal91YnJvcmtpcDNmSklsVGRrQQ?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxNQjVTLWhvdUxpa3N1MDZQQS1qa05kWmRQTFdNVm52U0otYVdlYk0zMU5hNUlPVFVDeGxFcDBjU180dDRsTHYxbzA5bGVUdllaenpRdXRxdWxiZTdMNWp5dFgxT01aVF9FeUxseThaQjZIUGwyQUM4MVFmRmlVd2pFTHdUZ0ZlNnRLdy1WajZRRzZDNFlMSmExMjZaTHZZS2t2VXRRMzVydEZMUQ?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxQOUkzbXdySEVsNVlzdHk0N0hNQkt0a2hLUml0akV4SndqaXNRbFE3dXo3NFk5RWFxb010emlNTTZoWHF2Q1pRQURPZXNWWnEwUWRXWGJCRGNMZHBWLVlxSnFPT2hvSkF6akJXUGRlcFNlM0xqbGhOdTkwVVo1MEl2WThXdnNLUEhYWUlKZ0tQN3BmZw?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxPR29jZklSR3ZOZ3VsNnhiQTY3SVlsb0c0OGFkeFlTUklmanNzUXJMYUg3ZDlFY3B5bUxCa3JseE5hVXZXR3RoWlcwQUNsNFREOFpFM2RDR0Z2cTRETlR5N1NmN0VlWEhCeXN2T3N0RTNGSTNJT1ZDVnQ1TmtmNnpyS2dieHNPSXJhRTU1NHpPaVRXWGFZMW9fSTVLMzd3UQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
