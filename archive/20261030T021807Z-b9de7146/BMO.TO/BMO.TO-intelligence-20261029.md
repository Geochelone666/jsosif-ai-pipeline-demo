# BMO.TO Intelligence Report

- ticker: **BMO.TO**
- Report as_of: **2026-10-29**
- Market data as_of: **2026-10-29**
- Quant sources: https://finance.yahoo.com/quote/BMO.TO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/BMO.TO/key-statistics/
- AI analysis snapshot as_of: **2026-10-29**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-30T02:20:34.931895+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 12, 'rule': 0, 'ai': 8, 'unknown': 0, 'irrelevant': 4})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **1** exact headline/source/date matches; prior report **20261029T020157Z-688a53f0/BMO.TO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 12 unique headlines; 8 named publishers; 0 exact duplicates; 12 HTTPS source links; largest publisher share 33.33%; oldest publication 2026-10-26

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 246.2800 |
| Return 1D (%) | 1.1625 |
| Return 1W (%) | 3.1755 |
| Return 1M (%) | 2.3225 |
| Return YTD (%) | 41.4977 |
| Return 1Y (%) | 44.8956 |
| Annualized volatility (%) | 19.1243 |
| Beta vs SPY | 0.8710 |
| Max drawdown (%) | -11.4239 |
| Sharpe (rf=0) | 2.0437 |
| Downside deviation (rf=0, %) | 13.0573 |
| Sortino (rf=0) | 2.9934 |
| Historical VaR 95% (1D, %) | 1.8771 |
| Historical ES 95% (1D, %) | 2.5885 |
| Correlation vs SPY | 0.5764 |
| Tracking error vs SPY (%) | 15.8444 |
| P/E (trailing) | 20.07 |
| P/B | 2.02 |
| EV/EBITDA | N/A |
| Revenue growth (%) | 12.00 |
| Forward P/E (estimate) | 14.96 |
| Gross margin (%) | 0.00 |
| Operating margin (%) | 30.50 |
| Return on equity (%) | 10.57 |
| Free cash flow yield (%) | N/A |
| MA50 | 239.2556 |
| Close vs MA50 (%) | 2.9359 |
| MA200 | 220.2833 |
| Close vs MA200 (%) | 11.8015 |
| RSI (14, Wilder) | 62.8713 |
| MACD (12,26) | 0.7367 |
| MACD signal (9) | -0.7123 |
| MACD histogram | 1.4490 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'BMO.TO': 270, 'SPY': 271}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 246.2800 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.1625 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 3.1755 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 2.3225 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 41.4977 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 44.8956 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 19.1243 -> Low annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 13.0573 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 2.9934 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.8771 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.5885 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5764 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 15.8444 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.8710 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -11.4239 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 2.0437 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 14.9589 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 0.0000 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 30.4990 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 10.5740 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 20.0717 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 62.8713 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 1.4490 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 2.9359 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 11.8015 -> Clearly above the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

No items in this run

## CATALYSTS

### Bank Of Montreal (TSX:BMO) Debuts Canada’s First Single Stock Autocallable Income ETFs
- Summary: BMO introduces its first single‑stock autocallable income ETF in Canada.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxOY05EeGdVOVhLcWtWZFYySWgxclRJT3dXMUJ4NkdKSjZURFZ2b3dTNnNiZ0hrM1Mtd0tnbXBtRmpEa05hVm5LY0oxWnRUUFVRWGFUc3N5VGJ4TVNwRnRvb09DbldhZFhqWTNOR1dFUFcweW1YLWZ0Nk5iZ0M2N21HSFJpZGJjTE5PYzQyLUFCNlJMYkgteEo5Zw?oc=5>

### Leaders from more than 100 companies, including Reddit and IBM, will join BMO's New York tech conference.
- Summary: BMO hosts a tech conference in New York with 100+ company leaders.
- Date: 2026-10-29 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxPT1BNdmdsbktYNHVzaE9hMkV5Z1BqNEdVMkhxVWpDUlpNWGhVR01aS2Yzcm1CMVFDNW16X1BWcVlPTkw0LUxrNWpwdnIxcXRuM0RWMU5sTHphdlVQOHl0Mjl5c3FlUjhKT3hXdHZOdV9fSlZnYzRkaHI0SFZpdTcwY1dndFVadEtkMU9kVGkyQ1dZekpQRGZ1MkdnRnhaOGVZQUloMHlPeVZhcG02elA5MGtPZ1Z6b2dJRTl5cHFMNA?oc=5>

### Bank Of Montreal (BMO) Stock Forecasts
- Summary: BMO releases stock forecasts for investors.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxNekhRZkdFMGJRRlA1ZW1Mdl9PcEpCMVJ6S1Z4VWtmS0NMdzFhTEk5aU1sRFhoZmNBdGpsaTByR0I4LU1fX0J4RGhlLXg5eER5NmpjSS12a0RkbHJGT2w2alk5bFVYcUJfU2FNXzRBYVNDMGJMSGk5X1JScnBIUFB5WmhNTlpFSzgtUFJueV9EZVhpQWc?oc=5>

### After selling two finance businesses, BMO holds a 19.9% stake in their buyer.
- Summary: BMO retains a 19.9% stake in the buyer after divesting two finance units.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxQZEpJVTBjWjlFd0htUEJic2JibmppTXd2d29TUmJzRGR4UGliOUtzZEFLbzBpb2RPREtpS2ZrRDBtVnRwY2wybk5rTUM1VFFCd3R3VnhBbkwxZ25QZm53MjMyWlpfX2VxMjVSeEFMOHQxS0c1REZwQzJTR19FaGotYlZ5bmpuR21HRXlYNWhyZmstUW5iZmVmU0x6N3c5bFZJOUU1NWF5NFZRZw?oc=5>

### BMO Launches Canada's First Single Stock Autocallable Income ETFs
- Summary: BMO launches Canada’s first single‑stock autocallable income ETF.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxPdEtncmR3a3h6SkxZbnhaY1JEX1V4dVJvRnFCSmxGLTdjYVZYWC0xLS1oU0xUVkppUEJqS29KOWR0QTNFdXc3ZXJpZ1RVeTQwYVd5WE5IaWxsdWhoY2Y4ZHdQeE1CTDVkQmwwWkl4eTFEVFdpdVhqTG4tclkwTGhQY09lbjlZV1ZQbjd0U1owMkcxaXQ1aEhKNDBtcER4NFQ1WFE?oc=5>

### Analysts assign a CAD 256.57 target to Bank of Montreal stock
- Summary: Analysts set a price target of CAD 256.57 for BMO shares.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxNbU1TRFROWWFVei0tc3dJRmhicGRPMlZYRGFtUkNHbjJLaTVUUDJnWnFkamVmUy0wV29xN29QeDNkS3NPSXRBNWh2UFFiVEN3OUFHOEY2QUMxeGpSV1k5UmVjNXViQS02cTU2UmkxX0J5THZjcENaaXRMNTJZdUUtUDF4YzY5S1RtWFI5UEtnTGRpRXlOeGZTZ3NyVFJiN2RCdS11SzZCVUFldlk4cGFMa0x4dHRkUm9reVFaUS03dDRhUQ?oc=5>

### Bank of Montreal raises prime rate to 4.70 percent: what it means for Bank of Montreal stock
- Summary: BMO increased its prime rate to 4.70%, signaling tighter lending conditions.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi6gFBVV95cUxQWUpfdmpmZEM5T3Vrb1VxN1RzMW9lVVY3Mk5WcWpobS05M0REN3BPNWIza3NHQk9hRXZucXBLWi1vWUFmSXF0ZHBFRUpNX0RxMWQ3TFpiTFNXVnhuUXV0T0k5Mm41TjVmaW9WQXNiUG9VaDVoc2xVZzZOY1pVVXZETTBZNDcydmx1bUFwb1Njc1k4Nm5XaXpIZFZyYmp6WDNnNEYzZWlTZnQzb3ZiTWdDeXhfTkNxUnhfanR5bDlWVTIwMnE0b1BSdlFVeE5vWUtPU3h6M2ZIM1pDZmNvR0RHYW55QmZCanBnNnc?oc=5>

### Simply Wall St questions fair value for BMO stock
- Summary: Simply Wall St doubts BMO’s valuation, suggesting it may be overvalued.
- Date: 2026-10-28 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxPem1GVmJxRU8xbzRBd1BUcWpiNWtmUXh5anFHcm52S1Q2a0Z5cDUyclI3Y2pXMHRKcy1FUThicnJZbEhRT2NNclFSbnVYT1Z0VTFSYnp0blVYSGowampMVHdPLXVyV1BtTTgzSzdZeGRwRXJRUXVWQ0hXNmphcFJ1SldULUtHUm83ZThXNUVzeG1RRzNjaFpFSzNZY1h1RDhfN1RhbUhUVnJKRjFZZDBEanlR?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **BMO.TO** | **20.07** | **2.02** | **N/A** | **12.00** | **171,187,306,496.00 CAD** | **44.90** |
| RY.TO | 18.17 | 2.98 | N/A | 8.90 | 399,006,498,816.00 CAD | 44.63 |
| TD.TO | 19.07 | 2.36 | N/A | 11.50 | 290,889,269,248.00 CAD | 60.93 |
| BNS.TO | 17.44 | 1.82 | N/A | 11.70 | 162,640,674,816.00 CAD | 52.49 |

Peers fetched as_of: 2026-10-29; BMO.TO reuses existing data (market data as_of: 2026-10-29); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-25
- Next expected earnings: 2026-12-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-29

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
- https://news.google.com/rss/articles/CBMivwFBVV95cUxPT1BNdmdsbktYNHVzaE9hMkV5Z1BqNEdVMkhxVWpDUlpNWGhVR01aS2Yzcm1CMVFDNW16X1BWcVlPTkw0LUxrNWpwdnIxcXRuM0RWMU5sTHphdlVQOHl0Mjl5c3FlUjhKT3hXdHZOdV9fSlZnYzRkaHI0SFZpdTcwY1dndFVadEtkMU9kVGkyQ1dZekpQRGZ1MkdnRnhaOGVZQUloMHlPeVZhcG02elA5MGtPZ1Z6b2dJRTl5cHFMNA?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxNekhRZkdFMGJRRlA1ZW1Mdl9PcEpCMVJ6S1Z4VWtmS0NMdzFhTEk5aU1sRFhoZmNBdGpsaTByR0I4LU1fX0J4RGhlLXg5eER5NmpjSS12a0RkbHJGT2w2alk5bFVYcUJfU2FNXzRBYVNDMGJMSGk5X1JScnBIUFB5WmhNTlpFSzgtUFJueV9EZVhpQWc?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxQZEpJVTBjWjlFd0htUEJic2JibmppTXd2d29TUmJzRGR4UGliOUtzZEFLbzBpb2RPREtpS2ZrRDBtVnRwY2wybk5rTUM1VFFCd3R3VnhBbkwxZ25QZm53MjMyWlpfX2VxMjVSeEFMOHQxS0c1REZwQzJTR19FaGotYlZ5bmpuR21HRXlYNWhyZmstUW5iZmVmU0x6N3c5bFZJOUU1NWF5NFZRZw?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxPdEtncmR3a3h6SkxZbnhaY1JEX1V4dVJvRnFCSmxGLTdjYVZYWC0xLS1oU0xUVkppUEJqS29KOWR0QTNFdXc3ZXJpZ1RVeTQwYVd5WE5IaWxsdWhoY2Y4ZHdQeE1CTDVkQmwwWkl4eTFEVFdpdVhqTG4tclkwTGhQY09lbjlZV1ZQbjd0U1owMkcxaXQ1aEhKNDBtcER4NFQ1WFE?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxNbU1TRFROWWFVei0tc3dJRmhicGRPMlZYRGFtUkNHbjJLaTVUUDJnWnFkamVmUy0wV29xN29QeDNkS3NPSXRBNWh2UFFiVEN3OUFHOEY2QUMxeGpSV1k5UmVjNXViQS02cTU2UmkxX0J5THZjcENaaXRMNTJZdUUtUDF4YzY5S1RtWFI5UEtnTGRpRXlOeGZTZ3NyVFJiN2RCdS11SzZCVUFldlk4cGFMa0x4dHRkUm9reVFaUS03dDRhUQ?oc=5
- https://news.google.com/rss/articles/CBMi6gFBVV95cUxQWUpfdmpmZEM5T3Vrb1VxN1RzMW9lVVY3Mk5WcWpobS05M0REN3BPNWIza3NHQk9hRXZucXBLWi1vWUFmSXF0ZHBFRUpNX0RxMWQ3TFpiTFNXVnhuUXV0T0k5Mm41TjVmaW9WQXNiUG9VaDVoc2xVZzZOY1pVVXZETTBZNDcydmx1bUFwb1Njc1k4Nm5XaXpIZFZyYmp6WDNnNEYzZWlTZnQzb3ZiTWdDeXhfTkNxUnhfanR5bDlWVTIwMnE0b1BSdlFVeE5vWUtPU3h6M2ZIM1pDZmNvR0RHYW55QmZCanBnNnc?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxPem1GVmJxRU8xbzRBd1BUcWpiNWtmUXh5anFHcm52S1Q2a0Z5cDUyclI3Y2pXMHRKcy1FUThicnJZbEhRT2NNclFSbnVYT1Z0VTFSYnp0blVYSGowampMVHdPLXVyV1BtTTgzSzdZeGRwRXJRUXVWQ0hXNmphcFJ1SldULUtHUm83ZThXNUVzeG1RRzNjaFpFSzNZY1h1RDhfN1RhbUhUVnJKRjFZZDBEanlR?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
