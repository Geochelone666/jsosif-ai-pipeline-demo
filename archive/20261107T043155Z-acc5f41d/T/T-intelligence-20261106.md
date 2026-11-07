# T Intelligence Report

- ticker: **T**
- Report as_of: **2026-11-06**
- Market data as_of: **2026-11-06**
- Quant sources: https://finance.yahoo.com/quote/T/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/T/key-statistics/
- AI analysis snapshot as_of: **2026-11-06**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-07T04:32:16.084871+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 15, 'rule': 3, 'ai': 8, 'unknown': 0, 'irrelevant': 4})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **5** exact headline/source/date matches; prior report **20261106T045829Z-1db1e5a7/T** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **3**; {'directional_claim_without_event_type': 1, 'low_uncalibrated_model_confidence': 2}
- RSS source audit (metadata only, not article fact-checking): 15 unique headlines; 10 named publishers; 0 exact duplicates; 15 HTTPS source links; largest publisher share 20.0%; oldest publication 2026-11-01

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 21.6300 |
| Return 1D (%) | -0.8708 |
| Return 1W (%) | 1.0276 |
| Return 1M (%) | -10.4604 |
| Return YTD (%) | -8.7680 |
| Return 1Y (%) | -8.3992 |
| Annualized volatility (%) | 28.6921 |
| Beta vs SPY | -0.3725 |
| Max drawdown (%) | -28.8854 |
| Sharpe (rf=0) | -0.1621 |
| Downside deviation (rf=0, %) | 21.9799 |
| Sortino (rf=0) | -0.2116 |
| Historical VaR 95% (1D, %) | 2.8546 |
| Historical ES 95% (1D, %) | 4.6484 |
| Correlation vs SPY | -0.1759 |
| Tracking error vs SPY (%) | 33.8175 |
| P/E (trailing) | 11.57 |
| P/B | 1.37 |
| EV/EBITDA | 7.26 |
| Revenue growth (%) | 5.30 |
| Forward P/E (estimate) | 8.33 |
| Gross margin (%) | 59.74 |
| Operating margin (%) | 24.65 |
| Return on equity (%) | 11.61 |
| Free cash flow yield (%) | 8.21 |
| MA50 | 23.7891 |
| Close vs MA50 (%) | -9.0759 |
| MA200 | 24.4173 |
| Close vs MA200 (%) | -11.4152 |
| RSI (14, Wilder) | 41.7162 |
| MACD (12,26) | -0.6457 |
| MACD signal (9) | -0.7404 |
| MACD histogram | 0.0948 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'T': 277, 'SPY': 277}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 21.6300 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.8708 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 1.0276 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -10.4604 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -8.7680 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -8.3992 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 28.6921 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 21.9799 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.2116 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.8546 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.6484 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.1759 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 33.8175 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.3725 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -28.8854 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.1621 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 8.3327 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 59.7420 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 24.6520 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 11.6130 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 8.2093 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 11.5668 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 41.7162 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.0948 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -9.0759 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -11.4152 -> Clearly below the moving-average trend level.

## TAILWINDS

### AT&T Inc. (NYSE:T) Stock Analysis — Session Gain, High Yield and Technical Divergence
- Summary: AT&T Inc. (NYSE:T) Stock Analysis — Session Gain, High Yield and Technical Divergence
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi3gFBVV95cUxQVHFuZHF0T3ZmTjBnTkx4clhEcDJiSGJDUnlBQnNJV0kzZy1kTS1CY25SVV8tTjgtMkZ2a1dvaDd6TDIyaUNmdnRSYmFySWRXS2VFX2dhNFkzR09xN1VUYkZCM0FoS0wzQmtLYUV0UUR2VFE0NDlXMVdQMjBuYVBqUHo1Q3J2TnVuVm9GZVFCR1BMODZJYXNJNXVIejI0TTRhOWdhVEMtQnlQNVZPTm44RzdUYXNXUDVTZ0JyTmRfaEJDQk1jUDVmQlJtMVQxVUZWX3hMMHlRaWVaTW9KZEE?oc=5>

### AT&T stock gains satellite handoff milestone as beta nears
- Summary: AT&T stock gains satellite handoff milestone as beta nears
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxPcEpFOTZmc2lwREkwb2dvVUlSUmNrR0NKaFUzSTBVbXhjNWIteWJ1Q3NqOEVWRXdZUnFzaU0zak5BQnVIaFB0TWd6Qk5NUTgxWFZnX1B5UDBiaVBOckdoMWxBVWhnT0hwLTR3MDZLQ0FOQjlnc0xOLWtjOHdELWJmejFOZWZlZUVaN3o0NmpjTFJtazdSTmlLYmxTek1uV1M4OXcwSHREdVd5dDQtb1BwaU9sOFZBekxwTVhBY09n?oc=5>

### What Are AT&T Stock Bulls Not Worried About?
- Summary: Explores reasons investors remain bullish on AT&T despite market concerns.
- Date: 2026-11-02 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxNSXRWRW9oXy1xdXNnckFLLUJ1bGFZS1lTS282LTl3cGtnb0ZJMU1RWG42TlQxWFdac3hKM1hOeUxxTGN6ZERVNTNyYUhkWFo0VE5uaG9qRzlpSWQtY2JXRHhnUExueGs5a1F5LTFlSENsQVZkbm96UDRTaHQtUEdZSzkzazJCLWpPSTdwNW93eG5BaVJqbnowN2tXZmR5RFI0N2c?oc=5>

### AT&T stock: Fiber momentum lifts 2026 earnings outlook
- Summary: Fiber growth boosts 2026 earnings outlook.
- Date: 2026-11-03 | Impact: high | Horizon: long | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxPX210U1RTc0VPU2M4M3pZNjNkSnVIWXFCOGw2elYzYVJQbVV3TXlwQUhJckQ2VVVxMkpKUU1GZEdmcERITzdLc1A2cTRzclkzUmM3Wi1PYnRJOXZvT0FVbVVVVHg0a2N5MnpKc3VEWklNMW44a0ItanlkMkdPOGxITVBhd3ViOVZMbnNKY3lKV0d5blBadFduX05ReUh3NXdBRTlMZW9KTzJvYTBIMzJwVXdxaWNneFE?oc=5>

## HEADWINDS

### Do Wall Street Analysts Like AT&T Stock?
- Summary: Analysts' sentiment toward AT&T stock questioned.
- Date: 2026-11-01 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxNbHVYTElaajZTMFN3Uy11UExZcXM2bWtmT2FZLVprVkVjS3B4QndlbGluWDlabDBsbGNndGpZMmNFOVRYbVBRTVNHdDRXd25vLXp6NnlrMWlEYXp1VEpHUUI1Sm1GVEg2WVZiOXIydkFYcm5IQTBnVlZCRjhVLXRFRVdyMVpfT2NRMUlUWDRSMEFyWmwxcl9ibQ?oc=5>

## CATALYSTS

### AT&T Inc. $T Stock Sold by Hennessy Advisors Inc.
- Summary: AT&T Inc. $T Stock Sold by Hennessy Advisors Inc.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxOMGlUNEtuai12dU1id1JBNXNXdUo4Q0YxWkVLRTlQOTlpMkxWa1dGbGlrNFp6c04tcVVaa1NqUFVJamJpX0dWNU82b0c4Y1JSSW9BVklVM1VpTjNIS0VaX1hVSURUbl9fY1dhR1pwdXNTTTFmVVNaWktTQVVuVEVvaWxkQTN0OE1LdnRJb0dEaklBWmFXbWhKTjd2d1ZXZHZ5aGMzY1EwWXZKZw?oc=5>

### Is AT&T (T) Undervalued As Its Satellite Handoff Opens A New Coverage Question?
- Summary: AT&T’s satellite handoff raises coverage concerns, potentially affecting valuation.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxQMENnU1dvSXNRUjl6S1hnVUZJT0oxRUphNUxqYTBFcHRjQmE0R1ROYVRfdDh6di1jT0Y0bWpYUk1LbU9uczBEMEhkNERQRW1TMUFLQUppSnNSSXBVSjUxNldYUGhSeEowcGtJSXA1clpvODV3R1BrcWdQMVIzSG9yREthclI4c3JwVUZxS2o1V043Xzg4cWluQXhGUnRERm8?oc=5>

### AT&T, T-Mobile Are Reportedly Ready To Boot Boost Mobile If SpaceX Buys It
- Summary: AT&T and T-Mobile may discontinue Boost Mobile if acquired by SpaceX.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMi2gFBVV95cUxNOTBicHN0a1hkd3pjMGFKUjBpWVNMMTJmc2FGdjZRODBwd1VqcjZTTzVuSXFsd3duOEFhM2htVUlfX2lrbWcyUE9DN2xnMFlzVWlPNlhTbWNNOXlkQkw5eUh0d3U5UHlkM3ZXRVVRbGJCcUtwU3MxcThiWHc2V0FtU0t5NmZVQlhEYzJnWnNfV250aV9zUVJXNFIzQ3FiVEp3YXpPMnJERnhGYVdoSGJHWjQzMWFyVVNhTEFyUVNHSmZ3VUMwaWlHRnlEV09MSGVabVhhZmZPUnBOUQ?oc=5>

### AT&T Inc. $T Stock: Trek Financial LLC Boosts Stake
- Summary: Trek Financial LLC increases its stake in AT&T, signaling confidence in the company.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxQbXgwckVldlJXcnJWMDhzazFkb05uVW1YeXpUZ0NPb2tMYUlFVFZ0M3pQVGo2ZGk3ZHptTWdqcWZaQ2JfNHlCZWhaVVNDQ0NpcHhzdkF2RlZ4ejFVdTZrblB6X1p6UDdiRkJhQkRodk1xczhPQkw3YVVKTVRxdllnTnlBdG5zOEcyNEd1UWI3TmZpcTRUZFE1dmFDUzlOZHgwbzVYaHF3LXVERjV6?oc=5>

### AT&T Inc. $T Stock Position Boosted by Rakuten Investment Management Inc.
- Summary: Rakuten Investment Management increased its stake in AT&T, signaling confidence in the telecom's prospects.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiygFBVV95cUxPbnU2VlpQa1YwTy1XSVJEWXZZUVU0dGlnNzVqazBMbUpBV281cmt0bW40cE1JUy01YTBvWS11dXNlLWF2ZTlQTDRIZjN6c3V1QXVPcU50UEZCekpjTHEtNENtd25vRUdBZ2RQMElnQmVRR2kxMzN6cU14ejFxNWhCaUVOZ01WYmloSGhwT1dybXJ3eWgydlpsbldDUTBZR2c3a2FBVTNJYTZhNG9VWDZYRUxTZjhMOHRPcWpuWl82NzVBeEdlNnFJdHVR?oc=5>

## RISKS

### AT&T stock targets copper theft as network outages raise risks
- Summary: AT&T faces copper theft threats linked to network outages, heightening operational risks.
- Date: 2026-11-06 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxNU1FXNnQ5N3ZQRjJQT05jT3M3WlpLUjZ4c0pOZTFkdkdTaGNkWk4tbU9fTXJwMDdBVFd0NkM4dVFXb0d3Y1ZpMjlvbUcyWkVWbzlpb1Z4X0pXMU95cGFfS3ljNHAzVjY3VEZwWTF1SWFjYzM3QmJFRnhsY2MzZUVQcnBkUHZTU2dZVXJFM2tSWHhGRnRJa3JwSDdzQ2hRUEpMblFVVHZDMEVhNjB3RG4tYTYySXFaSHFza1JhU3lkZ25LVk0?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **T** | **11.57** | **1.37** | **7.26** | **5.30** | **145,709,924,352.00 USD** | **-8.40** |
| VZ | 11.66 | 1.79 | 7.32 | 1.50 | 189,366,681,600.00 USD | 22.38 |
| TMUS | 15.62 | 3.06 | 8.06 | 7.40 | 171,612,749,824.00 USD | -17.70 |
| BCE | 11.88 | 1.43 | 7.42 | 1.50 | 20,161,208,320.00 USD | -1.68 |

Peers fetched as_of: 2026-11-06; T reuses existing data (market data as_of: 2026-11-06); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-21
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-06

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-21
- Revenue (latest available single quarter): 32,322,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 891,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/732717/000073271726000372/t-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMi3gFBVV95cUxQVHFuZHF0T3ZmTjBnTkx4clhEcDJiSGJDUnlBQnNJV0kzZy1kTS1CY25SVV8tTjgtMkZ2a1dvaDd6TDIyaUNmdnRSYmFySWRXS2VFX2dhNFkzR09xN1VUYkZCM0FoS0wzQmtLYUV0UUR2VFE0NDlXMVdQMjBuYVBqUHo1Q3J2TnVuVm9GZVFCR1BMODZJYXNJNXVIejI0TTRhOWdhVEMtQnlQNVZPTm44RzdUYXNXUDVTZ0JyTmRfaEJDQk1jUDVmQlJtMVQxVUZWX3hMMHlRaWVaTW9KZEE?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxPcEpFOTZmc2lwREkwb2dvVUlSUmNrR0NKaFUzSTBVbXhjNWIteWJ1Q3NqOEVWRXdZUnFzaU0zak5BQnVIaFB0TWd6Qk5NUTgxWFZnX1B5UDBiaVBOckdoMWxBVWhnT0hwLTR3MDZLQ0FOQjlnc0xOLWtjOHdELWJmejFOZWZlZUVaN3o0NmpjTFJtazdSTmlLYmxTek1uV1M4OXcwSHREdVd5dDQtb1BwaU9sOFZBekxwTVhBY09n?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxNSXRWRW9oXy1xdXNnckFLLUJ1bGFZS1lTS282LTl3cGtnb0ZJMU1RWG42TlQxWFdac3hKM1hOeUxxTGN6ZERVNTNyYUhkWFo0VE5uaG9qRzlpSWQtY2JXRHhnUExueGs5a1F5LTFlSENsQVZkbm96UDRTaHQtUEdZSzkzazJCLWpPSTdwNW93eG5BaVJqbnowN2tXZmR5RFI0N2c?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxPX210U1RTc0VPU2M4M3pZNjNkSnVIWXFCOGw2elYzYVJQbVV3TXlwQUhJckQ2VVVxMkpKUU1GZEdmcERITzdLc1A2cTRzclkzUmM3Wi1PYnRJOXZvT0FVbVVVVHg0a2N5MnpKc3VEWklNMW44a0ItanlkMkdPOGxITVBhd3ViOVZMbnNKY3lKV0d5blBadFduX05ReUh3NXdBRTlMZW9KTzJvYTBIMzJwVXdxaWNneFE?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxNbHVYTElaajZTMFN3Uy11UExZcXM2bWtmT2FZLVprVkVjS3B4QndlbGluWDlabDBsbGNndGpZMmNFOVRYbVBRTVNHdDRXd25vLXp6NnlrMWlEYXp1VEpHUUI1Sm1GVEg2WVZiOXIydkFYcm5IQTBnVlZCRjhVLXRFRVdyMVpfT2NRMUlUWDRSMEFyWmwxcl9ibQ?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxOMGlUNEtuai12dU1id1JBNXNXdUo4Q0YxWkVLRTlQOTlpMkxWa1dGbGlrNFp6c04tcVVaa1NqUFVJamJpX0dWNU82b0c4Y1JSSW9BVklVM1VpTjNIS0VaX1hVSURUbl9fY1dhR1pwdXNTTTFmVVNaWktTQVVuVEVvaWxkQTN0OE1LdnRJb0dEaklBWmFXbWhKTjd2d1ZXZHZ5aGMzY1EwWXZKZw?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxQMENnU1dvSXNRUjl6S1hnVUZJT0oxRUphNUxqYTBFcHRjQmE0R1ROYVRfdDh6di1jT0Y0bWpYUk1LbU9uczBEMEhkNERQRW1TMUFLQUppSnNSSXBVSjUxNldYUGhSeEowcGtJSXA1clpvODV3R1BrcWdQMVIzSG9yREthclI4c3JwVUZxS2o1V043Xzg4cWluQXhGUnRERm8?oc=5
- https://news.google.com/rss/articles/CBMi2gFBVV95cUxNOTBicHN0a1hkd3pjMGFKUjBpWVNMMTJmc2FGdjZRODBwd1VqcjZTTzVuSXFsd3duOEFhM2htVUlfX2lrbWcyUE9DN2xnMFlzVWlPNlhTbWNNOXlkQkw5eUh0d3U5UHlkM3ZXRVVRbGJCcUtwU3MxcThiWHc2V0FtU0t5NmZVQlhEYzJnWnNfV250aV9zUVJXNFIzQ3FiVEp3YXpPMnJERnhGYVdoSGJHWjQzMWFyVVNhTEFyUVNHSmZ3VUMwaWlHRnlEV09MSGVabVhhZmZPUnBOUQ?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxQbXgwckVldlJXcnJWMDhzazFkb05uVW1YeXpUZ0NPb2tMYUlFVFZ0M3pQVGo2ZGk3ZHptTWdqcWZaQ2JfNHlCZWhaVVNDQ0NpcHhzdkF2RlZ4ejFVdTZrblB6X1p6UDdiRkJhQkRodk1xczhPQkw3YVVKTVRxdllnTnlBdG5zOEcyNEd1UWI3TmZpcTRUZFE1dmFDUzlOZHgwbzVYaHF3LXVERjV6?oc=5
- https://news.google.com/rss/articles/CBMiygFBVV95cUxPbnU2VlpQa1YwTy1XSVJEWXZZUVU0dGlnNzVqazBMbUpBV281cmt0bW40cE1JUy01YTBvWS11dXNlLWF2ZTlQTDRIZjN6c3V1QXVPcU50UEZCekpjTHEtNENtd25vRUdBZ2RQMElnQmVRR2kxMzN6cU14ejFxNWhCaUVOZ01WYmloSGhwT1dybXJ3eWgydlpsbldDUTBZR2c3a2FBVTNJYTZhNG9VWDZYRUxTZjhMOHRPcWpuWl82NzVBeEdlNnFJdHVR?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxNU1FXNnQ5N3ZQRjJQT05jT3M3WlpLUjZ4c0pOZTFkdkdTaGNkWk4tbU9fTXJwMDdBVFd0NkM4dVFXb0d3Y1ZpMjlvbUcyWkVWbzlpb1Z4X0pXMU95cGFfS3ljNHAzVjY3VEZwWTF1SWFjYzM3QmJFRnhsY2MzZUVQcnBkUHZTU2dZVXJFM2tSWHhGRnRJa3JwSDdzQ2hRUEpMblFVVHZDMEVhNjB3RG4tYTYySXFaSHFza1JhU3lkZ25LVk0?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
