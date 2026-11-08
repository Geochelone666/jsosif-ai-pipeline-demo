# NVDA Intelligence Report

- ticker: **NVDA**
- Report as_of: **2026-11-07**
- Market data as_of: **2026-11-06**
- Quant sources: https://finance.yahoo.com/quote/NVDA/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NVDA/key-statistics/
- AI analysis snapshot as_of: **2026-11-07**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-08T04:26:57.803747+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 23, 'rule': 2, 'ai': 10, 'unknown': 0, 'irrelevant': 11})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **11** exact headline/source/date matches; prior report **20261107T043155Z-acc5f41d/NVDA** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'low_uncalibrated_model_confidence': 1, 'short_term_price_move_in_structural_risks': 1}
- RSS source audit (metadata only, not article fact-checking): 23 unique headlines; 11 named publishers; 2 exact duplicates; 23 HTTPS source links; largest publisher share 34.78%; oldest publication 2026-11-03

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
| Downside deviation (rf=0, %) | 26.8288 |
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
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 26.8288 -> No interpretation rule is available for this metric.
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

### Nvidia Stock Rises on Dip-Buying: 3 Reasons to Be Optimistic
- Summary: Nvidia Stock Rises on Dip-Buying: 3 Reasons to Be Optimistic
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMid0FVX3lxTFBpbHc0aG5OM2dVRUpBUEFXeVRDZnB3WWpwemtTYU44MGx0MHNRUkRlUFgzUFZyaV9UTFZWSG1GekFBSktPLTl3ZzFSeEVaYnpEUUpWMkxmN3lyanNXTVhYbDNDVU1kOEh5RVdaemdOekM0Z3NMZGVZ?oc=5>

### Nvidia’s Dismal Run Might Be Coming to an End. Grab NVDA Stock While It’s Still Around $200.
- Summary: Speculation that Nvidia’s poor performance may reverse, suggesting a potential upside.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNdEgyWm5JN1NaYmppU3BFaUktcExpOVVTbjVKQTQyV3Rvc2NDV3EySldvVk5wREtUY3NON09yLVRucW1xOW9nVTVTR0tnbm0xVmVmOHJldVYxSk9fcXFQRC0zR0x2b2JfMjJXLXFLYnUtVmtjd1pTY1UyR0RVcWI5YVhTZ2F5U1kzMWNVRGxXcFVMSVdpZk5vR0xIYw?oc=5>

## HEADWINDS

### Nvidia stock oversold setup: Key levels after a 9% drop
- Summary: Nvidia stock oversold setup: Key levels after a 9% drop
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNNjhTc0JFcEFDRDdXX3N3VDROUHZWS25HV0loYWVGV2tYaC05U3Vvc3hxdW91UERlREdKQVIxS2Y0c1M1UmE5LXUtdU9WT0pqVFJBRWZzRU0zS1hPWTByX2QtRUp3SFN2dGRyekZPSV9VdVY2NHBkSEJjdnc4T2JaRU9RdVhiaDdRY1VUR2NYWUI5cnVVMHJVaE1faGE?oc=5>

### NVIDIA Stocks Rebound 6.78% as Lawmakers Call Jensen Huang to Closed-Door Briefing
- Summary: Lawmakers summoned CEO Jensen Huang for a closed-door briefing, potentially raising regulatory scrutiny and affecting investor sentiment.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxQRnZ2Y1c3VTFIcmJCY2kwcjBRdFBzcWMzV1UyaXJzWDN5YkhRWXJweVdpQlF4dXRpRmRaSTZDbk9PeUtUR2tjbjFMYTBVMG9hM1E4ZEgxZVM2TVBYSlMxcEVoaDlxMWFpQkJfS0RKbDB5YXRRaTVYZWdoSmxNSXlxUjRFbW83ajdhcEhRRXpTUHhIVHhuWlE?oc=5>

## CATALYSTS

### Nvidia: Competitive Moat Widening; Buy (NASDAQ:NVDA)
- Summary: Analyst signals widening competitive moat, recommending buy.
- Date: 2026-11-06 | Impact: medium | Horizon: medium | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMigwFBVV95cUxPZ3JjdG55eXd4UHpTU0FsNkw5Szl3MVgzckZGM2dUN1l3bmxiVENVdGhaV2hfcmRIbW9zWUVLTEZZX3FlS0U0WmprUW5lRHZ6a09GM3E1WXRuWUphVVJMT3ludVFnblZoN2ZENVRmS0MxSnpuYnc2N3hnQ1p0dU1nZW5vTQ?oc=5>

### U.S. Stock Market Movements | NVIDIA (NVDA.US) Surges Over 6% as It Plans Data Center Retrofitting Projects with Capacity Reaching 1 Gigawatt
- Summary: NVIDIA plans data center retrofitting projects reaching 1 GW, driving a 6% stock surge.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxNSGs5d3lFcWd5WEVwZlBvelNFUWdkUFpJeEgwNGhxckJ1aVdHTmlEVHpmbnZyUEZFMHJnbnZ3c1JVUE1zZmx6eXFhUG04dnp4RzBrRF9Xa3RjVjA3ektfYmZhb0NEaFR3MVFMOUU2QTJDeGZuR2owUTJoYTVYWWdOTnZJRmkzaHhqYlBJMWlHTlZfWWpXTng2V3BzSWFPa2kzWlE?oc=5>

### Why Nvidia Stock Is Getting Punished Today
- Summary: Nvidia shares decline, investors concerned about valuation and earnings prospects.
- Date: 2026-11-05 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxOOFo4dk9jUS1IVlNPa2VyZC0wSmRhMm5ZTHNkdExPSTlOZkxLMEgwcDhmeHhDM2duYjRjLUNsaDFpdWRpVkV1UVgzQ002UERWMmM1a2YtSzM0eDJvM3BLVEpTVUl5d3I4U0dBMjRhYVg3V3hySGYyWkRZTWFud2tRdXhNV21WUzVVOGVkdVp3?oc=5>

### Nvidia Stock Just Crashed 22%. Jim Cramer Says It’s the Cheapest in a Decade
- Summary: Nvidia shares fall 22%, analyst comments on low valuation.
- Date: 2026-11-06 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxOd3lNRlQ1UVRERUlJODdLWF9neGNROWZCWGxKRnpCX1RqM3pGVHAtOFJZME9SWWJ1M182SmpuTXNpTXpJbUgxSVRUd253YzRIc3BLYTY4R3FxcElvRFUyYWMxWGlTSXRoNjBDdVR5bXNidldmQVB4MlZJZnJMLVRZLTlLV2s0aUJ2b0lMZnl5UVdVWXo1X3hraXRMRlAyeE13b19iajM0ZE85eWJFZFZkUkZyU202a2l5?oc=5>

### Nvidia Stock: $181.60 After a 9% Plunge, $440B Lost
- Summary: Shares drop 9%, market cap loss of $440B.
- Date: 2026-11-06 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxOWEdSTnVORFRWcGlUdXhib2VyWVJjeGRJajNEb09abkE3Wjc0Z3hrcnRSMFpWSVRaUWhlNE94TjVBS3NLR0xjYm1OWVhfc0g2NGJuZF9OcExGWUtITEh6Q3E0MzBXVFFScFZVMnV3ZUsxNldyNklwQ1R3TUpZWWtySEowZU94Yzc3Tl9DU0t2X3ZUQjNha1R5YWJQZlE0dXBLN3M2RjRHTGtFdEd3cTFINS1LNkJoWTc4eFRaTGFSSVNrdUNUNTZIRVZmWkExUGNGRnd3VWZB?oc=5>

### NVIDIA Corporation (NVDA) stock price, news, quote and history
- Summary: General stock price information, no specific event.
- Date: 2026-11-07 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiUkFVX3lxTE81OEFKQTktenlhclpBTlVtWEJqNVpKOVNWNlRaNlRDRnR0dHRielpfZXdtR0pXcUcyNDN1WTlzOWVrWXZTNVhTbEVIOUxEaklxVWc?oc=5>

### NVIDIA sparks valuation debate after selloff (NVDA:NASDAQ)
- Summary: Selloff triggers valuation discussion among investors.
- Date: 2026-11-07 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxOTFVHWjZ5elJ3NU1wVHZGVFpaSnIzcXRZdmt1TktrLXFVXzJyQjdBVTBJa3QxS3lzRWVxT1BhclFYLVU5bnVabnRzdnVZTnNvQTU0c2Q5bHZXQ0dlTWpJVktEcTlvZDd6TmxRMGZoNmUyMzhMS21sNEg5UnRiUEpXTWlUY3BLbWFUUkE?oc=5>

## RISKS

### Nvidia Just Had Its Worst Day Since DeepSeek, Losing About $450 Billion
- Summary: Nvidia’s stock fell sharply, marking its worst day since DeepSeek and a loss of roughly $450 billion in market value.
- Date: 2026-11-06 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxOcV9uZUtoOFJZdmVFeHdoQTExOXZ2RkE0RUFSOUZMbkFZSnZrSTh6ajRIVExXZmxhbG9SbXNPVUhGUV9PTWw3VDk3RHNHSEZ0dVFzVlN1S3NhT0RQZFFicG1TZ2V2dGZDS004MmNWWWVfZGJERmNyZVM5eENGblI3QzZpYktnOWNsVzdkLU1TcDJnWlVi?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NVDA** | **23.60** | **19.68** | **22.23** | **105.90** | **4,506,795,900,928.00 USD** | **-0.53** |
| AMD | 95.95 | 10.77 | 65.50 | 44.70 | 736,464,797,696.00 USD | 88.91 |
| AVGO | 37.51 | 14.06 | 27.50 | 85.50 | 1,401,967,345,664.00 USD | -16.79 |
| INTC | N/A | 2.60 | 16.30 | 20.90 | 299,128,193,024.00 USD | 51.13 |

Peers fetched as_of: 2026-11-07; NVDA reuses existing data (market data as_of: 2026-11-06); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-26
- Next expected earnings: 2026-11-17 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-07

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

- https://news.google.com/rss/articles/CBMid0FVX3lxTFBpbHc0aG5OM2dVRUpBUEFXeVRDZnB3WWpwemtTYU44MGx0MHNRUkRlUFgzUFZyaV9UTFZWSG1GekFBSktPLTl3ZzFSeEVaYnpEUUpWMkxmN3lyanNXTVhYbDNDVU1kOEh5RVdaemdOekM0Z3NMZGVZ?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNdEgyWm5JN1NaYmppU3BFaUktcExpOVVTbjVKQTQyV3Rvc2NDV3EySldvVk5wREtUY3NON09yLVRucW1xOW9nVTVTR0tnbm0xVmVmOHJldVYxSk9fcXFQRC0zR0x2b2JfMjJXLXFLYnUtVmtjd1pTY1UyR0RVcWI5YVhTZ2F5U1kzMWNVRGxXcFVMSVdpZk5vR0xIYw?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNNjhTc0JFcEFDRDdXX3N3VDROUHZWS25HV0loYWVGV2tYaC05U3Vvc3hxdW91UERlREdKQVIxS2Y0c1M1UmE5LXUtdU9WT0pqVFJBRWZzRU0zS1hPWTByX2QtRUp3SFN2dGRyekZPSV9VdVY2NHBkSEJjdnc4T2JaRU9RdVhiaDdRY1VUR2NYWUI5cnVVMHJVaE1faGE?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxQRnZ2Y1c3VTFIcmJCY2kwcjBRdFBzcWMzV1UyaXJzWDN5YkhRWXJweVdpQlF4dXRpRmRaSTZDbk9PeUtUR2tjbjFMYTBVMG9hM1E4ZEgxZVM2TVBYSlMxcEVoaDlxMWFpQkJfS0RKbDB5YXRRaTVYZWdoSmxNSXlxUjRFbW83ajdhcEhRRXpTUHhIVHhuWlE?oc=5
- https://news.google.com/rss/articles/CBMigwFBVV95cUxPZ3JjdG55eXd4UHpTU0FsNkw5Szl3MVgzckZGM2dUN1l3bmxiVENVdGhaV2hfcmRIbW9zWUVLTEZZX3FlS0U0WmprUW5lRHZ6a09GM3E1WXRuWUphVVJMT3ludVFnblZoN2ZENVRmS0MxSnpuYnc2N3hnQ1p0dU1nZW5vTQ?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxNSGs5d3lFcWd5WEVwZlBvelNFUWdkUFpJeEgwNGhxckJ1aVdHTmlEVHpmbnZyUEZFMHJnbnZ3c1JVUE1zZmx6eXFhUG04dnp4RzBrRF9Xa3RjVjA3ektfYmZhb0NEaFR3MVFMOUU2QTJDeGZuR2owUTJoYTVYWWdOTnZJRmkzaHhqYlBJMWlHTlZfWWpXTng2V3BzSWFPa2kzWlE?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxOOFo4dk9jUS1IVlNPa2VyZC0wSmRhMm5ZTHNkdExPSTlOZkxLMEgwcDhmeHhDM2duYjRjLUNsaDFpdWRpVkV1UVgzQ002UERWMmM1a2YtSzM0eDJvM3BLVEpTVUl5d3I4U0dBMjRhYVg3V3hySGYyWkRZTWFud2tRdXhNV21WUzVVOGVkdVp3?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxOd3lNRlQ1UVRERUlJODdLWF9neGNROWZCWGxKRnpCX1RqM3pGVHAtOFJZME9SWWJ1M182SmpuTXNpTXpJbUgxSVRUd253YzRIc3BLYTY4R3FxcElvRFUyYWMxWGlTSXRoNjBDdVR5bXNidldmQVB4MlZJZnJMLVRZLTlLV2s0aUJ2b0lMZnl5UVdVWXo1X3hraXRMRlAyeE13b19iajM0ZE85eWJFZFZkUkZyU202a2l5?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQaDZYVFlNUEs5R3oxN2piM1FfQl84SUdVN1ZadFhDV2ZaaC1IX25BMVZjQ0ZUQUs5aWg3NGdTdGhRdG1UMU5XN2YyVWRUVlk0eVJ3SHo3SnlULUZmbnNFeGVEQVlTZE9jQzBGQ01vMHQ3dWZLNFA3VFVPMFFiWGh3Q3BROE5WODIwckV2anIxMnZfUHVrbG1fdQ?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxOWEdSTnVORFRWcGlUdXhib2VyWVJjeGRJajNEb09abkE3Wjc0Z3hrcnRSMFpWSVRaUWhlNE94TjVBS3NLR0xjYm1OWVhfc0g2NGJuZF9OcExGWUtITEh6Q3E0MzBXVFFScFZVMnV3ZUsxNldyNklwQ1R3TUpZWWtySEowZU94Yzc3Tl9DU0t2X3ZUQjNha1R5YWJQZlE0dXBLN3M2RjRHTGtFdEd3cTFINS1LNkJoWTc4eFRaTGFSSVNrdUNUNTZIRVZmWkExUGNGRnd3VWZB?oc=5
- https://news.google.com/rss/articles/CBMiUkFVX3lxTE81OEFKQTktenlhclpBTlVtWEJqNVpKOVNWNlRaNlRDRnR0dHRielpfZXdtR0pXcUcyNDN1WTlzOWVrWXZTNVhTbEVIOUxEaklxVWc?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxOTFVHWjZ5elJ3NU1wVHZGVFpaSnIzcXRZdmt1TktrLXFVXzJyQjdBVTBJa3QxS3lzRWVxT1BhclFYLVU5bnVabnRzdnVZTnNvQTU0c2Q5bHZXQ0dlTWpJVktEcTlvZDd6TmxRMGZoNmUyMzhMS21sNEg5UnRiUEpXTWlUY3BLbWFUUkE?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxOcV9uZUtoOFJZdmVFeHdoQTExOXZ2RkE0RUFSOUZMbkFZSnZrSTh6ajRIVExXZmxhbG9SbXNPVUhGUV9PTWw3VDk3RHNHSEZ0dVFzVlN1S3NhT0RQZFFicG1TZ2V2dGZDS004MmNWWWVfZGJERmNyZVM5eENGblI3QzZpYktnOWNsVzdkLU1TcDJnWlVi?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
