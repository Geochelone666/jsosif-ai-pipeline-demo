# XYL Intelligence Report

- ticker: **XYL**
- Report as_of: **2026-11-09**
- Market data as_of: **2026-11-09**
- Quant sources: https://finance.yahoo.com/quote/XYL/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/XYL/key-statistics/
- AI analysis snapshot as_of: **2026-11-09**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-10T05:54:06.299289+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 11, 'rule': 2, 'ai': 7, 'unknown': 0, 'irrelevant': 2})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **5** exact headline/source/date matches; prior report **20261109T043242Z-c8e908de/XYL** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 11 unique headlines; 8 named publishers; 0 exact duplicates; 11 HTTPS source links; largest publisher share 36.36%; oldest publication 2026-11-05

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 99.2600 |
| Return 1D (%) | 1.4617 |
| Return 1W (%) | 2.0563 |
| Return 1M (%) | -3.3590 |
| Return YTD (%) | -26.2979 |
| Return 1Y (%) | -33.4800 |
| Annualized volatility (%) | 30.7053 |
| Beta vs SPY | 0.6264 |
| Max drawdown (%) | -40.7701 |
| Sharpe (rf=0) | -1.1744 |
| Downside deviation (rf=0, %) | 25.2363 |
| Sortino (rf=0) | -1.4289 |
| Historical VaR 95% (1D, %) | 3.0033 |
| Historical ES 95% (1D, %) | 5.0991 |
| Correlation vs SPY | 0.2793 |
| Tracking error vs SPY (%) | 29.9235 |
| P/E (trailing) | 22.01 |
| P/B | 2.23 |
| EV/EBITDA | 12.89 |
| Revenue growth (%) | -3.00 |
| Forward P/E (estimate) | 16.90 |
| Gross margin (%) | 39.32 |
| Operating margin (%) | 15.95 |
| Return on equity (%) | 9.76 |
| Free cash flow yield (%) | 5.32 |
| MA50 | 103.3082 |
| Close vs MA50 (%) | -3.9186 |
| MA200 | 115.3970 |
| Close vs MA200 (%) | -13.9839 |
| RSI (14, Wilder) | 47.5652 |
| MACD (12,26) | -1.8421 |
| MACD signal (9) | -2.0744 |
| MACD histogram | 0.2322 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'XYL': 278, 'SPY': 278}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 99.2600 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.4617 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 2.0563 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -3.3590 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -26.2979 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -33.4800 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 30.7053 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 25.2363 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -1.4289 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.0033 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.0991 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2793 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 29.9235 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.6264 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -40.7701 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -1.1744 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 16.8979 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 39.3200 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 15.9470 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 9.7560 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 5.3171 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 22.0089 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 47.5652 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.2322 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -3.9186 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -13.9839 -> Clearly below the moving-average trend level.

## TAILWINDS

### Xylem (XYL) Valuation Faces A Fresh Test After Strong EPS And Softer 2026 Outlook
- Summary: Discusses valuation pressure due to strong EPS and weaker 2026 outlook.
- Date: 2026-11-05 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQTktwcmlkNldqRU1GS0wydEZGSzVIX0Zra0tocG5WVTJ6am9HR0hYenQzSGhudWJ0djFBSmFZNE1QOG54OC1UQm5vUlo2eWgxMWRrQTRQRURDbHZpT2pTWkRmaEpRcHlrUEp1LUY0ck1aY3JfN1ZwUHJzaEdtN1NPNWhobEcyY3FUMERwVWVWSFoyR085czZaQnd0bXU?oc=5>

### Xylem (XYL) Posted Stronger EPS, Is The Stock Cheap?
- Summary: Analyzes Xylem's recent earnings per share and valuation attractiveness.
- Date: 2026-11-07 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxOc3FvTWRlclJrWTcyQm92QU5VbVEtaUF5bzJvTjZleF9WYmhlMkR4OW1CSFJEOUE1ZEpBdHgyY0dtbGp6bk9wSXdGQTRQNVdmRnpxcnBJUWJuZkJaMjNzODJpbS0tNkl6WThiMDB1ZjlULXJPSWx0NGtaVDAzR1p0dnY5OGQ4MzQ0bzJlUExmOVZiTUpZZTVZMmFjU3E0aTctV2wzTlF3S1FUdlhIeUEtUm9qc1bSAboBQVVfeXFMTTRwbmxyeDYzRzVqUHBaenRNVzktTjdhbnY3bkN1VzVKaVk3cFp0WmZaY25tNF9hMm9zd0thZHBRNFdMTDhybU9SNjRsa2FpWTJpU2ZxYW1QS3draV9aVmtHbEpTd0dzTUtkOXQyb3YzZGlVZXg5OVEwS3kwZEctejlscnlLWDd0OERBWk92Yi1ycy1nLUxyWUd4T2c5WnctQUdxT2pJVzEwdTVqYkFmSnQzX21ObzdIVnd3?oc=5>

## HEADWINDS

### 106,420 Xylem Inc. $XYL Shares Sold by Candriam S.C.A.
- Summary: Investor sells 106,420 shares of Xylem.
- Date: 2026-11-08 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxPMkhlSkExRU0yN0NoM1k4cUM5RnNiaDdYLUFJazRUbUlqWE9BYWZhelFiVHhORGgxUjlRZWwxaTR2R1oyVDlDT3RRNjVNVWZxX3BtcXYySHBFVV93MDltMnc5WUJ5bkVfUVd6QXdjcE1VejlneEVVUWs5Q2pNcnZaWVkxQlVNbGhPTXY2QTdtYmdocUkwZjg5UWdjam9UT2FWY1VQamNwWW5sZUplYnc?oc=5>

## CATALYSTS

### Xylem Completes Acquisition of Cornell Pump and Roper Pump
- Summary: Xylem Completes Acquisition of Cornell Pump and Roper Pump
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxPbHBjNnVRUHV4RG9lWWVVTDV3cDd5R2R3dHp2NmhFSzlxWi1ZeHBkWmZTcWZtR2hESTBQUTBtVE9BOVRQLThqYVhmSnFEUnpHdERKYVh1ZUxNS0xxSDI0WFp5VDN6emk2Z2ZRaWxNUkZOZHJMM20xU2pXWHdfNWlRc29qZjZFUVNNeHNFQXBvaDNKT2x2dkhPRi1RV3JCdDVWbTQxSFlYUHJYV00?oc=5>

### Xylem Inc. $XYL Stock Sold by Pictet Asset Management Holding SA
- Summary: Xylem Inc. $XYL Stock Sold by Pictet Asset Management Holding SA
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxPY192UzVvLWN1YkIwT2REckRVYmowQ3VoNjVHWDZ2Uk1WbkxKbi12eGJRM3JZZXBGWkI2QWJha3diV1B1UGlNUXpWUW1PeXZKa3dXdEdEclExWlVfeHpPdkxSZUFhdkY4MnlnbGlOVUdrWi1CNExvUjRkVTdWSHMwX3BrbTZNRkhacGhfYWFncHBKdjlHLXk4YXFLWEtxcVNHT2pJajFCSHdWTU9UZGtITm9iREo3X0ZhTzdUWG4zQ1E?oc=5>

### Xylem Inc. $XYL Stake Lifted by Cincinnati Insurance Co.
- Summary: Cincinnati Insurance increases stake in Xylem.
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxOeWJDN3lLa3UydmZqR1ZxZC1XMHF4TTc5WHNzS2t1SUJTMFBLVWlRdl8xTmNiQjl0WlozN1NiRDdXV3FxT2k4SnhvWHdfS0h1RnNrRVo3YkxrMFRBaHdyMDVkdmhXYzdLQkIyZlNHczFUd2ZwUlVSbjJNMVlvOVctaVJEYlR4MlJnT3VYLVIyRERfeF9uUlFhTzNvMHBvWkRTczRFc3BzSVZHRnhGVTlaY3JJQjE?oc=5>

### Mirae Asset Global Investments Co. Ltd. Purchases New Shares in Xylem Inc. $XYL
- Summary: Mirae Asset buys new Xylem shares.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0gFBVV95cUxORUhUV0VFUDRBZFNyQjZJWnJTUzhQUEdCVlVvTzl0TDNkVGlRbXo1TVRpMzFSV0xQdzI3ZXRxNzd3dGhNY1RoQkdUNFExWHFDcWN6WU5aUGlJYnYzU19aa3ItS3dEazZHUzhYc0otSDdvd292OVp0ek1RdXp0MG9FNEgydnZBY1NsQkdxdXhoM2dpV0Znb2FiSmRRN3dqN21yYUtqM2JZZUxOVEpuTDY1eTRPWVBjM29SSV9wekR6Q2Vua1N4SmVRSXJIamhiZGkwbVE?oc=5>

### Fund Update: 1,763,752 XYLEM (XYL) shares added to BESSEMER GROUP INC portfolio
- Summary: Bessemer Group adds 1.76 million XYL shares, signaling confidence in the company.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxPeW1DR2lYY3p5Zk1wemFBOWFzOF9fTWZtZk92NVNDSjdUbXNzTGRib3A3VmtobC1GRnFGUUZFQWNySVlCUnpGT0laYWdVUGtEU2N0ZEpsc1JFRWpXc0Z2ZXU3NWx1RzJ5WHRFYUs4ME0yLU1QTlR1ZXdKLWpiRENlaW8tX2pJSUlFcWd0QjBIeUp6X1pJelE1UHRmeWhiWExzTGxmOVN6Si15b2VpNjhUOS14UFBIcUh2QVUtWW1URQ?oc=5>

## RISKS

### Xylem (XYL) Shareholder Investigation: Revenue Forecast Springs a Leak as Project Delays Surface
- Summary: Shareholder probe reveals revenue forecast leak and project delays, raising concerns about future performance.
- Date: 2026-11-09 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi0gFBVV95cUxQT0lVaEs0X2NjZThpZXB5OWlDQjl4anZySFlhdE1tMzRUUHFndldaZlBiNEhMdDZ3VVdoaFluRVprUlNvUWdQZnpMekZ6dUZoc3dwT0p0MzQ1OWtqY2RfUHJrTDRJSHlYOEJnZ01DRThQRnhCQ3VKSXhaVzlYUENGU1pad18zQ3NsM1BQZTJQTG40TEIzbHlWdnhzQk1TUWxYc2NQbTlHV3h5MHZpdXBiSGR5Q3JzN0NSMmtETm1VX3RYa3c5UEdEcXlVakh6MnVfN3c?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **XYL** | **22.01** | **2.23** | **12.89** | **-3.00** | **22,763,751,424.00 USD** | **-33.48** |
| AOS | 18.21 | 4.80 | 11.76 | -0.20 | 8,758,247,424.00 USD | 0.65 |
| PH | 32.86 | 7.55 | 23.05 | 17.90 | 120,622,931,968.00 USD | 14.04 |
| DOV | 24.85 | 3.71 | 15.26 | 7.50 | 28,327,976,960.00 USD | 19.31 |

Peers fetched as_of: 2026-11-09; XYL reuses existing data (market data as_of: 2026-11-09); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-27
- Next expected earnings: 2027-02-09 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-09

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
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

- https://news.google.com/rss/articles/CBMinAFBVV95cUxQTktwcmlkNldqRU1GS0wydEZGSzVIX0Zra0tocG5WVTJ6am9HR0hYenQzSGhudWJ0djFBSmFZNE1QOG54OC1UQm5vUlo2eWgxMWRrQTRQRURDbHZpT2pTWkRmaEpRcHlrUEp1LUY0ck1aY3JfN1ZwUHJzaEdtN1NPNWhobEcyY3FUMERwVWVWSFoyR085czZaQnd0bXU?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxOc3FvTWRlclJrWTcyQm92QU5VbVEtaUF5bzJvTjZleF9WYmhlMkR4OW1CSFJEOUE1ZEpBdHgyY0dtbGp6bk9wSXdGQTRQNVdmRnpxcnBJUWJuZkJaMjNzODJpbS0tNkl6WThiMDB1ZjlULXJPSWx0NGtaVDAzR1p0dnY5OGQ4MzQ0bzJlUExmOVZiTUpZZTVZMmFjU3E0aTctV2wzTlF3S1FUdlhIeUEtUm9qc1bSAboBQVVfeXFMTTRwbmxyeDYzRzVqUHBaenRNVzktTjdhbnY3bkN1VzVKaVk3cFp0WmZaY25tNF9hMm9zd0thZHBRNFdMTDhybU9SNjRsa2FpWTJpU2ZxYW1QS3draV9aVmtHbEpTd0dzTUtkOXQyb3YzZGlVZXg5OVEwS3kwZEctejlscnlLWDd0OERBWk92Yi1ycy1nLUxyWUd4T2c5WnctQUdxT2pJVzEwdTVqYkFmSnQzX21ObzdIVnd3?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxPMkhlSkExRU0yN0NoM1k4cUM5RnNiaDdYLUFJazRUbUlqWE9BYWZhelFiVHhORGgxUjlRZWwxaTR2R1oyVDlDT3RRNjVNVWZxX3BtcXYySHBFVV93MDltMnc5WUJ5bkVfUVd6QXdjcE1VejlneEVVUWs5Q2pNcnZaWVkxQlVNbGhPTXY2QTdtYmdocUkwZjg5UWdjam9UT2FWY1VQamNwWW5sZUplYnc?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxPbHBjNnVRUHV4RG9lWWVVTDV3cDd5R2R3dHp2NmhFSzlxWi1ZeHBkWmZTcWZtR2hESTBQUTBtVE9BOVRQLThqYVhmSnFEUnpHdERKYVh1ZUxNS0xxSDI0WFp5VDN6emk2Z2ZRaWxNUkZOZHJMM20xU2pXWHdfNWlRc29qZjZFUVNNeHNFQXBvaDNKT2x2dkhPRi1RV3JCdDVWbTQxSFlYUHJYV00?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxPY192UzVvLWN1YkIwT2REckRVYmowQ3VoNjVHWDZ2Uk1WbkxKbi12eGJRM3JZZXBGWkI2QWJha3diV1B1UGlNUXpWUW1PeXZKa3dXdEdEclExWlVfeHpPdkxSZUFhdkY4MnlnbGlOVUdrWi1CNExvUjRkVTdWSHMwX3BrbTZNRkhacGhfYWFncHBKdjlHLXk4YXFLWEtxcVNHT2pJajFCSHdWTU9UZGtITm9iREo3X0ZhTzdUWG4zQ1E?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxOeWJDN3lLa3UydmZqR1ZxZC1XMHF4TTc5WHNzS2t1SUJTMFBLVWlRdl8xTmNiQjl0WlozN1NiRDdXV3FxT2k4SnhvWHdfS0h1RnNrRVo3YkxrMFRBaHdyMDVkdmhXYzdLQkIyZlNHczFUd2ZwUlVSbjJNMVlvOVctaVJEYlR4MlJnT3VYLVIyRERfeF9uUlFhTzNvMHBvWkRTczRFc3BzSVZHRnhGVTlaY3JJQjE?oc=5
- https://news.google.com/rss/articles/CBMi0gFBVV95cUxORUhUV0VFUDRBZFNyQjZJWnJTUzhQUEdCVlVvTzl0TDNkVGlRbXo1TVRpMzFSV0xQdzI3ZXRxNzd3dGhNY1RoQkdUNFExWHFDcWN6WU5aUGlJYnYzU19aa3ItS3dEazZHUzhYc0otSDdvd292OVp0ek1RdXp0MG9FNEgydnZBY1NsQkdxdXhoM2dpV0Znb2FiSmRRN3dqN21yYUtqM2JZZUxOVEpuTDY1eTRPWVBjM29SSV9wekR6Q2Vua1N4SmVRSXJIamhiZGkwbVE?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxPeW1DR2lYY3p5Zk1wemFBOWFzOF9fTWZtZk92NVNDSjdUbXNzTGRib3A3VmtobC1GRnFGUUZFQWNySVlCUnpGT0laYWdVUGtEU2N0ZEpsc1JFRWpXc0Z2ZXU3NWx1RzJ5WHRFYUs4ME0yLU1QTlR1ZXdKLWpiRENlaW8tX2pJSUlFcWd0QjBIeUp6X1pJelE1UHRmeWhiWExzTGxmOVN6Si15b2VpNjhUOS14UFBIcUh2QVUtWW1URQ?oc=5
- https://news.google.com/rss/articles/CBMi0gFBVV95cUxQT0lVaEs0X2NjZThpZXB5OWlDQjl4anZySFlhdE1tMzRUUHFndldaZlBiNEhMdDZ3VVdoaFluRVprUlNvUWdQZnpMekZ6dUZoc3dwT0p0MzQ1OWtqY2RfUHJrTDRJSHlYOEJnZ01DRThQRnhCQ3VKSXhaVzlYUENGU1pad18zQ3NsM1BQZTJQTG40TEIzbHlWdnhzQk1TUWxYc2NQbTlHV3h5MHZpdXBiSGR5Q3JzN0NSMmtETm1VX3RYa3c5UEdEcXlVakh6MnVfN3c?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
