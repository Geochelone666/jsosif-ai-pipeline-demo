# T Intelligence Report

- ticker: **T**
- Report as_of: **2026-11-09**
- Market data as_of: **2026-11-09**
- Quant sources: https://finance.yahoo.com/quote/T/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/T/key-statistics/
- AI analysis snapshot as_of: **2026-11-09**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-10T05:51:37.934442+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 12, 'rule': 1, 'ai': 9, 'unknown': 0, 'irrelevant': 2})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **6** exact headline/source/date matches; prior report **20261109T043242Z-c8e908de/T** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 12 unique headlines; 10 named publishers; 2 exact duplicates; 12 HTTPS source links; largest publisher share 16.67%; oldest publication 2026-11-02

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 21.8000 |
| Return 1D (%) | 0.7859 |
| Return 1W (%) | 1.6791 |
| Return 1M (%) | -1.7133 |
| Return YTD (%) | -8.0510 |
| Return 1Y (%) | -8.0139 |
| Annualized volatility (%) | 28.7584 |
| Beta vs SPY | -0.3565 |
| Max drawdown (%) | -28.8854 |
| Sharpe (rf=0) | -0.1476 |
| Downside deviation (rf=0, %) | 22.0238 |
| Sortino (rf=0) | -0.1927 |
| Historical VaR 95% (1D, %) | 2.8611 |
| Historical ES 95% (1D, %) | 4.6484 |
| Correlation vs SPY | -0.1697 |
| Tracking error vs SPY (%) | 33.8846 |
| P/E (trailing) | 11.66 |
| P/B | 1.38 |
| EV/EBITDA | 7.29 |
| Revenue growth (%) | 5.30 |
| Forward P/E (estimate) | 8.40 |
| Gross margin (%) | 59.74 |
| Operating margin (%) | 24.65 |
| Return on equity (%) | 11.61 |
| Free cash flow yield (%) | 8.15 |
| MA50 | 23.7107 |
| Close vs MA50 (%) | -8.0583 |
| MA200 | 24.4124 |
| Close vs MA200 (%) | -10.7011 |
| RSI (14, Wilder) | 43.7790 |
| MACD (12,26) | -0.5907 |
| MACD signal (9) | -0.7105 |
| MACD histogram | 0.1198 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'T': 278, 'SPY': 278}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 21.8000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.7859 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 1.6791 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -1.7133 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -8.0510 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -8.0139 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 28.7584 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 22.0238 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.1927 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.8611 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.6484 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.1697 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 33.8846 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.3565 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -28.8854 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.1476 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 8.3982 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 59.7420 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 24.6520 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 11.6130 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 8.1453 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 11.6578 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 43.7790 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.1198 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -8.0583 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -10.7011 -> Clearly below the moving-average trend level.

## TAILWINDS

### AT&T stock gains satellite handoff milestone as beta nears
- Summary: AT&T stock gains satellite handoff milestone as beta nears
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxPZjM0LW8wSEpEWXNNZVMwZHdUZWV3Z3NubEVjQUlydFl0TnFwQU9sQkRVTnF3MnVLZDZXdWhlcThhb19WSHhxaDEtUVAwMTJOR1R6VURoTzJhYjMzT3lTbjhyUy1FQW9nTWszcGRFYzEzUzdKYzJXVGMxUW5YdUV2Q0R1dzVGNnh6Um95U3MyQnpIbzRBbzFmSng3b19QQWdtb1ptYy04cW92TVQzUDhtdXZXWENQcGFjRU10OVlB?oc=5>

### AT&T stock advances after ground-to-satellite handoff milestone
- Summary: AT&T stock rises following a ground-to-satellite handoff milestone, indicating progress in its satellite network.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxQaTBpWkVoX2xVQ1VtWlZRNXd4NHlOQ2c3U1pFNmxTZFZiVFdibHJqTUQtUGJ2NnoyeUlRaDhGUnRwN2VGM0dXd24tWmQ1MUZ3M016M2gxSVl1MXVKM0xtWTdUcmg3MUVUS1VLSVZDdDVaNloxMGpENWx3cG5WWFJiVGUtZlVzR2RWUGxtdGFZYUFDTWl4NzdkVHplMWZzOXIzQUtpOGY3RzJzWVozNlFLMkpYT1pqNFo3Y043TVlOaEdhUU5R?oc=5>

## HEADWINDS

### AT&T Stock Falls 11.8% in a Year: Should You Buy the Dip?
- Summary: AT&T shares dropped 11.8% over the year, raising doubts about value.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0AFBVV95cUxOX1RqTnRGQkpieEpOckpkVlRHb0J2NUtFUkRJLTRyQWRMTDVvSFF3WWlidHZ6ZHZpN1FOQ0RfVzVSWGxWVVlOWHU1cm5rd0VBbC1RMC1KdzZPdFVHZUlad2FNbEp4Sk1vWjZuMXAwMlhOT05HbnJFRERRRjBmcnBkUVhRNk14ZlhHMmx6MUVVY3RDV0lIbnB3UnN2a1JaczN2eHpyTkNjN1ZYemU3QVkzdXdtamNueUNpWTFncGphd2t5NXJnN0lmcnY0UGxjcG01?oc=5>

### Why AT&T Stock Slumped in October
- Summary: AT&T stock fell in October, reflecting a decline in investor confidence.
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMihwFBVV95cUxNcm8tYWtGY1RKVEpGcGc3THl3dXNvOTRQN0xoTXNBdnJwUmswMVg0d180VjlELTRFeFd2ejhvR1M5cE5QeUF3WDAwLTJpbFZQaFRuRG1NdkVON0drcGpFbjNvVU9uTngxU05FcmdWU2cwbDE0dS01MXRZSUdBZk9rSzJlRXdIRVE?oc=5>

### 'Big Short' Investor Steve Eisman Says AT&T, Verizon and T-Mobile Are 'Uninvestable' as Elon Musk Targets US Wireless Market
- Summary: Investor Steve Eisman deems AT&T uninvestable amid Musk's market entry, signaling negative outlook.
- Date: 2026-11-09 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxOdE9zdjg3TERlenVnUzQ2MkpLTTRtSUU0LTBadHZvQmJyN3hTZWdOQVhuc2tVNnhzRzItUzYxS19NUkJnZFhIYjVGSHpwMDJ1dmNDRDhTZC1SY2lSWTNDdE1SVDBtbmJoVWx3VFdqSDVLNDI1NmEybmI5ZU03a01aMC1fbDZHanNqY0c3Yl9nSUYtblVDQUFYc0xPQUM?oc=5>

### AT&T, T-Mobile Are Reportedly Ready To Boot Boost Mobile If SpaceX Buys It
- Summary: AT&T and T-Mobile may remove Boost Mobile if SpaceX acquires it, indicating potential market disruption.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2gFBVV95cUxNOTBicHN0a1hkd3pjMGFKUjBpWVNMMTJmc2FGdjZRODBwd1VqcjZTTzVuSXFsd3duOEFhM2htVUlfX2lrbWcyUE9DN2xnMFlzVWlPNlhTbWNNOXlkQkw5eUh0d3U5UHlkM3ZXRVVRbGJCcUtwU3MxcThiWHc2V0FtU0t5NmZVQlhEYzJnWnNfV250aV9zUVJXNFIzQ3FiVEp3YXpPMnJERnhGYVdoSGJHWjQzMWFyVVNhTEFyUVNHSmZ3VUMwaWlHRnlEV09MSGVabVhhZmZPUnBOUQ?oc=5>

### SpaceX Could Buy a Legacy Telco to Take On AT&T and T-Mobile, Elon Musk Says
- Summary: SpaceX may acquire a legacy telco to compete with AT&T and T-Mobile, posing a competitive threat.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxNWnBIWHdvT0NMZTc1dXl6bmFfLXJveS01UWxLb05hWTRGZGtMUkVLUTdyZ3BjRWQ5aTZkVVdXVlJMUWYycFF4bTdSLV9xWGNqZmJsRE85SjJSVWV6NV9wVWphbEZDWFRnbGFLSEJNdzRPTnZmM2RHMXFDb2psR3RVaWowdXNtbHpJeGFuNXM5d2d1djVQbkt1LVZHMzhPeEZFdzBqelNLaFNDVWNuOENkWQ?oc=5>

## CATALYSTS

### Is AT&T (T) Undervalued As Its Satellite Handoff Opens A New Coverage Question?
- Summary: AT&T’s satellite handoff raises coverage concerns, potentially affecting valuation.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxQMENnU1dvSXNRUjl6S1hnVUZJT0oxRUphNUxqYTBFcHRjQmE0R1ROYVRfdDh6di1jT0Y0bWpYUk1LbU9uczBEMEhkNERQRW1TMUFLQUppSnNSSXBVSjUxNldYUGhSeEowcGtJSXA1clpvODV3R1BrcWdQMVIzSG9yREthclI4c3JwVUZxS2o1V043Xzg4cWluQXhGUnRERm8?oc=5>

### TELUS Faces Q3 Challenges Amid Strategic Shift; AT&T (T) Dividen
- Summary: AT&T announced a dividend amid TELUS’s Q3 challenges.
- Date: 2026-11-07 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxNSTNSUU9EenFtcnVyRHdYNm5mMXU3MDUwcEJaT3FnaWhSRElpSjVwV1NsQUphRmN4SV9GLTk4cXJFNnFtc1c2dGF0cG91aXFCdXVSc044UWhJdDBPN2VIak5NWXptZHRraUJvRGVvdVVtUF90S2NPejRnWExXNHlLVEp4dF9wMXh5WWdVV2RRVXNDZlZ3cWREOGNyRnJhUTFoeTlhQ2NCSmduNk0zWlFFSlJnZlVjbDhXbnZZZXJhcjlMdw?oc=5>

### A phone connection switched from towers to a satellite without interruption. AT&T expects real-world trials next.
- Summary: AT&T plans real‑world trials of satellite‑based phone service after successful tower‑to‑satellite switch.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxQSnJWY2hhNzhnRDd6TDhzNU1RMVpMajVBQ1dDNVRVaFBZQWM4blQ5eHlnLTdfczFGdGtobVp5YS1wRHZBSHNfZ09QdndRMndNbE40Y0UwSWtLZWJMMlh0OFJ4bVU5U2NMWWFUaFZwZUV5bGtzR2VmNFpEZHNBc0FMWV9VQjQtQTBzejdGMkNKMVBHaV9vZzN6SFlzdjVIVlFFZnBmSUZnb0dFeHB3YWFrQ2ZoNA?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **T** | **11.66** | **1.38** | **7.29** | **5.30** | **146,855,116,800.00 USD** | **-8.01** |
| VZ | 11.75 | 1.80 | 7.35 | 1.50 | 190,900,207,616.00 USD | 22.72 |
| TMUS | 16.27 | 3.18 | 8.26 | 7.40 | 178,709,889,024.00 USD | -16.78 |
| BCE | 11.62 | 1.35 | 7.37 | 2.20 | 20,039,979,008.00 USD | -2.36 |

Peers fetched as_of: 2026-11-09; T reuses existing data (market data as_of: 2026-11-09); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-21
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

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
- Filing date: 2026-10-21
- Revenue (latest available single quarter): 32,322,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 891,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/732717/000073271726000372/t-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMivgFBVV95cUxPZjM0LW8wSEpEWXNNZVMwZHdUZWV3Z3NubEVjQUlydFl0TnFwQU9sQkRVTnF3MnVLZDZXdWhlcThhb19WSHhxaDEtUVAwMTJOR1R6VURoTzJhYjMzT3lTbjhyUy1FQW9nTWszcGRFYzEzUzdKYzJXVGMxUW5YdUV2Q0R1dzVGNnh6Um95U3MyQnpIbzRBbzFmSng3b19QQWdtb1ptYy04cW92TVQzUDhtdXZXWENQcGFjRU10OVlB?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxPcEpFOTZmc2lwREkwb2dvVUlSUmNrR0NKaFUzSTBVbXhjNWIteWJ1Q3NqOEVWRXdZUnFzaU0zak5BQnVIaFB0TWd6Qk5NUTgxWFZnX1B5UDBiaVBOckdoMWxBVWhnT0hwLTR3MDZLQ0FOQjlnc0xOLWtjOHdELWJmejFOZWZlZUVaN3o0NmpjTFJtazdSTmlLYmxTek1uV1M4OXcwSHREdVd5dDQtb1BwaU9sOFZBekxwTVhBY09n?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxQaTBpWkVoX2xVQ1VtWlZRNXd4NHlOQ2c3U1pFNmxTZFZiVFdibHJqTUQtUGJ2NnoyeUlRaDhGUnRwN2VGM0dXd24tWmQ1MUZ3M016M2gxSVl1MXVKM0xtWTdUcmg3MUVUS1VLSVZDdDVaNloxMGpENWx3cG5WWFJiVGUtZlVzR2RWUGxtdGFZYUFDTWl4NzdkVHplMWZzOXIzQUtpOGY3RzJzWVozNlFLMkpYT1pqNFo3Y043TVlOaEdhUU5R?oc=5
- https://news.google.com/rss/articles/CBMi0AFBVV95cUxOX1RqTnRGQkpieEpOckpkVlRHb0J2NUtFUkRJLTRyQWRMTDVvSFF3WWlidHZ6ZHZpN1FOQ0RfVzVSWGxWVVlOWHU1cm5rd0VBbC1RMC1KdzZPdFVHZUlad2FNbEp4Sk1vWjZuMXAwMlhOT05HbnJFRERRRjBmcnBkUVhRNk14ZlhHMmx6MUVVY3RDV0lIbnB3UnN2a1JaczN2eHpyTkNjN1ZYemU3QVkzdXdtamNueUNpWTFncGphd2t5NXJnN0lmcnY0UGxjcG01?oc=5
- https://news.google.com/rss/articles/CBMihwFBVV95cUxNcm8tYWtGY1RKVEpGcGc3THl3dXNvOTRQN0xoTXNBdnJwUmswMVg0d180VjlELTRFeFd2ejhvR1M5cE5QeUF3WDAwLTJpbFZQaFRuRG1NdkVON0drcGpFbjNvVU9uTngxU05FcmdWU2cwbDE0dS01MXRZSUdBZk9rSzJlRXdIRVE?oc=5
- https://news.google.com/rss/articles/CBMie0FVX3lxTFB2YXVlREQ3R0NieWVFMkRISThWcE5kRFRqcXVfdjVzUy0zenpJNVo4eFQ2Wmt5Q1Q1N002cVZ6MTUyU2JLYk9tQVg0bFM3d0VNU013Y180allLd1ZPeHE1OUtOeURuc0xrV0N5S3h4M2pmRGxwMURMV1JlOA?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxOdE9zdjg3TERlenVnUzQ2MkpLTTRtSUU0LTBadHZvQmJyN3hTZWdOQVhuc2tVNnhzRzItUzYxS19NUkJnZFhIYjVGSHpwMDJ1dmNDRDhTZC1SY2lSWTNDdE1SVDBtbmJoVWx3VFdqSDVLNDI1NmEybmI5ZU03a01aMC1fbDZHanNqY0c3Yl9nSUYtblVDQUFYc0xPQUM?oc=5
- https://news.google.com/rss/articles/CBMi2gFBVV95cUxNOTBicHN0a1hkd3pjMGFKUjBpWVNMMTJmc2FGdjZRODBwd1VqcjZTTzVuSXFsd3duOEFhM2htVUlfX2lrbWcyUE9DN2xnMFlzVWlPNlhTbWNNOXlkQkw5eUh0d3U5UHlkM3ZXRVVRbGJCcUtwU3MxcThiWHc2V0FtU0t5NmZVQlhEYzJnWnNfV250aV9zUVJXNFIzQ3FiVEp3YXpPMnJERnhGYVdoSGJHWjQzMWFyVVNhTEFyUVNHSmZ3VUMwaWlHRnlEV09MSGVabVhhZmZPUnBOUQ?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxNWnBIWHdvT0NMZTc1dXl6bmFfLXJveS01UWxLb05hWTRGZGtMUkVLUTdyZ3BjRWQ5aTZkVVdXVlJMUWYycFF4bTdSLV9xWGNqZmJsRE85SjJSVWV6NV9wVWphbEZDWFRnbGFLSEJNdzRPTnZmM2RHMXFDb2psR3RVaWowdXNtbHpJeGFuNXM5d2d1djVQbkt1LVZHMzhPeEZFdzBqelNLaFNDVWNuOENkWQ?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxQMENnU1dvSXNRUjl6S1hnVUZJT0oxRUphNUxqYTBFcHRjQmE0R1ROYVRfdDh6di1jT0Y0bWpYUk1LbU9uczBEMEhkNERQRW1TMUFLQUppSnNSSXBVSjUxNldYUGhSeEowcGtJSXA1clpvODV3R1BrcWdQMVIzSG9yREthclI4c3JwVUZxS2o1V043Xzg4cWluQXhGUnRERm8?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxNSTNSUU9EenFtcnVyRHdYNm5mMXU3MDUwcEJaT3FnaWhSRElpSjVwV1NsQUphRmN4SV9GLTk4cXJFNnFtc1c2dGF0cG91aXFCdXVSc044UWhJdDBPN2VIak5NWXptZHRraUJvRGVvdVVtUF90S2NPejRnWExXNHlLVEp4dF9wMXh5WWdVV2RRVXNDZlZ3cWREOGNyRnJhUTFoeTlhQ2NCSmduNk0zWlFFSlJnZlVjbDhXbnZZZXJhcjlMdw?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxQSnJWY2hhNzhnRDd6TDhzNU1RMVpMajVBQ1dDNVRVaFBZQWM4blQ5eHlnLTdfczFGdGtobVp5YS1wRHZBSHNfZ09QdndRMndNbE40Y0UwSWtLZWJMMlh0OFJ4bVU5U2NMWWFUaFZwZUV5bGtzR2VmNFpEZHNBc0FMWV9VQjQtQTBzejdGMkNKMVBHaV9vZzN6SFlzdjVIVlFFZnBmSUZnb0dFeHB3YWFrQ2ZoNA?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
