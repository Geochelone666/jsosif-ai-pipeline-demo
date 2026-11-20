# BMO.TO Intelligence Report

- ticker: **BMO.TO**
- Report as_of: **2026-11-19**
- Market data as_of: **2026-11-19**
- Quant sources: https://finance.yahoo.com/quote/BMO.TO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/BMO.TO/key-statistics/
- AI analysis snapshot as_of: **2026-11-19**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-20T06:03:20.598201+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 11, 'rule': 3, 'ai': 7, 'unknown': 0, 'irrelevant': 1})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **3** exact headline/source/date matches; prior report **20261119T054856Z-9eb86811/BMO.TO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 11 unique headlines; 8 named publishers; 1 exact duplicates; 11 HTTPS source links; largest publisher share 27.27%; oldest publication 2026-11-13

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 231.0600 |
| Return 1D (%) | -0.5466 |
| Return 1W (%) | -6.3435 |
| Return 1M (%) | -0.7865 |
| Return YTD (%) | 33.6814 |
| Return 1Y (%) | 39.1783 |
| Annualized volatility (%) | 19.8416 |
| Beta vs SPY | 0.8456 |
| Max drawdown (%) | -11.4239 |
| Sharpe (rf=0) | 1.7729 |
| Downside deviation (rf=0, %) | 13.6700 |
| Sortino (rf=0) | 2.5733 |
| Historical VaR 95% (1D, %) | 2.0468 |
| Historical ES 95% (1D, %) | 2.6770 |
| Correlation vs SPY | 0.5903 |
| Tracking error vs SPY (%) | 16.2949 |
| P/E (trailing) | 18.72 |
| P/B | 1.90 |
| EV/EBITDA | N/A |
| Revenue growth (%) | 12.00 |
| Forward P/E (estimate) | 13.98 |
| Gross margin (%) | 0.00 |
| Operating margin (%) | 37.94 |
| Return on equity (%) | 10.57 |
| Free cash flow yield (%) | N/A |
| MA50 | 238.8010 |
| Close vs MA50 (%) | -3.2416 |
| MA200 | 223.1714 |
| Close vs MA200 (%) | 3.5348 |
| RSI (14, Wilder) | 37.7444 |
| MACD (12,26) | -0.1924 |
| MACD signal (9) | 1.2763 |
| MACD histogram | -1.4688 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'BMO.TO': 285, 'SPY': 286}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 231.0600 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.5466 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -6.3435 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -0.7865 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 33.6814 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 39.1783 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 19.8416 -> Low annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 13.6700 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 2.5733 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.0468 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.6770 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5903 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 16.2949 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.8456 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -11.4239 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.7729 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 13.9772 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 0.0000 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 37.9380 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 10.5740 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 18.7245 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 37.7444 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -1.4688 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -3.2416 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 3.5348 -> Slightly above the moving-average trend level.

## TAILWINDS

No items in this run

## HEADWINDS

### Bank of Montreal falls 2.37% in Wednesday's session
- Summary: Bank of Montreal falls 2.37% in Wednesday's session
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiAFBVV95cUxPRm5nbGtwSUU1amIzenFGMm91MHcwTTJCbHRDRDgwZEszZ01OX0lsT255OVMwUHpvYW12VW1LYmRRZVpwZm95QzJkYUdmLTlKODN6cUFQQmEwamt6T2FRTGFoZGJHczlYZnc3dVNqZnNzWVlDdnA4aHktdU1lYkpuVEl5elVFY0xY?oc=5>

### Bank of Montreal (TSE:BMO) Stock Crosses Below 50-Day Moving Average After Analyst Downgrade
- Summary: Bank of Montreal (TSE:BMO) Stock Crosses Below 50-Day Moving Average After Analyst Downgrade
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi5AFBVV95cUxQaHBNcERtdnQwcjYyN3laVmN0V283bktUNWtDdmFLRXRNbWRqSGYwc09Ob0tvY2JCeFNkNWZaVUdVdW52Y0ZPVEQwdUgyMXgxbzNhWVpxREFHdmNMZFFrN0xuYjhfMU5Bd1V6TDc0U0w2b09JM0RiS0NIV1lBY3BIZ05DS2pzVlVJOTAzV3FFd3d2dC1YYkszRUhjNVF4SFY4Y0FTMGdHZmlId1ljVUc1aEkwWERIMTZDR1Z3S3hYQ0h2eTN6MXBBMXdmc3gwV1lNQXkzWjJwLVFmdVRhbVBtb1JNa2Q?oc=5>

## CATALYSTS

### Bank of Montreal (TSX:BMO): S&P/TSX Large-Cap Value Stock and the Outlook for Its Dividend
- Summary: Bank of Montreal (TSX:BMO): S&P/TSX Large-Cap Value Stock and the Outlook for Its Dividend
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxNajRldVoxRV8wYjQyeHp5V09OdVhIN2tqdlR0RDFZVmoyWXQ3M3o5QWhUVTUtREY3QWlkRFJEMmxnLVFMeE4wUTNGaHRkZXdkWm9nX0NnY3JpQkVpMmliWW1QenhxQ09IeUpHQ0lsRDRiNFhFLUg5QlR2SXdCTl9WV2dFbVJEM09MVGNjcDNJWTNUU2VCWGE0bDhRaFZSc1JNZnd5N1BpNWd2bXBCMVhFXzc5eFd4S29DUm9tYmtvTzROdw?oc=5>

### Bank of Montreal (TSX:BMO) Pushes Digital Banking While Valuation Stays In Focus
- Summary: BMO emphasizes digital banking expansion while maintaining valuation focus.
- Date: 2026-11-13 | Impact: medium | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxOa2dUZmEwdWxkaGVCUnB0SVNTTWU3ekl0M2lEcDk4TDhTNFpva1h5RHpqWkw0V1dZOElLa1E3RENvQ3FxNGx4cnVfSVNjNHpzbkxVU1JrRXh6UmxOR2w3eUV1QkhuQU15ZEhtM21PQkN4Ukd6aGhYZGU4aXNic0pHTGlMQ0lETVZpSWVISWN3YmR6VkJ0RkZmaw?oc=5>

### Bank of Montreal (BMO.TO) - What Are Brokerages Thinking About This Stock?
- Summary: Brokerages are evaluating BMO’s prospects, potentially influencing investor sentiment and valuation.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizAFBVV95cUxNQ2Z3Ym1zQlk0YUJsd01EWm53aFhPcDJJZXI3V3cyeUhhbDhqWnk4bEMybHh4NWRxT2FDdlh2SjVDSGlPUXRZNXFwbWFfaXZkSnczaEd6d3RRS0ctb1NFdkpIUzF1T1IwUWUyeGVXdVIyMTRWeVhpNTBfYzNhenNKc3NWYm1fV2dhWXhtZzRNSlU3X1EzVVlJMjM3aUc1OUZTTlN6V2Q2V1d4QjlkV0FCVzk4U2xKRGJKR1pudHFJYTFteFYxVEg5MHkzRUk?oc=5>

### Bank Of Montreal (BMO) Stock Forecasts
- Summary: Analysts provide future performance predictions for BMO.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxPeTlOMVRiYnBiRGduWThhLXhuQ2c2ajZYXzdHa2hSOFBKanBiWURBbER3V2hmek9zUGR6VTZfLTFNclMzOGdGSVdtaWpER0R6SzkyRTZYeEpvVFBhTE4xVkN3X3hHS2ZEUGlmSGtxX2RUMVZKc1htejh3dm9rSnFDUGtQT1V5QWM0QTZxMW1IOA?oc=5>

### BMO: SEC Form FWP filed by Bank Of Montreal
- Summary: BMO files a Form FWP with the SEC.
- Date: 2026-11-17 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiAFBVV95cUxQUkV5SzBnc2J4LUtpYnNSRGtycC1RLXAwa3EtZU5wWkpMYm9MMEt4T1g4Vk1US2M3MTg0UU1xUVdzdVhLRGZxUThPYzF0WjFTenk1N0xKbFRFaXFQODNqVElKNXlfb2JscDM3N29rRFI4LVhDTFJBNFZLRjg3N2w1TDctQ2N0dEF4?oc=5>

### BMO returns to U.S. oil, gas investment banking, source says
- Summary: BMO resumes U.S. oil and gas investment banking services.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxOTFN5Z0hQT3lMQVhRQUY5T05WeTJfc25DeUJuLVhxU2otU21zMHNnZHFJa3k5bklmdXhGQnM5al8xSmUzOEFXbkJRMWc3eThjT25xNFZnVmVsZVQzVE44aVRHcXdCNzZBWWUzQWFWQnBoZFpqN3R4VmxoeUZLNWZjX1g5Z2RNYW9yQkF0bjFKbk1zRENITUlWc3J1ZmVpWUgwSGcwXy0tY3l0QQ?oc=5>

### ETF expansion leaves Bank of Montreal stock consolidating near C$249.37 resistance
- Summary: BMO stock consolidates after ETF expansion.
- Date: 2026-11-16 | Impact: low | Horizon: short | Confidence: 0.65
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxPTVFuUFFrVkdza2x0a2VSTmVmVmhCcXJ1NV9aV1dKMjVpUzhsODd4S01BU0hvUFhicTByamNhNUtWRE5yaWVRdnF6ZS1EUzJKVnRVMmdGWnVzVHhfbnE2Y3pLSUpTWVByRjI2S3pscGNBel9EMENoV05WSldZaFdyZzVuS2IweDYxU0o4aEtn?oc=5>

### Bank Of Montreal (NYSE:BMO) Stock Now Rated "Hold" by Wall Street Brokerages
- Summary: Brokerages issue a hold rating on BMO stock.
- Date: 2026-11-15 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0gFBVV95cUxQQlRjVWFHLWpCT1kwemF2Z1YtcTVMQjlZMW5YUkRGalZETGRtbEhMVy05THpNUUpqYXZCLU1aVGlxdWhQRkV5LV9XTzJ1TTdPa0gyeGowNUpKZkg2T3F3RmJFOTViODZka2pyZEV5Ri1XMmVGQmVEUVdWU2NDYzlKWnd5Nm9fQXlzcEVvZ3ctdmRQMUtPNTFlZ2JxTGFkRlZjdUhaYlhVX1dJVk9pNU9aX1dQNGZ3dnlZb3diREpVTy03YnlqUUNMdUVaUEp2NkFnRnc?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **BMO.TO** | **18.72** | **1.90** | **N/A** | **12.00** | **160,608,010,240.00 CAD** | **39.18** |
| RY.TO | 16.99 | 2.79 | N/A | 8.90 | 373,034,647,552.00 CAD | 32.65 |
| TD.TO | 17.64 | 2.19 | N/A | 11.50 | 269,888,684,032.00 CAD | 48.47 |
| BNS.TO | 15.91 | 1.69 | N/A | 11.70 | 150,202,597,376.00 CAD | 36.67 |

Peers fetched as_of: 2026-11-19; BMO.TO reuses existing data (market data as_of: 2026-11-19); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-25
- Next expected earnings: 2026-12-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-19

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

- https://news.google.com/rss/articles/CBMiiAFBVV95cUxPRm5nbGtwSUU1amIzenFGMm91MHcwTTJCbHRDRDgwZEszZ01OX0lsT255OVMwUHpvYW12VW1LYmRRZVpwZm95QzJkYUdmLTlKODN6cUFQQmEwamt6T2FRTGFoZGJHczlYZnc3dVNqZnNzWVlDdnA4aHktdU1lYkpuVEl5elVFY0xY?oc=5
- https://news.google.com/rss/articles/CBMi5AFBVV95cUxQaHBNcERtdnQwcjYyN3laVmN0V283bktUNWtDdmFLRXRNbWRqSGYwc09Ob0tvY2JCeFNkNWZaVUdVdW52Y0ZPVEQwdUgyMXgxbzNhWVpxREFHdmNMZFFrN0xuYjhfMU5Bd1V6TDc0U0w2b09JM0RiS0NIV1lBY3BIZ05DS2pzVlVJOTAzV3FFd3d2dC1YYkszRUhjNVF4SFY4Y0FTMGdHZmlId1ljVUc1aEkwWERIMTZDR1Z3S3hYQ0h2eTN6MXBBMXdmc3gwV1lNQXkzWjJwLVFmdVRhbVBtb1JNa2Q?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxNajRldVoxRV8wYjQyeHp5V09OdVhIN2tqdlR0RDFZVmoyWXQ3M3o5QWhUVTUtREY3QWlkRFJEMmxnLVFMeE4wUTNGaHRkZXdkWm9nX0NnY3JpQkVpMmliWW1QenhxQ09IeUpHQ0lsRDRiNFhFLUg5QlR2SXdCTl9WV2dFbVJEM09MVGNjcDNJWTNUU2VCWGE0bDhRaFZSc1JNZnd5N1BpNWd2bXBCMVhFXzc5eFd4S29DUm9tYmtvTzROdw?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxOa2dUZmEwdWxkaGVCUnB0SVNTTWU3ekl0M2lEcDk4TDhTNFpva1h5RHpqWkw0V1dZOElLa1E3RENvQ3FxNGx4cnVfSVNjNHpzbkxVU1JrRXh6UmxOR2w3eUV1QkhuQU15ZEhtM21PQkN4Ukd6aGhYZGU4aXNic0pHTGlMQ0lETVZpSWVISWN3YmR6VkJ0RkZmaw?oc=5
- https://news.google.com/rss/articles/CBMizAFBVV95cUxNQ2Z3Ym1zQlk0YUJsd01EWm53aFhPcDJJZXI3V3cyeUhhbDhqWnk4bEMybHh4NWRxT2FDdlh2SjVDSGlPUXRZNXFwbWFfaXZkSnczaEd6d3RRS0ctb1NFdkpIUzF1T1IwUWUyeGVXdVIyMTRWeVhpNTBfYzNhenNKc3NWYm1fV2dhWXhtZzRNSlU3X1EzVVlJMjM3aUc1OUZTTlN6V2Q2V1d4QjlkV0FCVzk4U2xKRGJKR1pudHFJYTFteFYxVEg5MHkzRUk?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxPeTlOMVRiYnBiRGduWThhLXhuQ2c2ajZYXzdHa2hSOFBKanBiWURBbER3V2hmek9zUGR6VTZfLTFNclMzOGdGSVdtaWpER0R6SzkyRTZYeEpvVFBhTE4xVkN3X3hHS2ZEUGlmSGtxX2RUMVZKc1htejh3dm9rSnFDUGtQT1V5QWM0QTZxMW1IOA?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxPN1hhX3VLZXFCQVQtQjVqYUpoN1ZiNV92bEd2MzlYakJCenhjNEwwdTlaV0d5ZGlNVWU5VjZJUF94bmVQazM5UkZBbVJNV1N0S3BHdnUxQ0o3XzhUZDZiYzBRaVlyOFFvWExpanVpbFgza0hMaWp5bUVrR09vMHhBZjVoT01zOEUyaVpUVllQenNkNlE?oc=5
- https://news.google.com/rss/articles/CBMiiAFBVV95cUxQUkV5SzBnc2J4LUtpYnNSRGtycC1RLXAwa3EtZU5wWkpMYm9MMEt4T1g4Vk1US2M3MTg0UU1xUVdzdVhLRGZxUThPYzF0WjFTenk1N0xKbFRFaXFQODNqVElKNXlfb2JscDM3N29rRFI4LVhDTFJBNFZLRjg3N2w1TDctQ2N0dEF4?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxOTFN5Z0hQT3lMQVhRQUY5T05WeTJfc25DeUJuLVhxU2otU21zMHNnZHFJa3k5bklmdXhGQnM5al8xSmUzOEFXbkJRMWc3eThjT25xNFZnVmVsZVQzVE44aVRHcXdCNzZBWWUzQWFWQnBoZFpqN3R4VmxoeUZLNWZjX1g5Z2RNYW9yQkF0bjFKbk1zRENITUlWc3J1ZmVpWUgwSGcwXy0tY3l0QQ?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxPTVFuUFFrVkdza2x0a2VSTmVmVmhCcXJ1NV9aV1dKMjVpUzhsODd4S01BU0hvUFhicTByamNhNUtWRE5yaWVRdnF6ZS1EUzJKVnRVMmdGWnVzVHhfbnE2Y3pLSUpTWVByRjI2S3pscGNBel9EMENoV05WSldZaFdyZzVuS2IweDYxU0o4aEtn?oc=5
- https://news.google.com/rss/articles/CBMi0gFBVV95cUxQQlRjVWFHLWpCT1kwemF2Z1YtcTVMQjlZMW5YUkRGalZETGRtbEhMVy05THpNUUpqYXZCLU1aVGlxdWhQRkV5LV9XTzJ1TTdPa0gyeGowNUpKZkg2T3F3RmJFOTViODZka2pyZEV5Ri1XMmVGQmVEUVdWU2NDYzlKWnd5Nm9fQXlzcEVvZ3ctdmRQMUtPNTFlZ2JxTGFkRlZjdUhaYlhVX1dJVk9pNU9aX1dQNGZ3dnlZb3diREpVTy03YnlqUUNMdUVaUEp2NkFnRnc?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
