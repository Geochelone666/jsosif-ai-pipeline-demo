# JPM Intelligence Report

- ticker: **JPM**
- Report as_of: **2026-11-18**
- Market data as_of: **2026-11-18**
- Quant sources: https://finance.yahoo.com/quote/JPM/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/JPM/key-statistics/
- AI analysis snapshot as_of: **2026-11-18**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-19T05:49:04.434166+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 3, 'ai': 16, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **0** exact headline/source/date matches; prior report **N/A** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 13 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 28.0%; oldest publication 2026-11-13

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 324.1100 |
| Return 1D (%) | -1.7729 |
| Return 1W (%) | -5.6146 |
| Return 1M (%) | -4.5950 |
| Return YTD (%) | 2.5238 |
| Return 1Y (%) | 10.3344 |
| Annualized volatility (%) | 22.9328 |
| Beta vs SPY | 0.8031 |
| Max drawdown (%) | -15.4717 |
| Sharpe (rf=0) | 0.5452 |
| Downside deviation (rf=0, %) | 16.5021 |
| Sortino (rf=0) | 0.7576 |
| Historical VaR 95% (1D, %) | 2.4357 |
| Historical ES 95% (1D, %) | 3.3208 |
| Correlation vs SPY | 0.4817 |
| Tracking error vs SPY (%) | 20.2781 |
| P/E (trailing) | 13.60 |
| P/B | 2.45 |
| EV/EBITDA | N/A |
| Revenue growth (%) | 10.20 |
| Forward P/E (estimate) | 12.67 |
| Gross margin (%) | 0.00 |
| Operating margin (%) | 44.79 |
| Return on equity (%) | 18.01 |
| Free cash flow yield (%) | N/A |
| MA50 | 338.3182 |
| Close vs MA50 (%) | -4.1997 |
| MA200 | 322.8195 |
| Close vs MA200 (%) | 0.3998 |
| RSI (14, Wilder) | 38.2221 |
| MACD (12,26) | -1.0158 |
| MACD signal (9) | 0.3273 |
| MACD histogram | -1.3431 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'JPM': 285, 'SPY': 285}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 324.1100 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.7729 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -5.6146 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -4.5950 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 2.5238 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 10.3344 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 22.9328 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 16.5021 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.7576 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.4357 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.3208 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4817 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 20.2781 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.8031 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -15.4717 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.5452 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 12.6739 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 0.0000 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 44.7880 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 18.0130 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 13.5952 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 38.2221 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -1.3431 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -4.1997 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 0.3998 -> Slightly above the moving-average trend level.

## TAILWINDS

### Why JPMorgan Chase (JPM) Is Back In The Spotlight
- Summary: JPM is regaining attention, potentially boosting investor interest.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxNYTk3NzNqX0VtODU4aG1tRDVqM1RRTFQwSmJUS3pWTXBxOVZvTzBIYXd0SXRjekEtdzZKV2tVWmYxS3JheUdjaS0yWmN5bjFWYnRtV0dWT2FFVUZMckoyZjBtTUJDT05aNkp5NWhqNFJ3M1N2b3REU2Nvc0JydHNxcXRaVk5YQmYtb3NScUVKRnFFY2x2N0ZR?oc=5>

### Jamie Dimon Just Said 5 Words Blocking Outside AI Agents From JPMorgan Accounts: "You Don't Want Rogue Agents." Here's Why That Security Stance Matters for JPM and Its Tech Rivals.
- Summary: JPM’s proactive AI security stance signals risk mitigation, potentially boosting investor confidence.
- Date: 2026-11-14 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxNQWQ4UlBOQ3VlbjFqcEpma1BDMjRRczVfalJRVWZaUjdyY2l0Rmw2NWtvb2gzVXZ2R2JTR09LSlFIcmd5aVh1NklOcU1BUGhVVTY3ZEFwdEdlcWZuLXZTbzNsOVoybXdOcDJTR3A3T2FvbDNaMmZZbmVTQTVGZGhCY3RGQVllZmN1ZG9DbXNfd090MzkwRHdR?oc=5>

## HEADWINDS

### JPMorgan Chase (JPM) Shares Fall Amid Bank Sector Technical Conc
- Summary: JPMorgan Chase (JPM) Shares Fall Amid Bank Sector Technical Conc
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxPOC1rVjdnQXJKQ3llNzgyVmpUTlc5U1pTVnNmN0pob0huNGRmSDZYcGRyZWdjcGl2d09qTlliV3hmRkNYOGZ4ek83bTBNMVYxSmh5dzNhMXVqemdCU1pGSWdiNDVCLXMxRzBDU2hueGpBTExtTWJIbDVUVlkxR2s4eGRCZHVGTm8yLXluRXlobTJhNU90a25VbkdIcDFQdlczZ184LUFIQUY?oc=5>

### JPMorgan Chase & Co. (JPM) Sees a More Significant Dip Than Broader Market: Some Facts to Know
- Summary: JPM shares are falling more than the broader market, indicating a negative market move.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxNbTc2eGZ3VHByLU0yNTg2ZFlNZ1c2ckpYV0l6eUpZY184aWtWMTJxUE12LVV4b2lBbkF0anhmRF9nOFptSFlMUHYydzNRdVJpdHFpclUydUQ5aWUwVzlJcHZ2YnRrRHZsWWRINU5fMEd0OUJuLUYxZlloX2xLUkpMOU5hUE5qMUtFejlJUm1HUWNwclcxWXc?oc=5>

### JPMorgan Stock Slides: What's Going On?
- Summary: JPM stock is declining, raising concerns about its short-term performance.
- Date: 2026-11-17 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxPY25wTkZqdFZDWF93OFdXcFRsSmJWM0oybzR3b3N1OHZ1bURYVjlFZkoySHhQVkxrNjluVTBqQzNIQ2pGWGQwN0ZheXhvbk8yT18xQzYtaDhnSVJYTVA4VVQ4eUNkZDFzNDc5TW1fMXZsMzRGR0FnelpUaVZLeEhkNnpPd2RVLTNncEY4SGluTVA5dE5IbnF3aFFFdFFSQQ?oc=5>

### JPMorgan Chase & Co. (NYSE:JPM) Shares Down 1.9% - Should You Sell?
- Summary: Shares fell 1.9%, prompting sell‑side commentary.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxPSjl5aTd3Xzd3c2J5MnZnUkFPc1lBLWt1d1lPTFI4cHJ6cHJLaE1ORVJoRTQ1N016ZGtLRGpvVUs3dE41cXV3ZTd6N0pqOXhTSUFaajBkLTRCb0pYM05LZGRhcTA5ZW9OaEpoYmhEZDlhMndtVk9YT0huZ18tWjhvREUzZjdnREJBNTM1WThlWGdqNWM0Mm1hS24tekxkTGUtM3VBTDc4VkkzaDBYUjBhX0c1ZzlMUVF5?oc=5>

### Chase, Bank of America, Wells Fargo Customers Report Banking Problems
- Summary: Customer-reported banking issues across major banks signal operational challenges.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxObjAzMG50cm9JUFhqYUZBb2JKdTJsUzZQWUpaTWJJc0pZS2lNUDJLSldZQjllUlloVG9xSng4eHNOdndBUW1GcmE3XzdHY1Z1V3Y4Njc2TXY1MndBMHA2aTIweTR3VXR6RFpIeVFMQWdwZ3lOWU90ei01VVJOQ0tGYTdEcVkzUHRTaGdJVFF3ZlAtOGhaX25GcGJzTmxxc1VyMjRfVmRsaThTNE54U0hGdGxORzc0RUNUdlNV?oc=5>

### JPMorgan, BofA, Wells Fargo, other banks trade lower amid user reports indicating problems
- Summary: Negative market reaction to reported banking problems lowers stock prices.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxNVWNFXzhUZ184SWp2TkR3VV9WUzdaVFpWT0ZmZUczNXI2WmZudzdRS0pHUHdxb1BsYnBrdGhOUS1HT1UtdmpsVFVRNG5JaE5RZHJvQ0VTdWlMR21uSHhiTms4ek44UjU2bTRualAtLXVma1FVaWlHLTB5NzdMQjRlLXlnUlZ2azh0OW5UMHRDcThfU2xveWllbXFSOGJlamd1MFg5LTlpOXZlSV9ySkFMT2tzN3Z3RWVkVFJMZmR1UEZWSDA?oc=5>

### After Monday's Banking Outage, JPMorgan Chase (NYSE:JPM) Slips as It Names a New CFO
- Summary: Banking outage and CFO change cause short-term stock decline.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxORC1SRjZ5SU8xVUlXeUNqa2VxbURUdW1ERERZNURkcjFDdkVHSHRjRTVSdWVTNG1qVVN4cS15d0xPQnllMUVsMDFlbUhIXzB2M0dfaXZOMVFUS29qaFZoSUJ3NnEwX01QTG1DdzZEQVNFY1VSTDc0TXdvaVFTQVdPXzBLZWd3eXlvOVoteW0wWUx4WjRMMXlaZlFBdWUxSElhNjAxUFJvRGxoSVlZVllDaV9Xbw?oc=5>

## CATALYSTS

### JPMorgan Chase Earned a Profit in Both 2008 and 2009. History Says That's the Bank to Own If a Recession Hits.
- Summary: JPMorgan Chase Earned a Profit in Both 2008 and 2009. History Says That's the Bank to Own If a Recession Hits.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxQeTVBRjkzUXJydk5JbmJILVNSU0N1dmI1MDMtLUhxbkFESmNGcDRZS1Jlc0wtQlFmeFVmM1h2Y3VCVXBKaGVacnFOai1DeFBwZWhCWElpVWdWMjM4eVJaS1ZROG84TTdQakxkNHFITUpPbjdaYS1XYnZkUG4xVVFQNGtuZ0QyWUN2TVhVRklrVUZwdDc3TVVib2gyUWdkN2s?oc=5>

### JPMorgan Chase (JPM) Launches After Hours Token Transfers And Backs $500 Million Financing
- Summary: JPMorgan Chase (JPM) Launches After Hours Token Transfers And Backs $500 Million Financing
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxNZFlCWkwwVG1XV0ticWR0NGR2d1dTN29wMk9vVllpbVJ6VVVSRXFuQUtaY0xwUmFoSk5wSVJQYlhvS1hmdkhsN01kQXBucU1YLTdoNEVkcmp2ekxBTzd5LV9TdFUzNzM3U2h3S01KNjItbHZWQ2xQakpEMDlDUlA1TFpKYUxPaWJQejZHNTRLd2VPcUtXTFg4bTd4bXZVeDg?oc=5>

### AI Infrastructure Demand Might Change The Case For Investing In JPMorgan Chase Stock (JPM)
- Summary: Growing AI infrastructure demand could enhance JPM's investment appeal.
- Date: 2026-11-16 | Impact: medium | Horizon: medium | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxPalR2WVhHOTNiT3R5MUU4ZWtxaUs3UWxjbFA3Ylg2Ti1tWDJRaHl1YXRmRmVHcEcxQURvU2EtcVM5MFNlQTRzNUdGZWNWRU9mX2l5OVoyaVphektVRTR2R2tJa2dhbzRDMThOT3ZGVkZFRTN6UnpZcVd4bldYZTJNWjQyb3hyd05jQnhEM0pMODNOUnVxTUVWRW1WZ1p1bU1SU2RXVw?oc=5>

### JPMorgan CFO Jeremy Barnum to step down as Jamie Dimon's succession plans take shape
- Summary: Leadership transition may influence JPM's strategic direction.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1wFBVV95cUxNX0JsTEFjeEpKWFRnRkwtZ1d5ajJLWUJDR1ZCeTJkTjh4ckctRXFTSW5ZYnduZ19HT0VwaDY4NE5tckZEVmN1amRvd18yR3h3bVBXeVltWTI2andCcUxPNEI3dFAzV2Z1TnZBMm0wQ3ZCOVdLMmc2eWgtNTMwREp1OXZlbHRNSnNQQjhsMlFMU1FXeHpDRElnbmg5aFI3M3BOZFZISTZsVjZoRVVfQm1CSW9HeTFmMkJtQnFhTlJGbmdmS3lnbTRmY09adjR3dnJQRUJqR3FMZw?oc=5>

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

## RISKS

### Why Are US Banks Reporting Outages? JPMorgan Rules Out Cyberattack, Blames Software Bug
- Summary: JPM rules out cyberattack, cites software bug for outages.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxOQUJ1YjM5SGU5WHJuMVY0aFpHZF9zcWN2VGVPNGJ0RllUZVpmSy16M2drVHI3YlJDcTI3ZHVKQlZvYTQ2WFd2Sm1oUVAxWFAzRkE4VVRjRWRneUw1RDduREp3UlNOaUxpdlRhRFVSXzJKd3JUaU1TTHVTcDZhbERFSThPX1dncWQzUmxFZHllMUh0NHJ2ODU1OThiWQ?oc=5>

### What Does JPMorgan Chase (JPM) Mean For Investors If Card Rates Are Capped?
- Summary: Potential card rate caps could affect JPM’s revenue and investor outlook.
- Date: 2026-11-15 | Impact: medium | Horizon: medium | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMixgFBVV95cUxOaUR6ZDNoRFpjanljYXQ2UmlNTHgzek1xcloyVTdHd0FoWHBJNlBFQmJLMkhPSVpHOTNOSGR1dkt5MnVqSVZycFBZdlVWQ0JLMEpDd2c0Vi1JQmoyemprRGtYQmtaQ2VtdDRsbGdDa1RyMC1GT0MzdDhXV0NoelFGcWU1TmRxTDZIRGdsQnJhRzFFdWtoRkxpdFk5V0trUjJSckhYX2x4M0pUWGYxclVmM2F1bXVsZFZIQURFT0tWSlVFelpYYUHSAcsBQVVfeXFMTlU0c1J6VFJ2ZjFvWmRlNHZ5TXE1b2otOFF2VmdJRXRyaTFoS3hnQVEzcE0zOTc3Z1hWTFlFZlluWFFld2lwSTRzN3NYWUpfaTcyblEyZjZlQnJWNXd5SWFqaS1MdEtLU09wUUpobXl5ODVEUVlwWGlmaGN0VEtQVHJfbTk1NE9HNzZZSW02ZGFxcXFvMEt4Y2RQdlBuWXhMV1RFak4xazB2cnE4THFsTTJxaks1dkxWWnR5MHkwS0V1d2toOHpYRXhVRkE?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **JPM** | **13.60** | **2.45** | **N/A** | **10.20** | **860,709,584,896.00 USD** | **10.33** |
| BAC | 11.67 | 1.25 | N/A | 3.40 | 337,489,231,872.00 USD | -3.27 |
| C | 11.44 | 1.01 | N/A | 8.00 | 194,221,686,784.00 USD | 21.81 |
| WFC | 11.66 | 1.53 | N/A | 0.40 | 242,909,724,672.00 USD | -1.34 |

Peers fetched as_of: 2026-11-18; JPM reuses existing data (market data as_of: 2026-11-18); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-13
- Next expected earnings: 2027-01-14 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-18

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

- https://news.google.com/rss/articles/CBMilwFBVV95cUxNYTk3NzNqX0VtODU4aG1tRDVqM1RRTFQwSmJUS3pWTXBxOVZvTzBIYXd0SXRjekEtdzZKV2tVWmYxS3JheUdjaS0yWmN5bjFWYnRtV0dWT2FFVUZMckoyZjBtTUJDT05aNkp5NWhqNFJ3M1N2b3REU2Nvc0JydHNxcXRaVk5YQmYtb3NScUVKRnFFY2x2N0ZR?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxNQWQ4UlBOQ3VlbjFqcEpma1BDMjRRczVfalJRVWZaUjdyY2l0Rmw2NWtvb2gzVXZ2R2JTR09LSlFIcmd5aVh1NklOcU1BUGhVVTY3ZEFwdEdlcWZuLXZTbzNsOVoybXdOcDJTR3A3T2FvbDNaMmZZbmVTQTVGZGhCY3RGQVllZmN1ZG9DbXNfd090MzkwRHdR?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxPOC1rVjdnQXJKQ3llNzgyVmpUTlc5U1pTVnNmN0pob0huNGRmSDZYcGRyZWdjcGl2d09qTlliV3hmRkNYOGZ4ek83bTBNMVYxSmh5dzNhMXVqemdCU1pGSWdiNDVCLXMxRzBDU2hueGpBTExtTWJIbDVUVlkxR2s4eGRCZHVGTm8yLXluRXlobTJhNU90a25VbkdIcDFQdlczZ184LUFIQUY?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxNbTc2eGZ3VHByLU0yNTg2ZFlNZ1c2ckpYV0l6eUpZY184aWtWMTJxUE12LVV4b2lBbkF0anhmRF9nOFptSFlMUHYydzNRdVJpdHFpclUydUQ5aWUwVzlJcHZ2YnRrRHZsWWRINU5fMEd0OUJuLUYxZlloX2xLUkpMOU5hUE5qMUtFejlJUm1HUWNwclcxWXc?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxPY25wTkZqdFZDWF93OFdXcFRsSmJWM0oybzR3b3N1OHZ1bURYVjlFZkoySHhQVkxrNjluVTBqQzNIQ2pGWGQwN0ZheXhvbk8yT18xQzYtaDhnSVJYTVA4VVQ4eUNkZDFzNDc5TW1fMXZsMzRGR0FnelpUaVZLeEhkNnpPd2RVLTNncEY4SGluTVA5dE5IbnF3aFFFdFFSQQ?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxPSjl5aTd3Xzd3c2J5MnZnUkFPc1lBLWt1d1lPTFI4cHJ6cHJLaE1ORVJoRTQ1N016ZGtLRGpvVUs3dE41cXV3ZTd6N0pqOXhTSUFaajBkLTRCb0pYM05LZGRhcTA5ZW9OaEpoYmhEZDlhMndtVk9YT0huZ18tWjhvREUzZjdnREJBNTM1WThlWGdqNWM0Mm1hS24tekxkTGUtM3VBTDc4VkkzaDBYUjBhX0c1ZzlMUVF5?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxObjAzMG50cm9JUFhqYUZBb2JKdTJsUzZQWUpaTWJJc0pZS2lNUDJLSldZQjllUlloVG9xSng4eHNOdndBUW1GcmE3XzdHY1Z1V3Y4Njc2TXY1MndBMHA2aTIweTR3VXR6RFpIeVFMQWdwZ3lOWU90ei01VVJOQ0tGYTdEcVkzUHRTaGdJVFF3ZlAtOGhaX25GcGJzTmxxc1VyMjRfVmRsaThTNE54U0hGdGxORzc0RUNUdlNV?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxNVWNFXzhUZ184SWp2TkR3VV9WUzdaVFpWT0ZmZUczNXI2WmZudzdRS0pHUHdxb1BsYnBrdGhOUS1HT1UtdmpsVFVRNG5JaE5RZHJvQ0VTdWlMR21uSHhiTms4ek44UjU2bTRualAtLXVma1FVaWlHLTB5NzdMQjRlLXlnUlZ2azh0OW5UMHRDcThfU2xveWllbXFSOGJlamd1MFg5LTlpOXZlSV9ySkFMT2tzN3Z3RWVkVFJMZmR1UEZWSDA?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxORC1SRjZ5SU8xVUlXeUNqa2VxbURUdW1ERERZNURkcjFDdkVHSHRjRTVSdWVTNG1qVVN4cS15d0xPQnllMUVsMDFlbUhIXzB2M0dfaXZOMVFUS29qaFZoSUJ3NnEwX01QTG1DdzZEQVNFY1VSTDc0TXdvaVFTQVdPXzBLZWd3eXlvOVoteW0wWUx4WjRMMXlaZlFBdWUxSElhNjAxUFJvRGxoSVlZVllDaV9Xbw?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxQeTVBRjkzUXJydk5JbmJILVNSU0N1dmI1MDMtLUhxbkFESmNGcDRZS1Jlc0wtQlFmeFVmM1h2Y3VCVXBKaGVacnFOai1DeFBwZWhCWElpVWdWMjM4eVJaS1ZROG84TTdQakxkNHFITUpPbjdaYS1XYnZkUG4xVVFQNGtuZ0QyWUN2TVhVRklrVUZwdDc3TVVib2gyUWdkN2s?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxNZFlCWkwwVG1XV0ticWR0NGR2d1dTN29wMk9vVllpbVJ6VVVSRXFuQUtaY0xwUmFoSk5wSVJQYlhvS1hmdkhsN01kQXBucU1YLTdoNEVkcmp2ekxBTzd5LV9TdFUzNzM3U2h3S01KNjItbHZWQ2xQakpEMDlDUlA1TFpKYUxPaWJQejZHNTRLd2VPcUtXTFg4bTd4bXZVeDg?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxPalR2WVhHOTNiT3R5MUU4ZWtxaUs3UWxjbFA3Ylg2Ti1tWDJRaHl1YXRmRmVHcEcxQURvU2EtcVM5MFNlQTRzNUdGZWNWRU9mX2l5OVoyaVphektVRTR2R2tJa2dhbzRDMThOT3ZGVkZFRTN6UnpZcVd4bldYZTJNWjQyb3hyd05jQnhEM0pMODNOUnVxTUVWRW1WZ1p1bU1SU2RXVw?oc=5
- https://news.google.com/rss/articles/CBMi1wFBVV95cUxNX0JsTEFjeEpKWFRnRkwtZ1d5ajJLWUJDR1ZCeTJkTjh4ckctRXFTSW5ZYnduZ19HT0VwaDY4NE5tckZEVmN1amRvd18yR3h3bVBXeVltWTI2andCcUxPNEI3dFAzV2Z1TnZBMm0wQ3ZCOVdLMmc2eWgtNTMwREp1OXZlbHRNSnNQQjhsMlFMU1FXeHpDRElnbmg5aFI3M3BOZFZISTZsVjZoRVVfQm1CSW9HeTFmMkJtQnFhTlJGbmdmS3lnbTRmY09adjR3dnJQRUJqR3FMZw?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxOX0tJbXd0el94UVZKU2p6S21CdUVKUHRsWHlkajRucjlZZkt0SjRRdWFER3E1aWFNMFNQUTN5T3oxV2hKVmZuVFFuaVNUVFFUQnd6S0NCTUN0V0xweVRMT2VOYVoxeDR5aF9qem9hZ0RJamhPVDZhQ2tUREpucHBHWnZ6eGozRUxNUjJqSENtNTUyWDhramFOQWV1RldqNXczME5USE83cWYzMWQ5WXhqUnF0dw?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxNbUgxQkh0ZkRTNW9FNlV6TElsVVdudTRKcG9GYlVrYnF4dFNsMVB1LU0wdGVobGxYLTFuSWtSOEVhZThSYy11Q3lJUmRZYWF3V2I3cndtb3plS25NMmtleUxNR21DcFRwajZqR0E1bXFYS253VjVwTUNMRnJyeUtjb3F2Ulpzd3BnVWY1MHdkR2xncGRxMndDQ0prcll2VE5ndlBPVGpFakZIdmlUTU9RRkxB?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxPLUo5Q1VwbWpnem5zNTdRZDhselFCQkMzQ3QybXE2ZktONndGVGxyNXM4RUdETFhRQ19DNWRKRFp4aXNWYzJMZ2hmTjBEdF9DWl9uM1k4UmwyeE5GaGxfTTFyMzJUaXpYMWsyQlRoQU9wXzhZUHNNLWdmR05jNVRyTG1icy1ROW51S0pXRVM4cGFzSENTTzU2ZnU1b3hnZVliSHlNTW5nSEk?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxPcVltbDQ3cFpCTGFVY2dIZlVFZHFFZkdoODNLeWF0Vm5Ka1oyaWpiTzYxVndCSFMtQ1ZlT09UdUk0aGh4MkZudGExby05anN5ei10ZE5KaFM3Q3ZxZHZXaG1DQXRYeHdHUThQeEZLLUkyUDg1QmVuNGpVaEl1Xy1ObzZJWi1pb2lMMTZvUml2eFBOb1h4dVhuM1lsYXlFRjc3eWVVWEx2WQ?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxOQUJ1YjM5SGU5WHJuMVY0aFpHZF9zcWN2VGVPNGJ0RllUZVpmSy16M2drVHI3YlJDcTI3ZHVKQlZvYTQ2WFd2Sm1oUVAxWFAzRkE4VVRjRWRneUw1RDduREp3UlNOaUxpdlRhRFVSXzJKd3JUaU1TTHVTcDZhbERFSThPX1dncWQzUmxFZHllMUh0NHJ2ODU1OThiWQ?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxOaUR6ZDNoRFpjanljYXQ2UmlNTHgzek1xcloyVTdHd0FoWHBJNlBFQmJLMkhPSVpHOTNOSGR1dkt5MnVqSVZycFBZdlVWQ0JLMEpDd2c0Vi1JQmoyemprRGtYQmtaQ2VtdDRsbGdDa1RyMC1GT0MzdDhXV0NoelFGcWU1TmRxTDZIRGdsQnJhRzFFdWtoRkxpdFk5V0trUjJSckhYX2x4M0pUWGYxclVmM2F1bXVsZFZIQURFT0tWSlVFelpYYUHSAcsBQVVfeXFMTlU0c1J6VFJ2ZjFvWmRlNHZ5TXE1b2otOFF2VmdJRXRyaTFoS3hnQVEzcE0zOTc3Z1hWTFlFZlluWFFld2lwSTRzN3NYWUpfaTcyblEyZjZlQnJWNXd5SWFqaS1MdEtLU09wUUpobXl5ODVEUVlwWGlmaGN0VEtQVHJfbTk1NE9HNzZZSW02ZGFxcXFvMEt4Y2RQdlBuWXhMV1RFak4xazB2cnE4THFsTTJxaks1dkxWWnR5MHkwS0V1d2toOHpYRXhVRkE?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
