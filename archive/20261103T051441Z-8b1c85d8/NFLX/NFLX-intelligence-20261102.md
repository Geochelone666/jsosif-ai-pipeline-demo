# NFLX Intelligence Report

- ticker: **NFLX**
- Report as_of: **2026-11-02**
- Market data as_of: **2026-11-02**
- Quant sources: https://finance.yahoo.com/quote/NFLX/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NFLX/key-statistics/
- AI analysis snapshot as_of: **2026-11-02**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-03T05:20:01.016622+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 4, 'ai': 17, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **11** exact headline/source/date matches; prior report **20261102T041627Z-c84a7052/NFLX** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **10**; {'directional_claim_without_event_type': 4, 'low_uncalibrated_model_confidence': 6}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 9 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 29.17%; oldest publication 2026-10-26

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 62.3400 |
| Return 1D (%) | 0.4188 |
| Return 1W (%) | -2.4413 |
| Return 1M (%) | -7.0385 |
| Return YTD (%) | -33.5111 |
| Return 1Y (%) | -44.2826 |
| Annualized volatility (%) | 35.8330 |
| Beta vs SPY | 0.1894 |
| Max drawdown (%) | -46.4449 |
| Sharpe (rf=0) | -1.4181 |
| Downside deviation (rf=0, %) | 26.4410 |
| Sortino (rf=0) | -1.9218 |
| Historical VaR 95% (1D, %) | 3.5205 |
| Historical ES 95% (1D, %) | 5.1308 |
| Correlation vs SPY | 0.0678 |
| Tracking error vs SPY (%) | 37.2307 |
| P/E (trailing) | 18.02 |
| P/B | 8.74 |
| EV/EBITDA | 16.63 |
| Revenue growth (%) | 11.80 |
| Forward P/E (estimate) | 16.53 |
| Gross margin (%) | 50.69 |
| Operating margin (%) | 34.63 |
| Return on equity (%) | 53.46 |
| Free cash flow yield (%) | 9.81 |
| MA50 | 72.3276 |
| Close vs MA50 (%) | -13.8088 |
| MA200 | 81.4678 |
| Close vs MA200 (%) | -23.4790 |
| RSI (14, Wilder) | 31.7852 |
| MACD (12,26) | -2.7541 |
| MACD signal (9) | -2.3017 |
| MACD histogram | -0.4524 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NFLX': 273, 'SPY': 273}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 62.3400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.4188 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -2.4413 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -7.0385 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -33.5111 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -44.2826 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 35.8330 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 26.4410 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -1.9218 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.5205 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.1308 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.0678 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 37.2307 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.1894 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -46.4449 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -1.4181 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 16.5299 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 50.6850 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 34.6320 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 53.4630 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 9.8142 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 18.0173 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 31.7852 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.4524 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -13.8088 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -23.4790 -> Clearly below the moving-average trend level.

## TAILWINDS

### The Battle That May Matter Most for Netflix Stock Isn't Against Disney
- Summary: Explores other competitors impacting Netflix stock beyond Disney.
- Date: 2026-10-29 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxNMEJjQl9vSl9kWk5nemlNQW5QangydndZUU9JRW52bjhwZ1ozX0Fnd0xhc21iUjBfNXNUV0VibVVUaHpmeFpWLVBEcHlpMXFkbXFZSzBBUzd1OV93a091XzVxdjQ0bDNyV0dYTFVaMmJuektoVmM3Z21XQW9aZUVxRVpPemFIaU5NdGZDX2tJY2pUYnRHRmY0?oc=5>

### Netflix Should Never Say Never To Reinventing Itself (NASDAQ:NFLX)
- Summary: Netflix emphasizes continuous reinvention, highlighting strategic product innovation and long-term growth prospects.
- Date: 2026-10-30 | Impact: medium | Horizon: long | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQY25aRjVOYlpTOUFjenBCbW8wQ1BEMU55SFZ2dlkwaUVydjBWOFdDREFzelhBeTBpanN3ZUgzUTdLWFRtamNYZDQxOGFacFlkeTZ1ak5KX2FWMGc4NXBEeGZIYkxKTVNBOC0xU0JFR09FT0NiV2xMc2xQVGFHQmFpdzBKSTJXdkl4Yk9PQzlCVVZXaWtFUHJRUw?oc=5>

### What Should Netflix Stock Investors Be Watching Now?
- Summary: Provides current factors investors should monitor for Netflix stock performance.
- Date: 2026-10-27 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxQUHJTT2tVYjBfMGpTdlVzaE1DWlF4NHdNOFZpeENYcjB0OEw4QzlPSF84Q3hGYy1EQVFmZHp6V0l1N2J3SUNHNTdMb0RMS3FTMUFYV1EzWGZxTmtTM2lUYmVHLWp6Q3lMZU9sQ0FMVEJGaHNGOTVSb2pnWDlQRnJvSXBMSl93SWxmWVlENklwbmlHcEcxdWpnNGx1VkJNdkxVSlE4bm9yd0dxYlVTVmNUSWpR?oc=5>

### Netflix(NFLX) Stock Options Chain | Quotes & News
- Summary: Provides options data, no direct event impact.
- Date: 2026-11-02 | Impact: low | Horizon: short | Confidence: 0.5
- Sources: <https://news.google.com/rss/articles/CBMi-wJBVV95cUxQWHdXaEZ4N1luTTYtS1J5cVpWbExEMWtOWi1vbXNFRVFLTU5TSDIzZWJkQVlfclg2N0FsUDdNaFl4aG9IRWI2dThKRm4wRzJsSGszY29zMjR0R3NCdEJwbVlqOTZmWEJDUVFfeXREcG10dVNxaDZBTGNsWmFmSUZqdUdhVlFLNjdfWWo2bUJscm5henljWGJHSkg2N0xNanBhY3JqRTFlRkE5dzB2eW9JSmFKbF9yX2oxUEFTLXRBcWtoaXlCODNvS2dUTUFKbG5QcXFYZXY0RFpCb1dnR2ViVmt2bzJWelJfUlVRQ2o3bWpjVDlPeWk0d2R5b3JWdTFnUGNCekttT1pkMDNKT29sdEphc0dWRDRpbjF5UUJBTnYyMS11ekRtLWJxOUFEZDlmeDVDbkYwNnFHbmk1ckZwZWR1TFJjUHRQajIyVUo3M3JVN0F2a3YzYUdpNmg3X2RaeDFkeFFHNXlMRHRQb1RIY1dzR1oybjBQUHlr?oc=5>

### Why Netflix Stock Could Double From This Dip
- Summary: Speculative upside potential, no concrete event.
- Date: 2026-11-01 | Impact: medium | Horizon: medium | Confidence: 0.5
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxOTHdVQzdqQ2pIcV9WT2tPUDdyTkQ1VzR5UXNPdk5xLXVIT3ducXc5ZTRiLWJWRjR5NWRkOTlOd3BUNUFJeE9lWTh5Z0RCdUtkcG93cVcwRmZiVV9ETHFFdkw2NGg4TDZjdWwySlYwdGp5NVZDalQzUG5HV1o1R24yRUhqZU1vdlNiUnJQMWh2UjE?oc=5>

### How Much Should One Number Worry Netflix Stock Holders?
- Summary: Analytical focus on valuation metric, no event.
- Date: 2026-11-01 | Impact: low | Horizon: short | Confidence: 0.5
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxQVllxOXphY0ZBQ19kR1h0aFpjU0VDenQ2SktFanRqX25FNThHc1F1d2Rob0laOHhFamZlLVFmLTEwTThLY1p0OWRld0hkWmd2OUFmc1VQeFZmMDdQNVJ1RmZ4YVRxdndnTWh6akxHZThuT2YwT0VHaTdrOExCVEs5b09Ud2piWmhuZFRVY2x1RjA2a1BSUkhrclRaeTFzS0VheHY2YzNGWUk5WHE0OTVHMTRKZ1BfUQ?oc=5>

### Netflix Stock Is Trading at a Historically Low Valuation. Is This a Generational Buying Opportunity?
- Summary: Highlights low valuation, potential buying signal.
- Date: 2026-11-01 | Impact: medium | Horizon: medium | Confidence: 0.5
- Sources: <https://news.google.com/rss/articles/CBMi2AFBVV95cUxPQ1lRWWc3cEFBTEVxNzlnRHUyYnVvdGV6MElkWmpmUGI2M1NSclZZQ291RDd5ZEdsZE5uMVhpMWxtclJYY0dSNGZ4cExGWWpvel9kUDc4QWVPR2xuWjNyQi1fWmNRZ0NGaG9xTHlNdVhxZ3otM1ZDRGpTV1c3bE05ck9zYnpDZ2N2b2MwdDNyVUhYLXRkb25DNzFiM2lXX1dvdjh5Nm43OXBMdHM0WUNHU2h5RDcwSzdEMW9BZlo4ZnhhWHZSVWxYY21PQjJoZmt4cWlDalEyQ3U?oc=5>

## HEADWINDS

### Netflix Shares Are Down 9% Since Earnings. Is the Stock a Buy?
- Summary: Netflix Shares Are Down 9% Since Earnings. Is the Stock a Buy?
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxPZ1pZb216M0NKaGhqWmdoXzkwOC1TQjFzRExLVEpXYVpSU19HTWN5QUVKbTg3cGNYem9nQmw5Mmsxd0V1M2IyMmJQWDJrdUszTllwRmFsRG5UNTZpTjRrVWRCYzBsdGlGazhkeGFwNW5ENUhXRzFEOUJ1U0J4aHJtaDhYdW5hNWdPM1FCajlZZk1pUQ?oc=5>

### Netflix Drops 4% as Engagement Worries Outweigh Earnings Beat; Disney and Spotify Slip
- Summary: Netflix Drops 4% as Engagement Worries Outweigh Earnings Beat; Disney and Spotify Slip
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxQRElvSkJSVnJ6NkNVSmN5TU15dmtGemdCRWFwRE0tcGtvUmxxbXBpOXIybUltTENZZDBtNm1aVjM0bFVJX1UxeVRVV0xYSjFrS1Y4WXY1U3psN3pzcmxvdkNhY1JUb3B1bTJIYVN6LURRS3lTRDM5bHhxSmkxOElpTzgxaUNpNktOeHQ2aEdyWTc2UlhDSkNWOVBqbXpHUlR3?oc=5>

### How Investors May Respond To Netflix (NFLX) Lower Ad Revenue Guidance
- Summary: Lower ad revenue guidance may hurt investor sentiment.
- Date: 2026-11-02 | Impact: high | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxNTmpuUm0tQldPM0g2UUNrdFpYUHVvZ05XM3JUVTVzYTVQV3JwSFJWRFM5aU14dlRGbDFHWUhaNDNsWXc4ZEl2RVVtcXRLN29wMU1xRXJGQWVQemU1MkZYMmRDVXFkMjgwR0txQkpza0phNXZFbWlCbzJNZ0VNek1sRmFiczNjVEF2UEFhcTV1ZW1sRDNwWHBBdG5qTE9Fc2Z5?oc=5>

### Netflix, Inc. $NFLX Stock: MGO One Seven LLC Decreases Holdings
- Summary: Major shareholder reduces stake in Netflix.
- Date: 2026-11-02 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxPcVlBT24zN19VWDFOejJxSWQyemhmc2lvUVlfRVVkQlFURDlPTHFJajViVmlCcjFpQW9EeXBCeHZYLUFZT3hxbGZ0M1FDS255QzRab0NZcC05dzBKWjRQNUZsV0ltV0sxMUdDWFNSTERMNlRuVHVDc01NLVppV0ZBNW1lbDBKZkZmSzdQWTh1ZG55dzhpZnliNEFYQjZnRk9JSUhLRU5ZeXk2RVFqNlZaemJKUDlxV2xiaHJoRQ?oc=5>

## CATALYSTS

### Netflix's Problem Isn't Profits. It's Viewing Time.
- Summary: Netflix's Problem Isn't Profits. It's Viewing Time.
- Date: 2026-10-31 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxOVGhjVDQ3VGtkNk1paC1uSjIwOUYweC1FRmI3YTlHU1JpaXBsTzN5UkhsYkQ2eXVKRUdTX0JnSHNPWk1PeGVfYVJRQjZTLXB3ejR1TEhiS19BX0NzV1VNSk95OTRkV3hXZHpTdFM4V2pQQTl1aXFYUlJyeldDQWYxTk5NMndJaGROdGRVeks4WVJTeDQ?oc=5>

### Netflix's U.S. Audience Engagement Problem Is Hurting The Stock (Rating Downgrade)
- Summary: Netflix's U.S. Audience Engagement Problem Is Hurting The Stock (Rating Downgrade)
- Date: 2026-11-01 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxOY3JYbDhETktQMDhGRklxQl8wM3d0YkFPdGpia3dkaFlXdUxlczVzVlFBTlVVTkRUSWw4MF9PbHZyazd5bE9EejVzR2ZBVmowNTZ2dWZuMDZ5aGhZQ3IxS3VkMmg0TFBDSFAyQ0R3OGxIMklaLV9xUEdLZGY4Q0VxTWFsal80OUZuQjRXSUZ0QUNxR2x1aTgwcVhGUnlKY1RoblJkZGZuNjlIVHZtWkpsd3ZzYWFiSUZ1RlE?oc=5>

### Netflix Stock: A $275bn Company Priced At No Growth (NASDAQ:NFLX)
- Summary: Despite a $275B market cap, Netflix shows limited growth, raising concerns about future earnings and valuation.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxNaUJrZk9aRDR5YV9IeFVvQ2cwMzlQLXJmRkxiZkVVOXVfbXhJa0p1aXE1VUJ2aE94TEFYbGlTQTBhbDJlSkpyWW84c3RmTFlrS2RtV0VGa0haTHBjbTZHUnNJbENnSUgxc1k1ZXlubElZMTd1Yld2VFpYQUZ1N2NrTnpma29rNEtyQ2FvMA?oc=5>

### Netflix Spent $4.8 Billion Buying Back Stock in 1 Quarter. Here's What That Tells You.
- Summary: Netflix repurchased $4.8B of shares this quarter, signaling confidence and potentially boosting EPS per share.
- Date: 2026-10-30 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxQUjViaXJMRjdUcktWc0Y0bWRGX2ViaHA4UXhJcTREbks0LUZjcGNYSzNqZl9CTHZEd3kwLUFhZFNhcDNwaVYtVnJ3cUltT1p4NkZNcTdrSE1oZVpZQzVLZHpySjdCYTV4QXVJdXhFcW9LWU1MUC0zcDl2RVp2QUwxb3liRDVWRVd4WHFFZWZwLV9RVzlx?oc=5>

### Netflix, Inc. (NFLX) Stock Forecasts
- Summary: Predictions for future performance of Netflix shares.
- Date: 2026-10-29 | Impact: low | Horizon: short | Confidence: 0.5
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxOeFN4ZjN0Q0RPX3AxYTVZemJxVHhNemRHWDBhdWhRSXdzRklENkdic24yUloyQjNONFhobWgxb0F6R1N5ZGp3RW52SWRHWjE2RW5tRE5qOTBCYlVXZ3VoY2pQQ1lpaFp0V1c0bXpXcXlicEhVdjBWeGNBaTkweDBWWG1Tb1k1WDBXU29kLWtn?oc=5>

### Netflix: Price Increases Are No Longer Providing Unchecked Upside (Downgrade) (NFLX)
- Summary: Downgrade signals Netflix's price hikes no longer yield upside.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxONkdVeC1kd29pUUlKbjZfd3lYckhoSFNnbktmU1VIbVFBR08yV3pYcWo3TDkzbE43SnBJQ2RlTE84OUhnTnRnYWNsTVo4N2hBMlVKdVotVWdDVV9IdGhxbWJKLUd3Yk1fZDBKTzc0Uk1SUzc1RUdBLXpqVkdfWkV4ay1FOXpwTTNvMGZGUmxiUEJUdlVnZW1pZ2RXWW1GNC1JaVczaWczU01NRWJ6UTV2Rm9VNUZMZw?oc=5>

### Options Volatility Rises for Netflix (NFLX) Ahead of Market Move
- Summary: Increase in options volatility for Netflix before a market event.
- Date: 2026-10-30 | Impact: low | Horizon: short | Confidence: 0.5
- Sources: <https://news.google.com/rss/articles/CBMizAJBVV95cUxPOXRvVWhSa2Fxam1fVHRJYWdjWUlydjZlOUlvekxuVUhTSm1obXIyYlBzSUpqdXByUkUxZnRERW5FU2xJWmk1Qk03c3N5azA5UE5ta2VVZUU0UmlqaUVBSDZ5cERZZEhFT1RzX1hXODA3UEl4dXBNRlpnb19ZZ19TNVFhVzB1UlJ2NU5yNDZVcThhRkNmRjEzWnZ6UnRFNkd0ZFZzM09DZHdtajEzRVZKei02MnIwcXNvM1Q3VkpiaWFDMUgtbzRzSk90Q1B5TUFybEpjUUxfVDVqX19vMDdmXzZ0bkFka3Jlek5XUVZwakU5RHNLMXIyaTlqaWdxYWtNN1ZLZWs1V20xUXVxMy1VR1M1d2FjNkZGVE51ZkFYbjllUHN3MkhVOU1IOUgzekN4TFptcnRRMXk2c1Q1TEE1OEpWTW1qbS1kQnM5cg?oc=5>

### Netflix, Inc. $NFLX Stock: Heritage Investors Management Corp Boosts Holdings
- Summary: Heritage Investors Management Corp increased its holdings in Netflix, signaling confidence in the company.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizwFBVV95cUxPYXFnS1VqcmgtQnJRLUUtaVNPSmFpeXdUQjVLY1phUHJIOXJqLWNyLUZUQ0FiZlBNNlBkMnNQSW1FOXczUWNVOEt3ZVo1RTNtY3R3M3ZsN21MVmhBanktVU9JUjNrZGtIN3czbW5YcVVXeG1BQ1RVdlAwQWFNR2tnUG1WRTFUR2V6MWF1Sndub2hyMUZxWThySTdjeUFkN2dHbTlxUUYzdGZFOFNfNm1nZTZnQTRFekV0bDdVQmpLaUZPbHRYdlRLZ3ZrNTduRzg?oc=5>

### What Does Netflix (NFLX) Leadership Shakeup Mean For Its Streaming Future?
- Summary: Leadership changes may affect Netflix's strategy.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxPOE5od1c5TVJpbXNITV9fdnpscVc0SEhwbkdYYl9Id2NpQlBMQ0ljQmtsd0xqSjd0X09Wd0dfc3hqak50ZjRZOExCWHE1aGdvMmV3YVc3OUZXUGNleUxZTS1PcXBSeDlkazBmVDQtOHVaQjRucDN2N1N3Nm5MY3NkSGRvamFyd05PQVNhNE5LZm9Xdll0U2ZDaEFma3dpTFRfeUtUaExGQQ?oc=5>

## RISKS

### Is Netflix (NFLX) A Bargain After Its 2026 Guidance Reset?
- Summary: Investors question if Netflix remains a bargain following its 2026 guidance reset, suggesting possible long-term downside risk.
- Date: 2026-10-30 | Impact: medium | Horizon: long | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxQYXFIRXR2UFNyNHdHZFVwM0FwMVQtdVhKRU1VTWljeTQ2Rm1qYVVWeERlaklHVklBU0pyNjRaUWZGYXVhOGJMZ0h5TmRpVERTTDVoZkJ3eW5OenNfcVhnUEhLLVBNY0VqSGdVRlZMS2FwWlgweUcwckJ3ZmYwc2dJb3lScWI2VFdKNmc3aGdpUGJFdTVVZFpIaW9qR3ZGSmN0?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NFLX** | **18.02** | **8.74** | **16.63** | **11.80** | **259,580,002,304.00 USD** | **-44.28** |
| DIS | 22.90 | 1.78 | 11.59 | 6.80 | 195,305,553,920.00 USD | 1.89 |
| WBD | N/A | 2.36 | 13.79 | -11.20 | 77,595,885,568.00 USD | N/A |
| CMCSA | 7.34 | 0.92 | 4.91 | -6.10 | 84,762,517,504.00 USD | -3.62 |

Peers fetched as_of: 2026-11-02; NFLX reuses existing data (market data as_of: 2026-11-02); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-20
- Next expected earnings: 2027-01-19 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-02

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-21
- Revenue (latest available single quarter): 12,874,176,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 3,663,927,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1065280/000106528026000291/nflx-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMilwFBVV95cUxNMEJjQl9vSl9kWk5nemlNQW5QangydndZUU9JRW52bjhwZ1ozX0Fnd0xhc21iUjBfNXNUV0VibVVUaHpmeFpWLVBEcHlpMXFkbXFZSzBBUzd1OV93a091XzVxdjQ0bDNyV0dYTFVaMmJuektoVmM3Z21XQW9aZUVxRVpPemFIaU5NdGZDX2tJY2pUYnRHRmY0?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQY25aRjVOYlpTOUFjenBCbW8wQ1BEMU55SFZ2dlkwaUVydjBWOFdDREFzelhBeTBpanN3ZUgzUTdLWFRtamNYZDQxOGFacFlkeTZ1ak5KX2FWMGc4NXBEeGZIYkxKTVNBOC0xU0JFR09FT0NiV2xMc2xQVGFHQmFpdzBKSTJXdkl4Yk9PQzlCVVZXaWtFUHJRUw?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxQUHJTT2tVYjBfMGpTdlVzaE1DWlF4NHdNOFZpeENYcjB0OEw4QzlPSF84Q3hGYy1EQVFmZHp6V0l1N2J3SUNHNTdMb0RMS3FTMUFYV1EzWGZxTmtTM2lUYmVHLWp6Q3lMZU9sQ0FMVEJGaHNGOTVSb2pnWDlQRnJvSXBMSl93SWxmWVlENklwbmlHcEcxdWpnNGx1VkJNdkxVSlE4bm9yd0dxYlVTVmNUSWpR?oc=5
- https://news.google.com/rss/articles/CBMi-wJBVV95cUxQWHdXaEZ4N1luTTYtS1J5cVpWbExEMWtOWi1vbXNFRVFLTU5TSDIzZWJkQVlfclg2N0FsUDdNaFl4aG9IRWI2dThKRm4wRzJsSGszY29zMjR0R3NCdEJwbVlqOTZmWEJDUVFfeXREcG10dVNxaDZBTGNsWmFmSUZqdUdhVlFLNjdfWWo2bUJscm5henljWGJHSkg2N0xNanBhY3JqRTFlRkE5dzB2eW9JSmFKbF9yX2oxUEFTLXRBcWtoaXlCODNvS2dUTUFKbG5QcXFYZXY0RFpCb1dnR2ViVmt2bzJWelJfUlVRQ2o3bWpjVDlPeWk0d2R5b3JWdTFnUGNCekttT1pkMDNKT29sdEphc0dWRDRpbjF5UUJBTnYyMS11ekRtLWJxOUFEZDlmeDVDbkYwNnFHbmk1ckZwZWR1TFJjUHRQajIyVUo3M3JVN0F2a3YzYUdpNmg3X2RaeDFkeFFHNXlMRHRQb1RIY1dzR1oybjBQUHlr?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxOTHdVQzdqQ2pIcV9WT2tPUDdyTkQ1VzR5UXNPdk5xLXVIT3ducXc5ZTRiLWJWRjR5NWRkOTlOd3BUNUFJeE9lWTh5Z0RCdUtkcG93cVcwRmZiVV9ETHFFdkw2NGg4TDZjdWwySlYwdGp5NVZDalQzUG5HV1o1R24yRUhqZU1vdlNiUnJQMWh2UjE?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxOZ2xkUHpTZ1FLVE9NNFlqQU4yRVg4d2xMcWk0ZDNGNUwzLWtKVldUbF9SVXNLSFJMZkRNUnhLYTZ6NWc3ZEc2dDNVcjNTTDk3c0pZblc2OVdtZkY1ZFhhZWc5MGE0NkRUSmpicTNXcDJTdDdJVFBmRXZFck1hUGRUYUtjSUU5eWZiOTNibXhHRzIwcGVaX3RESGtScw?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxQVllxOXphY0ZBQ19kR1h0aFpjU0VDenQ2SktFanRqX25FNThHc1F1d2Rob0laOHhFamZlLVFmLTEwTThLY1p0OWRld0hkWmd2OUFmc1VQeFZmMDdQNVJ1RmZ4YVRxdndnTWh6akxHZThuT2YwT0VHaTdrOExCVEs5b09Ud2piWmhuZFRVY2x1RjA2a1BSUkhrclRaeTFzS0VheHY2YzNGWUk5WHE0OTVHMTRKZ1BfUQ?oc=5
- https://news.google.com/rss/articles/CBMi2AFBVV95cUxPQ1lRWWc3cEFBTEVxNzlnRHUyYnVvdGV6MElkWmpmUGI2M1NSclZZQ291RDd5ZEdsZE5uMVhpMWxtclJYY0dSNGZ4cExGWWpvel9kUDc4QWVPR2xuWjNyQi1fWmNRZ0NGaG9xTHlNdVhxZ3otM1ZDRGpTV1c3bE05ck9zYnpDZ2N2b2MwdDNyVUhYLXRkb25DNzFiM2lXX1dvdjh5Nm43OXBMdHM0WUNHU2h5RDcwSzdEMW9BZlo4ZnhhWHZSVWxYY21PQjJoZmt4cWlDalEyQ3U?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxPZ1pZb216M0NKaGhqWmdoXzkwOC1TQjFzRExLVEpXYVpSU19HTWN5QUVKbTg3cGNYem9nQmw5Mmsxd0V1M2IyMmJQWDJrdUszTllwRmFsRG5UNTZpTjRrVWRCYzBsdGlGazhkeGFwNW5ENUhXRzFEOUJ1U0J4aHJtaDhYdW5hNWdPM1FCajlZZk1pUQ?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxQRElvSkJSVnJ6NkNVSmN5TU15dmtGemdCRWFwRE0tcGtvUmxxbXBpOXIybUltTENZZDBtNm1aVjM0bFVJX1UxeVRVV0xYSjFrS1Y4WXY1U3psN3pzcmxvdkNhY1JUb3B1bTJIYVN6LURRS3lTRDM5bHhxSmkxOElpTzgxaUNpNktOeHQ2aEdyWTc2UlhDSkNWOVBqbXpHUlR3?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxNTmpuUm0tQldPM0g2UUNrdFpYUHVvZ05XM3JUVTVzYTVQV3JwSFJWRFM5aU14dlRGbDFHWUhaNDNsWXc4ZEl2RVVtcXRLN29wMU1xRXJGQWVQemU1MkZYMmRDVXFkMjgwR0txQkpza0phNXZFbWlCbzJNZ0VNek1sRmFiczNjVEF2UEFhcTV1ZW1sRDNwWHBBdG5qTE9Fc2Z5?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxPcVlBT24zN19VWDFOejJxSWQyemhmc2lvUVlfRVVkQlFURDlPTHFJajViVmlCcjFpQW9EeXBCeHZYLUFZT3hxbGZ0M1FDS255QzRab0NZcC05dzBKWjRQNUZsV0ltV0sxMUdDWFNSTERMNlRuVHVDc01NLVppV0ZBNW1lbDBKZkZmSzdQWTh1ZG55dzhpZnliNEFYQjZnRk9JSUhLRU5ZeXk2RVFqNlZaemJKUDlxV2xiaHJoRQ?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxOVGhjVDQ3VGtkNk1paC1uSjIwOUYweC1FRmI3YTlHU1JpaXBsTzN5UkhsYkQ2eXVKRUdTX0JnSHNPWk1PeGVfYVJRQjZTLXB3ejR1TEhiS19BX0NzV1VNSk95OTRkV3hXZHpTdFM4V2pQQTl1aXFYUlJyeldDQWYxTk5NMndJaGROdGRVeks4WVJTeDQ?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxOY3JYbDhETktQMDhGRklxQl8wM3d0YkFPdGpia3dkaFlXdUxlczVzVlFBTlVVTkRUSWw4MF9PbHZyazd5bE9EejVzR2ZBVmowNTZ2dWZuMDZ5aGhZQ3IxS3VkMmg0TFBDSFAyQ0R3OGxIMklaLV9xUEdLZGY4Q0VxTWFsal80OUZuQjRXSUZ0QUNxR2x1aTgwcVhGUnlKY1RoblJkZGZuNjlIVHZtWkpsd3ZzYWFiSUZ1RlE?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxNaUJrZk9aRDR5YV9IeFVvQ2cwMzlQLXJmRkxiZkVVOXVfbXhJa0p1aXE1VUJ2aE94TEFYbGlTQTBhbDJlSkpyWW84c3RmTFlrS2RtV0VGa0haTHBjbTZHUnNJbENnSUgxc1k1ZXlubElZMTd1Yld2VFpYQUZ1N2NrTnpma29rNEtyQ2FvMA?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxQUjViaXJMRjdUcktWc0Y0bWRGX2ViaHA4UXhJcTREbks0LUZjcGNYSzNqZl9CTHZEd3kwLUFhZFNhcDNwaVYtVnJ3cUltT1p4NkZNcTdrSE1oZVpZQzVLZHpySjdCYTV4QXVJdXhFcW9LWU1MUC0zcDl2RVp2QUwxb3liRDVWRVd4WHFFZWZwLV9RVzlx?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxOeFN4ZjN0Q0RPX3AxYTVZemJxVHhNemRHWDBhdWhRSXdzRklENkdic24yUloyQjNONFhobWgxb0F6R1N5ZGp3RW52SWRHWjE2RW5tRE5qOTBCYlVXZ3VoY2pQQ1lpaFp0V1c0bXpXcXlicEhVdjBWeGNBaTkweDBWWG1Tb1k1WDBXU29kLWtn?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxONkdVeC1kd29pUUlKbjZfd3lYckhoSFNnbktmU1VIbVFBR08yV3pYcWo3TDkzbE43SnBJQ2RlTE84OUhnTnRnYWNsTVo4N2hBMlVKdVotVWdDVV9IdGhxbWJKLUd3Yk1fZDBKTzc0Uk1SUzc1RUdBLXpqVkdfWkV4ay1FOXpwTTNvMGZGUmxiUEJUdlVnZW1pZ2RXWW1GNC1JaVczaWczU01NRWJ6UTV2Rm9VNUZMZw?oc=5
- https://news.google.com/rss/articles/CBMizAJBVV95cUxPOXRvVWhSa2Fxam1fVHRJYWdjWUlydjZlOUlvekxuVUhTSm1obXIyYlBzSUpqdXByUkUxZnRERW5FU2xJWmk1Qk03c3N5azA5UE5ta2VVZUU0UmlqaUVBSDZ5cERZZEhFT1RzX1hXODA3UEl4dXBNRlpnb19ZZ19TNVFhVzB1UlJ2NU5yNDZVcThhRkNmRjEzWnZ6UnRFNkd0ZFZzM09DZHdtajEzRVZKei02MnIwcXNvM1Q3VkpiaWFDMUgtbzRzSk90Q1B5TUFybEpjUUxfVDVqX19vMDdmXzZ0bkFka3Jlek5XUVZwakU5RHNLMXIyaTlqaWdxYWtNN1ZLZWs1V20xUXVxMy1VR1M1d2FjNkZGVE51ZkFYbjllUHN3MkhVOU1IOUgzekN4TFptcnRRMXk2c1Q1TEE1OEpWTW1qbS1kQnM5cg?oc=5
- https://news.google.com/rss/articles/CBMizwFBVV95cUxPYXFnS1VqcmgtQnJRLUUtaVNPSmFpeXdUQjVLY1phUHJIOXJqLWNyLUZUQ0FiZlBNNlBkMnNQSW1FOXczUWNVOEt3ZVo1RTNtY3R3M3ZsN21MVmhBanktVU9JUjNrZGtIN3czbW5YcVVXeG1BQ1RVdlAwQWFNR2tnUG1WRTFUR2V6MWF1Sndub2hyMUZxWThySTdjeUFkN2dHbTlxUUYzdGZFOFNfNm1nZTZnQTRFekV0bDdVQmpLaUZPbHRYdlRLZ3ZrNTduRzg?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxPOE5od1c5TVJpbXNITV9fdnpscVc0SEhwbkdYYl9Id2NpQlBMQ0ljQmtsd0xqSjd0X09Wd0dfc3hqak50ZjRZOExCWHE1aGdvMmV3YVc3OUZXUGNleUxZTS1PcXBSeDlkazBmVDQtOHVaQjRucDN2N1N3Nm5MY3NkSGRvamFyd05PQVNhNE5LZm9Xdll0U2ZDaEFma3dpTFRfeUtUaExGQQ?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxQYXFIRXR2UFNyNHdHZFVwM0FwMVQtdVhKRU1VTWljeTQ2Rm1qYVVWeERlaklHVklBU0pyNjRaUWZGYXVhOGJMZ0h5TmRpVERTTDVoZkJ3eW5OenNfcVhnUEhLLVBNY0VqSGdVRlZMS2FwWlgweUcwckJ3ZmYwc2dJb3lScWI2VFdKNmc3aGdpUGJFdTVVZFpIaW9qR3ZGSmN0?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
