# VRTX Intelligence Report

- ticker: **VRTX**
- Report as_of: **2026-11-19**
- Market data as_of: **2026-11-19**
- Quant sources: https://finance.yahoo.com/quote/VRTX/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/VRTX/key-statistics/
- AI analysis snapshot as_of: **2026-11-19**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-20T05:58:30.526719+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 8, 'rule': 0, 'ai': 5, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **5** exact headline/source/date matches; prior report **20261119T054856Z-9eb86811/VRTX** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 8 unique headlines; 5 named publishers; 0 exact duplicates; 8 HTTPS source links; largest publisher share 50.0%; oldest publication 2026-11-16

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 520.6600 |
| Return 1D (%) | -2.9434 |
| Return 1W (%) | -4.0470 |
| Return 1M (%) | 3.7275 |
| Return YTD (%) | 14.8447 |
| Return 1Y (%) | 23.6634 |
| Annualized volatility (%) | 29.5834 |
| Beta vs SPY | 0.4578 |
| Max drawdown (%) | -15.2113 |
| Sharpe (rf=0) | 0.8670 |
| Downside deviation (rf=0, %) | 18.2051 |
| Sortino (rf=0) | 1.4089 |
| Historical VaR 95% (1D, %) | 2.8866 |
| Historical ES 95% (1D, %) | 3.4662 |
| Correlation vs SPY | 0.2151 |
| Tracking error vs SPY (%) | 29.8580 |
| P/E (trailing) | 33.50 |
| P/B | 6.31 |
| EV/EBITDA | 25.91 |
| Revenue growth (%) | 11.80 |
| Forward P/E (estimate) | 26.14 |
| Gross margin (%) | 54.81 |
| Operating margin (%) | 37.79 |
| Return on equity (%) | 20.80 |
| Free cash flow yield (%) | 1.77 |
| MA50 | 522.7354 |
| Close vs MA50 (%) | -0.3970 |
| MA200 | 484.5977 |
| Close vs MA200 (%) | 7.4417 |
| RSI (14, Wilder) | 43.3698 |
| MACD (12,26) | 3.2405 |
| MACD signal (9) | 6.0876 |
| MACD histogram | -2.8471 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'VRTX': 286, 'SPY': 286}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 520.6600 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -2.9434 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -4.0470 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 3.7275 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 14.8447 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 23.6634 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 29.5834 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 18.2051 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.4089 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.8866 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.4662 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2151 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 29.8580 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.4578 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -15.2113 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.8670 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 26.1413 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 54.8090 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 37.7920 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 20.8020 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.7710 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 33.5045 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 43.3698 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -2.8471 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -0.3970 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 7.4417 -> Clearly above the moving-average trend level.

## TAILWINDS

### Vertex Pharmaceuticals (VRTX) Stock May Be Undervalued After Its 187% Run
- Summary: Shares may be undervalued following a strong 187% run, suggesting potential upside.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxOMzdqc19Jc2NUcjA5cHVIOWczYUxqTm1wM1JnczRZbURpcFdSNzZMalFPb2JwZlJpSzQ4QlpwUGE2dFN5b0RtWDdvczZDZ2dPRkRtY1NNVmRFVWFKR0FKa2hBVkdzX1pxZ0szMEI4Wlk0X1lDVmQtbjVnSWpJUGZsZXhRVHp4REFXVHoySkxBN1JxZ004Yk5WWHljU0dkUmdWb0l1Vg?oc=5>

## HEADWINDS

### At $547.86 apiece, a director sold 271 Vertex Pharmaceuticals (VRTX) shares.
- Summary: Director sold 271 shares at $547.86, a potential negative signal.
- Date: 2026-11-18 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxPcTJKUkJKY0dwb2NJVl9fYWNJTzlZT2ZyUktRQktUajNBZWNEZWEwYU04STJySWswZ0xpVVlFRVh2OWhWdm1IWXJLaEhNR2NweGpDVGdyaUkwUUZxdUlsMFBWY0d2eGlwaWRIRjI3dTV2NVY4aDJCMFNWeXdUOVEtaXhlSHo1ejZjM24ycW9rcDhnTEVObWNqOTY0VWpTOXlNRnBUdXJDdlBPT21wc2pXa2VLLTFkT0RxMzRvR2szWlU?oc=5>

### After selling 1,000 shares of Vertex Pharmaceuticals (VRTX), Nancy Thornberry directly held 1,109.
- Summary: Director sold 1,000 shares but still holds 1,109, neutral impact.
- Date: 2026-11-18 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxQRHNsbWZZNUdXVHpKWURYUE1FZzFHU1NlNndWYmFySU5jMlFSUnIwUXVvZ0FUWnFHbkpTVWxoaXA3SjNYOFlqNTUwLUNRVWpBRmdaLTdBX0NOcHdQbkVNemlFM3hwOGJGZ21SS0JBcmx1eHRPS084b3Vmb2cyN3hBSFd4MG9KMUVRRkFkSGp5N3ZGUjRicHNwRnFwOU9DRTFlZlBac0Jsd2VwRXdlNDBmXy1MZ3NSSC0tQnVuLU44dzA?oc=5>

### Director Nancy A. Thornberry proposes selling 1,000 Vertex Pharmaceuticals (VRTX) shares.
- Summary: Director plans to sell 1,000 shares, possibly indicating a negative outlook.
- Date: 2026-11-16 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxOazFrcDI5VnZTcmtwY1kxcS04WGVfaVJaM2g3MkVJVGpzQmRMZDdjSDJYb1NZQUlGaVJydl9Od3N2a1hmTi1BbzY2S2x0NTBjSTBSdHVKb0hGeHNYTGF1MmpGajczSGRWZEt0aXlwR09rOFVSUG5IVzhGRjVuaXdsWEVyMGtHakZCUkc2YnJGQk5UbWZhcnB3emtqNjdwUDhjMXdRME1jaDdJUQ?oc=5>

## CATALYSTS

### Vertex Pharmaceuticals (VRTX) Director Nancy Thornberry Sells 1,000 Shares
- Summary: Director sold 1,000 shares, indicating insider activity.
- Date: 2026-11-19 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxOUjhveUltNGtMMHkxRV9nbmVuTWIwa2dTOUZfOVhJVHVrdTlVYXVVOU4yUEVkbUdveW1HMEhlLXI5SFhGOHozeDVhMm9KQ0wtd0Nrc0FhbEhJYWlJTVlrdXVpYjk2NWRMUkd2ODlLNS1EbG1Wb0Z1MXVmMVdPRW1TZUdmb3VEa01CNW0yNk1QdjFSVEVraWt2TXgwWFhsTDU1LWYybEQ2ZEJTaWpPOWIw?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **VRTX** | **33.50** | **6.31** | **25.91** | **11.80** | **132,006,920,192.00 USD** | **23.66** |
| REGN | 20.90 | 2.77 | 15.24 | 36.30 | 95,517,548,544.00 USD | 32.06 |
| BIIB | 106.98 | 1.93 | 13.03 | 10.60 | 36,530,810,880.00 USD | 47.16 |
| AMGN | 25.74 | 16.54 | 15.78 | 8.50 | 237,362,790,400.00 USD | 31.72 |

Peers fetched as_of: 2026-11-19; VRTX reuses existing data (market data as_of: 2026-11-19); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-02
- Next expected earnings: 2027-02-11 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-19

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-03
- Revenue (latest available single quarter): 640,799,000.00 USD; period 2018-01-01/2018-03-31; fiscal year/reporting period 2018/Q1
- Net income (latest available single quarter): 653,600,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/875320/000087532026000291/vrtx-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMipAFBVV95cUxOMzdqc19Jc2NUcjA5cHVIOWczYUxqTm1wM1JnczRZbURpcFdSNzZMalFPb2JwZlJpSzQ4QlpwUGE2dFN5b0RtWDdvczZDZ2dPRkRtY1NNVmRFVWFKR0FKa2hBVkdzX1pxZ0szMEI4Wlk0X1lDVmQtbjVnSWpJUGZsZXhRVHp4REFXVHoySkxBN1JxZ004Yk5WWHljU0dkUmdWb0l1Vg?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxPcTJKUkJKY0dwb2NJVl9fYWNJTzlZT2ZyUktRQktUajNBZWNEZWEwYU04STJySWswZ0xpVVlFRVh2OWhWdm1IWXJLaEhNR2NweGpDVGdyaUkwUUZxdUlsMFBWY0d2eGlwaWRIRjI3dTV2NVY4aDJCMFNWeXdUOVEtaXhlSHo1ejZjM24ycW9rcDhnTEVObWNqOTY0VWpTOXlNRnBUdXJDdlBPT21wc2pXa2VLLTFkT0RxMzRvR2szWlU?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxQRHNsbWZZNUdXVHpKWURYUE1FZzFHU1NlNndWYmFySU5jMlFSUnIwUXVvZ0FUWnFHbkpTVWxoaXA3SjNYOFlqNTUwLUNRVWpBRmdaLTdBX0NOcHdQbkVNemlFM3hwOGJGZ21SS0JBcmx1eHRPS084b3Vmb2cyN3hBSFd4MG9KMUVRRkFkSGp5N3ZGUjRicHNwRnFwOU9DRTFlZlBac0Jsd2VwRXdlNDBmXy1MZ3NSSC0tQnVuLU44dzA?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxOazFrcDI5VnZTcmtwY1kxcS04WGVfaVJaM2g3MkVJVGpzQmRMZDdjSDJYb1NZQUlGaVJydl9Od3N2a1hmTi1BbzY2S2x0NTBjSTBSdHVKb0hGeHNYTGF1MmpGajczSGRWZEt0aXlwR09rOFVSUG5IVzhGRjVuaXdsWEVyMGtHakZCUkc2YnJGQk5UbWZhcnB3emtqNjdwUDhjMXdRME1jaDdJUQ?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxOUjhveUltNGtMMHkxRV9nbmVuTWIwa2dTOUZfOVhJVHVrdTlVYXVVOU4yUEVkbUdveW1HMEhlLXI5SFhGOHozeDVhMm9KQ0wtd0Nrc0FhbEhJYWlJTVlrdXVpYjk2NWRMUkd2ODlLNS1EbG1Wb0Z1MXVmMVdPRW1TZUdmb3VEa01CNW0yNk1QdjFSVEVraWt2TXgwWFhsTDU1LWYybEQ2ZEJTaWpPOWIw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
