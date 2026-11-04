# VRTX Intelligence Report

- ticker: **VRTX**
- Report as_of: **2026-11-03**
- Market data as_of: **2026-11-03**
- Quant sources: https://finance.yahoo.com/quote/VRTX/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/VRTX/key-statistics/
- AI analysis snapshot as_of: **2026-11-03**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-04T04:48:53.471466+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 7, 'ai': 11, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **8** exact headline/source/date matches; prior report **20261103T051441Z-8b1c85d8/VRTX** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'directional_claim_without_event_type': 1, 'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 13 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 33.33%; oldest publication 2026-10-28

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 530.7600 |
| Return 1D (%) | -4.0477 |
| Return 1W (%) | 1.8675 |
| Return 1M (%) | 5.1572 |
| Return YTD (%) | 17.0725 |
| Return 1Y (%) | 24.5916 |
| Annualized volatility (%) | 29.6640 |
| Beta vs SPY | 0.4447 |
| Max drawdown (%) | -15.2113 |
| Sharpe (rf=0) | 0.8908 |
| Downside deviation (rf=0, %) | 18.3277 |
| Sortino (rf=0) | 1.4418 |
| Historical VaR 95% (1D, %) | 2.8866 |
| Historical ES 95% (1D, %) | 3.4957 |
| Correlation vs SPY | 0.1919 |
| Tracking error vs SPY (%) | 29.9676 |
| P/E (trailing) | 35.60 |
| P/B | 7.22 |
| EV/EBITDA | 26.34 |
| Revenue growth (%) | 12.50 |
| Forward P/E (estimate) | 26.53 |
| Gross margin (%) | 54.96 |
| Operating margin (%) | 38.05 |
| Return on equity (%) | 23.54 |
| Free cash flow yield (%) | 1.95 |
| MA50 | 522.9798 |
| Close vs MA50 (%) | 1.4877 |
| MA200 | 480.2321 |
| Close vs MA200 (%) | 10.5216 |
| RSI (14, Wilder) | 53.1178 |
| MACD (12,26) | 7.5515 |
| MACD signal (9) | 3.8331 |
| MACD histogram | 3.7184 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'VRTX': 274, 'SPY': 274}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 530.7600 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -4.0477 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 1.8675 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 5.1572 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 17.0725 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 24.5916 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 29.6640 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 18.3277 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.4418 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.8866 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.4957 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.1919 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 29.9676 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.4447 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -15.2113 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.8908 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 26.5317 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 54.9570 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 38.0550 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 23.5430 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.9547 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 35.5976 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 53.1178 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 3.7184 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 1.4877 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 10.5216 -> Clearly above the moving-average trend level.

## TAILWINDS

### Vertex Pharmaceuticals Analysts Raise Their Forecasts Following Q3 Results
- Summary: Vertex Pharmaceuticals Analysts Raise Their Forecasts Following Q3 Results
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi4wFBVV95cUxNdXBJYm1wR2x0ZUk0TG1tOFg2aVhmcnJUNmp3LThZNmRiMld1WXNRUG5LdUdsNTFseXBBLWRRTEdybzAtQkVVUndITWJsdWV4WHdWRE1XRE5YUkdGVTcwYVUxdmdWb2x0UEI0dURPME5mXzltMG5kU2lxMlVaSVdmUVRIRG1TcmFveUZxZ0NybmhkbFZJTWVhVmNEbmVrQkJIWm0zdFZnbDZnUHZfRVU3QXh6SW5OVGIwVE9hZDNsMU9LX0RMamsxY0xCVnFoS0JVZnhXQ2pVLVR6RjVuZk5SM0lKRQ?oc=5>

### Vertex Pharmaceuticals’s (NASDAQ:VRTX) Q3 2026 sales top estimates
- Summary: Vertex Pharmaceuticals’s (NASDAQ:VRTX) Q3 2026 sales top estimates
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0AFBVV95cUxQcGVyQmVJenp3WUtvZjB0a0VsdGF4cVBkSGtabzRlOGxIMEdnb2dWRUpOdFJMQTBkZDBCcmhSdE05OHRJUW9mY0tlQ2hBajBMWW1yQjBxXzg0dFY2b1VQQUZBNFlZc29sSExORDIwaW1yTkpLWDVtZXZYYkhRdHJyUmEzYTF1Q1hzVWM5anhDb1N1TmtVZ0hpWUlpU00xVm91V2xoX3hkQllONkVBcXlGaDFmQlo0R0k1SEthZGxvWS00MFlfdVhPZ1FpSkhJWlhB?oc=5>

### VERTEX PHARMACEUTICALS ($VRTX) Releases Q3 2026 Earnings, Stock Rises
- Summary: VERTEX PHARMACEUTICALS ($VRTX) Releases Q3 2026 Earnings, Stock Rises
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxPUWtrcEtLVWhscXVpcmQwSHBEY05EM0RYaEJaaTJqUzktOXp6RzBGT0l2WF9nc0h0UzJOVktZdkRkR0t0S2cyd2w5SzRSeWlPMEYxUVdwY1IwN0ZwWXFqanV4c0hMYi1XYlltUHZFWWxFaktIOVpZMnRmZGJVR1ZwZEc3SnBaeFhueF9kVnNKZ3Y3c2ZuZW5rb1YzaG9aSjhVUEtWM1RlZW1jSWJVbkRv?oc=5>

### Here is What to Know Beyond Why Vertex Pharmaceuticals Incorporated (VRTX) is a Trending Stock
- Summary: General information about Vertex’s trending status.
- Date: 2026-10-28 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxQQVdrekpkclVkTF93RUxySVd2Tm0tYmJibzdpUUNLdlZuZTlwM1A3NWxjcWpxbkNaOEhBUkVSaTcyOVdSd3Zvd29xT3dFMXpYb0N4eEl0MkN0U25BdERES0ZpbG5tTVdOemQxc0lwaVBOVjI3WTB5aERPbndUYWVqMVpzRW1rQnoyVlo4N2VrbzhIZHlXQk9YZExXQnBtMjJFZ0VrUzZR?oc=5>

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

### Vertex Pharmaceuticals earnings: what to look for from VRTX
- Summary: Vertex Pharmaceuticals earnings: what to look for from VRTX
- Date: 2026-11-01 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxPeWFMdHNCUHVYcW13dkRPZjFvdVpMV19kRlpZb3JHWU5mcndEc1hsMV81YzZYZnhHbWQ2bEV6T3dYUkdONy1uRDJfTXR5WEpCbGhWN1lKZThoazV4VmNSSk4zYXU0LVB3WjhaYTVqTnNiTmhkdHU4aXlWZDRIdE92WlhBbDdOUkNnWjlrWlBYQy1ubVFrVFQwTkJldzBuYUN4Mk5KSA?oc=5>

### Ahead of Vertex (VRTX) Q3 Earnings: Get Ready With Wall Street Estimates for Key Metrics
- Summary: Upcoming Q3 earnings estimates.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxQdXJROFhGNXJCQTZoUDlrdDJoU2FieHZidWZmNTY0X2I3WVRoVDYtaEY4ZnhUdTc4VEpmekVJTlh1V3ZFeVd4VjcwdVdhZkpiaDlXdXlxc2ZfQ1NsUm43cl9oRTlONXVyYkp3Z0hXbE9zOG5EdThfM3F4amhWM0RyUHFwN3M5bGVxcUR3R3R4NUxKVG5KSDZVMmhn?oc=5>

### Vertex Q3 Earnings Call Highlights Revenue Beat and Pipeline Expansion
- Summary: Q3 earnings beat expectations, pipeline expands.
- Date: 2026-11-03 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxNZFFGaEtfQ3Utb2xmbldPOGJ0SVlPNW1PcGtNQjFxUXFVN3ljdV9ZVXMxb216OFBVSnR3ZjY5enRwMWo5dzBycWpCeFNrYmJCd2NfYjMtbWJJX0RfVm9wQXZlM2Y0OGJSQmxJUl85Tjc0UklxX2lXRWlkZkZRYXE4OC05bWM0b3VEV2E4N1RFLTB0MTZnTWFGSnpkQV9uTG9pRHlxNFZTRzBRYWJJRHk2NldiczFvQVFVUWo1R1hNc0tTNlVz?oc=5>

### VRTX Q3 deep dive: Pipeline, product launches, and Crinetics integration shape outlook
- Summary: Analysis of Q3 results, pipeline updates, and Crinetics integration; provides outlook for future performance.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi3AFBVV95cUxOR3NWVFd3OHc3R05XTFh1dWdFSDRkREVLQ2E2eVBVVGhrT0FYMTNWTUd6elJua1BYZXZfbGczWHhGd3lnY2x6dDZrZ21MSHl2SEtjcW96d002ZTg5REp5enZwV1VhT1FfUlN2M2phVzBIZkx6ZDZRaXNvemRhR09ERXpWR3ViSVk5LW5tSGtZSENUV0QtVmk1cDRxUW40M3NCbFI3SkQ0SERxbkgyeVNYWFZhX0ZIeHowYTBzVUwxNXN0MUxhVXl5VFp3cnRRLVNqSmw1SnBfclM2bFNk?oc=5>

### CRSP, VRTX Stocks Surge As FDA Clears Casgevy For Children Ages 2 And Up
- Summary: FDA clearance of Casgevy for children boosts stock; indicates product launch success.
- Date: 2026-10-31 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMi0AFBVV95cUxOYktrRnhKM1NTMmJLOGE5VW1jYU5QX3N4VmZWanhjMklxX0d1X3NzN0tmb21LNVJlOTFWZzVlamhPYWo0SDM5aUwtZkFkOURGRDNfWm9BQkh3NjYxTkhPVll0UFA0S1ZEYm5Ock9iMURqa1llQjBlSUdlaFlsbXdVWktodllGcVZoQUN2aWg5QzJmMVdLdnVTUWd2U1Y5MWJHSkJ3UTNCTFRKSFB1NFY1Sy1hVkNWbFVsVFJQOTVLQTg2VGkzWG91ekF1MkFkMVRf?oc=5>

### Vertex Pharma's FDA kidney drug ruling: what investors need to know
- Summary: FDA ruling on kidney drug impacts product pipeline and investor outlook.
- Date: 2026-11-03 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxPdW9vS2VHbzl6VVBsTzVyNWdRMHNEenlLazIxdWRRM25jS1JBQ3JsVnR5UGtNM3N6bnMyV29xV0lpRW1JMnBGdjBqZHhCWXJxQjNlMk1NZmo4Tk1GUXJyZGRHZC1RRlJvRnh4cWQ0MWt2V0ZzMTV0djd6TjhLTVpYNTBZWlBBbkYzbnRfUkFOdE9TTFNIbzZpQ01LV2ZmbklpWkNyT1l6SmxLbzFWTU9mTXUzaGZ3cDUwUlNoVEVYeG04amc?oc=5>

### Vertex Stock May See Further Appreciation on Approval, Launch of Povetacicept, RBC Says
- Summary: RBC predicts Vertex stock could rise after approval and launch of Povetacicept, indicating potential upside for investors.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxPemxMYk1Cc3YxMm42Wm1HOWxKYlJNVjcxblFNZXZXZjBaTmxBeS1Icl9JcGd4dTN3OGRUcTllMXJWZUdvWmpiYTNiSjBTeVdXd1owdjYzZlM3Unlsa05acWszZ2VxdG56aVdXV2ZpOVY4V1oxb1J3M1pqMnh6VnJCODZDTFdfdWprVTJERlcyajByNWpTRGNFUw?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **VRTX** | **35.60** | **7.22** | **26.34** | **12.50** | **134,441,508,864.00 USD** | **24.59** |
| REGN | 21.52 | 2.91 | 16.13 | 36.30 | 100,692,000,768.00 USD | 52.33 |
| BIIB | 107.76 | 1.94 | 13.11 | 10.60 | 36,796,887,040.00 USD | 64.38 |
| AMGN | 28.92 | 21.33 | 16.95 | 9.50 | 249,371,918,336.00 USD | 59.99 |

Peers fetched as_of: 2026-11-03; VRTX reuses existing data (market data as_of: 2026-11-03); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-02
- Next expected earnings: 2027-02-11 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-03

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

- https://news.google.com/rss/articles/CBMi4wFBVV95cUxNdXBJYm1wR2x0ZUk0TG1tOFg2aVhmcnJUNmp3LThZNmRiMld1WXNRUG5LdUdsNTFseXBBLWRRTEdybzAtQkVVUndITWJsdWV4WHdWRE1XRE5YUkdGVTcwYVUxdmdWb2x0UEI0dURPME5mXzltMG5kU2lxMlVaSVdmUVRIRG1TcmFveUZxZ0NybmhkbFZJTWVhVmNEbmVrQkJIWm0zdFZnbDZnUHZfRVU3QXh6SW5OVGIwVE9hZDNsMU9LX0RMamsxY0xCVnFoS0JVZnhXQ2pVLVR6RjVuZk5SM0lKRQ?oc=5
- https://news.google.com/rss/articles/CBMi0AFBVV95cUxQcGVyQmVJenp3WUtvZjB0a0VsdGF4cVBkSGtabzRlOGxIMEdnb2dWRUpOdFJMQTBkZDBCcmhSdE05OHRJUW9mY0tlQ2hBajBMWW1yQjBxXzg0dFY2b1VQQUZBNFlZc29sSExORDIwaW1yTkpLWDVtZXZYYkhRdHJyUmEzYTF1Q1hzVWM5anhDb1N1TmtVZ0hpWUlpU00xVm91V2xoX3hkQllONkVBcXlGaDFmQlo0R0k1SEthZGxvWS00MFlfdVhPZ1FpSkhJWlhB?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxPUWtrcEtLVWhscXVpcmQwSHBEY05EM0RYaEJaaTJqUzktOXp6RzBGT0l2WF9nc0h0UzJOVktZdkRkR0t0S2cyd2w5SzRSeWlPMEYxUVdwY1IwN0ZwWXFqanV4c0hMYi1XYlltUHZFWWxFaktIOVpZMnRmZGJVR1ZwZEc3SnBaeFhueF9kVnNKZ3Y3c2ZuZW5rb1YzaG9aSjhVUEtWM1RlZW1jSWJVbkRv?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxQQVdrekpkclVkTF93RUxySVd2Tm0tYmJibzdpUUNLdlZuZTlwM1A3NWxjcWpxbkNaOEhBUkVSaTcyOVdSd3Zvd29xT3dFMXpYb0N4eEl0MkN0U25BdERES0ZpbG5tTVdOemQxc0lwaVBOVjI3WTB5aERPbndUYWVqMVpzRW1rQnoyVlo4N2VrbzhIZHlXQk9YZExXQnBtMjJFZ0VrUzZR?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxOQkxvczdERVJOZk1vRlAxV0lsOU5CVHlHM0t3OFNpaW9kVDRyYmlRY0ZuQk8zVy1tVTliQzJuclI1SHo0QlQwN3Z5Vk10UTNUUWtydlJRZTVwUXJkZVR0bHJteGsweEdCNkNOVHRIdjNwdVpDVTBoUDhxTkdIQldmVUhFdUppc19KUzl5ejM2TVBxMFNqTnVQejhLS1ZlbHZacEE?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxNQkhXbFpDRVBlV24zTm5rMElyTEQyVE84UnVCOW96cFBIa3lYS1VQWTVzTEhyYnhud0tCLUxBZ09QcG5SMTE0cUlsdlhnZUtHdHVfZXl0Z1g4NENSRTBJSDkxS2ZBcVIwczYxUW5vQWduQUktQzZQeGxscnlSZmFzYVNuYXBtZzJXc1dHR0Q1dDFsakxVbDc5bkhqM0xmeDdDMW1Ycm5acHBIdGxrQmY1UnVOMUU3WVhaVmRIRWdERW1yUQ?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxPNDcyZzFRTnZad09oYmp1YWYzMV96MzFTN0xPVGZPbERldjc1TFZRNHE5YU1idUEtZC04bEFqSHQ1LWlSeGk1WmlvRzlCYnZ4T19ZU0hsS0VNMTFLcWhycFY4WFhIZmZ2TUpweEZfbUNSVDJUaXc4VW95U0dlNC1pZDBnbVFRVklYWTV5WkhqaGJzSGRwU2dKa1lEVmxtb0w4LUFQOQ?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxOVGMxMWdzSGREUl9GSVRlYzhUd0kxbVphdzdyd1cyckoxMWxZNlAyREdlM2FzMWVheDkzYklVOC0yUmRqVmlCNndhcUpRTG5HMlk3d0VlaHdrM1c1U244SC1rbElBVXVSZDU5V044VjhCWlIyLXdwT3Q0WHJjamVSMlFEZ1Fhdk5Wa1F6aUFFS1hHemhReHlRWHNWTQ?oc=5
- https://news.google.com/rss/articles/CBMi4gFBVV95cUxPeHNUd3QtM0V5TFcwQ01jby1uSTRDSjdIa2tMWndZVEFOa2dkUkhpckc4aW1MVGtFSGVTTDFfNTU3Tm9seWJxbE1CWGRaYlBOUEFEYmxBQ2tIbG1ZWmprcjk2VmdpTmdqd21LU3NlT1B5TkNJSkJOOWp6WTRPaVlrX3NYYzI4OTMweHNZNW1jRnJ4eUNvd2tKWWlYandzRm9GVnc3b3hvQ2hSaDhXZ1FUX0p2bDVCX1B5ek9lam5iSkRKT1FnSFlEQnV4cmdOLWZqY3ZIQkNEUWJJN2RwTHJzcWZR?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxPOGRBcmNBS0FxMkxoV3g1dE9sd3Q3bVI1dGN1bFpPT2tFVkxLNWxqd1l3LVN0eUNfZEVtSzA1VlRZN1N2MFJNdlBtYnBiOTZ5bGtwZFB1WmV2YlVVM0JWN3NmRlhPNFUxYXkxa2p4UnlNYmNHREJpTjdHVjFKLVVJV3ZkZzRfalYwS2JZbVRUVGVKVVFRYTdvTk5PVXQwelcxZkNTU016QzVKVWZFRXpaOUMxM3hOZUpuY09uZ2dmUS0ydw?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxNMUcySXV6cmhUVzl1X0tzWTNKbFNfaERVQzMxQ2JTbWxXX0ZrQW5rTHlBWGNMWTFCLXBKQzhWSWtBTnZFOHd6TzJqcmpBZDFWb3dtb0pZT2RuSDNKY2hhb0NSYnBYTUZZblBULXpEMm1Rd3dOMGVpN1BKUWs3S296YmZEX0pBRnVwVEE4UDZFWDJCdnAySzZyX20zZE15ZGhkYjhscjZYN3FVQQ?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxPeWFMdHNCUHVYcW13dkRPZjFvdVpMV19kRlpZb3JHWU5mcndEc1hsMV81YzZYZnhHbWQ2bEV6T3dYUkdONy1uRDJfTXR5WEpCbGhWN1lKZThoazV4VmNSSk4zYXU0LVB3WjhaYTVqTnNiTmhkdHU4aXlWZDRIdE92WlhBbDdOUkNnWjlrWlBYQy1ubVFrVFQwTkJldzBuYUN4Mk5KSA?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxQdXJROFhGNXJCQTZoUDlrdDJoU2FieHZidWZmNTY0X2I3WVRoVDYtaEY4ZnhUdTc4VEpmekVJTlh1V3ZFeVd4VjcwdVdhZkpiaDlXdXlxc2ZfQ1NsUm43cl9oRTlONXVyYkp3Z0hXbE9zOG5EdThfM3F4amhWM0RyUHFwN3M5bGVxcUR3R3R4NUxKVG5KSDZVMmhn?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxNZFFGaEtfQ3Utb2xmbldPOGJ0SVlPNW1PcGtNQjFxUXFVN3ljdV9ZVXMxb216OFBVSnR3ZjY5enRwMWo5dzBycWpCeFNrYmJCd2NfYjMtbWJJX0RfVm9wQXZlM2Y0OGJSQmxJUl85Tjc0UklxX2lXRWlkZkZRYXE4OC05bWM0b3VEV2E4N1RFLTB0MTZnTWFGSnpkQV9uTG9pRHlxNFZTRzBRYWJJRHk2NldiczFvQVFVUWo1R1hNc0tTNlVz?oc=5
- https://news.google.com/rss/articles/CBMi3AFBVV95cUxOR3NWVFd3OHc3R05XTFh1dWdFSDRkREVLQ2E2eVBVVGhrT0FYMTNWTUd6elJua1BYZXZfbGczWHhGd3lnY2x6dDZrZ21MSHl2SEtjcW96d002ZTg5REp5enZwV1VhT1FfUlN2M2phVzBIZkx6ZDZRaXNvemRhR09ERXpWR3ViSVk5LW5tSGtZSENUV0QtVmk1cDRxUW40M3NCbFI3SkQ0SERxbkgyeVNYWFZhX0ZIeHowYTBzVUwxNXN0MUxhVXl5VFp3cnRRLVNqSmw1SnBfclM2bFNk?oc=5
- https://news.google.com/rss/articles/CBMi0AFBVV95cUxOYktrRnhKM1NTMmJLOGE5VW1jYU5QX3N4VmZWanhjMklxX0d1X3NzN0tmb21LNVJlOTFWZzVlamhPYWo0SDM5aUwtZkFkOURGRDNfWm9BQkh3NjYxTkhPVll0UFA0S1ZEYm5Ock9iMURqa1llQjBlSUdlaFlsbXdVWktodllGcVZoQUN2aWg5QzJmMVdLdnVTUWd2U1Y5MWJHSkJ3UTNCTFRKSFB1NFY1Sy1hVkNWbFVsVFJQOTVLQTg2VGkzWG91ekF1MkFkMVRf?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxPdW9vS2VHbzl6VVBsTzVyNWdRMHNEenlLazIxdWRRM25jS1JBQ3JsVnR5UGtNM3N6bnMyV29xV0lpRW1JMnBGdjBqZHhCWXJxQjNlMk1NZmo4Tk1GUXJyZGRHZC1RRlJvRnh4cWQ0MWt2V0ZzMTV0djd6TjhLTVpYNTBZWlBBbkYzbnRfUkFOdE9TTFNIbzZpQ01LV2ZmbklpWkNyT1l6SmxLbzFWTU9mTXUzaGZ3cDUwUlNoVEVYeG04amc?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxPemxMYk1Cc3YxMm42Wm1HOWxKYlJNVjcxblFNZXZXZjBaTmxBeS1Icl9JcGd4dTN3OGRUcTllMXJWZUdvWmpiYTNiSjBTeVdXd1owdjYzZlM3Unlsa05acWszZ2VxdG56aVdXV2ZpOVY4V1oxb1J3M1pqMnh6VnJCODZDTFdfdWprVTJERlcyajByNWpTRGNFUw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
