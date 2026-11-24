# BRK-B Intelligence Report

- ticker: **BRK-B**
- Report as_of: **2026-11-23**
- Market data as_of: **2026-11-23**
- Quant sources: https://finance.yahoo.com/quote/BRK-B/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/BRK-B/key-statistics/
- AI analysis snapshot as_of: **2026-11-23**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-24T08:31:13.315780+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 20, 'rule': 0, 'ai': 14, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **10** exact headline/source/date matches; prior report **20261123T053847Z-45053549/BRK-B** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 20 unique headlines; 4 named publishers; 5 exact duplicates; 20 HTTPS source links; largest publisher share 55.0%; oldest publication 2026-11-18

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 572.3600 |
| Return 1D (%) | 0.4140 |
| Return 1W (%) | -3.4562 |
| Return 1M (%) | 5.5645 |
| Return YTD (%) | 13.8685 |
| Return 1Y (%) | 13.5545 |
| Annualized volatility (%) | 15.1552 |
| Beta vs SPY | 0.0809 |
| Max drawdown (%) | -9.4218 |
| Sharpe (rf=0) | 0.8716 |
| Downside deviation (rf=0, %) | 10.2627 |
| Sortino (rf=0) | 1.2871 |
| Historical VaR 95% (1D, %) | 1.4212 |
| Historical ES 95% (1D, %) | 2.0519 |
| Correlation vs SPY | 0.0800 |
| Tracking error vs SPY (%) | 20.4363 |
| P/E (trailing) | 16.02 |
| P/B | 0.00 |
| EV/EBITDA | -2.04 |
| Revenue growth (%) | 11.20 |
| Forward P/E (estimate) | 25.09 |
| Gross margin (%) | 26.60 |
| Operating margin (%) | 26.60 |
| Return on equity (%) | 10.57 |
| Free cash flow yield (%) | 4.32 |
| MA50 | 538.0124 |
| Close vs MA50 (%) | 6.3842 |
| MA200 | 502.8903 |
| Close vs MA200 (%) | 13.8141 |
| RSI (14, Wilder) | 58.2122 |
| MACD (12,26) | 11.5953 |
| MACD signal (9) | 14.4092 |
| MACD histogram | -2.8139 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'BRK-B': 288, 'SPY': 288}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 572.3600 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.4140 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -3.4562 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 5.5645 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 13.8685 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 13.5545 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 15.1552 -> Low annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 10.2627 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.2871 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.4212 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.0519 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.0800 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 20.4363 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.0809 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -9.4218 -> Shallow peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.8716 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 25.0852 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 26.6020 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 26.6020 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 10.5740 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 4.3154 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 16.0190 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 58.2122 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -2.8139 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 6.3842 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 13.8141 -> Clearly above the moving-average trend level.

## TAILWINDS

### 41.6% of Berkshire Hathaway's $358 Billion Portfolio Is Parked in 3 Artificial Intelligence (AI) Stocks
- Summary: Portfolio heavily weighted in three AI stocks, indicating exposure to AI sector.
- Date: 2026-11-22 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizAFBVV95cUxQOHZwendMTjFORVBNdGZ1VEVHeXZWVWtSRjVTT0JfVVpLeWRBS0YtTnptTEJzRjFfR3FUS1VMd1NhVGZ6ZUc4WlNUUTBpQ2lvRnE5QmVzTDdvMHd4OFY2VXJKc1Qtem4zclRQTmQxdmZNamNQYmNaT3R4VzJENTJuTFJ4ZU85akxHWGtmSWJUcWxVNnJ0ck5sVGY1MmN4T19SNmh3WUh0ZzNuTWYzbFZvY19EeVNyZjFBNEItbURWcjVOQ1YtMjJGd29YUWE?oc=5>

### I'm Raising My Fair Value Estimate for Berkshire Hathaway Stock. Here's What I Think It's Worth.
- Summary: Analyst raises Berkshire Hathaway fair value estimate, suggesting potential upside for investors.
- Date: 2026-11-22 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi0wFBVV95cUxQWHRsZlZodkt5dFpjZzVZaXhVUGxmMXE4S3FuZXlIOTlsUDhRMTVQbGxPd3M3c1FHQ2VIR285dVFyR3hrcktkUVcxQzY2V2dSQ0VKQWlTUHYtSzRWMlI2TGpEN2xMRjN5SFFfWEVmNGFMeUhqRlVWd3pIanBycmVtZy16aHJyakZ0WXlIRVg1dENZemJyUnRBXzJnZVo1aVlCdENXalhfQWVZeFg1dF9XYWhZd2NjWlNNMnpNdzdWdl94NkpNY0l5WjBmSHlVYVNQdWtj?oc=5>

### If You'd Invested $1,000 in Berkshire Hathaway (BRKB) Stock 20 Years Ago, Here's How Much You'd Have Today
- Summary: Shows long-term growth of Berkshire stock, illustrating significant returns.
- Date: 2026-11-18 | Impact: high | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxPaVE4aWVGM0NzRnJNTW5XYVVfbUZRSU9RTllBU1hWbUpKYS1HLXh1aHVLLUNsSmMtR1k0QmZSMUd2akFkOTh2cFFKREd6TUh1UWcyRDVzaVZQNVdlX1JaQUNhTVNfV3piQXIyY3hJRGhuZENnSjBqT08xUUt5WEZoR3BCaTdBTmF1anBvSmNfaG9qQUhXZVFjMg?oc=5>

## HEADWINDS

### Stock Market Sell-Off: Warren Buffett’s “Be Greedy” Rule Has a Catch Most Investors Forget
- Summary: Market sell-off linked to Buffett’s rule may pressure Berkshire’s portfolio.
- Date: 2026-11-23 | Impact: high | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxOUVRINVNYOERQSWdpVmw4WWJPYXpPUlFBdjVUazY3ZU9lRTFadHVKUnMzYlBZVjVkNXkwTnZ1ZkZsM01QalBrQkJiSk91RHpqd0U0Z01sbTE5Vy1JQ21sNWx2VXNPUlg2WkIxUFZHb1B2d19ZUVdxVlQyQWs1eTlKY0UwekJoT1RtZjlmMWhIZ0NYRExHUlE2dw?oc=5>

## CATALYSTS

### Buffett’s Berkshire trims stake in surging 143-year-old retailer
- Summary: Berkshire reduced its holding in a long‑standing retailer.
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi6AFBVV95cUxNbjJ3RE1xdlV0Ym40cTFQaDNxUnZSUnQtYWZBakc3aWgxNnhYaHFOSnloWDhmQk11UlJNczNQV3dtNV9kNUg5M1hFc3J4RFNwS0JWcTdzLXJuRXBrNnpoSUc2N3ZEdXZyc1NhbldCd0pic1E4UHJQc1ZBOUx5SjFKVVdMRno4Ym0wQUdZQ2t0Q3VNbFZHUnFsQzJuZEZVSDF0SmM1UnFDeGFCX01iejk0aUtyaEpCT3B6cjVwS0F5MmJxMWVpdWZ4NlZ0Z2xoT0RLcWdLQ3JPOUs1TXNpTDQ2T1lpVFdxazg0?oc=5>

### Warren Buffett’s Successor, Greg Abel, Has Invested Nearly 47% of Berkshire Hathaway’s $360 Billion Stock Portfolio in Just 3 Stocks (and None Are AI Hyperscalers)
- Summary: Greg Abel concentrated portfolio in three stocks, excluding AI hyperscalers.
- Date: 2026-11-22 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxPam9lcUIybDhzMEFMZkFsU2xZWkdJR19fOGplTllISm95UXQ5SmVkLXlUMnZobzhDMmVWWlAtYjFsVzFfQjhPWGZwSkl2bnFvLTZnajEtYnlyQkFYcFUyYVRDMVoxb25UYmJNdWZnaXlJQzhMdHFZYUl3Z0RxbGxLUWNoeU5fQW85REdLWmMtRmNONnV4MXBWLU8zWVlLV3lF?oc=5>

### Greg Abel Just Approved a Record $9.6 Billion in Stock Buybacks for Berkshire Hathaway Last Quarter, More Than Double the Pace Set in the Second Quarter. Is Berkshire Still a Buy as Shares Sit Near All-Time Highs?
- Summary: Record $9.6B buyback approved, doubling prior pace.
- Date: 2026-11-21 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxQVVJjLU5QcVZ4WWF1RmRSMXFjY1lSY0x2UkdxRXYxY3JSQzBjRkowOWFMQTU4QWVlNDJZd3gwMTRlWUNnSk5DdEE0cVBHTDlYaXgwUG03a05FOEpITWpoWWhQNHNLZFdHZDRSYUFMcGlQMjdTMVlnTDBZaFRSVm1hWkV6TmN0a3d1cU9JTGVHU3hYaHkzMU5ERUNOTQ?oc=5>

## RISKS

### Berkshire Hathaway is betting big on 1 beleaguered US market. Is it too late to get in?
- Summary: Bet on a struggling US market introduces potential downside.
- Date: 2026-11-22 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMihAFBVV95cUxOYnc2NDdPMVc4Qml2NWhDalQ1Q2ZYZjJDN3U3NHVoRXJodFpxbVBRRWdsWDhlN2RSblhnSmVFQ2pDME9wQ0pVUXExQ3JWbzJ5Q0RJeXVVTUdJTS1EYzNNY29kSUtNcXVDeXNNR1JhUXgyMnNCcDFLTkRINnFvVGVPQXdOVWs?oc=5>

### Warren Buffett's Successor, Greg Abel, Just Sent a Massive Warning to the Market
- Summary: Abel’s warning signals potential downside for Berkshire.
- Date: 2026-11-23 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxON3RKd2NscjNIdG5YeVNYdDNrR1RJN3B1Z1V5aHVIdUlMcHc2dTFlNHVqYmRXeHhOeHA2ZHd5eC11OXBpUkFoX21BTVdOYW5taWluRmpBSkNndW9YamNMUzFLVTVONFc5eFQzazNnN0lpNDNLaFRXZG1XcFdIMDhkUElVUFhkLXdzb09Sc3FKekdVUTFqTjd4M1c0UE9PWUVxNnc?oc=5>

### Berkshire Hathaway: Slightly Too Expensive To Be Worth It (Rating Downgrade) (NYSE:BRK.A)
- Summary: Downgrade suggests Berkshire may be overvalued.
- Date: 2026-11-23 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxONzFpZ2xoSzlkazFtUkNhX09sQ1k0T2FwT19GenVaR3dwYi03M0s4Vk9GOG5ZTHpsWkxMMnd2U2Z5TXJtUDMwYmxjWnVUSGJ1YWdLcUZ6bXlxTHdiNFlKRjBHM1htejMtN1c2RVhtRDVlZXBlcFAyM3FIREY4MW1BdWVxQ1EyUFZZUjZiUzF6bjVaaUQ0U0R2c3l5WkwtQQ?oc=5>

### Berkshire Hathaway Owns 22.6% of American Express. Is the Stock a Buy, Sell, or Hold After a 17% Drop in 2026?
- Summary: Ownership stake prompts analysis of future recommendation.
- Date: 2026-11-23 | Impact: medium | Horizon: long | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQSi16bmFZMVBVb3A0ZTVXNWJvQ3JjNGJJV1JVMERpWEVNazYyQlRvQk5JeVVGLVo2MDRna0wxU0d2Z3pZZTVTQUhabUEta0UycXVFQnBVVTN1cUFobGJrQlFtbWp6S0l2VlFZbmpiQmlaS0JsMUFwYTlGa19neVZBSkdYV05EeDRaWFJOZ1U0cjZTNTZ6LUo1Ug?oc=5>

### Berkshire Has Owned These 2 Consumer Stocks for Decades. I'd Buy Both Before December and Never Sell.
- Summary: Recommendation to buy Berkshire-held consumer stocks.
- Date: 2026-11-23 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxNOXFOWUN6T1R3ekVMRVVNeFZrQnNYSnpWUmRDYWJYZU1OUzhEbTJhZ0JHS29CTzdNZ2h4cXpXOFg1UjRyZnh0ajdUdGYxZVdwUVBEWEx4ckNhMS1uOHpaQXNJXzUzc0JJYWt4Um5aU1l5MTBrWEdHQUYyRnpRbEFObGNaQjl5ZXhLZ1ZLZUgzRUNqbFVaSUU2dVl2SGVZYVU?oc=5>

### Warren Buffett Expects Berkshire Hathaway (BRKA, BRKB) Stock to Drop About 50% Again Someday. Here's What He Says to Do Then.
- Summary: Buffett predicts a future 50% drop in Berkshire stock and offers guidance on actions to take.
- Date: 2026-11-19 | Impact: medium | Horizon: long | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxQV1FWcTNHWTNfd3pnSmZ2MUJYWXpaWm0taXI3TFE5bmRyV041UjVRSUFiYmF6SENLYVV3ZWZiM2pZZ3FISlNUeS13MDhSaWdOVW10M09XVWVJVDllSkFaby1YYm9hZElMM1huZlU1OEJINmc4Z29QZC12Ri1hUThsWmc3TmdueXNoN3dYWlc0TTRHcDMyX1FjVVA1a21jelVzVmJmZU9LTTZwUQ?oc=5>

### Warren Buffett's Successor, Greg Abel, Has 31% of Berkshire Hathaway's $363 Billion Portfolio Invested in 3 Game-Changing AI Stocks
- Summary: Abel’s portfolio heavily weighted in AI stocks, indicating significant exposure to AI sector volatility.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMi0gFBVV95cUxPTmlyN21KMGdKcXZYMVlvM0hRR2xKUmNKNEMzVHo1cUdjZ3Nqc1E2c2tudFBfLVFVT2ZjNUFyeF9kMmRWb2xvRkV1WVhUTWhtbG44SGdObWhjWTRVbHJlaHJ2MWxXUmNBa0dhNDFuTEdudlBHUlVaMWFXQ1NYRGM3UFA3UWdVakx0MjNKeW9rMDFza2I2OUxPZklmNHlvRDJuZHJmckI1RHFxc0ltaGZjSVl3VXhLc0VCSEhjNjJiOGkteEVES3ZrcGhzTmk4MW9xUnc?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **BRK-B** | **16.02** | **0.00** | **-2.04** | **11.20** | **1,215,989,809,152.00 USD** | **13.55** |
| MKL | 13.84 | 1.29 | 7.96 | -11.20 | 23,790,639,104.00 USD | -4.36 |
| FFH.TO | 9.80 | 1.42 | 8.70 | 1.90 | 55,744,110,592.00 CAD | 12.73 |
| L | 15.23 | 1.22 | 8.64 | 1.90 | 22,273,087,488.00 USD | 3.75 |

Peers fetched as_of: 2026-11-23; BRK-B reuses existing data (market data as_of: 2026-11-23); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-07
- Next expected earnings: 2027-03-01 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-23

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-09
- Revenue (latest available single quarter): 105,647,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 22,112,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1067983/000119312526452412/brka-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMizAFBVV95cUxQOHZwendMTjFORVBNdGZ1VEVHeXZWVWtSRjVTT0JfVVpLeWRBS0YtTnptTEJzRjFfR3FUS1VMd1NhVGZ6ZUc4WlNUUTBpQ2lvRnE5QmVzTDdvMHd4OFY2VXJKc1Qtem4zclRQTmQxdmZNamNQYmNaT3R4VzJENTJuTFJ4ZU85akxHWGtmSWJUcWxVNnJ0ck5sVGY1MmN4T19SNmh3WUh0ZzNuTWYzbFZvY19EeVNyZjFBNEItbURWcjVOQ1YtMjJGd29YUWE?oc=5
- https://news.google.com/rss/articles/CBMi0wFBVV95cUxQWHRsZlZodkt5dFpjZzVZaXhVUGxmMXE4S3FuZXlIOTlsUDhRMTVQbGxPd3M3c1FHQ2VIR285dVFyR3hrcktkUVcxQzY2V2dSQ0VKQWlTUHYtSzRWMlI2TGpEN2xMRjN5SFFfWEVmNGFMeUhqRlVWd3pIanBycmVtZy16aHJyakZ0WXlIRVg1dENZemJyUnRBXzJnZVo1aVlCdENXalhfQWVZeFg1dF9XYWhZd2NjWlNNMnpNdzdWdl94NkpNY0l5WjBmSHlVYVNQdWtj?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxPaVE4aWVGM0NzRnJNTW5XYVVfbUZRSU9RTllBU1hWbUpKYS1HLXh1aHVLLUNsSmMtR1k0QmZSMUd2akFkOTh2cFFKREd6TUh1UWcyRDVzaVZQNVdlX1JaQUNhTVNfV3piQXIyY3hJRGhuZENnSjBqT08xUUt5WEZoR3BCaTdBTmF1anBvSmNfaG9qQUhXZVFjMg?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxOYlNnaVRSZEk4cjAtNVRNQlpESjdzYUItUDd0TWpuekZrSl9pM2JZQ3cwTndwSUc0LTVhRy1Bal9QdUt3dVNnTE1TM1BqRGdwLThCSHpiMXlaUG03S04xUjNzNkRSWWRJZjlrdTJSbjI4WFl6dTliUHN4bnQ4d1piVHZlWGc3UkZ3VWtjQmhmZFBObU5IV2JlVzJn?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxOUVRINVNYOERQSWdpVmw4WWJPYXpPUlFBdjVUazY3ZU9lRTFadHVKUnMzYlBZVjVkNXkwTnZ1ZkZsM01QalBrQkJiSk91RHpqd0U0Z01sbTE5Vy1JQ21sNWx2VXNPUlg2WkIxUFZHb1B2d19ZUVdxVlQyQWs1eTlKY0UwekJoT1RtZjlmMWhIZ0NYRExHUlE2dw?oc=5
- https://news.google.com/rss/articles/CBMiygFBVV95cUxOZWZtU19JUDJfdjVVa3QzMTVZekcydzIyZ1k3RV9PTFFHWkZyc1RoanVSRUNTMXA3bFlHb0tIelJzQ09uUGhqUUpzVXJHSDRyT3JYZnNhT1R6NkpPM3NZbEhWRm11ajZoUzlETGMzOVJ6R08xUTZxdnRvMkFJUEt6OXdOMWRlNTJWakZ5cENCTzNUeDNUOVpmUktmT2NsSm8xdjgzckg5X3JNQW9UZThrakNabEktTHR5cGU2LTdlU1FHTzJtUnNhQXV3?oc=5
- https://news.google.com/rss/articles/CBMi6AFBVV95cUxNbjJ3RE1xdlV0Ym40cTFQaDNxUnZSUnQtYWZBakc3aWgxNnhYaHFOSnloWDhmQk11UlJNczNQV3dtNV9kNUg5M1hFc3J4RFNwS0JWcTdzLXJuRXBrNnpoSUc2N3ZEdXZyc1NhbldCd0pic1E4UHJQc1ZBOUx5SjFKVVdMRno4Ym0wQUdZQ2t0Q3VNbFZHUnFsQzJuZEZVSDF0SmM1UnFDeGFCX01iejk0aUtyaEpCT3B6cjVwS0F5MmJxMWVpdWZ4NlZ0Z2xoT0RLcWdLQ3JPOUs1TXNpTDQ2T1lpVFdxazg0?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxPam9lcUIybDhzMEFMZkFsU2xZWkdJR19fOGplTllISm95UXQ5SmVkLXlUMnZobzhDMmVWWlAtYjFsVzFfQjhPWGZwSkl2bnFvLTZnajEtYnlyQkFYcFUyYVRDMVoxb25UYmJNdWZnaXlJQzhMdHFZYUl3Z0RxbGxLUWNoeU5fQW85REdLWmMtRmNONnV4MXBWLU8zWVlLV3lF?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxQVVJjLU5QcVZ4WWF1RmRSMXFjY1lSY0x2UkdxRXYxY3JSQzBjRkowOWFMQTU4QWVlNDJZd3gwMTRlWUNnSk5DdEE0cVBHTDlYaXgwUG03a05FOEpITWpoWWhQNHNLZFdHZDRSYUFMcGlQMjdTMVlnTDBZaFRSVm1hWkV6TmN0a3d1cU9JTGVHU3hYaHkzMU5ERUNOTQ?oc=5
- https://news.google.com/rss/articles/CBMihAFBVV95cUxOYnc2NDdPMVc4Qml2NWhDalQ1Q2ZYZjJDN3U3NHVoRXJodFpxbVBRRWdsWDhlN2RSblhnSmVFQ2pDME9wQ0pVUXExQ3JWbzJ5Q0RJeXVVTUdJTS1EYzNNY29kSUtNcXVDeXNNR1JhUXgyMnNCcDFLTkRINnFvVGVPQXdOVWs?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxON3RKd2NscjNIdG5YeVNYdDNrR1RJN3B1Z1V5aHVIdUlMcHc2dTFlNHVqYmRXeHhOeHA2ZHd5eC11OXBpUkFoX21BTVdOYW5taWluRmpBSkNndW9YamNMUzFLVTVONFc5eFQzazNnN0lpNDNLaFRXZG1XcFdIMDhkUElVUFhkLXdzb09Sc3FKekdVUTFqTjd4M1c0UE9PWUVxNnc?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxQM3F5ZGpjMHA3bEdmeGU4WW5Xd2FKNHZOa1NRQ2J1UWt2MnNiYXdqS1U4azc5Mk5obUtPN0tTUmNMek4ybnh3RktEcjFfczdZNkRyTFptNUJZZnFZMWVRN2ZOWmFtdkNoVVRPUGFSeTdlS1lJRlFXclJVQm1XUDZJQndKTG1hZUhBaTBlQkxmRFdWMXlENkd2REg4MjJRQzlIdFhKcFhHaXg2RHJ1cFNtODhFYkpNYU5qU3l4a2R3?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxONzFpZ2xoSzlkazFtUkNhX09sQ1k0T2FwT19GenVaR3dwYi03M0s4Vk9GOG5ZTHpsWkxMMnd2U2Z5TXJtUDMwYmxjWnVUSGJ1YWdLcUZ6bXlxTHdiNFlKRjBHM1htejMtN1c2RVhtRDVlZXBlcFAyM3FIREY4MW1BdWVxQ1EyUFZZUjZiUzF6bjVaaUQ0U0R2c3l5WkwtQQ?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQSi16bmFZMVBVb3A0ZTVXNWJvQ3JjNGJJV1JVMERpWEVNazYyQlRvQk5JeVVGLVo2MDRna0wxU0d2Z3pZZTVTQUhabUEta0UycXVFQnBVVTN1cUFobGJrQlFtbWp6S0l2VlFZbmpiQmlaS0JsMUFwYTlGa19neVZBSkdYV05EeDRaWFJOZ1U0cjZTNTZ6LUo1Ug?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxNOXFOWUN6T1R3ekVMRVVNeFZrQnNYSnpWUmRDYWJYZU1OUzhEbTJhZ0JHS29CTzdNZ2h4cXpXOFg1UjRyZnh0ajdUdGYxZVdwUVBEWEx4ckNhMS1uOHpaQXNJXzUzc0JJYWt4Um5aU1l5MTBrWEdHQUYyRnpRbEFObGNaQjl5ZXhLZ1ZLZUgzRUNqbFVaSUU2dVl2SGVZYVU?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxQV1FWcTNHWTNfd3pnSmZ2MUJYWXpaWm0taXI3TFE5bmRyV041UjVRSUFiYmF6SENLYVV3ZWZiM2pZZ3FISlNUeS13MDhSaWdOVW10M09XVWVJVDllSkFaby1YYm9hZElMM1huZlU1OEJINmc4Z29QZC12Ri1hUThsWmc3TmdueXNoN3dYWlc0TTRHcDMyX1FjVVA1a21jelVzVmJmZU9LTTZwUQ?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxPa1lzNGRJZmZXMG9yOG1XaWVBRXRycW1pTXU5SXE2Z0JBbDVLUXpDQTdoREJSbENSOGFlZGwtck9xMkNzbWpwbXBCZXlXWU5MSDFET1gxM3NxWG5xalA1NUM5T0RhcjFwTWZiSEJyVjN1akZXZzVhem92blQ1X3BFeUo2cUp2N24yNmY0STBNeEVrT2RqcFRidQ?oc=5
- https://news.google.com/rss/articles/CBMi0gFBVV95cUxPTmlyN21KMGdKcXZYMVlvM0hRR2xKUmNKNEMzVHo1cUdjZ3Nqc1E2c2tudFBfLVFVT2ZjNUFyeF9kMmRWb2xvRkV1WVhUTWhtbG44SGdObWhjWTRVbHJlaHJ2MWxXUmNBa0dhNDFuTEdudlBHUlVaMWFXQ1NYRGM3UFA3UWdVakx0MjNKeW9rMDFza2I2OUxPZklmNHlvRDJuZHJmckI1RHFxc0ltaGZjSVl3VXhLc0VCSEhjNjJiOGkteEVES3ZrcGhzTmk4MW9xUnc?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
