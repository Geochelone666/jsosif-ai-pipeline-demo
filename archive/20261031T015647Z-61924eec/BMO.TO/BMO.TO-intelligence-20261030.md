# BMO.TO Intelligence Report

- ticker: **BMO.TO**
- Report as_of: **2026-10-30**
- Market data as_of: **2026-10-30**
- Quant sources: https://finance.yahoo.com/quote/BMO.TO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/BMO.TO/key-statistics/
- AI analysis snapshot as_of: **2026-10-30**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-31T02:12:40.569349+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 15, 'rule': 0, 'ai': 6, 'unknown': 0, 'irrelevant': 9})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **7** exact headline/source/date matches; prior report **20261030T021807Z-b9de7146/BMO.TO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 15 unique headlines; 11 named publishers; 0 exact duplicates; 15 HTTPS source links; largest publisher share 20.0%; oldest publication 2026-10-26

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 239.2200 |
| Return 1D (%) | -2.1875 |
| Return 1W (%) | 1.6982 |
| Return 1M (%) | 1.2281 |
| Return YTD (%) | 38.4025 |
| Return 1Y (%) | 42.5613 |
| Annualized volatility (%) | 19.2537 |
| Beta vs SPY | 0.8814 |
| Max drawdown (%) | -11.4239 |
| Sharpe (rf=0) | 1.9465 |
| Downside deviation (rf=0, %) | 13.2269 |
| Sortino (rf=0) | 2.8334 |
| Historical VaR 95% (1D, %) | 1.9150 |
| Historical ES 95% (1D, %) | 2.6099 |
| Correlation vs SPY | 0.5830 |
| Tracking error vs SPY (%) | 15.8477 |
| P/E (trailing) | 19.50 |
| P/B | 1.96 |
| EV/EBITDA | N/A |
| Revenue growth (%) | 12.00 |
| Forward P/E (estimate) | 14.53 |
| Gross margin (%) | 0.00 |
| Operating margin (%) | 30.50 |
| Return on equity (%) | 10.57 |
| Free cash flow yield (%) | N/A |
| MA50 | 237.5601 |
| Close vs MA50 (%) | 0.6987 |
| MA200 | 219.0525 |
| Close vs MA200 (%) | 9.2067 |
| RSI (14, Wilder) | 52.8096 |
| MACD (12,26) | 0.7711 |
| MACD signal (9) | -0.4116 |
| MACD histogram | 1.1828 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'BMO.TO': 271, 'SPY': 272}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 239.2200 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -2.1875 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 1.6982 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 1.2281 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 38.4025 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 42.5613 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 19.2537 -> Low annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 13.2269 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 2.8334 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.9150 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.6099 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5830 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 15.8477 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.8814 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -11.4239 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.9465 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 14.5301 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 0.0000 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 30.4990 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 10.5740 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 19.4963 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 52.8096 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 1.1828 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 0.6987 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 9.2067 -> Clearly above the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

No items in this run

## CATALYSTS

### Bank Of Montreal (TSX:BMO) Debuts Canada’s First Single Stock Autocallable Income ETFs
- Summary: BMO introduces its first single‑stock autocallable income ETF in Canada.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxOY05EeGdVOVhLcWtWZFYySWgxclRJT3dXMUJ4NkdKSjZURFZ2b3dTNnNiZ0hrM1Mtd0tnbXBtRmpEa05hVm5LY0oxWnRUUFVRWGFUc3N5VGJ4TVNwRnRvb09DbldhZFhqWTNOR1dFUFcweW1YLWZ0Nk5iZ0M2N21HSFJpZGJjTE5PYzQyLUFCNlJMYkgteEo5Zw?oc=5>

### After selling two finance businesses, BMO holds a 19.9% stake in their buyer.
- Summary: BMO retains a 19.9% stake in the buyer after divesting two finance units.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxQZEpJVTBjWjlFd0htUEJic2JibmppTXd2d29TUmJzRGR4UGliOUtzZEFLbzBpb2RPREtpS2ZrRDBtVnRwY2wybk5rTUM1VFFCd3R3VnhBbkwxZ25QZm53MjMyWlpfX2VxMjVSeEFMOHQxS0c1REZwQzJTR19FaGotYlZ5bmpuR21HRXlYNWhyZmstUW5iZmVmU0x6N3c5bFZJOUU1NWF5NFZRZw?oc=5>

### BMO Launches Canada's First Single Stock Autocallable Income ETFs
- Summary: BMO launches Canada’s first single‑stock autocallable income ETF.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxPdEtncmR3a3h6SkxZbnhaY1JEX1V4dVJvRnFCSmxGLTdjYVZYWC0xLS1oU0xUVkppUEJqS29KOWR0QTNFdXc3ZXJpZ1RVeTQwYVd5WE5IaWxsdWhoY2Y4ZHdQeE1CTDVkQmwwWkl4eTFEVFdpdVhqTG4tclkwTGhQY09lbjlZV1ZQbjd0U1owMkcxaXQ1aEhKNDBtcER4NFQ1WFE?oc=5>

### How Higher Prime Rates At BMO Stock Have Changed Its Investment Story
- Summary: Higher prime rates at BMO have altered its investment narrative, impacting investor perception and potential valuation.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxNTGF1M29GbmJpTmpjYWlheDhKenJidkVqOEgyZ2NPaG9rY003bjNrWENZX0RrbzNtOFVyV2sxQWRVNnVKRi1xZEd0M2dKOTBZMXlJMVU4aUJHQm5ibUtUclBDdnFWY0s3NWVhSXc0V21yRS1ZOXpPZnZfejZ6a0Y5TUgwX0dwT0dJRHJUVC1KRjA3WFlsdnJQOQ?oc=5>

### BMO stock: Stonepeak deal shifts C$11 billion portfolio
- Summary: BMO partners with Stonepeak, moving C$11 billion of assets into a new portfolio structure, potentially enhancing diversification and strategic positioning.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxPSVoxQ09sS0JVVWJuRnJBem5VS2o1UXpKM1FVVkpnbVFlNWp0VGhUUjJfc1hhLWF2SFhHVEJvcDNPbHJ3VFBFcW1qcXhUWGRMQ0Z5RzZwZHkzV09mU0J1ZkpoanpKWlNZcXl1RVhmUTllWlhCYWV4a3pNRXNMY2xsREJKbWNpRllJdU4xLXV4dVpuZXpVUGhDdUJMRXVuU0pfV3VNSnFqNXlNR1lWcU11S21pSk0wWll2?oc=5>

### Bank of Montreal stock: BMO closes C$14.5 billion finance sale
- Summary: BMO completes a C$14.5B finance sale, marking a significant transaction for the bank.
- Date: 2026-10-30 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxQeDJNUWlLaHRsdUhsazhaMHZLRktCc25mZ0l3U0FEZE9Wa3pNMkJnbm9abmdKWENfcWpsSEZtbUNHZWJnVmthMnpqTTdMcmcyUFZ1cEZiUVVGS1J2b1RtSEloRG5mNThmeVI0M09MbHVLcUZkc0N6ZGR1WVlVa09oald5WkNvM01CankyUGJqeGJsb2hYeVpud3ZTeS1RVUVid1I3QnRGX2Vmc3NuVjNOZ2pYejEwV2ZiZVRpdldVbmNkQQ?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **BMO.TO** | **19.50** | **1.96** | **N/A** | **12.00** | **166,279,970,816.00 CAD** | **42.56** |
| RY.TO | 17.90 | 2.94 | N/A | 8.90 | 393,081,159,680.00 CAD | 42.78 |
| TD.TO | 18.63 | 2.30 | N/A | 11.50 | 284,210,200,576.00 CAD | 56.39 |
| BNS.TO | 17.13 | 1.79 | N/A | 11.70 | 159,727,665,152.00 CAD | 48.52 |

Peers fetched as_of: 2026-10-30; BMO.TO reuses existing data (market data as_of: 2026-10-30); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-25
- Next expected earnings: 2026-12-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-30

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
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

- https://news.google.com/rss/articles/CBMimAFBVV95cUxOY05EeGdVOVhLcWtWZFYySWgxclRJT3dXMUJ4NkdKSjZURFZ2b3dTNnNiZ0hrM1Mtd0tnbXBtRmpEa05hVm5LY0oxWnRUUFVRWGFUc3N5VGJ4TVNwRnRvb09DbldhZFhqWTNOR1dFUFcweW1YLWZ0Nk5iZ0M2N21HSFJpZGJjTE5PYzQyLUFCNlJMYkgteEo5Zw?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxQZEpJVTBjWjlFd0htUEJic2JibmppTXd2d29TUmJzRGR4UGliOUtzZEFLbzBpb2RPREtpS2ZrRDBtVnRwY2wybk5rTUM1VFFCd3R3VnhBbkwxZ25QZm53MjMyWlpfX2VxMjVSeEFMOHQxS0c1REZwQzJTR19FaGotYlZ5bmpuR21HRXlYNWhyZmstUW5iZmVmU0x6N3c5bFZJOUU1NWF5NFZRZw?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxPdEtncmR3a3h6SkxZbnhaY1JEX1V4dVJvRnFCSmxGLTdjYVZYWC0xLS1oU0xUVkppUEJqS29KOWR0QTNFdXc3ZXJpZ1RVeTQwYVd5WE5IaWxsdWhoY2Y4ZHdQeE1CTDVkQmwwWkl4eTFEVFdpdVhqTG4tclkwTGhQY09lbjlZV1ZQbjd0U1owMkcxaXQ1aEhKNDBtcER4NFQ1WFE?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxNTGF1M29GbmJpTmpjYWlheDhKenJidkVqOEgyZ2NPaG9rY003bjNrWENZX0RrbzNtOFVyV2sxQWRVNnVKRi1xZEd0M2dKOTBZMXlJMVU4aUJHQm5ibUtUclBDdnFWY0s3NWVhSXc0V21yRS1ZOXpPZnZfejZ6a0Y5TUgwX0dwT0dJRHJUVC1KRjA3WFlsdnJQOQ?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxPSVoxQ09sS0JVVWJuRnJBem5VS2o1UXpKM1FVVkpnbVFlNWp0VGhUUjJfc1hhLWF2SFhHVEJvcDNPbHJ3VFBFcW1qcXhUWGRMQ0Z5RzZwZHkzV09mU0J1ZkpoanpKWlNZcXl1RVhmUTllWlhCYWV4a3pNRXNMY2xsREJKbWNpRllJdU4xLXV4dVpuZXpVUGhDdUJMRXVuU0pfV3VNSnFqNXlNR1lWcU11S21pSk0wWll2?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxQeDJNUWlLaHRsdUhsazhaMHZLRktCc25mZ0l3U0FEZE9Wa3pNMkJnbm9abmdKWENfcWpsSEZtbUNHZWJnVmthMnpqTTdMcmcyUFZ1cEZiUVVGS1J2b1RtSEloRG5mNThmeVI0M09MbHVLcUZkc0N6ZGR1WVlVa09oald5WkNvM01CankyUGJqeGJsb2hYeVpud3ZTeS1RVUVid1I3QnRGX2Vmc3NuVjNOZ2pYejEwV2ZiZVRpdldVbmNkQQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
