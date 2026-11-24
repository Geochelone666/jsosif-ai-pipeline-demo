# NVDA Intelligence Report

- ticker: **NVDA**
- Report as_of: **2026-11-23**
- Market data as_of: **2026-11-23**
- Quant sources: https://finance.yahoo.com/quote/NVDA/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NVDA/key-statistics/
- AI analysis snapshot as_of: **2026-11-23**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-24T08:20:09.702694+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 4, 'ai': 16, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **1** exact headline/source/date matches; prior report **20261123T053847Z-45053549/NVDA** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 8 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 68.0%; oldest publication 2026-11-21

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 165.0500 |
| Return 1D (%) | 31.4825 |
| Return 1W (%) | 5.7064 |
| Return 1M (%) | -21.7624 |
| Return YTD (%) | -11.2943 |
| Return 1Y (%) | -7.5104 |
| Annualized volatility (%) | 51.9743 |
| Beta vs SPY | 2.3920 |
| Max drawdown (%) | -47.5297 |
| Sharpe (rf=0) | 0.0540 |
| Downside deviation (rf=0, %) | 31.3785 |
| Sortino (rf=0) | 0.0895 |
| Historical VaR 95% (1D, %) | 4.2484 |
| Historical ES 95% (1D, %) | 5.8772 |
| Correlation vs SPY | 0.6892 |
| Tracking error vs SPY (%) | 43.0434 |
| P/E (trailing) | 17.73 |
| P/B | 14.92 |
| EV/EBITDA | 16.11 |
| Revenue growth (%) | 103.20 |
| Forward P/E (estimate) | 9.94 |
| Gross margin (%) | 74.92 |
| Operating margin (%) | 66.08 |
| Return on equity (%) | 117.36 |
| Free cash flow yield (%) | 2.49 |
| MA50 | 206.0822 |
| Close vs MA50 (%) | -19.9106 |
| MA200 | 202.9857 |
| Close vs MA200 (%) | -18.6889 |
| RSI (14, Wilder) | 42.8744 |
| MACD (12,26) | -18.0722 |
| MACD signal (9) | -15.7729 |
| MACD histogram | -2.2994 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NVDA': 288, 'SPY': 288}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 165.0500 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 31.4825 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 5.7064 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -21.7624 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -11.2943 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -7.5104 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 51.9743 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 31.3785 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.0895 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.2484 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.8772 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6892 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 43.0434 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 2.3920 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -47.5297 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.0540 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 9.9396 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 74.9210 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 66.0820 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 117.3640 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.4901 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 17.7282 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 42.8744 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -2.2994 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -19.9106 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -18.6889 -> Clearly below the moving-average trend level.

## TAILWINDS

### Nvidia Poised For Biggest One Day Gain In History Of Stock Market As Jensen Huang Returns
- Summary: Nvidia Poised For Biggest One Day Gain In History Of Stock Market As Jensen Huang Returns
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxPdUllNzZaazk0eDdDc2xuZUx1c1lxczdlR3BITFJ3ZG43OTZlcjlmTUM0NS1BYnVKOEc1N3pZYzJiY0d6UGIzb1VYdDF1TkYwei04cTBVaHFwRjZhWW5FN25kNlZoSFlkWHFla2ZRLWptTThxTUNpYThmeXZvMmViZ3VreVRCbURNSGxjanFJLTI1WWV2LW9NdVpR?oc=5>

### NVIDIA Jumps 28% as Jensen Huang Reportedly Reinstated as CEO; Intel Rallies 13%, AMD Gains 7%
- Summary: NVIDIA Jumps 28% as Jensen Huang Reportedly Reinstated as CEO; Intel Rallies 13%, AMD Gains 7%
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxPZGtJcFpjWlhPdkg1NW5YRlQzZ3dBdXpKX2pGSXZQamRwdXhGYWN1WDctR1hDYlFRN05XVU1LcVZmQTFDY3dnbFpONnRGUzZEalFycHZKM2c0UEFBU210c2U4bVk2Qzg0eFRLVDhBZTE2S3R1QlJ6TWJQUXpGaGotNGExTG5SWlBrQWVFUGNHSnliS3oyX0tr?oc=5>

### Amazon Makes AI Chip Move; Stock Climbs Alongside Nvidia Relief Rally
- Summary: Amazon's AI chip launch boosts market sentiment, supporting Nvidia's rally.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihAFBVV95cUxONGNWcWFkazVXMUhqYkdVOXN3UUJFbVppRWw4RUZaVFA1ci1TLWlXUk5xOG1pUWJ0X1VKZEN4SVRpYUpzbVlsSnVhVW1fM3dDdGp3NHFiMXVraHVvUXZBOUExZy0yVWdscE5wZWNUd256d1U0bzh6b0Uwell0NXRqekVVOEo?oc=5>

### Jensen Huang reinstated as Nvidia CEO. Stock skyrockets 31%
- Summary: Jensen Huang returns as CEO, boosting investor confidence and driving a 31% stock surge.
- Date: 2026-11-23 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMibEFVX3lxTE9McnlkOWZjTEROTXNrdGgtS19oWmNzcTFQSFBwUUdmbzBkOVFYQWY4R2JSdloweTM0V0F1a1gyZExpV2ktdC0zcTExdGxlbVgzaFRGTFR0cjViMTZkeTdyQzMtQ0JYMmJPQUNReNIBckFVX3lxTE00WXNRTHAtbXVYeEpKUVFhaExjRzNtSVg4VWphUk04cWIxOUpRY0VQeWNtdHdCT0Y4dXRZc3pqbDRQWkZ0UFk3S3NVRTFXazFOY3pyLWgwcVZFcWFMZUQ0b2Qzd1dDQjZWV0lGd2tvaDhiQQ?oc=5>

### Tech stocks see monster rally after Jensen Huang returns as Nvidia CEO
- Summary: Nvidia’s CEO return sparks a broad tech rally, lifting market sentiment.
- Date: 2026-11-23 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMibEFVX3lxTFBJVmhYR3dCSjgwTWZWTGJGUGE1S0NKbkxQUDhzODNkU2lSRFU3dk5LeENVUjI0RS0zYnJ6LWFCMFZZaEpUWmdzSUFwQzRzOFM4VWNpSU9JTHo2c3o5U3NXcUpkNEdoSFdtbkdoatIBckFVX3lxTE9TTG1paDhMMG81cTlpOHdVOVRUMmVhTnRMOXR2MFd3ZHBvY3BTX1d6NVBZOVV4cDdVQ1dfRUs5YW95cmpieTdNZzlkWmFqUVNUR05EOGQ0SEk5a1RMZDdBaU1VdGlkdXN1cXFCM2RwN1d4QQ?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Nvidia (NVDA) Stock Looks Below Fair Value After Recent Turmoil
- Summary: Nvidia (NVDA) Stock Looks Below Fair Value After Recent Turmoil
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxQbUpxbnpVNGpTNThJa3dsbWR4R3cyQ3hWbVFydFJ6bW10dldabWVTU3hPMGRoZlFhczNXZWgzbHppOVBIZzNKb1VTNWZ0dFd3S3lHdTJFRkdJOUo2N0FIQ1I3VnVPLVdwSWdmS1NsbWVmVW9WVXdrOFI5TnV2a1JFb0dfVWRjUWxMMUhwT0FQdUdRMEFvVFBjTjZR?oc=5>

### NVDA Stock Sees Biggest Fall In 22 Months, But Top Analyst Says Nvidia’s AI Boom Isn’t Over Yet — Here Are 5 Reasons Why
- Summary: NVDA Stock Sees Biggest Fall In 22 Months, But Top Analyst Says Nvidia’s AI Boom Isn’t Over Yet — Here Are 5 Reasons Why
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQbDBWLTd5T3R4NFVNLWI0Vm9nWEJmd1FHdDdqLUdfWjJJdXBOWFU1d2x1Nk1NUjNCVW5OT1IzY0hLUnRIbkIxZXBsd1pNMV9MQUppQ2twZmRQT2EwT3Q3V0I2dVVLX1EyOEN6cjdSOTJHWmkydGJ6bFpfb2VaN295ekRxWDM3SXhqcVdOZlhoVzlma3VSOERiaA?oc=5>

### Nvidia stock soars as Trump makes U-turn on Jensen Huang, cheers Huang's return as CEO
- Summary: Jensen Huang returns as CEO, boosting stock sharply.
- Date: 2026-11-23 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi4gFBVV95cUxNRXVUaE5oREVIRVpXeWxtcDNPVzl2aklWQXhtQkFCdlUxdDBiNEtjN3hoRFZlRVdENWp2cHFvWnpSOVJtcTN3bjlKYzZPOXhzMUZkVmRqLVlrOHVWTGYzSFA2alhrdFFnRnVEdHZoYnRkTGRzaGRKSWtYMUZZamkwbzdOdDY4R0FNaFhYY0RkMUowX1Y3eEZsRHhsakpzY01KVjZ6eU1nR0I2STVsd2pNMXJhSkFIcmJCU0diemtINklXaFdOd3R6Y3N2WHBKNWxmLW50QTlYOGtVRmxQY1MzRlFB?oc=5>

### Nvidia: Crisis Prices Won't Last (Rating Upgrade) (NASDAQ:NVDA)
- Summary: Analyst upgrades Nvidia rating, signaling confidence.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxPbC1nNWxqaUtsZ3oyOVFoOFJQd0ozS0VvZ1FWZmVmRTNPdm1sZXhCUk9fYTNPdkxXTk9mMGtEX3FqSzM2TXY1dUdLa1hUZ21MOEpBbU5XekQ5U1IyeE5RYWo4WlNJTHNDVERLOFdVLTJ4X2V5X19CV3VDOW90RkJWZ3VGbVFQNTNXaXZoMy1qUQ?oc=5>

### Is the AI Rally Safe With Jensen Huang Back at Nvidia—Here’s What Wall Street Thinks
- Summary: Wall Street assesses AI rally risk with Huang back.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxQeGVqQi1qQ0dvVlVDWXlNVUNSMklhbzdZWFBRWnZMbVlXVkpDZjZxd3dpNm4tM1RSLVF3QjFETHljS05TbHRDWXBXdlFCTlVyZXpGU3lWV21UU0YwU01VT0N5RGl5ZUxieVBUM0xQZkV5cTgzR3JZOXFLNjJPdzdZWHQxdVZDc0dHS2RudXFnU1pLNFpTU19SNWMtWkwtcmF4T1NIbXNaOUUwbkR5RVB6UDFuRTdua2xPejJHR3l1NnJkZXZ2?oc=5>

### 5 things to consider as Nvidia restores Jensen Huang as the company's leader
- Summary: Key factors for Huang’s leadership restoration highlighted.
- Date: 2026-11-23 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxPQW5hN25aQlFRM1RvY3RTdXpkTlhrNXVmVm90dDVWejNPd1ZrOV9XNXVUNkxSRk52ZEpLZ2RMdUczRUNvQXQyUWI0a25rcU5BUG94OHRCMWN1Vi14SGVCMGg2Sjlwc1lNV2hLNVliZkxwa0g5WVp6Sm9aRmVSY1BYVkV6S2g0c3VSQm1YY2wtUENDWDlwYlc3eUM1MUthWUdjLU9iVnFxaXdaTzhaWmlJNjl3RVo5S0p3MjNNSTlIZ2FfUmNuX01MNHBXRy1hY19BQzlrUUpn?oc=5>

### Nvidia gains nearly $1T as Trump says nobody could 'revive the stock like it's being revived'
- Summary: Trump’s comment boosts Nvidia’s market value, driving a near $1T increase.
- Date: 2026-11-23 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi3wFBVV95cUxQR1l0YldHVjdWbVRmRXVkTWxOQTN0bWlZTU9rbkRMaS1MRlh6eW9zS2hESkNxVEdWODFIM3VLNkRsYmxCcUdEWGNLdlUtRU8zN3FUNGlPY3c4aWVPV0tiQ1lJN3E5VmlINjg3ZmhjdUNmZS1oZnFHenhNTXRZLWpNWWVHaDE2N0pIZURQVWlxWURBZnNSaE9YMTlyOTc3UzN0QmFWX296RzZJbEJqYnNjQjJfWVZ5MlBFNm9GbXVqMl9iTDVjSEQ1SDVfT0ZFTFhBYzE4dVNnS2JObHlmMFY4?oc=5>

### Nvidia soars 31% as board reinstates Jensen Huang as CEO, chip stocks jump
- Summary: Board reinstates Huang, spurring a 31% surge in Nvidia shares and broader chip stocks.
- Date: 2026-11-23 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiyAFBVV95cUxPQXQxeWtYZkw0VGdES0pzRTNhc1h5aW9VNWNkRU0zeVE0QzBBYk12VmM1cjFkWEJSUmwzQndzZHVJaGF3bGdvSGI1UEtwWXBzZ1NuZExiejR2bkFsVl9ZWl9hS1FEekV3TS1ZV1hnZnNSVU9ybGRJTkF5b193dXVPLUs1ZDRJMWY3X25UYV8wNEU0RTliTXk4NFNDUElmWjZhSFJXVy1MSmlsbXZEajY5MEJoVmpBWEt1a3g0SFRFalpZSmdXWjVZYw?oc=5>

### Nvidia’s Jensen Huang Is Back. Is the Stock a Buy?
- Summary: Huang’s return prompts debate on Nvidia’s investment potential.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNM29tbkMyLS1Hb0dtRnRPRTg3blN4c0NiXzhhbkQySUJsbk9tel9tUHdIZ0QwVE8zYVFEQ3BFZEo2NTRrd2ZwTnAzVFEwU0ppVjBGajZ3bVNzNnJFdnhKZmlOYUNNUXZOb0dqX19ldzFpNWpQUEprTGR4emt4d09WckV5Ylh2LTBKMWNSSHJ3U09KWkdaRVdqeG1Udw?oc=5>

### This Is the Number That Could Change Nvidia Stock’s Outlook for 2027
- Summary: Key metric highlighted as potential game-changer for Nvidia’s 2027 outlook.
- Date: 2026-11-23 | Impact: medium | Horizon: long | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxPYUFzdWlhc1k3ME5hc29jdHM1bS1LX1BFSHNvVVdyVlRva1BqT3NHcXo2cjF5SWdLaUsyay13ZWt6Y0diRDZLWXdzY2RPUk02dHotZWxGbzNzQ3N2UGhoX2lVak1ZQ1p4VlVzaEg2SUhWWWViTEpyWDRVR2tRMkpxX0EybW5NQTZtRDZhWHdsUEFwdlhFNHp1cTF6bXR2dw?oc=5>

### Should You Buy Nvidia Stock Now That Jensen Huang Is Back in Charge?
- Summary: Analysts weigh buying Nvidia after Huang’s return.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxNRG9RS1Y1Nm5CdV9IVjFxNE9tOWtmOVQ5VmZqdFppVElLTVdOeXkxU181RHVDYzlVLTJhMUpaWFdDRGFMNDM3MWozdmE5NlZmRmhxbjhPckF2RHN2aVMxUkt5VmhobXEwM1JtYkhXaUliUU9hYkNUNXJYNTdSdVFWTUpxRW5oSEFWUlg5Q2xSWUc4cEI4U0Fv?oc=5>

### Jensen Huang Is Back. Is It Safe To Buy Nvidia Stock Now?
- Summary: Jensen Huang's return signals leadership stability for Nvidia.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxQU21TSnZ2X1RYWUQzajVqVGpZZ2dQa2NJbGVuaXB2YzNLcy1fazdZaUFGcHdzQnJSOG1SYU9IT3lOSDFiT3I3TEZKN3JKMGRoZmxWLUozV1h0YlY2SE8tdkVLR2hWckhwdXpmbEtHb3UxVHVPTUNjaXJGSFZDQ1gzTUpVSWplMjhiZEl2cW54Um5pSWUtX3c?oc=5>

### Nvidia Stock Soars as Jensen Huang Returns as CEO - NVIDIA (NASDAQ:NVDA)
- Summary: CEO return drives Nvidia stock surge.
- Date: 2026-11-23 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxPZllDMTMtZUpUWGpHV05FSGlaN3JQeE5lNU9LUldOTVR1ZFJaclFvMU5QUzc2MkJVNjdKRzZMbkdWU1JmSC1hR1ZyMUhVbFFvbUNvUFBmWWVXb0o4ckZZQmQ0OFF3U0J1a25JaFdteXhRYUpRZ1N1OUE5WHlPNTFYQTlNMHJqQWdPNTB4T2MxSzhZLWE5dTIxZU9MYzRGeUhlZVNKRVZUZHNvM1NlWVYw?oc=5>

### Michael Burry on Nvidia Board? ‘Big Short’ Investor Jokes He’d ‘Volunteer’ as NVDA Stock Sinks 40%
- Summary: Rumors of Burry joining Nvidia board amid a 40% stock decline raise concerns.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxPUFJtZzBWMnNaVnFSNUhiUkdyYkYwcVA4U05SWnMzLTBDQjRvYTVTRzlaOGxjWFIzUVhPYlhxVmJRUk85RF8xaHlqVi1XdTFIZkNUMDhCVFdpTzBSWmRpNWJpRjRaM3laMDA4Y2RkdG1aZVFPOEJOSU1XYkhSU0xRMkpqWElPMG9zYURiaEY5WWJqME5jVjBNS0Yycw?oc=5>

## RISKS

### Nvidia stock extends $2.7 trillion rout as SEC probe reportedly investigates its accounting
- Summary: SEC investigation into accounting practices threatens stock stability.
- Date: 2026-11-21 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi3wFBVV95cUxQS25iVW9uNHFsc3lYdkNPRTJyTUhYcWRVbjhOZlR4QUpLZGs4RkE0d1lSLTEtN2x6N0ZxZnlZdE9KaTQxeS1TbWRFaGFpd0hGc0ZKWmF5OEVRdnFDX1NNWFlBTl9rdVRUVFlxSVRIelpPNmluWVdUVElhQzh1NWtjemJaUnlhRnJ2N3Q2dDNVYlhVYWtXbkswbXhYLWdiOHE0V1dkQ2xjNjFsTlpEQ0hzRDBja0RqV0VFX0FZaXdKRVZ2RHdGVUUtS2VzanJrTkhiSVcxeGVCRXNlUUhSVWJ3?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NVDA** | **17.73** | **14.92** | **16.11** | **103.20** | **3,985,462,263,808.00 USD** | **-7.51** |
| AMD | 96.89 | 10.87 | 66.15 | 44.70 | 750,506,016,768.00 USD | 122.52 |
| AVGO | 40.04 | 15.02 | 29.32 | 85.50 | 1,496,771,592,192.00 USD | -7.15 |
| INTC | N/A | 2.76 | 17.24 | 20.90 | 317,092,888,576.00 USD | 72.93 |

Peers fetched as_of: 2026-11-23; NVDA reuses existing data (market data as_of: 2026-11-23); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-17
- Next expected earnings: 2027-02-24 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-23

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

- https://news.google.com/rss/articles/CBMimgFBVV95cUxPdUllNzZaazk0eDdDc2xuZUx1c1lxczdlR3BITFJ3ZG43OTZlcjlmTUM0NS1BYnVKOEc1N3pZYzJiY0d6UGIzb1VYdDF1TkYwei04cTBVaHFwRjZhWW5FN25kNlZoSFlkWHFla2ZRLWptTThxTUNpYThmeXZvMmViZ3VreVRCbURNSGxjanFJLTI1WWV2LW9NdVpR?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxPZGtJcFpjWlhPdkg1NW5YRlQzZ3dBdXpKX2pGSXZQamRwdXhGYWN1WDctR1hDYlFRN05XVU1LcVZmQTFDY3dnbFpONnRGUzZEalFycHZKM2c0UEFBU210c2U4bVk2Qzg0eFRLVDhBZTE2S3R1QlJ6TWJQUXpGaGotNGExTG5SWlBrQWVFUGNHSnliS3oyX0tr?oc=5
- https://news.google.com/rss/articles/CBMihAFBVV95cUxONGNWcWFkazVXMUhqYkdVOXN3UUJFbVppRWw4RUZaVFA1ci1TLWlXUk5xOG1pUWJ0X1VKZEN4SVRpYUpzbVlsSnVhVW1fM3dDdGp3NHFiMXVraHVvUXZBOUExZy0yVWdscE5wZWNUd256d1U0bzh6b0Uwell0NXRqekVVOEo?oc=5
- https://news.google.com/rss/articles/CBMibEFVX3lxTE9McnlkOWZjTEROTXNrdGgtS19oWmNzcTFQSFBwUUdmbzBkOVFYQWY4R2JSdloweTM0V0F1a1gyZExpV2ktdC0zcTExdGxlbVgzaFRGTFR0cjViMTZkeTdyQzMtQ0JYMmJPQUNReNIBckFVX3lxTE00WXNRTHAtbXVYeEpKUVFhaExjRzNtSVg4VWphUk04cWIxOUpRY0VQeWNtdHdCT0Y4dXRZc3pqbDRQWkZ0UFk3S3NVRTFXazFOY3pyLWgwcVZFcWFMZUQ0b2Qzd1dDQjZWV0lGd2tvaDhiQQ?oc=5
- https://news.google.com/rss/articles/CBMibEFVX3lxTFBJVmhYR3dCSjgwTWZWTGJGUGE1S0NKbkxQUDhzODNkU2lSRFU3dk5LeENVUjI0RS0zYnJ6LWFCMFZZaEpUWmdzSUFwQzRzOFM4VWNpSU9JTHo2c3o5U3NXcUpkNEdoSFdtbkdoatIBckFVX3lxTE9TTG1paDhMMG81cTlpOHdVOVRUMmVhTnRMOXR2MFd3ZHBvY3BTX1d6NVBZOVV4cDdVQ1dfRUs5YW95cmpieTdNZzlkWmFqUVNUR05EOGQ0SEk5a1RMZDdBaU1VdGlkdXN1cXFCM2RwN1d4QQ?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxQbUpxbnpVNGpTNThJa3dsbWR4R3cyQ3hWbVFydFJ6bW10dldabWVTU3hPMGRoZlFhczNXZWgzbHppOVBIZzNKb1VTNWZ0dFd3S3lHdTJFRkdJOUo2N0FIQ1I3VnVPLVdwSWdmS1NsbWVmVW9WVXdrOFI5TnV2a1JFb0dfVWRjUWxMMUhwT0FQdUdRMEFvVFBjTjZR?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQbDBWLTd5T3R4NFVNLWI0Vm9nWEJmd1FHdDdqLUdfWjJJdXBOWFU1d2x1Nk1NUjNCVW5OT1IzY0hLUnRIbkIxZXBsd1pNMV9MQUppQ2twZmRQT2EwT3Q3V0I2dVVLX1EyOEN6cjdSOTJHWmkydGJ6bFpfb2VaN295ekRxWDM3SXhqcVdOZlhoVzlma3VSOERiaA?oc=5
- https://news.google.com/rss/articles/CBMi4gFBVV95cUxNRXVUaE5oREVIRVpXeWxtcDNPVzl2aklWQXhtQkFCdlUxdDBiNEtjN3hoRFZlRVdENWp2cHFvWnpSOVJtcTN3bjlKYzZPOXhzMUZkVmRqLVlrOHVWTGYzSFA2alhrdFFnRnVEdHZoYnRkTGRzaGRKSWtYMUZZamkwbzdOdDY4R0FNaFhYY0RkMUowX1Y3eEZsRHhsakpzY01KVjZ6eU1nR0I2STVsd2pNMXJhSkFIcmJCU0diemtINklXaFdOd3R6Y3N2WHBKNWxmLW50QTlYOGtVRmxQY1MzRlFB?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxPbC1nNWxqaUtsZ3oyOVFoOFJQd0ozS0VvZ1FWZmVmRTNPdm1sZXhCUk9fYTNPdkxXTk9mMGtEX3FqSzM2TXY1dUdLa1hUZ21MOEpBbU5XekQ5U1IyeE5RYWo4WlNJTHNDVERLOFdVLTJ4X2V5X19CV3VDOW90RkJWZ3VGbVFQNTNXaXZoMy1qUQ?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxQeGVqQi1qQ0dvVlVDWXlNVUNSMklhbzdZWFBRWnZMbVlXVkpDZjZxd3dpNm4tM1RSLVF3QjFETHljS05TbHRDWXBXdlFCTlVyZXpGU3lWV21UU0YwU01VT0N5RGl5ZUxieVBUM0xQZkV5cTgzR3JZOXFLNjJPdzdZWHQxdVZDc0dHS2RudXFnU1pLNFpTU19SNWMtWkwtcmF4T1NIbXNaOUUwbkR5RVB6UDFuRTdua2xPejJHR3l1NnJkZXZ2?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxPQW5hN25aQlFRM1RvY3RTdXpkTlhrNXVmVm90dDVWejNPd1ZrOV9XNXVUNkxSRk52ZEpLZ2RMdUczRUNvQXQyUWI0a25rcU5BUG94OHRCMWN1Vi14SGVCMGg2Sjlwc1lNV2hLNVliZkxwa0g5WVp6Sm9aRmVSY1BYVkV6S2g0c3VSQm1YY2wtUENDWDlwYlc3eUM1MUthWUdjLU9iVnFxaXdaTzhaWmlJNjl3RVo5S0p3MjNNSTlIZ2FfUmNuX01MNHBXRy1hY19BQzlrUUpn?oc=5
- https://news.google.com/rss/articles/CBMi3wFBVV95cUxQR1l0YldHVjdWbVRmRXVkTWxOQTN0bWlZTU9rbkRMaS1MRlh6eW9zS2hESkNxVEdWODFIM3VLNkRsYmxCcUdEWGNLdlUtRU8zN3FUNGlPY3c4aWVPV0tiQ1lJN3E5VmlINjg3ZmhjdUNmZS1oZnFHenhNTXRZLWpNWWVHaDE2N0pIZURQVWlxWURBZnNSaE9YMTlyOTc3UzN0QmFWX296RzZJbEJqYnNjQjJfWVZ5MlBFNm9GbXVqMl9iTDVjSEQ1SDVfT0ZFTFhBYzE4dVNnS2JObHlmMFY4?oc=5
- https://news.google.com/rss/articles/CBMiyAFBVV95cUxPQXQxeWtYZkw0VGdES0pzRTNhc1h5aW9VNWNkRU0zeVE0QzBBYk12VmM1cjFkWEJSUmwzQndzZHVJaGF3bGdvSGI1UEtwWXBzZ1NuZExiejR2bkFsVl9ZWl9hS1FEekV3TS1ZV1hnZnNSVU9ybGRJTkF5b193dXVPLUs1ZDRJMWY3X25UYV8wNEU0RTliTXk4NFNDUElmWjZhSFJXVy1MSmlsbXZEajY5MEJoVmpBWEt1a3g0SFRFalpZSmdXWjVZYw?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNM29tbkMyLS1Hb0dtRnRPRTg3blN4c0NiXzhhbkQySUJsbk9tel9tUHdIZ0QwVE8zYVFEQ3BFZEo2NTRrd2ZwTnAzVFEwU0ppVjBGajZ3bVNzNnJFdnhKZmlOYUNNUXZOb0dqX19ldzFpNWpQUEprTGR4emt4d09WckV5Ylh2LTBKMWNSSHJ3U09KWkdaRVdqeG1Udw?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxPYUFzdWlhc1k3ME5hc29jdHM1bS1LX1BFSHNvVVdyVlRva1BqT3NHcXo2cjF5SWdLaUsyay13ZWt6Y0diRDZLWXdzY2RPUk02dHotZWxGbzNzQ3N2UGhoX2lVak1ZQ1p4VlVzaEg2SUhWWWViTEpyWDRVR2tRMkpxX0EybW5NQTZtRDZhWHdsUEFwdlhFNHp1cTF6bXR2dw?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxNRG9RS1Y1Nm5CdV9IVjFxNE9tOWtmOVQ5VmZqdFppVElLTVdOeXkxU181RHVDYzlVLTJhMUpaWFdDRGFMNDM3MWozdmE5NlZmRmhxbjhPckF2RHN2aVMxUkt5VmhobXEwM1JtYkhXaUliUU9hYkNUNXJYNTdSdVFWTUpxRW5oSEFWUlg5Q2xSWUc4cEI4U0Fv?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxQU21TSnZ2X1RYWUQzajVqVGpZZ2dQa2NJbGVuaXB2YzNLcy1fazdZaUFGcHdzQnJSOG1SYU9IT3lOSDFiT3I3TEZKN3JKMGRoZmxWLUozV1h0YlY2SE8tdkVLR2hWckhwdXpmbEtHb3UxVHVPTUNjaXJGSFZDQ1gzTUpVSWplMjhiZEl2cW54Um5pSWUtX3c?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxPZllDMTMtZUpUWGpHV05FSGlaN3JQeE5lNU9LUldOTVR1ZFJaclFvMU5QUzc2MkJVNjdKRzZMbkdWU1JmSC1hR1ZyMUhVbFFvbUNvUFBmWWVXb0o4ckZZQmQ0OFF3U0J1a25JaFdteXhRYUpRZ1N1OUE5WHlPNTFYQTlNMHJqQWdPNTB4T2MxSzhZLWE5dTIxZU9MYzRGeUhlZVNKRVZUZHNvM1NlWVYw?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxPUFJtZzBWMnNaVnFSNUhiUkdyYkYwcVA4U05SWnMzLTBDQjRvYTVTRzlaOGxjWFIzUVhPYlhxVmJRUk85RF8xaHlqVi1XdTFIZkNUMDhCVFdpTzBSWmRpNWJpRjRaM3laMDA4Y2RkdG1aZVFPOEJOSU1XYkhSU0xRMkpqWElPMG9zYURiaEY5WWJqME5jVjBNS0Yycw?oc=5
- https://news.google.com/rss/articles/CBMi3wFBVV95cUxQS25iVW9uNHFsc3lYdkNPRTJyTUhYcWRVbjhOZlR4QUpLZGs4RkE0d1lSLTEtN2x6N0ZxZnlZdE9KaTQxeS1TbWRFaGFpd0hGc0ZKWmF5OEVRdnFDX1NNWFlBTl9rdVRUVFlxSVRIelpPNmluWVdUVElhQzh1NWtjemJaUnlhRnJ2N3Q2dDNVYlhVYWtXbkswbXhYLWdiOHE0V1dkQ2xjNjFsTlpEQ0hzRDBja0RqV0VFX0FZaXdKRVZ2RHdGVUUtS2VzanJrTkhiSVcxeGVCRXNlUUhSVWJ3?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
