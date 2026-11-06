# T Intelligence Report

- ticker: **T**
- Report as_of: **2026-11-05**
- Market data as_of: **2026-11-05**
- Quant sources: https://finance.yahoo.com/quote/T/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/T/key-statistics/
- AI analysis snapshot as_of: **2026-11-05**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-06T05:08:42.784705+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 9, 'rule': 3, 'ai': 6, 'unknown': 0})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **3** exact headline/source/date matches; prior report **20261105T045846Z-bde0a1fe/T** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **3**; {'directional_claim_without_event_type': 1, 'low_uncalibrated_model_confidence': 2}
- RSS source audit (metadata only, not article fact-checking): 9 unique headlines; 5 named publishers; 0 exact duplicates; 9 HTTPS source links; largest publisher share 33.33%; oldest publication 2026-11-01

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 21.8200 |
| Return 1D (%) | -0.0458 |
| Return 1W (%) | 4.3021 |
| Return 1M (%) | -8.9659 |
| Return YTD (%) | -7.9666 |
| Return 1Y (%) | -6.9174 |
| Annualized volatility (%) | 28.6891 |
| Beta vs SPY | -0.3734 |
| Max drawdown (%) | -28.8854 |
| Sharpe (rf=0) | -0.1060 |
| Downside deviation (rf=0, %) | 21.9626 |
| Sortino (rf=0) | -0.1385 |
| Historical VaR 95% (1D, %) | 2.8546 |
| Historical ES 95% (1D, %) | 4.6484 |
| Correlation vs SPY | -0.1769 |
| Tracking error vs SPY (%) | 33.8503 |
| P/E (trailing) | 11.67 |
| P/B | 1.38 |
| EV/EBITDA | 7.29 |
| Revenue growth (%) | 5.30 |
| Forward P/E (estimate) | 8.41 |
| Gross margin (%) | 59.74 |
| Operating margin (%) | 24.65 |
| Return on equity (%) | 11.61 |
| Free cash flow yield (%) | 8.14 |
| MA50 | 23.8594 |
| Close vs MA50 (%) | -8.5475 |
| MA200 | 24.4230 |
| Close vs MA200 (%) | -10.6579 |
| RSI (14, Wilder) | 43.3676 |
| MACD (12,26) | -0.6891 |
| MACD signal (9) | -0.7641 |
| MACD histogram | 0.0750 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'T': 276, 'SPY': 276}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 21.8200 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.0458 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 4.3021 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -8.9659 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -7.9666 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -6.9174 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 28.6891 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 21.9626 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.1385 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.8546 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.6484 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.1769 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 33.8503 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.3734 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -28.8854 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.1060 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 8.4059 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 59.7420 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 24.6520 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 11.6130 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 8.1378 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 11.6684 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 43.3676 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.0750 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -8.5475 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -10.6579 -> Clearly below the moving-average trend level.

## TAILWINDS

### AT&T stock gains satellite handoff milestone as beta nears
- Summary: AT&T stock gains satellite handoff milestone as beta nears
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxPcEpFOTZmc2lwREkwb2dvVUlSUmNrR0NKaFUzSTBVbXhjNWIteWJ1Q3NqOEVWRXdZUnFzaU0zak5BQnVIaFB0TWd6Qk5NUTgxWFZnX1B5UDBiaVBOckdoMWxBVWhnT0hwLTR3MDZLQ0FOQjlnc0xOLWtjOHdELWJmejFOZWZlZUVaN3o0NmpjTFJtazdSTmlLYmxTek1uV1M4OXcwSHREdVd5dDQtb1BwaU9sOFZBekxwTVhBY09n?oc=5>

### AT&T Inc. (NYSE:T) Stock Analysis — Session Gain, High Yield and Technical Divergence
- Summary: AT&T Inc. (NYSE:T) Stock Analysis — Session Gain, High Yield and Technical Divergence
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi3gFBVV95cUxQVHFuZHF0T3ZmTjBnTkx4clhEcDJiSGJDUnlBQnNJV0kzZy1kTS1CY25SVV8tTjgtMkZ2a1dvaDd6TDIyaUNmdnRSYmFySWRXS2VFX2dhNFkzR09xN1VUYkZCM0FoS0wzQmtLYUV0UUR2VFE0NDlXMVdQMjBuYVBqUHo1Q3J2TnVuVm9GZVFCR1BMODZJYXNJNXVIejI0TTRhOWdhVEMtQnlQNVZPTm44RzdUYXNXUDVTZ0JyTmRfaEJDQk1jUDVmQlJtMVQxVUZWX3hMMHlRaWVaTW9KZEE?oc=5>

### AT&T stock gains 3.25% as customer-care shift adds new focus
- Summary: AT&T stock gains 3.25% as customer-care shift adds new focus
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxOaHNGWDBKdWlBWlotVkxNa05xaHNZNkZmR1FBVUxCY09FeS1XdGo4RHV2bTVfa3MyTFNxeXdQZDd4NWd6V1RwSjZyNEhnd0t1STh5SjRkUXhQaUxRd3VvdkdBcTJlbnp0dVFlY2xTS0N0aTZyWVMzTkxDbFZWNjdDU0oxVFpnRnNteXRIVWtYQm1kNUFUeHNHV3pFVGR5N0lMRTZhUEw1ZkhVWTVPZEZ4WTZzZTl6MDJwSjQtTWhGbw?oc=5>

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

### Is AT&T (T) Undervalued As Its Satellite Handoff Opens A New Coverage Question?
- Summary: AT&T’s satellite handoff raises coverage concerns, potentially affecting valuation.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxQMENnU1dvSXNRUjl6S1hnVUZJT0oxRUphNUxqYTBFcHRjQmE0R1ROYVRfdDh6di1jT0Y0bWpYUk1LbU9uczBEMEhkNERQRW1TMUFLQUppSnNSSXBVSjUxNldYUGhSeEowcGtJSXA1clpvODV3R1BrcWdQMVIzSG9yREthclI4c3JwVUZxS2o1V043Xzg4cWluQXhGUnRERm8?oc=5>

### AT&T (T) Sets 2027 Deadline For All U.S. Based Consumer Support
- Summary: AT&T will end U.S. consumer support by 2027, impacting service availability.
- Date: 2026-11-05 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxQVlZKTzI2eFh5YVpzc0poY293ZVZyRllfcmd1Z1VtU3pQLUxiclkxTTRuaVI5ZnY0ZXEwb21DbmJlLXVFay1CWjJkRVpRc2NOM0xzSzdQakVTZXRoYng5YWRRb21Sc1BYTEVtSE5fUjNJNFZmbWl4bjZmMTZqNWI5REhpNkRyMG41SUZMd3FUVQ?oc=5>

### AT&T, T-Mobile Are Reportedly Ready To Boot Boost Mobile If SpaceX Buys It
- Summary: AT&T and T-Mobile may discontinue Boost Mobile if acquired by SpaceX.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMi2gFBVV95cUxNOTBicHN0a1hkd3pjMGFKUjBpWVNMMTJmc2FGdjZRODBwd1VqcjZTTzVuSXFsd3duOEFhM2htVUlfX2lrbWcyUE9DN2xnMFlzVWlPNlhTbWNNOXlkQkw5eUh0d3U5UHlkM3ZXRVVRbGJCcUtwU3MxcThiWHc2V0FtU0t5NmZVQlhEYzJnWnNfV250aV9zUVJXNFIzQ3FiVEp3YXpPMnJERnhGYVdoSGJHWjQzMWFyVVNhTEFyUVNHSmZ3VUMwaWlHRnlEV09MSGVabVhhZmZPUnBOUQ?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **T** | **11.67** | **1.38** | **7.29** | **5.30** | **146,989,858,816.00 USD** | **-6.92** |
| VZ | 11.77 | 1.80 | 7.36 | 1.50 | 191,148,867,584.00 USD | 23.93 |
| TMUS | 15.35 | 3.03 | 8.02 | 7.40 | 170,108,583,936.00 USD | -19.91 |
| BCE | 4.33 | 1.46 | 7.42 | 1.50 | 20,543,545,344.00 USD | 3.67 |

Peers fetched as_of: 2026-11-05; T reuses existing data (market data as_of: 2026-11-05); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-21
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

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
- Filing date: 2026-10-21
- Revenue (latest available single quarter): 32,322,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 891,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/732717/000073271726000372/t-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMivgFBVV95cUxPcEpFOTZmc2lwREkwb2dvVUlSUmNrR0NKaFUzSTBVbXhjNWIteWJ1Q3NqOEVWRXdZUnFzaU0zak5BQnVIaFB0TWd6Qk5NUTgxWFZnX1B5UDBiaVBOckdoMWxBVWhnT0hwLTR3MDZLQ0FOQjlnc0xOLWtjOHdELWJmejFOZWZlZUVaN3o0NmpjTFJtazdSTmlLYmxTek1uV1M4OXcwSHREdVd5dDQtb1BwaU9sOFZBekxwTVhBY09n?oc=5
- https://news.google.com/rss/articles/CBMi3gFBVV95cUxQVHFuZHF0T3ZmTjBnTkx4clhEcDJiSGJDUnlBQnNJV0kzZy1kTS1CY25SVV8tTjgtMkZ2a1dvaDd6TDIyaUNmdnRSYmFySWRXS2VFX2dhNFkzR09xN1VUYkZCM0FoS0wzQmtLYUV0UUR2VFE0NDlXMVdQMjBuYVBqUHo1Q3J2TnVuVm9GZVFCR1BMODZJYXNJNXVIejI0TTRhOWdhVEMtQnlQNVZPTm44RzdUYXNXUDVTZ0JyTmRfaEJDQk1jUDVmQlJtMVQxVUZWX3hMMHlRaWVaTW9KZEE?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxOaHNGWDBKdWlBWlotVkxNa05xaHNZNkZmR1FBVUxCY09FeS1XdGo4RHV2bTVfa3MyTFNxeXdQZDd4NWd6V1RwSjZyNEhnd0t1STh5SjRkUXhQaUxRd3VvdkdBcTJlbnp0dVFlY2xTS0N0aTZyWVMzTkxDbFZWNjdDU0oxVFpnRnNteXRIVWtYQm1kNUFUeHNHV3pFVGR5N0lMRTZhUEw1ZkhVWTVPZEZ4WTZzZTl6MDJwSjQtTWhGbw?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxNSXRWRW9oXy1xdXNnckFLLUJ1bGFZS1lTS282LTl3cGtnb0ZJMU1RWG42TlQxWFdac3hKM1hOeUxxTGN6ZERVNTNyYUhkWFo0VE5uaG9qRzlpSWQtY2JXRHhnUExueGs5a1F5LTFlSENsQVZkbm96UDRTaHQtUEdZSzkzazJCLWpPSTdwNW93eG5BaVJqbnowN2tXZmR5RFI0N2c?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxPX210U1RTc0VPU2M4M3pZNjNkSnVIWXFCOGw2elYzYVJQbVV3TXlwQUhJckQ2VVVxMkpKUU1GZEdmcERITzdLc1A2cTRzclkzUmM3Wi1PYnRJOXZvT0FVbVVVVHg0a2N5MnpKc3VEWklNMW44a0ItanlkMkdPOGxITVBhd3ViOVZMbnNKY3lKV0d5blBadFduX05ReUh3NXdBRTlMZW9KTzJvYTBIMzJwVXdxaWNneFE?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxNbHVYTElaajZTMFN3Uy11UExZcXM2bWtmT2FZLVprVkVjS3B4QndlbGluWDlabDBsbGNndGpZMmNFOVRYbVBRTVNHdDRXd25vLXp6NnlrMWlEYXp1VEpHUUI1Sm1GVEg2WVZiOXIydkFYcm5IQTBnVlZCRjhVLXRFRVdyMVpfT2NRMUlUWDRSMEFyWmwxcl9ibQ?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxQMENnU1dvSXNRUjl6S1hnVUZJT0oxRUphNUxqYTBFcHRjQmE0R1ROYVRfdDh6di1jT0Y0bWpYUk1LbU9uczBEMEhkNERQRW1TMUFLQUppSnNSSXBVSjUxNldYUGhSeEowcGtJSXA1clpvODV3R1BrcWdQMVIzSG9yREthclI4c3JwVUZxS2o1V043Xzg4cWluQXhGUnRERm8?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxQVlZKTzI2eFh5YVpzc0poY293ZVZyRllfcmd1Z1VtU3pQLUxiclkxTTRuaVI5ZnY0ZXEwb21DbmJlLXVFay1CWjJkRVpRc2NOM0xzSzdQakVTZXRoYng5YWRRb21Sc1BYTEVtSE5fUjNJNFZmbWl4bjZmMTZqNWI5REhpNkRyMG41SUZMd3FUVQ?oc=5
- https://news.google.com/rss/articles/CBMi2gFBVV95cUxNOTBicHN0a1hkd3pjMGFKUjBpWVNMMTJmc2FGdjZRODBwd1VqcjZTTzVuSXFsd3duOEFhM2htVUlfX2lrbWcyUE9DN2xnMFlzVWlPNlhTbWNNOXlkQkw5eUh0d3U5UHlkM3ZXRVVRbGJCcUtwU3MxcThiWHc2V0FtU0t5NmZVQlhEYzJnWnNfV250aV9zUVJXNFIzQ3FiVEp3YXpPMnJERnhGYVdoSGJHWjQzMWFyVVNhTEFyUVNHSmZ3VUMwaWlHRnlEV09MSGVabVhhZmZPUnBOUQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
