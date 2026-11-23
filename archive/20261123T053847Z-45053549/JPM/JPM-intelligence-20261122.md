# JPM Intelligence Report

- ticker: **JPM**
- Report as_of: **2026-11-22**
- Market data as_of: **2026-11-20**
- Quant sources: https://finance.yahoo.com/quote/JPM/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/JPM/key-statistics/
- AI analysis snapshot as_of: **2026-11-22**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-23T05:43:00.940870+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 2, 'ai': 18, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **13** exact headline/source/date matches; prior report **20261122T045655Z-f5ef568d/JPM** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 12 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 32.0%; oldest publication 2026-11-16

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 310.5300 |
| Return 1D (%) | -3.0260 |
| Return 1W (%) | -10.3007 |
| Return 1M (%) | -7.3764 |
| Return YTD (%) | -1.7719 |
| Return 1Y (%) | 6.0764 |
| Annualized volatility (%) | 23.0788 |
| Beta vs SPY | 0.7968 |
| Max drawdown (%) | -15.4717 |
| Sharpe (rf=0) | 0.3719 |
| Downside deviation (rf=0, %) | 16.7436 |
| Sortino (rf=0) | 0.5126 |
| Historical VaR 95% (1D, %) | 2.4552 |
| Historical ES 95% (1D, %) | 3.3659 |
| Correlation vs SPY | 0.4935 |
| Tracking error vs SPY (%) | 20.2814 |
| P/E (trailing) | 13.03 |
| P/B | 2.35 |
| EV/EBITDA | N/A |
| Revenue growth (%) | 10.20 |
| Forward P/E (estimate) | 12.14 |
| Gross margin (%) | 0.00 |
| Operating margin (%) | 44.79 |
| Return on equity (%) | 18.01 |
| Free cash flow yield (%) | N/A |
| MA50 | 336.8079 |
| Close vs MA50 (%) | -7.8020 |
| MA200 | 322.8815 |
| Close vs MA200 (%) | -3.8254 |
| RSI (14, Wilder) | 30.7457 |
| MACD (12,26) | -4.0046 |
| MACD signal (9) | -0.9551 |
| MACD histogram | -3.0494 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'JPM': 287, 'SPY': 287}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 310.5300 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -3.0260 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -10.3007 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -7.3764 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -1.7719 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 6.0764 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 23.0788 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 16.7436 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.5126 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.4552 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.3659 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4935 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 20.2814 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.7968 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -15.4717 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.3719 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 12.1429 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 0.0000 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 44.7880 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 18.0130 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 13.0256 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 30.7457 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -3.0494 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -7.8020 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -3.8254 -> Slightly below the moving-average trend level.

## TAILWINDS

### A property insurer puts $250 million into J.P. Morgan's new global stock fund
- Summary: Insurer invests $250M in JPM's global stock fund, supporting capital growth.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxQQTkyOEx3VGhEZDlSckZqUl85UzY1NmthY1p2V2dKWnBlTDNiM0FNczFCaENucVZTdWszNTU4QzNaTC1xT0w2LXhZakVGbXplQ2V2c0lyOTFrYWM1OWdvS3lxZ3lHeWFNX3FBTjcxVGJmTmFoNE9vc1hmMTNFY3ZXbFRYZGIxSjIxemJmMXlUbnJ3UExQc3dDUENDMmxlS0xXdjVTYjJ3TnViOTNvVW0wVE9GMUxsYlVfTnFnLWlR?oc=5>

### 105,134 JPMorgan Chase & Co. $JPM Shares Bought by Private Advisor Group LLC
- Summary: Private advisor buys 105,134 JPM shares, indicating confidence in the bank.
- Date: 2026-11-22 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizAFBVV95cUxNOGtpX1VWZm9ELWJOcFdFZ29pajNkSmJoWjBRNHZkVVdpQXJ5WE9wMlFtdDh0eFV1NlhKajZ4cXl0aHJuTEZPMFdNVVdqelduN0RxN2NnTkpxUjljNDN5RmlWZU5MS3ZXNEVvS1dPTC1HTHFOVjdRTkhqcTd4TDNwZDgtMTR3ZW9XMHk5N1V0TFBrRVV6ajgzUVVCWHZfQUJtdzBITWh2MHdlUVZrZnE2NEJwbGdoeC1kckdRUWlBYjVGWmhlYUVhblRFN1k?oc=5>

### Boston Partners Purchases 103,238 Shares of JPMorgan Chase & Co. $JPM
- Summary: Boston Partners acquires 103,238 JPM shares, reflecting bullish stance.
- Date: 2026-11-22 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxPdEx5TGFUN2VKY2VaZGxTaDdMVlAtTjlFbWtQRmN3M3JsN3lUT1Mya0NBYUJvd3lCZzdiMlIzLVJBdU83NUVMVERwaE1oVHBHYkxoc19ZNDZjbkFrcWxnUW5lTEhoaDB4c2E5bHNwZjE4MUpta1lnZDlmQ1ZJeXAzVElzcUo0VGJiZVg2Nm9RZVhHNzNvQTA2YWlfeVMwOC1YQ2JrYkJwZVVZR0oxMW9zVUo0TVJfOUpPVVFOX0Vnb1dna2s?oc=5>

## HEADWINDS

### JPMorgan Stock Slides: What's Going On?
- Summary: JPM stock is declining, raising concerns about its short-term performance.
- Date: 2026-11-17 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxPY25wTkZqdFZDWF93OFdXcFRsSmJWM0oybzR3b3N1OHZ1bURYVjlFZkoySHhQVkxrNjluVTBqQzNIQ2pGWGQwN0ZheXhvbk8yT18xQzYtaDhnSVJYTVA4VVQ4eUNkZDFzNDc5TW1fMXZsMzRGR0FnelpUaVZLeEhkNnpPd2RVLTNncEY4SGluTVA5dE5IbnF3aFFFdFFSQQ?oc=5>

### Third-party vendors of JPMorgan Chase, Visa, Mastercard reportedly faced cyberattacks (JPM:NYSE)
- Summary: Cyberattacks on third‑party vendors threaten JPM operations.
- Date: 2026-11-19 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxNS1daVEN0SlZtVGhOUjZxSTI3TmhybWJYN3dIMkdOVUtYck1LQjhyRUNsMkdhMXo5dWFtUWRxUnVROFloQzI1Y3ZNRWpURFZwakNWM041ekhjTTc2c0JJN1FjRDdST3E4OUdWSk1SdERfWW00aUp6QVl0Q1dHTnNYMFlXQ3JNd0szM2hvSGpyOXM2dlFfR2NwV1VpVXRaS21FLUxzQ19DOHJkNXpNV3V2Uw?oc=5>

### JPMorgan Chase & Co. (NYSE:JPM) Stock Price Breaks Below Two Hundred Day Moving Average - Should You Sell?
- Summary: JPM stock falls below 200‑day moving average, signaling potential downside pressure.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi7wFBVV95cUxOMVlnOTBybnpvZDFpOUdlNnV3eG1vWm5yNjk3QThKandiQ2xSUDRKR3VsQWxGRUZIOWJqajRtMGhlY3Vmd0ZlTEtGRE5oM1VZQnBHeUhNaFVPVHZ5UmxaX2VUR3o5SUpNb2dBdHAyeW9pVE5tWGRZSklfQnRQZFlMMjIwQk5nRUd6Q3RNaEZwekdPQi1wVGJRU0JJZVVPUUl1dk85ZnF4YTNNTm43QW1pMEZMcXNhS1Rfbzh6VkR1VlVTRE1LQzZHREktU2xNWmRFamJYbXhHd25Wdkl0QUlIdjJiMXE4M25oME9YbGVxVQ?oc=5>

### JPMorgan Chase (JPM) Says Vendor Cyberattack Exposed Customer Data
- Summary: Vendor cyberattack exposed customer data, raising security concerns.
- Date: 2026-11-22 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxNcGZsSnc2NEFiS2tDdllhMmJ2V243b2lyQ0pUdkQ4SUpEVjlZakFtTlg3bUxVanlBWWh2RnFEd3dyaXBtOS1Eb2xmbDdWQWk1SWVoay1RS1FCQ2VYdXhzLUQzc0lCUGZySWdQY3EtOFVKc0FPV1h5dTd1MXFieW9sUkFPa1VST3NwZ3NKM0d2U0U3Rm1sOUpuOF9fV0E5WW0wenp5N1hTNmZqU1NCRTNNRGZReXFTTWtNQUQ3bmFmNjMxRnZj0gHKAUFVX3lxTE9lUXloUGRvaXRMdVhyc0NNVnVGYmVaVERkdGpLbEFCUGQ1dG9Rc3IxZUZVNHFOZWJYZmNXMUxudFc2dEZHYk5hY0lDSG9QRk92LWszOUhyeHl0YnljYzhtRlhiS0pLSTdlUkNVWkhfTDZQVlBIS0tjSzFxd0hCYVV0blM1OEg0NTZQWFJlc0FZaXlRN2ptOEZBR0hiUi1xSmZ0MVozUkpKa3BaM1VRZy1IZkpqdkFocmE5MlRreENpSjdUN0hONjFYeHc?oc=5>

### JPMorgan Chase & Co. (NYSE:JPM) Stock Price Down 2.3% - Should You Sell?
- Summary: Stock price fell 2.3%, indicating a short‑term decline.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxOeTYyMXg5NERqWVdFXzBTTEZFOVpsUHZKRHZkSEFNUUhiLU11djRUbmtRU2VxU2F6b2lZczBGZFZld2g5UDRYZWUyUkV2Qkl2VjBlOTVpNFpiVjdNQlg2eWVXNW9sYmJRNkhWc0J2NUN5NGVlQlh6NDdfQ2VMYVRxUTlJMDNsRXVzX2IwOGxvbERtTHV0ajlmWThOazdGS1NYa051b043TzdxRjdsZlMySll4dXdKdWt3M1NtNGtlUQ?oc=5>

### JPMorgan Chase (NYSE:JPM) Faces Pressure As Momentum Weakens
- Summary: Momentum weakening suggests a short‑term headwind for the bank.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxPaGpTV3RVUkt6dUhNY2hjSnI3V25VOWRzVUVoTVU0X1pwS001YUJFc19JempUaWV3SXNMeTctajlfVlFQajlzN0NWY3ROTjE3cEJOWnJyYlA2RjJlaWNhOE1iYTZWdm94NjdFYzFSRkFyZXJPTjhPWXNvRG5xRlNMT3pCc19KanhxcWZIRTRVS3JJNGoyRWJJMVlYd2FwampHLWpwSA?oc=5>

### JPMorgan Chase (JPM) Stock Price Prediction: JPMorgan slips back toward support as analysts stay constructive but momentum softens
- Summary: Analysts predict a dip toward support, signaling a short‑term headwind.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQZndENWhIclE5Z2ZvZDhzSmt6WHVLR3dkMkNCcC0yV2VqTVRmY3h5OUxEOWhOd3F1UkFJMGtEeE9JWnRNZmNWRkhQMmFZdVRMMkROcC1pNndpZ19hQzlNQVYtUnlFY0xXZTFPell1Smw4ZVhBNnpLYlJqaXZrQy1SR2w3bFNfT2trZjZCVjY2UlVQaG1CMWthZ29JTUQ?oc=5>

### Will JPMorgan Chase (NYSE:JPM) Keep Its Edge As Sentiment Shifts?
- Summary: Questioning the bank’s edge amid shifting sentiment indicates a potential short‑term headwind.
- Date: 2026-11-22 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxQQkdQdDNvYWVmZkpicDRZVkh3aUdqeXZmbGF5dFpMdTJpN25lMzRHT180Sk1JcG4yaW93RUxyV1RWTjJ1V1IzNlJhdl91Z2ZKUzB5WW1HZm9nR0hwYWI1ejdQWlVEdDFqbkQ3aXlBRzlQd3RBdkFsTjdxT1FINDBmSzdOM0hyV0h6RWtBcUFsQnVWNWlqLXFnc19DSVVYckVFU0FFYmV3ckw?oc=5>

### JPMorgan Chase & Co. (NYSE:JPM) Shares Down 1.9% - Should You Sell?
- Summary: Shares of JPM fell 1.9%, prompting sell‑side commentary. The decline reflects short‑term market volatility and investor sentiment.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxPSjl5aTd3Xzd3c2J5MnZnUkFPc1lBLWt1d1lPTFI4cHJ6cHJLaE1ORVJoRTQ1N016ZGtLRGpvVUs3dE41cXV3ZTd6N0pqOXhTSUFaajBkLTRCb0pYM05LZGRhcTA5ZW9OaEpoYmhEZDlhMndtVk9YT0huZ18tWjhvREUzZjdnREJBNTM1WThlWGdqNWM0Mm1hS24tekxkTGUtM3VBTDc4VkkzaDBYUjBhX0c1ZzlMUVF5?oc=5>

## CATALYSTS

### JPMorgan Chase (JPM) Receives a Rating Update from a Top Analyst
- Summary: JPMorgan Chase (JPM) Receives a Rating Update from a Top Analyst
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi3wFBVV95cUxOWjcyUFpnWTZMQVFNdFcwaUhIak9LQnczREtpTjNLLTlYblJvZWp2ZFhWWS02VDdmZTFKMHVDcFFkaEk2S2RwYlFLVzV0ODkyUnNQeS1oeG52T0lSWXVnQk5rR3R1bThpYWVzVG1Dc0s3NkNhRmtHMzJBTUVyRHFyYzZ2dEJXcHVZRk5JVzdkeWN3ZDhyUU9HSWlUdjBZQTVaNTNIR1ZLcV9yM28tRUZmUmJ2UmRHeHBlaldQRXIzdnU4WnFnMy14RTFoNG5IWWJGM3ozNE01b3RISk8wM1RB?oc=5>

### JPMorgan Chase & Co. $JPM Stock Purchased by Bessemer Group Inc.
- Summary: JPMorgan Chase & Co. $JPM Stock Purchased by Bessemer Group Inc.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxNSlNkM3FYeXlxdDY1TXZKcDJlR1pJX2ZadGoyODNRQTNqMzkxUFNoLVBILVEzR3RhbURJVUd4eWo4NF9RNmlkeS12eVMyS0RZTnAtNFhBYlFiOGhsMlcyblc5WWRIRjZhMlpuYTZOcS1uRm5BcWdxY1VyQ1Iyc19Cek1EUWNtVm5ENUNpa3IxNjVSMnIxMmZhVkIwVl9tbU8yVGdrOHJuMmVKeHBEZTZheTl0V0ZRMEVHbDNyQw?oc=5>

### JPMorgan names Bregje de Best as next CFO, succeeding Barnum
- Summary: JPM appoints Bregje de Best as CFO, succeeding Barnum.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxOX0tJbXd0el94UVZKU2p6S21CdUVKUHRsWHlkajRucjlZZkt0SjRRdWFER3E1aWFNMFNQUTN5T3oxV2hKVmZuVFFuaVNUVFFUQnd6S0NCTUN0V0xweVRMT2VOYVoxeDR5aF9qem9hZ0RJamhPVDZhQ2tUREpucHBHWnZ6eGozRUxNUjJqSENtNTUyWDhramFOQWV1RldqNXczME5USE83cWYzMWQ5WXhqUnF0dw?oc=5>

### JPMorgan Chase announces CFO transition, confirms resolving 'technical issue' (JPM:NYSE)
- Summary: JPM confirms CFO transition and technical issue resolution.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxNbUgxQkh0ZkRTNW9FNlV6TElsVVdudTRKcG9GYlVrYnF4dFNsMVB1LU0wdGVobGxYLTFuSWtSOEVhZThSYy11Q3lJUmRZYWF3V2I3cndtb3plS25NMmtleUxNR21DcFRwajZqR0E1bXFYS253VjVwTUNMRnJyeUtjb3F2Ulpzd3BnVWY1MHdkR2xncGRxMndDQ0prcll2VE5ndlBPVGpFakZIdmlUTU9RRkxB?oc=5>

### AI Infrastructure Demand Might Change The Case For Investing In JPMorgan Chase Stock (JPM)
- Summary: Growing AI infrastructure demand could enhance JPM's investment appeal.
- Date: 2026-11-16 | Impact: medium | Horizon: medium | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxPalR2WVhHOTNiT3R5MUU4ZWtxaUs3UWxjbFA3Ylg2Ti1tWDJRaHl1YXRmRmVHcEcxQURvU2EtcVM5MFNlQTRzNUdGZWNWRU9mX2l5OVoyaVphektVRTR2R2tJa2dhbzRDMThOT3ZGVkZFRTN6UnpZcVd4bldYZTJNWjQyb3hyd05jQnhEM0pMODNOUnVxTUVWRW1WZ1p1bU1SU2RXVw?oc=5>

### Why Is JPMorgan Chase (JPM) Naming Bregje De Best As Its Next CFO?
- Summary: Appointment of Bregje De Best as CFO signals leadership change.
- Date: 2026-11-19 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxQU1ctTHZIMkJYenpSU2NxUHkxbGVHbzFaUEM1czlaVG5sN1F6VWpwbEpPd0NxTjFUUGlLc1ZVZDBLVGdEa21zTDRET195R29IM3U4TkdlWDFNWjlFeTBYZVM5aFVkM0prdGI4RWJUUUtrYm43a1BjdlFGSkpRRXJlbDlUbnpkSXl0NUJlcGp2aWZCR1k5eHFmOVB6VFgyTG10MWRqMXc1ajRMZ294ZUN4MUpJWnR1MXVmMUJHOG5GM09DbmZi0gHKAUFVX3lxTFB2Y1poVVNOaVk3cHE1eExtbW91cFQtQ3JmRXRoMVIxb3kxRVo5QXctNUJSNDl4dVFRejIzTndFMUVKd0hJMDZ4d2d1NG9sRktXUTdRc1A0d1psSkRaNWJuRUVEQm1VX1ZaRF8yMEN1MWVDTVQ0U1RtVWFEMDlCLWd5N3FvQWJreXFXaENUWENkYlM4ZWpkNlFFRnJrYzFJalhsdndERE1LUkNxeVQ0SWN0bGdCOWdpRWs5MjZiOUo3MzVLbDFPVktMN1E?oc=5>

### JPMorgan Chase (JPM) names its next CFO. Jeremy Barnum will become vice chairman.
- Summary: Appointment of new CFO and vice chairman signals leadership change.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxPLUo5Q1VwbWpnem5zNTdRZDhselFCQkMzQ3QybXE2ZktONndGVGxyNXM4RUdETFhRQ19DNWRKRFp4aXNWYzJMZ2hmTjBEdF9DWl9uM1k4UmwyeE5GaGxfTTFyMzJUaXpYMWsyQlRoQU9wXzhZUHNNLWdmR05jNVRyTG1icy1ROW51S0pXRVM4cGFzSENTTzU2ZnU1b3hnZVliSHlNTW5nSEk?oc=5>

## RISKS

### JPM: SEC Form FWP filed by JP Morgan Chase & Co.
- Summary: JPM filed a Form FWP with the SEC, indicating a regulatory filing that may affect compliance or operational oversight.
- Date: 2026-11-20 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxOYmVEU3hCOWtMa2E2SEFnQXp3M0ticXpjMm5zY2tPWHNNWGt0MTBncTFlbUh6VnJhRWpFazBLbU5Kd3RMSURiMWI5Z0N5WnFVbFI4cHlvTVZhQmU4U2tTSVVPa1MzWWtLUG9xdGsyWlBGaEFtYWxrNWloLWZ4VEpsSUdYempUSUdidjN3?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **JPM** | **13.03** | **2.35** | **N/A** | **10.20** | **824,646,434,816.00 USD** | **6.08** |
| BAC | 11.23 | 1.20 | N/A | 3.40 | 324,585,848,832.00 USD | -5.80 |
| C | 10.78 | 0.96 | N/A | 8.00 | 183,098,720,256.00 USD | 15.65 |
| WFC | 11.09 | 1.49 | N/A | 0.40 | 236,005,490,688.00 USD | -2.44 |

Peers fetched as_of: 2026-11-22; JPM reuses existing data (market data as_of: 2026-11-20); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-13
- Next expected earnings: 2027-01-14 (yfinance; expected dates may change)

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
- Filing date: 2026-11-03
- Revenue (latest available single quarter): 24,246,000,000.00 USD; period 2014-07-01/2014-09-30; fiscal year/reporting period 2014/Q3
- Net income (latest available single quarter): 15,305,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/19617/000162828026069523/jpm-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMivgFBVV95cUxQQTkyOEx3VGhEZDlSckZqUl85UzY1NmthY1p2V2dKWnBlTDNiM0FNczFCaENucVZTdWszNTU4QzNaTC1xT0w2LXhZakVGbXplQ2V2c0lyOTFrYWM1OWdvS3lxZ3lHeWFNX3FBTjcxVGJmTmFoNE9vc1hmMTNFY3ZXbFRYZGIxSjIxemJmMXlUbnJ3UExQc3dDUENDMmxlS0xXdjVTYjJ3TnViOTNvVW0wVE9GMUxsYlVfTnFnLWlR?oc=5
- https://news.google.com/rss/articles/CBMizAFBVV95cUxNOGtpX1VWZm9ELWJOcFdFZ29pajNkSmJoWjBRNHZkVVdpQXJ5WE9wMlFtdDh0eFV1NlhKajZ4cXl0aHJuTEZPMFdNVVdqelduN0RxN2NnTkpxUjljNDN5RmlWZU5MS3ZXNEVvS1dPTC1HTHFOVjdRTkhqcTd4TDNwZDgtMTR3ZW9XMHk5N1V0TFBrRVV6ajgzUVVCWHZfQUJtdzBITWh2MHdlUVZrZnE2NEJwbGdoeC1kckdRUWlBYjVGWmhlYUVhblRFN1k?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxPdEx5TGFUN2VKY2VaZGxTaDdMVlAtTjlFbWtQRmN3M3JsN3lUT1Mya0NBYUJvd3lCZzdiMlIzLVJBdU83NUVMVERwaE1oVHBHYkxoc19ZNDZjbkFrcWxnUW5lTEhoaDB4c2E5bHNwZjE4MUpta1lnZDlmQ1ZJeXAzVElzcUo0VGJiZVg2Nm9RZVhHNzNvQTA2YWlfeVMwOC1YQ2JrYkJwZVVZR0oxMW9zVUo0TVJfOUpPVVFOX0Vnb1dna2s?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxPY25wTkZqdFZDWF93OFdXcFRsSmJWM0oybzR3b3N1OHZ1bURYVjlFZkoySHhQVkxrNjluVTBqQzNIQ2pGWGQwN0ZheXhvbk8yT18xQzYtaDhnSVJYTVA4VVQ4eUNkZDFzNDc5TW1fMXZsMzRGR0FnelpUaVZLeEhkNnpPd2RVLTNncEY4SGluTVA5dE5IbnF3aFFFdFFSQQ?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxNS1daVEN0SlZtVGhOUjZxSTI3TmhybWJYN3dIMkdOVUtYck1LQjhyRUNsMkdhMXo5dWFtUWRxUnVROFloQzI1Y3ZNRWpURFZwakNWM041ekhjTTc2c0JJN1FjRDdST3E4OUdWSk1SdERfWW00aUp6QVl0Q1dHTnNYMFlXQ3JNd0szM2hvSGpyOXM2dlFfR2NwV1VpVXRaS21FLUxzQ19DOHJkNXpNV3V2Uw?oc=5
- https://news.google.com/rss/articles/CBMi7wFBVV95cUxOMVlnOTBybnpvZDFpOUdlNnV3eG1vWm5yNjk3QThKandiQ2xSUDRKR3VsQWxGRUZIOWJqajRtMGhlY3Vmd0ZlTEtGRE5oM1VZQnBHeUhNaFVPVHZ5UmxaX2VUR3o5SUpNb2dBdHAyeW9pVE5tWGRZSklfQnRQZFlMMjIwQk5nRUd6Q3RNaEZwekdPQi1wVGJRU0JJZVVPUUl1dk85ZnF4YTNNTm43QW1pMEZMcXNhS1Rfbzh6VkR1VlVTRE1LQzZHREktU2xNWmRFamJYbXhHd25Wdkl0QUlIdjJiMXE4M25oME9YbGVxVQ?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxNcGZsSnc2NEFiS2tDdllhMmJ2V243b2lyQ0pUdkQ4SUpEVjlZakFtTlg3bUxVanlBWWh2RnFEd3dyaXBtOS1Eb2xmbDdWQWk1SWVoay1RS1FCQ2VYdXhzLUQzc0lCUGZySWdQY3EtOFVKc0FPV1h5dTd1MXFieW9sUkFPa1VST3NwZ3NKM0d2U0U3Rm1sOUpuOF9fV0E5WW0wenp5N1hTNmZqU1NCRTNNRGZReXFTTWtNQUQ3bmFmNjMxRnZj0gHKAUFVX3lxTE9lUXloUGRvaXRMdVhyc0NNVnVGYmVaVERkdGpLbEFCUGQ1dG9Rc3IxZUZVNHFOZWJYZmNXMUxudFc2dEZHYk5hY0lDSG9QRk92LWszOUhyeHl0YnljYzhtRlhiS0pLSTdlUkNVWkhfTDZQVlBIS0tjSzFxd0hCYVV0blM1OEg0NTZQWFJlc0FZaXlRN2ptOEZBR0hiUi1xSmZ0MVozUkpKa3BaM1VRZy1IZkpqdkFocmE5MlRreENpSjdUN0hONjFYeHc?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxOeTYyMXg5NERqWVdFXzBTTEZFOVpsUHZKRHZkSEFNUUhiLU11djRUbmtRU2VxU2F6b2lZczBGZFZld2g5UDRYZWUyUkV2Qkl2VjBlOTVpNFpiVjdNQlg2eWVXNW9sYmJRNkhWc0J2NUN5NGVlQlh6NDdfQ2VMYVRxUTlJMDNsRXVzX2IwOGxvbERtTHV0ajlmWThOazdGS1NYa051b043TzdxRjdsZlMySll4dXdKdWt3M1NtNGtlUQ?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxPaGpTV3RVUkt6dUhNY2hjSnI3V25VOWRzVUVoTVU0X1pwS001YUJFc19JempUaWV3SXNMeTctajlfVlFQajlzN0NWY3ROTjE3cEJOWnJyYlA2RjJlaWNhOE1iYTZWdm94NjdFYzFSRkFyZXJPTjhPWXNvRG5xRlNMT3pCc19KanhxcWZIRTRVS3JJNGoyRWJJMVlYd2FwampHLWpwSA?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQZndENWhIclE5Z2ZvZDhzSmt6WHVLR3dkMkNCcC0yV2VqTVRmY3h5OUxEOWhOd3F1UkFJMGtEeE9JWnRNZmNWRkhQMmFZdVRMMkROcC1pNndpZ19hQzlNQVYtUnlFY0xXZTFPell1Smw4ZVhBNnpLYlJqaXZrQy1SR2w3bFNfT2trZjZCVjY2UlVQaG1CMWthZ29JTUQ?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxQQkdQdDNvYWVmZkpicDRZVkh3aUdqeXZmbGF5dFpMdTJpN25lMzRHT180Sk1JcG4yaW93RUxyV1RWTjJ1V1IzNlJhdl91Z2ZKUzB5WW1HZm9nR0hwYWI1ejdQWlVEdDFqbkQ3aXlBRzlQd3RBdkFsTjdxT1FINDBmSzdOM0hyV0h6RWtBcUFsQnVWNWlqLXFnc19DSVVYckVFU0FFYmV3ckw?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxPSjl5aTd3Xzd3c2J5MnZnUkFPc1lBLWt1d1lPTFI4cHJ6cHJLaE1ORVJoRTQ1N016ZGtLRGpvVUs3dE41cXV3ZTd6N0pqOXhTSUFaajBkLTRCb0pYM05LZGRhcTA5ZW9OaEpoYmhEZDlhMndtVk9YT0huZ18tWjhvREUzZjdnREJBNTM1WThlWGdqNWM0Mm1hS24tekxkTGUtM3VBTDc4VkkzaDBYUjBhX0c1ZzlMUVF5?oc=5
- https://news.google.com/rss/articles/CBMi3wFBVV95cUxOWjcyUFpnWTZMQVFNdFcwaUhIak9LQnczREtpTjNLLTlYblJvZWp2ZFhWWS02VDdmZTFKMHVDcFFkaEk2S2RwYlFLVzV0ODkyUnNQeS1oeG52T0lSWXVnQk5rR3R1bThpYWVzVG1Dc0s3NkNhRmtHMzJBTUVyRHFyYzZ2dEJXcHVZRk5JVzdkeWN3ZDhyUU9HSWlUdjBZQTVaNTNIR1ZLcV9yM28tRUZmUmJ2UmRHeHBlaldQRXIzdnU4WnFnMy14RTFoNG5IWWJGM3ozNE01b3RISk8wM1RB?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxNSlNkM3FYeXlxdDY1TXZKcDJlR1pJX2ZadGoyODNRQTNqMzkxUFNoLVBILVEzR3RhbURJVUd4eWo4NF9RNmlkeS12eVMyS0RZTnAtNFhBYlFiOGhsMlcyblc5WWRIRjZhMlpuYTZOcS1uRm5BcWdxY1VyQ1Iyc19Cek1EUWNtVm5ENUNpa3IxNjVSMnIxMmZhVkIwVl9tbU8yVGdrOHJuMmVKeHBEZTZheTl0V0ZRMEVHbDNyQw?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxOX0tJbXd0el94UVZKU2p6S21CdUVKUHRsWHlkajRucjlZZkt0SjRRdWFER3E1aWFNMFNQUTN5T3oxV2hKVmZuVFFuaVNUVFFUQnd6S0NCTUN0V0xweVRMT2VOYVoxeDR5aF9qem9hZ0RJamhPVDZhQ2tUREpucHBHWnZ6eGozRUxNUjJqSENtNTUyWDhramFOQWV1RldqNXczME5USE83cWYzMWQ5WXhqUnF0dw?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxNbUgxQkh0ZkRTNW9FNlV6TElsVVdudTRKcG9GYlVrYnF4dFNsMVB1LU0wdGVobGxYLTFuSWtSOEVhZThSYy11Q3lJUmRZYWF3V2I3cndtb3plS25NMmtleUxNR21DcFRwajZqR0E1bXFYS253VjVwTUNMRnJyeUtjb3F2Ulpzd3BnVWY1MHdkR2xncGRxMndDQ0prcll2VE5ndlBPVGpFakZIdmlUTU9RRkxB?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxPalR2WVhHOTNiT3R5MUU4ZWtxaUs3UWxjbFA3Ylg2Ti1tWDJRaHl1YXRmRmVHcEcxQURvU2EtcVM5MFNlQTRzNUdGZWNWRU9mX2l5OVoyaVphektVRTR2R2tJa2dhbzRDMThOT3ZGVkZFRTN6UnpZcVd4bldYZTJNWjQyb3hyd05jQnhEM0pMODNOUnVxTUVWRW1WZ1p1bU1SU2RXVw?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxQU1ctTHZIMkJYenpSU2NxUHkxbGVHbzFaUEM1czlaVG5sN1F6VWpwbEpPd0NxTjFUUGlLc1ZVZDBLVGdEa21zTDRET195R29IM3U4TkdlWDFNWjlFeTBYZVM5aFVkM0prdGI4RWJUUUtrYm43a1BjdlFGSkpRRXJlbDlUbnpkSXl0NUJlcGp2aWZCR1k5eHFmOVB6VFgyTG10MWRqMXc1ajRMZ294ZUN4MUpJWnR1MXVmMUJHOG5GM09DbmZi0gHKAUFVX3lxTFB2Y1poVVNOaVk3cHE1eExtbW91cFQtQ3JmRXRoMVIxb3kxRVo5QXctNUJSNDl4dVFRejIzTndFMUVKd0hJMDZ4d2d1NG9sRktXUTdRc1A0d1psSkRaNWJuRUVEQm1VX1ZaRF8yMEN1MWVDTVQ0U1RtVWFEMDlCLWd5N3FvQWJreXFXaENUWENkYlM4ZWpkNlFFRnJrYzFJalhsdndERE1LUkNxeVQ0SWN0bGdCOWdpRWs5MjZiOUo3MzVLbDFPVktMN1E?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxPLUo5Q1VwbWpnem5zNTdRZDhselFCQkMzQ3QybXE2ZktONndGVGxyNXM4RUdETFhRQ19DNWRKRFp4aXNWYzJMZ2hmTjBEdF9DWl9uM1k4UmwyeE5GaGxfTTFyMzJUaXpYMWsyQlRoQU9wXzhZUHNNLWdmR05jNVRyTG1icy1ROW51S0pXRVM4cGFzSENTTzU2ZnU1b3hnZVliSHlNTW5nSEk?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxOYmVEU3hCOWtMa2E2SEFnQXp3M0ticXpjMm5zY2tPWHNNWGt0MTBncTFlbUh6VnJhRWpFazBLbU5Kd3RMSURiMWI5Z0N5WnFVbFI4cHlvTVZhQmU4U2tTSVVPa1MzWWtLUG9xdGsyWlBGaEFtYWxrNWloLWZ4VEpsSUdYempUSUdidjN3?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
