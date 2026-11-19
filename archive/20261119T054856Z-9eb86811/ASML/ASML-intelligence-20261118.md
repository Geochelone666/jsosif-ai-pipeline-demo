# ASML Intelligence Report

- ticker: **ASML**
- Report as_of: **2026-11-18**
- Market data as_of: **2026-11-18**
- Quant sources: https://finance.yahoo.com/quote/ASML/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/ASML/key-statistics/
- AI analysis snapshot as_of: **2026-11-18**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-19T05:54:53.177840+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 6, 'ai': 12, 'unknown': 0, 'irrelevant': 7})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **10** exact headline/source/date matches; prior report **20261118T054934Z-e0d070d9/ASML** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 15 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 20.0%; oldest publication 2026-11-14

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 1395.2700 |
| Return 1D (%) | 0.8792 |
| Return 1W (%) | -9.0686 |
| Return 1M (%) | -14.8892 |
| Return YTD (%) | 31.2155 |
| Return 1Y (%) | 39.8146 |
| Annualized volatility (%) | 49.0364 |
| Beta vs SPY | 2.3029 |
| Max drawdown (%) | -31.6292 |
| Sharpe (rf=0) | 0.9309 |
| Downside deviation (rf=0, %) | 33.3755 |
| Sortino (rf=0) | 1.3678 |
| Historical VaR 95% (1D, %) | 5.0034 |
| Historical ES 95% (1D, %) | 6.5779 |
| Correlation vs SPY | 0.6461 |
| Tracking error vs SPY (%) | 41.4991 |
| P/E (trailing) | 34.33 |
| P/B | 1198.05 |
| EV/EBITDA | 1834.57 |
| Revenue growth (%) | 55.20 |
| Forward P/E (estimate) | 22.01 |
| Gross margin (%) | 54.34 |
| Operating margin (%) | 38.55 |
| Return on equity (%) | 65.64 |
| Free cash flow yield (%) | N/A |
| MA50 | 1638.5262 |
| Close vs MA50 (%) | -14.8460 |
| MA200 | 1597.8139 |
| Close vs MA200 (%) | -12.6763 |
| RSI (14, Wilder) | 36.2653 |
| MACD (12,26) | -67.3233 |
| MACD signal (9) | -59.7413 |
| MACD histogram | -7.5820 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'ASML': 285, 'SPY': 285}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 1395.2700 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.8792 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -9.0686 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -14.8892 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 31.2155 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 39.8146 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 49.0364 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 33.3755 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.3678 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 5.0034 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 6.5779 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6461 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 41.4991 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 2.3029 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -31.6292 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.9309 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 22.0077 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 54.3370 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 38.5520 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 65.6360 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 34.3324 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 36.2653 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -7.5820 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -14.8460 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -12.6763 -> Clearly below the moving-average trend level.

## TAILWINDS

### ASML emerges as a top AI stock pick as volatility hits ahead of the Anthropic IPO
- Summary: ASML emerges as a top AI stock pick as volatility hits ahead of the Anthropic IPO
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMia0FVX3lxTFA5SzAtRE1SMDIyUEh3QjI3VEJWMmEza0xyRFYzQWdqRXRzcnFoQWpqRXltVnZKYW80aDN4WTdRNlZLZDhpTjhxaFhEQW1FMXd5RnZMeWJHTGVKZHRuSmM1NEJPWk1XVUhSaTJ3?oc=5>

### ASML Holding N.V. : Gets a Buy rating from Bernstein
- Summary: Bernstein upgrades ASML to Buy, signaling positive outlook.
- Date: 2026-11-17 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxPRXVRS2duSzVqMXNJdHNNNzJUVVlUdzFuQkhHQzYxdWVLTGFqYnJzSDE2YzR5cnRTYkY4VXNlVGJ3M3FUemJfanFNVGo2WG9uT19mUndubU5GV3N4OFcta21GeVBQSTVKeHFMU2Z3M2Z0Y3kwQVhYX3UxVWlpN0g4QW9OMXpBRHZqMGZBMGllSFpQQS1POFZsREg3QnBMb0I1LVZnZA?oc=5>

### ASML Soars 10% in a Week as Chip Stocks Bounce and Musk’s Terafab Eyes a Million Wafers
- Summary: ASML shares jumped 10% amid positive market sentiment and optimism about chip demand.
- Date: 2026-11-14 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxPaFhnU3VhU3lYbkxKUHRsQUZZN004VXEtbXFmOXpLa0sybHBaLVZPQTQzSVR6cUVCcXJpVUxCckFjVUt4a2FUMlhWQkFpZ2xHLVhyREg4MHAyX1FIX1g3VFo1V3FxcTctZTAyYzVjbGJHSExuZ0V0Ull1NTFKY004eWFKRDlXVFkwT3ZVQ19RUmMtTkZpUl92dVlhX2pYUEVxRmRnblpPbFJ5bmhib0l5Tg?oc=5>

## HEADWINDS

### ASML Stocks Fall 2.72% as New US Rule Tightens the Chip Supply Chain It Serves
- Summary: ASML Stocks Fall 2.72% as New US Rule Tightens the Chip Supply Chain It Serves
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0wFBVV95cUxNc1M2Mmc5Y2VDRFZPZ2R1QmlKRkhmeDg5Xzh3NTV2VDlHT2ZHRW1mTHE0LVlWZzJoZlRBMkxYNjFod0tNNkNCV1VmNE1lSTlWbnlySWJ2UW0wazhIMXBSbmQ5VmVJT2ppQjRYakY4SGpvRDJROC1nYlNzOEV4WjRabHVWLXd3Y3Vha0t3ZFM4TnVBY0tfeVhuZm41M2diWDdfdjE5eVJTNmhMYTZ2SGIyalFUQnVWcmpBUDVVWUNNbHZKU3I1eWpoZzZrQVgyYUJTcHUw?oc=5>

### ASML Holding falls 2.41% in Monday's session
- Summary: ASML Holding falls 2.41% in Monday's session
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihAFBVV95cUxPaEktdGVqODJOdjQxa0x5T3ItTGRwUlFud2xhMWcxblRYVWV6RUpoOFdSbUtoR09VSDJqZVQtWS1XdElya2dydjR6TkU1MlhSdlo2eFNRODFtQUk4ek40QXkxVTZ2czRaeC1kV1NqT2lSQ09YVWRaakE3bGg4SXRyalFjT0E?oc=5>

### ASML slides as broader chip selloff appears to pressure shares
- Summary: ASML slides as broader chip selloff appears to pressure shares
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxON3V1T0l4QmtndUVSMHM1RzJWalliN3BIaDlFTExiQnpELUI4Y2Yyc2UzVk9XbnczcGx3RzFjN3BPN3dhTWotOG42MWQybE5iQW5NTEE3Y19ZTzFBbV9weW9tcnRocmdEdWlfY0RlT0M5Q1R3SlRwbmRxWWhFZUZQcmVLS1VUbFNnUVpaV0EzamJUZjhPU3pvd0o3WQ?oc=5>

### ASML Holding NV (ASML) Shares Fall 5.9% -- What GF Score of 97 T
- Summary: ASML Holding NV (ASML) Shares Fall 5.9% -- What GF Score of 97 T
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxNS1JVYW1TU2RuaUI5S1Z6YmE0WktQa3NKWTJtc0cycVBuMnNhTi0ydTNLeEc1eEhzUENMa3U0TG9tUmMwZW9QM3M0Q2tlRG1PSmRGZTd0UU15SjZhUlhSVEh6blJCeGpaU01PRnVBOXRNbkZaMldTQU02azBwb016RHd1RXFybk54QW94MnFCQkREZUJlUFlfOXRKLUZLc19GQkxxbF9hbzFZMTRPMW9v?oc=5>

### Why is ASML stock sliding today?
- Summary: Investors question the factors behind ASML's recent share price decline.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxPUjUxQVlLLUhQRlhhbDhiazlZempiRGR3ZnNRT2JmWmdsTG9sUWpHN1UyS29rRHVEVGNQUjR4eEpGZ3BpcnFBVmV6Vnp3RDNuS0Y4ZXZCWGVRVEV4Y24wRUtyYmhWemVsRXFRa1JRdVBaRTNYNktHWi1zaVVSTTdSTTFkMUpPUDRnSExpM3hnRDh0bnluZDR2UQ?oc=5>

### ASML Holding NV Stock (ASML) Moved Down by 3.02% on Nov 17: What Investors Need To Know
- Summary: ASML shares fell 3.02% on Nov 17, prompting investors to assess reasons for the decline.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxOaHFra2Y3LUFrdVY3ejF4TnptNmhHOVFXV0Z0c1RYQ0s2eXlWYmJ1YzZfTG9aeFNyN3ZoVHhZZGZmdjhwaVZ3dTNGY3dpWUNWbEJGd1RQNklnVVE3LUJ3TGVubzIwZWxfNTdhUE1CbXAxd21lZ3JIR1I2ZE1XanRxemx1anlfU0xFN2VR?oc=5>

### ASML Plunged 17% Lower Over 3 Months: This Wall Street Desk Expects 88% Gains Over the Next 12
- Summary: ASML shares fell 17% over three months, reflecting short‑term negative market pressure.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0AFBVV95cUxNUmtfcVVoWkt3b3VrbzdVM1g2STlWM2lpeXp0Vm5BY2ZsOG51S3dXbVVYZ242S2lnS0ludXFjQzduenc2OHM0alFmY1Rxb3EzRDh5UHpHbU1Ea1oyc0JNVTRreTl2MWxjWDlVamdzRk9mZnZCZ1BNNnl6WTJUTUdLR3lPUGpFLU5NWEtQcFI0bmxLOWliWGd1bF9fWEZ6QWVwdHV3V29TbndCSWpqeTJCVG5qaU95QUI1R0JlM0JmaTVqVXQxZ3FhLUlBLVlxWG95?oc=5>

### ASML Holding NV Stock (ASML) Opened Down by 3.69% on Nov 16: Key Drivers Unveiled
- Summary: ASML stock opened 3.69% lower on Nov 16, indicating short‑term negative market reaction.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxQR2xLMTJ3cHZWbUtmUWdBdEplc3ZqeEJzR0h1TWhLRTZEUzVSQ0ZzN0hObmRtX0ZJdUgzTFJIUHJZLVJ6VFU2U2k5VkhWZllCNXN2Mm1TOXFaam1Yb3BVSHh4NUNQcmo1QUxDcW1wcnJaUHdJVmlIMWVVWHd6b3VuVm0wUENSMnoxTWZj?oc=5>

### Can ASML Holding (ENXTAM:ASML) Stay Cheap Enough on Cash Flow?
- Summary: Questioning ASML's ability to maintain low cash flow costs amid rising expenses.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxNN3J5SkhiTk5hdmRyUTVuREItYmxSMEszWWFCS29RTHVWZ001WTlaa2tUZ1V2c0hoVDBQNTROYTBMU2dRQWpSRzVnTXVzVnlLclZ6VnNEbDJuUUtjYlNtWWM2SkhfYVo3ZXpBSk0tS1VjTjRfUU5iZldJUl9rQ3lMMTBGbzVUZUJEUG9CV2xlSExYQ3FFRkhkOGNwLWZLdjBWN1VFSHN0NkdkYzV3cFo0NkNEbVdtWTYxQ2F2Ry1EOUpqcVVwekJBeWJJZGdpQ0tmcmdGZm9n0gHbAUFVX3lxTE1yM2NwbDYySThYQzJzTHNvYVJWbkY4dnFoZUNaVmZ1bTRlY2JCRzkyeEU0TS12RngzejdzR0I1S1FvY3JMYnBIU3E0UjlGUUhwY0ZmWVJxbXd6QWI0bTdvOVI4cjJGVFdqX043MzdhTThBX1E1NDlnVmtBQmIzdGU2bGxSRWRSRnBZME1nVlNCZFZ4cjB2M085d1VhYWljYmhoU3RXb2xsdWhmb2JLSjJVN0JOX0NzbXBSMlo4QXlNMzIzRWpmTTdBZkNqRlczTjdFNzNJRVFzMWdnVQ?oc=5>

## CATALYSTS

### ASML's Buyback Ticks Along While the Real Risk Sits in a Maintenance Clause
- Summary: ASML's Buyback Ticks Along While the Real Risk Sits in a Maintenance Clause
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi4AFBVV95cUxQOTl6SVFBcHNHUFc4YktjNXMybTlSZmJPcll5QTUyel9VNXJ2QlhJM0Q0SldJUnNLS3plS2k0Zkc1RjJPTDd3VzNZZHRvVmVTWTR1bklxUzVva1Bwd3c2Mk1yQ0llY0plbmw0QWUyLW9ZVkRkV0Npb0lmMHN0MFlZMWZxRTloQVROTkRJZk1zTGEtbTZPakJjcHQ3SzRrM2llb3A4U2o5dW9xQTdFS1hLQmk3ZTZISHN0MlNWN3Q3YktzajlzNjdrUE5iSGhrRjljb1RLNzdnZXlOYU13OF91SQ?oc=5>

### ASML Stock Price Prediction: Q3 strength collides with a bearish tape
- Summary: Q3 earnings expected to be strong, but market sentiment remains bearish.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxQR25vZXVkdHJ2d21FdFphRzAwRmJ1bmE4M0tzRV9VTmFDSUNoamRoQ0UxeUU0bVRkbXUwOTU3S2FMUWRBYUMwbWphNWxQNXY4QVlncXZYYkNZLU51UTFOZlktOVp1WC1sUmIyVlBka0NDbWNHYzNDb3p3U0RZaTdSUVVTblN2TUFXMlhZWTJyVmQ4eGxUU01HMHB0UQ?oc=5>

### ASML Stock Price Prediction: AI demand lifts guidance, but price action is still repairing damage
- Summary: AI demand boosts guidance, yet price action remains in recovery phase.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxNNE16OG80X3h6Um83WXp0LWpBVFllcXE0RmlmNjFnNHU2NVVSbV95WmlleXE1bGNuRE1hUVl3T196MDNGZDF6al9NeVlSYnRyUzBFXzdpQWVjaUlLTERteE1aQ0IwSnhtcVpxRlBZdnZiZWgwdXhmYWtCTlp3UHE5ZEdoR3p1c3RUT0JwWHdPdEZ2d3RCZWl5VVc4aVhSYU13VlRF?oc=5>

### ASML Stock Price Prediction: ASML lifts guidance again as the stock tests lower support
- Summary: ASML raises guidance, indicating positive outlook.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxQOWY1cDlwVWExLTUwUHFTUXpTa0ZUVDMtRkxVaExqdHNWY0FZMDByWXdVaXpUTV9pTmdqN3d1S2VMTUtmR0VvRWxnWENxRnE2TUhfQktYNm5LNlFaUUZzSGlvZHVYb1FYSDRveE5YTE04S3ZmSy1KMjZHR1ZhZzF2cTdLd05aN1ZQd1dKamh5Y2FnaXk4QUpR?oc=5>

## RISKS

### ASML Holding stock: US chip rules add China risk
- Summary: US chip regulations increase China risk for ASML.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxOUjJHbWVFbTVoSk5Ddl9NRVUyb0xFeUJGdTU0cDhNVWJHNWZXOVRtekNjZElvTEM4MjlBSjFQRVFmXzlfanVlSXdkQks2RVNvQlJhTzZIOXdFTnhRb2V6QlZfX1VrcllzRG10c3ZaeTlxekJ4WERoWU9wZExnblJfaVJicGR3V3hYVDlTaTlsdEZvTmZkX0tKT0dKSi1ENVduWC14cHhndWI1MkRnaVhV?oc=5>

### ASML's AI Demand Story Meets Its Political Ceiling
- Summary: Political limits curb AI demand growth for ASML.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxNV3pDRmlCMEFKOWdqbUxJZ3oyempzSUt6T1dyNUlDNGJqeGZiWXRjSlZGU2p6aUxCR1Eyb0QwcnRDMnRId0RxaGVVNUhRZE5yMk5QTkU5TXpMaU9IS2ZtVnJWdms4TXRNbm5Xc0hWT0pRd3pMS01INE1ZZkFWZTkzSXJxVS1nX3dHRXNMUmp0MXN6U3pLTmo2MHBCTlpNWWhYWmQxTW1rb0MyREtBbWNBOWt0U1R3dzFOWW1GWFcybw?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **ASML** | **34.33** | **1,198.05** | **1,834.57** | **55.20** | **537,761,808,384.00 USD** | **39.81** |
| AMAT | 27.92 | 10.70 | 23.20 | 53.10 | 279,584,374,784.00 USD | 57.36 |
| LRCX | 31.41 | 19.01 | 25.77 | 54.40 | 264,412,004,352.00 USD | 48.46 |
| KLAC | 36.31 | 28.95 | 28.88 | 28.90 | 188,773,203,968.00 USD | 29.68 |

Peers fetched as_of: 2026-11-18; ASML reuses existing data (market data as_of: 2026-11-18); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-14
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-18

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: N/A
- Filing date: N/A
- Revenue (latest available single quarter): N/A
- Net income (latest available single quarter): N/A
- SEC link: N/A

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMia0FVX3lxTFA5SzAtRE1SMDIyUEh3QjI3VEJWMmEza0xyRFYzQWdqRXRzcnFoQWpqRXltVnZKYW80aDN4WTdRNlZLZDhpTjhxaFhEQW1FMXd5RnZMeWJHTGVKZHRuSmM1NEJPWk1XVUhSaTJ3?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxPRXVRS2duSzVqMXNJdHNNNzJUVVlUdzFuQkhHQzYxdWVLTGFqYnJzSDE2YzR5cnRTYkY4VXNlVGJ3M3FUemJfanFNVGo2WG9uT19mUndubU5GV3N4OFcta21GeVBQSTVKeHFMU2Z3M2Z0Y3kwQVhYX3UxVWlpN0g4QW9OMXpBRHZqMGZBMGllSFpQQS1POFZsREg3QnBMb0I1LVZnZA?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxPaFhnU3VhU3lYbkxKUHRsQUZZN004VXEtbXFmOXpLa0sybHBaLVZPQTQzSVR6cUVCcXJpVUxCckFjVUt4a2FUMlhWQkFpZ2xHLVhyREg4MHAyX1FIX1g3VFo1V3FxcTctZTAyYzVjbGJHSExuZ0V0Ull1NTFKY004eWFKRDlXVFkwT3ZVQ19RUmMtTkZpUl92dVlhX2pYUEVxRmRnblpPbFJ5bmhib0l5Tg?oc=5
- https://news.google.com/rss/articles/CBMi0wFBVV95cUxNc1M2Mmc5Y2VDRFZPZ2R1QmlKRkhmeDg5Xzh3NTV2VDlHT2ZHRW1mTHE0LVlWZzJoZlRBMkxYNjFod0tNNkNCV1VmNE1lSTlWbnlySWJ2UW0wazhIMXBSbmQ5VmVJT2ppQjRYakY4SGpvRDJROC1nYlNzOEV4WjRabHVWLXd3Y3Vha0t3ZFM4TnVBY0tfeVhuZm41M2diWDdfdjE5eVJTNmhMYTZ2SGIyalFUQnVWcmpBUDVVWUNNbHZKU3I1eWpoZzZrQVgyYUJTcHUw?oc=5
- https://news.google.com/rss/articles/CBMihAFBVV95cUxPaEktdGVqODJOdjQxa0x5T3ItTGRwUlFud2xhMWcxblRYVWV6RUpoOFdSbUtoR09VSDJqZVQtWS1XdElya2dydjR6TkU1MlhSdlo2eFNRODFtQUk4ek40QXkxVTZ2czRaeC1kV1NqT2lSQ09YVWRaakE3bGg4SXRyalFjT0E?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxON3V1T0l4QmtndUVSMHM1RzJWalliN3BIaDlFTExiQnpELUI4Y2Yyc2UzVk9XbnczcGx3RzFjN3BPN3dhTWotOG42MWQybE5iQW5NTEE3Y19ZTzFBbV9weW9tcnRocmdEdWlfY0RlT0M5Q1R3SlRwbmRxWWhFZUZQcmVLS1VUbFNnUVpaV0EzamJUZjhPU3pvd0o3WQ?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxNS1JVYW1TU2RuaUI5S1Z6YmE0WktQa3NKWTJtc0cycVBuMnNhTi0ydTNLeEc1eEhzUENMa3U0TG9tUmMwZW9QM3M0Q2tlRG1PSmRGZTd0UU15SjZhUlhSVEh6blJCeGpaU01PRnVBOXRNbkZaMldTQU02azBwb016RHd1RXFybk54QW94MnFCQkREZUJlUFlfOXRKLUZLc19GQkxxbF9hbzFZMTRPMW9v?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxPUjUxQVlLLUhQRlhhbDhiazlZempiRGR3ZnNRT2JmWmdsTG9sUWpHN1UyS29rRHVEVGNQUjR4eEpGZ3BpcnFBVmV6Vnp3RDNuS0Y4ZXZCWGVRVEV4Y24wRUtyYmhWemVsRXFRa1JRdVBaRTNYNktHWi1zaVVSTTdSTTFkMUpPUDRnSExpM3hnRDh0bnluZDR2UQ?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxOaHFra2Y3LUFrdVY3ejF4TnptNmhHOVFXV0Z0c1RYQ0s2eXlWYmJ1YzZfTG9aeFNyN3ZoVHhZZGZmdjhwaVZ3dTNGY3dpWUNWbEJGd1RQNklnVVE3LUJ3TGVubzIwZWxfNTdhUE1CbXAxd21lZ3JIR1I2ZE1XanRxemx1anlfU0xFN2VR?oc=5
- https://news.google.com/rss/articles/CBMi0AFBVV95cUxNUmtfcVVoWkt3b3VrbzdVM1g2STlWM2lpeXp0Vm5BY2ZsOG51S3dXbVVYZ242S2lnS0ludXFjQzduenc2OHM0alFmY1Rxb3EzRDh5UHpHbU1Ea1oyc0JNVTRreTl2MWxjWDlVamdzRk9mZnZCZ1BNNnl6WTJUTUdLR3lPUGpFLU5NWEtQcFI0bmxLOWliWGd1bF9fWEZ6QWVwdHV3V29TbndCSWpqeTJCVG5qaU95QUI1R0JlM0JmaTVqVXQxZ3FhLUlBLVlxWG95?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxQR2xLMTJ3cHZWbUtmUWdBdEplc3ZqeEJzR0h1TWhLRTZEUzVSQ0ZzN0hObmRtX0ZJdUgzTFJIUHJZLVJ6VFU2U2k5VkhWZllCNXN2Mm1TOXFaam1Yb3BVSHh4NUNQcmo1QUxDcW1wcnJaUHdJVmlIMWVVWHd6b3VuVm0wUENSMnoxTWZj?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxNN3J5SkhiTk5hdmRyUTVuREItYmxSMEszWWFCS29RTHVWZ001WTlaa2tUZ1V2c0hoVDBQNTROYTBMU2dRQWpSRzVnTXVzVnlLclZ6VnNEbDJuUUtjYlNtWWM2SkhfYVo3ZXpBSk0tS1VjTjRfUU5iZldJUl9rQ3lMMTBGbzVUZUJEUG9CV2xlSExYQ3FFRkhkOGNwLWZLdjBWN1VFSHN0NkdkYzV3cFo0NkNEbVdtWTYxQ2F2Ry1EOUpqcVVwekJBeWJJZGdpQ0tmcmdGZm9n0gHbAUFVX3lxTE1yM2NwbDYySThYQzJzTHNvYVJWbkY4dnFoZUNaVmZ1bTRlY2JCRzkyeEU0TS12RngzejdzR0I1S1FvY3JMYnBIU3E0UjlGUUhwY0ZmWVJxbXd6QWI0bTdvOVI4cjJGVFdqX043MzdhTThBX1E1NDlnVmtBQmIzdGU2bGxSRWRSRnBZME1nVlNCZFZ4cjB2M085d1VhYWljYmhoU3RXb2xsdWhmb2JLSjJVN0JOX0NzbXBSMlo4QXlNMzIzRWpmTTdBZkNqRlczTjdFNzNJRVFzMWdnVQ?oc=5
- https://news.google.com/rss/articles/CBMi4AFBVV95cUxQOTl6SVFBcHNHUFc4YktjNXMybTlSZmJPcll5QTUyel9VNXJ2QlhJM0Q0SldJUnNLS3plS2k0Zkc1RjJPTDd3VzNZZHRvVmVTWTR1bklxUzVva1Bwd3c2Mk1yQ0llY0plbmw0QWUyLW9ZVkRkV0Npb0lmMHN0MFlZMWZxRTloQVROTkRJZk1zTGEtbTZPakJjcHQ3SzRrM2llb3A4U2o5dW9xQTdFS1hLQmk3ZTZISHN0MlNWN3Q3YktzajlzNjdrUE5iSGhrRjljb1RLNzdnZXlOYU13OF91SQ?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxQR25vZXVkdHJ2d21FdFphRzAwRmJ1bmE4M0tzRV9VTmFDSUNoamRoQ0UxeUU0bVRkbXUwOTU3S2FMUWRBYUMwbWphNWxQNXY4QVlncXZYYkNZLU51UTFOZlktOVp1WC1sUmIyVlBka0NDbWNHYzNDb3p3U0RZaTdSUVVTblN2TUFXMlhZWTJyVmQ4eGxUU01HMHB0UQ?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxNNE16OG80X3h6Um83WXp0LWpBVFllcXE0RmlmNjFnNHU2NVVSbV95WmlleXE1bGNuRE1hUVl3T196MDNGZDF6al9NeVlSYnRyUzBFXzdpQWVjaUlLTERteE1aQ0IwSnhtcVpxRlBZdnZiZWgwdXhmYWtCTlp3UHE5ZEdoR3p1c3RUT0JwWHdPdEZ2d3RCZWl5VVc4aVhSYU13VlRF?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxQOWY1cDlwVWExLTUwUHFTUXpTa0ZUVDMtRkxVaExqdHNWY0FZMDByWXdVaXpUTV9pTmdqN3d1S2VMTUtmR0VvRWxnWENxRnE2TUhfQktYNm5LNlFaUUZzSGlvZHVYb1FYSDRveE5YTE04S3ZmSy1KMjZHR1ZhZzF2cTdLd05aN1ZQd1dKamh5Y2FnaXk4QUpR?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxOUjJHbWVFbTVoSk5Ddl9NRVUyb0xFeUJGdTU0cDhNVWJHNWZXOVRtekNjZElvTEM4MjlBSjFQRVFmXzlfanVlSXdkQks2RVNvQlJhTzZIOXdFTnhRb2V6QlZfX1VrcllzRG10c3ZaeTlxekJ4WERoWU9wZExnblJfaVJicGR3V3hYVDlTaTlsdEZvTmZkX0tKT0dKSi1ENVduWC14cHhndWI1MkRnaVhV?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxNV3pDRmlCMEFKOWdqbUxJZ3oyempzSUt6T1dyNUlDNGJqeGZiWXRjSlZGU2p6aUxCR1Eyb0QwcnRDMnRId0RxaGVVNUhRZE5yMk5QTkU5TXpMaU9IS2ZtVnJWdms4TXRNbm5Xc0hWT0pRd3pMS01INE1ZZkFWZTkzSXJxVS1nX3dHRXNMUmp0MXN6U3pLTmo2MHBCTlpNWWhYWmQxTW1rb0MyREtBbWNBOWt0U1R3dzFOWW1GWFcybw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
