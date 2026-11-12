# TSM Intelligence Report

- ticker: **TSM**
- Report as_of: **2026-11-11**
- Market data as_of: **2026-11-11**
- Quant sources: https://finance.yahoo.com/quote/TSM/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/TSM/key-statistics/
- AI analysis snapshot as_of: **2026-11-11**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-12T05:50:23.870813+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 4, 'ai': 9, 'unknown': 0, 'irrelevant': 11})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **9** exact headline/source/date matches; prior report **20261111T043601Z-d14951e6/TSM** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'directional_claim_without_event_type': 1, 'short_term_price_move_in_structural_risks': 1}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 14 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 25.0%; oldest publication 2026-11-09

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 413.3500 |
| Return 1D (%) | 4.2549 |
| Return 1W (%) | 4.4473 |
| Return 1M (%) | -8.8152 |
| Return YTD (%) | 37.0891 |
| Return 1Y (%) | 43.4642 |
| Annualized volatility (%) | 41.8111 |
| Beta vs SPY | 2.1606 |
| Max drawdown (%) | -27.3158 |
| Sharpe (rf=0) | 1.0762 |
| Downside deviation (rf=0, %) | 28.6806 |
| Sortino (rf=0) | 1.5689 |
| Historical VaR 95% (1D, %) | 4.2423 |
| Historical ES 95% (1D, %) | 5.7594 |
| Correlation vs SPY | 0.7095 |
| Tracking error vs SPY (%) | 33.4988 |
| P/E (trailing) | 26.79 |
| P/B | 78.88 |
| EV/EBITDA | 3.86 |
| Revenue growth (%) | 50.90 |
| Forward P/E (estimate) | 17.68 |
| Gross margin (%) | 65.85 |
| Operating margin (%) | 57.96 |
| Return on equity (%) | 41.85 |
| Free cash flow yield (%) | N/A |
| MA50 | 430.4703 |
| Close vs MA50 (%) | -3.9771 |
| MA200 | 401.0311 |
| Close vs MA200 (%) | 3.0718 |
| RSI (14, Wilder) | 49.6348 |
| MACD (12,26) | -12.3139 |
| MACD signal (9) | -11.4158 |
| MACD histogram | -0.8981 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'TSM': 280, 'SPY': 280}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 413.3500 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 4.2549 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 4.4473 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -8.8152 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 37.0891 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 43.4642 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 41.8111 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 28.6806 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.5689 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.2423 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.7594 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.7095 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 33.4988 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 2.1606 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -27.3158 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.0762 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 17.6756 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 65.8460 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 57.9600 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 41.8550 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 26.7887 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 49.6348 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.8981 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -3.9771 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 3.0718 -> Slightly above the moving-average trend level.

## TAILWINDS

### TSMC Shares Rise 1.54% After Hours - Alphabet (NASDAQ:GOOGL), Alphabet (NASDAQ:GOOG)
- Summary: TSMC Shares Rise 1.54% After Hours - Alphabet (NASDAQ:GOOGL), Alphabet (NASDAQ:GOOG)
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxNY1JnT1VFWkxmdFRWZ1Y2X2VBcjJCcEM3NzRMR1RiOHVPdG8tU1M5b2xHSC1rc3FoZzNxTGljTmZUNTlVbXFlTm1YQkdxNDFsaVNCOFFNQjVfYUsxb2lXeWhZMWRRYm1oOXh5QWFsRUlxaE9sR3FuVDZPXzdqbUxScm5VZlZkWTRHX0xNRk5oLUUtakVzby1KbVJzMzk2eWNQLUZnSjJKTG5GZVBzSFNPRkRsYw?oc=5>

### TSMC’s Revenue Rises 60% in a Sign of Resilient AI Chip Demand
- Summary: TSMC’s Revenue Rises 60% in a Sign of Resilient AI Chip Demand
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxONGRJQkVuVkdsUDBxN0RaX2F3a0FqWmlUajBQX1NkY01SY293VnZicy1OYUMwaFJkMUtMczQtVi01c25RYnlianZwNGI0Umh0MTNhbjFSU1p0MHZMVUl4VFdSN3ZvZW5ncHV4VlU2MmJDbktNNlcxSG5vTm40LTE0X20wREg5X05jOHRQeFlBVkdnTk9ISEFvVjZlOExmSHMzMkNPSS0wMkFQSElsTzlBQjJ4M0M5R0d6MmNJLWFqQQ?oc=5>

### TSMC Reports 59.7% Rise in October Revenue to NT$367.47 Billion Amid AI Chip Demand
- Summary: TSMC Reports 59.7% Rise in October Revenue to NT$367.47 Billion Amid AI Chip Demand
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxNNVQtMVpnMEU0a2NBQWRlazZlb0Z5dmxQOHREaGlnTDVFVFNaNE1OeUJVajZ5b0JqdjFjOW1Na0I4VnZtT1hTdVZMNi0zM2ZyYk1SdUphWmRWNjhJeU1la2hJY3pwcDUxT21WWjVjYjZlNnhDOU9mM2hTSDQyeHhWaGpQN1FjaE1wdGt4RkZOZw?oc=5>

### Taiwan Semiconductor Sales Jump 60% In October As AI Boom Continues
- Summary: TSM reports a 60% sales increase in October driven by AI demand.
- Date: 2026-11-10 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxNdXVPN1FxVkpoWXdpeG9DdDJyNEl5aUlMWF8yZVM2aG1SNkdTbUFMNnQwQWFMMjhkNjJkOVdjb19IQTRtQzJBZ085alZEdjVpLTFMek9haGlValNDZzFTR3lfNnpmc1BPRk44N2RuWHR1dE03SWdTMXhHVGRSQm1ONkJpSkJVZmhvRzdLUEQwdUx4VHUzbnpN?oc=5>

### What Does Taiwan Semiconductor Manufacturing (TSM) AI Revenue Surge Mean For Investors?
- Summary: TSM's AI revenue surge signals strong product demand, boosting investor confidence.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxPdHZ6QnVWUlEtOE5fb0dnOGRMbEttQ1FIM0dTdy1CZzloTk1Tc0RaNm40VTB1YjR1bmpnVmRFelE5RjlyeGJQQl9lY2s5SThnZ1d2QmRHbnM0cHVFTnZCcXh6QzRqZVN0TFoyOGVpSExjYm56czYydkdZLV9YX1RYYWdBY1hMRWlTQVhWR2MxQmp1clVoTW93b2J6NVdTZEdjdGZMc041NldwODR4?oc=5>

### Wedbush Has a Strong Message for TSMC Stock Fans
- Summary: Wedbush analyst endorses TSMC, suggesting positive outlook.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxORk9oU1JVdGlRMFByRzFoVC1yU2d2TjlIMUVmdnVIRXY3am53NkdfaF9LNTloYWtSUUQyS0JvakxRU1lXNTBnbTkyR0I2OE9IUHJsbGFNRl8wX0RGdktPQjdvRlliek05TUVpa0JwTjNJSXpZUDdEY21FNDM4MHl6UWpzeTB1OWluSXpwZmpQVFVLRWZ3RmI4N2VLZDBwenc?oc=5>

### Why Is Taiwan Semiconductor Stock Gaining Wednesday?
- Summary: TSM shares rise, indicating positive market sentiment and potential short-term upside.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxNWGFvVFk2WFI4T0VZN2JmVHA5Zk41VDNUWHdlN2loVTJFTW5LakFHY3V4TjhoMk9ZZy01YmZ2eUxONlFEZlhPUmhldzVHYjlObFJzLXVTOTEzN3E3a21aY0ZmaHFEN1VNRm10UVpwR0EtVTIycFk3MkNITHp4RF8zaVdPVTM2NWx3T3hoaWRLUVlYOVNMM2Q0M0lOUVhoQlpyS1dGOFExUm53T1VDaEpHdmJB?oc=5>

## HEADWINDS

### Taiwan Semiconductor Manufacturing (TSM) Stock Could Be 7% Undervalued Despite Fab Expansion Plans
- Summary: Analysts suggest TSMC may be undervalued, indicating potential downside risk.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxNclhidVc5Z2VTNE9uZzRCcldGRDUzLXcyc1otalhRaExZNHR2cVRPNk03Z052ekExdUt1QzgxWGkya1NHcElYeWowOXRESHM1UFlsZUx3Yi14bUFHcHp3bVJuTlJPUDlzZFZjYV9URFR6b19NQVRtYUhMdFNobGIwWWFJb1JwODdWM1h6ZjQ4RS1obDRfNUkxdHdGUDdFR0JqbkhnX2ZzVUtRTml2Nmc?oc=5>

## CATALYSTS

### TSM Stock Jumps Premarket After Board Approves $1B Investment In Anthropic And OpenAI, Dividend Raise
- Summary: TSM Stock Jumps Premarket After Board Approves $1B Investment In Anthropic And OpenAI, Dividend Raise
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi8gFBVV95cUxQekU3N2oxZW5RcFNsQV9HVlJpbGN2X3IyVXp4bnhDazg1cmtIUUItRklGbE5xTXV0cmx5bW53TXA3U2tYS3Jaa1FFSXZVZ1RPWF9DWjQ3LU5rSTFZeklEWDl0ZEh6dU41N2lYYzRYTjNzck9JVjRZX2JJblNXOXVINU5aR3plWlczdFh0azBJREswcDRPb0EzekVGRkRoQkhfOEIwUE5IZkJhUUZzSkh4dVNmTm44VTNVQ1JOa1YyZVR6dmZVOFhJQUZ2UTN0X2Zqb0dlNUEtOUlHTi03ZEdjQ3d6V0MwSTQ5b2VDRVVKeC1Jdw?oc=5>

### Taiwan Semiconductor Manufacturing Co Ltd Stock (TSM) Opened Up by 3.15% on Nov 11: What Investors Need To Know
- Summary: TSM shares rose 3.15% on Nov 11, indicating a short‑term market move.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxNTVZZZHRRUTFaSFZZWGJLVi1OaFdDWFN1NFZkazBSTV9ka2NMeDVvb2Z1R28xWnYweFBCWjR3MlVTRjhOdEdaNUZhUWFUcmpyMU5TeUJXX00yV29kOTdXM3JQNGhpc2piM20yc2RjRlZJNVFjQ1Y5UnpGV2RaTVRIVXVqcklDSlktS3c?oc=5>

### Marvell and Intel Rally 7% as CoreWeave's Results Reignite the AI Chip Trade; Taiwan Semiconductor Climbs 4%
- Summary: TSM shares climbed 4% following AI chip trade rally, a short‑term market move.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi4gFBVV95cUxOams4aFViZ0MzZnZKUXdOUEUtcVJ0QzNQTXpLSjExRjctOVdOZnhGZDU2WVlQWFJxMUZYNjFabC0tU1NMekFxT21VdjktUkNFZDZ4WmRFMi11MHY3MllzWXRPV3FhbjZ6dkxDV2RFMEY4XzVfZzdUTVlFcy01WU5PelljOElGb0dmekt0ZmZsbzU1NWJnTVczU0loYVpfNkJYQWUyZ1Y0MnBXaXlqTDN2MFZBME5xZFdVcE1iMGxWbVo3bnY4TkxTVnBMYUNON2FBT1J4YlVQQmg2NnRyZ2pmbU1R?oc=5>

### Taiwan Semiconductor Manufacturing (TSM) executive Yoo bought 54 shares for $3,807 at $70.50
- Summary: TSM executive Yoo purchased 54 shares, indicating confidence in the company.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxQSGFUdFVUWkRaOVlPd3AwNnhWX0s4UTFLbXplYkVkTlMwcEYzX255UDBtR2xWeTlfV21Lb3o1eDl1ZWpGelV0RlI3VWVJSzNsd0c5cU1BSnVqaTRESnZxSlJuWVNoVk9aNlBFR1hqZjZ4YVFuNkktV3BaQXVDR1REbkZZTU5Na2pfM05ibTNqMkVEekFkR1ROM1Q3WQ?oc=5>

## RISKS

### What Is Going on With Taiwan Semiconductor Stock on Monday?
- Summary: Inquiry about TSM stock movement on Monday.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxNdlVNUlBPLXliejk5cW53UXNqT0FxZTBBUnQ1ZlhjS2dldDZGSjl2QUsyT3BGY2Q3OGRkUWw3VmV1TFgxVU05eGdJRXZRckQ0ZXU0di1nMGdoYzhJX3YzWGxVcGIxbm9FR0Z2bEpQenM4bkhsNkcydFVCLUtOeHVMd1htQ0ZuV185SVV4bTgzM2l5YjlONURuc0FyWHN2NFpyS2hSdDJyMm8yRE5TWGVZcg?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **TSM** | **26.79** | **78.88** | **3.86** | **50.90** | **2,143,828,574,208.00 USD** | **43.46** |
| UMC | 15.17 | 2.77 | -0.27 | 25.60 | 40,325,324,800.00 USD | 121.72 |
| GFS | 122.43 | 2.00 | 11.51 | 12.50 | 23,886,678,016.00 USD | 23.58 |
| INTC | N/A | 2.89 | 18.03 | 20.90 | 332,187,500,544.00 USD | 64.99 |

Peers fetched as_of: 2026-11-11; TSM reuses existing data (market data as_of: 2026-11-11); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-15
- Next expected earnings: 2027-01-14 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-11

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: N/A
- Filing date: N/A
- Revenue (latest available single quarter): N/A
- Net income (latest available single quarter): N/A
- SEC link: N/A

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiswFBVV95cUxNY1JnT1VFWkxmdFRWZ1Y2X2VBcjJCcEM3NzRMR1RiOHVPdG8tU1M5b2xHSC1rc3FoZzNxTGljTmZUNTlVbXFlTm1YQkdxNDFsaVNCOFFNQjVfYUsxb2lXeWhZMWRRYm1oOXh5QWFsRUlxaE9sR3FuVDZPXzdqbUxScm5VZlZkWTRHX0xNRk5oLUUtakVzby1KbVJzMzk2eWNQLUZnSjJKTG5GZVBzSFNPRkRsYw?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxONGRJQkVuVkdsUDBxN0RaX2F3a0FqWmlUajBQX1NkY01SY293VnZicy1OYUMwaFJkMUtMczQtVi01c25RYnlianZwNGI0Umh0MTNhbjFSU1p0MHZMVUl4VFdSN3ZvZW5ncHV4VlU2MmJDbktNNlcxSG5vTm40LTE0X20wREg5X05jOHRQeFlBVkdnTk9ISEFvVjZlOExmSHMzMkNPSS0wMkFQSElsTzlBQjJ4M0M5R0d6MmNJLWFqQQ?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxNNVQtMVpnMEU0a2NBQWRlazZlb0Z5dmxQOHREaGlnTDVFVFNaNE1OeUJVajZ5b0JqdjFjOW1Na0I4VnZtT1hTdVZMNi0zM2ZyYk1SdUphWmRWNjhJeU1la2hJY3pwcDUxT21WWjVjYjZlNnhDOU9mM2hTSDQyeHhWaGpQN1FjaE1wdGt4RkZOZw?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxNdXVPN1FxVkpoWXdpeG9DdDJyNEl5aUlMWF8yZVM2aG1SNkdTbUFMNnQwQWFMMjhkNjJkOVdjb19IQTRtQzJBZ085alZEdjVpLTFMek9haGlValNDZzFTR3lfNnpmc1BPRk44N2RuWHR1dE03SWdTMXhHVGRSQm1ONkJpSkJVZmhvRzdLUEQwdUx4VHUzbnpN?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxPdHZ6QnVWUlEtOE5fb0dnOGRMbEttQ1FIM0dTdy1CZzloTk1Tc0RaNm40VTB1YjR1bmpnVmRFelE5RjlyeGJQQl9lY2s5SThnZ1d2QmRHbnM0cHVFTnZCcXh6QzRqZVN0TFoyOGVpSExjYm56czYydkdZLV9YX1RYYWdBY1hMRWlTQVhWR2MxQmp1clVoTW93b2J6NVdTZEdjdGZMc041NldwODR4?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxORk9oU1JVdGlRMFByRzFoVC1yU2d2TjlIMUVmdnVIRXY3am53NkdfaF9LNTloYWtSUUQyS0JvakxRU1lXNTBnbTkyR0I2OE9IUHJsbGFNRl8wX0RGdktPQjdvRlliek05TUVpa0JwTjNJSXpZUDdEY21FNDM4MHl6UWpzeTB1OWluSXpwZmpQVFVLRWZ3RmI4N2VLZDBwenc?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxNWGFvVFk2WFI4T0VZN2JmVHA5Zk41VDNUWHdlN2loVTJFTW5LakFHY3V4TjhoMk9ZZy01YmZ2eUxONlFEZlhPUmhldzVHYjlObFJzLXVTOTEzN3E3a21aY0ZmaHFEN1VNRm10UVpwR0EtVTIycFk3MkNITHp4RF8zaVdPVTM2NWx3T3hoaWRLUVlYOVNMM2Q0M0lOUVhoQlpyS1dGOFExUm53T1VDaEpHdmJB?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxNclhidVc5Z2VTNE9uZzRCcldGRDUzLXcyc1otalhRaExZNHR2cVRPNk03Z052ekExdUt1QzgxWGkya1NHcElYeWowOXRESHM1UFlsZUx3Yi14bUFHcHp3bVJuTlJPUDlzZFZjYV9URFR6b19NQVRtYUhMdFNobGIwWWFJb1JwODdWM1h6ZjQ4RS1obDRfNUkxdHdGUDdFR0JqbkhnX2ZzVUtRTml2Nmc?oc=5
- https://news.google.com/rss/articles/CBMi8gFBVV95cUxQekU3N2oxZW5RcFNsQV9HVlJpbGN2X3IyVXp4bnhDazg1cmtIUUItRklGbE5xTXV0cmx5bW53TXA3U2tYS3Jaa1FFSXZVZ1RPWF9DWjQ3LU5rSTFZeklEWDl0ZEh6dU41N2lYYzRYTjNzck9JVjRZX2JJblNXOXVINU5aR3plWlczdFh0azBJREswcDRPb0EzekVGRkRoQkhfOEIwUE5IZkJhUUZzSkh4dVNmTm44VTNVQ1JOa1YyZVR6dmZVOFhJQUZ2UTN0X2Zqb0dlNUEtOUlHTi03ZEdjQ3d6V0MwSTQ5b2VDRVVKeC1Jdw?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxNTVZZZHRRUTFaSFZZWGJLVi1OaFdDWFN1NFZkazBSTV9ka2NMeDVvb2Z1R28xWnYweFBCWjR3MlVTRjhOdEdaNUZhUWFUcmpyMU5TeUJXX00yV29kOTdXM3JQNGhpc2piM20yc2RjRlZJNVFjQ1Y5UnpGV2RaTVRIVXVqcklDSlktS3c?oc=5
- https://news.google.com/rss/articles/CBMi4gFBVV95cUxOams4aFViZ0MzZnZKUXdOUEUtcVJ0QzNQTXpLSjExRjctOVdOZnhGZDU2WVlQWFJxMUZYNjFabC0tU1NMekFxT21VdjktUkNFZDZ4WmRFMi11MHY3MllzWXRPV3FhbjZ6dkxDV2RFMEY4XzVfZzdUTVlFcy01WU5PelljOElGb0dmekt0ZmZsbzU1NWJnTVczU0loYVpfNkJYQWUyZ1Y0MnBXaXlqTDN2MFZBME5xZFdVcE1iMGxWbVo3bnY4TkxTVnBMYUNON2FBT1J4YlVQQmg2NnRyZ2pmbU1R?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxQSGFUdFVUWkRaOVlPd3AwNnhWX0s4UTFLbXplYkVkTlMwcEYzX255UDBtR2xWeTlfV21Lb3o1eDl1ZWpGelV0RlI3VWVJSzNsd0c5cU1BSnVqaTRESnZxSlJuWVNoVk9aNlBFR1hqZjZ4YVFuNkktV3BaQXVDR1REbkZZTU5Na2pfM05ibTNqMkVEekFkR1ROM1Q3WQ?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxNdlVNUlBPLXliejk5cW53UXNqT0FxZTBBUnQ1ZlhjS2dldDZGSjl2QUsyT3BGY2Q3OGRkUWw3VmV1TFgxVU05eGdJRXZRckQ0ZXU0di1nMGdoYzhJX3YzWGxVcGIxbm9FR0Z2bEpQenM4bkhsNkcydFVCLUtOeHVMd1htQ0ZuV185SVV4bTgzM2l5YjlONURuc0FyWHN2NFpyS2hSdDJyMm8yRE5TWGVZcg?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
