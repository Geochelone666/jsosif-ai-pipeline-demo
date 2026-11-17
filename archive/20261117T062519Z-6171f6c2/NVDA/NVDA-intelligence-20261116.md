# NVDA Intelligence Report

- ticker: **NVDA**
- Report as_of: **2026-11-16**
- Market data as_of: **2026-11-16**
- Quant sources: https://finance.yahoo.com/quote/NVDA/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NVDA/key-statistics/
- AI analysis snapshot as_of: **2026-11-16**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-17T06:37:13.731458+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 6, 'ai': 8, 'unknown': 0, 'irrelevant': 10})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **4** exact headline/source/date matches; prior report **20261116T043911Z-b81cfeb4/NVDA** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **3**; {'directional_claim_without_event_type': 1, 'low_uncalibrated_model_confidence': 2}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 7 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 58.33%; oldest publication 2026-11-15

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 156.1400 |
| Return 1D (%) | -4.1204 |
| Return 1W (%) | -12.6098 |
| Return 1M (%) | -27.0817 |
| Return YTD (%) | -16.0829 |
| Return 1Y (%) | -17.6978 |
| Annualized volatility (%) | 38.8718 |
| Beta vs SPY | 1.7831 |
| Max drawdown (%) | -34.7350 |
| Sharpe (rf=0) | -0.2618 |
| Downside deviation (rf=0, %) | 28.0377 |
| Sortino (rf=0) | -0.3630 |
| Historical VaR 95% (1D, %) | 4.1960 |
| Historical ES 95% (1D, %) | 5.1243 |
| Correlation vs SPY | 0.6315 |
| Tracking error vs SPY (%) | 32.0100 |
| P/E (trailing) | 19.74 |
| P/B | 16.47 |
| EV/EBITDA | 18.58 |
| Revenue growth (%) | 105.90 |
| Forward P/E (estimate) | 9.86 |
| Gross margin (%) | 74.67 |
| Operating margin (%) | 65.21 |
| Return on equity (%) | 117.21 |
| Free cash flow yield (%) | 1.11 |
| MA50 | 213.1528 |
| Close vs MA50 (%) | -26.7474 |
| MA200 | 203.7475 |
| Close vs MA200 (%) | -23.3659 |
| RSI (14, Wilder) | 22.7165 |
| MACD (12,26) | -15.3735 |
| MACD signal (9) | -11.1552 |
| MACD histogram | -4.2184 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NVDA': 283, 'SPY': 283}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 156.1400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -4.1204 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -12.6098 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -27.0817 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -16.0829 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -17.6978 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 38.8718 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 28.0377 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.3630 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.1960 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.1243 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6315 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 32.0100 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.7831 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -34.7350 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.2618 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 9.8554 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 74.6740 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 65.2140 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 117.2110 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.1089 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 19.7396 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 22.7165 -> Oversold momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -4.2184 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -26.7474 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -23.3659 -> Clearly below the moving-average trend level.

## TAILWINDS

### Nvidia Stock Has a 20% Rebound in Sight—If Bulls Can Clear a Hurdle
- Summary: Positive market movement with a 20% rebound potential if key hurdle cleared.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxPVHlZMXdwbHJLTmdVa0lYcE8xRG5pOXlNckticy1NeWhxZWJZZFVaeERFT2wzdzMzS3dZMjVTMUhpZzNEOXgtSkwzdElrd3lCdDctemVDeEJfX2tWVF9wMVNIMHNXZVo1d3l0OFFWazhCQ0xCMFlMd1ZrRkY5RENONFYtYTVoclFHMWxfQTNpVENrbzY5dnpzMThB?oc=5>

## HEADWINDS

### Nvidia stock falls as Jensen Huang reportedly weighs CEO comeback, Musk backs return
- Summary: Nvidia stock falls as Jensen Huang reportedly weighs CEO comeback, Musk backs return
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2AFBVV95cUxNVzVrZl9udUdNTVdUdnNoUG1meHJncG1HUVN6WXlXQ3JkTGNSOE9HQU1pcHJ5RFhEZ01STzQ0ZHFlNUh4YVV6eVNpN3NHNXR0eUpoT2l6bTY2QW5hT05yaXMzaGtZcVBrUWdOa25YeWNkckJ6SW80U3Q1VFhsUUJjUjV1dzNyM0EtUlR5OWh6T1paRnVjeUIzSjVqS0hIaDA1REVkMGMxM3lzMDhYdG1wOFZCLVdxRjRleXNDNTdYc2pQSDVmZVhzZ1ZTUThfWUgwdkRnUzhQOGc?oc=5>

### NVIDIA Falls 4% Ahead of Earnings as Elon Musk Joins Calls to Reinstate Jensen Huang; AMD Drops 6%, Taiwan Semiconductor Slides 5%
- Summary: NVIDIA Falls 4% Ahead of Earnings as Elon Musk Joins Calls to Reinstate Jensen Huang; AMD Drops 6%, Taiwan Semiconductor Slides 5%
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxOVTN6c1RxdUhEaFJpcmd1amZzR19ISTZfTlhqc0lVNXR3ZE9HQzF6eWlYb3R0TnZZc2FNczBHRkRwTWlLV2RwV2RJSENsMmtFdFUyck5VLUh5eVRHSTliOFJ6U2JpVlJHc0tNX284SE42RGtEMldnXzM0MFVGX2ZLbE9WUHNJYkZYSm1oYi1xeFI3OEFDbnRHcVVn?oc=5>

### 'Massive shoes to fill': Wall Street sours on Nvidia stock after Jensen Huang's exit
- Summary: Wall Street reacts negatively to CEO departure, expecting potential strategic shifts and stock volatility.
- Date: 2026-11-15 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMixgFBVV95cUxQSUhad2VoUnU5VjNDX3N6UW5WX1FFaFA1eUU2V1kxX3BTQlpVX2twdVVaUHEtTWozYWZBRzRwbHZ6NE1OdHpQWXV2cml5b2R5bGY0bVk1Y19qM0pFcjk1V1NWUFNuX2lHOUlVLXVpeVRJam9mSjdiMTI2OG1KS3FvcmVQVGV0Uzh0TldXa2NLUmhNeTQtZS1oS3dydFJHTWNDcHdDLUtpakNCcV85eDdKTG15M3hqNnZOUko5RVB3aHhvbEJuVVE?oc=5>

### Why Nvidia Stock Fell Again
- Summary: Recent decline in Nvidia stock price indicates a negative market move.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxOVFVRTjVuUWNiM1EwR1JwdVpSc2VlOHlYUVh1c3YzSEFkRUNXQjBVcVBaZUxLWHNhM1g2Ym9FREFDbHpVTEh1endhV2czc2FrNHozQ2t0c093dWxqbzN6clYyQkl0MXBBNTIyalowM1ZYeVVDYlppbUpxbGFBNjJlSFNSVHBzaDRkTFROdmp0UnQxSU1xUk44?oc=5>

## CATALYSTS

### Nvidia (NASDAQ:NVDA) Stock Faces $109 Billion Earnings Test After Jensen Huang’s Exit
- Summary: Nvidia (NASDAQ:NVDA) Stock Faces $109 Billion Earnings Test After Jensen Huang’s Exit
- Date: 2026-11-15 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMigAFBVV95cUxNbmhHNDBIY21SSTFlRm1jdlFiMjBGc1A1b05VczFYeE8yQkZGODNOWUhmQXMzeFF6U0ZVd3RVMzR5Mnl0OVdZWlYwQlRDdTR4cG9UWThITnJIOWtoWkxzbDY3VEVtTUExNW9iSkc1VFhBaXNMVDZwZFN0N1BIcjZXSg?oc=5>

### Nvidia Reports Earnings Tomorrow as Cathie Wood Boosts Stake by 85% in Q3. What Investors Should Know
- Summary: Nvidia Reports Earnings Tomorrow as Cathie Wood Boosts Stake by 85% in Q3. What Investors Should Know
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMifEFVX3lxTFBrMGtrMVlZbFQzU1FHUFMzMjFuYmR2bTBKQUFYMXFxR3NaNDJkSFZNaUlfRE1DYW9qTzRsZXpNTEc0OEg3QlNzMVpvRHpQTkIzRUVITmRhekdsU2QzWlJZMExzck05YzlvSVFweVQ3ME11UW1XSEI4MnFRWko?oc=5>

### Nvidia Reports Q3 Earnings Tomorrow – Options Traders Brace for an 8.83% Move in NVDA Stock
- Summary: Nvidia Reports Q3 Earnings Tomorrow – Options Traders Brace for an 8.83% Move in NVDA Stock
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxPSTBRQkRBejByR0pDX2dtX3piQ0NXMUR0TFc1NlZnVUprNG02dVVjV2M0azI1T1Y3amhncTVQbmNfcEZhRm01TGRMWW1lTWNPWDlQdnZlZldTc0JFcFFtZ0d4OElHdDRheHV5dVpoVXBCV2tEaG0wS2FBSXNYS3F5LUFkOXZSUXU3YUlVeEg4N01XalJLQlN2dUtmNzA0OWJiVzFrVHFhWlRqclRkNHFGelcwSXBiMEVWZ010Zm0zcFRtanBn?oc=5>

### Nvidia stock valuation looks 'draconian,' even without Jensen Huang: Analyst
- Summary: Nvidia stock valuation looks 'draconian,' even without Jensen Huang: Analyst
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0gFBVV95cUxOMDl4WHFaaUdid1hZWl9vazlpQTJwbmxuR2xyT3RUblBjemlFOHRnR3BGemhCUmI3ZWktSHlib1NqUDl5SnFPVWlFenh6NUFUMUk1YWdyWmxfTmRKbzJDSDFZdUJCU3FTb3UzbVF0NXBJS25QMWxIOHFiSmhLXzR5clZqYmZYZkRHYi1WVXdnYkdwOUNVX2JrS1ZxUWhkaXZJdnJTcTBWMzRPbm42dm1zVEE2NmNhOEcyRUtjTkFFZU1KWWJUZk5WTVhxd1dmYXpSQlE?oc=5>

### Jensen Huang leaves Nvidia with a $132 billion stake — here's when he can sell and why investors may not know when he does: Chart of the Day
- Summary: CEO departure with large stake; sale timing uncertain.
- Date: 2026-11-15 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingJBVV95cUxNVjJKRThIRnJiTkxmT2NTMlJKbjhMWXhOSlhVcWRDUFNwYXRwUUlwRzJYZ1lJWFpqOVk0RUFqTFRtdmY3cVNscUxMRDVyVFFnLUxfdFoxX29KeW1iODB1d0cwVlVObjlIU3RvaUdDMFpJUzd5OXhfZUZCWkhKZkFRMEl6M3o2S2tIbkVVdngzVE5wcDR2d0Q4eWFqVXZScGlPQmFTTTNsdExXNWNDZXlXdF9UQ3ZfX3lweU1aMU9FOWthV1pYNEJabUNvb0Fna2dnM000dUdJbEFTOWU4UHhtZTExU1VqSi00V2EzUWwyemk3R3FlN3pEeWo1Uy1nU0V5ODhSMlh0SG1pMXpZS2FYLUJ1V1FtLTZDSnFOS3RB?oc=5>

### Should you buy Nvidia stock right now?
- Summary: Investor query about current Nvidia stock purchase.
- Date: 2026-11-15 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxNOWk5b2U5UXB0UncwYlJpQWRFZXFLMjZVSE9JS0JtUEVpQ2E3SjBVRS1EdzkwUW9RTWRHbVpEMzhtQldCTXJJZ180aVVUVGg0Q01XN3FhdFMyMGN3TGJoSk1CY1J1Vm9BWEN6dmVpbVotR3NKT3RJNWJJWkY1UllFSUQ1VGtQa0JKV0N4V1J6eHZNc1FwZmk2VmdpbXRJX3BtTWhF?oc=5>

### Should Nvidia stock be a buy ahead of earnings?
- Summary: Questioning investment stance before earnings release.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxNdzFjdXVCYTYweU53RmZfTk9na0VVcnFnS2kxbUNBcndUZ1AzWElDUHNsZXd0ekZiNnphOUZvbkxwRnFTajNGRXJWY1R5QmpSTmpHVVNlQVdXdE9fR0F0QWhkVE5DSG5QLTY3QkQ1cXVrRVZWYWRKTDlCRVVPbFZVZkxWc2NQdFIwY2RJOFMtc0xnTTBQT3l6Rw?oc=5>

## RISKS

### Nvidia (NVDA) Is Under Multiple US Justice Department Investigations
- Summary: Multiple DOJ investigations pose legal risk to Nvidia.
- Date: 2026-11-16 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxPX0RBNjNHLXc1REtobHJHUTVnTzZvTGkzWnVzQlk4cWRiNm1HdG9aWW1kRDk1LTZ2NlYwUmtsdERzcjdUdHdkY0lob3dTeXc1cEY3aF84MW82R1RYVzRKX2lEVHAtcnNDcVU2RXRic3kxQ2J5dm1VV01IS0IzMWZ4ZThKdDFRc1pCOUFLZmlZUE5lS0UzUzJfWg?oc=5>

### Don’t Know What to Do With Nvidia Stock After Jensen Huang Stepped Down as CEO? Consider These 5 Warren Buffett Quotes.
- Summary: Leadership change introduces uncertainty and potential risk.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMi8gFBVV95cUxOYUw1cXRIWlpzMktWREVOVnp4dnB1WEpzWXBhZWJLSktFeWNqaG1MNTdjRFEtQ2R4bk1pWVJlNWdfNFlGWFNqMExweDhqRnlBbVJtZHdNNWhJYklJSF9YTS1idUVsa3ppY1NtSHhPMnZZQVR1WGVJUldXS0hyQUJwYXRnUmoyV3pJTWFjcElWZktTNGE5TTVuajlSNkgtbnhZOGJjVm10cmRZalhKS2tXc1l4NFJ5NjRqOUxCWURfMVJ0VlAxNUZEcV82MzRkQWhPeDNTRFh3bDltM0ZpOW5yT2lJRDV3ZHlVUkc4OTh4WHNwQQ?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NVDA** | **19.74** | **16.47** | **18.58** | **105.90** | **3,770,312,556,544.00 USD** | **-17.70** |
| AMD | 107.75 | 12.09 | 73.63 | 44.70 | 827,063,205,888.00 USD | 104.32 |
| AVGO | 42.58 | 15.97 | 31.13 | 85.50 | 1,591,528,259,584.00 USD | -1.92 |
| INTC | N/A | 2.56 | 16.07 | 20.90 | 294,823,034,880.00 USD | 56.17 |

Peers fetched as_of: 2026-11-16; NVDA reuses existing data (market data as_of: 2026-11-16); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-26
- Next expected earnings: 2026-11-17 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-16

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-08-26
- Revenue (latest available single quarter): 96,221,000,000.00 USD; period 2026-04-27/2026-07-26; fiscal year/reporting period 2027/Q2
- Net income (latest available single quarter): 59,688,000,000.00 USD; period 2026-04-27/2026-07-26; fiscal year/reporting period 2027/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMimgFBVV95cUxPVHlZMXdwbHJLTmdVa0lYcE8xRG5pOXlNckticy1NeWhxZWJZZFVaeERFT2wzdzMzS3dZMjVTMUhpZzNEOXgtSkwzdElrd3lCdDctemVDeEJfX2tWVF9wMVNIMHNXZVo1d3l0OFFWazhCQ0xCMFlMd1ZrRkY5RENONFYtYTVoclFHMWxfQTNpVENrbzY5dnpzMThB?oc=5
- https://news.google.com/rss/articles/CBMi2AFBVV95cUxNVzVrZl9udUdNTVdUdnNoUG1meHJncG1HUVN6WXlXQ3JkTGNSOE9HQU1pcHJ5RFhEZ01STzQ0ZHFlNUh4YVV6eVNpN3NHNXR0eUpoT2l6bTY2QW5hT05yaXMzaGtZcVBrUWdOa25YeWNkckJ6SW80U3Q1VFhsUUJjUjV1dzNyM0EtUlR5OWh6T1paRnVjeUIzSjVqS0hIaDA1REVkMGMxM3lzMDhYdG1wOFZCLVdxRjRleXNDNTdYc2pQSDVmZVhzZ1ZTUThfWUgwdkRnUzhQOGc?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxOVTN6c1RxdUhEaFJpcmd1amZzR19ISTZfTlhqc0lVNXR3ZE9HQzF6eWlYb3R0TnZZc2FNczBHRkRwTWlLV2RwV2RJSENsMmtFdFUyck5VLUh5eVRHSTliOFJ6U2JpVlJHc0tNX284SE42RGtEMldnXzM0MFVGX2ZLbE9WUHNJYkZYSm1oYi1xeFI3OEFDbnRHcVVn?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxQSUhad2VoUnU5VjNDX3N6UW5WX1FFaFA1eUU2V1kxX3BTQlpVX2twdVVaUHEtTWozYWZBRzRwbHZ6NE1OdHpQWXV2cml5b2R5bGY0bVk1Y19qM0pFcjk1V1NWUFNuX2lHOUlVLXVpeVRJam9mSjdiMTI2OG1KS3FvcmVQVGV0Uzh0TldXa2NLUmhNeTQtZS1oS3dydFJHTWNDcHdDLUtpakNCcV85eDdKTG15M3hqNnZOUko5RVB3aHhvbEJuVVE?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxOVFVRTjVuUWNiM1EwR1JwdVpSc2VlOHlYUVh1c3YzSEFkRUNXQjBVcVBaZUxLWHNhM1g2Ym9FREFDbHpVTEh1endhV2czc2FrNHozQ2t0c093dWxqbzN6clYyQkl0MXBBNTIyalowM1ZYeVVDYlppbUpxbGFBNjJlSFNSVHBzaDRkTFROdmp0UnQxSU1xUk44?oc=5
- https://news.google.com/rss/articles/CBMigAFBVV95cUxNbmhHNDBIY21SSTFlRm1jdlFiMjBGc1A1b05VczFYeE8yQkZGODNOWUhmQXMzeFF6U0ZVd3RVMzR5Mnl0OVdZWlYwQlRDdTR4cG9UWThITnJIOWtoWkxzbDY3VEVtTUExNW9iSkc1VFhBaXNMVDZwZFN0N1BIcjZXSg?oc=5
- https://news.google.com/rss/articles/CBMifEFVX3lxTFBrMGtrMVlZbFQzU1FHUFMzMjFuYmR2bTBKQUFYMXFxR3NaNDJkSFZNaUlfRE1DYW9qTzRsZXpNTEc0OEg3QlNzMVpvRHpQTkIzRUVITmRhekdsU2QzWlJZMExzck05YzlvSVFweVQ3ME11UW1XSEI4MnFRWko?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxPSTBRQkRBejByR0pDX2dtX3piQ0NXMUR0TFc1NlZnVUprNG02dVVjV2M0azI1T1Y3amhncTVQbmNfcEZhRm01TGRMWW1lTWNPWDlQdnZlZldTc0JFcFFtZ0d4OElHdDRheHV5dVpoVXBCV2tEaG0wS2FBSXNYS3F5LUFkOXZSUXU3YUlVeEg4N01XalJLQlN2dUtmNzA0OWJiVzFrVHFhWlRqclRkNHFGelcwSXBiMEVWZ010Zm0zcFRtanBn?oc=5
- https://news.google.com/rss/articles/CBMi0gFBVV95cUxOMDl4WHFaaUdid1hZWl9vazlpQTJwbmxuR2xyT3RUblBjemlFOHRnR3BGemhCUmI3ZWktSHlib1NqUDl5SnFPVWlFenh6NUFUMUk1YWdyWmxfTmRKbzJDSDFZdUJCU3FTb3UzbVF0NXBJS25QMWxIOHFiSmhLXzR5clZqYmZYZkRHYi1WVXdnYkdwOUNVX2JrS1ZxUWhkaXZJdnJTcTBWMzRPbm42dm1zVEE2NmNhOEcyRUtjTkFFZU1KWWJUZk5WTVhxd1dmYXpSQlE?oc=5
- https://news.google.com/rss/articles/CBMingJBVV95cUxNVjJKRThIRnJiTkxmT2NTMlJKbjhMWXhOSlhVcWRDUFNwYXRwUUlwRzJYZ1lJWFpqOVk0RUFqTFRtdmY3cVNscUxMRDVyVFFnLUxfdFoxX29KeW1iODB1d0cwVlVObjlIU3RvaUdDMFpJUzd5OXhfZUZCWkhKZkFRMEl6M3o2S2tIbkVVdngzVE5wcDR2d0Q4eWFqVXZScGlPQmFTTTNsdExXNWNDZXlXdF9UQ3ZfX3lweU1aMU9FOWthV1pYNEJabUNvb0Fna2dnM000dUdJbEFTOWU4UHhtZTExU1VqSi00V2EzUWwyemk3R3FlN3pEeWo1Uy1nU0V5ODhSMlh0SG1pMXpZS2FYLUJ1V1FtLTZDSnFOS3RB?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxNOWk5b2U5UXB0UncwYlJpQWRFZXFLMjZVSE9JS0JtUEVpQ2E3SjBVRS1EdzkwUW9RTWRHbVpEMzhtQldCTXJJZ180aVVUVGg0Q01XN3FhdFMyMGN3TGJoSk1CY1J1Vm9BWEN6dmVpbVotR3NKT3RJNWJJWkY1UllFSUQ1VGtQa0JKV0N4V1J6eHZNc1FwZmk2VmdpbXRJX3BtTWhF?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxNdzFjdXVCYTYweU53RmZfTk9na0VVcnFnS2kxbUNBcndUZ1AzWElDUHNsZXd0ekZiNnphOUZvbkxwRnFTajNGRXJWY1R5QmpSTmpHVVNlQVdXdE9fR0F0QWhkVE5DSG5QLTY3QkQ1cXVrRVZWYWRKTDlCRVVPbFZVZkxWc2NQdFIwY2RJOFMtc0xnTTBQT3l6Rw?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxPX0RBNjNHLXc1REtobHJHUTVnTzZvTGkzWnVzQlk4cWRiNm1HdG9aWW1kRDk1LTZ2NlYwUmtsdERzcjdUdHdkY0lob3dTeXc1cEY3aF84MW82R1RYVzRKX2lEVHAtcnNDcVU2RXRic3kxQ2J5dm1VV01IS0IzMWZ4ZThKdDFRc1pCOUFLZmlZUE5lS0UzUzJfWg?oc=5
- https://news.google.com/rss/articles/CBMi8gFBVV95cUxOYUw1cXRIWlpzMktWREVOVnp4dnB1WEpzWXBhZWJLSktFeWNqaG1MNTdjRFEtQ2R4bk1pWVJlNWdfNFlGWFNqMExweDhqRnlBbVJtZHdNNWhJYklJSF9YTS1idUVsa3ppY1NtSHhPMnZZQVR1WGVJUldXS0hyQUJwYXRnUmoyV3pJTWFjcElWZktTNGE5TTVuajlSNkgtbnhZOGJjVm10cmRZalhKS2tXc1l4NFJ5NjRqOUxCWURfMVJ0VlAxNUZEcV82MzRkQWhPeDNTRFh3bDltM0ZpOW5yT2lJRDV3ZHlVUkc4OTh4WHNwQQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
