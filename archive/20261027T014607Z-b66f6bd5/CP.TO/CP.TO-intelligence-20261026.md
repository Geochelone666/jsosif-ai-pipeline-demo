# CP.TO Intelligence Report

- ticker: **CP.TO**
- Report as_of: **2026-10-26**
- Market data as_of: **2026-10-26**
- Quant sources: https://finance.yahoo.com/quote/CP.TO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/CP.TO/key-statistics/
- AI analysis snapshot as_of: **2026-10-26**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-27T02:00:50.078959+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 6, 'rule': 0, 'ai': 3, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **N/A (no successful AI classification call)**
- Verified recent classification reuse: **6** exact headline/source/date matches; prior report **20261026T005504Z-6368ad31/CP.TO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 6 unique headlines; 4 named publishers; 0 exact duplicates; 6 HTTPS source links; largest publisher share 33.33%; oldest publication 2026-10-20

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 125.9100 |
| Return 1D (%) | 0.3107 |
| Return 1W (%) | 3.0023 |
| Return 1M (%) | 2.4491 |
| Return YTD (%) | 25.4050 |
| Return 1Y (%) | 20.2256 |
| Annualized volatility (%) | 21.8272 |
| Beta vs SPY | 0.3916 |
| Max drawdown (%) | -11.9692 |
| Sharpe (rf=0) | 1.0239 |
| Downside deviation (rf=0, %) | 14.5658 |
| Sortino (rf=0) | 1.5343 |
| Historical VaR 95% (1D, %) | 1.8654 |
| Historical ES 95% (1D, %) | 2.9512 |
| Correlation vs SPY | 0.2272 |
| Tracking error vs SPY (%) | 22.7925 |
| P/E (trailing) | 29.28 |
| P/B | 2.38 |
| EV/EBITDA | 16.54 |
| Revenue growth (%) | 12.60 |
| Forward P/E (estimate) | 21.11 |
| Gross margin (%) | 53.40 |
| Operating margin (%) | 38.98 |
| Return on equity (%) | 8.15 |
| Free cash flow yield (%) | 1.97 |
| MA50 | 124.8479 |
| Close vs MA50 (%) | 0.8507 |
| MA200 | 118.4214 |
| Close vs MA200 (%) | 6.3237 |
| RSI (14, Wilder) | 58.2260 |
| MACD (12,26) | 0.3498 |
| MACD signal (9) | -0.3196 |
| MACD histogram | 0.6694 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'CP.TO': 267, 'SPY': 268}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 125.9100 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.3107 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 3.0023 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 2.4491 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 25.4050 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 20.2256 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 21.8272 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 14.5658 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.5343 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.8654 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.9512 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2272 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 22.7925 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.3916 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -11.9692 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.0239 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 21.1092 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 53.3950 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 38.9770 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 8.1540 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.9708 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 29.2814 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 58.2260 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.6694 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 0.8507 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 6.3237 -> Clearly above the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

No items in this run

## CATALYSTS

### Canadian Pacific Kansas City (TSX:CP) Stock May Be Fully Priced On Cash Flow
- Summary: Analysts suggest CP’s stock may already reflect its cash flow, indicating potential valuation stability.
- Date: 2026-10-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxPelFjTU5SLUoxYzB4VllGcVRseXZZTTRsZVg1bEZaU0ZNV0JjMzZOdl8tTTJ0RjRlbG1LdFdxbVFFMDNzMHdXZldRMlVXVFQ5TUhKTVphTGYzTGE1UVJXUTZ4M2VwZUIwaU1MOHZzMGVtUl9ObnhabGNHcFNwMGtvUTg1QkdPdm0zNVNIcl9tekw2RHZUd2liNERSNXJLUQ?oc=5>

### Canadian Pacific Kansas City (CP) Stock Forecast and Price Target 2026 $CP
- Summary: Forecast and price target for CP for 2026.
- Date: 2026-10-23 | Impact: medium | Horizon: long | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiYEFVX3lxTE0xbk84NjVMX1ZDWENSeDZoYzVYb0xkRHh1bHppV2l6STBLMFNkeTlHR1gwdUY3NUIwcFFsVUxhZUtZbnZkLWRiWnBSb0RkNjNycTRMTGprN0NfdnRGOW1jSA?oc=5>

### Canadian Pacific Kansas City stock: Raymond James keeps CAD 144.00 target for CP stock
- Summary: Raymond James maintains a CAD 144.00 target price for CP stock, indicating stable analyst outlook.
- Date: 2026-10-20 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi4gFBVV95cUxQblNvRWxYMm85SXdzRTFYTnpmNU1Odzlyc2VFS0NWYUNMeTdkMjh4SWNaZUFMajZtODVRSVQ4YWdOTUtRWjY2VVIta21WWlhTNFk5QjdMdDJHSFpxa2E5b3Z2V2hGdUtkZk1KZEdMRUlBMHZUeWUyRVlRUnVKZ0otUFVxa2VPSjh5VDhoTDJTd0YyOVpwNFFsS0VoWE9CNGx4b1RRUlBWcFVsR19yajRPTHgtTGFHVEtJV2hfUDVmWEM3S2dQMG1kcVoxYjc1Y1g3RVVZeGM0b25kZzg3cGpqcnFR?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **CP.TO** | **29.28** | **2.38** | **16.54** | **12.60** | **110,684,872,704.00 CAD** | **20.23** |
| CNR.TO | 22.21 | 4.78 | 13.88 | 11.30 | 104,509,292,544.00 CAD | 32.75 |
| UNP | 23.16 | 8.01 | 15.40 | 15.30 | 176,422,600,704.00 USD | 39.99 |
| NSC | 28.00 | 4.48 | 15.64 | 13.60 | 75,019,722,752.00 USD | 21.17 |

Peers fetched as_of: 2026-10-26; CP.TO reuses existing data (market data as_of: 2026-10-26); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-07-29
- Next expected earnings: 2026-10-28 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-26

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-07-30
- Revenue (latest available single quarter): N/A
- Net income (latest available single quarter): N/A
- SEC link: https://www.sec.gov/Archives/edgar/data/16875/000001687526000026/cp-20260630.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMingFBVV95cUxPelFjTU5SLUoxYzB4VllGcVRseXZZTTRsZVg1bEZaU0ZNV0JjMzZOdl8tTTJ0RjRlbG1LdFdxbVFFMDNzMHdXZldRMlVXVFQ5TUhKTVphTGYzTGE1UVJXUTZ4M2VwZUIwaU1MOHZzMGVtUl9ObnhabGNHcFNwMGtvUTg1QkdPdm0zNVNIcl9tekw2RHZUd2liNERSNXJLUQ?oc=5
- https://news.google.com/rss/articles/CBMiYEFVX3lxTE0xbk84NjVMX1ZDWENSeDZoYzVYb0xkRHh1bHppV2l6STBLMFNkeTlHR1gwdUY3NUIwcFFsVUxhZUtZbnZkLWRiWnBSb0RkNjNycTRMTGprN0NfdnRGOW1jSA?oc=5
- https://news.google.com/rss/articles/CBMi4gFBVV95cUxQblNvRWxYMm85SXdzRTFYTnpmNU1Odzlyc2VFS0NWYUNMeTdkMjh4SWNaZUFMajZtODVRSVQ4YWdOTUtRWjY2VVIta21WWlhTNFk5QjdMdDJHSFpxa2E5b3Z2V2hGdUtkZk1KZEdMRUlBMHZUeWUyRVlRUnVKZ0otUFVxa2VPSjh5VDhoTDJTd0YyOVpwNFFsS0VoWE9CNGx4b1RRUlBWcFVsR19yajRPTHgtTGFHVEtJV2hfUDVmWEM3S2dQMG1kcVoxYjc1Y1g3RVVZeGM0b25kZzg3cGpqcnFR?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
