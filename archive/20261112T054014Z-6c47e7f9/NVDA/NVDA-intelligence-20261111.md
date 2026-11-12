# NVDA Intelligence Report

- ticker: **NVDA**
- Report as_of: **2026-11-11**
- Market data as_of: **2026-11-11**
- Quant sources: https://finance.yahoo.com/quote/NVDA/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NVDA/key-statistics/
- AI analysis snapshot as_of: **2026-11-11**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-12T05:44:32.858205+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 8, 'ai': 15, 'unknown': 0, 'irrelevant': 2})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **4** exact headline/source/date matches; prior report **20261111T043601Z-d14951e6/NVDA** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'low_uncalibrated_model_confidence': 1, 'short_term_price_move_in_structural_risks': 1}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 11 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 52.0%; oldest publication 2026-11-09

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 173.7300 |
| Return 1D (%) | 2.8658 |
| Return 1W (%) | -13.1914 |
| Return 1M (%) | -24.2280 |
| Return YTD (%) | -6.6292 |
| Return 1Y (%) | -9.8435 |
| Annualized volatility (%) | 38.5348 |
| Beta vs SPY | 1.7708 |
| Max drawdown (%) | -29.4056 |
| Sharpe (rf=0) | -0.0777 |
| Downside deviation (rf=0, %) | 27.5568 |
| Sortino (rf=0) | -0.1087 |
| Historical VaR 95% (1D, %) | 4.1642 |
| Historical ES 95% (1D, %) | 5.1108 |
| Correlation vs SPY | 0.6309 |
| Tracking error vs SPY (%) | 31.7157 |
| P/E (trailing) | 21.96 |
| P/B | 18.32 |
| EV/EBITDA | 20.68 |
| Revenue growth (%) | 105.90 |
| Forward P/E (estimate) | 10.92 |
| Gross margin (%) | 74.67 |
| Operating margin (%) | 65.21 |
| Return on equity (%) | 117.21 |
| Free cash flow yield (%) | 1.00 |
| MA50 | 217.0983 |
| Close vs MA50 (%) | -19.9763 |
| MA200 | 204.1907 |
| Close vs MA200 (%) | -14.9178 |
| RSI (14, Wilder) | 28.7397 |
| MACD (12,26) | -12.1192 |
| MACD signal (9) | -8.0281 |
| MACD histogram | -4.0911 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NVDA': 280, 'SPY': 280}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 173.7300 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 2.8658 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -13.1914 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -24.2280 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -6.6292 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -9.8435 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 38.5348 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 27.5568 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.1087 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.1642 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.1108 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6309 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 31.7157 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.7708 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -29.4056 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.0777 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 10.9203 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 74.6740 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 65.2140 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 117.2110 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 0.9966 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 21.9633 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 28.7397 -> Oversold momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -4.0911 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -19.9763 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -14.9178 -> Clearly below the moving-average trend level.

## TAILWINDS

### NVIDIA Shares Rise 1% After Hours After Sharp Sell-Off and Leadership Probe - NVIDIA (NASDAQ:NVDA)
- Summary: NVIDIA Shares Rise 1% After Hours After Sharp Sell-Off and Leadership Probe - NVIDIA (NASDAQ:NVDA)
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxQUFNnaWVBSmp5dHI5MTB3ZVJITUdsd1o4MWp0WVdWRDdGcFF0YV9CTHVuREphX2pfQU00akpMRUlFUEN5TDUtTE5ycXBXSUdUNm5wYTNYcnZlSGFwcktwblRYcG5SZjhMV3N1a3A2RlhGbEJQbnNMNU1Wak8wazdnbGJIdjdoQkFXMnUtbE94Mi1jX0dFU1l1TjFxVGJEVFdLb0FUQ1V3aXhkc0FvbS1KVU1JQ3lvenpYREtmWFFNZlVlZw?oc=5>

### Prediction: This Will Be Nvidia’s Stock Price By the End of 2027
- Summary: Forecast of Nvidia’s stock price for 2027.
- Date: 2026-11-11 | Impact: low | Horizon: long | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxOcnFFQkpxelZ3U08taVJQYkhhdHpRX25qcXBsaGNDMEhlazJxdDMtTGlYd3ZWdy1RQTRtMEhaTUtKYllJWlhGWlNyanpWVnN2S3FCcm1FOEZlTHFwUk5sNXpfVldRY0tLdGZyOUx3RmRLMHpjZ1p0eVhYWUNicV9melJPMHBGYUtURzBDNGJxZnVQVkVrZVRDYm5lOExRSmdtbkZSMTg2Zk0tdw?oc=5>

### Analysts Set Nvidia (NVDA) Stock Price Target For 12 Months
- Summary: Analysts set a 12‑month price target for Nvidia.
- Date: 2026-11-11 | Impact: low | Horizon: medium | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxPNGFKTmdPU3lZaU50aGN2Q094VDkyakt0MjhGNkU4Vmp5UjZ1VTBNUGhyU3puMlhUZmphekZJVnBtS3Z6VnBPdFdWRkpIbV9ZeFlzTXJfTVFrcG5oRjN6dEpVMnRDbzVpVkJjMzlITnlxdlZZT3JBbFFjaVFzZld5cXlzQW9oa19FcGZiNE5IcnpFdTFCTDBxVVNmNNIBoAFBVV95cUxPN3BVVlkyX2NSVzFzcHBaSWFlaEVrYTY2M1hfaWMzM2l2NkYxak5sekJ3SjZ4WGNGZkxXWGZzczZ0ZmtzZHQtX1ZhTHdacW1nMXpGaE94YTRFeUZPeHJNRnNnTURQVDBXek9HSF94b3pjNEgzSXlnYjA1a01EaGtVbWc3WGxxVEF4d2RjbzBLbmpiaThlQ2kxcTBQZFRpNUth?oc=5>

### Why Nvidia Stock Rose Despite Calls for CEO Jensen Huang to Step Down
- Summary: Stock rose amid CEO resignation calls, indicating resilience.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiekFVX3lxTE1UZzI1WVJLZk1fSkxrcWZvOHhNRm5YTWp6bkxqOFN0ZjBTVkJBd2w2dG92eXY5U21SZUdYLU1vQjFRcHpyNkpmTTRYSUdFeWNVZVJmaVpGdWFqNzJhYWtPYzZ2U1lrQWZDZ3BMdFZXTUFKR2hRbURCbEln?oc=5>

## HEADWINDS

### Nvidia Downgraded Ahead Of Report, But Stock Joins AI Rebound
- Summary: Nvidia Downgraded Ahead Of Report, But Stock Joins AI Rebound
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxPQnpPLXNLMDVpTUxSWkd4ZVZlTk9Uck1vMkNhZHpndWVxbUt3YURlM09hTzRWOVd1VU9oVTgtdTJjeXlkRjE5MzMwZlgtZVgwMFJlSjJFNG1sRm9PYnRMWWJsRmxvRG1vYkduLXpRX1pfRFV4dmEwdTdfR3pCSEhaVmFjNnczV0x1LUFqTk9tUTMxN2paM3l4Ry1jWQ?oc=5>

### NVDA Stock Slides To Fresh 7-Month Low Amid CEO Turmoil: Ross Gerber Calls Selloff A Chance To Buy Shares At ‘Absurdly Low Price’
- Summary: NVDA Stock Slides To Fresh 7-Month Low Amid CEO Turmoil: Ross Gerber Calls Selloff A Chance To Buy Shares At ‘Absurdly Low Price’
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxNdnhmZl90TXVGZmFxb3kzTThoajJldGNoTThOWDhzME9Md0M1VTdnWldSRHJZWXFES1NzWlA1b09xWUtHcmZUd0ctc1V0TzBkSUlFWS1pZVI4RXloeVcwMDRMT1RGRzQzTzMySHlBeC0yWThNNlQwTUx3VV8wMVNESVg2Z0RRTVJrLUpndVh5N3lJY25T?oc=5>

### Nvidia stock drops 3%, extending decline on report alleged Chinese spy linked to Nvidia CEO aided $7.5 billion in China chip shipments
- Summary: Nvidia stock drops 3%, extending decline on report alleged Chinese spy linked to Nvidia CEO aided $7.5 billion in China chip shipments
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgJBVV95cUxQaTMzXy1sdW5VeFphNTFTbjYzWUZmdHJLNmhXMTE3cVBybWQ1NFhBUU5lUEZqcWUzNnBMN0J2RmdoYWtidXBQc1pPbFNhZV8zcGVJX2VxX3pzU01JZTV1cFpKanZVWHhSVE5IbWUyaVo5bXoxaUdkQ2Jwd0poWXNrX1VrOGI4SlBNOVExdUMyT0NDeS15dHY3N3FRZ1YyMHpZWmRtOC1MTXFhVEFvMm1xREZmb0xBSWpJTUt1aHdMVTl4NHY5TFY3QjZPSWFqNDNCM2xfeFJDM1FLN18zbmZfMG5OeS1lQ25jWUs1R3hIVkc5amVmMHBIS3kyQl8wS3B3T0d5bjFqM2lYQkt1UDk5Rm9kdlMtZw?oc=5>

### NVDA Stock Set For Best Day In Over 2 Months – Baird Downgrades Shares, Flags Slower AI Spending, Jensen Huang Risk
- Summary: NVDA Stock Set For Best Day In Over 2 Months – Baird Downgrades Shares, Flags Slower AI Spending, Jensen Huang Risk
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxORkgwN3diRWtuWWpxMjBhMEtyblJOTGJzclZ0N0JfVExQaWpkLTVzQ0tJTHpVMkFOcHdNVlE4RlV3Z2N5ckI2V0dLM2ItM3l6a1hMRzVXQk5VWlZsb2JneVVFY1NnRmh4bEgya2tyTXFZeEpScDJVX2VoMm1QZWkzSTFiU3JzOHVjdFVyLW8yUm5IQQ?oc=5>

### Nvidia stock sinks 5% as chipmaker investigates CEO Jensen Huang's relationship with alleged Chinese spy
- Summary: Nvidia stock sinks 5% as chipmaker investigates CEO Jensen Huang's relationship with alleged Chinese spy
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi7gFBVV95cUxObWVFY2cxQURmMnJ2aWFxSlRfeFJzeGJDOEhxbjVqUWVpMU96Mm4wcFNBVG5BaVdBZUIwYnN3WXNsWEZld000V1ZrMl9SR0pVZFB0a21rTUV1U3NJajhTUTN6bjBmVmtIQmhtRWxyV1dyemhvcDFrT1J5TmItcGJyVmt6VGY0VW9nZVBVZ2RIalNEOUhKRGRybVgtdzBPMkpzRTBicXpTaGw3c29vUXhiR21hVmVlWk10NzgySGJwbV9MSWpLeXVpT2hJT1FqU05XTXlZMGQwS285QlhudnBJdkhrMGlRbVJsX0h5alBn?oc=5>

### Nvidia sells off for second day in fallout from Jensen Huang’s affair with alleged spy
- Summary: The CEO’s personal scandal has triggered a sustained sell‑off, damaging investor confidence in NVDA.
- Date: 2026-11-10 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMihwFBVV95cUxQYUp3aWtLM3FHZFMycjJkRGVUeXFXWUdPOV9fbEtkVUhwUk5oX2xDVHZ4alZwdl93VnY1UzMwSUN5QjJneHVzdTZHR21JUnkyU2NtZ05LazhQMHoteDNzSVUxQ2lTR0VVSk8yczdTVTd5cXFHNnFUR1hHdVlfc1psbktyRy1OTTQ?oc=5>

### Chip stocks' slide nears $5 trillion as Nvidia hits most extreme selling level since 2019
- Summary: A broader semiconductor market decline has pushed NVDA shares to a record low, increasing downside risk.
- Date: 2026-11-10 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi3AFBVV95cUxNeGhUMWhtSk5Kdm9GOHhVaFlETXR3clBfSEI0VnRtTHNtWEFNWkIxelY4R2NyUjQzMjg5SF9JZ0xOZldPSGR3WlBhejJjNTdmM21HdFQzaGpwMEFrVGxMMFB1RHQ0MkVvOUtCeklOMFJmemRmUDRIRS1sS2VheW5UUDc4anhmQU5ZUV9HY09lTEpUWmFfLWZOOXhUcVZFeTRVQXZVeGE0TzhxdVVnaDRPTzdVWXY2TmQ1UEgyNGJHMFhFS241ZkJGa1o2NHphdmdSV0xCRjh0Q0k0MHdF?oc=5>

### Why Nvidia Stock Just Fell Again
- Summary: Recent stock decline signals market uncertainty.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxNSmtybzdycmQ0VmZnWUU4OXBtbUs3ZUNsM1BzZG9FNi1Temw4enFfN09LQXhHS3VvSF9oSkNkLWZwaWxDeHRnU0lQTVNPbWJUSGtYTmlqaHBlVUN2bW9zTzl5VWVfNUd0Z3AxQ1pIbGxtRHJ5M2h4MFk0WldqbXVvM2dWQ2NaYVNiRFJQb0Njd2RpZ2RlLWc?oc=5>

## CATALYSTS

### Nvidia is worth nearly 30% less if Jensen Huang is no longer CEO: tech analyst
- Summary: Nvidia is worth nearly 30% less if Jensen Huang is no longer CEO: tech analyst
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1wFBVV95cUxQc0MwV3BSdEl1N0dEckdJQUhVMk1sc3BLYm1zWHJxYk92YjhkU081aGhiUl9hbUlfOGF0Y3d0ekFuWVI2UzdIUzZ5TklTMi1NT3V0VDJuZUZxRGVld3ZHQ2ZQSlJidWNuU2NKa19qR2YtOVFpTkNLb1RjZ2x4RHpCYmNhaXVZTWV0aFFYUnJycTl2OEk0OGRBckRVZXJPaHhrc0lkNURZOHlkVDJRbndaQUhxRmJaQ2p3NWZ4cGdIajE5djh1QWxMcnpteGlGSW1tZG1wLS1wMA?oc=5>

### Nvidia Stock Just Had Its Price Target Slashed 60%. Others Still Say Buy. Who's Right?
- Summary: Nvidia Stock Just Had Its Price Target Slashed 60%. Others Still Say Buy. Who's Right?
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxPX29wX0hjNEdkbG15cGFOaFJlQTJxN0ZORjZwa3lhaE9sTlg4aVZZaTNNVnp0ekxkbE1fVVBzdEc5MnQ0LXllS1dsQ0VRdV91ZEp2WHhOQjBScVM1aW5jYWJ3SmNNV2ZGOHlyYVRDaVdtOTIwU3JfZEozUDlfNlYzY1dPWV9MWjRvdzdCY1VnRU9UTjFLRjhDTmFJbHhlYUNFazAyRFViYk9xc3dyNFJVNmhnb1FkVUtuVzVFbDVxTWVnMkE?oc=5>

### 'Icarus' rise and fall': Analyst downgrades Nvidia stock amid Jensen Huang woes, highlights risks
- Summary: Analyst downgrade citing Jensen Huang concerns, indicating potential downside pressure.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi4wFBVV95cUxOUFJBOGQzQXE2NFkxd21JeE9YUml1MHdrVUo3c2wxRVhYal9YU1NPUllYR3Q0QUdMSG5iRFRGb3l4SE1iT2NWc2tLcXpUZktPMUs2SUdPSmRwWjR0ZVM4STdtNjNGbzhDX3FGNE9QYjR5M2o3NjdNTmRvNEo3S283Wk15Vk4zVnBQSlM3X09VR3lXb1RRN09GUkRCVTFnc1UzNXg5VlhqazV2WXhFdnNzSzJSaGc2cmRXYmtuRnhJYjB1QVY1RjhNTnlTRWd0ODItRjBHSjE1LWt4WWlxMHpTTzhBRQ?oc=5>

### Nvidia: Selloff Into Earnings Sets Up An Upside Guidance Surprise (NASDAQ:NVDA)
- Summary: Selloff precedes positive earnings guidance surprise, potentially boosting stock.
- Date: 2026-11-11 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxQdXdTT3ExWm92eXhwOEJTMXRvNFdod0xhWnB4UEViSUZMQjMwNUlRUXdlWWtIcEZlOHdFVXFPNEt5bEh0VEdFYkhNMnpMckRqckEzNFdiTm1ITzNhQXlUdGhkQXBoTDRXMUlrOXJrY21ERXc2ckRMT1F4U3JKQVM3OUp2SHZWaF84czJCazZYWlBzWDFGS3dvMlU1RUlQbDAzNUpqYWV2OTM?oc=5>

### NVIDIA (NVDA) Stock Update: Morgan Stanley Removes from Preferre
- Summary: Morgan Stanley removes Nvidia from preferred list, signaling negative outlook.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxOSXNYSXJhNk5fdFJJYl9XR2cxU3pWSVc2U2ZLUHpNSUswTWlMakJTUU02WXI3MzFJTWMzd2did3dYSW1QTFdNS1A3VlBsRDN6TERaTFNrZk1jWVNwWnRVcVBNeDVZS2ZMYVBvRXpYOEdjZkdLUHdrSGhLalpqamZ4dWZHQTdWbDE1X1h6WUtHeVA2U0t3YlNzaHNpdWU2SV91VV80NmwzY0prQQ?oc=5>

### Nvidia Stock (NVDA) Hasn’t Been This Cheap in 15 Years. Time to Buy?
- Summary: Recommendation to buy due to low price, suggesting bullish view.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxOZXRKam4tUlZaV2hKNi1JWG5iWXRBaTZiY1NJVkp0bFNhS18xWXBUUFdoMzY3N0JUcWdpWjN1NWlFQVZRVEVJa3BNTGJkd19KM2xJNU9nN3NQaDJrU0tYengxbHFXcVRnU01VSzhzeWZUektULWtNSFo0blJpZmtzVThmQ2h5UDcwSXowYVViV1B0YVRUNEVPcQ?oc=5>

### Michael Burry Sees Nvidia Becoming ‘A Heck Of A Trade’ — Reveals His 2 Biggest Bets And Where He’s Buying More
- Summary: Burry bullish on Nvidia, increasing positions, indicating positive sentiment.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxOTGtjRlAyQkNSTWY2SE5uQVh6cUZqQkNHcGl0SEptX1VFUXJtV1FMakhDTWlQbEFFYzZuWkZrRXlkZDVQTEtmbUFad2ZxUlhoUTdNZmo1Ym9vQ3c4Qk5kakpYbVlzTF9UQS0xbTl1Q0xqRDlaNWFnVGdSd0ZLVTdBUlItd3hRVEJWdjkyVVk4b3pPdUNMSmRxSHY3aXBpbUpr?oc=5>

### Wall Street is cooling on Jensen Huang's Nvidia — but history says don't give up on the stock just yet
- Summary: Wall Street sentiment cooling on Nvidia, yet historical resilience suggests potential rebound.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi8AFBVV95cUxPcVFOR2J3MVVxbW16U3BQWHZaMzVwUGRMTkY4SUxxbXFvUDFvSldIRk5VMXUwVUE5QUdnbXBMbUVORHVESk5YUVZmUlo2NHZqc1pIUFAwazZnR2xyc0Nvcjl4WnVWX05xQXYzYzRlbnRBX0ZOX0loZ3ptR3NKS2lwN3AxYmNwdFo4Y0UyeFo2R214WUU3VU9OSjdrNGFzekxNSzlPRzNLRW83M3lRbGxpbERCWk5iTHpzOWpKZWloaGJJNjFEa1RqMm1LZ0Jab1lfVW5QME1fY3owdlpCQUxNcF9ETklWeDNfVi1laVNMN2E?oc=5>

### NVIDIA Stocks Rise Despite Baird Downgrade as $10 Billion Anthropic Bet Emerges
- Summary: Stocks climb amid a $10B Anthropic bet, despite a Baird downgrade.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxQMmdSdTRSdmdQT3NENEU4UEU5ODUyWFBINmZYY1RVMTZlRlRDVGttaW93WnRPUmVxdzBlZmJqMFR4SHBhMFp3ekM4N1lTQnd0dkh3WDBWQjhWa0tERTJvaUo5X29OcWNJaUE5cWZLWEN5TXF4cm9kTTVlTHVTRGk5ckRDcDAtZlRIMkMyN25mcU5XeHlPUEh2MERuWHpBUQ?oc=5>

### Analysts Are Cutting Price Targets on Nvidia Stock. Here's Why.
- Summary: Analysts lower price targets for Nvidia, signaling negative outlook.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxQVWNhclZoTWVNR0tfRExEQzZmRXBaMjBDLWpwSVg5aDAwRkFLQmZQUTEzcUNjeV9McGlfRDV0clFmNlh4OWIxWlpGZ2hPSW96ZWFnWFpFQVNrWXU0bzQxcW5UTU8tUmlJYmo5SEpXLTdrTmtiYm1tVWQwYUZzR2ZiNnJ3V3RqYXJHS0kwcEE1aEdLUkt4TVdIVnpvamJESERSYnZ6Wg?oc=5>

## RISKS

### Prediction: After Losing Over $1.7 Trillion in Market Cap This Year, Nvidia Stock Will Rebound in Epic Fashion. Here's Why.
- Summary: Despite massive market cap loss, a predicted rebound indicates high upside potential.
- Date: 2026-11-11 | Impact: high | Horizon: medium | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMi9wFBVV95cUxNUk5yd1l5YjdaOTM2dDFiWmQ4U0V2QTd3ZHlkLWtnVV9zUzN1SXZYSE93NzQyVWZ1Rk5BZldqZ1BiQmp0YXNKb19Zc2lxanhqQUViWGtPeWhjWUt0WHgyVTd5QmhKUmZlSXhHbmtMRDJlZlBXLW9PYUZoMEF2ZkdJa2RKUlJRV2FlR244MGp5OUFmSEc5UmlEOFh6MncwNENJOG1hSVlxUk80dFVDM3BGc1A5RmY3MFM1OFFvdU5VWmpHRmlxb0hCYmh0c0JBZ3Y1aVNKM2Z3ZFlVbjhKYWM2LTFGbFY3Smt3R2ZoZm13UExrU3o3N0RN?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NVDA** | **21.96** | **18.32** | **20.68** | **105.90** | **4,195,058,188,288.00 USD** | **-9.84** |
| AMD | 110.14 | 13.26 | 80.79 | 44.70 | 906,804,330,496.00 USD | 132.78 |
| AVGO | 44.09 | 16.53 | 32.21 | 85.50 | 1,647,952,527,360.00 USD | -1.19 |
| INTC | N/A | 2.89 | 18.03 | 20.90 | 332,187,500,544.00 USD | 64.99 |

Peers fetched as_of: 2026-11-11; NVDA reuses existing data (market data as_of: 2026-11-11); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-26
- Next expected earnings: 2026-11-17 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-11

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

- https://news.google.com/rss/articles/CBMiwgFBVV95cUxQUFNnaWVBSmp5dHI5MTB3ZVJITUdsd1o4MWp0WVdWRDdGcFF0YV9CTHVuREphX2pfQU00akpMRUlFUEN5TDUtTE5ycXBXSUdUNm5wYTNYcnZlSGFwcktwblRYcG5SZjhMV3N1a3A2RlhGbEJQbnNMNU1Wak8wazdnbGJIdjdoQkFXMnUtbE94Mi1jX0dFU1l1TjFxVGJEVFdLb0FUQ1V3aXhkc0FvbS1KVU1JQ3lvenpYREtmWFFNZlVlZw?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxOcnFFQkpxelZ3U08taVJQYkhhdHpRX25qcXBsaGNDMEhlazJxdDMtTGlYd3ZWdy1RQTRtMEhaTUtKYllJWlhGWlNyanpWVnN2S3FCcm1FOEZlTHFwUk5sNXpfVldRY0tLdGZyOUx3RmRLMHpjZ1p0eVhYWUNicV9melJPMHBGYUtURzBDNGJxZnVQVkVrZVRDYm5lOExRSmdtbkZSMTg2Zk0tdw?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxPNGFKTmdPU3lZaU50aGN2Q094VDkyakt0MjhGNkU4Vmp5UjZ1VTBNUGhyU3puMlhUZmphekZJVnBtS3Z6VnBPdFdWRkpIbV9ZeFlzTXJfTVFrcG5oRjN6dEpVMnRDbzVpVkJjMzlITnlxdlZZT3JBbFFjaVFzZld5cXlzQW9oa19FcGZiNE5IcnpFdTFCTDBxVVNmNNIBoAFBVV95cUxPN3BVVlkyX2NSVzFzcHBaSWFlaEVrYTY2M1hfaWMzM2l2NkYxak5sekJ3SjZ4WGNGZkxXWGZzczZ0ZmtzZHQtX1ZhTHdacW1nMXpGaE94YTRFeUZPeHJNRnNnTURQVDBXek9HSF94b3pjNEgzSXlnYjA1a01EaGtVbWc3WGxxVEF4d2RjbzBLbmpiaThlQ2kxcTBQZFRpNUth?oc=5
- https://news.google.com/rss/articles/CBMiekFVX3lxTE1UZzI1WVJLZk1fSkxrcWZvOHhNRm5YTWp6bkxqOFN0ZjBTVkJBd2w2dG92eXY5U21SZUdYLU1vQjFRcHpyNkpmTTRYSUdFeWNVZVJmaVpGdWFqNzJhYWtPYzZ2U1lrQWZDZ3BMdFZXTUFKR2hRbURCbEln?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxPQnpPLXNLMDVpTUxSWkd4ZVZlTk9Uck1vMkNhZHpndWVxbUt3YURlM09hTzRWOVd1VU9oVTgtdTJjeXlkRjE5MzMwZlgtZVgwMFJlSjJFNG1sRm9PYnRMWWJsRmxvRG1vYkduLXpRX1pfRFV4dmEwdTdfR3pCSEhaVmFjNnczV0x1LUFqTk9tUTMxN2paM3l4Ry1jWQ?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxNdnhmZl90TXVGZmFxb3kzTThoajJldGNoTThOWDhzME9Md0M1VTdnWldSRHJZWXFES1NzWlA1b09xWUtHcmZUd0ctc1V0TzBkSUlFWS1pZVI4RXloeVcwMDRMT1RGRzQzTzMySHlBeC0yWThNNlQwTUx3VV8wMVNESVg2Z0RRTVJrLUpndVh5N3lJY25T?oc=5
- https://news.google.com/rss/articles/CBMilgJBVV95cUxQaTMzXy1sdW5VeFphNTFTbjYzWUZmdHJLNmhXMTE3cVBybWQ1NFhBUU5lUEZqcWUzNnBMN0J2RmdoYWtidXBQc1pPbFNhZV8zcGVJX2VxX3pzU01JZTV1cFpKanZVWHhSVE5IbWUyaVo5bXoxaUdkQ2Jwd0poWXNrX1VrOGI4SlBNOVExdUMyT0NDeS15dHY3N3FRZ1YyMHpZWmRtOC1MTXFhVEFvMm1xREZmb0xBSWpJTUt1aHdMVTl4NHY5TFY3QjZPSWFqNDNCM2xfeFJDM1FLN18zbmZfMG5OeS1lQ25jWUs1R3hIVkc5amVmMHBIS3kyQl8wS3B3T0d5bjFqM2lYQkt1UDk5Rm9kdlMtZw?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxORkgwN3diRWtuWWpxMjBhMEtyblJOTGJzclZ0N0JfVExQaWpkLTVzQ0tJTHpVMkFOcHdNVlE4RlV3Z2N5ckI2V0dLM2ItM3l6a1hMRzVXQk5VWlZsb2JneVVFY1NnRmh4bEgya2tyTXFZeEpScDJVX2VoMm1QZWkzSTFiU3JzOHVjdFVyLW8yUm5IQQ?oc=5
- https://news.google.com/rss/articles/CBMi7gFBVV95cUxObWVFY2cxQURmMnJ2aWFxSlRfeFJzeGJDOEhxbjVqUWVpMU96Mm4wcFNBVG5BaVdBZUIwYnN3WXNsWEZld000V1ZrMl9SR0pVZFB0a21rTUV1U3NJajhTUTN6bjBmVmtIQmhtRWxyV1dyemhvcDFrT1J5TmItcGJyVmt6VGY0VW9nZVBVZ2RIalNEOUhKRGRybVgtdzBPMkpzRTBicXpTaGw3c29vUXhiR21hVmVlWk10NzgySGJwbV9MSWpLeXVpT2hJT1FqU05XTXlZMGQwS285QlhudnBJdkhrMGlRbVJsX0h5alBn?oc=5
- https://news.google.com/rss/articles/CBMihwFBVV95cUxQYUp3aWtLM3FHZFMycjJkRGVUeXFXWUdPOV9fbEtkVUhwUk5oX2xDVHZ4alZwdl93VnY1UzMwSUN5QjJneHVzdTZHR21JUnkyU2NtZ05LazhQMHoteDNzSVUxQ2lTR0VVSk8yczdTVTd5cXFHNnFUR1hHdVlfc1psbktyRy1OTTQ?oc=5
- https://news.google.com/rss/articles/CBMi3AFBVV95cUxNeGhUMWhtSk5Kdm9GOHhVaFlETXR3clBfSEI0VnRtTHNtWEFNWkIxelY4R2NyUjQzMjg5SF9JZ0xOZldPSGR3WlBhejJjNTdmM21HdFQzaGpwMEFrVGxMMFB1RHQ0MkVvOUtCeklOMFJmemRmUDRIRS1sS2VheW5UUDc4anhmQU5ZUV9HY09lTEpUWmFfLWZOOXhUcVZFeTRVQXZVeGE0TzhxdVVnaDRPTzdVWXY2TmQ1UEgyNGJHMFhFS241ZkJGa1o2NHphdmdSV0xCRjh0Q0k0MHdF?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxNSmtybzdycmQ0VmZnWUU4OXBtbUs3ZUNsM1BzZG9FNi1Temw4enFfN09LQXhHS3VvSF9oSkNkLWZwaWxDeHRnU0lQTVNPbWJUSGtYTmlqaHBlVUN2bW9zTzl5VWVfNUd0Z3AxQ1pIbGxtRHJ5M2h4MFk0WldqbXVvM2dWQ2NaYVNiRFJQb0Njd2RpZ2RlLWc?oc=5
- https://news.google.com/rss/articles/CBMi1wFBVV95cUxQc0MwV3BSdEl1N0dEckdJQUhVMk1sc3BLYm1zWHJxYk92YjhkU081aGhiUl9hbUlfOGF0Y3d0ekFuWVI2UzdIUzZ5TklTMi1NT3V0VDJuZUZxRGVld3ZHQ2ZQSlJidWNuU2NKa19qR2YtOVFpTkNLb1RjZ2x4RHpCYmNhaXVZTWV0aFFYUnJycTl2OEk0OGRBckRVZXJPaHhrc0lkNURZOHlkVDJRbndaQUhxRmJaQ2p3NWZ4cGdIajE5djh1QWxMcnpteGlGSW1tZG1wLS1wMA?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxPX29wX0hjNEdkbG15cGFOaFJlQTJxN0ZORjZwa3lhaE9sTlg4aVZZaTNNVnp0ekxkbE1fVVBzdEc5MnQ0LXllS1dsQ0VRdV91ZEp2WHhOQjBScVM1aW5jYWJ3SmNNV2ZGOHlyYVRDaVdtOTIwU3JfZEozUDlfNlYzY1dPWV9MWjRvdzdCY1VnRU9UTjFLRjhDTmFJbHhlYUNFazAyRFViYk9xc3dyNFJVNmhnb1FkVUtuVzVFbDVxTWVnMkE?oc=5
- https://news.google.com/rss/articles/CBMi4wFBVV95cUxOUFJBOGQzQXE2NFkxd21JeE9YUml1MHdrVUo3c2wxRVhYal9YU1NPUllYR3Q0QUdMSG5iRFRGb3l4SE1iT2NWc2tLcXpUZktPMUs2SUdPSmRwWjR0ZVM4STdtNjNGbzhDX3FGNE9QYjR5M2o3NjdNTmRvNEo3S283Wk15Vk4zVnBQSlM3X09VR3lXb1RRN09GUkRCVTFnc1UzNXg5VlhqazV2WXhFdnNzSzJSaGc2cmRXYmtuRnhJYjB1QVY1RjhNTnlTRWd0ODItRjBHSjE1LWt4WWlxMHpTTzhBRQ?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxQdXdTT3ExWm92eXhwOEJTMXRvNFdod0xhWnB4UEViSUZMQjMwNUlRUXdlWWtIcEZlOHdFVXFPNEt5bEh0VEdFYkhNMnpMckRqckEzNFdiTm1ITzNhQXlUdGhkQXBoTDRXMUlrOXJrY21ERXc2ckRMT1F4U3JKQVM3OUp2SHZWaF84czJCazZYWlBzWDFGS3dvMlU1RUlQbDAzNUpqYWV2OTM?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxOSXNYSXJhNk5fdFJJYl9XR2cxU3pWSVc2U2ZLUHpNSUswTWlMakJTUU02WXI3MzFJTWMzd2did3dYSW1QTFdNS1A3VlBsRDN6TERaTFNrZk1jWVNwWnRVcVBNeDVZS2ZMYVBvRXpYOEdjZkdLUHdrSGhLalpqamZ4dWZHQTdWbDE1X1h6WUtHeVA2U0t3YlNzaHNpdWU2SV91VV80NmwzY0prQQ?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxOZXRKam4tUlZaV2hKNi1JWG5iWXRBaTZiY1NJVkp0bFNhS18xWXBUUFdoMzY3N0JUcWdpWjN1NWlFQVZRVEVJa3BNTGJkd19KM2xJNU9nN3NQaDJrU0tYengxbHFXcVRnU01VSzhzeWZUektULWtNSFo0blJpZmtzVThmQ2h5UDcwSXowYVViV1B0YVRUNEVPcQ?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxOTGtjRlAyQkNSTWY2SE5uQVh6cUZqQkNHcGl0SEptX1VFUXJtV1FMakhDTWlQbEFFYzZuWkZrRXlkZDVQTEtmbUFad2ZxUlhoUTdNZmo1Ym9vQ3c4Qk5kakpYbVlzTF9UQS0xbTl1Q0xqRDlaNWFnVGdSd0ZLVTdBUlItd3hRVEJWdjkyVVk4b3pPdUNMSmRxSHY3aXBpbUpr?oc=5
- https://news.google.com/rss/articles/CBMi8AFBVV95cUxPcVFOR2J3MVVxbW16U3BQWHZaMzVwUGRMTkY4SUxxbXFvUDFvSldIRk5VMXUwVUE5QUdnbXBMbUVORHVESk5YUVZmUlo2NHZqc1pIUFAwazZnR2xyc0Nvcjl4WnVWX05xQXYzYzRlbnRBX0ZOX0loZ3ptR3NKS2lwN3AxYmNwdFo4Y0UyeFo2R214WUU3VU9OSjdrNGFzekxNSzlPRzNLRW83M3lRbGxpbERCWk5iTHpzOWpKZWloaGJJNjFEa1RqMm1LZ0Jab1lfVW5QME1fY3owdlpCQUxNcF9ETklWeDNfVi1laVNMN2E?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxQMmdSdTRSdmdQT3NENEU4UEU5ODUyWFBINmZYY1RVMTZlRlRDVGttaW93WnRPUmVxdzBlZmJqMFR4SHBhMFp3ekM4N1lTQnd0dkh3WDBWQjhWa0tERTJvaUo5X29OcWNJaUE5cWZLWEN5TXF4cm9kTTVlTHVTRGk5ckRDcDAtZlRIMkMyN25mcU5XeHlPUEh2MERuWHpBUQ?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxQVWNhclZoTWVNR0tfRExEQzZmRXBaMjBDLWpwSVg5aDAwRkFLQmZQUTEzcUNjeV9McGlfRDV0clFmNlh4OWIxWlpGZ2hPSW96ZWFnWFpFQVNrWXU0bzQxcW5UTU8tUmlJYmo5SEpXLTdrTmtiYm1tVWQwYUZzR2ZiNnJ3V3RqYXJHS0kwcEE1aEdLUkt4TVdIVnpvamJESERSYnZ6Wg?oc=5
- https://news.google.com/rss/articles/CBMi9wFBVV95cUxNUk5yd1l5YjdaOTM2dDFiWmQ4U0V2QTd3ZHlkLWtnVV9zUzN1SXZYSE93NzQyVWZ1Rk5BZldqZ1BiQmp0YXNKb19Zc2lxanhqQUViWGtPeWhjWUt0WHgyVTd5QmhKUmZlSXhHbmtMRDJlZlBXLW9PYUZoMEF2ZkdJa2RKUlJRV2FlR244MGp5OUFmSEc5UmlEOFh6MncwNENJOG1hSVlxUk80dFVDM3BGc1A5RmY3MFM1OFFvdU5VWmpHRmlxb0hCYmh0c0JBZ3Y1aVNKM2Z3ZFlVbjhKYWM2LTFGbFY3Smt3R2ZoZm13UExrU3o3N0RN?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
