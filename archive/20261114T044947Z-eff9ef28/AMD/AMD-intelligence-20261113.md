# AMD Intelligence Report

- ticker: **AMD**
- Report as_of: **2026-11-13**
- Market data as_of: **2026-11-13**
- Quant sources: https://finance.yahoo.com/quote/AMD/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AMD/key-statistics/
- AI analysis snapshot as_of: **2026-11-13**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-14T05:11:07.584106+00:00**
- AI status: **Partial: 5 headlines remain unclassified and excluded from research conclusions**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 4, 'ai': 11, 'unknown': 5, 'irrelevant': 4})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **2** exact headline/source/date matches; prior report **20261113T045636Z-34122c9a/AMD** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 19 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 12.5%; oldest publication 2026-11-11

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 534.0600 |
| Return 1D (%) | -8.7545 |
| Return 1W (%) | 18.9337 |
| Return 1M (%) | -11.8029 |
| Return YTD (%) | 149.3743 |
| Return 1Y (%) | 115.3815 |
| Annualized volatility (%) | 73.4201 |
| Beta vs SPY | 3.4490 |
| Max drawdown (%) | -37.7290 |
| Sharpe (rf=0) | 1.4162 |
| Downside deviation (rf=0, %) | 47.7508 |
| Sortino (rf=0) | 2.1775 |
| Historical VaR 95% (1D, %) | 6.7006 |
| Historical ES 95% (1D, %) | 9.6472 |
| Correlation vs SPY | 0.6404 |
| Tracking error vs SPY (%) | 65.5306 |
| P/E (trailing) | 125.07 |
| P/B | 12.81 |
| EV/EBITDA | 78.02 |
| Revenue growth (%) | 44.70 |
| Forward P/E (estimate) | 30.19 |
| Gross margin (%) | 56.00 |
| Operating margin (%) | 17.82 |
| Return on equity (%) | 11.96 |
| Free cash flow yield (%) | 0.84 |
| MA50 | 554.5522 |
| Close vs MA50 (%) | -3.6953 |
| MA200 | 423.1181 |
| Close vs MA200 (%) | 26.2201 |
| RSI (14, Wilder) | 50.3561 |
| MACD (12,26) | -8.3491 |
| MACD signal (9) | -15.8960 |
| MACD histogram | 7.5469 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AMD': 282, 'SPY': 282}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 534.0600 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -8.7545 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 18.9337 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -11.8029 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 149.3743 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 115.3815 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 73.4201 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 47.7508 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 2.1775 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 6.7006 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 9.6472 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6404 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 65.5306 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 3.4490 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -37.7290 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.4162 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 30.1888 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 56.0000 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 17.8210 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 11.9600 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 0.8399 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 125.0726 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 50.3561 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 7.5469 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -3.6953 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 26.2201 -> Clearly above the moving-average trend level.

## TAILWINDS

### AMD Stock Gets Upgrade. What It Says About the Future of the AI Trade. -- Barrons.com
- Summary: AMD Stock Gets Upgrade. What It Says About the Future of the AI Trade. -- Barrons.com
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxQbFdwblpVLThWUTFCaGZSNFY2c1ZOMGlEdkJUakdnM1BKQlF0WUdHOE5uLVgzd0ZjdVl3UUJWWTc5UHZNTnFyVWItVGlsRkhUTG1scjFXTG1aQ2g2RHotb2dhQUZPVWFfbDZMc3lRZEhSSGhBczI2SDAzNkg4WjRDbHRrdEFDVVJ3WE9mc3hlWWJzRnZ4WDBxSE1NTQ?oc=5>

### AMD Stock Looks Poised to Revisit Its All-Time Highs
- Summary: AMD Stock Looks Poised to Revisit Its All-Time Highs
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxQNWFuQzhuM0xCM09xUzRvZm9tajFNTGJpZl9YZjhsX3hCN3RPQk9fZE1vMWtQVm5FVTBwUjR5T1ZaUnJTd2czLWV3WkZXcTFmTkxXX3g0MmJkckJaa09KRlBicEhuaGZpQ3EzVncxSmlzWWJBVVlIQUduSFh1RDVPUVY2LVpXME9iOGJxbm9XWTVrT0lR?oc=5>

### Advanced Micro Devices Stock Climbs 45% On A 5-Day Winning Streak
- Summary: Advanced Micro Devices Stock Climbs 45% On A 5-Day Winning Streak
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxNLVczQjEtckJ5SUxEX1dPYk1JUU9aSkFjUUNhM25Ed28zT2pGeURvcXJ2Q04wY2Q1Z05ENVBObGlOZFRZZ2cwbGduSUw2c2pjZEtkaEIxUmc1OWgwb1NkcEVXdXk3M3hGbGRjaXBtTWRQd3NabE9CRUEtQ2dLcmZxWEF5T3UzSjZjNWQ0UU1jZlNqeXQwVGhOQlVCMHhOdEw4Vmt2dE1GUFI2b0RMVDY2dDU3ZFhJT3JfNDc2dFprWENMQQ?oc=5>

### Why AMD Shares Are Surging and What a $10,000 Investment in the Stock Could Be Worth in 3 Years
- Summary: Share surge suggests strong future returns over 3 years.
- Date: 2026-11-12 | Impact: high | Horizon: long | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi1wFBVV95cUxObzh5UGl4cjhpRTFJdGJCa3h6NlFER25XZE9FeXVrRFA2dW9QZ3B1MkZBN0NEYTU4d2lJRmF2Q1FobHJuVDZlbzJJT2dGQjJOT0M2STF1NDNhaElxS1JQSURMMFFBVXlRdFhwNDJJVFEzNUhibnRTcjA4c0F6WGNSbUZ5bEJNUnp0dnd1YmdzUUxSbDY4Y1JJNXB6ZUw3amQ0WklsVWtTbEJwQUFjd1A0Ukc5ZU5qZ1l4cHhBSjF0RzBPRnZldXhDUkNlZzRMQ0I1Rkp3azlPOA?oc=5>

### AMD and Broadcom Stock Get a Boost From Nvidia’s Loss
- Summary: Competitor loss lifts AMD and Broadcom stocks.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiggFBVV95cUxOMGJPR1pTTlRRSUZBTFNIZTZCd1JYRHltdEx2N2F3OVpvRzRDbFZ2UWlhR01SLWZadTlKNnRjbi1sQU5RazZKaDdReWZmdHhqOEVuemFRTlQ3dWk5SUt2RnMtTU1CcTlDbGctMWZGLUhNREtPNXNnZXNNRUJwQkpMQTVB?oc=5>

### AMD: The AI Trade Just Entered Another Phase (NASDAQ:AMD)
- Summary: AMD signals a new phase in AI trading, indicating potential growth in AI-related revenue.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihwFBVV95cUxNa2VtWVFyQnFuVlFEeGpfN0NNUXlkYWNEZVRtM2dvMmpNX2FsREdkcGtoLVFIYThOeUJMbHN5WDVVMGIwR3pRZTJURzlUeTJnLVVLUEV4c2dwOV9BQl82WGEweGZZZnc1cHJ4Tkg2bVQzM09NMjZqNllLb0wtcGh5Q3BmNEt5TEk?oc=5>

## HEADWINDS

### Advanced Micro Devices (NASDAQ:AMD) Stock Price Down 8.8% After Insider Selling
- Summary: Advanced Micro Devices (NASDAQ:AMD) Stock Price Down 8.8% After Insider Selling
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0AFBVV95cUxNRUVxdHowcHRiQmw4YmJXVnhZd0VZMUhUMDdCZHM0enVvYWVjOU00Rlh4ZWNFMWZ3bG90SkowMkdxTXhkdkpVdU40dDdoay1hVDgyYk1rZlFOVFJXMndxaVJXdnBaWDZETlBCSzNFU2VSQ0Q4ZFAyS0FrcEtBc2k1cExnTTAtS3QxdnROcU0ySGs1cEJIQ2lJNXhiUGFFQW8zQlFvejFPLXRsZVlrbHpUa0VieXczOVZQQ04zZlJkcjNoSVAyWHZjblEtREhEaE9M?oc=5>

### AMD Stocks Fall 6.46% After 30% Weekly Surge on Nvidia Leadership Shock
- Summary: AMD shares dropped 6.46% following a 30% weekly surge driven by Nvidia's leadership shock.
- Date: 2026-11-13 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiyAFBVV95cUxPbUF4MUNsOW90WFp2TUdNM0pkZE1CSnJGSlQxaVM4OGVpTkh1TzJESExRQy1jOHhQR0tXRDhsSXhRVkZmMHlsUlJUZ3FKWXRRajM5RjMwbkY3YkRDLWY4WlpyNHdHbGlSU1ZEeHFWME5BcXBmYUNCSDBoak5UWVl5TzJ4MjRWTmlEdExFcTk3clhWM3NUM3dmNncyMzFoeGQtV19VcXVpaTFIZzhqZUpITFl2a3JUYnlCbEU4MWw3X0pZczExTlJwOA?oc=5>

### Why is Advanced Micro Devices stock sliding today?
- Summary: AMD stock is sliding today, raising concerns about short-term performance.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxQYUUxdlFKWmN3bzFscjkxc3RtTzNmejkyYjBRMHhHR2NHaFc5WEtJQ1VQUVRrZWlvUzZlZFlEdmJMTmxtR1ExRFRqMzZtMFJSNjB3QnVMclNJVE9GcGNOczYzX0F6V2owbEpTeW9aMXgxZ3BhVUw2V3llM3JhVkFuX19ZYUp4UE1sTTd6NThSQ3AtcUtMclhMUGhTN1dsRnBydDkxTjVSMGZEUTQ5dlVxeA?oc=5>

### AMD Swung 17% Down and Back in One Week: Take Profits, or Buy More?
- Summary: AMD shares fluctuated 17% down then back up within a week, reflecting volatility.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxOU3VKTElUc1ZteDc1d2lvRmwxQTJ2WmwtUjZaTjJEOEFJWjJ1al9IZmRsSld4SmswakR5MzBDS1doWkNLLXUzZFpXTzlPMG9sTlhWYjltSjZqUmJXZUdyZmMxX0U3Z1NiZUpUd0hTNm1sT28tbmhCRzJTQmlBSVNIckNKV2ppaENSZ3duNUhnYUlKYk0?oc=5>

### AMD Tumbles 11%, Broadcom and Intel Slide 6% as Chip Rally Reverses
- Summary: AMD fell 11% as the chip rally reversed, with Broadcom and Intel also sliding.
- Date: 2026-11-13 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxORGF0bHBHVFVLQllub3poU29ZYjB0eGhLMGdOUWVwSWk5UHNOVTNwbE5oSGlEbHpQazdwUklLRHhxYS1nU2pIVzNMNElWMVBYOEJkX18taldPMDZKdTlZc3duSllBYkN6clJKZWw2MVhsc1ZqQkFGajM2NHJ2LWpUM0FxZUJOOElBdWE4ZXc5Zy1MbnFWdlBYdHRqSnZyYnhHcUcyTjlEU2JzSlFr?oc=5>

## CATALYSTS

### Why Are Nvidia, AMD and Broadcom Stocks Falling Today? AI Chip Selloff Deepens
- Summary: AMD stock falls amid broader AI chip selloff.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMifkFVX3lxTFB0a205Sl8wWTVxQ20xTmlJWGRPNnNGVFJLLVBSMUM1b05BQ3Q4VGZwSEpVdWdUX29IRWdtbTJHdnhjeFE5aHZUVURkellBNWpSb0h2XzJwb1dYWVRWSTB1d3huYWRVQ1dRNks1SktEMGdvc1BNS3N1QVFnR3FuQQ?oc=5>

### Bank of America resets AMD stock price target as Nvidia CEO exits
- Summary: Bank of America revises AMD price target.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMigAFBVV95cUxPTkJZQXJQbWVNOVE4SWRtdlZfSTYtcEJVN1hvTGFpTkpmdGswajMwNUMwX1BEeUY3SWZTc3phN1JVUkxMWXJIY3NudTBWWktVNDdEVGp3NmZZdHplUFRFODdWYzlvN1Z6N3R3bU4xMFg1dTBvS1ZhcExidTBWdkl2YQ?oc=5>

### AMD Sinks 9%, Marvell Down 5% as Chip Rally Reverses and Treasury Yields Hit 5%
- Summary: AMD shares drop 9% in market reversal.
- Date: 2026-11-13 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxNNS05Y2s5ZHQxNGh6WDQtUFZLZGNGSF8wbWJsbUNuMFVzRklBckRTdjNsOFdSSFFUZWlucl9WZEFuSFprZjZ2d0JjNzgtN3RDbFRHSlVWMzNyMWNzanFjSUl6c3VKckU1Z1ZPcERCcFlyT3N1aUFwckFuUGllSUJLX3NXTkhWYkNMVHU2NTBlU21LOUk?oc=5>

### Anthropic Delivers Huge News for Nvidia Stock, AMD Stock, Micron Stock, and Broadcom Stock Investors
- Summary: Anthropic news impacts AMD stock sentiment.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMi1wFBVV95cUxPbmxsOGJlRTdQaEdfV2k0d2szNHdld1E0aFFjWGJDdU96dEhjbTB6dmlMazliU3F1WGpRT0xyb3Bwa1ZVWjZFc0lxNXJfRTh4ZzVUd1VFVWg5Q08wTWtERmxraTlTSl9SUEljTGxveHUtM0RjY0lRRVgxOVRHNjR5cXowWXNmWTItNzZxQTEtSzlrRVdPMWZjMTBBSGxsMXhNNGd5cGtRa1FrdjRqakhEc2FvUkwtcHZxbUtlb1Vwb0VZQ1dBU0o3WkZSZ0lJa3NwTGFNRWoyUQ?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AMD** | **125.07** | **12.81** | **78.02** | **44.70** | **875,905,024,000.00 USD** | **115.38** |
| NVDA | 21.01 | 17.17 | 19.38 | 105.90 | 3,932,339,044,352.00 USD | -12.64 |
| INTC | N/A | 2.76 | 17.24 | 20.90 | 317,092,888,576.00 USD | 66.14 |
| AVGO | 46.52 | 16.62 | 32.38 | 85.50 | 1,656,497,373,184.00 USD | 2.83 |

Peers fetched as_of: 2026-11-13; AMD reuses existing data (market data as_of: 2026-11-13); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-03
- Next expected earnings: 2027-02-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-13

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-04
- Revenue (latest available single quarter): 1,584,000,000.00 USD; period 2017-07-02/2017-09-30; fiscal year/reporting period 2018/Q3
- Net income (latest available single quarter): 2,428,000,000.00 USD; period 2026-06-28/2026-09-26; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/2488/000000248826000191/amd-20260926.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMimwFBVV95cUxQbFdwblpVLThWUTFCaGZSNFY2c1ZOMGlEdkJUakdnM1BKQlF0WUdHOE5uLVgzd0ZjdVl3UUJWWTc5UHZNTnFyVWItVGlsRkhUTG1scjFXTG1aQ2g2RHotb2dhQUZPVWFfbDZMc3lRZEhSSGhBczI2SDAzNkg4WjRDbHRrdEFDVVJ3WE9mc3hlWWJzRnZ4WDBxSE1NTQ?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxQNWFuQzhuM0xCM09xUzRvZm9tajFNTGJpZl9YZjhsX3hCN3RPQk9fZE1vMWtQVm5FVTBwUjR5T1ZaUnJTd2czLWV3WkZXcTFmTkxXX3g0MmJkckJaa09KRlBicEhuaGZpQ3EzVncxSmlzWWJBVVlIQUduSFh1RDVPUVY2LVpXME9iOGJxbm9XWTVrT0lR?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxNLVczQjEtckJ5SUxEX1dPYk1JUU9aSkFjUUNhM25Ed28zT2pGeURvcXJ2Q04wY2Q1Z05ENVBObGlOZFRZZ2cwbGduSUw2c2pjZEtkaEIxUmc1OWgwb1NkcEVXdXk3M3hGbGRjaXBtTWRQd3NabE9CRUEtQ2dLcmZxWEF5T3UzSjZjNWQ0UU1jZlNqeXQwVGhOQlVCMHhOdEw4Vmt2dE1GUFI2b0RMVDY2dDU3ZFhJT3JfNDc2dFprWENMQQ?oc=5
- https://news.google.com/rss/articles/CBMi1wFBVV95cUxObzh5UGl4cjhpRTFJdGJCa3h6NlFER25XZE9FeXVrRFA2dW9QZ3B1MkZBN0NEYTU4d2lJRmF2Q1FobHJuVDZlbzJJT2dGQjJOT0M2STF1NDNhaElxS1JQSURMMFFBVXlRdFhwNDJJVFEzNUhibnRTcjA4c0F6WGNSbUZ5bEJNUnp0dnd1YmdzUUxSbDY4Y1JJNXB6ZUw3amQ0WklsVWtTbEJwQUFjd1A0Ukc5ZU5qZ1l4cHhBSjF0RzBPRnZldXhDUkNlZzRMQ0I1Rkp3azlPOA?oc=5
- https://news.google.com/rss/articles/CBMiggFBVV95cUxOMGJPR1pTTlRRSUZBTFNIZTZCd1JYRHltdEx2N2F3OVpvRzRDbFZ2UWlhR01SLWZadTlKNnRjbi1sQU5RazZKaDdReWZmdHhqOEVuemFRTlQ3dWk5SUt2RnMtTU1CcTlDbGctMWZGLUhNREtPNXNnZXNNRUJwQkpMQTVB?oc=5
- https://news.google.com/rss/articles/CBMihwFBVV95cUxNa2VtWVFyQnFuVlFEeGpfN0NNUXlkYWNEZVRtM2dvMmpNX2FsREdkcGtoLVFIYThOeUJMbHN5WDVVMGIwR3pRZTJURzlUeTJnLVVLUEV4c2dwOV9BQl82WGEweGZZZnc1cHJ4Tkg2bVQzM09NMjZqNllLb0wtcGh5Q3BmNEt5TEk?oc=5
- https://news.google.com/rss/articles/CBMi0AFBVV95cUxNRUVxdHowcHRiQmw4YmJXVnhZd0VZMUhUMDdCZHM0enVvYWVjOU00Rlh4ZWNFMWZ3bG90SkowMkdxTXhkdkpVdU40dDdoay1hVDgyYk1rZlFOVFJXMndxaVJXdnBaWDZETlBCSzNFU2VSQ0Q4ZFAyS0FrcEtBc2k1cExnTTAtS3QxdnROcU0ySGs1cEJIQ2lJNXhiUGFFQW8zQlFvejFPLXRsZVlrbHpUa0VieXczOVZQQ04zZlJkcjNoSVAyWHZjblEtREhEaE9M?oc=5
- https://news.google.com/rss/articles/CBMiyAFBVV95cUxPbUF4MUNsOW90WFp2TUdNM0pkZE1CSnJGSlQxaVM4OGVpTkh1TzJESExRQy1jOHhQR0tXRDhsSXhRVkZmMHlsUlJUZ3FKWXRRajM5RjMwbkY3YkRDLWY4WlpyNHdHbGlSU1ZEeHFWME5BcXBmYUNCSDBoak5UWVl5TzJ4MjRWTmlEdExFcTk3clhWM3NUM3dmNncyMzFoeGQtV19VcXVpaTFIZzhqZUpITFl2a3JUYnlCbEU4MWw3X0pZczExTlJwOA?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxQYUUxdlFKWmN3bzFscjkxc3RtTzNmejkyYjBRMHhHR2NHaFc5WEtJQ1VQUVRrZWlvUzZlZFlEdmJMTmxtR1ExRFRqMzZtMFJSNjB3QnVMclNJVE9GcGNOczYzX0F6V2owbEpTeW9aMXgxZ3BhVUw2V3llM3JhVkFuX19ZYUp4UE1sTTd6NThSQ3AtcUtMclhMUGhTN1dsRnBydDkxTjVSMGZEUTQ5dlVxeA?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxOU3VKTElUc1ZteDc1d2lvRmwxQTJ2WmwtUjZaTjJEOEFJWjJ1al9IZmRsSld4SmswakR5MzBDS1doWkNLLXUzZFpXTzlPMG9sTlhWYjltSjZqUmJXZUdyZmMxX0U3Z1NiZUpUd0hTNm1sT28tbmhCRzJTQmlBSVNIckNKV2ppaENSZ3duNUhnYUlKYk0?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxORGF0bHBHVFVLQllub3poU29ZYjB0eGhLMGdOUWVwSWk5UHNOVTNwbE5oSGlEbHpQazdwUklLRHhxYS1nU2pIVzNMNElWMVBYOEJkX18taldPMDZKdTlZc3duSllBYkN6clJKZWw2MVhsc1ZqQkFGajM2NHJ2LWpUM0FxZUJOOElBdWE4ZXc5Zy1MbnFWdlBYdHRqSnZyYnhHcUcyTjlEU2JzSlFr?oc=5
- https://news.google.com/rss/articles/CBMifkFVX3lxTFB0a205Sl8wWTVxQ20xTmlJWGRPNnNGVFJLLVBSMUM1b05BQ3Q4VGZwSEpVdWdUX29IRWdtbTJHdnhjeFE5aHZUVURkellBNWpSb0h2XzJwb1dYWVRWSTB1d3huYWRVQ1dRNks1SktEMGdvc1BNS3N1QVFnR3FuQQ?oc=5
- https://news.google.com/rss/articles/CBMigAFBVV95cUxPTkJZQXJQbWVNOVE4SWRtdlZfSTYtcEJVN1hvTGFpTkpmdGswajMwNUMwX1BEeUY3SWZTc3phN1JVUkxMWXJIY3NudTBWWktVNDdEVGp3NmZZdHplUFRFODdWYzlvN1Z6N3R3bU4xMFg1dTBvS1ZhcExidTBWdkl2YQ?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxNNS05Y2s5ZHQxNGh6WDQtUFZLZGNGSF8wbWJsbUNuMFVzRklBckRTdjNsOFdSSFFUZWlucl9WZEFuSFprZjZ2d0JjNzgtN3RDbFRHSlVWMzNyMWNzanFjSUl6c3VKckU1Z1ZPcERCcFlyT3N1aUFwckFuUGllSUJLX3NXTkhWYkNMVHU2NTBlU21LOUk?oc=5
- https://news.google.com/rss/articles/CBMi1wFBVV95cUxPbmxsOGJlRTdQaEdfV2k0d2szNHdld1E0aFFjWGJDdU96dEhjbTB6dmlMazliU3F1WGpRT0xyb3Bwa1ZVWjZFc0lxNXJfRTh4ZzVUd1VFVWg5Q08wTWtERmxraTlTSl9SUEljTGxveHUtM0RjY0lRRVgxOVRHNjR5cXowWXNmWTItNzZxQTEtSzlrRVdPMWZjMTBBSGxsMXhNNGd5cGtRa1FrdjRqakhEc2FvUkwtcHZxbUtlb1Vwb0VZQ1dBU0o3WkZSZ0lJa3NwTGFNRWoyUQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
