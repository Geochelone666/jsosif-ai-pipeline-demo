# ACN Intelligence Report

- ticker: **ACN**
- Report as_of: **2026-11-02**
- Market data as_of: **2026-11-02**
- Quant sources: https://finance.yahoo.com/quote/ACN/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/ACN/key-statistics/
- AI analysis snapshot as_of: **2026-11-02**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-03T05:30:45.739877+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 18, 'rule': 2, 'ai': 9, 'unknown': 0, 'irrelevant': 7})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **12** exact headline/source/date matches; prior report **20261102T041627Z-c84a7052/ACN** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'low_uncalibrated_model_confidence': 2}
- RSS source audit (metadata only, not article fact-checking): 18 unique headlines; 10 named publishers; 0 exact duplicates; 18 HTTPS source links; largest publisher share 27.78%; oldest publication 2026-10-27

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 260.9400 |
| Return 1D (%) | 1.0455 |
| Return 1W (%) | 5.5454 |
| Return 1M (%) | 32.2440 |
| Return YTD (%) | 0.0572 |
| Return 1Y (%) | 7.3385 |
| Annualized volatility (%) | 49.9698 |
| Beta vs SPY | 0.0036 |
| Max drawdown (%) | -56.5068 |
| Sharpe (rf=0) | 0.4071 |
| Downside deviation (rf=0, %) | 34.7006 |
| Sortino (rf=0) | 0.5863 |
| Historical VaR 95% (1D, %) | 4.6071 |
| Historical ES 95% (1D, %) | 6.8005 |
| Correlation vs SPY | 0.0009 |
| Tracking error vs SPY (%) | 51.5772 |
| P/E (trailing) | 19.24 |
| P/B | 4.92 |
| EV/EBITDA | 11.65 |
| Revenue growth (%) | 6.20 |
| Forward P/E (estimate) | 16.42 |
| Gross margin (%) | 32.05 |
| Operating margin (%) | 17.83 |
| Return on equity (%) | 26.02 |
| Free cash flow yield (%) | 6.69 |
| MA50 | 203.2193 |
| Close vs MA50 (%) | 28.4032 |
| MA200 | 188.0073 |
| Close vs MA200 (%) | 38.7925 |
| RSI (14, Wilder) | 71.4569 |
| MACD (12,26) | 16.3574 |
| MACD signal (9) | 15.0329 |
| MACD histogram | 1.3245 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'ACN': 273, 'SPY': 273}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 260.9400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.0455 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 5.5454 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 32.2440 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 0.0572 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 7.3385 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 49.9698 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 34.7006 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.5863 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.6071 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 6.8005 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.0009 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 51.5772 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.0036 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -56.5068 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.4071 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 16.4239 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 32.0500 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 17.8280 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 26.0250 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 6.6912 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 19.2434 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 71.4569 -> Overbought momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 1.3245 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 28.4032 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 38.7925 -> Clearly above the moving-average trend level.

## TAILWINDS

### Accenture PLC (ACN) Shares Surge 4.5% -- What GF Score of 91 Tel
- Summary: Accenture PLC (ACN) Shares Surge 4.5% -- What GF Score of 91 Tel
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxNZlRfSHNlSTlBaWhBdkdGUjBGTmxSR1dxaExZclpvNEVuWDdKZDZmbmdyQ1U4VWQtVkFTSXdELWdSQmljQVItSmVLd0V0aTFnMTEyck9jVzBFUXBqV2s2eTZzWmhUOXdLNWM5OU8yME5sa2xDZDV3aEdNTmFObHA4TmMtV1JVN0luUFZQbFp2akk5LWZTVVU1UFg5S3R0dHp3czlfb19YM1VmWEps?oc=5>

### Investors Heavily Search Accenture PLC (ACN): Here is What You Need to Know
- Summary: High search volume indicates growing investor interest in Accenture, suggesting potential market attention and possible valuation reconsideration.
- Date: 2026-10-28 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxQWDdRZmdQeFp2NHRYRGZja1duVmNsYm54WlN5bWdMdEsyZUQ4VFFpN3NOR0toUDVFTkg2MEFpWWltb3EzUkw0LXpZbnR5SkcyaGJWWkR6RDJzcUNWdjJFcXJ1aERieWxSc2d5bmNuYzVORWtNNHJvME9MMUx6Vl9BTW1fVk1nMFY2bjh0ZjJOVTNLUjl3U2psdV9MTU1ZRTdwZnFKRHNn?oc=5>

### Accenture PLC Stock (ACN) Moved Up by 4.43% on Oct 28: A Full Analysis
- Summary: Positive price movement indicates favorable market sentiment.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxNNXk1MVNuS3ktZW9oOUFuazFHZkgxU0h6MWhjZ213aGN4d01RZFZJMkY5N3RSTDZXdUVIY1dzYS1LQ3pMeGFvUmYwYjBaWWEyanprTHBReU4ycTI2a2lITlhuOW5sLTRjbzRXRjRRWDJTSW9VaEhYZ2x4ejQ2Z0h0QkRyMFFiaGNFLVE?oc=5>

### Accenture PLC Stock (ACN) Closed Up by 4.46% on Oct 30: Facts Behind the Movement
- Summary: Accenture shares closed 4.46% higher on Oct 30, indicating a positive price movement.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxOT1ZmaHVvYVhiUHNncFhEcTZSUGxCeERXZXlSbHNOR2FZNkFCOFJFU2o2eGE1b0FVczJfWHBTR012bndna2JOYTFQSzMxTHFQUXFjekVvWmt1QU9SNGNsa25rbUxrMjNwZGU0NTIyVmhkRFpwUW1PNC1UR1VrRlBibHdvV2tqaGFoMnc?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Accenture (ACN) Stock Looks Fairly Valued After Fresh AI Launch News
- Summary: Accenture (ACN) Stock Looks Fairly Valued After Fresh AI Launch News
- Date: 2026-10-31 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxOSVVTUVJRenRtUXpyRThiN3A5X0NiZnUyTHFvZjRaNFdPa3BpMFp1M0U5cVh1Q0o4bWRKSk1pWXhkWVZGN1lCWnJSeXZuWlVaQ1V3eXhNbUxubnVJMWJzNHphZVpxMGpvQ1JOQXBFSmQ0aXZDRkNua1NTRVNiZnNiamFWR2hVaVVXQ2h4VkladENSa1hncWg3X3lCekkxZw?oc=5>

### Accenture (ACN) Increases Despite Market Slip: Here's What You Need to Know
- Summary: Accenture shares rise amid broader market decline, indicating resilience and potential upside.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxOTHpaZ0RYVTJfbm5Hd3JueTYwNDFYZm1pLXpyRExoek5uaTZESUlNSWJPSkc1Mm5tSnd3blBRWjlLSHZqdFdUMWxOQU15dE03SmdPdmFSZ2tSczgxUjJoREZGUW91dG5OZHJlT3FmUDFmVmFQY3dfTDhqZWNrcGFIam9NNi1hcUVJYmRWNThTZWlaLWFfbWRnekYtMmNzc2piQWEyOGhn?oc=5>

### Accenture (ACN) vs. CTSH and IBM: Can Valuation Recovery and Dividend Growth Drive the Next Upside?
- Summary: Analyst compares Accenture's valuation recovery and dividend growth potential against competitors.
- Date: 2026-10-27 | Impact: low | Horizon: medium | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxQN29ZdmJ3OFdfTXRLVHNvWnVCa3pCWE5HdlJBRkQ1cUlRcHNSOENSZmg1a2Y1SEhuRDNqdnU0RDA1RTNTZUpWal9xTHJhZVMtdkhDT0wycVI4QjJQX19vMzBHcTNFYmF1NEt4NG1aR2kyRXBmcDVnZHdibGNPaTV5VXAyN0hSLUVWU1llT2x0REpLbEFR?oc=5>

### Accenture CEO Julie Sweet Buys $3 Million in Stock as Director Also Purchases Shares
- Summary: CEO Julie Sweet purchases $3M of ACN shares, indicating confidence in company value.
- Date: 2026-10-28 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxPMWJ0ZDVWdC1VQUZNOVlDV0d5Ti02cU5tTHBjQkdsdUtNSF9tNUJBZkJrMk1kLTRHR3RnU0dmeG1OYk9UUTlGamtwTmhlR0NWN3JrbXhYdmFKOGlxY1dBS1EwNlp0Rmk3R3Vxck1WZnlCZmpFa0pKTDN4OG54QWtDRUE0TlM1Nmp0cHVtRUoyOTdWSjcxaVowT3BSMUZacF9XbW45TEVtUEplVHZEMVdPcTBOYjVpZnk4d2o0?oc=5>

### Accenture PLC Stock (ACN) Moved Down by 4.41% on Oct 27: Key Drivers Unveiled
- Summary: Accenture shares fell 4.41% on Oct 27 due to identified key drivers.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxNT0NCZ21GY2RlNUUyVkVnNEpxbzJJZlFXa0x1RllfcXV4UzlIaGllRlVaa0pJaS1Zb2NPcnBLSWtRdm53d3cySU14Si1tRXVlRmtPNTQwMW5kU2UzeldwMFlJQVpIRkF2MXZ4VE40TjZlcnpraEotWG1uYnhKX0tESkpRYkhxVW5NWUE?oc=5>

### Did Physical AI Safety Suite Just Shift Accenture's (ACN) Investment Narrative?
- Summary: Accenture's new Physical AI Safety Suite may alter its investment focus, signaling a strategic shift toward AI safety solutions.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxNbF9fQnZzV0Y4RmhXUmFxdDA0M0FUMkt4akZOb1g0WHcwNndGcDEyR2tkWDhfRnQ3WjZYeXhyZEY3VHRFUVZyLUVLMWY0QWVWSmZKQ3hQWjRKVThWNHBhLUlSX2VjczlWMkdBdmZWM3hpVU9qOW5EckRzTEpqX193QnF0Tm5wNnRyUzRPUk9BNkhQUzk0M0ZBMmtCdXloMkNYNVJqcExkOVlKWDI4U3BVU3ZjSTlUeUxHZGhWSjN0cktkRFnSAcgBQVVfeXFMTnBRTTdiNDlBSVdJRTNWRS1kSFVLMkVmOFVTY01BcDZadkpGYU80bERXNEd0X2UwOUtCYU10d1Y3YWcxeXcyQS1SMVhSanA4cVhKTzVHamh0N0h6SnEwTWRyTmZ5Ty16Y0R2eWVjLVJKZEd3dzRtbndXTXk3NGJOSlhBSEJhbHpzR2RyMlRIdzQyNEpHWTRaQkRpUkxVVy1KaDBSSzd4RkpvUS1tZ0lhN3luQTNTRERwUGJhUjJUVGdTOVlhQVgtdGE?oc=5>

### Is Accenture (NYSE:ACN) Proving AI Demand With Record Large Bookings?
- Summary: Accenture reports record large AI bookings, indicating strong demand and potential revenue growth.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxQdUFOYzNQX293cDlSdkxMTzE0S0J1SmlPdFZ3UEduNnZUNmFGdWxEVVlkUHpvajNJMVJqakVId0l0YkxQR0tvX25Ib0h6XzI4RU5QekZJX1ZHSDdCQ2pNUE80dkpxX3pJSUJvay1vMnNpT3d5ZExVTjNCVEJfUXZRcGZqM0h1RVZZcXlDalRNTWRlMVRGWlRZaS0ycFJGc3Q5TWRRRU4zdkhWVGNSLVE?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **ACN** | **19.24** | **4.92** | **11.65** | **6.20** | **159,680,167,936.00 USD** | **7.34** |
| IBM | 21.55 | 6.72 | 17.76 | 4.70 | 238,652,456,960.00 USD | -15.72 |
| CTSH | 11.88 | 1.98 | 7.23 | 4.60 | 29,097,209,856.00 USD | -8.67 |
| INFY | 15.47 | 9.82 | 21.82 | 1.40 | 50,751,217,664.00 USD | -22.75 |

Peers fetched as_of: 2026-11-02; ACN reuses existing data (market data as_of: 2026-11-02); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-01
- Next expected earnings: 2026-12-17 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-02

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
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

- https://news.google.com/rss/articles/CBMirAFBVV95cUxNZlRfSHNlSTlBaWhBdkdGUjBGTmxSR1dxaExZclpvNEVuWDdKZDZmbmdyQ1U4VWQtVkFTSXdELWdSQmljQVItSmVLd0V0aTFnMTEyck9jVzBFUXBqV2s2eTZzWmhUOXdLNWM5OU8yME5sa2xDZDV3aEdNTmFObHA4TmMtV1JVN0luUFZQbFp2akk5LWZTVVU1UFg5S3R0dHp3czlfb19YM1VmWEps?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxQWDdRZmdQeFp2NHRYRGZja1duVmNsYm54WlN5bWdMdEsyZUQ4VFFpN3NOR0toUDVFTkg2MEFpWWltb3EzUkw0LXpZbnR5SkcyaGJWWkR6RDJzcUNWdjJFcXJ1aERieWxSc2d5bmNuYzVORWtNNHJvME9MMUx6Vl9BTW1fVk1nMFY2bjh0ZjJOVTNLUjl3U2psdV9MTU1ZRTdwZnFKRHNn?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxNNXk1MVNuS3ktZW9oOUFuazFHZkgxU0h6MWhjZ213aGN4d01RZFZJMkY5N3RSTDZXdUVIY1dzYS1LQ3pMeGFvUmYwYjBaWWEyanprTHBReU4ycTI2a2lITlhuOW5sLTRjbzRXRjRRWDJTSW9VaEhYZ2x4ejQ2Z0h0QkRyMFFiaGNFLVE?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxOT1ZmaHVvYVhiUHNncFhEcTZSUGxCeERXZXlSbHNOR2FZNkFCOFJFU2o2eGE1b0FVczJfWHBTR012bndna2JOYTFQSzMxTHFQUXFjekVvWmt1QU9SNGNsa25rbUxrMjNwZGU0NTIyVmhkRFpwUW1PNC1UR1VrRlBibHdvV2tqaGFoMnc?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxOSVVTUVJRenRtUXpyRThiN3A5X0NiZnUyTHFvZjRaNFdPa3BpMFp1M0U5cVh1Q0o4bWRKSk1pWXhkWVZGN1lCWnJSeXZuWlVaQ1V3eXhNbUxubnVJMWJzNHphZVpxMGpvQ1JOQXBFSmQ0aXZDRkNua1NTRVNiZnNiamFWR2hVaVVXQ2h4VkladENSa1hncWg3X3lCekkxZw?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxOTHpaZ0RYVTJfbm5Hd3JueTYwNDFYZm1pLXpyRExoek5uaTZESUlNSWJPSkc1Mm5tSnd3blBRWjlLSHZqdFdUMWxOQU15dE03SmdPdmFSZ2tSczgxUjJoREZGUW91dG5OZHJlT3FmUDFmVmFQY3dfTDhqZWNrcGFIam9NNi1hcUVJYmRWNThTZWlaLWFfbWRnekYtMmNzc2piQWEyOGhn?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxQN29ZdmJ3OFdfTXRLVHNvWnVCa3pCWE5HdlJBRkQ1cUlRcHNSOENSZmg1a2Y1SEhuRDNqdnU0RDA1RTNTZUpWal9xTHJhZVMtdkhDT0wycVI4QjJQX19vMzBHcTNFYmF1NEt4NG1aR2kyRXBmcDVnZHdibGNPaTV5VXAyN0hSLUVWU1llT2x0REpLbEFR?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxPMWJ0ZDVWdC1VQUZNOVlDV0d5Ti02cU5tTHBjQkdsdUtNSF9tNUJBZkJrMk1kLTRHR3RnU0dmeG1OYk9UUTlGamtwTmhlR0NWN3JrbXhYdmFKOGlxY1dBS1EwNlp0Rmk3R3Vxck1WZnlCZmpFa0pKTDN4OG54QWtDRUE0TlM1Nmp0cHVtRUoyOTdWSjcxaVowT3BSMUZacF9XbW45TEVtUEplVHZEMVdPcTBOYjVpZnk4d2o0?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxNT0NCZ21GY2RlNUUyVkVnNEpxbzJJZlFXa0x1RllfcXV4UzlIaGllRlVaa0pJaS1Zb2NPcnBLSWtRdm53d3cySU14Si1tRXVlRmtPNTQwMW5kU2UzeldwMFlJQVpIRkF2MXZ4VE40TjZlcnpraEotWG1uYnhKX0tESkpRYkhxVW5NWUE?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxNbF9fQnZzV0Y4RmhXUmFxdDA0M0FUMkt4akZOb1g0WHcwNndGcDEyR2tkWDhfRnQ3WjZYeXhyZEY3VHRFUVZyLUVLMWY0QWVWSmZKQ3hQWjRKVThWNHBhLUlSX2VjczlWMkdBdmZWM3hpVU9qOW5EckRzTEpqX193QnF0Tm5wNnRyUzRPUk9BNkhQUzk0M0ZBMmtCdXloMkNYNVJqcExkOVlKWDI4U3BVU3ZjSTlUeUxHZGhWSjN0cktkRFnSAcgBQVVfeXFMTnBRTTdiNDlBSVdJRTNWRS1kSFVLMkVmOFVTY01BcDZadkpGYU80bERXNEd0X2UwOUtCYU10d1Y3YWcxeXcyQS1SMVhSanA4cVhKTzVHamh0N0h6SnEwTWRyTmZ5Ty16Y0R2eWVjLVJKZEd3dzRtbndXTXk3NGJOSlhBSEJhbHpzR2RyMlRIdzQyNEpHWTRaQkRpUkxVVy1KaDBSSzd4RkpvUS1tZ0lhN3luQTNTRERwUGJhUjJUVGdTOVlhQVgtdGE?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxQdUFOYzNQX293cDlSdkxMTzE0S0J1SmlPdFZ3UEduNnZUNmFGdWxEVVlkUHpvajNJMVJqakVId0l0YkxQR0tvX25Ib0h6XzI4RU5QekZJX1ZHSDdCQ2pNUE80dkpxX3pJSUJvay1vMnNpT3d5ZExVTjNCVEJfUXZRcGZqM0h1RVZZcXlDalRNTWRlMVRGWlRZaS0ycFJGc3Q5TWRRRU4zdkhWVGNSLVE?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
