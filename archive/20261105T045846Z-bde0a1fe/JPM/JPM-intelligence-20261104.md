# JPM Intelligence Report

- ticker: **JPM**
- Report as_of: **2026-11-04**
- Market data as_of: **2026-11-04**
- Quant sources: https://finance.yahoo.com/quote/JPM/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/JPM/key-statistics/
- AI analysis snapshot as_of: **2026-11-04**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-05T05:10:13.078538+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 15, 'rule': 2, 'ai': 7, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **7** exact headline/source/date matches; prior report **20261104T044411Z-6b13f9ec/JPM** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 15 unique headlines; 7 named publishers; 0 exact duplicates; 15 HTTPS source links; largest publisher share 26.67%; oldest publication 2026-10-30

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 352.1100 |
| Return 1D (%) | 4.1807 |
| Return 1W (%) | 3.7754 |
| Return 1M (%) | 6.4645 |
| Return YTD (%) | 11.3809 |
| Return 1Y (%) | 16.0522 |
| Annualized volatility (%) | 22.5128 |
| Beta vs SPY | 0.7772 |
| Max drawdown (%) | -15.4717 |
| Sharpe (rf=0) | 0.7765 |
| Downside deviation (rf=0, %) | 16.0046 |
| Sortino (rf=0) | 1.0922 |
| Historical VaR 95% (1D, %) | 2.3879 |
| Historical ES 95% (1D, %) | 3.2600 |
| Correlation vs SPY | 0.4433 |
| Tracking error vs SPY (%) | 20.3821 |
| P/E (trailing) | 14.77 |
| P/B | 2.66 |
| EV/EBITDA | N/A |
| Revenue growth (%) | 10.20 |
| Forward P/E (estimate) | 13.77 |
| Gross margin (%) | 0.00 |
| Operating margin (%) | 42.58 |
| Return on equity (%) | 18.01 |
| Free cash flow yield (%) | N/A |
| MA50 | 341.6401 |
| Close vs MA50 (%) | 3.0646 |
| MA200 | 320.9003 |
| Close vs MA200 (%) | 9.7257 |
| RSI (14, Wilder) | 63.6275 |
| MACD (12,26) | 1.0657 |
| MACD signal (9) | -0.7082 |
| MACD histogram | 1.7739 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'JPM': 275, 'SPY': 275}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 352.1100 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 4.1807 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 3.7754 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 6.4645 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 11.3809 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 16.0522 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 22.5128 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 16.0046 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.0922 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.3879 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.2600 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4433 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 20.3821 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.7772 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -15.4717 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.7765 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 13.7688 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 0.0000 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 42.5840 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 18.0130 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 14.7697 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 63.6275 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 1.7739 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 3.0646 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 9.7257 -> Clearly above the moving-average trend level.

## TAILWINDS

### JPMorgan Chase & Co. (NYSE:JPM) Shares Climb 4.2% - Still a Buy?
- Summary: JPMorgan Chase & Co. (NYSE:JPM) Shares Climb 4.2% - Still a Buy?
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxNVWxOeW1RbUJRaHhDYjBUeW1XYlBpekxJVTIwUWNWRzBxcUo5V1YzZWN6STVDMEdMOFB1bXMxakRIQ2Nqb3htUzdTWjNsNXEtYVc5NkMwRDdyTFJfWFpCVnpzTW9ueVpKYk1sSmpGZlZfcXh1TXp5dzFJaWh3TEJQb2V4eEF1YXdjX2pQOG5ZRks5VzJjcE9TR2ZTZnhBdWpacVY2UGdpUmpHd0dyVUtoLTlsZkk?oc=5>

### JPMorgan Chase & Co. (NYSE:JPM) Stock Price Up 1.1% After Analyst Upgrade
- Summary: JPMorgan Chase & Co. (NYSE:JPM) Stock Price Up 1.1% After Analyst Upgrade
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxPeVBaeVl2dlVyRlhuVTlZWVVkaHJZU284ZzFTYWh5TUo3cU14MHVNYm5YUHFNZFNFd1Btejl6Tl93VEhvYlk1QWktMmdLRzdnNTBkdTF3RzdiQVRxWUxwaHpfcUthT3FhVi1zMjB1TV81OWRXbUVKSnFJUWZ5bjdUTUc5RnhzR2x1Nlc5WkROaVhFc3hLVE12MmpKRkh1Vi0wRjFkb19TQ09WTzNTV3JlQ2FMTkpSZmdEU2doZUNtNTkxZVRa?oc=5>

### JPMorgan Chase (JPM) Draws Fresh ETF Buying, Is The Stock Still Undervalued?
- Summary: ETF buying indicates increased demand for JPM shares.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMixgFBVV95cUxNdUVKQkh1T29HY3dqdnllRFIxTS1xRXhiaE1fa1c4cnVMWVNhaG5kSWNRajBjWU9JdGxPdnRrLS1nZmt4RUVLLUw4X3NjNWp4SllRR2VINXkyTG9qb3lNNG4wd2tPY3k4SGdpa3Z0eVhUR0UwRjhpSF84VjhDeEFVTHdlV3otLUtuYmprVHo0dGZYaVlnM1lES0FhV2tEeDh5T0ZoNkRZQ2dUeE5YdnV1VXJJY3JhWjJ6MUtqZzcwSDZIWE9ZaEHSAcsBQVVfeXFMTzd6YTVqeGJWUjFaLW5FYlhPcmNqQ2hLMkhtM1d5c25SSDBiLVJQeGpIYXprS1BlT0VOTUpibGlpZVl2aXpybkdyeWYtcmVmMXRLdU83ODdMTVpZRWtVak5xbGlZcE9lRHBkaXdVV2hyLVlhMkl5TW9zOHZSMjZwQWJvYnBGM3BuTHR4RklMbVRkbkNuQUUwREo5TWRoSkJyYk1jdUVJQWpsSVJUdk9PQzRfMG9sWjI4WFlCbnNzVnlxemdVSVVkU2k1Zzg?oc=5>

### What Does JPMorgan Chase (JPM) Gain From Its Dubai Push And US Hires?
- Summary: JPM is expanding its presence in Dubai and hiring in the U.S., potentially boosting its global footprint and client base.
- Date: 2026-11-04 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQcmlBcHZCVmVlNFlabHJPWU9HaHJweFV4cVhybU1nZ29OOU8xdXFUckM1QXhza0RiVG0zSUhRcmdGcGNkWVhteVdwUGJYbDNKMS12TjlOU1VHRWZhWU82WXZrblo4NWZ0TzNYRG5hby1tUFFFdkNZZGlsY3BERFVsRks1bmdpTlQ4dV9GeDgzNjR0R09ESHRnYQ?oc=5>

### JPMorgan Chase reports higher Q3 earnings: Can JPM continue its gains?
- Summary: JPMorgan Chase posted higher Q3 earnings, raising questions about sustaining growth.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 1
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxNTlZxWXV5WWxUZ0hma2FkYVF6SFVvNmR6ejdnM25BRmgxa2FXM2dxZTgwQkpjZ1NYa1VBMzI4NUh1MFFoT3dIUGRLeXlHNm92REZLZkNfLVpBV2pzY09QM1FrTEFfUm1RaUsyYjQ5OHZMeElVSkpINUR1TXZpQTdFQnNncmNaZUpKWjBOZkl4cw?oc=5>

## HEADWINDS

### Learn Why The Bull Case For JPMorgan Chase Stock Could Change Following Earnings Miss
- Summary: JPM missed earnings expectations, potentially weakening its bull case.
- Date: 2026-11-01 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQN3lvaEZRZy1SYlZ2cVlxSlRjTHJERVNPbE00T0JUS3JhdHUzQmlnMGtEX1R0WTF5eS1UcTEyYlBWcmM0RlB4eWJMaWQ5aW42b0dja0dxMTFfaVB4QXA3aENadDczdTA2WDRndkRlbGNhQlhreGxhakxLcGVlUk1nMVNoTjVDNVNGS0RtLV9PcGZpTUZ0MWtPVA?oc=5>

## CATALYSTS

### JPMorganChase had $5.1 trillion in assets on Sept. 30 and filed its quarterly report.
- Summary: Quarterly filing provides financial performance data.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxQa2NsUU1QVERDdHlSN0F1Z1ppZGJITjlranczVnVYYUJIS25VQ3pJSzFzaEEwRlVadG5qeGdLSnh0aUxUb3Q3RHRPanVGeW14NlVoejdDUXFPLWpXSmVpdkN3VUtpVEZxRUkwNXZiVG81OExaYzVzQmZvWHl2dHlEMm5QYjZ0dDl0RU1Zb2g5ZF9sb0lHTTJmaEZNSmpjYTFaT3Uxa2pJX29hWGI0MHU4RjJTTkN6VW5CUGJRNg?oc=5>

### Why Is JPMorgan Chase (NYSE:JPM) Setting The Tone For Blue Chip Stocks?
- Summary: Analysts discuss JPMorgan's influence on blue-chip market trends.
- Date: 2026-11-03 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxNeDFOLXZobFQweGk4d2dHQ0FWTDduNWNrSWNIQTc1WDJoRmh1VlRReE42Rk8yVFZWYzdWdjdZR0FMX2lfVzZPdzlxWGNFM1JuOEg5WDAxYmdLd3dlS0NxYTZZcy1QWkdNak1oVnUtWHlqUnV4TnMyYXRWNVBBRjBQSEZGSklWNWpNbGdhR2ctM3lUUTFmai1nMUF4UmdsbUNmdVRWMWFYR3lmNmNOYVBsRA?oc=5>

### JPMorgan Chase (JPM) Stock May Be 32% Undervalued Following Blockchain Expansion
- Summary: Analysts suggest JPM's stock is undervalued due to its blockchain initiatives, indicating potential upside.
- Date: 2026-11-02 | Impact: medium | Horizon: medium | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMixgFBVV95cUxNQUtmOUNqSlFCMFFPVTBHYTlUN1BPVVhLVEh5LTNWNi1ka2lWeHBOMnNENVR3NWV2dGZIaURWR3Z5SkdfM3BxZ1dxOVZYUU55Wmp3NnlGSmFsb2djUmwyMWZlVnBmcnctMXlaX2Z5MlE1RWZoNFhvZU9kXzVqZXlBM2R3aTZPUXM4by1mbzJHNGJweDJrMVcxZjdnakJDXzN6NDF5QV9BSW1LRThHZTJDVHNvTkZZT0YzM0c0aFQ1M2JjdGw0Q3fSAcsBQVVfeXFMTmZFeXpBTGVaTW0tazZNUFJoVXRnaFBDZFBaNTA0TjFoWUN0RjZjaE95SmUxRmpMQXhsVXZHWmtfMlk4eFNDNS1lREp6OW5ma1BBeUlHYXFsTE5RVS16dUpoZm1Tal95c0hKQjNQMWxUc3JKR1dCT1ZqZjdvNTZGdDl2QUZJVUtTQjYtamdudGFHRkpRa1lZM0k5RVdnemRtaW5Ya3c0OWZUOFJjenp6WmtnMlJOclJBdFBya3M3ajIwUXl3OU0tQ1dpX1k?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **JPM** | **14.77** | **2.66** | **N/A** | **10.20** | **935,063,322,624.00 USD** | **16.05** |
| BAC | 11.84 | 1.32 | N/A | 3.40 | 356,257,792,000.00 USD | -1.51 |
| C | 11.96 | 1.08 | N/A | 8.00 | 206,469,644,288.00 USD | 26.05 |
| WFC | 12.06 | 1.65 | N/A | 0.40 | 262,451,773,440.00 USD | 2.53 |

Peers fetched as_of: 2026-11-04; JPM reuses existing data (market data as_of: 2026-11-04); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-13
- Next expected earnings: 2027-01-14 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-04

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-03
- Revenue (latest available single quarter): 24,246,000,000.00 USD; period 2014-07-01/2014-09-30; fiscal year/reporting period 2014/Q3
- Net income (latest available single quarter): 15,305,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/19617/000162828026069523/jpm-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMitAFBVV95cUxNVWxOeW1RbUJRaHhDYjBUeW1XYlBpekxJVTIwUWNWRzBxcUo5V1YzZWN6STVDMEdMOFB1bXMxakRIQ2Nqb3htUzdTWjNsNXEtYVc5NkMwRDdyTFJfWFpCVnpzTW9ueVpKYk1sSmpGZlZfcXh1TXp5dzFJaWh3TEJQb2V4eEF1YXdjX2pQOG5ZRks5VzJjcE9TR2ZTZnhBdWpacVY2UGdpUmpHd0dyVUtoLTlsZkk?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxPeVBaeVl2dlVyRlhuVTlZWVVkaHJZU284ZzFTYWh5TUo3cU14MHVNYm5YUHFNZFNFd1Btejl6Tl93VEhvYlk1QWktMmdLRzdnNTBkdTF3RzdiQVRxWUxwaHpfcUthT3FhVi1zMjB1TV81OWRXbUVKSnFJUWZ5bjdUTUc5RnhzR2x1Nlc5WkROaVhFc3hLVE12MmpKRkh1Vi0wRjFkb19TQ09WTzNTV3JlQ2FMTkpSZmdEU2doZUNtNTkxZVRa?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxNdUVKQkh1T29HY3dqdnllRFIxTS1xRXhiaE1fa1c4cnVMWVNhaG5kSWNRajBjWU9JdGxPdnRrLS1nZmt4RUVLLUw4X3NjNWp4SllRR2VINXkyTG9qb3lNNG4wd2tPY3k4SGdpa3Z0eVhUR0UwRjhpSF84VjhDeEFVTHdlV3otLUtuYmprVHo0dGZYaVlnM1lES0FhV2tEeDh5T0ZoNkRZQ2dUeE5YdnV1VXJJY3JhWjJ6MUtqZzcwSDZIWE9ZaEHSAcsBQVVfeXFMTzd6YTVqeGJWUjFaLW5FYlhPcmNqQ2hLMkhtM1d5c25SSDBiLVJQeGpIYXprS1BlT0VOTUpibGlpZVl2aXpybkdyeWYtcmVmMXRLdU83ODdMTVpZRWtVak5xbGlZcE9lRHBkaXdVV2hyLVlhMkl5TW9zOHZSMjZwQWJvYnBGM3BuTHR4RklMbVRkbkNuQUUwREo5TWRoSkJyYk1jdUVJQWpsSVJUdk9PQzRfMG9sWjI4WFlCbnNzVnlxemdVSVVkU2k1Zzg?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQcmlBcHZCVmVlNFlabHJPWU9HaHJweFV4cVhybU1nZ29OOU8xdXFUckM1QXhza0RiVG0zSUhRcmdGcGNkWVhteVdwUGJYbDNKMS12TjlOU1VHRWZhWU82WXZrblo4NWZ0TzNYRG5hby1tUFFFdkNZZGlsY3BERFVsRks1bmdpTlQ4dV9GeDgzNjR0R09ESHRnYQ?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxNTlZxWXV5WWxUZ0hma2FkYVF6SFVvNmR6ejdnM25BRmgxa2FXM2dxZTgwQkpjZ1NYa1VBMzI4NUh1MFFoT3dIUGRLeXlHNm92REZLZkNfLVpBV2pzY09QM1FrTEFfUm1RaUsyYjQ5OHZMeElVSkpINUR1TXZpQTdFQnNncmNaZUpKWjBOZkl4cw?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQN3lvaEZRZy1SYlZ2cVlxSlRjTHJERVNPbE00T0JUS3JhdHUzQmlnMGtEX1R0WTF5eS1UcTEyYlBWcmM0RlB4eWJMaWQ5aW42b0dja0dxMTFfaVB4QXA3aENadDczdTA2WDRndkRlbGNhQlhreGxhakxLcGVlUk1nMVNoTjVDNVNGS0RtLV9PcGZpTUZ0MWtPVA?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxQa2NsUU1QVERDdHlSN0F1Z1ppZGJITjlranczVnVYYUJIS25VQ3pJSzFzaEEwRlVadG5qeGdLSnh0aUxUb3Q3RHRPanVGeW14NlVoejdDUXFPLWpXSmVpdkN3VUtpVEZxRUkwNXZiVG81OExaYzVzQmZvWHl2dHlEMm5QYjZ0dDl0RU1Zb2g5ZF9sb0lHTTJmaEZNSmpjYTFaT3Uxa2pJX29hWGI0MHU4RjJTTkN6VW5CUGJRNg?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxNeDFOLXZobFQweGk4d2dHQ0FWTDduNWNrSWNIQTc1WDJoRmh1VlRReE42Rk8yVFZWYzdWdjdZR0FMX2lfVzZPdzlxWGNFM1JuOEg5WDAxYmdLd3dlS0NxYTZZcy1QWkdNak1oVnUtWHlqUnV4TnMyYXRWNVBBRjBQSEZGSklWNWpNbGdhR2ctM3lUUTFmai1nMUF4UmdsbUNmdVRWMWFYR3lmNmNOYVBsRA?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxNQUtmOUNqSlFCMFFPVTBHYTlUN1BPVVhLVEh5LTNWNi1ka2lWeHBOMnNENVR3NWV2dGZIaURWR3Z5SkdfM3BxZ1dxOVZYUU55Wmp3NnlGSmFsb2djUmwyMWZlVnBmcnctMXlaX2Z5MlE1RWZoNFhvZU9kXzVqZXlBM2R3aTZPUXM4by1mbzJHNGJweDJrMVcxZjdnakJDXzN6NDF5QV9BSW1LRThHZTJDVHNvTkZZT0YzM0c0aFQ1M2JjdGw0Q3fSAcsBQVVfeXFMTmZFeXpBTGVaTW0tazZNUFJoVXRnaFBDZFBaNTA0TjFoWUN0RjZjaE95SmUxRmpMQXhsVXZHWmtfMlk4eFNDNS1lREp6OW5ma1BBeUlHYXFsTE5RVS16dUpoZm1Tal95c0hKQjNQMWxUc3JKR1dCT1ZqZjdvNTZGdDl2QUZJVUtTQjYtamdudGFHRkpRa1lZM0k5RVdnemRtaW5Ya3c0OWZUOFJjenp6WmtnMlJOclJBdFBya3M3ajIwUXl3OU0tQ1dpX1k?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
