# JPM Intelligence Report

- ticker: **JPM**
- Report as_of: **2026-11-02**
- Market data as_of: **2026-11-02**
- Quant sources: https://finance.yahoo.com/quote/JPM/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/JPM/key-statistics/
- AI analysis snapshot as_of: **2026-11-02**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-03T05:41:17.385780+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 8, 'ai': 6, 'unknown': 0, 'irrelevant': 11})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **7** exact headline/source/date matches; prior report **20261102T041627Z-c84a7052/JPM** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 8 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 60.0%; oldest publication 2026-10-27

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 340.5800 |
| Return 1D (%) | 1.0503 |
| Return 1W (%) | 1.9578 |
| Return 1M (%) | 2.9783 |
| Return YTD (%) | 7.7337 |
| Return 1Y (%) | 11.5774 |
| Annualized volatility (%) | 22.1589 |
| Beta vs SPY | 0.7439 |
| Max drawdown (%) | -15.4717 |
| Sharpe (rf=0) | 0.6351 |
| Downside deviation (rf=0, %) | 16.0182 |
| Sortino (rf=0) | 0.8786 |
| Historical VaR 95% (1D, %) | 2.3923 |
| Historical ES 95% (1D, %) | 3.2600 |
| Correlation vs SPY | 0.4304 |
| Tracking error vs SPY (%) | 20.2691 |
| P/E (trailing) | 14.29 |
| P/B | 2.57 |
| EV/EBITDA | N/A |
| Revenue growth (%) | 10.20 |
| Forward P/E (estimate) | 13.32 |
| Gross margin (%) | 0.00 |
| Operating margin (%) | 42.58 |
| Return on equity (%) | 18.01 |
| Free cash flow yield (%) | N/A |
| MA50 | 342.0292 |
| Close vs MA50 (%) | -0.4237 |
| MA200 | 320.4813 |
| Close vs MA200 (%) | 6.2714 |
| RSI (14, Wilder) | 53.7877 |
| MACD (12,26) | -0.1807 |
| MACD signal (9) | -1.4110 |
| MACD histogram | 1.2303 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'JPM': 273, 'SPY': 273}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 340.5800 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.0503 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 1.9578 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 2.9783 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 7.7337 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 11.5774 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 22.1589 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 16.0182 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.8786 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.3923 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.2600 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4304 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 20.2691 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.7439 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -15.4717 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.6351 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 13.3179 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 0.0000 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 42.5840 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 18.0130 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 14.2861 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 53.7877 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 1.2303 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -0.4237 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 6.2714 -> Clearly above the moving-average trend level.

## TAILWINDS

### JPMorgan Chase & Co. (NYSE:JPM) Stock Price Up 1.1% After Analyst Upgrade
- Summary: JPMorgan Chase & Co. (NYSE:JPM) Stock Price Up 1.1% After Analyst Upgrade
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxPeVBaeVl2dlVyRlhuVTlZWVVkaHJZU284ZzFTYWh5TUo3cU14MHVNYm5YUHFNZFNFd1Btejl6Tl93VEhvYlk1QWktMmdLRzdnNTBkdTF3RzdiQVRxWUxwaHpfcUthT3FhVi1zMjB1TV81OWRXbUVKSnFJUWZ5bjdUTUc5RnhzR2x1Nlc5WkROaVhFc3hLVE12MmpKRkh1Vi0wRjFkb19TQ09WTzNTV3JlQ2FMTkpSZmdEU2doZUNtNTkxZVRa?oc=5>

### JPMorgan Chase & Co. (NYSE:JPM) Stock Jumps 1.3% - Here's What Happened
- Summary: JPMorgan Chase & Co. (NYSE:JPM) Stock Jumps 1.3% - Here's What Happened
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxQUkJ4WmtfOUVNSmVqNE5wWTRoelpORGlRQUhCTUpsVUhmYlN2OUdfVmZDeUo4ZExqNFFBMEptQVNtR1pLVENjeDBHbzItRjh5b0ZMb3dJc0J6RU5YeFFhNTBDYk9VRXpmMXdMTHlwTFRTLWZ2dXdVMWRjNGF5NmVDeklrVVBrVl9GaFJ2MWxwU1lfeUpMYWdGd3RBOXoxa1hhQ3JwR1N2MC1zUFJwRWcyU3hqeVlnVHdWejlOV3Bn?oc=5>

### JPMorgan Chase & Co. $JPM Stake Lifted by Oppenheimer & Co. Inc.
- Summary: Oppenheimer increases its JPM stake, indicating confidence in the bank.
- Date: 2026-11-01 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxQREhXVnQxOXFEUF8zaF9idGJfRU1UdTItOWRXU1k5RmZDZUlTTjhaTlRxSFFDR3FOdVdlNS1Ya3h4WEZ3RVoyMnRFUUFkdWFmSkJuYmVfam9NbVFVSDVvdy0xaGI2a1VUYlo1N0RJMURyWFByYkEzZGtaQzA2UFRfcWQ0RDBBSktvdWVlcHdUanlUT2ZGdWZVTmZKVENuN29tVEdfOW5VaUpGOUVBcktWajRaVTlxQVlt?oc=5>

## HEADWINDS

### JPMorgan Chase & Co. (NYSE:JPM) Shares Down 1.9% - Here's Why
- Summary: JPMorgan Chase & Co. (NYSE:JPM) Shares Down 1.9% - Here's Why
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxONjItaEJtcUNLWXd2Rk5DZzRXcDFLQXY4WWo3dEZrLWlHaTl6WmZiU2NwQ2s1bjFza0xuLTJycHFYbkpzMzE5LUhGNExJelRlUjNBWE9tRG9zVzdPQW90X2xqRWJXY1dSQ21BdlRib0FyOWM2Mm1FdE9BNDIzY09xU01TMkhuRXpKWW0zZUFBdXFmLWdTOGk2UE1YM24tX0NFMThCUjBJRlFncUtWcmV3RQ?oc=5>

### Learn Why The Bull Case For JPMorgan Chase Stock Could Change Following Earnings Miss
- Summary: JPM missed earnings expectations, potentially weakening its bull case.
- Date: 2026-11-01 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQN3lvaEZRZy1SYlZ2cVlxSlRjTHJERVNPbE00T0JUS3JhdHUzQmlnMGtEX1R0WTF5eS1UcTEyYlBWcmM0RlB4eWJMaWQ5aW42b0dja0dxMTFfaVB4QXA3aENadDczdTA2WDRndkRlbGNhQlhreGxhakxLcGVlUk1nMVNoTjVDNVNGS0RtLV9PcGZpTUZ0MWtPVA?oc=5>

## CATALYSTS

### JPMorgan Chase & Co. $JPM Stock Acquired by Generali Asset Management SPA SGR
- Summary: JPMorgan Chase & Co. $JPM Stock Acquired by Generali Asset Management SPA SGR
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizwFBVV95cUxNWUxiM1htTGl3NVc0NU1fa3pHc2NoU0YxMjdpYlFLN04tNVVhdV9XNFFNZ3JFVmlZam9fV0MyUHVqNXRYOUc4TWNCNXB4VGdLNXc3ODZmNDQ5dnZ0LVpqWnQ5NldnWFh5UzJOcjFLaU9mRmIwTm44TmN6S1BNc3BGdnhqNWk0V1Bpc1FHRVpvWGI1WUhTaXRNekgxdmRNLVh5R2NFVWJ2dmNvdDlfbjZYemlDQUF3cFZfXzA0dWk5S1dET05hUGtWSzJzZzd2M2c?oc=5>

### JPMorgan Chase & Co. $JPM Stock Sold by Mcdonald Capital Investors Inc. CA
- Summary: JPMorgan Chase & Co. $JPM Stock Sold by Mcdonald Capital Investors Inc. CA
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiygFBVV95cUxNWkQ5UnRYd2ROdFNTR0lMOWxFWTQyZnBwS0hnU0twWEFJWURXMldZN00tNHRnTnVITkNOaGZsTjF3VnUtb1VUX0tONUIxNlpHVmM4OFJoTXl0cnZDLUw4UVJ5M1BCb0tyWUw1RnBUSnF2TUFPSzJMcEVDS05PM0hiY0VKTUJmdWVsN1lmYldmcTRJTjZuVWxtLTlNc2hSUDFFcFphbDAwSFp1RGNQR3ctMjItWk1hbXN5M0V6Y0Fha3dDeUcybUJhYjV3?oc=5>

### JPMorgan Chase & Co. $JPM Stock: Asset Management One Co. Ltd. Increases Stake
- Summary: JPMorgan Chase & Co. $JPM Stock: Asset Management One Co. Ltd. Increases Stake
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizAFBVV95cUxOaHA3WU1meEx6YW1OS2dXc3pOTFBYQjlWSUsyR2wwTExkRThmOVUwbTR0aDdlblNfSWJUQ3F6LTZBM2hnbE0xeFJMSXpyTllQMGIwSGlhNTZhckEwa2FfeVBhaThMNDNiSVFjYjdBWmVpSEdULXQ2a19OVHU2Vm9fcHdwRU5VTHZqa2pOVVI0OGV2NUZ4WWU3U0IyTS1laVZtOERmT0FQX19vV083SVVGbmRMcEV3RmhDQ1R4eFNmd2JDeE10LXBkOW90YTQ?oc=5>

### JPMorgan Chase & Co. $JPM Stock Purchased by Verdence Capital Advisors LLC
- Summary: JPMorgan Chase & Co. $JPM Stock Purchased by Verdence Capital Advisors LLC
- Date: 2026-11-01 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiywFBVV95cUxPQk5MN1U0YjRuTWU2YnpJZWlmNmdydWhUc1h0c0J6WENIZFVWY19wTWxwLWtXV3plTTBrX3VxSldXNGNJYTM2MHNKa3A5ajZCUmdqTDJqQ2NDd2x6dUZrdmRsN2dSQU9ERWNxVEpVdzhvaUJxcWppN0dBaTY1dHIxSlY2ektiUmNrWFVZZkFOZzEtOG1kLTZURnozYjFhMzZDeUE4RFJ4bHQ1TE1Bc3FwS1BUSGdjQ1F2VE9TS2tOYUZJc0RwMmRKU1A5OA?oc=5>

### JPMorgan Chase & Co. $JPM Stock: Mill Capital Management LLC Cuts Stake
- Summary: JPMorgan Chase & Co. $JPM Stock: Mill Capital Management LLC Cuts Stake
- Date: 2026-11-01 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixgFBVV95cUxQajJ1YVV2UzI0VldHWEJpMmtQUlNEaTN6R3RfdktGd1dxVTI0ZzlnYUZBa011VWNpNlNfSlh0OTdSMWtRNHRsXzdDVHVJaEQzOS1yTGROcENsaDh6c05ISkxCb0NvUFNYa05haFo3Qi1JaWJONTdTZ0s0OWRrT0ZTM3BHMkZWSXdNOEEwMkV4bkpJNEtVUEJpeGExMGM3Z2RnSzhpcVVWbFZPbWRBRzdFcDEtSFM3dTExZ0N6UGhuUEpzcklmSkE?oc=5>

### JPMorgan to lead Anthropic's U.S. retail IPO offering - report (ANT:Pending)
- Summary: JPMorgan is set to lead Anthropic’s U.S. retail IPO, positioning the bank as a key underwriter for the AI firm’s public debut.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxOdEFrNlV2MlJVWEh5LWM1ZFdVcHBaSDhqdk15Y2UxUVdCSUEtaGI1QmE1TmhhVmtGelJ4a3U2cVp6bHJBS0ZwZTJZSnQwSGJxdXhRamxhVV9DTnhtTmM3bUsta3ZUYnROT3RzRjE3bTNQRGVfX1ZiR3lOME9fX2FjRlBzU3EyclB6QUlIT1FQT0tWVEFFWkNlbE1YX01DZw?oc=5>

### JPMorgan’s 2027 earnings calls run into January 2028.
- Summary: JPMorgan will hold its 2027 earnings calls in January 2028, extending the reporting period.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxNWEhzRVVleTBsNWhMc1d3YzZ2U3k3QzNjTEpvcUdFWkkwcDY3N3UxdTJTeXZzcUhhQURCYlhkVlZpZlNBX0Y1M0VMdGJmQlVER0hCR2Y5Q3I3MS1mRnVXVzcwMzhwUUswZVAxU1g2TVl3Szh3eUdDcllnU3JnU1VEU2JfS201bS1Wc2VoMHBnd05fRS1mYno3cW9LWXA4TGVUUV80RGVBMA?oc=5>

### JPMorgan Chase & Co. $JPM Shares Newly Purchased by Leo Wealth LLC
- Summary: Shares of JPM acquired by Leo Wealth LLC, indicating a new ownership stake.
- Date: 2026-10-31 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxNOHNfSjRPaFNFQWdKYWpCbU44X2FtV0FWbGNfMkp3b0IwVWRGemZVWlhJUGlFZzl0XzUtd0lFRkx0RzYxN29URzAyYzFSZmFYU0JLSXFNVFVKOVpwTlpHcHk0YTBlbXFRbnkxYURGY0hYR25VMmM3ZEttdmFRV3RXZU1iaFhyN2UtekY5WTREZ1Eyb1g3Qy1HTFhQRjluZXRNRVRtRDFYUzhpNEZUb3p4QjdabDJwX25xWEdtWjZfbkI?oc=5>

### JPMorgan Chase & Co. $JPM Stock Position Trimmed by Anderson Hoagland & Co.
- Summary: Anderson Hoagland & Co. reduced its JPM stock holdings, indicating a shift in investment stance.
- Date: 2026-10-30 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiyAFBVV95cUxPaTlpeE1xeHViLVlyVGNDTC1peVlRSVE0X3BQbEdOcVl3aGtCUDd0TWJRU05KZTViWXpfM0xxMVdDWWZHakVsWHlmRzhEcTJTYzVCYVR2Ynk3cUJ3amU4Z2V1MDZxbk5nSUt2R3JpcXpYY2J5VmlPbGpjVFdkWXpaU2hTMC1lMzdIeE9CSGtTbVdDYmtaWVZqRGNUb0hrbl9zZjBmQWVSQmlLQUJaUmlJbS1HQ19kSUtvYXZ2NFA1dkxfc0FWazhYSg?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **JPM** | **14.29** | **2.57** | **N/A** | **10.20** | **904,444,248,064.00 USD** | **11.58** |
| BAC | 11.83 | 1.26 | N/A | 3.40 | 342,043,361,280.00 USD | -5.28 |
| C | 12.00 | 1.06 | N/A | 8.00 | 203,755,110,400.00 USD | 24.86 |
| WFC | 11.77 | 1.62 | N/A | 0.40 | 257,828,929,536.00 USD | 0.91 |

Peers fetched as_of: 2026-11-02; JPM reuses existing data (market data as_of: 2026-11-02); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-13
- Next expected earnings: 2027-01-14 (yfinance; expected dates may change)

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
- Filing date: 2026-08-06
- Revenue (latest available single quarter): 24,246,000,000.00 USD; period 2014-07-01/2014-09-30; fiscal year/reporting period 2014/Q3
- Net income (latest available single quarter): 21,155,000,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/19617/000162828026054343/jpm-20260630.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMixAFBVV95cUxPeVBaeVl2dlVyRlhuVTlZWVVkaHJZU284ZzFTYWh5TUo3cU14MHVNYm5YUHFNZFNFd1Btejl6Tl93VEhvYlk1QWktMmdLRzdnNTBkdTF3RzdiQVRxWUxwaHpfcUthT3FhVi1zMjB1TV81OWRXbUVKSnFJUWZ5bjdUTUc5RnhzR2x1Nlc5WkROaVhFc3hLVE12MmpKRkh1Vi0wRjFkb19TQ09WTzNTV3JlQ2FMTkpSZmdEU2doZUNtNTkxZVRa?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxQUkJ4WmtfOUVNSmVqNE5wWTRoelpORGlRQUhCTUpsVUhmYlN2OUdfVmZDeUo4ZExqNFFBMEptQVNtR1pLVENjeDBHbzItRjh5b0ZMb3dJc0J6RU5YeFFhNTBDYk9VRXpmMXdMTHlwTFRTLWZ2dXdVMWRjNGF5NmVDeklrVVBrVl9GaFJ2MWxwU1lfeUpMYWdGd3RBOXoxa1hhQ3JwR1N2MC1zUFJwRWcyU3hqeVlnVHdWejlOV3Bn?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxQREhXVnQxOXFEUF8zaF9idGJfRU1UdTItOWRXU1k5RmZDZUlTTjhaTlRxSFFDR3FOdVdlNS1Ya3h4WEZ3RVoyMnRFUUFkdWFmSkJuYmVfam9NbVFVSDVvdy0xaGI2a1VUYlo1N0RJMURyWFByYkEzZGtaQzA2UFRfcWQ0RDBBSktvdWVlcHdUanlUT2ZGdWZVTmZKVENuN29tVEdfOW5VaUpGOUVBcktWajRaVTlxQVlt?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxONjItaEJtcUNLWXd2Rk5DZzRXcDFLQXY4WWo3dEZrLWlHaTl6WmZiU2NwQ2s1bjFza0xuLTJycHFYbkpzMzE5LUhGNExJelRlUjNBWE9tRG9zVzdPQW90X2xqRWJXY1dSQ21BdlRib0FyOWM2Mm1FdE9BNDIzY09xU01TMkhuRXpKWW0zZUFBdXFmLWdTOGk2UE1YM24tX0NFMThCUjBJRlFncUtWcmV3RQ?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQN3lvaEZRZy1SYlZ2cVlxSlRjTHJERVNPbE00T0JUS3JhdHUzQmlnMGtEX1R0WTF5eS1UcTEyYlBWcmM0RlB4eWJMaWQ5aW42b0dja0dxMTFfaVB4QXA3aENadDczdTA2WDRndkRlbGNhQlhreGxhakxLcGVlUk1nMVNoTjVDNVNGS0RtLV9PcGZpTUZ0MWtPVA?oc=5
- https://news.google.com/rss/articles/CBMizwFBVV95cUxNWUxiM1htTGl3NVc0NU1fa3pHc2NoU0YxMjdpYlFLN04tNVVhdV9XNFFNZ3JFVmlZam9fV0MyUHVqNXRYOUc4TWNCNXB4VGdLNXc3ODZmNDQ5dnZ0LVpqWnQ5NldnWFh5UzJOcjFLaU9mRmIwTm44TmN6S1BNc3BGdnhqNWk0V1Bpc1FHRVpvWGI1WUhTaXRNekgxdmRNLVh5R2NFVWJ2dmNvdDlfbjZYemlDQUF3cFZfXzA0dWk5S1dET05hUGtWSzJzZzd2M2c?oc=5
- https://news.google.com/rss/articles/CBMiygFBVV95cUxNWkQ5UnRYd2ROdFNTR0lMOWxFWTQyZnBwS0hnU0twWEFJWURXMldZN00tNHRnTnVITkNOaGZsTjF3VnUtb1VUX0tONUIxNlpHVmM4OFJoTXl0cnZDLUw4UVJ5M1BCb0tyWUw1RnBUSnF2TUFPSzJMcEVDS05PM0hiY0VKTUJmdWVsN1lmYldmcTRJTjZuVWxtLTlNc2hSUDFFcFphbDAwSFp1RGNQR3ctMjItWk1hbXN5M0V6Y0Fha3dDeUcybUJhYjV3?oc=5
- https://news.google.com/rss/articles/CBMizAFBVV95cUxOaHA3WU1meEx6YW1OS2dXc3pOTFBYQjlWSUsyR2wwTExkRThmOVUwbTR0aDdlblNfSWJUQ3F6LTZBM2hnbE0xeFJMSXpyTllQMGIwSGlhNTZhckEwa2FfeVBhaThMNDNiSVFjYjdBWmVpSEdULXQ2a19OVHU2Vm9fcHdwRU5VTHZqa2pOVVI0OGV2NUZ4WWU3U0IyTS1laVZtOERmT0FQX19vV083SVVGbmRMcEV3RmhDQ1R4eFNmd2JDeE10LXBkOW90YTQ?oc=5
- https://news.google.com/rss/articles/CBMiywFBVV95cUxPQk5MN1U0YjRuTWU2YnpJZWlmNmdydWhUc1h0c0J6WENIZFVWY19wTWxwLWtXV3plTTBrX3VxSldXNGNJYTM2MHNKa3A5ajZCUmdqTDJqQ2NDd2x6dUZrdmRsN2dSQU9ERWNxVEpVdzhvaUJxcWppN0dBaTY1dHIxSlY2ektiUmNrWFVZZkFOZzEtOG1kLTZURnozYjFhMzZDeUE4RFJ4bHQ1TE1Bc3FwS1BUSGdjQ1F2VE9TS2tOYUZJc0RwMmRKU1A5OA?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxQajJ1YVV2UzI0VldHWEJpMmtQUlNEaTN6R3RfdktGd1dxVTI0ZzlnYUZBa011VWNpNlNfSlh0OTdSMWtRNHRsXzdDVHVJaEQzOS1yTGROcENsaDh6c05ISkxCb0NvUFNYa05haFo3Qi1JaWJONTdTZ0s0OWRrT0ZTM3BHMkZWSXdNOEEwMkV4bkpJNEtVUEJpeGExMGM3Z2RnSzhpcVVWbFZPbWRBRzdFcDEtSFM3dTExZ0N6UGhuUEpzcklmSkE?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxOdEFrNlV2MlJVWEh5LWM1ZFdVcHBaSDhqdk15Y2UxUVdCSUEtaGI1QmE1TmhhVmtGelJ4a3U2cVp6bHJBS0ZwZTJZSnQwSGJxdXhRamxhVV9DTnhtTmM3bUsta3ZUYnROT3RzRjE3bTNQRGVfX1ZiR3lOME9fX2FjRlBzU3EyclB6QUlIT1FQT0tWVEFFWkNlbE1YX01DZw?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxNWEhzRVVleTBsNWhMc1d3YzZ2U3k3QzNjTEpvcUdFWkkwcDY3N3UxdTJTeXZzcUhhQURCYlhkVlZpZlNBX0Y1M0VMdGJmQlVER0hCR2Y5Q3I3MS1mRnVXVzcwMzhwUUswZVAxU1g2TVl3Szh3eUdDcllnU3JnU1VEU2JfS201bS1Wc2VoMHBnd05fRS1mYno3cW9LWXA4TGVUUV80RGVBMA?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxNOHNfSjRPaFNFQWdKYWpCbU44X2FtV0FWbGNfMkp3b0IwVWRGemZVWlhJUGlFZzl0XzUtd0lFRkx0RzYxN29URzAyYzFSZmFYU0JLSXFNVFVKOVpwTlpHcHk0YTBlbXFRbnkxYURGY0hYR25VMmM3ZEttdmFRV3RXZU1iaFhyN2UtekY5WTREZ1Eyb1g3Qy1HTFhQRjluZXRNRVRtRDFYUzhpNEZUb3p4QjdabDJwX25xWEdtWjZfbkI?oc=5
- https://news.google.com/rss/articles/CBMiyAFBVV95cUxPaTlpeE1xeHViLVlyVGNDTC1peVlRSVE0X3BQbEdOcVl3aGtCUDd0TWJRU05KZTViWXpfM0xxMVdDWWZHakVsWHlmRzhEcTJTYzVCYVR2Ynk3cUJ3amU4Z2V1MDZxbk5nSUt2R3JpcXpYY2J5VmlPbGpjVFdkWXpaU2hTMC1lMzdIeE9CSGtTbVdDYmtaWVZqRGNUb0hrbl9zZjBmQWVSQmlLQUJaUmlJbS1HQ19kSUtvYXZ2NFA1dkxfc0FWazhYSg?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
