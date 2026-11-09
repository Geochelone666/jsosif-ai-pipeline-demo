# NVDA Intelligence Report

- ticker: **NVDA**
- Report as_of: **2026-11-08**
- Market data as_of: **2026-11-06**
- Quant sources: https://finance.yahoo.com/quote/NVDA/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NVDA/key-statistics/
- AI analysis snapshot as_of: **2026-11-08**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-09T04:36:16.637555+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 23, 'rule': 3, 'ai': 15, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **5** exact headline/source/date matches; prior report **20261108T041758Z-43fb2458/NVDA** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 23 unique headlines; 14 named publishers; 2 exact duplicates; 23 HTTPS source links; largest publisher share 34.78%; oldest publication 2026-11-05

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 186.6400 |
| Return 1D (%) | 2.7753 |
| Return 1W (%) | -8.7959 |
| Return 1M (%) | -21.9863 |
| Return YTD (%) | 0.3092 |
| Return 1Y (%) | -0.5279 |
| Annualized volatility (%) | 38.3481 |
| Beta vs SPY | 1.8850 |
| Max drawdown (%) | -24.0930 |
| Sharpe (rf=0) | 0.1772 |
| Downside deviation (rf=0, %) | 26.8287 |
| Sortino (rf=0) | 0.2532 |
| Historical VaR 95% (1D, %) | 3.9708 |
| Historical ES 95% (1D, %) | 4.9990 |
| Correlation vs SPY | 0.6660 |
| Tracking error vs SPY (%) | 31.0163 |
| P/E (trailing) | 23.60 |
| P/B | 19.68 |
| EV/EBITDA | 22.23 |
| Revenue growth (%) | 105.90 |
| Forward P/E (estimate) | 11.73 |
| Gross margin (%) | 74.67 |
| Operating margin (%) | 66.24 |
| Return on equity (%) | 117.21 |
| Free cash flow yield (%) | 0.93 |
| MA50 | 219.7732 |
| Close vs MA50 (%) | -15.0761 |
| MA200 | 204.3910 |
| Close vs MA200 (%) | -8.6848 |
| RSI (14, Wilder) | 30.7664 |
| MACD (12,26) | -8.2280 |
| MACD signal (9) | -5.0272 |
| MACD histogram | -3.2008 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NVDA': 277, 'SPY': 277}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 186.6400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 2.7753 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -8.7959 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -21.9863 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 0.3092 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -0.5279 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 38.3481 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 26.8287 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.2532 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.9708 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.9990 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6660 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 31.0163 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.8850 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -24.0930 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.1772 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 11.7276 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 74.6740 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 66.2370 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 117.2110 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 0.9277 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 23.5954 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 30.7664 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -3.2008 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -15.0761 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -8.6848 -> Clearly below the moving-average trend level.

## TAILWINDS

### Why Nvidia Stock Looks Like a Bargain Right Now
- Summary: Analysts view NVDA as undervalued, suggesting buying opportunity.
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNZ0NBcUNnaGtIbGthQ2hxZnpYaFFYdElrV3BrLUNHTkp0N0UteEE5bTFsZFNUVmhfMHVCMDFEUEVNSDhfRFpBUEdCZml0VHIwZ3FDSy1aa3NGYUJPblplN2hicUU2S01fZUtLdjgySEhJZlBvb3dBV3BVRHk5R18zanFobWY2Z25rVXVnZDh0YTlpM2JyM2o2RGQybw?oc=5>

### Nvidia: Competitive Moat Widening; Buy (NASDAQ:NVDA)
- Summary: Company’s competitive advantage expanding, encouraging purchase.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMigwFBVV95cUxPZ3JjdG55eXd4UHpTU0FsNkw5Szl3MVgzckZGM2dUN1l3bmxiVENVdGhaV2hfcmRIbW9zWUVLTEZZX3FlS0U0WmprUW5lRHZ6a09GM3E1WXRuWUphVVJMT3ludVFnblZoN2ZENVRmS0MxSnpuYnc2N3hnQ1p0dU1nZW5vTQ?oc=5>

## HEADWINDS

### Nvidia Is Now Down for the Year After a Sharp Selloff. You Can Buy NVDA Stock Gradually, but Don’t Rush In.
- Summary: Nvidia Is Now Down for the Year After a Sharp Selloff. You Can Buy NVDA Stock Gradually, but Don’t Rush In.
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi4AFBVV95cUxOdEUzQWhaem5BMHNyZnZoVHNDZV9fdXRBNVQ4T210dV9kUHlBVGlGdklmY08xQVlMcjNGblJ0ZDhSM3FDUmpRQm8tcFhVNXR3OUJWWlNjdEhPNW8zd1I5QjZOdHJqSlFHaDJ4LWd6TXR2c0YtSFFMSWZSMGsxbHNIbU9DUGxvTnVaZXEtdm5ZaDFvNlgwQ0gxZnRhaUtwTTM4MmVoZUNqUWxSVzZ0UDNxaWNkMGEtdzl1a3RRcFZSRzk4OHRCR0dRQVBDTnA1UEc0R2ptOHRMZWJIaUMwSUVFeQ?oc=5>

### Nvidia stock oversold setup: Key levels after a 9% drop
- Summary: Nvidia stock oversold setup: Key levels after a 9% drop
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNNjhTc0JFcEFDRDdXX3N3VDROUHZWS25HV0loYWVGV2tYaC05U3Vvc3hxdW91UERlREdKQVIxS2Y0c1M1UmE5LXUtdU9WT0pqVFJBRWZzRU0zS1hPWTByX2QtRUp3SFN2dGRyekZPSV9VdVY2NHBkSEJjdnc4T2JaRU9RdVhiaDdRY1VUR2NYWUI5cnVVMHJVaE1faGE?oc=5>

### NVIDIA Stocks Rebound 6.78% as Lawmakers Call Jensen Huang to Closed-Door Briefing
- Summary: Lawmakers summoned CEO Jensen Huang for a closed-door briefing, potentially raising regulatory scrutiny and affecting investor sentiment.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxQRnZ2Y1c3VTFIcmJCY2kwcjBRdFBzcWMzV1UyaXJzWDN5YkhRWXJweVdpQlF4dXRpRmRaSTZDbk9PeUtUR2tjbjFMYTBVMG9hM1E4ZEgxZVM2TVBYSlMxcEVoaDlxMWFpQkJfS0RKbDB5YXRRaTVYZWdoSmxNSXlxUjRFbW83ajdhcEhRRXpTUHhIVHhuWlE?oc=5>

### Nvidia Stock Loses $1.39 Trillion Since October Peak — Jim Cramer Says NVDA Can 'Buy and Reload'
- Summary: Stock value dropped significantly, though bullish comment noted.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxPNmJ3NGFObTl6ZGs5MUFnbk04S0hSREVIeWdxT3JVNjlXUGMyT0tvbWExS0lPQjZDUFB4akdvc2FFYVMzYWZyR3BfYjBsS1gxZGtXalV3MEhDMjlYZ2Z3alBSblQzT2dWTkN6UkR6NXl2RWJPVWtRYm8zbVpEVVZQd29xdmEyR1RWVGxfcWNodTUwVzZqV2VJeERvSkU4NlhvVmtTRnZRcERSTUZWQWhPalBn?oc=5>

### Why Nvidia at 13 Times Expected Earnings Still Isn’t Cheap
- Summary: High valuation suggests stock may be overvalued.
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxPSEhJbGo5Z213RFlZOGstMFRLUW52OVk0NmF1NVl6TlJVbHlzay0tZm4zLVIySnNnSjM2SFduV2psMzk2M1YxVEtSWmpyZ3JCcVQ5MXZFX2ZrdlJkM0t0UDc2a1JvMi03R2xpbVJTeU9PcG5jNTlWVUR3Zi1YVlF6dXhDa2wzM0lOazh5anRyRmlJaTBodFcxUA?oc=5>

### NVIDIA sparks valuation debate after selloff (NVDA:NASDAQ)
- Summary: Selloff triggered debate over company’s valuation.
- Date: 2026-11-07 | Impact: medium | Horizon: short | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxOTFVHWjZ5elJ3NU1wVHZGVFpaSnIzcXRZdmt1TktrLXFVXzJyQjdBVTBJa3QxS3lzRWVxT1BhclFYLVU5bnVabnRzdnVZTnNvQTU0c2Q5bHZXQ0dlTWpJVktEcTlvZDd6TmxRMGZoNmUyMzhMS21sNEg5UnRiUEpXTWlUY3BLbWFUUkE?oc=5>

## CATALYSTS

### Nvidia Stock Is Heavily Discounted. Here’s Why Analysts See 80% Upside.
- Summary: Nvidia Stock Is Heavily Discounted. Here’s Why Analysts See 80% Upside.
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxQYWVoQTRyTjV4OE5iZ0gyY2NzM1M3STlkWFdhTUJxRE5fZWh2UENxRThXNVltUWpDUFVRMlBLeWxmZTFIRWh1Q2VtaEdQMVBkWVk0VG9RVENkUXRjZTFwUnlUZTBtdDE0Q3pKNVFUUXg0RWU0NXpObWxQT2wtNkd5Sy13ZVJ0bFd3OWhNM1RyQjRRRlc1cDBPS3JXUW1Fck1Pd1E?oc=5>

### U.S. Stock Market Movements | NVIDIA (NVDA.US) Surges Over 6% as It Plans Data Center Retrofitting Projects with Capacity Reaching 1 Gigawatt
- Summary: NVIDIA plans data center retrofitting projects reaching 1 GW, driving a 6% stock surge.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxNSGs5d3lFcWd5WEVwZlBvelNFUWdkUFpJeEgwNGhxckJ1aVdHTmlEVHpmbnZyUEZFMHJnbnZ3c1JVUE1zZmx6eXFhUG04dnp4RzBrRF9Xa3RjVjA3ektfYmZhb0NEaFR3MVFMOUU2QTJDeGZuR2owUTJoYTVYWWdOTnZJRmkzaHhqYlBJMWlHTlZfWWpXTng2V3BzSWFPa2kzWlE?oc=5>

### Asian stocks face new pressure as Nvidia spy probe rattles tech sector (NVDA:NASDAQ)
- Summary: Reports of a spy probe into Nvidia create market pressure on tech stocks, including NVDA.
- Date: 2026-11-08 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxOcEFxSEFid1djemktcFlja1EyNW5PZkl5cHd1d1VySUdtWEF1bGFXdk5SSzIyd2x3bTEyX1A0REZ3YXNxNldtNjlLN3VwcHBMbVl2bjNIQ3FBd1RkNlF5a3pRaXllSFA5OWRCb2k1MG40VGh5THo0RGp3WVp5Z0tBMzdEaC1jSzZQTUlsblRnVjdmUHNWdmJwd0NJWmNycndNQjdkNUp3SnItcUV1?oc=5>

### Is NVDA stock a buy or sell? Spy alert?
- Summary: Analyst debate on whether to buy or sell NVDA amid spy alert concerns.
- Date: 2026-11-08 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMie0FVX3lxTE9idXM2c01NckxhaUZZUDkzTVg1UTM3VmF1UTQ5anlKblBtVUZienBwR2xicC1EZ2ROaVhVV2k5bkdSR01SZUM4cUU4dEFPbTFwWDRrSTlESXFDR2Q4dG5VeDhKb2Y1TFh0M3k1WkRadXlCYjFiV2hpTFphQQ?oc=5>

### Nvidia Stock in Focus After Explosive Jensen Huang Report — What Investors Should Know
- Summary: Investors review Jensen Huang's report to assess NVDA's future prospects.
- Date: 2026-11-08 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxQa191TC1XUmx2MGhqSkttRXozSF9TV2VUaG1JN0hxV0xXTUtmeFU3V2N0SUxNSlRwTlltZnZZcFNkYl8yLVlKZ0NtWVlGRjdUampudXdzMzFrMElzTzlBenFENnpBOGhhQUZRTmhvVVNYWkZZMUFDc21BcHBfa1RhdWJHV3V0WHEzYTVNSmU4WjMzQ2htWUQ4X0VrRnMwWEctYnpWdENHWGJSckZDQ2NLMlVQVnU?oc=5>

### Nvidia Stock $186.64: Results 17 Nov, $200 or $172 Next
- Summary: Analysis of NVDA's upcoming earnings and potential price targets.
- Date: 2026-11-06 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizAFBVV95cUxOcUZESk9EalEta2UtTFc1X2FYc2ZOZWhvVUdfOEdNU0NFZGFyNkV3aFR1YklNYWxpN0pSWXZBTGhXZE0tN0sybnIySXdtbTZSOXpEM3lnV2VQSUdjenA0MnM3ZmRIV3ZQNTdYSXFhcFVQLVJ3Nk1ZdjNOZGV0S2xneGQ3T1U4NE04aHpLbGpVODRFNEN0UkN3emtKTEJiYkpuZXhONjV4LU13REhyYVZkVy1tTWZPdFowOE5hVTk4cWc4bUVwQ1Y3b2FKRDU?oc=5>

### Should You Buy Nvidia Stock Before Nov. 17?
- Summary: Guidance on buying NVDA before its earnings release on Nov 17.
- Date: 2026-11-06 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxPUDNJdk9KUDJGQXU1cHkzVUdNdWUwc2Eyb3c3dFFOVkJHeDNhX3AtbEhIWlZMMWpjUmYwd05RMzhsSjFMUTR5UzBzNWw5NHprVW54OEIxbWEwYl9Ga3BiNzZmb3o1Qjl5aW1NVWxBTG9GOFM5UGRKU3MxOWpGOWhob29lU2ctTm9MdUpiag?oc=5>

## RISKS

### US Stock Futures Volatile Amid Concerns Over Nvidia CEO Investigation (NVDA)
- Summary: Nvidia CEO investigation causes market volatility, raising concerns about company stability.
- Date: 2026-11-08 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxPVFR1QjA3ODFRRlZTSXpGbG9fc1J0X2pzdjJZOHNGbEJGSnYyNTBlMEVOeHczRE5sbWdXeGhVa3Bub29EdjQtTWpqcXByR3RJQTh6emtqdU9wYzB4UkhQMzE2bUdXbW9OYm1vUTB3RjgxZVAxZks3NV95NmNBeUx2bndRUl9WUXotZTNTOUd4ZndxemVuelh0bnE5RDZhWkZCZGZTRlotMno1NnZlaWJublFqRQ?oc=5>

### Nvidia investigates CEO Jensen Huang's relationship with alleged Chinese spy
- Summary: Nvidia probes CEO's alleged ties to a suspected Chinese spy, potentially impacting reputation.
- Date: 2026-11-08 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMihwFBVV95cUxPd1BJNjAwTmc1dWhNWkFEblREai1hbkhYZFBjT2MxaWV1b283RXNKTnk1emdfY2p5LWlXOEo5M0hLWWhjTG1UVmdVV2xvS09sb0tlelBpalV1Z1lTdUZ1VWJ5Uzl4cFJqeXV2ZUF5WVpTSWFGeGU4eldfdHpScTMySHpZQk9fWGc?oc=5>

### Nvidia's Jensen Huang admits to affair after allegations of romance with Chinese spy: Report
- Summary: CEO admits affair amid spy romance allegations, heightening scrutiny and risk.
- Date: 2026-11-08 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi4AFBVV95cUxNYU5fTUZfS2drVGlTTk43X0NHYU9EMWZJQ0pmN1IyMDlWRFJLUjdpamR6QmlYN2pLR2FYaGw2RHJPbHl6VTdXOTRDaTlMSEJEWUZLYXlSNkw0VWlRSmlTNGl6WjFmVU5rRkRVeng2alFRSjdRR2lVTEpvSWM3THFmc1dQNk5SVG9pcm93WW1IQjFLV0xSOTBZd0RoQnU4SWJJRWhMcHZWMFpWcHRvSU1TQWVsTXR6NzdBcFFRRURMdUlCZ0hnSnNzZkV6eGZ6clp6dGVhcEZUMTkwRHpwSGhibg?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NVDA** | **23.60** | **19.68** | **22.23** | **105.90** | **4,506,795,900,928.00 USD** | **-0.53** |
| AMD | 95.95 | 10.77 | N/A | 44.70 | 736,464,797,696.00 USD | 88.91 |
| AVGO | 37.51 | 14.06 | 27.50 | 85.50 | 1,401,967,345,664.00 USD | -16.79 |
| INTC | N/A | 2.60 | 16.30 | 20.90 | 299,128,193,024.00 USD | 51.13 |

Peers fetched as_of: 2026-11-08; NVDA reuses existing data (market data as_of: 2026-11-06); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-26
- Next expected earnings: 2026-11-17 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-08

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-08-26
- Revenue (latest available single quarter): 96,221,000,000.00 USD; period 2026-04-27/2026-07-26; fiscal year/reporting period 2027/Q2
- Net income (latest available single quarter): 59,688,000,000.00 USD; period 2026-04-27/2026-07-26; fiscal year/reporting period 2027/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMimwFBVV95cUxNZ0NBcUNnaGtIbGthQ2hxZnpYaFFYdElrV3BrLUNHTkp0N0UteEE5bTFsZFNUVmhfMHVCMDFEUEVNSDhfRFpBUEdCZml0VHIwZ3FDSy1aa3NGYUJPblplN2hicUU2S01fZUtLdjgySEhJZlBvb3dBV3BVRHk5R18zanFobWY2Z25rVXVnZDh0YTlpM2JyM2o2RGQybw?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxQaDJTdlJrdzJEWjZqQTJpZHp3MTBtOFE3OUVJODBXMDdRUDRkUDdGLXRGcFhfMDQ1UXA0SWpsT2JadDlhdkg5bVRRcnNEd08yRng1bzc5Qkg3RDJlQk9uMlkzWXhZSEZjRzJnVUdQWkZpSkJqYTd6elEzVFYzVkg1cVFhelg2MF9KUXhiQ0o3T2tTdW03?oc=5
- https://news.google.com/rss/articles/CBMigwFBVV95cUxPZ3JjdG55eXd4UHpTU0FsNkw5Szl3MVgzckZGM2dUN1l3bmxiVENVdGhaV2hfcmRIbW9zWUVLTEZZX3FlS0U0WmprUW5lRHZ6a09GM3E1WXRuWUphVVJMT3ludVFnblZoN2ZENVRmS0MxSnpuYnc2N3hnQ1p0dU1nZW5vTQ?oc=5
- https://news.google.com/rss/articles/CBMi4AFBVV95cUxOdEUzQWhaem5BMHNyZnZoVHNDZV9fdXRBNVQ4T210dV9kUHlBVGlGdklmY08xQVlMcjNGblJ0ZDhSM3FDUmpRQm8tcFhVNXR3OUJWWlNjdEhPNW8zd1I5QjZOdHJqSlFHaDJ4LWd6TXR2c0YtSFFMSWZSMGsxbHNIbU9DUGxvTnVaZXEtdm5ZaDFvNlgwQ0gxZnRhaUtwTTM4MmVoZUNqUWxSVzZ0UDNxaWNkMGEtdzl1a3RRcFZSRzk4OHRCR0dRQVBDTnA1UEc0R2ptOHRMZWJIaUMwSUVFeQ?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNNjhTc0JFcEFDRDdXX3N3VDROUHZWS25HV0loYWVGV2tYaC05U3Vvc3hxdW91UERlREdKQVIxS2Y0c1M1UmE5LXUtdU9WT0pqVFJBRWZzRU0zS1hPWTByX2QtRUp3SFN2dGRyekZPSV9VdVY2NHBkSEJjdnc4T2JaRU9RdVhiaDdRY1VUR2NYWUI5cnVVMHJVaE1faGE?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxQRnZ2Y1c3VTFIcmJCY2kwcjBRdFBzcWMzV1UyaXJzWDN5YkhRWXJweVdpQlF4dXRpRmRaSTZDbk9PeUtUR2tjbjFMYTBVMG9hM1E4ZEgxZVM2TVBYSlMxcEVoaDlxMWFpQkJfS0RKbDB5YXRRaTVYZWdoSmxNSXlxUjRFbW83ajdhcEhRRXpTUHhIVHhuWlE?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxPNmJ3NGFObTl6ZGs5MUFnbk04S0hSREVIeWdxT3JVNjlXUGMyT0tvbWExS0lPQjZDUFB4akdvc2FFYVMzYWZyR3BfYjBsS1gxZGtXalV3MEhDMjlYZ2Z3alBSblQzT2dWTkN6UkR6NXl2RWJPVWtRYm8zbVpEVVZQd29xdmEyR1RWVGxfcWNodTUwVzZqV2VJeERvSkU4NlhvVmtTRnZRcERSTUZWQWhPalBn?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxPSEhJbGo5Z213RFlZOGstMFRLUW52OVk0NmF1NVl6TlJVbHlzay0tZm4zLVIySnNnSjM2SFduV2psMzk2M1YxVEtSWmpyZ3JCcVQ5MXZFX2ZrdlJkM0t0UDc2a1JvMi03R2xpbVJTeU9PcG5jNTlWVUR3Zi1YVlF6dXhDa2wzM0lOazh5anRyRmlJaTBodFcxUA?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxOTFVHWjZ5elJ3NU1wVHZGVFpaSnIzcXRZdmt1TktrLXFVXzJyQjdBVTBJa3QxS3lzRWVxT1BhclFYLVU5bnVabnRzdnVZTnNvQTU0c2Q5bHZXQ0dlTWpJVktEcTlvZDd6TmxRMGZoNmUyMzhMS21sNEg5UnRiUEpXTWlUY3BLbWFUUkE?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxQYWVoQTRyTjV4OE5iZ0gyY2NzM1M3STlkWFdhTUJxRE5fZWh2UENxRThXNVltUWpDUFVRMlBLeWxmZTFIRWh1Q2VtaEdQMVBkWVk0VG9RVENkUXRjZTFwUnlUZTBtdDE0Q3pKNVFUUXg0RWU0NXpObWxQT2wtNkd5Sy13ZVJ0bFd3OWhNM1RyQjRRRlc1cDBPS3JXUW1Fck1Pd1E?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxNSGs5d3lFcWd5WEVwZlBvelNFUWdkUFpJeEgwNGhxckJ1aVdHTmlEVHpmbnZyUEZFMHJnbnZ3c1JVUE1zZmx6eXFhUG04dnp4RzBrRF9Xa3RjVjA3ektfYmZhb0NEaFR3MVFMOUU2QTJDeGZuR2owUTJoYTVYWWdOTnZJRmkzaHhqYlBJMWlHTlZfWWpXTng2V3BzSWFPa2kzWlE?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxOcEFxSEFid1djemktcFlja1EyNW5PZkl5cHd1d1VySUdtWEF1bGFXdk5SSzIyd2x3bTEyX1A0REZ3YXNxNldtNjlLN3VwcHBMbVl2bjNIQ3FBd1RkNlF5a3pRaXllSFA5OWRCb2k1MG40VGh5THo0RGp3WVp5Z0tBMzdEaC1jSzZQTUlsblRnVjdmUHNWdmJwd0NJWmNycndNQjdkNUp3SnItcUV1?oc=5
- https://news.google.com/rss/articles/CBMie0FVX3lxTE9idXM2c01NckxhaUZZUDkzTVg1UTM3VmF1UTQ5anlKblBtVUZienBwR2xicC1EZ2ROaVhVV2k5bkdSR01SZUM4cUU4dEFPbTFwWDRrSTlESXFDR2Q4dG5VeDhKb2Y1TFh0M3k1WkRadXlCYjFiV2hpTFphQQ?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxQa191TC1XUmx2MGhqSkttRXozSF9TV2VUaG1JN0hxV0xXTUtmeFU3V2N0SUxNSlRwTlltZnZZcFNkYl8yLVlKZ0NtWVlGRjdUampudXdzMzFrMElzTzlBenFENnpBOGhhQUZRTmhvVVNYWkZZMUFDc21BcHBfa1RhdWJHV3V0WHEzYTVNSmU4WjMzQ2htWUQ4X0VrRnMwWEctYnpWdENHWGJSckZDQ2NLMlVQVnU?oc=5
- https://news.google.com/rss/articles/CBMizAFBVV95cUxOcUZESk9EalEta2UtTFc1X2FYc2ZOZWhvVUdfOEdNU0NFZGFyNkV3aFR1YklNYWxpN0pSWXZBTGhXZE0tN0sybnIySXdtbTZSOXpEM3lnV2VQSUdjenA0MnM3ZmRIV3ZQNTdYSXFhcFVQLVJ3Nk1ZdjNOZGV0S2xneGQ3T1U4NE04aHpLbGpVODRFNEN0UkN3emtKTEJiYkpuZXhONjV4LU13REhyYVZkVy1tTWZPdFowOE5hVTk4cWc4bUVwQ1Y3b2FKRDU?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxPUDNJdk9KUDJGQXU1cHkzVUdNdWUwc2Eyb3c3dFFOVkJHeDNhX3AtbEhIWlZMMWpjUmYwd05RMzhsSjFMUTR5UzBzNWw5NHprVW54OEIxbWEwYl9Ga3BiNzZmb3o1Qjl5aW1NVWxBTG9GOFM5UGRKU3MxOWpGOWhob29lU2ctTm9MdUpiag?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxNcHoxdVI4MTRJRWR4VmQycnkxX01ZeklUYlJlRXJCcDZnTG1FQ1AtZGh3YTBndWZVSWZsZEdYZkxad1ljNkdTMGlmZFp3R0Vrcmt4VTNrcnBzcEtQSlNNejhrNDJvUHdjanBFLXA1YUZYMjNuRlcyVmN6RHBub3JQNXZaaDNrcHpIYlZmWW1kRHhRUQ?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxPVFR1QjA3ODFRRlZTSXpGbG9fc1J0X2pzdjJZOHNGbEJGSnYyNTBlMEVOeHczRE5sbWdXeGhVa3Bub29EdjQtTWpqcXByR3RJQTh6emtqdU9wYzB4UkhQMzE2bUdXbW9OYm1vUTB3RjgxZVAxZks3NV95NmNBeUx2bndRUl9WUXotZTNTOUd4ZndxemVuelh0bnE5RDZhWkZCZGZTRlotMno1NnZlaWJublFqRQ?oc=5
- https://news.google.com/rss/articles/CBMihwFBVV95cUxPd1BJNjAwTmc1dWhNWkFEblREai1hbkhYZFBjT2MxaWV1b283RXNKTnk1emdfY2p5LWlXOEo5M0hLWWhjTG1UVmdVV2xvS09sb0tlelBpalV1Z1lTdUZ1VWJ5Uzl4cFJqeXV2ZUF5WVpTSWFGeGU4eldfdHpScTMySHpZQk9fWGc?oc=5
- https://news.google.com/rss/articles/CBMi4AFBVV95cUxNYU5fTUZfS2drVGlTTk43X0NHYU9EMWZJQ0pmN1IyMDlWRFJLUjdpamR6QmlYN2pLR2FYaGw2RHJPbHl6VTdXOTRDaTlMSEJEWUZLYXlSNkw0VWlRSmlTNGl6WjFmVU5rRkRVeng2alFRSjdRR2lVTEpvSWM3THFmc1dQNk5SVG9pcm93WW1IQjFLV0xSOTBZd0RoQnU4SWJJRWhMcHZWMFpWcHRvSU1TQWVsTXR6NzdBcFFRRURMdUlCZ0hnSnNzZkV6eGZ6clp6dGVhcEZUMTkwRHpwSGhibg?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
