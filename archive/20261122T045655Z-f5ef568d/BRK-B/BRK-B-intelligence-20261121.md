# BRK-B Intelligence Report

- ticker: **BRK-B**
- Report as_of: **2026-11-21**
- Market data as_of: **2026-11-20**
- Quant sources: https://finance.yahoo.com/quote/BRK-B/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/BRK-B/key-statistics/
- AI analysis snapshot as_of: **2026-11-21**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-22T04:57:03.619056+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 23, 'rule': 1, 'ai': 17, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **1** exact headline/source/date matches; prior report **20261120T053808Z-e360129e/BRK-B** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'positive_sentiment_in_headwinds': 1}
- RSS source audit (metadata only, not article fact-checking): 23 unique headlines; 9 named publishers; 2 exact duplicates; 23 HTTPS source links; largest publisher share 43.48%; oldest publication 2026-11-16

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 570.0000 |
| Return 1D (%) | -0.3566 |
| Return 1W (%) | -3.8689 |
| Return 1M (%) | 5.5908 |
| Return YTD (%) | 13.3990 |
| Return 1Y (%) | 13.7452 |
| Annualized volatility (%) | 15.1459 |
| Beta vs SPY | 0.0876 |
| Max drawdown (%) | -9.4218 |
| Sharpe (rf=0) | 0.9294 |
| Downside deviation (rf=0, %) | 10.2423 |
| Sortino (rf=0) | 1.3744 |
| Historical VaR 95% (1D, %) | 1.4206 |
| Historical ES 95% (1D, %) | 2.0519 |
| Correlation vs SPY | 0.0827 |
| Tracking error vs SPY (%) | 19.9489 |
| P/E (trailing) | 15.95 |
| P/B | 0.00 |
| EV/EBITDA | -2.04 |
| Revenue growth (%) | 11.20 |
| Forward P/E (estimate) | 24.98 |
| Gross margin (%) | 26.60 |
| Operating margin (%) | 26.60 |
| Return on equity (%) | 10.57 |
| Free cash flow yield (%) | 4.33 |
| MA50 | 536.8642 |
| Close vs MA50 (%) | 6.1721 |
| MA200 | 502.5689 |
| Close vs MA200 (%) | 13.4173 |
| RSI (14, Wilder) | 56.6048 |
| MACD (12,26) | 12.7999 |
| MACD signal (9) | 15.1127 |
| MACD histogram | -2.3128 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'BRK-B': 287, 'SPY': 287}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 570.0000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.3566 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -3.8689 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 5.5908 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 13.3990 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 13.7452 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 15.1459 -> Low annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 10.2423 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.3744 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.4206 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.0519 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.0827 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 19.9489 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.0876 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -9.4218 -> Shallow peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.9294 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 24.9818 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 26.6020 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 26.6020 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 10.5740 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 4.3332 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 15.9530 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 56.6048 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -2.3128 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 6.1721 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 13.4173 -> Clearly above the moving-average trend level.

## TAILWINDS

### Berkshire Hathaway Is Up 14% in 2026 While the NASDAQ 100 Has Gone Nowhere. Is It Time to Dump Tech Stocks and Buy Berkshire?
- Summary: Berkshire’s strong 2026 performance suggests a favorable investment case.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi-gFBVV95cUxQWVRpSTNremhENnJudzFTeW1WR2owMlFpd0psbERmR2ZTQWtLRTFfMTJSdEJfekVtZ0pGYURiYTRJZVhIY3Y1Zm1qZnIwbU1ELWZlNm9Pbk42NmoyblAxUVBZOW9CYXlUTXNQbVg0aU8tc1kteGloM2F4emt6ZVdub2xRMzZ6VjFJVHRrZTE4R0x2NUFtRjVGWFdDV0RfV3Yzd0lwQmRoUHpVblUyWGpHclVOcjZzSUhBT3JFQXJIb3EzZVE4eU1qLUgzalI5WlpicmhGN2k4eGdTTENKYTJ4VElYc2pLanBfa0s1SG5DMjFjOUVtWEpIV2F3?oc=5>

### Warren Buffett Says Berkshire Will Never Prefer Cash Over Good Businesses. History Says Your Portfolio Shouldn't Either.
- Summary: Buffett emphasizes investing in quality businesses over cash, reinforcing long‑term growth strategy.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxOandVMkcyYUwwQWtUZVNvQWM3WFV3TnhOVlFqZ1ZjWF9nYlNuS1lyUDNFYjlic3B0SmdFX2U4T1oyTXdGdnV5cm5xVk45ckxDQkJmNWw3OEtKenNVVXBkUjNId29mUFplbXRLRF9nVDMtb0NvNWtORmNxUzJ4a3l4VTZBYUkta0g1VlpYc2RQNXVVbDNaQ3QtYkV4T1RFdklFVFE?oc=5>

### The 5 Best Stocks in Berkshire Hathaway’s Portfolio
- Summary: Highlights top holdings in Berkshire’s portfolio, showcasing strong investment choices.
- Date: 2026-11-19 | Impact: high | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiggFBVV95cUxNZm8yVUFHSFRtYkk3Z2U3aktQRExiWXNTRVFjdGVyc1hkRWhxaF9laVUxMkJGaXZzcndPbTd1NnlMRnNnS0xHZHVkTV9TazdaSktRZGNpRTlVWFl3OEdybnlWbTFNb1ZtV19nc1NWbU1pWTZ5M1lxVmROU0M4R01qRnRB?oc=5>

### Tracking Berkshire Hathaway Portfolio – Q3 2026 Update (NYSE:BRK.A)
- Summary: Provides quarterly update on Berkshire’s portfolio performance and holdings.
- Date: 2026-11-17 | Impact: high | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQM19sV01OdFRtLUprWElVYlNtcVE5bG1YMjBpNmU2Z1RXU2VNMFlUNEF1Tk1CV2E2NXFlRC14eUZxTHlpb1pjRlhxczBhVEstRHlDU0FlY1IxODlhZFNYM3oyb3RucXJCYWtLRmNQRW54RnFiTkpqNU91dnM2UEN3cGZmc09BcGJ3c3hadXpqNVFsVk1ILUFvRg?oc=5>

### If You'd Invested $1,000 in Berkshire Hathaway (BRKB) Stock 20 Years Ago, Here's How Much You'd Have Today
- Summary: Shows long-term growth of Berkshire stock, illustrating significant returns.
- Date: 2026-11-18 | Impact: high | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxPaVE4aWVGM0NzRnJNTW5XYVVfbUZRSU9RTllBU1hWbUpKYS1HLXh1aHVLLUNsSmMtR1k0QmZSMUd2akFkOTh2cFFKREd6TUh1UWcyRDVzaVZQNVdlX1JaQUNhTVNfV3piQXIyY3hJRGhuZENnSjBqT08xUUt5WEZoR3BCaTdBTmF1anBvSmNfaG9qQUhXZVFjMg?oc=5>

### Warren Buffett quadruples Thanksgiving gifts: A breakdown of how much wealth he's giving away
- Summary: Details Buffett’s charitable gifts, reflecting philanthropic impact.
- Date: 2026-11-21 | Impact: high | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiiAFBVV95cUxNY0V5NkR5YWNCdWIxLU5xaUVpYU1iekc2OG1oMWh0OFBuRWs2Y0NaSXlpenNrSE5XdmFuLTM3RGZPMHphOUp5dlh2cUZtajNyY2I1aV9va0Z2Sk1kVE5TeG9fdkdINnlwQnBrSThxVUwwX2pwY2VhcGc3aXZGQ3Y4TXpCYXJGZl9z0gGOAUFVX3lxTE9ibnFmenJ0M1NEdDQxTWFBWkpDaER1ZHN0QVZCa3pERGFDeld3QzdCMC1DM0FkVllURjZOVmtSc2pWMmRCSkpxdUk3a3JCZ3dXQVUtMUZCQnFJNDZYb0Q1bEZNQldEbkwyTVBncTk1OWVuYWtHLUV3c0pwUW9WZEc0OWlweEVwZDltZmhoMVE?oc=5>

### Berkshire Hathaway Hits an All-Time High: Here’s What $10,000 Invested a Year Ago Is Worth Now
- Summary: Reports record high stock price and investment value growth.
- Date: 2026-11-16 | Impact: high | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxNd0hqNy1GWDNUU1BxVHhjYkpxOUVDTTFKczBzc3hMNFA3LTNWOExfRXJSOTlnSTJlLTZWQTZNeFZFR3kyazZIT3otRWxoRDB3d2hWQWNzYklLZFlLM2JlLUs1WmEtcVhKblhFS1locGdsSEZhNl9TandTUlUyR0pRSVZRNGhUMmhESUdfVEVpTmljZUJ4RldiSXpRTEFGMEU?oc=5>

## HEADWINDS

### Berkshire almost doubles stake in tumbling housing stock
- Summary: Berkshire almost doubles stake in tumbling housing stock
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxOMERPMWdJQlAwVjFiTXVsd294dVUxeTQzdXh1WjhIX0hnMjJxNFJyN0hJaTBNLUVPMkd3MHZJVFpuejFIMnNodmM3azd5d0tNb0hOR3E0ZnJQYUFfR05jSmUyN1hkbzlsak0wRkh3UHpVQ2VGYjNKQlFCNUVsbEswc29relZlVm40d1o1ekVwMUI5Z1hDZG42eElWN2I1MFNaNGNqVUpoUXM4RUU?oc=5>

### Berkshire Hathaway has been a popular 'anti-AI trade.' One firm says it’s too expensive now
- Summary: Critics view Berkshire’s valuation as high, dampening enthusiasm.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxPOXBfRjdkSEpHSTJ3b2o3dUttNFRyRU1OVVExLWVSWmV6M2FDUWNKVFl1dERwUFFoSGdiUkIwZk9UODRaQjEzbFpaODJnYmRiZXVlcjJKMFBkdGhvcUpLcHFjMVBIX19tLXNZS2NCanJXN2FzQmQ5RlRrREtzN1dZMGFIUDRfYjVWS0oySnFQdjVRbEZhZUp2bnlTZzZPUTVDdXJKSGhfUV9ZQVVXWmRDUkE3cm1JVDgzRzlFbmRuZkVWQQ?oc=5>

### Berkshire Hathaway Is Up 18% in 3 Months. Its General Counsel Just Bought $250,000 More
- Summary: Insider buying and stock rise noted.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxOZkdCTkJQSGN4aEY1ekRsbzNIUGFKSmpjX3did2NNdWtKSGRBbS1HaXpRRDEzd0k1cWpodkwyRE5UU3lHMEI5T2lubUZBZnhVQ2lpMFBzMWV6M2ExOURYMktOWGtMRXdPNDY0a1Z1RTZGV2w4UHdUSVEyNWkyMWdkYkNiTGRUSjhBZWJPWXcySi1yeGJ6UE5DVExxeDN0MUgwZTRWUWVpTF9rR3U3Z3c?oc=5>

### Warren Buffett Expects Berkshire Hathaway (BRKA, BRKB) Stock to Drop About 50% Again Someday. Here's What He Says to Do Then.
- Summary: Buffett warns of a potential 50% drop in Berkshire stock, advising future actions.
- Date: 2026-11-19 | Impact: high | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxQV1FWcTNHWTNfd3pnSmZ2MUJYWXpaWm0taXI3TFE5bmRyV041UjVRSUFiYmF6SENLYVV3ZWZiM2pZZ3FISlNUeS13MDhSaWdOVW10M09XVWVJVDllSkFaby1YYm9hZElMM1huZlU1OEJINmc4Z29QZC12Ri1hUThsWmc3TmdueXNoN3dYWlc0TTRHcDMyX1FjVVA1a21jelVzVmJmZU9LTTZwUQ?oc=5>

## CATALYSTS

### Buffett's Berkshire trims stake in surging 143-year-old retailer
- Summary: Berkshire reduces its holding in a growing retailer, indicating a strategic shift.
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxPbFk3alQ2cFJYUjlHVVo4SWQyUXlEN0FWOVRlM3ppUmJTWW5NNmU3U2FJclBSZGdqeVBqczJuNFBVb2NzMUd4ZjdHSzFQWVo4cl9DZ2hNU0FmazJRcHR5NWlBZTVlam9pT2g2dkd6dmpqbl9xUV95YVVWanI4VG83aWxGSGRpRzZuc0puUHhnTUdYMUtKc25vZ3FsWkM1VjZ4X3pNSjlB?oc=5>

### Forget Apple. Warren Buffett’s Berkshire Is Pouring Nearly $1 Billion Into This Little-Known Tech Stock.
- Summary: Berkshire invests almost $1B in a small tech company.
- Date: 2026-11-19 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMi3AFBVV95cUxNNkJQLVk5VVlHT1dtNGdncEF5NURIQ01zRFE5VmV6c0NUYTM5N0dlOXJqOWxlaUt2dVBkUEtkZ2VWS1M3Yk1SRXllVnNQZEtmcTQwclhTTS12dmhoOE1nNXNyc0FOS2ZNNmlQSUl6bnVBMC1ER0MwMW1acnhRSC1SWXZ5WVNMekVURm11aHFQYy1nOHMtYnFIbmFlZThqeE1Cb1lNbnY5eHdUeUstWFBNMGhHMzdQQUFLdllqU3dJX0dhbEo0dDk2WjRmbzVrRVN1elp1TlM3UTlvYzl6?oc=5>

### Warren Buffett's Successor, Greg Abel, Has 31% of Berkshire Hathaway's $363 Billion Portfolio Invested in 3 Game-Changing AI Stocks
- Summary: Abel’s significant AI investment signals strategic focus on high‑growth tech.
- Date: 2026-11-20 | Impact: high | Horizon: medium | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxNRFRLbE10Rlg2alFJOC10OXotVDNqS0I4dDlHYjU5bFhGSzc1YVlVWmZleXBYbHVKdGhsRkIydWNIdW9aZzdaN2oybjZ6WlM4Q1BIUTZrajREZGNDcGw4WHpmUTBsaVp3QWhLVFBadWQ1VmtSbUt1T0plR1FEclk0VVNXRDVIbzdlT2JSME1Nd2JxVkxVcHN5OEZHVV8zUlBy?oc=5>

### Warren Buffett Has Backed This Consumer Stock for Decades, and Greg Abel Is Still Holding It. Here's Why It's a Buy in November.
- Summary: Continued support for a consumer stock highlights confidence in its long‑term prospects.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxQWnFtaVlwaGRxS1RTbEwtSU00TmtoY3pCVVgwV0Q3bVhNNHZSclNkNVRhS2dxRmt0R3hlckxNOF9ReG9hdDRGalpxQ1NDcWY5SU1MOGlIb0hCbTUzNnNISGc0N2hNcHFzSlQyNENjcGZJdXFqRHdhRFBGbkg2YmxSRk41VVhJN2JJeHJSY2wxWkxYYXRQUy1RQVhFYkpTZVNSOThJ?oc=5>

### Warren Buffett Stopped Giving Bill Gates's Foundation Berkshire Shares. It Just Sold $1 Billion More and Bought a Dollar Store. Here's When the Rest Runs Out
- Summary: Shift in holdings: selling shares and buying a dollar store indicates portfolio realignment.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogJBVV95cUxPMDV2NFVXb1VsQmVXTnd5bW5YcjZ5eXVzQXJ0OElqMXV3T3I4OUJsdTRPZmdPc3B0TG4xenBwWGU3cFA2eERhSDJJdUFHT0xLOG5NR0F1T2lOb1BUazRGcUE0OFdUV3QyN184X2hvTm8tVGdndGZ0ZDdzUjA4aGxHQUd0ajhMY3phOUllRFZEX25EWHI4V2V3V0ZqcUp0SmlqQUM4SHZ5M0hVZUgzOHQ3YW0wVjZ5V2R0ek91c3J2XzZWTHNmSnBBbllvZ3JwZUQ2emxJOW1zdkF2UTlRaFN2ZjF2TVpPTHV5NnkwcHU5VjE5LUdpNUg4ZFdHM2tWMG1sa3ZZT2JTcFM0Um4zS09XWnltQl81WVllX01mdXFra0xhUQ?oc=5>

### Greg Abel Just Approved a Record $9.6 Billion in Stock Buybacks for Berkshire Hathaway Last Quarter, More Than Double the Pace Set in the Second Quarter. Is Berkshire Still a Buy as Shares Sit Near All-Time Highs?
- Summary: Berkshire Hathaway approved $9.6B in stock buybacks, double Q2 pace, signaling confidence and shareholder value focus.
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxQVVJjLU5QcVZ4WWF1RmRSMXFjY1lSY0x2UkdxRXYxY3JSQzBjRkowOWFMQTU4QWVlNDJZd3gwMTRlWUNnSk5DdEE0cVBHTDlYaXgwUG03a05FOEpITWpoWWhQNHNLZFdHZDRSYUFMcGlQMjdTMVlnTDBZaFRSVm1hWkV6TmN0a3d1cU9JTGVHU3hYaHkzMU5ERUNOTQ?oc=5>

## RISKS

### Berkshire Hathaway Stock Gets Downgraded After ‘Anti-AI’ Rally – Here’s Why
- Summary: Downgrade due to anti-AI rally concerns.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxQUFJZb256Q2xRQTJvVUJLRlJwcjJZbjM2N05NVlVwZGxJaVA4dUpWUHlJNHJuTlZGWWxtVGZ1eUVIRmxXM3JtMVVMQnowdmdvVEg4S0FhRjk0VDg4blAxRmNSbks3cmdObHhzM3JKNW9STlFLZmtzQUtoSkEyZ0VDN3NYZDdfT2hkRFJBQTBHUWp1QVV6V3l5NGlQR3pJYUJ2U2c?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **BRK-B** | **15.95** | **0.00** | **-2.04** | **11.20** | **1,210,976,043,008.00 USD** | **13.75** |
| MKL | 13.78 | 1.28 | 7.92 | -11.20 | 23,683,143,680.00 USD | -5.08 |
| FFH.TO | 9.59 | 1.39 | 8.54 | 1.90 | 54,538,334,208.00 CAD | 12.10 |
| L | 15.13 | 1.21 | 8.59 | 1.90 | 22,123,440,128.00 USD | 4.49 |

Peers fetched as_of: 2026-11-21; BRK-B reuses existing data (market data as_of: 2026-11-20); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-07
- Next expected earnings: 2027-03-01 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-21

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

- https://news.google.com/rss/articles/CBMi-gFBVV95cUxQWVRpSTNremhENnJudzFTeW1WR2owMlFpd0psbERmR2ZTQWtLRTFfMTJSdEJfekVtZ0pGYURiYTRJZVhIY3Y1Zm1qZnIwbU1ELWZlNm9Pbk42NmoyblAxUVBZOW9CYXlUTXNQbVg0aU8tc1kteGloM2F4emt6ZVdub2xRMzZ6VjFJVHRrZTE4R0x2NUFtRjVGWFdDV0RfV3Yzd0lwQmRoUHpVblUyWGpHclVOcjZzSUhBT3JFQXJIb3EzZVE4eU1qLUgzalI5WlpicmhGN2k4eGdTTENKYTJ4VElYc2pLanBfa0s1SG5DMjFjOUVtWEpIV2F3?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxOandVMkcyYUwwQWtUZVNvQWM3WFV3TnhOVlFqZ1ZjWF9nYlNuS1lyUDNFYjlic3B0SmdFX2U4T1oyTXdGdnV5cm5xVk45ckxDQkJmNWw3OEtKenNVVXBkUjNId29mUFplbXRLRF9nVDMtb0NvNWtORmNxUzJ4a3l4VTZBYUkta0g1VlpYc2RQNXVVbDNaQ3QtYkV4T1RFdklFVFE?oc=5
- https://news.google.com/rss/articles/CBMiggFBVV95cUxNZm8yVUFHSFRtYkk3Z2U3aktQRExiWXNTRVFjdGVyc1hkRWhxaF9laVUxMkJGaXZzcndPbTd1NnlMRnNnS0xHZHVkTV9TazdaSktRZGNpRTlVWFl3OEdybnlWbTFNb1ZtV19nc1NWbU1pWTZ5M1lxVmROU0M4R01qRnRB?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQM19sV01OdFRtLUprWElVYlNtcVE5bG1YMjBpNmU2Z1RXU2VNMFlUNEF1Tk1CV2E2NXFlRC14eUZxTHlpb1pjRlhxczBhVEstRHlDU0FlY1IxODlhZFNYM3oyb3RucXJCYWtLRmNQRW54RnFiTkpqNU91dnM2UEN3cGZmc09BcGJ3c3hadXpqNVFsVk1ILUFvRg?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxPaVE4aWVGM0NzRnJNTW5XYVVfbUZRSU9RTllBU1hWbUpKYS1HLXh1aHVLLUNsSmMtR1k0QmZSMUd2akFkOTh2cFFKREd6TUh1UWcyRDVzaVZQNVdlX1JaQUNhTVNfV3piQXIyY3hJRGhuZENnSjBqT08xUUt5WEZoR3BCaTdBTmF1anBvSmNfaG9qQUhXZVFjMg?oc=5
- https://news.google.com/rss/articles/CBMiiAFBVV95cUxNY0V5NkR5YWNCdWIxLU5xaUVpYU1iekc2OG1oMWh0OFBuRWs2Y0NaSXlpenNrSE5XdmFuLTM3RGZPMHphOUp5dlh2cUZtajNyY2I1aV9va0Z2Sk1kVE5TeG9fdkdINnlwQnBrSThxVUwwX2pwY2VhcGc3aXZGQ3Y4TXpCYXJGZl9z0gGOAUFVX3lxTE9ibnFmenJ0M1NEdDQxTWFBWkpDaER1ZHN0QVZCa3pERGFDeld3QzdCMC1DM0FkVllURjZOVmtSc2pWMmRCSkpxdUk3a3JCZ3dXQVUtMUZCQnFJNDZYb0Q1bEZNQldEbkwyTVBncTk1OWVuYWtHLUV3c0pwUW9WZEc0OWlweEVwZDltZmhoMVE?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxNd0hqNy1GWDNUU1BxVHhjYkpxOUVDTTFKczBzc3hMNFA3LTNWOExfRXJSOTlnSTJlLTZWQTZNeFZFR3kyazZIT3otRWxoRDB3d2hWQWNzYklLZFlLM2JlLUs1WmEtcVhKblhFS1locGdsSEZhNl9TandTUlUyR0pRSVZRNGhUMmhESUdfVEVpTmljZUJ4RldiSXpRTEFGMEU?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxOMERPMWdJQlAwVjFiTXVsd294dVUxeTQzdXh1WjhIX0hnMjJxNFJyN0hJaTBNLUVPMkd3MHZJVFpuejFIMnNodmM3azd5d0tNb0hOR3E0ZnJQYUFfR05jSmUyN1hkbzlsak0wRkh3UHpVQ2VGYjNKQlFCNUVsbEswc29relZlVm40d1o1ekVwMUI5Z1hDZG42eElWN2I1MFNaNGNqVUpoUXM4RUU?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxPOXBfRjdkSEpHSTJ3b2o3dUttNFRyRU1OVVExLWVSWmV6M2FDUWNKVFl1dERwUFFoSGdiUkIwZk9UODRaQjEzbFpaODJnYmRiZXVlcjJKMFBkdGhvcUpLcHFjMVBIX19tLXNZS2NCanJXN2FzQmQ5RlRrREtzN1dZMGFIUDRfYjVWS0oySnFQdjVRbEZhZUp2bnlTZzZPUTVDdXJKSGhfUV9ZQVVXWmRDUkE3cm1JVDgzRzlFbmRuZkVWQQ?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxOZkdCTkJQSGN4aEY1ekRsbzNIUGFKSmpjX3did2NNdWtKSGRBbS1HaXpRRDEzd0k1cWpodkwyRE5UU3lHMEI5T2lubUZBZnhVQ2lpMFBzMWV6M2ExOURYMktOWGtMRXdPNDY0a1Z1RTZGV2w4UHdUSVEyNWkyMWdkYkNiTGRUSjhBZWJPWXcySi1yeGJ6UE5DVExxeDN0MUgwZTRWUWVpTF9rR3U3Z3c?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxQV1FWcTNHWTNfd3pnSmZ2MUJYWXpaWm0taXI3TFE5bmRyV041UjVRSUFiYmF6SENLYVV3ZWZiM2pZZ3FISlNUeS13MDhSaWdOVW10M09XVWVJVDllSkFaby1YYm9hZElMM1huZlU1OEJINmc4Z29QZC12Ri1hUThsWmc3TmdueXNoN3dYWlc0TTRHcDMyX1FjVVA1a21jelVzVmJmZU9LTTZwUQ?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxPa1lzNGRJZmZXMG9yOG1XaWVBRXRycW1pTXU5SXE2Z0JBbDVLUXpDQTdoREJSbENSOGFlZGwtck9xMkNzbWpwbXBCZXlXWU5MSDFET1gxM3NxWG5xalA1NUM5T0RhcjFwTWZiSEJyVjN1akZXZzVhem92blQ1X3BFeUo2cUp2N24yNmY0STBNeEVrT2RqcFRidQ?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxPbFk3alQ2cFJYUjlHVVo4SWQyUXlEN0FWOVRlM3ppUmJTWW5NNmU3U2FJclBSZGdqeVBqczJuNFBVb2NzMUd4ZjdHSzFQWVo4cl9DZ2hNU0FmazJRcHR5NWlBZTVlam9pT2g2dkd6dmpqbl9xUV95YVVWanI4VG83aWxGSGRpRzZuc0puUHhnTUdYMUtKc25vZ3FsWkM1VjZ4X3pNSjlB?oc=5
- https://news.google.com/rss/articles/CBMi3AFBVV95cUxNNkJQLVk5VVlHT1dtNGdncEF5NURIQ01zRFE5VmV6c0NUYTM5N0dlOXJqOWxlaUt2dVBkUEtkZ2VWS1M3Yk1SRXllVnNQZEtmcTQwclhTTS12dmhoOE1nNXNyc0FOS2ZNNmlQSUl6bnVBMC1ER0MwMW1acnhRSC1SWXZ5WVNMekVURm11aHFQYy1nOHMtYnFIbmFlZThqeE1Cb1lNbnY5eHdUeUstWFBNMGhHMzdQQUFLdllqU3dJX0dhbEo0dDk2WjRmbzVrRVN1elp1TlM3UTlvYzl6?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxNRFRLbE10Rlg2alFJOC10OXotVDNqS0I4dDlHYjU5bFhGSzc1YVlVWmZleXBYbHVKdGhsRkIydWNIdW9aZzdaN2oybjZ6WlM4Q1BIUTZrajREZGNDcGw4WHpmUTBsaVp3QWhLVFBadWQ1VmtSbUt1T0plR1FEclk0VVNXRDVIbzdlT2JSME1Nd2JxVkxVcHN5OEZHVV8zUlBy?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxQWnFtaVlwaGRxS1RTbEwtSU00TmtoY3pCVVgwV0Q3bVhNNHZSclNkNVRhS2dxRmt0R3hlckxNOF9ReG9hdDRGalpxQ1NDcWY5SU1MOGlIb0hCbTUzNnNISGc0N2hNcHFzSlQyNENjcGZJdXFqRHdhRFBGbkg2YmxSRk41VVhJN2JJeHJSY2wxWkxYYXRQUy1RQVhFYkpTZVNSOThJ?oc=5
- https://news.google.com/rss/articles/CBMiogJBVV95cUxPMDV2NFVXb1VsQmVXTnd5bW5YcjZ5eXVzQXJ0OElqMXV3T3I4OUJsdTRPZmdPc3B0TG4xenBwWGU3cFA2eERhSDJJdUFHT0xLOG5NR0F1T2lOb1BUazRGcUE0OFdUV3QyN184X2hvTm8tVGdndGZ0ZDdzUjA4aGxHQUd0ajhMY3phOUllRFZEX25EWHI4V2V3V0ZqcUp0SmlqQUM4SHZ5M0hVZUgzOHQ3YW0wVjZ5V2R0ek91c3J2XzZWTHNmSnBBbllvZ3JwZUQ2emxJOW1zdkF2UTlRaFN2ZjF2TVpPTHV5NnkwcHU5VjE5LUdpNUg4ZFdHM2tWMG1sa3ZZT2JTcFM0Um4zS09XWnltQl81WVllX01mdXFra0xhUQ?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxQVVJjLU5QcVZ4WWF1RmRSMXFjY1lSY0x2UkdxRXYxY3JSQzBjRkowOWFMQTU4QWVlNDJZd3gwMTRlWUNnSk5DdEE0cVBHTDlYaXgwUG03a05FOEpITWpoWWhQNHNLZFdHZDRSYUFMcGlQMjdTMVlnTDBZaFRSVm1hWkV6TmN0a3d1cU9JTGVHU3hYaHkzMU5ERUNOTQ?oc=5
- https://news.google.com/rss/articles/CBMi3AJBVV95cUxPVUtsOWFTb09lRFJVdlFCTXRLWG9maGNrNFVsTTlhdGNjT0FIaWtCNGhDUElGY3FOSHVWNHJRd0dlZ2FGbk10Q0E4eGt4eV9IdEpHNkdacDdYbURIaXVIWW9TcFVOSmFWSzV5VWJ6aXctNTQxNHpyUkppYWZVdHNNTjdlT0NCRTZpX2tjYV9YcTNwS0RTS1NBekFQT2lsQXBZM2twUmt6MG5NOUZrcHZRcVIxdXgwejBoQkducWFQR0pacXJIUzlfY2JGeHpDQm55a09YQTUxc3NwNGJXOWppRzlaSGVpc2hsT3hGdlRvRWhaNlRheXpadERmdUVMUDR4QmpFWkN4MUtVQUQ0RkJPVnNLMVhVNklhbFFkOVFlVFhGMFhCLUFOVTlldlJoNld5NzcwWGhUVFlSWDBCUHpHOF92Z3hnc0Y2NmxQbXAtYkhVUjBTSGxRS1plU08?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxQUFJZb256Q2xRQTJvVUJLRlJwcjJZbjM2N05NVlVwZGxJaVA4dUpWUHlJNHJuTlZGWWxtVGZ1eUVIRmxXM3JtMVVMQnowdmdvVEg4S0FhRjk0VDg4blAxRmNSbks3cmdObHhzM3JKNW9STlFLZmtzQUtoSkEyZ0VDN3NYZDdfT2hkRFJBQTBHUWp1QVV6V3l5NGlQR3pJYUJ2U2c?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
