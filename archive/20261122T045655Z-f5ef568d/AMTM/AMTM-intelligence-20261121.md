# AMTM Intelligence Report

- ticker: **AMTM**
- Report as_of: **2026-11-21**
- Market data as_of: **2026-11-20**
- Quant sources: https://finance.yahoo.com/quote/AMTM/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AMTM/key-statistics/
- AI analysis snapshot as_of: **2026-11-21**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-22T05:03:33.928606+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 3, 'rule': 2, 'ai': 0, 'unknown': 0, 'irrelevant': 1})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **0** exact headline/source/date matches; prior report **N/A** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 3 unique headlines; 3 named publishers; 0 exact duplicates; 3 HTTPS source links; largest publisher share 33.33%; oldest publication 2026-11-19

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 20.3400 |
| Return 1D (%) | -3.2350 |
| Return 1W (%) | -7.3349 |
| Return 1M (%) | 2.3654 |
| Return YTD (%) | -29.8621 |
| Return 1Y (%) | -16.5710 |
| Annualized volatility (%) | 43.8158 |
| Beta vs SPY | 0.9654 |
| Max drawdown (%) | -51.7186 |
| Sharpe (rf=0) | -0.1987 |
| Downside deviation (rf=0, %) | 29.9770 |
| Sortino (rf=0) | -0.2904 |
| Historical VaR 95% (1D, %) | 3.8323 |
| Historical ES 95% (1D, %) | 5.9321 |
| Correlation vs SPY | 0.3150 |
| Tracking error vs SPY (%) | 41.5887 |
| P/E (trailing) | 24.51 |
| P/B | 1.06 |
| EV/EBITDA | 8.38 |
| Revenue growth (%) | -2.00 |
| Forward P/E (estimate) | 7.71 |
| Gross margin (%) | 10.49 |
| Operating margin (%) | 4.01 |
| Return on equity (%) | 4.29 |
| Free cash flow yield (%) | 9.74 |
| MA50 | 20.3154 |
| Close vs MA50 (%) | 0.1211 |
| MA200 | 23.4506 |
| Close vs MA200 (%) | -13.2645 |
| RSI (14, Wilder) | 41.9398 |
| MACD (12,26) | 0.1623 |
| MACD signal (9) | 0.4375 |
| MACD histogram | -0.2752 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AMTM': 287, 'SPY': 287}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 20.3400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -3.2350 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -7.3349 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 2.3654 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -29.8621 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -16.5710 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 43.8158 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 29.9770 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.2904 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.8323 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.9321 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.3150 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 41.5887 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.9654 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -51.7186 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.1987 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 7.7059 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 10.4880 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 4.0130 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 4.2870 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 9.7371 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 24.5060 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 41.9398 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.2752 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 0.1211 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -13.2645 -> Clearly below the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

No items in this run

## CATALYSTS

### AMENTUM HOLDINGS Q4 2026 Earnings Preview: Recent $AMTM Insider Trading, Hedge Fund Activity, and More
- Summary: AMENTUM HOLDINGS Q4 2026 Earnings Preview: Recent $AMTM Insider Trading, Hedge Fund Activity, and More
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2wFBVV95cUxOOVlQamJUZlBUcy1Zem1aOG1IWkhLQm9hNERENDVaTWRRYTZRSEJQd3pXblZPYUpxcUJtM2h5elNUV1hzd0cwVEcwdV9WSHJNN0s0VnhxcnVQVHU2WEpWSXM2OWZKMThlTlp6WjdxSk5ONTRFQ19TSnNVT1Y2WEJYcTBqaDZ3NXV1X25nTjBtWGpEV3NvZWozNmNPZ3g1Nmd6aWs3SjhtX2d0ZGw5Q3Z6bVI3VlJhdUp1UTVCQl9ZX0hFRGhnQnItdHVoRExtUFF5S2hiS0NlQTdrODQ?oc=5>

### Amentum Holdings (AMTM) CEO Heller acquired 51,965 shares
- Summary: Amentum Holdings (AMTM) CEO Heller acquired 51,965 shares
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxPblJvRDk4UkZ0RnlrUHV3NmFtcVhwNzQ2U3hMdjExaTRLY2FyOUhTZk56ekt6bnpHcUVlUDcxcUp0UzFFeGUxajdMVktUbGc1STJJVTNUNlo3WVdvTlpUOGk5UGJhZTNGcmxobmFoVTlpSlVGLWlKX3p3aWFWamJsdjVUU2g5aWNITF9aMzZWOUVfMWRha3U2Um5mdjlodTVDSHMyTS1EbF9DTU8tcHc?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AMTM** | **24.51** | **1.06** | **8.38** | **-2.00** | **4,973,260,288.00 USD** | **-16.57** |
| LDOS | 10.92 | 2.88 | 8.67 | 3.60 | 14,908,972,032.00 USD | -33.41 |
| CACI | 24.13 | 2.81 | 14.46 | 8.20 | 13,056,338,944.00 USD | -1.21 |
| SAIC | 16.60 | 4.16 | 11.34 | 6.30 | 5,960,776,704.00 USD | 69.60 |

Peers fetched as_of: 2026-11-21; AMTM reuses existing data (market data as_of: 2026-11-20); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-10
- Next expected earnings: 2026-11-23 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-21

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-08-11
- Revenue (latest available single quarter): 3,490,000,000.00 USD; period 2026-04-04/2026-07-03; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 66,000,000.00 USD; period 2026-04-04/2026-07-03; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/2011286/000162828026055727/amtm-20260703.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMi2wFBVV95cUxOOVlQamJUZlBUcy1Zem1aOG1IWkhLQm9hNERENDVaTWRRYTZRSEJQd3pXblZPYUpxcUJtM2h5elNUV1hzd0cwVEcwdV9WSHJNN0s0VnhxcnVQVHU2WEpWSXM2OWZKMThlTlp6WjdxSk5ONTRFQ19TSnNVT1Y2WEJYcTBqaDZ3NXV1X25nTjBtWGpEV3NvZWozNmNPZ3g1Nmd6aWs3SjhtX2d0ZGw5Q3Z6bVI3VlJhdUp1UTVCQl9ZX0hFRGhnQnItdHVoRExtUFF5S2hiS0NlQTdrODQ?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxPblJvRDk4UkZ0RnlrUHV3NmFtcVhwNzQ2U3hMdjExaTRLY2FyOUhTZk56ekt6bnpHcUVlUDcxcUp0UzFFeGUxajdMVktUbGc1STJJVTNUNlo3WVdvTlpUOGk5UGJhZTNGcmxobmFoVTlpSlVGLWlKX3p3aWFWamJsdjVUU2g5aWNITF9aMzZWOUVfMWRha3U2Um5mdjlodTVDSHMyTS1EbF9DTU8tcHc?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
