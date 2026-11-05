# MSFT Intelligence Report

- ticker: **MSFT**
- Report as_of: **2026-11-04**
- Market data as_of: **2026-11-04**
- Quant sources: https://finance.yahoo.com/quote/MSFT/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/MSFT/key-statistics/
- AI analysis snapshot as_of: **2026-11-04**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-05T05:14:28.959067+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 5, 'ai': 12, 'unknown': 0, 'irrelevant': 8})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **3** exact headline/source/date matches; prior report **20261104T044411Z-6b13f9ec/MSFT** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 12 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 36.0%; oldest publication 2026-10-28

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 555.8000 |
| Return 1D (%) | 6.6815 |
| Return 1W (%) | 4.6685 |
| Return 1M (%) | 7.3947 |
| Return YTD (%) | 15.6540 |
| Return 1Y (%) | 8.9520 |
| Annualized volatility (%) | 33.6851 |
| Beta vs SPY | 1.0608 |
| Max drawdown (%) | -30.9656 |
| Sharpe (rf=0) | 0.4207 |
| Downside deviation (rf=0, %) | 21.3345 |
| Sortino (rf=0) | 0.6642 |
| Historical VaR 95% (1D, %) | 2.7847 |
| Historical ES 95% (1D, %) | 4.0430 |
| Correlation vs SPY | 0.4043 |
| Tracking error vs SPY (%) | 30.8187 |
| P/E (trailing) | 27.19 |
| P/B | 8.77 |
| EV/EBITDA | 20.40 |
| Revenue growth (%) | 18.80 |
| Forward P/E (estimate) | 22.99 |
| Gross margin (%) | 67.66 |
| Operating margin (%) | 49.76 |
| Return on equity (%) | 34.22 |
| Free cash flow yield (%) | 0.07 |
| MA50 | 515.3436 |
| Close vs MA50 (%) | 7.8504 |
| MA200 | 437.9615 |
| Close vs MA200 (%) | 26.9061 |
| RSI (14, Wilder) | 64.3312 |
| MACD (12,26) | 4.5268 |
| MACD signal (9) | 5.2242 |
| MACD histogram | -0.6974 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'MSFT': 275, 'SPY': 275}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 555.8000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 6.6815 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 4.6685 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 7.3947 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 15.6540 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 8.9520 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 33.6851 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 21.3345 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.6642 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.7847 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.0430 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4043 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 30.8187 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.0608 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -30.9656 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.4207 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 22.9866 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 67.6570 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 49.7570 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 34.2210 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 0.0725 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 27.1918 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 64.3312 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.6974 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 7.8504 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 26.9061 -> Clearly above the moving-average trend level.

## TAILWINDS

### Microsoft stock jumps 4% as cloud growth drives earnings and revenue beat
- Summary: Microsoft stock jumps 4% as cloud growth drives earnings and revenue beat
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMigAFBVV95cUxNclpVVGdGd3NYYWo4bGNFRTVlYjhQc0VhMzhmZnRsRnlTNkRidVNwaGlQVVdPMktwMHRMYzhUTWpYUXFYaVFfZFRkSkRmbDNGOWxVa29MSWhhUDk4RE9BVElXUTY3SWo2SHRNbGVhRU9vbjd3ZHJnZlpTdHpSbHpDNNIBhgFBVV95cUxNRXA0VC1WZEYxMWVmenJmdVRiRzhDRFVzUVNVNlJXaEJDc011NjZuT2VHdTJLYndYaGV1NDM2UU93Zm12X1J2VWtYMEJNQ3ZkU0Nhb3M0c0dQT3pzVFl3eTlqLWluNHJjRHpVRTJicTdqSXNTSHBVQjdKWlJtYjZjN2tQZkc3dw?oc=5>

### Microsoft Corp. (MSFT) Surges 37.8% on Record Quarterly Gains
- Summary: MSFT stock jumps 37.8% after reporting record quarterly earnings, boosting investor sentiment.
- Date: 2026-11-02 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxOQXo2dG9qMTRmU003ZF92OVVZQlpfU2JuS25fczJhUHpGWVFQNm1sQjYwSV9wd0IwNTBzZkZzdjVwNktPRkxNRGtlR3FGUFIya0hEenBBUHhHcy1JeFNWdUhmQjZFRExqcHZndzZzSDl0NXRBNUNwSUFhTi1DRTN5RTU1b0EtMS1YWjQ0NDM2bTd1dzlJVFV6VG5n?oc=5>

### Alphabet, Amazon, and Microsoft All Surged Today. You Can Thank the Big Blue Wave.
- Summary: Microsoft shares surged alongside Alphabet and Amazon, reflecting a strong market rally.
- Date: 2026-11-04 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxQS3FPNjF0Qnk2dkx5Z1hfblotbmJudmtpaWF5Zk1vR2xmMHBQLUVMbUVNTC1nQUJfRDVacldTUDllT3lpOHRVSnJCSTB0eEZlV1AycktIdFFNMmF4UVJxa0Z6VExPcFBXUFhKZzNBeUZCMHd4UGhQcjZscVl5blJodFZqSDE4WU82Q3FXTmo2YTdWM0tta01ZREFSbmxBUzdDVVpqaXNLXzM1YmlUaWlLV2RNQXRaVW1GVkJtWjlB?oc=5>

### Microsoft Corp Stock (MSFT) Opened Up by 5.61% on Nov 4: What Signal Does It Send?
- Summary: MSFT opened 5.61% higher on Nov 4, indicating bullish investor sentiment.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxPZHZHSEpuclhTdFJqcEJTN2h6enV5Ry1CU2U5NTIwWXotZVllTVR0aW1oY1U1WWNOS05GUXpuNTJ5UEdCYlR3Z20wbXp5MHRPdGIwY0pWeUdNZWZLNFEyd3JFT0tsN0xlMjQ1MmJXQlRSdzBtbERwZHFvY0loU3d1d2hlYUJqRDZOM0Y0?oc=5>

### Microsoft climbs 7% to hit a new 52-week high (MSFT:NASDAQ)
- Summary: MSFT rose 7%, reaching a new 52‑week high, signaling strong performance.
- Date: 2026-11-04 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMihwFBVV95cUxPVVlnY2ZOa2RoVWFscDZPblVuWTNWeFp3VkUySTNHNEpiU0lMaHFxMnZtaEZtYXlWQzVodG5sNXV0ZC1JNUtHQ0xDaUlNQVI3RHJRaEMtOGozT0dVUkNPVWtYc1hUdlRfczVxcWptWkNJa1RtZnpwV0JWRTZfWWtJTDlYX2E4VHM?oc=5>

### ETFs Bought $561.6 Million of Microsoft (MSFT) on Monday
- Summary: Large ETF purchases signal institutional confidence in MSFT shares.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxONWRFWERQczFobzFSekhaN0lBX3JRSk1SN3Q1VWg0azN4M3BTTmZFNVFhaG5LRUVWZGN3YV9kN1h5Y3ROTUJncTRMbUxXbHhtNlJfNl9YNlZvNUU3THdSeTZERmZpeG15YmdqU240TGx5TnFlaExjazFiaDE1RkZGZThNcTk4anYwZTBkZWhsZnhLMG9r?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Microsoft (MSFT) Stock Gets Fair Value Bump On Azure And AI Optimism
- Summary: Microsoft (MSFT) Stock Gets Fair Value Bump On Azure And AI Optimism
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihgFBVV95cUxNMVNHUmdfVEtaUVd0cG00UmVMSlFtSXJ6cTVVdEpPR0NYcmtvSzFLVEtEd28yREhYeTh0QXN3NGlJc0tlN0NwdUFBZEwzTE9vbnRVV2tpVmwza01XLVhwQU5uTzEtWGZPSVpNbTlTT01LS2tmRUQ1YllVNFQxcVB1bnhlMXUwQQ?oc=5>

### Microsoft Corporation (MSFT) Delivered Strong Fiscal Fourth-Quarter Results: Mott Capital’s Take
- Summary: Microsoft Corporation (MSFT) Delivered Strong Fiscal Fourth-Quarter Results: Mott Capital’s Take
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxNQk9QazJNaHFhVHFmSzhPcUFMbHJzQk05dXV3ZXNwZ0xEM3JoazhBbktLS0I1RVpIckc1VnhQOEt4VzNOU3I3N1N2YVU2cW50S0RheWhNU3ZUNjJja0RXbkVuU2N1VThHM0tNX0hWemd3LXpGNjluODk2NzFnVV9jclAwNnhtTWxKeFhYcVRBcm11cWhVaUVWZWJnbXJVclAzQ1UtLU9KZzV4MUd5?oc=5>

### Microsoft Delivered a Beat on Both Earnings and Revenue. Here’s How to Think About MSFT Stock Now.
- Summary: Microsoft Delivered a Beat on Both Earnings and Revenue. Here’s How to Think About MSFT Stock Now.
- Date: 2026-11-01 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxQMklLMEw0WDU1anlpRDg1aHFyekJ6Q1VaRFpQb256emNMSTFGUjFZOUMwcEQwMWMwUkN3U1BiaHJ6R3RGSzZhWERGVmpVNDdrXzhlYnVUdUZsaFl6TXF3NWdXczFpUGRXQ2hTNGNUQVRORzR5VlhkVENqak9qSGFmdzh4MWhqY3I0UkROOEZmdnVmRTF3aXRVOXJPTmZnaFNVa3JVOF9B?oc=5>

### Microsoft (MSFT) Stock Shrugs Off Q1 Earnings As AI Spending Looms
- Summary: Microsoft (MSFT) Stock Shrugs Off Q1 Earnings As AI Spending Looms
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNcVl0VWhEWUhhTi1wb2pFS2EwdEhvem12dWtCNENMNGRhNjVCbkJ4OHJsLWgtaVRSa2xXcFFoQ1I0RzNLRVdUTmhjYVVkZDJQTmM3SUdZUk5jcWFxZjZfcnJrQnF4Qm5ickpyOU01QmJqMUNsQ2l4UjNmWU9BcDN3Nzk1NUVsTklzTmtUQnM4dTlFLVZEQzRpVkgtUWo?oc=5>

### Why is Microsoft stock surging today?
- Summary: Microsoft shares jump as investors anticipate AI-driven growth.
- Date: 2026-11-04 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxPUFVCTXBvOHp5SDY5R1AwUGlfcEtSeVR5MVZsRG1GckxNRjJZelBKcDFRWjJORDMyRE1GTjAtZTh4WEQtbDFSWVItSXhPc0F4U1lPRDRqNl9KeWV6QlRXTGdDNm40UFg3VGlLal9fZVlzRWluSlJaeC02LTZWWlRkVWVWLTJrSHlhX1dDcEhkMjJtaHI4N1h4OG5rZUdubGc?oc=5>

### Forget the 12-Month Squeeze: Microsoft Is Primed for an Explosive AI Payoff
- Summary: Analysts highlight AI potential to boost Microsoft’s future earnings.
- Date: 2026-11-04 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxOdkpnZnA5b1dlU3FEaXp5Y2NZOFVFc2h2YmduaWJpcXd1SDIzSV9mOGQzTldKMG93YkpEU2NnejRvc2MzU3BnbGdXZC05TEVuRExQdm5RVGh1T3FqR1BGQ1hvUUMzM1R2TjNIQndxUURkUWpiOEJvRmZOT3Jrb2FvWkZyX3EySE56Q3VDQkJGTzF4TUttY2VVT0VhZTdibTgzN3FISHRNdFl2Q2NYY3JTNVE1NWV3SzRKTnc?oc=5>

### What's Going on With Microsoft Stock on Wednesday?
- Summary: Microsoft stock rises amid AI optimism and positive market sentiment.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxQRVhBNThEMG02b1Fmc2xKZnktTDJUbGU5SkdxNFlDR0RLUjFPY1dudnZaZnRKZzdSUllHNTNnMUQwSk0zSXFmNnRBZkVhXzdfQU1tMEFsSXo3RmZZWVVySUpEV0ZKZlk1LVZrcjFoeURsWUVRd0pGQUdiNV9vWlhYYk81QWVUY0VrdEJFcGFyYU1SUldPVTJHeDYzN0VuaEl1WS1R?oc=5>

### Microsoft Stock (NASDAQ:MSFT) Surges as AI Development May Pay Off
- Summary: Shares climb as AI developments promise future revenue growth.
- Date: 2026-11-04 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxNbUZ5VDBrWW9GUUhQTDV4eGVCTFN0ZURkVVpkcDNETWNPdl8wUnRUSW1rTXNkMkhvZ0FidlE5blUzMWxVcFg3QUF0OE9yeXlnd2h4RTlvd0dSRE9LMGRuTmM4ZVNaaVY1cjJQMTVvQnlSNE5aLTZFdmRBbkZ1OTFvcHpFUUJHSXVCbTRHZ0tZZnprQS10S2xWaw?oc=5>

### Microsoft Corporation (MSFT) Outperforms with Record Quarter Driven by Azure Demand Surge
- Summary: Microsoft reports record earnings, driven by strong Azure demand.
- Date: 2026-11-04 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxORm1BVWgtcHBpSHoyRGM1T1BpODlZQWRuTkk0TFBmRU9RMGg1UkVBcTVoTGstSVhjY1ZfaDUyM0lmSTlocU50QWNxOGx6S1VwY1RyN25RSzhWaHZoMHlodGxCTmJhQjJmaVVQSThSUnJad2dCTG5VMTRZYUZmUExqTzlOTU51MGM3N0twb2V3NDBqR3JYeHg5TkpxSmZDa2tpUGlxR2U3UVFYNGFEbnlV?oc=5>

### Microsoft Stocks Rise With $44.9 Billion Anthropic Commitment Disclosed
- Summary: Microsoft announces a $44.9B partnership with Anthropic, boosting its AI capabilities and market confidence.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxObXFfaGEzdUp6NjFkRHpzVU16VVhlNFVsZ1hQTVh6cUdQTmJCUUxZaXZKdF9EeVhpTTE5WmkzWEt3MGVDQ2p6bDZzQU1SR3VHX0pKeDB4WGdYc1VxN2g5a0VWUzI4Q3p0NHRRQzQ5SFdMMm9BQ1BZdWxrbk02QTFSbFdSOGhaZm5qSlh5Y0JwX2FoSm1DeUE?oc=5>

## RISKS

### Microsoft: Don’t Get Too Excited About Its Positive FCF (Rating Downgrade) (NASDAQ:MSFT)
- Summary: Credit rating downgrade signals potential financial risk, dampening investor enthusiasm despite strong free cash flow.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxOdWMybGRXZjEtTGRDVldwU0RFUmo5OWxLbWtpRHA3dDFBLURXd1gxMGFfRnJMSmxlOEI5QWFzR2dZMDFxb0FyTUFCekY4aWVTNDhUNWRsenNUOEExYnJQNEdIX1pXZ0MyYlFEa3dMa0tqNWJfcHlEYll3dVpMcDh1LUoxbEtzMm5nT0JoNy1oUkJtc2RlSTdsZVBnNUhrcXhXSUtXNFhXa2h0QmFqanQ2TA?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **MSFT** | **27.19** | **8.77** | **20.40** | **18.80** | **4,127,478,775,808.00 USD** | **8.95** |
| ORCL | 19.39 | 6.05 | 14.86 | 29.60 | 375,087,628,288.00 USD | -49.48 |
| GOOGL | 14.62 | 5.39 | 18.63 | 24.70 | 3,552,105,201,664.00 USD | 4.37 |
| AMZN | 20.26 | 4.69 | 16.70 | 12.10 | 2,876,619,096,064.00 USD | 6.70 |

Peers fetched as_of: 2026-11-04; MSFT reuses existing data (market data as_of: 2026-11-04); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-28
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-04

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-28
- Revenue (latest available single quarter): 19,953,000,000.00 USD; period 2010-10-01/2010-12-31; fiscal year/reporting period 2011/Q2
- Net income (latest available single quarter): 36,629,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2027/Q1
- SEC link: https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/msft-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMigAFBVV95cUxNclpVVGdGd3NYYWo4bGNFRTVlYjhQc0VhMzhmZnRsRnlTNkRidVNwaGlQVVdPMktwMHRMYzhUTWpYUXFYaVFfZFRkSkRmbDNGOWxVa29MSWhhUDk4RE9BVElXUTY3SWo2SHRNbGVhRU9vbjd3ZHJnZlpTdHpSbHpDNNIBhgFBVV95cUxNRXA0VC1WZEYxMWVmenJmdVRiRzhDRFVzUVNVNlJXaEJDc011NjZuT2VHdTJLYndYaGV1NDM2UU93Zm12X1J2VWtYMEJNQ3ZkU0Nhb3M0c0dQT3pzVFl3eTlqLWluNHJjRHpVRTJicTdqSXNTSHBVQjdKWlJtYjZjN2tQZkc3dw?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxOQXo2dG9qMTRmU003ZF92OVVZQlpfU2JuS25fczJhUHpGWVFQNm1sQjYwSV9wd0IwNTBzZkZzdjVwNktPRkxNRGtlR3FGUFIya0hEenBBUHhHcy1JeFNWdUhmQjZFRExqcHZndzZzSDl0NXRBNUNwSUFhTi1DRTN5RTU1b0EtMS1YWjQ0NDM2bTd1dzlJVFV6VG5n?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxQS3FPNjF0Qnk2dkx5Z1hfblotbmJudmtpaWF5Zk1vR2xmMHBQLUVMbUVNTC1nQUJfRDVacldTUDllT3lpOHRVSnJCSTB0eEZlV1AycktIdFFNMmF4UVJxa0Z6VExPcFBXUFhKZzNBeUZCMHd4UGhQcjZscVl5blJodFZqSDE4WU82Q3FXTmo2YTdWM0tta01ZREFSbmxBUzdDVVpqaXNLXzM1YmlUaWlLV2RNQXRaVW1GVkJtWjlB?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxPZHZHSEpuclhTdFJqcEJTN2h6enV5Ry1CU2U5NTIwWXotZVllTVR0aW1oY1U1WWNOS05GUXpuNTJ5UEdCYlR3Z20wbXp5MHRPdGIwY0pWeUdNZWZLNFEyd3JFT0tsN0xlMjQ1MmJXQlRSdzBtbERwZHFvY0loU3d1d2hlYUJqRDZOM0Y0?oc=5
- https://news.google.com/rss/articles/CBMihwFBVV95cUxPVVlnY2ZOa2RoVWFscDZPblVuWTNWeFp3VkUySTNHNEpiU0lMaHFxMnZtaEZtYXlWQzVodG5sNXV0ZC1JNUtHQ0xDaUlNQVI3RHJRaEMtOGozT0dVUkNPVWtYc1hUdlRfczVxcWptWkNJa1RtZnpwV0JWRTZfWWtJTDlYX2E4VHM?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxONWRFWERQczFobzFSekhaN0lBX3JRSk1SN3Q1VWg0azN4M3BTTmZFNVFhaG5LRUVWZGN3YV9kN1h5Y3ROTUJncTRMbUxXbHhtNlJfNl9YNlZvNUU3THdSeTZERmZpeG15YmdqU240TGx5TnFlaExjazFiaDE1RkZGZThNcTk4anYwZTBkZWhsZnhLMG9r?oc=5
- https://news.google.com/rss/articles/CBMihgFBVV95cUxNMVNHUmdfVEtaUVd0cG00UmVMSlFtSXJ6cTVVdEpPR0NYcmtvSzFLVEtEd28yREhYeTh0QXN3NGlJc0tlN0NwdUFBZEwzTE9vbnRVV2tpVmwza01XLVhwQU5uTzEtWGZPSVpNbTlTT01LS2tmRUQ1YllVNFQxcVB1bnhlMXUwQQ?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxNQk9QazJNaHFhVHFmSzhPcUFMbHJzQk05dXV3ZXNwZ0xEM3JoazhBbktLS0I1RVpIckc1VnhQOEt4VzNOU3I3N1N2YVU2cW50S0RheWhNU3ZUNjJja0RXbkVuU2N1VThHM0tNX0hWemd3LXpGNjluODk2NzFnVV9jclAwNnhtTWxKeFhYcVRBcm11cWhVaUVWZWJnbXJVclAzQ1UtLU9KZzV4MUd5?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxQMklLMEw0WDU1anlpRDg1aHFyekJ6Q1VaRFpQb256emNMSTFGUjFZOUMwcEQwMWMwUkN3U1BiaHJ6R3RGSzZhWERGVmpVNDdrXzhlYnVUdUZsaFl6TXF3NWdXczFpUGRXQ2hTNGNUQVRORzR5VlhkVENqak9qSGFmdzh4MWhqY3I0UkROOEZmdnVmRTF3aXRVOXJPTmZnaFNVa3JVOF9B?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNcVl0VWhEWUhhTi1wb2pFS2EwdEhvem12dWtCNENMNGRhNjVCbkJ4OHJsLWgtaVRSa2xXcFFoQ1I0RzNLRVdUTmhjYVVkZDJQTmM3SUdZUk5jcWFxZjZfcnJrQnF4Qm5ickpyOU01QmJqMUNsQ2l4UjNmWU9BcDN3Nzk1NUVsTklzTmtUQnM4dTlFLVZEQzRpVkgtUWo?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxPUFVCTXBvOHp5SDY5R1AwUGlfcEtSeVR5MVZsRG1GckxNRjJZelBKcDFRWjJORDMyRE1GTjAtZTh4WEQtbDFSWVItSXhPc0F4U1lPRDRqNl9KeWV6QlRXTGdDNm40UFg3VGlLal9fZVlzRWluSlJaeC02LTZWWlRkVWVWLTJrSHlhX1dDcEhkMjJtaHI4N1h4OG5rZUdubGc?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxOdkpnZnA5b1dlU3FEaXp5Y2NZOFVFc2h2YmduaWJpcXd1SDIzSV9mOGQzTldKMG93YkpEU2NnejRvc2MzU3BnbGdXZC05TEVuRExQdm5RVGh1T3FqR1BGQ1hvUUMzM1R2TjNIQndxUURkUWpiOEJvRmZOT3Jrb2FvWkZyX3EySE56Q3VDQkJGTzF4TUttY2VVT0VhZTdibTgzN3FISHRNdFl2Q2NYY3JTNVE1NWV3SzRKTnc?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxQRVhBNThEMG02b1Fmc2xKZnktTDJUbGU5SkdxNFlDR0RLUjFPY1dudnZaZnRKZzdSUllHNTNnMUQwSk0zSXFmNnRBZkVhXzdfQU1tMEFsSXo3RmZZWVVySUpEV0ZKZlk1LVZrcjFoeURsWUVRd0pGQUdiNV9vWlhYYk81QWVUY0VrdEJFcGFyYU1SUldPVTJHeDYzN0VuaEl1WS1R?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxNbUZ5VDBrWW9GUUhQTDV4eGVCTFN0ZURkVVpkcDNETWNPdl8wUnRUSW1rTXNkMkhvZ0FidlE5blUzMWxVcFg3QUF0OE9yeXlnd2h4RTlvd0dSRE9LMGRuTmM4ZVNaaVY1cjJQMTVvQnlSNE5aLTZFdmRBbkZ1OTFvcHpFUUJHSXVCbTRHZ0tZZnprQS10S2xWaw?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxORm1BVWgtcHBpSHoyRGM1T1BpODlZQWRuTkk0TFBmRU9RMGg1UkVBcTVoTGstSVhjY1ZfaDUyM0lmSTlocU50QWNxOGx6S1VwY1RyN25RSzhWaHZoMHlodGxCTmJhQjJmaVVQSThSUnJad2dCTG5VMTRZYUZmUExqTzlOTU51MGM3N0twb2V3NDBqR3JYeHg5TkpxSmZDa2tpUGlxR2U3UVFYNGFEbnlV?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxObXFfaGEzdUp6NjFkRHpzVU16VVhlNFVsZ1hQTVh6cUdQTmJCUUxZaXZKdF9EeVhpTTE5WmkzWEt3MGVDQ2p6bDZzQU1SR3VHX0pKeDB4WGdYc1VxN2g5a0VWUzI4Q3p0NHRRQzQ5SFdMMm9BQ1BZdWxrbk02QTFSbFdSOGhaZm5qSlh5Y0JwX2FoSm1DeUE?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxOdWMybGRXZjEtTGRDVldwU0RFUmo5OWxLbWtpRHA3dDFBLURXd1gxMGFfRnJMSmxlOEI5QWFzR2dZMDFxb0FyTUFCekY4aWVTNDhUNWRsenNUOEExYnJQNEdIX1pXZ0MyYlFEa3dMa0tqNWJfcHlEYll3dVpMcDh1LUoxbEtzMm5nT0JoNy1oUkJtc2RlSTdsZVBnNUhrcXhXSUtXNFhXa2h0QmFqanQ2TA?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
