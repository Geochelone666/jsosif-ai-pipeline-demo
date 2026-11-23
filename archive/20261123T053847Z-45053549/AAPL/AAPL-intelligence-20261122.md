# AAPL Intelligence Report

- ticker: **AAPL**
- Report as_of: **2026-11-22**
- Market data as_of: **2026-11-20**
- Quant sources: https://finance.yahoo.com/quote/AAPL/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AAPL/key-statistics/
- AI analysis snapshot as_of: **2026-11-22**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-23T05:51:49.804405+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 3, 'ai': 10, 'unknown': 0, 'irrelevant': 12})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **12** exact headline/source/date matches; prior report **20261122T045655Z-f5ef568d/AAPL** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 13 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 28.0%; oldest publication 2026-11-16

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 342.5600 |
| Return 1D (%) | -1.9043 |
| Return 1W (%) | -3.8482 |
| Return 1M (%) | 0.9780 |
| Return YTD (%) | 26.4450 |
| Return 1Y (%) | 29.1093 |
| Annualized volatility (%) | 24.9651 |
| Beta vs SPY | 0.6069 |
| Max drawdown (%) | -13.7985 |
| Sharpe (rf=0) | 1.1527 |
| Downside deviation (rf=0, %) | 16.9835 |
| Sortino (rf=0) | 1.6944 |
| Historical VaR 95% (1D, %) | 2.0034 |
| Historical ES 95% (1D, %) | 3.4742 |
| Correlation vs SPY | 0.3475 |
| Tracking error vs SPY (%) | 24.0741 |
| P/E (trailing) | 38.15 |
| P/B | 44.41 |
| EV/EBITDA | 29.25 |
| Revenue growth (%) | 11.70 |
| Forward P/E (estimate) | 32.40 |
| Gross margin (%) | 48.79 |
| Operating margin (%) | 33.01 |
| Return on equity (%) | 142.26 |
| Free cash flow yield (%) | 2.12 |
| MA50 | 341.5850 |
| Close vs MA50 (%) | 0.2854 |
| MA200 | 302.7858 |
| Close vs MA200 (%) | 13.1361 |
| RSI (14, Wilder) | 46.5890 |
| MACD (12,26) | 2.7432 |
| MACD signal (9) | 3.4789 |
| MACD histogram | -0.7357 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AAPL': 287, 'SPY': 287}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 342.5600 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.9043 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -3.8482 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 0.9780 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 26.4450 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 29.1093 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 24.9651 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 16.9835 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.6944 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.0034 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.4742 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.3475 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 24.0741 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.6069 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -13.7985 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.1527 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 32.4003 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 48.7860 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 33.0100 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 142.2570 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.1224 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 38.1470 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 46.5890 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.7357 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 0.2854 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 13.1361 -> Clearly above the moving-average trend level.

## TAILWINDS

### AAPL Stock Posted Best Week In 4 Months Amid Nvidia Disruption: Apple Reportedly Plans Smart Glasses To Rival Meta Next Year
- Summary: Apple plans smart glasses to compete with Meta, boosting product prospects.
- Date: 2026-11-16 | Impact: high | Horizon: long | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxPaTZ2ZWQ2QTBxMk1iWTJ4ZXBGc3hpUDRHMDVVdFdMaGtkWVVkcEtzM2djWFpZQ1ZxTnYtUHFhMHFIbjFSSjhPSXVDWWsxdXlvQzQ1RDliaVNNUzR5QzZLWEl0UW9ROGx5RnZVdko4LWYzbWNqWEJORkJDTEVmY3ZObDgyaHNmZzRHaWpQN2ZCaDFQM05ja21J?oc=5>

## HEADWINDS

### Apple (NASDAQ:AAPL) Stock Price Down 1.8% Following Insider Selling
- Summary: Apple (NASDAQ:AAPL) Stock Price Down 1.8% Following Insider Selling
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxPcUhuY1AtZTk3M0tUV21lYS1xS3lOMWtBWVRpTzJmYldNdDZubVhKZVNHcW9OalhlcXlIU1p6Vmg0NFpHd2FrR3ZDa0JUcnNadC1GNkJWZ1VmYmNzNVRHd2dNUGw1LWR0MzRUbzBXWnpjc2ZBaktZazJhaU1wUDc1R3ZTUjJiWlhEMUlTUVo5UG9LaXF0Y0JoQU8yS2Z3a09GOEVsN014Mmk1MkpReDlEVnpVUE5oUGxqcVZlUG5zc24?oc=5>

### Apple (AAPL) Stock Could Be 33% Overvalued On Fresh Service Outage Concerns
- Summary: Service outage worries may depress Apple’s valuation, signaling potential short‑term downside.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxPcW1UV2NiYVZ2ZmxTbDc1dVoxblRuVWpUSlFHdWlaRXhzMmFUWFoxRHY2c2hMTEFyNmdrbUwwTHU0YUswM1VDMF9XZGVpbUhEaHRhSEwzdXZxaFFVVlNUWEJhNU5MTXRvY2tVd1FVbldtX0JfYUlyRG94MTh6WnEyWHF6Nl9mRkszMGJ4SW5mOWZDOTBK?oc=5>

### How Investors May Respond To Apple (AAPL) Service Outages
- Summary: Service outages could negatively affect investor sentiment.
- Date: 2026-11-19 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxOXy02WGZ5d1JKRjdEUFlEZm92TmEwYy1Kd2F6X0lobUIyd0sxSFJrNlhGR3hOMkxma2ZpQmQ0V3RaUXVnUFNGR3dLc3RzTHFCcEJOaXNsRlVCS2dxZWVwOWExbUFiQi1pYnFuNGZlTzExLWZmNXd2WlJHWkV4WWdtLUFleE5iWTdMeW9wb1d5RTBjbHRXblhqVDY5WkpTUQ?oc=5>

### Apple’s Haven Status Makes It One of Priciest Stocks in Market
- Summary: Apple’s high valuation may deter investors.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxOWFdXODZmaFdpSjdGdFF5Mm5IQVRyZTJUczJ5R08zSGttalFxSFgtdTQxVENCajRVYlJWOG1hUmcwRHpmcHBENVBDNU1NMDgzbDdDZEtLbE5uT0N6bHdnNGdaOUZxbV9ad3FXSVUyVUt1Mld2S0NYaHpDNG1EaUlfSDFJZFZ0R1hmSDl3dmczRkc2RW4xM1VKdHZCY3FWWUJpUkswM2hsRGtCR1VmdWRuMFRaQQ?oc=5>

### ANT, META Stock Slip After-Hours Amid Reports That Apple Is Working On Its Own AI Agent
- Summary: Apple's AI agent development may weigh on short-term sentiment as related stocks slip.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi5AFBVV95cUxNVURFWFJWdFV5MDVOWDBtSm13SjBXZmlCVm1HUWRVY01VdWtub2wzc0o1ZDBnMEo3LUYxbW1wNm00d1BCMzZVaVJxVzlrNWRtM3JHU0tZT3ozQTNUdjRtMFY0Y3IxYUc3akJ6YXFMTFZSaXhvc0FwazFEV0FOUWx6Q2ZuQzdtSThKT2xXTTZ0U00zaFZld3BRbHI0UjdfSVdIVE84SWU0c0lzX2gtNndJcjYxSUlOS214SlhNS1MtbHctTUZ2RHd0eTY0c2tPYzRXTENudnJfcmJPWDZaNVp4LXRVaVY?oc=5>

## CATALYSTS

### Apple Nears a Rare Long-Term DRAM Supply Deal With Samsung Electronics. What This Means for AAPL Stock.
- Summary: Apple Nears a Rare Long-Term DRAM Supply Deal With Samsung Electronics. What This Means for AAPL Stock.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi3gFBVV95cUxOTVIzNGkwNkdPZFJwV1dKdkFrSTNGWUtqMlNObWFiYk1WUU0wQm51RVZvQTVGVkJxSDJfVHY3bnJKdFFtLW9GcGtjUWI4R3BTSkl4MGNqdk9RSnZzejZBdE5YMWE5QkVyVHBCeWFseXdYTEhhdUUyRWpxS2JxM0tBbDltazFfaDlXT0tkbklqZWhtR01CTjVYeDJOc2VHSjdaS1VBREVSdXZMU191UmtudXg0Y3hRV2dYNWFNQUZkMVJ0U2hISExQdU9MbV9KWWJGUzdneE5TRHFPUUVVbXc?oc=5>

### Apple (AAPL) Grows at 12% and Trades at 37 Times Earnings. Is It Worth It?
- Summary: Apple (AAPL) Grows at 12% and Trades at 37 Times Earnings. Is It Worth It?
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxQT1hOSDdlQ05nblBRMDlCSGdUZ010Sm9oZUV0bjdtRFBUeWJFdEt1aXg2bmxiMllXSWJ1U050ZDFoX3RVa0s5eTNOWkRpMjJJR0w4THRCa1dNNm9GY0xBWXdnOHZrYldvdmh0dDY3OFhHa0cwWndrM1FiVGJLQnJPMW9JVW5acG1YeUdLc2pEd0ZYQ1lmQ2c?oc=5>

### Apple Is Now Worth Over $5 Trillion Without Betting Big on AI Data Centers. AAPL Stock Now Trades Near Wall Street’s Targets.
- Summary: Apple’s market cap surpasses $5 trillion; stock trades near analyst targets, indicating bullish sentiment.
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi-AFBVV95cUxNRXVwb1laS1Btbm1iTjFsMEg3OGRxd2I4MDBheXBhTmpLTnBpLVpFaGZCdmVabEZnS3FWREh5WDAxcW1KVGpOVFB5NzltWnAyakRibjhhckdQM3BpcVRtSTdHckRoY2RtRFdmZG82T3NlY0xkLS1MczU4b29KQXFXVGdXSjNHMUxBT0NoZmRSb0tuYTdCOEZYWWhGRW8xbUVOTlhkZjJFVGhOUEVaQVptUW05eW1UalZBeG9wRUhLVXljWlVFU0JLc0dkVm1aZjM5OHJEWlVuUmFUd1FJNW1Rdi1UdDN5YlRER0JMZnVpaGNvSVUyRUx5ZA?oc=5>

### AAPL Stock Alert: What to Know as Apple Develops AI Agent to Compete With Muse
- Summary: Apple’s new AI agent launch could boost product portfolio and market share.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxQekFPM3ZncUc5OWU5R3NERDJHalhFbE9WNURJNUNmc3RnelpCTW9OcHNHcXZuTDMxVGtMbWkwUnM3WDBCSHVYalU4dnhzWFY4NW10dGJROGVEOE5KNXNIUjJUY1ltN1A3SHJTZE9XS0ZUQTNUT0c5S1BVUzJGRDlzVlVuZkV4YUNNTHFxZVhmai05QUcwdmc?oc=5>

### Apple Stock Shows Strength Now, and a Key Catalyst Is Brewing in June 2027
- Summary: Apple’s stock is strong, with a future catalyst expected in June 2027, indicating potential upside.
- Date: 2026-11-18 | Impact: medium | Horizon: long | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxQX3p5TThXSGxzdkt1b0Q5amlfQXcwU3BKVkUxd1l5cmRGWEMxb1ZualpoM0NvOE9XWWZtQlN2WmZ6cVVzQUQ2aGZHVVVmQV9kZ21xWXVoQUEzZjVaS1oyQldhbXRRTm42RGtHMlhuNy1ZTDVqRTc1dld1anBXclNYQm0xNXJuZ1Vvdl83RHRJU0hTdS0ycktwNGhObw?oc=5>

### Apple's Rare Samsung Memory Plan Could Solve One Problem and Create Another
- Summary: Apple partners with Samsung for memory, potentially addressing supply issues but raising new challenges.
- Date: 2026-11-20 | Impact: medium | Horizon: medium | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxOcHgxQXUxOTRLWU9lcUV4SHB1OXZXOEctM1hEci1wajgwdnhlaEtDWjFDeFdMR2dMeDN4T2hlNnpWT3Q2YVpqSHZuaW9BRUlJRXVhOGdpcmVVMExJdzhoVW1lWFh0V0NrcnJTeDV6ZW9PU3RIOFo3TlpMcU0wRGd6V19DWDlOZ1FwdHFDR0IxVjRGNmlJX0tRVGF5aXZoOElCakZuN1NTQklaVDNtWlJyYQ?oc=5>

## RISKS

### Apple: The Hidden Risk Behind My Downgrade (NASDAQ:AAPL)
- Summary: Analyst downgrade highlights hidden risks to Apple’s outlook.
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxNaG1BZDFsdExZcmFBTHcwYkZGMElvdlhwMk1kRVl0RUlOTk90REhiRVJubWI0RlFqVWYyYWYxTUk1UjVkZzFtZGNyMXd6U0FuT0FTY2pPSDlVN3JCODFrSTFjZjEzSFY5TlhoenhTcDZ5ckVjWllwXzlNV0k1dGlwOTRCbE1RVWxmRFE?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AAPL** | **38.15** | **44.41** | **29.25** | **11.70** | **4,978,144,444,416.00 USD** | **29.11** |
| MSFT | 25.29 | 7.65 | 17.83 | 18.80 | 3,598,139,523,072.00 USD | 2.11 |
| GOOGL | 13.85 | 4.95 | 17.06 | 24.70 | 3,261,475,323,904.00 USD | -8.11 |
| SONY | 20.37 | 2.95 | 0.30 | 10.30 | 159,053,053,952.00 USD | -1.66 |

Peers fetched as_of: 2026-11-22; AAPL reuses existing data (market data as_of: 2026-11-20); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-02
- Next expected earnings: 2027-01-28 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-22

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-K
- Filing date: 2026-11-03
- Revenue (latest available single quarter): 62,900,000,000.00 USD; period 2018-07-01/2018-09-29; fiscal year/reporting period 2018/FY
- Net income (latest available single quarter): 29,789,000,000.00 USD; period 2026-03-29/2026-06-27; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/320193/000032019326000026/aapl-20260926.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMilwFBVV95cUxPaTZ2ZWQ2QTBxMk1iWTJ4ZXBGc3hpUDRHMDVVdFdMaGtkWVVkcEtzM2djWFpZQ1ZxTnYtUHFhMHFIbjFSSjhPSXVDWWsxdXlvQzQ1RDliaVNNUzR5QzZLWEl0UW9ROGx5RnZVdko4LWYzbWNqWEJORkJDTEVmY3ZObDgyaHNmZzRHaWpQN2ZCaDFQM05ja21J?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxPcUhuY1AtZTk3M0tUV21lYS1xS3lOMWtBWVRpTzJmYldNdDZubVhKZVNHcW9OalhlcXlIU1p6Vmg0NFpHd2FrR3ZDa0JUcnNadC1GNkJWZ1VmYmNzNVRHd2dNUGw1LWR0MzRUbzBXWnpjc2ZBaktZazJhaU1wUDc1R3ZTUjJiWlhEMUlTUVo5UG9LaXF0Y0JoQU8yS2Z3a09GOEVsN014Mmk1MkpReDlEVnpVUE5oUGxqcVZlUG5zc24?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxPcW1UV2NiYVZ2ZmxTbDc1dVoxblRuVWpUSlFHdWlaRXhzMmFUWFoxRHY2c2hMTEFyNmdrbUwwTHU0YUswM1VDMF9XZGVpbUhEaHRhSEwzdXZxaFFVVlNUWEJhNU5MTXRvY2tVd1FVbldtX0JfYUlyRG94MTh6WnEyWHF6Nl9mRkszMGJ4SW5mOWZDOTBK?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxOXy02WGZ5d1JKRjdEUFlEZm92TmEwYy1Kd2F6X0lobUIyd0sxSFJrNlhGR3hOMkxma2ZpQmQ0V3RaUXVnUFNGR3dLc3RzTHFCcEJOaXNsRlVCS2dxZWVwOWExbUFiQi1pYnFuNGZlTzExLWZmNXd2WlJHWkV4WWdtLUFleE5iWTdMeW9wb1d5RTBjbHRXblhqVDY5WkpTUQ?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxOWFdXODZmaFdpSjdGdFF5Mm5IQVRyZTJUczJ5R08zSGttalFxSFgtdTQxVENCajRVYlJWOG1hUmcwRHpmcHBENVBDNU1NMDgzbDdDZEtLbE5uT0N6bHdnNGdaOUZxbV9ad3FXSVUyVUt1Mld2S0NYaHpDNG1EaUlfSDFJZFZ0R1hmSDl3dmczRkc2RW4xM1VKdHZCY3FWWUJpUkswM2hsRGtCR1VmdWRuMFRaQQ?oc=5
- https://news.google.com/rss/articles/CBMi5AFBVV95cUxNVURFWFJWdFV5MDVOWDBtSm13SjBXZmlCVm1HUWRVY01VdWtub2wzc0o1ZDBnMEo3LUYxbW1wNm00d1BCMzZVaVJxVzlrNWRtM3JHU0tZT3ozQTNUdjRtMFY0Y3IxYUc3akJ6YXFMTFZSaXhvc0FwazFEV0FOUWx6Q2ZuQzdtSThKT2xXTTZ0U00zaFZld3BRbHI0UjdfSVdIVE84SWU0c0lzX2gtNndJcjYxSUlOS214SlhNS1MtbHctTUZ2RHd0eTY0c2tPYzRXTENudnJfcmJPWDZaNVp4LXRVaVY?oc=5
- https://news.google.com/rss/articles/CBMi3gFBVV95cUxOTVIzNGkwNkdPZFJwV1dKdkFrSTNGWUtqMlNObWFiYk1WUU0wQm51RVZvQTVGVkJxSDJfVHY3bnJKdFFtLW9GcGtjUWI4R3BTSkl4MGNqdk9RSnZzejZBdE5YMWE5QkVyVHBCeWFseXdYTEhhdUUyRWpxS2JxM0tBbDltazFfaDlXT0tkbklqZWhtR01CTjVYeDJOc2VHSjdaS1VBREVSdXZMU191UmtudXg0Y3hRV2dYNWFNQUZkMVJ0U2hISExQdU9MbV9KWWJGUzdneE5TRHFPUUVVbXc?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxQT1hOSDdlQ05nblBRMDlCSGdUZ010Sm9oZUV0bjdtRFBUeWJFdEt1aXg2bmxiMllXSWJ1U050ZDFoX3RVa0s5eTNOWkRpMjJJR0w4THRCa1dNNm9GY0xBWXdnOHZrYldvdmh0dDY3OFhHa0cwWndrM1FiVGJLQnJPMW9JVW5acG1YeUdLc2pEd0ZYQ1lmQ2c?oc=5
- https://news.google.com/rss/articles/CBMi-AFBVV95cUxNRXVwb1laS1Btbm1iTjFsMEg3OGRxd2I4MDBheXBhTmpLTnBpLVpFaGZCdmVabEZnS3FWREh5WDAxcW1KVGpOVFB5NzltWnAyakRibjhhckdQM3BpcVRtSTdHckRoY2RtRFdmZG82T3NlY0xkLS1MczU4b29KQXFXVGdXSjNHMUxBT0NoZmRSb0tuYTdCOEZYWWhGRW8xbUVOTlhkZjJFVGhOUEVaQVptUW05eW1UalZBeG9wRUhLVXljWlVFU0JLc0dkVm1aZjM5OHJEWlVuUmFUd1FJNW1Rdi1UdDN5YlRER0JMZnVpaGNvSVUyRUx5ZA?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxQekFPM3ZncUc5OWU5R3NERDJHalhFbE9WNURJNUNmc3RnelpCTW9OcHNHcXZuTDMxVGtMbWkwUnM3WDBCSHVYalU4dnhzWFY4NW10dGJROGVEOE5KNXNIUjJUY1ltN1A3SHJTZE9XS0ZUQTNUT0c5S1BVUzJGRDlzVlVuZkV4YUNNTHFxZVhmai05QUcwdmc?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxQX3p5TThXSGxzdkt1b0Q5amlfQXcwU3BKVkUxd1l5cmRGWEMxb1ZualpoM0NvOE9XWWZtQlN2WmZ6cVVzQUQ2aGZHVVVmQV9kZ21xWXVoQUEzZjVaS1oyQldhbXRRTm42RGtHMlhuNy1ZTDVqRTc1dld1anBXclNYQm0xNXJuZ1Vvdl83RHRJU0hTdS0ycktwNGhObw?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxOcHgxQXUxOTRLWU9lcUV4SHB1OXZXOEctM1hEci1wajgwdnhlaEtDWjFDeFdMR2dMeDN4T2hlNnpWT3Q2YVpqSHZuaW9BRUlJRXVhOGdpcmVVMExJdzhoVW1lWFh0V0NrcnJTeDV6ZW9PU3RIOFo3TlpMcU0wRGd6V19DWDlOZ1FwdHFDR0IxVjRGNmlJX0tRVGF5aXZoOElCakZuN1NTQklaVDNtWlJyYQ?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxNaG1BZDFsdExZcmFBTHcwYkZGMElvdlhwMk1kRVl0RUlOTk90REhiRVJubWI0RlFqVWYyYWYxTUk1UjVkZzFtZGNyMXd6U0FuT0FTY2pPSDlVN3JCODFrSTFjZjEzSFY5TlhoenhTcDZ5ckVjWllwXzlNV0k1dGlwOTRCbE1RVWxmRFE?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
