# NVDA Intelligence Report

- ticker: **NVDA**
- Report as_of: **2026-11-05**
- Market data as_of: **2026-11-05**
- Quant sources: https://finance.yahoo.com/quote/NVDA/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NVDA/key-statistics/
- AI analysis snapshot as_of: **2026-11-05**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-06T04:58:36.880719+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 0, 'ai': 8, 'unknown': 0, 'irrelevant': 16})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **2** exact headline/source/date matches; prior report **20261104T044411Z-6b13f9ec/NVDA** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'directional_claim_without_event_type': 1, 'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 15 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 25.0%; oldest publication 2026-11-02

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 181.6000 |
| Return 1D (%) | -9.2590 |
| Return 1W (%) | -15.0051 |
| Return 1M (%) | -23.9849 |
| Return YTD (%) | -2.3995 |
| Return 1Y (%) | -6.7491 |
| Annualized volatility (%) | 38.4245 |
| Beta vs SPY | 1.8912 |
| Max drawdown (%) | -24.0930 |
| Sharpe (rf=0) | 0.0089 |
| Downside deviation (rf=0, %) | 27.0772 |
| Sortino (rf=0) | 0.0126 |
| Historical VaR 95% (1D, %) | 3.9708 |
| Historical ES 95% (1D, %) | 4.9990 |
| Correlation vs SPY | 0.6690 |
| Tracking error vs SPY (%) | 31.0213 |
| P/E (trailing) | 22.96 |
| P/B | 19.15 |
| EV/EBITDA | 21.63 |
| Revenue growth (%) | 105.90 |
| Forward P/E (estimate) | 11.41 |
| Gross margin (%) | 74.67 |
| Operating margin (%) | 66.24 |
| Return on equity (%) | 117.21 |
| Free cash flow yield (%) | 0.95 |
| MA50 | 220.5949 |
| Close vs MA50 (%) | -17.6772 |
| MA200 | 204.3798 |
| Close vs MA200 (%) | -11.1458 |
| RSI (14, Wilder) | 25.3952 |
| MACD (12,26) | -7.2114 |
| MACD signal (9) | -4.2270 |
| MACD histogram | -2.9843 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NVDA': 276, 'SPY': 276}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 181.6000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -9.2590 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -15.0051 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -23.9849 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -2.3995 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -6.7491 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 38.4245 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 27.0772 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.0126 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.9708 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.9990 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6690 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 31.0213 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.8912 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -24.0930 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.0089 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 11.4109 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 74.6740 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 66.2370 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 117.2110 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 0.9535 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 22.9583 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 25.3952 -> Oversold momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -2.9843 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -17.6772 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -11.1458 -> Clearly below the moving-average trend level.

## TAILWINDS

### Nvidia Stock Looks Surprisingly Cheap. Why NVDA Could Rise 61%.
- Summary: Positive market sentiment suggests potential upside for NVDA shares.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxQYjA4NDQtRjBtaDZMX05LdkpMeWZrOVYxWFc2TTgtU0phdXlnc1RvZlJVb3NxWjlfbnkwY3VIOXpvZWpzUklKWEh3LTF6NVBxLWs3OWlsVDY2bXpwa2MwZXczNDhXelFzYUNfWHhwaDVKSnhWZnZDQ1FiRWN4TUNjUVdsaHNHWjJCMDNmbFR0SHFscGpZekx4b21zYmZ5aDVsSkF2UTRmQQ?oc=5>

### Stocks making the biggest moves midday: Micron, Tesla, Tripadvisor, AppLovin, Nvidia & more
- Summary: Nvidia among the biggest movers in the midday market.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxPQ3FKb0tTczRZcVFtbklBaFp2WWFCSU5zR1h3UEdPSERONW9PYUFhMmZ6aFV1U0Eta0ViYV9mM1B4NWVBTU9ELXByNm9aNVVYaDBhQXJtN1dDTzRzVUMycTUxaFA1aUw4aFE0Z1RrRDhtT0NLbDN3R0I3ZVY1OW1qaG9BUF9QLUFCampwdVp0U1RHUzRIZ0R3eFB1d2Z3Zw?oc=5>

### US Tech Stocks Wipe Out $1.7 Trillion as Nvidia, AMD Sink - NVIDIA (NASDAQ:NVDA)
- Summary: Nvidia stock fell, contributing to a large tech market decline.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxOVEtSSk90bnR0SzRoTHZrZnlvbW5YN2JEbjh2cThrRUF6bHpxemtNMXZRbVJKZDNkQWpnVUxULUNxamhIampHdWJEUkdnRzRaOXFxQm1KTTdVajlLZmxxTGc3NUJFY3lpNmptaGczckdHel9GdUc4RnB6UUt0bUNBdDduTVVRQXRwd1lxeHNaS3p0R1l5UjZyOVFHYmdfVjF5Qk9jS1pjamxLMGt6ZGNFeGFZUFEyWlE?oc=5>

### Nvidia Stock To $129?
- Summary: Speculation about Nvidia reaching $129, no confirmed event.
- Date: 2026-11-05 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMihwFBVV95cUxNM2VyR29oenNDRlVpaXRHSzI1djRKLXMwXzZDeDc0bGp4WEhObXgxMnRxVWQtMHdGQ0hRSTQzVFZIRUNzcTNsTVBzQ1R6ZUZNajV6d3VzODBTcjBjVUZBaDlYTWVVc2dTX3FMcjRobUJ3c2ZRNFMxN29vRzlKZHlIWlp6VkxRSnM?oc=5>

## HEADWINDS

### Nvidia Flashes Sell Signals As Earnings Loom; Is Nvidia A Buy Now?
- Summary: Negative sell signals ahead of earnings.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxQNlNYZi1HUzQyS0s4YlN6TUtGZG5JYXI3VXQ0cW1hNjhzNzlmQ2JSdGxSWTBuX1JiMW04LUVTcFptOE9ORjY1YjJRNG15cVpyaHBzVGZ0X3FLeGRyUUg0OVRlNWcwNUlCNzJ6ZWUtdEYtc0wyMFlIMzR4QjVlOHRwcHRKOFNoMnRQZjVOcg?oc=5>

### Why Nvidia Stock Is Getting Punished Today
- Summary: Nvidia shares fall, reflecting market concerns over valuation and earnings expectations.
- Date: 2026-11-05 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxPbFB5TmFOS1JyNlQ5UVA1OE1uaEpkY0tfZUlVX3J0NnN0MFA3SUxJSlM1SU9LOXl1NjFSaXRLZ1JicjJudEQ0dHMwcGY3cjd1Z0pfekg0WHhxSkFUazhkcEZvTFFiVm1pMjBvZzgtZmFDVFFhLW4wZFY3QTQzSzJCMHJJMXhHU2NRQjYyQTBkN25rcXRLZDlhYlBOYWlKX3M?oc=5>

### Nvidia has lost nearly $1.4 trillion since its October record
- Summary: Stock value decline signals long-term valuation pressure for Nvidia.
- Date: 2026-11-05 | Impact: high | Horizon: long | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxPc2NrRkNsOE94M2lLbzNWdWkwZWdyZmVNd2ZsTW0zcTNSWW4ySjBFeVJyaktrS0dtaWcxVC1keV9SLURsMkRKTnk1cklBUmxSRUM5TEFKci1TQlBWS01fNzFhUFR6LXdxVmRBdGduNzUtZi11dlE0alphdjRyQjEtdmFwR0Q2OWdMODFjdld3aTRzWmlDcGpVNHdEX0Zra2NFc09oc09Oamh3R3hlQ0Q1aHl1dGFVWk0?oc=5>

### Nvidia Just Dipped Below $200 for the First Time Since August
- Summary: Shares fall below $200, indicating short-term price weakness.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxNNVdZbm54VXJuc25IZ1R2ME01UTBpZGhsSXJ4TksyMTIwd1dORnJ6bDJzMTlweDRKdnpiajB3SExpemUtUkxUY3B3RjNYc2JVRHJYMW9vTVluOVloN0s5TlZYV2QzTnhOanpqTXY5UHhGMTF6blo2WnBkRXhWSktkWU5jY0JfVjZ6WjVJekhTdGhDU3V2YVkybQ?oc=5>

## CATALYSTS

No items in this run

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NVDA** | **22.96** | **19.15** | **21.63** | **105.90** | **4,385,095,286,784.00 USD** | **-6.75** |
| AMD | 104.50 | 9.70 | 58.93 | 44.70 | 663,251,320,832.00 USD | 57.77 |
| AVGO | 41.59 | 13.96 | 27.31 | 85.50 | 1,391,656,304,640.00 USD | -18.19 |
| INTC | N/A | 2.41 | 15.18 | 20.90 | 277,708,734,464.00 USD | 36.14 |

Peers fetched as_of: 2026-11-05; NVDA reuses existing data (market data as_of: 2026-11-05); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-26
- Next expected earnings: 2026-11-17 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-05

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-08-26
- Revenue (latest available single quarter): 96,221,000,000.00 USD; period 2026-04-27/2026-07-26; fiscal year/reporting period 2027/Q2
- Net income (latest available single quarter): 59,688,000,000.00 USD; period 2026-04-27/2026-07-26; fiscal year/reporting period 2027/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMipwFBVV95cUxQYjA4NDQtRjBtaDZMX05LdkpMeWZrOVYxWFc2TTgtU0phdXlnc1RvZlJVb3NxWjlfbnkwY3VIOXpvZWpzUklKWEh3LTF6NVBxLWs3OWlsVDY2bXpwa2MwZXczNDhXelFzYUNfWHhwaDVKSnhWZnZDQ1FiRWN4TUNjUVdsaHNHWjJCMDNmbFR0SHFscGpZekx4b21zYmZ5aDVsSkF2UTRmQQ?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxPQ3FKb0tTczRZcVFtbklBaFp2WWFCSU5zR1h3UEdPSERONW9PYUFhMmZ6aFV1U0Eta0ViYV9mM1B4NWVBTU9ELXByNm9aNVVYaDBhQXJtN1dDTzRzVUMycTUxaFA1aUw4aFE0Z1RrRDhtT0NLbDN3R0I3ZVY1OW1qaG9BUF9QLUFCampwdVp0U1RHUzRIZ0R3eFB1d2Z3Zw?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxOVEtSSk90bnR0SzRoTHZrZnlvbW5YN2JEbjh2cThrRUF6bHpxemtNMXZRbVJKZDNkQWpnVUxULUNxamhIampHdWJEUkdnRzRaOXFxQm1KTTdVajlLZmxxTGc3NUJFY3lpNmptaGczckdHel9GdUc4RnB6UUt0bUNBdDduTVVRQXRwd1lxeHNaS3p0R1l5UjZyOVFHYmdfVjF5Qk9jS1pjamxLMGt6ZGNFeGFZUFEyWlE?oc=5
- https://news.google.com/rss/articles/CBMihwFBVV95cUxNM2VyR29oenNDRlVpaXRHSzI1djRKLXMwXzZDeDc0bGp4WEhObXgxMnRxVWQtMHdGQ0hRSTQzVFZIRUNzcTNsTVBzQ1R6ZUZNajV6d3VzODBTcjBjVUZBaDlYTWVVc2dTX3FMcjRobUJ3c2ZRNFMxN29vRzlKZHlIWlp6VkxRSnM?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxQNlNYZi1HUzQyS0s4YlN6TUtGZG5JYXI3VXQ0cW1hNjhzNzlmQ2JSdGxSWTBuX1JiMW04LUVTcFptOE9ORjY1YjJRNG15cVpyaHBzVGZ0X3FLeGRyUUg0OVRlNWcwNUlCNzJ6ZWUtdEYtc0wyMFlIMzR4QjVlOHRwcHRKOFNoMnRQZjVOcg?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxPbFB5TmFOS1JyNlQ5UVA1OE1uaEpkY0tfZUlVX3J0NnN0MFA3SUxJSlM1SU9LOXl1NjFSaXRLZ1JicjJudEQ0dHMwcGY3cjd1Z0pfekg0WHhxSkFUazhkcEZvTFFiVm1pMjBvZzgtZmFDVFFhLW4wZFY3QTQzSzJCMHJJMXhHU2NRQjYyQTBkN25rcXRLZDlhYlBOYWlKX3M?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxPc2NrRkNsOE94M2lLbzNWdWkwZWdyZmVNd2ZsTW0zcTNSWW4ySjBFeVJyaktrS0dtaWcxVC1keV9SLURsMkRKTnk1cklBUmxSRUM5TEFKci1TQlBWS01fNzFhUFR6LXdxVmRBdGduNzUtZi11dlE0alphdjRyQjEtdmFwR0Q2OWdMODFjdld3aTRzWmlDcGpVNHdEX0Zra2NFc09oc09Oamh3R3hlQ0Q1aHl1dGFVWk0?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxNNVdZbm54VXJuc25IZ1R2ME01UTBpZGhsSXJ4TksyMTIwd1dORnJ6bDJzMTlweDRKdnpiajB3SExpemUtUkxUY3B3RjNYc2JVRHJYMW9vTVluOVloN0s5TlZYV2QzTnhOanpqTXY5UHhGMTF6blo2WnBkRXhWSktkWU5jY0JfVjZ6WjVJekhTdGhDU3V2YVkybQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
