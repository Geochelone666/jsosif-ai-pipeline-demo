# META Intelligence Report

- ticker: **META**
- Report as_of: **2026-11-13**
- Market data as_of: **2026-11-13**
- Quant sources: https://finance.yahoo.com/quote/META/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/META/key-statistics/
- AI analysis snapshot as_of: **2026-11-13**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-14T05:00:18.750259+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 22, 'rule': 1, 'ai': 14, 'unknown': 0, 'irrelevant': 7})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **8** exact headline/source/date matches; prior report **20261113T045636Z-34122c9a/META** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 22 unique headlines; 8 named publishers; 3 exact duplicates; 22 HTTPS source links; largest publisher share 63.64%; oldest publication 2026-11-08

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 641.6900 |
| Return 1D (%) | 2.8993 |
| Return 1W (%) | 5.1692 |
| Return 1M (%) | -15.8439 |
| Return YTD (%) | -2.5372 |
| Return 1Y (%) | 5.5709 |
| Annualized volatility (%) | 41.6526 |
| Beta vs SPY | 1.3720 |
| Max drawdown (%) | -28.7332 |
| Sharpe (rf=0) | 0.3367 |
| Downside deviation (rf=0, %) | 27.4282 |
| Sortino (rf=0) | 0.5112 |
| Historical VaR 95% (1D, %) | 3.7761 |
| Historical ES 95% (1D, %) | 5.6434 |
| Correlation vs SPY | 0.4491 |
| Tracking error vs SPY (%) | 37.5602 |
| P/E (trailing) | 21.28 |
| P/B | 6.02 |
| EV/EBITDA | 14.40 |
| Revenue growth (%) | 26.10 |
| Forward P/E (estimate) | 18.03 |
| Gross margin (%) | 81.03 |
| Operating margin (%) | 37.78 |
| Return on equity (%) | 32.26 |
| Free cash flow yield (%) | 1.03 |
| MA50 | 679.7032 |
| Close vs MA50 (%) | -5.5926 |
| MA200 | 630.0237 |
| Close vs MA200 (%) | 1.8517 |
| RSI (14, Wilder) | 47.8020 |
| MACD (12,26) | -15.2194 |
| MACD signal (9) | -17.5739 |
| MACD histogram | 2.3545 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'META': 282, 'SPY': 282}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 641.6900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 2.8993 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 5.1692 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -15.8439 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -2.5372 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 5.5709 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 41.6526 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 27.4282 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.5112 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.7761 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.6434 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4491 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 37.5602 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.3720 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -28.7332 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.3367 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 18.0312 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 81.0340 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 37.7770 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 32.2640 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.0269 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 21.2762 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 47.8020 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 2.3545 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -5.5926 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 1.8517 -> Slightly above the moving-average trend level.

## TAILWINDS

### Meta Platforms (META) Wins JPMorgan Backing, Is It Still 37% Below Fair Value?
- Summary: JPMorgan backing signals confidence, potentially boosting Meta’s valuation prospects.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxOOFRKM0RTQ0U1c1Y1SW50LWp4c3phSmVxRnZJdHBvcGI5QXJ2Z0Rydkxud3pLUm9YRFUtRkhlUjVyOUwyMU5lU3BaNFQ3dktYd1ZFVTB2dy0zc0x0Y0pUZUZKMkU5T3hkM04wVVFVd2QwUS1PSklfYlR0SlhLZmRxdUhJbWphdnczNzFiaUdGYjdDUjM3U2U4X1BZN1BqQlU?oc=5>

### META, AMZN Stocks Jump As JPMorgan Picks Pair Over Alphabet — Sees Stronger AI Returns, Cloud Growth
- Summary: JPMorgan names Meta and Amazon top picks, citing stronger AI returns and cloud growth.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxPUlRYcGF5YmpQQkx5NWI4RHdxbjNNNk16RldoUnduOG5hTzJYSUVxSFprTmNKXzVJZlAybzVUMzNzX3JPYTNObDE5enVrckpoOEtCWjZQNjVrOHJyMUY5OEFXa1p5OGdxLUFIWGhGM0Jxak5EeURaNHlxY0R6RUFuenFOVmI1SEVHSVBXY1dneFYwSGhlaXVtYk1Vcw?oc=5>

### Why Is Meta Stock Going Up?
- Summary: Meta’s stock rise attributed to robust user growth and advertising revenue.
- Date: 2026-11-10 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxObFhiNTNYeFpZRXlEZUE4eGtJLXJVbmZtbmhRa3JzS2hiS2FKR0pERmRQQzItVHBKX2daMWNoQjlpWnhwakJiVExOV2FIcGZpajRMTU05djNPWlprek1rLTdQR2hQc2xWSnZ3UzVsMk1vZ2RrSXE3aXlYMzMyVUUxdFZ6dXZybDRVMl9jVTlRLTU?oc=5>

### Why is Meta Platforms stock climbing today?
- Summary: Meta stock rises today, but no specific event cited.
- Date: 2026-11-13 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxNSHlmWUhJMVl3T3ZHYUpsWnJ4S3BOWUhleGJtemdaaXdWRTc3VW9zVGdIem1JTVdyWjBwTUZsd2VnT2dyWWNpSkF0eDNKVHF4ckNPZGh2cEhqclZYX3JYTFNOb0tLRVhNdzFHR09GWC1qN001QjBCZzJuMnVCa21rTS1ucEYwZGVtSnhxdFpfQXpiQVUxMEVwZHlXcnJuNi1jR2JUVGhZRQ?oc=5>

## HEADWINDS

### Meta Stock: Midterm Election Results Raise Concerns Over AI Data Center Expansion
- Summary: Election outcomes may hinder Meta’s AI data center expansion plans.
- Date: 2026-11-11 | Impact: high | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxQcVlqaXUwYkwwcHFqNjdaSk95ZEhFNlpBdmRsV1ZsM2loSExqZzh0TVhka3ZtQ2ljWGpULVlrTXU2SlpGM19LalpDV0dIZlZ6bVZmOWJaalFvcVFqRjJRUjMxVG5QUlFRYWR2RFplZ1FzYnNKRXowd1owNl9qZ2NHRHVDWHRZVnY4TENuSkZHaHJHLU43ZTlNR3pfcjllbTVC?oc=5>

### Meta Platforms, Inc. (META) May Need Hundreds of Billions for AI: What Does This Mean for Investors?
- Summary: Meta may require massive AI investment, raising concerns about future profitability and shareholder returns.
- Date: 2026-11-10 | Impact: high | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxNOHBTVFl0X0c1STJ6b2JOTElOUlhucUlDcTZwVUZoQ2ZNSUo0WXJQZWsyd0ZVWVZFam9hWUdRVEE1VThUT1JrVTN3RnEzemQ4YnJyTnlYenYxdm9zb0JSeVNuelA2R1dxeGNoaml0ZEtsREh1WFNkWDB4U2lNSGxyQjJETkFFdTRRVkZFWHBFLXdxUFZ2MUtZ?oc=5>

### ETFs Are Net Sellers of Meta Platforms (META) on Nov. 5
- Summary: Meta shares face selling pressure from ETFs on Nov. 5.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxPeU53QjM2VzdMNWQ5dGtzNlVwLWdWbU9fenBHZ3pkLWFtYXJlYkJUWjViTTN1LVo3aU1oLXNiQU9DNjNKZzhlMnN6YlhaSDFabUF1NFgzMG9tT3YzWmNvWjRLWE0tWkZjai1tSWZiSjVBSjFCUkVrWTNobHhsaFpIbU9RdElsTGN4QVUtSXVrb2x0NHpwMlVUWWRYdVI?oc=5>

### Meta Stock Dips Towards $600 But Don’t Load Up Just Yet
- Summary: Meta stock is falling toward $600, suggesting caution.
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMifkFVX3lxTE5IV0M4bnduUzdZYjg0UjlTLS1CWkF2QlhvdUtlSkxmbWFfeDFzVjhPWTRBdWU5Y2lfU3Eta0N6d0VoNXVIeV9fdlpMQzZlWm5RZHo4UjluLVhrRkxkRWF5VlZDMTFKcVEtRzhQLW5LWlFIYlMxWFRnUnY3WWluQQ?oc=5>

## CATALYSTS

### Meta Platforms Stock: Is it a Steal of a Deal at $650?
- Summary: Meta Platforms Stock: Is it a Steal of a Deal at $650?
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQWl90bVRBbmtwUVN2aEJ6enF6M0o4Yml4SlA2YVRvR3hCbkFFS1pVTnEweHlGMHd3UFgzQjBsY2ZIOEhpS1ZQbHY5U19jSk0xTF9yRHYzV0RmUGNNNmNCUW43a0wzUmxxVUtIaG9EV19xVU43a1ljcDFTTW5EYmxJNzJranVJbURuNUdJUU53OHJ1VXgzdS1md04xVzM?oc=5>

### What Is Meta Platforms (META) Facing As Legal Risks Rise And AI Deals Expand?
- Summary: Meta faces increasing legal challenges while expanding AI partnerships.
- Date: 2026-11-08 | Impact: high | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxPcmJmaDIwcnRLMjh1eGNUOGhuVjJNMGhyNFltVkNCYl9wMG43ck9jWnpNMHY0elFkWk1aYnM2WERaZ0lTWVpqV3AwVnYwZ2p2QVFWREpnRG5mV3dvRF8yMUhOb1NUcDlnSjAtUTlCanZkWWhINjhWWmcxS2g0aXZJUWEwY2Qyc0kxV25ibHJXNGVRelh5Um85N0x1TmFoZw?oc=5>

### As Meta Platforms Continues To Weaken, A Bearish Trade May Be In Order
- Summary: Analysts suggest a bearish trade due to Meta's weakening performance.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxPeXYtc0wwTWRuR29fdGRXZE83a0JHb3Y2Q2Y4b3NPOXVZSjM3TEc5VzJhTkFBN1dHekhaUm9XOWdrbWl2OUx5eWRraVVIWm02YjhQV2M3MWpLbk5ld1c5TG1rRGE5Sm1Td0dMWFQ0b2dMYVp2Wko5SmxEMGEtSDFJWldKXzFEV3hjOTNtQkVFeVRpSjEzOFE?oc=5>

### Why Meta Platforms Stock Rallied on Monday
- Summary: Meta's stock rallied on Monday, indicating short-term positive momentum.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxQRUdMOElZOWFLR1FCQzMxbE5XN0tJeElzdUdrUksySzktUlN3U2QyTGhLbmc0LVZ0b0RadmtCNzkzamlnV2d3dGZoU1Nveks4UHgwMmk4MU93b0owRHNtMjVTWEM4NDJPTDhlM2wyZ0hnbTl2djJ5eFZ4azRrdVN2T05TNWNXaTBHSWtQaG05NnNxV1NlTDdZS0IyQlNCZw?oc=5>

### 55 ETFs Add to Meta Platforms (META) on Nov. 11
- Summary: Fifty-five ETFs increased holdings in Meta, signaling institutional support.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxQZkc4MEpkMmtxWldrMnI5ZUdHVjMyb1ZBU3duZklHdnBQekw0VnYzR0hoZWRMV3EtOUdScmpzd2E1ZEYxcjNfR3NKNWR6R3JzZWJtWE5SbG4ydTcxSzZRN3lXMmFHV01JaU1SSDNXVF8yRnM3U1VJS2RQYllEd0p3cGNTWV9jc3JTcjRpQkVla0ZLMUd3V1E?oc=5>

### What To Expect Out of Meta By The End of 2026 With an Announced January Stock Split
- Summary: Meta announced a January stock split, expected to affect share price by 2026.
- Date: 2026-11-11 | Impact: medium | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxOLWVDY2lZaGRsVW16Y2RrUnJ5ek5ST2V1RzlPNFhLUVNCSmJnR2NMczJYN2d3XzlfbjQ2ZllRNllfcGxYQ3NwRWsxMUNjV1Q4anZXaVhhWVpKcnAtT3JVZThYVTlDbTAtLS0zRWtWX2JUTURETVlKLU5UMkVGb3huZVp6WGhNTGMxM1JJV2pKaGFWUjlyYjdxZ25yUQ?oc=5>

### As Meta Platforms Buys Conductor, Here’s How to Play META Stock
- Summary: Meta acquires Conductor, potentially expanding its offerings.
- Date: 2026-11-08 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxNNUstX3dpZlZvUHdaWndNVlVrakVBdVpncUk0a1BBVHA3WWpFRld6VUxlRGhxajF0b0dLMF9OM2hhSl83ekhfRkh2bWNPekRTcFVxbzJkczZfUWNMbkpvRmJNb1BkRHU4Z0U5ejlOUV90LXFSVmR1YTRDZHM5MXVPTXZJVzJ6Z0RlZDJaWndxYUlnTXF4RDlMdkl5bkxxMGM?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **META** | **21.28** | **6.02** | **14.40** | **26.10** | **1,640,694,153,216.00 USD** | **5.57** |
| GOOGL | 15.60 | 5.51 | 19.08 | 24.70 | 3,636,196,016,128.00 USD | 6.45 |
| SNAP | N/A | 4.05 | 55.11 | 14.30 | 9,081,794,560.00 USD | -38.69 |
| PINS | 79.79 | 3.53 | 36.16 | 11.90 | 10,982,674,432.00 USD | -28.46 |

Peers fetched as_of: 2026-11-13; META reuses existing data (market data as_of: 2026-11-13); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-21
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-13

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

- https://news.google.com/rss/articles/CBMinwFBVV95cUxOOFRKM0RTQ0U1c1Y1SW50LWp4c3phSmVxRnZJdHBvcGI5QXJ2Z0Rydkxud3pLUm9YRFUtRkhlUjVyOUwyMU5lU3BaNFQ3dktYd1ZFVTB2dy0zc0x0Y0pUZUZKMkU5T3hkM04wVVFVd2QwUS1PSklfYlR0SlhLZmRxdUhJbWphdnczNzFiaUdGYjdDUjM3U2U4X1BZN1BqQlU?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxPUlRYcGF5YmpQQkx5NWI4RHdxbjNNNk16RldoUnduOG5hTzJYSUVxSFprTmNKXzVJZlAybzVUMzNzX3JPYTNObDE5enVrckpoOEtCWjZQNjVrOHJyMUY5OEFXa1p5OGdxLUFIWGhGM0Jxak5EeURaNHlxY0R6RUFuenFOVmI1SEVHSVBXY1dneFYwSGhlaXVtYk1Vcw?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxObFhiNTNYeFpZRXlEZUE4eGtJLXJVbmZtbmhRa3JzS2hiS2FKR0pERmRQQzItVHBKX2daMWNoQjlpWnhwakJiVExOV2FIcGZpajRMTU05djNPWlprek1rLTdQR2hQc2xWSnZ3UzVsMk1vZ2RrSXE3aXlYMzMyVUUxdFZ6dXZybDRVMl9jVTlRLTU?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxNSHlmWUhJMVl3T3ZHYUpsWnJ4S3BOWUhleGJtemdaaXdWRTc3VW9zVGdIem1JTVdyWjBwTUZsd2VnT2dyWWNpSkF0eDNKVHF4ckNPZGh2cEhqclZYX3JYTFNOb0tLRVhNdzFHR09GWC1qN001QjBCZzJuMnVCa21rTS1ucEYwZGVtSnhxdFpfQXpiQVUxMEVwZHlXcnJuNi1jR2JUVGhZRQ?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxQcVlqaXUwYkwwcHFqNjdaSk95ZEhFNlpBdmRsV1ZsM2loSExqZzh0TVhka3ZtQ2ljWGpULVlrTXU2SlpGM19LalpDV0dIZlZ6bVZmOWJaalFvcVFqRjJRUjMxVG5QUlFRYWR2RFplZ1FzYnNKRXowd1owNl9qZ2NHRHVDWHRZVnY4TENuSkZHaHJHLU43ZTlNR3pfcjllbTVC?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxNOHBTVFl0X0c1STJ6b2JOTElOUlhucUlDcTZwVUZoQ2ZNSUo0WXJQZWsyd0ZVWVZFam9hWUdRVEE1VThUT1JrVTN3RnEzemQ4YnJyTnlYenYxdm9zb0JSeVNuelA2R1dxeGNoaml0ZEtsREh1WFNkWDB4U2lNSGxyQjJETkFFdTRRVkZFWHBFLXdxUFZ2MUtZ?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxPeU53QjM2VzdMNWQ5dGtzNlVwLWdWbU9fenBHZ3pkLWFtYXJlYkJUWjViTTN1LVo3aU1oLXNiQU9DNjNKZzhlMnN6YlhaSDFabUF1NFgzMG9tT3YzWmNvWjRLWE0tWkZjai1tSWZiSjVBSjFCUkVrWTNobHhsaFpIbU9RdElsTGN4QVUtSXVrb2x0NHpwMlVUWWRYdVI?oc=5
- https://news.google.com/rss/articles/CBMifkFVX3lxTE5IV0M4bnduUzdZYjg0UjlTLS1CWkF2QlhvdUtlSkxmbWFfeDFzVjhPWTRBdWU5Y2lfU3Eta0N6d0VoNXVIeV9fdlpMQzZlWm5RZHo4UjluLVhrRkxkRWF5VlZDMTFKcVEtRzhQLW5LWlFIYlMxWFRnUnY3WWluQQ?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQWl90bVRBbmtwUVN2aEJ6enF6M0o4Yml4SlA2YVRvR3hCbkFFS1pVTnEweHlGMHd3UFgzQjBsY2ZIOEhpS1ZQbHY5U19jSk0xTF9yRHYzV0RmUGNNNmNCUW43a0wzUmxxVUtIaG9EV19xVU43a1ljcDFTTW5EYmxJNzJranVJbURuNUdJUU53OHJ1VXgzdS1md04xVzM?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxNakxvaEdiTzR5M0tqcm5KeE1mVDFYUTVuZlhCdzl6MHdXV0tiek90QU1qZHBxdktxWjNIaHNoRDhPNTVrN0F5OGx1VUtiTWhObkJRcl9pVXFDbzFsT2cxcTRwaHBKZF93cEgzM0JHd3VkVVpIZ0theFMxdEJIY2FvQ0xtSlQyNTMwNmlMRzVKYS0yRjZVMkR6cGln?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxPcmJmaDIwcnRLMjh1eGNUOGhuVjJNMGhyNFltVkNCYl9wMG43ck9jWnpNMHY0elFkWk1aYnM2WERaZ0lTWVpqV3AwVnYwZ2p2QVFWREpnRG5mV3dvRF8yMUhOb1NUcDlnSjAtUTlCanZkWWhINjhWWmcxS2g0aXZJUWEwY2Qyc0kxV25ibHJXNGVRelh5Um85N0x1TmFoZw?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxPeXYtc0wwTWRuR29fdGRXZE83a0JHb3Y2Q2Y4b3NPOXVZSjM3TEc5VzJhTkFBN1dHekhaUm9XOWdrbWl2OUx5eWRraVVIWm02YjhQV2M3MWpLbk5ld1c5TG1rRGE5Sm1Td0dMWFQ0b2dMYVp2Wko5SmxEMGEtSDFJWldKXzFEV3hjOTNtQkVFeVRpSjEzOFE?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxQRUdMOElZOWFLR1FCQzMxbE5XN0tJeElzdUdrUksySzktUlN3U2QyTGhLbmc0LVZ0b0RadmtCNzkzamlnV2d3dGZoU1Nveks4UHgwMmk4MU93b0owRHNtMjVTWEM4NDJPTDhlM2wyZ0hnbTl2djJ5eFZ4azRrdVN2T05TNWNXaTBHSWtQaG05NnNxV1NlTDdZS0IyQlNCZw?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxOblRPS2JSaEh6Z2xwbDBmN196Y3dZQW1sNkRMYTRSMHV2dzkyeEtETEVvc295b0k3S1RFcmZ2YjUwbWxBeVhrNEpBNzRVa1FuMlpFUUpaWnBER2NVejFXVGNNX2N2dTdoSVREN2NDcTFaTEtURzUyVUFkSTBIcFdpQ2txdUxvMWF5Z19vT3ln?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxQZkc4MEpkMmtxWldrMnI5ZUdHVjMyb1ZBU3duZklHdnBQekw0VnYzR0hoZWRMV3EtOUdScmpzd2E1ZEYxcjNfR3NKNWR6R3JzZWJtWE5SbG4ydTcxSzZRN3lXMmFHV01JaU1SSDNXVF8yRnM3U1VJS2RQYllEd0p3cGNTWV9jc3JTcjRpQkVla0ZLMUd3V1E?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxOLWVDY2lZaGRsVW16Y2RrUnJ5ek5ST2V1RzlPNFhLUVNCSmJnR2NMczJYN2d3XzlfbjQ2ZllRNllfcGxYQ3NwRWsxMUNjV1Q4anZXaVhhWVpKcnAtT3JVZThYVTlDbTAtLS0zRWtWX2JUTURETVlKLU5UMkVGb3huZVp6WGhNTGMxM1JJV2pKaGFWUjlyYjdxZ25yUQ?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxNNUstX3dpZlZvUHdaWndNVlVrakVBdVpncUk0a1BBVHA3WWpFRld6VUxlRGhxajF0b0dLMF9OM2hhSl83ekhfRkh2bWNPekRTcFVxbzJkczZfUWNMbkpvRmJNb1BkRHU4Z0U5ejlOUV90LXFSVmR1YTRDZHM5MXVPTXZJVzJ6Z0RlZDJaWndxYUlnTXF4RDlMdkl5bkxxMGM?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
