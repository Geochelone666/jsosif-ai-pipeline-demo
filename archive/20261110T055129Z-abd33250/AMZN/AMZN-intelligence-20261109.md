# AMZN Intelligence Report

- ticker: **AMZN**
- Report as_of: **2026-11-09**
- Market data as_of: **2026-11-09**
- Quant sources: https://finance.yahoo.com/quote/AMZN/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AMZN/key-statistics/
- AI analysis snapshot as_of: **2026-11-09**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-10T05:57:15.394186+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 3, 'ai': 16, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **6** exact headline/source/date matches; prior report **20261109T043242Z-c8e908de/AMZN** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 11 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 29.17%; oldest publication 2026-11-02

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 266.9300 |
| Return 1D (%) | 2.9425 |
| Return 1W (%) | 8.6716 |
| Return 1M (%) | 1.7147 |
| Return YTD (%) | 15.6442 |
| Return 1Y (%) | 9.2140 |
| Annualized volatility (%) | 34.0477 |
| Beta vs SPY | 1.3563 |
| Max drawdown (%) | -20.1967 |
| Sharpe (rf=0) | 0.3794 |
| Downside deviation (rf=0, %) | 21.0681 |
| Sortino (rf=0) | 0.6131 |
| Historical VaR 95% (1D, %) | 2.9016 |
| Historical ES 95% (1D, %) | 4.0742 |
| Correlation vs SPY | 0.5454 |
| Tracking error vs SPY (%) | 28.9513 |
| P/E (trailing) | 21.58 |
| P/B | 4.70 |
| EV/EBITDA | 16.75 |
| Revenue growth (%) | 12.10 |
| Forward P/E (estimate) | 24.48 |
| Gross margin (%) | 51.37 |
| Operating margin (%) | 13.90 |
| Return on equity (%) | 27.42 |
| Free cash flow yield (%) | -1.20 |
| MA50 | 253.9602 |
| Close vs MA50 (%) | 5.1070 |
| MA200 | 244.0790 |
| Close vs MA200 (%) | 9.3621 |
| RSI (14, Wilder) | 59.2297 |
| MACD (12,26) | 1.4444 |
| MACD signal (9) | -0.1317 |
| MACD histogram | 1.5761 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AMZN': 278, 'SPY': 278}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 266.9300 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 2.9425 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 8.6716 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 1.7147 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 15.6442 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 9.2140 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 34.0477 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 21.0681 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.6131 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.9016 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.0742 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5454 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 28.9513 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.3563 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -20.1967 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.3794 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 24.4808 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 51.3740 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 13.9030 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 27.4160 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: -1.2033 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 21.5788 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 59.2297 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 1.5761 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 5.1070 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 9.3621 -> Clearly above the moving-average trend level.

## TAILWINDS

### Amazon.com (NASDAQ:AMZN) Stock Price Up 2.9% - What's Next?
- Summary: Amazon.com (NASDAQ:AMZN) Stock Price Up 2.9% - What's Next?
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxPT1pla2hfV2tqYk5LNkkxVklhV1VDQU1VeWFTTFZmMTRScDBUN2FLU1JRVWtFU0VlVVVoaEVYX2RDY2J5QVpDLVI4UFNSYko1Y1VIOU9jSkVvVm05eEt4UURKZUd6YmFGS1FzU01IRnpQdDRhaUdvWWJyLTJGVWY4US1nMHE4TU1jTkI2LTJ6WjktYWVrNXBCNHRxS0JmVXFTV3ZjWWt1emUtN1ZrUVdB?oc=5>

### Amazon (AMZN) Stock for the Next 10 Years: Buy, Hold, or Avoid?
- Summary: Analyst recommends holding Amazon stock for long-term growth.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxQcDh2YnpDZXpDN1NMZ0FJcEVxNlE1SjIydEJzRXlrMlVlNkg2dk1nQ2xYcVE5aXlUQUpHWWFmdTZKS2FSQWxtbm1sNm9OSTIzSFJGazlqSDhkZWx4NDhrc1dsYlNoN0VGbFhXaFVDQzhzelp3a0FkMi1Hel80UzcyVlctS1FOZ1Y1X0R1UGNWVjZjSzZk?oc=5>

### Amazon: Grocery & Alexa Deep Dive As Retail Margins Hit Records (NASDAQ:AMZN)
- Summary: Amazon's grocery and Alexa divisions show record retail margins, boosting outlook.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxQSzBmakhLXzdsMFpzZ1pqT3Yzb2IzWEdBZ3U2cVBfRk9VNUw1bVJpVlFrdGJRZE84WkhTRVd4VU5uV1Z3LXh4UWFBVVh6SW5DNVZPTUhvQlh2WndZcEFEQllJWmZyS2JsX0tjVWVIamlieEpCV0xCR0FNbUREQUdKYkpIUHE1TTBoSUIybWcwS2o2bWpUMjNCN0N6c2dSM3dlYk93Rk41bXo?oc=5>

### Amazon, Microsoft among hyperscalers that benefit if a data center slowdown occurs: Ives (AMZN:NASDAQ)
- Summary: Amazon benefits from data center slowdown, supporting cloud revenue.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxNYWZWYl9tamprSjdWMThvU05yQ1dBTjBpTzczcV9sRU1Nd1kyVmI1SXdGQWc1dXdFSHhxNjZoMEpEdVhxZFJJcnNfMTFndlpiRVhRU0RlVFJEZ0dIOE5pNHRENG9ldGt6ZDlsb0l3Vld5S21KWVowRTVlZ2dDcEFCZmhPNldobDFfVTFtaDNGZXAzNjRzc2R2VDFsaWZvYmMzTktWQ3B0ZFc2X1UwQ2NhTEFoUWpsRnZCZUVXWHBnNzZDUQ?oc=5>

### Amazon: Strong Buy Before AWS Growth Rewrites The Earnings Story
- Summary: Strong buy call based on AWS growth potential.
- Date: 2026-11-07 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxQQl93OVpSVnlBdHh4UXdoM21WcHVRSFdWc0NDSU1oMXZVcl9QcmEtOHRxa2pOTmxkWFNhN2RjcXMyZTVSX1pYWFhqa0s3Z0xxakQ0eTF2dTBVWDZtZ3lNR2M2emY4eVNlTzJRWkF1OHJsQ1lhcjc4UExBVkdoN3lzd0xkX0ROSzQzcklfLU5JU2NKNE5ELU04U3M0VHNEangzblBmX3Nibw?oc=5>

### Amazon AWS Revenues Up 39% in Q3 as Cloud Rivals Gain Pace: Hold Stock?
- Summary: AWS revenue surge indicates strong cloud performance.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxNLUZROFVtbTFyY0dPYWpZUHkwVlVhWEZ5TzZkZmg0TGtWUmdjc2JMbWxVdEEwWGtfdzE4R0tXOEhWSUZVTWlDQkEwbWl6NnVoWFhYc2hlSC1UN20xSlg4RFpzaTFoZVQwblQtVzY1TmR6dnRaN0hPaHdQYmFTWFZDQWpmZVFkaUVDRlV0b3BySVFxV3RHblY3MGJNZVdWTGtTUFdNbmFtRThRTWRzaFFQelJ1QnBmRHhacjY0T0VoVlIwQQ?oc=5>

## HEADWINDS

### Amazon Stock (AMZN) Falls 2.2% as Tech Stocks Slide (Nov 5)
- Summary: Amazon Stock (AMZN) Falls 2.2% as Tech Stocks Slide (Nov 5)
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMif0FVX3lxTE41RmJybEw3OGE1a0Nzb0luN0NRcXRKY0R5aVl5Q0xTd3ZOUG5hcVF1OVoxN1NCVzlMSl9ZOWhMbFEtR2VIMXJWZmlGT1I3VWVYWF95bl9xYm12eGhYcUpBbE5yMmtoa1ZDVWY2VDF1cTllWG5IcURQbFNOaXBBODg?oc=5>

### Amazon Stock Pulls Back: What's Going On?
- Summary: Amazon shares decline amid market uncertainty, indicating a short‑term headwind.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxQZEZIcG9ISmV5RWJCdDNzY2I2ZHBHaE1YckJnV0ZSWm0tZ3V6Q0lJZDlwclF5NGpQX0hvYlcwZmF0cmVMR29qMHhTZjgwZ293Y1ZMT2JfQ1NFd2h0ZU9xUFRlMVJBelk3d0Nqdkh1WVJyODJKVEdKNV9rTGMta19zNll6cXpaa0xhVkNRTloxQ0Y2QjhSN21RZ3FMWTMyMDl4?oc=5>

### AWS Is on Fire, But Here’s Why Amazon Stock Isn’t Ready to Fly
- Summary: Despite AWS growth, concerns about overall stock performance remain.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxPcUFMek9tMUZ1ZkMzZzZUZ0lNOVpNZkdfYUpVUERqaDZMNENrWlFFNVowOE9TeWlHeDRxWmtBQlpaYWFXbG9BU2NNVGdmSlZXc2VaS0ZuYWdZZVBLazF0SU84WkgxclRXTjZlc01nS0RfTEdFMkR5UXgxaVh2V05ydWNrZTloWFFNV2M5ZE5aRGpUaUox?oc=5>

### Stock Market Today, Nov. 5: Amazon Shares Slide as Technology Selloff Erases Early Gains
- Summary: Technology selloff pushes Amazon shares lower, a short‑term headwind.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxPT1hBWi11VWIxcnd2cDlwR1RaSVhUYnZNLUxnc3hIS0w1cDRPYXJ2R0ItLW9XblVMOHh5cllxeGlBQzlHd3dvelZ5TmJNSmZacDdwTzU4RHpvamJPTkJ2blJaUnlMN0VKVW9uZUlSN01JVnZMVnNlTF9RLTlkbElYUE9aZFp5TlZLNGxDeU1NS3F3M28?oc=5>

## CATALYSTS

### Amazon Generated $202 Billion in Quarterly Sales. Most of Its Operating Profit Came From Just 1 Business.
- Summary: Amazon Generated $202 Billion in Quarterly Sales. Most of Its Operating Profit Came From Just 1 Business.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxQSkRvdFM5aDBCaE1MZFZXNWhhdTU0NDAxQzA3YzBGZlVseE12Sjk3NGRfUDRsU193bk1aWk5FckdONXhnRHhjbHhRSjQtd2M1LVF0V0RaVm1hMXBGX1FCTWJyTlNiYW1XVGtxdmQ4clBuQWVqUzlxQUxhUlNJb1RsV3Nsa2lxWWx5cEVlX09Wb3J1MWo4?oc=5>

### Amazon's CEO Andy Jassy Just Announced Huge News for Amazon Investors
- Summary: CEO Jassy announced significant news for investors.
- Date: 2026-11-06 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxPbWRaT1l6VHFoLWlFNThuekNIcllxd2lQbWxZYkM4Qk5EVjNlQ0E4di13cjk4UXQ4YjdnQWRVZjg4ZWpPTGlEeHpJUW40YllHbUxQY09Gb2UzSENJam9KbEJyb3pURzdGZ3ZvbGhwcU1weUFqZk5uTlVaS1FmRHkzWTR1NlVCZEthQWxpWWFZbVdFZ1c2?oc=5>

### Andy Jassy Just Announced Fantastic News for Amazon Stock Investors
- Summary: Amazon CEO announces positive outlook for investors, likely guidance or earnings update.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxQckNpQzYyUWt1NE4xRzdkUGl1NnZGbkJTZFJheXQ3OUFsTGR3NFp1LUVoS2tJcXhQUWhiWmlpLW5JZHZKZV9reHFRNVV6YmtYZ3B2YlFnbWtfaDM3UU01NkRjcUM2THE0WFlQclk4M2Z0emQ2eURfRGlwNHVJZE91M1F0X19OTTkzeFdaYkJHWGFvNU1aekQ0bUxBUDZ2T0ViWjNteXgxaFJfVHRWOUlN?oc=5>

### Amazon.com Inc Stock (AMZN) Opened Up by 5.67% on Nov 9: What Signal Does It Send?
- Summary: AMZN shares opened higher, indicating positive market sentiment.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxNc01Mak9YeUt2ZkhBSkotOW81Nkx3eUptS1dFb3FiRHNfVUVQX3J2dzl2VXhnZDRUNkxVcXI1SWNvWEgtel8tMDFMQUZpeHVCd29JZFdWRkd0VUoxQVFtOE5WaTUzbldmOFQwdDE1YjFHSVNMcmZFZ1NkWC1hZ1ZMcnBOaVlDb2NQYk44?oc=5>

### Why Amazon (AMZN) stock is up today
- Summary: Shares are up today, reflecting favorable market reaction.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxPc0psZUdJVkZZWUFsN0FzeGw0Zk1LcVUzQjNnMDJxMDQwalRDY3hOZ1oxdmJBZzRlSjVoS29wemdJREJEajVpNWxJbzlITnhma2ltME5aTHpvSEhYSWREeW8wekphMUNyNkdZTEZIYTZJT2llaGNsbVNNN1VnTV9pYjlqcERhSm9CeE1oS05oRlFyRU9BbzdHN1BiS3hoRnNNd2VGTVgwYTNmSmU5VHhGRWJpeHlGaUs1Smc?oc=5>

### Amazon Is “the Cheapest It’s Been” in Years. Its P/E Fell From 34 to 21
- Summary: Amazon’s P/E ratio dropped from 34 to 21, indicating a cheaper valuation for investors.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxOWDBOTm13THhibmtfRG1EOS1sSlRjY25uRTdxbUlCbS03OExaa2s0Z2JHR3BndzZfVWo1Z3BIWWN5ZEQ3cm5mUlJvWXlrZWRRS2pVM0pUSW85NU8yeDNVMUpQTUJfNDFOVjVnSnVXcE10ZVc0blRHWEJ1OTRPU0EtMU1aSmxjdmZoRHhsb3d3NkhUOHhr?oc=5>

### Amazon: AWS Just Confirmed Bill Ackman’s 50% Margin Thesis (NASDAQ:AMZN)
- Summary: AWS confirms a 50% margin, supporting Amazon’s profitability outlook.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxOZ09xYjVfWVBtQVdYanFzUVFFTWFKS0F1MzVzblBhTjVvOHR1aXNMUnpvY25tVm1NMHY3WFo2WUJiaVRIU0kxTFNBWWI4VURSV0xxWmc0YTd0XzQzRnY5WVdBZVNZa0t6WEJWVVlsckpFMVVTSkdlbmRGMndTbGM3V1JVMHRIQ0twMnhsbTU5TmJqcG01eFhyNTJHNnNpQ01lUXM3SzEtOA?oc=5>

### Amazon to deploy record 40 satellites on first Vulcan flight (AMZN:NASDAQ)
- Summary: Amazon announces deployment of 40 satellites via Vulcan launch, expanding its space capabilities.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxQYXNWVkJkdE1ORm1BZmtVRHQ3T2U2WHRGcXhtRDdEVGE1akVsdmRDNVhSN0lVcEttWjBlQzFwWDNISXRfT01ackZ1RXNEdWE5Qy1IOG5xZDFyaER0dWV6NnN4bDc2ZUdhODR1RzdDX3VEblowNlZNdnQzSkw5Nkx3a0hFTlBXTHpVN0ZDeVE0WXV3YkNfa0o0cW4ySzRFZ0U?oc=5>

## RISKS

### What Could Derail Amazon Stock?
- Summary: Potential risks to Amazon’s stock identified, indicating a high‑impact headwind.
- Date: 2026-11-05 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxNc2RSanZyZnEtaHBiMlkzYl83UTRKSlJ1N0VEWDEydTExcnNjSmxGc1JYYXVOV2tzMVF2U0pzaGNfZ2JIOUlJbkRCQUkwUUlrbjRGdHpqMkgwWnlaUWxQd0N6YmNKVzBuWDgyQkpUY3JVeHpMVHNSTTRLUDhZNzdWXzc2YktFOUJjR3J1bl82dmxUT3VWbnc?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AMZN** | **21.58** | **4.70** | **16.75** | **12.10** | **2,886,350,929,920.00 USD** | **9.21** |
| WMT | 45.53 | 10.16 | 24.21 | 5.90 | 1,000,012,251,136.00 USD | 23.52 |
| MSFT | 28.45 | 8.61 | 20.02 | 18.80 | 4,048,612,753,408.00 USD | 10.64 |
| GOOGL | 15.05 | 5.37 | 18.57 | 24.70 | 3,542,515,974,144.00 USD | 3.61 |

Peers fetched as_of: 2026-11-09; AMZN reuses existing data (market data as_of: 2026-11-09); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-29
- Next expected earnings: 2027-02-04 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-09

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-30
- Revenue (latest available single quarter): 201,944,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 20,685,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMirwFBVV95cUxPT1pla2hfV2tqYk5LNkkxVklhV1VDQU1VeWFTTFZmMTRScDBUN2FLU1JRVWtFU0VlVVVoaEVYX2RDY2J5QVpDLVI4UFNSYko1Y1VIOU9jSkVvVm05eEt4UURKZUd6YmFGS1FzU01IRnpQdDRhaUdvWWJyLTJGVWY4US1nMHE4TU1jTkI2LTJ6WjktYWVrNXBCNHRxS0JmVXFTV3ZjWWt1emUtN1ZrUVdB?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxQcDh2YnpDZXpDN1NMZ0FJcEVxNlE1SjIydEJzRXlrMlVlNkg2dk1nQ2xYcVE5aXlUQUpHWWFmdTZKS2FSQWxtbm1sNm9OSTIzSFJGazlqSDhkZWx4NDhrc1dsYlNoN0VGbFhXaFVDQzhzelp3a0FkMi1Hel80UzcyVlctS1FOZ1Y1X0R1UGNWVjZjSzZk?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxONEtuZjZqdkU4S09PeGIzTFBDQldwWGRNamhYUDZ3N29RQVM3ejFCQWc4Sk9PNUdfd2Vhc3hOWkdENGFMdUg2aFRaMzZ5Vk90Y05ic0VoZ2V4V0ZqbmtfZGZqTFpubHpLeGVQT0oxSlpMWE5sa1RxYWpOOVpPMjQ5NlBsZVJXdjhtVU9ZOGRGWmU1SFhEWng0?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxQSzBmakhLXzdsMFpzZ1pqT3Yzb2IzWEdBZ3U2cVBfRk9VNUw1bVJpVlFrdGJRZE84WkhTRVd4VU5uV1Z3LXh4UWFBVVh6SW5DNVZPTUhvQlh2WndZcEFEQllJWmZyS2JsX0tjVWVIamlieEpCV0xCR0FNbUREQUdKYkpIUHE1TTBoSUIybWcwS2o2bWpUMjNCN0N6c2dSM3dlYk93Rk41bXo?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxNYWZWYl9tamprSjdWMThvU05yQ1dBTjBpTzczcV9sRU1Nd1kyVmI1SXdGQWc1dXdFSHhxNjZoMEpEdVhxZFJJcnNfMTFndlpiRVhRU0RlVFJEZ0dIOE5pNHRENG9ldGt6ZDlsb0l3Vld5S21KWVowRTVlZ2dDcEFCZmhPNldobDFfVTFtaDNGZXAzNjRzc2R2VDFsaWZvYmMzTktWQ3B0ZFc2X1UwQ2NhTEFoUWpsRnZCZUVXWHBnNzZDUQ?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxQQl93OVpSVnlBdHh4UXdoM21WcHVRSFdWc0NDSU1oMXZVcl9QcmEtOHRxa2pOTmxkWFNhN2RjcXMyZTVSX1pYWFhqa0s3Z0xxakQ0eTF2dTBVWDZtZ3lNR2M2emY4eVNlTzJRWkF1OHJsQ1lhcjc4UExBVkdoN3lzd0xkX0ROSzQzcklfLU5JU2NKNE5ELU04U3M0VHNEangzblBmX3Nibw?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxNLUZROFVtbTFyY0dPYWpZUHkwVlVhWEZ5TzZkZmg0TGtWUmdjc2JMbWxVdEEwWGtfdzE4R0tXOEhWSUZVTWlDQkEwbWl6NnVoWFhYc2hlSC1UN20xSlg4RFpzaTFoZVQwblQtVzY1TmR6dnRaN0hPaHdQYmFTWFZDQWpmZVFkaUVDRlV0b3BySVFxV3RHblY3MGJNZVdWTGtTUFdNbmFtRThRTWRzaFFQelJ1QnBmRHhacjY0T0VoVlIwQQ?oc=5
- https://news.google.com/rss/articles/CBMif0FVX3lxTE41RmJybEw3OGE1a0Nzb0luN0NRcXRKY0R5aVl5Q0xTd3ZOUG5hcVF1OVoxN1NCVzlMSl9ZOWhMbFEtR2VIMXJWZmlGT1I3VWVYWF95bl9xYm12eGhYcUpBbE5yMmtoa1ZDVWY2VDF1cTllWG5IcURQbFNOaXBBODg?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxQZEZIcG9ISmV5RWJCdDNzY2I2ZHBHaE1YckJnV0ZSWm0tZ3V6Q0lJZDlwclF5NGpQX0hvYlcwZmF0cmVMR29qMHhTZjgwZ293Y1ZMT2JfQ1NFd2h0ZU9xUFRlMVJBelk3d0Nqdkh1WVJyODJKVEdKNV9rTGMta19zNll6cXpaa0xhVkNRTloxQ0Y2QjhSN21RZ3FMWTMyMDl4?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxPcUFMek9tMUZ1ZkMzZzZUZ0lNOVpNZkdfYUpVUERqaDZMNENrWlFFNVowOE9TeWlHeDRxWmtBQlpaYWFXbG9BU2NNVGdmSlZXc2VaS0ZuYWdZZVBLazF0SU84WkgxclRXTjZlc01nS0RfTEdFMkR5UXgxaVh2V05ydWNrZTloWFFNV2M5ZE5aRGpUaUox?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxPT1hBWi11VWIxcnd2cDlwR1RaSVhUYnZNLUxnc3hIS0w1cDRPYXJ2R0ItLW9XblVMOHh5cllxeGlBQzlHd3dvelZ5TmJNSmZacDdwTzU4RHpvamJPTkJ2blJaUnlMN0VKVW9uZUlSN01JVnZMVnNlTF9RLTlkbElYUE9aZFp5TlZLNGxDeU1NS3F3M28?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxQSkRvdFM5aDBCaE1MZFZXNWhhdTU0NDAxQzA3YzBGZlVseE12Sjk3NGRfUDRsU193bk1aWk5FckdONXhnRHhjbHhRSjQtd2M1LVF0V0RaVm1hMXBGX1FCTWJyTlNiYW1XVGtxdmQ4clBuQWVqUzlxQUxhUlNJb1RsV3Nsa2lxWWx5cEVlX09Wb3J1MWo4?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxPbWRaT1l6VHFoLWlFNThuekNIcllxd2lQbWxZYkM4Qk5EVjNlQ0E4di13cjk4UXQ4YjdnQWRVZjg4ZWpPTGlEeHpJUW40YllHbUxQY09Gb2UzSENJam9KbEJyb3pURzdGZ3ZvbGhwcU1weUFqZk5uTlVaS1FmRHkzWTR1NlVCZEthQWxpWWFZbVdFZ1c2?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxQckNpQzYyUWt1NE4xRzdkUGl1NnZGbkJTZFJheXQ3OUFsTGR3NFp1LUVoS2tJcXhQUWhiWmlpLW5JZHZKZV9reHFRNVV6YmtYZ3B2YlFnbWtfaDM3UU01NkRjcUM2THE0WFlQclk4M2Z0emQ2eURfRGlwNHVJZE91M1F0X19OTTkzeFdaYkJHWGFvNU1aekQ0bUxBUDZ2T0ViWjNteXgxaFJfVHRWOUlN?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxNc01Mak9YeUt2ZkhBSkotOW81Nkx3eUptS1dFb3FiRHNfVUVQX3J2dzl2VXhnZDRUNkxVcXI1SWNvWEgtel8tMDFMQUZpeHVCd29JZFdWRkd0VUoxQVFtOE5WaTUzbldmOFQwdDE1YjFHSVNMcmZFZ1NkWC1hZ1ZMcnBOaVlDb2NQYk44?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxPc0psZUdJVkZZWUFsN0FzeGw0Zk1LcVUzQjNnMDJxMDQwalRDY3hOZ1oxdmJBZzRlSjVoS29wemdJREJEajVpNWxJbzlITnhma2ltME5aTHpvSEhYSWREeW8wekphMUNyNkdZTEZIYTZJT2llaGNsbVNNN1VnTV9pYjlqcERhSm9CeE1oS05oRlFyRU9BbzdHN1BiS3hoRnNNd2VGTVgwYTNmSmU5VHhGRWJpeHlGaUs1Smc?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxOWDBOTm13THhibmtfRG1EOS1sSlRjY25uRTdxbUlCbS03OExaa2s0Z2JHR3BndzZfVWo1Z3BIWWN5ZEQ3cm5mUlJvWXlrZWRRS2pVM0pUSW85NU8yeDNVMUpQTUJfNDFOVjVnSnVXcE10ZVc0blRHWEJ1OTRPU0EtMU1aSmxjdmZoRHhsb3d3NkhUOHhr?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxOZ09xYjVfWVBtQVdYanFzUVFFTWFKS0F1MzVzblBhTjVvOHR1aXNMUnpvY25tVm1NMHY3WFo2WUJiaVRIU0kxTFNBWWI4VURSV0xxWmc0YTd0XzQzRnY5WVdBZVNZa0t6WEJWVVlsckpFMVVTSkdlbmRGMndTbGM3V1JVMHRIQ0twMnhsbTU5TmJqcG01eFhyNTJHNnNpQ01lUXM3SzEtOA?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxQYXNWVkJkdE1ORm1BZmtVRHQ3T2U2WHRGcXhtRDdEVGE1akVsdmRDNVhSN0lVcEttWjBlQzFwWDNISXRfT01ackZ1RXNEdWE5Qy1IOG5xZDFyaER0dWV6NnN4bDc2ZUdhODR1RzdDX3VEblowNlZNdnQzSkw5Nkx3a0hFTlBXTHpVN0ZDeVE0WXV3YkNfa0o0cW4ySzRFZ0U?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxNc2RSanZyZnEtaHBiMlkzYl83UTRKSlJ1N0VEWDEydTExcnNjSmxGc1JYYXVOV2tzMVF2U0pzaGNfZ2JIOUlJbkRCQUkwUUlrbjRGdHpqMkgwWnlaUWxQd0N6YmNKVzBuWDgyQkpUY3JVeHpMVHNSTTRLUDhZNzdWXzc2YktFOUJjR3J1bl82dmxUT3VWbnc?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
