# VRTX Intelligence Report

- ticker: **VRTX**
- Report as_of: **2026-11-09**
- Market data as_of: **2026-11-09**
- Quant sources: https://finance.yahoo.com/quote/VRTX/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/VRTX/key-statistics/
- AI analysis snapshot as_of: **2026-11-09**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-10T05:53:50.374221+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 17, 'rule': 7, 'ai': 6, 'unknown': 0, 'irrelevant': 4})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **6** exact headline/source/date matches; prior report **20261109T043242Z-c8e908de/VRTX** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 17 unique headlines; 11 named publishers; 0 exact duplicates; 17 HTTPS source links; largest publisher share 17.65%; oldest publication 2026-11-02

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 550.8700 |
| Return 1D (%) | 0.6909 |
| Return 1W (%) | -0.4122 |
| Return 1M (%) | 7.9968 |
| Return YTD (%) | 21.5083 |
| Return 1Y (%) | 34.5324 |
| Annualized volatility (%) | 29.7268 |
| Beta vs SPY | 0.4294 |
| Max drawdown (%) | -15.2113 |
| Sharpe (rf=0) | 1.0572 |
| Downside deviation (rf=0, %) | 18.2673 |
| Sortino (rf=0) | 1.7205 |
| Historical VaR 95% (1D, %) | 2.8874 |
| Historical ES 95% (1D, %) | 3.4957 |
| Correlation vs SPY | 0.1978 |
| Tracking error vs SPY (%) | 30.1689 |
| P/E (trailing) | 35.45 |
| P/B | 6.68 |
| EV/EBITDA | 27.42 |
| Revenue growth (%) | 11.80 |
| Forward P/E (estimate) | 27.66 |
| Gross margin (%) | 54.81 |
| Operating margin (%) | 35.57 |
| Return on equity (%) | 20.80 |
| Free cash flow yield (%) | 1.67 |
| MA50 | 522.9822 |
| Close vs MA50 (%) | 5.3325 |
| MA200 | 481.9847 |
| Close vs MA200 (%) | 14.2920 |
| RSI (14, Wilder) | 59.2659 |
| MACD (12,26) | 9.2579 |
| MACD signal (9) | 6.7792 |
| MACD histogram | 2.4787 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'VRTX': 278, 'SPY': 278}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 550.8700 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.6909 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -0.4122 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 7.9968 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 21.5083 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 34.5324 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 29.7268 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 18.2673 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.7205 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.8874 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.4957 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.1978 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 30.1689 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.4294 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -15.2113 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.0572 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 27.6569 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 54.8090 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 35.5700 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 20.8020 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.6738 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 35.4485 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 59.2659 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 2.4787 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 5.3325 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 14.2920 -> Clearly above the moving-average trend level.

## TAILWINDS

### Vertex Pharmaceuticals Thrives on Higher Sales and Guidance
- Summary: Vertex Pharmaceuticals Thrives on Higher Sales and Guidance
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxNM0lyaGt0UEJxN19FZlRnRUdUX291SlVKQXJkd3NFZDlnWDdlRXRsM1NRUFc5SlpUNUQwS2lLWEhudTdJQ2xjUjV6Z0pfczVOZ0pEUlp4RnVXOG1tRlJiS1M2WjlySW82bmlralJUMS15RzhKMm9RSF91WlFNazBNRW9PZ1E1MXNYcncwM19lQUZ4RjY5ZFAzUXRqVkxoX0M1dVd3YnRkUEMwM2VjY193SjVn?oc=5>

### Vertex Pharmaceuticals Analysts Raise Their Forecasts Following Q3 Results
- Summary: Vertex Pharmaceuticals Analysts Raise Their Forecasts Following Q3 Results
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi4wFBVV95cUxNdXBJYm1wR2x0ZUk0TG1tOFg2aVhmcnJUNmp3LThZNmRiMld1WXNRUG5LdUdsNTFseXBBLWRRTEdybzAtQkVVUndITWJsdWV4WHdWRE1XRE5YUkdGVTcwYVUxdmdWb2x0UEI0dURPME5mXzltMG5kU2lxMlVaSVdmUVRIRG1TcmFveUZxZ0NybmhkbFZJTWVhVmNEbmVrQkJIWm0zdFZnbDZnUHZfRVU3QXh6SW5OVGIwVE9hZDNsMU9LX0RMamsxY0xCVnFoS0JVZnhXQ2pVLVR6RjVuZk5SM0lKRQ?oc=5>

### Vertex Pharmaceuticals’s (NASDAQ:VRTX) Q3 2026 sales top estimates
- Summary: Vertex Pharmaceuticals’s (NASDAQ:VRTX) Q3 2026 sales top estimates
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi4AFBVV95cUxPbnFlYXFUdmRsY2x2TW9kQW1tUlFITHhSeS00RVpUVU9iVTRIckt1ZjNzeGM4YnU2LU1pMjI1WlNyOGNnYzF3dzhzSk1CcFpiTk5LcnJfZklXcC1ZTjh1RnJiUzRISnR6WUFleVpPVjVfeGh3WmlISmNsWi01VlpqQnZnVUJ3TE1zZnZmRndJbjJJS1I4V3VqTnpJYU5LcWlXVG1YM3doZU8xNmRZMWRxTzF5YTR1dllRUm5hMGlPX0toZnVmWGZ6VG84bzNNMjNEdXBfSHZ5UmxfNjdYMm03eQ?oc=5>

### How Raised Revenue Guidance At Vertex Pharmaceuticals (VRTX) Has Changed Its Investment Story
- Summary: Vertex raised revenue guidance, potentially boosting investor confidence and valuation.
- Date: 2026-11-09 | Impact: high | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi7AFBVV95cUxQdjFSTFJQS2s0ZEJaX3hjQU05Q1NQN2lNNEFrYVpmckZ4ekxhSlhVQXh2VUUyVnhsMVZpRWJCMkhnZXFkRWFaX1ZIV2o3SXFwM19iU0NqSWxDdkZpZWx4NW9oWGI2SE5aN3FmYUdkanNOeHh6UHl4RHFNUWh4LVZSRzJoaWJ6NVg2X0xLX0JGYzV1cGtWNC0wQV95eXh4SG5Fb09IeC1qT2JYaC1iU19Zd3E2REpZZm5oNzZhZTRSZEVnMks5cW40OTM4dElnNlZuY25KQ0hBdDhVYVE2R0FfRU1BT0ppX3JSYTFkcNIB8gFBVV95cUxPRHFmSDEzbHNWeko3VDBfc2s4eHF4Z3V6b25GdGFYTDhERF85N2NUMHJKMkt4ZTBsOGR3RnV5c29fanFEb2c0SW5OZW4ybnFKWDJLTkxiRUxHYnpDUzU5bC1QdU5tNGhUV3VXX19wWHFaYVhybVJXNTcwTW4tVUJPc1NtZ1VnbnhhemJLSGI2MEE5OXdESktqM3V3RDBLTUhGdkxlc3FuZjhMcVBTckxkaWZWNHkzVHU5cnBpNmpacFlPVTdNdVZ0WjZ4eEtrX25admxmRVNNc0dOUV9DZWgxUnNTaGQ4WldDUFIwd01faUF1Zw?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Vertex Pharmaceuticals Incorporated 2026 Q3 - Results - Earnings Call Presentation (NASDAQ:VRTX) 2026-11-05
- Summary: Vertex Pharmaceuticals Incorporated 2026 Q3 - Results - Earnings Call Presentation (NASDAQ:VRTX) 2026-11-05
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxNVUNNdGlpM3pLOHhmNGNDMXFyMTVibDdkcXAzSl9zSHczN2tQVjRIdUxXVXJnYnlIMHFjdThMQVM5emNVcVJuZ0VwWXl2U0hUdU11SkZya0M0QTVhZDlaQlpxNXlLUTVmc1FpVzVIdkJTUW9nTXBsM3pfQnU4WWVhY2hVR2l6RXRYaV9zVld6a2MzUldZUUFzRGt3NXhtb3JYN2NiOFltbXp6VG5Ja3ZQUUJVdFh2VXhCRmhB?oc=5>

### Vertex Pharmaceuticals earnings analysis: questions answered and next catalysts
- Summary: Vertex Pharmaceuticals earnings analysis: questions answered and next catalysts
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxQWGNseDhkbkZvSnZtYTBVSVZ0Q1FUUmdlT2U5VzZwaVNhMTNYSkVQdkRMMFpucjl6U3RZNkllOXBuNXU5NVVuLTI0Vzg5UzhPOGRRZ1JNUlNmMFlMTWd4Y28ybzF6OWJfMTdldnA0djBJSUJQTzlnQjlzTVFFQk9KTmhQNFRsS1JtaEVjT19YNmY1U2ZVUXVYU2hKSEljVkZmbzJkMlRMQ0VHMThub25hTg?oc=5>

### VRTX's Q3 Earnings Lag Estimates, Revenues Top, 2026 Sales View Raised
- Summary: VRTX's Q3 Earnings Lag Estimates, Revenues Top, 2026 Sales View Raised
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxPOGRBcmNBS0FxMkxoV3g1dE9sd3Q3bVI1dGN1bFpPT2tFVkxLNWxqd1l3LVN0eUNfZEVtSzA1VlRZN1N2MFJNdlBtYnBiOTZ5bGtwZFB1WmV2YlVVM0JWN3NmRlhPNFUxYXkxa2p4UnlNYmNHREJpTjdHVjFKLVVJV3ZkZzRfalYwS2JZbVRUVGVKVVFRYTdvTk5PVXQwelcxZkNTU016QzVKVWZFRXpaOUMxM3hOZUpuY09uZ2dmUS0ydw?oc=5>

### Vertex Pharmaceuticals (VRTX) Stock Rethinks Q3 Results After Profit Squeeze
- Summary: Vertex Pharmaceuticals (VRTX) Stock Rethinks Q3 Results After Profit Squeeze
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi6wFBVV95cUxOX0FFbi0yMjdKVFgtN0Q1aTdjRzU4ak9iS1R1bDMySVZfQ3EyRWRyUWlrcjBTd3pvM3hsclU1UEptODl0b2RlLUFJNGFYbV8wek1SUGt4ejQwZ09KbnFXN0hJOUVKUUl4RDNudUYzdFJaQWNFT0l5RGJFY3U3em4tN2tEdjZNcnBQNkNwaWZNN2VRR3JDcVNjV1pmR0UwREFNbkRxMUNzNnpabHJFSDA1UmgySFZsUVlqdmg3b1owRmRySm9zNW9ZRmUyc1NRaWRvVnQyaWkyaS1XcnYxWjhUdXpJMUFNZ016OG440gHwAUFVX3lxTE5RWm1KRUxKSjVBNVhvaEtSWUhKVk52Z3ZpWTdrRXRlRm03Y2NueE9yX2JWV20zN2FWQUppUlllUl9wR18yaUl2VUJjRVVEMTdtdzk5ZUlMdU9wdjVpdGF1OFRoT3lqUXBhSWtrU21CYmFyOTB1aVZrN05qOHpzUy1YWFFmZWtsTzhOX3dEejdTdzJRa0NTTjhhRlE2Y0dlbFM2TVZ5UE82QlRISFk3TzJoT0sxel9qY3RDRzRCWlo2MXcxVWRZSkFiNndGdmF5a2lWM3Z4ZU9XVERmVlIzdEZzQ3NZWU1FVGI0TjJ2emZpUQ?oc=5>

### Vertex Pharmaceuticals (VRTX) Lifts Revenue Guidance, Is It Still A Bargain?
- Summary: Vertex raises revenue outlook, suggesting stronger future earnings.
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi7AFBVV95cUxPZjlDSDg2MW9QSkNDQVZLQ1A4MlhBd216MWNYUVVpdjJuNWIxdmVPdmdTekN0TUdfanpOOFI2bzdRWUdYd0hURUFaeDRpLVlSQ3ZZb2RKbDQ2Y1hhb2FfeS13TDExNXpuZTVFV0h0M1ZHMXdCQmRtYTZlcjQwdThBcUtvYWVPYXBKaVgzSEZqQ0JTampVT05IQ2lWQmY3YWdaNHA2TzJDVFpweWpvd255SEFEU3JhNzdwNnoyRFdwN29meXVwUFRLZTVnZ0pXWlpmZERfV0EtbGtub0t6QWlMVVFHYm5iN1ZJb2Ryb9IB8gFBVV95cUxPcW9qT1dpUGlINXRRd1F6ajRKOWdLWExUaWVpakhYNXFPcXhaZnRNOG9Jc0N5cEdmRmdiN3Rlenk4ZzZqRFoyVUtBdFZnODBuQ3g4Z3NicGw0QkxabThWdWVCM3Q5ZGtHNGNuaG96aGgzcTBzU1N4WUFiR0dBWmZNaElWbkgzdlVJd3FtcFVaMTZGMHZaZy1MQ2ltX2Z3eWF3bVRnZUxldndad2hnYXd4ZXowUzdVOHpzUTltZ2JIRlMza1pzTWxad2l0Ml9VNUY1TmlabkpJZHF2ZVdDd2dLNjlCcU1rV2p4YmdOYXllWThpUQ?oc=5>

### Vertex Q3 Earnings Call Highlights Revenue Beat and Pipeline Expansion
- Summary: Q3 earnings beat expectations, pipeline expands.
- Date: 2026-11-03 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxNZFFGaEtfQ3Utb2xmbldPOGJ0SVlPNW1PcGtNQjFxUXFVN3ljdV9ZVXMxb216OFBVSnR3ZjY5enRwMWo5dzBycWpCeFNrYmJCd2NfYjMtbWJJX0RfVm9wQXZlM2Y0OGJSQmxJUl85Tjc0UklxX2lXRWlkZkZRYXE4OC05bWM0b3VEV2E4N1RFLTB0MTZnTWFGSnpkQV9uTG9pRHlxNFZTRzBRYWJJRHk2NldiczFvQVFVUWo1R1hNc0tTNlVz?oc=5>

### Up to $13.25 billion: Vertex raises its 2026 revenue forecast.
- Summary: Vertex raises 2026 revenue forecast to $13.25B.
- Date: 2026-11-02 | Impact: high | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxPZmNTNXltTG9Ua2g4RzhCUE13QWhkV1BPeUJhcmtlOS16SDVSazZlQUJBWlVHaXEzSlRMTWluSm5ob1lkQWZpRG9NX2QxbWRWWDFnWlB5bGJuQ1BGOTYyTjhaeG1VUXMtdjdNRVdnX2I0MVVTdzBCYi1vSDRsakc4RUh5X19JNTM0T0ZvYVpzRTk1NVkxUV9sQzZ3OVg2clU?oc=5>

### Can Vertex Pharmaceuticals (NASDAQ:VRTX) Turn New Launches Into Growth?
- Summary: New product launches could drive future growth, but execution risk remains.
- Date: 2026-11-05 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxQd0N5VzlRNWlVSUFkb0MwVE4zaE5HMWRQRWNKRmp5WVdHdDdvVE03RUMxWnNjN2p2ZVN5UF9RUzBpOWhia05SLTZxdDFOLWdYTmxlaDgxaHRVS1VCTWt1VG5aVXd6WXFrcWJEWWNQN1puaS1YMjFiUzNmRVItOWk2LUUxSVRRZjA5dXY4U0tpd0F5WjFrNXMyMS1zQlkyZGhDeDlvX3NYajRPeGF5MWUxeVB5SQ?oc=5>

### How Is Vertex Pharmaceuticals (NASDAQ:VRTX) Expanding Beyond Its Core Business?
- Summary: Vertex explores new business areas beyond its main focus.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxPMUJCN2hFNzUwUi10U0dwVUZGS3hhbkdNYjFRV00yeWhZWkhtSVUyM0UxbXA4X2pJMllVQ3Fick9IY0pJU2NPR2pBNmZGZHdkM3RRSkJJRjlpQjRWeHhOX0pOZU01ZjNJYl8ycngwUW9DLVBINmVZNHlaTnd6aHZ3R01LcEVRMGpQSnBPTTlhN1pZQ2x6Ym1MOHV3UEpsVG41d1l1Sm0wNUdMdER2UV96Uk5tNDY0c0xyY2ljd3pB?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **VRTX** | **35.45** | **6.68** | **27.42** | **11.80** | **139,666,292,736.00 USD** | **34.53** |
| REGN | 20.34 | 2.75 | 15.18 | 36.30 | 95,167,889,408.00 USD | 40.63 |
| BIIB | 110.33 | 1.99 | 13.38 | 10.60 | 37,674,938,368.00 USD | 63.89 |
| AMGN | 26.97 | 17.53 | 16.59 | 8.50 | 251,648,262,144.00 USD | 49.32 |

Peers fetched as_of: 2026-11-09; VRTX reuses existing data (market data as_of: 2026-11-09); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-02
- Next expected earnings: 2027-02-11 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-09

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-03
- Revenue (latest available single quarter): 640,799,000.00 USD; period 2018-01-01/2018-03-31; fiscal year/reporting period 2018/Q1
- Net income (latest available single quarter): 653,600,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/875320/000087532026000291/vrtx-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMisgFBVV95cUxNM0lyaGt0UEJxN19FZlRnRUdUX291SlVKQXJkd3NFZDlnWDdlRXRsM1NRUFc5SlpUNUQwS2lLWEhudTdJQ2xjUjV6Z0pfczVOZ0pEUlp4RnVXOG1tRlJiS1M2WjlySW82bmlralJUMS15RzhKMm9RSF91WlFNazBNRW9PZ1E1MXNYcncwM19lQUZ4RjY5ZFAzUXRqVkxoX0M1dVd3YnRkUEMwM2VjY193SjVn?oc=5
- https://news.google.com/rss/articles/CBMi4wFBVV95cUxNdXBJYm1wR2x0ZUk0TG1tOFg2aVhmcnJUNmp3LThZNmRiMld1WXNRUG5LdUdsNTFseXBBLWRRTEdybzAtQkVVUndITWJsdWV4WHdWRE1XRE5YUkdGVTcwYVUxdmdWb2x0UEI0dURPME5mXzltMG5kU2lxMlVaSVdmUVRIRG1TcmFveUZxZ0NybmhkbFZJTWVhVmNEbmVrQkJIWm0zdFZnbDZnUHZfRVU3QXh6SW5OVGIwVE9hZDNsMU9LX0RMamsxY0xCVnFoS0JVZnhXQ2pVLVR6RjVuZk5SM0lKRQ?oc=5
- https://news.google.com/rss/articles/CBMi4AFBVV95cUxPbnFlYXFUdmRsY2x2TW9kQW1tUlFITHhSeS00RVpUVU9iVTRIckt1ZjNzeGM4YnU2LU1pMjI1WlNyOGNnYzF3dzhzSk1CcFpiTk5LcnJfZklXcC1ZTjh1RnJiUzRISnR6WUFleVpPVjVfeGh3WmlISmNsWi01VlpqQnZnVUJ3TE1zZnZmRndJbjJJS1I4V3VqTnpJYU5LcWlXVG1YM3doZU8xNmRZMWRxTzF5YTR1dllRUm5hMGlPX0toZnVmWGZ6VG84bzNNMjNEdXBfSHZ5UmxfNjdYMm03eQ?oc=5
- https://news.google.com/rss/articles/CBMi7AFBVV95cUxQdjFSTFJQS2s0ZEJaX3hjQU05Q1NQN2lNNEFrYVpmckZ4ekxhSlhVQXh2VUUyVnhsMVZpRWJCMkhnZXFkRWFaX1ZIV2o3SXFwM19iU0NqSWxDdkZpZWx4NW9oWGI2SE5aN3FmYUdkanNOeHh6UHl4RHFNUWh4LVZSRzJoaWJ6NVg2X0xLX0JGYzV1cGtWNC0wQV95eXh4SG5Fb09IeC1qT2JYaC1iU19Zd3E2REpZZm5oNzZhZTRSZEVnMks5cW40OTM4dElnNlZuY25KQ0hBdDhVYVE2R0FfRU1BT0ppX3JSYTFkcNIB8gFBVV95cUxPRHFmSDEzbHNWeko3VDBfc2s4eHF4Z3V6b25GdGFYTDhERF85N2NUMHJKMkt4ZTBsOGR3RnV5c29fanFEb2c0SW5OZW4ybnFKWDJLTkxiRUxHYnpDUzU5bC1QdU5tNGhUV3VXX19wWHFaYVhybVJXNTcwTW4tVUJPc1NtZ1VnbnhhemJLSGI2MEE5OXdESktqM3V3RDBLTUhGdkxlc3FuZjhMcVBTckxkaWZWNHkzVHU5cnBpNmpacFlPVTdNdVZ0WjZ4eEtrX25admxmRVNNc0dOUV9DZWgxUnNTaGQ4WldDUFIwd01faUF1Zw?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxNVUNNdGlpM3pLOHhmNGNDMXFyMTVibDdkcXAzSl9zSHczN2tQVjRIdUxXVXJnYnlIMHFjdThMQVM5emNVcVJuZ0VwWXl2U0hUdU11SkZya0M0QTVhZDlaQlpxNXlLUTVmc1FpVzVIdkJTUW9nTXBsM3pfQnU4WWVhY2hVR2l6RXRYaV9zVld6a2MzUldZUUFzRGt3NXhtb3JYN2NiOFltbXp6VG5Ja3ZQUUJVdFh2VXhCRmhB?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxQWGNseDhkbkZvSnZtYTBVSVZ0Q1FUUmdlT2U5VzZwaVNhMTNYSkVQdkRMMFpucjl6U3RZNkllOXBuNXU5NVVuLTI0Vzg5UzhPOGRRZ1JNUlNmMFlMTWd4Y28ybzF6OWJfMTdldnA0djBJSUJQTzlnQjlzTVFFQk9KTmhQNFRsS1JtaEVjT19YNmY1U2ZVUXVYU2hKSEljVkZmbzJkMlRMQ0VHMThub25hTg?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxPOGRBcmNBS0FxMkxoV3g1dE9sd3Q3bVI1dGN1bFpPT2tFVkxLNWxqd1l3LVN0eUNfZEVtSzA1VlRZN1N2MFJNdlBtYnBiOTZ5bGtwZFB1WmV2YlVVM0JWN3NmRlhPNFUxYXkxa2p4UnlNYmNHREJpTjdHVjFKLVVJV3ZkZzRfalYwS2JZbVRUVGVKVVFRYTdvTk5PVXQwelcxZkNTU016QzVKVWZFRXpaOUMxM3hOZUpuY09uZ2dmUS0ydw?oc=5
- https://news.google.com/rss/articles/CBMi6wFBVV95cUxOX0FFbi0yMjdKVFgtN0Q1aTdjRzU4ak9iS1R1bDMySVZfQ3EyRWRyUWlrcjBTd3pvM3hsclU1UEptODl0b2RlLUFJNGFYbV8wek1SUGt4ejQwZ09KbnFXN0hJOUVKUUl4RDNudUYzdFJaQWNFT0l5RGJFY3U3em4tN2tEdjZNcnBQNkNwaWZNN2VRR3JDcVNjV1pmR0UwREFNbkRxMUNzNnpabHJFSDA1UmgySFZsUVlqdmg3b1owRmRySm9zNW9ZRmUyc1NRaWRvVnQyaWkyaS1XcnYxWjhUdXpJMUFNZ016OG440gHwAUFVX3lxTE5RWm1KRUxKSjVBNVhvaEtSWUhKVk52Z3ZpWTdrRXRlRm03Y2NueE9yX2JWV20zN2FWQUppUlllUl9wR18yaUl2VUJjRVVEMTdtdzk5ZUlMdU9wdjVpdGF1OFRoT3lqUXBhSWtrU21CYmFyOTB1aVZrN05qOHpzUy1YWFFmZWtsTzhOX3dEejdTdzJRa0NTTjhhRlE2Y0dlbFM2TVZ5UE82QlRISFk3TzJoT0sxel9qY3RDRzRCWlo2MXcxVWRZSkFiNndGdmF5a2lWM3Z4ZU9XVERmVlIzdEZzQ3NZWU1FVGI0TjJ2emZpUQ?oc=5
- https://news.google.com/rss/articles/CBMi7AFBVV95cUxPZjlDSDg2MW9QSkNDQVZLQ1A4MlhBd216MWNYUVVpdjJuNWIxdmVPdmdTekN0TUdfanpOOFI2bzdRWUdYd0hURUFaeDRpLVlSQ3ZZb2RKbDQ2Y1hhb2FfeS13TDExNXpuZTVFV0h0M1ZHMXdCQmRtYTZlcjQwdThBcUtvYWVPYXBKaVgzSEZqQ0JTampVT05IQ2lWQmY3YWdaNHA2TzJDVFpweWpvd255SEFEU3JhNzdwNnoyRFdwN29meXVwUFRLZTVnZ0pXWlpmZERfV0EtbGtub0t6QWlMVVFHYm5iN1ZJb2Ryb9IB8gFBVV95cUxPcW9qT1dpUGlINXRRd1F6ajRKOWdLWExUaWVpakhYNXFPcXhaZnRNOG9Jc0N5cEdmRmdiN3Rlenk4ZzZqRFoyVUtBdFZnODBuQ3g4Z3NicGw0QkxabThWdWVCM3Q5ZGtHNGNuaG96aGgzcTBzU1N4WUFiR0dBWmZNaElWbkgzdlVJd3FtcFVaMTZGMHZaZy1MQ2ltX2Z3eWF3bVRnZUxldndad2hnYXd4ZXowUzdVOHpzUTltZ2JIRlMza1pzTWxad2l0Ml9VNUY1TmlabkpJZHF2ZVdDd2dLNjlCcU1rV2p4YmdOYXllWThpUQ?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxNZFFGaEtfQ3Utb2xmbldPOGJ0SVlPNW1PcGtNQjFxUXFVN3ljdV9ZVXMxb216OFBVSnR3ZjY5enRwMWo5dzBycWpCeFNrYmJCd2NfYjMtbWJJX0RfVm9wQXZlM2Y0OGJSQmxJUl85Tjc0UklxX2lXRWlkZkZRYXE4OC05bWM0b3VEV2E4N1RFLTB0MTZnTWFGSnpkQV9uTG9pRHlxNFZTRzBRYWJJRHk2NldiczFvQVFVUWo1R1hNc0tTNlVz?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxPZmNTNXltTG9Ua2g4RzhCUE13QWhkV1BPeUJhcmtlOS16SDVSazZlQUJBWlVHaXEzSlRMTWluSm5ob1lkQWZpRG9NX2QxbWRWWDFnWlB5bGJuQ1BGOTYyTjhaeG1VUXMtdjdNRVdnX2I0MVVTdzBCYi1vSDRsakc4RUh5X19JNTM0T0ZvYVpzRTk1NVkxUV9sQzZ3OVg2clU?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxQd0N5VzlRNWlVSUFkb0MwVE4zaE5HMWRQRWNKRmp5WVdHdDdvVE03RUMxWnNjN2p2ZVN5UF9RUzBpOWhia05SLTZxdDFOLWdYTmxlaDgxaHRVS1VCTWt1VG5aVXd6WXFrcWJEWWNQN1puaS1YMjFiUzNmRVItOWk2LUUxSVRRZjA5dXY4U0tpd0F5WjFrNXMyMS1zQlkyZGhDeDlvX3NYajRPeGF5MWUxeVB5SQ?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxPMUJCN2hFNzUwUi10U0dwVUZGS3hhbkdNYjFRV00yeWhZWkhtSVUyM0UxbXA4X2pJMllVQ3Fick9IY0pJU2NPR2pBNmZGZHdkM3RRSkJJRjlpQjRWeHhOX0pOZU01ZjNJYl8ycngwUW9DLVBINmVZNHlaTnd6aHZ3R01LcEVRMGpQSnBPTTlhN1pZQ2x6Ym1MOHV3UEpsVG41d1l1Sm0wNUdMdER2UV96Uk5tNDY0c0xyY2ljd3pB?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
