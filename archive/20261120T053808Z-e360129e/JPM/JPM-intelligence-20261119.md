# JPM Intelligence Report

- ticker: **JPM**
- Report as_of: **2026-11-19**
- Market data as_of: **2026-11-19**
- Quant sources: https://finance.yahoo.com/quote/JPM/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/JPM/key-statistics/
- AI analysis snapshot as_of: **2026-11-19**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-20T05:56:14.744085+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 1, 'ai': 19, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **15** exact headline/source/date matches; prior report **20261119T054856Z-9eb86811/JPM** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 14 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 16.0%; oldest publication 2026-11-14

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 320.2200 |
| Return 1D (%) | -1.2002 |
| Return 1W (%) | -6.5924 |
| Return 1M (%) | -3.9906 |
| Return YTD (%) | 1.2933 |
| Return 1Y (%) | 7.6227 |
| Annualized volatility (%) | 22.9329 |
| Beta vs SPY | 0.7975 |
| Max drawdown (%) | -15.4717 |
| Sharpe (rf=0) | 0.4362 |
| Downside deviation (rf=0, %) | 16.5458 |
| Sortino (rf=0) | 0.6045 |
| Historical VaR 95% (1D, %) | 2.4357 |
| Historical ES 95% (1D, %) | 3.3208 |
| Correlation vs SPY | 0.4834 |
| Tracking error vs SPY (%) | 20.2723 |
| P/E (trailing) | 13.43 |
| P/B | 2.42 |
| EV/EBITDA | N/A |
| Revenue growth (%) | 10.20 |
| Forward P/E (estimate) | 12.52 |
| Gross margin (%) | 0.00 |
| Operating margin (%) | 44.79 |
| Return on equity (%) | 18.01 |
| Free cash flow yield (%) | N/A |
| MA50 | 337.6865 |
| Close vs MA50 (%) | -5.1724 |
| MA200 | 322.8572 |
| Close vs MA200 (%) | -0.8168 |
| RSI (14, Wilder) | 35.8546 |
| MACD (12,26) | -2.2727 |
| MACD signal (9) | -0.1927 |
| MACD histogram | -2.0800 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'JPM': 286, 'SPY': 286}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 320.2200 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.2002 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -6.5924 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -3.9906 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 1.2933 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 7.6227 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 22.9329 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 16.5458 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.6045 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.4357 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.3208 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4834 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 20.2723 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.7975 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -15.4717 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.4362 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 12.5218 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 0.0000 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 44.7880 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 18.0130 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 13.4320 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 35.8546 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -2.0800 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -5.1724 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -0.8168 -> Slightly below the moving-average trend level.

## TAILWINDS

### Jamie Dimon Just Said 5 Words Blocking Outside AI Agents From JPMorgan Accounts: "You Don't Want Rogue Agents." Here's Why That Security Stance Matters for JPM and Its Tech Rivals.
- Summary: JPM’s proactive AI security stance signals risk mitigation, potentially boosting investor confidence.
- Date: 2026-11-14 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxNQWQ4UlBOQ3VlbjFqcEpma1BDMjRRczVfalJRVWZaUjdyY2l0Rmw2NWtvb2gzVXZ2R2JTR09LSlFIcmd5aVh1NklOcU1BUGhVVTY3ZEFwdEdlcWZuLXZTbzNsOVoybXdOcDJTR3A3T2FvbDNaMmZZbmVTQTVGZGhCY3RGQVllZmN1ZG9DbXNfd090MzkwRHdR?oc=5>

### A property insurer puts $250 million into J.P. Morgan's new global stock fund
- Summary: Insurer invests $250M in JPM's global stock fund, supporting capital growth.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxQQTkyOEx3VGhEZDlSckZqUl85UzY1NmthY1p2V2dKWnBlTDNiM0FNczFCaENucVZTdWszNTU4QzNaTC1xT0w2LXhZakVGbXplQ2V2c0lyOTFrYWM1OWdvS3lxZ3lHeWFNX3FBTjcxVGJmTmFoNE9vc1hmMTNFY3ZXbFRYZGIxSjIxemJmMXlUbnJ3UExQc3dDUENDMmxlS0xXdjVTYjJ3TnViOTNvVW0wVE9GMUxsYlVfTnFnLWlR?oc=5>

## HEADWINDS

### JPMorgan Chase (JPM) Shares Fall Amid Bank Sector Technical Conc
- Summary: JPMorgan Chase (JPM) Shares Fall Amid Bank Sector Technical Conc
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxPOC1rVjdnQXJKQ3llNzgyVmpUTlc5U1pTVnNmN0pob0huNGRmSDZYcGRyZWdjcGl2d09qTlliV3hmRkNYOGZ4ek83bTBNMVYxSmh5dzNhMXVqemdCU1pGSWdiNDVCLXMxRzBDU2hueGpBTExtTWJIbDVUVlkxR2s4eGRCZHVGTm8yLXluRXlobTJhNU90a25VbkdIcDFQdlczZ184LUFIQUY?oc=5>

### JPMorgan Stock Slides: What's Going On?
- Summary: JPM stock is declining, raising concerns about its short-term performance.
- Date: 2026-11-17 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxPY25wTkZqdFZDWF93OFdXcFRsSmJWM0oybzR3b3N1OHZ1bURYVjlFZkoySHhQVkxrNjluVTBqQzNIQ2pGWGQwN0ZheXhvbk8yT18xQzYtaDhnSVJYTVA4VVQ4eUNkZDFzNDc5TW1fMXZsMzRGR0FnelpUaVZLeEhkNnpPd2RVLTNncEY4SGluTVA5dE5IbnF3aFFFdFFSQQ?oc=5>

### Chase, Bank of America, Wells Fargo Customers Report Banking Problems
- Summary: Customer-reported banking issues across major banks signal operational challenges.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxObjAzMG50cm9JUFhqYUZBb2JKdTJsUzZQWUpaTWJJc0pZS2lNUDJLSldZQjllUlloVG9xSng4eHNOdndBUW1GcmE3XzdHY1Z1V3Y4Njc2TXY1MndBMHA2aTIweTR3VXR6RFpIeVFMQWdwZ3lOWU90ei01VVJOQ0tGYTdEcVkzUHRTaGdJVFF3ZlAtOGhaX25GcGJzTmxxc1VyMjRfVmRsaThTNE54U0hGdGxORzc0RUNUdlNV?oc=5>

### After Monday's Banking Outage, JPMorgan Chase (NYSE:JPM) Slips as It Names a New CFO
- Summary: Banking outage and CFO change cause short-term stock decline.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxORC1SRjZ5SU8xVUlXeUNqa2VxbURUdW1ERERZNURkcjFDdkVHSHRjRTVSdWVTNG1qVVN4cS15d0xPQnllMUVsMDFlbUhIXzB2M0dfaXZOMVFUS29qaFZoSUJ3NnEwX01QTG1DdzZEQVNFY1VSTDc0TXdvaVFTQVdPXzBLZWd3eXlvOVoteW0wWUx4WjRMMXlaZlFBdWUxSElhNjAxUFJvRGxoSVlZVllDaV9Xbw?oc=5>

### JPMorgan Chase & Co. (NYSE:JPM) Shares Down 1.9% - Should You Sell?
- Summary: Shares fell 1.9%, prompting sell‑side commentary.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxPSjl5aTd3Xzd3c2J5MnZnUkFPc1lBLWt1d1lPTFI4cHJ6cHJLaE1ORVJoRTQ1N016ZGtLRGpvVUs3dE41cXV3ZTd6N0pqOXhTSUFaajBkLTRCb0pYM05LZGRhcTA5ZW9OaEpoYmhEZDlhMndtVk9YT0huZ18tWjhvREUzZjdnREJBNTM1WThlWGdqNWM0Mm1hS24tekxkTGUtM3VBTDc4VkkzaDBYUjBhX0c1ZzlMUVF5?oc=5>

### Third-party vendors of JPMorgan Chase, Visa, Mastercard reportedly faced cyberattacks (JPM:NYSE)
- Summary: Cyberattacks on third‑party vendors threaten JPM operations.
- Date: 2026-11-19 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxNS1daVEN0SlZtVGhOUjZxSTI3TmhybWJYN3dIMkdOVUtYck1LQjhyRUNsMkdhMXo5dWFtUWRxUnVROFloQzI1Y3ZNRWpURFZwakNWM041ekhjTTc2c0JJN1FjRDdST3E4OUdWSk1SdERfWW00aUp6QVl0Q1dHTnNYMFlXQ3JNd0szM2hvSGpyOXM2dlFfR2NwV1VpVXRaS21FLUxzQ19DOHJkNXpNV3V2Uw?oc=5>

### Visa, Mastercard, JPMorgan Hit By Reported Data Leak, Payment Information Not Affected
- Summary: Data leak involving JPM and partners raises security concerns.
- Date: 2026-11-19 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxNemtoLTNrQVB1M1loZGQyaUtzUkdiZDVHNDBkRF8waURYakthUVpueGRSUTZGMnc1VVlscGVLeEtZRl93V1hXNzR5VkhNcmg2SUtyOXBQQWlJZnFnU2FwYzZlNktrM3NReXJCVEtaYTV1b0g2ZHVZUFVZY3FPMHlfRWVrNHVVeTZKWWt3QnM2LW45ZVU3QmxzelF4SmRRYUE?oc=5>

### JPMorgan Chase & Co. (NYSE:JPM) Stock Price Breaks Below Two Hundred Day Moving Average - Should You Sell?
- Summary: JPM stock falls below 200‑day moving average, signaling potential downside pressure.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi7wFBVV95cUxOMVlnOTBybnpvZDFpOUdlNnV3eG1vWm5yNjk3QThKandiQ2xSUDRKR3VsQWxGRUZIOWJqajRtMGhlY3Vmd0ZlTEtGRE5oM1VZQnBHeUhNaFVPVHZ5UmxaX2VUR3o5SUpNb2dBdHAyeW9pVE5tWGRZSklfQnRQZFlMMjIwQk5nRUd6Q3RNaEZwekdPQi1wVGJRU0JJZVVPUUl1dk85ZnF4YTNNTm43QW1pMEZMcXNhS1Rfbzh6VkR1VlVTRE1LQzZHREktU2xNWmRFamJYbXhHd25Wdkl0QUlIdjJiMXE4M25oME9YbGVxVQ?oc=5>

### JPMorgan Chase (NYSE:JPM) Faces Pressure As Momentum Weakens
- Summary: JPM stock momentum weakens, indicating possible short‑term selling pressure.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxPaGpTV3RVUkt6dUhNY2hjSnI3V25VOWRzVUVoTVU0X1pwS001YUJFc19JempUaWV3SXNMeTctajlfVlFQajlzN0NWY3ROTjE3cEJOWnJyYlA2RjJlaWNhOE1iYTZWdm94NjdFYzFSRkFyZXJPTjhPWXNvRG5xRlNMT3pCc19KanhxcWZIRTRVS3JJNGoyRWJJMVlYd2FwampHLWpwSA?oc=5>

### JPMorgan Chase (JPM) Stock Price Prediction: JPMorgan Chase slips below near-term trend as analysts stay constructive
- Summary: JPM stock slips below near‑term trend, despite constructive analyst outlook.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxPWTNzZ3lKRnN2X0JxRWRNVXJwSmRPcGxEbWtkQkNEUGdhbjdaTWdLRU5OVkd1ZGZ5c3NzNHR1ZE5xQjk5RHpZTVIzZTVYM0dPSkE4cTJqU21nVVZWTTdHOFhCek13QnRDa1BKV25jemlaSFRxWEh6S3NwRkI2cG1keXdYOTV0aWQ5cGJ5djZKWE1uWW91MHFHaC1zNA?oc=5>

## CATALYSTS

### AI Infrastructure Demand Might Change The Case For Investing In JPMorgan Chase Stock (JPM)
- Summary: Growing AI infrastructure demand could enhance JPM's investment appeal.
- Date: 2026-11-16 | Impact: medium | Horizon: medium | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxPalR2WVhHOTNiT3R5MUU4ZWtxaUs3UWxjbFA3Ylg2Ti1tWDJRaHl1YXRmRmVHcEcxQURvU2EtcVM5MFNlQTRzNUdGZWNWRU9mX2l5OVoyaVphektVRTR2R2tJa2dhbzRDMThOT3ZGVkZFRTN6UnpZcVd4bldYZTJNWjQyb3hyd05jQnhEM0pMODNOUnVxTUVWRW1WZ1p1bU1SU2RXVw?oc=5>

### JPMorgan names Bregje de Best as next CFO, succeeding Barnum
- Summary: JPM appoints Bregje de Best as CFO, succeeding Barnum.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxOX0tJbXd0el94UVZKU2p6S21CdUVKUHRsWHlkajRucjlZZkt0SjRRdWFER3E1aWFNMFNQUTN5T3oxV2hKVmZuVFFuaVNUVFFUQnd6S0NCTUN0V0xweVRMT2VOYVoxeDR5aF9qem9hZ0RJamhPVDZhQ2tUREpucHBHWnZ6eGozRUxNUjJqSENtNTUyWDhramFOQWV1RldqNXczME5USE83cWYzMWQ5WXhqUnF0dw?oc=5>

### JPMorgan Chase announces CFO transition, confirms resolving 'technical issue' (JPM:NYSE)
- Summary: JPM confirms CFO transition and technical issue resolution.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxNbUgxQkh0ZkRTNW9FNlV6TElsVVdudTRKcG9GYlVrYnF4dFNsMVB1LU0wdGVobGxYLTFuSWtSOEVhZThSYy11Q3lJUmRZYWF3V2I3cndtb3plS25NMmtleUxNR21DcFRwajZqR0E1bXFYS253VjVwTUNMRnJyeUtjb3F2Ulpzd3BnVWY1MHdkR2xncGRxMndDQ0prcll2VE5ndlBPVGpFakZIdmlUTU9RRkxB?oc=5>

### JPMorgan Chase (JPM) names its next CFO. Jeremy Barnum will become vice chairman.
- Summary: JPMorgan Chase appoints Jeremy Barnum as CFO and vice chairman, signaling leadership change.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxPLUo5Q1VwbWpnem5zNTdRZDhselFCQkMzQ3QybXE2ZktONndGVGxyNXM4RUdETFhRQ19DNWRKRFp4aXNWYzJMZ2hmTjBEdF9DWl9uM1k4UmwyeE5GaGxfTTFyMzJUaXpYMWsyQlRoQU9wXzhZUHNNLWdmR05jNVRyTG1icy1ROW51S0pXRVM4cGFzSENTTzU2ZnU1b3hnZVliSHlNTW5nSEk?oc=5>

### Who Is Bregje de Best, the Next CFO of JPMorganChase (NYSE:JPM)?
- Summary: Article explores Bregje de Best’s background as JPMorgan Chase’s incoming CFO.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxPcVltbDQ3cFpCTGFVY2dIZlVFZHFFZkdoODNLeWF0Vm5Ka1oyaWpiTzYxVndCSFMtQ1ZlT09UdUk0aGh4MkZudGExby05anN5ei10ZE5KaFM3Q3ZxZHZXaG1DQXRYeHdHUThQeEZLLUkyUDg1QmVuNGpVaEl1Xy1ObzZJWi1pb2lMMTZvUml2eFBOb1h4dVhuM1lsYXlFRjc3eWVVWEx2WQ?oc=5>

### Why Is JPMorgan Chase (JPM) Naming Bregje De Best As Its Next CFO?
- Summary: Appointment of Bregje De Best as CFO signals leadership change.
- Date: 2026-11-19 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxQU1ctTHZIMkJYenpSU2NxUHkxbGVHbzFaUEM1czlaVG5sN1F6VWpwbEpPd0NxTjFUUGlLc1ZVZDBLVGdEa21zTDRET195R29IM3U4TkdlWDFNWjlFeTBYZVM5aFVkM0prdGI4RWJUUUtrYm43a1BjdlFGSkpRRXJlbDlUbnpkSXl0NUJlcGp2aWZCR1k5eHFmOVB6VFgyTG10MWRqMXc1ajRMZ294ZUN4MUpJWnR1MXVmMUJHOG5GM09DbmZi0gHKAUFVX3lxTFB2Y1poVVNOaVk3cHE1eExtbW91cFQtQ3JmRXRoMVIxb3kxRVo5QXctNUJSNDl4dVFRejIzTndFMUVKd0hJMDZ4d2d1NG9sRktXUTdRc1A0d1psSkRaNWJuRUVEQm1VX1ZaRF8yMEN1MWVDTVQ0U1RtVWFEMDlCLWd5N3FvQWJreXFXaENUWENkYlM4ZWpkNlFFRnJrYzFJalhsdndERE1LUkNxeVQ0SWN0bGdCOWdpRWs5MjZiOUo3MzVLbDFPVktMN1E?oc=5>

## RISKS

### What Does JPMorgan Chase (JPM) Mean For Investors If Card Rates Are Capped?
- Summary: Potential card rate caps could affect JPM’s revenue and investor outlook.
- Date: 2026-11-15 | Impact: medium | Horizon: medium | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMixgFBVV95cUxOaUR6ZDNoRFpjanljYXQ2UmlNTHgzek1xcloyVTdHd0FoWHBJNlBFQmJLMkhPSVpHOTNOSGR1dkt5MnVqSVZycFBZdlVWQ0JLMEpDd2c0Vi1JQmoyemprRGtYQmtaQ2VtdDRsbGdDa1RyMC1GT0MzdDhXV0NoelFGcWU1TmRxTDZIRGdsQnJhRzFFdWtoRkxpdFk5V0trUjJSckhYX2x4M0pUWGYxclVmM2F1bXVsZFZIQURFT0tWSlVFelpYYUHSAcsBQVVfeXFMTlU0c1J6VFJ2ZjFvWmRlNHZ5TXE1b2otOFF2VmdJRXRyaTFoS3hnQVEzcE0zOTc3Z1hWTFlFZlluWFFld2lwSTRzN3NYWUpfaTcyblEyZjZlQnJWNXd5SWFqaS1MdEtLU09wUUpobXl5ODVEUVlwWGlmaGN0VEtQVHJfbTk1NE9HNzZZSW02ZGFxcXFvMEt4Y2RQdlBuWXhMV1RFak4xazB2cnE4THFsTTJxaks1dkxWWnR5MHkwS0V1d2toOHpYRXhVRkE?oc=5>

### JPMorgan Chase (JPM) Says Vendors Hit by Cyberattack
- Summary: Cyberattack on vendors could disrupt JPM operations and increase risk exposure.
- Date: 2026-11-19 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMihwFBVV95cUxNbGhnR09Gb1c0S1Q2c1FRT1NzcmlaR1pDTmhEYl9LTFFjMjdocnJ4VEJsYTFWOXJxN2ozaExGQ20xUlQydTVuRUFiMk4wdzM3dFlTYVYxbS1fR1VqbWpTa2JHaGlkazA5RERMSDhrZmRCNk5hRnNoRkdNelJzLXNIOWNFQngydGs?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **JPM** | **13.43** | **2.42** | **N/A** | **10.20** | **850,379,341,824.00 USD** | **7.62** |
| BAC | 11.68 | 1.24 | N/A | 3.40 | 335,143,141,376.00 USD | -4.64 |
| C | 11.44 | 1.00 | N/A | 8.00 | 190,811,963,392.00 USD | 17.86 |
| WFC | 11.37 | 1.53 | N/A | 0.40 | 241,979,162,624.00 USD | -2.06 |

Peers fetched as_of: 2026-11-19; JPM reuses existing data (market data as_of: 2026-11-19); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-13
- Next expected earnings: 2027-01-14 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-19

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

- https://news.google.com/rss/articles/CBMilwFBVV95cUxNQWQ4UlBOQ3VlbjFqcEpma1BDMjRRczVfalJRVWZaUjdyY2l0Rmw2NWtvb2gzVXZ2R2JTR09LSlFIcmd5aVh1NklOcU1BUGhVVTY3ZEFwdEdlcWZuLXZTbzNsOVoybXdOcDJTR3A3T2FvbDNaMmZZbmVTQTVGZGhCY3RGQVllZmN1ZG9DbXNfd090MzkwRHdR?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxQQTkyOEx3VGhEZDlSckZqUl85UzY1NmthY1p2V2dKWnBlTDNiM0FNczFCaENucVZTdWszNTU4QzNaTC1xT0w2LXhZakVGbXplQ2V2c0lyOTFrYWM1OWdvS3lxZ3lHeWFNX3FBTjcxVGJmTmFoNE9vc1hmMTNFY3ZXbFRYZGIxSjIxemJmMXlUbnJ3UExQc3dDUENDMmxlS0xXdjVTYjJ3TnViOTNvVW0wVE9GMUxsYlVfTnFnLWlR?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxPOC1rVjdnQXJKQ3llNzgyVmpUTlc5U1pTVnNmN0pob0huNGRmSDZYcGRyZWdjcGl2d09qTlliV3hmRkNYOGZ4ek83bTBNMVYxSmh5dzNhMXVqemdCU1pGSWdiNDVCLXMxRzBDU2hueGpBTExtTWJIbDVUVlkxR2s4eGRCZHVGTm8yLXluRXlobTJhNU90a25VbkdIcDFQdlczZ184LUFIQUY?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxPY25wTkZqdFZDWF93OFdXcFRsSmJWM0oybzR3b3N1OHZ1bURYVjlFZkoySHhQVkxrNjluVTBqQzNIQ2pGWGQwN0ZheXhvbk8yT18xQzYtaDhnSVJYTVA4VVQ4eUNkZDFzNDc5TW1fMXZsMzRGR0FnelpUaVZLeEhkNnpPd2RVLTNncEY4SGluTVA5dE5IbnF3aFFFdFFSQQ?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxObjAzMG50cm9JUFhqYUZBb2JKdTJsUzZQWUpaTWJJc0pZS2lNUDJLSldZQjllUlloVG9xSng4eHNOdndBUW1GcmE3XzdHY1Z1V3Y4Njc2TXY1MndBMHA2aTIweTR3VXR6RFpIeVFMQWdwZ3lOWU90ei01VVJOQ0tGYTdEcVkzUHRTaGdJVFF3ZlAtOGhaX25GcGJzTmxxc1VyMjRfVmRsaThTNE54U0hGdGxORzc0RUNUdlNV?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxORC1SRjZ5SU8xVUlXeUNqa2VxbURUdW1ERERZNURkcjFDdkVHSHRjRTVSdWVTNG1qVVN4cS15d0xPQnllMUVsMDFlbUhIXzB2M0dfaXZOMVFUS29qaFZoSUJ3NnEwX01QTG1DdzZEQVNFY1VSTDc0TXdvaVFTQVdPXzBLZWd3eXlvOVoteW0wWUx4WjRMMXlaZlFBdWUxSElhNjAxUFJvRGxoSVlZVllDaV9Xbw?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxPSjl5aTd3Xzd3c2J5MnZnUkFPc1lBLWt1d1lPTFI4cHJ6cHJLaE1ORVJoRTQ1N016ZGtLRGpvVUs3dE41cXV3ZTd6N0pqOXhTSUFaajBkLTRCb0pYM05LZGRhcTA5ZW9OaEpoYmhEZDlhMndtVk9YT0huZ18tWjhvREUzZjdnREJBNTM1WThlWGdqNWM0Mm1hS24tekxkTGUtM3VBTDc4VkkzaDBYUjBhX0c1ZzlMUVF5?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxNS1daVEN0SlZtVGhOUjZxSTI3TmhybWJYN3dIMkdOVUtYck1LQjhyRUNsMkdhMXo5dWFtUWRxUnVROFloQzI1Y3ZNRWpURFZwakNWM041ekhjTTc2c0JJN1FjRDdST3E4OUdWSk1SdERfWW00aUp6QVl0Q1dHTnNYMFlXQ3JNd0szM2hvSGpyOXM2dlFfR2NwV1VpVXRaS21FLUxzQ19DOHJkNXpNV3V2Uw?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxNemtoLTNrQVB1M1loZGQyaUtzUkdiZDVHNDBkRF8waURYakthUVpueGRSUTZGMnc1VVlscGVLeEtZRl93V1hXNzR5VkhNcmg2SUtyOXBQQWlJZnFnU2FwYzZlNktrM3NReXJCVEtaYTV1b0g2ZHVZUFVZY3FPMHlfRWVrNHVVeTZKWWt3QnM2LW45ZVU3QmxzelF4SmRRYUE?oc=5
- https://news.google.com/rss/articles/CBMi7wFBVV95cUxOMVlnOTBybnpvZDFpOUdlNnV3eG1vWm5yNjk3QThKandiQ2xSUDRKR3VsQWxGRUZIOWJqajRtMGhlY3Vmd0ZlTEtGRE5oM1VZQnBHeUhNaFVPVHZ5UmxaX2VUR3o5SUpNb2dBdHAyeW9pVE5tWGRZSklfQnRQZFlMMjIwQk5nRUd6Q3RNaEZwekdPQi1wVGJRU0JJZVVPUUl1dk85ZnF4YTNNTm43QW1pMEZMcXNhS1Rfbzh6VkR1VlVTRE1LQzZHREktU2xNWmRFamJYbXhHd25Wdkl0QUlIdjJiMXE4M25oME9YbGVxVQ?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxPaGpTV3RVUkt6dUhNY2hjSnI3V25VOWRzVUVoTVU0X1pwS001YUJFc19JempUaWV3SXNMeTctajlfVlFQajlzN0NWY3ROTjE3cEJOWnJyYlA2RjJlaWNhOE1iYTZWdm94NjdFYzFSRkFyZXJPTjhPWXNvRG5xRlNMT3pCc19KanhxcWZIRTRVS3JJNGoyRWJJMVlYd2FwampHLWpwSA?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxPWTNzZ3lKRnN2X0JxRWRNVXJwSmRPcGxEbWtkQkNEUGdhbjdaTWdLRU5OVkd1ZGZ5c3NzNHR1ZE5xQjk5RHpZTVIzZTVYM0dPSkE4cTJqU21nVVZWTTdHOFhCek13QnRDa1BKV25jemlaSFRxWEh6S3NwRkI2cG1keXdYOTV0aWQ5cGJ5djZKWE1uWW91MHFHaC1zNA?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxPalR2WVhHOTNiT3R5MUU4ZWtxaUs3UWxjbFA3Ylg2Ti1tWDJRaHl1YXRmRmVHcEcxQURvU2EtcVM5MFNlQTRzNUdGZWNWRU9mX2l5OVoyaVphektVRTR2R2tJa2dhbzRDMThOT3ZGVkZFRTN6UnpZcVd4bldYZTJNWjQyb3hyd05jQnhEM0pMODNOUnVxTUVWRW1WZ1p1bU1SU2RXVw?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxOX0tJbXd0el94UVZKU2p6S21CdUVKUHRsWHlkajRucjlZZkt0SjRRdWFER3E1aWFNMFNQUTN5T3oxV2hKVmZuVFFuaVNUVFFUQnd6S0NCTUN0V0xweVRMT2VOYVoxeDR5aF9qem9hZ0RJamhPVDZhQ2tUREpucHBHWnZ6eGozRUxNUjJqSENtNTUyWDhramFOQWV1RldqNXczME5USE83cWYzMWQ5WXhqUnF0dw?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxNbUgxQkh0ZkRTNW9FNlV6TElsVVdudTRKcG9GYlVrYnF4dFNsMVB1LU0wdGVobGxYLTFuSWtSOEVhZThSYy11Q3lJUmRZYWF3V2I3cndtb3plS25NMmtleUxNR21DcFRwajZqR0E1bXFYS253VjVwTUNMRnJyeUtjb3F2Ulpzd3BnVWY1MHdkR2xncGRxMndDQ0prcll2VE5ndlBPVGpFakZIdmlUTU9RRkxB?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxPLUo5Q1VwbWpnem5zNTdRZDhselFCQkMzQ3QybXE2ZktONndGVGxyNXM4RUdETFhRQ19DNWRKRFp4aXNWYzJMZ2hmTjBEdF9DWl9uM1k4UmwyeE5GaGxfTTFyMzJUaXpYMWsyQlRoQU9wXzhZUHNNLWdmR05jNVRyTG1icy1ROW51S0pXRVM4cGFzSENTTzU2ZnU1b3hnZVliSHlNTW5nSEk?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxPcVltbDQ3cFpCTGFVY2dIZlVFZHFFZkdoODNLeWF0Vm5Ka1oyaWpiTzYxVndCSFMtQ1ZlT09UdUk0aGh4MkZudGExby05anN5ei10ZE5KaFM3Q3ZxZHZXaG1DQXRYeHdHUThQeEZLLUkyUDg1QmVuNGpVaEl1Xy1ObzZJWi1pb2lMMTZvUml2eFBOb1h4dVhuM1lsYXlFRjc3eWVVWEx2WQ?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxQU1ctTHZIMkJYenpSU2NxUHkxbGVHbzFaUEM1czlaVG5sN1F6VWpwbEpPd0NxTjFUUGlLc1ZVZDBLVGdEa21zTDRET195R29IM3U4TkdlWDFNWjlFeTBYZVM5aFVkM0prdGI4RWJUUUtrYm43a1BjdlFGSkpRRXJlbDlUbnpkSXl0NUJlcGp2aWZCR1k5eHFmOVB6VFgyTG10MWRqMXc1ajRMZ294ZUN4MUpJWnR1MXVmMUJHOG5GM09DbmZi0gHKAUFVX3lxTFB2Y1poVVNOaVk3cHE1eExtbW91cFQtQ3JmRXRoMVIxb3kxRVo5QXctNUJSNDl4dVFRejIzTndFMUVKd0hJMDZ4d2d1NG9sRktXUTdRc1A0d1psSkRaNWJuRUVEQm1VX1ZaRF8yMEN1MWVDTVQ0U1RtVWFEMDlCLWd5N3FvQWJreXFXaENUWENkYlM4ZWpkNlFFRnJrYzFJalhsdndERE1LUkNxeVQ0SWN0bGdCOWdpRWs5MjZiOUo3MzVLbDFPVktMN1E?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxOaUR6ZDNoRFpjanljYXQ2UmlNTHgzek1xcloyVTdHd0FoWHBJNlBFQmJLMkhPSVpHOTNOSGR1dkt5MnVqSVZycFBZdlVWQ0JLMEpDd2c0Vi1JQmoyemprRGtYQmtaQ2VtdDRsbGdDa1RyMC1GT0MzdDhXV0NoelFGcWU1TmRxTDZIRGdsQnJhRzFFdWtoRkxpdFk5V0trUjJSckhYX2x4M0pUWGYxclVmM2F1bXVsZFZIQURFT0tWSlVFelpYYUHSAcsBQVVfeXFMTlU0c1J6VFJ2ZjFvWmRlNHZ5TXE1b2otOFF2VmdJRXRyaTFoS3hnQVEzcE0zOTc3Z1hWTFlFZlluWFFld2lwSTRzN3NYWUpfaTcyblEyZjZlQnJWNXd5SWFqaS1MdEtLU09wUUpobXl5ODVEUVlwWGlmaGN0VEtQVHJfbTk1NE9HNzZZSW02ZGFxcXFvMEt4Y2RQdlBuWXhMV1RFak4xazB2cnE4THFsTTJxaks1dkxWWnR5MHkwS0V1d2toOHpYRXhVRkE?oc=5
- https://news.google.com/rss/articles/CBMihwFBVV95cUxNbGhnR09Gb1c0S1Q2c1FRT1NzcmlaR1pDTmhEYl9LTFFjMjdocnJ4VEJsYTFWOXJxN2ozaExGQ20xUlQydTVuRUFiMk4wdzM3dFlTYVYxbS1fR1VqbWpTa2JHaGlkazA5RERMSDhrZmRCNk5hRnNoRkdNelJzLXNIOWNFQngydGs?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
