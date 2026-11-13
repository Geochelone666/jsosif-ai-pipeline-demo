# AAPL Intelligence Report

- ticker: **AAPL**
- Report as_of: **2026-11-12**
- Market data as_of: **2026-11-12**
- Quant sources: https://finance.yahoo.com/quote/AAPL/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AAPL/key-statistics/
- AI analysis snapshot as_of: **2026-11-12**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-13T05:01:41.121436+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 4, 'ai': 18, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **10** exact headline/source/date matches; prior report **20261112T054014Z-6c47e7f9/AAPL** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **13**; {'directional_claim_without_event_type': 8, 'low_uncalibrated_model_confidence': 5}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 11 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 44.0%; oldest publication 2026-11-05

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 354.8800 |
| Return 1D (%) | -0.1351 |
| Return 1W (%) | 3.1902 |
| Return 1M (%) | 4.1586 |
| Return YTD (%) | 30.9926 |
| Return 1Y (%) | 30.2214 |
| Annualized volatility (%) | 24.9333 |
| Beta vs SPY | 0.6160 |
| Max drawdown (%) | -13.7985 |
| Sharpe (rf=0) | 1.1884 |
| Downside deviation (rf=0, %) | 16.9428 |
| Sortino (rf=0) | 1.7489 |
| Historical VaR 95% (1D, %) | 2.0034 |
| Historical ES 95% (1D, %) | 3.4742 |
| Correlation vs SPY | 0.3393 |
| Tracking error vs SPY (%) | 24.0394 |
| P/E (trailing) | 39.52 |
| P/B | 46.01 |
| EV/EBITDA | 30.29 |
| Revenue growth (%) | 11.70 |
| Forward P/E (estimate) | 33.65 |
| Gross margin (%) | 48.79 |
| Operating margin (%) | 33.01 |
| Return on equity (%) | 142.26 |
| Free cash flow yield (%) | 2.05 |
| MA50 | 338.2236 |
| Close vs MA50 (%) | 4.9247 |
| MA200 | 300.2802 |
| Close vs MA200 (%) | 18.1830 |
| RSI (14, Wilder) | 59.9519 |
| MACD (12,26) | 3.7948 |
| MACD signal (9) | 3.0602 |
| MACD histogram | 0.7346 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AAPL': 281, 'SPY': 281}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 354.8800 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.1351 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 3.1902 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 4.1586 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 30.9926 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 30.2214 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 24.9333 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 16.9428 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.7489 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.0034 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.4742 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.3393 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 24.0394 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.6160 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -13.7985 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.1884 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 33.6524 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 48.7860 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 33.0100 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 142.2570 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.0488 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 39.5189 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 59.9519 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.7346 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 4.9247 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 18.1830 -> Clearly above the moving-average trend level.

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

### Apple Inc. (AAPL) Rallied 15% as Investors Reassessed Its Growth: What’s Next for the Stock?
- Summary: Apple shares surged 15% after investors reassessed growth prospects.
- Date: 2026-11-10 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxQOTluMHhsdUl2LXpHekdlOUZIWmFHQ0t5M3c1LTJaNm9uUU9ENHJlQ25BNzN6SFJaaXd5NVE0SlJtMEl2UHBhNnllV0JXVS1GRGhJWUdEMjBxT1RhRDBwTmo1R2hnNTZpOVpPb3Z4YVl0My0tQTc0NTZMZzZKTnpGOHlNYXUtd252c3NSOE9vMFhybUc4?oc=5>

### Apple: Capex-Light AI Amid Regulatory Uncertainty (Rating Upgrade)
- Summary: Apple’s rating upgrade signals confidence in its AI strategy amid regulatory uncertainty.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxQZTA4SG95UkQwOXZ5amtHTXJlT0ZsNE5lejVQZDBudkFRS1BsbVo2WjV4a1cwYUNvVUdfZ1dKZTBJZHZIRUh0Y3hCc1BPd2hFU0FXd3VKTDhnNGdoYUxhMjNHUHpWcFNPcDh3WWtZdGJpNlZ0eThnNVZmU0hGb2lFdEdSTDdJWS0zSmQ1MlFDTHYzanRNSVRFX1RvVTZwQnBJMXVyR0tsUVFxb0JxSkc4?oc=5>

### Apple (AAPL) Stock: $348.51, Down 0.62% Nov 10
- Summary: Current Apple stock price and recent decline.
- Date: 2026-11-11 | Impact: low | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxOMUpaWVdPaHVGd2dQLXBWZHo0TXpUYWthUWxrUnYzNHg4TzRGWWZaVEl6dEpFaEQ0M3F0VmtqeTZ5YkpMNkthTDUtbWg5bXNZMXpLRnJBUUNzRHQwM09CVF9YSURjYjlGem9lOS1WVHhoZjRuLURYdUFEYWpndWtnOGhOY0dkX3JPT3FzcWtVZXdpM3ZDQzZEOGJSZkRaVHc?oc=5>

### Apple Is Above $5 Trillion After Its First-Ever Close Above $350
- Summary: Apple's market cap surpassed $5 trillion following a record close above $350.
- Date: 2026-11-10 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxPeDE2Yk1XT0NWbHpadlh6V3ZYc3hwOTQxWFQ2V0lfcUJoY3JEM2hrRk0yMnI2b0dfN3lxZUJHcURsdVBlVzVjMkt4N1A1MnhkckpWb2lOTndwZUF3MVZsUW1vN2pZV3ZZOVFtNjh3MTh1bWpYaHJNVzVGNWJWTDlUMnhKMXVuamtpWHFKanZ1TnNOR3owbE1QU1JZQm9zN2x4eTN6dVRZS0J1dw?oc=5>

### Apple Inc. (AAPL) stock price, news, quote and history
- Summary: General update on Apple stock price and historical data.
- Date: 2026-11-12 | Impact: low | Horizon: short | Confidence: 0.5
- Sources: <https://news.google.com/rss/articles/CBMiUkFVX3lxTE1RekFrNTdjZWx5T0FxTHdGWE9RWlJEakdYdWtNRkJNOGdka3FSdkdwWEgzYUgtanJUb0llSVdZdW5QTE9Mb3pPUGI0LV9jcXpvRVE?oc=5>

### What Is Going on With Apple Stock on Thursday?
- Summary: Discussion of Apple stock movements on a specific day.
- Date: 2026-11-12 | Impact: low | Horizon: short | Confidence: 0.5
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxON1hYY01mSnpmdUdVUVFPdG84eGc1R2JnZC1VTDVFYkRRQ0ZMNmFXTktyTm1LZHdDejUzTURxcVFQQ1kyUDFoT25jeXJYX1NTRzRNYldGZVpJWmw1dVVDQ203ckhQeUU1OGM5aVFGSkhwWFZQQVF2ZEtlbW1TU3hoMHgxQThqM3hObk1KN0c3VjQzckVlaURrVlVkdTFWTjdkQ2c?oc=5>

### Apple Inc. (AAPL) Stock Price, News, Quote & History
- Summary: Overview of Apple stock price and related news.
- Date: 2026-11-11 | Impact: low | Horizon: short | Confidence: 0.5
- Sources: <https://news.google.com/rss/articles/CBMiUkFVX3lxTE5TSWlVaERqVVBsb2hTVzZaa3l2bkpRTGZVT0lzaGo2TDNNRzVKMkttcFRXV2U1T1RDLVBLNktsRmxVcTNtbXpmTGFLUHdsT3VmR1E?oc=5>

### Apple: Deserves Costco's Multiple (Rating Upgrade) (NASDAQ:AAPL)
- Summary: Analysis of Apple’s valuation relative to Costco with a rating upgrade.
- Date: 2026-11-12 | Impact: low | Horizon: short | Confidence: 0.5
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxNX1Q3Q0ppRGVaRnZnZmo0ekF1V3FUZkh0YTEwVXhYX2REUGIteGNjaTl2a2szb21zQkd3eEdMOHdlYlhhNFMzeVlIbWQwbFk1VFdHckxmQW9qcExZSlQ2S1UtTGJleWZEQ28yRHF5OGZUbVZQOGs3UHRtT3pVSDNVSTZzdVVicEFkV0VhOXBMczA?oc=5>

### Drama Notable Only By Its Absence: Why Investors Love Apple (NASDAQ:AAPL)
- Summary: Exploration of investor sentiment toward Apple amid market calm.
- Date: 2026-11-12 | Impact: low | Horizon: short | Confidence: 0.5
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxNWDQtTm5fUUhEZ1R2UnlWV3NrZnF0alhzalJBWFloTG5ucFJRZldRdTc5T2p2ZUI1X0Q5U0JlcHF3VEtWOFRFUnlDSzR2cTlER09HQWNUX2gwTWRtS2ZXLXQtNEJ2a1hGOXhsb0ZQS2l3MmNpeF81U3hmLW0zMnBoWUtLT29KUGI2YTJBdDJZZkZOOEthYXFhamYzSUJseTcw?oc=5>

### Apple (AAPL) Sees $460.3 Million in Net ETF Buying on Nov. 10
- Summary: Apple reports significant net ETF buying, indicating strong investor demand.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxOdDJER0dOZTdtdWwxU1FtekJMOFl1MVhYbDhHQ044RjB2NlVza1NDaUNRUVZMTGtLTlM4b19KTmZHazlrcXV4VTgtX0NSSldrU0hTVWl0Y05wdzlLXzRxUXFEVk01RTh0ZVBFQ0RKcVQtV2tsb2dsQ21RUEE1YVlXTjNORnd2RVJmaWU4RWRYYw?oc=5>

## HEADWINDS

### ETFs Are Net Sellers of Apple (AAPL) on Nov. 5
- Summary: ETFs sold Apple shares, adding downward pressure on the stock.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxQOVRSNEFPS0VIX0ZGNVZzOEp6YnFxenV3NFJ2T0hWc1NGYmRsNjBVemZjY0xfa0FiWVlWc0FrVFFYOVFHVjBob1FFX3lxYlhKclVvZXdhWDJUeWhyLXVlNUUyUlVmZThnTUpiRE9GZng0VWpscE5KNXdkUkNWNllCaVlRV0V1TV9KWWZEdlFZdV8xWWRlb2g4?oc=5>

## CATALYSTS

### Apple (AAPL): A CIBC Pick Riding Record Results and a New iPhone Lineup
- Summary: Apple (AAPL): A CIBC Pick Riding Record Results and a New iPhone Lineup
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxObkprVXRMSk04czVtX0RBcEE1RGhOeTd6dHZpLTRiYkFXUnVUVHJFdnZBUFRsMXlSZU9yTkNlbEp2Q0JMZzJSWHhKTVlfTmdPbGo3Z3MxV1ZWeDJIZ3FDLUMwcXB1SWg5eUxfZlpZZTdnSWtOWFF2NnI4cFAxb05hNzJLbnBxNzdRNkNOajZUbmdELVVMY1dj?oc=5>

### Apple (AAPL) Stock Gets Fair Value Bump As Analysts Debate Margins And iPhone Demand
- Summary: Apple (AAPL) Stock Gets Fair Value Bump As Analysts Debate Margins And iPhone Demand
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxNZHZNT19NWVNzc0ZrNmpzYlVESDQ1RFZyRTd4SlU5Q000TnJBUzlUTEhKdHRodWpjdmtjMkxMQW5GV0FveDhRaWU3MDluZUYxTnp4R1RsQTZSM3duU2F4aWxSZWJJNXlwc09PVjRFaDRUX051YmFPRnRRY3VoUkRFcS1aMjVtYno3SFUyTFVaTlFmTU5Ca2c?oc=5>

### Apple’s iPhone Demand Surges, But AAPL Still Isn’t a ‘Strong Buy’
- Summary: Apple’s iPhone Demand Surges, But AAPL Still Isn’t a ‘Strong Buy’
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQNDVKTlMwU0ZacGZ4WmxuNnJHQTh4aXh1dk9oRUhMNEo1ZEpsU3dVTFZqQlhVb09DXzJTTDJkWFVGdDM5STVybEhlUTI3QlIzd1R3UjVFbUw3ODZTc0pBU3RSTHBpRVFfZkFpdUp6WXlpQ3NOcEVtb2VYcV9MTXZYaTExUHRKeUFiQ0p2QXdhZzFZMEE1NUNXbi1qbEk?oc=5>

### Apple (AAPL) Stock Could Be 30% Overvalued Despite Record iPhone Sales
- Summary: Apple’s stock may be overvalued by 30% despite strong iPhone sales.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxObHl6UFg0RmRmWXdsZHllLVp6VWs5WHcxWTlraVhPR3hfdGtPMnJnTEkwZUxZakktLUNWU19hMS1aZnRhQjk4eERNN3RIbGZxM3pCVHotUjhwbmwyVUViTVctbFU3X1Nxb3JReE9aTm5JbTBXZWhyeU5zci1PTXV1REJJYjYtOFN4TEoweUc5Qi1GWU9W?oc=5>

### China Renaissance Upgraded Apple (AAPL) to Buy. DZ Bank Cut It to Sell. Here’s the Split
- Summary: China Renaissance upgrades Apple to Buy, while DZ Bank downgrades to Sell, reflecting mixed analyst views.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxOdUoxTFBXd2RMMTVLOW9QaE9rSzFXWmg5cGxiVDJsejJIZXlQckR1Q3pVeU93WHhMeUFoQTlPOVJHMTN2ekZ5TFlGSUFhVXJCVjhObDhEak1rR01XWVRaSVBOd05XUnhNOWltYTQ4T01mSGRjU1BJWDZqQnF2bjFHU1BaSmhwRzVFemdBSTZkWHlUT3hKWnhmV21BNjFpZlBkYTFTeg?oc=5>

### Apple (AAPL) Stock Hits New 52-Week High
- Summary: Apple shares reach a new 52‑week peak, reflecting strong investor confidence.
- Date: 2026-11-09 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxQTWNWeXk1bWJyZU5ndU5uOHZBbFYzT29IN0Q1anlPMGxXVzV3cWxiaXhpcFNhM20xSkRMN3NHSVZ0a0l5OVpFZ0xYSC1vQzhvQk5ROEJ4c052WjNQUnBXQmthUE5JSTdQbmVKWGJLdE5hcmVCdk9uLUF5alQ1THVEVzlIa2VBTkJYVnhSRFhn?oc=5>

### Apple (AAPL) Pushes AI Timelines Higher As Siri Engineering Leadership May Change
- Summary: Apple may accelerate AI development and change Siri leadership, indicating a push toward advanced AI features.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxNT0FHLVF5SkhsQk1nQko5eDF6X3lqRXVmRlViX2E1YVdmSUJXelp5a21DUmpaNFJ0cHExaGF1cmFSTXVGb2Z3cmw3anZOYm1MNFdnbXAxcnAwVDJ3d0d2Rk9IOWtXOFFpNW85RVN1ekVtTmRidk5ZUERKc3pXdk80cDc3YnV4STVzLUtDdnAtTWFNV2xYVTNWb0Fn?oc=5>

## RISKS

### Apple (AAPL) Faces A 38% Premium Following Fresh Debt Issuance
- Summary: Apple’s new debt issuance led to a 38% premium, raising concerns about future debt servicing and potential dilution.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxQeElvQXI0RHF2Vkd4cDBoMEVpc3VJcHBKY3NLMVNRbXBMUFNReTlTbF9Zb08wZUVTNFNCUjJfRS1BeE11MGp5YjV3a21qOGZlbkRlTUxvcktRNVNSWElFREN6NTZsVjltVnRKWEVKZ3JVVE9ETkQzMmZfS1V6WUF2bjNITkdObzI2c0pkbU1BU1pqMEpNZkV3?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AAPL** | **39.52** | **46.01** | **30.29** | **11.70** | **5,157,180,932,096.00 USD** | **30.22** |
| MSFT | 27.20 | 8.26 | 19.22 | 18.80 | 3,883,899,813,888.00 USD | 3.16 |
| GOOGL | 15.60 | 5.57 | 19.27 | 24.70 | 3,672,217,747,456.00 USD | 4.45 |
| SONY | 19.90 | 2.88 | 0.30 | 10.30 | 155,381,235,712.00 USD | -11.90 |

Peers fetched as_of: 2026-11-12; AAPL reuses existing data (market data as_of: 2026-11-12); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-02
- Next expected earnings: 2027-01-28 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-12

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
- https://news.google.com/rss/articles/CBMilAFBVV95cUxQOTluMHhsdUl2LXpHekdlOUZIWmFHQ0t5M3c1LTJaNm9uUU9ENHJlQ25BNzN6SFJaaXd5NVE0SlJtMEl2UHBhNnllV0JXVS1GRGhJWUdEMjBxT1RhRDBwTmo1R2hnNTZpOVpPb3Z4YVl0My0tQTc0NTZMZzZKTnpGOHlNYXUtd252c3NSOE9vMFhybUc4?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxQZTA4SG95UkQwOXZ5amtHTXJlT0ZsNE5lejVQZDBudkFRS1BsbVo2WjV4a1cwYUNvVUdfZ1dKZTBJZHZIRUh0Y3hCc1BPd2hFU0FXd3VKTDhnNGdoYUxhMjNHUHpWcFNPcDh3WWtZdGJpNlZ0eThnNVZmU0hGb2lFdEdSTDdJWS0zSmQ1MlFDTHYzanRNSVRFX1RvVTZwQnBJMXVyR0tsUVFxb0JxSkc4?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxOMUpaWVdPaHVGd2dQLXBWZHo0TXpUYWthUWxrUnYzNHg4TzRGWWZaVEl6dEpFaEQ0M3F0VmtqeTZ5YkpMNkthTDUtbWg5bXNZMXpLRnJBUUNzRHQwM09CVF9YSURjYjlGem9lOS1WVHhoZjRuLURYdUFEYWpndWtnOGhOY0dkX3JPT3FzcWtVZXdpM3ZDQzZEOGJSZkRaVHc?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxPeDE2Yk1XT0NWbHpadlh6V3ZYc3hwOTQxWFQ2V0lfcUJoY3JEM2hrRk0yMnI2b0dfN3lxZUJHcURsdVBlVzVjMkt4N1A1MnhkckpWb2lOTndwZUF3MVZsUW1vN2pZV3ZZOVFtNjh3MTh1bWpYaHJNVzVGNWJWTDlUMnhKMXVuamtpWHFKanZ1TnNOR3owbE1QU1JZQm9zN2x4eTN6dVRZS0J1dw?oc=5
- https://news.google.com/rss/articles/CBMiUkFVX3lxTE1RekFrNTdjZWx5T0FxTHdGWE9RWlJEakdYdWtNRkJNOGdka3FSdkdwWEgzYUgtanJUb0llSVdZdW5QTE9Mb3pPUGI0LV9jcXpvRVE?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxON1hYY01mSnpmdUdVUVFPdG84eGc1R2JnZC1VTDVFYkRRQ0ZMNmFXTktyTm1LZHdDejUzTURxcVFQQ1kyUDFoT25jeXJYX1NTRzRNYldGZVpJWmw1dVVDQ203ckhQeUU1OGM5aVFGSkhwWFZQQVF2ZEtlbW1TU3hoMHgxQThqM3hObk1KN0c3VjQzckVlaURrVlVkdTFWTjdkQ2c?oc=5
- https://news.google.com/rss/articles/CBMiUkFVX3lxTE5TSWlVaERqVVBsb2hTVzZaa3l2bkpRTGZVT0lzaGo2TDNNRzVKMkttcFRXV2U1T1RDLVBLNktsRmxVcTNtbXpmTGFLUHdsT3VmR1E?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxNX1Q3Q0ppRGVaRnZnZmo0ekF1V3FUZkh0YTEwVXhYX2REUGIteGNjaTl2a2szb21zQkd3eEdMOHdlYlhhNFMzeVlIbWQwbFk1VFdHckxmQW9qcExZSlQ2S1UtTGJleWZEQ28yRHF5OGZUbVZQOGs3UHRtT3pVSDNVSTZzdVVicEFkV0VhOXBMczA?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxNWDQtTm5fUUhEZ1R2UnlWV3NrZnF0alhzalJBWFloTG5ucFJRZldRdTc5T2p2ZUI1X0Q5U0JlcHF3VEtWOFRFUnlDSzR2cTlER09HQWNUX2gwTWRtS2ZXLXQtNEJ2a1hGOXhsb0ZQS2l3MmNpeF81U3hmLW0zMnBoWUtLT29KUGI2YTJBdDJZZkZOOEthYXFhamYzSUJseTcw?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxOdDJER0dOZTdtdWwxU1FtekJMOFl1MVhYbDhHQ044RjB2NlVza1NDaUNRUVZMTGtLTlM4b19KTmZHazlrcXV4VTgtX0NSSldrU0hTVWl0Y05wdzlLXzRxUXFEVk01RTh0ZVBFQ0RKcVQtV2tsb2dsQ21RUEE1YVlXTjNORnd2RVJmaWU4RWRYYw?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxQOVRSNEFPS0VIX0ZGNVZzOEp6YnFxenV3NFJ2T0hWc1NGYmRsNjBVemZjY0xfa0FiWVlWc0FrVFFYOVFHVjBob1FFX3lxYlhKclVvZXdhWDJUeWhyLXVlNUUyUlVmZThnTUpiRE9GZng0VWpscE5KNXdkUkNWNllCaVlRV0V1TV9KWWZEdlFZdV8xWWRlb2g4?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxObkprVXRMSk04czVtX0RBcEE1RGhOeTd6dHZpLTRiYkFXUnVUVHJFdnZBUFRsMXlSZU9yTkNlbEp2Q0JMZzJSWHhKTVlfTmdPbGo3Z3MxV1ZWeDJIZ3FDLUMwcXB1SWg5eUxfZlpZZTdnSWtOWFF2NnI4cFAxb05hNzJLbnBxNzdRNkNOajZUbmdELVVMY1dj?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxNZHZNT19NWVNzc0ZrNmpzYlVESDQ1RFZyRTd4SlU5Q000TnJBUzlUTEhKdHRodWpjdmtjMkxMQW5GV0FveDhRaWU3MDluZUYxTnp4R1RsQTZSM3duU2F4aWxSZWJJNXlwc09PVjRFaDRUX051YmFPRnRRY3VoUkRFcS1aMjVtYno3SFUyTFVaTlFmTU5Ca2c?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQNDVKTlMwU0ZacGZ4WmxuNnJHQTh4aXh1dk9oRUhMNEo1ZEpsU3dVTFZqQlhVb09DXzJTTDJkWFVGdDM5STVybEhlUTI3QlIzd1R3UjVFbUw3ODZTc0pBU3RSTHBpRVFfZkFpdUp6WXlpQ3NOcEVtb2VYcV9MTXZYaTExUHRKeUFiQ0p2QXdhZzFZMEE1NUNXbi1qbEk?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxObHl6UFg0RmRmWXdsZHllLVp6VWs5WHcxWTlraVhPR3hfdGtPMnJnTEkwZUxZakktLUNWU19hMS1aZnRhQjk4eERNN3RIbGZxM3pCVHotUjhwbmwyVUViTVctbFU3X1Nxb3JReE9aTm5JbTBXZWhyeU5zci1PTXV1REJJYjYtOFN4TEoweUc5Qi1GWU9W?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxOdUoxTFBXd2RMMTVLOW9QaE9rSzFXWmg5cGxiVDJsejJIZXlQckR1Q3pVeU93WHhMeUFoQTlPOVJHMTN2ekZ5TFlGSUFhVXJCVjhObDhEak1rR01XWVRaSVBOd05XUnhNOWltYTQ4T01mSGRjU1BJWDZqQnF2bjFHU1BaSmhwRzVFemdBSTZkWHlUT3hKWnhmV21BNjFpZlBkYTFTeg?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxQTWNWeXk1bWJyZU5ndU5uOHZBbFYzT29IN0Q1anlPMGxXVzV3cWxiaXhpcFNhM20xSkRMN3NHSVZ0a0l5OVpFZ0xYSC1vQzhvQk5ROEJ4c052WjNQUnBXQmthUE5JSTdQbmVKWGJLdE5hcmVCdk9uLUF5alQ1THVEVzlIa2VBTkJYVnhSRFhn?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxNT0FHLVF5SkhsQk1nQko5eDF6X3lqRXVmRlViX2E1YVdmSUJXelp5a21DUmpaNFJ0cHExaGF1cmFSTXVGb2Z3cmw3anZOYm1MNFdnbXAxcnAwVDJ3d0d2Rk9IOWtXOFFpNW85RVN1ekVtTmRidk5ZUERKc3pXdk80cDc3YnV4STVzLUtDdnAtTWFNV2xYVTNWb0Fn?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxQeElvQXI0RHF2Vkd4cDBoMEVpc3VJcHBKY3NLMVNRbXBMUFNReTlTbF9Zb08wZUVTNFNCUjJfRS1BeE11MGp5YjV3a21qOGZlbkRlTUxvcktRNVNSWElFREN6NTZsVjltVnRKWEVKZ3JVVE9ETkQzMmZfS1V6WUF2bjNITkdObzI2c0pkbU1BU1pqMEpNZkV3?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
