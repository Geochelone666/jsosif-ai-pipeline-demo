# CP.TO Intelligence Report

- ticker: **CP.TO**
- Report as_of: **2026-10-24**
- Market data as_of: **2026-10-23**
- Quant sources: https://finance.yahoo.com/quote/CP.TO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/CP.TO/key-statistics/
- AI analysis snapshot as_of: **2026-10-24**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-25T01:00:35.513152+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 7, 'rule': 2, 'ai': 2, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- RSS source audit (metadata only, not article fact-checking): 7 unique headlines; 5 named publishers; 0 exact duplicates; 7 HTTPS source links; largest publisher share 28.57%; oldest publication 2026-10-17

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 125.5200 |
| Return 1D (%) | -1.1109 |
| Return 1W (%) | 1.6521 |
| Return 1M (%) | 1.0385 |
| Return YTD (%) | 25.0166 |
| Return 1Y (%) | 19.1763 |
| Annualized volatility (%) | 21.8417 |
| Beta vs SPY | 0.3736 |
| Max drawdown (%) | -11.9692 |
| Sharpe (rf=0) | 0.9153 |
| Downside deviation (rf=0, %) | 14.6136 |
| Sortino (rf=0) | 1.3681 |
| Historical VaR 95% (1D, %) | 1.8654 |
| Historical ES 95% (1D, %) | 2.9512 |
| Correlation vs SPY | 0.2172 |
| Tracking error vs SPY (%) | 22.9382 |
| P/E (trailing) | 29.19 |
| P/B | 2.37 |
| EV/EBITDA | 16.50 |
| Revenue growth (%) | 12.60 |
| Forward P/E (estimate) | 21.04 |
| Gross margin (%) | 53.40 |
| Operating margin (%) | 38.98 |
| Return on equity (%) | 8.15 |
| Free cash flow yield (%) | 1.98 |
| MA50 | 124.9398 |
| Close vs MA50 (%) | 0.4644 |
| MA200 | 118.2889 |
| Close vs MA200 (%) | 6.1130 |
| RSI (14, Wilder) | 57.1351 |
| MACD (12,26) | 0.1733 |
| MACD signal (9) | -0.4870 |
| MACD histogram | 0.6603 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'CP.TO': 266, 'SPY': 267}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 125.5200 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.1109 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 1.6521 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 1.0385 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 25.0166 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 19.1763 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 21.8417 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 14.6136 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.3681 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.8654 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.9512 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2172 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 22.9382 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.3736 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -11.9692 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.9153 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 21.0438 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 53.3950 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 38.9770 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 8.1540 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.9769 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 29.1907 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 57.1351 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.6603 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 0.4644 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 6.1130 -> Clearly above the moving-average trend level.

## TAILWINDS

### Unveiling Canadian Pacific Kansas City (CP) Q3 Outlook: Wall Street Estimates for Key Metrics
- Summary: CP releases Q3 outlook with key metrics, indicating potential growth and positive market expectations.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxQYndBTGxYVEVDN2o2TlJZLWZRZUswT0tLb0lXWC1qZ2ZYY3BmSlBCLUMyWkJ2elltaDhkbGV0V1k0cENWWWlOeWlnb3hoeDRuOEt2NXJnaWRWVHR1emZFbmFoM28xVGpobmlpbnJuaGpLSnlKRmF3SzhJZUkzeW42b3JPdkpmOTh5Qm4zZEpQOEt3UGRJYWJ4ekd4Z0ZnQnhKZVdaTHZB?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Canadian Pacific Kansas City (CP) Reports Next Week: Wall Street Expects Earnings Growth
- Summary: Canadian Pacific Kansas City (CP) Reports Next Week: Wall Street Expects Earnings Growth
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihwFBVV95cUxPQ0Z6RXdfODZyRTg5UFlJNVY5UzNLTDZqUXFtaFdEamhuYnVWZ3dlZ1lEaGJfY0dsdnZzSXV6eEFXeHZUVWxKU2VDeUhlbkpoekJvTTB3UjRYTGZIMU5NeGZrSFpNWDJDOXJ2YjdDRXhQQWhWOGJITTBOcmxTazZUX2hFaHdPZDg?oc=5>

### Canadian Pacific Kansas City (TSX:CP) Stock Looks Near Fair Value On Cash Flow
- Summary: Canadian Pacific Kansas City (TSX:CP) Stock Looks Near Fair Value On Cash Flow
- Date: 2026-10-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi6wFBVV95cUxOOXZFTkZZRE5Ca1RZOHZiUERWNnI1a3lNWmZoSFdpMkpGR3VoWXJJMDY0TmcySTFZR25XbnFKN1E1Ym9xdlBKTEliblZrcWdMb25DQ25Fc3VzOEh0VG1UN29SeWdFQmRQWVhYcG80bVZQd29LVGVybzlCNFpxYWliU3A2dElZUkFBTkF2VDYyUDRockJ5bmRuUzRTQUR4T21WMkxoY09jb2JhWTE2ZVExY1hFXy1ma0hwNjc5aTA5LXVnVnVKc3hIT3hvc3Y3STVzbnBxdEZKZ1l4Q3VBMnRrcDJtSEhmamhNc29J0gHwAUFVX3lxTE9NLXY2OEp0YmhZYmI1YllqU193NExRNGlfQk9ESFFlYVFWWVVoaHBOR05CWmMxb3ZXN2hnbm0tc1NqSm8zaUU3aEFIX1V6ZS1YMk9USlFPM2xob01HRlRnYUFPMnVBR0swNWhxMjFyRjktaVFGNHB5NW1tSno4ZGdIc2ZSM21PcUdwSXpPcXFraTJwUHN3TXFmTWM0Y1JYcE1Hd3BSeGNhQUZTcU5QeWJnalVVZFE1bkVnYmo5RkVENy1PT2FxS1JvRENRWHp0akhSX2NCajJKUGhXaURfODdHYUJ3WkhyNXZhQ1JvemkySQ?oc=5>

### Canadian Pacific Kansas City (TSX:CP) Could Be 12% Undervalued As Holiday Train Returns
- Summary: Analysis suggests CP may be undervalued by 12% as holiday train traffic resumes, indicating potential upside.
- Date: 2026-10-18 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxNV3dVTzdhbmExM2U1ckFwdE1FZl93MzRHdlRhU09XZ0g1UjBWSWdzV2QtRFJHMnIxYk5nbWx4VnhPcE84bzdsYzFnMjB0Q2o0Ykx5N0dGcWdiNTJFRHBUaG1DdHZrYWlWTGg2U3p4engza0g1VGV3ZU1xNnJnNzhtQU10bkR5VTNtQnNoX1laLUZsdFBPZjZ2b2JjN01GUQ?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **CP.TO** | **29.19** | **2.37** | **16.50** | **12.60** | **110,342,021,120.00 CAD** | **19.18** |
| CNR.TO | 22.14 | 4.76 | 13.85 | 11.30 | 104,207,245,312.00 CAD | 31.56 |
| UNP | 22.84 | 7.90 | 15.26 | 15.30 | 173,986,889,728.00 USD | 35.90 |
| NSC | 27.66 | 4.43 | 15.44 | 13.60 | 74,121,256,960.00 USD | 18.31 |

Peers fetched as_of: 2026-10-24; CP.TO reuses existing data (market data as_of: 2026-10-23); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-07-29
- Next expected earnings: 2026-10-28 (yfinance; expected dates may change)

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
- Filing date: 2026-07-30
- Revenue (latest available single quarter): N/A
- Net income (latest available single quarter): N/A
- SEC link: https://www.sec.gov/Archives/edgar/data/16875/000001687526000026/cp-20260630.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMipgFBVV95cUxQYndBTGxYVEVDN2o2TlJZLWZRZUswT0tLb0lXWC1qZ2ZYY3BmSlBCLUMyWkJ2elltaDhkbGV0V1k0cENWWWlOeWlnb3hoeDRuOEt2NXJnaWRWVHR1emZFbmFoM28xVGpobmlpbnJuaGpLSnlKRmF3SzhJZUkzeW42b3JPdkpmOTh5Qm4zZEpQOEt3UGRJYWJ4ekd4Z0ZnQnhKZVdaTHZB?oc=5
- https://news.google.com/rss/articles/CBMihwFBVV95cUxPQ0Z6RXdfODZyRTg5UFlJNVY5UzNLTDZqUXFtaFdEamhuYnVWZ3dlZ1lEaGJfY0dsdnZzSXV6eEFXeHZUVWxKU2VDeUhlbkpoekJvTTB3UjRYTGZIMU5NeGZrSFpNWDJDOXJ2YjdDRXhQQWhWOGJITTBOcmxTazZUX2hFaHdPZDg?oc=5
- https://news.google.com/rss/articles/CBMi6wFBVV95cUxOOXZFTkZZRE5Ca1RZOHZiUERWNnI1a3lNWmZoSFdpMkpGR3VoWXJJMDY0TmcySTFZR25XbnFKN1E1Ym9xdlBKTEliblZrcWdMb25DQ25Fc3VzOEh0VG1UN29SeWdFQmRQWVhYcG80bVZQd29LVGVybzlCNFpxYWliU3A2dElZUkFBTkF2VDYyUDRockJ5bmRuUzRTQUR4T21WMkxoY09jb2JhWTE2ZVExY1hFXy1ma0hwNjc5aTA5LXVnVnVKc3hIT3hvc3Y3STVzbnBxdEZKZ1l4Q3VBMnRrcDJtSEhmamhNc29J0gHwAUFVX3lxTE9NLXY2OEp0YmhZYmI1YllqU193NExRNGlfQk9ESFFlYVFWWVVoaHBOR05CWmMxb3ZXN2hnbm0tc1NqSm8zaUU3aEFIX1V6ZS1YMk9USlFPM2xob01HRlRnYUFPMnVBR0swNWhxMjFyRjktaVFGNHB5NW1tSno4ZGdIc2ZSM21PcUdwSXpPcXFraTJwUHN3TXFmTWM0Y1JYcE1Hd3BSeGNhQUZTcU5QeWJnalVVZFE1bkVnYmo5RkVENy1PT2FxS1JvRENRWHp0akhSX2NCajJKUGhXaURfODdHYUJ3WkhyNXZhQ1JvemkySQ?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxNV3dVTzdhbmExM2U1ckFwdE1FZl93MzRHdlRhU09XZ0g1UjBWSWdzV2QtRFJHMnIxYk5nbWx4VnhPcE84bzdsYzFnMjB0Q2o0Ykx5N0dGcWdiNTJFRHBUaG1DdHZrYWlWTGg2U3p4engza0g1VGV3ZU1xNnJnNzhtQU10bkR5VTNtQnNoX1laLUZsdFBPZjZ2b2JjN01GUQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
