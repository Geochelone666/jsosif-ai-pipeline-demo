# MU Intelligence Report

- ticker: **MU**
- Report as_of: **2026-11-17**
- Market data as_of: **2026-11-17**
- Quant sources: https://finance.yahoo.com/quote/MU/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/MU/key-statistics/
- AI analysis snapshot as_of: **2026-11-17**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-18T05:56:42.057878+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 22, 'rule': 0, 'ai': 5, 'unknown': 0, 'irrelevant': 17})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **8** exact headline/source/date matches; prior report **20261117T062519Z-6171f6c2/MU** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'short_term_price_move_in_structural_risks': 1}
- RSS source audit (metadata only, not article fact-checking): 22 unique headlines; 10 named publishers; 3 exact duplicates; 22 HTTPS source links; largest publisher share 31.82%; oldest publication 2026-11-14

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 712.4200 |
| Return 1D (%) | -0.9179 |
| Return 1W (%) | -1.7501 |
| Return 1M (%) | -18.9363 |
| Return YTD (%) | 149.7954 |
| Return 1Y (%) | 194.7837 |
| Annualized volatility (%) | 84.5778 |
| Beta vs SPY | 3.4292 |
| Max drawdown (%) | -45.8952 |
| Sharpe (rf=0) | 1.7035 |
| Downside deviation (rf=0, %) | 53.0344 |
| Sortino (rf=0) | 2.7167 |
| Historical VaR 95% (1D, %) | 7.3172 |
| Historical ES 95% (1D, %) | 10.3774 |
| Correlation vs SPY | 0.5588 |
| Tracking error vs SPY (%) | 77.7226 |
| P/E (trailing) | 9.67 |
| P/B | 5.82 |
| EV/EBITDA | 7.05 |
| Revenue growth (%) | 379.30 |
| Forward P/E (estimate) | 3.43 |
| Gross margin (%) | 80.72 |
| Operating margin (%) | 74.59 |
| Return on equity (%) | 88.26 |
| Free cash flow yield (%) | 3.62 |
| MA50 | 931.9876 |
| Close vs MA50 (%) | -23.5591 |
| MA200 | 768.3136 |
| Close vs MA200 (%) | -7.2748 |
| RSI (14, Wilder) | 37.5394 |
| MACD (12,26) | -58.6886 |
| MACD signal (9) | -55.1792 |
| MACD histogram | -3.5093 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'MU': 284, 'SPY': 284}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 712.4200 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.9179 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -1.7501 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -18.9363 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 149.7954 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 194.7837 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 84.5778 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 53.0344 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 2.7167 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 7.3172 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 10.3774 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5588 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 77.7226 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 3.4292 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -45.8952 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.7035 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 3.4290 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 80.7160 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 74.5860 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 88.2600 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 3.6152 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 9.6730 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 37.5394 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -3.5093 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -23.5591 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -7.2748 -> Clearly below the moving-average trend level.

## TAILWINDS

### Micron Stock (MU) Forecast – Why Are Analysts Bullish Despite Ongoing Volatility?
- Summary: Analysts remain optimistic about Micron’s future, citing strong demand and potential upside despite market volatility.
- Date: 2026-11-14 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxNV1J2alhFSlhSeFc5cG9KRWZ3R0hGd013SC1hc3lFcjRNVE8tdnpyc2lnS0FSUDJ6Qzc1SWhtUk5QZ2pkX3V0U0R1U3h3WWNOMENqUjJYdlkxSmdOYlVfcEluQ3phV1NUNjVCS3pHNkN1QWx0Nnp3ZFBVbXZmcmp0dEYxT1F5YXEtMlNmZmhzVWZxSmhYa010dUx3SHFPSVZxOEFma2xDa0JxZzdNeG9KVnljSW4?oc=5>

### Micron Technology (MU): Does a Low Earnings Multiple Understate Its AI Opportunity?
- Summary: Analysis questions if low earnings multiple undervalues Micron’s AI prospects.
- Date: 2026-11-14 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQRmFxb0NFNGNaVzBRdzExcGJ6a2Jremg4N1JFQk1lRHlQME04V3NnQ2ZocVlBR2RkeVpVWmwzQ3BaVmZSZjhrTFZZTndQSTJNR2hieUtXSzdaNUdraVFlU3ZUNllBRFpNTUtTZUFJeTg3TTdIWGtib0ZKZmROZGk1NHVSeERfLXZoOHNGNmY1TTlqZGpVWjl2Sg?oc=5>

### Micron Technology (MU) Has More Than 75% Of 2027 Output Committed
- Summary: Micron secured over 75% of 2027 output, indicating strong demand.
- Date: 2026-11-14 | Impact: high | Horizon: long | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxNU1J4THBrTkV3M19WbEtScExWeGVyeUtlOGdEZHB5WE95NVo1dlBrMlp1b1JFXzBnQnd0Q3ZSaXFlNGdYWGJKYjhlaGMtS3NtOHEySFBqWVBSaVZFV0dRaG1qY19pZDgtc2N0R3pGd0R0VG1GdnlyX1RRajFrU1dpdTRNajE4amplYk5ubkF2WWV5WWc?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Micron Stock Is Down 41%, but the $35 Billion Buyback Could Change the Game. Here's How.
- Summary: Micron announces a $35 billion share buyback, potentially boosting stock value.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMixgFBVV95cUxNS1huaXhkbmEtaUlvU2dCZl9iWTA2WDVJWEZvdS0yMERkWDhrbEpqSUhCbzFEOFZWa211ZkRPYjd0TkV1YktoSzJJeGFjZ0tHNDFIYkk2dEE1UV9hQlI4c2J2THQtU19KZ1pOb2JOSHVLa2d6bl9YVHRDS3llekpiSy1HTndLYjVQdEEtYmZ3SzI0amdGSS05Z1ptN2FtUVFrekc4ZTJjRlY4dkw4QUR0Qno5eWlPbVA1WTV4WXJWTW9NTnJkdXc?oc=5>

## RISKS

### Why Micron Stock Dove Today
- Summary: Micron shares fell today, indicating short-term downside pressure.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiekFVX3lxTE5ua2lEMDdzTnFrazZhY0hiTk5IVkhPSWJrSGRXUkhlbU8wRlJDcVJ6Wlk4Ui1fUWs0SUNyd1ZMSWlqTDB2M09QaFdtd3luZ0pYR2gwcko2eGJ0dEIzcmVzRTBFb2VCNVQ3d2tjMnJsLUFVR2hqMlo3cGRn?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **MU** | **9.67** | **5.82** | **7.05** | **379.30** | **806,048,497,664.00 USD** | **194.78** |
| WDC | 9.88 | 11.34 | 16.74 | 55.50 | 106,057,007,104.00 USD | 74.74 |
| STX | 26.45 | 33.56 | 19.98 | 61.00 | 115,790,618,624.00 USD | 94.11 |
| NXPI | 19.99 | 5.27 | 13.19 | 19.30 | 63,645,900,800.00 USD | 34.89 |

Peers fetched as_of: 2026-11-17; MU reuses existing data (market data as_of: 2026-11-17); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-09-30
- Next expected earnings: 2026-12-23 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-17

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-K
- Filing date: 2026-10-09
- Revenue (latest available single quarter): 8,440,000,000.00 USD; period 2018-06-01/2018-08-30; fiscal year/reporting period 2018/FY
- Net income (latest available single quarter): 28,243,000,000.00 USD; period 2026-02-27/2026-05-28; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/723125/000072312526000023/mu-20260903.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMitAFBVV95cUxNV1J2alhFSlhSeFc5cG9KRWZ3R0hGd013SC1hc3lFcjRNVE8tdnpyc2lnS0FSUDJ6Qzc1SWhtUk5QZ2pkX3V0U0R1U3h3WWNOMENqUjJYdlkxSmdOYlVfcEluQ3phV1NUNjVCS3pHNkN1QWx0Nnp3ZFBVbXZmcmp0dEYxT1F5YXEtMlNmZmhzVWZxSmhYa010dUx3SHFPSVZxOEFma2xDa0JxZzdNeG9KVnljSW4?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQRmFxb0NFNGNaVzBRdzExcGJ6a2Jremg4N1JFQk1lRHlQME04V3NnQ2ZocVlBR2RkeVpVWmwzQ3BaVmZSZjhrTFZZTndQSTJNR2hieUtXSzdaNUdraVFlU3ZUNllBRFpNTUtTZUFJeTg3TTdIWGtib0ZKZmROZGk1NHVSeERfLXZoOHNGNmY1TTlqZGpVWjl2Sg?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxNU1J4THBrTkV3M19WbEtScExWeGVyeUtlOGdEZHB5WE95NVo1dlBrMlp1b1JFXzBnQnd0Q3ZSaXFlNGdYWGJKYjhlaGMtS3NtOHEySFBqWVBSaVZFV0dRaG1qY19pZDgtc2N0R3pGd0R0VG1GdnlyX1RRajFrU1dpdTRNajE4amplYk5ubkF2WWV5WWc?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxNS1huaXhkbmEtaUlvU2dCZl9iWTA2WDVJWEZvdS0yMERkWDhrbEpqSUhCbzFEOFZWa211ZkRPYjd0TkV1YktoSzJJeGFjZ0tHNDFIYkk2dEE1UV9hQlI4c2J2THQtU19KZ1pOb2JOSHVLa2d6bl9YVHRDS3llekpiSy1HTndLYjVQdEEtYmZ3SzI0amdGSS05Z1ptN2FtUVFrekc4ZTJjRlY4dkw4QUR0Qno5eWlPbVA1WTV4WXJWTW9NTnJkdXc?oc=5
- https://news.google.com/rss/articles/CBMiekFVX3lxTE5ua2lEMDdzTnFrazZhY0hiTk5IVkhPSWJrSGRXUkhlbU8wRlJDcVJ6Wlk4Ui1fUWs0SUNyd1ZMSWlqTDB2M09QaFdtd3luZ0pYR2gwcko2eGJ0dEIzcmVzRTBFb2VCNVQ3d2tjMnJsLUFVR2hqMlo3cGRn?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
