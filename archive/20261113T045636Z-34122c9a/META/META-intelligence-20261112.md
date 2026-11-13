# META Intelligence Report

- ticker: **META**
- Report as_of: **2026-11-12**
- Market data as_of: **2026-11-12**
- Quant sources: https://finance.yahoo.com/quote/META/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/META/key-statistics/
- AI analysis snapshot as_of: **2026-11-12**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-13T05:15:50.013294+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 21, 'rule': 3, 'ai': 12, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **9** exact headline/source/date matches; prior report **20261112T054014Z-6c47e7f9/META** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'directional_claim_without_event_type': 1}
- RSS source audit (metadata only, not article fact-checking): 21 unique headlines; 9 named publishers; 4 exact duplicates; 21 HTTPS source links; largest publisher share 47.62%; oldest publication 2026-11-08

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 623.6100 |
| Return 1D (%) | -0.8207 |
| Return 1W (%) | 3.0624 |
| Return 1M (%) | -16.0641 |
| Return YTD (%) | -5.2833 |
| Return 1Y (%) | 2.7447 |
| Annualized volatility (%) | 41.5544 |
| Beta vs SPY | 1.3573 |
| Max drawdown (%) | -28.7332 |
| Sharpe (rf=0) | 0.2709 |
| Downside deviation (rf=0, %) | 27.4282 |
| Sortino (rf=0) | 0.4104 |
| Historical VaR 95% (1D, %) | 3.7761 |
| Historical ES 95% (1D, %) | 5.6434 |
| Correlation vs SPY | 0.4486 |
| Tracking error vs SPY (%) | 37.4609 |
| P/E (trailing) | 21.28 |
| P/B | 5.85 |
| EV/EBITDA | 14.00 |
| Revenue growth (%) | 26.10 |
| Forward P/E (estimate) | 17.52 |
| Gross margin (%) | 81.03 |
| Operating margin (%) | 37.78 |
| Return on equity (%) | 32.26 |
| Free cash flow yield (%) | 1.06 |
| MA50 | 679.0733 |
| Close vs MA50 (%) | -8.1675 |
| MA200 | 630.4973 |
| Close vs MA200 (%) | -1.0924 |
| RSI (14, Wilder) | 42.1198 |
| MACD (12,26) | -17.2951 |
| MACD signal (9) | -18.1626 |
| MACD histogram | 0.8675 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'META': 281, 'SPY': 281}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 623.6100 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.8207 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 3.0624 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -16.0641 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -5.2833 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 2.7447 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 41.5544 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 27.4282 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.4104 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.7761 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.6434 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4486 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 37.4609 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.3573 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -28.7332 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.2709 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 17.5231 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 81.0340 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 37.7770 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 32.2640 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.0567 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 21.2764 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 42.1198 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.8675 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -8.1675 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -1.0924 -> Slightly below the moving-average trend level.

## TAILWINDS

### Prediction: Meta Stock’s Next Big Catalyst Could Be Just Around the Corner
- Summary: Speculation that a significant catalyst may soon emerge for Meta, potentially boosting investor sentiment.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNT1BXTDl0b2N5STg5NTZqR3FTQmlWMWJMdFJKbjNrWGgyTUZkNXViNElLNTdrSVM2T3ZzMGhjU1V3cVZZNWFqTVl4U1FrdlVxWGE0UFJGUWxaWS1MekRnQ0hfQ3YwaklhcVhCbUZlLWs4aEM5WEpfWFNwRVcxSjhnU2Q1NC1maFctRGVxRU5KWWw1RnlCcTVyQnlPTQ?oc=5>

### Why Is Meta Stock Going Up?
- Summary: Meta’s stock rise attributed to robust user growth and advertising revenue.
- Date: 2026-11-10 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxObFhiNTNYeFpZRXlEZUE4eGtJLXJVbmZtbmhRa3JzS2hiS2FKR0pERmRQQzItVHBKX2daMWNoQjlpWnhwakJiVExOV2FIcGZpajRMTU05djNPWlprek1rLTdQR2hQc2xWSnZ3UzVsMk1vZ2RrSXE3aXlYMzMyVUUxdFZ6dXZybDRVMl9jVTlRLTU?oc=5>

### Meta Platforms (META) Wins JPMorgan Backing, Is It Still 37% Below Fair Value?
- Summary: JPMorgan backing signals confidence, potentially boosting Meta’s valuation prospects.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxOOFRKM0RTQ0U1c1Y1SW50LWp4c3phSmVxRnZJdHBvcGI5QXJ2Z0Rydkxud3pLUm9YRFUtRkhlUjVyOUwyMU5lU3BaNFQ3dktYd1ZFVTB2dy0zc0x0Y0pUZUZKMkU5T3hkM04wVVFVd2QwUS1PSklfYlR0SlhLZmRxdUhJbWphdnczNzFiaUdGYjdDUjM3U2U4X1BZN1BqQlU?oc=5>

### JPMorgan Just Added Meta Platforms to Its Analyst Focus List
- Summary: JPMorgan's inclusion of Meta in its analyst focus list signals increased analyst attention and potential positive coverage.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxQMmFWV1dTcEphNzdJU1psZHZReUJiV25PNnVMNnRzZzFKTzZycGRjeG5fM1FZV0RSM2xSZTRHUi1FdHBsTWVxa3lyWXhvZ0phY2EzWnN6T1JNRS1kdHRkUmFjMEI4YkxwX3RvcXUwMUlNaWlSak8tb19QZm84Z3ROQ0pvYWRmbGN0Uk5uYTVnbGtrUFZ2SERtaTc0UXNfZHF0?oc=5>

### META, AMZN Stocks Jump As JPMorgan Picks Pair Over Alphabet — Sees Stronger AI Returns, Cloud Growth
- Summary: JPMorgan names Meta and Amazon top picks, citing stronger AI returns and cloud growth.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxPUlRYcGF5YmpQQkx5NWI4RHdxbjNNNk16RldoUnduOG5hTzJYSUVxSFprTmNKXzVJZlAybzVUMzNzX3JPYTNObDE5enVrckpoOEtCWjZQNjVrOHJyMUY5OEFXa1p5OGdxLUFIWGhGM0Jxak5EeURaNHlxY0R6RUFuenFOVmI1SEVHSVBXY1dneFYwSGhlaXVtYk1Vcw?oc=5>

### Meta Platforms Completes Euro-Denominated Senior Notes Offering
- Summary: Meta issued euro-denominated senior notes, raising capital for corporate purposes.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxOYWFFall5cEZ1U0RtZ2wtSHhJcTk3Y29kRzVBaGRFaVZUbnJNWnNwZzVFa1M0bzdLV0ZVS2w5a0RVMnduODJ2UzlRR1FHeHRHeUR2MTh0X1lrVmxGcE0wUkt2ejI3RlljVFNvZVdZRGMxM3VVSlVoai0xckF3eGQ4SFFPRVhCcFRBUTFUYk9iOGZZV09ZUlYwbjFqbUpYcG12VGlES3ZlNzZqRTEwTlpST2VMaHI1Zw?oc=5>

## HEADWINDS

### Meta Platforms (NASDAQ:META) Stock Price Down 2% - Here's What Happened
- Summary: Meta Platforms (NASDAQ:META) Stock Price Down 2% - Here's What Happened
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxQRHpPa0hlVTB1TlNwTzgtbkNfS3FQVXFpMGxUNXdCNC1OWFdrbHlyMGRIZzJ2SmhlT3dVdmRQTVp1NDRzN0JfSUtRTUxlb1VJRHVCOEo5d3FDZ1ZNenRoVUdZamN1Z3RVUEdxUlZXbFpRTF9relZ3VFpKSEs0LTh1ZVJXRmppUFJaZGtZRDFaZjBrVG1NamRzWGZBRExTc2dFWllGdFYyNjd1Yl82UUY4Q1lhMDY2THpKX3puNGdBSzBWQ2c?oc=5>

### Meta Platforms, Inc. (META) May Need Hundreds of Billions for AI: What Does This Mean for Investors?
- Summary: Meta may require massive AI investment, raising concerns about future profitability and shareholder returns.
- Date: 2026-11-10 | Impact: high | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxNOHBTVFl0X0c1STJ6b2JOTElOUlhucUlDcTZwVUZoQ2ZNSUo0WXJQZWsyd0ZVWVZFam9hWUdRVEE1VThUT1JrVTN3RnEzemQ4YnJyTnlYenYxdm9zb0JSeVNuelA2R1dxeGNoaml0ZEtsREh1WFNkWDB4U2lNSGxyQjJETkFFdTRRVkZFWHBFLXdxUFZ2MUtZ?oc=5>

### Meta Stock: Midterm Election Results Raise Concerns Over AI Data Center Expansion
- Summary: Election outcomes may hinder Meta’s AI data center expansion plans.
- Date: 2026-11-11 | Impact: high | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxQcVlqaXUwYkwwcHFqNjdaSk95ZEhFNlpBdmRsV1ZsM2loSExqZzh0TVhka3ZtQ2ljWGpULVlrTXU2SlpGM19LalpDV0dIZlZ6bVZmOWJaalFvcVFqRjJRUjMxVG5QUlFRYWR2RFplZ1FzYnNKRXowd1owNl9qZ2NHRHVDWHRZVnY4TENuSkZHaHJHLU43ZTlNR3pfcjllbTVC?oc=5>

## CATALYSTS

### Meta Platforms Stock: Is it a Steal of a Deal at $650?
- Summary: Meta Platforms Stock: Is it a Steal of a Deal at $650?
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxNakxvaEdiTzR5M0tqcm5KeE1mVDFYUTVuZlhCdzl6MHdXV0tiek90QU1qZHBxdktxWjNIaHNoRDhPNTVrN0F5OGx1VUtiTWhObkJRcl9pVXFDbzFsT2cxcTRwaHBKZF93cEgzM0JHd3VkVVpIZ0theFMxdEJIY2FvQ0xtSlQyNTMwNmlMRzVKYS0yRjZVMkR6cGln?oc=5>

### Meta Stock Climbs on Muse Launch Reports in UK
- Summary: Meta Stock Climbs on Muse Launch Reports in UK
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxORVVHQ3NjN3pmQ1dDdFlUZUduN1poVHNVRTdwakFhSnhRU1NLQWY5NldGNWVzZTVmTlNEckdHSGFuZTduaEt5LUNlZG9IeW1KS3V6NjZGQzNyWHNnQnJSMFJFOE5BT05MNXBPYTkxWHNKdEZmX05hRGFZMGpWRkhRX19WUW9hYWZ0U056bUVhY3kxYzZBTDZNMlFvUFdtN3FLV2JDeTBKbkpYVW8?oc=5>

### What Is Meta Platforms (META) Facing As Legal Risks Rise And AI Deals Expand?
- Summary: Meta faces increasing legal challenges while expanding AI partnerships.
- Date: 2026-11-08 | Impact: high | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxPcmJmaDIwcnRLMjh1eGNUOGhuVjJNMGhyNFltVkNCYl9wMG43ck9jWnpNMHY0elFkWk1aYnM2WERaZ0lTWVpqV3AwVnYwZ2p2QVFWREpnRG5mV3dvRF8yMUhOb1NUcDlnSjAtUTlCanZkWWhINjhWWmcxS2g0aXZJUWEwY2Qyc0kxV25ibHJXNGVRelh5Um85N0x1TmFoZw?oc=5>

### Why Meta Platforms Stock Rallied on Monday
- Summary: Meta’s stock price increased on Monday, indicating positive market sentiment.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxQRUdMOElZOWFLR1FCQzMxbE5XN0tJeElzdUdrUksySzktUlN3U2QyTGhLbmc0LVZ0b0RadmtCNzkzamlnV2d3dGZoU1Nveks4UHgwMmk4MU93b0owRHNtMjVTWEM4NDJPTDhlM2wyZ0hnbTl2djJ5eFZ4azRrdVN2T05TNWNXaTBHSWtQaG05NnNxV1NlTDdZS0IyQlNCZw?oc=5>

### Should You Buy Meta Platforms Before Its Stock Split?
- Summary: Meta is planning a stock split, potentially increasing liquidity and attracting investors. The split may boost trading volume and improve market perception.
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxOeGliT3JmRml6TmRJN3VpZDRFU1RmSk55aWxZWlNVenV3U2o2UndNZTNJZEQ2QTB1Y2VfVXpxcHk4WUszOTdFRWNwVXh5eXRLaVZ1aHB6U2x0UG9ES1QxWDZMeUF5VlNPRjRScFlJOVpIbVc5YkhmVVFKRzR4cll3NE95MWR2MVl4MWZueWdBUzRlbGpnZUlKeDFQdw?oc=5>

## RISKS

### META: SEC Form CERT filed by Meta Platforms Inc.
- Summary: Meta filed a CERT form with the SEC, indicating a regulatory disclosure that could affect investor perception.
- Date: 2026-11-12 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxQSy0tb3FoenloXzdqakVWWGtMaGNzU1VwSFJUUGFkWm1nMWFrb3Z4ZzVfQzZPQVhXcFdPVTkxV0h6TVZLYTRoS1BnWVE1Ty1mT2o0b3VPb3c0U094Zk1LWElnbUxidUlpMGdEZTBacGU5MUliWUtNZ3kyV2ZCeW4tS2lPTTVqekhTX2drbg?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **META** | **21.28** | **5.85** | **14.00** | **26.10** | **1,594,466,631,680.00 USD** | **2.74** |
| GOOGL | 15.60 | 5.57 | 19.27 | 24.70 | 3,672,217,747,456.00 USD | 4.45 |
| SNAP | N/A | 4.02 | 54.75 | 14.30 | 9,012,729,856.00 USD | -42.57 |
| PINS | 79.67 | 3.53 | 36.10 | 11.90 | 10,965,470,208.00 USD | -30.01 |

Peers fetched as_of: 2026-11-12; META reuses existing data (market data as_of: 2026-11-12); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-21
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-12

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-22
- Revenue (latest available single quarter): 13,727,000,000.00 USD; period 2018-07-01/2018-09-30; fiscal year/reporting period 2018/Q3
- Net income (latest available single quarter): 9,860,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMimwFBVV95cUxNT1BXTDl0b2N5STg5NTZqR3FTQmlWMWJMdFJKbjNrWGgyTUZkNXViNElLNTdrSVM2T3ZzMGhjU1V3cVZZNWFqTVl4U1FrdlVxWGE0UFJGUWxaWS1MekRnQ0hfQ3YwaklhcVhCbUZlLWs4aEM5WEpfWFNwRVcxSjhnU2Q1NC1maFctRGVxRU5KWWw1RnlCcTVyQnlPTQ?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxObFhiNTNYeFpZRXlEZUE4eGtJLXJVbmZtbmhRa3JzS2hiS2FKR0pERmRQQzItVHBKX2daMWNoQjlpWnhwakJiVExOV2FIcGZpajRMTU05djNPWlprek1rLTdQR2hQc2xWSnZ3UzVsMk1vZ2RrSXE3aXlYMzMyVUUxdFZ6dXZybDRVMl9jVTlRLTU?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxOOFRKM0RTQ0U1c1Y1SW50LWp4c3phSmVxRnZJdHBvcGI5QXJ2Z0Rydkxud3pLUm9YRFUtRkhlUjVyOUwyMU5lU3BaNFQ3dktYd1ZFVTB2dy0zc0x0Y0pUZUZKMkU5T3hkM04wVVFVd2QwUS1PSklfYlR0SlhLZmRxdUhJbWphdnczNzFiaUdGYjdDUjM3U2U4X1BZN1BqQlU?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxQMmFWV1dTcEphNzdJU1psZHZReUJiV25PNnVMNnRzZzFKTzZycGRjeG5fM1FZV0RSM2xSZTRHUi1FdHBsTWVxa3lyWXhvZ0phY2EzWnN6T1JNRS1kdHRkUmFjMEI4YkxwX3RvcXUwMUlNaWlSak8tb19QZm84Z3ROQ0pvYWRmbGN0Uk5uYTVnbGtrUFZ2SERtaTc0UXNfZHF0?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxPUlRYcGF5YmpQQkx5NWI4RHdxbjNNNk16RldoUnduOG5hTzJYSUVxSFprTmNKXzVJZlAybzVUMzNzX3JPYTNObDE5enVrckpoOEtCWjZQNjVrOHJyMUY5OEFXa1p5OGdxLUFIWGhGM0Jxak5EeURaNHlxY0R6RUFuenFOVmI1SEVHSVBXY1dneFYwSGhlaXVtYk1Vcw?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxOYWFFall5cEZ1U0RtZ2wtSHhJcTk3Y29kRzVBaGRFaVZUbnJNWnNwZzVFa1M0bzdLV0ZVS2w5a0RVMnduODJ2UzlRR1FHeHRHeUR2MTh0X1lrVmxGcE0wUkt2ejI3RlljVFNvZVdZRGMxM3VVSlVoai0xckF3eGQ4SFFPRVhCcFRBUTFUYk9iOGZZV09ZUlYwbjFqbUpYcG12VGlES3ZlNzZqRTEwTlpST2VMaHI1Zw?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxQRHpPa0hlVTB1TlNwTzgtbkNfS3FQVXFpMGxUNXdCNC1OWFdrbHlyMGRIZzJ2SmhlT3dVdmRQTVp1NDRzN0JfSUtRTUxlb1VJRHVCOEo5d3FDZ1ZNenRoVUdZamN1Z3RVUEdxUlZXbFpRTF9relZ3VFpKSEs0LTh1ZVJXRmppUFJaZGtZRDFaZjBrVG1NamRzWGZBRExTc2dFWllGdFYyNjd1Yl82UUY4Q1lhMDY2THpKX3puNGdBSzBWQ2c?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxNOHBTVFl0X0c1STJ6b2JOTElOUlhucUlDcTZwVUZoQ2ZNSUo0WXJQZWsyd0ZVWVZFam9hWUdRVEE1VThUT1JrVTN3RnEzemQ4YnJyTnlYenYxdm9zb0JSeVNuelA2R1dxeGNoaml0ZEtsREh1WFNkWDB4U2lNSGxyQjJETkFFdTRRVkZFWHBFLXdxUFZ2MUtZ?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxQcVlqaXUwYkwwcHFqNjdaSk95ZEhFNlpBdmRsV1ZsM2loSExqZzh0TVhka3ZtQ2ljWGpULVlrTXU2SlpGM19LalpDV0dIZlZ6bVZmOWJaalFvcVFqRjJRUjMxVG5QUlFRYWR2RFplZ1FzYnNKRXowd1owNl9qZ2NHRHVDWHRZVnY4TENuSkZHaHJHLU43ZTlNR3pfcjllbTVC?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxNakxvaEdiTzR5M0tqcm5KeE1mVDFYUTVuZlhCdzl6MHdXV0tiek90QU1qZHBxdktxWjNIaHNoRDhPNTVrN0F5OGx1VUtiTWhObkJRcl9pVXFDbzFsT2cxcTRwaHBKZF93cEgzM0JHd3VkVVpIZ0theFMxdEJIY2FvQ0xtSlQyNTMwNmlMRzVKYS0yRjZVMkR6cGln?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQWl90bVRBbmtwUVN2aEJ6enF6M0o4Yml4SlA2YVRvR3hCbkFFS1pVTnEweHlGMHd3UFgzQjBsY2ZIOEhpS1ZQbHY5U19jSk0xTF9yRHYzV0RmUGNNNmNCUW43a0wzUmxxVUtIaG9EV19xVU43a1ljcDFTTW5EYmxJNzJranVJbURuNUdJUU53OHJ1VXgzdS1md04xVzM?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxORVVHQ3NjN3pmQ1dDdFlUZUduN1poVHNVRTdwakFhSnhRU1NLQWY5NldGNWVzZTVmTlNEckdHSGFuZTduaEt5LUNlZG9IeW1KS3V6NjZGQzNyWHNnQnJSMFJFOE5BT05MNXBPYTkxWHNKdEZmX05hRGFZMGpWRkhRX19WUW9hYWZ0U056bUVhY3kxYzZBTDZNMlFvUFdtN3FLV2JDeTBKbkpYVW8?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxPcmJmaDIwcnRLMjh1eGNUOGhuVjJNMGhyNFltVkNCYl9wMG43ck9jWnpNMHY0elFkWk1aYnM2WERaZ0lTWVpqV3AwVnYwZ2p2QVFWREpnRG5mV3dvRF8yMUhOb1NUcDlnSjAtUTlCanZkWWhINjhWWmcxS2g0aXZJUWEwY2Qyc0kxV25ibHJXNGVRelh5Um85N0x1TmFoZw?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxQRUdMOElZOWFLR1FCQzMxbE5XN0tJeElzdUdrUksySzktUlN3U2QyTGhLbmc0LVZ0b0RadmtCNzkzamlnV2d3dGZoU1Nveks4UHgwMmk4MU93b0owRHNtMjVTWEM4NDJPTDhlM2wyZ0hnbTl2djJ5eFZ4azRrdVN2T05TNWNXaTBHSWtQaG05NnNxV1NlTDdZS0IyQlNCZw?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxOblRPS2JSaEh6Z2xwbDBmN196Y3dZQW1sNkRMYTRSMHV2dzkyeEtETEVvc295b0k3S1RFcmZ2YjUwbWxBeVhrNEpBNzRVa1FuMlpFUUpaWnBER2NVejFXVGNNX2N2dTdoSVREN2NDcTFaTEtURzUyVUFkSTBIcFdpQ2txdUxvMWF5Z19vT3ln?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxOeGliT3JmRml6TmRJN3VpZDRFU1RmSk55aWxZWlNVenV3U2o2UndNZTNJZEQ2QTB1Y2VfVXpxcHk4WUszOTdFRWNwVXh5eXRLaVZ1aHB6U2x0UG9ES1QxWDZMeUF5VlNPRjRScFlJOVpIbVc5YkhmVVFKRzR4cll3NE95MWR2MVl4MWZueWdBUzRlbGpnZUlKeDFQdw?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQVXJPbUx6X3JPTjRSYkZ3RjNvLWJ3OG5qQThGV1l4ZnFMZEY0Ny16R19va3kxV1hYVFdzM2hGYzZlc1RqRk54TlNUYjRoM1hKdm9mdHZXMFFhUUxheGpqU0x5VUE3X2JPLU1VN2IyREN2dGhzTWRLNGsyRUVxTldDYTlkaENZRVBUSjFZTUQyNWoyUzNrbldIbg?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxQSy0tb3FoenloXzdqakVWWGtMaGNzU1VwSFJUUGFkWm1nMWFrb3Z4ZzVfQzZPQVhXcFdPVTkxV0h6TVZLYTRoS1BnWVE1Ty1mT2o0b3VPb3c0U094Zk1LWElnbUxidUlpMGdEZTBacGU5MUliWUtNZ3kyV2ZCeW4tS2lPTTVqekhTX2drbg?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
