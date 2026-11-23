# XYL Intelligence Report

- ticker: **XYL**
- Report as_of: **2026-11-22**
- Market data as_of: **2026-11-20**
- Quant sources: https://finance.yahoo.com/quote/XYL/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/XYL/key-statistics/
- AI analysis snapshot as_of: **2026-11-22**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-23T05:51:37.615316+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 9, 'rule': 2, 'ai': 1, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **3** exact headline/source/date matches; prior report **20261122T045655Z-f5ef568d/XYL** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 9 unique headlines; 5 named publishers; 0 exact duplicates; 9 HTTPS source links; largest publisher share 33.33%; oldest publication 2026-11-17

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 94.6600 |
| Return 1D (%) | -0.6090 |
| Return 1W (%) | 0.5097 |
| Return 1M (%) | -9.8648 |
| Return YTD (%) | -29.7134 |
| Return 1Y (%) | -30.4644 |
| Annualized volatility (%) | 30.6657 |
| Beta vs SPY | 0.5369 |
| Max drawdown (%) | -38.9486 |
| Sharpe (rf=0) | -1.0317 |
| Downside deviation (rf=0, %) | 25.1133 |
| Sortino (rf=0) | -1.2598 |
| Historical VaR 95% (1D, %) | 2.9628 |
| Historical ES 95% (1D, %) | 5.0929 |
| Correlation vs SPY | 0.2503 |
| Tracking error vs SPY (%) | 30.4186 |
| P/E (trailing) | 20.99 |
| P/B | 2.12 |
| EV/EBITDA | 12.35 |
| Revenue growth (%) | -3.00 |
| Forward P/E (estimate) | 16.30 |
| Gross margin (%) | 39.32 |
| Operating margin (%) | 15.51 |
| Return on equity (%) | 9.76 |
| Free cash flow yield (%) | 5.58 |
| MA50 | 101.0794 |
| Close vs MA50 (%) | -6.3508 |
| MA200 | 113.4828 |
| Close vs MA200 (%) | -16.5865 |
| RSI (14, Wilder) | 42.2823 |
| MACD (12,26) | -1.9718 |
| MACD signal (9) | -2.0625 |
| MACD histogram | 0.0908 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'XYL': 287, 'SPY': 287}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 94.6600 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.6090 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 0.5097 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -9.8648 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -29.7134 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -30.4644 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 30.6657 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 25.1133 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -1.2598 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.9628 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.0929 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2503 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 30.4186 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.5369 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -38.9486 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -1.0317 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 16.3024 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 39.3200 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 15.5090 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 9.7560 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 5.5755 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 20.9889 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 42.2823 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.0908 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -6.3508 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -16.5865 -> Clearly below the moving-average trend level.

## TAILWINDS

### Xylem (XYL) Stock May Be 37% Undervalued On Fresh Buyback News
- Summary: Xylem’s recent buyback may have left its stock undervalued, suggesting potential upside for investors.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxOd3dEWVotdVI5NHpMeWh3bjJMdUg3Qi1nYlRCSWR6cFlORlg2NUtMUlVRa1A4WE5PM0o4M3lRb3JtTXZnYUFqMXkwa2Z3YS1VdXNBTFV6b0N5Q3BISTJtTHQ3V3NjMjhMaHkyajBvdk4xWHBKSkNIN3lDOThzUFBCSi12bXNwdHJGWER3LXVLRlY?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Xylem (XYL) Buyback Puts Value In Focus As Investors Ask If Shares Are A Bargain
- Summary: Xylem (XYL) Buyback Puts Value In Focus As Investors Ask If Shares Are A Bargain
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxPWnVmcjdxS2pUSGhGT2hNclVvVmVQdjlIaHV2S0F0ZjQ1eU5jaDJ4RS1mSTktZ1oxNEtxUnZPMnNrcXI0ank2VTFHcElpeUF2TDVWS3ZWX3pJa1JkVV93NGlXYXltYzh5eU5PRzdXd0owcUIzMXNxTnFRMkd0eDB6SUFnTVlKN1JZWDhyRmJVLUVJQUlfdGk1dmdVeFhOcTJNRE1ycFdUZHlHVkVucDRYNFRjZjQwcjBPMllLMElGa1B4U1Ay0gHKAUFVX3lxTE93bndUUVhxS3lDNl8tQlk2QU02RjRYdDRXRWREdnBCekZzTzg2VHFKZ3ZoZ0RJSlk3QlktVWFMaU1pQXB2V1RwV3dWLTdIeXF1OTkwbjlwOFlpSHpKNENaNVdhdS1Kd2VEUUlmZF92aDJRLXlocTczRTJWVmllMUNyRWF2Q29udDZ5VjRrV3RCaWRTNFdxYkUxWUdWeEl6VjZEYzVoRUZ2OWRYZldJTWlkQ2tQN1c0R294clBqb1dFS041VkJ1RVZ0RGc?oc=5>

### Xylem Inc. (NYSE:XYL) Declares Quarterly Dividend of $0.43
- Summary: Xylem Inc. (NYSE:XYL) Declares Quarterly Dividend of $0.43
- Date: 2026-11-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxPM3JxcUdhVGsxRjRiMC1IU0RiSjNlVFdrUzcyWE9COVZfS1ROSkk0aDctdzJ0TDNWWEVrVlRnRlBvSkdJMlFBSzdVMGFMVzAtNmd3MEVSam1leGFtSXZTZkNOdXdyajE0dEtMc1pTcUZNY3lmTEdOOHpEaVp0NVNuYWhXcF8xaXdpNWFXUUMwUDY2X1h6cWo0bmFDT2liU1ZhZ0NObnpyaXpwOEZSc0MzbEN6U1JISnM?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **XYL** | **20.99** | **2.12** | **12.35** | **-3.00** | **21,708,814,336.00 USD** | **-30.46** |
| AOS | 17.66 | 4.66 | 11.42 | -0.20 | 8,494,963,712.00 USD | 2.27 |
| PH | 29.95 | 6.88 | 21.26 | 17.90 | 109,938,745,344.00 USD | 7.28 |
| DOV | 22.67 | 3.38 | 13.99 | 7.50 | 25,842,063,360.00 USD | 10.25 |

Peers fetched as_of: 2026-11-22; XYL reuses existing data (market data as_of: 2026-11-20); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-27
- Next expected earnings: 2027-02-09 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-22

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-27
- Revenue (latest available single quarter): 2,201,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 291,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1524472/000152447226000148/xyl-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMikAFBVV95cUxOd3dEWVotdVI5NHpMeWh3bjJMdUg3Qi1nYlRCSWR6cFlORlg2NUtMUlVRa1A4WE5PM0o4M3lRb3JtTXZnYUFqMXkwa2Z3YS1VdXNBTFV6b0N5Q3BISTJtTHQ3V3NjMjhMaHkyajBvdk4xWHBKSkNIN3lDOThzUFBCSi12bXNwdHJGWER3LXVLRlY?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxPWnVmcjdxS2pUSGhGT2hNclVvVmVQdjlIaHV2S0F0ZjQ1eU5jaDJ4RS1mSTktZ1oxNEtxUnZPMnNrcXI0ank2VTFHcElpeUF2TDVWS3ZWX3pJa1JkVV93NGlXYXltYzh5eU5PRzdXd0owcUIzMXNxTnFRMkd0eDB6SUFnTVlKN1JZWDhyRmJVLUVJQUlfdGk1dmdVeFhOcTJNRE1ycFdUZHlHVkVucDRYNFRjZjQwcjBPMllLMElGa1B4U1Ay0gHKAUFVX3lxTE93bndUUVhxS3lDNl8tQlk2QU02RjRYdDRXRWREdnBCekZzTzg2VHFKZ3ZoZ0RJSlk3QlktVWFMaU1pQXB2V1RwV3dWLTdIeXF1OTkwbjlwOFlpSHpKNENaNVdhdS1Kd2VEUUlmZF92aDJRLXlocTczRTJWVmllMUNyRWF2Q29udDZ5VjRrV3RCaWRTNFdxYkUxWUdWeEl6VjZEYzVoRUZ2OWRYZldJTWlkQ2tQN1c0R294clBqb1dFS041VkJ1RVZ0RGc?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxPM3JxcUdhVGsxRjRiMC1IU0RiSjNlVFdrUzcyWE9COVZfS1ROSkk0aDctdzJ0TDNWWEVrVlRnRlBvSkdJMlFBSzdVMGFMVzAtNmd3MEVSam1leGFtSXZTZkNOdXdyajE0dEtMc1pTcUZNY3lmTEdOOHpEaVp0NVNuYWhXcF8xaXdpNWFXUUMwUDY2X1h6cWo0bmFDT2liU1ZhZ0NObnpyaXpwOEZSc0MzbEN6U1JISnM?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
