# NVDA Intelligence Report

- ticker: **NVDA**
- Report as_of: **2026-11-17**
- Market data as_of: **2026-11-17**
- Quant sources: https://finance.yahoo.com/quote/NVDA/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NVDA/key-statistics/
- AI analysis snapshot as_of: **2026-11-17**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-18T05:59:17.103744+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 10, 'ai': 7, 'unknown': 0, 'irrelevant': 7})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **2** exact headline/source/date matches; prior report **20261117T062519Z-6171f6c2/NVDA** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'low_uncalibrated_model_confidence': 2}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 9 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 50.0%; oldest publication 2026-11-15

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 155.4600 |
| Return 1D (%) | -0.4355 |
| Return 1W (%) | -7.9519 |
| Return 1M (%) | -27.3992 |
| Return YTD (%) | -16.4484 |
| Return 1Y (%) | -16.4885 |
| Annualized volatility (%) | 38.7960 |
| Beta vs SPY | 1.7746 |
| Max drawdown (%) | -35.0192 |
| Sharpe (rf=0) | -0.2726 |
| Downside deviation (rf=0, %) | 27.9851 |
| Sortino (rf=0) | -0.3779 |
| Historical VaR 95% (1D, %) | 4.1931 |
| Historical ES 95% (1D, %) | 5.1243 |
| Correlation vs SPY | 0.6304 |
| Tracking error vs SPY (%) | 31.9529 |
| P/E (trailing) | 19.73 |
| P/B | 16.39 |
| EV/EBITDA | 18.50 |
| Revenue growth (%) | 105.90 |
| Forward P/E (estimate) | 9.79 |
| Gross margin (%) | 74.67 |
| Operating margin (%) | 65.21 |
| Return on equity (%) | 117.21 |
| Free cash flow yield (%) | 1.11 |
| MA50 | 211.7524 |
| Close vs MA50 (%) | -26.5841 |
| MA200 | 203.5989 |
| Close vs MA200 (%) | -23.6440 |
| RSI (14, Wilder) | 22.5048 |
| MACD (12,26) | -16.1525 |
| MACD signal (9) | -12.1547 |
| MACD histogram | -3.9979 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NVDA': 284, 'SPY': 284}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 155.4600 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.4355 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -7.9519 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -27.3992 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -16.4484 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -16.4885 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 38.7960 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 27.9851 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.3779 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.1931 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.1243 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6304 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 31.9529 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.7746 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -35.0192 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.2726 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 9.7903 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 74.6740 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 65.2140 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 117.2110 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.1138 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 19.7284 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 22.5048 -> Oversold momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -3.9979 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -26.5841 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -23.6440 -> Clearly below the moving-average trend level.

## TAILWINDS

### Nvidia Stock Rises On Report. Board Says No To CEO Return Bid.
- Summary: Nvidia Stock Rises On Report. Board Says No To CEO Return Bid.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxOTEx5ajRyZTctMzlRWGYyelF2RHNJcEEzd3I5alJ1YktQb1NqcFgxR3NPZVpMZUFMZzdhVTlMRkxxRG5kZVBhcG1qNTMwYlEybVN5NVhUazJYX0NPUVVHc1E1Mms5SXVuWHZVakZBZ0M5ZU56U01fRzZxVjBGeEEzcU9WU0phOXc0S0I0dHNBdUNPNC16?oc=5>

### Nvidia Stock (NVDA) Rises After Earnings Smash Estimates
- Summary: Nvidia Stock (NVDA) Rises After Earnings Smash Estimates
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihgFBVV95cUxNdmVRQU5SOWszN2VFV2ZOWUJtZ2RyUmExNG12WmRiNVEzYW9fRXJCZzcxdGFaS19EUGNkLVM5dVRUWU1lRXFpM1lVRVhqYWYwQVdxVXdrTktGRHEyUTlqTTZoTFItTTlRRWNDSTVDZXdqNE43Y1gxaE1NNXZFNGxVeXBKSDBZdw?oc=5>

### Nvidia’s First Report Without Jensen Huang: $115.8 Billion in Revenue, a $130 Billion Forecast, and the Stock Is Up 2.3% After Hours
- Summary: Nvidia’s First Report Without Jensen Huang: $115.8 Billion in Revenue, a $130 Billion Forecast, and the Stock Is Up 2.3% After Hours
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxPM0taRWswaHNxR25hZy1YTTJ3cDNod2psd3laZXZ0ZVV4OVdLVmJoWUhfa1RxNVFQdnBPNENzb25CV1VzZ0xIYlQtdENSdVJRYWFnSV9NeWJ3MUNPYTdCTEpXUk5KTUg5VlJmUEhaakN1Z0kwdVl6dERyTTRJTmlsUjJCRFlSMkk5dmhMSVNsZ2dKanpkQmVPaG5GWFkwR3NH?oc=5>

## HEADWINDS

### Nvidia stock falls as Jensen Huang reportedly weighs CEO comeback, Musk backs return
- Summary: Nvidia stock falls as Jensen Huang reportedly weighs CEO comeback, Musk backs return
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2AFBVV95cUxNVzVrZl9udUdNTVdUdnNoUG1meHJncG1HUVN6WXlXQ3JkTGNSOE9HQU1pcHJ5RFhEZ01STzQ0ZHFlNUh4YVV6eVNpN3NHNXR0eUpoT2l6bTY2QW5hT05yaXMzaGtZcVBrUWdOa25YeWNkckJ6SW80U3Q1VFhsUUJjUjV1dzNyM0EtUlR5OWh6T1paRnVjeUIzSjVqS0hIaDA1REVkMGMxM3lzMDhYdG1wOFZCLVdxRjRleXNDNTdYc2pQSDVmZVhzZ1ZTUThfWUgwdkRnUzhQOGc?oc=5>

### Nvidia Stock (NVDA) Falls as Jensen Huang Signals Openness to Return as CEO — Hours Before Q3 Earnings
- Summary: Nvidia Stock (NVDA) Falls as Jensen Huang Signals Openness to Return as CEO — Hours Before Q3 Earnings
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxNOFhwUjEyWTcyZm9jaTc4TmY2QV8wTTZXSlpXQUhYWjNpUGphSGhrLW1YaEtKSzV6SzRIdWFNd2U3SGN6T3VaWTR0WC1EQ3UxWnY5Y05kUmJ5dFFBbUFhYkFMRVVMdlZCOExUVkEtTEEtZ1dQOTk0bEpUNDRxSTVPNEtFUXhISC1EdmVRY0ZRdm9HVXE2Mko5YU90VTdYNHVOT085ZGx3emtDemx6ZVk4?oc=5>

## CATALYSTS

### Nvidia rises on strong Q3 results, guidance, buyback; Chairman says Huang not returning (NVDA:NASDAQ)
- Summary: Nvidia rises on strong Q3 results, guidance, buyback; Chairman says Huang not returning (NVDA:NASDAQ)
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxQXy1VeHZ6RVMtSXVuN2dHNzl6d0RnV1pwOWhiWDVUc1lnQTRPWlNZR2NGVGlXMk1JY2Q5QWRIdENnVFJtNnAzVy1DYmlHMEhpUVJlMHZjcWViMW53TzBaa3RuNDhaRXU0WG9acV83cTJiUHpHdGJvekIzanllcGN5SlFKTkJlRk5ZNXV1eWJVZHZXTnExem1BbGt4d2FQdTB1ZG5RdXZ5R1RjX1Y3cm1FWA?oc=5>

### Nvidia (NASDAQ:NVDA) Stock Faces $109 Billion Earnings Test After Jensen Huang’s Exit
- Summary: Nvidia (NASDAQ:NVDA) Stock Faces $109 Billion Earnings Test After Jensen Huang’s Exit
- Date: 2026-11-15 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMigAFBVV95cUxNbmhHNDBIY21SSTFlRm1jdlFiMjBGc1A1b05VczFYeE8yQkZGODNOWUhmQXMzeFF6U0ZVd3RVMzR5Mnl0OVdZWlYwQlRDdTR4cG9UWThITnJIOWtoWkxzbDY3VEVtTUExNW9iSkc1VFhBaXNMVDZwZFN0N1BIcjZXSg?oc=5>

### Nvidia Last-Minute Q3 Earnings Alert: Options Traders Expect a Large Move in NVDA Stock
- Summary: Nvidia Last-Minute Q3 Earnings Alert: Options Traders Expect a Large Move in NVDA Stock
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMif0FVX3lxTE1xckZUZ0lFM25odUdKaTJUWm9qLVF5MTQ2ekNYR0Z0SWRkOGZ5VHgzaEoyZnduTWMzanRwckRTRXRvV1paNlZodG9jajBHOUJwZTZnYWI4d3pad0p0SXRoYlNNTlVycVRZeEZvYjdxSnFQdC04MVJ1ZW10MHZycnM?oc=5>

### Nvidia's Q3 numbers were pretty good. Its earnings call optics were another story.
- Summary: Nvidia's Q3 numbers were pretty good. Its earnings call optics were another story.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxPeUdaQVBPSDdqX1pSZTdXMVJYS01IaGRZWVBIaERrZ1FHTldTVGtZVUh0SDlnbFU1ZEQzMUNLaGR4N0JIN1RYY2ZXVkFUaE5PekNRZlJDZUxFYkwwSzFzV0JNRFF5SHRWTklyaUJfZE56MHU1WWZ3Z0RRVG82akQ3QVF4RUF2M2pkU1picFpVLUVJWVJqd1ZrQTJSRFZPWXdEVzVUekhYcU1aQTZoVWFkeFA0Qk9LNEp2RUNTZjZaeVBUVXJR?oc=5>

### Nvidia stock valuation looks 'draconian,' even without Jensen Huang: Analyst
- Summary: Nvidia stock valuation looks 'draconian,' even without Jensen Huang: Analyst
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0gFBVV95cUxOMDl4WHFaaUdid1hZWl9vazlpQTJwbmxuR2xyT3RUblBjemlFOHRnR3BGemhCUmI3ZWktSHlib1NqUDl5SnFPVWlFenh6NUFUMUk1YWdyWmxfTmRKbzJDSDFZdUJCU3FTb3UzbVF0NXBJS25QMWxIOHFiSmhLXzR5clZqYmZYZkRHYi1WVXdnYkdwOUNVX2JrS1ZxUWhkaXZJdnJTcTBWMzRPbm42dm1zVEE2NmNhOEcyRUtjTkFFZU1KWWJUZk5WTVhxd1dmYXpSQlE?oc=5>

### Nvidia’s Third-Quarter Earnings, Outlook Top Wall Street Expectations
- Summary: Nvidia reported Q3 earnings surpassing analyst expectations, with strong revenue and guidance, indicating robust performance.
- Date: 2026-11-17 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxOd09QMUxzbVhUclZQOE5JTDY0VjRCUU80amJ3S0lHZnd2MERNWkthb0VHY0JpLWw5Q2xwTXM1ZlBGRERERlFVeXlxeUtTTFU1YzNuVS1UeEV1Y21TZTVrQkZidTF3N1NBOWhmZjFrTlhUNjNVSnBJVmcyRVNvQ256cTRPX091MFRGVy11bjVaTG16QWRJTjVic1VNZ3NfZnFrWmo0bVk1bW5jMWtGTXVyR3BVUlJHRzA1ZHlCZmR3?oc=5>

### Prediction: Here’s What Nvidia Stock Will Do After Its Projected $108 Billion Quarter Results Are Announced on Nov. 17
- Summary: Predicts post‑earnings stock movement after projected $108B Q3 results.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxPclVsbmIwMl9xMThBNTBoQnFKV1lqajUwWVVPbC1USWNkbDRVYW56d2ZRa08xQTJwMHMxdE5Vb3R1dVV3YU9kNzU0VEpnOTlpYllFcFVTX0Q3anZGdnJQZnhYcW9XTDU1ckxlX01zbHduSldjT2Z5WGM5a1ZYaVpxcTBCeHdHU05PbmtVbWZNd0ZGTXFoQUVGYkR2WFRLaXZEem4xN2trazhHWGI2NTFMUzY2U2dTdw?oc=5>

### Musk Joins 160,000 Signers Calling for Jensen Huang’s Nvidia Comeback: How Is NVDA Stock Reacting?
- Summary: Calls for CEO comeback; potential leadership change impact.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxOT09wamVRYTNQdlA3VVJzXzlXaDBtVVA0SjZoOXkyYUZZeXhIMnhSSkF3ZnhBbVhjbjV3bklrRUtEbUh1X3VDV01ZUE9jUFZwLTFKeDBHS21MdzhGaTlrUGc4V09xTXJvMURmY01acTFvdG5QTU1GdjZrVEkxZFR6Znd4RjZIWEhsQnFXUXp5RFZqMzdib0E?oc=5>

### Prediction: Nvidia Will Be “Forced to Implement Biometric” Kill Switches, Says Jason Calacanis
- Summary: Predicts regulatory pressure to adopt biometric kill switches.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxNNHdjdl9qZF93b3JYNlQzLWZabW45Q0s3dTVHUkpUYXgtM2dEUkl3RnQzeFBtWlJ3Mm5NN3BoeGZUMk5qZ0pJTjBZdWkzZkxXU2NaQjVSRUt3Wlc4TnhJdmtWbllkSUJlV2VSRUREeWhZa2w4SEhyZTVxc0syVS1zck1NUmFaZXZyb1B1SVhjMVJMQVlXSXZFNEVBRTNoRksyV3VQXzFNdXIzTldIREE?oc=5>

### NVIDIA Corporation Q3 2027 Earnings Call: Live Updates of $NVDA Earnings, Stock Forecast
- Summary: Live earnings call with Q3 2027 results and forecast.
- Date: 2026-11-17 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxNX015YnN1VDI3bkxGUkhSYWdCMndiLXJKNFNnVnNyTGtYWWF1a3VfYkRYODUxN0NuRy1uTnduaUlRVHFXTHl4NWV1Vk5mdGUxbURjbjJZZm5CWmV1cnpSN1UxNW5aVHkxdWV5MUJTaDdLT2J3eVNzLVUyeDNzQ0p2b3QwcWlUTUZ6U1dKaFpINno1aElUTF9oNGNwYWZkQWhJTmc?oc=5>

### Nvidia Sold a Quarter of Its Intel Shares and More Than Half Its Nokia Stake. SpaceX Is Now Its Biggest Investment
- Summary: Nvidia divested a quarter of its Intel holdings and over half of its Nokia stake, while SpaceX became its largest investment. This ownership shift may affect portfolio composition.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxPRkVjZXpReE4tRG1WY3lBRnhYdUlMYWplXzFUTVR5SGZUM3RZeVB3aHlKamJCSW40X0NlZ2VRaXhjSFdLZjlMY0JpX0k3TnBxcnpDdE1kX3h1VGRFUEJYdVFNV0VMakNxYlI4RWI2V0dEMDhRNlR3VERMSDV6QWJrS1kxY201N2NJSmZEWnIzQ2RhWlhPdkRGUXF6Zm14dw?oc=5>

## RISKS

### Nvidia (NVDA) Is Under Multiple US Justice Department Investigations
- Summary: Multiple DOJ investigations pose legal risk to Nvidia.
- Date: 2026-11-16 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxPX0RBNjNHLXc1REtobHJHUTVnTzZvTGkzWnVzQlk4cWRiNm1HdG9aWW1kRDk1LTZ2NlYwUmtsdERzcjdUdHdkY0lob3dTeXc1cEY3aF84MW82R1RYVzRKX2lEVHAtcnNDcVU2RXRic3kxQ2J5dm1VV01IS0IzMWZ4ZThKdDFRc1pCOUFLZmlZUE5lS0UzUzJfWg?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NVDA** | **19.73** | **16.39** | **18.50** | **105.90** | **3,753,892,642,816.00 USD** | **-16.49** |
| AMD | 107.80 | 12.07 | 73.50 | 44.70 | 833,176,600,576.00 USD | 109.30 |
| AVGO | 43.63 | 16.36 | 31.88 | 85.50 | 1,630,671,994,880.00 USD | 0.43 |
| INTC | N/A | 2.55 | 15.99 | 20.90 | 293,228,544,000.00 USD | 58.95 |

Peers fetched as_of: 2026-11-17; NVDA reuses existing data (market data as_of: 2026-11-17); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-17
- Next expected earnings: N/A (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-17

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
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

- https://news.google.com/rss/articles/CBMilAFBVV95cUxOTEx5ajRyZTctMzlRWGYyelF2RHNJcEEzd3I5alJ1YktQb1NqcFgxR3NPZVpMZUFMZzdhVTlMRkxxRG5kZVBhcG1qNTMwYlEybVN5NVhUazJYX0NPUVVHc1E1Mms5SXVuWHZVakZBZ0M5ZU56U01fRzZxVjBGeEEzcU9WU0phOXc0S0I0dHNBdUNPNC16?oc=5
- https://news.google.com/rss/articles/CBMihgFBVV95cUxNdmVRQU5SOWszN2VFV2ZOWUJtZ2RyUmExNG12WmRiNVEzYW9fRXJCZzcxdGFaS19EUGNkLVM5dVRUWU1lRXFpM1lVRVhqYWYwQVdxVXdrTktGRHEyUTlqTTZoTFItTTlRRWNDSTVDZXdqNE43Y1gxaE1NNXZFNGxVeXBKSDBZdw?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxPM0taRWswaHNxR25hZy1YTTJ3cDNod2psd3laZXZ0ZVV4OVdLVmJoWUhfa1RxNVFQdnBPNENzb25CV1VzZ0xIYlQtdENSdVJRYWFnSV9NeWJ3MUNPYTdCTEpXUk5KTUg5VlJmUEhaakN1Z0kwdVl6dERyTTRJTmlsUjJCRFlSMkk5dmhMSVNsZ2dKanpkQmVPaG5GWFkwR3NH?oc=5
- https://news.google.com/rss/articles/CBMi2AFBVV95cUxNVzVrZl9udUdNTVdUdnNoUG1meHJncG1HUVN6WXlXQ3JkTGNSOE9HQU1pcHJ5RFhEZ01STzQ0ZHFlNUh4YVV6eVNpN3NHNXR0eUpoT2l6bTY2QW5hT05yaXMzaGtZcVBrUWdOa25YeWNkckJ6SW80U3Q1VFhsUUJjUjV1dzNyM0EtUlR5OWh6T1paRnVjeUIzSjVqS0hIaDA1REVkMGMxM3lzMDhYdG1wOFZCLVdxRjRleXNDNTdYc2pQSDVmZVhzZ1ZTUThfWUgwdkRnUzhQOGc?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxNOFhwUjEyWTcyZm9jaTc4TmY2QV8wTTZXSlpXQUhYWjNpUGphSGhrLW1YaEtKSzV6SzRIdWFNd2U3SGN6T3VaWTR0WC1EQ3UxWnY5Y05kUmJ5dFFBbUFhYkFMRVVMdlZCOExUVkEtTEEtZ1dQOTk0bEpUNDRxSTVPNEtFUXhISC1EdmVRY0ZRdm9HVXE2Mko5YU90VTdYNHVOT085ZGx3emtDemx6ZVk4?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxQXy1VeHZ6RVMtSXVuN2dHNzl6d0RnV1pwOWhiWDVUc1lnQTRPWlNZR2NGVGlXMk1JY2Q5QWRIdENnVFJtNnAzVy1DYmlHMEhpUVJlMHZjcWViMW53TzBaa3RuNDhaRXU0WG9acV83cTJiUHpHdGJvekIzanllcGN5SlFKTkJlRk5ZNXV1eWJVZHZXTnExem1BbGt4d2FQdTB1ZG5RdXZ5R1RjX1Y3cm1FWA?oc=5
- https://news.google.com/rss/articles/CBMigAFBVV95cUxNbmhHNDBIY21SSTFlRm1jdlFiMjBGc1A1b05VczFYeE8yQkZGODNOWUhmQXMzeFF6U0ZVd3RVMzR5Mnl0OVdZWlYwQlRDdTR4cG9UWThITnJIOWtoWkxzbDY3VEVtTUExNW9iSkc1VFhBaXNMVDZwZFN0N1BIcjZXSg?oc=5
- https://news.google.com/rss/articles/CBMif0FVX3lxTE1xckZUZ0lFM25odUdKaTJUWm9qLVF5MTQ2ekNYR0Z0SWRkOGZ5VHgzaEoyZnduTWMzanRwckRTRXRvV1paNlZodG9jajBHOUJwZTZnYWI4d3pad0p0SXRoYlNNTlVycVRZeEZvYjdxSnFQdC04MVJ1ZW10MHZycnM?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxPeUdaQVBPSDdqX1pSZTdXMVJYS01IaGRZWVBIaERrZ1FHTldTVGtZVUh0SDlnbFU1ZEQzMUNLaGR4N0JIN1RYY2ZXVkFUaE5PekNRZlJDZUxFYkwwSzFzV0JNRFF5SHRWTklyaUJfZE56MHU1WWZ3Z0RRVG82akQ3QVF4RUF2M2pkU1picFpVLUVJWVJqd1ZrQTJSRFZPWXdEVzVUekhYcU1aQTZoVWFkeFA0Qk9LNEp2RUNTZjZaeVBUVXJR?oc=5
- https://news.google.com/rss/articles/CBMi0gFBVV95cUxOMDl4WHFaaUdid1hZWl9vazlpQTJwbmxuR2xyT3RUblBjemlFOHRnR3BGemhCUmI3ZWktSHlib1NqUDl5SnFPVWlFenh6NUFUMUk1YWdyWmxfTmRKbzJDSDFZdUJCU3FTb3UzbVF0NXBJS25QMWxIOHFiSmhLXzR5clZqYmZYZkRHYi1WVXdnYkdwOUNVX2JrS1ZxUWhkaXZJdnJTcTBWMzRPbm42dm1zVEE2NmNhOEcyRUtjTkFFZU1KWWJUZk5WTVhxd1dmYXpSQlE?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxOd09QMUxzbVhUclZQOE5JTDY0VjRCUU80amJ3S0lHZnd2MERNWkthb0VHY0JpLWw5Q2xwTXM1ZlBGRERERlFVeXlxeUtTTFU1YzNuVS1UeEV1Y21TZTVrQkZidTF3N1NBOWhmZjFrTlhUNjNVSnBJVmcyRVNvQ256cTRPX091MFRGVy11bjVaTG16QWRJTjVic1VNZ3NfZnFrWmo0bVk1bW5jMWtGTXVyR3BVUlJHRzA1ZHlCZmR3?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxPclVsbmIwMl9xMThBNTBoQnFKV1lqajUwWVVPbC1USWNkbDRVYW56d2ZRa08xQTJwMHMxdE5Vb3R1dVV3YU9kNzU0VEpnOTlpYllFcFVTX0Q3anZGdnJQZnhYcW9XTDU1ckxlX01zbHduSldjT2Z5WGM5a1ZYaVpxcTBCeHdHU05PbmtVbWZNd0ZGTXFoQUVGYkR2WFRLaXZEem4xN2trazhHWGI2NTFMUzY2U2dTdw?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxOT09wamVRYTNQdlA3VVJzXzlXaDBtVVA0SjZoOXkyYUZZeXhIMnhSSkF3ZnhBbVhjbjV3bklrRUtEbUh1X3VDV01ZUE9jUFZwLTFKeDBHS21MdzhGaTlrUGc4V09xTXJvMURmY01acTFvdG5QTU1GdjZrVEkxZFR6Znd4RjZIWEhsQnFXUXp5RFZqMzdib0E?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxNNHdjdl9qZF93b3JYNlQzLWZabW45Q0s3dTVHUkpUYXgtM2dEUkl3RnQzeFBtWlJ3Mm5NN3BoeGZUMk5qZ0pJTjBZdWkzZkxXU2NaQjVSRUt3Wlc4TnhJdmtWbllkSUJlV2VSRUREeWhZa2w4SEhyZTVxc0syVS1zck1NUmFaZXZyb1B1SVhjMVJMQVlXSXZFNEVBRTNoRksyV3VQXzFNdXIzTldIREE?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxNX015YnN1VDI3bkxGUkhSYWdCMndiLXJKNFNnVnNyTGtYWWF1a3VfYkRYODUxN0NuRy1uTnduaUlRVHFXTHl4NWV1Vk5mdGUxbURjbjJZZm5CWmV1cnpSN1UxNW5aVHkxdWV5MUJTaDdLT2J3eVNzLVUyeDNzQ0p2b3QwcWlUTUZ6U1dKaFpINno1aElUTF9oNGNwYWZkQWhJTmc?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxPRkVjZXpReE4tRG1WY3lBRnhYdUlMYWplXzFUTVR5SGZUM3RZeVB3aHlKamJCSW40X0NlZ2VRaXhjSFdLZjlMY0JpX0k3TnBxcnpDdE1kX3h1VGRFUEJYdVFNV0VMakNxYlI4RWI2V0dEMDhRNlR3VERMSDV6QWJrS1kxY201N2NJSmZEWnIzQ2RhWlhPdkRGUXF6Zm14dw?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxPX0RBNjNHLXc1REtobHJHUTVnTzZvTGkzWnVzQlk4cWRiNm1HdG9aWW1kRDk1LTZ2NlYwUmtsdERzcjdUdHdkY0lob3dTeXc1cEY3aF84MW82R1RYVzRKX2lEVHAtcnNDcVU2RXRic3kxQ2J5dm1VV01IS0IzMWZ4ZThKdDFRc1pCOUFLZmlZUE5lS0UzUzJfWg?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
