# SHOP.TO Intelligence Report

- ticker: **SHOP.TO**
- Report as_of: **2026-11-02**
- Market data as_of: **2026-11-02**
- Quant sources: https://finance.yahoo.com/quote/SHOP.TO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/SHOP.TO/key-statistics/
- AI analysis snapshot as_of: **2026-11-02**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-03T05:25:00.735830+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 4, 'rule': 1, 'ai': 2, 'unknown': 0, 'irrelevant': 1})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **2** exact headline/source/date matches; prior report **20261102T041627Z-c84a7052/SHOP.TO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 4 unique headlines; 3 named publishers; 0 exact duplicates; 4 HTTPS source links; largest publisher share 50.0%; oldest publication 2026-10-29

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 217.6400 |
| Return 1D (%) | -1.2388 |
| Return 1W (%) | -7.7523 |
| Return 1M (%) | 0.8246 |
| Return YTD (%) | -1.5204 |
| Return 1Y (%) | -10.7521 |
| Annualized volatility (%) | 57.7413 |
| Beta vs SPY | 1.7659 |
| Max drawdown (%) | -46.2010 |
| Sharpe (rf=0) | 0.0958 |
| Downside deviation (rf=0, %) | 40.4710 |
| Sortino (rf=0) | 0.1367 |
| Historical VaR 95% (1D, %) | 6.0545 |
| Historical ES 95% (1D, %) | 7.6952 |
| Correlation vs SPY | 0.3902 |
| Tracking error vs SPY (%) | 54.5426 |
| P/E (trailing) | 106.17 |
| P/B | 15.75 |
| EV/EBITDA | 114.93 |
| Revenue growth (%) | 33.70 |
| Forward P/E (estimate) | 63.08 |
| Gross margin (%) | 47.77 |
| Operating margin (%) | 17.55 |
| Return on equity (%) | 15.54 |
| Free cash flow yield (%) | N/A |
| MA50 | 213.7032 |
| Close vs MA50 (%) | 1.8422 |
| MA200 | 180.2532 |
| Close vs MA200 (%) | 20.7412 |
| RSI (14, Wilder) | 42.4768 |
| MACD (12,26) | 3.7098 |
| MACD signal (9) | 7.7471 |
| MACD histogram | -4.0373 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'SHOP.TO': 272, 'SPY': 273}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 217.6400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.2388 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -7.7523 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 0.8246 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -1.5204 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -10.7521 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 57.7413 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 40.4710 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.1367 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 6.0545 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 7.6952 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.3902 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 54.5426 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.7659 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -46.2010 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.0958 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 63.0763 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 47.7650 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 17.5550 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 15.5430 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 106.1659 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 42.4768 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -4.0373 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 1.8422 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 20.7412 -> Clearly above the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

No items in this run

## CATALYSTS

### Shopify (SHOP) to report earnings tomorrow: here is what to expect
- Summary: Shopify (SHOP) to report earnings tomorrow: here is what to expect
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxNdENoRHFmZEtZZFlGM0VYUDZyNmdOM1l0VTEtanFBTHNjNll5eG41ajZvNWxXam9xX2RqZWpINE95VlZmVktMdm5NSF9KWG8zOFU0R1JBMnd6cGZhdWVhRDc1N0g1cnRvY3A2RE9MY09jQUozQzJBUWgzUDFwcHk5TWU1RGI4WmdIa3V1VFVyYy00aGhLUk92Tl81R3dma21JbjhVTg?oc=5>

### Shopify Tokenized Stock (Robinhood) Price (SHOP/USD) Today | Live Price, Market Cap & Chart
- Summary: Shopify’s tokenized stock is now listed on Robinhood, offering a new trading format for investors.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMidEFVX3lxTE9JU3c2QTBJZkdUNVJUU05iNHlPa1ljN1pkOTB6WmJhM0M1alA2YkRnWmhjbDl1MXhpRXZxVHBzVFVjNXVRNWh6MkJrcUJlbHFNMDcwNTktaXNuc00tUC03Mk9SR190TEpLRl9Gc2p2RG82LTRX?oc=5>

### Ahead of Shopify Earnings, Here's What Barchart Data Says Comes Next for SHOP Stock
- Summary: Barchart data analysis predicts potential price movement for SHOP stock ahead of its earnings release.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxPWU5CU00wT0xFOHBZb0hDMXVuUVBNMHMzYlZZZjlDczdYaUpqeE9ScGd6Wk8xWWtrcTNCclRESlRjT3M3Ylk1UGpPR2V0dkxVa3hPOHhwSzF3Y0hiMThqYXRWczdKQlJ4YThNRlUydEtJOW4yWU5OSk05R3cxR29QQ0tqbGpTbWl1aE92eXpwYzFqRXRNbGFGLThodHhzX0tYYm9kRQ?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **SHOP.TO** | **106.17** | **15.75** | **114.93** | **33.70** | **282,421,559,296.00 CAD** | **-10.75** |
| WIX | N/A | -1.85 | -29.08 | 14.90 | 3,136,620,800.00 USD | -48.50 |
| CRM | 20.69 | 4.85 | 16.83 | 10.80 | 186,146,127,872.00 USD | -12.41 |
| GDDY | 16.04 | -102.74 | 11.79 | 6.00 | 14,768,389,120.00 USD | -12.41 |

Peers fetched as_of: 2026-11-02; SHOP.TO reuses existing data (market data as_of: 2026-11-02); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-05
- Next expected earnings: 2026-11-03 (yfinance; expected dates may change)

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

- https://news.google.com/rss/articles/CBMipAFBVV95cUxNdENoRHFmZEtZZFlGM0VYUDZyNmdOM1l0VTEtanFBTHNjNll5eG41ajZvNWxXam9xX2RqZWpINE95VlZmVktMdm5NSF9KWG8zOFU0R1JBMnd6cGZhdWVhRDc1N0g1cnRvY3A2RE9MY09jQUozQzJBUWgzUDFwcHk5TWU1RGI4WmdIa3V1VFVyYy00aGhLUk92Tl81R3dma21JbjhVTg?oc=5
- https://news.google.com/rss/articles/CBMidEFVX3lxTE9JU3c2QTBJZkdUNVJUU05iNHlPa1ljN1pkOTB6WmJhM0M1alA2YkRnWmhjbDl1MXhpRXZxVHBzVFVjNXVRNWh6MkJrcUJlbHFNMDcwNTktaXNuc00tUC03Mk9SR190TEpLRl9Gc2p2RG82LTRX?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxPWU5CU00wT0xFOHBZb0hDMXVuUVBNMHMzYlZZZjlDczdYaUpqeE9ScGd6Wk8xWWtrcTNCclRESlRjT3M3Ylk1UGpPR2V0dkxVa3hPOHhwSzF3Y0hiMThqYXRWczdKQlJ4YThNRlUydEtJOW4yWU5OSk05R3cxR29QQ0tqbGpTbWl1aE92eXpwYzFqRXRNbGFGLThodHhzX0tYYm9kRQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
