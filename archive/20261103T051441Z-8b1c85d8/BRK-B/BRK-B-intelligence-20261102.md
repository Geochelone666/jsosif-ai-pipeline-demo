# BRK-B Intelligence Report

- ticker: **BRK-B**
- Report as_of: **2026-11-02**
- Market data as_of: **2026-11-02**
- Quant sources: https://finance.yahoo.com/quote/BRK-B/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/BRK-B/key-statistics/
- AI analysis snapshot as_of: **2026-11-02**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-03T05:34:21.611009+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 1, 'ai': 18, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **13** exact headline/source/date matches; prior report **20261102T041627Z-c84a7052/BRK-B** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 6 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 70.83%; oldest publication 2026-10-26

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 556.1100 |
| Return 1D (%) | 2.5106 |
| Return 1W (%) | 1.3763 |
| Return 1M (%) | 10.6356 |
| Return YTD (%) | 10.6356 |
| Return 1Y (%) | 16.4531 |
| Annualized volatility (%) | 14.8439 |
| Beta vs SPY | -0.0457 |
| Max drawdown (%) | -9.4218 |
| Sharpe (rf=0) | 1.1352 |
| Downside deviation (rf=0, %) | 10.0328 |
| Sortino (rf=0) | 1.6796 |
| Historical VaR 95% (1D, %) | 1.4125 |
| Historical ES 95% (1D, %) | 2.0016 |
| Correlation vs SPY | -0.0395 |
| Tracking error vs SPY (%) | 19.9946 |
| P/E (trailing) | 13.99 |
| P/B | 0.00 |
| EV/EBITDA | -1.79 |
| Revenue growth (%) | 10.00 |
| Forward P/E (estimate) | 24.79 |
| Gross margin (%) | 30.33 |
| Operating margin (%) | 32.56 |
| Return on equity (%) | 12.12 |
| Free cash flow yield (%) | 6.05 |
| MA50 | 516.3178 |
| Close vs MA50 (%) | 7.7069 |
| MA200 | 496.0610 |
| Close vs MA200 (%) | 12.1052 |
| RSI (14, Wilder) | 74.6924 |
| MACD (12,26) | 10.1363 |
| MACD signal (9) | 8.9250 |
| MACD histogram | 1.2113 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'BRK-B': 273, 'SPY': 273}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 556.1100 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 2.5106 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 1.3763 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 10.6356 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 10.6356 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 16.4531 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 14.8439 -> Low annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 10.0328 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.6796 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.4125 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.0016 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.0395 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 19.9946 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.0457 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -9.4218 -> Shallow peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.1352 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 24.7915 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 30.3320 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 32.5610 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 12.1200 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 6.0460 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 13.9867 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 74.6924 -> Overbought momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 1.2113 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 7.7069 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 12.1052 -> Clearly above the moving-average trend level.

## TAILWINDS

### Berkshire Hathaway Shares Just Rallied to Their Highest Level Since Warren Buffett Announced He Would Step Down as CEO, Closing Within 1.5% of Their All-Time High. Does That Rally Validate His Succession Plan?
- Summary: Berkshire Hathaway Shares Just Rallied to Their Highest Level Since Warren Buffett Announced He Would Step Down as CEO, Closing Within 1.5% of Their All-Time High. Does That Rally Validate His Succession Plan?
- Date: 2026-11-01 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxQVUV2VG9CYjU2MXh1Um1SbjkyUllBVExtbzhNQkZQVFN4bjdkU0JqenZDZmRoa0VHeHd3ME1CNkxjdjhFNUp5NTdHYWNuTG5oRUkyUzdEVXItNWx4bEpRLUhoREdrbGJISW5WNTdzQWl6ZU1iQXJ5QVRlS0dOWEtNeTdtdVZ5dVV5empvMVlORUMtbF8wT2RDRm14UldBbGE0LUdUeXV3?oc=5>

### Berkshire ekes out some new highs, but October rally stalls
- Summary: Berkshire’s stock hits new highs, though October rally stalls, indicating short-term market movement.
- Date: 2026-10-31 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNMks0NDZlNFp2b3hfeWpkTXE5MlFGMlBTMjlZQTB5VEg5UXNSQWZ5UF8yTjJkaERqby05NVJWS3RjcmtMQm9rTktMcm1MaXhJdjZvYjRMY2kzYkdtYUNjQWtyZ04tQ2xhUU9zZkVkVGc3Y1E1VE1UNGVFc0lLWWlXRlVHNkQ0Z0hzZ1hBeXFWNWZpQjlQUkg4aGJpQdIBoAFBVV95cUxPTmFsNFUtR05QdmdUU1FUclBLWmlBMEN6WndVQ2ltX3F0THczZ2JKSXU2bmlreVN6bW1xTXN5aEtnT09peW9QOEJCTE1OVUxwR2xGWHVEcTVMdHhRZ0xKZlAxN0hJd3Q5ZFNSY2RWUER1YnJsMDhnUWlwcHBtd3Bmc3RRc0NCUXlacmF4ZElrbzVYeUlvbWFFbEVycjhiNzlu?oc=5>

### Berkshire Hathaway (BRK.B) Gains Momentum As Valuation Still Looks In Focus
- Summary: Berkshire’s valuation remains attractive, driving momentum in its stock.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNS3EtUEZPZUlYeU9nbjVBS2NfYmlVVTlnOWtCWXhEcjF1cjVOMlZyU1RmOXNHNE15cE5BVVMxNjBDNHduMHF3eEtmZEpvbjJENkUtSjk4aVJmT3RYR0ZmQllZUE5iNXpPejkxdVUzNVlCRlQyNFRlVFh3Mk9LYUR0RDRCX1lSbXhFcDk4Z3dQY3hteFdXMDVlQXo1aw?oc=5>

### Berkshire Hathaway Trades Above its 50-SMA: Time to Buy the Stock?
- Summary: Stock trading above 50‑day SMA, suggesting a potential buying opportunity.
- Date: 2026-10-28 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxQYVgtNWNPbmtVb3NFZ2hraFRULUNXZk1tMFpOUlluREw5MHZ1RklSQU4wODFxSkFUWGNNNGpVS25xMzRkU2dnZ2tjU2hIYnZqTkhibUdHckdYcEJ4UXd5NjZ1TFUwZzkxMHl6THhIX0Z4eEhSd3ctaFNFZHNpM3JMV2VwM3FhMFo1dXlDcC1uT0pIdVgxcEdiNGF6NnE2YjhJ?oc=5>

### Here's How Warren Buffett's Berkshire Hathaway Stock Did in Every S&P 500 Down Year Since 2000
- Summary: Historical analysis shows Berkshire’s resilience during market downturns, highlighting long-term stability.
- Date: 2026-11-02 | Impact: medium | Horizon: long | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi2AFBVV95cUxQd0x4OEg0ZlFpTFNaQkllVGZ0bVNlRnkyYm5uUGZBNHB6NkpOblBoOFJXMFNCMmNPbFd1OVQ3dzFjc1kyNXl3azNkUWllazVGVnZZWlVWM01mTUZDTU4yd0M4SFo0TW9NYjZxS3RMX2djRTJQUG96V0p0V1RQdTRyYmZxN1FveGppRm1OUUNtclhJT3U3TDZ2MjFDUTh2NGVpWjI3LXExT3IwNG9BMHdMZjFCMy1JMW5teURDMXdETGRENFlWc29vZWYtX1NEYW9ReVFQYnIxdnk?oc=5>

### History Says Berkshire Hathaway Stock Rewards Patience: It Rose in 50 of the Last 61 Years
- Summary: Long‑term performance data confirms Berkshire’s consistent growth over six decades.
- Date: 2026-11-02 | Impact: medium | Horizon: long | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxPWEpBZDRaVGZiU1gyRXdOQ0IwYkFINklhcXpIT1RNVmNHWnFWY2VWNkNFc0N4NDZrSTdmQTREQVFReTJlaV84VUlDOFFIY25hLW1yaGFtamJnQTQyVkxoUkp4ZlN0aGExeTdKLTZNOXNqUUdOTnctQ0dTZldSaFNiY281RTlUY05HRTQtUjBnU0ZKVmpzRzA0M181N3I4VDJHLUY2bA?oc=5>

### Berkshire Can Grow Without GEICO (NYSE:BRK.A)
- Summary: Berkshire’s diversification strategy indicates potential growth beyond its GEICO holdings.
- Date: 2026-11-02 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMifkFVX3lxTE9XTmJsSUFGNVlRaHdSSjdVdVJ6cF85UmVSSGJveWl5ZjVXTWZfRXBfSDNnZG1KTlRCejByRG5zX3ctWFJ3blhtVmozRVMzcDBzeUd2a0J1VmZINi1iZndTQmZpYVZVUlRzR0YycHU3UzRnTHpHXzA1Y2NKVkE4Zw?oc=5>

### ETFs Bought $81.5 Million of Berkshire Hathaway (BRK.B) on Thurs
- Summary: ETFs purchased $81.5M of BRK.B shares, indicating investor confidence.
- Date: 2026-11-02 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxQZ3JRNG9BbFdDdHpkT052WkNMeWxVQWxqQnY3N1BZUVljSWxPc1pNZlZCUnN0bElqZ0VaUlZHZVNfRnRVTjk5cHNWckhoYWJXSUV4Nk5NdkdjRlBiNkZ4V3EtcjZuQ0ZyMXlvQjdIOTZ6RHRBeGhkRGVVNHVYZ1AyU05fWmFTNC16S1lKenBRMktxLW9qcENhcFpfV2RsRkhYY3lr?oc=5>

## HEADWINDS

### Berkshire Hathaway: Is the Stock Still a Safe Buy Without Warren Buffett?
- Summary: Uncertainty about Berkshire’s safety post-Buffett raises concerns.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxOb3d2TFVQVlNMSXVKOU5rcWplYlNOdVV5WVdDMWlIQ3pJeXRtZ1RJakpmZTdOMi00aFJKWlcxeXZ6WW8xYk9BV0lxRzJwOUdVaDgyQTZzeHRtblpfRnF5OGpndFN3ZU9pbXpGT1J2WjZDS3NLREhoWXlXcjR1Rk1GVVBxazdsWGpnSVZFZmRFb0NiM01USTZyWDJKUC1TMWlCV1E?oc=5>

### 1 of Greg Abel's Favorite Stocks and a Top 5 Berkshire Hathaway Holding Just Suffered a Devastating Decline
- Summary: A Berkshire holding dropped sharply, impacting portfolio performance.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxPTGI0X1ZyaHhPM3BJeFBlRmtFZzBuTm9sbXRLdy1aU1BvQXFUOFZCVG1KWTRoNy1pR1N3dV8waExaeEdNRFVWZ3ZPZHRGdUdrQ1FxbWFGNnF1VzlJVlQtVjRidncwYjB3emk2c3FkR2VYM2tSLW5kWXNlcURwMHViZF93MV9GRDNJOGhMTV9OU0lxT3IwcUZueg?oc=5>

### Berkshire Hathaway’s Alphabet Loss Exposes Weak Stock-Picking Record
- Summary: Loss on Alphabet highlights poor stock selection, affecting returns.
- Date: 2026-11-02 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxQdzg5Z0JmTGJKTXNlaWROTlRkLW5FYkxFN1pNT0dBcE85d1Y5akRqOFBfeWc5MU4xcFAxOU9oWnFIYm40ejNnRkNxUkJsbnVxR2RYb0ZUdzFGZmFNTDB6TDYwOURHbmxZaTJGeU41VXBtWG0yTExhYU1JTlJvQzVORU5KU0lNdzYwQmdsaDVBMGNWMkdNY0dMNTktMA?oc=5>

## CATALYSTS

### Is Berkshire Hathaway Stock a Buy Near Its All-Time High?
- Summary: Analyst question on buying Berkshire stock near all-time high.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxOcHQ5LXhDTDB0czloZWlqRTdncFROSEZJc1ZTcXdTcGJ2V0Y5TlY2dlZPbmc3dlk3blZ0VWpRa1dUemtGWmR0WFRvcDVqQUUyUDd5LTM4QXhCVnhfLVpEeGFxLUxaOUdJcjhKZDcxT0dwVi1Rd2NmdktWZGFoN3FKUjgtaUxwSmw2U3pvV0duMk1pUG4wZWx5d3lvMmQ0czA?oc=5>

### Learn Why The Bull Case For Berkshire Hathaway (BRK.A) Could Change Following Tech Stake Increase
- Summary: Stake increase may alter Berkshire’s valuation outlook.
- Date: 2026-10-31 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxPbGJfQ2ljcFBDUl81N0lUbjlOTE1nSmhsS1dNQnBZOWt0OXlHZ2J5SGNZQW15bDVSYmU1cjQ2b2dqUTlTdk15QjJ3SWlJV2EwU19xSVZ4OW9YOWJTMzRjaldoci1CUzUtcXdoUHROUUl5bnk4VGpXRHNLNHY0TGgwTlZsenhtcEx3djJQaHpaSGR2UFBTZnhjLVl3?oc=5>

### Warren Buffett's Apple Bet Is Still Berkshire Hathaway's Biggest Stock Holding at 22% of the Portfolio
- Summary: Apple remains Berkshire’s largest holding at 22% of portfolio.
- Date: 2026-11-01 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxOMkt5SlVKQkJXX3JyV1J3Qk5fY3lZZWtsZDFKenh6WTZ6b0VIdG9WMVlGenNFcGd3MFhPRmZnR1JsZzNCS013Mk80S1VYYndxTi0yYk1mWWR5QnBoTngtbEl0OUE2X0xEcVNSbWc0c3d6OVFmcmxFcEZzSVJ6WTFJNXl6XzRaZmlybU1BNFE3ekRScWdQS0N6dWVMeGc?oc=5>

### Warren Buffett's $48 Billion American Express Stake Has Been a Huge Winner. The Latest Results Say the Streak Is Far From Over.
- Summary: Berkshire’s American Express stake continues to perform well, reinforcing portfolio strength.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxNY0Y1YzJaSTc3OHdpX0tuRlFUNGlPNkthbzFPUTZBNklmcmp3S3Z3TFhZd0JMbUh0SzYtSkd4RVRXU3dNUnl4eG9WOGVhcVhKZmNHWFdhQ0dBazZjMGQxU2JoU0VkTm4zZFU1bVl5UEpveFZoNDJUS3BHQ1ItOEhfbDBIMHQzVVR1c1J6UDB2VW9rSGdsUHh4aERsLTg2WHZFSXc?oc=5>

### Warren Buffett's Successor, Greg Abel, Dumped Amazon Earlier This Year and Has Begun Piling Into a Hot Tech IPO
- Summary: Greg Abel sold Amazon shares and is buying a hot tech IPO, signaling a shift in Berkshire's portfolio.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxQLUhnY0E4a0lkZVRJYndkVjVndm1XenlRYjZIUDRYQk1ZcWFnczFTdEc1ZjFNMnhrWDRHOFhuQjNEYkJBcjVUM1NrcFoySElEUXJQb3ZUSEJLQjJfN09OZ3BXdUNZOV9fU1FwNVBPbXBaMG9sYWVxR0diUl9XTFA4c3VLNEF3R0xpSElCbHhqZUtCaWM3RzMxZXZFcm9TbFZkSWg3M2lpYzhlN25ScE1wY21fS2xMSWNGd3J0NV8yQQ?oc=5>

### Warren Buffett's Successor, Greg Abel, Has 54% of Berkshire Hathaway's $365 Billion Portfolio Invested in 4 Proven Winners
- Summary: Greg Abel holds 54% of Berkshire's portfolio in four proven winners, reflecting concentrated investment strategy.
- Date: 2026-10-30 | Impact: medium | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi4AFBVV95cUxQLVAwVlpaYTFxbXV4RmV5RzF2bzExVTdmVFRhdS1YQWVNYjZrSHNma3ZmcTJpY3VlQ0gwYkhQLUc2ZlRYRkhnMm0weDhpX2MwTEZXQU95ZnVqVEh0X3ZQMVJIOUJyWHJfU0t2V1B1SDBqY1V5Wm85a3R1OVQ0QnNySDNiLWh1ZVpNX3I3VlREVzZZa09QWXM0UDlweHVrYmozbzNqekxBc0Q4aXZlVW5Qdk1XaDdSMUlubTlDU2piUUJuTGpFYjBQUWRIbDZadFQ2R3hoTGUxWE1PQ2FKZXdXUw?oc=5>

### Warren Buffett hasn’t had water in 48 years, says Ackman. His $1.3B bet on his favorite drink now pays $848M a year
- Summary: Buffett’s $1.3B water bet generates $848M annually, boosting Berkshire’s earnings.
- Date: 2026-11-01 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxOX2g4ZGx6MzRKWGJqU0FZcThDdHNYSDc4NEJ2QXNHSWt0dVQzczFpWjNzLVgwcENmVnNXN19TN21SdWZpZVpYejJiZXBHT1NXMlJ3NzE4UDRjVVA0T2lfQ0hKNkd2d0tMZ01TWEYwektCR0tRNTJOaWE1TTZDUFhKbDNzd1Y4cU41Z1ItZExQMmRpUHA5?oc=5>

## RISKS

### Analysts Estimate Berkshire Hathaway B (BRK.B) to Report a Decline in Earnings: What to Look Out for
- Summary: Forecasts predict a drop in Berkshire’s earnings, potentially affecting investor sentiment.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxNYXlWNjd6V2dkUmdRRHBUMjRSR09JclBRdm9fZGVLcE1iSnZET293bFBLVnJJdm9YNkxtZnJDSnVRVWxZRzhGazJvdnhHbFFtUk95dVJPNDN5YWs3RkRSN1R5MnRXb2lWa2JsNVFjbzJ4QlJ2N1BxelBXM1JSYTRYcjBma19pTktRZmlzR213alhsNXh2b3h4MDh2bXVRUjRMTGU4TTZn?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **BRK-B** | **13.99** | **0.00** | **-1.79** | **10.00** | **1,190,470,090,752.00 USD** | **16.45** |
| MKL | 13.55 | 1.26 | 7.78 | -11.20 | 23,289,847,808.00 USD | -3.55 |
| FFH.TO | 8.84 | 1.36 | 7.95 | -0.50 | 55,719,620,608.00 CAD | 10.27 |
| L | 13.64 | 1.23 | 8.10 | 3.90 | 22,760,980,480.00 USD | 12.09 |

Peers fetched as_of: 2026-11-02; BRK-B reuses existing data (market data as_of: 2026-11-02); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-08
- Next expected earnings: 2026-11-07 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-02

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-08-10
- Revenue (latest available single quarter): 101,808,000,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- Net income (latest available single quarter): 25,667,000,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/1067983/000119312526341032/brka-20260630.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMipgFBVV95cUxQVUV2VG9CYjU2MXh1Um1SbjkyUllBVExtbzhNQkZQVFN4bjdkU0JqenZDZmRoa0VHeHd3ME1CNkxjdjhFNUp5NTdHYWNuTG5oRUkyUzdEVXItNWx4bEpRLUhoREdrbGJISW5WNTdzQWl6ZU1iQXJ5QVRlS0dOWEtNeTdtdVZ5dVV5empvMVlORUMtbF8wT2RDRm14UldBbGE0LUdUeXV3?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxNRnhobGVyclJON2dZSktPb2Q5ei1zV1pxY2ItWTlyMWRkanY1X1Y1UmxRODZwNEtwSlpNZFU0WldKdTNuNFM2a0NPamJVRWNvYWxMU3QyaGxrZ2o1TjYzR1pUU2JyRFRQUDFiSUItYXBkWENVSXY0aUEtUWFyd05sR21qek8xWF9ncHN1YTNSNmQ3ZnFQZXBlYw?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNMks0NDZlNFp2b3hfeWpkTXE5MlFGMlBTMjlZQTB5VEg5UXNSQWZ5UF8yTjJkaERqby05NVJWS3RjcmtMQm9rTktMcm1MaXhJdjZvYjRMY2kzYkdtYUNjQWtyZ04tQ2xhUU9zZkVkVGc3Y1E1VE1UNGVFc0lLWWlXRlVHNkQ0Z0hzZ1hBeXFWNWZpQjlQUkg4aGJpQdIBoAFBVV95cUxPTmFsNFUtR05QdmdUU1FUclBLWmlBMEN6WndVQ2ltX3F0THczZ2JKSXU2bmlreVN6bW1xTXN5aEtnT09peW9QOEJCTE1OVUxwR2xGWHVEcTVMdHhRZ0xKZlAxN0hJd3Q5ZFNSY2RWUER1YnJsMDhnUWlwcHBtd3Bmc3RRc0NCUXlacmF4ZElrbzVYeUlvbWFFbEVycjhiNzlu?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNS3EtUEZPZUlYeU9nbjVBS2NfYmlVVTlnOWtCWXhEcjF1cjVOMlZyU1RmOXNHNE15cE5BVVMxNjBDNHduMHF3eEtmZEpvbjJENkUtSjk4aVJmT3RYR0ZmQllZUE5iNXpPejkxdVUzNVlCRlQyNFRlVFh3Mk9LYUR0RDRCX1lSbXhFcDk4Z3dQY3hteFdXMDVlQXo1aw?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxQYVgtNWNPbmtVb3NFZ2hraFRULUNXZk1tMFpOUlluREw5MHZ1RklSQU4wODFxSkFUWGNNNGpVS25xMzRkU2dnZ2tjU2hIYnZqTkhibUdHckdYcEJ4UXd5NjZ1TFUwZzkxMHl6THhIX0Z4eEhSd3ctaFNFZHNpM3JMV2VwM3FhMFo1dXlDcC1uT0pIdVgxcEdiNGF6NnE2YjhJ?oc=5
- https://news.google.com/rss/articles/CBMi2AFBVV95cUxQd0x4OEg0ZlFpTFNaQkllVGZ0bVNlRnkyYm5uUGZBNHB6NkpOblBoOFJXMFNCMmNPbFd1OVQ3dzFjc1kyNXl3azNkUWllazVGVnZZWlVWM01mTUZDTU4yd0M4SFo0TW9NYjZxS3RMX2djRTJQUG96V0p0V1RQdTRyYmZxN1FveGppRm1OUUNtclhJT3U3TDZ2MjFDUTh2NGVpWjI3LXExT3IwNG9BMHdMZjFCMy1JMW5teURDMXdETGRENFlWc29vZWYtX1NEYW9ReVFQYnIxdnk?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxPWEpBZDRaVGZiU1gyRXdOQ0IwYkFINklhcXpIT1RNVmNHWnFWY2VWNkNFc0N4NDZrSTdmQTREQVFReTJlaV84VUlDOFFIY25hLW1yaGFtamJnQTQyVkxoUkp4ZlN0aGExeTdKLTZNOXNqUUdOTnctQ0dTZldSaFNiY281RTlUY05HRTQtUjBnU0ZKVmpzRzA0M181N3I4VDJHLUY2bA?oc=5
- https://news.google.com/rss/articles/CBMifkFVX3lxTE9XTmJsSUFGNVlRaHdSSjdVdVJ6cF85UmVSSGJveWl5ZjVXTWZfRXBfSDNnZG1KTlRCejByRG5zX3ctWFJ3blhtVmozRVMzcDBzeUd2a0J1VmZINi1iZndTQmZpYVZVUlRzR0YycHU3UzRnTHpHXzA1Y2NKVkE4Zw?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxQZ3JRNG9BbFdDdHpkT052WkNMeWxVQWxqQnY3N1BZUVljSWxPc1pNZlZCUnN0bElqZ0VaUlZHZVNfRnRVTjk5cHNWckhoYWJXSUV4Nk5NdkdjRlBiNkZ4V3EtcjZuQ0ZyMXlvQjdIOTZ6RHRBeGhkRGVVNHVYZ1AyU05fWmFTNC16S1lKenBRMktxLW9qcENhcFpfV2RsRkhYY3lr?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxOb3d2TFVQVlNMSXVKOU5rcWplYlNOdVV5WVdDMWlIQ3pJeXRtZ1RJakpmZTdOMi00aFJKWlcxeXZ6WW8xYk9BV0lxRzJwOUdVaDgyQTZzeHRtblpfRnF5OGpndFN3ZU9pbXpGT1J2WjZDS3NLREhoWXlXcjR1Rk1GVVBxazdsWGpnSVZFZmRFb0NiM01USTZyWDJKUC1TMWlCV1E?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxPTGI0X1ZyaHhPM3BJeFBlRmtFZzBuTm9sbXRLdy1aU1BvQXFUOFZCVG1KWTRoNy1pR1N3dV8waExaeEdNRFVWZ3ZPZHRGdUdrQ1FxbWFGNnF1VzlJVlQtVjRidncwYjB3emk2c3FkR2VYM2tSLW5kWXNlcURwMHViZF93MV9GRDNJOGhMTV9OU0lxT3IwcUZueg?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxQdzg5Z0JmTGJKTXNlaWROTlRkLW5FYkxFN1pNT0dBcE85d1Y5akRqOFBfeWc5MU4xcFAxOU9oWnFIYm40ejNnRkNxUkJsbnVxR2RYb0ZUdzFGZmFNTDB6TDYwOURHbmxZaTJGeU41VXBtWG0yTExhYU1JTlJvQzVORU5KU0lNdzYwQmdsaDVBMGNWMkdNY0dMNTktMA?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxOcHQ5LXhDTDB0czloZWlqRTdncFROSEZJc1ZTcXdTcGJ2V0Y5TlY2dlZPbmc3dlk3blZ0VWpRa1dUemtGWmR0WFRvcDVqQUUyUDd5LTM4QXhCVnhfLVpEeGFxLUxaOUdJcjhKZDcxT0dwVi1Rd2NmdktWZGFoN3FKUjgtaUxwSmw2U3pvV0duMk1pUG4wZWx5d3lvMmQ0czA?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxPbGJfQ2ljcFBDUl81N0lUbjlOTE1nSmhsS1dNQnBZOWt0OXlHZ2J5SGNZQW15bDVSYmU1cjQ2b2dqUTlTdk15QjJ3SWlJV2EwU19xSVZ4OW9YOWJTMzRjaldoci1CUzUtcXdoUHROUUl5bnk4VGpXRHNLNHY0TGgwTlZsenhtcEx3djJQaHpaSGR2UFBTZnhjLVl3?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxOMkt5SlVKQkJXX3JyV1J3Qk5fY3lZZWtsZDFKenh6WTZ6b0VIdG9WMVlGenNFcGd3MFhPRmZnR1JsZzNCS013Mk80S1VYYndxTi0yYk1mWWR5QnBoTngtbEl0OUE2X0xEcVNSbWc0c3d6OVFmcmxFcEZzSVJ6WTFJNXl6XzRaZmlybU1BNFE3ekRScWdQS0N6dWVMeGc?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxNY0Y1YzJaSTc3OHdpX0tuRlFUNGlPNkthbzFPUTZBNklmcmp3S3Z3TFhZd0JMbUh0SzYtSkd4RVRXU3dNUnl4eG9WOGVhcVhKZmNHWFdhQ0dBazZjMGQxU2JoU0VkTm4zZFU1bVl5UEpveFZoNDJUS3BHQ1ItOEhfbDBIMHQzVVR1c1J6UDB2VW9rSGdsUHh4aERsLTg2WHZFSXc?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxQLUhnY0E4a0lkZVRJYndkVjVndm1XenlRYjZIUDRYQk1ZcWFnczFTdEc1ZjFNMnhrWDRHOFhuQjNEYkJBcjVUM1NrcFoySElEUXJQb3ZUSEJLQjJfN09OZ3BXdUNZOV9fU1FwNVBPbXBaMG9sYWVxR0diUl9XTFA4c3VLNEF3R0xpSElCbHhqZUtCaWM3RzMxZXZFcm9TbFZkSWg3M2lpYzhlN25ScE1wY21fS2xMSWNGd3J0NV8yQQ?oc=5
- https://news.google.com/rss/articles/CBMi4AFBVV95cUxQLVAwVlpaYTFxbXV4RmV5RzF2bzExVTdmVFRhdS1YQWVNYjZrSHNma3ZmcTJpY3VlQ0gwYkhQLUc2ZlRYRkhnMm0weDhpX2MwTEZXQU95ZnVqVEh0X3ZQMVJIOUJyWHJfU0t2V1B1SDBqY1V5Wm85a3R1OVQ0QnNySDNiLWh1ZVpNX3I3VlREVzZZa09QWXM0UDlweHVrYmozbzNqekxBc0Q4aXZlVW5Qdk1XaDdSMUlubTlDU2piUUJuTGpFYjBQUWRIbDZadFQ2R3hoTGUxWE1PQ2FKZXdXUw?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxOX2g4ZGx6MzRKWGJqU0FZcThDdHNYSDc4NEJ2QXNHSWt0dVQzczFpWjNzLVgwcENmVnNXN19TN21SdWZpZVpYejJiZXBHT1NXMlJ3NzE4UDRjVVA0T2lfQ0hKNkd2d0tMZ01TWEYwektCR0tRNTJOaWE1TTZDUFhKbDNzd1Y4cU41Z1ItZExQMmRpUHA5?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxNYXlWNjd6V2dkUmdRRHBUMjRSR09JclBRdm9fZGVLcE1iSnZET293bFBLVnJJdm9YNkxtZnJDSnVRVWxZRzhGazJvdnhHbFFtUk95dVJPNDN5YWs3RkRSN1R5MnRXb2lWa2JsNVFjbzJ4QlJ2N1BxelBXM1JSYTRYcjBma19pTktRZmlzR213alhsNXh2b3h4MDh2bXVRUjRMTGU4TTZn?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
