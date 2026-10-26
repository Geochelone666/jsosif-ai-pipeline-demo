# ACN Intelligence Report

- ticker: **ACN**
- Report as_of: **2026-10-25**
- Market data as_of: **2026-10-23**
- Quant sources: https://finance.yahoo.com/quote/ACN/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/ACN/key-statistics/
- AI analysis snapshot as_of: **2026-10-25**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-26T01:04:42.473503+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 22, 'rule': 5, 'ai': 8, 'unknown': 0, 'irrelevant': 9})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **0** exact headline/source/date matches; prior report **N/A** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 22 unique headlines; 10 named publishers; 0 exact duplicates; 22 HTTPS source links; largest publisher share 27.27%; oldest publication 2026-10-19

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 249.3700 |
| Return 1D (%) | -3.6214 |
| Return 1W (%) | 8.5728 |
| Return 1M (%) | 36.9717 |
| Return YTD (%) | -4.3793 |
| Return 1Y (%) | 2.6982 |
| Annualized volatility (%) | 49.3586 |
| Beta vs SPY | 0.0749 |
| Max drawdown (%) | -56.5068 |
| Sharpe (rf=0) | 0.3019 |
| Downside deviation (rf=0, %) | 34.3622 |
| Sortino (rf=0) | 0.4337 |
| Historical VaR 95% (1D, %) | 4.4016 |
| Historical ES 95% (1D, %) | 6.7690 |
| Correlation vs SPY | 0.0193 |
| Tracking error vs SPY (%) | 50.7386 |
| P/E (trailing) | 18.39 |
| P/B | 4.70 |
| EV/EBITDA | 11.14 |
| Revenue growth (%) | 6.20 |
| Forward P/E (estimate) | 15.70 |
| Gross margin (%) | 32.05 |
| Operating margin (%) | 17.83 |
| Return on equity (%) | 26.02 |
| Free cash flow yield (%) | 7.00 |
| MA50 | 194.5973 |
| Close vs MA50 (%) | 28.1467 |
| MA200 | 188.7917 |
| Close vs MA200 (%) | 32.0874 |
| RSI (14, Wilder) | 73.2038 |
| MACD (12,26) | 16.7446 |
| MACD signal (9) | 12.5479 |
| MACD histogram | 4.1967 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'ACN': 267, 'SPY': 267}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 249.3700 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -3.6214 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 8.5728 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 36.9717 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -4.3793 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 2.6982 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 49.3586 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 34.3622 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.4337 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.4016 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 6.7690 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.0193 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 50.7386 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.0749 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -56.5068 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.3019 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 15.6959 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 32.0500 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 17.8280 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 26.0250 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 7.0016 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 18.3901 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 73.2038 -> Overbought momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 4.1967 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 28.1467 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 32.0874 -> Clearly above the moving-average trend level.

## TAILWINDS

### Accenture PLC (ACN) Stock Up 7.7% and Still Undervalued -- GF Sc
- Summary: Accenture PLC (ACN) Stock Up 7.7% and Still Undervalued -- GF Sc
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxNYzN3b1o1cG85eDhLaTFlSWw1cTJWUXRoUU9iRnVldzBfbXhRQjBINHFiLTVDWXo5QUx4R1IyTU42NUJVVG9KWFNUX1h6TEJHMWhIMzZXWmE5SmtTZWdnRXdnZVJqQkN1cmZTUmRuNU90c1VjMWFlLUhqam5FTW91V1J0dzV1YXpBZXFuNXVLSnJVMlJZdEptR0xfQk5VYW9vT2N6V0NKSWM?oc=5>

### Accenture Stock Climbs 24% On A 9-Day Winning Streak
- Summary: Accenture Stock Climbs 24% On A 9-Day Winning Streak
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxNMTBKMDl3UUNqemQ4aFpqNU1QR3g1WTZlMjN4R2x4TE1UendCc09pYkxtV0RDdWVfd1p5M2g5QVhqMXExa0Y0U2w4T3Y2SFZTV0NtdGFBVGxiQlpoMkZ2bzhJcTFJdmxLWjlYVUJJLU5nQXVTbmpLMFFlMFE5OEtqVTFWSzVsOVY2SVVnYnRnY09xdkRXOHJjbXNFbWZCZGN0M2FTS1drQjRDaXliZEJMdQ?oc=5>

### Accenture Stock Rides A 10-Day Winning Streak To A 25% Gain
- Summary: Accenture Stock Rides A 10-Day Winning Streak To A 25% Gain
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxOT1QtRndiY2RLdnF5cDR6VG5nVU0wVy0tSGc2WjRrNWs5MWhuaUJVNlFJNWNwOUJCRXVjWEhKdElzQmN3UnZIT2JqNnQtS1lTdGpzbVB0aUpsZ29LMm94eURBb2VUdmRiVEdURUlwR3pxaW5xRkJvUXVUQUc2VGQ5U0xGTTMtMlBIWWxsYzJxOHNUWl9nVDh5Ty1MZjRCQnJTRWFocXc0WmgxdVE5Q3pRY1lGcFpxMTlESHc?oc=5>

### Accenture PLC (ACN) Shares Surge 3.2% -- What GF Score of 87 Tel
- Summary: Accenture PLC (ACN) Shares Surge 3.2% -- What GF Score of 87 Tel
- Date: 2026-10-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxQa0R6OF94QVlySHJIaGo5RkxWMF9XbWhfU0VrZXNycEpobS1hQkhLYmI5bk1YbVE3Qnh2X0hDc0llN1NEeVlRdGxpVGc5UTczQ2E0SGxpcnVwLUpHMFFKdGxZTHp0c2xFOWZSc1RkT0U2UjZMQ1BDNzk0QWIxUzltLXVLaTJlWWZNVUlRSkJEVVV5aUZ5NGpQaDc1ZnN2ZFgzWXlJbjhJZkc5cGlE?oc=5>

### Zacks Investment Ideas feature highlights: Accenture, Hasbro and MSCI
- Summary: Zacks highlights Accenture as a top investment idea, suggesting positive analyst sentiment.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxObXZIOGJENy1YVmZVZndNUUxRZ202WDdTQlNZbklPTEJYVkw3RGhTaENtRC1mQ2VCTU5UMld5NlJzcmhFcXdYb2hfYzN2clpYUzN4Rkg3QjZZeXZFQUVDNlFzWHdNNlcxdURoamVCWWttbjdTbXhTMklaMDNzWUlKcUQ0ZkVUdks1U09fTndmUVhfSlVWV1k5bS15Z2N5eGhGWUJmT1hRZENSQQ?oc=5>

### Accenture: 75% Total Return Since July, 23% More By December 2027 (NYSE:ACN)
- Summary: Accenture’s total return has risen 75% since July, with projections of an additional 23% by Dec 2027.
- Date: 2026-10-23 | Impact: medium | Horizon: long | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxPWkV3TXZFbXhsN3dBUnRYdmI2UWZmUkJNUm9sMmc2TEZzMXhMaEJfaFBqVjdSOWhBNUl6UVZXODMtb2JUblhyT19oY0RlV2ZRYm1JRUp3c1FoRThIR2pKcEpuREZtcWZGbjBrbG9oQXZ5bFNZN3Rodl9WUUlNMVlMSHBidVl6ZFM1ZENwU0NqYmJ5MVI2QjUxSk04a2txeDVCVEIyQmJrRk5Gam9UczMwTzNsQXdlMGI4cFE?oc=5>

### Accenture (ACN) Stock Still Seems Cheap Following Its 31% Rebound
- Summary: Accenture shares rebound 31%, viewed as undervalued, indicating positive market sentiment.
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxPNS1jOFAxdHJsZndDRUlES1R5OWY3bFJ4eFRkMUV4SHVlVkVoWDU3ZEtWcldCM0puTDZvd2NOMHlidEMzVkZYQkxSRkUtV1prcDg5bk1saXRMNzItWTI4RUtQWm9mcVVyMTZfX0VfV3BiMGZWSFJzUGZNbndRMFBzUk5sMFFRSVBZMktFeTlqMTE1Z0EwZ1BpOVdMRFZ3cTFFdy1aQWpXcVk1S083aUoxSWZMZjN5VTl6Q1RpUURId2ZsMEnSAcgBQVVfeXFMTkN2T2J4cnJQZ0hRMmgyZy16ZUxDWG5OUU50T3JFS0ZzWEktVlFIR2Y1dFlCZDlVV2pxVnlRZjY0RXN3OXFWUDE2X21kM2NoU3k2MW1MWkFPOWpwMTIzd1V3YXU5QkVYdm1WQWVyeDZHQ0hyXzdJdE11MG1aNjFZaF9Lbmc1NUVsMTRZMXBCYW1HQ1dRc2Z5ZUhWRDV0U05DTFBLYm5kb2RWMWVvQTF4d0dtZ01pT2tUcS1EMnJla2FIcGVGU09rbWQ?oc=5>

## HEADWINDS

### Accenture downgraded to Neutral at Baird as risk-reward comes into balance (ACN:NYSE)
- Summary: Accenture downgraded to Neutral at Baird as risk-reward comes into balance (ACN:NYSE)
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxQQkY1V0RyTVRGcXhmbGVWU0Nqb2loekNaUWhNek5BeDZIQVNqTXlqN25MVDFzOVZNb2M3UmtTMnhBV1ZEY0p5c3liazloMzlWYmd6NnY3cUN2VXhYUmRwOF9PU3FrbW1UMldSN3lDWFpMT3laSjNyNElfRUU3YjlWMUxpSkx3cFJqSUtFUXQzWnFkZFItZkVvdkRPY1ZyOFlJOWw1cmQ3aTNUX2VpTDN6OHJ3?oc=5>

### ISRG, NFLX, ACN Stocks Slide Before The Bell: Why Intuitive Surgical, Netflix And Accenture Are Heading Lower
- Summary: Accenture shares fell pre‑market, indicating a short‑term negative market move.
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi-AFBVV95cUxOMFhIdWZXalhBQ1FaTDhzSGRwRHdoWGZTR0RSenNLYkcwTmNXSUl3RWRjaGppNXFXN2VaSmVxVDlhUlE4OXY0UE5CQWtsdHkyYl9halQ1VjFFS0ZjNFpTTWJtMGE1OGRRd0FSYTB5cGd4eXUtSnJRNXE5QzQ0X1NQNE9FRjlxTkM4XzhrRWkzb0VOUzI5TlpNR2Fhd1huWDFBRkNPYkdzRnlkb1dTQURkWnNDQUY2YWMzVm1LU2pDRC1aM1NadTFHVThraGhlUFFwRnhXUi04SUZsQlU1Vm5SUXlmcVIxeF9WQWFrckNXWWctTldhcnVlRg?oc=5>

### Accenture PLC Stock (ACN) Opened Down by 4.04% on Oct 23: What Signal Does It Send?
- Summary: Opening decline of 4.04% signals short‑term market weakness for Accenture.
- Date: 2026-10-23 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxPS2VsM01FdzJrTVZmc2RZNDVMVG9xa0pKa2dqNXN0Vm05YVRlN0cxTEE5WmR3a1JJZU9odjljTV9FX2FtaF9CMm5RemZNSnBCbUtYemhZQ0R1XzkxZG90RFZjdl82SXU4aEpnOG1lcEJRNG9FN0pENy1zTHVGMDkyclV4a1FHTVlFTEE?oc=5>

## CATALYSTS

No items in this run

## RISKS

### Accenture (ACN) Co-CEO Asia Pacific Ryoji Sekido Sells 5,844 Sha
- Summary: Insider sale by Co‑CEO raises concerns about internal confidence.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxNTFc1VkFaR0tHdExqaFZLdGVzTFNVRkJtV1pfT2VoSVpMM3UydktGbUxpMmRFZmhaYVh0YXB5Y3dybmg5QTZMOEtMVS1HY21xYzRKZ1pvd0o3blA3eFdUMUNMaVJMaDVqeHZYVGFZdXM1M1BZV3RnZ2hxUEN2M1kzbDFoMDlHRWp3eVlCUTVDZGlQTVRJU2RqY0NvSWxSaHE1RlQ2VQ?oc=5>

### Baird Downgrades Accenture (ACN) to Neutral After Nearly 100% Ra
- Summary: Analyst downgrade to neutral signals potential valuation concerns.
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxNcy1UbGEwdzdoU3RGWXFwT1MxN0dOSjZQaFdsYnczZ1d5Q084bGE5WXllSEp1ZXR4c21JMGtXWVl4NDZxZGxJdlhSampJT0lnOElJQzZ3WGZRWWR0OGRjUU11VURHaXJEU1ZFYnVzZGg1dG44V0JXV0JjUmdoeVROTnVGQlgweU9HalJYdG55aWR0WWhYUTUtRzVkTUxaQm9ESEFyTkVR?oc=5>

### Accenture considers selling China business for up to $1.5B - report (ACN:NYSE)
- Summary: Potential divestiture of China unit could reshape business focus.
- Date: 2026-10-19 | Impact: medium | Horizon: medium | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxQcDkzMVJfTzFodkpVNThKVHBiTm9zakxQZnByVXd4VWczR2I0YVdHSUhvSnpYSWxmNHR1NGFJdlhHS0ItWkpXYjdmTU40NUlSekVZZnJfSXFyWmNoRWdFU3Jja0JLdDV5aWw0MHQyMUtOZzZ6Q3dBX3dPUk5uTTdZektBbENoSzNScHhQcTFfZTdlTjAxQ1l3ZVMySWxNenl0am91UHZB?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **ACN** | **18.39** | **4.70** | **11.14** | **6.20** | **152,599,986,176.00 USD** | **2.70** |
| IBM | 21.63 | 6.74 | 17.82 | 4.70 | 239,644,835,840.00 USD | -8.72 |
| CTSH | 15.17 | 2.20 | 8.13 | 4.50 | 31,774,334,976.00 USD | 6.03 |
| INFY | 15.25 | 9.68 | 21.50 | 1.40 | 50,022,150,144.00 USD | -26.94 |

Peers fetched as_of: 2026-10-25; ACN reuses existing data (market data as_of: 2026-10-23); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-01
- Next expected earnings: 2026-12-17 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-25

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-K
- Filing date: 2026-10-16
- Revenue (latest available single quarter): 18,679,110,000.00 USD; period 2026-06-01/2026-08-31; fiscal year/reporting period 2026/FY
- Net income (latest available single quarter): 1,991,267,000.00 USD; period 2026-06-01/2026-08-31; fiscal year/reporting period 2026/FY
- SEC link: https://www.sec.gov/Archives/edgar/data/1467373/000146737326000049/acn-20260831.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiqAFBVV95cUxNYzN3b1o1cG85eDhLaTFlSWw1cTJWUXRoUU9iRnVldzBfbXhRQjBINHFiLTVDWXo5QUx4R1IyTU42NUJVVG9KWFNUX1h6TEJHMWhIMzZXWmE5SmtTZWdnRXdnZVJqQkN1cmZTUmRuNU90c1VjMWFlLUhqam5FTW91V1J0dzV1YXpBZXFuNXVLSnJVMlJZdEptR0xfQk5VYW9vT2N6V0NKSWM?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxNMTBKMDl3UUNqemQ4aFpqNU1QR3g1WTZlMjN4R2x4TE1UendCc09pYkxtV0RDdWVfd1p5M2g5QVhqMXExa0Y0U2w4T3Y2SFZTV0NtdGFBVGxiQlpoMkZ2bzhJcTFJdmxLWjlYVUJJLU5nQXVTbmpLMFFlMFE5OEtqVTFWSzVsOVY2SVVnYnRnY09xdkRXOHJjbXNFbWZCZGN0M2FTS1drQjRDaXliZEJMdQ?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxOT1QtRndiY2RLdnF5cDR6VG5nVU0wVy0tSGc2WjRrNWs5MWhuaUJVNlFJNWNwOUJCRXVjWEhKdElzQmN3UnZIT2JqNnQtS1lTdGpzbVB0aUpsZ29LMm94eURBb2VUdmRiVEdURUlwR3pxaW5xRkJvUXVUQUc2VGQ5U0xGTTMtMlBIWWxsYzJxOHNUWl9nVDh5Ty1MZjRCQnJTRWFocXc0WmgxdVE5Q3pRY1lGcFpxMTlESHc?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxQa0R6OF94QVlySHJIaGo5RkxWMF9XbWhfU0VrZXNycEpobS1hQkhLYmI5bk1YbVE3Qnh2X0hDc0llN1NEeVlRdGxpVGc5UTczQ2E0SGxpcnVwLUpHMFFKdGxZTHp0c2xFOWZSc1RkT0U2UjZMQ1BDNzk0QWIxUzltLXVLaTJlWWZNVUlRSkJEVVV5aUZ5NGpQaDc1ZnN2ZFgzWXlJbjhJZkc5cGlE?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxObXZIOGJENy1YVmZVZndNUUxRZ202WDdTQlNZbklPTEJYVkw3RGhTaENtRC1mQ2VCTU5UMld5NlJzcmhFcXdYb2hfYzN2clpYUzN4Rkg3QjZZeXZFQUVDNlFzWHdNNlcxdURoamVCWWttbjdTbXhTMklaMDNzWUlKcUQ0ZkVUdks1U09fTndmUVhfSlVWV1k5bS15Z2N5eGhGWUJmT1hRZENSQQ?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxPWkV3TXZFbXhsN3dBUnRYdmI2UWZmUkJNUm9sMmc2TEZzMXhMaEJfaFBqVjdSOWhBNUl6UVZXODMtb2JUblhyT19oY0RlV2ZRYm1JRUp3c1FoRThIR2pKcEpuREZtcWZGbjBrbG9oQXZ5bFNZN3Rodl9WUUlNMVlMSHBidVl6ZFM1ZENwU0NqYmJ5MVI2QjUxSk04a2txeDVCVEIyQmJrRk5Gam9UczMwTzNsQXdlMGI4cFE?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxPNS1jOFAxdHJsZndDRUlES1R5OWY3bFJ4eFRkMUV4SHVlVkVoWDU3ZEtWcldCM0puTDZvd2NOMHlidEMzVkZYQkxSRkUtV1prcDg5bk1saXRMNzItWTI4RUtQWm9mcVVyMTZfX0VfV3BiMGZWSFJzUGZNbndRMFBzUk5sMFFRSVBZMktFeTlqMTE1Z0EwZ1BpOVdMRFZ3cTFFdy1aQWpXcVk1S083aUoxSWZMZjN5VTl6Q1RpUURId2ZsMEnSAcgBQVVfeXFMTkN2T2J4cnJQZ0hRMmgyZy16ZUxDWG5OUU50T3JFS0ZzWEktVlFIR2Y1dFlCZDlVV2pxVnlRZjY0RXN3OXFWUDE2X21kM2NoU3k2MW1MWkFPOWpwMTIzd1V3YXU5QkVYdm1WQWVyeDZHQ0hyXzdJdE11MG1aNjFZaF9Lbmc1NUVsMTRZMXBCYW1HQ1dRc2Z5ZUhWRDV0U05DTFBLYm5kb2RWMWVvQTF4d0dtZ01pT2tUcS1EMnJla2FIcGVGU09rbWQ?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxQQkY1V0RyTVRGcXhmbGVWU0Nqb2loekNaUWhNek5BeDZIQVNqTXlqN25MVDFzOVZNb2M3UmtTMnhBV1ZEY0p5c3liazloMzlWYmd6NnY3cUN2VXhYUmRwOF9PU3FrbW1UMldSN3lDWFpMT3laSjNyNElfRUU3YjlWMUxpSkx3cFJqSUtFUXQzWnFkZFItZkVvdkRPY1ZyOFlJOWw1cmQ3aTNUX2VpTDN6OHJ3?oc=5
- https://news.google.com/rss/articles/CBMi-AFBVV95cUxOMFhIdWZXalhBQ1FaTDhzSGRwRHdoWGZTR0RSenNLYkcwTmNXSUl3RWRjaGppNXFXN2VaSmVxVDlhUlE4OXY0UE5CQWtsdHkyYl9halQ1VjFFS0ZjNFpTTWJtMGE1OGRRd0FSYTB5cGd4eXUtSnJRNXE5QzQ0X1NQNE9FRjlxTkM4XzhrRWkzb0VOUzI5TlpNR2Fhd1huWDFBRkNPYkdzRnlkb1dTQURkWnNDQUY2YWMzVm1LU2pDRC1aM1NadTFHVThraGhlUFFwRnhXUi04SUZsQlU1Vm5SUXlmcVIxeF9WQWFrckNXWWctTldhcnVlRg?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxPS2VsM01FdzJrTVZmc2RZNDVMVG9xa0pKa2dqNXN0Vm05YVRlN0cxTEE5WmR3a1JJZU9odjljTV9FX2FtaF9CMm5RemZNSnBCbUtYemhZQ0R1XzkxZG90RFZjdl82SXU4aEpnOG1lcEJRNG9FN0pENy1zTHVGMDkyclV4a1FHTVlFTEE?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxNTFc1VkFaR0tHdExqaFZLdGVzTFNVRkJtV1pfT2VoSVpMM3UydktGbUxpMmRFZmhaYVh0YXB5Y3dybmg5QTZMOEtMVS1HY21xYzRKZ1pvd0o3blA3eFdUMUNMaVJMaDVqeHZYVGFZdXM1M1BZV3RnZ2hxUEN2M1kzbDFoMDlHRWp3eVlCUTVDZGlQTVRJU2RqY0NvSWxSaHE1RlQ2VQ?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxNcy1UbGEwdzdoU3RGWXFwT1MxN0dOSjZQaFdsYnczZ1d5Q084bGE5WXllSEp1ZXR4c21JMGtXWVl4NDZxZGxJdlhSampJT0lnOElJQzZ3WGZRWWR0OGRjUU11VURHaXJEU1ZFYnVzZGg1dG44V0JXV0JjUmdoeVROTnVGQlgweU9HalJYdG55aWR0WWhYUTUtRzVkTUxaQm9ESEFyTkVR?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxQcDkzMVJfTzFodkpVNThKVHBiTm9zakxQZnByVXd4VWczR2I0YVdHSUhvSnpYSWxmNHR1NGFJdlhHS0ItWkpXYjdmTU40NUlSekVZZnJfSXFyWmNoRWdFU3Jja0JLdDV5aWw0MHQyMUtOZzZ6Q3dBX3dPUk5uTTdZektBbENoSzNScHhQcTFfZTdlTjAxQ1l3ZVMySWxNenl0am91UHZB?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
