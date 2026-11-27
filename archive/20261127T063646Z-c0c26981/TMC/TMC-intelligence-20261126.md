# TMC Intelligence Report

- ticker: **TMC**
- Report as_of: **2026-11-26**
- Market data as_of: **2026-11-25**
- Quant sources: https://finance.yahoo.com/quote/TMC/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/TMC/key-statistics/
- AI analysis snapshot as_of: **2026-11-26**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-27T06:40:43.908650+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 5, 'rule': 4, 'ai': 0, 'unknown': 0, 'irrelevant': 1})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **0** exact headline/source/date matches; prior report **N/A** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 5 unique headlines; 3 named publishers; 1 exact duplicates; 5 HTTPS source links; largest publisher share 60.0%; oldest publication 2026-11-20

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 1.9400 |
| Return 1D (%) | 18.2927 |
| Return 1W (%) | 12.1387 |
| Return 1M (%) | -20.1646 |
| Return YTD (%) | -68.5575 |
| Return 1Y (%) | -64.2726 |
| Annualized volatility (%) | 96.9991 |
| Beta vs SPY | 3.3278 |
| Max drawdown (%) | -83.8983 |
| Sharpe (rf=0) | -0.5876 |
| Downside deviation (rf=0, %) | 65.0220 |
| Sortino (rf=0) | -0.8765 |
| Historical VaR 95% (1D, %) | 9.3843 |
| Historical ES 95% (1D, %) | 12.0481 |
| Correlation vs SPY | 0.5122 |
| Tracking error vs SPY (%) | 90.2670 |
| P/E (trailing) | N/A |
| P/B | -19.60 |
| EV/EBITDA | -4.24 |
| Revenue growth (%) | N/A |
| Forward P/E (estimate) | N/A |
| Gross margin (%) | 0.00 |
| Operating margin (%) | 0.00 |
| Return on equity (%) | N/A |
| Free cash flow yield (%) | 0.46 |
| MA50 | 2.8414 |
| Close vs MA50 (%) | -31.7238 |
| MA200 | 4.4264 |
| Close vs MA200 (%) | -56.1723 |
| RSI (14, Wilder) | 41.0484 |
| MACD (12,26) | -0.3212 |
| MACD signal (9) | -0.3163 |
| MACD histogram | -0.0049 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'TMC': 290, 'SPY': 290}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 1.9400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 18.2927 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 12.1387 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -20.1646 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -68.5575 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -64.2726 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 96.9991 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 65.0220 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.8765 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 9.3843 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 12.0481 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5122 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 90.2670 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 3.3278 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -83.8983 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.5876 -> Negative risk-adjusted return.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 0.0000 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 0.0000 -> No interpretation rule is available for this metric.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 0.4573 -> No interpretation rule is available for this metric.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 41.0484 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.0049 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -31.7238 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -56.1723 -> Clearly below the moving-average trend level.

## TAILWINDS

### The Metals Company Jumps 12% With Mining Shares
- Summary: The Metals Company Jumps 12% With Mining Shares
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihAFBVV95cUxOTEFfRTFzUERGeTM0UmJPUUh1czZndHM2czhWNEZZTFVaQUpteGdLOW9aWHNGZU5HVDlXV2FXRUpEQTJfUUNfTkFwYjhRZmJXZjRKODJHSXRmSWUtWTZ6dTVJdm00d2tnQlBlUGtrVEtFaFNpZWswT2lpODRERXJfYno4RlQ?oc=5>

### The Metals Company Rises 8% Today
- Summary: The Metals Company Rises 8% Today
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihAFBVV95cUxNWTJzMGR2c29XVm9zakxaeDJ4bnI2WUZrSUcwRGJhd3k4YU9MdXNsVzdfeUVJdEZCWnJUTXZtVGV0WFNvVzRBOFZYZ1ExM2JKTlJCN215SmFmRFZlSWRFSjF6TElWbTRYd2Yzam1pOWEza1VOeU5sLURzVGlEdmFmeVpVSnY?oc=5>

### TMC (TMC) Stock Is Up 14.3% Today Without Company News
- Summary: TMC (TMC) Stock Is Up 14.3% Today Without Company News
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxOU2dpbjJZRG02aF8yMmZlaFV1cm9FMlY5ME8tQ0ROMHMxN0VMRDRqSkw2bFJOX2V6NFNHZ3lYd2swd3kxbHZ6OTVVWjA2TDNtT05Sb0Vwd1VfUVZXeTRfOGtReDRSU01CaWJ0bzFuN29veFNNWDI1cko2UHM4c1dfamU1U2pvNTBVaVJxVm5LM3g1dHc?oc=5>

## HEADWINDS

### The Metals Company Falls 7% As Rate Fears Hit Markets
- Summary: The Metals Company Falls 7% As Rate Fears Hit Markets
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihAFBVV95cUxPVDY4NElpZmZDandQYmsyb1phSFJLOHZHYVpXMlVaOHRoMktDN0pYMG12REY1dEVSRlhQbGtYal96V2JrNU8xMDE0Mzk3dXRRY2RkMGdTX0hNV3BEbl95Zl9fbjd0Nk82SWd3S2FoTXNIek1NSWRyd3lXT0xWVWZvR1A4SnE?oc=5>

## CATALYSTS

No items in this run

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **TMC** | **N/A** | **-19.60** | **-4.24** | **N/A** | **1,098,026,368.00 USD** | **-64.27** |
| MP | N/A | 3.23 | 101.92 | 190.90 | 6,292,858,880.00 USD | -39.36 |
| LAC | 3.69 | 0.32 | -22.00 | N/A | 486,761,824.00 USD | -74.35 |
| VALE | 61.31 | 1.08 | 1.86 | -3.90 | 41,749,045,248.00 USD | -12.85 |

Peers fetched as_of: 2026-11-26; TMC reuses existing data (market data as_of: 2026-11-25); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-12
- Next expected earnings: 2027-03-25 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-26

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-12
- Revenue (latest available single quarter): 410,000.00 USD; period 2024-04-01/2024-06-30; fiscal year/reporting period 2024/Q2
- Net income (latest available single quarter): -28,361,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1798562/000162828026073463/tmc-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMihAFBVV95cUxOTEFfRTFzUERGeTM0UmJPUUh1czZndHM2czhWNEZZTFVaQUpteGdLOW9aWHNGZU5HVDlXV2FXRUpEQTJfUUNfTkFwYjhRZmJXZjRKODJHSXRmSWUtWTZ6dTVJdm00d2tnQlBlUGtrVEtFaFNpZWswT2lpODRERXJfYno4RlQ?oc=5
- https://news.google.com/rss/articles/CBMihAFBVV95cUxNWTJzMGR2c29XVm9zakxaeDJ4bnI2WUZrSUcwRGJhd3k4YU9MdXNsVzdfeUVJdEZCWnJUTXZtVGV0WFNvVzRBOFZYZ1ExM2JKTlJCN215SmFmRFZlSWRFSjF6TElWbTRYd2Yzam1pOWEza1VOeU5sLURzVGlEdmFmeVpVSnY?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxOU2dpbjJZRG02aF8yMmZlaFV1cm9FMlY5ME8tQ0ROMHMxN0VMRDRqSkw2bFJOX2V6NFNHZ3lYd2swd3kxbHZ6OTVVWjA2TDNtT05Sb0Vwd1VfUVZXeTRfOGtReDRSU01CaWJ0bzFuN29veFNNWDI1cko2UHM4c1dfamU1U2pvNTBVaVJxVm5LM3g1dHc?oc=5
- https://news.google.com/rss/articles/CBMihAFBVV95cUxPVDY4NElpZmZDandQYmsyb1phSFJLOHZHYVpXMlVaOHRoMktDN0pYMG12REY1dEVSRlhQbGtYal96V2JrNU8xMDE0Mzk3dXRRY2RkMGdTX0hNV3BEbl95Zl9fbjd0Nk82SWd3S2FoTXNIek1NSWRyd3lXT0xWVWZvR1A4SnE?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
