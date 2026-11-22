# JPM Intelligence Report

- ticker: **JPM**
- Report as_of: **2026-11-21**
- Market data as_of: **2026-11-20**
- Quant sources: https://finance.yahoo.com/quote/JPM/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/JPM/key-statistics/
- AI analysis snapshot as_of: **2026-11-21**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-22T05:10:16.768148+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 4, 'ai': 14, 'unknown': 0, 'irrelevant': 7})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **14** exact headline/source/date matches; prior report **20261121T053104Z-422ce34b/JPM** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 10 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 32.0%; oldest publication 2026-11-14

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
| Tracking error vs SPY (%) | 20.2815 |
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
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 20.2815 -> No interpretation rule is available for this metric.
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

### Jamie Dimon Just Said 5 Words Blocking Outside AI Agents From JPMorgan Accounts: "You Don't Want Rogue Agents." Here's Why That Security Stance Matters for JPM and Its Tech Rivals.
- Summary: JPM’s proactive AI security stance signals risk mitigation, potentially boosting investor confidence.
- Date: 2026-11-14 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxNQWQ4UlBOQ3VlbjFqcEpma1BDMjRRczVfalJRVWZaUjdyY2l0Rmw2NWtvb2gzVXZ2R2JTR09LSlFIcmd5aVh1NklOcU1BUGhVVTY3ZEFwdEdlcWZuLXZTbzNsOVoybXdOcDJTR3A3T2FvbDNaMmZZbmVTQTVGZGhCY3RGQVllZmN1ZG9DbXNfd090MzkwRHdR?oc=5>

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

## CATALYSTS

### JPMorgan Chase (JPM) Receives a Rating Update from a Top Analyst
- Summary: JPMorgan Chase (JPM) Receives a Rating Update from a Top Analyst
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi4gFBVV95cUxOLWJuTUEtb0ZadnJaSWJVekRwcnR5M3B1ODl3dGVvaXpQNDNsOTNzTC1wbGhHNGVUR0hNc2lnR0hMU3hRVm1lU1FyVnhsdzlOcUctYzBvanRRWEpOTWJKenVQcEF4RzBVdi1MOXFhakttbmthQWhhS1I4ZmFQOUFGX3V1UGU3b21xUlRsTWxVX3FwYnloelZDTmlCbEthX1lEME1nbm9ReXdqREtkM0xCY0FGWkhmbU1JVmJqMFNmaUtRNWNTY1VMclJzWExXSkNyN3UxR2ZwR3VKaW1VVFZNVXRR?oc=5>

### JPMorgan Chase & Co. $JPM Stock: Cibc World Market Inc. Cuts Position
- Summary: JPMorgan Chase & Co. $JPM Stock: Cibc World Market Inc. Cuts Position
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxOVG1uRXlnZExYY3JUM3hUbzM5SVdzbmZncnJyZEZZWXUwd1JWZ01hWE0wckVPYVlKNGpRMUxMWmw0cGs5eXc2dnZUd3I3SUtVSDN1U3dod1J6WFhtclVZczBUYk9hcDV2Z0JoTzIwWS1XcW5aeng4R3V4dWh5UmlRaWtmMlZMZkI1bWVCQ2I2d1lVb0R5dS1jdmNWMEdGVWpVTndnRnBhVGxpOWRpRzNaMGR2MFVNUkQ1OThrbU1nVHVlUQ?oc=5>

### JPMorgan Chase & Co. $JPM Shares Sold by Public Sector Pension Investment Board
- Summary: JPMorgan Chase & Co. $JPM Shares Sold by Public Sector Pension Investment Board
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0gFBVV95cUxOODJHNkNxRXZTaFhDT2ptdnZheDY3dmdZYzctTDlNN2hQc1kzVE0tbnpublI1cklZbWo5Q2tlaEFjU05NbG01ekxLSlIzQzFXdkpWaUN5RzVOMk93RDY5azFYblE0c29FQmZxUXhuODAzS1FDNzRYVWNOMWd5Tk9lOERpSExlYjBzeks2T3FnTEFXVmNnbTNsWk1xR2ZocWhlZl9rdzZNMHZicjhHTzZUQmlUMElGZ0w4WVZ3bW41TG5sdTM4T3gzOENmbFZrNmMyN0E?oc=5>

### JPMorgan Chase & Co. $JPM Stock: Danske Bank A S Cuts Holdings
- Summary: JPMorgan Chase & Co. $JPM Stock: Danske Bank A S Cuts Holdings
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxPZVAzZWJrQ2FHcmFZY0o4MTJHT2VsVzRGMWQ5WTNabHl5Rl9DQXdWNHkwTmhRSFpsbGZDTkF4dTV0S0d3RWFEMjNRYTREeG5uVUllOVpXQ0tMbFBFRXd4TFpueHY0UDJMcEJMek9IcFFOVF9aTHc3Y0lhUmFveVd4OWdqVmVNb2M5akFkem5fNVo5ejlPTUx4c05lVEUzUXZwN0huWDFWMkxUaUxseHY4UFE0LW5mV2lpeFE?oc=5>

### JP Morgan Chase & (JPM): Auto-callable note tied to lowest of three indices, due 2029
- Summary: JPM issues an auto-callable note linked to three indices, maturing 2029.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxQMzdFRGdmS3hBaDZSZ0xKRW5sZmJkVDdqbEVtTVJrblZveHlpbVRlZzc1OWhDSVBsNlVNQUxmM0x3dUpScmVfNTRqT2hncFpZU1U2U0Vnc3g5TEVjLXlreHcwdkFUWVhibktJa0xKWm0zZWw0ZHRUemV5aEgzdVpqVjZnWXJUMHBHalRJ?oc=5>

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

### JPM: SEC Form FWP filed by JP Morgan Chase & Co.
- Summary: JPM filed a regulatory Form FWP, indicating compliance activity.
- Date: 2026-11-20 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxPWEFndFgxWWpld0RGMnFfcjU5WjlNQkEyZFhvbHJYWFdTZldqMzBKd212VGVENFJFVm1FR215NHFLcUVvanY4di0xbU5EWEVwNGs2QkNrU2VqXzhyQ2poclBCOEFrdkpQdjZKaWZPZzVmU0puWWs5V0xzV1NFalRxRnV1MXYtTXFZRUI0?oc=5>

### JPMorgan Chase Financial Company LLC Declares Quarterly Coupon on Alerian MLP Index ETN
- Summary: JPM declared a quarterly coupon on an ETN, providing investors a dividend-like return.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxQOW1jbmc1R3N5QkszczFMYURJNjdMN2NSdE82bXdpaWJhMUFfZ3U0SzEwcVlFdFBlR0Nzdlp1QXdCYXdheXJQcmRVSGFBeGRnd1NxWFBFa2IwTXNwTGNQa0FwQldJV0FaamdiVjBJbjZMdHJtRlE0dW5xSnJsNWNBRmNrUnI4TTdNd2trRUo2cjAzTWEweDcwbXgzR3FnTmRTS3RCMmtfdkw1ODZSelZUd3JKRHZSeVk?oc=5>

### JPMorgan Chase & Co. $JPM Stock Position Cut by Voya Investment Management LLC
- Summary: Voya reduced its JPM holdings, signaling a change in ownership stakes.
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0AFBVV95cUxPMk1QYlFWakhOTmI0TlQ5czVXMU9QZVpCaTJaTXV4NXlsbzlqYldGcVhPVUNEazVrNXo4Z3l5aFBvem5yeE9SNFNCOUJYX1dQV1MwOTM3clhGUWNteTg1SnRraGVNeEdkT05RYkd3cWd4VlFZbGVCRmwwaG5DYVJOdkgtZndVSFZCbFRhMGdOWjRyd0MwS3B4ZkNGcTk4OGNUaS1odGJDa2c2dk9PUnJGeG1jc2ZmU2c3N0ROZUR1WDdoUVBPMVFFcWpjeGVMN05Z?oc=5>

## RISKS

### Visa, Mastercard, JPMorgan Hit By Reported Data Leak, Payment Information Not Affected
- Summary: JPMorgan, along with Visa and Mastercard, faced a reported data leak, though payment data remained secure. The incident raises security concerns and potential regulatory scrutiny.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxNemtoLTNrQVB1M1loZGQyaUtzUkdiZDVHNDBkRF8waURYakthUVpueGRSUTZGMnc1VVlscGVLeEtZRl93V1hXNzR5VkhNcmg2SUtyOXBQQWlJZnFnU2FwYzZlNktrM3NReXJCVEtaYTV1b0g2ZHVZUFVZY3FPMHlfRWVrNHVVeTZKWWt3QnM2LW45ZVU3QmxzelF4SmRRYUE?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **JPM** | **13.03** | **2.35** | **N/A** | **10.20** | **824,646,434,816.00 USD** | **6.08** |
| BAC | 11.23 | 1.20 | N/A | 3.40 | 324,585,848,832.00 USD | -5.80 |
| C | 10.78 | 0.96 | N/A | 8.00 | 183,098,720,256.00 USD | 15.65 |
| WFC | 11.09 | 1.49 | N/A | 0.40 | 236,005,490,688.00 USD | -2.44 |

Peers fetched as_of: 2026-11-21; JPM reuses existing data (market data as_of: 2026-11-20); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-13
- Next expected earnings: 2027-01-14 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-21

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
- https://news.google.com/rss/articles/CBMilwFBVV95cUxNQWQ4UlBOQ3VlbjFqcEpma1BDMjRRczVfalJRVWZaUjdyY2l0Rmw2NWtvb2gzVXZ2R2JTR09LSlFIcmd5aVh1NklOcU1BUGhVVTY3ZEFwdEdlcWZuLXZTbzNsOVoybXdOcDJTR3A3T2FvbDNaMmZZbmVTQTVGZGhCY3RGQVllZmN1ZG9DbXNfd090MzkwRHdR?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxPY25wTkZqdFZDWF93OFdXcFRsSmJWM0oybzR3b3N1OHZ1bURYVjlFZkoySHhQVkxrNjluVTBqQzNIQ2pGWGQwN0ZheXhvbk8yT18xQzYtaDhnSVJYTVA4VVQ4eUNkZDFzNDc5TW1fMXZsMzRGR0FnelpUaVZLeEhkNnpPd2RVLTNncEY4SGluTVA5dE5IbnF3aFFFdFFSQQ?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxNS1daVEN0SlZtVGhOUjZxSTI3TmhybWJYN3dIMkdOVUtYck1LQjhyRUNsMkdhMXo5dWFtUWRxUnVROFloQzI1Y3ZNRWpURFZwakNWM041ekhjTTc2c0JJN1FjRDdST3E4OUdWSk1SdERfWW00aUp6QVl0Q1dHTnNYMFlXQ3JNd0szM2hvSGpyOXM2dlFfR2NwV1VpVXRaS21FLUxzQ19DOHJkNXpNV3V2Uw?oc=5
- https://news.google.com/rss/articles/CBMi7wFBVV95cUxOMVlnOTBybnpvZDFpOUdlNnV3eG1vWm5yNjk3QThKandiQ2xSUDRKR3VsQWxGRUZIOWJqajRtMGhlY3Vmd0ZlTEtGRE5oM1VZQnBHeUhNaFVPVHZ5UmxaX2VUR3o5SUpNb2dBdHAyeW9pVE5tWGRZSklfQnRQZFlMMjIwQk5nRUd6Q3RNaEZwekdPQi1wVGJRU0JJZVVPUUl1dk85ZnF4YTNNTm43QW1pMEZMcXNhS1Rfbzh6VkR1VlVTRE1LQzZHREktU2xNWmRFamJYbXhHd25Wdkl0QUlIdjJiMXE4M25oME9YbGVxVQ?oc=5
- https://news.google.com/rss/articles/CBMi4gFBVV95cUxOLWJuTUEtb0ZadnJaSWJVekRwcnR5M3B1ODl3dGVvaXpQNDNsOTNzTC1wbGhHNGVUR0hNc2lnR0hMU3hRVm1lU1FyVnhsdzlOcUctYzBvanRRWEpOTWJKenVQcEF4RzBVdi1MOXFhakttbmthQWhhS1I4ZmFQOUFGX3V1UGU3b21xUlRsTWxVX3FwYnloelZDTmlCbEthX1lEME1nbm9ReXdqREtkM0xCY0FGWkhmbU1JVmJqMFNmaUtRNWNTY1VMclJzWExXSkNyN3UxR2ZwR3VKaW1VVFZNVXRR?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxOVG1uRXlnZExYY3JUM3hUbzM5SVdzbmZncnJyZEZZWXUwd1JWZ01hWE0wckVPYVlKNGpRMUxMWmw0cGs5eXc2dnZUd3I3SUtVSDN1U3dod1J6WFhtclVZczBUYk9hcDV2Z0JoTzIwWS1XcW5aeng4R3V4dWh5UmlRaWtmMlZMZkI1bWVCQ2I2d1lVb0R5dS1jdmNWMEdGVWpVTndnRnBhVGxpOWRpRzNaMGR2MFVNUkQ1OThrbU1nVHVlUQ?oc=5
- https://news.google.com/rss/articles/CBMi0gFBVV95cUxOODJHNkNxRXZTaFhDT2ptdnZheDY3dmdZYzctTDlNN2hQc1kzVE0tbnpublI1cklZbWo5Q2tlaEFjU05NbG01ekxLSlIzQzFXdkpWaUN5RzVOMk93RDY5azFYblE0c29FQmZxUXhuODAzS1FDNzRYVWNOMWd5Tk9lOERpSExlYjBzeks2T3FnTEFXVmNnbTNsWk1xR2ZocWhlZl9rdzZNMHZicjhHTzZUQmlUMElGZ0w4WVZ3bW41TG5sdTM4T3gzOENmbFZrNmMyN0E?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxPZVAzZWJrQ2FHcmFZY0o4MTJHT2VsVzRGMWQ5WTNabHl5Rl9DQXdWNHkwTmhRSFpsbGZDTkF4dTV0S0d3RWFEMjNRYTREeG5uVUllOVpXQ0tMbFBFRXd4TFpueHY0UDJMcEJMek9IcFFOVF9aTHc3Y0lhUmFveVd4OWdqVmVNb2M5akFkem5fNVo5ejlPTUx4c05lVEUzUXZwN0huWDFWMkxUaUxseHY4UFE0LW5mV2lpeFE?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxQMzdFRGdmS3hBaDZSZ0xKRW5sZmJkVDdqbEVtTVJrblZveHlpbVRlZzc1OWhDSVBsNlVNQUxmM0x3dUpScmVfNTRqT2hncFpZU1U2U0Vnc3g5TEVjLXlreHcwdkFUWVhibktJa0xKWm0zZWw0ZHRUemV5aEgzdVpqVjZnWXJUMHBHalRJ?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxOX0tJbXd0el94UVZKU2p6S21CdUVKUHRsWHlkajRucjlZZkt0SjRRdWFER3E1aWFNMFNQUTN5T3oxV2hKVmZuVFFuaVNUVFFUQnd6S0NCTUN0V0xweVRMT2VOYVoxeDR5aF9qem9hZ0RJamhPVDZhQ2tUREpucHBHWnZ6eGozRUxNUjJqSENtNTUyWDhramFOQWV1RldqNXczME5USE83cWYzMWQ5WXhqUnF0dw?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxNbUgxQkh0ZkRTNW9FNlV6TElsVVdudTRKcG9GYlVrYnF4dFNsMVB1LU0wdGVobGxYLTFuSWtSOEVhZThSYy11Q3lJUmRZYWF3V2I3cndtb3plS25NMmtleUxNR21DcFRwajZqR0E1bXFYS253VjVwTUNMRnJyeUtjb3F2Ulpzd3BnVWY1MHdkR2xncGRxMndDQ0prcll2VE5ndlBPVGpFakZIdmlUTU9RRkxB?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxPalR2WVhHOTNiT3R5MUU4ZWtxaUs3UWxjbFA3Ylg2Ti1tWDJRaHl1YXRmRmVHcEcxQURvU2EtcVM5MFNlQTRzNUdGZWNWRU9mX2l5OVoyaVphektVRTR2R2tJa2dhbzRDMThOT3ZGVkZFRTN6UnpZcVd4bldYZTJNWjQyb3hyd05jQnhEM0pMODNOUnVxTUVWRW1WZ1p1bU1SU2RXVw?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxQU1ctTHZIMkJYenpSU2NxUHkxbGVHbzFaUEM1czlaVG5sN1F6VWpwbEpPd0NxTjFUUGlLc1ZVZDBLVGdEa21zTDRET195R29IM3U4TkdlWDFNWjlFeTBYZVM5aFVkM0prdGI4RWJUUUtrYm43a1BjdlFGSkpRRXJlbDlUbnpkSXl0NUJlcGp2aWZCR1k5eHFmOVB6VFgyTG10MWRqMXc1ajRMZ294ZUN4MUpJWnR1MXVmMUJHOG5GM09DbmZi0gHKAUFVX3lxTFB2Y1poVVNOaVk3cHE1eExtbW91cFQtQ3JmRXRoMVIxb3kxRVo5QXctNUJSNDl4dVFRejIzTndFMUVKd0hJMDZ4d2d1NG9sRktXUTdRc1A0d1psSkRaNWJuRUVEQm1VX1ZaRF8yMEN1MWVDTVQ0U1RtVWFEMDlCLWd5N3FvQWJreXFXaENUWENkYlM4ZWpkNlFFRnJrYzFJalhsdndERE1LUkNxeVQ0SWN0bGdCOWdpRWs5MjZiOUo3MzVLbDFPVktMN1E?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxPWEFndFgxWWpld0RGMnFfcjU5WjlNQkEyZFhvbHJYWFdTZldqMzBKd212VGVENFJFVm1FR215NHFLcUVvanY4di0xbU5EWEVwNGs2QkNrU2VqXzhyQ2poclBCOEFrdkpQdjZKaWZPZzVmU0puWWs5V0xzV1NFalRxRnV1MXYtTXFZRUI0?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxQOW1jbmc1R3N5QkszczFMYURJNjdMN2NSdE82bXdpaWJhMUFfZ3U0SzEwcVlFdFBlR0Nzdlp1QXdCYXdheXJQcmRVSGFBeGRnd1NxWFBFa2IwTXNwTGNQa0FwQldJV0FaamdiVjBJbjZMdHJtRlE0dW5xSnJsNWNBRmNrUnI4TTdNd2trRUo2cjAzTWEweDcwbXgzR3FnTmRTS3RCMmtfdkw1ODZSelZUd3JKRHZSeVk?oc=5
- https://news.google.com/rss/articles/CBMi0AFBVV95cUxPMk1QYlFWakhOTmI0TlQ5czVXMU9QZVpCaTJaTXV4NXlsbzlqYldGcVhPVUNEazVrNXo4Z3l5aFBvem5yeE9SNFNCOUJYX1dQV1MwOTM3clhGUWNteTg1SnRraGVNeEdkT05RYkd3cWd4VlFZbGVCRmwwaG5DYVJOdkgtZndVSFZCbFRhMGdOWjRyd0MwS3B4ZkNGcTk4OGNUaS1odGJDa2c2dk9PUnJGeG1jc2ZmU2c3N0ROZUR1WDdoUVBPMVFFcWpjeGVMN05Z?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxNemtoLTNrQVB1M1loZGQyaUtzUkdiZDVHNDBkRF8waURYakthUVpueGRSUTZGMnc1VVlscGVLeEtZRl93V1hXNzR5VkhNcmg2SUtyOXBQQWlJZnFnU2FwYzZlNktrM3NReXJCVEtaYTV1b0g2ZHVZUFVZY3FPMHlfRWVrNHVVeTZKWWt3QnM2LW45ZVU3QmxzelF4SmRRYUE?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
