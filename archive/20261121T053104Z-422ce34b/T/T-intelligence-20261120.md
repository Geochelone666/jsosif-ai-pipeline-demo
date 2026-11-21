# T Intelligence Report

- ticker: **T**
- Report as_of: **2026-11-20**
- Market data as_of: **2026-11-20**
- Quant sources: https://finance.yahoo.com/quote/T/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/T/key-statistics/
- AI analysis snapshot as_of: **2026-11-20**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-21T05:39:11.351699+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 18, 'rule': 0, 'ai': 15, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **5** exact headline/source/date matches; prior report **20261120T053808Z-e360129e/T** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **5**; {'directional_claim_without_event_type': 5}
- RSS source audit (metadata only, not article fact-checking): 18 unique headlines; 11 named publishers; 0 exact duplicates; 18 HTTPS source links; largest publisher share 22.22%; oldest publication 2026-11-13

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 22.3100 |
| Return 1D (%) | 2.1053 |
| Return 1W (%) | 0.5861 |
| Return 1M (%) | -4.7395 |
| Return YTD (%) | -5.8999 |
| Return 1Y (%) | -8.4072 |
| Annualized volatility (%) | 28.7228 |
| Beta vs SPY | -0.3433 |
| Max drawdown (%) | -28.8854 |
| Sharpe (rf=0) | -0.1619 |
| Downside deviation (rf=0, %) | 21.9912 |
| Sortino (rf=0) | -0.2115 |
| Historical VaR 95% (1D, %) | 2.8546 |
| Historical ES 95% (1D, %) | 4.6484 |
| Correlation vs SPY | -0.1709 |
| Tracking error vs SPY (%) | 34.2005 |
| P/E (trailing) | 11.68 |
| P/B | 1.41 |
| EV/EBITDA | 7.36 |
| Revenue growth (%) | 5.30 |
| Forward P/E (estimate) | 8.59 |
| Gross margin (%) | 59.74 |
| Operating margin (%) | 22.59 |
| Return on equity (%) | 11.61 |
| Free cash flow yield (%) | 7.96 |
| MA50 | 23.1076 |
| Close vs MA50 (%) | -3.4516 |
| MA200 | 24.3008 |
| Close vs MA200 (%) | -8.1924 |
| RSI (14, Wilder) | 50.8062 |
| MACD (12,26) | -0.1812 |
| MACD signal (9) | -0.3219 |
| MACD histogram | 0.1408 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'T': 287, 'SPY': 287}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 22.3100 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 2.1053 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 0.5861 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -4.7395 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -5.8999 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -8.4072 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 28.7228 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 21.9912 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.2115 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.8546 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.6484 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.1709 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 34.2005 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.3433 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -28.8854 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.1619 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 8.5947 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 59.7420 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 22.5930 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 11.6130 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 7.9591 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 11.6806 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 50.8062 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.1408 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -3.4516 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -8.1924 -> Clearly below the moving-average trend level.

## TAILWINDS

### AT&T will connect U.S. Soccer’s new center, where men’s and women’s teams will train at one site for the first time.
- Summary: AT&T to connect new U.S. Soccer training center.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxOdEgyMkxYUU05LVdLNUY3UnUtQlFyMTM4LVhqMTBaTEROaHBRcl90dlJ2RDB4ZGNOSllxY3FLWFBDb3VaeDB5dHBrWmFRWDJJVlRRalo3RnZEZlRKVmpFdnlqTDQyREtiSVBrLUFsemljU1U0bDlxTE5KaHduSDJxblBlejl4dDJfQTdlREpGd3ByaDVhWWNYeTRiN2Z6NG9haEpIbVQydnpCZ0FrUlNIWTQ4T20tb3c?oc=5>

### AT&T (T) Stock Looks Reasonable On Its 62% Three Year Run
- Summary: Assessment of AT&T's stock performance over three years.
- Date: 2026-11-15 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxNeWlWTVNHb1JxQ3c0amtDcjNhZDlwTXFPd25YeXk0YUVhYlBCS3VDdXNlb2d1WUZqOS1mY2s4SThiMzhMUDJxUTJvOFRjdDZSa2xpOHl2b0Z3REEtb24zRlJZWUtqd1RYTVRxQ0c3SzFBNzgzWktqQ1RjX2NJNzVwZmNpQy00UHpVQmllcnNZWTJWYVNOYzZMeEppel9xc0FLemU0ajdLaXdoUk92OHfSAbMBQVVfeXFMTmxmZzB2LURENGF6VkxKbkt5SUgwdFUwMEJzZHJ6aHI5d3FzQ0Q1Vm0xLUZSd3QzQUluZmJxVi0zMzMtSTlDZUhvclY0ZzFtQVRPelJjQ0swb0xpSE5TbWFZZ2RmSVB4ZVVoaC1NNE5ZSHhsSHlTb28tRlliMERpOFlFQ0N2LTZQbXpvLWRZQ0h1VFJ3dzVPOHhyejBhVmVBUnBwdjIxM1RwRjRBLXRXdTZfSzA?oc=5>

### What Could Surprise AT&T Stock Investors On The Upside?
- Summary: Explores potential positive factors that could lift AT&T stock.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxQME9kTmY2N0haSHE2RXhlWFN0bjk0OVp6RWhvbjAtSVFBd21lVVBGTGNIaVJwLTFkQ2FhemVQWU9mbWl2dm1TTmN4UmlfOGFZN1VXWU9yb2ZURUNVbmRjc1FtejNrRXVNb191ck9VYWotRW5tNXNNUV96SENQeHpIRVYtZlVra29yTzRYQ3VjZEkzcWl4a1JqclRLVjlFNjg2OFp0anhOVG1ZeEc1dHpUXw?oc=5>

### How Is AT&T (NYSE:T) Stock Up 4% in US Trading While the Wider Market Sells Off?
- Summary: Analyzes reasons behind AT&T's recent price gain amid market decline.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxOWFBNS1lPLTRTbVN3d1F3Tm9HMjNTeTg4NTViTk01NTE1VkVxbWhtdFYzeERfck1qckRoWUNxVkx4T1o2MlhsRTU5QURCc0ROTHNXOW15V29aZkJnbzJGV05VWlcxOEFRTFVnX1BkbUkxeFM0cTRISmtxQ3JBejk0NkJmUW14QTVfejdsak5Jd3hsNnFHSk1DX2NfRHdLU3ZqTUxMU05TZTVkRHA5aW1Ic25qMA?oc=5>

### AT&T(T) Stock Price Today | Quotes & News
- Summary: Provides current price and recent news updates for AT&T stock.
- Date: 2026-11-20 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgJBVV95cUxQM2JVM3E2bmYyUXBNdmhHTmpMdjhtMDRpUlFkSm1rM25RY21FMFNzTlk3dGd3RmJuS1B6S0lIczlOY3pyVGEzR21zcGVOc3gtVVBDREI3YzhMWFVqbGUtazdmRG1uNHd4eXV6MEFyNzBWNkVUbGRIenhyXzBwSEZsWjNiWTc3bjZXR3lXaEExTndaVGFTaWljYTAzejhsbUNieXg1TXVHX1V2ME5tVVd0Wk5IZllsRDBPSDZGLXJyWGRPMGh5cFhKeFhkb19TaE1vWXNqVng5UWdtakNoX0Z2b1BzcXZlTWVtRDZwVFJuanVJVFBzanRXSTF3VHVTdHlCaU5hdlcxQm9wRDQxcW50dW1BV1dpVjVjdmc?oc=5>

### AT&T vs. Verizon: Total Revenue Volume and Recent Growth for Two Phone Network Giants
- Summary: Compares revenue and growth metrics between AT&T and Verizon.
- Date: 2026-11-18 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0gFBVV95cUxObGM2ZmhYdnhHZnBFSElwenJjSTh3X0lUbFNVRjRjWmU5dU9PZmptY08yc21LS2VCQUx3N0ZLRnBla3dGN3NqRG5VRE0wbFcyTy1FczdGMTE4RkIxR0swWVNkQTB2UHJZNlNUQzdOYXdzNXR2Z2RYTl9XUEVBU2JMVXR4bU1iMTB6cXZxcTNiMkxDWjlxLW85TmJuM2lDUy1mU25VRmxHaHhzRGFka0tvZi1RMmNNX09VX1BScG5RLUJwMGFYemRDZG5NamppMTJ2WUE?oc=5>

### Which Dates Could Move AT&T Stock Most?
- Summary: Identifies key dates that may influence AT&T stock movement.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxQSXk4Rk04YWZLcDVxTTJSLWNyZmRXbTZSdDBINWdqXzI4bTcwYTI5R0dOMFIxU3Q0dTBMVmo5WE1KZ0t4Z0F6NjA4VUo3aEx5M21hWklKMHlvRTdYNlNTbmxnSFlwc0ZveC1DbzYza3FWRkVjWl9aTy10TzFub3Z2d0dfbVFZZzRpdnBWZkRXV2otRUtVV1JJa0tsTQ?oc=5>

### AT&T (NYSE:T) Stock Price Up 2.2% - Should You Buy?
- Summary: AT&T shares rose 2.2%, suggesting a short‑term positive market reaction.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxObXREZklBdjg2ZTlMb1BSVGw0V2s5bUwzNUdNYklCd3BsQnlqbE11Sl9CbE5mSVBtaFdSOG1hQThMQUhfU2tJS1RJY3J4Y0xwVzN2c0NjUjRXTGZDc29lWEpjMWFyQUR5VlBkM1NfVXUwYjExMjFSYnl2d3Z1YkN2RVdTQ21lcG1vVHZIRFNXUE11T29QaE1DR3NqaW9MdUl4TkdJbkR3?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Clean Execution Lifted AT&T (T) in Q3
- Summary: AT&T's Q3 earnings improved due to clean execution.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxNOG8zdFF2YjExaGFJamFKLUJ0MmQ3SzJLeW8tUnFwOThVREh4NzllWWhuQmtUU05MakRIWkVtRDl0VmVpSnotbkczaC1FcE5CdGFlSGIxNndkN0JDcFlaSUhHeno3U1M4RExJTkZUVFE1VVZ1NDh1YVg0RVdqZjU3X3lXakN0cTByQlhFNl84bWRqN1ZlZ1E?oc=5>

### Why Is AT&T (T) Down 3.9% Since Last Earnings Report?
- Summary: Analysis of recent price decline post-earnings.
- Date: 2026-11-20 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihgFBVV95cUxPazl4Uk8wUWVYdl9ySG54bENtQmhEZ1hvQ1kzSEY3cVV5dzNwTXVGVzFJOFNwZGtWMEJXQXRrRmRtZHgwOU5Pc2VIejAyTlRLRkd1MWs4ZXNhMkJyaHFvWkRkMGh2akpmcGZRRmpGdmVrWUtiZEJMbGlLZTgzWm9TX0RPdHVUdw?oc=5>

### What Gave AT&T Stock Its Edge Over Verizon?
- Summary: Comparison of AT&T and Verizon performance factors.
- Date: 2026-11-17 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxNdDFMbG1EWldTbGMzRG9iYTZGeWI0eXo4RUlBdUd1eWxlc2JjM0FoVl9zSzRoVE5tZk1BODJHSXRjN2ZGdWxmaUphTmRCbUV3TlNEenl3RzQzNDVNa05QYm5OVnRJU3NkUUduS05QUVZWZGdNSlloLTNveFlhdnZfU2NqdUFYX1ZfenI3cGh6V04?oc=5>

### AT&T vs. Verizon: Which Telecom Stock Is a Better Buy for 2027?
- Summary: Long‑term comparison of AT&T and Verizon.
- Date: 2026-11-14 | Impact: low | Horizon: long | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxNUzhub0VqaEZvTm9SX3ZCMWdnYnQzcmRiTzZmUnJXay1rVWdPdXZlMDdvWDdDZm5nUG9iV3c1Q2Jwelk0Uk1UU3Frdm5QNFZtSTl0VFQ2MHM2MHlBcFVVYTZHeVdvVmxuMFRlVUpWQkdoMVl2VTNoalhfMVRwNHhkUENia05NelAxWjlxbGxlUG5tTDQ3VGE4UVVyUVlMdkZRbFpMZGRObWM3Mk0yeHZxQjhKUk9ZZ1hi?oc=5>

### How Much Could You Lose In AT&T Stock After CPI?
- Summary: Potential downside after CPI release.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxQS1NVMFpPdjljd0FtQlhhbTRKeE9pSmlLZlJGZnJMTFR6UXFNRVF0emh1ZDZFQXg3YmZXVkR1XzVGR1FqV012SzVfM0hzMnR4TDhGcFY2emp1ZWhnWkpPNkpJX3RjbU5tQU1BT1VUOWJIY00xZHJkb3hvUDJvcXBLb2Itb2xYbS1NcFJwMWktaHZ2a0N3OGVDbXQ3dUlVaDhPdFdLNUdtTW8?oc=5>

### Has AT&T Stock Become A Different Bet?
- Summary: Reevaluation of AT&T’s investment profile.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxNMk12SGlFVEJmM0FqaDRGT0ZITXNJdG1NRkxHOXh0ZFliZmphRS1SMGFlMDhPVTNuUG56YXVqOEdXVHgwMGxCYXlPR2lyVFFXQU5LVHo3M1hkTkp3S0NLRFJrRU9IQWlycE5Ma01FMlZ0RUpmRDc3WTJhMFduX2VDcUl2bURQQTFlN3Z1Y2M2bncwendVN0lCVDhn?oc=5>

### AT&T Inc. Stock Price Today | T-PA Live Chart & News
- Summary: Current AT&T price displayed; market move, short horizon, low impact.
- Date: 2026-11-17 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiYEFVX3lxTE9ic1g0WWV5TVhadXRaemJjb0pmZDcwcFJnbHNUS21zLWEtcTNDNTA0NXdGcmtSOU8tcUJLYTZScm1LQ25YaEU0a0xTUkpSbC0zOThNbEV6V1lueXJ1NXZIVg?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **T** | **11.68** | **1.41** | **7.36** | **5.30** | **150,290,726,912.00 USD** | **-8.41** |
| VZ | 11.86 | 1.82 | 7.39 | 1.50 | 192,640,925,696.00 USD | 21.62 |
| TMUS | 15.97 | 3.13 | 8.17 | 7.40 | 175,415,541,760.00 USD | -19.67 |
| BCE | 11.82 | 1.37 | 7.41 | 2.20 | 20,385,015,808.00 USD | 0.36 |

Peers fetched as_of: 2026-11-20; T reuses existing data (market data as_of: 2026-11-20); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-21
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

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
- Filing date: 2026-10-21
- Revenue (latest available single quarter): 32,322,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 891,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/732717/000073271726000372/t-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMitwFBVV95cUxOdEgyMkxYUU05LVdLNUY3UnUtQlFyMTM4LVhqMTBaTEROaHBRcl90dlJ2RDB4ZGNOSllxY3FLWFBDb3VaeDB5dHBrWmFRWDJJVlRRalo3RnZEZlRKVmpFdnlqTDQyREtiSVBrLUFsemljU1U0bDlxTE5KaHduSDJxblBlejl4dDJfQTdlREpGd3ByaDVhWWNYeTRiN2Z6NG9haEpIbVQydnpCZ0FrUlNIWTQ4T20tb3c?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxNeWlWTVNHb1JxQ3c0amtDcjNhZDlwTXFPd25YeXk0YUVhYlBCS3VDdXNlb2d1WUZqOS1mY2s4SThiMzhMUDJxUTJvOFRjdDZSa2xpOHl2b0Z3REEtb24zRlJZWUtqd1RYTVRxQ0c3SzFBNzgzWktqQ1RjX2NJNzVwZmNpQy00UHpVQmllcnNZWTJWYVNOYzZMeEppel9xc0FLemU0ajdLaXdoUk92OHfSAbMBQVVfeXFMTmxmZzB2LURENGF6VkxKbkt5SUgwdFUwMEJzZHJ6aHI5d3FzQ0Q1Vm0xLUZSd3QzQUluZmJxVi0zMzMtSTlDZUhvclY0ZzFtQVRPelJjQ0swb0xpSE5TbWFZZ2RmSVB4ZVVoaC1NNE5ZSHhsSHlTb28tRlliMERpOFlFQ0N2LTZQbXpvLWRZQ0h1VFJ3dzVPOHhyejBhVmVBUnBwdjIxM1RwRjRBLXRXdTZfSzA?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxQME9kTmY2N0haSHE2RXhlWFN0bjk0OVp6RWhvbjAtSVFBd21lVVBGTGNIaVJwLTFkQ2FhemVQWU9mbWl2dm1TTmN4UmlfOGFZN1VXWU9yb2ZURUNVbmRjc1FtejNrRXVNb191ck9VYWotRW5tNXNNUV96SENQeHpIRVYtZlVra29yTzRYQ3VjZEkzcWl4a1JqclRLVjlFNjg2OFp0anhOVG1ZeEc1dHpUXw?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxOWFBNS1lPLTRTbVN3d1F3Tm9HMjNTeTg4NTViTk01NTE1VkVxbWhtdFYzeERfck1qckRoWUNxVkx4T1o2MlhsRTU5QURCc0ROTHNXOW15V29aZkJnbzJGV05VWlcxOEFRTFVnX1BkbUkxeFM0cTRISmtxQ3JBejk0NkJmUW14QTVfejdsak5Jd3hsNnFHSk1DX2NfRHdLU3ZqTUxMU05TZTVkRHA5aW1Ic25qMA?oc=5
- https://news.google.com/rss/articles/CBMimgJBVV95cUxQM2JVM3E2bmYyUXBNdmhHTmpMdjhtMDRpUlFkSm1rM25RY21FMFNzTlk3dGd3RmJuS1B6S0lIczlOY3pyVGEzR21zcGVOc3gtVVBDREI3YzhMWFVqbGUtazdmRG1uNHd4eXV6MEFyNzBWNkVUbGRIenhyXzBwSEZsWjNiWTc3bjZXR3lXaEExTndaVGFTaWljYTAzejhsbUNieXg1TXVHX1V2ME5tVVd0Wk5IZllsRDBPSDZGLXJyWGRPMGh5cFhKeFhkb19TaE1vWXNqVng5UWdtakNoX0Z2b1BzcXZlTWVtRDZwVFJuanVJVFBzanRXSTF3VHVTdHlCaU5hdlcxQm9wRDQxcW50dW1BV1dpVjVjdmc?oc=5
- https://news.google.com/rss/articles/CBMi0gFBVV95cUxObGM2ZmhYdnhHZnBFSElwenJjSTh3X0lUbFNVRjRjWmU5dU9PZmptY08yc21LS2VCQUx3N0ZLRnBla3dGN3NqRG5VRE0wbFcyTy1FczdGMTE4RkIxR0swWVNkQTB2UHJZNlNUQzdOYXdzNXR2Z2RYTl9XUEVBU2JMVXR4bU1iMTB6cXZxcTNiMkxDWjlxLW85TmJuM2lDUy1mU25VRmxHaHhzRGFka0tvZi1RMmNNX09VX1BScG5RLUJwMGFYemRDZG5NamppMTJ2WUE?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxQSXk4Rk04YWZLcDVxTTJSLWNyZmRXbTZSdDBINWdqXzI4bTcwYTI5R0dOMFIxU3Q0dTBMVmo5WE1KZ0t4Z0F6NjA4VUo3aEx5M21hWklKMHlvRTdYNlNTbmxnSFlwc0ZveC1DbzYza3FWRkVjWl9aTy10TzFub3Z2d0dfbVFZZzRpdnBWZkRXV2otRUtVV1JJa0tsTQ?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxObXREZklBdjg2ZTlMb1BSVGw0V2s5bUwzNUdNYklCd3BsQnlqbE11Sl9CbE5mSVBtaFdSOG1hQThMQUhfU2tJS1RJY3J4Y0xwVzN2c0NjUjRXTGZDc29lWEpjMWFyQUR5VlBkM1NfVXUwYjExMjFSYnl2d3Z1YkN2RVdTQ21lcG1vVHZIRFNXUE11T29QaE1DR3NqaW9MdUl4TkdJbkR3?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxNOG8zdFF2YjExaGFJamFKLUJ0MmQ3SzJLeW8tUnFwOThVREh4NzllWWhuQmtUU05MakRIWkVtRDl0VmVpSnotbkczaC1FcE5CdGFlSGIxNndkN0JDcFlaSUhHeno3U1M4RExJTkZUVFE1VVZ1NDh1YVg0RVdqZjU3X3lXakN0cTByQlhFNl84bWRqN1ZlZ1E?oc=5
- https://news.google.com/rss/articles/CBMihgFBVV95cUxPazl4Uk8wUWVYdl9ySG54bENtQmhEZ1hvQ1kzSEY3cVV5dzNwTXVGVzFJOFNwZGtWMEJXQXRrRmRtZHgwOU5Pc2VIejAyTlRLRkd1MWs4ZXNhMkJyaHFvWkRkMGh2akpmcGZRRmpGdmVrWUtiZEJMbGlLZTgzWm9TX0RPdHVUdw?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxNdDFMbG1EWldTbGMzRG9iYTZGeWI0eXo4RUlBdUd1eWxlc2JjM0FoVl9zSzRoVE5tZk1BODJHSXRjN2ZGdWxmaUphTmRCbUV3TlNEenl3RzQzNDVNa05QYm5OVnRJU3NkUUduS05QUVZWZGdNSlloLTNveFlhdnZfU2NqdUFYX1ZfenI3cGh6V04?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxNUzhub0VqaEZvTm9SX3ZCMWdnYnQzcmRiTzZmUnJXay1rVWdPdXZlMDdvWDdDZm5nUG9iV3c1Q2Jwelk0Uk1UU3Frdm5QNFZtSTl0VFQ2MHM2MHlBcFVVYTZHeVdvVmxuMFRlVUpWQkdoMVl2VTNoalhfMVRwNHhkUENia05NelAxWjlxbGxlUG5tTDQ3VGE4UVVyUVlMdkZRbFpMZGRObWM3Mk0yeHZxQjhKUk9ZZ1hi?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxQS1NVMFpPdjljd0FtQlhhbTRKeE9pSmlLZlJGZnJMTFR6UXFNRVF0emh1ZDZFQXg3YmZXVkR1XzVGR1FqV012SzVfM0hzMnR4TDhGcFY2emp1ZWhnWkpPNkpJX3RjbU5tQU1BT1VUOWJIY00xZHJkb3hvUDJvcXBLb2Itb2xYbS1NcFJwMWktaHZ2a0N3OGVDbXQ3dUlVaDhPdFdLNUdtTW8?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxNMk12SGlFVEJmM0FqaDRGT0ZITXNJdG1NRkxHOXh0ZFliZmphRS1SMGFlMDhPVTNuUG56YXVqOEdXVHgwMGxCYXlPR2lyVFFXQU5LVHo3M1hkTkp3S0NLRFJrRU9IQWlycE5Ma01FMlZ0RUpmRDc3WTJhMFduX2VDcUl2bURQQTFlN3Z1Y2M2bncwendVN0lCVDhn?oc=5
- https://news.google.com/rss/articles/CBMiYEFVX3lxTE9ic1g0WWV5TVhadXRaemJjb0pmZDcwcFJnbHNUS21zLWEtcTNDNTA0NXdGcmtSOU8tcUJLYTZScm1LQ25YaEU0a0xTUkpSbC0zOThNbEV6V1lueXJ1NXZIVg?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
