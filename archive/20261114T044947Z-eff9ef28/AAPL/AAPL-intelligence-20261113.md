# AAPL Intelligence Report

- ticker: **AAPL**
- Report as_of: **2026-11-13**
- Market data as_of: **2026-11-13**
- Quant sources: https://finance.yahoo.com/quote/AAPL/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AAPL/key-statistics/
- AI analysis snapshot as_of: **2026-11-13**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-14T05:10:20.546620+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 5, 'ai': 19, 'unknown': 0, 'irrelevant': 1})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **13** exact headline/source/date matches; prior report **20261113T045636Z-34122c9a/AAPL** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **10**; {'directional_claim_without_event_type': 6, 'low_uncalibrated_model_confidence': 4}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 9 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 36.0%; oldest publication 2026-11-08

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 356.2700 |
| Return 1D (%) | 0.3917 |
| Return 1W (%) | 4.1390 |
| Return 1M (%) | 4.4747 |
| Return YTD (%) | 31.5056 |
| Return 1Y (%) | 30.9805 |
| Annualized volatility (%) | 24.9329 |
| Beta vs SPY | 0.6218 |
| Max drawdown (%) | -13.7985 |
| Sharpe (rf=0) | 1.2119 |
| Downside deviation (rf=0, %) | 16.9417 |
| Sortino (rf=0) | 1.7835 |
| Historical VaR 95% (1D, %) | 2.0034 |
| Historical ES 95% (1D, %) | 3.4742 |
| Correlation vs SPY | 0.3400 |
| Tracking error vs SPY (%) | 24.0081 |
| P/E (trailing) | 39.50 |
| P/B | 46.19 |
| EV/EBITDA | 30.41 |
| Revenue growth (%) | 11.70 |
| Forward P/E (estimate) | 33.70 |
| Gross margin (%) | 48.79 |
| Operating margin (%) | 33.01 |
| Return on equity (%) | 142.26 |
| Free cash flow yield (%) | 2.04 |
| MA50 | 338.7898 |
| Close vs MA50 (%) | 5.1596 |
| MA200 | 300.7746 |
| Close vs MA200 (%) | 18.4508 |
| RSI (14, Wilder) | 60.9028 |
| MACD (12,26) | 4.2090 |
| MACD signal (9) | 3.2900 |
| MACD histogram | 0.9191 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AAPL': 282, 'SPY': 282}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 356.2700 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.3917 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 4.1390 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 4.4747 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 31.5056 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 30.9805 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 24.9329 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 16.9417 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.7835 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.0034 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.4742 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.3400 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 24.0081 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.6218 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -13.7985 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.2119 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 33.7009 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 48.7860 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 33.0100 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 142.2570 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.0408 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 39.4978 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 60.9028 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.9191 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 5.1596 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 18.4508 -> Clearly above the moving-average trend level.

## TAILWINDS

### Apple Stock Called ‘Safe Haven,’ Hits Record High
- Summary: Apple Stock Called ‘Safe Haven,’ Hits Record High
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxQSjNua2NKRWx2ckNtazhaanloVXE0b3padGZlSnlfSDBXLURWYmM4Tm9xUWlmaWxqaXJsN3JQekh6YmtWcEFPRGJBVGYzdDFDVTdsYWpMSUhuSERxbGhFaWM3LWVvV2RvRGZocmwxLWlTWFhIemg0V0piMTJOVGpzUk5CeTRjQmR4YmdTaXVOSF9feUk?oc=5>

### Apple Shares (AAPL) Look Expensive Heading into 2027
- Summary: Analysis of Apple shares’ valuation approaching 2027.
- Date: 2026-11-11 | Impact: low | Horizon: long | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxOM2lsenhVYnFXTUNRUHVQUkVxVEVMUDNwSzdFcDNnNWNRU3F2dDVGTHh2Zkh1N2laS1FtZHdzb2hQN3B6bHhrcUUxa2VFOWxzY1NlZTVwRFB5YkE4MGxjUHBueG1WQjRjUExnanJaZGZFSTQzX1Y0YTU3bmJ6UGNZYjNyaVdPenFDZHVhU0JlMUZySFBONHVDU2wxNnNIUQ?oc=5>

### What's Going On With Apple Stock Wednesday?
- Summary: A discussion of Apple’s current stock performance and market factors.
- Date: 2026-11-11 | Impact: low | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxOdW5ZN2QxY2xIN3lFT1dqRWx3dUxLYVlieklHV2IyVVVnVEJFZkNnWE83Q1JtV1Y3ZUcwWE0tcy13YmRMNmxDa0NmNlNWaDJYSFBJT3Uyd1RhblBSc1Jjenp1UFFZdWNCVTV4TlBBMHFYa2h6N2xGNG9PMm9lU2tpbnA3dk11MVB1MGFXTTZJTUhZMXVQU0RaLV90MEg?oc=5>

### What Is Going on With Apple Stock on Thursday?
- Summary: Discussion of Apple stock movements on a specific day.
- Date: 2026-11-12 | Impact: low | Horizon: short | Confidence: 0.5
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxON1hYY01mSnpmdUdVUVFPdG84eGc1R2JnZC1VTDVFYkRRQ0ZMNmFXTktyTm1LZHdDejUzTURxcVFQQ1kyUDFoT25jeXJYX1NTRzRNYldGZVpJWmw1dVVDQ203ckhQeUU1OGM5aVFGSkhwWFZQQVF2ZEtlbW1TU3hoMHgxQThqM3hObk1KN0c3VjQzckVlaURrVlVkdTFWTjdkQ2c?oc=5>

### Apple Inc. (AAPL) Rallied 15% as Investors Reassessed Its Growth: What’s Next for the Stock?
- Summary: Apple shares surged 15% after investors reassessed growth prospects.
- Date: 2026-11-10 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxQOTluMHhsdUl2LXpHekdlOUZIWmFHQ0t5M3c1LTJaNm9uUU9ENHJlQ25BNzN6SFJaaXd5NVE0SlJtMEl2UHBhNnllV0JXVS1GRGhJWUdEMjBxT1RhRDBwTmo1R2hnNTZpOVpPb3Z4YVl0My0tQTc0NTZMZzZKTnpGOHlNYXUtd252c3NSOE9vMFhybUc4?oc=5>

### Apple (AAPL) Sees $460.3 Million in Net ETF Buying on Nov. 10
- Summary: Apple reports significant net ETF buying, indicating strong investor demand.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxOdDJER0dOZTdtdWwxU1FtekJMOFl1MVhYbDhHQ044RjB2NlVza1NDaUNRUVZMTGtLTlM4b19KTmZHazlrcXV4VTgtX0NSSldrU0hTVWl0Y05wdzlLXzRxUXFEVk01RTh0ZVBFQ0RKcVQtV2tsb2dsQ21RUEE1YVlXTjNORnd2RVJmaWU4RWRYYw?oc=5>

### Drama Notable Only By Its Absence: Why Investors Love Apple (NASDAQ:AAPL)
- Summary: Exploration of investor sentiment toward Apple amid market calm.
- Date: 2026-11-12 | Impact: low | Horizon: short | Confidence: 0.5
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxNWDQtTm5fUUhEZ1R2UnlWV3NrZnF0alhzalJBWFloTG5ucFJRZldRdTc5T2p2ZUI1X0Q5U0JlcHF3VEtWOFRFUnlDSzR2cTlER09HQWNUX2gwTWRtS2ZXLXQtNEJ2a1hGOXhsb0ZQS2l3MmNpeF81U3hmLW0zMnBoWUtLT29KUGI2YTJBdDJZZkZOOEthYXFhamYzSUJseTcw?oc=5>

### Apple: Capex-Light AI Amid Regulatory Uncertainty (Rating Upgrade)
- Summary: Apple’s rating upgrade signals confidence in its AI strategy amid regulatory uncertainty.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxQZTA4SG95UkQwOXZ5amtHTXJlT0ZsNE5lejVQZDBudkFRS1BsbVo2WjV4a1cwYUNvVUdfZ1dKZTBJZHZIRUh0Y3hCc1BPd2hFU0FXd3VKTDhnNGdoYUxhMjNHUHpWcFNPcDh3WWtZdGJpNlZ0eThnNVZmU0hGb2lFdEdSTDdJWS0zSmQ1MlFDTHYzanRNSVRFX1RvVTZwQnBJMXVyR0tsUVFxb0JxSkc4?oc=5>

### Apple: Deserves Costco's Multiple (Rating Upgrade) (NASDAQ:AAPL)
- Summary: Analysis of Apple’s valuation relative to Costco with a rating upgrade.
- Date: 2026-11-12 | Impact: low | Horizon: short | Confidence: 0.5
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxNX1Q3Q0ppRGVaRnZnZmo0ekF1V3FUZkh0YTEwVXhYX2REUGIteGNjaTl2a2szb21zQkd3eEdMOHdlYlhhNFMzeVlIbWQwbFk1VFdHckxmQW9qcExZSlQ2S1UtTGJleWZEQ28yRHF5OGZUbVZQOGs3UHRtT3pVSDNVSTZzdVVicEFkV0VhOXBMczA?oc=5>

### Apple (AAPL) Stock: $348.51, Down 0.62% Nov 10
- Summary: Current Apple stock price and recent decline.
- Date: 2026-11-11 | Impact: low | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxOMUpaWVdPaHVGd2dQLXBWZHo0TXpUYWthUWxrUnYzNHg4TzRGWWZaVEl6dEpFaEQ0M3F0VmtqeTZ5YkpMNkthTDUtbWg5bXNZMXpLRnJBUUNzRHQwM09CVF9YSURjYjlGem9lOS1WVHhoZjRuLURYdUFEYWpndWtnOGhOY0dkX3JPT3FzcWtVZXdpM3ZDQzZEOGJSZkRaVHc?oc=5>

### Apple Is Above $5 Trillion After Its First-Ever Close Above $350
- Summary: Apple's market cap surpassed $5 trillion following a record close above $350.
- Date: 2026-11-10 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxPeDE2Yk1XT0NWbHpadlh6V3ZYc3hwOTQxWFQ2V0lfcUJoY3JEM2hrRk0yMnI2b0dfN3lxZUJHcURsdVBlVzVjMkt4N1A1MnhkckpWb2lOTndwZUF3MVZsUW1vN2pZV3ZZOVFtNjh3MTh1bWpYaHJNVzVGNWJWTDlUMnhKMXVuamtpWHFKanZ1TnNOR3owbE1QU1JZQm9zN2x4eTN6dVRZS0J1dw?oc=5>

### AAPL Stock Quote Price and Forecast
- Summary: Apple stock price and forecast analysis.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiUEFVX3lxTE00U3JoRzhkckt5aVFxb1NVNnBndWhrcDM5N0NqUzZGUk8xQk04OF9jVWRULXh2RmlJaGpTS1FJWEREaUlNUnhfSHk2cm53NllX?oc=5>

### Apple Is the World’s Largest Company, and Nvidia Is Second. Here’s What $10,000 Invested in Each Today Could Be Worth by the End of Next Year.
- Summary: Apple remains largest company; comparison with Nvidia.
- Date: 2026-11-13 | Impact: low | Horizon: long | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMi_gFBVV95cUxNWVJhZDJfcFlqSnN2N25TRHpLazhkbE9GRFBWODJkaGVYd3FNZzRjR0prczZNcGdVV2djMVo5bHM0ZFd2djIzYlFkVFBQUk9KYjBuSFpVTExPQjRPT2pSd2Y4TFJlaE5wUHhBdDZUbnZUQXpGNG9lY2hkdWxDVnZ4aDl2bmxtVnI0WWZDaHUybEV3RU9GaGdhSWhGMG9JWnk5NkZCazk4d01uTlRBLVNnRGptVEotdXRFS05oY0tuV3U0d2gtaHFLaVJ0cU5mdWdvVFlBaE05Mng3WXZJdDJTTDZfRng2a3lNTTczbGtYY18wSzJwbGtTelpocm1JZw?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Apple (AAPL) Stock Gets Fair Value Bump As Analysts Debate Margins And iPhone Demand
- Summary: Apple (AAPL) Stock Gets Fair Value Bump As Analysts Debate Margins And iPhone Demand
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxNZHZNT19NWVNzc0ZrNmpzYlVESDQ1RFZyRTd4SlU5Q000TnJBUzlUTEhKdHRodWpjdmtjMkxMQW5GV0FveDhRaWU3MDluZUYxTnp4R1RsQTZSM3duU2F4aWxSZWJJNXlwc09PVjRFaDRUX051YmFPRnRRY3VoUkRFcS1aMjVtYno3SFUyTFVaTlFmTU5Ca2c?oc=5>

### Apple (AAPL): A CIBC Pick Riding Record Results and a New iPhone Lineup
- Summary: Apple (AAPL): A CIBC Pick Riding Record Results and a New iPhone Lineup
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxObkprVXRMSk04czVtX0RBcEE1RGhOeTd6dHZpLTRiYkFXUnVUVHJFdnZBUFRsMXlSZU9yTkNlbEp2Q0JMZzJSWHhKTVlfTmdPbGo3Z3MxV1ZWeDJIZ3FDLUMwcXB1SWg5eUxfZlpZZTdnSWtOWFF2NnI4cFAxb05hNzJLbnBxNzdRNkNOajZUbmdELVVMY1dj?oc=5>

### Apple’s iPhone Demand Surges, But AAPL Still Isn’t a ‘Strong Buy’
- Summary: Apple’s iPhone Demand Surges, But AAPL Still Isn’t a ‘Strong Buy’
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQNDVKTlMwU0ZacGZ4WmxuNnJHQTh4aXh1dk9oRUhMNEo1ZEpsU3dVTFZqQlhVb09DXzJTTDJkWFVGdDM5STVybEhlUTI3QlIzd1R3UjVFbUw3ODZTc0pBU3RSTHBpRVFfZkFpdUp6WXlpQ3NOcEVtb2VYcV9MTXZYaTExUHRKeUFiQ0p2QXdhZzFZMEE1NUNXbi1qbEk?oc=5>

### Apple iPhone 18 Pro wait times near zero: UBS data (AAPL:NASDAQ)
- Summary: Apple iPhone 18 Pro wait times near zero: UBS data (AAPL:NASDAQ)
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxNdF82RlFXZU1zRjd1S0Q4VDdveHlsRHItOEhxLWFySlZzRFVFcjhxWmtsSGdtNlRTMlVHVWpRcHR3WFJVYXphaUtCaG44Yy1FX1hWQld1dFRPQzZVdF9rQkR5ci1MdzhldWdVN3JEaUpuM2twb2dDdlkzblVCWl96LWpNc2podGhONjFyVXdyLW4?oc=5>

### Apple (AAPL) Pushes AI Timelines Higher As Siri Engineering Leadership May Change
- Summary: Apple may accelerate AI development and change Siri leadership, indicating a push toward advanced AI features.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxNT0FHLVF5SkhsQk1nQko5eDF6X3lqRXVmRlViX2E1YVdmSUJXelp5a21DUmpaNFJ0cHExaGF1cmFSTXVGb2Z3cmw3anZOYm1MNFdnbXAxcnAwVDJ3d0d2Rk9IOWtXOFFpNW85RVN1ekVtTmRidk5ZUERKc3pXdk80cDc3YnV4STVzLUtDdnAtTWFNV2xYVTNWb0Fn?oc=5>

### Apple (AAPL) Stock Hits New 52-Week High
- Summary: Apple shares reach a new 52‑week peak, reflecting strong investor confidence.
- Date: 2026-11-09 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxQTWNWeXk1bWJyZU5ndU5uOHZBbFYzT29IN0Q1anlPMGxXVzV3cWxiaXhpcFNhM20xSkRMN3NHSVZ0a0l5OVpFZ0xYSC1vQzhvQk5ROEJ4c052WjNQUnBXQmthUE5JSTdQbmVKWGJLdE5hcmVCdk9uLUF5alQ1THVEVzlIa2VBTkJYVnhSRFhn?oc=5>

### AAPL is Trading at a Premium at 36.15X P/E: Is the Stock Still a Hold?
- Summary: Apple trading at high P/E; hold recommendation questioned.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxOS3NWZkRCc2Z2aUNKWGdheDJPLVc0b3l2eldHWmVjcllNMWZrRFRlOWR4bm81LWdGVTR0aDkyLUhDRDRIWDZSVnJNRFpiTUFOeEpIcGVOYU15elJCS3VEY2NCYWlxWUg1RTNaV193ZlhqLVVPVENYRXRjOXBGdklIbGxwbUpTOEFyWm5mTlY5VnRCZUFVazYzQmhydlUzSU9QVGV0OGUxMG5ZcFNKcWdkSDhUVVRKYjg2ZFdlQkpsRDJSdw?oc=5>

### A $1,999 Sellout. What China Renaissance Sees in Apple (AAPL)
- Summary: China Renaissance's $1,999 sellout view on Apple.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxPUVhYalN0S3o2VVRpNWZPTU9oWEZJZnlRNi1VU1pTY3VzUXFueTh3Um9IUWIzdjY4OW9EU3kwVG5QblI5MzcxUVg2Y3J3QW5KM3RuZGh3UmRJYTRBWVR0Ql9iZVAzb2JucTM5Qi1IQkl1bHNLQXpDeFltVzhqQm9mTXFneG5GSi1vQ25oSGY0VnBrSEI5a1hWb1d3VDU?oc=5>

### Apple (AAPL) Puts Tim Cook At The Center Of A Surprise CEO Search
- Summary: Apple announces a surprise CEO search, placing Tim Cook at the center of the process, signaling potential leadership changes.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxQZ2pUMi1tNld3R2xsYWtXRlNIck5ST3gyZVNBUE5tcE04d1Q5SWdJeUJaSjVVNm9kWHpVX3huOWQtTHFGbWxLNUY4TGsxMkFNX1BtUXdndVUxTnpDajhkdm5FMXROeXRIdDhCN05aQ3NiQXBqeEYtT21KRThBemZKSnhwVk1kZmxGVVhTZ053?oc=5>

### SA analyst upgrades/downgrades: NVDA, AAPL, SMCI, TSLA (SP500:)
- Summary: Analyst ratings for Apple and other tech stocks are updated, reflecting market sentiment and potential investment shifts.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxQNm95eXRjNjRsU0JJS1BRWnlDVXpLbG5LTTJEU1hRNGYwNG5CcU5EcW9ZWTRXMjVlaE5HT1B5SG42S1pIbHZTbXFhVFZFYTM2QnFWYlY3MHFHT3FZR1hEWjZVZWZibjVubWcwd2Z6Q3RTeTd3bTJOUWZGUmJRZEpkT2Etd19PaG5kaVdLajNYN2s?oc=5>

## RISKS

### What Does Apple's Run Mean for a 72-Year-Old Widow With $600,000 of a $1.6 Million IRA in the Stock?
- Summary: Apple stock impact on individual IRA.
- Date: 2026-11-13 | Impact: low | Horizon: medium | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxNUWZuZXJCVjBmM2FjaGoxWlFzS2p2RzZ0aDdidzA4TkJ4NG9EYndHNlhhSjZ4V0NRMmpyVVZDMHltaVdaVDZVdzMyRWFzaU5WbDdQZ1BWZGdGRW1wVGVVbGhLbW5BM0tUbGRMSFYwa2lWYWJYYTIzRTRPZUhDWDQ2RFNmOUc2VUNRS0VmTWxCczZLcERJV0VMVk9jLTFHWnAyVFF2Wm5DSWlybHlIalpELUJfeXZTYnlNYlh2YUExS01TNVBrUHhCbjZlckxQNDJaRmtsaFBR?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AAPL** | **39.50** | **46.19** | **30.41** | **11.70** | **5,177,380,175,872.00 USD** | **30.98** |
| MSFT | 27.30 | 8.27 | 19.25 | 18.80 | 3,890,434,801,664.00 USD | 4.95 |
| GOOGL | 15.60 | 5.51 | 19.08 | 24.70 | 3,636,196,016,128.00 USD | 6.45 |
| SONY | 19.90 | 2.92 | 0.30 | 10.30 | 157,770,825,728.00 USD | -8.05 |

Peers fetched as_of: 2026-11-13; AAPL reuses existing data (market data as_of: 2026-11-13); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-02
- Next expected earnings: 2027-01-28 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-13

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

- https://news.google.com/rss/articles/CBMikwFBVV95cUxQSjNua2NKRWx2ckNtazhaanloVXE0b3padGZlSnlfSDBXLURWYmM4Tm9xUWlmaWxqaXJsN3JQekh6YmtWcEFPRGJBVGYzdDFDVTdsYWpMSUhuSERxbGhFaWM3LWVvV2RvRGZocmwxLWlTWFhIemg0V0piMTJOVGpzUk5CeTRjQmR4YmdTaXVOSF9feUk?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxOM2lsenhVYnFXTUNRUHVQUkVxVEVMUDNwSzdFcDNnNWNRU3F2dDVGTHh2Zkh1N2laS1FtZHdzb2hQN3B6bHhrcUUxa2VFOWxzY1NlZTVwRFB5YkE4MGxjUHBueG1WQjRjUExnanJaZGZFSTQzX1Y0YTU3bmJ6UGNZYjNyaVdPenFDZHVhU0JlMUZySFBONHVDU2wxNnNIUQ?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxOdW5ZN2QxY2xIN3lFT1dqRWx3dUxLYVlieklHV2IyVVVnVEJFZkNnWE83Q1JtV1Y3ZUcwWE0tcy13YmRMNmxDa0NmNlNWaDJYSFBJT3Uyd1RhblBSc1Jjenp1UFFZdWNCVTV4TlBBMHFYa2h6N2xGNG9PMm9lU2tpbnA3dk11MVB1MGFXTTZJTUhZMXVQU0RaLV90MEg?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxON1hYY01mSnpmdUdVUVFPdG84eGc1R2JnZC1VTDVFYkRRQ0ZMNmFXTktyTm1LZHdDejUzTURxcVFQQ1kyUDFoT25jeXJYX1NTRzRNYldGZVpJWmw1dVVDQ203ckhQeUU1OGM5aVFGSkhwWFZQQVF2ZEtlbW1TU3hoMHgxQThqM3hObk1KN0c3VjQzckVlaURrVlVkdTFWTjdkQ2c?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxQOTluMHhsdUl2LXpHekdlOUZIWmFHQ0t5M3c1LTJaNm9uUU9ENHJlQ25BNzN6SFJaaXd5NVE0SlJtMEl2UHBhNnllV0JXVS1GRGhJWUdEMjBxT1RhRDBwTmo1R2hnNTZpOVpPb3Z4YVl0My0tQTc0NTZMZzZKTnpGOHlNYXUtd252c3NSOE9vMFhybUc4?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxOdDJER0dOZTdtdWwxU1FtekJMOFl1MVhYbDhHQ044RjB2NlVza1NDaUNRUVZMTGtLTlM4b19KTmZHazlrcXV4VTgtX0NSSldrU0hTVWl0Y05wdzlLXzRxUXFEVk01RTh0ZVBFQ0RKcVQtV2tsb2dsQ21RUEE1YVlXTjNORnd2RVJmaWU4RWRYYw?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxNWDQtTm5fUUhEZ1R2UnlWV3NrZnF0alhzalJBWFloTG5ucFJRZldRdTc5T2p2ZUI1X0Q5U0JlcHF3VEtWOFRFUnlDSzR2cTlER09HQWNUX2gwTWRtS2ZXLXQtNEJ2a1hGOXhsb0ZQS2l3MmNpeF81U3hmLW0zMnBoWUtLT29KUGI2YTJBdDJZZkZOOEthYXFhamYzSUJseTcw?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxQZTA4SG95UkQwOXZ5amtHTXJlT0ZsNE5lejVQZDBudkFRS1BsbVo2WjV4a1cwYUNvVUdfZ1dKZTBJZHZIRUh0Y3hCc1BPd2hFU0FXd3VKTDhnNGdoYUxhMjNHUHpWcFNPcDh3WWtZdGJpNlZ0eThnNVZmU0hGb2lFdEdSTDdJWS0zSmQ1MlFDTHYzanRNSVRFX1RvVTZwQnBJMXVyR0tsUVFxb0JxSkc4?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxNX1Q3Q0ppRGVaRnZnZmo0ekF1V3FUZkh0YTEwVXhYX2REUGIteGNjaTl2a2szb21zQkd3eEdMOHdlYlhhNFMzeVlIbWQwbFk1VFdHckxmQW9qcExZSlQ2S1UtTGJleWZEQ28yRHF5OGZUbVZQOGs3UHRtT3pVSDNVSTZzdVVicEFkV0VhOXBMczA?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxOMUpaWVdPaHVGd2dQLXBWZHo0TXpUYWthUWxrUnYzNHg4TzRGWWZaVEl6dEpFaEQ0M3F0VmtqeTZ5YkpMNkthTDUtbWg5bXNZMXpLRnJBUUNzRHQwM09CVF9YSURjYjlGem9lOS1WVHhoZjRuLURYdUFEYWpndWtnOGhOY0dkX3JPT3FzcWtVZXdpM3ZDQzZEOGJSZkRaVHc?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxPeDE2Yk1XT0NWbHpadlh6V3ZYc3hwOTQxWFQ2V0lfcUJoY3JEM2hrRk0yMnI2b0dfN3lxZUJHcURsdVBlVzVjMkt4N1A1MnhkckpWb2lOTndwZUF3MVZsUW1vN2pZV3ZZOVFtNjh3MTh1bWpYaHJNVzVGNWJWTDlUMnhKMXVuamtpWHFKanZ1TnNOR3owbE1QU1JZQm9zN2x4eTN6dVRZS0J1dw?oc=5
- https://news.google.com/rss/articles/CBMiUEFVX3lxTE00U3JoRzhkckt5aVFxb1NVNnBndWhrcDM5N0NqUzZGUk8xQk04OF9jVWRULXh2RmlJaGpTS1FJWEREaUlNUnhfSHk2cm53NllX?oc=5
- https://news.google.com/rss/articles/CBMi_gFBVV95cUxNWVJhZDJfcFlqSnN2N25TRHpLazhkbE9GRFBWODJkaGVYd3FNZzRjR0prczZNcGdVV2djMVo5bHM0ZFd2djIzYlFkVFBQUk9KYjBuSFpVTExPQjRPT2pSd2Y4TFJlaE5wUHhBdDZUbnZUQXpGNG9lY2hkdWxDVnZ4aDl2bmxtVnI0WWZDaHUybEV3RU9GaGdhSWhGMG9JWnk5NkZCazk4d01uTlRBLVNnRGptVEotdXRFS05oY0tuV3U0d2gtaHFLaVJ0cU5mdWdvVFlBaE05Mng3WXZJdDJTTDZfRng2a3lNTTczbGtYY18wSzJwbGtTelpocm1JZw?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxNZHZNT19NWVNzc0ZrNmpzYlVESDQ1RFZyRTd4SlU5Q000TnJBUzlUTEhKdHRodWpjdmtjMkxMQW5GV0FveDhRaWU3MDluZUYxTnp4R1RsQTZSM3duU2F4aWxSZWJJNXlwc09PVjRFaDRUX051YmFPRnRRY3VoUkRFcS1aMjVtYno3SFUyTFVaTlFmTU5Ca2c?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxObkprVXRMSk04czVtX0RBcEE1RGhOeTd6dHZpLTRiYkFXUnVUVHJFdnZBUFRsMXlSZU9yTkNlbEp2Q0JMZzJSWHhKTVlfTmdPbGo3Z3MxV1ZWeDJIZ3FDLUMwcXB1SWg5eUxfZlpZZTdnSWtOWFF2NnI4cFAxb05hNzJLbnBxNzdRNkNOajZUbmdELVVMY1dj?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQNDVKTlMwU0ZacGZ4WmxuNnJHQTh4aXh1dk9oRUhMNEo1ZEpsU3dVTFZqQlhVb09DXzJTTDJkWFVGdDM5STVybEhlUTI3QlIzd1R3UjVFbUw3ODZTc0pBU3RSTHBpRVFfZkFpdUp6WXlpQ3NOcEVtb2VYcV9MTXZYaTExUHRKeUFiQ0p2QXdhZzFZMEE1NUNXbi1qbEk?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxNdF82RlFXZU1zRjd1S0Q4VDdveHlsRHItOEhxLWFySlZzRFVFcjhxWmtsSGdtNlRTMlVHVWpRcHR3WFJVYXphaUtCaG44Yy1FX1hWQld1dFRPQzZVdF9rQkR5ci1MdzhldWdVN3JEaUpuM2twb2dDdlkzblVCWl96LWpNc2podGhONjFyVXdyLW4?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxNT0FHLVF5SkhsQk1nQko5eDF6X3lqRXVmRlViX2E1YVdmSUJXelp5a21DUmpaNFJ0cHExaGF1cmFSTXVGb2Z3cmw3anZOYm1MNFdnbXAxcnAwVDJ3d0d2Rk9IOWtXOFFpNW85RVN1ekVtTmRidk5ZUERKc3pXdk80cDc3YnV4STVzLUtDdnAtTWFNV2xYVTNWb0Fn?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxQTWNWeXk1bWJyZU5ndU5uOHZBbFYzT29IN0Q1anlPMGxXVzV3cWxiaXhpcFNhM20xSkRMN3NHSVZ0a0l5OVpFZ0xYSC1vQzhvQk5ROEJ4c052WjNQUnBXQmthUE5JSTdQbmVKWGJLdE5hcmVCdk9uLUF5alQ1THVEVzlIa2VBTkJYVnhSRFhn?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxOS3NWZkRCc2Z2aUNKWGdheDJPLVc0b3l2eldHWmVjcllNMWZrRFRlOWR4bm81LWdGVTR0aDkyLUhDRDRIWDZSVnJNRFpiTUFOeEpIcGVOYU15elJCS3VEY2NCYWlxWUg1RTNaV193ZlhqLVVPVENYRXRjOXBGdklIbGxwbUpTOEFyWm5mTlY5VnRCZUFVazYzQmhydlUzSU9QVGV0OGUxMG5ZcFNKcWdkSDhUVVRKYjg2ZFdlQkpsRDJSdw?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxPUVhYalN0S3o2VVRpNWZPTU9oWEZJZnlRNi1VU1pTY3VzUXFueTh3Um9IUWIzdjY4OW9EU3kwVG5QblI5MzcxUVg2Y3J3QW5KM3RuZGh3UmRJYTRBWVR0Ql9iZVAzb2JucTM5Qi1IQkl1bHNLQXpDeFltVzhqQm9mTXFneG5GSi1vQ25oSGY0VnBrSEI5a1hWb1d3VDU?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxQZ2pUMi1tNld3R2xsYWtXRlNIck5ST3gyZVNBUE5tcE04d1Q5SWdJeUJaSjVVNm9kWHpVX3huOWQtTHFGbWxLNUY4TGsxMkFNX1BtUXdndVUxTnpDajhkdm5FMXROeXRIdDhCN05aQ3NiQXBqeEYtT21KRThBemZKSnhwVk1kZmxGVVhTZ053?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxQNm95eXRjNjRsU0JJS1BRWnlDVXpLbG5LTTJEU1hRNGYwNG5CcU5EcW9ZWTRXMjVlaE5HT1B5SG42S1pIbHZTbXFhVFZFYTM2QnFWYlY3MHFHT3FZR1hEWjZVZWZibjVubWcwd2Z6Q3RTeTd3bTJOUWZGUmJRZEpkT2Etd19PaG5kaVdLajNYN2s?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxNUWZuZXJCVjBmM2FjaGoxWlFzS2p2RzZ0aDdidzA4TkJ4NG9EYndHNlhhSjZ4V0NRMmpyVVZDMHltaVdaVDZVdzMyRWFzaU5WbDdQZ1BWZGdGRW1wVGVVbGhLbW5BM0tUbGRMSFYwa2lWYWJYYTIzRTRPZUhDWDQ2RFNmOUc2VUNRS0VmTWxCczZLcERJV0VMVk9jLTFHWnAyVFF2Wm5DSWlybHlIalpELUJfeXZTYnlNYlh2YUExS01TNVBrUHhCbjZlckxQNDJaRmtsaFBR?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
