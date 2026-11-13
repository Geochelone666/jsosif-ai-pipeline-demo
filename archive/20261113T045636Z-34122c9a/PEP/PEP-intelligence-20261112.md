# PEP Intelligence Report

- ticker: **PEP**
- Report as_of: **2026-11-12**
- Market data as_of: **2026-11-12**
- Quant sources: https://finance.yahoo.com/quote/PEP/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/PEP/key-statistics/
- AI analysis snapshot as_of: **2026-11-12**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-13T05:19:39.713006+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 11, 'rule': 3, 'ai': 4, 'unknown': 0, 'irrelevant': 4})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **5** exact headline/source/date matches; prior report **20261112T054014Z-6c47e7f9/PEP** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 11 unique headlines; 8 named publishers; 0 exact duplicates; 11 HTTPS source links; largest publisher share 27.27%; oldest publication 2026-11-09

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 142.2600 |
| Return 1D (%) | -1.1672 |
| Return 1W (%) | -0.3153 |
| Return 1M (%) | 12.2987 |
| Return YTD (%) | 2.1394 |
| Return 1Y (%) | 2.5170 |
| Annualized volatility (%) | 21.6023 |
| Beta vs SPY | -0.1935 |
| Max drawdown (%) | -25.2176 |
| Sharpe (rf=0) | 0.2228 |
| Downside deviation (rf=0, %) | 14.3430 |
| Sortino (rf=0) | 0.3355 |
| Historical VaR 95% (1D, %) | 2.1996 |
| Historical ES 95% (1D, %) | 2.6412 |
| Correlation vs SPY | -0.1230 |
| Tracking error vs SPY (%) | 26.9872 |
| P/E (trailing) | 17.89 |
| P/B | 8.70 |
| EV/EBITDA | 12.25 |
| Revenue growth (%) | 5.60 |
| Forward P/E (estimate) | 16.50 |
| Gross margin (%) | 54.33 |
| Operating margin (%) | 16.05 |
| Return on equity (%) | 52.19 |
| Free cash flow yield (%) | 4.67 |
| MA50 | 133.4998 |
| Close vs MA50 (%) | 6.5620 |
| MA200 | 143.6865 |
| Close vs MA200 (%) | -0.9928 |
| RSI (14, Wilder) | 61.6166 |
| MACD (12,26) | 3.0849 |
| MACD signal (9) | 2.4801 |
| MACD histogram | 0.6048 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'PEP': 281, 'SPY': 281}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 142.2600 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.1672 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -0.3153 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 12.2987 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 2.1394 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 2.5170 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 21.6023 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 14.3430 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.3355 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.1996 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.6412 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.1230 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 26.9872 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.1935 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -25.2176 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.2228 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 16.4991 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 54.3270 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 16.0460 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 52.1870 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 4.6653 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 17.8943 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 61.6166 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.6048 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 6.5620 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -0.9928 -> Slightly below the moving-average trend level.

## TAILWINDS

### PepsiCo (NASDAQ:PEP) Stock Price Up 1.2% - Here's What Happened
- Summary: PepsiCo (NASDAQ:PEP) Stock Price Up 1.2% - Here's What Happened
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxQQ3VwYVByV2d1Q1NMb0xtaVFxSkoyNWtRdXZxQXZrR25OUEw0UEdFZ0VnRGRMRjFnd1pXVUpBVVdwdC03M0YxanRJVGJYSjVCcDNPTm5EVXpJZDJJN3N1Ym54U2lPdnhuclRCcXlFMXhvdDZSR3FFVzdqeG1INmZuaWZGQ0RxWTJpRllSMmZsbTZxdDZMWDhGb19kM3VpTVpPYi1xbnY5d1ByVjdtTlZkSHk1QkZsd0k?oc=5>

### Do PepsiCo’s Dividends Make Up For A Lagging Stock?
- Summary: Analysis questions if dividends offset a lagging stock, suggesting potential positive impact.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxQVlhoS2hVbXB4TFlVMVRsUGtjVWdJOFpLVVNFalQyN3RYazBFUHNrT212ZHZwR09za2ZIWUcwYnZ2S3BJVGt0SHU3elZCZlN5RTdxbE0xcUxqUzRTdUlQU2tGTG5JV3ozdkRRUTExMndOX1IzMW5QdDBsRjYta2lCRl82NzVCMXd3QkxXTzlaQjZjY3duQkNHU2JHSWMzcl9WNjJQU1FUaTRoVGxfQkE?oc=5>

## HEADWINDS

### PepsiCo (NASDAQ:PEP) Stock Price Down 1.2% - Here's Why
- Summary: PepsiCo (NASDAQ:PEP) Stock Price Down 1.2% - Here's Why
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxQekl6NkVNTlBJZkNyLTNrOXEtV1dCOEo3OVhoc3JfcGYxRjNJTEYzaFlMa0RtLUZ5eXVlOGIwQkZydlpUbERha29QS09pZnpDNU1YZVBkX2c0OTZNMUs4MFgwY0U4T0xZOW1Xa1Vxclh3U1RrcExfckNZWUpJR2ZvUXViLWRjMnZQU3NTbEdFZVQwbDlBMWg2T3dRbk9Kamg3N3lERzNqcGZVOTlR?oc=5>

### PepsiCo (PEP) Cuts 1,000 Jobs as North American Sales Struggle
- Summary: Job cuts amid sales decline signal operational challenges.
- Date: 2026-11-10 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxOYnZMM0Z1REtrT1JJaFhBdWR6OW1pUG1SS3M5OFYzR0NUQUY2YlU2clg5WU1IamxjRXdibEVmZk1xRlIwSHVCcnJJTWxlMXZjQTQ0WUduTG9PdnNpUWNmVFg1NWg1UGtlWVdNZVV1MW1pSnN0MGFySVBtYXFEY3FjYTQ0d2QteVlpcGFTTVhPVUJRTU0?oc=5>

## CATALYSTS

### PepsiCo Has Raised Its Dividend 54 Straight Years, but $1,000 in Coca-Cola Finished $1,296 Ahead Over the Past Decade
- Summary: PepsiCo Has Raised Its Dividend 54 Straight Years, but $1,000 in Coca-Cola Finished $1,296 Ahead Over the Past Decade
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi7AFBVV95cUxPREZNWVpQWFR3bmZjcUZJQTAwQUdTa1hCQnVpaEJuN19xMjNfMmVhSW1xNjI0U2JXRnA5LXlySjB0bDNvak5ZX0ZzU2t4U0J0bkNJUHZBZEJNdmVqSVFLVUZqZTRTZnM2WVdaN1JuS1psaWJ1WHZic05Vc1Njc05CT2RoTXF4SjZ1Sk5OVXdZZXVhRWxiU0ljb1c4Um1GdEVKR3dhLUpxd3hvQWQ0TlVpcmh2VkRLNEE3MGRrSFZtY0Q3VjVZRzdud3JqTDZDbnQ3eW5kYXFZbklnVjEtLW5tdEhxVGV3SlVqUmhveg?oc=5>

### PepsiCo reshapes North American business with 1,000 job reductions (PEP:NASDAQ)
- Summary: PepsiCo cuts 1,000 jobs in North America, signaling a workforce reduction strategy.
- Date: 2026-11-09 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxNbFFHVHlsLWJnOWIta3lIQnBNdE9DVkhZbVJkM0NJbHFIUlpTeVJoSzhNODZadFI4WGNabEdxd29LeUh4ZEdFTmZRdU91Nm5hbGl2SlJHMWdVU2lSc3d5Mno3dlZILTRxSTVDMlNOVHBxTjJpU0ppUk9GNndIaTZIT0FmQ0dWRnFDU3l4VDhmUFlJZ2p3NjZLM053SGhFN29EVHhBTFRn?oc=5>

## RISKS

### PepsiCo Stock Outlook: Is Wall Street Bullish or Bearish?
- Summary: Analysts debate PepsiCo's future market sentiment.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxQdEdUQURjRnlZNzNUZGhaVEMwVC01RFFab0xTb1ZaZ2l0d0tzUDJ1NDNiMWxPQ3BJSDV4cllLM0U2MFo5R3pWREc0TUxveHU0QmJSQ2g2THRPZ0xKNkhxelVVQUxKbmRQdGZuVG5vNFBDR2UwWmFZd0hWN1pjbXlsd1FjZDlhUUJ1QzVNcDBOUVlTc0hId0MwX0FhY21aMHM?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **PEP** | **17.89** | **8.70** | **12.25** | **5.60** | **193,863,548,928.00 USD** | **2.52** |
| KO | 28.74 | 11.22 | 25.64 | 7.40 | 419,177,365,504.00 USD | 39.88 |
| MNST | 41.43 | 9.07 | 28.73 | 16.70 | 89,203,818,496.00 USD | 29.31 |
| KDP | 31.91 | 1.90 | 16.40 | 70.60 | 48,204,787,712.00 USD | 35.87 |

Peers fetched as_of: 2026-11-12; PEP reuses existing data (market data as_of: 2026-11-12); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-08
- Next expected earnings: 2027-02-02 (yfinance; expected dates may change)

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
- Filing date: 2026-10-08
- Revenue (latest available single quarter): 25,274,000,000.00 USD; period 2026-06-14/2026-09-05; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 3,048,000,000.00 USD; period 2026-06-14/2026-09-05; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/77476/000007747626000048/pep-20260905.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMitwFBVV95cUxQQ3VwYVByV2d1Q1NMb0xtaVFxSkoyNWtRdXZxQXZrR25OUEw0UEdFZ0VnRGRMRjFnd1pXVUpBVVdwdC03M0YxanRJVGJYSjVCcDNPTm5EVXpJZDJJN3N1Ym54U2lPdnhuclRCcXlFMXhvdDZSR3FFVzdqeG1INmZuaWZGQ0RxWTJpRllSMmZsbTZxdDZMWDhGb19kM3VpTVpPYi1xbnY5d1ByVjdtTlZkSHk1QkZsd0k?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxQVlhoS2hVbXB4TFlVMVRsUGtjVWdJOFpLVVNFalQyN3RYazBFUHNrT212ZHZwR09za2ZIWUcwYnZ2S3BJVGt0SHU3elZCZlN5RTdxbE0xcUxqUzRTdUlQU2tGTG5JV3ozdkRRUTExMndOX1IzMW5QdDBsRjYta2lCRl82NzVCMXd3QkxXTzlaQjZjY3duQkNHU2JHSWMzcl9WNjJQU1FUaTRoVGxfQkE?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxQekl6NkVNTlBJZkNyLTNrOXEtV1dCOEo3OVhoc3JfcGYxRjNJTEYzaFlMa0RtLUZ5eXVlOGIwQkZydlpUbERha29QS09pZnpDNU1YZVBkX2c0OTZNMUs4MFgwY0U4T0xZOW1Xa1Vxclh3U1RrcExfckNZWUpJR2ZvUXViLWRjMnZQU3NTbEdFZVQwbDlBMWg2T3dRbk9Kamg3N3lERzNqcGZVOTlR?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxOYnZMM0Z1REtrT1JJaFhBdWR6OW1pUG1SS3M5OFYzR0NUQUY2YlU2clg5WU1IamxjRXdibEVmZk1xRlIwSHVCcnJJTWxlMXZjQTQ0WUduTG9PdnNpUWNmVFg1NWg1UGtlWVdNZVV1MW1pSnN0MGFySVBtYXFEY3FjYTQ0d2QteVlpcGFTTVhPVUJRTU0?oc=5
- https://news.google.com/rss/articles/CBMi7AFBVV95cUxPREZNWVpQWFR3bmZjcUZJQTAwQUdTa1hCQnVpaEJuN19xMjNfMmVhSW1xNjI0U2JXRnA5LXlySjB0bDNvak5ZX0ZzU2t4U0J0bkNJUHZBZEJNdmVqSVFLVUZqZTRTZnM2WVdaN1JuS1psaWJ1WHZic05Vc1Njc05CT2RoTXF4SjZ1Sk5OVXdZZXVhRWxiU0ljb1c4Um1GdEVKR3dhLUpxd3hvQWQ0TlVpcmh2VkRLNEE3MGRrSFZtY0Q3VjVZRzdud3JqTDZDbnQ3eW5kYXFZbklnVjEtLW5tdEhxVGV3SlVqUmhveg?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxNbFFHVHlsLWJnOWIta3lIQnBNdE9DVkhZbVJkM0NJbHFIUlpTeVJoSzhNODZadFI4WGNabEdxd29LeUh4ZEdFTmZRdU91Nm5hbGl2SlJHMWdVU2lSc3d5Mno3dlZILTRxSTVDMlNOVHBxTjJpU0ppUk9GNndIaTZIT0FmQ0dWRnFDU3l4VDhmUFlJZ2p3NjZLM053SGhFN29EVHhBTFRn?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxQdEdUQURjRnlZNzNUZGhaVEMwVC01RFFab0xTb1ZaZ2l0d0tzUDJ1NDNiMWxPQ3BJSDV4cllLM0U2MFo5R3pWREc0TUxveHU0QmJSQ2g2THRPZ0xKNkhxelVVQUxKbmRQdGZuVG5vNFBDR2UwWmFZd0hWN1pjbXlsd1FjZDlhUUJ1QzVNcDBOUVlTc0hId0MwX0FhY21aMHM?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
