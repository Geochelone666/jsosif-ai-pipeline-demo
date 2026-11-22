# SYY Intelligence Report

- ticker: **SYY**
- Report as_of: **2026-11-21**
- Market data as_of: **2026-11-20**
- Quant sources: https://finance.yahoo.com/quote/SYY/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/SYY/key-statistics/
- AI analysis snapshot as_of: **2026-11-21**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-22T05:17:27.752031+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 3, 'rule': 1, 'ai': 2, 'unknown': 0})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **0** exact headline/source/date matches; prior report **N/A** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 3 unique headlines; 2 named publishers; 0 exact duplicates; 3 HTTPS source links; largest publisher share 66.67%; oldest publication 2026-11-18

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 78.1700 |
| Return 1D (%) | 1.3221 |
| Return 1W (%) | 1.3878 |
| Return 1M (%) | -5.6943 |
| Return YTD (%) | 9.1538 |
| Return 1Y (%) | 6.5652 |
| Annualized volatility (%) | 29.2721 |
| Beta vs SPY | 0.1920 |
| Max drawdown (%) | -23.9798 |
| Sharpe (rf=0) | 0.3681 |
| Downside deviation (rf=0, %) | 22.4096 |
| Sortino (rf=0) | 0.4808 |
| Historical VaR 95% (1D, %) | 2.1606 |
| Historical ES 95% (1D, %) | 4.3236 |
| Correlation vs SPY | 0.0938 |
| Tracking error vs SPY (%) | 31.3486 |
| P/E (trailing) | 20.79 |
| P/B | 9.51 |
| EV/EBITDA | 11.22 |
| Revenue growth (%) | 2.80 |
| Forward P/E (estimate) | 14.48 |
| Gross margin (%) | 18.54 |
| Operating margin (%) | 4.13 |
| Return on equity (%) | 58.74 |
| Free cash flow yield (%) | 6.26 |
| MA50 | 78.9593 |
| Close vs MA50 (%) | -0.9996 |
| MA200 | 79.3806 |
| Close vs MA200 (%) | -1.5251 |
| RSI (14, Wilder) | 48.5059 |
| MACD (12,26) | -0.6585 |
| MACD signal (9) | -0.6696 |
| MACD histogram | 0.0111 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'SYY': 287, 'SPY': 287}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 78.1700 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.3221 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 1.3878 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -5.6943 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 9.1538 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 6.5652 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 29.2721 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 22.4096 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.4808 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.1606 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.3236 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.0938 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 31.3486 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.1920 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -23.9798 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.3681 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 14.4832 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 18.5430 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 4.1330 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 58.7360 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 6.2567 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 20.7899 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 48.5059 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.0111 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -0.9996 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -1.5251 -> Slightly below the moving-average trend level.

## TAILWINDS

### Sysco (SYY) Stock Looks Undervalued After Its 19% Three Year Gain
- Summary: Sysco (SYY) Stock Looks Undervalued After Its 19% Three Year Gain
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxON29JSXNTcWRsVXpuZ2RPQXV0VTc3Y0VESXBWdG5tcnVveHBKQk1YYlp6Z1VOSzBEOGZZLUV1OTJmeC1VXzUtR0NlNDlobzRxYWtPV0hLVGtxdVRaX21qQXF6bGFvZm04ajFybGhNT3JrM3plM3Fxd3Vyb3FhMmZXWF9vSHdYS0FCNkJpM01xc0k1R3Uwb09NWUVwd2I5cTA?oc=5>

### Why Sysco (SYY) Stock Is Up Today
- Summary: Shares of Sysco rose today, reflecting positive market sentiment and potential investor confidence.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMidEFVX3lxTE9vNlVEb2duRldOdDMtdTFFRXgwVTVndDNQbXg4LXhWUTUzLVBxSFhmeUpKSWpzSk9lVzJNSm9FZjdEYTZ5MDktSFlGdUtPdVJGU3Y4Zlc1Tjh0d0N1bTdiZWlxQngwaHhIS01rQzd4MmRacmxy?oc=5>

### Sysco (SYY) Affirms Dividend, Is It Still Below Fair Value?
- Summary: Sysco confirmed its dividend, suggesting stable cash flow and shareholder value, though valuation remains below perceived fair value.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxPNmFYZHVScVoxLTMtNTBiTElOaFhlcVNjcFBLR08tSk80OG9tcnVNb1VOZldOOGhyQUpUcktMMG83a1FrOFRFYU5MMlFDMHAySVJ2ck1tdlJNREROemV0UlRHb0lQQTE2RnlWNGlzQU1LcGRWOEctZDI0SDVPTVZoV1JxOUZ1UGVubnFod1VJcHlJWF9ISjhNamt4MnQ3UQ?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

No items in this run

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **SYY** | **20.79** | **9.51** | **11.22** | **2.80** | **38,480,801,792.00 USD** | **6.57** |
| USFD | 29.99 | 5.32 | 14.89 | 2.10 | 23,047,159,808.00 USD | 53.25 |
| PFGC | 43.14 | 3.34 | 14.15 | 5.50 | 17,084,908,544.00 USD | 14.83 |
| CHEF | 44.06 | 6.10 | 19.11 | 11.20 | 4,462,335,488.00 USD | 79.27 |

Peers fetched as_of: 2026-11-21; SYY reuses existing data (market data as_of: 2026-11-20); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-03
- Next expected earnings: 2027-02-02 (yfinance; expected dates may change)

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
- Filing date: 2026-11-04
- Revenue (latest available single quarter): 21,744,000,000.00 USD; period 2026-06-28/2026-09-26; fiscal year/reporting period 2027/Q1
- Net income (latest available single quarter): 526,000,000.00 USD; period 2026-06-28/2026-09-26; fiscal year/reporting period 2027/Q1
- SEC link: https://www.sec.gov/Archives/edgar/data/96021/000009602126000050/syy-20260926.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMinwFBVV95cUxON29JSXNTcWRsVXpuZ2RPQXV0VTc3Y0VESXBWdG5tcnVveHBKQk1YYlp6Z1VOSzBEOGZZLUV1OTJmeC1VXzUtR0NlNDlobzRxYWtPV0hLVGtxdVRaX21qQXF6bGFvZm04ajFybGhNT3JrM3plM3Fxd3Vyb3FhMmZXWF9vSHdYS0FCNkJpM01xc0k1R3Uwb09NWUVwd2I5cTA?oc=5
- https://news.google.com/rss/articles/CBMidEFVX3lxTE9vNlVEb2duRldOdDMtdTFFRXgwVTVndDNQbXg4LXhWUTUzLVBxSFhmeUpKSWpzSk9lVzJNSm9FZjdEYTZ5MDktSFlGdUtPdVJGU3Y4Zlc1Tjh0d0N1bTdiZWlxQngwaHhIS01rQzd4MmRacmxy?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxPNmFYZHVScVoxLTMtNTBiTElOaFhlcVNjcFBLR08tSk80OG9tcnVNb1VOZldOOGhyQUpUcktMMG83a1FrOFRFYU5MMlFDMHAySVJ2ck1tdlJNREROemV0UlRHb0lQQTE2RnlWNGlzQU1LcGRWOEctZDI0SDVPTVZoV1JxOUZ1UGVubnFod1VJcHlJWF9ISjhNamt4MnQ3UQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
