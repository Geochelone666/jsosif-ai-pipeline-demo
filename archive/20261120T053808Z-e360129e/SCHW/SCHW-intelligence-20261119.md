# SCHW Intelligence Report

- ticker: **SCHW**
- Report as_of: **2026-11-19**
- Market data as_of: **2026-11-19**
- Quant sources: https://finance.yahoo.com/quote/SCHW/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/SCHW/key-statistics/
- AI analysis snapshot as_of: **2026-11-19**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-20T05:51:40.735469+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 8, 'rule': 2, 'ai': 5, 'unknown': 0, 'irrelevant': 1})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **0** exact headline/source/date matches; prior report **N/A** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 8 unique headlines; 7 named publishers; 0 exact duplicates; 8 HTTPS source links; largest publisher share 25.0%; oldest publication 2026-11-18

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 92.1200 |
| Return 1D (%) | -0.4754 |
| Return 1W (%) | 0.7877 |
| Return 1M (%) | 3.1955 |
| Return YTD (%) | -6.5569 |
| Return 1Y (%) | 0.7761 |
| Annualized volatility (%) | 25.7283 |
| Beta vs SPY | 0.4135 |
| Max drawdown (%) | -22.5253 |
| Sharpe (rf=0) | 0.1596 |
| Downside deviation (rf=0, %) | 19.4530 |
| Sortino (rf=0) | 0.2111 |
| Historical VaR 95% (1D, %) | 2.5277 |
| Historical ES 95% (1D, %) | 3.9438 |
| Correlation vs SPY | 0.2234 |
| Tracking error vs SPY (%) | 26.3695 |
| P/E (trailing) | 15.83 |
| P/B | 3.51 |
| EV/EBITDA | N/A |
| Revenue growth (%) | 16.90 |
| Forward P/E (estimate) | 11.81 |
| Gross margin (%) | 97.51 |
| Operating margin (%) | 51.11 |
| Return on equity (%) | 21.11 |
| Free cash flow yield (%) | N/A |
| MA50 | 95.3037 |
| Close vs MA50 (%) | -3.3406 |
| MA200 | 96.1450 |
| Close vs MA200 (%) | -4.1864 |
| RSI (14, Wilder) | 47.7416 |
| MACD (12,26) | -0.5899 |
| MACD signal (9) | -1.1115 |
| MACD histogram | 0.5216 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'SCHW': 286, 'SPY': 286}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 92.1200 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.4754 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 0.7877 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 3.1955 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -6.5569 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 0.7761 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 25.7283 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 19.4530 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.2111 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.5277 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.9438 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2234 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 26.3695 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.4135 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -22.5253 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.1596 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 11.8061 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 97.5060 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 51.1070 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 21.1130 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 15.8282 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 47.7416 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.5216 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -3.3406 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -4.1864 -> Slightly below the moving-average trend level.

## TAILWINDS

### Charles Schwab raised to Strong Buy at Raymond James on macro outlook, strong execution
- Summary: Charles Schwab raised to Strong Buy at Raymond James on macro outlook, strong execution
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxQR0puZTV4YXhUZC1qd3JUN193S1BDYXlza09rUXQ0eW5aSFJiTlNFSlQySmdGaDhtVEFPUW9PN1FtTi1TODRweVFDdzlUclRIemlmM1J1bldwc0RxVWNrNjhTMFV2U1FpVzhlZmxna003WUNjbTNOdmt5RDJEQ0IxQlFreDB2Nk9heWxDR1NPSW5Lc0l1YXFsTDhvTHE4RFQ2cG1rNDRIYU1QcGZpZFhydjRzWFZtU1dNSFIxLTY5MzFMdw?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Charles Schwab (SCHW) Now Has The Largest U.S. Dividend ETF
- Summary: Charles Schwab (SCHW) Now Has The Largest U.S. Dividend ETF
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxOUUlPTDRtRVdHM3EtT3ZLLW5IYjh6T1lJVEJvVGVqMjlXTVJBU0hBXy02WTZuMWJpd0ZfSnA2MXE4dmt6MFR5VU5PSTd1akxUanpqMm1Fczk4MEtia294aW92RjNGX0tvTmxMdm9WZVJPZlhTUVp5SHZWUURWQ215VGRTdTVHb0E1Sm9mRzVQMGtRcEJxbG9EazQwbDI?oc=5>

### Charles Schwab (SCHW) Stock Could Be 31% Undervalued Today
- Summary: Schwab shares may be undervalued by 31%, suggesting potential upside for investors.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihwFBVV95cUxPMl9ndmI0bnIxMkY1V3BQVTkzdGlEaXMwWmdYZG4xZkNBX2p3eXBDOXJQS0ZGckhxOGFPRFB1SjctWTM4N0JiVEhyUldsMmhvelFxMktnNXNSbGZWUzhsMXZfVFIzVzQzVHIwNTJoQ21yMUZ2Rjg1Z2ZzV1RHd2lJZHhjQWFFcHM?oc=5>

### Charles Schwab (SCHW) Stock May Be 31% Undervalued Despite Its AI Push
- Summary: Despite AI initiatives, Schwab shares could still be 31% undervalued, indicating growth prospects.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi3AFBVV95cUxPSHZvbHFlWHlyVmUxeW5GaGFQQ19JVVhMUE1aNEtTbmNaUGMxUXo5TTRpZTJjalFMZFU4Yllxczc3eGpCd2I4YWotaE05c2l4U1Ewd1ZtRzdiZC0yNlN4RjFlV0Nvc1dfTzE4bVJ0RjAzQ1A4T1QzS2Z6cnU3dl9ZVjJpVG1FaDV1T3BfZmNKTkw2dENTdjlEdGpBSVNVUDhVRkxWTENWd2EtX3lBaHZDTjVrRldVMFg1OFJyemlncGxFc2paRE8yeW9xTE9OTjVCSWQ1U0lqS3k4bGE00gHiAUFVX3lxTFBWNkdaTzBjTXdFeFZ0aUZsZllCWEhiOE1HSzJlUG9GS0tXaHNZaFpUVXFQbzFZblQwb0dCQWxfQWdQby0tV0duSTJrbDhTWmkwMGlXVFhwMkNXdmdCck4xRjMtR0FSa3kwQjVsUnl3b1hySEhabXU3M3JVOXEtMlZ3dE5GTHJkYWxMbXRINXZuRHlIYjI2LWp4a2VGM3ZZMVJVbDFxVTEtczVBLWJubnZqQjJqUWRkYUdZZVZqckducmdBbnpJcGNuZEg2aDlJbDNLeGJ3a0g4ek1XbzhCVlV1ZlE?oc=5>

### Charles Schwab (SCHW) Expands AI Tools, Is It Still 22% Below Fair Value?
- Summary: Schwab is adding AI tools; shares may remain 22% below fair value, hinting at future gains.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxOakEweUZiNDNFR0tVNHRzYmZxcElkN0l2d3JvQXk5ZUJ6UE03Q21NSzQ3djBPRFFveUp5alBHU0ZibjJNY1dJWXpGYXZZajM2eW1KUWFwaVdIUlFEUGNOdWkxd2FEM3ZzaWU3YkVzMkctQzV6dVRkcDAtWWU4cjdxM282N0QtdExlaVBnanJPanFwZUNFRjJ4M1Flbw?oc=5>

### $1000 Invested In Charles Schwab 15 Years Ago Would Be Worth This Much Today
- Summary: A $1,000 Schwab investment 15 years ago would have grown significantly, highlighting long-term performance.
- Date: 2026-11-19 | Impact: medium | Horizon: long | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxQZjVlRm5PSUtDdnp2M3ZmbWhsYUF2d1RybjFtNTJISzVzTWhyVjZLMGIwMC1QVzBWVEtjNnZMUE5BYU9QQldiMVlZYWhRVDRYS2JQWVZRUkM2dm1sQUdZWnZxMmRnYk5HZ1Nma0MwT2JqTkl2QTAtN1VSdjhIOFVFbHJ6ejNmNElFbC1ReTctQ2pJSEo4ak5DN2FtNzBKX1hOSV9hWXFsOVNzRmVUMF9ndFh3?oc=5>

### Charles Schwab (NYSE:SCHW) Stock Rating Raised to "Strong-Buy" at Raymond James Financial
- Summary: Raymond James upgrades Schwab to Strong-Buy, signaling positive outlook for the brokerage firm.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi4AFBVV95cUxONmE3SGJrSFNFbWlRRzJ4ODlWYms5MXIyV0FXTWF2bHF4Z29PdU5HUFlQSlBQSHpnd1Q5eVp0aFlZcXVXLXFBOEJUU3BXSnBaVjAxdTVzZlB1cnUxVkMzZzVWaXFvQUY3V21Bb3BRbE44SmJsSktVV0R2Nl9mQlltbktVUlhRVURoNWY5WVB1NUFYM0ZkeEpQMTlVNHJXdl9YTDhYNFVXeTBzTllKcXE1SmxPWllhUGRWMlVxSlNmNW9tdl9kdC1tcVpUczVONnRzSGl4T192NGFWSXI2Z1Y0Vw?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **SCHW** | **15.83** | **3.51** | **N/A** | **16.90** | **158,999,838,720.00 USD** | **0.78** |
| IBKR | 29.21 | 5.52 | N/A | 13.50 | 128,895,582,208.00 USD | 17.67 |
| HOOD | 31.64 | 6.18 | N/A | 11.80 | 61,818,728,448.00 USD | -39.48 |
| LPLA | 15.79 | 3.64 | N/A | 17.80 | 21,050,167,296.00 USD | -23.85 |

Peers fetched as_of: 2026-11-19; SCHW reuses existing data (market data as_of: 2026-11-19); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-15
- Next expected earnings: 2027-01-21 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-19

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-06
- Revenue (latest available single quarter): 7,171,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 2,906,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/316709/000031670926000038/schw-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiwgFBVV95cUxQR0puZTV4YXhUZC1qd3JUN193S1BDYXlza09rUXQ0eW5aSFJiTlNFSlQySmdGaDhtVEFPUW9PN1FtTi1TODRweVFDdzlUclRIemlmM1J1bldwc0RxVWNrNjhTMFV2U1FpVzhlZmxna003WUNjbTNOdmt5RDJEQ0IxQlFreDB2Nk9heWxDR1NPSW5Lc0l1YXFsTDhvTHE4RFQ2cG1rNDRIYU1QcGZpZFhydjRzWFZtU1dNSFIxLTY5MzFMdw?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxOUUlPTDRtRVdHM3EtT3ZLLW5IYjh6T1lJVEJvVGVqMjlXTVJBU0hBXy02WTZuMWJpd0ZfSnA2MXE4dmt6MFR5VU5PSTd1akxUanpqMm1Fczk4MEtia294aW92RjNGX0tvTmxMdm9WZVJPZlhTUVp5SHZWUURWQ215VGRTdTVHb0E1Sm9mRzVQMGtRcEJxbG9EazQwbDI?oc=5
- https://news.google.com/rss/articles/CBMihwFBVV95cUxPMl9ndmI0bnIxMkY1V3BQVTkzdGlEaXMwWmdYZG4xZkNBX2p3eXBDOXJQS0ZGckhxOGFPRFB1SjctWTM4N0JiVEhyUldsMmhvelFxMktnNXNSbGZWUzhsMXZfVFIzVzQzVHIwNTJoQ21yMUZ2Rjg1Z2ZzV1RHd2lJZHhjQWFFcHM?oc=5
- https://news.google.com/rss/articles/CBMi3AFBVV95cUxPSHZvbHFlWHlyVmUxeW5GaGFQQ19JVVhMUE1aNEtTbmNaUGMxUXo5TTRpZTJjalFMZFU4Yllxczc3eGpCd2I4YWotaE05c2l4U1Ewd1ZtRzdiZC0yNlN4RjFlV0Nvc1dfTzE4bVJ0RjAzQ1A4T1QzS2Z6cnU3dl9ZVjJpVG1FaDV1T3BfZmNKTkw2dENTdjlEdGpBSVNVUDhVRkxWTENWd2EtX3lBaHZDTjVrRldVMFg1OFJyemlncGxFc2paRE8yeW9xTE9OTjVCSWQ1U0lqS3k4bGE00gHiAUFVX3lxTFBWNkdaTzBjTXdFeFZ0aUZsZllCWEhiOE1HSzJlUG9GS0tXaHNZaFpUVXFQbzFZblQwb0dCQWxfQWdQby0tV0duSTJrbDhTWmkwMGlXVFhwMkNXdmdCck4xRjMtR0FSa3kwQjVsUnl3b1hySEhabXU3M3JVOXEtMlZ3dE5GTHJkYWxMbXRINXZuRHlIYjI2LWp4a2VGM3ZZMVJVbDFxVTEtczVBLWJubnZqQjJqUWRkYUdZZVZqckducmdBbnpJcGNuZEg2aDlJbDNLeGJ3a0g4ek1XbzhCVlV1ZlE?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxOakEweUZiNDNFR0tVNHRzYmZxcElkN0l2d3JvQXk5ZUJ6UE03Q21NSzQ3djBPRFFveUp5alBHU0ZibjJNY1dJWXpGYXZZajM2eW1KUWFwaVdIUlFEUGNOdWkxd2FEM3ZzaWU3YkVzMkctQzV6dVRkcDAtWWU4cjdxM282N0QtdExlaVBnanJPanFwZUNFRjJ4M1Flbw?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxQZjVlRm5PSUtDdnp2M3ZmbWhsYUF2d1RybjFtNTJISzVzTWhyVjZLMGIwMC1QVzBWVEtjNnZMUE5BYU9QQldiMVlZYWhRVDRYS2JQWVZRUkM2dm1sQUdZWnZxMmRnYk5HZ1Nma0MwT2JqTkl2QTAtN1VSdjhIOFVFbHJ6ejNmNElFbC1ReTctQ2pJSEo4ak5DN2FtNzBKX1hOSV9hWXFsOVNzRmVUMF9ndFh3?oc=5
- https://news.google.com/rss/articles/CBMi4AFBVV95cUxONmE3SGJrSFNFbWlRRzJ4ODlWYms5MXIyV0FXTWF2bHF4Z29PdU5HUFlQSlBQSHpnd1Q5eVp0aFlZcXVXLXFBOEJUU3BXSnBaVjAxdTVzZlB1cnUxVkMzZzVWaXFvQUY3V21Bb3BRbE44SmJsSktVV0R2Nl9mQlltbktVUlhRVURoNWY5WVB1NUFYM0ZkeEpQMTlVNHJXdl9YTDhYNFVXeTBzTllKcXE1SmxPWllhUGRWMlVxSlNmNW9tdl9kdC1tcVpUczVONnRzSGl4T192NGFWSXI2Z1Y0Vw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
