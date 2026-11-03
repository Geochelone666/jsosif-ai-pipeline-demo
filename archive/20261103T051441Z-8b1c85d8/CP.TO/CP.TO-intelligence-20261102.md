# CP.TO Intelligence Report

- ticker: **CP.TO**
- Report as_of: **2026-11-02**
- Market data as_of: **2026-11-02**
- Quant sources: https://finance.yahoo.com/quote/CP.TO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/CP.TO/key-statistics/
- AI analysis snapshot as_of: **2026-11-02**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-03T05:37:01.770024+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 6, 'rule': 2, 'ai': 3, 'unknown': 0, 'irrelevant': 1})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **2** exact headline/source/date matches; prior report **20261102T041627Z-c84a7052/CP.TO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'negative_sentiment_in_tailwinds': 1}
- RSS source audit (metadata only, not article fact-checking): 6 unique headlines; 6 named publishers; 0 exact duplicates; 6 HTTPS source links; largest publisher share 16.67%; oldest publication 2026-10-28

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 127.9000 |
| Return 1D (%) | 2.0506 |
| Return 1W (%) | 1.5805 |
| Return 1M (%) | 4.3996 |
| Return YTD (%) | 27.3870 |
| Return 1Y (%) | 27.8249 |
| Annualized volatility (%) | 21.9922 |
| Beta vs SPY | 0.3713 |
| Max drawdown (%) | -11.9692 |
| Sharpe (rf=0) | 1.3071 |
| Downside deviation (rf=0, %) | 14.5575 |
| Sortino (rf=0) | 1.9746 |
| Historical VaR 95% (1D, %) | 1.8654 |
| Historical ES 95% (1D, %) | 2.9512 |
| Correlation vs SPY | 0.2156 |
| Tracking error vs SPY (%) | 23.1128 |
| P/E (trailing) | 30.17 |
| P/B | 2.43 |
| EV/EBITDA | 16.30 |
| Revenue growth (%) | 15.20 |
| Forward P/E (estimate) | 21.67 |
| Gross margin (%) | 52.76 |
| Operating margin (%) | 38.56 |
| Return on equity (%) | 8.27 |
| Free cash flow yield (%) | 2.46 |
| MA50 | 124.4620 |
| Close vs MA50 (%) | 2.7623 |
| MA200 | 119.1020 |
| Close vs MA200 (%) | 7.3870 |
| RSI (14, Wilder) | 59.6435 |
| MACD (12,26) | 0.7972 |
| MACD signal (9) | 0.3445 |
| MACD histogram | 0.4527 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'CP.TO': 272, 'SPY': 273}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 127.9000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 2.0506 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 1.5805 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 4.3996 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 27.3870 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 27.8249 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 21.9922 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 14.5575 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.9746 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.8654 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.9512 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2156 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 23.1128 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.3713 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -11.9692 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.3071 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 21.6692 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 52.7640 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 38.5640 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 8.2680 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.4633 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 30.1651 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 59.6435 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.4527 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 2.7623 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 7.3870 -> Clearly above the moving-average trend level.

## TAILWINDS

### Evercore ISI cuts Canadian Pacific Kansas City stock price target on cost pressures
- Summary: Evercore lowered CP.TO target price citing cost pressures, signaling potential downside risk for investors.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi3AFBVV95cUxNYjJCVmhEeGxRbkxESVhzMS1QUkNwYkxKWG9vSGYxZ0M4NjV1OWFMemlCTThxQWgtRi1XRGFPMnF3bWNsN083Yk1zM0k1ZTFGU2REMXNvNGstYWFudVVLZzhhTm1zQVFrVDFsLUJCSWdLSkd0eTJzZUVhRHpBWmhZeUpzOC1ydDh5OHpFTlNCWU5LY0Y3aXFIanIxYy1hOUtGbXpzLWJNZXhpUWItTmp4aU1yLUxRaldBbFhuNE56ZFZBR00wSWVqS1Z3dkJiUDU4MVV2Tnd5WWpwenYy?oc=5>

### Canadian Pacific Kansas City stock extends upward price move as buyer support outweighs weak momentum
- Summary: CP.TO shares rally as buyer support drives upward momentum, despite weak underlying performance.
- Date: 2026-11-02 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxPbDMxSDdzUEN6aGxCUS1BUm1DOFVZQ09lVGVobUJYOVlOUWI2ODNEaFppUVVmWnZkS2ptX2x4b3lKQmN2QjVLZXI3S0EwcW55UUlpNk9ZRWluLWtSY3RSUHh2eVZlQ09hWTlUYTFIX1NyeE5SNkxHMjJvZHNyeDFjZ2UtdkhVTTdVOFE?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Canadian Pacific Kansas City gets target hike as Scotiabank eyes earnings rebound
- Summary: Canadian Pacific Kansas City gets target hike as Scotiabank eyes earnings rebound
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxPYUJkTHlZcXRleVY0WGFWZV9HeWhhZm54S21feU9IdmJ3dDZpU1Y4ZV9yOFFWUnlHRDhHT1RCdGZrV2ZSQjdmdUczeHhYTVZfNXBqcC01Skd5dDRXQUtORjNEQkJucUF1VXBWa3FLaktqTFkxSGFMZ3ZtTFZGMGpROW8xTm8wMzBWWWh3S3pTMW50a1hDWVE3QVhTZ1ZjZG8?oc=5>

### Canadian Pacific Kansas City (CP) Reports Q3 Earnings: What Key Metrics Have to Say
- Summary: Canadian Pacific Kansas City (CP) Reports Q3 Earnings: What Key Metrics Have to Say
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihwFBVV95cUxOYWRReWJ0RmM4ZW9oZjFFZUtJbnV4Zlp4TW82UDJLWW1YV3B3Y2NGajRLaExycFZTUTdhXzZvUGFqNnNOU252WERTeFA1cnBPODducmhiMlhDQjRyam1jQjlodHRRQ2xLZDkydWFSMlpuNjYydUYwVjVVZVY1bnYyT1VOOU5SWU0?oc=5>

### Earnings Flash (CP.TO) Canadian Pacific Kansas City Limited Reports Q3 Revenue CA$4.22B, vs. FactSet Est of CA$4.21B
- Summary: CP reports Q3 revenue of CA$4.22B, slightly above estimates.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi4wFBVV95cUxQWXRoemkwWVRMdzgxbkpId1VqZDY4ekRTNmZ4VHdGVEhTX04wYUplSlREZm1uaFB1aVVtMWhrS3VlWnB2U1lxTUgtdXJ3dElVbFk1TWh0UWU5dGZzUGZHS2ZQSVZTTnMxNU5ZckpSa1QwX2JjZjdZeE1SWENZQlE4bjZTazMxdEFSN19yRXBKTHRITXozU1FHa05rYVVwZTVKRk96cl9HZ0lKZ3BoU1pxdkhoeWVCZ2didVFaT2piOUNnNVVXRE9HdWxzV09pbzUxUzJmSnFCLXU0cjE2MXVLZmZJaw?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **CP.TO** | **30.17** | **2.43** | **16.30** | **15.20** | **111,216,050,176.00 CAD** | **27.82** |
| CNR.TO | 22.28 | 4.86 | 13.79 | 14.60 | 106,356,793,344.00 CAD | 35.02 |
| UNP | 23.95 | 8.29 | 15.85 | 15.30 | 182,381,182,976.00 USD | 42.25 |
| NSC | 28.71 | 4.64 | 16.09 | 13.60 | 77,645,496,320.00 USD | 24.13 |

Peers fetched as_of: 2026-11-02; CP.TO reuses existing data (market data as_of: 2026-11-02); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-28
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-02

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
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

- https://news.google.com/rss/articles/CBMi3AFBVV95cUxNYjJCVmhEeGxRbkxESVhzMS1QUkNwYkxKWG9vSGYxZ0M4NjV1OWFMemlCTThxQWgtRi1XRGFPMnF3bWNsN083Yk1zM0k1ZTFGU2REMXNvNGstYWFudVVLZzhhTm1zQVFrVDFsLUJCSWdLSkd0eTJzZUVhRHpBWmhZeUpzOC1ydDh5OHpFTlNCWU5LY0Y3aXFIanIxYy1hOUtGbXpzLWJNZXhpUWItTmp4aU1yLUxRaldBbFhuNE56ZFZBR00wSWVqS1Z3dkJiUDU4MVV2Tnd5WWpwenYy?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxPbDMxSDdzUEN6aGxCUS1BUm1DOFVZQ09lVGVobUJYOVlOUWI2ODNEaFppUVVmWnZkS2ptX2x4b3lKQmN2QjVLZXI3S0EwcW55UUlpNk9ZRWluLWtSY3RSUHh2eVZlQ09hWTlUYTFIX1NyeE5SNkxHMjJvZHNyeDFjZ2UtdkhVTTdVOFE?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxPYUJkTHlZcXRleVY0WGFWZV9HeWhhZm54S21feU9IdmJ3dDZpU1Y4ZV9yOFFWUnlHRDhHT1RCdGZrV2ZSQjdmdUczeHhYTVZfNXBqcC01Skd5dDRXQUtORjNEQkJucUF1VXBWa3FLaktqTFkxSGFMZ3ZtTFZGMGpROW8xTm8wMzBWWWh3S3pTMW50a1hDWVE3QVhTZ1ZjZG8?oc=5
- https://news.google.com/rss/articles/CBMihwFBVV95cUxOYWRReWJ0RmM4ZW9oZjFFZUtJbnV4Zlp4TW82UDJLWW1YV3B3Y2NGajRLaExycFZTUTdhXzZvUGFqNnNOU252WERTeFA1cnBPODducmhiMlhDQjRyam1jQjlodHRRQ2xLZDkydWFSMlpuNjYydUYwVjVVZVY1bnYyT1VOOU5SWU0?oc=5
- https://news.google.com/rss/articles/CBMi4wFBVV95cUxQWXRoemkwWVRMdzgxbkpId1VqZDY4ekRTNmZ4VHdGVEhTX04wYUplSlREZm1uaFB1aVVtMWhrS3VlWnB2U1lxTUgtdXJ3dElVbFk1TWh0UWU5dGZzUGZHS2ZQSVZTTnMxNU5ZckpSa1QwX2JjZjdZeE1SWENZQlE4bjZTazMxdEFSN19yRXBKTHRITXozU1FHa05rYVVwZTVKRk96cl9HZ0lKZ3BoU1pxdkhoeWVCZ2didVFaT2piOUNnNVVXRE9HdWxzV09pbzUxUzJmSnFCLXU0cjE2MXVLZmZJaw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
