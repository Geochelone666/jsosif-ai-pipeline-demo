# BRK-B Intelligence Report

- ticker: **BRK-B**
- Report as_of: **2026-11-03**
- Market data as_of: **2026-11-03**
- Quant sources: https://finance.yahoo.com/quote/BRK-B/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/BRK-B/key-statistics/
- AI analysis snapshot as_of: **2026-11-03**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-04T04:53:31.034588+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 23, 'rule': 2, 'ai': 15, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **11** exact headline/source/date matches; prior report **20261103T051441Z-8b1c85d8/BRK-B** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 23 unique headlines; 11 named publishers; 2 exact duplicates; 23 HTTPS source links; largest publisher share 56.52%; oldest publication 2026-10-27

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 557.0700 |
| Return 1D (%) | 0.1726 |
| Return 1W (%) | 2.5931 |
| Return 1M (%) | 10.8266 |
| Return YTD (%) | 10.8266 |
| Return 1Y (%) | 17.1102 |
| Annualized volatility (%) | 14.8145 |
| Beta vs SPY | -0.0456 |
| Max drawdown (%) | -9.4218 |
| Sharpe (rf=0) | 1.1446 |
| Downside deviation (rf=0, %) | 10.0127 |
| Sortino (rf=0) | 1.6936 |
| Historical VaR 95% (1D, %) | 1.4122 |
| Historical ES 95% (1D, %) | 2.0016 |
| Correlation vs SPY | -0.0394 |
| Tracking error vs SPY (%) | 19.9551 |
| P/E (trailing) | 13.99 |
| P/B | 0.00 |
| EV/EBITDA | -1.79 |
| Revenue growth (%) | 10.00 |
| Forward P/E (estimate) | 24.83 |
| Gross margin (%) | 30.33 |
| Operating margin (%) | 32.56 |
| Return on equity (%) | 12.12 |
| Free cash flow yield (%) | 6.04 |
| MA50 | 517.3728 |
| Close vs MA50 (%) | 7.6728 |
| MA200 | 496.3799 |
| Close vs MA200 (%) | 12.2265 |
| RSI (14, Wilder) | 75.1402 |
| MACD (12,26) | 10.7100 |
| MACD signal (9) | 9.2820 |
| MACD histogram | 1.4280 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'BRK-B': 274, 'SPY': 274}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 557.0700 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.1726 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 2.5931 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 10.8266 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 10.8266 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 17.1102 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 14.8145 -> Low annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 10.0127 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.6936 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.4122 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.0016 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.0394 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 19.9551 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.0456 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -9.4218 -> Shallow peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.1446 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 24.8343 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 30.3320 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 32.5610 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 12.1200 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 6.0355 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 13.9862 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 75.1402 -> Overbought momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 1.4280 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 7.6728 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 12.2265 -> Clearly above the moving-average trend level.

## TAILWINDS

### Berkshire Hathaway Shares Are Up 11% This Year. Is the Stock a Buy Ahead of Earnings?
- Summary: Berkshire Hathaway Shares Are Up 11% This Year. Is the Stock a Buy Ahead of Earnings?
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxQRm5DaTN3NmRadmh5LVczYXBueVBlUnhtaDZrQ2FGRGtmS0J1WnRkOWcwQ1FmT1pLN0dwQUV2ajRWZENUTGRFRmRBMEpJdjBMbUVmcnB0ZGxRWTNDRWV6RlItbjBfWndhNWVhVVZuWkxWdUY5RnZmU3h5dVlfaXItdEs4NDN5RVdnTFF6RnNBWXZMTExSRUoyS3B6UTNiSE9qbWx2X3VHNVZYRENl?oc=5>

### Berkshire Hathaway Shares Just Rallied to Their Highest Level Since Warren Buffett Announced He Would Step Down as CEO, Closing Within 1.5% of Their All-Time High. Does That Rally Validate His Succession Plan?
- Summary: Berkshire Hathaway Shares Just Rallied to Their Highest Level Since Warren Buffett Announced He Would Step Down as CEO, Closing Within 1.5% of Their All-Time High. Does That Rally Validate His Succession Plan?
- Date: 2026-11-01 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxQVUV2VG9CYjU2MXh1Um1SbjkyUllBVExtbzhNQkZQVFN4bjdkU0JqenZDZmRoa0VHeHd3ME1CNkxjdjhFNUp5NTdHYWNuTG5oRUkyUzdEVXItNWx4bEpRLUhoREdrbGJISW5WNTdzQWl6ZU1iQXJ5QVRlS0dOWEtNeTdtdVZ5dVV5empvMVlORUMtbF8wT2RDRm14UldBbGE0LUdUeXV3?oc=5>

### History Says Berkshire Hathaway Stock Rewards Patience: It Rose in 50 of the Last 61 Years
- Summary: Long‑term performance data confirms Berkshire’s consistent growth over six decades.
- Date: 2026-11-02 | Impact: medium | Horizon: long | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxPWEpBZDRaVGZiU1gyRXdOQ0IwYkFINklhcXpIT1RNVmNHWnFWY2VWNkNFc0N4NDZrSTdmQTREQVFReTJlaV84VUlDOFFIY25hLW1yaGFtamJnQTQyVkxoUkp4ZlN0aGExeTdKLTZNOXNqUUdOTnctQ0dTZldSaFNiY281RTlUY05HRTQtUjBnU0ZKVmpzRzA0M181N3I4VDJHLUY2bA?oc=5>

### Berkshire Hathaway (BRK.B) Gains Momentum As Valuation Still Looks In Focus
- Summary: Berkshire’s valuation remains attractive, driving momentum in its stock.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNS3EtUEZPZUlYeU9nbjVBS2NfYmlVVTlnOWtCWXhEcjF1cjVOMlZyU1RmOXNHNE15cE5BVVMxNjBDNHduMHF3eEtmZEpvbjJENkUtSjk4aVJmT3RYR0ZmQllZUE5iNXpPejkxdVUzNVlCRlQyNFRlVFh3Mk9LYUR0RDRCX1lSbXhFcDk4Z3dQY3hteFdXMDVlQXo1aw?oc=5>

### Berkshire ekes out some new highs, but October rally stalls
- Summary: Berkshire shares hit new highs but October rally paused, indicating short-term volatility.
- Date: 2026-10-31 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxPTmFsNFUtR05QdmdUU1FUclBLWmlBMEN6WndVQ2ltX3F0THczZ2JKSXU2bmlreVN6bW1xTXN5aEtnT09peW9QOEJCTE1OVUxwR2xGWHVEcTVMdHhRZ0xKZlAxN0hJd3Q5ZFNSY2RWUER1YnJsMDhnUWlwcHBtd3Bmc3RRc0NCUXlacmF4ZElrbzVYeUlvbWFFbEVycjhiNzlu0gGgAUFVX3lxTE9OYWw0VS1HTlB2Z1RTUVRyUEtaaUEwQ3pad1VDaW1fcXRMdzNnYkpJdTZuaWt5U3ptbXFNc3loS2dPT2l5b1A4QkJMTU5VTHBHbEZYdURxNUx0eFFnTEpmUDE3SEl3dDlkU1JjZFZQRHVicmwwOGdRaXBwcG13cGZzdFFzQ0JReVpyYXhkSWtvNVh5SW9tYUVsRXJyOGI3OW4?oc=5>

### Berkshire Hathaway B (BRK.B) Increases Despite Market Slip: Here's What You Need to Know
- Summary: BRK.B shares rose amid broader market decline, suggesting resilience.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMigAFBVV95cUxNVVZNekpBdVlkQVhEUGlvb1haWXZhbnliZG5SRmZFc1J1bjZtbVMySUZjQVFNWElKSHhvQjBaWWtod0p5THFaWnZmOEZxR0UwX3hwLUhlZ24zX2RmY2hZTU1EWGo5dDVZak1reUhzdUUtdDBieW9uejB6cERWb1o0ZA?oc=5>

## HEADWINDS

### Berkshire Hathaway’s Alphabet Loss Exposes Weak Stock-Picking Record
- Summary: Loss on Alphabet highlights poor stock selection, affecting returns.
- Date: 2026-11-02 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxQdzg5Z0JmTGJKTXNlaWROTlRkLW5FYkxFN1pNT0dBcE85d1Y5akRqOFBfeWc5MU4xcFAxOU9oWnFIYm40ejNnRkNxUkJsbnVxR2RYb0ZUdzFGZmFNTDB6TDYwOURHbmxZaTJGeU41VXBtWG0yTExhYU1JTlJvQzVORU5KU0lNdzYwQmdsaDVBMGNWMkdNY0dMNTktMA?oc=5>

### 1 of Greg Abel's Favorite Stocks and a Top 5 Berkshire Hathaway Holding Just Suffered a Devastating Decline
- Summary: A Berkshire holding dropped sharply, impacting portfolio performance.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxPTGI0X1ZyaHhPM3BJeFBlRmtFZzBuTm9sbXRLdy1aU1BvQXFUOFZCVG1KWTRoNy1pR1N3dV8waExaeEdNRFVWZ3ZPZHRGdUdrQ1FxbWFGNnF1VzlJVlQtVjRidncwYjB3emk2c3FkR2VYM2tSLW5kWXNlcURwMHViZF93MV9GRDNJOGhMTV9OU0lxT3IwcUZueg?oc=5>

## CATALYSTS

### Learn Why The Bull Case For Berkshire Hathaway (BRK.A) Could Change Following Tech Stake Increase
- Summary: Stake increase may alter Berkshire’s valuation outlook.
- Date: 2026-10-31 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxPbGJfQ2ljcFBDUl81N0lUbjlOTE1nSmhsS1dNQnBZOWt0OXlHZ2J5SGNZQW15bDVSYmU1cjQ2b2dqUTlTdk15QjJ3SWlJV2EwU19xSVZ4OW9YOWJTMzRjaldoci1CUzUtcXdoUHROUUl5bnk4VGpXRHNLNHY0TGgwTlZsenhtcEx3djJQaHpaSGR2UFBTZnhjLVl3?oc=5>

### Is Berkshire Hathaway Stock a Buy Near Its All-Time High?
- Summary: Analyst question on buying Berkshire stock near all-time high.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxOcHQ5LXhDTDB0czloZWlqRTdncFROSEZJc1ZTcXdTcGJ2V0Y5TlY2dlZPbmc3dlk3blZ0VWpRa1dUemtGWmR0WFRvcDVqQUUyUDd5LTM4QXhCVnhfLVpEeGFxLUxaOUdJcjhKZDcxT0dwVi1Rd2NmdktWZGFoN3FKUjgtaUxwSmw2U3pvV0duMk1pUG4wZWx5d3lvMmQ0czA?oc=5>

### Warren Buffett's Successor, Greg Abel, Has 54% of Berkshire Hathaway's $365 Billion Portfolio Invested in 4 Proven Winners
- Summary: Greg Abel holds 54% of Berkshire's portfolio in four proven winners, reflecting concentrated investment strategy.
- Date: 2026-10-30 | Impact: medium | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi4AFBVV95cUxQLVAwVlpaYTFxbXV4RmV5RzF2bzExVTdmVFRhdS1YQWVNYjZrSHNma3ZmcTJpY3VlQ0gwYkhQLUc2ZlRYRkhnMm0weDhpX2MwTEZXQU95ZnVqVEh0X3ZQMVJIOUJyWHJfU0t2V1B1SDBqY1V5Wm85a3R1OVQ0QnNySDNiLWh1ZVpNX3I3VlREVzZZa09QWXM0UDlweHVrYmozbzNqekxBc0Q4aXZlVW5Qdk1XaDdSMUlubTlDU2piUUJuTGpFYjBQUWRIbDZadFQ2R3hoTGUxWE1PQ2FKZXdXUw?oc=5>

### Berkshire Hathaway Inc. (BRK-A) Stock Forecasts
- Summary: Analysts predict future performance of Berkshire Hathaway shares.
- Date: 2026-11-03 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxPN3YwV3BBTjFGZ3o1ZlFEaEtickd5U3IycFAzd25tTVQ0TEpkemd4OHJaWkItTkJxZ0lfbEl6b0V4d2lXYVU0OVByOXloNERIZGpoSHYzMW5VNHlXYnhYS0dOSFI4MU9ZS2tLZUY3alJTaDY1WmJVM3FyUmVXdGlCczk4VXlJcUpCV2hRVEx5MGg?oc=5>

### Is Berkshire Hathaway (BRK.B) Cheap After Fresh AI Deal Interest?
- Summary: Speculation on Berkshire's valuation following AI deal interest.
- Date: 2026-10-29 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNS3dNQmcyZGI1akpVUTVjVWVRcFVQeGpid0w0QXR2SHdtU2tqRWFaVFJsRWs4OXZxa2V4c1MtTEczUGtrYzl4emFvR0hveVdRb0xUMGRmV3NsdVFISWRScnk5ZWNIWnZiQ1NoNkNKSTFkdjJVVnNKNEhVQ18za0xrT0haQkZNX29JYTlOM2NzQjRYaDNNSEtWaW1PTQ?oc=5>

### Berkshire Hathaway (BRK.B) stock price forecast: insurance businesses hold $359 bn in cash
- Summary: Forecast of Berkshire stock price based on cash reserves.
- Date: 2026-10-29 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxNNFBxTEo5Q1doT1VNaTcyakVXSzFVaFRra3A4NXA1SUNnTjBRbFFzQUJCUU4yNmJ3ZU1iVDdEazkzMDd2eWhrQ2JDWVNCU2l5bzhmZm9BSjlyTlZ4OUlPT0FHZEhwQjVlMFVkcWJwdkJNajB5MzRDSk5vNExSVW5mQ0FCeUwwekV4RWFibG04WmhHb21ZeGxJWmlTeFBlRVZxRk5JdzlNVk42T1RhcDVkUEk3c0Y2QVQxZDdCUDdYZmdpd2s?oc=5>

### BRK.B Stock Nears $557.59 as Berkshire Earnings Approach
- Summary: Stock price approaching $557.59 ahead of earnings release.
- Date: 2026-11-03 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxNWmtsSnQteVUwUmxzRWFualBtWDNjc2VLVWdlSUxXYjl4S0R0RHZFMFdJc0llSVZjenpwMDBuUUtMdThvTFVDaXFqVWRLRlZMZExVSW85aFY4SkVSTXN6b3VhN09vcHVleVRxU3h4MlZpR014WTUxQ0NOT1NfQllWWkV0VndTX0J5ZU9sRjVBSkpLOHBVWjJrc1dTRGRaWUE?oc=5>

### Berkshire Hathaway-B (BRK.B) Stock Forecast & Analyst Ratings
- Summary: Analyst ratings and stock forecast for Berkshire Hathaway.
- Date: 2026-11-01 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMipAJBVV95cUxQTUlMNE1FRTVZQjlTWDhkaTI2MUJwZmZnWHh0Tl9YQTRvNWp2cFFmcmNSRWVFOS1XMW9wamJTV2h4dnprMlhKV1djSkwtSTMtZU9ud1VTeWpOX3ZFbU9nUGpGc21mNFVvSXFCZzlCbzVNbEFQOVJkSUZUNUtBWl9nYWF3ZlZMZ0lfalh0ckFRQzRmSV9LcmprNFdNcGpVZjBQNU83N0xaLXZUM2l3dUJZdGp3cEJwTU04QllqajJlcktFbHZuQlpnNjBSS1pnTTB0UzVURlkxb25YUlNQcy0waU4tU0M2X2x1QXQwVk9YanY4NzdtbjluQm9HalNTbHNNbktKR2pKTjA2LVVCNGVEeTZGRl9zNVlQaHN4THUzTkV3Rmd1?oc=5>

## RISKS

### Analysts Estimate Berkshire Hathaway B (BRK.B) to Report a Decline in Earnings: What to Look Out for
- Summary: Forecasts predict a drop in Berkshire’s earnings, potentially affecting investor sentiment.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxNYXlWNjd6V2dkUmdRRHBUMjRSR09JclBRdm9fZGVLcE1iSnZET293bFBLVnJJdm9YNkxtZnJDSnVRVWxZRzhGazJvdnhHbFFtUk95dVJPNDN5YWs3RkRSN1R5MnRXb2lWa2JsNVFjbzJ4QlJ2N1BxelBXM1JSYTRYcjBma19pTktRZmlzR213alhsNXh2b3h4MDh2bXVRUjRMTGU4TTZn?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **BRK-B** | **13.99** | **0.00** | **-1.79** | **10.00** | **1,192,525,168,640.00 USD** | **17.11** |
| MKL | 13.55 | 1.26 | 7.75 | -11.20 | 23,215,982,592.00 USD | -2.90 |
| FFH.TO | 8.84 | 1.36 | 7.94 | -0.50 | 55,680,471,040.00 CAD | 12.08 |
| L | 15.40 | 1.22 | 8.63 | 1.90 | 22,238,709,760.00 USD | 10.87 |

Peers fetched as_of: 2026-11-03; BRK-B reuses existing data (market data as_of: 2026-11-03); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-08
- Next expected earnings: 2026-11-07 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-03

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

- https://news.google.com/rss/articles/CBMirAFBVV95cUxQRm5DaTN3NmRadmh5LVczYXBueVBlUnhtaDZrQ2FGRGtmS0J1WnRkOWcwQ1FmT1pLN0dwQUV2ajRWZENUTGRFRmRBMEpJdjBMbUVmcnB0ZGxRWTNDRWV6RlItbjBfWndhNWVhVVZuWkxWdUY5RnZmU3h5dVlfaXItdEs4NDN5RVdnTFF6RnNBWXZMTExSRUoyS3B6UTNiSE9qbWx2X3VHNVZYRENl?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxQVUV2VG9CYjU2MXh1Um1SbjkyUllBVExtbzhNQkZQVFN4bjdkU0JqenZDZmRoa0VHeHd3ME1CNkxjdjhFNUp5NTdHYWNuTG5oRUkyUzdEVXItNWx4bEpRLUhoREdrbGJISW5WNTdzQWl6ZU1iQXJ5QVRlS0dOWEtNeTdtdVZ5dVV5empvMVlORUMtbF8wT2RDRm14UldBbGE0LUdUeXV3?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxNRnhobGVyclJON2dZSktPb2Q5ei1zV1pxY2ItWTlyMWRkanY1X1Y1UmxRODZwNEtwSlpNZFU0WldKdTNuNFM2a0NPamJVRWNvYWxMU3QyaGxrZ2o1TjYzR1pUU2JyRFRQUDFiSUItYXBkWENVSXY0aUEtUWFyd05sR21qek8xWF9ncHN1YTNSNmQ3ZnFQZXBlYw?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxPWEpBZDRaVGZiU1gyRXdOQ0IwYkFINklhcXpIT1RNVmNHWnFWY2VWNkNFc0N4NDZrSTdmQTREQVFReTJlaV84VUlDOFFIY25hLW1yaGFtamJnQTQyVkxoUkp4ZlN0aGExeTdKLTZNOXNqUUdOTnctQ0dTZldSaFNiY281RTlUY05HRTQtUjBnU0ZKVmpzRzA0M181N3I4VDJHLUY2bA?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNS3EtUEZPZUlYeU9nbjVBS2NfYmlVVTlnOWtCWXhEcjF1cjVOMlZyU1RmOXNHNE15cE5BVVMxNjBDNHduMHF3eEtmZEpvbjJENkUtSjk4aVJmT3RYR0ZmQllZUE5iNXpPejkxdVUzNVlCRlQyNFRlVFh3Mk9LYUR0RDRCX1lSbXhFcDk4Z3dQY3hteFdXMDVlQXo1aw?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxPTmFsNFUtR05QdmdUU1FUclBLWmlBMEN6WndVQ2ltX3F0THczZ2JKSXU2bmlreVN6bW1xTXN5aEtnT09peW9QOEJCTE1OVUxwR2xGWHVEcTVMdHhRZ0xKZlAxN0hJd3Q5ZFNSY2RWUER1YnJsMDhnUWlwcHBtd3Bmc3RRc0NCUXlacmF4ZElrbzVYeUlvbWFFbEVycjhiNzlu0gGgAUFVX3lxTE9OYWw0VS1HTlB2Z1RTUVRyUEtaaUEwQ3pad1VDaW1fcXRMdzNnYkpJdTZuaWt5U3ptbXFNc3loS2dPT2l5b1A4QkJMTU5VTHBHbEZYdURxNUx0eFFnTEpmUDE3SEl3dDlkU1JjZFZQRHVicmwwOGdRaXBwcG13cGZzdFFzQ0JReVpyYXhkSWtvNVh5SW9tYUVsRXJyOGI3OW4?oc=5
- https://news.google.com/rss/articles/CBMigAFBVV95cUxNVVZNekpBdVlkQVhEUGlvb1haWXZhbnliZG5SRmZFc1J1bjZtbVMySUZjQVFNWElKSHhvQjBaWWtod0p5THFaWnZmOEZxR0UwX3hwLUhlZ24zX2RmY2hZTU1EWGo5dDVZak1reUhzdUUtdDBieW9uejB6cERWb1o0ZA?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxQdzg5Z0JmTGJKTXNlaWROTlRkLW5FYkxFN1pNT0dBcE85d1Y5akRqOFBfeWc5MU4xcFAxOU9oWnFIYm40ejNnRkNxUkJsbnVxR2RYb0ZUdzFGZmFNTDB6TDYwOURHbmxZaTJGeU41VXBtWG0yTExhYU1JTlJvQzVORU5KU0lNdzYwQmdsaDVBMGNWMkdNY0dMNTktMA?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxPTGI0X1ZyaHhPM3BJeFBlRmtFZzBuTm9sbXRLdy1aU1BvQXFUOFZCVG1KWTRoNy1pR1N3dV8waExaeEdNRFVWZ3ZPZHRGdUdrQ1FxbWFGNnF1VzlJVlQtVjRidncwYjB3emk2c3FkR2VYM2tSLW5kWXNlcURwMHViZF93MV9GRDNJOGhMTV9OU0lxT3IwcUZueg?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxPbGJfQ2ljcFBDUl81N0lUbjlOTE1nSmhsS1dNQnBZOWt0OXlHZ2J5SGNZQW15bDVSYmU1cjQ2b2dqUTlTdk15QjJ3SWlJV2EwU19xSVZ4OW9YOWJTMzRjaldoci1CUzUtcXdoUHROUUl5bnk4VGpXRHNLNHY0TGgwTlZsenhtcEx3djJQaHpaSGR2UFBTZnhjLVl3?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxOcHQ5LXhDTDB0czloZWlqRTdncFROSEZJc1ZTcXdTcGJ2V0Y5TlY2dlZPbmc3dlk3blZ0VWpRa1dUemtGWmR0WFRvcDVqQUUyUDd5LTM4QXhCVnhfLVpEeGFxLUxaOUdJcjhKZDcxT0dwVi1Rd2NmdktWZGFoN3FKUjgtaUxwSmw2U3pvV0duMk1pUG4wZWx5d3lvMmQ0czA?oc=5
- https://news.google.com/rss/articles/CBMi4AFBVV95cUxQLVAwVlpaYTFxbXV4RmV5RzF2bzExVTdmVFRhdS1YQWVNYjZrSHNma3ZmcTJpY3VlQ0gwYkhQLUc2ZlRYRkhnMm0weDhpX2MwTEZXQU95ZnVqVEh0X3ZQMVJIOUJyWHJfU0t2V1B1SDBqY1V5Wm85a3R1OVQ0QnNySDNiLWh1ZVpNX3I3VlREVzZZa09QWXM0UDlweHVrYmozbzNqekxBc0Q4aXZlVW5Qdk1XaDdSMUlubTlDU2piUUJuTGpFYjBQUWRIbDZadFQ2R3hoTGUxWE1PQ2FKZXdXUw?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxPN3YwV3BBTjFGZ3o1ZlFEaEtickd5U3IycFAzd25tTVQ0TEpkemd4OHJaWkItTkJxZ0lfbEl6b0V4d2lXYVU0OVByOXloNERIZGpoSHYzMW5VNHlXYnhYS0dOSFI4MU9ZS2tLZUY3alJTaDY1WmJVM3FyUmVXdGlCczk4VXlJcUpCV2hRVEx5MGg?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNS3dNQmcyZGI1akpVUTVjVWVRcFVQeGpid0w0QXR2SHdtU2tqRWFaVFJsRWs4OXZxa2V4c1MtTEczUGtrYzl4emFvR0hveVdRb0xUMGRmV3NsdVFISWRScnk5ZWNIWnZiQ1NoNkNKSTFkdjJVVnNKNEhVQ18za0xrT0haQkZNX29JYTlOM2NzQjRYaDNNSEtWaW1PTQ?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxNNFBxTEo5Q1doT1VNaTcyakVXSzFVaFRra3A4NXA1SUNnTjBRbFFzQUJCUU4yNmJ3ZU1iVDdEazkzMDd2eWhrQ2JDWVNCU2l5bzhmZm9BSjlyTlZ4OUlPT0FHZEhwQjVlMFVkcWJwdkJNajB5MzRDSk5vNExSVW5mQ0FCeUwwekV4RWFibG04WmhHb21ZeGxJWmlTeFBlRVZxRk5JdzlNVk42T1RhcDVkUEk3c0Y2QVQxZDdCUDdYZmdpd2s?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxNWmtsSnQteVUwUmxzRWFualBtWDNjc2VLVWdlSUxXYjl4S0R0RHZFMFdJc0llSVZjenpwMDBuUUtMdThvTFVDaXFqVWRLRlZMZExVSW85aFY4SkVSTXN6b3VhN09vcHVleVRxU3h4MlZpR014WTUxQ0NOT1NfQllWWkV0VndTX0J5ZU9sRjVBSkpLOHBVWjJrc1dTRGRaWUE?oc=5
- https://news.google.com/rss/articles/CBMipAJBVV95cUxQTUlMNE1FRTVZQjlTWDhkaTI2MUJwZmZnWHh0Tl9YQTRvNWp2cFFmcmNSRWVFOS1XMW9wamJTV2h4dnprMlhKV1djSkwtSTMtZU9ud1VTeWpOX3ZFbU9nUGpGc21mNFVvSXFCZzlCbzVNbEFQOVJkSUZUNUtBWl9nYWF3ZlZMZ0lfalh0ckFRQzRmSV9LcmprNFdNcGpVZjBQNU83N0xaLXZUM2l3dUJZdGp3cEJwTU04QllqajJlcktFbHZuQlpnNjBSS1pnTTB0UzVURlkxb25YUlNQcy0waU4tU0M2X2x1QXQwVk9YanY4NzdtbjluQm9HalNTbHNNbktKR2pKTjA2LVVCNGVEeTZGRl9zNVlQaHN4THUzTkV3Rmd1?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxNYXlWNjd6V2dkUmdRRHBUMjRSR09JclBRdm9fZGVLcE1iSnZET293bFBLVnJJdm9YNkxtZnJDSnVRVWxZRzhGazJvdnhHbFFtUk95dVJPNDN5YWs3RkRSN1R5MnRXb2lWa2JsNVFjbzJ4QlJ2N1BxelBXM1JSYTRYcjBma19pTktRZmlzR213alhsNXh2b3h4MDh2bXVRUjRMTGU4TTZn?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
