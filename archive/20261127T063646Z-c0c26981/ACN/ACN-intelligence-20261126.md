# ACN Intelligence Report

- ticker: **ACN**
- Report as_of: **2026-11-26**
- Market data as_of: **2026-11-25**
- Quant sources: https://finance.yahoo.com/quote/ACN/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/ACN/key-statistics/
- AI analysis snapshot as_of: **2026-11-26**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-27T06:36:55.494243+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 5, 'rule': 3, 'ai': 0, 'unknown': 0, 'irrelevant': 2})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **1** exact headline/source/date matches; prior report **20261125T065354Z-0b3565c6/ACN** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 5 unique headlines; 4 named publishers; 0 exact duplicates; 5 HTTPS source links; largest publisher share 40.0%; oldest publication 2026-11-24

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 240.4900 |
| Return 1D (%) | 3.5167 |
| Return 1W (%) | 5.7145 |
| Return 1M (%) | -3.5610 |
| Return YTD (%) | -7.7843 |
| Return 1Y (%) | -0.7284 |
| Annualized volatility (%) | 50.4868 |
| Beta vs SPY | -0.0132 |
| Max drawdown (%) | -56.5068 |
| Sharpe (rf=0) | 0.2388 |
| Downside deviation (rf=0, %) | 35.2855 |
| Sortino (rf=0) | 0.3417 |
| Historical VaR 95% (1D, %) | 4.7185 |
| Historical ES 95% (1D, %) | 6.8166 |
| Correlation vs SPY | -0.0039 |
| Tracking error vs SPY (%) | 52.7043 |
| P/E (trailing) | 17.74 |
| P/B | 4.54 |
| EV/EBITDA | 10.75 |
| Revenue growth (%) | 6.20 |
| Forward P/E (estimate) | 15.11 |
| Gross margin (%) | 32.05 |
| Operating margin (%) | 16.42 |
| Return on equity (%) | 26.02 |
| Free cash flow yield (%) | 7.52 |
| MA50 | 223.5024 |
| Close vs MA50 (%) | 7.6007 |
| MA200 | 187.1399 |
| Close vs MA200 (%) | 28.5082 |
| RSI (14, Wilder) | 52.7433 |
| MACD (12,26) | -0.1117 |
| MACD signal (9) | 3.7622 |
| MACD histogram | -3.8739 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'ACN': 290, 'SPY': 290}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 240.4900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 3.5167 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 5.7145 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -3.5610 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -7.7843 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -0.7284 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 50.4868 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 35.2855 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.3417 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.7185 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 6.8166 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.0039 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 52.7043 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.0132 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -56.5068 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.2388 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 15.1115 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 32.0500 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 16.4190 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 26.0250 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 7.5208 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 17.7353 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 52.7433 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -3.8739 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 7.6007 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 28.5082 -> Clearly above the moving-average trend level.

## TAILWINDS

### Accenture PLC Stock (ACN) Moved Up by 4.83% on Nov 24: Facts Behind the Movement
- Summary: Accenture PLC Stock (ACN) Moved Up by 4.83% on Nov 24: Facts Behind the Movement
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxNVzN2ZGtRQ2JpanZ4MXd3c0xCUWpuZHA1UW9BLTlzN0RiWW5pb3VBSDBLWlRlWC1WVk5lLWFIMVhMZmNmRExLWUoxWWczaUQ1Q25md2NSNlBHTFRGckM0ZzEtQmFJUVF6YlZWNWdwblZKZDZaMjNEVGl6RWxpcGQ4RkZsYTZWeE1tZWc?oc=5>

### Accenture PLC Stock (ACN) Moved Up by 4.94% on Nov 25: What Investors Need To Know
- Summary: Accenture PLC Stock (ACN) Moved Up by 4.94% on Nov 25: What Investors Need To Know
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxQZkQ0MU9HT1VGd1k0aGh2ZGJNOHNHeElHUXlBRWNaNDNnZnVtcUIzNzU0VGkzbzhqSnZKdmJObWZrd0ZMQ2VyXzlERDV4MS1OdFRJZ05HOFdVNHN3MTBlaFlQdU5UNFY0cE44YVBNUmlqNHNqMjZ1aFh0MEhKdXNTRkx0dklWbDloMnc?oc=5>

### Accenture PLC (ACN) Stock Up 4.5% and Still Undervalued -- GF Sc
- Summary: Accenture PLC (ACN) Stock Up 4.5% and Still Undervalued -- GF Sc
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxOSFNtY2N3bGs0VzVuYTNzR2d2dmtFYWs3NElRX0RKVGxKcjBNZHVtZS1VUEZZRDVrNmNWQTFaWXpQbEFsNjRRdmJXN0RfeFlYQTRseTdHTFgtNTRMb0hmYURlU2ZEaERsQmFoY1dWV2ctdUpJV1pPdDFsYUVjZ3c2X2tTYWFMVXJ0cjJBYWRFRlZMZzVudWxWNVFDR1Jaa2hCNHZGQmpjb1k?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

No items in this run

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **ACN** | **17.74** | **4.54** | **10.75** | **6.20** | **142,066,450,432.00 USD** | **-0.73** |
| IBM | 20.77 | 6.48 | 17.25 | 4.70 | 230,108,577,792.00 USD | -17.84 |
| CTSH | 11.55 | 1.93 | 7.03 | 4.60 | 28,305,967,104.00 USD | -15.24 |
| INFY | 16.07 | 10.21 | 20.91 | 1.40 | 52,735,901,696.00 USD | -23.02 |

Peers fetched as_of: 2026-11-26; ACN reuses existing data (market data as_of: 2026-11-25); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-01
- Next expected earnings: 2026-12-17 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-26

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
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

- https://news.google.com/rss/articles/CBMiigFBVV95cUxNVzN2ZGtRQ2JpanZ4MXd3c0xCUWpuZHA1UW9BLTlzN0RiWW5pb3VBSDBLWlRlWC1WVk5lLWFIMVhMZmNmRExLWUoxWWczaUQ1Q25md2NSNlBHTFRGckM0ZzEtQmFJUVF6YlZWNWdwblZKZDZaMjNEVGl6RWxpcGQ4RkZsYTZWeE1tZWc?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxQZkQ0MU9HT1VGd1k0aGh2ZGJNOHNHeElHUXlBRWNaNDNnZnVtcUIzNzU0VGkzbzhqSnZKdmJObWZrd0ZMQ2VyXzlERDV4MS1OdFRJZ05HOFdVNHN3MTBlaFlQdU5UNFY0cE44YVBNUmlqNHNqMjZ1aFh0MEhKdXNTRkx0dklWbDloMnc?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxOSFNtY2N3bGs0VzVuYTNzR2d2dmtFYWs3NElRX0RKVGxKcjBNZHVtZS1VUEZZRDVrNmNWQTFaWXpQbEFsNjRRdmJXN0RfeFlYQTRseTdHTFgtNTRMb0hmYURlU2ZEaERsQmFoY1dWV2ctdUpJV1pPdDFsYUVjZ3c2X2tTYWFMVXJ0cjJBYWRFRlZMZzVudWxWNVFDR1Jaa2hCNHZGQmpjb1k?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
