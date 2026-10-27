# GIS Intelligence Report

- ticker: **GIS**
- Report as_of: **2026-10-26**
- Market data as_of: **2026-10-26**
- Quant sources: https://finance.yahoo.com/quote/GIS/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/GIS/key-statistics/
- AI analysis snapshot as_of: **2026-10-26**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-27T02:03:21.867516+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 22, 'rule': 9, 'ai': 8, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **9** exact headline/source/date matches; prior report **20261026T005504Z-6368ad31/GIS** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 22 unique headlines; 8 named publishers; 2 exact duplicates; 22 HTTPS source links; largest publisher share 45.45%; oldest publication 2026-10-19

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 33.7000 |
| Return 1D (%) | -2.0064 |
| Return 1W (%) | 3.4695 |
| Return 1M (%) | 2.0827 |
| Return YTD (%) | -22.5268 |
| Return 1Y (%) | -24.0138 |
| Annualized volatility (%) | 30.2080 |
| Beta vs SPY | -0.3832 |
| Max drawdown (%) | -33.2524 |
| Sharpe (rf=0) | -0.8273 |
| Downside deviation (rf=0, %) | 21.4983 |
| Sortino (rf=0) | -1.1625 |
| Historical VaR 95% (1D, %) | 3.0361 |
| Historical ES 95% (1D, %) | 3.8909 |
| Correlation vs SPY | -0.1613 |
| Tracking error vs SPY (%) | 34.6141 |
| P/E (trailing) | N/A |
| P/B | 2.42 |
| EV/EBITDA | 9.14 |
| Revenue growth (%) | -2.80 |
| Forward P/E (estimate) | 10.69 |
| Gross margin (%) | 33.73 |
| Operating margin (%) | 15.24 |
| Return on equity (%) | -10.49 |
| Free cash flow yield (%) | 7.23 |
| MA50 | 35.2885 |
| Close vs MA50 (%) | -4.5016 |
| MA200 | 36.4380 |
| Close vs MA200 (%) | -7.5142 |
| RSI (14, Wilder) | 50.9410 |
| MACD (12,26) | -0.2049 |
| MACD signal (9) | -0.6345 |
| MACD histogram | 0.4296 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'GIS': 268, 'SPY': 268}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 33.7000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -2.0064 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 3.4695 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 2.0827 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -22.5268 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -24.0138 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 30.2080 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 21.4983 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -1.1625 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.0361 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.8909 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.1613 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 34.6141 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.3832 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -33.2524 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.8273 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 10.6907 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 33.7280 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 15.2430 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: -10.4950 -> Adjusted price fell over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 7.2291 -> No interpretation rule is available for this metric.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 50.9410 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.4296 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -4.5016 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -7.5142 -> Clearly below the moving-average trend level.

## TAILWINDS

### Wagyu beef and hot honey chicken are now meat-stick flavors
- Summary: General Mills introduces new meat-stick flavors, expanding product line.
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxQTHFaU0laTzlvaXB4LUl1MDhnSURnb2lTY0QyOFRnajhPVDJ5X3M1RTh4UXRLdzJ0bkZLTUp5eTFHNzdHZWJGbnFlOXIyRi16LTZBZEpldUNpWlVsN3FXMWVmRFRSU1BiRnk0SEtMRUhlWlpCZXc2RUdoNnhFMVEwVS1UQXNhQ2FoTXEzSmsxUVJrMXpvM0ZYYzBJc3JSVDBMNGdEVTBaZ0FtYlFZOEtMRUZ0TE52X0lnU3c?oc=5>

## HEADWINDS

### General Mills (GIS) Stock Seems About Right On Its 38% Slide
- Summary: General Mills (GIS) Stock Seems About Right On Its 38% Slide
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxOSHV0OTVXbmVEVk56cFpiTFMxQkQ5cktwREVEbC04c2hwdGRRNi1qMTJlZzdpaFVDZzJyMnZjMHFuWkZLYzdXVVY0OF9MdkZ0S0dyc1I2NVRBQ2FFSFo3dHFYcnRwNEw0R1EtM3lXVzkyQ0VsRi02MlJKQnVvdWlmdzJOT19XajgtRjVfbUw3SzRHaTNKdWNRSEtR?oc=5>

### General Mills (NYSE:GIS) Stock Falls 2.6% - Here's What Happened
- Summary: General Mills (NYSE:GIS) Stock Falls 2.6% - Here's What Happened
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxOQkFZdjFhZXl2bTYzMXRCZ2p6dlI2ajQ4U0NKS0d4U05JT3R0OURaSU52ZzIydDJhWTRfNl84RDNmTjhYRTEtQkdnWlk1TDdRNEVyY1lCRWtQYjVreFl6ekJiOThSTVI2c2k3VnFlMnhqbVk2Q3JJR1BFMVdGTHZnSXd4OVVtcW9sSE9TZ0ZLXzFOXzRDUEVaTG1BYXhuQlU4aHRLWTdobGVrSHctS0JqZEtzcEplZ2Nt?oc=5>

### General Mills (NYSE:GIS) Shares Down 2.3% - What's Next?
- Summary: General Mills (NYSE:GIS) Shares Down 2.3% - What's Next?
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxPYm9PY0NHVnlSQ2Y2TFg2dnIxVjV5VGxoNkhoY0ZibTV5ZFg4bzVrWkplaXZMdy14cUYwdEhBVWk4WTJoVGh6ODNNUTU1WDBtSTJxM1lfUWo4Tmt3U3M3dGZ2VFotVnBSeXFnaHowbEd0RWZmb040YnBPYlc4Uy03azM4QzhrM0JsN1VrYVJDdlRUNHJ3ajZ6SHJBVGRsdGJPUDByY1NBLTMtMThE?oc=5>

### General Mills (NYSE:GIS) Stock Falls 1.6% - Here's Why
- Summary: General Mills (NYSE:GIS) Stock Falls 1.6% - Here's Why
- Date: 2026-10-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxPSndhN1M5MzdTRVNDaU9QTWFpc2N4X0lJOG9VUzlnLUhWZjNoclQ1MUl5Q1Nhb3RsLV9mN0dJV1plZ1Vwa3VUdjFzRGtxcDgwdjRZenQxZEdtMVJFQW5oTS1NblVseWR3OXVuSmNyam1TUE5iSGpvbklIYnRpZFFFOWNZY01rZkFXYUxpR05QNm1FeUpUdWdCQzgwaWIzNkFYMlR1ZTMzdTJyNXM?oc=5>

### General Mills (GIS): Buy, Sell, or Hold Post Q3 Earnings?
- Summary: Analyst guidance on whether to buy, sell, or hold GIS shares following Q3 earnings release.
- Date: 2026-10-20 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxNNDRncUZFR1VXdGd5WXJFZFNSaWduaHBQRUR0S1BvUl9fN01FMkkxWkNqRVhJLU9KSUlSZktkU1pFUWc3REJVRzYyZUt2VklpaEc1ay0teFlCVVdCdDJndENGaC1Kem5tM3ZZcVpUTTVRNm5ieUVnSVZuaFVEMGVqZW1DVmVNdWtpbHB2THNkOUZSb0NCYkE?oc=5>

## CATALYSTS

### General Mills Stock Is Down 30%, and Wall Street Analysts Keep Cutting Their Price Targets. Here's Why History Says They're Missing the Bigger Picture.
- Summary: General Mills Stock Is Down 30%, and Wall Street Analysts Keep Cutting Their Price Targets. Here's Why History Says They're Missing the Bigger Picture.
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxPM0E2YW1vN0tDaC1Oc3dsa2x4MVJILWhBbGdIV0xuNjgxV2NKblpXN08yU0tsNkZOX1NVT2k3TG5OUkFVWlRvcW9KVFZTQlA2WldtZE9iZ0l4SnhLWWNFYzBrTlYzODgwWnF1aFF2YWZyUk9HekxRSkltNnoxWjAxX0Z3MFVQNkljMHdBZGpadjRkR1M2V0ZOTQ?oc=5>

### General Mills, Inc. $GIS Stock Sold by Quadrant Capital Group LLC
- Summary: General Mills, Inc. $GIS Stock Sold by Quadrant Capital Group LLC
- Date: 2026-10-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxNREFTTFpiYjV2N3AzSFNBVEJ4aVhNSGJDbmx0ckEyUF80eUN5RzlVejE2TU5zZnMxekpHeFQ4bEtlbVNkZzJMNzg3ZVJVSHQ0a2dCSkM5Qkp2UUx4WmpXVHQzNVg2XzZWMFBfWHR5b05SMjg5dF85aS1QZWZUNHA5dWhBVGZlSmkwMkM1dW1XQWFFZFc2TlZjUUFUdVZpUmV2dVJhMm1mVmpON2l5STZYekRPdHJYQXJvRW5SbHhrS08?oc=5>

### General Mills, Inc. (GIS) - What Are Analysts Saying About This Stock?
- Summary: General Mills, Inc. (GIS) - What Are Analysts Saying About This Stock?
- Date: 2026-10-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixgFBVV95cUxPMFVPLXFVcGJ4b3BQb0Z5THJ4Z3hFcllvWjRIY3V6NE4zM2ZGR1dUbXpveTFmdk5JckNwOTVTZEw0b1NGUWM1aHRZRktmLUcxblhoeEhTTHlzUHdGY2NxMzBkajEwOHJKVS0zSjFPZWRUZDMyU2N5UE5aNVJmOWF0aXNpT1cyREJBOGZkY0V1aWRVTDFld3RQY2RsWTJUMlFnSVJnWFViQ3M0eGdxalBkdXpwY1hack9NS0ozNjJRZDZtNVlZOUE?oc=5>

### General Mills (GIS) After Debt Tenders And Dividend Hold Is The Stock Still Undervalued
- Summary: General Mills (GIS) After Debt Tenders And Dividend Hold Is The Stock Still Undervalued
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2gFBVV95cUxQMEZxQnp0aXlpMndXMFVub3M1NFJnMXJyNjJJbkt3Yk9ETGlia2RWdGxIYjVFNGVrdVFfdVd0OVl4eGtxRGVZUEgtU1JkRV9CZGhOR0xQcV9KNF93X3JFX1NpeDBzRTJPRVp4MzY0SmhDcWNab2xYaGtBYlJiemNBTXMzRURLU1U4NmVLdTJrV3dXNUx6amtQVFBrZ2Z1dkNJUVZXMnk3WUpVRWVuRFo4X1lqZmZSdXlxalBDc0dzMGkwazNKSGRaSWg3QXJYUDc5QW1GcU96Tl9nd9IB3wFBVV95cUxPem9Pa3ViWXU0WUlRY2VyMTdseWJiNmgwbU9YU2FpSU1Nd2JPbXhVRmNBZktvVzd1WV9OaTlTeEJIdXFQUE1FVU9HdHVBRlczT0NCTzZVZlM1Mjh0ZVYwblF3TjNpUlF1UWRZZ3dyOTFwSF9IaXRNX1RJYW1LRXBDMEpDUFJYRG1RaHAzdlhVcWwtck05aWtvU3VXUVd5dmt6RkNqZWIwSkR3U3hrRERxUkE2TzJ2X0dSbExhcEZyRmlLUmNDYU9hYUMtd2lEczFjb2FwQ3VIaVBpQW13VmRr?oc=5>

### General Mills, Inc. $GIS Stock: Cyndeo Wealth Partners LLC Reduces Holdings
- Summary: General Mills, Inc. $GIS Stock: Cyndeo Wealth Partners LLC Reduces Holdings
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizAFBVV95cUxPV0tPYzlvQVp1WTFmUG1tT0REd1cwNkhEVzdxTnZMWVVscm9Eem1VTF9MUVNYNnl3cTF3ZEQzWFNQaG9LSVVfbkl3b2lUWGlBazc4bWo3dGdJN2ZuV0pqMjJwWVFfWTFlbGltTHRicm1TcjZ3VVpBRUZONFVXTzJKMTRGQkFXUU14TFlzN1NuaHlrd0ZBMFZycFYwQ0ZaR1BJekNnLUtCNHR2di1Qc1JTaEhtblRfVnotb1JibWlBM2kzYk0xZnBJVW54Zmo?oc=5>

### Why General Mills (GIS) Stock Is Up Today
- Summary: Explains factors driving today's rise in GIS stock price.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMif0FVX3lxTE9LT3o4SFlxbzZjNzRrRlloQ0Y1SGxpR0dJTTVvdVhMSnV1QmpHRGNwcHVKOVM1Q2gxcGw4T0tYQ0twcWMxcHozeFBUYzE4V3E2eTFQdTlrNmdnWWN0UGFHVFNmc0pSWmRPbG1zZzdNcFZoTXMxMFZNSU5hV3J1eG8?oc=5>

### General Mills (GIS) Launches EPIC Sticks, Is The Stock Still Cheap?
- Summary: Announces EPIC Sticks launch and questions stock valuation.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQdWVHS2FZd2dTM1U4UkdzdGFmM1AwWVFpNDJwZFA2WmUwN1U4X1d0aTkxN2ZEYU9CMndUY1VpajZVbU5wNjUxM0hkcHdqT1QwSElQLWZfdDUwZTY2aVhmcnc2eEwybWlvaldSMFRLbkpWZkhvSm14VzhTbmk1TVlQX3Z4S3hLMDk4Q05WeTNzZW1zY0tGRFNjUWI5cGQ?oc=5>

### General Mills (GIS) Stock Looks Reasonably Priced For Now
- Summary: Analyst suggests current price is fair, no immediate upside.
- Date: 2026-10-23 | Impact: low | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi0wFBVV95cUxOaVExbjV1YWNRalAyS2NtY2NTV3NPTzVCUGYwUmFsNWMwRUFMUUxLRkxBRzNQdXk4eFpaWjZPUk1xbzlxWTJ6THhlWlJULTk0Z2VmcHpqcjR0Q3ZJczFYbXZRTXU0UzVPWG9HMm5kUE5VNDc4Q0tFRjNrajV2Y1F4bVJRWHdQc1RUb1A0SU9PcHVsSnFxVDQzUFU2Tl9wRWJPSUFRRkF2MzNkRHZNd251a2JicjN0THQxRTd5VjFKQ24tenpwdDc4Z2dOenpfRVhoNFY40gHYAUFVX3lxTE44clVSWVp3eVlJYlNJcGlwR0I0ZWlqVFV2dGVVUThPb1ltV3JUNGFwaDNqNzRzVldPMHZQYkEzSGl4MDJtQUwybmNyT0p5SWZSUjFpaDkweGFuUUl3MldHTXI1ZVBMa0Y3QWI1bDlid2EtOENuOXl5WUhTdlhHaTBwdUtuLVBkZ0s0b0ZnVU1iWlpNVFVJSEM5TkQtUXBmZ1g3MmhJeElEa3VKU1pyN0V4WWh1SU1iTXJfODRTbV8yeFRUZ3dncVBRUDlyLXhzeWxteENZRThOVQ?oc=5>

### Despite Structural Challenges, General Mills' Valuation And 7.1% Yield Stand Out (Upgrade)
- Summary: Analyst upgrade highlights strong valuation and yield.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxNdW1xa3dCaEVrVzBscUpYZWRPR3U4QmFmZWtqT3M4ODVLdU43Q3lFWS1NcC0xdWF4ZnE5OU9SbFIway1wd0R0MmNtQ0NURnlraE1sQWRQbUFaVDRtbkhvbFI0OWRxQVRoYUZ3Uk9URnRwMzlQdm10dTVkTHdGSWpEZ0l0Rk9aTy1uTWFVYUVkYWxSTVNNeHEyMkR5T3A4djdCRElGSkFScVNMZWdmbDdMSWZibzZLallzUHRmcmdpY2ZXTVNFUTNN?oc=5>

### General Mills, Inc. $GIS Stock Holdings Lessened by Crossmark Global Holdings Inc.
- Summary: Crossmark Global Holdings reduced its stake in General Mills, indicating a change in shareholder composition.
- Date: 2026-10-26 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxPTDdqU3RscVlpMDFoWDBPcV9DUjEtT3RTclVuM2ROUF9MeDBZZmtDTUVodjFFcHpfVXpBNlU3VnlXdEJyVERzNHRoN1pWWDdTcjYtWFlUR0txYnh6SE5LQ3JzSEluay1Ocnc4Y242TWJuVlNiZzJoQXRDVzRiaFlPY0pOeEh2eURiUFFYOUVTbFBIRlYyOUxiUkdtaWM4cTEyRUt5T05iSGdhQjVkanctZG5iNkRpdTNrcVlFWDNoWXFDczBxUThFdVFsYmo1Wmh4X2VVSDdn?oc=5>

## RISKS

### General Mills, Inc. $GIS Stock: Sumitomo Mitsui DS Asset Management Company Ltd Trims Position
- Summary: Major shareholder reduces stake, indicating potential concern.
- Date: 2026-10-23 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi5gFBVV95cUxNYzBDNkk5UTVjRXJWektBR29LREZRRXdueFdNTzg3emdEVHU4Rk9YbFUyazZRaWNEdGRRcG1uOUNyN1ZnRC1Fa0lNYkVFdkRSNlhhN29XQ1pNS2xfbWpHbXM5elFaNDJrZmo2eWVjR01MVjhfbWJhVDM5Tzd5ZjRTelkxMlZBSF9hbWhJUk5JZTVaTWNhYWkzVklSUGJQampsc3lqaTE5NFBFR3dCbGZoM1pSM0lpbE93b3d3ZVZZdlBjWkw3YkhoUERINzAwSk5YTWJvaU1OYkhNb2syUlloMGphRmNOQQ?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **GIS** | **N/A** | **2.42** | **9.14** | **-2.80** | **18,018,957,312.00 USD** | **-24.01** |
| KHC | N/A | 0.81 | 8.33 | -1.40 | 29,325,420,544.00 USD | 4.65 |
| CPB | 15.75 | 1.60 | 8.34 | -7.90 | 6,152,581,120.00 USD | -29.04 |
| SJM | 60.11 | 2.39 | 9.12 | 5.00 | 13,741,733,888.00 USD | 31.13 |

Peers fetched as_of: 2026-10-26; GIS reuses existing data (market data as_of: 2026-10-26); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-09-23
- Next expected earnings: 2026-12-23 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-26

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-09-23
- Revenue (latest available single quarter): 4,389,500,000.00 USD; period 2026-06-01/2026-08-30; fiscal year/reporting period 2027/Q1
- Net income (latest available single quarter): 397,000,000.00 USD; period 2026-06-01/2026-08-30; fiscal year/reporting period 2027/Q1
- SEC link: https://www.sec.gov/Archives/edgar/data/40704/000162828026063201/gis-20260830.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiugFBVV95cUxQTHFaU0laTzlvaXB4LUl1MDhnSURnb2lTY0QyOFRnajhPVDJ5X3M1RTh4UXRLdzJ0bkZLTUp5eTFHNzdHZWJGbnFlOXIyRi16LTZBZEpldUNpWlVsN3FXMWVmRFRSU1BiRnk0SEtMRUhlWlpCZXc2RUdoNnhFMVEwVS1UQXNhQ2FoTXEzSmsxUVJrMXpvM0ZYYzBJc3JSVDBMNGdEVTBaZ0FtYlFZOEtMRUZ0TE52X0lnU3c?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxOSHV0OTVXbmVEVk56cFpiTFMxQkQ5cktwREVEbC04c2hwdGRRNi1qMTJlZzdpaFVDZzJyMnZjMHFuWkZLYzdXVVY0OF9MdkZ0S0dyc1I2NVRBQ2FFSFo3dHFYcnRwNEw0R1EtM3lXVzkyQ0VsRi02MlJKQnVvdWlmdzJOT19XajgtRjVfbUw3SzRHaTNKdWNRSEtR?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxOQkFZdjFhZXl2bTYzMXRCZ2p6dlI2ajQ4U0NKS0d4U05JT3R0OURaSU52ZzIydDJhWTRfNl84RDNmTjhYRTEtQkdnWlk1TDdRNEVyY1lCRWtQYjVreFl6ekJiOThSTVI2c2k3VnFlMnhqbVk2Q3JJR1BFMVdGTHZnSXd4OVVtcW9sSE9TZ0ZLXzFOXzRDUEVaTG1BYXhuQlU4aHRLWTdobGVrSHctS0JqZEtzcEplZ2Nt?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxPYm9PY0NHVnlSQ2Y2TFg2dnIxVjV5VGxoNkhoY0ZibTV5ZFg4bzVrWkplaXZMdy14cUYwdEhBVWk4WTJoVGh6ODNNUTU1WDBtSTJxM1lfUWo4Tmt3U3M3dGZ2VFotVnBSeXFnaHowbEd0RWZmb040YnBPYlc4Uy03azM4QzhrM0JsN1VrYVJDdlRUNHJ3ajZ6SHJBVGRsdGJPUDByY1NBLTMtMThE?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxPSndhN1M5MzdTRVNDaU9QTWFpc2N4X0lJOG9VUzlnLUhWZjNoclQ1MUl5Q1Nhb3RsLV9mN0dJV1plZ1Vwa3VUdjFzRGtxcDgwdjRZenQxZEdtMVJFQW5oTS1NblVseWR3OXVuSmNyam1TUE5iSGpvbklIYnRpZFFFOWNZY01rZkFXYUxpR05QNm1FeUpUdWdCQzgwaWIzNkFYMlR1ZTMzdTJyNXM?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxNNDRncUZFR1VXdGd5WXJFZFNSaWduaHBQRUR0S1BvUl9fN01FMkkxWkNqRVhJLU9KSUlSZktkU1pFUWc3REJVRzYyZUt2VklpaEc1ay0teFlCVVdCdDJndENGaC1Kem5tM3ZZcVpUTTVRNm5ieUVnSVZuaFVEMGVqZW1DVmVNdWtpbHB2THNkOUZSb0NCYkE?oc=5
- https://news.google.com/rss/articles/CBMi0AFBVV95cUxOVzdWcHAxTmoyVVo0ZlpJY0dmdkhUcGRyMENNZUc4MmwycmRjd2ZRSEtxQnFaMFBTN1VTampaczVOWFZ1SDBJYXRaTGNhbldXQUE2czRMbFQ1Wm5lbDlvTVlGY3dTS3ZMUHh5cDNZOExSdS02NF9NZmZOLWxpMFJRQnMzOTl1elZkcEt5cFNXbDdCLUU5bnh1NjBrS3h0U1MxdGVKWGs2dWxaX0Juc1JtTWJQZEZyYTFXREhSenFYSzBoWUpwYU5kWXFXTlU5SF9K?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxPM0E2YW1vN0tDaC1Oc3dsa2x4MVJILWhBbGdIV0xuNjgxV2NKblpXN08yU0tsNkZOX1NVT2k3TG5OUkFVWlRvcW9KVFZTQlA2WldtZE9iZ0l4SnhLWWNFYzBrTlYzODgwWnF1aFF2YWZyUk9HekxRSkltNnoxWjAxX0Z3MFVQNkljMHdBZGpadjRkR1M2V0ZOTQ?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxOVFZrLVBPNE9IR2RyeF9GRWRFNi1fOGNkVnFMeFBQWURqUFk0aDJ6dVZ3bzZrZmFaVXVfOVUwY245WXQyMS1wVTQ1U3VPeFZGOTA3S0w3SW5hQ01TUl9yRzVYZzh0M0xwWGlKemF2M0RFZ3VGZ3MzSmZoWWhmdXBZY3BxYVBMODNBTTBYZ19qZWUyZWVDTmM0?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxNREFTTFpiYjV2N3AzSFNBVEJ4aVhNSGJDbmx0ckEyUF80eUN5RzlVejE2TU5zZnMxekpHeFQ4bEtlbVNkZzJMNzg3ZVJVSHQ0a2dCSkM5Qkp2UUx4WmpXVHQzNVg2XzZWMFBfWHR5b05SMjg5dF85aS1QZWZUNHA5dWhBVGZlSmkwMkM1dW1XQWFFZFc2TlZjUUFUdVZpUmV2dVJhMm1mVmpON2l5STZYekRPdHJYQXJvRW5SbHhrS08?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxPMFVPLXFVcGJ4b3BQb0Z5THJ4Z3hFcllvWjRIY3V6NE4zM2ZGR1dUbXpveTFmdk5JckNwOTVTZEw0b1NGUWM1aHRZRktmLUcxblhoeEhTTHlzUHdGY2NxMzBkajEwOHJKVS0zSjFPZWRUZDMyU2N5UE5aNVJmOWF0aXNpT1cyREJBOGZkY0V1aWRVTDFld3RQY2RsWTJUMlFnSVJnWFViQ3M0eGdxalBkdXpwY1hack9NS0ozNjJRZDZtNVlZOUE?oc=5
- https://news.google.com/rss/articles/CBMi2gFBVV95cUxQMEZxQnp0aXlpMndXMFVub3M1NFJnMXJyNjJJbkt3Yk9ETGlia2RWdGxIYjVFNGVrdVFfdVd0OVl4eGtxRGVZUEgtU1JkRV9CZGhOR0xQcV9KNF93X3JFX1NpeDBzRTJPRVp4MzY0SmhDcWNab2xYaGtBYlJiemNBTXMzRURLU1U4NmVLdTJrV3dXNUx6amtQVFBrZ2Z1dkNJUVZXMnk3WUpVRWVuRFo4X1lqZmZSdXlxalBDc0dzMGkwazNKSGRaSWg3QXJYUDc5QW1GcU96Tl9nd9IB3wFBVV95cUxPem9Pa3ViWXU0WUlRY2VyMTdseWJiNmgwbU9YU2FpSU1Nd2JPbXhVRmNBZktvVzd1WV9OaTlTeEJIdXFQUE1FVU9HdHVBRlczT0NCTzZVZlM1Mjh0ZVYwblF3TjNpUlF1UWRZZ3dyOTFwSF9IaXRNX1RJYW1LRXBDMEpDUFJYRG1RaHAzdlhVcWwtck05aWtvU3VXUVd5dmt6RkNqZWIwSkR3U3hrRERxUkE2TzJ2X0dSbExhcEZyRmlLUmNDYU9hYUMtd2lEczFjb2FwQ3VIaVBpQW13VmRr?oc=5
- https://news.google.com/rss/articles/CBMizAFBVV95cUxPV0tPYzlvQVp1WTFmUG1tT0REd1cwNkhEVzdxTnZMWVVscm9Eem1VTF9MUVNYNnl3cTF3ZEQzWFNQaG9LSVVfbkl3b2lUWGlBazc4bWo3dGdJN2ZuV0pqMjJwWVFfWTFlbGltTHRicm1TcjZ3VVpBRUZONFVXTzJKMTRGQkFXUU14TFlzN1NuaHlrd0ZBMFZycFYwQ0ZaR1BJekNnLUtCNHR2di1Qc1JTaEhtblRfVnotb1JibWlBM2kzYk0xZnBJVW54Zmo?oc=5
- https://news.google.com/rss/articles/CBMif0FVX3lxTE9LT3o4SFlxbzZjNzRrRlloQ0Y1SGxpR0dJTTVvdVhMSnV1QmpHRGNwcHVKOVM1Q2gxcGw4T0tYQ0twcWMxcHozeFBUYzE4V3E2eTFQdTlrNmdnWWN0UGFHVFNmc0pSWmRPbG1zZzdNcFZoTXMxMFZNSU5hV3J1eG8?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQdWVHS2FZd2dTM1U4UkdzdGFmM1AwWVFpNDJwZFA2WmUwN1U4X1d0aTkxN2ZEYU9CMndUY1VpajZVbU5wNjUxM0hkcHdqT1QwSElQLWZfdDUwZTY2aVhmcnc2eEwybWlvaldSMFRLbkpWZkhvSm14VzhTbmk1TVlQX3Z4S3hLMDk4Q05WeTNzZW1zY0tGRFNjUWI5cGQ?oc=5
- https://news.google.com/rss/articles/CBMi0wFBVV95cUxOaVExbjV1YWNRalAyS2NtY2NTV3NPTzVCUGYwUmFsNWMwRUFMUUxLRkxBRzNQdXk4eFpaWjZPUk1xbzlxWTJ6THhlWlJULTk0Z2VmcHpqcjR0Q3ZJczFYbXZRTXU0UzVPWG9HMm5kUE5VNDc4Q0tFRjNrajV2Y1F4bVJRWHdQc1RUb1A0SU9PcHVsSnFxVDQzUFU2Tl9wRWJPSUFRRkF2MzNkRHZNd251a2JicjN0THQxRTd5VjFKQ24tenpwdDc4Z2dOenpfRVhoNFY40gHYAUFVX3lxTE44clVSWVp3eVlJYlNJcGlwR0I0ZWlqVFV2dGVVUThPb1ltV3JUNGFwaDNqNzRzVldPMHZQYkEzSGl4MDJtQUwybmNyT0p5SWZSUjFpaDkweGFuUUl3MldHTXI1ZVBMa0Y3QWI1bDlid2EtOENuOXl5WUhTdlhHaTBwdUtuLVBkZ0s0b0ZnVU1iWlpNVFVJSEM5TkQtUXBmZ1g3MmhJeElEa3VKU1pyN0V4WWh1SU1iTXJfODRTbV8yeFRUZ3dncVBRUDlyLXhzeWxteENZRThOVQ?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxNdW1xa3dCaEVrVzBscUpYZWRPR3U4QmFmZWtqT3M4ODVLdU43Q3lFWS1NcC0xdWF4ZnE5OU9SbFIway1wd0R0MmNtQ0NURnlraE1sQWRQbUFaVDRtbkhvbFI0OWRxQVRoYUZ3Uk9URnRwMzlQdm10dTVkTHdGSWpEZ0l0Rk9aTy1uTWFVYUVkYWxSTVNNeHEyMkR5T3A4djdCRElGSkFScVNMZWdmbDdMSWZibzZLallzUHRmcmdpY2ZXTVNFUTNN?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxPTDdqU3RscVlpMDFoWDBPcV9DUjEtT3RTclVuM2ROUF9MeDBZZmtDTUVodjFFcHpfVXpBNlU3VnlXdEJyVERzNHRoN1pWWDdTcjYtWFlUR0txYnh6SE5LQ3JzSEluay1Ocnc4Y242TWJuVlNiZzJoQXRDVzRiaFlPY0pOeEh2eURiUFFYOUVTbFBIRlYyOUxiUkdtaWM4cTEyRUt5T05iSGdhQjVkanctZG5iNkRpdTNrcVlFWDNoWXFDczBxUThFdVFsYmo1Wmh4X2VVSDdn?oc=5
- https://news.google.com/rss/articles/CBMi5gFBVV95cUxNYzBDNkk5UTVjRXJWektBR29LREZRRXdueFdNTzg3emdEVHU4Rk9YbFUyazZRaWNEdGRRcG1uOUNyN1ZnRC1Fa0lNYkVFdkRSNlhhN29XQ1pNS2xfbWpHbXM5elFaNDJrZmo2eWVjR01MVjhfbWJhVDM5Tzd5ZjRTelkxMlZBSF9hbWhJUk5JZTVaTWNhYWkzVklSUGJQampsc3lqaTE5NFBFR3dCbGZoM1pSM0lpbE93b3d3ZVZZdlBjWkw3YkhoUERINzAwSk5YTWJvaU1OYkhNb2syUlloMGphRmNOQQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
