# MG.TO Intelligence Report

- ticker: **MG.TO**
- Report as_of: **2026-11-25**
- Market data as_of: **2026-11-25**
- Quant sources: https://finance.yahoo.com/quote/MG.TO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/MG.TO/key-statistics/
- AI analysis snapshot as_of: **2026-11-25**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-26T06:51:00.498338+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 6, 'rule': 0, 'ai': 5, 'unknown': 0, 'irrelevant': 1})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **4** exact headline/source/date matches; prior report **20261125T065354Z-0b3565c6/MG.TO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'short_term_price_move_in_structural_risks': 1}
- RSS source audit (metadata only, not article fact-checking): 6 unique headlines; 4 named publishers; 0 exact duplicates; 6 HTTPS source links; largest publisher share 33.33%; oldest publication 2026-11-20

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 89.7800 |
| Return 1D (%) | 1.8954 |
| Return 1W (%) | 0.4251 |
| Return 1M (%) | 1.1266 |
| Return YTD (%) | 26.5181 |
| Return 1Y (%) | 33.3717 |
| Annualized volatility (%) | 37.0755 |
| Beta vs SPY | 1.0862 |
| Max drawdown (%) | -22.7904 |
| Sharpe (rf=0) | 0.9596 |
| Downside deviation (rf=0, %) | 21.7018 |
| Sortino (rf=0) | 1.6394 |
| Historical VaR 95% (1D, %) | 2.8820 |
| Historical ES 95% (1D, %) | 4.2406 |
| Correlation vs SPY | 0.4361 |
| Tracking error vs SPY (%) | 33.6743 |
| P/E (trailing) | 21.48 |
| P/B | 1.43 |
| EV/EBITDA | 6.53 |
| Revenue growth (%) | -3.90 |
| Forward P/E (estimate) | 8.10 |
| Gross margin (%) | 15.18 |
| Operating margin (%) | 5.74 |
| Return on equity (%) | 7.09 |
| Free cash flow yield (%) | N/A |
| MA50 | 89.4599 |
| Close vs MA50 (%) | 0.3578 |
| MA200 | 87.1212 |
| Close vs MA200 (%) | 3.0519 |
| RSI (14, Wilder) | 52.7964 |
| MACD (12,26) | -0.4473 |
| MACD signal (9) | -0.6400 |
| MACD histogram | 0.1927 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'MG.TO': 289, 'SPY': 290}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 89.7800 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.8954 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 0.4251 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 1.1266 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 26.5181 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 33.3717 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 37.0755 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 21.7018 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.6394 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.8820 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.2406 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4361 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 33.6743 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.0862 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -22.7904 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.9596 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 8.1015 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 15.1770 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 5.7440 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 7.0910 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 21.4785 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 52.7964 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.1927 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 0.3578 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 3.0519 -> Slightly above the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

No items in this run

## CATALYSTS

### Magna International Stock Price Forecast. Should You Buy MG.TO?
- Summary: Analyst forecast on Magna’s future stock performance, offering buying guidance.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiSkFVX3lxTE9SemxwVHBuQzhCb2Y4Rk1VZERTTEx0amYtamF2SFdpRUVvREVJOTlhdERzbk9QWkl1Y3FXSktzWmlPTWxkeFJKcW9B?oc=5>

### Here Is How Magna International (MGA) Is Positioned to Capitalize on US Midterms
- Summary: Analysis of Magna’s strategic positioning relative to upcoming US elections.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxPOHkzVEpWN3FxNXc5R0dYeVRKeGJaWEMtOEVYclVRNEc0ejBzeFh6aktVSEJlWFpIRzlPN3I1c2JFY1FqWk5udzZUTlBaVTItM2lZbTVfV2Z1VVUxZ3RmUXZOek1MdzFUNXUzbW9xTDJtSTJ2dHFxUmhJSkVDWXBmOEdSZEtrVURfaVpiNXdwbVd0cW4wMDlLWGRoa182d0lZNTNvUk0tdVRBZE1tbnln?oc=5>

### Magna International (TSX:MG): TSX Composite Large Cap Value Stock in Focus as Investors Track the Next Catalyst
- Summary: Investors monitoring Magna for upcoming catalyst events.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMi2wFBVV95cUxNb0ZhemNDMmNwR2xaMk5QOUc5WWJLQnE3RmhSekFfcVRhRE84TGZvdnM4ZTRJOVdoWVZfRUZCeVZQeUlNTkhxSUx5bE9zMnp2VnRqVERoMnZydHRSdFk1WE1CbHdZNFhkb3dQd3RqRlA2SnJGYmhuYThZUkpxbTRQN3ZWRElSR0xoNTBiMWVRMm1reEI5YTByY0RTd3VCa09hcGRlU05sMXpSc0JsT3RPUzhURU9ZNF9lTFlzbS1IbjRpMEpiZEdyNlFGS1BGenNRakhUSkZYYkNuRzQ?oc=5>

### Magna International (TSX:MG) Stock Trades At A Premium Following Its 36% Run
- Summary: MG.TO shares trade at a premium after a 36% run, indicating strong investor demand.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxPOVV4ekpkbndPR3lqOXlWSFFfTTVsLVBEbkhjNmlPeWpRMTVSSVNUa212TmxqT3Vyd2R0NUtmRE1lRnE0bC1OZmNZUjdkZl9JZFNUNnZiWTA0ZnJfVnB2T21xWGY0WlBRN0hkeDVRYlZVa0k4WDh4SEdnYnNnU1JUUXRhWUlNN2RXZjNVUHNRWEVpbWJBem5BNTBlVnA4QQ?oc=5>

## RISKS

### S&P/TSX Composite: Magna International Inc. (TSX:MG) — Large Cap Value Stock in Focus as Investors Track the Next Catalyst
- Summary: Investors monitoring potential future catalyst for Magna.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi6gFBVV95cUxNRXNyWDBReV9Kblh0WkE0X2hPTHlmbU9oY2Z1OE1GQldWX184bWg4b25lUTNuc1RVOXFtd2JGbklmMDZncFdiOGRzcFBHbEVnQTh0bXo0M2RCSG1BelhUNk9KdEtEYVluRktvNU1KeEE3TjdHNDZJY2MyNTdrLXpGeFU2UVlOWGtFNnBTcXdlSkxfeFNJb1BVdE5Oc3Foa0hOZEZlZE1kUEN0SGVKaGUxVjJjLTdwNUxTOGZfR2hSS2R1VW02OHRTbHlMS0pxanlpd05nMmJuWHltaHQtaXpjeWNfdlI3UFk4YlE?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **MG.TO** | **21.48** | **1.43** | **6.53** | **-3.90** | **23,197,671,424.00 CAD** | **33.37** |
| APTV | 10.49 | 0.87 | 3.94 | 2.30 | 7,601,249,280.00 USD | -50.84 |
| BWA | 21.08 | 1.78 | 5.88 | -2.90 | 10,119,020,544.00 USD | 16.96 |
| LEA | 9.06 | 1.00 | 4.59 | 1.60 | 5,014,382,080.00 USD | -1.53 |

Peers fetched as_of: 2026-11-25; MG.TO reuses existing data (market data as_of: 2026-11-25); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-30
- Next expected earnings: 2027-02-12 (yfinance; expected dates may change)

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

- https://news.google.com/rss/articles/CBMiSkFVX3lxTE9SemxwVHBuQzhCb2Y4Rk1VZERTTEx0amYtamF2SFdpRUVvREVJOTlhdERzbk9QWkl1Y3FXSktzWmlPTWxkeFJKcW9B?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxPOHkzVEpWN3FxNXc5R0dYeVRKeGJaWEMtOEVYclVRNEc0ejBzeFh6aktVSEJlWFpIRzlPN3I1c2JFY1FqWk5udzZUTlBaVTItM2lZbTVfV2Z1VVUxZ3RmUXZOek1MdzFUNXUzbW9xTDJtSTJ2dHFxUmhJSkVDWXBmOEdSZEtrVURfaVpiNXdwbVd0cW4wMDlLWGRoa182d0lZNTNvUk0tdVRBZE1tbnln?oc=5
- https://news.google.com/rss/articles/CBMi2wFBVV95cUxNb0ZhemNDMmNwR2xaMk5QOUc5WWJLQnE3RmhSekFfcVRhRE84TGZvdnM4ZTRJOVdoWVZfRUZCeVZQeUlNTkhxSUx5bE9zMnp2VnRqVERoMnZydHRSdFk1WE1CbHdZNFhkb3dQd3RqRlA2SnJGYmhuYThZUkpxbTRQN3ZWRElSR0xoNTBiMWVRMm1reEI5YTByY0RTd3VCa09hcGRlU05sMXpSc0JsT3RPUzhURU9ZNF9lTFlzbS1IbjRpMEpiZEdyNlFGS1BGenNRakhUSkZYYkNuRzQ?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxPOVV4ekpkbndPR3lqOXlWSFFfTTVsLVBEbkhjNmlPeWpRMTVSSVNUa212TmxqT3Vyd2R0NUtmRE1lRnE0bC1OZmNZUjdkZl9JZFNUNnZiWTA0ZnJfVnB2T21xWGY0WlBRN0hkeDVRYlZVa0k4WDh4SEdnYnNnU1JUUXRhWUlNN2RXZjNVUHNRWEVpbWJBem5BNTBlVnA4QQ?oc=5
- https://news.google.com/rss/articles/CBMi6gFBVV95cUxNRXNyWDBReV9Kblh0WkE0X2hPTHlmbU9oY2Z1OE1GQldWX184bWg4b25lUTNuc1RVOXFtd2JGbklmMDZncFdiOGRzcFBHbEVnQTh0bXo0M2RCSG1BelhUNk9KdEtEYVluRktvNU1KeEE3TjdHNDZJY2MyNTdrLXpGeFU2UVlOWGtFNnBTcXdlSkxfeFNJb1BVdE5Oc3Foa0hOZEZlZE1kUEN0SGVKaGUxVjJjLTdwNUxTOGZfR2hSS2R1VW02OHRTbHlMS0pxanlpd05nMmJuWHltaHQtaXpjeWNfdlI3UFk4YlE?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
