# TSM Intelligence Report

- ticker: **TSM**
- Report as_of: **2026-10-29**
- Market data as_of: **2026-10-29**
- Quant sources: https://finance.yahoo.com/quote/TSM/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/TSM/key-statistics/
- AI analysis snapshot as_of: **2026-10-29**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-30T02:36:14.499342+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 22, 'rule': 3, 'ai': 9, 'unknown': 0, 'irrelevant': 10})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **7** exact headline/source/date matches; prior report **20261029T020157Z-688a53f0/TSM** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'low_uncalibrated_model_confidence': 1, 'short_term_price_move_in_structural_risks': 1}
- RSS source audit (metadata only, not article fact-checking): 22 unique headlines; 14 named publishers; 3 exact duplicates; 22 HTTPS source links; largest publisher share 27.27%; oldest publication 2026-10-26

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 431.8100 |
| Return 1D (%) | -1.7520 |
| Return 1W (%) | 4.7193 |
| Return 1M (%) | -5.4996 |
| Return YTD (%) | 43.2114 |
| Return 1Y (%) | 43.0333 |
| Annualized volatility (%) | 39.2501 |
| Beta vs SPY | 2.1459 |
| Max drawdown (%) | -21.5466 |
| Sharpe (rf=0) | 1.1113 |
| Downside deviation (rf=0, %) | 26.0957 |
| Sortino (rf=0) | 1.6715 |
| Historical VaR 95% (1D, %) | 4.1383 |
| Historical ES 95% (1D, %) | 5.1216 |
| Correlation vs SPY | 0.6949 |
| Tracking error vs SPY (%) | 31.7616 |
| P/E (trailing) | 27.99 |
| P/B | 82.41 |
| EV/EBITDA | 4.08 |
| Revenue growth (%) | 50.90 |
| Forward P/E (estimate) | 18.47 |
| Gross margin (%) | 65.85 |
| Operating margin (%) | 58.66 |
| Return on equity (%) | 41.85 |
| Free cash flow yield (%) | N/A |
| MA50 | 434.7096 |
| Close vs MA50 (%) | -0.6670 |
| MA200 | 398.2412 |
| Close vs MA200 (%) | 8.4293 |
| RSI (14, Wilder) | 48.2022 |
| MACD (12,26) | -3.5438 |
| MACD signal (9) | -3.0228 |
| MACD histogram | -0.5210 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'TSM': 271, 'SPY': 271}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 431.8100 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.7520 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 4.7193 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -5.4996 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 43.2114 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 43.0333 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 39.2501 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 26.0957 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.6715 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.1383 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.1216 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6949 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 31.7616 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 2.1459 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -21.5466 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.1113 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 18.4650 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 65.8460 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 58.6550 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 41.8550 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 27.9851 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 48.2022 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.5210 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -0.6670 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 8.4293 -> Clearly above the moving-average trend level.

## TAILWINDS

### TSMC Gains 3% on Reported 20% Price Hike for AI Chip Packaging
- Summary: TSMC Gains 3% on Reported 20% Price Hike for AI Chip Packaging
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxPT3luSFdYRzlnYVJkdTJTVWJ2VHhkMVlscnhKZ3N1RUxJQnRCOEdlVmpCTXlBMjB3UC1DVHpqZVdmQWd0WlNUMTRHVC1WamVvbG9OYVJQT05FTHhLSzdWOEJncWZCSFJTYk1FVmc3UWRtNldBWndqY2hFT0lLQmdfRFZ0Rjk0dTBLbVRzWGdDRQ?oc=5>

### Bull of the Day: Taiwan Semiconductor Manufacturing Company (TSM)
- Summary: Positive analyst sentiment highlights TSM as a strong buy for the day.
- Date: 2026-10-27 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi4AFBVV95cUxPallzbHE0bXVGSS14X2RCVFU4TENQOHVHSF9ORjByQkJEQjRuZDM3czV5U1hyUzVfWk96T2tYbWF4M0VPLXhDY1U0S2xxTEF3TURvMGZZWXVLQTJNbGtvajdINU52SVA5RjJMc2I3aTZVUHFfV1d1ME9ZTjVlOXE4bk1hRDNVUUZlc1kxVWpnS29qR3lWdlNNVGpEUVdxc2pWSTMwdHlEeWJ6UV9XWFl5UDBzbWVDZV9ad2VRSWQyT1BRWU5vZjFseEJ1SDRHWFdoNjRjbjUxcVVHNDRaTjJuZg?oc=5>

### Taiwan Semiconductor Manufacturing and Sonoco have been highlighted as Zacks Bull and Bear of the Day
- Summary: Zacks identifies TSM as a bullish pick, boosting investor confidence.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxONE5QVFhJN2VhMTlERWt6d2V3TTBEb1NkUDNWQ3FxMHlPQ2VrMEVuVzRLWnV0VmVtZ3FpZ1dMZnAwTzM3ajJtbnJPUFV0RGhxYWpvZXZfMXpFT1ZpMGVOOVo5ek45b0JtVzFjRlZVSjlLYzYyckRrZDFqSi1zOV80cmFmZGdyRkZMMWNTa0lGWTd0M1QtV24yREtkTEFveEFaUjRRdg?oc=5>

## HEADWINDS

### Taiwan Semiconductor Manufacturing (NYSE:TSM) Stock Falls 1.9% - Here's What Happened
- Summary: Taiwan Semiconductor Manufacturing (NYSE:TSM) Stock Falls 1.9% - Here's What Happened
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1AFBVV95cUxNSktMSTFRZmxtRjE3V2RHT3VyckktcUxXX0VsX2FweU45d3dCVE1Dd2IwRFh1Qml3d3lFV1VPZkNkRGU4SDB0anpxX3dHZkF6a0kxNkVHNjdGb21DQkd6bUlEemhMWVV4TlRFYzRhXzZLeGFIbl9aUjA3Z2NyRGtPUFNMd1VGOVFNcFIyN2xIMlREU3NoZGlTNzc1RjZRRy1nTldnMlJjSkFFSEM4TE5Wd2NEV2xIR2VWZW5LVmxPMDByVDVHeF8yREkwaEJYa1VMX0RqTA?oc=5>

### Taiwan Semiconductor Manufacturing (TSM) Stock Looks Pricey Against Cash Flow
- Summary: Valuation concerns relative to cash flow.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxORldEaFpNSnljQTZVWGtRUmV3X0R2QTZQTE9pNm0yWDlremFDNV85cHVhRnlZTy02c2Zkd0dsTTE0Zkx4LWJibjZVR0RHWlhZdy1WcHRVZ2dHQlpHOWxGWEVHUnlJRU5mcFVhU1FnWXk5TzB4ZFdMYjkzRDctYjJ0d0tYeGxfbHlBU1ducHNRZEFOYkwzZy1TTXRGNjRkcDlZZTUwcDNLdlZXSGFsb3c?oc=5>

### TSMC: The Cracks Are Showing (NYSE:TSM)
- Summary: Report indicates operational or financial challenges for TSM, raising concerns.
- Date: 2026-10-29 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMid0FVX3lxTE5NM2ZPNW5mb2NfMHdER3RRX2QyeVkwSDl3anVfdVdWUTQ4UkxyRHBxeGJ0QkFRb0tybEpVNWNXRXZwR0gyWm5UNV9PQUIwOWV5M0xVc1lxZXdKeTV2eFVzTWc1MUF0cEdtYW1NRTMyamVWX0t6V0Y0?oc=5>

## CATALYSTS

### Taiwan Semiconductor Manufacturing Company Limited 2026 Q3 - Results - Earnings Call Presentation
- Summary: Taiwan Semiconductor Manufacturing Company Limited 2026 Q3 - Results - Earnings Call Presentation
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizwFBVV95cUxQcUd6a0dTbklKcC1hSlZQQXp5VnRWZUszUE9iaEhtcWJ4eFN0SHItNG0tV2tKVnZqSjZCM2N2c0dLMVQyQURGR05QV0dBdkpGWm9DcUNVRENHZWEzUkg4UVZfckpoTGZxLUVYYk1CTnUzWXhTcTc1YllhbFhaeW1FT2VLdE43cTBwLTFOcEl4Y1d0NmFwY0NEZEd3bFh1cktLTkJXd0VoTV9PSmVZbU1aM3M2RkNfVkMtbzJDWTFnUUF6SXJ6TjlNSjJRUE95YTQ?oc=5>

### TSMC: The Toll Road Of The AI Economy Is On Sale (NYSE:TSM)
- Summary: TSMC highlights its role in AI economy, suggesting growth potential.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxNMXNDRzVKSl9XSDFyUlRwRWctZzJFQVExcGZsZmhKZzVfUnRTYUtlUm5TTHZPR1dZakx3c2VEUjBtTWxGdjFoODB3RFFOVDE0Q1BKVGRpRW1hTzdxcHUxbjVkcUdLWGVfVWx1RVNCN3lWbjZOcGI2cUVlNHVwTWUwUVJ6OGlLcnp6RmV5WjBaRFhfUQ?oc=5>

### Why TSMC's Q3 2026 Results Highlight Pitfalls In The AI Hype (NYSE:TSM)
- Summary: TSMC’s upcoming Q3 2026 earnings may reveal challenges in AI demand, potentially affecting future revenue growth.
- Date: 2026-10-27 | Impact: medium | Horizon: long | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxQZEN1M1JmbHlBV3NidEFjN2xfTF9CazJKaTRUT0JJblVyZ3ZVcjNCNC1pdDFrSFFQcEFUOF9Lb1RtU0hnYUxwblQ5Y0tjSXlvZHlnVlZqaHdUZ1JCblZGRHZLT2xucHVVSElKOEtnSlVZaWpwZjRlTUw1Q2J3VUtfWFU1RWl5Y3ZSOUw5bmRJSndxcFVzMGZxQXpiZTJJdzlsNEE?oc=5>

### Beyond NVIDIA: Why TSMC Stock Looks Attractive After Q3 Earnings
- Summary: TSMC’s Q3 earnings boost stock appeal, highlighting strong performance and future prospects.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxOb3d0dU5xTXJwMzUwMnZYdDFwTE5CLVpqVnliWm9RczlQZ0NQQnl3QmQtbkpSVzU0S0xhS2lKS1lCYk1YcFp5VlBScEMwT1JSTGZMSmRrbWhNSFZVQ3lKeXhpUzdsa2d5UTctdnRuVUp6LVcxTXJMa3Vxc2FoMzJzeXpsLUs4Sjl5Ujc0UEVMbzJhTXEyTG5RTTBkdlFtcm12THJ6b3kzQQ?oc=5>

### Cathie Wood Extends Archer, Joby Buying Spree; Ark Sells More AMD, Taiwan Semiconductor Shares
- Summary: Ark sells additional TSM shares, indicating a shift in investor holdings.
- Date: 2026-10-28 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMi7wFBVV95cUxQNlI2alFjamgtbVhhUERmYUx1SmIwdWRsbTV5UUtKWVo4TXNiUzZHd3o5MGZ5bXZTM3RUd3ZDNEZwSmtQWVVRbDk0bVR4UVFEUmY0UjdJM0pYVDJaTDNmRC1xbHNKRVRRSGpiZWljYTR4RVZzZHFWUXRORnpsa05zSDJod08tVWVBVVphRkllalhjdUFtSUdRbFlCdlIyWmRqUUQzQlVnZl8wb25hMTdGUVVLZzg0RlMxYl9oR1NWNTlrWTg3Mk9ITnU3OUpNZUc0VFFCSVNyY0V5WjM2TVN4VDdtUTJNXzZ4WDZZYjJRdw?oc=5>

## RISKS

### Taiwan Semiconductor raising prices could mean less competition from Intel: Wedbush (TSM:NYSE)
- Summary: TSMC’s price hike may reduce Intel competition but could affect margins.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxPeXJ1SWxyZ3Q0aUtiYVAwZHd5N1pKTVN5YjkweEhCMGNMbmNPNEhmRUJrQkNIb2Q2a3dXbUdVdUs2aGNBbEx5UVY0bEsyRzJiV3p1UTVqcjBzZ1pKZjRFVlVibzhnMGZPQzg5WXhmWk9HOXhkeGJhN2ZGVk05eklQdlJueTZBUEthRkcwdlNoYVFSX01NbWkyT0FnX0pRX05SU21scVh2eDRwSG8yR3RFWTBXSmxhSnRzRFpGTg?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **TSM** | **27.99** | **82.41** | **4.08** | **50.90** | **2,239,571,427,328.00 USD** | **43.03** |
| UMC | 17.02 | 3.09 | -0.23 | 25.60 | 45,240,602,624.00 USD | 148.41 |
| GFS | 35.82 | 2.13 | 12.39 | 5.80 | 25,557,643,264.00 USD | 34.01 |
| INTC | N/A | 5.30 | 29.74 | 25.40 | 486,691,700,736.00 USD | 122.71 |

Peers fetched as_of: 2026-10-29; TSM reuses existing data (market data as_of: 2026-10-29); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-15
- Next expected earnings: 2027-01-14 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-29

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
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

- https://news.google.com/rss/articles/CBMijwFBVV95cUxPT3luSFdYRzlnYVJkdTJTVWJ2VHhkMVlscnhKZ3N1RUxJQnRCOEdlVmpCTXlBMjB3UC1DVHpqZVdmQWd0WlNUMTRHVC1WamVvbG9OYVJQT05FTHhLSzdWOEJncWZCSFJTYk1FVmc3UWRtNldBWndqY2hFT0lLQmdfRFZ0Rjk0dTBLbVRzWGdDRQ?oc=5
- https://news.google.com/rss/articles/CBMi4AFBVV95cUxPallzbHE0bXVGSS14X2RCVFU4TENQOHVHSF9ORjByQkJEQjRuZDM3czV5U1hyUzVfWk96T2tYbWF4M0VPLXhDY1U0S2xxTEF3TURvMGZZWXVLQTJNbGtvajdINU52SVA5RjJMc2I3aTZVUHFfV1d1ME9ZTjVlOXE4bk1hRDNVUUZlc1kxVWpnS29qR3lWdlNNVGpEUVdxc2pWSTMwdHlEeWJ6UV9XWFl5UDBzbWVDZV9ad2VRSWQyT1BRWU5vZjFseEJ1SDRHWFdoNjRjbjUxcVVHNDRaTjJuZg?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxQM2NXeFZEN1AwYlZkSmdSTEdHelNieFFYSkZQaWR5RHJRVnAyRHIweXZ4Ny04TkdhNkpxa3ZiZXF2XzVwUVFnMEppRG00YnJ5TTFFa2xSVXU1a25mcERMLU9FY2d1clFld2pXU2QwTzdYZ2tnWVVMYU01MkhDbUlWeUF1UVdNU1I1bWtoZFRfZ2lmX09fcHY4d21XWXBadE43S1BrVC1n?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxONE5QVFhJN2VhMTlERWt6d2V3TTBEb1NkUDNWQ3FxMHlPQ2VrMEVuVzRLWnV0VmVtZ3FpZ1dMZnAwTzM3ajJtbnJPUFV0RGhxYWpvZXZfMXpFT1ZpMGVOOVo5ek45b0JtVzFjRlZVSjlLYzYyckRrZDFqSi1zOV80cmFmZGdyRkZMMWNTa0lGWTd0M1QtV24yREtkTEFveEFaUjRRdg?oc=5
- https://news.google.com/rss/articles/CBMi1AFBVV95cUxNSktMSTFRZmxtRjE3V2RHT3VyckktcUxXX0VsX2FweU45d3dCVE1Dd2IwRFh1Qml3d3lFV1VPZkNkRGU4SDB0anpxX3dHZkF6a0kxNkVHNjdGb21DQkd6bUlEemhMWVV4TlRFYzRhXzZLeGFIbl9aUjA3Z2NyRGtPUFNMd1VGOVFNcFIyN2xIMlREU3NoZGlTNzc1RjZRRy1nTldnMlJjSkFFSEM4TE5Wd2NEV2xIR2VWZW5LVmxPMDByVDVHeF8yREkwaEJYa1VMX0RqTA?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxORldEaFpNSnljQTZVWGtRUmV3X0R2QTZQTE9pNm0yWDlremFDNV85cHVhRnlZTy02c2Zkd0dsTTE0Zkx4LWJibjZVR0RHWlhZdy1WcHRVZ2dHQlpHOWxGWEVHUnlJRU5mcFVhU1FnWXk5TzB4ZFdMYjkzRDctYjJ0d0tYeGxfbHlBU1ducHNRZEFOYkwzZy1TTXRGNjRkcDlZZTUwcDNLdlZXSGFsb3c?oc=5
- https://news.google.com/rss/articles/CBMid0FVX3lxTE5NM2ZPNW5mb2NfMHdER3RRX2QyeVkwSDl3anVfdVdWUTQ4UkxyRHBxeGJ0QkFRb0tybEpVNWNXRXZwR0gyWm5UNV9PQUIwOWV5M0xVc1lxZXdKeTV2eFVzTWc1MUF0cEdtYW1NRTMyamVWX0t6V0Y0?oc=5
- https://news.google.com/rss/articles/CBMizwFBVV95cUxQcUd6a0dTbklKcC1hSlZQQXp5VnRWZUszUE9iaEhtcWJ4eFN0SHItNG0tV2tKVnZqSjZCM2N2c0dLMVQyQURGR05QV0dBdkpGWm9DcUNVRENHZWEzUkg4UVZfckpoTGZxLUVYYk1CTnUzWXhTcTc1YllhbFhaeW1FT2VLdE43cTBwLTFOcEl4Y1d0NmFwY0NEZEd3bFh1cktLTkJXd0VoTV9PSmVZbU1aM3M2RkNfVkMtbzJDWTFnUUF6SXJ6TjlNSjJRUE95YTQ?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxNMXNDRzVKSl9XSDFyUlRwRWctZzJFQVExcGZsZmhKZzVfUnRTYUtlUm5TTHZPR1dZakx3c2VEUjBtTWxGdjFoODB3RFFOVDE0Q1BKVGRpRW1hTzdxcHUxbjVkcUdLWGVfVWx1RVNCN3lWbjZOcGI2cUVlNHVwTWUwUVJ6OGlLcnp6RmV5WjBaRFhfUQ?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxQZEN1M1JmbHlBV3NidEFjN2xfTF9CazJKaTRUT0JJblVyZ3ZVcjNCNC1pdDFrSFFQcEFUOF9Lb1RtU0hnYUxwblQ5Y0tjSXlvZHlnVlZqaHdUZ1JCblZGRHZLT2xucHVVSElKOEtnSlVZaWpwZjRlTUw1Q2J3VUtfWFU1RWl5Y3ZSOUw5bmRJSndxcFVzMGZxQXpiZTJJdzlsNEE?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxOb3d0dU5xTXJwMzUwMnZYdDFwTE5CLVpqVnliWm9RczlQZ0NQQnl3QmQtbkpSVzU0S0xhS2lKS1lCYk1YcFp5VlBScEMwT1JSTGZMSmRrbWhNSFZVQ3lKeXhpUzdsa2d5UTctdnRuVUp6LVcxTXJMa3Vxc2FoMzJzeXpsLUs4Sjl5Ujc0UEVMbzJhTXEyTG5RTTBkdlFtcm12THJ6b3kzQQ?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxOTl9Qckw0VV9Ud2FBeDJiSnRJXzdhX2c0VGtNVklNTVZUNlZXaG14Q3VicGQ5SHhnUF9kYWRfZmNXNjJLUW9RMTdBb0d3VXlTejhyQVJsb3JLX3JjTTV0bkJlTnZ0bFEtSlZ6MkNoNDZVSHNwYktuWDF4YlBnNGlObk10WFY2enpwS0RRMk14aGFsTWVGZFdV?oc=5
- https://news.google.com/rss/articles/CBMi7wFBVV95cUxQNlI2alFjamgtbVhhUERmYUx1SmIwdWRsbTV5UUtKWVo4TXNiUzZHd3o5MGZ5bXZTM3RUd3ZDNEZwSmtQWVVRbDk0bVR4UVFEUmY0UjdJM0pYVDJaTDNmRC1xbHNKRVRRSGpiZWljYTR4RVZzZHFWUXRORnpsa05zSDJod08tVWVBVVphRkllalhjdUFtSUdRbFlCdlIyWmRqUUQzQlVnZl8wb25hMTdGUVVLZzg0RlMxYl9oR1NWNTlrWTg3Mk9ITnU3OUpNZUc0VFFCSVNyY0V5WjM2TVN4VDdtUTJNXzZ4WDZZYjJRdw?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxPeXJ1SWxyZ3Q0aUtiYVAwZHd5N1pKTVN5YjkweEhCMGNMbmNPNEhmRUJrQkNIb2Q2a3dXbUdVdUs2aGNBbEx5UVY0bEsyRzJiV3p1UTVqcjBzZ1pKZjRFVlVibzhnMGZPQzg5WXhmWk9HOXhkeGJhN2ZGVk05eklQdlJueTZBUEthRkcwdlNoYVFSX01NbWkyT0FnX0pRX05SU21scVh2eDRwSG8yR3RFWTBXSmxhSnRzRFpGTg?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
