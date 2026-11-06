# VRTX Intelligence Report

- ticker: **VRTX**
- Report as_of: **2026-11-05**
- Market data as_of: **2026-11-05**
- Quant sources: https://finance.yahoo.com/quote/VRTX/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/VRTX/key-statistics/
- AI analysis snapshot as_of: **2026-11-05**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-06T05:11:24.799760+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 20, 'rule': 8, 'ai': 8, 'unknown': 0, 'irrelevant': 4})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **10** exact headline/source/date matches; prior report **20261105T045846Z-bde0a1fe/VRTX** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 20 unique headlines; 12 named publishers; 1 exact duplicates; 20 HTTPS source links; largest publisher share 20.0%; oldest publication 2026-10-31

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 542.5000 |
| Return 1D (%) | -1.1912 |
| Return 1W (%) | 0.4630 |
| Return 1M (%) | 7.7458 |
| Return YTD (%) | 19.6621 |
| Return 1Y (%) | 30.0959 |
| Annualized volatility (%) | 29.8338 |
| Beta vs SPY | 0.4496 |
| Max drawdown (%) | -15.2113 |
| Sharpe (rf=0) | 1.0331 |
| Downside deviation (rf=0, %) | 18.3047 |
| Sortino (rf=0) | 1.6837 |
| Historical VaR 95% (1D, %) | 2.8866 |
| Historical ES 95% (1D, %) | 3.4957 |
| Correlation vs SPY | 0.2049 |
| Tracking error vs SPY (%) | 30.1443 |
| P/E (trailing) | 35.34 |
| P/B | 6.58 |
| EV/EBITDA | 27.00 |
| Revenue growth (%) | 11.80 |
| Forward P/E (estimate) | 27.19 |
| Gross margin (%) | 54.81 |
| Operating margin (%) | 35.57 |
| Return on equity (%) | 20.80 |
| Free cash flow yield (%) | 1.70 |
| MA50 | 522.8078 |
| Close vs MA50 (%) | 3.7666 |
| MA200 | 481.1737 |
| Close vs MA200 (%) | 12.7451 |
| RSI (14, Wilder) | 56.4460 |
| MACD (12,26) | 8.4863 |
| MACD signal (9) | 5.4979 |
| MACD histogram | 2.9883 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'VRTX': 276, 'SPY': 276}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 542.5000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.1912 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 0.4630 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 7.7458 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 19.6621 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 30.0959 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 29.8338 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 18.3047 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.6837 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.8866 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.4957 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2049 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 30.1443 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.4496 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -15.2113 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.0331 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 27.1925 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 54.8090 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 35.5700 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 20.8020 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.6997 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 35.3420 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 56.4460 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 2.9883 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 3.7666 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 12.7451 -> Clearly above the moving-average trend level.

## TAILWINDS

### Vertex Pharmaceuticals Thrives on Higher Sales and Guidance
- Summary: Vertex Pharmaceuticals Thrives on Higher Sales and Guidance
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxNM0lyaGt0UEJxN19FZlRnRUdUX291SlVKQXJkd3NFZDlnWDdlRXRsM1NRUFc5SlpUNUQwS2lLWEhudTdJQ2xjUjV6Z0pfczVOZ0pEUlp4RnVXOG1tRlJiS1M2WjlySW82bmlralJUMS15RzhKMm9RSF91WlFNazBNRW9PZ1E1MXNYcncwM19lQUZ4RjY5ZFAzUXRqVkxoX0M1dVd3YnRkUEMwM2VjY193SjVn?oc=5>

### Vertex Pharmaceuticals’s (NASDAQ:VRTX) Q3 2026 sales top estimates
- Summary: Vertex Pharmaceuticals’s (NASDAQ:VRTX) Q3 2026 sales top estimates
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0AFBVV95cUxQcGVyQmVJenp3WUtvZjB0a0VsdGF4cVBkSGtabzRlOGxIMEdnb2dWRUpOdFJMQTBkZDBCcmhSdE05OHRJUW9mY0tlQ2hBajBMWW1yQjBxXzg0dFY2b1VQQUZBNFlZc29sSExORDIwaW1yTkpLWDVtZXZYYkhRdHJyUmEzYTF1Q1hzVWM5anhDb1N1TmtVZ0hpWUlpU00xVm91V2xoX3hkQllONkVBcXlGaDFmQlo0R0k1SEthZGxvWS00MFlfdVhPZ1FpSkhJWlhB?oc=5>

### Vertex Pharmaceuticals Analysts Raise Their Forecasts Following Q3 Results
- Summary: Vertex Pharmaceuticals Analysts Raise Their Forecasts Following Q3 Results
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi4wFBVV95cUxNdXBJYm1wR2x0ZUk0TG1tOFg2aVhmcnJUNmp3LThZNmRiMld1WXNRUG5LdUdsNTFseXBBLWRRTEdybzAtQkVVUndITWJsdWV4WHdWRE1XRE5YUkdGVTcwYVUxdmdWb2x0UEI0dURPME5mXzltMG5kU2lxMlVaSVdmUVRIRG1TcmFveUZxZ0NybmhkbFZJTWVhVmNEbmVrQkJIWm0zdFZnbDZnUHZfRVU3QXh6SW5OVGIwVE9hZDNsMU9LX0RMamsxY0xCVnFoS0JVZnhXQ2pVLVR6RjVuZk5SM0lKRQ?oc=5>

### Vertex raises 2026 revenue guidance following mixed Q3 results
- Summary: Vertex lifts 2026 revenue outlook after mixed Q3, signaling stronger future sales.
- Date: 2026-11-02 | Impact: high | Horizon: long | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxOQkxvczdERVJOZk1vRlAxV0lsOU5CVHlHM0t3OFNpaW9kVDRyYmlRY0ZuQk8zVy1tVTliQzJuclI1SHo0QlQwN3Z5Vk10UTNUUWtydlJRZTVwUXJkZVR0bHJteGsweEdCNkNOVHRIdjNwdVpDVTBoUDhxTkdIQldmVUhFdUppc19KUzl5ejM2TVBxMFNqTnVQejhLS1ZlbHZacEE?oc=5>

### Vertex Pharmaceuticals (VRTX) Revises 2026 Revenue Forecast Slig
- Summary: Revised 2026 revenue forecast upward.
- Date: 2026-11-03 | Impact: medium | Horizon: long | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxNQkhXbFpDRVBlV24zTm5rMElyTEQyVE84UnVCOW96cFBIa3lYS1VQWTVzTEhyYnhud0tCLUxBZ09QcG5SMTE0cUlsdlhnZUtHdHVfZXl0Z1g4NENSRTBJSDkxS2ZBcVIwczYxUW5vQWduQUktQzZQeGxscnlSZmFzYVNuYXBtZzJXc1dHR0Q1dDFsakxVbDc5bkhqM0xmeDdDMW1Ycm5acHBIdGxrQmY1UnVOMUU3WVhaVmRIRWdERW1yUQ?oc=5>

## HEADWINDS

### Vertex Pharmaceuticals (VRTX) Misses Q3 Earnings Estimates
- Summary: Vertex Pharmaceuticals (VRTX) Misses Q3 Earnings Estimates
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxPNDcyZzFRTnZad09oYmp1YWYzMV96MzFTN0xPVGZPbERldjc1TFZRNHE5YU1idUEtZC04bEFqSHQ1LWlSeGk1WmlvRzlCYnZ4T19ZU0hsS0VNMTFLcWhycFY4WFhIZmZ2TUpweEZfbUNSVDJUaXc4VW95U0dlNC1pZDBnbVFRVklYWTV5WkhqaGJzSGRwU2dKa1lEVmxtb0w4LUFQOQ?oc=5>

### Vertex (VRTX) Q3 Earnings: Taking a Look at Key Metrics Versus Estimates
- Summary: Q3 earnings analysis shows metrics below expectations.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxOVGMxMWdzSGREUl9GSVRlYzhUd0kxbVphdzdyd1cyckoxMWxZNlAyREdlM2FzMWVheDkzYklVOC0yUmRqVmlCNndhcUpRTG5HMlk3d0VlaHdrM1c1U244SC1rbElBVXVSZDU5V044VjhCWlIyLXdwT3Q0WHJjamVSMlFEZ1Fhdk5Wa1F6aUFFS1hHemhReHlRWHNWTQ?oc=5>

### Earnings Flash (VRTX) Vertex Pharmaceuticals Incorporated Posts Q3 Adjusted EPS $4.76 per Share, vs. FactSet Est of $4.82
- Summary: Q3 EPS missed estimates, indicating earnings pressure.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi4gFBVV95cUxPeHNUd3QtM0V5TFcwQ01jby1uSTRDSjdIa2tMWndZVEFOa2dkUkhpckc4aW1MVGtFSGVTTDFfNTU3Tm9seWJxbE1CWGRaYlBOUEFEYmxBQ2tIbG1ZWmprcjk2VmdpTmdqd21LU3NlT1B5TkNJSkJOOWp6WTRPaVlrX3NYYzI4OTMweHNZNW1jRnJ4eUNvd2tKWWlYandzRm9GVnc3b3hvQ2hSaDhXZ1FUX0p2bDVCX1B5ek9lam5iSkRKT1FnSFlEQnV4cmdOLWZqY3ZIQkNEUWJJN2RwTHJzcWZR?oc=5>

## CATALYSTS

### VRTX's Q3 Earnings Lag Estimates, Revenues Top, 2026 Sales View Raised
- Summary: VRTX's Q3 Earnings Lag Estimates, Revenues Top, 2026 Sales View Raised
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxPOGRBcmNBS0FxMkxoV3g1dE9sd3Q3bVI1dGN1bFpPT2tFVkxLNWxqd1l3LVN0eUNfZEVtSzA1VlRZN1N2MFJNdlBtYnBiOTZ5bGtwZFB1WmV2YlVVM0JWN3NmRlhPNFUxYXkxa2p4UnlNYmNHREJpTjdHVjFKLVVJV3ZkZzRfalYwS2JZbVRUVGVKVVFRYTdvTk5PVXQwelcxZkNTU016QzVKVWZFRXpaOUMxM3hOZUpuY09uZ2dmUS0ydw?oc=5>

### Vertex Pharmaceuticals (VRTX) Set to Report Q3 Earnings on Novem
- Summary: Vertex Pharmaceuticals (VRTX) Set to Report Q3 Earnings on Novem
- Date: 2026-11-01 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxNMUcySXV6cmhUVzl1X0tzWTNKbFNfaERVQzMxQ2JTbWxXX0ZrQW5rTHlBWGNMWTFCLXBKQzhWSWtBTnZFOHd6TzJqcmpBZDFWb3dtb0pZT2RuSDNKY2hhb0NSYnBYTUZZblBULXpEMm1Rd3dOMGVpN1BKUWs3S296YmZEX0pBRnVwVEE4UDZFWDJCdnAySzZyX20zZE15ZGhkYjhscjZYN3FVQQ?oc=5>

### Vertex Pharmaceuticals (VRTX) Stock Rethinks Q3 Results After Profit Squeeze
- Summary: Vertex Pharmaceuticals (VRTX) Stock Rethinks Q3 Results After Profit Squeeze
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi6wFBVV95cUxOX0FFbi0yMjdKVFgtN0Q1aTdjRzU4ak9iS1R1bDMySVZfQ3EyRWRyUWlrcjBTd3pvM3hsclU1UEptODl0b2RlLUFJNGFYbV8wek1SUGt4ejQwZ09KbnFXN0hJOUVKUUl4RDNudUYzdFJaQWNFT0l5RGJFY3U3em4tN2tEdjZNcnBQNkNwaWZNN2VRR3JDcVNjV1pmR0UwREFNbkRxMUNzNnpabHJFSDA1UmgySFZsUVlqdmg3b1owRmRySm9zNW9ZRmUyc1NRaWRvVnQyaWkyaS1XcnYxWjhUdXpJMUFNZ016OG440gHwAUFVX3lxTE5RWm1KRUxKSjVBNVhvaEtSWUhKVk52Z3ZpWTdrRXRlRm03Y2NueE9yX2JWV20zN2FWQUppUlllUl9wR18yaUl2VUJjRVVEMTdtdzk5ZUlMdU9wdjVpdGF1OFRoT3lqUXBhSWtrU21CYmFyOTB1aVZrN05qOHpzUy1YWFFmZWtsTzhOX3dEejdTdzJRa0NTTjhhRlE2Y0dlbFM2TVZ5UE82QlRISFk3TzJoT0sxel9qY3RDRzRCWlo2MXcxVWRZSkFiNndGdmF5a2lWM3Z4ZU9XVERmVlIzdEZzQ3NZWU1FVGI0TjJ2emZpUQ?oc=5>

### Vertex Pharmaceuticals earnings: what to look for from VRTX
- Summary: Vertex Pharmaceuticals earnings: what to look for from VRTX
- Date: 2026-11-01 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxOd0N4VUVaYjRYaHphMkxPZEZjSkZJdFBTQ1BzYUVpcVVoRVZILXpmNWxkU1BqcWxPQkZLT21JLUhHNWFSalRWQjJpVEJSSWRsM3RjTER3SUdCWmxhWE1BMFJtZzVBWnZEaUNYUWtlOVJjVE5GUHZvam9veERwSlJXcjh1YnBDTEZqQkY0WjVwdzVyVXk4MG1YUjdmYi1uenpsbVRpbUtITmtIQUNnMWcxSG1UalJTeXF4WU93?oc=5>

### Vertex Q3 Earnings Call Highlights Revenue Beat and Pipeline Expansion
- Summary: Q3 earnings beat expectations, pipeline expands.
- Date: 2026-11-03 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxNZFFGaEtfQ3Utb2xmbldPOGJ0SVlPNW1PcGtNQjFxUXFVN3ljdV9ZVXMxb216OFBVSnR3ZjY5enRwMWo5dzBycWpCeFNrYmJCd2NfYjMtbWJJX0RfVm9wQXZlM2Y0OGJSQmxJUl85Tjc0UklxX2lXRWlkZkZRYXE4OC05bWM0b3VEV2E4N1RFLTB0MTZnTWFGSnpkQV9uTG9pRHlxNFZTRzBRYWJJRHk2NldiczFvQVFVUWo1R1hNc0tTNlVz?oc=5>

### VRTX Q3 deep dive: Pipeline, product launches, and Crinetics integration shape outlook
- Summary: Analysis of Q3 results, pipeline updates, and Crinetics integration; provides outlook for future performance.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi3AFBVV95cUxOR3NWVFd3OHc3R05XTFh1dWdFSDRkREVLQ2E2eVBVVGhrT0FYMTNWTUd6elJua1BYZXZfbGczWHhGd3lnY2x6dDZrZ21MSHl2SEtjcW96d002ZTg5REp5enZwV1VhT1FfUlN2M2phVzBIZkx6ZDZRaXNvemRhR09ERXpWR3ViSVk5LW5tSGtZSENUV0QtVmk1cDRxUW40M3NCbFI3SkQ0SERxbkgyeVNYWFZhX0ZIeHowYTBzVUwxNXN0MUxhVXl5VFp3cnRRLVNqSmw1SnBfclM2bFNk?oc=5>

### Up to $13.25 billion: Vertex raises its 2026 revenue forecast.
- Summary: Vertex raises 2026 revenue forecast to $13.25B.
- Date: 2026-11-02 | Impact: high | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxPZmNTNXltTG9Ua2g4RzhCUE13QWhkV1BPeUJhcmtlOS16SDVSazZlQUJBWlVHaXEzSlRMTWluSm5ob1lkQWZpRG9NX2QxbWRWWDFnWlB5bGJuQ1BGOTYyTjhaeG1VUXMtdjdNRVdnX2I0MVVTdzBCYi1vSDRsakc4RUh5X19JNTM0T0ZvYVpzRTk1NVkxUV9sQzZ3OVg2clU?oc=5>

### Vertex Pharmaceuticals (VRTX) Stock Looks Cheap Next To Its Cash Flow
- Summary: Vertex’s stock appears undervalued relative to its cash flow, suggesting potential upside for investors.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi7AFBVV95cUxQcUVUWmlrQm9JQzFTLWotR1hOM3JBbFV5ZUltelFVdEpiVHlPc1had1RQREY1MHNrVGNaMlN3bm5McGwwU1NaNi1fZUJ6UGI1NjZTc3RPZHlYdXlSeGxxMkhIclBaT0E4UnBNckp5VERuVExISXgzY3k1d3E0UFNmZVJJWFl6ZVVCcnRfSks2ZmlmM2lUckRULXp6WXN5QUcyM1ZpSnZrWXJFMG9saFlGUU5IWk5NVUlPZFdJTENUU0R0cTJZMFIwZTI2Vkl3TUFHZXNGTWNPTzlhM2xXZ1NOQjBUOXdVbE5MNjlBWNIB8gFBVV95cUxOWTJDOUJHbkt5a1BhWkRFVU95aTkxMWhJRGtDOTEwSXFxbHdTQ0d6aXlDeTdmeVZFVWVGNWc4dm5XNjBxRjVQYTRPRlMxZnNFNUNVR3ZvT2kzUFZNUWJfeTZvdjJPOXFRVlFuVjdlU2h5Y0w3YVNVZE5jSW1MRzRFNXJPd0NLSDBmRi1jSi1HdFVrYVZVMTlTLXBKM21JbzQ4Y282ZnpUZ2dEUkR4aVpGSllqVENlcjZkaUU5UC14VmludmJmcEtLdlFQM0VDaW9pd2ZBMGVTRDAtNDdOQ19uOGNmeldJOE1iUE5ncUxNdW1xUQ?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **VRTX** | **35.34** | **6.58** | **27.00** | **11.80** | **137,544,187,904.00 USD** | **30.10** |
| REGN | 20.57 | 2.70 | 14.88 | 36.30 | 93,403,070,464.00 USD | 40.88 |
| BIIB | 110.38 | 1.91 | 12.89 | 10.60 | 36,057,784,320.00 USD | 58.98 |
| AMGN | 26.68 | 17.35 | 17.35 | 8.50 | 248,970,739,712.00 USD | 47.89 |

Peers fetched as_of: 2026-11-05; VRTX reuses existing data (market data as_of: 2026-11-05); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-02
- Next expected earnings: 2027-02-11 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-05

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
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
- https://news.google.com/rss/articles/CBMi0AFBVV95cUxQcGVyQmVJenp3WUtvZjB0a0VsdGF4cVBkSGtabzRlOGxIMEdnb2dWRUpOdFJMQTBkZDBCcmhSdE05OHRJUW9mY0tlQ2hBajBMWW1yQjBxXzg0dFY2b1VQQUZBNFlZc29sSExORDIwaW1yTkpLWDVtZXZYYkhRdHJyUmEzYTF1Q1hzVWM5anhDb1N1TmtVZ0hpWUlpU00xVm91V2xoX3hkQllONkVBcXlGaDFmQlo0R0k1SEthZGxvWS00MFlfdVhPZ1FpSkhJWlhB?oc=5
- https://news.google.com/rss/articles/CBMi4wFBVV95cUxNdXBJYm1wR2x0ZUk0TG1tOFg2aVhmcnJUNmp3LThZNmRiMld1WXNRUG5LdUdsNTFseXBBLWRRTEdybzAtQkVVUndITWJsdWV4WHdWRE1XRE5YUkdGVTcwYVUxdmdWb2x0UEI0dURPME5mXzltMG5kU2lxMlVaSVdmUVRIRG1TcmFveUZxZ0NybmhkbFZJTWVhVmNEbmVrQkJIWm0zdFZnbDZnUHZfRVU3QXh6SW5OVGIwVE9hZDNsMU9LX0RMamsxY0xCVnFoS0JVZnhXQ2pVLVR6RjVuZk5SM0lKRQ?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxOQkxvczdERVJOZk1vRlAxV0lsOU5CVHlHM0t3OFNpaW9kVDRyYmlRY0ZuQk8zVy1tVTliQzJuclI1SHo0QlQwN3Z5Vk10UTNUUWtydlJRZTVwUXJkZVR0bHJteGsweEdCNkNOVHRIdjNwdVpDVTBoUDhxTkdIQldmVUhFdUppc19KUzl5ejM2TVBxMFNqTnVQejhLS1ZlbHZacEE?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxNQkhXbFpDRVBlV24zTm5rMElyTEQyVE84UnVCOW96cFBIa3lYS1VQWTVzTEhyYnhud0tCLUxBZ09QcG5SMTE0cUlsdlhnZUtHdHVfZXl0Z1g4NENSRTBJSDkxS2ZBcVIwczYxUW5vQWduQUktQzZQeGxscnlSZmFzYVNuYXBtZzJXc1dHR0Q1dDFsakxVbDc5bkhqM0xmeDdDMW1Ycm5acHBIdGxrQmY1UnVOMUU3WVhaVmRIRWdERW1yUQ?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxPNDcyZzFRTnZad09oYmp1YWYzMV96MzFTN0xPVGZPbERldjc1TFZRNHE5YU1idUEtZC04bEFqSHQ1LWlSeGk1WmlvRzlCYnZ4T19ZU0hsS0VNMTFLcWhycFY4WFhIZmZ2TUpweEZfbUNSVDJUaXc4VW95U0dlNC1pZDBnbVFRVklYWTV5WkhqaGJzSGRwU2dKa1lEVmxtb0w4LUFQOQ?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxOVGMxMWdzSGREUl9GSVRlYzhUd0kxbVphdzdyd1cyckoxMWxZNlAyREdlM2FzMWVheDkzYklVOC0yUmRqVmlCNndhcUpRTG5HMlk3d0VlaHdrM1c1U244SC1rbElBVXVSZDU5V044VjhCWlIyLXdwT3Q0WHJjamVSMlFEZ1Fhdk5Wa1F6aUFFS1hHemhReHlRWHNWTQ?oc=5
- https://news.google.com/rss/articles/CBMi4gFBVV95cUxPeHNUd3QtM0V5TFcwQ01jby1uSTRDSjdIa2tMWndZVEFOa2dkUkhpckc4aW1MVGtFSGVTTDFfNTU3Tm9seWJxbE1CWGRaYlBOUEFEYmxBQ2tIbG1ZWmprcjk2VmdpTmdqd21LU3NlT1B5TkNJSkJOOWp6WTRPaVlrX3NYYzI4OTMweHNZNW1jRnJ4eUNvd2tKWWlYandzRm9GVnc3b3hvQ2hSaDhXZ1FUX0p2bDVCX1B5ek9lam5iSkRKT1FnSFlEQnV4cmdOLWZqY3ZIQkNEUWJJN2RwTHJzcWZR?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxPOGRBcmNBS0FxMkxoV3g1dE9sd3Q3bVI1dGN1bFpPT2tFVkxLNWxqd1l3LVN0eUNfZEVtSzA1VlRZN1N2MFJNdlBtYnBiOTZ5bGtwZFB1WmV2YlVVM0JWN3NmRlhPNFUxYXkxa2p4UnlNYmNHREJpTjdHVjFKLVVJV3ZkZzRfalYwS2JZbVRUVGVKVVFRYTdvTk5PVXQwelcxZkNTU016QzVKVWZFRXpaOUMxM3hOZUpuY09uZ2dmUS0ydw?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxNMUcySXV6cmhUVzl1X0tzWTNKbFNfaERVQzMxQ2JTbWxXX0ZrQW5rTHlBWGNMWTFCLXBKQzhWSWtBTnZFOHd6TzJqcmpBZDFWb3dtb0pZT2RuSDNKY2hhb0NSYnBYTUZZblBULXpEMm1Rd3dOMGVpN1BKUWs3S296YmZEX0pBRnVwVEE4UDZFWDJCdnAySzZyX20zZE15ZGhkYjhscjZYN3FVQQ?oc=5
- https://news.google.com/rss/articles/CBMi6wFBVV95cUxOX0FFbi0yMjdKVFgtN0Q1aTdjRzU4ak9iS1R1bDMySVZfQ3EyRWRyUWlrcjBTd3pvM3hsclU1UEptODl0b2RlLUFJNGFYbV8wek1SUGt4ejQwZ09KbnFXN0hJOUVKUUl4RDNudUYzdFJaQWNFT0l5RGJFY3U3em4tN2tEdjZNcnBQNkNwaWZNN2VRR3JDcVNjV1pmR0UwREFNbkRxMUNzNnpabHJFSDA1UmgySFZsUVlqdmg3b1owRmRySm9zNW9ZRmUyc1NRaWRvVnQyaWkyaS1XcnYxWjhUdXpJMUFNZ016OG440gHwAUFVX3lxTE5RWm1KRUxKSjVBNVhvaEtSWUhKVk52Z3ZpWTdrRXRlRm03Y2NueE9yX2JWV20zN2FWQUppUlllUl9wR18yaUl2VUJjRVVEMTdtdzk5ZUlMdU9wdjVpdGF1OFRoT3lqUXBhSWtrU21CYmFyOTB1aVZrN05qOHpzUy1YWFFmZWtsTzhOX3dEejdTdzJRa0NTTjhhRlE2Y0dlbFM2TVZ5UE82QlRISFk3TzJoT0sxel9qY3RDRzRCWlo2MXcxVWRZSkFiNndGdmF5a2lWM3Z4ZU9XVERmVlIzdEZzQ3NZWU1FVGI0TjJ2emZpUQ?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxOd0N4VUVaYjRYaHphMkxPZEZjSkZJdFBTQ1BzYUVpcVVoRVZILXpmNWxkU1BqcWxPQkZLT21JLUhHNWFSalRWQjJpVEJSSWRsM3RjTER3SUdCWmxhWE1BMFJtZzVBWnZEaUNYUWtlOVJjVE5GUHZvam9veERwSlJXcjh1YnBDTEZqQkY0WjVwdzVyVXk4MG1YUjdmYi1uenpsbVRpbUtITmtIQUNnMWcxSG1UalJTeXF4WU93?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxNZFFGaEtfQ3Utb2xmbldPOGJ0SVlPNW1PcGtNQjFxUXFVN3ljdV9ZVXMxb216OFBVSnR3ZjY5enRwMWo5dzBycWpCeFNrYmJCd2NfYjMtbWJJX0RfVm9wQXZlM2Y0OGJSQmxJUl85Tjc0UklxX2lXRWlkZkZRYXE4OC05bWM0b3VEV2E4N1RFLTB0MTZnTWFGSnpkQV9uTG9pRHlxNFZTRzBRYWJJRHk2NldiczFvQVFVUWo1R1hNc0tTNlVz?oc=5
- https://news.google.com/rss/articles/CBMi3AFBVV95cUxOR3NWVFd3OHc3R05XTFh1dWdFSDRkREVLQ2E2eVBVVGhrT0FYMTNWTUd6elJua1BYZXZfbGczWHhGd3lnY2x6dDZrZ21MSHl2SEtjcW96d002ZTg5REp5enZwV1VhT1FfUlN2M2phVzBIZkx6ZDZRaXNvemRhR09ERXpWR3ViSVk5LW5tSGtZSENUV0QtVmk1cDRxUW40M3NCbFI3SkQ0SERxbkgyeVNYWFZhX0ZIeHowYTBzVUwxNXN0MUxhVXl5VFp3cnRRLVNqSmw1SnBfclM2bFNk?oc=5
- https://news.google.com/rss/articles/CBMi4AFBVV95cUxNUWxBR1pRVnNsNmpRWlB1YkVDS2pTX3ZvTUJuTkU5WjIxX3IwbW9rdXY4MjJkV0pjYzhvMlJmR1N5LWF1RmJXWF9MWE92akVxbDBnNWN6MDA4eG5XQ0p1cUF3NkVnYjB6aXNyWFNhR0lXRVZZdFVOTURnQmdPNlVyZWE2T1ZEbWRDTW03SHBTMDNaZXpMWU15TmFNRnBUeVNQQktXbm9MdURFOVdQUDdyN0Y0RnhwUnFkYldaNnQxVGF6Mlpmdktia05lTVBqdFdWUlU5eWRkS3VqekEyNm0zMQ?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxPZmNTNXltTG9Ua2g4RzhCUE13QWhkV1BPeUJhcmtlOS16SDVSazZlQUJBWlVHaXEzSlRMTWluSm5ob1lkQWZpRG9NX2QxbWRWWDFnWlB5bGJuQ1BGOTYyTjhaeG1VUXMtdjdNRVdnX2I0MVVTdzBCYi1vSDRsakc4RUh5X19JNTM0T0ZvYVpzRTk1NVkxUV9sQzZ3OVg2clU?oc=5
- https://news.google.com/rss/articles/CBMi7AFBVV95cUxQcUVUWmlrQm9JQzFTLWotR1hOM3JBbFV5ZUltelFVdEpiVHlPc1had1RQREY1MHNrVGNaMlN3bm5McGwwU1NaNi1fZUJ6UGI1NjZTc3RPZHlYdXlSeGxxMkhIclBaT0E4UnBNckp5VERuVExISXgzY3k1d3E0UFNmZVJJWFl6ZVVCcnRfSks2ZmlmM2lUckRULXp6WXN5QUcyM1ZpSnZrWXJFMG9saFlGUU5IWk5NVUlPZFdJTENUU0R0cTJZMFIwZTI2Vkl3TUFHZXNGTWNPTzlhM2xXZ1NOQjBUOXdVbE5MNjlBWNIB8gFBVV95cUxOWTJDOUJHbkt5a1BhWkRFVU95aTkxMWhJRGtDOTEwSXFxbHdTQ0d6aXlDeTdmeVZFVWVGNWc4dm5XNjBxRjVQYTRPRlMxZnNFNUNVR3ZvT2kzUFZNUWJfeTZvdjJPOXFRVlFuVjdlU2h5Y0w3YVNVZE5jSW1MRzRFNXJPd0NLSDBmRi1jSi1HdFVrYVZVMTlTLXBKM21JbzQ4Y282ZnpUZ2dEUkR4aVpGSllqVENlcjZkaUU5UC14VmludmJmcEtLdlFQM0VDaW9pd2ZBMGVTRDAtNDdOQ19uOGNmeldJOE1iUE5ncUxNdW1xUQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
