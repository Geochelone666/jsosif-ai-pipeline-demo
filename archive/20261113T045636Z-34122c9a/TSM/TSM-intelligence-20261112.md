# TSM Intelligence Report

- ticker: **TSM**
- Report as_of: **2026-11-12**
- Market data as_of: **2026-11-12**
- Quant sources: https://finance.yahoo.com/quote/TSM/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/TSM/key-statistics/
- AI analysis snapshot as_of: **2026-11-12**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-13T04:58:56.341687+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 3, 'ai': 12, 'unknown': 0, 'irrelevant': 9})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **11** exact headline/source/date matches; prior report **20261112T054014Z-6c47e7f9/TSM** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'directional_claim_without_event_type': 1, 'short_term_price_move_in_structural_risks': 1}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 12 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 29.17%; oldest publication 2026-11-09

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 405.4900 |
| Return 1D (%) | -1.9015 |
| Return 1W (%) | 14.8372 |
| Return 1M (%) | -8.7454 |
| Return YTD (%) | 34.4823 |
| Return 1Y (%) | 41.0025 |
| Annualized volatility (%) | 41.8615 |
| Beta vs SPY | 2.1632 |
| Max drawdown (%) | -27.3158 |
| Sharpe (rf=0) | 1.0338 |
| Downside deviation (rf=0, %) | 28.7432 |
| Sortino (rf=0) | 1.5057 |
| Historical VaR 95% (1D, %) | 4.2423 |
| Historical ES 95% (1D, %) | 5.7594 |
| Correlation vs SPY | 0.7098 |
| Tracking error vs SPY (%) | 33.5388 |
| P/E (trailing) | 26.28 |
| P/B | 77.38 |
| EV/EBITDA | 3.77 |
| Revenue growth (%) | 50.90 |
| Forward P/E (estimate) | 17.34 |
| Gross margin (%) | 65.85 |
| Operating margin (%) | 57.96 |
| Return on equity (%) | 41.85 |
| Free cash flow yield (%) | N/A |
| MA50 | 430.2924 |
| Close vs MA50 (%) | -5.7641 |
| MA200 | 401.3604 |
| Close vs MA200 (%) | 1.0289 |
| RSI (14, Wilder) | 47.2747 |
| MACD (12,26) | -11.0914 |
| MACD signal (9) | -11.3509 |
| MACD histogram | 0.2596 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'TSM': 281, 'SPY': 281}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 405.4900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.9015 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 14.8372 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -8.7454 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 34.4823 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 41.0025 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 41.8615 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 28.7432 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.5057 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.2423 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.7594 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.7098 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 33.5388 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 2.1632 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -27.3158 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.0338 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 17.3395 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 65.8460 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 57.9600 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 41.8550 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 26.2793 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 47.2747 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.2596 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -5.7641 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 1.0289 -> Slightly above the moving-average trend level.

## TAILWINDS

### TSMC Shares Rise 1.54% After Hours - Alphabet (NASDAQ:GOOGL), Alphabet (NASDAQ:GOOG)
- Summary: TSMC Shares Rise 1.54% After Hours - Alphabet (NASDAQ:GOOGL), Alphabet (NASDAQ:GOOG)
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxNY1JnT1VFWkxmdFRWZ1Y2X2VBcjJCcEM3NzRMR1RiOHVPdG8tU1M5b2xHSC1rc3FoZzNxTGljTmZUNTlVbXFlTm1YQkdxNDFsaVNCOFFNQjVfYUsxb2lXeWhZMWRRYm1oOXh5QWFsRUlxaE9sR3FuVDZPXzdqbUxScm5VZlZkWTRHX0xNRk5oLUUtakVzby1KbVJzMzk2eWNQLUZnSjJKTG5GZVBzSFNPRkRsYw?oc=5>

### Taiwan Semiconductor Sales Jump 60% In October As AI Boom Continues
- Summary: TSM reports a 60% sales increase in October driven by AI demand.
- Date: 2026-11-10 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxNdXVPN1FxVkpoWXdpeG9DdDJyNEl5aUlMWF8yZVM2aG1SNkdTbUFMNnQwQWFMMjhkNjJkOVdjb19IQTRtQzJBZ085alZEdjVpLTFMek9haGlValNDZzFTR3lfNnpmc1BPRk44N2RuWHR1dE03SWdTMXhHVGRSQm1ONkJpSkJVZmhvRzdLUEQwdUx4VHUzbnpN?oc=5>

### Why Is Taiwan Semiconductor Stock Gaining Wednesday?
- Summary: TSM shares rise, indicating positive market sentiment and potential short-term upside.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxNWGFvVFk2WFI4T0VZN2JmVHA5Zk41VDNUWHdlN2loVTJFTW5LakFHY3V4TjhoMk9ZZy01YmZ2eUxONlFEZlhPUmhldzVHYjlObFJzLXVTOTEzN3E3a21aY0ZmaHFEN1VNRm10UVpwR0EtVTIycFk3MkNITHp4RF8zaVdPVTM2NWx3T3hoaWRLUVlYOVNMM2Q0M0lOUVhoQlpyS1dGOFExUm53T1VDaEpHdmJB?oc=5>

### What Does Taiwan Semiconductor Manufacturing (TSM) AI Revenue Surge Mean For Investors?
- Summary: TSM's AI revenue surge signals strong product demand, boosting investor confidence.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxPdHZ6QnVWUlEtOE5fb0dnOGRMbEttQ1FIM0dTdy1CZzloTk1Tc0RaNm40VTB1YjR1bmpnVmRFelE5RjlyeGJQQl9lY2s5SThnZ1d2QmRHbnM0cHVFTnZCcXh6QzRqZVN0TFoyOGVpSExjYm56czYydkdZLV9YX1RYYWdBY1hMRWlTQVhWR2MxQmp1clVoTW93b2J6NVdTZEdjdGZMc041NldwODR4?oc=5>

### Wedbush Has a Strong Message for TSMC Stock Fans
- Summary: Wedbush analyst endorses TSMC, suggesting positive outlook.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxORk9oU1JVdGlRMFByRzFoVC1yU2d2TjlIMUVmdnVIRXY3am53NkdfaF9LNTloYWtSUUQyS0JvakxRU1lXNTBnbTkyR0I2OE9IUHJsbGFNRl8wX0RGdktPQjdvRlliek05TUVpa0JwTjNJSXpZUDdEY21FNDM4MHl6UWpzeTB1OWluSXpwZmpQVFVLRWZ3RmI4N2VLZDBwenc?oc=5>

### Bernstein’s Mark Li Raised His Taiwan Semiconductor Manufacturing (TSM) Target to $600. Here’s What Changed
- Summary: Analyst raises TSM target price to $600, indicating bullish outlook.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQOGpUMzJxTHl5SzNTODh3bFBOVlJzSV95TGNNbTRnWG52S0ptQ0wydXdrTkRQLUZFUHFLdlZLMHRfLTFDbDRhcUYtampvbTEwMWExeDdqdlV4RExiWmVPQnM0Y2ZtYS01TUtqcWVtMTh4UWFwYXNXVDRXeXU4Zk5vZm1ndjZtU3Y4c1lZbzh3Y2JrcG52SldITWxOa04?oc=5>

## HEADWINDS

### TSMC Stocks Fall 2.21% as NVIDIA Shake-Up Overshadows Record October Revenue
- Summary: TSMC Stocks Fall 2.21% as NVIDIA Shake-Up Overshadows Record October Revenue
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0AFBVV95cUxNNEVOZm85ai1fTjJ3Smc0NWJaVjcwcU1hLVZCNl80aUhTWEd1QWo2WmlIX290ZUFkVF9HaHh4OG1IRmhReTlyRHU3SDlKNEFJcnExOHdQUjZYeno5c1ZaRnM0YXdLSm96eGlOQjUtVms4M2tuMlJPbjZWOUpGdmNRM1JsdmdoLXpaLXZqcTl4SXJVbUYweUZkaEVYdHJKSDFtTFlmT1hnOUVlWXhSS1Z3NnBlelVhWkZSUXgzVTBvdkFJYUFSbVVJa2tqLWhCcjlQ?oc=5>

### Taiwan Semiconductor Manufacturing (TSM) Stock Could Be 7% Undervalued Despite Fab Expansion Plans
- Summary: Analysts suggest TSMC may be undervalued, indicating potential downside risk.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxNclhidVc5Z2VTNE9uZzRCcldGRDUzLXcyc1otalhRaExZNHR2cVRPNk03Z052ekExdUt1QzgxWGkya1NHcElYeWowOXRESHM1UFlsZUx3Yi14bUFHcHp3bVJuTlJPUDlzZFZjYV9URFR6b19NQVRtYUhMdFNobGIwWWFJb1JwODdWM1h6ZjQ4RS1obDRfNUkxdHdGUDdFR0JqbkhnX2ZzVUtRTml2Nmc?oc=5>

## CATALYSTS

### TSM Stock Jumps Premarket After Board Approves $1B Investment In Anthropic And OpenAI, Dividend Raise
- Summary: TSM Stock Jumps Premarket After Board Approves $1B Investment In Anthropic And OpenAI, Dividend Raise
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNcUZzUVF1NFQ5NFVFYVRGSUNtVkhnc0plRGxFazRvVWFheFJOVEdnTnlfNDktZWJmc0Zvb044TGVkVVJiYS1vbmd1SmdLX25qTE9fV3pPckVzdlZqbW9hS19jRDVueWZRRTNMcFRQTGZzTlhnTUtseks2ZUFadmtha09yZG5yckJMbW5XUW9ZS0s0MnBMdFZPZFlqd1I?oc=5>

### TSMC Approves Up to $1 Billion Investment Plan in Anthropic, OpenAI
- Summary: TSMC invests up to $1B in Anthropic and OpenAI, expanding AI partnership.
- Date: 2026-11-11 | Impact: medium | Horizon: medium | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxNT3ZlYXlWNllKZkZETDl2YUpGcXdKYnBpc01rZ2pMenZYcXJrcmVhbFdlUW5oQnFWeTZ1dlN2S2RwVFFUaVJIUWk0UVJsOHk4R25nSGt4NnlfYTZVNXZvTzlrcXU4V2ZGNUNQQTY1amMwcHZ3bC00aTFBMTRKcFExdThaQlY2Nmp4ek1qSXRDdVVuLUlOSWVPQWMtSHlqT0g3RmlCbQ?oc=5>

### As October Revenue Surges, Wall Street Is Still Bullish on Taiwan Semi Stock
- Summary: Wall Street remains optimistic as TSM's October revenue jumps, signaling strong performance.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxOU2RWVW9CTzdRNW1nYlJPWTRHd0N4WlpQRFphaVVUYWZtZDJlS2JybGF3UVptd0p3UFhQZjFCeFE3R2hfZ3VyYzZvZGp3S25IUlFXcVZ4UTBjN1VkUTQ2eHp6MnZDcUZjekN2Wm4xY2tackRRbkFXS3JPc3R3NlZwelhRT0lWQlNvWmt1eERfNGwwS0ZwSHJIc0tFblp2TUphLS1mQ1hJOS1SejdaWHYwWXM5bEI1YkJzeHRz?oc=5>

### Here’s Why Bernstein’s Mark Li Is Raising His Price Target on TSMC (TSM) to $600
- Summary: Analyst Mark Li lifts TSM price target to $600, reflecting bullish outlook.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxQTTlUdnBEMndLSFFyVEV0bVNDVWlRRW0zZXdNSTJxeEY5VjVOOHluSVA2TEJldkJWTl91a1Z0bWJ4QTBhLVdpSWlVeUZTcF91Q0txMGZyaXpyUEN2TTNsRUdLT2ZGSzJha3kzeU91T2RGVElDTmd0clBWMFRmUkx2MkY2SkdSSFhZRGQteWhJalVMcWlVS2Z1R3hR?oc=5>

## RISKS

### What Is Going on With Taiwan Semiconductor Stock on Monday?
- Summary: Inquiry about TSM stock movement on Monday.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxNdlVNUlBPLXliejk5cW53UXNqT0FxZTBBUnQ1ZlhjS2dldDZGSjl2QUsyT3BGY2Q3OGRkUWw3VmV1TFgxVU05eGdJRXZRckQ0ZXU0di1nMGdoYzhJX3YzWGxVcGIxbm9FR0Z2bEpQenM4bkhsNkcydFVCLUtOeHVMd1htQ0ZuV185SVV4bTgzM2l5YjlONURuc0FyWHN2NFpyS2hSdDJyMm8yRE5TWGVZcg?oc=5>

### TSMC discovers data on thousands of current, former employees leaked to external website
- Summary: Data leak of employee information poses security risk.
- Date: 2026-11-12 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxNZ2J6RWloVkFVNXVGYUdSRVR0Tm5HT29vZUtPZzBkbWlSaHQxUGZodFBweWozNlRfN2hHSHc2bmcwVTNsUUFaNndrYlRseXVJSlNCNnpxcEN3Nm9RRXlkMTFiVVh1ZXBhc2dTV09Ibmp3M21oZDcwRW43T1JKRnU0Zk5XNXhiNVVEMnJ5MUNhamswXzF0RjljWWlTVjZtb0RMdFo5WE1qTDllODE4eDFTOU1ZekNvbjRrU3diNzdYM2NncDg?oc=5>

### A Massive Employee Data Leak Is Dragging Down TSM Stock
- Summary: Employee data leak negatively impacts TSM stock price.
- Date: 2026-11-12 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxPS3JKYmx5NFF2OUo1N3ZNTXF3MXh3TWJ3NndMNXl1RW5KZ0M2ZWIyc1ZwZkRKRmlubUh5cmtwVjFSVkV0Z3JhNHpXMXd5TkJGZk1RNDNpQ3pXMG9uQzM1djBMeWszcnB1U2U4OUdEc3NqTEg1VGE2Y3ZqcnMtMmFpWTFPeWVyLUo5c0d5azlzb29XMXVGRWVXNEQ3NHl3VS1S?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **TSM** | **26.28** | **77.38** | **3.77** | **50.90** | **2,103,062,822,912.00 USD** | **41.00** |
| UMC | 14.87 | 2.72 | -0.27 | 25.60 | 39,522,832,384.00 USD | 121.51 |
| GFS | 121.77 | 1.99 | 11.45 | 12.50 | 23,758,465,024.00 USD | 25.22 |
| INTC | N/A | 2.83 | 17.67 | 20.90 | 325,278,007,296.00 USD | 61.52 |

Peers fetched as_of: 2026-11-12; TSM reuses existing data (market data as_of: 2026-11-12); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-15
- Next expected earnings: 2027-01-14 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-12

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
- https://news.google.com/rss/articles/CBMilwFBVV95cUxNdXVPN1FxVkpoWXdpeG9DdDJyNEl5aUlMWF8yZVM2aG1SNkdTbUFMNnQwQWFMMjhkNjJkOVdjb19IQTRtQzJBZ085alZEdjVpLTFMek9haGlValNDZzFTR3lfNnpmc1BPRk44N2RuWHR1dE03SWdTMXhHVGRSQm1ONkJpSkJVZmhvRzdLUEQwdUx4VHUzbnpN?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxNWGFvVFk2WFI4T0VZN2JmVHA5Zk41VDNUWHdlN2loVTJFTW5LakFHY3V4TjhoMk9ZZy01YmZ2eUxONlFEZlhPUmhldzVHYjlObFJzLXVTOTEzN3E3a21aY0ZmaHFEN1VNRm10UVpwR0EtVTIycFk3MkNITHp4RF8zaVdPVTM2NWx3T3hoaWRLUVlYOVNMM2Q0M0lOUVhoQlpyS1dGOFExUm53T1VDaEpHdmJB?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxPdHZ6QnVWUlEtOE5fb0dnOGRMbEttQ1FIM0dTdy1CZzloTk1Tc0RaNm40VTB1YjR1bmpnVmRFelE5RjlyeGJQQl9lY2s5SThnZ1d2QmRHbnM0cHVFTnZCcXh6QzRqZVN0TFoyOGVpSExjYm56czYydkdZLV9YX1RYYWdBY1hMRWlTQVhWR2MxQmp1clVoTW93b2J6NVdTZEdjdGZMc041NldwODR4?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxORk9oU1JVdGlRMFByRzFoVC1yU2d2TjlIMUVmdnVIRXY3am53NkdfaF9LNTloYWtSUUQyS0JvakxRU1lXNTBnbTkyR0I2OE9IUHJsbGFNRl8wX0RGdktPQjdvRlliek05TUVpa0JwTjNJSXpZUDdEY21FNDM4MHl6UWpzeTB1OWluSXpwZmpQVFVLRWZ3RmI4N2VLZDBwenc?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQOGpUMzJxTHl5SzNTODh3bFBOVlJzSV95TGNNbTRnWG52S0ptQ0wydXdrTkRQLUZFUHFLdlZLMHRfLTFDbDRhcUYtampvbTEwMWExeDdqdlV4RExiWmVPQnM0Y2ZtYS01TUtqcWVtMTh4UWFwYXNXVDRXeXU4Zk5vZm1ndjZtU3Y4c1lZbzh3Y2JrcG52SldITWxOa04?oc=5
- https://news.google.com/rss/articles/CBMi0AFBVV95cUxNNEVOZm85ai1fTjJ3Smc0NWJaVjcwcU1hLVZCNl80aUhTWEd1QWo2WmlIX290ZUFkVF9HaHh4OG1IRmhReTlyRHU3SDlKNEFJcnExOHdQUjZYeno5c1ZaRnM0YXdLSm96eGlOQjUtVms4M2tuMlJPbjZWOUpGdmNRM1JsdmdoLXpaLXZqcTl4SXJVbUYweUZkaEVYdHJKSDFtTFlmT1hnOUVlWXhSS1Z3NnBlelVhWkZSUXgzVTBvdkFJYUFSbVVJa2tqLWhCcjlQ?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxNclhidVc5Z2VTNE9uZzRCcldGRDUzLXcyc1otalhRaExZNHR2cVRPNk03Z052ekExdUt1QzgxWGkya1NHcElYeWowOXRESHM1UFlsZUx3Yi14bUFHcHp3bVJuTlJPUDlzZFZjYV9URFR6b19NQVRtYUhMdFNobGIwWWFJb1JwODdWM1h6ZjQ4RS1obDRfNUkxdHdGUDdFR0JqbkhnX2ZzVUtRTml2Nmc?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNcUZzUVF1NFQ5NFVFYVRGSUNtVkhnc0plRGxFazRvVWFheFJOVEdnTnlfNDktZWJmc0Zvb044TGVkVVJiYS1vbmd1SmdLX25qTE9fV3pPckVzdlZqbW9hS19jRDVueWZRRTNMcFRQTGZzTlhnTUtseks2ZUFadmtha09yZG5yckJMbW5XUW9ZS0s0MnBMdFZPZFlqd1I?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxNT3ZlYXlWNllKZkZETDl2YUpGcXdKYnBpc01rZ2pMenZYcXJrcmVhbFdlUW5oQnFWeTZ1dlN2S2RwVFFUaVJIUWk0UVJsOHk4R25nSGt4NnlfYTZVNXZvTzlrcXU4V2ZGNUNQQTY1amMwcHZ3bC00aTFBMTRKcFExdThaQlY2Nmp4ek1qSXRDdVVuLUlOSWVPQWMtSHlqT0g3RmlCbQ?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxOU2RWVW9CTzdRNW1nYlJPWTRHd0N4WlpQRFphaVVUYWZtZDJlS2JybGF3UVptd0p3UFhQZjFCeFE3R2hfZ3VyYzZvZGp3S25IUlFXcVZ4UTBjN1VkUTQ2eHp6MnZDcUZjekN2Wm4xY2tackRRbkFXS3JPc3R3NlZwelhRT0lWQlNvWmt1eERfNGwwS0ZwSHJIc0tFblp2TUphLS1mQ1hJOS1SejdaWHYwWXM5bEI1YkJzeHRz?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxQTTlUdnBEMndLSFFyVEV0bVNDVWlRRW0zZXdNSTJxeEY5VjVOOHluSVA2TEJldkJWTl91a1Z0bWJ4QTBhLVdpSWlVeUZTcF91Q0txMGZyaXpyUEN2TTNsRUdLT2ZGSzJha3kzeU91T2RGVElDTmd0clBWMFRmUkx2MkY2SkdSSFhZRGQteWhJalVMcWlVS2Z1R3hR?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxNdlVNUlBPLXliejk5cW53UXNqT0FxZTBBUnQ1ZlhjS2dldDZGSjl2QUsyT3BGY2Q3OGRkUWw3VmV1TFgxVU05eGdJRXZRckQ0ZXU0di1nMGdoYzhJX3YzWGxVcGIxbm9FR0Z2bEpQenM4bkhsNkcydFVCLUtOeHVMd1htQ0ZuV185SVV4bTgzM2l5YjlONURuc0FyWHN2NFpyS2hSdDJyMm8yRE5TWGVZcg?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxNZ2J6RWloVkFVNXVGYUdSRVR0Tm5HT29vZUtPZzBkbWlSaHQxUGZodFBweWozNlRfN2hHSHc2bmcwVTNsUUFaNndrYlRseXVJSlNCNnpxcEN3Nm9RRXlkMTFiVVh1ZXBhc2dTV09Ibmp3M21oZDcwRW43T1JKRnU0Zk5XNXhiNVVEMnJ5MUNhamswXzF0RjljWWlTVjZtb0RMdFo5WE1qTDllODE4eDFTOU1ZekNvbjRrU3diNzdYM2NncDg?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxPS3JKYmx5NFF2OUo1N3ZNTXF3MXh3TWJ3NndMNXl1RW5KZ0M2ZWIyc1ZwZkRKRmlubUh5cmtwVjFSVkV0Z3JhNHpXMXd5TkJGZk1RNDNpQ3pXMG9uQzM1djBMeWszcnB1U2U4OUdEc3NqTEg1VGE2Y3ZqcnMtMmFpWTFPeWVyLUo5c0d5azlzb29XMXVGRWVXNEQ3NHl3VS1S?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxOcDNWZVdoQkpRUnh5dEk1TDQ1YVkwNFczYzczMG81YklqcVdZQWlydjBtUmZkSW5wRnlyNDhNV3h2WEFVbkdhLXhMZ1ZiTTZMSHRNNFdfdUR5LWZSNEFwMmFqaE5UMVo4YVNRNjJ0NXJBVnVGSjlPRGlrVk1FTzNhbmlLRVhYNllDc3l3bTNnbjFyekZnM1hTclFFYU43aWp6LUE?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
