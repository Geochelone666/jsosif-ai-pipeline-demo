# CP.TO Intelligence Report

- ticker: **CP.TO**
- Report as_of: **2026-11-07**
- Market data as_of: **2026-11-06**
- Quant sources: https://finance.yahoo.com/quote/CP.TO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/CP.TO/key-statistics/
- AI analysis snapshot as_of: **2026-11-07**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-08T04:21:31.314199+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 4, 'rule': 3, 'ai': 1, 'unknown': 0})
- AI model(s) actually used: **N/A (no successful AI classification call)**
- Verified recent classification reuse: **1** exact headline/source/date matches; prior report **20261107T043155Z-acc5f41d/CP.TO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 4 unique headlines; 2 named publishers; 0 exact duplicates; 4 HTTPS source links; largest publisher share 75.0%; oldest publication 2026-11-02

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 129.9700 |
| Return 1D (%) | -1.0657 |
| Return 1W (%) | 3.7022 |
| Return 1M (%) | 7.0240 |
| Return YTD (%) | 29.4487 |
| Return 1Y (%) | 34.7812 |
| Annualized volatility (%) | 22.0784 |
| Beta vs SPY | 0.3512 |
| Max drawdown (%) | -11.9692 |
| Sharpe (rf=0) | 1.4679 |
| Downside deviation (rf=0, %) | 14.4242 |
| Sortino (rf=0) | 2.2469 |
| Historical VaR 95% (1D, %) | 1.8632 |
| Historical ES 95% (1D, %) | 2.9374 |
| Correlation vs SPY | 0.2148 |
| Tracking error vs SPY (%) | 23.4631 |
| P/E (trailing) | 30.02 |
| P/B | 2.47 |
| EV/EBITDA | 16.51 |
| Revenue growth (%) | 15.20 |
| Forward P/E (estimate) | 22.03 |
| Gross margin (%) | 52.76 |
| Operating margin (%) | 38.56 |
| Return on equity (%) | 8.27 |
| Free cash flow yield (%) | 2.42 |
| MA50 | 124.3782 |
| Close vs MA50 (%) | 4.4958 |
| MA200 | 119.7246 |
| Close vs MA200 (%) | 8.5575 |
| RSI (14, Wilder) | 61.0742 |
| MACD (12,26) | 1.7419 |
| MACD signal (9) | 1.0235 |
| MACD histogram | 0.7185 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'CP.TO': 276, 'SPY': 277}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 129.9700 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.0657 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 3.7022 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 7.0240 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 29.4487 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 34.7812 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 22.0784 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 14.4242 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 2.2469 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.8632 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.9374 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2148 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 23.4631 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.3512 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -11.9692 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.4679 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 22.0330 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 52.7640 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 38.5640 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 8.2680 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.4241 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 30.0162 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 61.0742 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.7185 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 4.4958 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 8.5575 -> Clearly above the moving-average trend level.

## TAILWINDS

### Canadian Pacific Kansas City stock gains about 2.5% after stronger Q3 revenue and ongoing Kansas City Southern integration
- Summary: Canadian Pacific Kansas City stock gains about 2.5% after stronger Q3 revenue and ongoing Kansas City Southern integration
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxQMHlkV1cxRWxGWjhGbEI3WTRka05OczJNdGhQZ0xLQjFYa3JlX0Zka3A5Sm50VDFqZlBESl8wbDB1ZzAtNm1CTkV0Rnk4c1RBa0JJY19mZUp2YzE5cVVIa0NULTc2Q0lzOEpJTklfZWY2NEo1bGdpUHpIOEpyOWJDUlE3b1czTU5Rc2l1TEFlalBuN0hNa0NB?oc=5>

## HEADWINDS

### Canadian Pacific Kansas City stock faces fuel pressure after Q3 growth
- Summary: Canadian Pacific Kansas City stock faces fuel pressure after Q3 growth
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizgFBVV95cUxPZFVEdjVCRUc3eE1iUGJZUHhjczZib05WR2N6cWthQldvOHBvNzliWHBnVm10amNQTjlkZk9QV3pyV0g3N0I5UE9vWXctaDJ2OV9GVm02RHdZM05XaHg0TVVOUWFmdXp6ZkpPbVdTaHRkX2pSLUlhVUpQSW1Yc0x4U1NtbHlBdEMwZnVSMDkycF90enphc1I3eDRESEswem9NZWw0LWNtUHJQX3gwT0xUTjM5VFNxXzQ2ODU3ZGFxYmdfYWYwYzEtbFNjeFhaZw?oc=5>

## CATALYSTS

### Canadian Pacific Kansas City stock posts 15% Q3 revenue growth
- Summary: Canadian Pacific Kansas City stock posts 15% Q3 revenue growth
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxOVm1IazNZZkJ2MWJoRkJwOEdEbXNOSHlVN1d5OUR1YmR6cktiT3J4Ni1EMEFyeHBrZFNUWGxuOGNQNHhHOGhpLUd1M0VmT09tWlBJYmZtLVg5V0M4N2dMa1ZmSEZTa2xTZV9WaWh6Nkk3WUtROEpSR3hTWkZjZkZRXzNlRWRQMnJWWFZuVGhtYkFXRDJsUUR2THdueDBxS3dyQmdjUnFWSkxkVDBqLTU4UnVwbUFCczJVQml2MkYzUGsyUQ?oc=5>

### Canadian Pacific Kansas City stock: Revenue rises 15 percent amid fuel pressure
- Summary: Revenue up 15% despite fuel cost pressures, indicating operational resilience.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi2AFBVV95cUxNa1ZSdUZKSmVtTlZycDlFdWFIN0tocnpSN2t2Z3JMM0R5Tm0xMjBndUtHM2ZySUFUZVpCRkh5ZFNnMUVRaFZuR0QzMi1YNFAtTjc5SFRsem5XaHgxWm85NzNnaXVJUUg5N29UelE1NF9EVF9aRXBKczZ4VndHeXNwTjJHRkdoVWJ1MkQ0dWxxVktDRUtDSW9EQW9fVFY2YmYyNzEzaERCeUo3ZWFYay11S0FMRlZQNXVwWHl2RmE3QzRtMEp5T0F6UjZSWVJKMzdFd0NicHhrT2c?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **CP.TO** | **30.02** | **2.47** | **16.51** | **15.20** | **113,016,029,184.00 CAD** | **34.78** |
| CNR.TO | 22.01 | 4.80 | 13.65 | 14.60 | 105,073,434,624.00 CAD | 34.41 |
| UNP | 22.63 | 7.83 | 15.09 | 15.30 | 172,376,948,736.00 USD | 35.91 |
| NSC | 26.82 | 4.30 | 15.09 | 13.60 | 71,863,861,248.00 USD | 15.89 |

Peers fetched as_of: 2026-11-07; CP.TO reuses existing data (market data as_of: 2026-11-06); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-28
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-07

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
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

- https://news.google.com/rss/articles/CBMilwFBVV95cUxQMHlkV1cxRWxGWjhGbEI3WTRka05OczJNdGhQZ0xLQjFYa3JlX0Zka3A5Sm50VDFqZlBESl8wbDB1ZzAtNm1CTkV0Rnk4c1RBa0JJY19mZUp2YzE5cVVIa0NULTc2Q0lzOEpJTklfZWY2NEo1bGdpUHpIOEpyOWJDUlE3b1czTU5Rc2l1TEFlalBuN0hNa0NB?oc=5
- https://news.google.com/rss/articles/CBMizgFBVV95cUxPZFVEdjVCRUc3eE1iUGJZUHhjczZib05WR2N6cWthQldvOHBvNzliWHBnVm10amNQTjlkZk9QV3pyV0g3N0I5UE9vWXctaDJ2OV9GVm02RHdZM05XaHg0TVVOUWFmdXp6ZkpPbVdTaHRkX2pSLUlhVUpQSW1Yc0x4U1NtbHlBdEMwZnVSMDkycF90enphc1I3eDRESEswem9NZWw0LWNtUHJQX3gwT0xUTjM5VFNxXzQ2ODU3ZGFxYmdfYWYwYzEtbFNjeFhaZw?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxOVm1IazNZZkJ2MWJoRkJwOEdEbXNOSHlVN1d5OUR1YmR6cktiT3J4Ni1EMEFyeHBrZFNUWGxuOGNQNHhHOGhpLUd1M0VmT09tWlBJYmZtLVg5V0M4N2dMa1ZmSEZTa2xTZV9WaWh6Nkk3WUtROEpSR3hTWkZjZkZRXzNlRWRQMnJWWFZuVGhtYkFXRDJsUUR2THdueDBxS3dyQmdjUnFWSkxkVDBqLTU4UnVwbUFCczJVQml2MkYzUGsyUQ?oc=5
- https://news.google.com/rss/articles/CBMi2AFBVV95cUxNa1ZSdUZKSmVtTlZycDlFdWFIN0tocnpSN2t2Z3JMM0R5Tm0xMjBndUtHM2ZySUFUZVpCRkh5ZFNnMUVRaFZuR0QzMi1YNFAtTjc5SFRsem5XaHgxWm85NzNnaXVJUUg5N29UelE1NF9EVF9aRXBKczZ4VndHeXNwTjJHRkdoVWJ1MkQ0dWxxVktDRUtDSW9EQW9fVFY2YmYyNzEzaERCeUo3ZWFYay11S0FMRlZQNXVwWHl2RmE3QzRtMEp5T0F6UjZSWVJKMzdFd0NicHhrT2c?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
