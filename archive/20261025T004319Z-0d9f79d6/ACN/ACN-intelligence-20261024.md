# ACN Intelligence Report

- ticker: **ACN**
- Report as_of: **2026-10-24**
- Market data as_of: **2026-10-23**
- Quant sources: https://finance.yahoo.com/quote/ACN/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/ACN/key-statistics/
- AI analysis snapshot as_of: **2026-10-24**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-25T00:45:35.918879+00:00**
- AI status: **Partial: 1 headline remains unclassified and excluded from research conclusions**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 7, 'ai': 11, 'unknown': 1, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 9 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 28.0%; oldest publication 2026-10-17

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 249.3700 |
| Return 1D (%) | -3.6214 |
| Return 1W (%) | 8.5728 |
| Return 1M (%) | 36.9717 |
| Return YTD (%) | -4.3793 |
| Return 1Y (%) | 2.6982 |
| Annualized volatility (%) | 49.3586 |
| Beta vs SPY | 0.0749 |
| Max drawdown (%) | -56.5068 |
| Sharpe (rf=0) | 0.3019 |
| Downside deviation (rf=0, %) | 34.3622 |
| Sortino (rf=0) | 0.4337 |
| Historical VaR 95% (1D, %) | 4.4016 |
| Historical ES 95% (1D, %) | 6.7690 |
| Correlation vs SPY | 0.0193 |
| Tracking error vs SPY (%) | 50.7386 |
| P/E (trailing) | 18.39 |
| P/B | 4.70 |
| EV/EBITDA | 11.14 |
| Revenue growth (%) | 6.20 |
| Forward P/E (estimate) | 15.70 |
| Gross margin (%) | 32.05 |
| Operating margin (%) | 17.83 |
| Return on equity (%) | 26.02 |
| Free cash flow yield (%) | 7.00 |
| MA50 | 194.5973 |
| Close vs MA50 (%) | 28.1467 |
| MA200 | 188.7917 |
| Close vs MA200 (%) | 32.0874 |
| RSI (14, Wilder) | 73.2038 |
| MACD (12,26) | 16.7446 |
| MACD signal (9) | 12.5479 |
| MACD histogram | 4.1967 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'ACN': 267, 'SPY': 267}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 249.3700 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -3.6214 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 8.5728 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 36.9717 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -4.3793 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 2.6982 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 49.3586 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 34.3622 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.4337 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.4016 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 6.7690 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.0193 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 50.7386 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.0749 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -56.5068 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.3019 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 15.6959 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 32.0500 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 17.8280 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 26.0250 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 7.0016 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 18.3901 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 73.2038 -> Overbought momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 4.1967 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 28.1467 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 32.0874 -> Clearly above the moving-average trend level.

## TAILWINDS

### Accenture PLC (ACN) Stock Up 7.7% and Still Undervalued -- GF Score: 90/100
- Summary: Accenture PLC (ACN) Stock Up 7.7% and Still Undervalued -- GF Score: 90/100
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxNYzN3b1o1cG85eDhLaTFlSWw1cTJWUXRoUU9iRnVldzBfbXhRQjBINHFiLTVDWXo5QUx4R1IyTU42NUJVVG9KWFNUX1h6TEJHMWhIMzZXWmE5SmtTZWdnRXdnZVJqQkN1cmZTUmRuNU90c1VjMWFlLUhqam5FTW91V1J0dzV1YXpBZXFuNXVLSnJVMlJZdEptR0xfQk5VYW9vT2N6V0NKSWM?oc=5>

### Accenture Stock: 11 Straight Green Days, Up 25%
- Summary: Accenture Stock: 11 Straight Green Days, Up 25%
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxOcU1TSFZoNFBoLXJNTFlRM2dWMzd0R2MwbjJNdnY2MklsSkVURVI4c2tOcC1FMW5UMGhveWhidkN2NDdlQ2tEUjU3ZTJBYWg2aGE1SEI5TDVhUmstODZpSUl0QTh4WWpiSWtLb193YUVwQmNyQmFTNFNRTGdNdkl6U296Q3RyTHV5SVp3VlpZTEdIYWh0d1NSQTFQa1RuTDctblJxMnBIYw?oc=5>

### Accenture Stock Climbs 24% On A 9-Day Winning Streak
- Summary: Accenture Stock Climbs 24% On A 9-Day Winning Streak
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxNMTBKMDl3UUNqemQ4aFpqNU1QR3g1WTZlMjN4R2x4TE1UendCc09pYkxtV0RDdWVfd1p5M2g5QVhqMXExa0Y0U2w4T3Y2SFZTV0NtdGFBVGxiQlpoMkZ2bzhJcTFJdmxLWjlYVUJJLU5nQXVTbmpLMFFlMFE5OEtqVTFWSzVsOVY2SVVnYnRnY09xdkRXOHJjbXNFbWZCZGN0M2FTS1drQjRDaXliZEJMdQ?oc=5>

### Accenture Stock Rides A 10-Day Winning Streak To A 25% Gain
- Summary: Accenture Stock Rides A 10-Day Winning Streak To A 25% Gain
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxOT1QtRndiY2RLdnF5cDR6VG5nVU0wVy0tSGc2WjRrNWs5MWhuaUJVNlFJNWNwOUJCRXVjWEhKdElzQmN3UnZIT2JqNnQtS1lTdGpzbVB0aUpsZ29LMm94eURBb2VUdmRiVEdURUlwR3pxaW5xRkJvUXVUQUc2VGQ5U0xGTTMtMlBIWWxsYzJxOHNUWl9nVDh5Ty1MZjRCQnJTRWFocXc0WmgxdVE5Q3pRY1lGcFpxMTlESHc?oc=5>

### Accenture Stock Rides An 8-Day Winning Streak To A 20% Gain
- Summary: Accenture Stock Rides An 8-Day Winning Streak To A 20% Gain
- Date: 2026-10-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxORWpISEZrYjNWcGk3MnE0bndDaFRuMmpWb1h5Vk1xQXMwbVM4dVh6cTI5YVllejd2WGVsYWdPUmJuZW9BRXM4Wm5wNmxvalJCOG9YR3lUZHpnVU1teERyNGliNTZ3X1dlVXBLVnRERGVLei1zcFROWGpvbTJHUWV5T1FLbXBYNURKNVJIeEZpWUd0S3J4TEd5UXBIWDdqQXdyUnNYbXhzUmhQeDRGZkJWT1lrYnJoZ0tubnc?oc=5>

### Accenture PLC (ACN) Shares Surge 3.2% -- What GF Score of 87 Tel
- Summary: Accenture PLC (ACN) Shares Surge 3.2% -- What GF Score of 87 Tel
- Date: 2026-10-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxQa0R6OF94QVlySHJIaGo5RkxWMF9XbWhfU0VrZXNycEpobS1hQkhLYmI5bk1YbVE3Qnh2X0hDc0llN1NEeVlRdGxpVGc5UTczQ2E0SGxpcnVwLUpHMFFKdGxZTHp0c2xFOWZSc1RkT0U2UjZMQ1BDNzk0QWIxUzltLXVLaTJlWWZNVUlRSkJEVVV5aUZ5NGpQaDc1ZnN2ZFgzWXlJbjhJZkc5cGlE?oc=5>

### A 12-Day Winning Streak Has Accenture Stock Up 35%
- Summary: Accenture stock rose 35% over 12 days, indicating strong short-term momentum.
- Date: 2026-10-23 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxNbFRPdzh4RGNBNnBJOTNIVXRQdjV5RUM4dzI3d0RxdFVyWDV2RGgwenRabmNySWctWFhyZkdIM1pvMDdNQXUxb0RLaExZQlJvMlVQRHAtRldGZTktRzgya19MakpjSHpvVHQzLTFiRHNtdmJVYU10bXRaeGpEOXBDSHU0YkVBcGpjLXdIOExMVHNEY1pHMUloYUktbkwtVWM4TExLMEZZVEg3Tkc0S0E?oc=5>

### Accenture: 75% Total Return Since July, 23% More By December 2027 (NYSE:ACN)
- Summary: Accenture has delivered 75% return since July, projecting 23% additional growth by Dec 2027.
- Date: 2026-10-23 | Impact: medium | Horizon: long | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxPWkV3TXZFbXhsN3dBUnRYdmI2UWZmUkJNUm9sMmc2TEZzMXhMaEJfaFBqVjdSOWhBNUl6UVZXODMtb2JUblhyT19oY0RlV2ZRYm1JRUp3c1FoRThIR2pKcEpuREZtcWZGbjBrbG9oQXZ5bFNZN3Rodl9WUUlNMVlMSHBidVl6ZFM1ZENwU0NqYmJ5MVI2QjUxSk04a2txeDVCVEIyQmJrRk5Gam9UczMwTzNsQXdlMGI4cFE?oc=5>

### Accenture (ACN) Q4 Results Reinforce AI Bookings And Margin Progress
- Summary: Q4 earnings show strong AI bookings and margin improvement.
- Date: 2026-10-18 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxPQXRJbEYxN1lNN1lLb3lLQzFiS3BTRVVhQ2thS0xjZlBQNWFjeUR2SjZpckcyVEc2VmY0T0Fra09ic0UwalJ6M0Y5S2xfdElrWnh3SWc5eTFwVEVrRUtaT0pSaUw1YjhITkp4M0xfQWRoMGZqY2UzM2hPYkhmbTRwV2RUMzR3YnpTZDRlR2Q0d3lLbHpvR1FQSGRlR0dTU1U?oc=5>

## HEADWINDS

### Accenture downgraded to Neutral at Baird as risk-reward comes into balance (ACN:NYSE)
- Summary: Accenture downgraded to Neutral at Baird as risk-reward comes into balance (ACN:NYSE)
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxQQkY1V0RyTVRGcXhmbGVWU0Nqb2loekNaUWhNek5BeDZIQVNqTXlqN25MVDFzOVZNb2M3UmtTMnhBV1ZEY0p5c3liazloMzlWYmd6NnY3cUN2VXhYUmRwOF9PU3FrbW1UMldSN3lDWFpMT3laSjNyNElfRUU3YjlWMUxpSkx3cFJqSUtFUXQzWnFkZFItZkVvdkRPY1ZyOFlJOWw1cmQ3aTNUX2VpTDN6OHJ3?oc=5>

### Accenture has risen for 12 straight sessions. Is it time to sell?
- Summary: Accenture's 12‑session rally raises sell‑off concerns, potentially signaling a reversal.
- Date: 2026-10-22 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxOY212UGp5T3M3MUVsNXJqQm81bTBOY0UxeEZrazdnVlByZHhXVGs4RkQ3NjZQaEZZOHFRZ25UNFU5RC1yTjV4R05IRFVMTFBtaWNxc2syX2xPVm1oUmwyNTllQWp2X242OTBLRnJxOHBSVkIzS0pJbkw3N2lRaVJ5QWlxQW85d255UGJhc3dYME1iaENwQmpidUU4TEE2TUJENy1DZnUxU0d5UQ?oc=5>

### ISRG, NFLX, ACN Stocks Slide Before The Bell: Why Intuitive Surgical, Netflix And Accenture Are Heading Lower
- Summary: Accenture shares fell pre‑market, reflecting broader downward pressure on tech stocks.
- Date: 2026-10-21 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxPUkZ5UXVsZjJXaGVOT3Z1RkR2TmdDb2xMQ0JNNWJpY2dTX3ZtNFNRVUVVckVReTR2ZGhlUUFtSXl5UElKZE55dnFYdHplX3NkQXVOU1lQcVkySzYyWGo5UFFaaGJadGpjRGRENHVnd0MwVW9KN0dzcm9qdWloZmpVeXAtUXY5ZnJHUE1nX0pyTlptMDZvRFE?oc=5>

### Accenture (ACN) Sees a More Significant Dip Than Broader Market: Some Facts to Know
- Summary: Accenture's dip outpaces the market, indicating potential downside risk.
- Date: 2026-10-23 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxOOWFkcld0SDEyOGVwRlB2NTUyZnN1cmc2RUtwLVRfc2M3b0JZSDgzS1RPVmk3UWVzMDNNRzlDeXpJWWMzUm9Dc2tDUjIyS3NMYkRPVWhSZmF0VUw1Z1pJdFFYNkdOTEtKXzhTekxHdFdhcEJKSDlodjJBV1Y1b3NuRHppWENLWnJzOFVraEdRWjJoX3RpSVpIOFFINXBwVER4dFE?oc=5>

### Baird Downgrades Accenture (ACN) to Neutral After Nearly 100% Ra
- Summary: Baird lowered Accenture’s rating to neutral after a significant rally.
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxNcy1UbGEwdzdoU3RGWXFwT1MxN0dOSjZQaFdsYnczZ1d5Q084bGE5WXllSEp1ZXR4c21JMGtXWVl4NDZxZGxJdlhSampJT0lnOElJQzZ3WGZRWWR0OGRjUU11VURHaXJEU1ZFYnVzZGg1dG44V0JXV0JjUmdoeVROTnVGQlgweU9HalJYdG55aWR0WWhYUTUtRzVkTUxaQm9ESEFyTkVR?oc=5>

### Accenture (ACN) Co-CEO Asia Pacific Ryoji Sekido Sells 5,844 Sha
- Summary: Co‑CEO sold 5,844 shares, indicating insider divestment.
- Date: 2026-10-22 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxNTFc1VkFaR0tHdExqaFZLdGVzTFNVRkJtV1pfT2VoSVpMM3UydktGbUxpMmRFZmhaYVh0YXB5Y3dybmg5QTZMOEtMVS1HY21xYzRKZ1pvd0o3blA3eFdUMUNMaVJMaDVqeHZYVGFZdXM1M1BZV3RnZ2hxUEN2M1kzbDFoMDlHRWp3eVlCUTVDZGlQTVRJU2RqY0NvSWxSaHE1RlQ2VQ?oc=5>

## CATALYSTS

### A 925-share award goes to Accenture (ACN) Chief Accounting Officer Melissa A. Burgum.
- Summary: Accenture awarded 925 shares to its Chief Accounting Officer.
- Date: 2026-10-22 | Impact: low | Horizon: short | Confidence: 1
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxNdmJSdXlUekhWMUFXY2ZRdVhZU0RtcURZdVA5QWFHSzlVOHQ1dXFNTkszUHFFaXJTakx3Q3FwQ2hReGN2S3dPcGZkVmpaX05CTjVVaVNHV3NyUjhRMmplMjdWV2VjNlhBNEExTHZBNUJnNHFqcmozekw0VmZxaVY0U3l0dDRPV1JsV3RaNFV2ZWJVNnJhWlZOZmtBdEhkc21FeFU3V0pTU1Q2dw?oc=5>

### TUV SUD and Accenture (ACN) Launch Physical AI Safety Suite to A
- Summary: Accenture partnered with TUV SUD to launch an AI safety suite.
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 1
- Sources: <https://news.google.com/rss/articles/CBMiyAFBVV95cUxPOXBDVl92X1dvYnRiYzdON255Nl9LLW5DWmM2SkNfUDV5U09yWW1tcFYycVVXUTJ4TTVYUm12T21FcW9GUDFtNk1wZ1puTzRBalBBYktfYU44OUxIWnU3UUxPcFdJamRZUEJJalJTbkNSUlFzWDY2TzdYR0Jwc1ZvNHZHQ0tXaV9zVUphZ0JncFJHTE1OQWdqMFQzSmVYR0JCS2FELXQtdUNVODlCUDk4LWU4S0gzaFJ3MnJ3ZGwyNG5wNEZQbG9RRQ?oc=5>

### A $0-per-share award goes to Accenture (ACN) CEO-Americas John F. Walsh for 10,211 shares.
- Summary: Accenture awarded 10,211 shares to its CEO.
- Date: 2026-10-22 | Impact: low | Horizon: short | Confidence: 1
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxQSTYyTVhlejA3WWdXQklreXAtdXI1SDNGWWpqWVFhdkVVR09JRHJWYlZtRW1rNTRpbEg2TFpCQUxjZ0lxc3NBMGdsLTB5aFdKSXlyU0ZwOXJnSnVpNjNGT3hPUGFLaXl1X3U1cHBPbXZvaVlZOFRCMHlzWDEtaUJLM0VVZnhKV2FzMmxicmlOR3Uya2hTR0JoSlUwS0R5R2RWazd4ak5VSkRSQQ?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **ACN** | **18.39** | **4.70** | **11.14** | **6.20** | **152,599,986,176.00 USD** | **2.70** |
| IBM | 21.63 | 6.74 | 17.82 | 4.70 | 239,644,835,840.00 USD | -8.72 |
| CTSH | 15.17 | 2.20 | 8.13 | 4.50 | 31,774,334,976.00 USD | 6.03 |
| INFY | 15.25 | 9.68 | 21.08 | 1.40 | 50,022,150,144.00 USD | -26.94 |

Peers fetched as_of: 2026-10-24; ACN reuses existing data (market data as_of: 2026-10-23); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-01
- Next expected earnings: 2026-12-17 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-24

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-K
- Filing date: 2026-10-16
- Revenue (latest available single quarter): 18,679,110,000.00 USD; period 2026-06-01/2026-08-31; fiscal year/reporting period 2026/FY
- Net income (latest available single quarter): 1,991,267,000.00 USD; period 2026-06-01/2026-08-31; fiscal year/reporting period 2026/FY
- SEC link: https://www.sec.gov/Archives/edgar/data/1467373/000146737326000049/acn-20260831.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiqAFBVV95cUxNYzN3b1o1cG85eDhLaTFlSWw1cTJWUXRoUU9iRnVldzBfbXhRQjBINHFiLTVDWXo5QUx4R1IyTU42NUJVVG9KWFNUX1h6TEJHMWhIMzZXWmE5SmtTZWdnRXdnZVJqQkN1cmZTUmRuNU90c1VjMWFlLUhqam5FTW91V1J0dzV1YXpBZXFuNXVLSnJVMlJZdEptR0xfQk5VYW9vT2N6V0NKSWM?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxOcU1TSFZoNFBoLXJNTFlRM2dWMzd0R2MwbjJNdnY2MklsSkVURVI4c2tOcC1FMW5UMGhveWhidkN2NDdlQ2tEUjU3ZTJBYWg2aGE1SEI5TDVhUmstODZpSUl0QTh4WWpiSWtLb193YUVwQmNyQmFTNFNRTGdNdkl6U296Q3RyTHV5SVp3VlpZTEdIYWh0d1NSQTFQa1RuTDctblJxMnBIYw?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxNMTBKMDl3UUNqemQ4aFpqNU1QR3g1WTZlMjN4R2x4TE1UendCc09pYkxtV0RDdWVfd1p5M2g5QVhqMXExa0Y0U2w4T3Y2SFZTV0NtdGFBVGxiQlpoMkZ2bzhJcTFJdmxLWjlYVUJJLU5nQXVTbmpLMFFlMFE5OEtqVTFWSzVsOVY2SVVnYnRnY09xdkRXOHJjbXNFbWZCZGN0M2FTS1drQjRDaXliZEJMdQ?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxOT1QtRndiY2RLdnF5cDR6VG5nVU0wVy0tSGc2WjRrNWs5MWhuaUJVNlFJNWNwOUJCRXVjWEhKdElzQmN3UnZIT2JqNnQtS1lTdGpzbVB0aUpsZ29LMm94eURBb2VUdmRiVEdURUlwR3pxaW5xRkJvUXVUQUc2VGQ5U0xGTTMtMlBIWWxsYzJxOHNUWl9nVDh5Ty1MZjRCQnJTRWFocXc0WmgxdVE5Q3pRY1lGcFpxMTlESHc?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxORWpISEZrYjNWcGk3MnE0bndDaFRuMmpWb1h5Vk1xQXMwbVM4dVh6cTI5YVllejd2WGVsYWdPUmJuZW9BRXM4Wm5wNmxvalJCOG9YR3lUZHpnVU1teERyNGliNTZ3X1dlVXBLVnRERGVLei1zcFROWGpvbTJHUWV5T1FLbXBYNURKNVJIeEZpWUd0S3J4TEd5UXBIWDdqQXdyUnNYbXhzUmhQeDRGZkJWT1lrYnJoZ0tubnc?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxQa0R6OF94QVlySHJIaGo5RkxWMF9XbWhfU0VrZXNycEpobS1hQkhLYmI5bk1YbVE3Qnh2X0hDc0llN1NEeVlRdGxpVGc5UTczQ2E0SGxpcnVwLUpHMFFKdGxZTHp0c2xFOWZSc1RkT0U2UjZMQ1BDNzk0QWIxUzltLXVLaTJlWWZNVUlRSkJEVVV5aUZ5NGpQaDc1ZnN2ZFgzWXlJbjhJZkc5cGlE?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxNbFRPdzh4RGNBNnBJOTNIVXRQdjV5RUM4dzI3d0RxdFVyWDV2RGgwenRabmNySWctWFhyZkdIM1pvMDdNQXUxb0RLaExZQlJvMlVQRHAtRldGZTktRzgya19MakpjSHpvVHQzLTFiRHNtdmJVYU10bXRaeGpEOXBDSHU0YkVBcGpjLXdIOExMVHNEY1pHMUloYUktbkwtVWM4TExLMEZZVEg3Tkc0S0E?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxPWkV3TXZFbXhsN3dBUnRYdmI2UWZmUkJNUm9sMmc2TEZzMXhMaEJfaFBqVjdSOWhBNUl6UVZXODMtb2JUblhyT19oY0RlV2ZRYm1JRUp3c1FoRThIR2pKcEpuREZtcWZGbjBrbG9oQXZ5bFNZN3Rodl9WUUlNMVlMSHBidVl6ZFM1ZENwU0NqYmJ5MVI2QjUxSk04a2txeDVCVEIyQmJrRk5Gam9UczMwTzNsQXdlMGI4cFE?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxPQXRJbEYxN1lNN1lLb3lLQzFiS3BTRVVhQ2thS0xjZlBQNWFjeUR2SjZpckcyVEc2VmY0T0Fra09ic0UwalJ6M0Y5S2xfdElrWnh3SWc5eTFwVEVrRUtaT0pSaUw1YjhITkp4M0xfQWRoMGZqY2UzM2hPYkhmbTRwV2RUMzR3YnpTZDRlR2Q0d3lLbHpvR1FQSGRlR0dTU1U?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxQQkY1V0RyTVRGcXhmbGVWU0Nqb2loekNaUWhNek5BeDZIQVNqTXlqN25MVDFzOVZNb2M3UmtTMnhBV1ZEY0p5c3liazloMzlWYmd6NnY3cUN2VXhYUmRwOF9PU3FrbW1UMldSN3lDWFpMT3laSjNyNElfRUU3YjlWMUxpSkx3cFJqSUtFUXQzWnFkZFItZkVvdkRPY1ZyOFlJOWw1cmQ3aTNUX2VpTDN6OHJ3?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxOY212UGp5T3M3MUVsNXJqQm81bTBOY0UxeEZrazdnVlByZHhXVGs4RkQ3NjZQaEZZOHFRZ25UNFU5RC1yTjV4R05IRFVMTFBtaWNxc2syX2xPVm1oUmwyNTllQWp2X242OTBLRnJxOHBSVkIzS0pJbkw3N2lRaVJ5QWlxQW85d255UGJhc3dYME1iaENwQmpidUU4TEE2TUJENy1DZnUxU0d5UQ?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxPUkZ5UXVsZjJXaGVOT3Z1RkR2TmdDb2xMQ0JNNWJpY2dTX3ZtNFNRVUVVckVReTR2ZGhlUUFtSXl5UElKZE55dnFYdHplX3NkQXVOU1lQcVkySzYyWGo5UFFaaGJadGpjRGRENHVnd0MwVW9KN0dzcm9qdWloZmpVeXAtUXY5ZnJHUE1nX0pyTlptMDZvRFE?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxOOWFkcld0SDEyOGVwRlB2NTUyZnN1cmc2RUtwLVRfc2M3b0JZSDgzS1RPVmk3UWVzMDNNRzlDeXpJWWMzUm9Dc2tDUjIyS3NMYkRPVWhSZmF0VUw1Z1pJdFFYNkdOTEtKXzhTekxHdFdhcEJKSDlodjJBV1Y1b3NuRHppWENLWnJzOFVraEdRWjJoX3RpSVpIOFFINXBwVER4dFE?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxNcy1UbGEwdzdoU3RGWXFwT1MxN0dOSjZQaFdsYnczZ1d5Q084bGE5WXllSEp1ZXR4c21JMGtXWVl4NDZxZGxJdlhSampJT0lnOElJQzZ3WGZRWWR0OGRjUU11VURHaXJEU1ZFYnVzZGg1dG44V0JXV0JjUmdoeVROTnVGQlgweU9HalJYdG55aWR0WWhYUTUtRzVkTUxaQm9ESEFyTkVR?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxNTFc1VkFaR0tHdExqaFZLdGVzTFNVRkJtV1pfT2VoSVpMM3UydktGbUxpMmRFZmhaYVh0YXB5Y3dybmg5QTZMOEtMVS1HY21xYzRKZ1pvd0o3blA3eFdUMUNMaVJMaDVqeHZYVGFZdXM1M1BZV3RnZ2hxUEN2M1kzbDFoMDlHRWp3eVlCUTVDZGlQTVRJU2RqY0NvSWxSaHE1RlQ2VQ?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxNdmJSdXlUekhWMUFXY2ZRdVhZU0RtcURZdVA5QWFHSzlVOHQ1dXFNTkszUHFFaXJTakx3Q3FwQ2hReGN2S3dPcGZkVmpaX05CTjVVaVNHV3NyUjhRMmplMjdWV2VjNlhBNEExTHZBNUJnNHFqcmozekw0VmZxaVY0U3l0dDRPV1JsV3RaNFV2ZWJVNnJhWlZOZmtBdEhkc21FeFU3V0pTU1Q2dw?oc=5
- https://news.google.com/rss/articles/CBMiyAFBVV95cUxPOXBDVl92X1dvYnRiYzdON255Nl9LLW5DWmM2SkNfUDV5U09yWW1tcFYycVVXUTJ4TTVYUm12T21FcW9GUDFtNk1wZ1puTzRBalBBYktfYU44OUxIWnU3UUxPcFdJamRZUEJJalJTbkNSUlFzWDY2TzdYR0Jwc1ZvNHZHQ0tXaV9zVUphZ0JncFJHTE1OQWdqMFQzSmVYR0JCS2FELXQtdUNVODlCUDk4LWU4S0gzaFJ3MnJ3ZGwyNG5wNEZQbG9RRQ?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxQSTYyTVhlejA3WWdXQklreXAtdXI1SDNGWWpqWVFhdkVVR09JRHJWYlZtRW1rNTRpbEg2TFpCQUxjZ0lxc3NBMGdsLTB5aFdKSXlyU0ZwOXJnSnVpNjNGT3hPUGFLaXl1X3U1cHBPbXZvaVlZOFRCMHlzWDEtaUJLM0VVZnhKV2FzMmxicmlOR3Uya2hTR0JoSlUwS0R5R2RWazd4ak5VSkRSQQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
