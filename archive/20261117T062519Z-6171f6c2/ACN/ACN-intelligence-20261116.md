# ACN Intelligence Report

- ticker: **ACN**
- Report as_of: **2026-11-16**
- Market data as_of: **2026-11-16**
- Quant sources: https://finance.yahoo.com/quote/ACN/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/ACN/key-statistics/
- AI analysis snapshot as_of: **2026-11-16**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-17T06:46:48.545577+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 10, 'rule': 0, 'ai': 6, 'unknown': 0, 'irrelevant': 4})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **8** exact headline/source/date matches; prior report **20261116T043911Z-b81cfeb4/ACN** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 10 unique headlines; 5 named publishers; 0 exact duplicates; 10 HTTPS source links; largest publisher share 50.0%; oldest publication 2026-11-09

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 247.7000 |
| Return 1D (%) | -1.1138 |
| Return 1W (%) | -2.6222 |
| Return 1M (%) | 7.8457 |
| Return YTD (%) | -5.0197 |
| Return 1Y (%) | 3.9241 |
| Annualized volatility (%) | 50.0989 |
| Beta vs SPY | -0.0438 |
| Max drawdown (%) | -56.5068 |
| Sharpe (rf=0) | 0.3610 |
| Downside deviation (rf=0, %) | 34.7786 |
| Sortino (rf=0) | 0.5200 |
| Historical VaR 95% (1D, %) | 4.6071 |
| Historical ES 95% (1D, %) | 6.8005 |
| Correlation vs SPY | -0.0120 |
| Tracking error vs SPY (%) | 52.1154 |
| P/E (trailing) | 18.27 |
| P/B | 4.67 |
| EV/EBITDA | 11.07 |
| Revenue growth (%) | 6.20 |
| Forward P/E (estimate) | 15.57 |
| Gross margin (%) | 32.05 |
| Operating margin (%) | 16.42 |
| Return on equity (%) | 26.02 |
| Free cash flow yield (%) | 7.30 |
| MA50 | 217.1575 |
| Close vs MA50 (%) | 14.0647 |
| MA200 | 187.4010 |
| Close vs MA200 (%) | 32.1765 |
| RSI (14, Wilder) | 54.9343 |
| MACD (12,26) | 9.8498 |
| MACD signal (9) | 12.9773 |
| MACD histogram | -3.1275 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'ACN': 283, 'SPY': 283}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 247.7000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.1138 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -2.6222 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 7.8457 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -5.0197 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 3.9241 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 50.0989 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 34.7786 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.5200 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.6071 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 6.8005 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.0120 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 52.1154 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.0438 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -56.5068 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.3610 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 15.5702 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 32.0500 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 16.4190 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 26.0250 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 7.3019 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 18.2670 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 54.9343 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -3.1275 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 14.0647 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 32.1765 -> Clearly above the moving-average trend level.

## TAILWINDS

### Accenture: Market Sentiment Is Aligning With Fundamentals
- Summary: Positive market sentiment matches fundamentals, supporting stock outlook.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxOT01yM1M0N3ZyYVBxcFVKS19lY242eEFlT2RzbV94WWhoZUlxaVFqMi01Y2c2Sm5SSlA4RGVPVGw4MGZ1UEhCVHZoLVBFR2luWVY3RHJpUWZwYTdWUWdBVEQxUkd5UHlHRndYTW5NdVlHMDBnaVNscnVGYUh4YUZiemFTWW9OV0FYcEF0WXQ4TEJYcm1SbHdLV1Z3?oc=5>

### Why Is Accenture (NYSE:ACN) Expanding Its AI Capabilities?
- Summary: Accenture is expanding AI capabilities, indicating product development.
- Date: 2026-11-09 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxNTUtPYVV4RksxMDluN1hFMFlFRlI4b0tvMnAtM05iT1RfcXB5bUJCLXZyWW8tX0w2VjVjNzBpYzhpTzR0cVJndVN6NVFMZUx1Z3NYUW9qTThqOGZOaml6cl9fMmNCODJ1SXk2bDVmTGJnSnh4M3pNSmpvcS1Ec3BWU2pGSWNxYUNjaWs4cXlnSkNwWE5aM1RuWVRKLWdZalU?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Should You Buy Accenture Stock For Its Cash Flow?
- Summary: Analysis of Accenture's cash flow suggests potential investment value.
- Date: 2026-11-13 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxQeWRaeWgyRkxxM2l2ZG1QbmhNcTQ2MkVLc0RYT2RPdVd1aV83LWVyYUNTVkcwNGlvTklWRVIyczNJTUJic0tBUEZHODBrTVltbkU0elQzN29CTnk5aWdLNkttckFtck1UNE5USXMyZmhsWWxGVWhFdE9sMU94eEVxZUhjbjExTGxRX0htbF8zX1lJbWQ1M3k1SVpYVzEyazRLenhkLTg2RWpGUktD?oc=5>

### Is Accenture Stock Becoming A Different Bet?
- Summary: Evaluates changes in Accenture's investment profile.
- Date: 2026-11-10 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxPMzZuNjNWbnQ3YUFBMUhtR3FDenZfbmp5eXB6QlRhZmVZcTgzdjdyOEg5S3JPTklHd2FGYUxQUmJmRElJMWpJTkU3cE05QllMNTk2MjlqMzBzdVZRNmtxNE4yY2YxLU5YVzFxb053UTZkRFZjdmpiWnBWM05ETG9QRjdqOHQzRUo1em5YdG44M3Z1aWFMN1pJZDRxUTVrWGtQOHdnS2tB?oc=5>

### Accenture: Sold On AI While AI Makes It Grow
- Summary: Examines Accenture's AI strategy and growth prospects.
- Date: 2026-11-13 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxPdTBKb19fWFdlSGhTenE3VkNwWXpCMHVnMU43ZW9kUi1DYnNqTXpwZ0dqYURJemRiN1pZbDJxeVFaZTF1bTUwbmdYc3l2Q25uSGtwRl9OS1QyMEtWX3p2V1FBNzNVSnQwcU1CQWVfZ1gyakFhS2hBM2JjRElhUVB4S09VLVhJNy1rQWFUSA?oc=5>

### Here's How Much $100 Invested In Accenture 20 Years Ago Would Be Worth Today
- Summary: Historical performance of Accenture stock over 20 years.
- Date: 2026-11-13 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxNQ2ZqQ0NLc2JCb0FGWG1PdjlDdHpGSjMtbnk3VExtenFhYUZOdHZLMGNxUGUzemY3MXZZSkNLbkg0dGpyVnZJN0JWYldSc2hOaFZVNk4tM0l6THBmQVA2MDZEeXV6MmtaZzVyZUR5M0laQXlzUG1WTDBRc3lDZS0yVXhIMmpBc0dTSURkcWZJdk54UlVyc0JOcHMyektFTmNGSU1ObEIwb2kzbzRIZlhhM1pnWFVvMWFu?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **ACN** | **18.27** | **4.67** | **11.07** | **6.20** | **146,325,667,840.00 USD** | **3.92** |
| IBM | 20.69 | 6.45 | 17.19 | 4.70 | 229,201,248,256.00 USD | -18.49 |
| CTSH | 11.37 | 1.89 | 6.92 | 4.60 | 27,845,525,504.00 USD | -11.83 |
| INFY | 15.20 | 9.65 | 19.74 | 1.40 | 49,860,136,960.00 USD | -24.47 |

Peers fetched as_of: 2026-11-16; ACN reuses existing data (market data as_of: 2026-11-16); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-01
- Next expected earnings: 2026-12-17 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-16

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

- https://news.google.com/rss/articles/CBMimgFBVV95cUxOT01yM1M0N3ZyYVBxcFVKS19lY242eEFlT2RzbV94WWhoZUlxaVFqMi01Y2c2Sm5SSlA4RGVPVGw4MGZ1UEhCVHZoLVBFR2luWVY3RHJpUWZwYTdWUWdBVEQxUkd5UHlHRndYTW5NdVlHMDBnaVNscnVGYUh4YUZiemFTWW9OV0FYcEF0WXQ4TEJYcm1SbHdLV1Z3?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxNTUtPYVV4RksxMDluN1hFMFlFRlI4b0tvMnAtM05iT1RfcXB5bUJCLXZyWW8tX0w2VjVjNzBpYzhpTzR0cVJndVN6NVFMZUx1Z3NYUW9qTThqOGZOaml6cl9fMmNCODJ1SXk2bDVmTGJnSnh4M3pNSmpvcS1Ec3BWU2pGSWNxYUNjaWs4cXlnSkNwWE5aM1RuWVRKLWdZalU?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxQeWRaeWgyRkxxM2l2ZG1QbmhNcTQ2MkVLc0RYT2RPdVd1aV83LWVyYUNTVkcwNGlvTklWRVIyczNJTUJic0tBUEZHODBrTVltbkU0elQzN29CTnk5aWdLNkttckFtck1UNE5USXMyZmhsWWxGVWhFdE9sMU94eEVxZUhjbjExTGxRX0htbF8zX1lJbWQ1M3k1SVpYVzEyazRLenhkLTg2RWpGUktD?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxPMzZuNjNWbnQ3YUFBMUhtR3FDenZfbmp5eXB6QlRhZmVZcTgzdjdyOEg5S3JPTklHd2FGYUxQUmJmRElJMWpJTkU3cE05QllMNTk2MjlqMzBzdVZRNmtxNE4yY2YxLU5YVzFxb053UTZkRFZjdmpiWnBWM05ETG9QRjdqOHQzRUo1em5YdG44M3Z1aWFMN1pJZDRxUTVrWGtQOHdnS2tB?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxPdTBKb19fWFdlSGhTenE3VkNwWXpCMHVnMU43ZW9kUi1DYnNqTXpwZ0dqYURJemRiN1pZbDJxeVFaZTF1bTUwbmdYc3l2Q25uSGtwRl9OS1QyMEtWX3p2V1FBNzNVSnQwcU1CQWVfZ1gyakFhS2hBM2JjRElhUVB4S09VLVhJNy1rQWFUSA?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxNQ2ZqQ0NLc2JCb0FGWG1PdjlDdHpGSjMtbnk3VExtenFhYUZOdHZLMGNxUGUzemY3MXZZSkNLbkg0dGpyVnZJN0JWYldSc2hOaFZVNk4tM0l6THBmQVA2MDZEeXV6MmtaZzVyZUR5M0laQXlzUG1WTDBRc3lDZS0yVXhIMmpBc0dTSURkcWZJdk54UlVyc0JOcHMyektFTmNGSU1ObEIwb2kzbzRIZlhhM1pnWFVvMWFu?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
