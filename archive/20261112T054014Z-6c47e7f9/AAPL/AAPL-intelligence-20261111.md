# AAPL Intelligence Report

- ticker: **AAPL**
- Report as_of: **2026-11-11**
- Market data as_of: **2026-11-11**
- Quant sources: https://finance.yahoo.com/quote/AAPL/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AAPL/key-statistics/
- AI analysis snapshot as_of: **2026-11-11**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-12T05:52:00.424495+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 7, 'ai': 17, 'unknown': 0, 'irrelevant': 1})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **8** exact headline/source/date matches; prior report **20261111T043601Z-d14951e6/AAPL** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **5**; {'directional_claim_without_event_type': 5}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 12 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 28.0%; oldest publication 2026-11-05

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 355.6300 |
| Return 1D (%) | 2.0430 |
| Return 1W (%) | 1.7510 |
| Return 1M (%) | 5.6410 |
| Return YTD (%) | 31.1697 |
| Return 1Y (%) | 29.5542 |
| Annualized volatility (%) | 24.9438 |
| Beta vs SPY | 0.6160 |
| Max drawdown (%) | -13.7985 |
| Sharpe (rf=0) | 1.1673 |
| Downside deviation (rf=0, %) | 16.9546 |
| Sortino (rf=0) | 1.7174 |
| Historical VaR 95% (1D, %) | 2.0034 |
| Historical ES 95% (1D, %) | 3.4742 |
| Correlation vs SPY | 0.3390 |
| Tracking error vs SPY (%) | 24.0513 |
| P/E (trailing) | 39.60 |
| P/B | 46.11 |
| EV/EBITDA | 30.36 |
| Revenue growth (%) | 11.70 |
| Forward P/E (estimate) | 33.72 |
| Gross margin (%) | 48.79 |
| Operating margin (%) | 33.01 |
| Return on equity (%) | 142.26 |
| Free cash flow yield (%) | 2.04 |
| MA50 | 337.8768 |
| Close vs MA50 (%) | 5.2543 |
| MA200 | 300.0113 |
| Close vs MA200 (%) | 18.5389 |
| RSI (14, Wilder) | 60.4231 |
| MACD (12,26) | 3.3549 |
| MACD signal (9) | 2.8788 |
| MACD histogram | 0.4762 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AAPL': 280, 'SPY': 280}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 355.6300 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 2.0430 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 1.7510 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 5.6410 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 31.1697 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 29.5542 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 24.9438 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 16.9546 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.7174 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.0034 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.4742 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.3390 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 24.0513 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.6160 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -13.7985 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.1673 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 33.7235 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 48.7860 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 33.0100 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 142.2570 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.0444 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 39.6024 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 60.4231 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.4762 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 5.2543 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 18.5389 -> Clearly above the moving-average trend level.

## TAILWINDS

### AAPL Stock Ticks Up After Clearing Key Regulatory Step in China for Apple Intelligence’s AI for iPads and Macs
- Summary: Apple’s AI for iPads and Macs cleared a key Chinese regulatory step, lifting the stock.
- Date: 2026-11-09 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxOSFh0M3FIZjBqaXlfTHdSaDdQelFBMEtmczRVVFdNUDhlV1pmaGI0ZXhiRmNQaHpYQXpBV3ZvYXE3V3RBamFaRW5XcnVRYkVRTVBvdV82X21mUno2U2lqeGlqTV9jMnAydnJSN2JCWUU5RlJLX1JvTXlmaVU2ODhJV0VrbFJ3REJadEpvUDZpUFRlNWxveUFONUxUREZ3ckN2OTcxYURnQjhobGFsTlI1VzJZVk1IRFUxeEUtZzFjeTRkSjI4NjFIMGlYdGo2NTlsb05STGln?oc=5>

### Apple Inc. (AAPL) Rallied 15% as Investors Reassessed Its Growth: What’s Next for the Stock?
- Summary: Apple shares surged 15% after investors reassessed growth prospects.
- Date: 2026-11-10 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxQOTluMHhsdUl2LXpHekdlOUZIWmFHQ0t5M3c1LTJaNm9uUU9ENHJlQ25BNzN6SFJaaXd5NVE0SlJtMEl2UHBhNnllV0JXVS1GRGhJWUdEMjBxT1RhRDBwTmo1R2hnNTZpOVpPb3Z4YVl0My0tQTc0NTZMZzZKTnpGOHlNYXUtd252c3NSOE9vMFhybUc4?oc=5>

### Apple (AAPL) Stock Hits New 52-Week High
- Summary: Apple’s stock reached a new 52‑week high, indicating strong investor confidence.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxQTWNWeXk1bWJyZU5ndU5uOHZBbFYzT29IN0Q1anlPMGxXVzV3cWxiaXhpcFNhM20xSkRMN3NHSVZ0a0l5OVpFZ0xYSC1vQzhvQk5ROEJ4c052WjNQUnBXQmthUE5JSTdQbmVKWGJLdE5hcmVCdk9uLUF5alQ1THVEVzlIa2VBTkJYVnhSRFhn?oc=5>

### Apple Is Above $5 Trillion After Its First-Ever Close Above $350
- Summary: Apple's market cap surpassed $5 trillion following a record close above $350.
- Date: 2026-11-10 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxPeDE2Yk1XT0NWbHpadlh6V3ZYc3hwOTQxWFQ2V0lfcUJoY3JEM2hrRk0yMnI2b0dfN3lxZUJHcURsdVBlVzVjMkt4N1A1MnhkckpWb2lOTndwZUF3MVZsUW1vN2pZV3ZZOVFtNjh3MTh1bWpYaHJNVzVGNWJWTDlUMnhKMXVuamtpWHFKanZ1TnNOR3owbE1QU1JZQm9zN2x4eTN6dVRZS0J1dw?oc=5>

### What's Going On With Apple Stock Wednesday?
- Summary: A discussion of Apple’s current stock performance and market factors.
- Date: 2026-11-11 | Impact: low | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxOdW5ZN2QxY2xIN3lFT1dqRWx3dUxLYVlieklHV2IyVVVnVEJFZkNnWE83Q1JtV1Y3ZUcwWE0tcy13YmRMNmxDa0NmNlNWaDJYSFBJT3Uyd1RhblBSc1Jjenp1UFFZdWNCVTV4TlBBMHFYa2h6N2xGNG9PMm9lU2tpbnA3dk11MVB1MGFXTTZJTUhZMXVQU0RaLV90MEg?oc=5>

### Apple Inc. (AAPL) stock price, news, quote and history
- Summary: Overview of Apple’s stock price history and recent quotes.
- Date: 2026-11-10 | Impact: low | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiUkFVX3lxTE5pbUxLdFVNSjJfVjFOUm9UYmFBYUVBRmV5Q3FJU3lfblNtbVNvZjI4N1hEdlVtTnBMYWRCMi0wUTVTUGdxMUhDb0plLWlmcWdqMEE?oc=5>

### Where Will Apple Stock Be in 5 Years?
- Summary: Speculation on Apple’s future stock trajectory over five years.
- Date: 2026-11-09 | Impact: low | Horizon: long | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihgFBVV95cUxQT3VCWFJQaWtIVW9pVVhTTDI0cHpHX0ZyandZZGlkTXp4SjRvQWxFVUllSXBrVEwzRllpLUM0Q2IyYUFDMWxfNkhGRjM2clF0eTRnbDlGQ3djejF5Y2RjaXdFV29Bd1RZTmxGNGhCTG41VzhZdVBVOTlYZW5CVmJjMkNFcUlOQQ?oc=5>

### Apple Shares (AAPL) Look Expensive Heading into 2027
- Summary: Analysis of Apple shares’ valuation approaching 2027.
- Date: 2026-11-11 | Impact: low | Horizon: long | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxOM2lsenhVYnFXTUNRUHVQUkVxVEVMUDNwSzdFcDNnNWNRU3F2dDVGTHh2Zkh1N2laS1FtZHdzb2hQN3B6bHhrcUUxa2VFOWxzY1NlZTVwRFB5YkE4MGxjUHBueG1WQjRjUExnanJaZGZFSTQzX1Y0YTU3bmJ6UGNZYjNyaVdPenFDZHVhU0JlMUZySFBONHVDU2wxNnNIUQ?oc=5>

### Apple (AAPL) Stock: $348.51, Down 0.62% Nov 10
- Summary: Current Apple stock price and recent decline.
- Date: 2026-11-11 | Impact: low | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxOMUpaWVdPaHVGd2dQLXBWZHo0TXpUYWthUWxrUnYzNHg4TzRGWWZaVEl6dEpFaEQ0M3F0VmtqeTZ5YkpMNkthTDUtbWg5bXNZMXpLRnJBUUNzRHQwM09CVF9YSURjYjlGem9lOS1WVHhoZjRuLURYdUFEYWpndWtnOGhOY0dkX3JPT3FzcWtVZXdpM3ZDQzZEOGJSZkRaVHc?oc=5>

### Apple: Capex-Light AI Amid Regulatory Uncertainty (Rating Upgrade)
- Summary: Apple’s rating upgrade signals confidence in its AI strategy amid regulatory uncertainty.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxQZTA4SG95UkQwOXZ5amtHTXJlT0ZsNE5lejVQZDBudkFRS1BsbVo2WjV4a1cwYUNvVUdfZ1dKZTBJZHZIRUh0Y3hCc1BPd2hFU0FXd3VKTDhnNGdoYUxhMjNHUHpWcFNPcDh3WWtZdGJpNlZ0eThnNVZmU0hGb2lFdEdSTDdJWS0zSmQ1MlFDTHYzanRNSVRFX1RvVTZwQnBJMXVyR0tsUVFxb0JxSkc4?oc=5>

### Why Apple Stock Looks Like a Safe Haven After the Midterms
- Summary: Apple perceived as a safe haven post-midterms, boosting investor sentiment.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxOR3hKcFhWVFpvNHpjLVF3bHNIaml4UDE5R1VKd3drSWI1bXo4NVpnLUJuRU1QSEloYzRmdUFxOU1LVktYQ3dMcjdodWhkenhtU1Q0dk9tQWplTUVBZjNjcXZiSmh0UThEdUJCSjJEd0djOFd5YzFxZXl2YWhUZ29JcVNwNW5MNzVONHdSaEh2TU1tazlEUElLRlU3UQ?oc=5>

### Apple Inc. $AAPL Stock Holdings Raised by Root Financial Partners LLC
- Summary: Root Financial Partners increased Apple holdings, indicating bullish outlook.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxPZ0ZFSG1ZZ2Myd250endSSjJJNjNEeW9PSnRTZWtPanZnaUMtNU1MTTNpcWVLMXZOdVEtRnVnenRscDlycnpsVzgtMjFYSFpsR2ZkZTlPZFBlRVJBZUJiMTFiLWpfUHFfbVhaekd0RVpnQ05oTzN5LWtaMXNaZGJndjNTQ05IN2FHak1nOW1wYktPRTllUXBwN04zZ2ZSQzNnRERrZzdPdmstUjdHVElCMHlCX1JGZFh1TFRGN0huYXVwcXAtQVNv?oc=5>

## HEADWINDS

### ETFs Are Net Sellers of Apple (AAPL) on Nov. 5
- Summary: ETFs sold Apple shares, adding downward pressure on the stock.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxQOVRSNEFPS0VIX0ZGNVZzOEp6YnFxenV3NFJ2T0hWc1NGYmRsNjBVemZjY0xfa0FiWVlWc0FrVFFYOVFHVjBob1FFX3lxYlhKclVvZXdhWDJUeWhyLXVlNUUyUlVmZThnTUpiRE9GZng0VWpscE5KNXdkUkNWNllCaVlRV0V1TV9KWWZEdlFZdV8xWWRlb2g4?oc=5>

### Apple: Record Earnings Mask A Growing Margin Problem (NASDAQ:AAPL)
- Summary: Record earnings hide margin decline, raising concerns about profitability.
- Date: 2026-11-09 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxNdmh3YmNIUHlOT3dJYjFzbjFhc0NGTWJqTmZwRk1xLUZXRHdsSlJyRjNhWTFkNExyakxzdGJGcmIyMUotVGVIMEMtUDlneGcxaVJJR3hTUHdnTFJqNzZxd2VNbEJYbTlES1ZQSEY3bENVUVpGNVQtclUxclpZZDRySzNrLW5vUHp1N2pScmVmTEJjdEpKcTFn?oc=5>

## CATALYSTS

### Apple (AAPL) Stock Gets Fair Value Bump As Analysts Debate Margins And iPhone Demand
- Summary: Apple (AAPL) Stock Gets Fair Value Bump As Analysts Debate Margins And iPhone Demand
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxNZHZNT19NWVNzc0ZrNmpzYlVESDQ1RFZyRTd4SlU5Q000TnJBUzlUTEhKdHRodWpjdmtjMkxMQW5GV0FveDhRaWU3MDluZUYxTnp4R1RsQTZSM3duU2F4aWxSZWJJNXlwc09PVjRFaDRUX051YmFPRnRRY3VoUkRFcS1aMjVtYno3SFUyTFVaTlFmTU5Ca2c?oc=5>

### Apple iPhone 18 Pro wait times near zero: UBS data (AAPL:NASDAQ)
- Summary: Apple iPhone 18 Pro wait times near zero: UBS data (AAPL:NASDAQ)
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxNdF82RlFXZU1zRjd1S0Q4VDdveHlsRHItOEhxLWFySlZzRFVFcjhxWmtsSGdtNlRTMlVHVWpRcHR3WFJVYXphaUtCaG44Yy1FX1hWQld1dFRPQzZVdF9rQkR5ci1MdzhldWdVN3JEaUpuM2twb2dDdlkzblVCWl96LWpNc2podGhONjFyVXdyLW4?oc=5>

### Apple’s iPhone Demand Surges, But AAPL Still Isn’t a ‘Strong Buy’
- Summary: Apple’s iPhone Demand Surges, But AAPL Still Isn’t a ‘Strong Buy’
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQNDVKTlMwU0ZacGZ4WmxuNnJHQTh4aXh1dk9oRUhMNEo1ZEpsU3dVTFZqQlhVb09DXzJTTDJkWFVGdDM5STVybEhlUTI3QlIzd1R3UjVFbUw3ODZTc0pBU3RSTHBpRVFfZkFpdUp6WXlpQ3NOcEVtb2VYcV9MTXZYaTExUHRKeUFiQ0p2QXdhZzFZMEE1NUNXbi1qbEk?oc=5>

### Apple (AAPL) Stock Looks Fully Valued On Future Cash Flow
- Summary: Apple (AAPL) Stock Looks Fully Valued On Future Cash Flow
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxNMjZ0WXFKaWhlbC1ZZV9jVG5kVVk3ZDhodE5QV1Q3MlNtY3NrS0VidjkwN1l0TmR3VGtsWXpNMTFfbjdNejRHbGF1cFo3bkJaVmtXY2h6OTZGUUF0OUFhLUhhR0xwa1k2TXdaVFdiTkx0Wm9mQkFhX3VTTUpKZnY3YTBYLXAzR0x6QlU2aGpKZm9CZFpocWlub1F3a2w3QnNYa0Rqc3llbVlQakVEZDk4QTkxTWxnZ9IBuwFBVV95cUxQUGdWRG5XcGNzTk44TjFSelptRVJJdkhtMjFBQWdsYlZDYUNWQ2d4RTRHbzQ3SkF0OU9HNEVkMU9vbllZbUxCMzVWdWlhTTBVVHJ1UnRFb3BFREtwOHljQklrcDJFZ2hJbTJPUlVfWTM2QlRYcVVSenRlclBrbzYyUXhmSzRSX2tYX0lRZWpVeXc4MUg3dExHT0ZZVmVfREliclZVckFkYm5JbW9Fa1dLWDlZSXZSNkhTYS1N?oc=5>

### Apple cut tax bill by $2.7B by moving some earnings to Singapore (AAPL:NASDAQ)
- Summary: Apple cut tax bill by $2.7B by moving some earnings to Singapore (AAPL:NASDAQ)
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxPYTJicFA2UmI2NFk2S29QbmlmLVJiRGRIVG1GeXJWYjRoeXpPXzdPRktLbXR3dzBCUFhGZDNWZllkUmFqekRQWWVKVThsd2VZY2J1bDVaREUzRjRsSEdyaFhHYmhRZWpSbF9USUtTZ3FRTDh3cE1oQ09jTm9PWU5Va1M4YkZyMmo3eU54bWVHY0dvX1ZqUkJYWW11MjhQMzNSNXc?oc=5>

### Apple Inc. $AAPL Stock Sold by Investment House LLC
- Summary: Apple Inc. $AAPL Stock Sold by Investment House LLC
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxPYVVSRERqVDdrOS01N0lHOWpJSjRFMDVDQjZPcjdLUWlISHlmZGVYV2FNbjEyQlV4WnNKMU5YaU9XZ1FTOEEzSDNCRjZ2NTJ5MUhVb0F6T1Y4WDNWRE1scll0LUtlWnRXYk5jZjJaZXA2V3AtZjRsYXpTOEphUFpnbU1zRk1JVjRMcnBfNlBCRE4tQmxFXy1mTnJIcDlDMFlVMHBDcjROZ25JRURVbmZJ?oc=5>

### Apple Inc. $AAPL Stock Purchased by Precedent Wealth Partners LLC
- Summary: Apple Inc. $AAPL Stock Purchased by Precedent Wealth Partners LLC
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxQZUVNUGFsSURIQW9ncTNzcFVUNk0wLVRoRU96SDhtOHBycU04MXJXZW5ZTnVTU01rVW9PME9WMlYwLW50U1Fmd3ZBV3lpaEJaZUk5VWs4Y05NRGZIMHJVRmxuVzVWbERBQlpMcFUwd1JrbnlwS0FKV2JDVWRLemhpYlNhd2R5NWt1R01rRHBPdnJRdDVmb05iZGNHQXJ6dTBxbW5DamhwWmxhaFpna1BKQmxhV1hNYlJRbzVidktmQ3N2QQ?oc=5>

### Apple (AAPL) Stock Could Be 30% Overvalued Despite Record iPhone Sales
- Summary: Apple’s stock may be overvalued by 30% despite strong iPhone sales.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxObHl6UFg0RmRmWXdsZHllLVp6VWs5WHcxWTlraVhPR3hfdGtPMnJnTEkwZUxZakktLUNWU19hMS1aZnRhQjk4eERNN3RIbGZxM3pCVHotUjhwbmwyVUViTVctbFU3X1Nxb3JReE9aTm5JbTBXZWhyeU5zci1PTXV1REJJYjYtOFN4TEoweUc5Qi1GWU9W?oc=5>

### Apple Won’t “Play in Traffic” on AI. It’s Up 28% in a Year: Too Late to Buy?
- Summary: Apple’s cautious AI stance may limit future growth, despite a 28% yearly rise.
- Date: 2026-11-09 | Impact: medium | Horizon: medium | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxOdlZnZWpJYXhac2ZUM2w2TGVrQ0lvb084bGRIeUZsSXJmbDdwUlpQNzhyWlNXYkxxQVU1SGoycUhGMzd6VEZJQ0dfT0xEeFREN1pQLTJTa1EzREtYTXA0MGV3WDEzeXdiWnhNUml4c3F6cnZpNWJfM3lTdFBmMDVINl81MGxSV0d2b3pxbkVsa3hJX3dNZ1Y0clBn?oc=5>

## RISKS

### Apple (AAPL) Faces A 38% Premium Following Fresh Debt Issuance
- Summary: Apple’s new debt issuance led to a 38% premium, raising concerns about future debt servicing and potential dilution.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxQeElvQXI0RHF2Vkd4cDBoMEVpc3VJcHBKY3NLMVNRbXBMUFNReTlTbF9Zb08wZUVTNFNCUjJfRS1BeE11MGp5YjV3a21qOGZlbkRlTUxvcktRNVNSWElFREN6NTZsVjltVnRKWEVKZ3JVVE9ETkQzMmZfS1V6WUF2bjNITkdObzI2c0pkbU1BU1pqMEpNZkV3?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AAPL** | **39.60** | **46.11** | **30.36** | **11.70** | **5,168,079,831,040.00 USD** | **29.55** |
| MSFT | 27.82 | 8.23 | 19.15 | 18.80 | 3,869,975,511,040.00 USD | 3.29 |
| GOOGL | 15.01 | 5.47 | 18.93 | 24.70 | 3,607,674,224,640.00 USD | 1.00 |
| SONY | 19.77 | 2.86 | 0.30 | 10.30 | 154,390,446,080.00 USD | -9.16 |

Peers fetched as_of: 2026-11-11; AAPL reuses existing data (market data as_of: 2026-11-11); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-02
- Next expected earnings: 2027-01-28 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-11

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

- https://news.google.com/rss/articles/CBMi1gFBVV95cUxOSFh0M3FIZjBqaXlfTHdSaDdQelFBMEtmczRVVFdNUDhlV1pmaGI0ZXhiRmNQaHpYQXpBV3ZvYXE3V3RBamFaRW5XcnVRYkVRTVBvdV82X21mUno2U2lqeGlqTV9jMnAydnJSN2JCWUU5RlJLX1JvTXlmaVU2ODhJV0VrbFJ3REJadEpvUDZpUFRlNWxveUFONUxUREZ3ckN2OTcxYURnQjhobGFsTlI1VzJZVk1IRFUxeEUtZzFjeTRkSjI4NjFIMGlYdGo2NTlsb05STGln?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxQOTluMHhsdUl2LXpHekdlOUZIWmFHQ0t5M3c1LTJaNm9uUU9ENHJlQ25BNzN6SFJaaXd5NVE0SlJtMEl2UHBhNnllV0JXVS1GRGhJWUdEMjBxT1RhRDBwTmo1R2hnNTZpOVpPb3Z4YVl0My0tQTc0NTZMZzZKTnpGOHlNYXUtd252c3NSOE9vMFhybUc4?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxQTWNWeXk1bWJyZU5ndU5uOHZBbFYzT29IN0Q1anlPMGxXVzV3cWxiaXhpcFNhM20xSkRMN3NHSVZ0a0l5OVpFZ0xYSC1vQzhvQk5ROEJ4c052WjNQUnBXQmthUE5JSTdQbmVKWGJLdE5hcmVCdk9uLUF5alQ1THVEVzlIa2VBTkJYVnhSRFhn?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxPeDE2Yk1XT0NWbHpadlh6V3ZYc3hwOTQxWFQ2V0lfcUJoY3JEM2hrRk0yMnI2b0dfN3lxZUJHcURsdVBlVzVjMkt4N1A1MnhkckpWb2lOTndwZUF3MVZsUW1vN2pZV3ZZOVFtNjh3MTh1bWpYaHJNVzVGNWJWTDlUMnhKMXVuamtpWHFKanZ1TnNOR3owbE1QU1JZQm9zN2x4eTN6dVRZS0J1dw?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxOdW5ZN2QxY2xIN3lFT1dqRWx3dUxLYVlieklHV2IyVVVnVEJFZkNnWE83Q1JtV1Y3ZUcwWE0tcy13YmRMNmxDa0NmNlNWaDJYSFBJT3Uyd1RhblBSc1Jjenp1UFFZdWNCVTV4TlBBMHFYa2h6N2xGNG9PMm9lU2tpbnA3dk11MVB1MGFXTTZJTUhZMXVQU0RaLV90MEg?oc=5
- https://news.google.com/rss/articles/CBMiUkFVX3lxTE5pbUxLdFVNSjJfVjFOUm9UYmFBYUVBRmV5Q3FJU3lfblNtbVNvZjI4N1hEdlVtTnBMYWRCMi0wUTVTUGdxMUhDb0plLWlmcWdqMEE?oc=5
- https://news.google.com/rss/articles/CBMihgFBVV95cUxQT3VCWFJQaWtIVW9pVVhTTDI0cHpHX0ZyandZZGlkTXp4SjRvQWxFVUllSXBrVEwzRllpLUM0Q2IyYUFDMWxfNkhGRjM2clF0eTRnbDlGQ3djejF5Y2RjaXdFV29Bd1RZTmxGNGhCTG41VzhZdVBVOTlYZW5CVmJjMkNFcUlOQQ?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxOM2lsenhVYnFXTUNRUHVQUkVxVEVMUDNwSzdFcDNnNWNRU3F2dDVGTHh2Zkh1N2laS1FtZHdzb2hQN3B6bHhrcUUxa2VFOWxzY1NlZTVwRFB5YkE4MGxjUHBueG1WQjRjUExnanJaZGZFSTQzX1Y0YTU3bmJ6UGNZYjNyaVdPenFDZHVhU0JlMUZySFBONHVDU2wxNnNIUQ?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxOMUpaWVdPaHVGd2dQLXBWZHo0TXpUYWthUWxrUnYzNHg4TzRGWWZaVEl6dEpFaEQ0M3F0VmtqeTZ5YkpMNkthTDUtbWg5bXNZMXpLRnJBUUNzRHQwM09CVF9YSURjYjlGem9lOS1WVHhoZjRuLURYdUFEYWpndWtnOGhOY0dkX3JPT3FzcWtVZXdpM3ZDQzZEOGJSZkRaVHc?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxQZTA4SG95UkQwOXZ5amtHTXJlT0ZsNE5lejVQZDBudkFRS1BsbVo2WjV4a1cwYUNvVUdfZ1dKZTBJZHZIRUh0Y3hCc1BPd2hFU0FXd3VKTDhnNGdoYUxhMjNHUHpWcFNPcDh3WWtZdGJpNlZ0eThnNVZmU0hGb2lFdEdSTDdJWS0zSmQ1MlFDTHYzanRNSVRFX1RvVTZwQnBJMXVyR0tsUVFxb0JxSkc4?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxOR3hKcFhWVFpvNHpjLVF3bHNIaml4UDE5R1VKd3drSWI1bXo4NVpnLUJuRU1QSEloYzRmdUFxOU1LVktYQ3dMcjdodWhkenhtU1Q0dk9tQWplTUVBZjNjcXZiSmh0UThEdUJCSjJEd0djOFd5YzFxZXl2YWhUZ29JcVNwNW5MNzVONHdSaEh2TU1tazlEUElLRlU3UQ?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxPZ0ZFSG1ZZ2Myd250endSSjJJNjNEeW9PSnRTZWtPanZnaUMtNU1MTTNpcWVLMXZOdVEtRnVnenRscDlycnpsVzgtMjFYSFpsR2ZkZTlPZFBlRVJBZUJiMTFiLWpfUHFfbVhaekd0RVpnQ05oTzN5LWtaMXNaZGJndjNTQ05IN2FHak1nOW1wYktPRTllUXBwN04zZ2ZSQzNnRERrZzdPdmstUjdHVElCMHlCX1JGZFh1TFRGN0huYXVwcXAtQVNv?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxQOVRSNEFPS0VIX0ZGNVZzOEp6YnFxenV3NFJ2T0hWc1NGYmRsNjBVemZjY0xfa0FiWVlWc0FrVFFYOVFHVjBob1FFX3lxYlhKclVvZXdhWDJUeWhyLXVlNUUyUlVmZThnTUpiRE9GZng0VWpscE5KNXdkUkNWNllCaVlRV0V1TV9KWWZEdlFZdV8xWWRlb2g4?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxNdmh3YmNIUHlOT3dJYjFzbjFhc0NGTWJqTmZwRk1xLUZXRHdsSlJyRjNhWTFkNExyakxzdGJGcmIyMUotVGVIMEMtUDlneGcxaVJJR3hTUHdnTFJqNzZxd2VNbEJYbTlES1ZQSEY3bENVUVpGNVQtclUxclpZZDRySzNrLW5vUHp1N2pScmVmTEJjdEpKcTFn?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxNZHZNT19NWVNzc0ZrNmpzYlVESDQ1RFZyRTd4SlU5Q000TnJBUzlUTEhKdHRodWpjdmtjMkxMQW5GV0FveDhRaWU3MDluZUYxTnp4R1RsQTZSM3duU2F4aWxSZWJJNXlwc09PVjRFaDRUX051YmFPRnRRY3VoUkRFcS1aMjVtYno3SFUyTFVaTlFmTU5Ca2c?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxNdF82RlFXZU1zRjd1S0Q4VDdveHlsRHItOEhxLWFySlZzRFVFcjhxWmtsSGdtNlRTMlVHVWpRcHR3WFJVYXphaUtCaG44Yy1FX1hWQld1dFRPQzZVdF9rQkR5ci1MdzhldWdVN3JEaUpuM2twb2dDdlkzblVCWl96LWpNc2podGhONjFyVXdyLW4?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQNDVKTlMwU0ZacGZ4WmxuNnJHQTh4aXh1dk9oRUhMNEo1ZEpsU3dVTFZqQlhVb09DXzJTTDJkWFVGdDM5STVybEhlUTI3QlIzd1R3UjVFbUw3ODZTc0pBU3RSTHBpRVFfZkFpdUp6WXlpQ3NOcEVtb2VYcV9MTXZYaTExUHRKeUFiQ0p2QXdhZzFZMEE1NUNXbi1qbEk?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxNMjZ0WXFKaWhlbC1ZZV9jVG5kVVk3ZDhodE5QV1Q3MlNtY3NrS0VidjkwN1l0TmR3VGtsWXpNMTFfbjdNejRHbGF1cFo3bkJaVmtXY2h6OTZGUUF0OUFhLUhhR0xwa1k2TXdaVFdiTkx0Wm9mQkFhX3VTTUpKZnY3YTBYLXAzR0x6QlU2aGpKZm9CZFpocWlub1F3a2w3QnNYa0Rqc3llbVlQakVEZDk4QTkxTWxnZ9IBuwFBVV95cUxQUGdWRG5XcGNzTk44TjFSelptRVJJdkhtMjFBQWdsYlZDYUNWQ2d4RTRHbzQ3SkF0OU9HNEVkMU9vbllZbUxCMzVWdWlhTTBVVHJ1UnRFb3BFREtwOHljQklrcDJFZ2hJbTJPUlVfWTM2QlRYcVVSenRlclBrbzYyUXhmSzRSX2tYX0lRZWpVeXc4MUg3dExHT0ZZVmVfREliclZVckFkYm5JbW9Fa1dLWDlZSXZSNkhTYS1N?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxPYTJicFA2UmI2NFk2S29QbmlmLVJiRGRIVG1GeXJWYjRoeXpPXzdPRktLbXR3dzBCUFhGZDNWZllkUmFqekRQWWVKVThsd2VZY2J1bDVaREUzRjRsSEdyaFhHYmhRZWpSbF9USUtTZ3FRTDh3cE1oQ09jTm9PWU5Va1M4YkZyMmo3eU54bWVHY0dvX1ZqUkJYWW11MjhQMzNSNXc?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxPYVVSRERqVDdrOS01N0lHOWpJSjRFMDVDQjZPcjdLUWlISHlmZGVYV2FNbjEyQlV4WnNKMU5YaU9XZ1FTOEEzSDNCRjZ2NTJ5MUhVb0F6T1Y4WDNWRE1scll0LUtlWnRXYk5jZjJaZXA2V3AtZjRsYXpTOEphUFpnbU1zRk1JVjRMcnBfNlBCRE4tQmxFXy1mTnJIcDlDMFlVMHBDcjROZ25JRURVbmZJ?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxQZUVNUGFsSURIQW9ncTNzcFVUNk0wLVRoRU96SDhtOHBycU04MXJXZW5ZTnVTU01rVW9PME9WMlYwLW50U1Fmd3ZBV3lpaEJaZUk5VWs4Y05NRGZIMHJVRmxuVzVWbERBQlpMcFUwd1JrbnlwS0FKV2JDVWRLemhpYlNhd2R5NWt1R01rRHBPdnJRdDVmb05iZGNHQXJ6dTBxbW5DamhwWmxhaFpna1BKQmxhV1hNYlJRbzVidktmQ3N2QQ?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxObHl6UFg0RmRmWXdsZHllLVp6VWs5WHcxWTlraVhPR3hfdGtPMnJnTEkwZUxZakktLUNWU19hMS1aZnRhQjk4eERNN3RIbGZxM3pCVHotUjhwbmwyVUViTVctbFU3X1Nxb3JReE9aTm5JbTBXZWhyeU5zci1PTXV1REJJYjYtOFN4TEoweUc5Qi1GWU9W?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxOdlZnZWpJYXhac2ZUM2w2TGVrQ0lvb084bGRIeUZsSXJmbDdwUlpQNzhyWlNXYkxxQVU1SGoycUhGMzd6VEZJQ0dfT0xEeFREN1pQLTJTa1EzREtYTXA0MGV3WDEzeXdiWnhNUml4c3F6cnZpNWJfM3lTdFBmMDVINl81MGxSV0d2b3pxbkVsa3hJX3dNZ1Y0clBn?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxQeElvQXI0RHF2Vkd4cDBoMEVpc3VJcHBKY3NLMVNRbXBMUFNReTlTbF9Zb08wZUVTNFNCUjJfRS1BeE11MGp5YjV3a21qOGZlbkRlTUxvcktRNVNSWElFREN6NTZsVjltVnRKWEVKZ3JVVE9ETkQzMmZfS1V6WUF2bjNITkdObzI2c0pkbU1BU1pqMEpNZkV3?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
