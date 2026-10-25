# J Intelligence Report

- ticker: **J**
- Report as_of: **2026-10-24**
- Market data as_of: **2026-10-23**
- Quant sources: https://finance.yahoo.com/quote/J/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/J/key-statistics/
- AI analysis snapshot as_of: **2026-10-24**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-25T01:08:26.863878+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 5, 'rule': 2, 'ai': 2, 'unknown': 0, 'irrelevant': 1})
- AI model(s) actually used: **openai/gpt-oss-20b**
- RSS source audit (metadata only, not article fact-checking): 5 unique headlines; 2 named publishers; 0 exact duplicates; 5 HTTPS source links; largest publisher share 80.0%; oldest publication 2026-10-17

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 145.0600 |
| Return 1D (%) | -0.8205 |
| Return 1W (%) | 2.8211 |
| Return 1M (%) | 2.7920 |
| Return YTD (%) | 10.4124 |
| Return 1Y (%) | -8.8104 |
| Annualized volatility (%) | 32.6217 |
| Beta vs SPY | 0.7537 |
| Max drawdown (%) | -33.0387 |
| Sharpe (rf=0) | -0.1195 |
| Downside deviation (rf=0, %) | 24.4047 |
| Sortino (rf=0) | -0.1597 |
| Historical VaR 95% (1D, %) | 3.0123 |
| Historical ES 95% (1D, %) | 5.1035 |
| Correlation vs SPY | 0.2945 |
| Tracking error vs SPY (%) | 31.3327 |
| P/E (trailing) | 48.19 |
| P/B | 5.20 |
| EV/EBITDA | 18.78 |
| Revenue growth (%) | 34.50 |
| Forward P/E (estimate) | 17.61 |
| Gross margin (%) | 22.07 |
| Operating margin (%) | 7.39 |
| Return on equity (%) | 8.00 |
| Free cash flow yield (%) | 3.80 |
| MA50 | 143.1238 |
| Close vs MA50 (%) | 1.3528 |
| MA200 | 133.0413 |
| Close vs MA200 (%) | 9.0338 |
| RSI (14, Wilder) | 58.4617 |
| MACD (12,26) | 0.5556 |
| MACD signal (9) | -0.2437 |
| MACD histogram | 0.7993 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'J': 267, 'SPY': 267}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 145.0600 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.8205 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 2.8211 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 2.7920 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 10.4124 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -8.8104 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 32.6217 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 24.4047 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.1597 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.0123 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.1035 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2945 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 31.3327 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.7537 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -33.0387 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.1195 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 17.6110 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 22.0670 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 7.3870 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 7.9980 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 3.8031 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 48.1927 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 58.4617 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.7993 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 1.3528 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 9.0338 -> Clearly above the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

No items in this run

## CATALYSTS

### Jacobs Solutions (NYSE:J) Given New $188.00 Price Target at Citigroup
- Summary: Jacobs Solutions (NYSE:J) Given New $188.00 Price Target at Citigroup
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixgFBVV95cUxNVWt3SXc0OUxPa0gwSUhvTC1yamtETGZZVkxLczZHRUxYbjA1UFdyNHdzbGZvM2VvTy1jaU5jeldfZ2xuT3Q0Mk1IRWJUUTZHUGZXLXZLOS1EeTNsOEt4dWhrYkpHRkhiY1FQbDBNdXZENjJuQzBZcUpnRGQ0WGlINHpvS2tYWkdoUzdtQktNakswQ2JaZTVwSVBEdUdUTFMydWFhemxLaTMtVFdjU0xaWU5iWDU2RlZmb3FlaVJvcm9hOVQwX3c?oc=5>

### Jacobs Solutions Inc. $J Stock: Vontobel Holding Ltd. Cuts Holdings
- Summary: Jacobs Solutions Inc. $J Stock: Vontobel Holding Ltd. Cuts Holdings
- Date: 2026-10-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxOSi11dXZKWWFLbXJBa0RIWWRHTlJ0ZUREaThWVTVsM1JEX3JkWHdQVld5eDAtLTliWVJ2VGc4aDdUSWRKT0wzUEFDT2kyc1djTVhDeGNNQ1hRd3FUMy1VejZDQnFpakszMVNyMnJzRVBMWGJtMkMxWXY4b21wUzI0ZkE4a29KQ0VUMjRfZnRtNURBMWpxOEJINjdncHlCMjVweHQ1ME5acXZtOVVhWTQ4S3BSQW15MGZhVldZRVN6X3NKdw?oc=5>

### 10,300 Jacobs Solutions Inc. $J Shares Bought by Oakmont Investment Advisors Inc.
- Summary: Oakmont Investment Advisors purchased 10,300 shares of Jacobs Solutions, indicating a bullish stance on the company.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi1AFBVV95cUxQOTl5czh5NTlHRUZyY2lQekNWNXFDZXE3cUo2QzBuWHRxOFdCb2RWNlBFMW13LXhfdVB2QzRQVk12YlYySFlhR0N1NFJyaXZCMHdaZ2Rhc18taUpOREpza3VaU1o1NGhMLTNIUnp0dm5KM0c2UHBwYlU3MUg3SzJQLWNIX3hqUEVmN3EzUVlQU1dWcC1iaGstRWVvMk5SYmo0NnNhdlJNWHlPTTdtR3dPbm80OXd6dk1LdGFUUGJNS2N0MmhFd3lFTE1sM2dwRTVUZVo1dQ?oc=5>

### Curated Wealth Partners LLC Sells 102,292 Shares of Jacobs Solutions Inc. $J
- Summary: Curated Wealth Partners sold 102,292 shares of Jacobs Solutions, reflecting a divestment or portfolio rebalancing.
- Date: 2026-10-19 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMizwFBVV95cUxPalBtYWs2a09KQ2lXcUdXSmhYM1NBR05LQ2VzNDhwTzNVZ2RFRkk4bzR1TUFQTG9mUnRraVFPajZWZGNxY2trelBySXB0UE1DQXdOdE1GMVpGUXp1UzU1NDBQZlVMbmtzR2xMQmx4dEhYREdHSHRKUnRLc053ZDVfbWlpRmdHMllTdWxwTFZsSm9DTTJnbHdQYjg0SnVZU3hjS2taM1ZsUF9MRXRQaXhmTnR1WEFjRnFncWd3a3RoTTdWMEdPQzFiZjhROHM5b2s?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **J** | **48.19** | **5.20** | **18.78** | **34.50** | **16,977,619,968.00 USD** | **-8.81** |
| ACM | 21.30 | 3.55 | 11.05 | -14.20 | 7,784,846,848.00 USD | -53.59 |
| FLR | N/A | 2.22 | -17.25 | 8.80 | 5,891,293,696.00 USD | -7.59 |
| KBR | 11.78 | 3.02 | 11.02 | 1.60 | 4,945,637,888.00 USD | -10.03 |

Peers fetched as_of: 2026-10-24; J reuses existing data (market data as_of: 2026-10-23); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-04
- Next expected earnings: 2026-11-19 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-24

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

- https://news.google.com/rss/articles/CBMixgFBVV95cUxNVWt3SXc0OUxPa0gwSUhvTC1yamtETGZZVkxLczZHRUxYbjA1UFdyNHdzbGZvM2VvTy1jaU5jeldfZ2xuT3Q0Mk1IRWJUUTZHUGZXLXZLOS1EeTNsOEt4dWhrYkpHRkhiY1FQbDBNdXZENjJuQzBZcUpnRGQ0WGlINHpvS2tYWkdoUzdtQktNakswQ2JaZTVwSVBEdUdUTFMydWFhemxLaTMtVFdjU0xaWU5iWDU2RlZmb3FlaVJvcm9hOVQwX3c?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxOSi11dXZKWWFLbXJBa0RIWWRHTlJ0ZUREaThWVTVsM1JEX3JkWHdQVld5eDAtLTliWVJ2VGc4aDdUSWRKT0wzUEFDT2kyc1djTVhDeGNNQ1hRd3FUMy1VejZDQnFpakszMVNyMnJzRVBMWGJtMkMxWXY4b21wUzI0ZkE4a29KQ0VUMjRfZnRtNURBMWpxOEJINjdncHlCMjVweHQ1ME5acXZtOVVhWTQ4S3BSQW15MGZhVldZRVN6X3NKdw?oc=5
- https://news.google.com/rss/articles/CBMi1AFBVV95cUxQOTl5czh5NTlHRUZyY2lQekNWNXFDZXE3cUo2QzBuWHRxOFdCb2RWNlBFMW13LXhfdVB2QzRQVk12YlYySFlhR0N1NFJyaXZCMHdaZ2Rhc18taUpOREpza3VaU1o1NGhMLTNIUnp0dm5KM0c2UHBwYlU3MUg3SzJQLWNIX3hqUEVmN3EzUVlQU1dWcC1iaGstRWVvMk5SYmo0NnNhdlJNWHlPTTdtR3dPbm80OXd6dk1LdGFUUGJNS2N0MmhFd3lFTE1sM2dwRTVUZVo1dQ?oc=5
- https://news.google.com/rss/articles/CBMizwFBVV95cUxPalBtYWs2a09KQ2lXcUdXSmhYM1NBR05LQ2VzNDhwTzNVZ2RFRkk4bzR1TUFQTG9mUnRraVFPajZWZGNxY2trelBySXB0UE1DQXdOdE1GMVpGUXp1UzU1NDBQZlVMbmtzR2xMQmx4dEhYREdHSHRKUnRLc053ZDVfbWlpRmdHMllTdWxwTFZsSm9DTTJnbHdQYjg0SnVZU3hjS2taM1ZsUF9MRXRQaXhmTnR1WEFjRnFncWd3a3RoTTdWMEdPQzFiZjhROHM5b2s?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
