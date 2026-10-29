# TSM Intelligence Report

- ticker: **TSM**
- Report as_of: **2026-10-28**
- Market data as_of: **2026-10-28**
- Quant sources: https://finance.yahoo.com/quote/TSM/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/TSM/key-statistics/
- AI analysis snapshot as_of: **2026-10-28**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-29T02:05:42.160455+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 21, 'rule': 3, 'ai': 6, 'unknown': 0, 'irrelevant': 12})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **7** exact headline/source/date matches; prior report **20261028T015717Z-533e470c/TSM** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'low_uncalibrated_model_confidence': 1, 'short_term_price_move_in_structural_risks': 1}
- RSS source audit (metadata only, not article fact-checking): 21 unique headlines; 6 named publishers; 4 exact duplicates; 21 HTTPS source links; largest publisher share 33.33%; oldest publication 2026-10-22

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 439.5100 |
| Return 1D (%) | 0.6043 |
| Return 1W (%) | 1.7643 |
| Return 1M (%) | -2.9522 |
| Return YTD (%) | 45.7652 |
| Return 1Y (%) | 47.3026 |
| Annualized volatility (%) | 39.2151 |
| Beta vs SPY | 2.1432 |
| Max drawdown (%) | -21.5466 |
| Sharpe (rf=0) | 1.1874 |
| Downside deviation (rf=0, %) | 26.0365 |
| Sortino (rf=0) | 1.7884 |
| Historical VaR 95% (1D, %) | 4.1383 |
| Historical ES 95% (1D, %) | 5.1216 |
| Correlation vs SPY | 0.6942 |
| Tracking error vs SPY (%) | 31.7422 |
| P/E (trailing) | 28.32 |
| P/B | 83.88 |
| EV/EBITDA | 4.16 |
| Revenue growth (%) | 50.90 |
| Forward P/E (estimate) | 18.79 |
| Gross margin (%) | 65.85 |
| Operating margin (%) | 58.66 |
| Return on equity (%) | 41.85 |
| Free cash flow yield (%) | N/A |
| MA50 | 434.2932 |
| Close vs MA50 (%) | 1.2012 |
| MA200 | 397.7253 |
| Close vs MA200 (%) | 10.5059 |
| RSI (14, Wilder) | 51.8936 |
| MACD (12,26) | -3.8264 |
| MACD signal (9) | -2.8925 |
| MACD histogram | -0.9339 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'TSM': 270, 'SPY': 270}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 439.5100 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.6043 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 1.7643 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -2.9522 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 45.7652 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 47.3026 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 39.2151 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 26.0365 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.7884 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.1383 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.1216 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6942 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 31.7422 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 2.1432 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -21.5466 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.1874 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 18.7943 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 65.8460 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 58.6550 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 41.8550 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 28.3189 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 51.8936 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.9339 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 1.2012 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 10.5059 -> Clearly above the moving-average trend level.

## TAILWINDS

### TSMC Gains 3% on Reported 20% Price Hike for AI Chip Packaging
- Summary: TSMC Gains 3% on Reported 20% Price Hike for AI Chip Packaging
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxNN3UtckREdlJ1c3JCRHdVNURWNVNsOW1TaVYwa1JIdk9tbEV5YTk4YmRoZDJIMkFGcXhWeTRaZ2RHT2JzWEZaeWRkMEJvRk41WW0xNGVwa3RpWVB3Y09vRVdPbHRQRms1UHAtaUpWS3cxNHAwNnJzdzVXWjJ2WFNPQWVHMHhOa2VUTWhzYnUyRXRaUQ?oc=5>

## HEADWINDS

### Taiwan Semiconductor (TSMC) Posted Record Profit and the Stock Still Fell. Here's What the Market Is Worried About.
- Summary: Taiwan Semiconductor (TSMC) Posted Record Profit and the Stock Still Fell. Here's What the Market Is Worried About.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxPUC14clR2aXF2cVFkUGpJWjYzNEFKYTlWQVBySmdMdUY4Y3QtQmNXbVlaVjVyWEpuNjNzbXlCRER4WVRyeFFwWGFHcXJPOFA3UGc5R1pNb05CX3V6ZkM4VWRibmdaRG9GN3NXbVBDTkZYZ1J2eUJSSkd5OWlza05OSnQ4TUE0VTNyOXhNTGtiSkRxd05xTmhB?oc=5>

### Taiwan Semiconductor Manufacturing (TSM) Stock Looks Pricey Against Cash Flow
- Summary: Valuation concerns relative to cash flow.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxORldEaFpNSnljQTZVWGtRUmV3X0R2QTZQTE9pNm0yWDlremFDNV85cHVhRnlZTy02c2Zkd0dsTTE0Zkx4LWJibjZVR0RHWlhZdy1WcHRVZ2dHQlpHOWxGWEVHUnlJRU5mcFVhU1FnWXk5TzB4ZFdMYjkzRDctYjJ0d0tYeGxfbHlBU1ducHNRZEFOYkwzZy1TTXRGNjRkcDlZZTUwcDNLdlZXSGFsb3c?oc=5>

## CATALYSTS

### Taiwan Semiconductor Manufacturing Company Limited 2026 Q3 - Results - Earnings Call Presentation
- Summary: Taiwan Semiconductor Manufacturing Company Limited 2026 Q3 - Results - Earnings Call Presentation
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizwFBVV95cUxQcUd6a0dTbklKcC1hSlZQQXp5VnRWZUszUE9iaEhtcWJ4eFN0SHItNG0tV2tKVnZqSjZCM2N2c0dLMVQyQURGR05QV0dBdkpGWm9DcUNVRENHZWEzUkg4UVZfckpoTGZxLUVYYk1CTnUzWXhTcTc1YllhbFhaeW1FT2VLdE43cTBwLTFOcEl4Y1d0NmFwY0NEZEd3bFh1cktLTkJXd0VoTV9PSmVZbU1aM3M2RkNfVkMtbzJDWTFnUUF6SXJ6TjlNSjJRUE95YTQ?oc=5>

### TSMC: The Toll Road Of The AI Economy Is On Sale (NYSE:TSM)
- Summary: TSMC highlights its role in AI economy, suggesting growth potential.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxNMXNDRzVKSl9XSDFyUlRwRWctZzJFQVExcGZsZmhKZzVfUnRTYUtlUm5TTHZPR1dZakx3c2VEUjBtTWxGdjFoODB3RFFOVDE0Q1BKVGRpRW1hTzdxcHUxbjVkcUdLWGVfVWx1RVNCN3lWbjZOcGI2cUVlNHVwTWUwUVJ6OGlLcnp6RmV5WjBaRFhfUQ?oc=5>

### Why TSMC's Q3 2026 Results Highlight Pitfalls In The AI Hype (NYSE:TSM)
- Summary: TSMC’s upcoming Q3 2026 earnings may reveal challenges in AI demand, potentially affecting future revenue growth.
- Date: 2026-10-27 | Impact: medium | Horizon: long | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxQZEN1M1JmbHlBV3NidEFjN2xfTF9CazJKaTRUT0JJblVyZ3ZVcjNCNC1pdDFrSFFQcEFUOF9Lb1RtU0hnYUxwblQ5Y0tjSXlvZHlnVlZqaHdUZ1JCblZGRHZLT2xucHVVSElKOEtnSlVZaWpwZjRlTUw1Q2J3VUtfWFU1RWl5Y3ZSOUw5bmRJSndxcFVzMGZxQXpiZTJJdzlsNEE?oc=5>

### Beyond NVIDIA: Why TSMC Stock Looks Attractive After Q3 Earnings
- Summary: TSMC’s Q3 earnings boost investor confidence, making the stock appealing amid AI demand.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxPN3dtcjE1SGRUV2FldnUxb0syS2hXaGZaMG8yMFNQTmNIMXN1S29Da2VLbHZhYlRYM2FsWjFzek1hQ0FRME9VZFBrUmlCNUIxXzhVU28tRUhBOWFuN29pRmN4cExKMGxaM1JWRVV6OS1lamFpUXZlSngxQnhuYXJYY0ZMSFl1VG5TZnVYeE9oOTd1Z2h1Yk4yNXkzTVRwR211aEUxemRCT2U5emVsOHNNMGZsc3hrOVlxVVc4?oc=5>

### Nvidia, Chipmakers Face Higher Costs? TSMC Reportedly Plans Up To 20% Price Hike For Advanced Chip Packaging
- Summary: TSMC may raise advanced packaging prices by up to 20%, potentially increasing costs for Nvidia and other chipmakers.
- Date: 2026-10-27 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxPekpKYkZzMEpfQmFkR2wtNmttWjJJOWQ2SWFzdS1oa0dhbU5nU1NnVHhqaHhXX243RmZDUHBNX0Q5a3pUWlg5SnVNSFNVVVRHVWxiOHJrSmZEdmpnSVpmZjlCMlZrR25BOWhVTHBSYmxOY3ZSajRTb2xVWkpSRF9LS2lqOEp3UzBfNDRLdzE1b211R2Nqc3lnQ0tHS2c?oc=5>

## RISKS

### Taiwan Semiconductor raising prices could mean less competition from Intel: Wedbush (TSM:NYSE)
- Summary: TSMC’s price hike may reduce Intel competition but could affect margins.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxPeXJ1SWxyZ3Q0aUtiYVAwZHd5N1pKTVN5YjkweEhCMGNMbmNPNEhmRUJrQkNIb2Q2a3dXbUdVdUs2aGNBbEx5UVY0bEsyRzJiV3p1UTVqcjBzZ1pKZjRFVlVibzhnMGZPQzg5WXhmWk9HOXhkeGJhN2ZGVk05eklQdlJueTZBUEthRkcwdlNoYVFSX01NbWkyT0FnX0pRX05SU21scVh2eDRwSG8yR3RFWTBXSmxhSnRzRFpGTg?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **TSM** | **28.32** | **83.88** | **4.16** | **50.90** | **2,279,507,230,720.00 USD** | **47.30** |
| UMC | 19.01 | 3.45 | -0.32 | 17.00 | 47,198,838,784.00 USD | 151.00 |
| GFS | 36.60 | 2.14 | 12.46 | 5.80 | 25,702,574,080.00 USD | 33.64 |
| INTC | N/A | 5.50 | 30.78 | 25.40 | 504,981,618,688.00 USD | 130.03 |

Peers fetched as_of: 2026-10-28; TSM reuses existing data (market data as_of: 2026-10-28); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-15
- Next expected earnings: 2027-01-14 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-28

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

- https://news.google.com/rss/articles/CBMikgFBVV95cUxNN3UtckREdlJ1c3JCRHdVNURWNVNsOW1TaVYwa1JIdk9tbEV5YTk4YmRoZDJIMkFGcXhWeTRaZ2RHT2JzWEZaeWRkMEJvRk41WW0xNGVwa3RpWVB3Y09vRVdPbHRQRms1UHAtaUpWS3cxNHAwNnJzdzVXWjJ2WFNPQWVHMHhOa2VUTWhzYnUyRXRaUQ?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxPUC14clR2aXF2cVFkUGpJWjYzNEFKYTlWQVBySmdMdUY4Y3QtQmNXbVlaVjVyWEpuNjNzbXlCRER4WVRyeFFwWGFHcXJPOFA3UGc5R1pNb05CX3V6ZkM4VWRibmdaRG9GN3NXbVBDTkZYZ1J2eUJSSkd5OWlza05OSnQ4TUE0VTNyOXhNTGtiSkRxd05xTmhB?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxORldEaFpNSnljQTZVWGtRUmV3X0R2QTZQTE9pNm0yWDlremFDNV85cHVhRnlZTy02c2Zkd0dsTTE0Zkx4LWJibjZVR0RHWlhZdy1WcHRVZ2dHQlpHOWxGWEVHUnlJRU5mcFVhU1FnWXk5TzB4ZFdMYjkzRDctYjJ0d0tYeGxfbHlBU1ducHNRZEFOYkwzZy1TTXRGNjRkcDlZZTUwcDNLdlZXSGFsb3c?oc=5
- https://news.google.com/rss/articles/CBMizwFBVV95cUxQcUd6a0dTbklKcC1hSlZQQXp5VnRWZUszUE9iaEhtcWJ4eFN0SHItNG0tV2tKVnZqSjZCM2N2c0dLMVQyQURGR05QV0dBdkpGWm9DcUNVRENHZWEzUkg4UVZfckpoTGZxLUVYYk1CTnUzWXhTcTc1YllhbFhaeW1FT2VLdE43cTBwLTFOcEl4Y1d0NmFwY0NEZEd3bFh1cktLTkJXd0VoTV9PSmVZbU1aM3M2RkNfVkMtbzJDWTFnUUF6SXJ6TjlNSjJRUE95YTQ?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxNMXNDRzVKSl9XSDFyUlRwRWctZzJFQVExcGZsZmhKZzVfUnRTYUtlUm5TTHZPR1dZakx3c2VEUjBtTWxGdjFoODB3RFFOVDE0Q1BKVGRpRW1hTzdxcHUxbjVkcUdLWGVfVWx1RVNCN3lWbjZOcGI2cUVlNHVwTWUwUVJ6OGlLcnp6RmV5WjBaRFhfUQ?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxQZEN1M1JmbHlBV3NidEFjN2xfTF9CazJKaTRUT0JJblVyZ3ZVcjNCNC1pdDFrSFFQcEFUOF9Lb1RtU0hnYUxwblQ5Y0tjSXlvZHlnVlZqaHdUZ1JCblZGRHZLT2xucHVVSElKOEtnSlVZaWpwZjRlTUw1Q2J3VUtfWFU1RWl5Y3ZSOUw5bmRJSndxcFVzMGZxQXpiZTJJdzlsNEE?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxPN3dtcjE1SGRUV2FldnUxb0syS2hXaGZaMG8yMFNQTmNIMXN1S29Da2VLbHZhYlRYM2FsWjFzek1hQ0FRME9VZFBrUmlCNUIxXzhVU28tRUhBOWFuN29pRmN4cExKMGxaM1JWRVV6OS1lamFpUXZlSngxQnhuYXJYY0ZMSFl1VG5TZnVYeE9oOTd1Z2h1Yk4yNXkzTVRwR211aEUxemRCT2U5emVsOHNNMGZsc3hrOVlxVVc4?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxPekpKYkZzMEpfQmFkR2wtNmttWjJJOWQ2SWFzdS1oa0dhbU5nU1NnVHhqaHhXX243RmZDUHBNX0Q5a3pUWlg5SnVNSFNVVVRHVWxiOHJrSmZEdmpnSVpmZjlCMlZrR25BOWhVTHBSYmxOY3ZSajRTb2xVWkpSRF9LS2lqOEp3UzBfNDRLdzE1b211R2Nqc3lnQ0tHS2c?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxPeXJ1SWxyZ3Q0aUtiYVAwZHd5N1pKTVN5YjkweEhCMGNMbmNPNEhmRUJrQkNIb2Q2a3dXbUdVdUs2aGNBbEx5UVY0bEsyRzJiV3p1UTVqcjBzZ1pKZjRFVlVibzhnMGZPQzg5WXhmWk9HOXhkeGJhN2ZGVk05eklQdlJueTZBUEthRkcwdlNoYVFSX01NbWkyT0FnX0pRX05SU21scVh2eDRwSG8yR3RFWTBXSmxhSnRzRFpGTg?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
