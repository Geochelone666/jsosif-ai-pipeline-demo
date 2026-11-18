# DIS Intelligence Report

- ticker: **DIS**
- Report as_of: **2026-11-17**
- Market data as_of: **2026-11-17**
- Quant sources: https://finance.yahoo.com/quote/DIS/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/DIS/key-statistics/
- AI analysis snapshot as_of: **2026-11-17**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-18T05:49:55.563393+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 2, 'ai': 18, 'unknown': 0, 'irrelevant': 4})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **1** exact headline/source/date matches; prior report **20261116T043911Z-b81cfeb4/DIS** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 11 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 25.0%; oldest publication 2026-11-12

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 116.9400 |
| Return 1D (%) | -1.4827 |
| Return 1W (%) | -1.9042 |
| Return 1M (%) | 5.7419 |
| Return YTD (%) | 3.5739 |
| Return 1Y (%) | 12.2465 |
| Annualized volatility (%) | 26.1040 |
| Beta vs SPY | 0.5394 |
| Max drawdown (%) | -20.2451 |
| Sharpe (rf=0) | 0.5744 |
| Downside deviation (rf=0, %) | 17.6349 |
| Sortino (rf=0) | 0.8502 |
| Historical VaR 95% (1D, %) | 2.3418 |
| Historical ES 95% (1D, %) | 3.3566 |
| Correlation vs SPY | 0.2848 |
| Tracking error vs SPY (%) | 25.8157 |
| P/E (trailing) | 20.77 |
| P/B | 1.84 |
| EV/EBITDA | 11.91 |
| Revenue growth (%) | 6.80 |
| Forward P/E (estimate) | 13.85 |
| Gross margin (%) | 37.59 |
| Operating margin (%) | 15.61 |
| Return on equity (%) | 8.01 |
| Free cash flow yield (%) | 2.41 |
| MA50 | 109.7058 |
| Close vs MA50 (%) | 6.5942 |
| MA200 | 103.4556 |
| Close vs MA200 (%) | 13.0340 |
| RSI (14, Wilder) | 59.0254 |
| MACD (12,26) | 2.7095 |
| MACD signal (9) | 2.6914 |
| MACD histogram | 0.0181 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'DIS': 284, 'SPY': 284}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 116.9400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.4827 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -1.9042 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 5.7419 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 3.5739 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 12.2465 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 26.1040 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 17.6349 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.8502 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.3418 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.3566 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2848 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 25.8157 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.5394 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -20.2451 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.5744 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 13.8509 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 37.5950 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 15.6120 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 8.0100 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.4071 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 20.7709 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 59.0254 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.0181 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 6.5942 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 13.0340 -> Clearly above the moving-average trend level.

## TAILWINDS

### Walt Disney (DIS) Beats Q4 Earnings and Revenue Estimates
- Summary: Walt Disney (DIS) Beats Q4 Earnings and Revenue Estimates
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMifkFVX3lxTE5WS3ZoVnVQaEdNYUU4b2E3U2ZoeGEwTElHOHhfVmFScF84QWJncmNWMVp2aldlYy1YUlJPNDZyRlVQNUFycTRnbTliOEhiNDIyOG9sYzdqR2JTVVV1eDIxLXFqVDFLODRDN1poUDc1UlpCZVZ6MkxjdVhoSXZBZw?oc=5>

### Walt Disney’s Financial Results Beat Estimates
- Summary: Walt Disney’s Financial Results Beat Estimates
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxOXzVydUVpX3VBa2YxVTk2YWd4Z0NNaGY0NWp5M3cydGNmVXc5VUhEeTNEbUtrMlN0dG1OT2U1OVptM0FaYkEwaDhLTDRIVzR1dTRHNkdPZ0thWER6NC1jeXlEdjJ1RldjUHNBb3hHem9KZTVPakRHSm1VWFROQVBWYl9ybjJPWldlMnVVSHROdGFKNlpuTnRPVWp4NnFSeEs4aXRBb3lfdFg0Zw?oc=5>

### Disney (DIS) Stock Rally After Earnings Beat as Investors Weigh 2027 Outlook
- Summary: Stock rally following earnings beat as investors assess 2027 outlook.
- Date: 2026-11-17 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxPcXEwR1pHRlBraFkzSndfb1dyak92U1lnNFNpSElCeVFSLTBPYkZvaEVWNVdZWm5mWHBmWmlzTnhlaXRwTWpiQ0JNdUhmSjRxWEI4elYzVktRSndiT2hRZG5oWGI1Tk14cHl3TGptck5kQTV2U05CNVVET2YxaHQtX3FlazkzWjBldjlDeU5JcC1XOWtfVnBfMzJhT1ZGUTQ2aDVYYnh4NVMtOUtFZEJsY0sxNDlXQdIBuwFBVV95cUxQTmhBZUU1R2lFSmNCNGlVMDJVRy11NzJwNk1peEVHYmZCSlZaR084VFBaSXhKRkFwb3NaaGZGTWdyQjk2RE1SY2tpUnlZSUp0cmRKRDY0aTlQRWFKOUZ0U1dLdHhHTm1DUHRVcEtHeUpwdkJ3bGhpV3dlMGFXTmpkanlRMEdCa0hXSjhLZk5xc0cwUjBfTGVtTUtMNHNBOUlHNDhlY0RUcnlVamlvVktuV0hDT083ZDlhYldB?oc=5>

### Disney's Parks, Cruises and Merchandise Earn More Than Movies, TV and Streaming
- Summary: Disney reports higher earnings from parks, cruises, and merchandise compared to movies, TV, and streaming, indicating strong non-media revenue streams.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxPRnNSM2Q0dmZkQXBDQ0t1NXN0MENrc3NnWmhWdHhDT2tKUE1Pd1lZVERIUktVODVQOEM3LThnamRTWW03UERnLUlXT2pqLVlCSzNfclRzUFA4blRKT0JOVGJMXzRfRzk5SUlBNmpmTGozMV9seE5YQnJqWDM3UzlkWVAzbmRBNWZWbmpUUmZKcw?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Walt Disney (DIS) Just Gave Investors Something To Think About
- Summary: Disney announced information prompting investor analysis.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxPVnMzZGtoM3FtTzA0UEl6MFRka3d6Qzl6UDZ3SGJGNWw1Nzh0NjBiQTBTdTlZSk1pZ3A4WTNSYzc2NW1vX0xIRVhMcHJhcDZ0ZkstNnpZWWNfYnlmczl4bk85UHRlOTgzczRDY1Qtc1Q0WmlxSDdBY08yd3hJOFpCU3VKSWJ5RkpjVEFmOWlzYzJINWJF?oc=5>

### Disney (DIS) Stock Price Forecasts – What Analysts Expect Ahead of Tomorrow’s Q4 Earnings
- Summary: Analysts discuss expectations for Disney’s upcoming Q4 earnings, potentially influencing investor sentiment and stock price.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxNd0ZuemQzSHRlczZuSGFPRkdIRk9ndDFTSkwyTU1fcWFtc05uOHRZV1Z2TTVTV2VOZE5PelJXTUdkT2FSYzllYzdCaFdjdXdCOEhSMkctMXZzek15dE8wQnJLUWYwNXVVNU5kNUxrc0UzeEVzVms0S0tBcTJPVXVwc2hNRHJ4WW9ob2pkZFpSVkM4Y3paUm9DUDJvSUt2VndQU2c1NHJJOWZtRU03aG41amRYR2w?oc=5>

### The Walt Disney Company (DIS) Stock Price, News, Quote & History
- Summary: Provides current stock price and historical data for Disney, offering context for market performance.
- Date: 2026-11-17 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiUEFVX3lxTE9pN2JFcy1FNGRvcDVUU1hzRENVb042SXN4c0ljeFBQUXFNVHdZWUdsZHB1d01wTnA5bmF4c1YzMElXb1JPaEdZVkxzTlhtcDBl?oc=5>

### The Walt Disney Company Q4 2026 Earnings Call Summary
- Summary: Summarizes Disney’s Q4 2026 earnings call, highlighting key financial metrics and management commentary.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxQQWRXWEl0Nk5obGhZeU1nTkNmaXR0aTFsMk9LN29ZMHg1ajRxNmZpTUFUM1paemxlY3o5c3dmSF9KNXlZTVZ4YUo5ZHdXbktyVzZsX0hPdk52cXVZWUI3ejBKa3FiN0FSSnB1OXhQTkxPb3JtcVhWNnB5RlY1LWVrOWxURWZsc0Eyai1Seks1Ykt4cXIwQ0xz?oc=5>

### Disney Stock Hits New Highs After Strong Q4 Earnings: Time to Buy DIS?
- Summary: Disney’s stock reached new highs following robust Q4 earnings, prompting buy‑side analysis.
- Date: 2026-11-17 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNMy1vczBlNUd2RGtCVlBzVl9qYUs4Ty1ubk1WTFVVRjBHUFRfTDJKZU9LWVdVS3BPU3phTEV6cVhKTlpJQWtPdE9mV180VXRiSlRhVEd4YlUtVURScF9sOFFmSllsaTlBTGQ0aG0yNHY3c1lFb2tqVkxEQ1M3c2pmZGdxWUtPZ3RwcEd4UzhValc2ODlYZUNJbHd1MA?oc=5>

### Disney (DIS) Reports Q4 Earnings: What Key Metrics Have to Say
- Summary: Details Disney’s Q4 earnings results and key performance indicators, informing investor decisions.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxQa1Rvc2FwcklkT2VTcGs0U0xvVGMxOGI1OUIwb21wWmxVX3BqNWVzVDdnYjFMaTJIUTJEWWF1YWpRYWJvSVJfV04zNlVFNW1GdE1IbDdMajVWbXdGUlVDNGNJX1Q4cXdrNW4zTjN5OWg3Zk1BcS1CY25pbDJRZXROWGh3dFl5QTJwRFNkUDlXNFBseElvM1ZjTkJKUQ?oc=5>

### Earnings Beat Might Change The Bull Case For Disney Stock (DIS)
- Summary: Disney's earnings beat could alter bullish outlook.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihwFBVV95cUxOVXJlTVp4ZkxpWXdlSXNoTjZIdWZMbVEtVFFwT3VTdnVham41Ylh4Qk1oTVFrWGRXV3BZbzdneVpud3RqQURhX0FSRkJkZWI5LXY1U1M5SVY3ZkdGdVRjMTRiU25JYlhjQkd3cURHckt6QkNDU0hxWk8weW9YMkR5Nl9wYkk2aU0?oc=5>

### Disney Just Raised Its Dividend 33%, Giving Shareholders a Bigger Payday
- Summary: Disney increased its dividend by 33%, boosting shareholder payouts.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxPaEtxRVYxd3FpdWpqeE1nbFd2by1wdnJoVlhHVE91RWl4UXVQblVuWGRUUmNCVDRyOVdLOTVYU2hUZWk3aENjc3hMQVFmUWhrNnlvaV9nbE80RUJZdmxnTzNHNnFtMXNiV3VnbkgxanMxTldIekRGWGRfbExoSmxIQmRxYnJZWlZOOVRRWkVUSktMdWVZLTBCTEY2TzVrNEt2dkMtT1hqSHRPc1ZYT0FKc2hPTF8?oc=5>

### Disney: One Franchise, Several Ways To Make Money (NYSE:DIS)
- Summary: Disney highlights multiple revenue streams from a single franchise.
- Date: 2026-11-17 | Impact: medium | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxNdE9hMWU2LUE3aFFJUEtqSjVTWkpnM2VoeVpzY3hZQ2FCcGY1Q3B1TUQ2VUdKNVFUQWNsV0FfbExscmhVTVg1dEVudnFqMHFjMTBqM0hPSU83YW91eVMtay1uTkhUMFVXX2ZIWHoxNmJnekJlZVJNVS1XcjFHeUhZdmQxQkpJaURHdkNYMDA3MGtKQQ?oc=5>

### Disney quarterly earnings exceed forecasts as streaming profitability improves (DIS:NYSE)
- Summary: Disney's quarterly earnings beat forecasts, driven by streaming gains.
- Date: 2026-11-17 | Impact: high | Horizon: short | Confidence: 0.97
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxQdFZnYU1KZVJvd0dMR002enhzVDhxYmR2V2E3SDNVRzdJMUV0Z1RWelhXSFVvXzhseEpMcl9hMmU1SWRnZTd3MmJCYm1KWGV6QkNfcVJIbFFoT0dHLXNTcmR5anZXbUtSOTNsQk1UcUZCOVI3Q0hMMTcxT1BFLTdjZW9BWUZ3NjRra2RyLUdOYlpxcENSVVgxb3BldFd3UHBhOFFHX1JhSzVDMEYzeHFPVUVNSEV4WU0?oc=5>

### Analysts weigh Disney's streaming progress against parks, content risks (DIS:NYSE)
- Summary: Analysts assess Disney's streaming growth versus park and content risks.
- Date: 2026-11-17 | Impact: medium | Horizon: medium | Confidence: 0.88
- Sources: <https://news.google.com/rss/articles/CBMiywFBVV95cUxNOFBCOE5qZWhwSHRDQ183TjF5NkZRaXBZeWN0VFZINzBFUlpzUTJzRXM5Sno4ZjJPUV9hVlM0Mnk3alBqOXlnLW9PRndwdTgtM1l6LVZRVjgtenR1YTdaM3JEc3lBdzQ3Q1FYOEl2Zi1IMVp2YmdLUkNKWVRMLV80dElHOGNQWWNFbER2bEtvVHcyNUVzSFhJQ1VTcU5RbW9jcmJ5dlFZVlB6UktReTBHSzJySEcxR2RjZUhMa09ETGxHeHcybkhGYmNMQQ?oc=5>

### Disney (NYSE:DIS) Earnings Beat: Revenue Jumps 16% as $3 Billion Cost-Cutting Plan Unveiled
- Summary: Disney beats earnings expectations, revenue up 16%, announces $3B cost‑cutting plan.
- Date: 2026-11-17 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMifEFVX3lxTE1HRTl5a0NOSWx2dVRGeGdmWjJ0LUVETzdZVjhMRVRFS3A5aG9pMkRfSm4wZ1ZwN2w0aUs0cjZtWnZuY3FyRTJjdVBhdHVvU1A4RUdab0ViODdsS25ZclZkYnNaWWtBaTQ0dVpod3FsdWhnZ3Nyak5wSVNZczM?oc=5>

### Disney faces earnings test as investors weigh cost cuts, streaming and parks growth (DIS:NYSE)
- Summary: Investors scrutinize Disney’s upcoming earnings amid cost cuts, streaming, parks growth.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxQUENzS2NSc1lYdG04dC0tM1g4QjNmUlVzTG9zTGhfd2FfemdqWXFnN244eV9LWHIwRERmamNzSGJpRHRaMnE2bFdmX3MwdklLNGpXTVY5WnZyc19GWTM2T3JhRk5xSHl4RVlBZXFCcVVod1d6UWVCbTI5MWlERTJUV2lvb0tKYkJyei0zUElScS1CVEo5Y0RhYlUwTHVFck5DTjZwZXdEaGZQckEwekI5LWJRMHZvWnZ6SHVMcQ?oc=5>

### Disney will pay shareholders in two $1 installments, with the first due in January.
- Summary: Disney to pay shareholders in two $1 installments starting January.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxORFljcVNvNVE3SkJkdTdLWklwdm51Rld5V1R1VVVwT2Rsa05YNmIzNGx3U1pTLUpkalRaaDkxWHBmZkhuVnczQTZIZTNkbGdBTTdKaFM3QzV3b2FaeVZnblRTY2V2V3R6d2lhNGNlZ0U1N2w3OHpuMm9jazg4T0Q3OHVLa0xmMzV0bDAtSmRVeTlFQnZWOWliRnc4OTZNOE93UHVzaUpNa0tEbFRnSU9TVzVn?oc=5>

### Disney will discuss its results in an 8:30 a.m. ET webcast, then make the replay available online.
- Summary: Disney to discuss results in webcast, replay online.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxPNm1nVTZETWVaWkpFWk5iblBqRFZpcDFnc2pja28tMW5sTkNDS2NpbExNRFZvNXR2cnJBUmZETXMyVWtOY2kwamNCREpHbnRDRHZFU0o4VjZQbjR3MnU3cnMxeUVKM2tuVUdqSXRKMmtsOEJwZW1MWDJoQlhMV1VxUWVrTTlDcHo4ZUhzOHJwYzl6SklfajE2ZHI5MWMzTC1IZk94dFhzc09aVG9uRVFXTjR2eHlxdw?oc=5>

### Disney Bets On Streaming And Content To Drive FY27 Growth — Raises Dividend, Targets $9B Buyback
- Summary: Disney raises dividend and plans a $9B buyback to boost FY27 growth via streaming and content.
- Date: 2026-11-17 | Impact: high | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxQQkt5anZTOFhFdm1tamxybjltWmF4Wk1GQkJtMlAxcWRhWE0yTkNtbjFLVlM3ZVNGdUkwMVhueFZTT0hXWU81Y3BneVM2TkFiUUlDNWRQUkJYSnk0eS1XYkI3RlJqMmdPVUY4VGRpNGc2TU5sTkY4dGJTb29XbXVKalM0OXcyRUVwenFtZUFPUjRvTmRrVjY0cDZ4akg5X181ejEwTGV3?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **DIS** | **20.77** | **1.84** | **11.91** | **6.80** | **201,918,758,912.00 USD** | **12.25** |
| NFLX | 17.55 | 8.37 | 15.94 | 11.80 | 245,065,531,392.00 USD | -45.89 |
| WBD | N/A | 2.36 | 13.79 | -11.20 | 77,595,885,568.00 USD | N/A |
| PSKY | N/A | 0.93 | 7.95 | 0.90 | 10,992,190,464.00 USD | N/A |

Peers fetched as_of: 2026-11-17; DIS reuses existing data (market data as_of: 2026-11-17); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-17
- Next expected earnings: N/A (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-17

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-K
- Filing date: 2026-11-17
- Revenue (latest available single quarter): 25,248,000,000.00 USD; period 2026-03-29/2026-06-27; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 2,638,000,000.00 USD; period 2026-03-29/2026-06-27; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1744489/000174448926000066/dis-20261003.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMifkFVX3lxTE5WS3ZoVnVQaEdNYUU4b2E3U2ZoeGEwTElHOHhfVmFScF84QWJncmNWMVp2aldlYy1YUlJPNDZyRlVQNUFycTRnbTliOEhiNDIyOG9sYzdqR2JTVVV1eDIxLXFqVDFLODRDN1poUDc1UlpCZVZ6MkxjdVhoSXZBZw?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxOXzVydUVpX3VBa2YxVTk2YWd4Z0NNaGY0NWp5M3cydGNmVXc5VUhEeTNEbUtrMlN0dG1OT2U1OVptM0FaYkEwaDhLTDRIVzR1dTRHNkdPZ0thWER6NC1jeXlEdjJ1RldjUHNBb3hHem9KZTVPakRHSm1VWFROQVBWYl9ybjJPWldlMnVVSHROdGFKNlpuTnRPVWp4NnFSeEs4aXRBb3lfdFg0Zw?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxPcXEwR1pHRlBraFkzSndfb1dyak92U1lnNFNpSElCeVFSLTBPYkZvaEVWNVdZWm5mWHBmWmlzTnhlaXRwTWpiQ0JNdUhmSjRxWEI4elYzVktRSndiT2hRZG5oWGI1Tk14cHl3TGptck5kQTV2U05CNVVET2YxaHQtX3FlazkzWjBldjlDeU5JcC1XOWtfVnBfMzJhT1ZGUTQ2aDVYYnh4NVMtOUtFZEJsY0sxNDlXQdIBuwFBVV95cUxQTmhBZUU1R2lFSmNCNGlVMDJVRy11NzJwNk1peEVHYmZCSlZaR084VFBaSXhKRkFwb3NaaGZGTWdyQjk2RE1SY2tpUnlZSUp0cmRKRDY0aTlQRWFKOUZ0U1dLdHhHTm1DUHRVcEtHeUpwdkJ3bGhpV3dlMGFXTmpkanlRMEdCa0hXSjhLZk5xc0cwUjBfTGVtTUtMNHNBOUlHNDhlY0RUcnlVamlvVktuV0hDT083ZDlhYldB?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxPRnNSM2Q0dmZkQXBDQ0t1NXN0MENrc3NnWmhWdHhDT2tKUE1Pd1lZVERIUktVODVQOEM3LThnamRTWW03UERnLUlXT2pqLVlCSzNfclRzUFA4blRKT0JOVGJMXzRfRzk5SUlBNmpmTGozMV9seE5YQnJqWDM3UzlkWVAzbmRBNWZWbmpUUmZKcw?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxPVnMzZGtoM3FtTzA0UEl6MFRka3d6Qzl6UDZ3SGJGNWw1Nzh0NjBiQTBTdTlZSk1pZ3A4WTNSYzc2NW1vX0xIRVhMcHJhcDZ0ZkstNnpZWWNfYnlmczl4bk85UHRlOTgzczRDY1Qtc1Q0WmlxSDdBY08yd3hJOFpCU3VKSWJ5RkpjVEFmOWlzYzJINWJF?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxNd0ZuemQzSHRlczZuSGFPRkdIRk9ndDFTSkwyTU1fcWFtc05uOHRZV1Z2TTVTV2VOZE5PelJXTUdkT2FSYzllYzdCaFdjdXdCOEhSMkctMXZzek15dE8wQnJLUWYwNXVVNU5kNUxrc0UzeEVzVms0S0tBcTJPVXVwc2hNRHJ4WW9ob2pkZFpSVkM4Y3paUm9DUDJvSUt2VndQU2c1NHJJOWZtRU03aG41amRYR2w?oc=5
- https://news.google.com/rss/articles/CBMiUEFVX3lxTE9pN2JFcy1FNGRvcDVUU1hzRENVb042SXN4c0ljeFBQUXFNVHdZWUdsZHB1d01wTnA5bmF4c1YzMElXb1JPaEdZVkxzTlhtcDBl?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxQQWRXWEl0Nk5obGhZeU1nTkNmaXR0aTFsMk9LN29ZMHg1ajRxNmZpTUFUM1paemxlY3o5c3dmSF9KNXlZTVZ4YUo5ZHdXbktyVzZsX0hPdk52cXVZWUI3ejBKa3FiN0FSSnB1OXhQTkxPb3JtcVhWNnB5RlY1LWVrOWxURWZsc0Eyai1Seks1Ykt4cXIwQ0xz?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNMy1vczBlNUd2RGtCVlBzVl9qYUs4Ty1ubk1WTFVVRjBHUFRfTDJKZU9LWVdVS3BPU3phTEV6cVhKTlpJQWtPdE9mV180VXRiSlRhVEd4YlUtVURScF9sOFFmSllsaTlBTGQ0aG0yNHY3c1lFb2tqVkxEQ1M3c2pmZGdxWUtPZ3RwcEd4UzhValc2ODlYZUNJbHd1MA?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxPZ3l2LUo4Uy1TVnYwa28zNEpVb0tCcnRoM1FlQ3VQMW5IQnNsLUhKVlhiUWxSbm1wVnNpV3hqMGY4SjdackliOWs5dXdfZ1c4Q1RNN3RtNVl1WTU4WFRvYkhaUmVQdzI5NElrb3M0S09oYm1TYm8zVEJmUmR0Mm44TnUxYllzVUNfNG5hUEVaSTlWRVNuSEZnRGthRUJDeTBIMGhPdmNCVVV5SVp0VVE?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxQa1Rvc2FwcklkT2VTcGs0U0xvVGMxOGI1OUIwb21wWmxVX3BqNWVzVDdnYjFMaTJIUTJEWWF1YWpRYWJvSVJfV04zNlVFNW1GdE1IbDdMajVWbXdGUlVDNGNJX1Q4cXdrNW4zTjN5OWg3Zk1BcS1CY25pbDJRZXROWGh3dFl5QTJwRFNkUDlXNFBseElvM1ZjTkJKUQ?oc=5
- https://news.google.com/rss/articles/CBMihwFBVV95cUxOVXJlTVp4ZkxpWXdlSXNoTjZIdWZMbVEtVFFwT3VTdnVham41Ylh4Qk1oTVFrWGRXV3BZbzdneVpud3RqQURhX0FSRkJkZWI5LXY1U1M5SVY3ZkdGdVRjMTRiU25JYlhjQkd3cURHckt6QkNDU0hxWk8weW9YMkR5Nl9wYkk2aU0?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxPaEtxRVYxd3FpdWpqeE1nbFd2by1wdnJoVlhHVE91RWl4UXVQblVuWGRUUmNCVDRyOVdLOTVYU2hUZWk3aENjc3hMQVFmUWhrNnlvaV9nbE80RUJZdmxnTzNHNnFtMXNiV3VnbkgxanMxTldIekRGWGRfbExoSmxIQmRxYnJZWlZOOVRRWkVUSktMdWVZLTBCTEY2TzVrNEt2dkMtT1hqSHRPc1ZYT0FKc2hPTF8?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxNdE9hMWU2LUE3aFFJUEtqSjVTWkpnM2VoeVpzY3hZQ2FCcGY1Q3B1TUQ2VUdKNVFUQWNsV0FfbExscmhVTVg1dEVudnFqMHFjMTBqM0hPSU83YW91eVMtay1uTkhUMFVXX2ZIWHoxNmJnekJlZVJNVS1XcjFHeUhZdmQxQkpJaURHdkNYMDA3MGtKQQ?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxQdFZnYU1KZVJvd0dMR002enhzVDhxYmR2V2E3SDNVRzdJMUV0Z1RWelhXSFVvXzhseEpMcl9hMmU1SWRnZTd3MmJCYm1KWGV6QkNfcVJIbFFoT0dHLXNTcmR5anZXbUtSOTNsQk1UcUZCOVI3Q0hMMTcxT1BFLTdjZW9BWUZ3NjRra2RyLUdOYlpxcENSVVgxb3BldFd3UHBhOFFHX1JhSzVDMEYzeHFPVUVNSEV4WU0?oc=5
- https://news.google.com/rss/articles/CBMiywFBVV95cUxNOFBCOE5qZWhwSHRDQ183TjF5NkZRaXBZeWN0VFZINzBFUlpzUTJzRXM5Sno4ZjJPUV9hVlM0Mnk3alBqOXlnLW9PRndwdTgtM1l6LVZRVjgtenR1YTdaM3JEc3lBdzQ3Q1FYOEl2Zi1IMVp2YmdLUkNKWVRMLV80dElHOGNQWWNFbER2bEtvVHcyNUVzSFhJQ1VTcU5RbW9jcmJ5dlFZVlB6UktReTBHSzJySEcxR2RjZUhMa09ETGxHeHcybkhGYmNMQQ?oc=5
- https://news.google.com/rss/articles/CBMifEFVX3lxTE1HRTl5a0NOSWx2dVRGeGdmWjJ0LUVETzdZVjhMRVRFS3A5aG9pMkRfSm4wZ1ZwN2w0aUs0cjZtWnZuY3FyRTJjdVBhdHVvU1A4RUdab0ViODdsS25ZclZkYnNaWWtBaTQ0dVpod3FsdWhnZ3Nyak5wSVNZczM?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxQUENzS2NSc1lYdG04dC0tM1g4QjNmUlVzTG9zTGhfd2FfemdqWXFnN244eV9LWHIwRERmamNzSGJpRHRaMnE2bFdmX3MwdklLNGpXTVY5WnZyc19GWTM2T3JhRk5xSHl4RVlBZXFCcVVod1d6UWVCbTI5MWlERTJUV2lvb0tKYkJyei0zUElScS1CVEo5Y0RhYlUwTHVFck5DTjZwZXdEaGZQckEwekI5LWJRMHZvWnZ6SHVMcQ?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxORFljcVNvNVE3SkJkdTdLWklwdm51Rld5V1R1VVVwT2Rsa05YNmIzNGx3U1pTLUpkalRaaDkxWHBmZkhuVnczQTZIZTNkbGdBTTdKaFM3QzV3b2FaeVZnblRTY2V2V3R6d2lhNGNlZ0U1N2w3OHpuMm9jazg4T0Q3OHVLa0xmMzV0bDAtSmRVeTlFQnZWOWliRnc4OTZNOE93UHVzaUpNa0tEbFRnSU9TVzVn?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxPNm1nVTZETWVaWkpFWk5iblBqRFZpcDFnc2pja28tMW5sTkNDS2NpbExNRFZvNXR2cnJBUmZETXMyVWtOY2kwamNCREpHbnRDRHZFU0o4VjZQbjR3MnU3cnMxeUVKM2tuVUdqSXRKMmtsOEJwZW1MWDJoQlhMV1VxUWVrTTlDcHo4ZUhzOHJwYzl6SklfajE2ZHI5MWMzTC1IZk94dFhzc09aVG9uRVFXTjR2eHlxdw?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxQQkt5anZTOFhFdm1tamxybjltWmF4Wk1GQkJtMlAxcWRhWE0yTkNtbjFLVlM3ZVNGdUkwMVhueFZTT0hXWU81Y3BneVM2TkFiUUlDNWRQUkJYSnk0eS1XYkI3RlJqMmdPVUY4VGRpNGc2TU5sTkY4dGJTb29XbXVKalM0OXcyRUVwenFtZUFPUjRvTmRrVjY0cDZ4akg5X181ejEwTGV3?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
