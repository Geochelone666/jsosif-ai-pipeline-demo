# SCHW Intelligence Report

- ticker: **SCHW**
- Report as_of: **2026-11-13**
- Market data as_of: **2026-11-13**
- Quant sources: https://finance.yahoo.com/quote/SCHW/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/SCHW/key-statistics/
- AI analysis snapshot as_of: **2026-11-13**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-14T05:05:09.736631+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 4, 'rule': 0, 'ai': 3, 'unknown': 0, 'irrelevant': 1})
- AI model(s) actually used: **N/A (no successful AI classification call)**
- Verified recent classification reuse: **4** exact headline/source/date matches; prior report **20261113T045636Z-34122c9a/SCHW** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 4 unique headlines; 4 named publishers; 0 exact duplicates; 4 HTTPS source links; largest publisher share 25.0%; oldest publication 2026-11-09

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 92.9800 |
| Return 1D (%) | 1.7287 |
| Return 1W (%) | 1.9844 |
| Return 1M (%) | -2.7460 |
| Return YTD (%) | -5.6846 |
| Return 1Y (%) | -0.9038 |
| Annualized volatility (%) | 25.8369 |
| Beta vs SPY | 0.4316 |
| Max drawdown (%) | -22.5253 |
| Sharpe (rf=0) | 0.0947 |
| Downside deviation (rf=0, %) | 19.6025 |
| Sortino (rf=0) | 0.1249 |
| Historical VaR 95% (1D, %) | 2.5523 |
| Historical ES 95% (1D, %) | 3.9505 |
| Correlation vs SPY | 0.2277 |
| Tracking error vs SPY (%) | 26.3246 |
| P/E (trailing) | 15.68 |
| P/B | 3.55 |
| EV/EBITDA | N/A |
| Revenue growth (%) | 16.90 |
| Forward P/E (estimate) | 11.92 |
| Gross margin (%) | 97.51 |
| Operating margin (%) | 51.11 |
| Return on equity (%) | 21.11 |
| Free cash flow yield (%) | N/A |
| MA50 | 96.4851 |
| Close vs MA50 (%) | -3.6328 |
| MA200 | 96.3536 |
| Close vs MA200 (%) | -3.5013 |
| RSI (14, Wilder) | 50.6140 |
| MACD (12,26) | -0.9870 |
| MACD signal (9) | -1.7315 |
| MACD histogram | 0.7445 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'SCHW': 282, 'SPY': 282}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 92.9800 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.7287 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 1.9844 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -2.7460 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -5.6846 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -0.9038 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 25.8369 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 19.6025 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.1249 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.5523 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.9505 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2277 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 26.3246 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.4316 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -22.5253 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.0947 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 11.9157 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 97.5060 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 51.1070 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 21.1130 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 15.6796 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 50.6140 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.7445 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -3.6328 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -3.5013 -> Slightly below the moving-average trend level.

## TAILWINDS

### Eligible Charles Schwab clients can now trade five cryptocurrencies
- Summary: Schwab expands crypto trading to clients.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxOOUxpUDlrMFpvVk5xR1daQ0NpWW1ybHZISEhBdHBEQXQ2b3BRc0FMWlFsbDBTWTZVYzhUaU1sdC1WUDkxTjhkdWFfc1dZYS14ZUtMd1hCNFdFNW9FLUFCT3IxaFZLU2FjM3VSWDU3U2UtZkZNZjNpY2Zna09rYzBfT3A5cG16cjVsVDBlY05PNXhpR2dHY2tfYjJma1RzQ2ZpeS1aR2pUTlQxaEJma0pEb3BpcmU2TFUwZFJj?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### What Is Charles Schwab (SCHW) Signaling By Adding Solana, Avalanche And Chainlink?
- Summary: Schwab adds Solana, Avalanche, and Chainlink to its platform, expanding crypto offerings.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxPZ2p3WG9NSmZCbDZZUzZDaFh4RE9QeEg4YVZBTUFmbHpxWUZVTWdUR24tX1NaWEVBYVVUMWJiZ1NSWVhJUVNTN2Y5ZEZvbjM5Y3hoczdZLWpmdGJ3UFE5WXZXcU8zcTMwVmM5MVl4Xy1xQmMzNXRwOXFmTm9nOTQxZ1JreEVjMFhMWWItYmdZcEV2R1FsZlI4ZnB1RDdELWd0RWpB?oc=5>

### Charles Schwab Issues $3 Billion in Senior Notes
- Summary: Schwab raises $3B via senior notes, expanding debt capacity for future growth and strategic initiatives.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxQWmtqUlNLMDNmeE9iV0szSVZ0enpwMExZbzRBLTVqLUh0YkNaVFFFcU50Y1BFaTNOWUtXd2FkN3ZWdGRFQlgySG5jckhoQ0JralNlVUt3cnlfa1RvUzdrR2c3MHZIVmZEel9XRlpMck5scHp6N213YzdGdnA1cFBNeGpYWWNoQUdoV2lfUTJVOFFEMlVtR1ZVWHpDekoyeHpK?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **SCHW** | **15.68** | **3.55** | **N/A** | **16.90** | **160,484,196,352.00 USD** | **-0.90** |
| IBKR | 31.10 | 5.96 | N/A | 13.50 | 139,357,175,808.00 USD | 22.52 |
| HOOD | 37.43 | 7.01 | N/A | 11.80 | 70,112,247,808.00 USD | -35.93 |
| LPLA | 16.74 | 3.94 | N/A | 17.80 | 22,773,395,456.00 USD | -21.17 |

Peers fetched as_of: 2026-11-13; SCHW reuses existing data (market data as_of: 2026-11-13); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-15
- Next expected earnings: 2027-01-21 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-13

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-06
- Revenue (latest available single quarter): 7,171,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 2,906,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/316709/000031670926000038/schw-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiuwFBVV95cUxOOUxpUDlrMFpvVk5xR1daQ0NpWW1ybHZISEhBdHBEQXQ2b3BRc0FMWlFsbDBTWTZVYzhUaU1sdC1WUDkxTjhkdWFfc1dZYS14ZUtMd1hCNFdFNW9FLUFCT3IxaFZLU2FjM3VSWDU3U2UtZkZNZjNpY2Zna09rYzBfT3A5cG16cjVsVDBlY05PNXhpR2dHY2tfYjJma1RzQ2ZpeS1aR2pUTlQxaEJma0pEb3BpcmU2TFUwZFJj?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxPZ2p3WG9NSmZCbDZZUzZDaFh4RE9QeEg4YVZBTUFmbHpxWUZVTWdUR24tX1NaWEVBYVVUMWJiZ1NSWVhJUVNTN2Y5ZEZvbjM5Y3hoczdZLWpmdGJ3UFE5WXZXcU8zcTMwVmM5MVl4Xy1xQmMzNXRwOXFmTm9nOTQxZ1JreEVjMFhMWWItYmdZcEV2R1FsZlI4ZnB1RDdELWd0RWpB?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxQWmtqUlNLMDNmeE9iV0szSVZ0enpwMExZbzRBLTVqLUh0YkNaVFFFcU50Y1BFaTNOWUtXd2FkN3ZWdGRFQlgySG5jckhoQ0JralNlVUt3cnlfa1RvUzdrR2c3MHZIVmZEel9XRlpMck5scHp6N213YzdGdnA1cFBNeGpYWWNoQUdoV2lfUTJVOFFEMlVtR1ZVWHpDekoyeHpK?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
