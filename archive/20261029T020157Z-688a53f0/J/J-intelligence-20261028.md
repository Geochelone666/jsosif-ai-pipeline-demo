# J Intelligence Report

- ticker: **J**
- Report as_of: **2026-10-28**
- Market data as_of: **2026-10-28**
- Quant sources: https://finance.yahoo.com/quote/J/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/J/key-statistics/
- AI analysis snapshot as_of: **2026-10-28**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-29T02:18:50.779716+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 5, 'rule': 1, 'ai': 2, 'unknown': 0, 'irrelevant': 2})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **2** exact headline/source/date matches; prior report **20261028T015717Z-533e470c/J** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 5 unique headlines; 5 named publishers; 0 exact duplicates; 5 HTTPS source links; largest publisher share 20.0%; oldest publication 2026-10-23

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 150.9100 |
| Return 1D (%) | 1.7325 |
| Return 1W (%) | 5.9092 |
| Return 1M (%) | 9.0627 |
| Return YTD (%) | 14.8651 |
| Return 1Y (%) | -3.6588 |
| Annualized volatility (%) | 32.6474 |
| Beta vs SPY | 0.7700 |
| Max drawdown (%) | -31.9224 |
| Sharpe (rf=0) | 0.0499 |
| Downside deviation (rf=0, %) | 24.3361 |
| Sortino (rf=0) | 0.0669 |
| Historical VaR 95% (1D, %) | 3.0123 |
| Historical ES 95% (1D, %) | 5.1035 |
| Correlation vs SPY | 0.2996 |
| Tracking error vs SPY (%) | 31.2845 |
| P/E (trailing) | 49.32 |
| P/B | 5.41 |
| EV/EBITDA | 19.43 |
| Revenue growth (%) | 34.50 |
| Forward P/E (estimate) | 18.32 |
| Gross margin (%) | 22.07 |
| Operating margin (%) | 7.39 |
| Return on equity (%) | 8.00 |
| Free cash flow yield (%) | 3.66 |
| MA50 | 143.4496 |
| Close vs MA50 (%) | 5.2007 |
| MA200 | 133.2011 |
| Close vs MA200 (%) | 13.2949 |
| RSI (14, Wilder) | 67.6569 |
| MACD (12,26) | 1.8118 |
| MACD signal (9) | 0.5689 |
| MACD histogram | 1.2429 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'J': 270, 'SPY': 270}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 150.9100 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.7325 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 5.9092 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 9.0627 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 14.8651 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -3.6588 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 32.6474 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 24.3361 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.0669 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.0123 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.1035 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2996 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 31.2845 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.7700 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -31.9224 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.0499 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 18.3212 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 22.0670 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 7.3870 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 7.9980 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 3.6557 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 49.3170 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 67.6569 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 1.2429 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 5.2007 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 13.2949 -> Clearly above the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

No items in this run

## CATALYSTS

### Jacobs Solutions Inc. $J Stock Sold by Robeco Institutional Asset Management B.V.
- Summary: Jacobs Solutions Inc. $J Stock Sold by Robeco Institutional Asset Management B.V.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1AFBVV95cUxNN3A4MnJ4RzhIZGNPX3Z6VkNwZVBlOWJTeVhOZGJ6bWxZdElRSkdlUE51LUIzdVVlazNycExuVjRrVTJfMnJxclJMcEdITC05NXo1bUMzWm9MdVhZX2pMeGZ1U3VGUjNxQU5QNXFGYTktVmRzc1ltQ0dpWnI4QnNOZ01SUWpjcExPUXNMWW9jMHQ1TTdQZUZUMWJsVldQUnowdkRlXzdSc21mVUQ1clVNdXBoY3B5VjBJbTdPa3VVR0lDdzlYbnpNdl85Q1RLeE9obEtpbA?oc=5>

### Jacobs Solutions (J) Stock Could Be 49% Below Fair Value On Wastewater Project Win
- Summary: Jacobs Solutions may be undervalued after winning a major wastewater contract, potentially boosting stock value.
- Date: 2026-10-28 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNOHVva3BIWjNuX3UtUEZFZWlNSzl4UktFc3lfNEV0b0N4RXhwRllJQzJtZERuSW8xM253bGhVcGFvZ3Jrc3h3LTdlX1J4VzNMQzhKRDRjZnZNWm02MXJmWDdxMjZyNUdHMURQVW9kYldBQjdnb3ZsakxNNVV5NXpHaHdFQ2xCQzFqOG93UDVEOWtaWWo2bXc3NmEtWQ?oc=5>

### How Investors May Respond To Jacobs Solutions (J) Major Wastewater Contract
- Summary: Investors could react positively to Jacobs Solutions securing a significant wastewater contract, indicating growth potential.
- Date: 2026-10-28 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi2AFBVV95cUxPQV9Sc01WSEtWQ0dvMXE0bUVTQ3h0NDNuM21FekdYUUZsTjY0VV9NcHFqN1UzVVNjcGpEVGpUNWw2bC1va1YwQVR2d2JNbWdBeENrMVByaWYzUzZqOWVOc3BEcXdGWUEzeDFXa3JzcjVmR05xODMzY052Y3RWVjNaSUdqUElmVm1TRGlqR2QwRUU1eV9zQVhOaE16S2JMWDZyVzNUdVpUTzdRR1dKTnZjN09rYmI1TzMxVWtSRGxleUphUDZFem9CdUQtTGpGWG5fcklQaHVJTHfSAd4BQVVfeXFMT2V3T2VENlBiaGJIYkdHWGgyTjl3UUlWR0pFV3NwNk01ejhJZUNMVUN3eUhqRjRFRm9YSjVpTXhxS1JwNjdya1oyRjA4TWxVZGFxYjJ0MU1Dc0F5NGo4dVdmTnduaGI3MXRCSHk0Z3BlLV9Id3BYdDIxVlBkcTh4ckQ1LWdaWTZuWDVHMnF1SmIzajNXQzVldHJLWUNyVE5uS1hWb2dBZUgxcVd6NjA0M2J4OGw0UWlncDNmdG5EbXVaYzRKclRlTUFUN19ucUVnVUs1QlpGckR0R0h4aUxB?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **J** | **49.32** | **5.41** | **19.43** | **34.50** | **17,662,296,064.00 USD** | **-3.66** |
| ACM | 21.70 | 3.65 | 11.30 | -14.20 | 8,013,926,400.00 USD | -52.16 |
| FLR | N/A | 2.37 | -18.93 | 8.80 | 6,281,818,112.00 USD | -6.08 |
| KBR | 12.09 | 3.09 | 11.19 | 1.60 | 5,060,359,680.00 USD | -5.12 |

Peers fetched as_of: 2026-10-28; J reuses existing data (market data as_of: 2026-10-28); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-04
- Next expected earnings: 2026-11-23 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-28

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-08-04
- Revenue (latest available single quarter): 4,142,644,000.00 USD; period 2018-06-30/2018-09-28; fiscal year/reporting period 2018/FY
- Net income (latest available single quarter): 136,553,000.00 USD; period 2026-03-28/2026-06-26; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/52988/000162828026052573/jec-20260626.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMi1AFBVV95cUxNN3A4MnJ4RzhIZGNPX3Z6VkNwZVBlOWJTeVhOZGJ6bWxZdElRSkdlUE51LUIzdVVlazNycExuVjRrVTJfMnJxclJMcEdITC05NXo1bUMzWm9MdVhZX2pMeGZ1U3VGUjNxQU5QNXFGYTktVmRzc1ltQ0dpWnI4QnNOZ01SUWpjcExPUXNMWW9jMHQ1TTdQZUZUMWJsVldQUnowdkRlXzdSc21mVUQ1clVNdXBoY3B5VjBJbTdPa3VVR0lDdzlYbnpNdl85Q1RLeE9obEtpbA?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNOHVva3BIWjNuX3UtUEZFZWlNSzl4UktFc3lfNEV0b0N4RXhwRllJQzJtZERuSW8xM253bGhVcGFvZ3Jrc3h3LTdlX1J4VzNMQzhKRDRjZnZNWm02MXJmWDdxMjZyNUdHMURQVW9kYldBQjdnb3ZsakxNNVV5NXpHaHdFQ2xCQzFqOG93UDVEOWtaWWo2bXc3NmEtWQ?oc=5
- https://news.google.com/rss/articles/CBMi2AFBVV95cUxPQV9Sc01WSEtWQ0dvMXE0bUVTQ3h0NDNuM21FekdYUUZsTjY0VV9NcHFqN1UzVVNjcGpEVGpUNWw2bC1va1YwQVR2d2JNbWdBeENrMVByaWYzUzZqOWVOc3BEcXdGWUEzeDFXa3JzcjVmR05xODMzY052Y3RWVjNaSUdqUElmVm1TRGlqR2QwRUU1eV9zQVhOaE16S2JMWDZyVzNUdVpUTzdRR1dKTnZjN09rYmI1TzMxVWtSRGxleUphUDZFem9CdUQtTGpGWG5fcklQaHVJTHfSAd4BQVVfeXFMT2V3T2VENlBiaGJIYkdHWGgyTjl3UUlWR0pFV3NwNk01ejhJZUNMVUN3eUhqRjRFRm9YSjVpTXhxS1JwNjdya1oyRjA4TWxVZGFxYjJ0MU1Dc0F5NGo4dVdmTnduaGI3MXRCSHk0Z3BlLV9Id3BYdDIxVlBkcTh4ckQ1LWdaWTZuWDVHMnF1SmIzajNXQzVldHJLWUNyVE5uS1hWb2dBZUgxcVd6NjA0M2J4OGw0UWlncDNmdG5EbXVaYzRKclRlTUFUN19ucUVnVUs1QlpGckR0R0h4aUxB?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
