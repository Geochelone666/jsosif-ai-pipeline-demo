# AAPL Intelligence Report

- ticker: **AAPL**
- Report as_of: **2026-11-10**
- Market data as_of: **2026-11-10**
- Quant sources: https://finance.yahoo.com/quote/AAPL/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AAPL/key-statistics/
- AI analysis snapshot as_of: **2026-11-10**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-11T04:52:38.016786+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 9, 'ai': 10, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **8** exact headline/source/date matches; prior report **20261110T055129Z-abd33250/AAPL** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 16 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 28.0%; oldest publication 2026-11-04

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 348.5100 |
| Return 1D (%) | -0.6216 |
| Return 1W (%) | 5.0045 |
| Return 1M (%) | 3.5260 |
| Return YTD (%) | 28.5436 |
| Return 1Y (%) | 29.7030 |
| Annualized volatility (%) | 24.9532 |
| Beta vs SPY | 0.6100 |
| Max drawdown (%) | -13.7985 |
| Sharpe (rf=0) | 1.1716 |
| Downside deviation (rf=0, %) | 16.9546 |
| Sortino (rf=0) | 1.7243 |
| Historical VaR 95% (1D, %) | 2.0034 |
| Historical ES 95% (1D, %) | 3.4742 |
| Correlation vs SPY | 0.3342 |
| Tracking error vs SPY (%) | 24.1150 |
| P/E (trailing) | 38.81 |
| P/B | 45.18 |
| EV/EBITDA | 29.75 |
| Revenue growth (%) | 11.70 |
| Forward P/E (estimate) | 33.03 |
| Gross margin (%) | 48.79 |
| Operating margin (%) | 31.13 |
| Return on equity (%) | 142.26 |
| Free cash flow yield (%) | 2.09 |
| MA50 | 337.2668 |
| Close vs MA50 (%) | 3.3336 |
| MA200 | 299.5210 |
| Close vs MA200 (%) | 16.3558 |
| RSI (14, Wilder) | 55.6219 |
| MACD (12,26) | 2.6921 |
| MACD signal (9) | 2.7597 |
| MACD histogram | -0.0676 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AAPL': 279, 'SPY': 279}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 348.5100 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.6216 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 5.0045 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 3.5260 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 28.5436 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 29.7030 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 24.9532 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 16.9546 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.7243 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.0034 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.4742 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.3342 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 24.1150 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.6100 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -13.7985 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.1716 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 33.0284 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 48.7860 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 31.1250 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 142.2570 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.0862 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 38.8096 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 55.6219 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.0676 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 3.3336 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 16.3558 -> Clearly above the moving-average trend level.

## TAILWINDS

### Apple Stock (AAPL) Rises 5.3% as Big Tech Gains on Midterms (Nov 4)
- Summary: Apple Stock (AAPL) Rises 5.3% as Big Tech Gains on Midterms (Nov 4)
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMifkFVX3lxTE40TFN3cG1ONnB1LUNONTZqY1hEQ09ZcEJrX2RvSDhQclk4RU1DZm93c1h6YjdmbjFDZnlLMmt3Y093TWQxdjQ0Q3VwOUxxdTVNLWRndEcxU1hObmJHRzhRTE1VLXpqc3ZoVjhkeEhKWEltaFA1YXNVeTVSVkNpdw?oc=5>

### Apple Stock Price Forecast: AAPL Pulls Back After Short-Term Surge to $350, Outlook Bullish for Break Above $400 Mark
- Summary: Apple Stock Price Forecast: AAPL Pulls Back After Short-Term Surge to $350, Outlook Bullish for Break Above $400 Mark
- Date: 2026-11-07 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxQa1E3eDRPU2dMSXRtMDh2U0N3Ylhqei15dmMzT0N3LVBrOFR5UlFRSTQwTEpKWmpWSTdBQzVkOTE4ZHJrU3B2YmRCNTJWRS1lU2tjYk5ZRlVHOFdnSnBYWERPY1phQVlNS3BRMVp3S2hJdXBFa1BQTFg0QUhuS05hVDlnM2dQVENDVUF6TWoxaXAtVUNqOG1Rcy1JRGtFb2NEVGZOaUtxSjhIQm9BMkV6YVhVc3N5WmloRHJtQ2tWVQ?oc=5>

### AAPL Stock Ticks Up After Clearing Key Regulatory Step in China for Apple Intelligence’s AI for iPads and Macs
- Summary: Apple’s AI for iPads and Macs cleared a key Chinese regulatory step, lifting the stock.
- Date: 2026-11-09 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxOSFh0M3FIZjBqaXlfTHdSaDdQelFBMEtmczRVVFdNUDhlV1pmaGI0ZXhiRmNQaHpYQXpBV3ZvYXE3V3RBamFaRW5XcnVRYkVRTVBvdV82X21mUno2U2lqeGlqTV9jMnAydnJSN2JCWUU5RlJLX1JvTXlmaVU2ODhJV0VrbFJ3REJadEpvUDZpUFRlNWxveUFONUxUREZ3ckN2OTcxYURnQjhobGFsTlI1VzJZVk1IRFUxeEUtZzFjeTRkSjI4NjFIMGlYdGo2NTlsb05STGln?oc=5>

### Apple (AAPL) Stock Hits New 52-Week High
- Summary: Apple’s stock reached a new 52‑week high, indicating strong investor confidence.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxQTWNWeXk1bWJyZU5ndU5uOHZBbFYzT29IN0Q1anlPMGxXVzV3cWxiaXhpcFNhM20xSkRMN3NHSVZ0a0l5OVpFZ0xYSC1vQzhvQk5ROEJ4c052WjNQUnBXQmthUE5JSTdQbmVKWGJLdE5hcmVCdk9uLUF5alQ1THVEVzlIa2VBTkJYVnhSRFhn?oc=5>

### Why did Apple Stock Hit an All-Time High Amid US Stock Market Crash?
- Summary: Apple’s stock surged to an all‑time high despite broader market downturns.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxOTmd6dkx0WWVDNTdFYkI0WF95QjJxaVVmam56Z0xKRURsN1VManBmdUNkajJXMzhSZzdaTlZ2ek1MOUY2LWtPTHJzbjdFaWJjSHVGQkRjTWVPVHhkdzVnbTE5T2hlZVFxRi02MnNBTUZvZmpmTzdIdGNhcVFKN1NCdlZEMkRiUC12WTBHN1hwOXo4SjQ?oc=5>

### Apple Inc. (AAPL) Rallied 15% as Investors Reassessed Its Growth: What’s Next for the Stock?
- Summary: Apple shares surged 15% after investors reassessed growth prospects.
- Date: 2026-11-10 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxQOTluMHhsdUl2LXpHekdlOUZIWmFHQ0t5M3c1LTJaNm9uUU9ENHJlQ25BNzN6SFJaaXd5NVE0SlJtMEl2UHBhNnllV0JXVS1GRGhJWUdEMjBxT1RhRDBwTmo1R2hnNTZpOVpPb3Z4YVl0My0tQTc0NTZMZzZKTnpGOHlNYXUtd252c3NSOE9vMFhybUc4?oc=5>

### Apple Is Above $5 Trillion After Its First-Ever Close Above $350
- Summary: Apple's market cap surpassed $5 trillion following a record close above $350.
- Date: 2026-11-10 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxPeDE2Yk1XT0NWbHpadlh6V3ZYc3hwOTQxWFQ2V0lfcUJoY3JEM2hrRk0yMnI2b0dfN3lxZUJHcURsdVBlVzVjMkt4N1A1MnhkckpWb2lOTndwZUF3MVZsUW1vN2pZV3ZZOVFtNjh3MTh1bWpYaHJNVzVGNWJWTDlUMnhKMXVuamtpWHFKanZ1TnNOR3owbE1QU1JZQm9zN2x4eTN6dVRZS0J1dw?oc=5>

## HEADWINDS

### What Will Decide Apple Stock As Memory Costs Rise?
- Summary: Apple stock influenced by rising memory costs.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxPSlFtVlNyWENVTXUwcV9zQXduMm4wMWQyUVdsQzRSS1hhbmRGNFVjT0JIRDczaW1HUjh1djRIX3FrekxkbXAtUEt6VnRCUWNULUtxOXdaTUo5NlBVdmM5OWlFc2JLMlpscjM2S2FlS2w5SjgxMHlnY3N2R2o0cmFxdDdpUVdROWtZTXY5V3VTbTZnZVVocTJtY081WVJJLVRPNFVySGh4MUhzZkhyaXNJ?oc=5>

## CATALYSTS

### Apple (AAPL) Stock Gets Fair Value Bump As Analysts Debate Margins And iPhone Demand
- Summary: Apple (AAPL) Stock Gets Fair Value Bump As Analysts Debate Margins And iPhone Demand
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxNZHZNT19NWVNzc0ZrNmpzYlVESDQ1RFZyRTd4SlU5Q000TnJBUzlUTEhKdHRodWpjdmtjMkxMQW5GV0FveDhRaWU3MDluZUYxTnp4R1RsQTZSM3duU2F4aWxSZWJJNXlwc09PVjRFaDRUX051YmFPRnRRY3VoUkRFcS1aMjVtYno3SFUyTFVaTlFmTU5Ca2c?oc=5>

### Apple’s iPhone Demand Surges, But AAPL Still Isn’t a ‘Strong Buy’
- Summary: Apple’s iPhone Demand Surges, But AAPL Still Isn’t a ‘Strong Buy’
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQNDVKTlMwU0ZacGZ4WmxuNnJHQTh4aXh1dk9oRUhMNEo1ZEpsU3dVTFZqQlhVb09DXzJTTDJkWFVGdDM5STVybEhlUTI3QlIzd1R3UjVFbUw3ODZTc0pBU3RSTHBpRVFfZkFpdUp6WXlpQ3NOcEVtb2VYcV9MTXZYaTExUHRKeUFiQ0p2QXdhZzFZMEE1NUNXbi1qbEk?oc=5>

### Apple (AAPL) Stock Faces Q4 Earnings Margin Squeeze
- Summary: Apple (AAPL) Stock Faces Q4 Earnings Margin Squeeze
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxOdDdteU5mbzM5MUZVUnZKLWJkdUNXX3JKVlhQVXMtRFdhWExJb2s1Q1Y4VDNrMVRZQ1JnYTVfaHpCeEhrZFpWbVQySDZUM3k1V3RtdXJuNmRuVHpxRDFIdWU3VWY5VURSeDZackdpRFZaRHFYb3FnalBHaWRLWUxXcFNMYmRfU3M0bWRGTi1YUG1Pdkxt?oc=5>

### Apple (AAPL) Stock Looks Fully Valued On Future Cash Flow
- Summary: Apple (AAPL) Stock Looks Fully Valued On Future Cash Flow
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxNMjZ0WXFKaWhlbC1ZZV9jVG5kVVk3ZDhodE5QV1Q3MlNtY3NrS0VidjkwN1l0TmR3VGtsWXpNMTFfbjdNejRHbGF1cFo3bkJaVmtXY2h6OTZGUUF0OUFhLUhhR0xwa1k2TXdaVFdiTkx0Wm9mQkFhX3VTTUpKZnY3YTBYLXAzR0x6QlU2aGpKZm9CZFpocWlub1F3a2w3QnNYa0Rqc3llbVlQakVEZDk4QTkxTWxnZ9IBuwFBVV95cUxQUGdWRG5XcGNzTk44TjFSelptRVJJdkhtMjFBQWdsYlZDYUNWQ2d4RTRHbzQ3SkF0OU9HNEVkMU9vbllZbUxCMzVWdWlhTTBVVHJ1UnRFb3BFREtwOHljQklrcDJFZ2hJbTJPUlVfWTM2QlRYcVVSenRlclBrbzYyUXhmSzRSX2tYX0lRZWpVeXc4MUg3dExHT0ZZVmVfREliclZVckFkYm5JbW9Fa1dLWDlZSXZSNkhTYS1N?oc=5>

### Apple Inc. $AAPL Stock Sold by Aire Advisors LLC
- Summary: Apple Inc. $AAPL Stock Sold by Aire Advisors LLC
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxPS0tUMFd5eExfT1ZzcGhRVU8yb2NmY1YxRDgxSDhDcmpLWjYzN2pLNHdoZl9qaXBVWXRPZUNQSlViYTZTMzBZWkhlaFh4WGpxSHVSa2IydkpMYTNHdXBENjhpRUNEdUJ3YW5RRHNLMHhDTVQtZUFBa2VFaDFnZkotUmZzVTlUT2gwQTNrV2RvbGctV0dkVW5zRFNZdW04THd6ODZEZjVPTm9nRmc?oc=5>

### Apple Inc. $AAPL Stock Sold by Smith Chas P & Associates PA Cpas
- Summary: Apple Inc. $AAPL Stock Sold by Smith Chas P & Associates PA Cpas
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxQck5EeXRtcDhvZWM3ZVVMRHpmOVZUMVFieFRXb0xxVjliX2dnS3hXRktoY2IxdFc5Sldjc2k0eHlOelRwTFkwYThQZnhWSkU1WFpMSE4zdWI3bmlveDlTWEh6NGJOZ1lRN19EekdSYXF0SG1fRmpuMFQxVmoyajFVdk56Ul8tREREM0lHU09mWWRDbnAtSDFoODhnN2tCdmVXa1ItWWtVOG5XY182eG5jYm5KR3Fmd0FSYTUzbFBB?oc=5>

### Apple Inc. $AAPL Stock Sold by SBI Securities Co. Ltd.
- Summary: Apple Inc. $AAPL Stock Sold by SBI Securities Co. Ltd.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxNV0VMNGFITE0wWms1ZndqSHktZk1mdVBFZnA5djRkZU9wOGJoNm4zamRwaW1GdWRvQUxMQ0RNWGQzWTJaVGVaRXFNclhVWG1HYkFEdkZXRDdIZ3BydXRZZV9ob21jejQ0TVpGNW05WEI1azVpaVloSHpHbGpQV3dTYlhsbzNsVG1nOHlkMGlPQm9DQUNBd3pCdWF4T2MwZXhJQzB0UTg3d0tmUE9wS0VidQ?oc=5>

### Apple (AAPL) Stock Could Be 30% Overvalued Despite Record iPhone Sales
- Summary: Apple’s stock may be overvalued by 30% despite strong iPhone sales.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxObHl6UFg0RmRmWXdsZHllLVp6VWs5WHcxWTlraVhPR3hfdGtPMnJnTEkwZUxZakktLUNWU19hMS1aZnRhQjk4eERNN3RIbGZxM3pCVHotUjhwbmwyVUViTVctbFU3X1Nxb3JReE9aTm5JbTBXZWhyeU5zci1PTXV1REJJYjYtOFN4TEoweUc5Qi1GWU9W?oc=5>

### Apple Won’t “Play in Traffic” on AI. It’s Up 28% in a Year: Too Late to Buy?
- Summary: Apple’s cautious AI stance may limit future growth, despite a 28% yearly rise.
- Date: 2026-11-09 | Impact: medium | Horizon: medium | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxOdlZnZWpJYXhac2ZUM2w2TGVrQ0lvb084bGRIeUZsSXJmbDdwUlpQNzhyWlNXYkxxQVU1SGoycUhGMzd6VEZJQ0dfT0xEeFREN1pQLTJTa1EzREtYTXA0MGV3WDEzeXdiWnhNUml4c3F6cnZpNWJfM3lTdFBmMDVINl81MGxSV0d2b3pxbkVsa3hJX3dNZ1Y0clBn?oc=5>

### Apple (AAPL) Reclaims Market Valuation Crown from NVIDIA (NVDA)
- Summary: Apple surpasses NVIDIA in market valuation, boosting its market position.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxOVkZfVUVDRUsydTZvNndiZy1LSU9iMmxyUEV2ZjlBZlQtMTdTcnhNQnptQmc5X1BFM2VubUc3T1V4d3Y2SzZfcm1PQWVaLXFsVGFSX2RUUUtGRC1ZMGdpTVBsNVZfRFVpRl9fR0hkTEFUSktHQ2hSQzlmNVFBUkwyaVc1LTJHV1VBUWNJUnVXcWItM0kyT3RJbVViVnR5VFU?oc=5>

## RISKS

### Apple (AAPL) Faces A 38% Premium Following Fresh Debt Issuance
- Summary: Apple’s new debt issuance led to a 38% premium, raising concerns about future debt servicing and potential dilution.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxQeElvQXI0RHF2Vkd4cDBoMEVpc3VJcHBKY3NLMVNRbXBMUFNReTlTbF9Zb08wZUVTNFNCUjJfRS1BeE11MGp5YjV3a21qOGZlbkRlTUxvcktRNVNSWElFREN6NTZsVjltVnRKWEVKZ3JVVE9ETkQzMmZfS1V6WUF2bjNITkdObzI2c0pkbU1BU1pqMEpNZkV3?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AAPL** | **38.81** | **45.18** | **29.75** | **11.70** | **5,064,611,069,952.00 USD** | **29.70** |
| MSFT | 27.83 | 8.42 | 19.59 | 18.80 | 3,959,349,575,680.00 USD | 6.23 |
| GOOGL | 15.01 | 5.36 | 18.52 | 24.70 | 3,533,049,692,160.00 USD | -0.68 |
| SONY | 20.23 | 2.89 | 0.30 | 10.30 | 155,672,657,920.00 USD | -4.50 |

Peers fetched as_of: 2026-11-10; AAPL reuses existing data (market data as_of: 2026-11-10); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-02
- Next expected earnings: 2027-01-28 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-10

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

- https://news.google.com/rss/articles/CBMifkFVX3lxTE40TFN3cG1ONnB1LUNONTZqY1hEQ09ZcEJrX2RvSDhQclk4RU1DZm93c1h6YjdmbjFDZnlLMmt3Y093TWQxdjQ0Q3VwOUxxdTVNLWRndEcxU1hObmJHRzhRTE1VLXpqc3ZoVjhkeEhKWEltaFA1YXNVeTVSVkNpdw?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxQa1E3eDRPU2dMSXRtMDh2U0N3Ylhqei15dmMzT0N3LVBrOFR5UlFRSTQwTEpKWmpWSTdBQzVkOTE4ZHJrU3B2YmRCNTJWRS1lU2tjYk5ZRlVHOFdnSnBYWERPY1phQVlNS3BRMVp3S2hJdXBFa1BQTFg0QUhuS05hVDlnM2dQVENDVUF6TWoxaXAtVUNqOG1Rcy1JRGtFb2NEVGZOaUtxSjhIQm9BMkV6YVhVc3N5WmloRHJtQ2tWVQ?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxOSFh0M3FIZjBqaXlfTHdSaDdQelFBMEtmczRVVFdNUDhlV1pmaGI0ZXhiRmNQaHpYQXpBV3ZvYXE3V3RBamFaRW5XcnVRYkVRTVBvdV82X21mUno2U2lqeGlqTV9jMnAydnJSN2JCWUU5RlJLX1JvTXlmaVU2ODhJV0VrbFJ3REJadEpvUDZpUFRlNWxveUFONUxUREZ3ckN2OTcxYURnQjhobGFsTlI1VzJZVk1IRFUxeEUtZzFjeTRkSjI4NjFIMGlYdGo2NTlsb05STGln?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxQTWNWeXk1bWJyZU5ndU5uOHZBbFYzT29IN0Q1anlPMGxXVzV3cWxiaXhpcFNhM20xSkRMN3NHSVZ0a0l5OVpFZ0xYSC1vQzhvQk5ROEJ4c052WjNQUnBXQmthUE5JSTdQbmVKWGJLdE5hcmVCdk9uLUF5alQ1THVEVzlIa2VBTkJYVnhSRFhn?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxOTmd6dkx0WWVDNTdFYkI0WF95QjJxaVVmam56Z0xKRURsN1VManBmdUNkajJXMzhSZzdaTlZ2ek1MOUY2LWtPTHJzbjdFaWJjSHVGQkRjTWVPVHhkdzVnbTE5T2hlZVFxRi02MnNBTUZvZmpmTzdIdGNhcVFKN1NCdlZEMkRiUC12WTBHN1hwOXo4SjQ?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxQOTluMHhsdUl2LXpHekdlOUZIWmFHQ0t5M3c1LTJaNm9uUU9ENHJlQ25BNzN6SFJaaXd5NVE0SlJtMEl2UHBhNnllV0JXVS1GRGhJWUdEMjBxT1RhRDBwTmo1R2hnNTZpOVpPb3Z4YVl0My0tQTc0NTZMZzZKTnpGOHlNYXUtd252c3NSOE9vMFhybUc4?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxPeDE2Yk1XT0NWbHpadlh6V3ZYc3hwOTQxWFQ2V0lfcUJoY3JEM2hrRk0yMnI2b0dfN3lxZUJHcURsdVBlVzVjMkt4N1A1MnhkckpWb2lOTndwZUF3MVZsUW1vN2pZV3ZZOVFtNjh3MTh1bWpYaHJNVzVGNWJWTDlUMnhKMXVuamtpWHFKanZ1TnNOR3owbE1QU1JZQm9zN2x4eTN6dVRZS0J1dw?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxPSlFtVlNyWENVTXUwcV9zQXduMm4wMWQyUVdsQzRSS1hhbmRGNFVjT0JIRDczaW1HUjh1djRIX3FrekxkbXAtUEt6VnRCUWNULUtxOXdaTUo5NlBVdmM5OWlFc2JLMlpscjM2S2FlS2w5SjgxMHlnY3N2R2o0cmFxdDdpUVdROWtZTXY5V3VTbTZnZVVocTJtY081WVJJLVRPNFVySGh4MUhzZkhyaXNJ?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxNZHZNT19NWVNzc0ZrNmpzYlVESDQ1RFZyRTd4SlU5Q000TnJBUzlUTEhKdHRodWpjdmtjMkxMQW5GV0FveDhRaWU3MDluZUYxTnp4R1RsQTZSM3duU2F4aWxSZWJJNXlwc09PVjRFaDRUX051YmFPRnRRY3VoUkRFcS1aMjVtYno3SFUyTFVaTlFmTU5Ca2c?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQNDVKTlMwU0ZacGZ4WmxuNnJHQTh4aXh1dk9oRUhMNEo1ZEpsU3dVTFZqQlhVb09DXzJTTDJkWFVGdDM5STVybEhlUTI3QlIzd1R3UjVFbUw3ODZTc0pBU3RSTHBpRVFfZkFpdUp6WXlpQ3NOcEVtb2VYcV9MTXZYaTExUHRKeUFiQ0p2QXdhZzFZMEE1NUNXbi1qbEk?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxOdDdteU5mbzM5MUZVUnZKLWJkdUNXX3JKVlhQVXMtRFdhWExJb2s1Q1Y4VDNrMVRZQ1JnYTVfaHpCeEhrZFpWbVQySDZUM3k1V3RtdXJuNmRuVHpxRDFIdWU3VWY5VURSeDZackdpRFZaRHFYb3FnalBHaWRLWUxXcFNMYmRfU3M0bWRGTi1YUG1Pdkxt?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxNMjZ0WXFKaWhlbC1ZZV9jVG5kVVk3ZDhodE5QV1Q3MlNtY3NrS0VidjkwN1l0TmR3VGtsWXpNMTFfbjdNejRHbGF1cFo3bkJaVmtXY2h6OTZGUUF0OUFhLUhhR0xwa1k2TXdaVFdiTkx0Wm9mQkFhX3VTTUpKZnY3YTBYLXAzR0x6QlU2aGpKZm9CZFpocWlub1F3a2w3QnNYa0Rqc3llbVlQakVEZDk4QTkxTWxnZ9IBuwFBVV95cUxQUGdWRG5XcGNzTk44TjFSelptRVJJdkhtMjFBQWdsYlZDYUNWQ2d4RTRHbzQ3SkF0OU9HNEVkMU9vbllZbUxCMzVWdWlhTTBVVHJ1UnRFb3BFREtwOHljQklrcDJFZ2hJbTJPUlVfWTM2QlRYcVVSenRlclBrbzYyUXhmSzRSX2tYX0lRZWpVeXc4MUg3dExHT0ZZVmVfREliclZVckFkYm5JbW9Fa1dLWDlZSXZSNkhTYS1N?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxPS0tUMFd5eExfT1ZzcGhRVU8yb2NmY1YxRDgxSDhDcmpLWjYzN2pLNHdoZl9qaXBVWXRPZUNQSlViYTZTMzBZWkhlaFh4WGpxSHVSa2IydkpMYTNHdXBENjhpRUNEdUJ3YW5RRHNLMHhDTVQtZUFBa2VFaDFnZkotUmZzVTlUT2gwQTNrV2RvbGctV0dkVW5zRFNZdW04THd6ODZEZjVPTm9nRmc?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxQck5EeXRtcDhvZWM3ZVVMRHpmOVZUMVFieFRXb0xxVjliX2dnS3hXRktoY2IxdFc5Sldjc2k0eHlOelRwTFkwYThQZnhWSkU1WFpMSE4zdWI3bmlveDlTWEh6NGJOZ1lRN19EekdSYXF0SG1fRmpuMFQxVmoyajFVdk56Ul8tREREM0lHU09mWWRDbnAtSDFoODhnN2tCdmVXa1ItWWtVOG5XY182eG5jYm5KR3Fmd0FSYTUzbFBB?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxNV0VMNGFITE0wWms1ZndqSHktZk1mdVBFZnA5djRkZU9wOGJoNm4zamRwaW1GdWRvQUxMQ0RNWGQzWTJaVGVaRXFNclhVWG1HYkFEdkZXRDdIZ3BydXRZZV9ob21jejQ0TVpGNW05WEI1azVpaVloSHpHbGpQV3dTYlhsbzNsVG1nOHlkMGlPQm9DQUNBd3pCdWF4T2MwZXhJQzB0UTg3d0tmUE9wS0VidQ?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxObHl6UFg0RmRmWXdsZHllLVp6VWs5WHcxWTlraVhPR3hfdGtPMnJnTEkwZUxZakktLUNWU19hMS1aZnRhQjk4eERNN3RIbGZxM3pCVHotUjhwbmwyVUViTVctbFU3X1Nxb3JReE9aTm5JbTBXZWhyeU5zci1PTXV1REJJYjYtOFN4TEoweUc5Qi1GWU9W?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxOdlZnZWpJYXhac2ZUM2w2TGVrQ0lvb084bGRIeUZsSXJmbDdwUlpQNzhyWlNXYkxxQVU1SGoycUhGMzd6VEZJQ0dfT0xEeFREN1pQLTJTa1EzREtYTXA0MGV3WDEzeXdiWnhNUml4c3F6cnZpNWJfM3lTdFBmMDVINl81MGxSV0d2b3pxbkVsa3hJX3dNZ1Y0clBn?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxOVkZfVUVDRUsydTZvNndiZy1LSU9iMmxyUEV2ZjlBZlQtMTdTcnhNQnptQmc5X1BFM2VubUc3T1V4d3Y2SzZfcm1PQWVaLXFsVGFSX2RUUUtGRC1ZMGdpTVBsNVZfRFVpRl9fR0hkTEFUSktHQ2hSQzlmNVFBUkwyaVc1LTJHV1VBUWNJUnVXcWItM0kyT3RJbVViVnR5VFU?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxQeElvQXI0RHF2Vkd4cDBoMEVpc3VJcHBKY3NLMVNRbXBMUFNReTlTbF9Zb08wZUVTNFNCUjJfRS1BeE11MGp5YjV3a21qOGZlbkRlTUxvcktRNVNSWElFREN6NTZsVjltVnRKWEVKZ3JVVE9ETkQzMmZfS1V6WUF2bjNITkdObzI2c0pkbU1BU1pqMEpNZkV3?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
