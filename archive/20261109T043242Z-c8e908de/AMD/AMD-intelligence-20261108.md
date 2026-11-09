# AMD Intelligence Report

- ticker: **AMD**
- Report as_of: **2026-11-08**
- Market data as_of: **2026-11-06**
- Quant sources: https://finance.yahoo.com/quote/AMD/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AMD/key-statistics/
- AI analysis snapshot as_of: **2026-11-08**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-09T04:43:14.107877+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 22, 'rule': 5, 'ai': 15, 'unknown': 0, 'irrelevant': 2})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **11** exact headline/source/date matches; prior report **20261108T041758Z-43fb2458/AMD** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 22 unique headlines; 9 named publishers; 3 exact duplicates; 22 HTTPS source links; largest publisher share 45.45%; oldest publication 2026-11-03

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 449.0400 |
| Return 1D (%) | 11.0386 |
| Return 1W (%) | -11.0460 |
| Return 1M (%) | -30.8552 |
| Return YTD (%) | 109.6750 |
| Return 1Y (%) | 88.9104 |
| Annualized volatility (%) | 72.0180 |
| Beta vs SPY | 3.3469 |
| Max drawdown (%) | -37.7290 |
| Sharpe (rf=0) | 1.2467 |
| Downside deviation (rf=0, %) | 47.2356 |
| Sortino (rf=0) | 1.9008 |
| Historical VaR 95% (1D, %) | 6.3184 |
| Historical ES 95% (1D, %) | 9.4746 |
| Correlation vs SPY | 0.6297 |
| Tracking error vs SPY (%) | 64.3521 |
| P/E (trailing) | 95.95 |
| P/B | 10.77 |
| EV/EBITDA | N/A |
| Revenue growth (%) | 44.70 |
| Forward P/E (estimate) | 25.45 |
| Gross margin (%) | 56.00 |
| Operating margin (%) | 21.17 |
| Return on equity (%) | 11.96 |
| Free cash flow yield (%) | 1.00 |
| MA50 | 546.8138 |
| Close vs MA50 (%) | -17.8806 |
| MA200 | 415.9775 |
| Close vs MA200 (%) | 7.9481 |
| RSI (14, Wilder) | 38.4071 |
| MACD (12,26) | -30.2042 |
| MACD signal (9) | -17.4482 |
| MACD histogram | -12.7559 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AMD': 277, 'SPY': 277}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 449.0400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 11.0386 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -11.0460 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -30.8552 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 109.6750 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 88.9104 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 72.0180 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 47.2356 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.9008 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 6.3184 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 9.4746 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6297 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 64.3521 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 3.3469 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -37.7290 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.2467 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 25.4530 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 56.0000 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 21.1710 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 11.9600 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 0.9990 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 95.9487 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 38.4071 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -12.7559 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -17.8806 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 7.9481 -> Clearly above the moving-average trend level.

## TAILWINDS

### AMD Stock Jumped After Its Report. I'd Wait for a Lower Price to Buy.
- Summary: AMD Stock Jumped After Its Report. I'd Wait for a Lower Price to Buy.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxNYm9xVXl2cl9helVoRzZkMHJvWExySWZEZ3l1Y05BNEhXbWtfbWdqOTRxUUhRODNSN3lDeTBoYUFzSWpzekZ5MDlCQkFwUEJUQ2t0eThXSUQ5eE9ZTXZOM3Rneks0REp5aFVPWTQ4QzVjOUkwWGRNQ0ZpSy1yWnkzRFkxdUN4UldlRndPeTloZzVSaVUzX0E?oc=5>

### Micron, AMD, SanDisk Lead AI Stock Bounce as Investors Buy the Dip - Advanced Micro Devices (NASDAQ:AMD)
- Summary: AI stock bounce led by AMD, Micron, SanDisk boosts investor confidence.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxPd29rd1lEZDQzdlR0ZWM1UmxsWF81NjQtZzBCMnBKNzVrSElvTE1LRS1SakFoWkVYUGRlbV9UaExocHY0VUhNQ19yNU1XNG5aSHZ2dlI2ZWUtc3UxRmM4SFh4al9GVC15eENFcGxCT1hVNVJSaWRONGlsNUwzU3JxODBPM0QxM1NscWhvRDd1YWZUVHNtVXg3czNvZDEtUXdfSXF0SThfMDEwQm5NLWNqYzNkVlRjSWNv?oc=5>

### Is AMD Stock a Buy as AI Revenue Soars?
- Summary: AI revenue growth suggests AMD stock may be attractive to investors.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiAFBVV95cUxQU0tXYkl3NVdKa3c0NUJISXAwem9VV2syZ0NQTE1qcW5ZQlRfMWhlOUdxeHNOQUJ2NXo4RGxNWk9BbVVvRDhENmhZMFhXelRRd2RhQnlNWVJHQ2pTbWdMemQtRVNmRzRQMWFBNXBRX3hVWjI0Zk5PX29jY09KbDd0ZGlNaDZSRHU3?oc=5>

### AMD Earnings: Strong Data Center Outlook Points to Upside for Stock
- Summary: Strong data center outlook in earnings signals potential upside for AMD stock.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxPdUdGaXRMT19sZ0xxbk1fVnV6Qlg2MUNPRndSWmJwU2o2ZThDczhEd2gzZi1XSHpMOWt1NEU5eENBTWJLM0dweTNDUERJR01HdVB4WWx3WUNiSnNkQ05UYkxXVWwtSjhMejF0WEowdXN4U3I3cDJsSl9yUkZDcThBTWJUNFlaZ2RSRUNlajZZMjlvVDVWOHFLMW10UXdId3QwckdxQ2p3?oc=5>

### 53 ETFs Add to Advanced Micro Devices (AMD) on Nov. 4
- Summary: ETF additions signal institutional confidence and potential liquidity boost.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxOLTJJcVJGQUh6QzJQOEF0WnNKb09adzIwUDAyQWR5emxKZjNaMmZmTFhkTmJiOUFiQnMtc3hucWpRQksxX3FCQzdtSm1ablVJUzhRYjkwd0VvdVRRR2h2VUdVd0JJVTA5dGdUWmM4WHRqTER0WHl2aFRQcWxRM05hRk1oSUNmZDVmd1hBaGZfbU44ODBNdWc?oc=5>

### AMD Soars 10%, Intel Up 7% as Chip Stocks Rebound From Election Sell-Off
- Summary: AMD shares jump 10% amid broader chip market rebound after election sell‑off.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxNYzJoZ0hiNmpxcHp2dUhpVjZ4UURiSjNtaEgydnhGTURfVXBib1VGZWZfa2JaQzh4blRMNDlOMnBvNFBLSkltWjV4YW1JQkJZaFZicWMxUldmYUd3THlaQTlIajBaRndrY3dMUDdUb2l0dnlsWldWVE96eXkxUVluMlpBT01ZUnI3YnNuVERR?oc=5>

### Advanced Micro Devices, Inc. (AMD) stock price, news, quote and history
- Summary: Provides current stock price and historical data for AMD.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 1
- Sources: <https://news.google.com/rss/articles/CBMiUEFVX3lxTE5zQU82NDA0LUZ3MzFqYV9TTVRvSV9ZTU12TEhvVGhGVXhiQkdpVXlON1FVQVF3NVh6NTk3U1g4X1piOEtudEEwdjg5d3N0elRJ?oc=5>

### AMD Stock Has More Than Doubled in 2026. Here's How Its Last 8 Doubles Played Out the Next Year.
- Summary: Highlights AMD’s significant stock price growth and future projections.
- Date: 2026-11-08 | Impact: high | Horizon: medium | Confidence: 1
- Sources: <https://news.google.com/rss/articles/CBMi0wFBVV95cUxONV9zRHFyM0hBc1h4X0RyX0lwZjQtNXZYVzFaYWp2ZnZMaU0tX3BCcWxqXzd5QUY2WHBVUUxEcDNqZXZBN0Q5U1YtUmtQMUk2QWE3bWhNZ3lCNWxlR04zbEdrSUYzanJzcmhRYlZDUDBFRXpfc2pSTE8xb2FOZm9zd3JkbEZBZWRZbzdfSDFsajhab2ZfVGEzd09Xd1pCa0hhY3FZYm5yemlmc2VwOTB2NXhmbVpoV0FQa2M0bkMyOGlFbzhmUnpXbHVjeVN6RWs5WE9R?oc=5>

### AMD or Nvidia: Which AI Chip Stock Would I Buy With $1,000 Today?
- Summary: Compares AMD and Nvidia AI chip stocks for potential investment.
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 1
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxNQnJXLUp4NVBqUXBZa0Vic3AyS01MYkwyekVpUVhKdV92Q1EzT2U2UjBaUVViWEczV2syYzZqZUpHTkNzRHUza0ROSS1LQm8tVjg1b0c0QjZXUEx0RnMtczl6QkQ0SXpCYUZNQlZvMVVDQ1Z6UnZzMnpvNVhuMm1YblJuN3lqbDg4ODZDdDZOWWFMSDE1WEczXw?oc=5>

### ETFs Are Buying Advanced Micro Devices (AMD) on Tuesday
- Summary: Reports increased ETF purchases of AMD shares.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 1
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxPZnVGWGp3ZGxiWFZwVmUtcVVydTJEbnVmQi1ScFdNMUQzWDluaUYtZnJQeHE3dlhHTGVzckhpZkhISjlEa1hFNm9JSldzcVNQM096QW5uakRNR3hFTkkwVG1VSkRoMVhkd3hhS0lrcUJiT3EzY25FZEVOQVFDYjRlSVIxR3FlalEybEwxX1lpNjc4a2d5Y0JMTFJRZ2tnRUR3?oc=5>

### Trending Industry Today: Advanced Micro Devices Leads Gains In CPU Concept Stocks
- Summary: Shows AMD leading gains among CPU concept stocks today.
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 1
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxQRUF6N1JKemk0VWJIcHM4SERsX0pmdS1KSllaVmVObFI5UlF6bmxRS05YRXJvNDI5Y3VseS1tZHNGWDhOT3FfV0ZJNHUyU2pPbU9zODhqczlqWWVWSHYwWEMxN0N2a2d4MTNvLWhuVWQ5T29kdm1xcnAtbVFsTUplZmgwTjB5QXdzdVd0X3lwSkd5QXJRQzFmeDRGSndBSUZ6eXp6NjZQNUtQa1R6dmc?oc=5>

## HEADWINDS

### AMD Stock Just Fell Below the Price I Said I'd Pay for It.
- Summary: AMD Stock Just Fell Below the Price I Said I'd Pay for It.
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxNNUZsRWVuUHliYXA1VjB0QVlPUWI3RjEtMU1Nc2YzVmNHV3FWVjk5bjl3aUdDN2VvWnRraHp0dUNJcFJ1SU1JVjNPNHIweDN3RHhtRmNWRVhhOS1BVmthaWpma0ZxUWdBbGJrblhCaTBadG1PQjNSSE1zc1AxZm9jSlFJaS1xdERjaUQ1VnVtam5wV1FlT3NBY3pyall5NXlpTHc?oc=5>

### Advanced Micro Devices (AMD) Recently Crashed Out of the $1 Trillion Club. Should You Buy the Dip?
- Summary: AMD's market cap fell below $1 trillion, indicating a negative market move.
- Date: 2026-11-07 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxQd2ZQUTRyZWQxTTFwMURZSkZITGU3Wkk5ZGliLUZFLWRjR1ZmbUN4OUZVWVZZcl9kd2hpekJzVXk1aEtxVTkzZ3BzWXVHUGljU1BhUEhGTHNVdzZKTDhCWno3Qkp1OFF1SWt5dVVQMjBVcjNoNFZmdFRNNVUtYzlEUnJ6OHY0WWFVZXpXUXdtdGVBdGN0Z3Atc3VhcUEzbU1icnc?oc=5>

## CATALYSTS

### Advanced Micro Devices, Inc. $AMD Stock: OPTIMAS CAPITAL Ltd Reduces Position
- Summary: Advanced Micro Devices, Inc. $AMD Stock: OPTIMAS CAPITAL Ltd Reduces Position
- Date: 2026-11-07 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizwFBVV95cUxQLTMtZEpHUHFVNnlNbGhtZmlOeEhVTF84dkNEZXJHczVKSTQ3WnBoU3VLTVQ3V0FjUy1FNnhyd2RjRFJsazQ4NEx6eXREUHBYeEh4b0o3RzRuRXczMWV1MG5fSkxWSEVOUzBFczhpdHQ3bkdsdDRYYVZuMDZEX0V1aEI4bUlLWUtZcFNqZE9WNWJabnJVVWhOaG9rSVF0WlZJTjRJcEpYLWpQOTY4elY2c3RRTERzdUttb24teDBicDdVdHI1dnJNcngwSkdUMzg?oc=5>

### AMD's data center revenue nearly doubles in Q3 and CEO Su expects growth to accelerate
- Summary: AMD's data center revenue nearly doubles in Q3 and CEO Su expects growth to accelerate
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMieEFVX3lxTFBfVXVMaFFzOXpSSmhDS2xlZWZLZDk0V2w5MHpTSnZ3d2c5bkMzRDhwbzhURWpMMVcwX3ZiME8ybmU4UHR1ekdtVlUwRTYxcTI0T1dadVhheUQ0LVVpWnRqYjdmeDkxMGJKQXBkNUtpaEVKZVlXNEhYRQ?oc=5>

### Advanced Micro Devices (AMD) Stock Fair Value Edges Higher On AI Optimism And Valuation Debate
- Summary: Advanced Micro Devices (AMD) Stock Fair Value Edges Higher On AI Optimism And Valuation Debate
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxOX1l0LWJQM0UweGdsZExDZWdodmZTNTBreS03LVp0UDE5aG0zM3QwSTA3Tk9zWTFoYjlVbzZMZGZsQV9pckhBLXZ0UUg5R3dtQlFTd2w2UlF3clZDMGw2blhaZUFXbzFuUmM0cmpCTC12UTZXYnJ4ZmxIdlR2eHFHSkZoNXhSS1hEVC1Ec0pMQ2Q1TVp2VXE5c1dhWDVRQQ?oc=5>

### What Just Happened To AMD Stock?
- Summary: Exploring recent price movements of AMD shares.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxPUTRETjN2U3Q4TzFMLVlDX0hNTlBTZDhQN3FnX0xYUnJCSmlkNW1BVmpjdGF6aEdHM191YVhMWm1SS3BlbWd0bVZwVmVBRU1JSjFaeWd4OFdkSDVNTjhwVmRuY3F6TTFaVnN6c1pZdm5fV2dTa0prQWVBbk5uVnN3RzRqeXdvVmU4a1ppQ09zcldMWllSOEE?oc=5>

### Is Advanced Micro Devices (AMD) Fully Priced After Record AI Growth?
- Summary: Questioning whether AMD’s valuation reflects its AI-driven growth.
- Date: 2026-11-05 | Impact: low | Horizon: medium | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxNN1ZjcDRNUjdDUkxUMDRadUlJckxJZ0RNVW9ZWnZRNHNhQm5qZU9qdEFJQ1dKZmJFMk1GMy14TGpmZWRHcEJETnFwZVJHcE1lWG5lV21Za2s4aVc2Nm9ZSjdiN1lLZFFaR2xHWGtBQUF4Vkt1X2Y2VV9qWXp5MWx3dm15MEJXazZPQXNHRm9DVXNlU3h6S0dxQlBER29qUQ?oc=5>

### AMD Tumbles 13%, NVIDIA Slides 7% as AI Regulation Fears Hit Chip Stocks; Intel Sinks 8%
- Summary: AMD shares fell 13% amid AI regulation fears affecting the chip sector.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxPdzNfN2w5ZVNDUjNHZUxyd0tWZG42ajdJbzg0NkU0NHN3UDN5NG5jWVZrUHhqd1JHMVhVMkpXQ2NDYjcxcDREQ0liOWJ4TEFySkpOV3lJSnJQZGtmeUJRX2dBMExXYU0zNFpnMGdhdllkVHlkcmgwTlFILXdfeTMtcjl4YThqSURBdExta09XQXhYb0x5Uldj?oc=5>

## RISKS

### Can AMD Stock Fall 50%?
- Summary: Questioning potential downside, but no concrete event reported.
- Date: 2026-11-06 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiiAFBVV95cUxQQl9xUGNqZ1pXalUyZXRUTWxhR3RkTktfa3dQdFVBSHpXN2FESFhpYkFNMklRdnRFblBkZFJYb0xkbFdSM2EzRnRMT25aVFozempPNHlkLVVzX3F3d2dfSDI3dlBFWlh0T3hTSHM4WWgxWnNRQ2JXSHZLN3l1amItczlrVnhxSlB6?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AMD** | **95.95** | **10.77** | **N/A** | **44.70** | **736,464,797,696.00 USD** | **88.91** |
| NVDA | 23.60 | 19.68 | 22.23 | 105.90 | 4,506,795,900,928.00 USD | -0.53 |
| INTC | N/A | 2.60 | 16.30 | 20.90 | 299,128,193,024.00 USD | 51.13 |
| AVGO | 37.51 | 14.06 | 27.50 | 85.50 | 1,401,967,345,664.00 USD | -16.79 |

Peers fetched as_of: 2026-11-08; AMD reuses existing data (market data as_of: 2026-11-06); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-03
- Next expected earnings: 2027-02-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-08

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
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

- https://news.google.com/rss/articles/CBMilgFBVV95cUxNYm9xVXl2cl9helVoRzZkMHJvWExySWZEZ3l1Y05BNEhXbWtfbWdqOTRxUUhRODNSN3lDeTBoYUFzSWpzekZ5MDlCQkFwUEJUQ2t0eThXSUQ5eE9ZTXZOM3Rneks0REp5aFVPWTQ4QzVjOUkwWGRNQ0ZpSy1yWnkzRFkxdUN4UldlRndPeTloZzVSaVUzX0E?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxPd29rd1lEZDQzdlR0ZWM1UmxsWF81NjQtZzBCMnBKNzVrSElvTE1LRS1SakFoWkVYUGRlbV9UaExocHY0VUhNQ19yNU1XNG5aSHZ2dlI2ZWUtc3UxRmM4SFh4al9GVC15eENFcGxCT1hVNVJSaWRONGlsNUwzU3JxODBPM0QxM1NscWhvRDd1YWZUVHNtVXg3czNvZDEtUXdfSXF0SThfMDEwQm5NLWNqYzNkVlRjSWNv?oc=5
- https://news.google.com/rss/articles/CBMiiAFBVV95cUxQU0tXYkl3NVdKa3c0NUJISXAwem9VV2syZ0NQTE1qcW5ZQlRfMWhlOUdxeHNOQUJ2NXo4RGxNWk9BbVVvRDhENmhZMFhXelRRd2RhQnlNWVJHQ2pTbWdMemQtRVNmRzRQMWFBNXBRX3hVWjI0Zk5PX29jY09KbDd0ZGlNaDZSRHU3?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxPdUdGaXRMT19sZ0xxbk1fVnV6Qlg2MUNPRndSWmJwU2o2ZThDczhEd2gzZi1XSHpMOWt1NEU5eENBTWJLM0dweTNDUERJR01HdVB4WWx3WUNiSnNkQ05UYkxXVWwtSjhMejF0WEowdXN4U3I3cDJsSl9yUkZDcThBTWJUNFlaZ2RSRUNlajZZMjlvVDVWOHFLMW10UXdId3QwckdxQ2p3?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxPUnR5SDRTd2RXY0kyRS1aN1hiZjRFLUZOZDVrRmhsS3ZmWjVWRjFjRHF6NFVRWXhKaWJnZlRyUlNmbGZLQl83U2YyY1lUa2lrWnRsZFRWOUdOQnYyQVJ0eHRVc181c3ZpLWlyeEg1cWpTZHVDRmM5MVQ3UkJrLUhRWXA1eDdLdlFBblJ3MnRET0pHX1k5cVpLeHkwcnRJWDEyVG5mclB3?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxOLTJJcVJGQUh6QzJQOEF0WnNKb09adzIwUDAyQWR5emxKZjNaMmZmTFhkTmJiOUFiQnMtc3hucWpRQksxX3FCQzdtSm1ablVJUzhRYjkwd0VvdVRRR2h2VUdVd0JJVTA5dGdUWmM4WHRqTER0WHl2aFRQcWxRM05hRk1oSUNmZDVmd1hBaGZfbU44ODBNdWc?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxNYzJoZ0hiNmpxcHp2dUhpVjZ4UURiSjNtaEgydnhGTURfVXBib1VGZWZfa2JaQzh4blRMNDlOMnBvNFBLSkltWjV4YW1JQkJZaFZicWMxUldmYUd3THlaQTlIajBaRndrY3dMUDdUb2l0dnlsWldWVE96eXkxUVluMlpBT01ZUnI3YnNuVERR?oc=5
- https://news.google.com/rss/articles/CBMiUEFVX3lxTE5zQU82NDA0LUZ3MzFqYV9TTVRvSV9ZTU12TEhvVGhGVXhiQkdpVXlON1FVQVF3NVh6NTk3U1g4X1piOEtudEEwdjg5d3N0elRJ?oc=5
- https://news.google.com/rss/articles/CBMi0wFBVV95cUxONV9zRHFyM0hBc1h4X0RyX0lwZjQtNXZYVzFaYWp2ZnZMaU0tX3BCcWxqXzd5QUY2WHBVUUxEcDNqZXZBN0Q5U1YtUmtQMUk2QWE3bWhNZ3lCNWxlR04zbEdrSUYzanJzcmhRYlZDUDBFRXpfc2pSTE8xb2FOZm9zd3JkbEZBZWRZbzdfSDFsajhab2ZfVGEzd09Xd1pCa0hhY3FZYm5yemlmc2VwOTB2NXhmbVpoV0FQa2M0bkMyOGlFbzhmUnpXbHVjeVN6RWs5WE9R?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxPV0lYbldENGNqNTBOMFZidU1lQV9mX2ppVVlpR1lBdGpvRmN0bUhYZF9ZdGFqMnVaZXR2UUkxbENGYUhuaHFzWFVlNHFhVXZYUlMwRGVHLTZraGJpejR4SHFjS0RrVFc4WVh0b09faElNQzI2OGVTRTZMZy1UQ3hzQS1CR1JWM2ZqclJFdy1TYV9Gazc4eURF?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxNQnJXLUp4NVBqUXBZa0Vic3AyS01MYkwyekVpUVhKdV92Q1EzT2U2UjBaUVViWEczV2syYzZqZUpHTkNzRHUza0ROSS1LQm8tVjg1b0c0QjZXUEx0RnMtczl6QkQ0SXpCYUZNQlZvMVVDQ1Z6UnZzMnpvNVhuMm1YblJuN3lqbDg4ODZDdDZOWWFMSDE1WEczXw?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxPZnVGWGp3ZGxiWFZwVmUtcVVydTJEbnVmQi1ScFdNMUQzWDluaUYtZnJQeHE3dlhHTGVzckhpZkhISjlEa1hFNm9JSldzcVNQM096QW5uakRNR3hFTkkwVG1VSkRoMVhkd3hhS0lrcUJiT3EzY25FZEVOQVFDYjRlSVIxR3FlalEybEwxX1lpNjc4a2d5Y0JMTFJRZ2tnRUR3?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxQRUF6N1JKemk0VWJIcHM4SERsX0pmdS1KSllaVmVObFI5UlF6bmxRS05YRXJvNDI5Y3VseS1tZHNGWDhOT3FfV0ZJNHUyU2pPbU9zODhqczlqWWVWSHYwWEMxN0N2a2d4MTNvLWhuVWQ5T29kdm1xcnAtbVFsTUplZmgwTjB5QXdzdVd0X3lwSkd5QXJRQzFmeDRGSndBSUZ6eXp6NjZQNUtQa1R6dmc?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxNNUZsRWVuUHliYXA1VjB0QVlPUWI3RjEtMU1Nc2YzVmNHV3FWVjk5bjl3aUdDN2VvWnRraHp0dUNJcFJ1SU1JVjNPNHIweDN3RHhtRmNWRVhhOS1BVmthaWpma0ZxUWdBbGJrblhCaTBadG1PQjNSSE1zc1AxZm9jSlFJaS1xdERjaUQ1VnVtam5wV1FlT3NBY3pyall5NXlpTHc?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxQd2ZQUTRyZWQxTTFwMURZSkZITGU3Wkk5ZGliLUZFLWRjR1ZmbUN4OUZVWVZZcl9kd2hpekJzVXk1aEtxVTkzZ3BzWXVHUGljU1BhUEhGTHNVdzZKTDhCWno3Qkp1OFF1SWt5dVVQMjBVcjNoNFZmdFRNNVUtYzlEUnJ6OHY0WWFVZXpXUXdtdGVBdGN0Z3Atc3VhcUEzbU1icnc?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxOeEpRMjVrSzZYZENMSFgxdHVucTIxajJzb0xQVXptZGVjRUh3eEMxUEU4MDVpUFJEMnBSYnU5UFhOYXI2SHFjdHQ0NW9QdDczV2MtVlczVzZCbEE0RDN5R0l3NnhkbE40bkJUR3FZSXpZMmVTQ0VPRHNFR3lWcW9mQ2FxTlJpQl9pZ01YTGV2RzlXNVdoVHFV?oc=5
- https://news.google.com/rss/articles/CBMizwFBVV95cUxQLTMtZEpHUHFVNnlNbGhtZmlOeEhVTF84dkNEZXJHczVKSTQ3WnBoU3VLTVQ3V0FjUy1FNnhyd2RjRFJsazQ4NEx6eXREUHBYeEh4b0o3RzRuRXczMWV1MG5fSkxWSEVOUzBFczhpdHQ3bkdsdDRYYVZuMDZEX0V1aEI4bUlLWUtZcFNqZE9WNWJabnJVVWhOaG9rSVF0WlZJTjRJcEpYLWpQOTY4elY2c3RRTERzdUttb24teDBicDdVdHI1dnJNcngwSkdUMzg?oc=5
- https://news.google.com/rss/articles/CBMieEFVX3lxTFBfVXVMaFFzOXpSSmhDS2xlZWZLZDk0V2w5MHpTSnZ3d2c5bkMzRDhwbzhURWpMMVcwX3ZiME8ybmU4UHR1ekdtVlUwRTYxcTI0T1dadVhheUQ0LVVpWnRqYjdmeDkxMGJKQXBkNUtpaEVKZVlXNEhYRQ?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxOX1l0LWJQM0UweGdsZExDZWdodmZTNTBreS03LVp0UDE5aG0zM3QwSTA3Tk9zWTFoYjlVbzZMZGZsQV9pckhBLXZ0UUg5R3dtQlFTd2w2UlF3clZDMGw2blhaZUFXbzFuUmM0cmpCTC12UTZXYnJ4ZmxIdlR2eHFHSkZoNXhSS1hEVC1Ec0pMQ2Q1TVp2VXE5c1dhWDVRQQ?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxPUTRETjN2U3Q4TzFMLVlDX0hNTlBTZDhQN3FnX0xYUnJCSmlkNW1BVmpjdGF6aEdHM191YVhMWm1SS3BlbWd0bVZwVmVBRU1JSjFaeWd4OFdkSDVNTjhwVmRuY3F6TTFaVnN6c1pZdm5fV2dTa0prQWVBbk5uVnN3RzRqeXdvVmU4a1ppQ09zcldMWllSOEE?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxNN1ZjcDRNUjdDUkxUMDRadUlJckxJZ0RNVW9ZWnZRNHNhQm5qZU9qdEFJQ1dKZmJFMk1GMy14TGpmZWRHcEJETnFwZVJHcE1lWG5lV21Za2s4aVc2Nm9ZSjdiN1lLZFFaR2xHWGtBQUF4Vkt1X2Y2VV9qWXp5MWx3dm15MEJXazZPQXNHRm9DVXNlU3h6S0dxQlBER29qUQ?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxPdzNfN2w5ZVNDUjNHZUxyd0tWZG42ajdJbzg0NkU0NHN3UDN5NG5jWVZrUHhqd1JHMVhVMkpXQ2NDYjcxcDREQ0liOWJ4TEFySkpOV3lJSnJQZGtmeUJRX2dBMExXYU0zNFpnMGdhdllkVHlkcmgwTlFILXdfeTMtcjl4YThqSURBdExta09XQXhYb0x5Uldj?oc=5
- https://news.google.com/rss/articles/CBMiiAFBVV95cUxQQl9xUGNqZ1pXalUyZXRUTWxhR3RkTktfa3dQdFVBSHpXN2FESFhpYkFNMklRdnRFblBkZFJYb0xkbFdSM2EzRnRMT25aVFozempPNHlkLVVzX3F3d2dfSDI3dlBFWlh0T3hTSHM4WWgxWnNRQ2JXSHZLN3l1amItczlrVnhxSlB6?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
