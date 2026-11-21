# VRTX Intelligence Report

- ticker: **VRTX**
- Report as_of: **2026-11-20**
- Market data as_of: **2026-11-20**
- Quant sources: https://finance.yahoo.com/quote/VRTX/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/VRTX/key-statistics/
- AI analysis snapshot as_of: **2026-11-20**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-21T05:40:33.435797+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 13, 'rule': 0, 'ai': 10, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **8** exact headline/source/date matches; prior report **20261120T053808Z-e360129e/VRTX** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 13 unique headlines; 9 named publishers; 0 exact duplicates; 13 HTTPS source links; largest publisher share 30.77%; oldest publication 2026-11-16

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 515.0200 |
| Return 1D (%) | -1.0832 |
| Return 1W (%) | -4.3780 |
| Return 1M (%) | 0.0719 |
| Return YTD (%) | 13.6007 |
| Return 1Y (%) | 21.9502 |
| Annualized volatility (%) | 29.6065 |
| Beta vs SPY | 0.4558 |
| Max drawdown (%) | -15.2113 |
| Sharpe (rf=0) | 0.8192 |
| Downside deviation (rf=0, %) | 18.2375 |
| Sortino (rf=0) | 1.3299 |
| Historical VaR 95% (1D, %) | 2.8866 |
| Historical ES 95% (1D, %) | 3.4662 |
| Correlation vs SPY | 0.2201 |
| Tracking error vs SPY (%) | 29.9102 |
| P/E (trailing) | 33.14 |
| P/B | 6.25 |
| EV/EBITDA | 25.63 |
| Revenue growth (%) | 11.80 |
| Forward P/E (estimate) | 25.86 |
| Gross margin (%) | 54.81 |
| Operating margin (%) | 37.79 |
| Return on equity (%) | 20.80 |
| Free cash flow yield (%) | 1.79 |
| MA50 | 522.7270 |
| Close vs MA50 (%) | -1.4744 |
| MA200 | 484.8788 |
| Close vs MA200 (%) | 6.2162 |
| RSI (14, Wilder) | 40.8542 |
| MACD (12,26) | 1.3001 |
| MACD signal (9) | 5.1301 |
| MACD histogram | -3.8300 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'VRTX': 287, 'SPY': 287}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 515.0200 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.0832 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -4.3780 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 0.0719 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 13.6007 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 21.9502 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 29.6065 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 18.2375 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.3299 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.8866 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.4662 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2201 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 29.9102 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.4558 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -15.2113 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.8192 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 25.8581 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 54.8090 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 37.7920 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 20.8020 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.7904 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 33.1416 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 40.8542 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -3.8300 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -1.4744 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 6.2162 -> Clearly above the moving-average trend level.

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

### Has Vertex Stock Become A Different Bet?
- Summary: Speculation on Vertex’s valuation shift and future prospects.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxQZXpZMUo0ZVNUd2NvOGY0N0tVVkVidzhBUS1IWGYxNVN2N2t2OTJSYkdZdnlHMVgyU0l5ZjlSeUt2N3dmVmVzdmJNdlBCUVNPeHlMaXptT2hEVjNVNFJvdEtDRk1kdjFLSDU2enFnMTBiUjRLRTFWNUxQRHlBc3dkTFdmYTRoRlM1dnRyejJGWWdhMEFJN1ZLU2pUQkZicGtSYUE?oc=5>

### Vertex Pharmaceuticals: Look For Povetacicept Approval In 2 Weeks As Next Catalyst
- Summary: Potential approval of Povetacicept within two weeks could boost Vertex’s pipeline.
- Date: 2026-11-20 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxNd3g5ZUlkYjdveC1zQUZ0cW5Bb3dUUXBfdlNxTFEzd2hKYm9HRWpBNGZlYXpoaFUwWFVha0VSdFdqQm1uMUp5WGw0OVg0LTBYYmtOUDg5RVpTMHkzbndsc0FCd1BzWFdIdUcweEszLXVwUGtpVTc0Y0E2RER5OWhHcWpZT29lWGZnSEJnNl9tOTlEd3M5OFR3UnNWRzZZN1ViWTBhcW1tWEwwYWNUc1EzS01TaVBqYXUxd1NPM0NDQQ?oc=5>

### Johnson & Johnson vs. Vertex Pharmaceuticals: Which Healthcare Stock Is a Better Buy for 2027?
- Summary: Comparative analysis of Vertex versus J&J for 2027 investment decisions.
- Date: 2026-11-17 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2gFBVV95cUxPQXUyN0FVWEdfYURrM3RDaVR5WjB5dFJNRXA5aFU0d2RNbURpbnJyOUZXZ1hoUmVBTm1mSE5OdDVoOF9xdWNZNUtGQXZ1QnladjFxZXdGb1lNeHdYX1NjZ2FOUnY0WXo2ZjctWHVUcEJmN2ZzNHVxTlVDMVhfeld4QmpVWnlFZW9VUXpmRko2eXBFcHNNLVE1M0xJYS05Q1kzOGJ2d1FlREc3Vmg0R2I5cldjbmRSNzBSOXdBc1ZPVGp1dDRLZjg1SE42VkZwU25WR3V3dERsQWVFQQ?oc=5>

### Vertex Pharmaceuticals (VRTX) Could Be 11% Undervalued On Late Stage Pipeline Focus
- Summary: Assessment that Vertex may be undervalued based on its late-stage pipeline.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxPalJjMEE3YjRwVHd6UWhSUXhyaDBUSF9ycnJkZW54SlkxQzU1NWNKY3J6eXdoeGZRcnhaWnRVUWk4aGloLWhHbUVMbEU4ZThTdUxSYWpQZzlWYmU5b1ZVRmVvWGdpelktVFNtM0JSYlJPNldXYlBHd3dVVHJQdGVBQUpHQXNzcS1Jd25zaEtmemtrcjBEYU90Z1M5ZkFOUQ?oc=5>

### Will Vertex Pharmaceuticals (NASDAQ:VRTX) Turn Its Pipeline Into Momentum?
- Summary: Questioning whether Vertex’s pipeline will generate market momentum.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxNMU1Na2x4LTJYbmw0VzEtZV82UldOUWkzYjVtdDFQVzRnVXlhaXh4OWNQRGt5QnY1c09DVWE2aVZYcE9zaE5XZjM4M3pBQWhBRzN3WVY3cUZrM1ZxcHVWMDdUeFgtWGx5RWp1dWFnSHdhYV9MdXZUNzkwTG1TZTFOYXZKZGt0cjlfOHNRblhWM1BaelIyV1NlYTZ4czMyZV9OcThpNVFJVE1lbVE4VmczN01jUU4wckU?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **VRTX** | **33.14** | **6.25** | **25.63** | **11.80** | **130,576,982,016.00 USD** | **21.95** |
| REGN | 20.35 | 2.76 | 15.19 | 36.30 | 95,243,403,264.00 USD | 25.54 |
| BIIB | 108.05 | 1.95 | 13.14 | 10.60 | 36,894,449,664.00 USD | 48.41 |
| AMGN | 25.43 | 16.42 | 15.68 | 8.50 | 235,642,683,392.00 USD | 33.99 |

Peers fetched as_of: 2026-11-20; VRTX reuses existing data (market data as_of: 2026-11-20); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-02
- Next expected earnings: 2027-02-11 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-20

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
- https://news.google.com/rss/articles/CBMiogFBVV95cUxQZXpZMUo0ZVNUd2NvOGY0N0tVVkVidzhBUS1IWGYxNVN2N2t2OTJSYkdZdnlHMVgyU0l5ZjlSeUt2N3dmVmVzdmJNdlBCUVNPeHlMaXptT2hEVjNVNFJvdEtDRk1kdjFLSDU2enFnMTBiUjRLRTFWNUxQRHlBc3dkTFdmYTRoRlM1dnRyejJGWWdhMEFJN1ZLU2pUQkZicGtSYUE?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxNd3g5ZUlkYjdveC1zQUZ0cW5Bb3dUUXBfdlNxTFEzd2hKYm9HRWpBNGZlYXpoaFUwWFVha0VSdFdqQm1uMUp5WGw0OVg0LTBYYmtOUDg5RVpTMHkzbndsc0FCd1BzWFdIdUcweEszLXVwUGtpVTc0Y0E2RER5OWhHcWpZT29lWGZnSEJnNl9tOTlEd3M5OFR3UnNWRzZZN1ViWTBhcW1tWEwwYWNUc1EzS01TaVBqYXUxd1NPM0NDQQ?oc=5
- https://news.google.com/rss/articles/CBMi2gFBVV95cUxPQXUyN0FVWEdfYURrM3RDaVR5WjB5dFJNRXA5aFU0d2RNbURpbnJyOUZXZ1hoUmVBTm1mSE5OdDVoOF9xdWNZNUtGQXZ1QnladjFxZXdGb1lNeHdYX1NjZ2FOUnY0WXo2ZjctWHVUcEJmN2ZzNHVxTlVDMVhfeld4QmpVWnlFZW9VUXpmRko2eXBFcHNNLVE1M0xJYS05Q1kzOGJ2d1FlREc3Vmg0R2I5cldjbmRSNzBSOXdBc1ZPVGp1dDRLZjg1SE42VkZwU25WR3V3dERsQWVFQQ?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxPalJjMEE3YjRwVHd6UWhSUXhyaDBUSF9ycnJkZW54SlkxQzU1NWNKY3J6eXdoeGZRcnhaWnRVUWk4aGloLWhHbUVMbEU4ZThTdUxSYWpQZzlWYmU5b1ZVRmVvWGdpelktVFNtM0JSYlJPNldXYlBHd3dVVHJQdGVBQUpHQXNzcS1Jd25zaEtmemtrcjBEYU90Z1M5ZkFOUQ?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxNMU1Na2x4LTJYbmw0VzEtZV82UldOUWkzYjVtdDFQVzRnVXlhaXh4OWNQRGt5QnY1c09DVWE2aVZYcE9zaE5XZjM4M3pBQWhBRzN3WVY3cUZrM1ZxcHVWMDdUeFgtWGx5RWp1dWFnSHdhYV9MdXZUNzkwTG1TZTFOYXZKZGt0cjlfOHNRblhWM1BaelIyV1NlYTZ4czMyZV9OcThpNVFJVE1lbVE4VmczN01jUU4wckU?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
