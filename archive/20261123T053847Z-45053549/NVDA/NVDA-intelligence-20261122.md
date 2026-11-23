# NVDA Intelligence Report

- ticker: **NVDA**
- Report as_of: **2026-11-22**
- Market data as_of: **2026-11-20**
- Quant sources: https://finance.yahoo.com/quote/NVDA/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NVDA/key-statistics/
- AI analysis snapshot as_of: **2026-11-22**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-23T05:46:59.365445+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 5, 'ai': 13, 'unknown': 0, 'irrelevant': 7})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **6** exact headline/source/date matches; prior report **20261122T045655Z-f5ef568d/NVDA** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 12 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 40.0%; oldest publication 2026-11-18

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 125.5300 |
| Return 1D (%) | -14.0088 |
| Return 1W (%) | -22.9168 |
| Return 1M (%) | -42.0104 |
| Return YTD (%) | -32.5342 |
| Return 1Y (%) | -30.3417 |
| Annualized volatility (%) | 41.1536 |
| Beta vs SPY | 1.8981 |
| Max drawdown (%) | -47.5297 |
| Sharpe (rf=0) | -0.6738 |
| Downside deviation (rf=0, %) | 31.3311 |
| Sortino (rf=0) | -0.8850 |
| Historical VaR 95% (1D, %) | 4.2460 |
| Historical ES 95% (1D, %) | 5.8772 |
| Correlation vs SPY | 0.6593 |
| Tracking error vs SPY (%) | 33.4994 |
| P/E (trailing) | 13.48 |
| P/B | 11.35 |
| EV/EBITDA | 12.19 |
| Revenue growth (%) | 103.20 |
| Forward P/E (estimate) | 7.56 |
| Gross margin (%) | 74.92 |
| Operating margin (%) | 66.08 |
| Return on equity (%) | 117.36 |
| Free cash flow yield (%) | 3.27 |
| MA50 | 207.0004 |
| Close vs MA50 (%) | -39.3576 |
| MA200 | 203.0853 |
| Close vs MA200 (%) | -38.1885 |
| RSI (14, Wilder) | 15.0466 |
| MACD (12,26) | -19.8282 |
| MACD signal (9) | -15.1980 |
| MACD histogram | -4.6302 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NVDA': 287, 'SPY': 287}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 125.5300 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -14.0088 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -22.9168 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -42.0104 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -32.5342 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -30.3417 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 41.1536 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 31.3311 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.8850 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.2460 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.8772 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6593 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 33.4994 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.8981 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -47.5297 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.6738 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 7.5596 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 74.9210 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 66.0820 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 117.3640 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 3.2740 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 13.4834 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 15.0466 -> Oversold momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -4.6302 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -39.3576 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -38.1885 -> Clearly below the moving-average trend level.

## TAILWINDS

### Bessent Softens on Jensen Huang. Can Nvidia Stock Finally Catch a Break?
- Summary: Analyst Bessent eases concerns, suggesting potential upside for Nvidia stock.
- Date: 2026-11-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMic0FVX3lxTE4xZktlbXhfcGx5MUJTWGpmZG55THFycmcyYWdRVkViMDVqMjZSbmt5ODdSakpEaFFPeXd3M2E2eHR5bDFRbzhEb25ZY0IxOEFLV21KSy0xanJlamd1VmQ1UWQ5ZmpZTGR1aFR1QmZPNndVNGs?oc=5>

## HEADWINDS

### Nvidia (NVDA) shares fell sharply as SEC investigates potential accounting issues
- Summary: Nvidia (NVDA) shares fell sharply as SEC investigates potential accounting issues
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNejVjekR5NUpDRmUzNmNTYUY5clRuR19VMS1VcmFXbld5LWJXMDZHX1otN204QXJoYjFYVEh2MjJjSEp3VHJaUHIyQzBVaHlYc1VQemdCb2FXRjFIRGJWdnVoVzBMeWhMZW1UMFJjalAtS2tESFJsYS10TXBMS0RpbEIxOWVYd2M4T0JUUUloVV9CV0tHQVloTGxYZw?oc=5>

### NVDA Stock Alert: What to Know as Moody's Cuts Nvidia's Outlook Rating
- Summary: NVDA Stock Alert: What to Know as Moody's Cuts Nvidia's Outlook Rating
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxQQmI0cjQ4cUVpYjVTeXNuNFdNRmE4bHFJTDBsbDBNLS1LZGEzeFhsUVRvYzltRjA0YUU4RnYzS1htMkNHTDRDcHdfQXk4QjdRYloyQVRJWGtlLXhHNmJiMmVQMVhJNTduQXNZdld6ald5SmN0bUVHWUJpbmRBR2RIN2tVdEI2cG9hcXNMeExDd1JWNFBtS0JLQlkzWERheDhVSWZVZ3Z1RUNsc21zRjVQNWg4cw?oc=5>

### Nvidia (NVDA) Stock Drops Despite Q3 Results Showing Huge AI Earnings
- Summary: Nvidia (NVDA) Stock Drops Despite Q3 Results Showing Huge AI Earnings
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxPWHNRcEVuR1ViVWpUY0p5RnIyekVpWDRTVUFLXzhLYnFDZ2tfeGctTGFkcENyRFliRXVRSktrc3hiTU01ZW9oY1dzaVJ2dzBNcTBxLWZienhFM0I0dVFDYXp3NTVjM3lZNGhxMXpuZUhuLXdUd1o0RTN2VVR0bzRDNnE0LXByUDJvWFl3VUFra1JDQXZmbV9FejNKdEI?oc=5>

### The post earnings slide in Nvidia stock is getting uglier by the day
- Summary: Nvidia’s post‑earnings performance deteriorates, worsening investor sentiment.
- Date: 2026-11-20 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMizAFBVV95cUxQYVo0b1dObGhWclp0S0JnV095MjVJVEx3QW1hQ3FIdk9VZ3NNZWt2cHp3YnVqbm9EVFJ1UXFlOG1YRmpNdV9CSEFTQ2Z1b0FfdGpaMFJjNVRxZEl5bDJzQ21oLTM1NnNkdHV2LXRvd3p5UjRnQktpanhIcHFPM3FONTlUZTZOU3lqME9rbEdXNVBlcER0WDZNSUxGOWkxaDhDRXI1YUFfcmFvWjliZDQ4UnhVeTNNVUpyN2Z6RUVMRkM4Q2lTdkJsYjBKajM?oc=5>

### Nvidia Stock Has A Cockroach Problem. What Comes Next Could Be Worse
- Summary: Negative report highlights operational issues, raising concerns about future performance.
- Date: 2026-11-22 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxNWklQNGRTcVdjQjVORTluS1l0VEJGd2dYTlNMQnRRTnBmekdvNjMydmp6bnk2aElqbjZ1UHdBeWZkTnZXVmVfZGp6U2NVMVE1NF9CeEhwU0NUYWE1S1VUQUNwQ1JCNE9qYV8ycVU5UmdNMVFEa3hENHRVR2lqcGJ6MmV4MEJKdXlyUXotaUJGVHE3NnZnNFlQMmM5YV9WOHc0amFjbFN3Uml6eHdYaE1SOGJLcUlGZ2Vv?oc=5>

### Leadership Risk vs. Record Numbers: Nvidia Posted $115 Billion in Revenue in Its First Report Without Jensen Huang. What It Means for NVDA Stock.
- Summary: Leadership uncertainty amid record revenue may affect investor confidence.
- Date: 2026-11-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikgJBVV95cUxOR3RGUXpRU3hQZS13ckJJLThxS0l5b0hsSDVUSEl1QW5HZDh4RnhQOGhhbGwwaEQ4RG5Sb1JmcE5IeUtzb1EyNlJXV19nclpyalh6dHJkRTVzaDlQUWdGa0RPdUNQT1JKbUpiZl9lcWNlNTg0LWtzN2h2Mk5kNnpiTjR6Tld2VDcwTDBQcEtRNmJ6Y053b1VTV3FVTGN0bkUtbzBSZDZWWk9nRk1Xc3RscG1rSXR5bldEZUM3VzhDZ01oZ2NxdHAyYlVaRXR0cmFyTDI1UDhjZEZmeGRuLWpYa0M4Nm1iT1FDdmliRGY2V3h1OFhxRnBicVlKZ2wwdEpFZm5Cb3MyZ2pLbEdnRHowckJR?oc=5>

## CATALYSTS

### NVDA Stock Sees Biggest Fall In 22 Months, But Top Analyst Says Nvidia’s AI Boom Isn’t Over Yet — Here Are 5 Reasons Why
- Summary: NVDA Stock Sees Biggest Fall In 22 Months, But Top Analyst Says Nvidia’s AI Boom Isn’t Over Yet — Here Are 5 Reasons Why
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQbDBWLTd5T3R4NFVNLWI0Vm9nWEJmd1FHdDdqLUdfWjJJdXBOWFU1d2x1Nk1NUjNCVW5OT1IzY0hLUnRIbkIxZXBsd1pNMV9MQUppQ2twZmRQT2EwT3Q3V0I2dVVLX1EyOEN6cjdSOTJHWmkydGJ6bFpfb2VaN295ekRxWDM3SXhqcVdOZlhoVzlma3VSOERiaA?oc=5>

### Nvidia (NVDA) Faces New Supply Chain Fears as Elon Musk Warns of Lost Deals Without Jensen Huang
- Summary: Nvidia (NVDA) Faces New Supply Chain Fears as Elon Musk Warns of Lost Deals Without Jensen Huang
- Date: 2026-11-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxNNXVGMmZaX3MybndxZHBsTFhCa0tMNkNEYkFQTVdRQ3RmZEtwQ3paTUl3NURUQXpjMDV0UnhCeUVJaFlfZ2NZZ29pSGZiNmtIcHRxdWQ1VEhYeWVyRWpkMXdvcWJBMDhud211eVE0QmFNRkQwN19BY21IZGt0WkluYUVfS0VxTmZxWl8zN1VEWGxtaXJ2enBzbHlRYnpPSHJQbkRNd3ZZaGxMRnhTNlR4bmlSMVVueHdjLTF5X0VDNEZLdw?oc=5>

### Trump Bought Up to $265,000 of NVIDIA Stock. Here’s Where the Price Target Stands
- Summary: Former President Trump purchased $265,000 worth of NVIDIA shares, indicating personal investment interest.
- Date: 2026-11-20 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxOWFdocXQzR1ZkeXlGTzBsZ3ZybUMwVEhveUlxX0RvekZxWDVYUjJiTnhwaVJ6U3hJZ2E2dUplQ0lndGJJXzVSdGFUWkZXa1RHY205T1JEMUNjcE1kVVhMVExUV3hFNndsMFFzSTJEam9EdUZfcm9DeVRlTEhRazhTSkExMEJObnlCR2gwM011WGxucTR0X3d3?oc=5>

### Nvidia (NVDA) CEO Jensen Huang Resigned As The SEC Opened An Accounting Probe
- Summary: CEO Jensen Huang resigned amid SEC accounting investigation.
- Date: 2026-11-22 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQOXN0TUVMd3I0Sy1tTVg2RkdxSjlaSzRqS0h5VEFab1VmajZ3Z2xTWUhOSjN3TDIzSWZpOGRnclc2NXFaRGdjT25TNzhlZ09pN05KeDF6SEhFMkpXWEI4THRZa2NDc011TjhlRTc1ZENkU3dTTjRNS3RMOTluaUY1MmhIRHRLVnRyVDFUZkhqcGM4YmZMem45cg?oc=5>

### Where Will Nvidia Stock Be in 20 Years? The Answer Might Surprise You.
- Summary: Speculation on Nvidia's stock trajectory over two decades.
- Date: 2026-11-22 | Impact: low | Horizon: long | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxOU2Qzd3l0VU5QZ0Z6cVhjVnhYZzBwVjJBRks4ek9mVV9MNzFrWGdYZDJEcVA0ZGNBVWNwbkRvdkJJTGF4THlVT3d3dzBVZFZOLWJRV3l1Z3FpbklJVGJhNi1PLWl0d0xJRHgxQ09fY1dPMVYzQXBvd3Jab3RaVTlERG1fc2ppWXBwSjhXWjA1a094MnZJT2M4?oc=5>

### Is Nvidia a Buy at $125? Here's My Honest Take
- Summary: Opinion on whether Nvidia shares at $125 represent a good purchase.
- Date: 2026-11-22 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxNNTNVbTlNQklMaHhodnk2a3MxemtGV2FIZWVvNUZfNVVfZFJqNklVOTdhUWhjQ0pQQlVuRXRXSEVuWGFzVDB0eTFyaGcxSExKZGI3T3R5N0hjTEU2aGtRRXp5NWQxeEt3TDM3a2pfcVdRY1paTmtVV01zLTVWeWpWNXlhU0JibDNvQmtZbnNEUkl3MWpq?oc=5>

### GPU prices are rising for Nvidia's older chips even as the stock keeps going down: Chart of the Day
- Summary: Analysis of older Nvidia GPU pricing versus stock performance.
- Date: 2026-11-22 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi6gFBVV95cUxPbmNXRjNhZUdxb2NzZG03T1VJOFdieU1vTWwwNllJRGV3N0h5ei1ZRldwTk5TNmFFSzNFblhCdnVhcFowOXlNZm54a29aeTJEOFJhUU03Z0ZTUU5Hc0doOF8xOE0tcDhlQjBIQ0o5R3p6dFo3eEdwQVFJQUU3bktTSUFDUzl6R2N6a096SGdOejhGdmhFQkRFZS1YMnpNUHpiSDdYU3VNdWloR3g0WFNtM2h0RmxjMUFwU0JUX0ZLa01IdEJZelBUMWdmbEpYVWJLR3ZzdWYwcExNWjJWVjZqNjdNeG9iTjBMcUE?oc=5>

### Prediction: These Will Be AMD’s and Nvidia’s Stock Prices by 2028
- Summary: Forecast of Nvidia and AMD stock prices for 2028.
- Date: 2026-11-22 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxNbHdFUC1rS21oaWZvRjdpMHZBcHN4dXA4U3JyWmtXQklpQTNxelowR1Z3akFuUzF0UkRWa1JJdlpRemxjVWZ4UU1XLVBqQ0g2Qzd4ZVYzMFVIZUtLRVI3RDhJaUpuQzJ5cHFwT1ZET08wN0hVSmpWem0wRi1kbmx0QU5ILTRWX25MUXdnX1diRnJURVFPQV9CWUNUV1JaLW9SckdMd3RiNTg?oc=5>

## RISKS

### Nvidia Stock Plunges 12% After Reuters Reports an SEC Probe of Its Accounting. It’s Nvidia’s Worst Day Since DeepSeek and It Has Lost $2.7 Trillion Since October
- Summary: SEC probe of Nvidia’s accounting triggers a 12% stock drop, marking the worst day since DeepSeek and a $2.7 trillion loss since October.
- Date: 2026-11-20 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNek83Um5vdUVIV3dWb2FVZlZSemZJUmh3Zkt6cUxiYUgxVjJzS3k4Z3lRWEhFRzZ4THRWVTlvSzR6TFVPaDVLYVlIV2Q1alRwODNZNndjQnctNFNmcTJGamk1LWR2bl9oMktRWThaeURldFFJRnowaXE4Nzd1T2hUaFpDSVQ2dlZ1TEVVU3EzOXg1STRmWmRQbDZRNU8?oc=5>

### Nvidia stock extends $2.7 trillion rout as SEC probe reportedly investigates its accounting
- Summary: SEC investigation into accounting practices threatens stock stability.
- Date: 2026-11-21 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi3wFBVV95cUxQS25iVW9uNHFsc3lYdkNPRTJyTUhYcWRVbjhOZlR4QUpLZGs4RkE0d1lSLTEtN2x6N0ZxZnlZdE9KaTQxeS1TbWRFaGFpd0hGc0ZKWmF5OEVRdnFDX1NNWFlBTl9rdVRUVFlxSVRIelpPNmluWVdUVElhQzh1NWtjemJaUnlhRnJ2N3Q2dDNVYlhVYWtXbkswbXhYLWdiOHE0V1dkQ2xjNjFsTlpEQ0hzRDBja0RqV0VFX0FZaXdKRVZ2RHdGVUUtS2VzanJrTkhiSVcxeGVCRXNlUUhSVWJ3?oc=5>

### EXCLUSIVE: Nvidia's accounting is a focus of US SEC investigation, sources say
- Summary: SEC probe focuses on Nvidia's accounting, posing regulatory risk.
- Date: 2026-11-21 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxPMzlPdFVTT2cyVkhmMFVKNWZ1MnpNT0NLcURnblg4THMwUWNuYTRBLWUxU0ZSSUR5bk1zNnBmVlhIUjByNkN6TzVBNC1uaXQxM0dwY2FkMzZQdm00a0xyMXo3NFNpSUNPdERZWU82aGZLa0lNZHpMOXVnVDBVQW9lMmNrWEVRczVYS1Racm1NNlNERDBJeTFJRG1pZVRfTC1LTy1pNjhpVzRaeGRrY25kSzQ1aDNUUQ?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NVDA** | **13.48** | **11.35** | **12.19** | **103.20** | **3,031,172,907,008.00 USD** | **-30.34** |
| AMD | 90.68 | 10.18 | 61.88 | 44.70 | 702,393,286,656.00 USD | 105.99 |
| AVGO | 38.88 | 14.58 | 28.48 | 85.50 | 1,453,140,738,048.00 USD | -11.58 |
| INTC | N/A | 2.37 | 14.91 | 20.90 | 272,553,181,184.00 USD | 52.53 |

Peers fetched as_of: 2026-11-22; NVDA reuses existing data (market data as_of: 2026-11-20); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-17
- Next expected earnings: 2027-02-24 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-22

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-08-26
- Revenue (latest available single quarter): 96,221,000,000.00 USD; period 2026-04-27/2026-07-26; fiscal year/reporting period 2027/Q2
- Net income (latest available single quarter): 59,688,000,000.00 USD; period 2026-04-27/2026-07-26; fiscal year/reporting period 2027/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMic0FVX3lxTE4xZktlbXhfcGx5MUJTWGpmZG55THFycmcyYWdRVkViMDVqMjZSbmt5ODdSakpEaFFPeXd3M2E2eHR5bDFRbzhEb25ZY0IxOEFLV21KSy0xanJlamd1VmQ1UWQ5ZmpZTGR1aFR1QmZPNndVNGs?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNejVjekR5NUpDRmUzNmNTYUY5clRuR19VMS1VcmFXbld5LWJXMDZHX1otN204QXJoYjFYVEh2MjJjSEp3VHJaUHIyQzBVaHlYc1VQemdCb2FXRjFIRGJWdnVoVzBMeWhMZW1UMFJjalAtS2tESFJsYS10TXBMS0RpbEIxOWVYd2M4T0JUUUloVV9CV0tHQVloTGxYZw?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxQQmI0cjQ4cUVpYjVTeXNuNFdNRmE4bHFJTDBsbDBNLS1LZGEzeFhsUVRvYzltRjA0YUU4RnYzS1htMkNHTDRDcHdfQXk4QjdRYloyQVRJWGtlLXhHNmJiMmVQMVhJNTduQXNZdld6ald5SmN0bUVHWUJpbmRBR2RIN2tVdEI2cG9hcXNMeExDd1JWNFBtS0JLQlkzWERheDhVSWZVZ3Z1RUNsc21zRjVQNWg4cw?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxPWHNRcEVuR1ViVWpUY0p5RnIyekVpWDRTVUFLXzhLYnFDZ2tfeGctTGFkcENyRFliRXVRSktrc3hiTU01ZW9oY1dzaVJ2dzBNcTBxLWZienhFM0I0dVFDYXp3NTVjM3lZNGhxMXpuZUhuLXdUd1o0RTN2VVR0bzRDNnE0LXByUDJvWFl3VUFra1JDQXZmbV9FejNKdEI?oc=5
- https://news.google.com/rss/articles/CBMizAFBVV95cUxQYVo0b1dObGhWclp0S0JnV095MjVJVEx3QW1hQ3FIdk9VZ3NNZWt2cHp3YnVqbm9EVFJ1UXFlOG1YRmpNdV9CSEFTQ2Z1b0FfdGpaMFJjNVRxZEl5bDJzQ21oLTM1NnNkdHV2LXRvd3p5UjRnQktpanhIcHFPM3FONTlUZTZOU3lqME9rbEdXNVBlcER0WDZNSUxGOWkxaDhDRXI1YUFfcmFvWjliZDQ4UnhVeTNNVUpyN2Z6RUVMRkM4Q2lTdkJsYjBKajM?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxNWklQNGRTcVdjQjVORTluS1l0VEJGd2dYTlNMQnRRTnBmekdvNjMydmp6bnk2aElqbjZ1UHdBeWZkTnZXVmVfZGp6U2NVMVE1NF9CeEhwU0NUYWE1S1VUQUNwQ1JCNE9qYV8ycVU5UmdNMVFEa3hENHRVR2lqcGJ6MmV4MEJKdXlyUXotaUJGVHE3NnZnNFlQMmM5YV9WOHc0amFjbFN3Uml6eHdYaE1SOGJLcUlGZ2Vv?oc=5
- https://news.google.com/rss/articles/CBMikgJBVV95cUxOR3RGUXpRU3hQZS13ckJJLThxS0l5b0hsSDVUSEl1QW5HZDh4RnhQOGhhbGwwaEQ4RG5Sb1JmcE5IeUtzb1EyNlJXV19nclpyalh6dHJkRTVzaDlQUWdGa0RPdUNQT1JKbUpiZl9lcWNlNTg0LWtzN2h2Mk5kNnpiTjR6Tld2VDcwTDBQcEtRNmJ6Y053b1VTV3FVTGN0bkUtbzBSZDZWWk9nRk1Xc3RscG1rSXR5bldEZUM3VzhDZ01oZ2NxdHAyYlVaRXR0cmFyTDI1UDhjZEZmeGRuLWpYa0M4Nm1iT1FDdmliRGY2V3h1OFhxRnBicVlKZ2wwdEpFZm5Cb3MyZ2pLbEdnRHowckJR?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQbDBWLTd5T3R4NFVNLWI0Vm9nWEJmd1FHdDdqLUdfWjJJdXBOWFU1d2x1Nk1NUjNCVW5OT1IzY0hLUnRIbkIxZXBsd1pNMV9MQUppQ2twZmRQT2EwT3Q3V0I2dVVLX1EyOEN6cjdSOTJHWmkydGJ6bFpfb2VaN295ekRxWDM3SXhqcVdOZlhoVzlma3VSOERiaA?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxNNXVGMmZaX3MybndxZHBsTFhCa0tMNkNEYkFQTVdRQ3RmZEtwQ3paTUl3NURUQXpjMDV0UnhCeUVJaFlfZ2NZZ29pSGZiNmtIcHRxdWQ1VEhYeWVyRWpkMXdvcWJBMDhud211eVE0QmFNRkQwN19BY21IZGt0WkluYUVfS0VxTmZxWl8zN1VEWGxtaXJ2enBzbHlRYnpPSHJQbkRNd3ZZaGxMRnhTNlR4bmlSMVVueHdjLTF5X0VDNEZLdw?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxOWFdocXQzR1ZkeXlGTzBsZ3ZybUMwVEhveUlxX0RvekZxWDVYUjJiTnhwaVJ6U3hJZ2E2dUplQ0lndGJJXzVSdGFUWkZXa1RHY205T1JEMUNjcE1kVVhMVExUV3hFNndsMFFzSTJEam9EdUZfcm9DeVRlTEhRazhTSkExMEJObnlCR2gwM011WGxucTR0X3d3?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQOXN0TUVMd3I0Sy1tTVg2RkdxSjlaSzRqS0h5VEFab1VmajZ3Z2xTWUhOSjN3TDIzSWZpOGRnclc2NXFaRGdjT25TNzhlZ09pN05KeDF6SEhFMkpXWEI4THRZa2NDc011TjhlRTc1ZENkU3dTTjRNS3RMOTluaUY1MmhIRHRLVnRyVDFUZkhqcGM4YmZMem45cg?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxOU2Qzd3l0VU5QZ0Z6cVhjVnhYZzBwVjJBRks4ek9mVV9MNzFrWGdYZDJEcVA0ZGNBVWNwbkRvdkJJTGF4THlVT3d3dzBVZFZOLWJRV3l1Z3FpbklJVGJhNi1PLWl0d0xJRHgxQ09fY1dPMVYzQXBvd3Jab3RaVTlERG1fc2ppWXBwSjhXWjA1a094MnZJT2M4?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxNNTNVbTlNQklMaHhodnk2a3MxemtGV2FIZWVvNUZfNVVfZFJqNklVOTdhUWhjQ0pQQlVuRXRXSEVuWGFzVDB0eTFyaGcxSExKZGI3T3R5N0hjTEU2aGtRRXp5NWQxeEt3TDM3a2pfcVdRY1paTmtVV01zLTVWeWpWNXlhU0JibDNvQmtZbnNEUkl3MWpq?oc=5
- https://news.google.com/rss/articles/CBMi6gFBVV95cUxPbmNXRjNhZUdxb2NzZG03T1VJOFdieU1vTWwwNllJRGV3N0h5ei1ZRldwTk5TNmFFSzNFblhCdnVhcFowOXlNZm54a29aeTJEOFJhUU03Z0ZTUU5Hc0doOF8xOE0tcDhlQjBIQ0o5R3p6dFo3eEdwQVFJQUU3bktTSUFDUzl6R2N6a096SGdOejhGdmhFQkRFZS1YMnpNUHpiSDdYU3VNdWloR3g0WFNtM2h0RmxjMUFwU0JUX0ZLa01IdEJZelBUMWdmbEpYVWJLR3ZzdWYwcExNWjJWVjZqNjdNeG9iTjBMcUE?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxNbHdFUC1rS21oaWZvRjdpMHZBcHN4dXA4U3JyWmtXQklpQTNxelowR1Z3akFuUzF0UkRWa1JJdlpRemxjVWZ4UU1XLVBqQ0g2Qzd4ZVYzMFVIZUtLRVI3RDhJaUpuQzJ5cHFwT1ZET08wN0hVSmpWem0wRi1kbmx0QU5ILTRWX25MUXdnX1diRnJURVFPQV9CWUNUV1JaLW9SckdMd3RiNTg?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNek83Um5vdUVIV3dWb2FVZlZSemZJUmh3Zkt6cUxiYUgxVjJzS3k4Z3lRWEhFRzZ4THRWVTlvSzR6TFVPaDVLYVlIV2Q1alRwODNZNndjQnctNFNmcTJGamk1LWR2bl9oMktRWThaeURldFFJRnowaXE4Nzd1T2hUaFpDSVQ2dlZ1TEVVU3EzOXg1STRmWmRQbDZRNU8?oc=5
- https://news.google.com/rss/articles/CBMi3wFBVV95cUxQS25iVW9uNHFsc3lYdkNPRTJyTUhYcWRVbjhOZlR4QUpLZGs4RkE0d1lSLTEtN2x6N0ZxZnlZdE9KaTQxeS1TbWRFaGFpd0hGc0ZKWmF5OEVRdnFDX1NNWFlBTl9rdVRUVFlxSVRIelpPNmluWVdUVElhQzh1NWtjemJaUnlhRnJ2N3Q2dDNVYlhVYWtXbkswbXhYLWdiOHE0V1dkQ2xjNjFsTlpEQ0hzRDBja0RqV0VFX0FZaXdKRVZ2RHdGVUUtS2VzanJrTkhiSVcxeGVCRXNlUUhSVWJ3?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxPMzlPdFVTT2cyVkhmMFVKNWZ1MnpNT0NLcURnblg4THMwUWNuYTRBLWUxU0ZSSUR5bk1zNnBmVlhIUjByNkN6TzVBNC1uaXQxM0dwY2FkMzZQdm00a0xyMXo3NFNpSUNPdERZWU82aGZLa0lNZHpMOXVnVDBVQW9lMmNrWEVRczVYS1Racm1NNlNERDBJeTFJRG1pZVRfTC1LTy1pNjhpVzRaeGRrY25kSzQ1aDNUUQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
