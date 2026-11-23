# CP.TO Intelligence Report

- ticker: **CP.TO**
- Report as_of: **2026-11-22**
- Market data as_of: **2026-11-20**
- Quant sources: https://finance.yahoo.com/quote/CP.TO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/CP.TO/key-statistics/
- AI analysis snapshot as_of: **2026-11-22**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-23T05:57:04.730421+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 11, 'rule': 2, 'ai': 4, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **3** exact headline/source/date matches; prior report **20261122T045655Z-f5ef568d/CP.TO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 11 unique headlines; 9 named publishers; 0 exact duplicates; 11 HTTPS source links; largest publisher share 18.18%; oldest publication 2026-11-15

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 128.7700 |
| Return 1D (%) | -1.7848 |
| Return 1W (%) | -4.0319 |
| Return 1M (%) | 4.9299 |
| Return YTD (%) | 28.2536 |
| Return 1Y (%) | 33.7430 |
| Annualized volatility (%) | 22.1181 |
| Beta vs SPY | 0.3657 |
| Max drawdown (%) | -11.9692 |
| Sharpe (rf=0) | 1.4305 |
| Downside deviation (rf=0, %) | 14.5271 |
| Sortino (rf=0) | 2.1781 |
| Historical VaR 95% (1D, %) | 1.8632 |
| Historical ES 95% (1D, %) | 2.9374 |
| Correlation vs SPY | 0.2357 |
| Tracking error vs SPY (%) | 23.5080 |
| P/E (trailing) | 29.74 |
| P/B | 2.45 |
| EV/EBITDA | 16.39 |
| Revenue growth (%) | 15.20 |
| Forward P/E (estimate) | 21.81 |
| Gross margin (%) | 52.76 |
| Operating margin (%) | 39.78 |
| Return on equity (%) | 8.27 |
| Free cash flow yield (%) | 2.45 |
| MA50 | 125.7840 |
| Close vs MA50 (%) | 2.3739 |
| MA200 | 121.3364 |
| Close vs MA200 (%) | 6.1264 |
| RSI (14, Wilder) | 48.0290 |
| MACD (12,26) | 1.9555 |
| MACD signal (9) | 2.2923 |
| MACD histogram | -0.3368 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'CP.TO': 286, 'SPY': 287}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 128.7700 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.7848 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -4.0319 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 4.9299 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 28.2536 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 33.7430 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 22.1181 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 14.5271 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 2.1781 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.8632 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.9374 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2357 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 23.5080 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.3657 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -11.9692 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.4305 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 21.8072 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 52.7640 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 39.7760 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 8.2680 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.4467 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 29.7390 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 48.0290 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.3368 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 2.3739 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 6.1264 -> Clearly above the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

### Canadian Pacific Kansas City Ltd. stock falls Friday, still outperforms market
- Summary: Canadian Pacific Kansas City Ltd. stock falls Friday, still outperforms market
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0gFBVV95cUxPb0FjMDJEalhfVFY0RVZlcXZJNzFnYWhCNWRuNnJLWVRhM2dqd0h4dTZrc2Q2ejdxdUxnWURTbmVGZEtZeHdzV1FPdnBHX0FuazB5Wm1EdXZMNnVUWFhIbWRHc3NmbDc2dllNTkdsaGlSZGFyMGNES3FDUm1ZVTlIbno1d2hjX2pvN2VuM050ZERNeFBJTVlzWEgtWE14X0xib1RqcmtVUTl4VzhvRHpzN2p0aTZJaWROZXNGXzN6cXJaREgtTjVvMk1FMUM4Z2pObkE?oc=5>

## CATALYSTS

### Canadian Pacific Kansas City stock: merger review fight moves forward
- Summary: Canadian Pacific Kansas City stock: merger review fight moves forward
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiywFBVV95cUxQWlNDVzY1Y3RMMXZiSWVETHNRNmdYbXE5R25iVDdTRGVDeldwcjdJN3hhd0pNR1FYMTNwaFFWcGZ4UXRPbjJmZjZnVFFmYVdoUjd4VHVRWmgwRjVXVzNfTU9RS3JmTDBwY21kVFBHbWxXS3JjOHVZSUMyeWtIcEhDeDRLVWkzelVCUGdUUG1CQnhqQWJrYWxpTVYwWHM2T0l4clpxUE5RUFU3TTFQNXVybk5XengxbHhqTFRsZFg4SUxaT0hheXM0dDNxNA?oc=5>

### Canadian Pacific Kansas City merger review gains support: Can CP stock recover from recent weakness?
- Summary: Merger review support may lift CP stock, potentially reversing recent weakness.
- Date: 2026-11-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxNcjhlaHEzYmZPZ2daaDlhZ19VMnZ3MTB4TVU4MWVJWHo1S09DUWQxTTZPUHExaWJkeFcxVjVCZVJLXzhnd0hHbW9IWjhRMktjT3NZZmt1ckpwdkFaSllkeFRyQUZCNTItbTVGdDZBRTNDR2Z0OUVPclRCSUJsWlNDWGEtZ1NsdERwd0dtNXRKYno?oc=5>

### Canadian Pacific Kansas City (TSX:CP) Rallies On Cross Border Network Story, Is It Still Undervalued?
- Summary: Shares rally on cross-border network news, questioning undervaluation.
- Date: 2026-11-15 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxONDhjWUpnQ0kzUDM0MEpqZHBhS2QtbzhKcy0wZ2pPTmZkZExjVXdtR0ptU0VEaXg5QVh2dGFwOE40UEwzeWkwSUE2MjFxenlzU1c1Q1N0OG1nanA4RkFhOU5DY0R5X3hoeUZ5aDJjbk8zSXl0a1N2cVZiM3ZPZHltdEJ6OTM0eWRSbW5NSEZLZXBzdGR2TFF2NHNnMjhZUQ?oc=5>

### Canadian Pacific Kansas City Sees Strongest Quarter as Grain and Intermodal Volumes Surge
- Summary: CP reports its best quarterly performance, driven by higher grain and intermodal traffic, indicating robust operational momentum and potential upside for investors.
- Date: 2026-11-22 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxPMnFGZ01ldmhDeVFRT1RrX2Y2Y3U4dFMwQXF5cGFQTG5EbW5TRmM5ZjUxeGVsdXcwSlpYS0gwYU1saXQwM1VNbWM4eWZwOHpEUTBObk91Q3ZuaVY1YmsxWUhNeThmOHduc3hEclhoX0lQdDJhRGhfNHBSOXlfbGxzQjJhSkNtRmFvNmExUTV2eXYwR05KMElzbmpqZ216Zzg?oc=5>

### CPKC at 26th Annual Scotiabank Transportation & Industrials Conference: growth outlook
- Summary: CPKC presented its growth outlook at the annual Scotiabank conference, outlining future expectations and strategic priorities.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi3gFBVV95cUxPcVktM0hxcUl5SXNKdFRjRnFUWDgwSmRxU2s5Ui10R3FBQ2JYcC16WGFRUExmTlBiWmw3cC1wVHF2U2pCYXQxZjRUQ3ZDcXN5YXhmLUVZbi0wWXA0SFlxUXhLQ0VrUi1FWWVpcV85Rjh1aS1fUWRvTEhsVmJENW1qYlU2Vi1lMm9ZM3g3SEl4Q3hpbHBTOURfdVItU0lWcHVUeEJQTXFrMkZlWENDNlJKY3RBRndsYjZ4dWJIT1RQTnVkYktyQWdMWFU2RXlxS3YxT1ZOUjVOcENqcUZrTEE?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **CP.TO** | **29.74** | **2.45** | **16.39** | **15.20** | **111,972,573,184.00 CAD** | **33.74** |
| CNR.TO | 22.03 | 4.80 | 13.66 | 14.60 | 105,175,384,064.00 CAD | 38.29 |
| UNP | 22.41 | 7.75 | 14.96 | 15.30 | 170,722,213,888.00 USD | 32.61 |
| NSC | 26.07 | 4.18 | 14.75 | 13.60 | 69,858,041,856.00 USD | 12.87 |

Peers fetched as_of: 2026-11-22; CP.TO reuses existing data (market data as_of: 2026-11-20); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-28
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-22

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-29
- Revenue (latest available single quarter): N/A
- Net income (latest available single quarter): N/A
- SEC link: https://www.sec.gov/Archives/edgar/data/16875/000001687526000033/cp-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMi0gFBVV95cUxPb0FjMDJEalhfVFY0RVZlcXZJNzFnYWhCNWRuNnJLWVRhM2dqd0h4dTZrc2Q2ejdxdUxnWURTbmVGZEtZeHdzV1FPdnBHX0FuazB5Wm1EdXZMNnVUWFhIbWRHc3NmbDc2dllNTkdsaGlSZGFyMGNES3FDUm1ZVTlIbno1d2hjX2pvN2VuM050ZERNeFBJTVlzWEgtWE14X0xib1RqcmtVUTl4VzhvRHpzN2p0aTZJaWROZXNGXzN6cXJaREgtTjVvMk1FMUM4Z2pObkE?oc=5
- https://news.google.com/rss/articles/CBMiywFBVV95cUxQWlNDVzY1Y3RMMXZiSWVETHNRNmdYbXE5R25iVDdTRGVDeldwcjdJN3hhd0pNR1FYMTNwaFFWcGZ4UXRPbjJmZjZnVFFmYVdoUjd4VHVRWmgwRjVXVzNfTU9RS3JmTDBwY21kVFBHbWxXS3JjOHVZSUMyeWtIcEhDeDRLVWkzelVCUGdUUG1CQnhqQWJrYWxpTVYwWHM2T0l4clpxUE5RUFU3TTFQNXVybk5XengxbHhqTFRsZFg4SUxaT0hheXM0dDNxNA?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxNcjhlaHEzYmZPZ2daaDlhZ19VMnZ3MTB4TVU4MWVJWHo1S09DUWQxTTZPUHExaWJkeFcxVjVCZVJLXzhnd0hHbW9IWjhRMktjT3NZZmt1ckpwdkFaSllkeFRyQUZCNTItbTVGdDZBRTNDR2Z0OUVPclRCSUJsWlNDWGEtZ1NsdERwd0dtNXRKYno?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxONDhjWUpnQ0kzUDM0MEpqZHBhS2QtbzhKcy0wZ2pPTmZkZExjVXdtR0ptU0VEaXg5QVh2dGFwOE40UEwzeWkwSUE2MjFxenlzU1c1Q1N0OG1nanA4RkFhOU5DY0R5X3hoeUZ5aDJjbk8zSXl0a1N2cVZiM3ZPZHltdEJ6OTM0eWRSbW5NSEZLZXBzdGR2TFF2NHNnMjhZUQ?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxPMnFGZ01ldmhDeVFRT1RrX2Y2Y3U4dFMwQXF5cGFQTG5EbW5TRmM5ZjUxeGVsdXcwSlpYS0gwYU1saXQwM1VNbWM4eWZwOHpEUTBObk91Q3ZuaVY1YmsxWUhNeThmOHduc3hEclhoX0lQdDJhRGhfNHBSOXlfbGxzQjJhSkNtRmFvNmExUTV2eXYwR05KMElzbmpqZ216Zzg?oc=5
- https://news.google.com/rss/articles/CBMi3gFBVV95cUxPcVktM0hxcUl5SXNKdFRjRnFUWDgwSmRxU2s5Ui10R3FBQ2JYcC16WGFRUExmTlBiWmw3cC1wVHF2U2pCYXQxZjRUQ3ZDcXN5YXhmLUVZbi0wWXA0SFlxUXhLQ0VrUi1FWWVpcV85Rjh1aS1fUWRvTEhsVmJENW1qYlU2Vi1lMm9ZM3g3SEl4Q3hpbHBTOURfdVItU0lWcHVUeEJQTXFrMkZlWENDNlJKY3RBRndsYjZ4dWJIT1RQTnVkYktyQWdMWFU2RXlxS3YxT1ZOUjVOcENqcUZrTEE?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
