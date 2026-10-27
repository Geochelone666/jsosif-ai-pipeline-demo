# ACN Intelligence Report

- ticker: **ACN**
- Report as_of: **2026-10-26**
- Market data as_of: **2026-10-26**
- Quant sources: https://finance.yahoo.com/quote/ACN/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/ACN/key-statistics/
- AI analysis snapshot as_of: **2026-10-26**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-27T02:13:37.782411+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 7, 'rule': 1, 'ai': 4, 'unknown': 0, 'irrelevant': 2})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **5** exact headline/source/date matches; prior report **20261026T005504Z-6368ad31/ACN** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 7 unique headlines; 5 named publishers; 0 exact duplicates; 7 HTTPS source links; largest publisher share 28.57%; oldest publication 2026-10-19

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 247.2300 |
| Return 1D (%) | -0.8582 |
| Return 1W (%) | 4.3473 |
| Return 1M (%) | 41.5100 |
| Return YTD (%) | -5.1999 |
| Return 1Y (%) | 2.7049 |
| Annualized volatility (%) | 49.4427 |
| Beta vs SPY | 0.0677 |
| Max drawdown (%) | -56.5068 |
| Sharpe (rf=0) | 0.2770 |
| Downside deviation (rf=0, %) | 34.4307 |
| Sortino (rf=0) | 0.3978 |
| Historical VaR 95% (1D, %) | 4.4087 |
| Historical ES 95% (1D, %) | 6.7690 |
| Correlation vs SPY | 0.0174 |
| Tracking error vs SPY (%) | 50.8367 |
| P/E (trailing) | 18.23 |
| P/B | 4.66 |
| EV/EBITDA | 11.05 |
| Revenue growth (%) | 6.20 |
| Forward P/E (estimate) | 15.56 |
| Gross margin (%) | 32.05 |
| Operating margin (%) | 17.83 |
| Return on equity (%) | 26.02 |
| Free cash flow yield (%) | 7.06 |
| MA50 | 196.0322 |
| Close vs MA50 (%) | 26.1170 |
| MA200 | 188.6582 |
| Close vs MA200 (%) | 31.0465 |
| RSI (14, Wilder) | 71.2741 |
| MACD (12,26) | 16.8565 |
| MACD signal (9) | 13.4096 |
| MACD histogram | 3.4469 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'ACN': 268, 'SPY': 268}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 247.2300 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.8582 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 4.3473 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 41.5100 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -5.1999 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 2.7049 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 49.4427 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 34.4307 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.3978 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.4087 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 6.7690 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.0174 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 50.8367 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.0677 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -56.5068 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.2770 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 15.5617 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 32.0500 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 17.8280 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 26.0250 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 7.0622 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 18.2323 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 71.2741 -> Overbought momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 3.4469 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 26.1170 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 31.0465 -> Clearly above the moving-average trend level.

## TAILWINDS

### Accenture Stock Rides A 10-Day Winning Streak To A 25% Gain
- Summary: Accenture Stock Rides A 10-Day Winning Streak To A 25% Gain
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxOT1QtRndiY2RLdnF5cDR6VG5nVU0wVy0tSGc2WjRrNWs5MWhuaUJVNlFJNWNwOUJCRXVjWEhKdElzQmN3UnZIT2JqNnQtS1lTdGpzbVB0aUpsZ29LMm94eURBb2VUdmRiVEdURUlwR3pxaW5xRkJvUXVUQUc2VGQ5U0xGTTMtMlBIWWxsYzJxOHNUWl9nVDh5Ty1MZjRCQnJTRWFocXc0WmgxdVE5Q3pRY1lGcFpxMTlESHc?oc=5>

### Accenture: 75% Total Return Since July, 23% More By December 2027 (NYSE:ACN)
- Summary: Accenture’s total return has risen 75% since July, with projections of an additional 23% by Dec 2027.
- Date: 2026-10-23 | Impact: medium | Horizon: long | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxPWkV3TXZFbXhsN3dBUnRYdmI2UWZmUkJNUm9sMmc2TEZzMXhMaEJfaFBqVjdSOWhBNUl6UVZXODMtb2JUblhyT19oY0RlV2ZRYm1JRUp3c1FoRThIR2pKcEpuREZtcWZGbjBrbG9oQXZ5bFNZN3Rodl9WUUlNMVlMSHBidVl6ZFM1ZENwU0NqYmJ5MVI2QjUxSk04a2txeDVCVEIyQmJrRk5Gam9UczMwTzNsQXdlMGI4cFE?oc=5>

## HEADWINDS

### Accenture PLC Stock (ACN) Opened Down by 4.04% on Oct 23: What Signal Does It Send?
- Summary: Opening decline of 4.04% signals short‑term market weakness for Accenture.
- Date: 2026-10-23 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxPS2VsM01FdzJrTVZmc2RZNDVMVG9xa0pKa2dqNXN0Vm05YVRlN0cxTEE5WmR3a1JJZU9odjljTV9FX2FtaF9CMm5RemZNSnBCbUtYemhZQ0R1XzkxZG90RFZjdl82SXU4aEpnOG1lcEJRNG9FN0pENy1zTHVGMDkyclV4a1FHTVlFTEE?oc=5>

## CATALYSTS

### ISRG, NFLX, ACN Stocks Slide Before The Bell: Why Intuitive Surgical, Netflix And Accenture Are Heading Lower
- Summary: Accenture shares fell before the market opened, reflecting broader market weakness.
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxPUkZ5UXVsZjJXaGVOT3Z1RkR2TmdDb2xMQ0JNNWJpY2dTX3ZtNFNRVUVVckVReTR2ZGhlUUFtSXl5UElKZE55dnFYdHplX3NkQXVOU1lQcVkySzYyWGo5UFFaaGJadGpjRGRENHVnd0MwVW9KN0dzcm9qdWloZmpVeXAtUXY5ZnJHUE1nX0pyTlptMDZvRFE?oc=5>

## RISKS

### Accenture considers selling China business for up to $1.5B - report (ACN:NYSE)
- Summary: Potential divestiture of China unit could reshape business focus.
- Date: 2026-10-19 | Impact: medium | Horizon: medium | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxQcDkzMVJfTzFodkpVNThKVHBiTm9zakxQZnByVXd4VWczR2I0YVdHSUhvSnpYSWxmNHR1NGFJdlhHS0ItWkpXYjdmTU40NUlSekVZZnJfSXFyWmNoRWdFU3Jja0JLdDV5aWw0MHQyMUtOZzZ6Q3dBX3dPUk5uTTdZektBbENoSzNScHhQcTFfZTdlTjAxQ1l3ZVMySWxNenl0am91UHZB?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **ACN** | **18.23** | **4.66** | **11.05** | **6.20** | **151,290,445,824.00 USD** | **2.70** |
| IBM | 21.62 | 6.74 | 17.81 | 4.70 | 239,531,425,792.00 USD | -15.43 |
| CTSH | 14.91 | 2.17 | 8.00 | 4.50 | 31,233,800,192.00 USD | 4.49 |
| INFY | 15.35 | 9.75 | 21.64 | 1.40 | 50,346,180,608.00 USD | -26.26 |

Peers fetched as_of: 2026-10-26; ACN reuses existing data (market data as_of: 2026-10-26); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-01
- Next expected earnings: 2026-12-17 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-26

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-K
- Filing date: 2026-10-16
- Revenue (latest available single quarter): 18,679,110,000.00 USD; period 2026-06-01/2026-08-31; fiscal year/reporting period 2026/FY
- Net income (latest available single quarter): 1,991,267,000.00 USD; period 2026-06-01/2026-08-31; fiscal year/reporting period 2026/FY
- SEC link: https://www.sec.gov/Archives/edgar/data/1467373/000146737326000049/acn-20260831.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiugFBVV95cUxOT1QtRndiY2RLdnF5cDR6VG5nVU0wVy0tSGc2WjRrNWs5MWhuaUJVNlFJNWNwOUJCRXVjWEhKdElzQmN3UnZIT2JqNnQtS1lTdGpzbVB0aUpsZ29LMm94eURBb2VUdmRiVEdURUlwR3pxaW5xRkJvUXVUQUc2VGQ5U0xGTTMtMlBIWWxsYzJxOHNUWl9nVDh5Ty1MZjRCQnJTRWFocXc0WmgxdVE5Q3pRY1lGcFpxMTlESHc?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxPWkV3TXZFbXhsN3dBUnRYdmI2UWZmUkJNUm9sMmc2TEZzMXhMaEJfaFBqVjdSOWhBNUl6UVZXODMtb2JUblhyT19oY0RlV2ZRYm1JRUp3c1FoRThIR2pKcEpuREZtcWZGbjBrbG9oQXZ5bFNZN3Rodl9WUUlNMVlMSHBidVl6ZFM1ZENwU0NqYmJ5MVI2QjUxSk04a2txeDVCVEIyQmJrRk5Gam9UczMwTzNsQXdlMGI4cFE?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxPS2VsM01FdzJrTVZmc2RZNDVMVG9xa0pKa2dqNXN0Vm05YVRlN0cxTEE5WmR3a1JJZU9odjljTV9FX2FtaF9CMm5RemZNSnBCbUtYemhZQ0R1XzkxZG90RFZjdl82SXU4aEpnOG1lcEJRNG9FN0pENy1zTHVGMDkyclV4a1FHTVlFTEE?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxPUkZ5UXVsZjJXaGVOT3Z1RkR2TmdDb2xMQ0JNNWJpY2dTX3ZtNFNRVUVVckVReTR2ZGhlUUFtSXl5UElKZE55dnFYdHplX3NkQXVOU1lQcVkySzYyWGo5UFFaaGJadGpjRGRENHVnd0MwVW9KN0dzcm9qdWloZmpVeXAtUXY5ZnJHUE1nX0pyTlptMDZvRFE?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxQcDkzMVJfTzFodkpVNThKVHBiTm9zakxQZnByVXd4VWczR2I0YVdHSUhvSnpYSWxmNHR1NGFJdlhHS0ItWkpXYjdmTU40NUlSekVZZnJfSXFyWmNoRWdFU3Jja0JLdDV5aWw0MHQyMUtOZzZ6Q3dBX3dPUk5uTTdZektBbENoSzNScHhQcTFfZTdlTjAxQ1l3ZVMySWxNenl0am91UHZB?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
