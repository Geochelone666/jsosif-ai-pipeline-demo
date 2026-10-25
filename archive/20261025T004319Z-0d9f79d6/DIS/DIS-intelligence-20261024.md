# DIS Intelligence Report

- ticker: **DIS**
- Report as_of: **2026-10-24**
- Market data as_of: **2026-10-23**
- Quant sources: https://finance.yahoo.com/quote/DIS/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/DIS/key-statistics/
- AI analysis snapshot as_of: **2026-10-24**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-25T01:03:10.972384+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 10, 'rule': 0, 'ai': 10, 'unknown': 0})
- AI model(s) actually used: **openai/gpt-oss-20b**
- RSS source audit (metadata only, not article fact-checking): 10 unique headlines; 4 named publishers; 1 exact duplicates; 10 HTTPS source links; largest publisher share 50.0%; oldest publication 2026-10-17

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 112.5200 |
| Return 1D (%) | -0.5392 |
| Return 1W (%) | 1.7452 |
| Return 1M (%) | 8.7570 |
| Return YTD (%) | -0.3409 |
| Return 1Y (%) | 0.9903 |
| Annualized volatility (%) | 26.8746 |
| Beta vs SPY | 0.6198 |
| Max drawdown (%) | -20.2451 |
| Sharpe (rf=0) | 0.1713 |
| Downside deviation (rf=0, %) | 19.1831 |
| Sortino (rf=0) | 0.2399 |
| Historical VaR 95% (1D, %) | 2.4075 |
| Historical ES 95% (1D, %) | 3.7715 |
| Correlation vs SPY | 0.2940 |
| Tracking error vs SPY (%) | 26.1402 |
| P/E (trailing) | 23.20 |
| P/B | 1.77 |
| EV/EBITDA | 11.54 |
| Revenue growth (%) | 6.80 |
| Forward P/E (estimate) | 15.01 |
| Gross margin (%) | 37.59 |
| Operating margin (%) | 19.30 |
| Return on equity (%) | 8.01 |
| Free cash flow yield (%) | 2.50 |
| MA50 | 106.8952 |
| Close vs MA50 (%) | 5.2620 |
| MA200 | 103.0807 |
| Close vs MA200 (%) | 9.1572 |
| RSI (14, Wilder) | 66.4920 |
| MACD (12,26) | 1.9352 |
| MACD signal (9) | 1.3415 |
| MACD histogram | 0.5936 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'DIS': 267, 'SPY': 267}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 112.5200 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.5392 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 1.7452 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 8.7570 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -0.3409 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 0.9903 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 26.8746 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 19.1831 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.2399 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.4075 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.7715 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2940 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 26.1402 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.6198 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -20.2451 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.1713 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 15.0102 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 37.5950 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 19.3010 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 8.0100 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.5016 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 23.2000 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 66.4920 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.5936 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 5.2620 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 9.1572 -> Clearly above the moving-average trend level.

## TAILWINDS

### 1 Stat That Makes Walt Disney (DIS) Hard to Ignore This October
- Summary: Stat highlights Disney's strong performance, suggesting positive outlook.
- Date: 2026-10-17 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxObnltanFMYXZnRzZtSkx3NUpmNmRSWmhZdDlFaUFKcFFnclB3Y3RuQ3R2RkRqQkhyTG1fOVRLTTJYcVdCT2hqaDVSaW1YQWFzZjg3RTF4dzFLcUdmZ0hVSExVd09DVTdEdmJWbXBrTjNwRjhzS29LbGVQNElUcEZFOEt1RzcxLTI0YzQ1c1BZekZZNTg?oc=5>

### Walt Disney (DIS) Could Be 13% Undervalued On TV And Streaming Restructuring
- Summary: Disney may be undervalued due to restructuring, indicating upside potential.
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxOVndXOFJydEpQc01GaS1CQVl3c0Y2QmF4MHZsTzUtUmQ0WWh4WEQ1dTkwLU8xbmpScEpFY2NOSU81TlBfM3ZZb3NCS3U0NVdWcEtRTHVudjRkQTNzOHdjYUtBdGRiVEJUTVNpWE00NDd5V2UycEp6czN3UEVDTVlKOVhhTERMRUpZcy14OVpEYXdDYTQ0My0tbkV2Q1dpNF83MFViaUs5WS1WeUhCa3N6eHp4T19wTncwRURjZnlSNS3SAcYBQVVfeXFMTUdHU095Ty1vaHEyY21ManRLLVFTREx5eUtjSlNGdUQ4c3NiWnVWQ2hqTHJzZmtGeElaaWJ2M3dBTkZmSEtEMXdFZzE3Wm9jUHRiWWs2MEpmcXV5OUVnQkxySHJsVE1MUlRnQTU1RUFWc1kzaUJya0FWUzVLSjJXcFhUYV93VjRFeVRyZmpOUm8yY1lsMDRmRUhuWk5ocWkxblp0YjMwYmFKbUFraDQyeTFEeVRqd3k5LTVWTEdpNWwyRUNMQkdR?oc=5>

### Disney (DIS) Stock May Be Near Fair Value Despite AI Asset Bid
- Summary: Stock appears fairly valued amid AI asset bid, implying stability.
- Date: 2026-10-22 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxPR1h5SUU0LXFib0pMaUxjOE9VR0Z1ZDhhWUhycl9YYXFlV2s1Ml80bHhBWm9oRllXTVNGNEoxUkVabW50VjVvaEx1dTgxZUIxdEkyamllVkE5QjM2Qmh1bVJNR3NnZW12YllJNGE5VEZhUDJ3dVFudGVjd2hTSmtBaUVoWnJjNXYzcWxTamxobG5pX3Z4Tlh6VWR2eFpNZkhaWUlYLTkxZFVNYXNKWDBtWnlLV1J5SmR0U3RsOUR3Qk04Z9IBxwFBVV95cUxNeGhLcHdfSmNlRFhESm16X3pkUmVIUEhpZVVsNzRjWWR5UGNsREJnZVU4TGRtVmtyZW5vNV9za054aVAtTHkzaEVfdWp1QmVSV2pPd1R6NVNiZjdHV0RwV182U3JfSldqQ3FSQXFyQlFZVXZET0ctQ0NxRDRibnViZHlpWUNXR1ZBdm9MVU9WeUFfbTdwdktOS3I5WjJjdXFFMUN0cFh6Y2R5U3l0QzNNdExuWkxsUEw5ajJ5eDVmazVha2dOVkpB?oc=5>

## HEADWINDS

### The Walt Disney Company $DIS Stock Holdings Lessened by Prime Capital Investment Advisors LLC
- Summary: Shareholder divestment reduces ownership stake, potential negative signal.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi6AFBVV95cUxOaGh3SUVLS3MzejhVU085TEIwNFVIUU9laUZ5UWtEY01xcS13RHdyWkRVN3kyaDRRMWVLQzNNUGFoWTZ0enI2Nnp2bnBUTVItUUR0ZXJXbjdfWFo3Tm81a3FScmFHZ0U4eFlUeDZaUnFwRjhKQ0RoLUhNZWdjbTZmTzRMVjU5VzlhQmRUYV9fUGt6YTBiaUNBR1ljUzlvZng3djNzaVgxM3kxaTlrWkcwQmlKdXlxdWhkOTNwTU94VFEwZXFTSVc0Xy1zOVhRUE1jQXc4a2t0S05LdFVndXlXdlphbkxSZENt?oc=5>

## CATALYSTS

### Disney (DIS): Should It Invest More in Cruise Ships or Theme Parks?
- Summary: Strategic investment decision could drive future growth.
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxPdDZsRTMyNjdybTktZEVTZ3JIaGxjeEVhd3VSVGUyc3hZNnlOcm14NWZxcDJuWGtGTFlFeU43WWJnSnNzSDd2ZW1QMWRIR3NPa0RNVlZBTlJWVGRoRXZDM3F0OW1wWEFLbzlZX3dDR0UzNWlHZ19SYWl4ejZLMWxEczR1QXdUaHpFTmlPOENfRHlJMDVrRGJLMkNn?oc=5>

### Walt Disney (DIS) Rises As Market Takes a Dip: Key Facts
- Summary: Disney shares climb while the broader market falls, highlighting a potential short‑term upside for investors.
- Date: 2026-10-22 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQZGhWalpQSjhncTE1ZEsyRy1KTHNXQ18yX0FRNlV6ekUyM1l1TzVOYUlfVFNiaFc3a256TFFVY3lwWXo4VGl5UElMalZYb3FMNHRDWjNZQWpBV3p4aVdpUmV4V1VzZlUyM1VHNEdaTlpMY3k2N3lESEpkb1ZVRWVlWkR5QTBLQ1JIYWNTTHRJV3pxanYwTi1NcA?oc=5>

### If Park Visitors Pull Back, What Happens To Your Disney Stock?
- Summary: Examines how a decline in theme‑park attendance could affect Disney’s stock performance.
- Date: 2026-10-22 | Impact: medium | Horizon: medium | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxPZ1RNTXN0U2dhM3RNaFM3b0lZMkgyVmlLMTRUVVlBOFZxZG93RjJ1aWRtLUJtLVd3dEFXYTdBX0hsYmlRbWpFMXQtRmNIcUV2UDdFcHVCd1lIR28taEhGWjF4d0tEb2ktcWl6ZExHSWROcXpHTEpDUmJkakZCT0ZFSEZ6M3dXUm1QSGVVRVE0M1VVb19QOG1hWnQ3bUpVNzdZQ25HZUZUVDZjOFM1N3poT3N5ejd6cUNoWi00Sg?oc=5>

### Trump Likes Walt Disney (DIS). Time to Buy The Stock?
- Summary: Speculates on the impact of former President Trump’s endorsement on Disney’s share price.
- Date: 2026-10-19 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxOR0tUOVFtWkpDaFZpM0VXM1dybXlXMF94ZVh5SGYxRE82eUtRNV9qeEtRYnFlZTZXaW9aRHd5SDRSdHAwcDA1VUFxanBwNHBxeDJEUmYxMEkzdWk4aXpKQVVpSEZMLWVZN0pFZl8xTnZJUWt6OGpxc2lVX0RHZUFJQ1VKMU1XdkxjYjF5Q3pLN2NsZklOZHlJ?oc=5>

### What Could Surprise Walt Disney Stock Investors On The Upside?
- Summary: Highlights potential positive catalysts that could lift Disney’s stock beyond current levels.
- Date: 2026-10-19 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxPcWhPMHdtNDFsTEZDUjZNbXJVWVNRSG92al83UEdlSU50dWcwQXRJUHpOUjV6d0dXSTRZcFpzYzZvNjRYdGVtTWdvcDVTMG9aSWp1SzZIU3laWnlraXdZVlA4TUhWaXBXdm5NUUo4M2k2WTdLOFYxMWR6UV9UbEtaT0lCQTQ2ZzhGUlJwVGtTRklvbGsxakl4dkM3ekU5UlR4aV9ZV0YtU2lHcWhjdURqQnVONnZRQXJSbXc5Mlpn?oc=5>

### Disney (DIS) Stock Looks Reasonably Priced After A 43% Gain
- Summary: Notes that Disney’s shares appear fairly valued following a significant 43% rally.
- Date: 2026-10-22 | Impact: low | Horizon: short | Confidence: 0.5
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxQOEdDdXl2bGNjMmg5WEs1T0I2RjE1V1lrdlpTR1hfYmYxa0EwT3NxN1lOUTdmVmpwc0tRRnVZcUI4QUV5dko3RGhnTmxkc1N4d3hFMTQ1UmpkM2xCSVVJUlA1b1NXSnpQUHZpUGFJSU53blZwVjl3QlJCczk2SkpkSmFYOUFycUdUWmQzTmpvZ0ItQ0ZRZ21JVk9MNS1fRWM?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **DIS** | **23.20** | **1.77** | **11.54** | **6.80** | **194,286,796,800.00 USD** | **0.99** |
| NFLX | 19.03 | 9.23 | 17.53 | 11.80 | 274,195,415,040.00 USD | -40.87 |
| WBD | N/A | 2.36 | 13.79 | -11.20 | 77,595,885,568.00 USD | N/A |
| PSKY | N/A | 0.93 | 7.95 | 0.90 | 10,992,190,464.00 USD | N/A |

Peers fetched as_of: 2026-10-24; DIS reuses existing data (market data as_of: 2026-10-23); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-05
- Next expected earnings: 2026-11-17 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-24

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-08-05
- Revenue (latest available single quarter): 25,248,000,000.00 USD; period 2026-03-29/2026-06-27; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 2,638,000,000.00 USD; period 2026-03-29/2026-06-27; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1744489/000174448926000057/dis-20260627.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMikwFBVV95cUxObnltanFMYXZnRzZtSkx3NUpmNmRSWmhZdDlFaUFKcFFnclB3Y3RuQ3R2RkRqQkhyTG1fOVRLTTJYcVdCT2hqaDVSaW1YQWFzZjg3RTF4dzFLcUdmZ0hVSExVd09DVTdEdmJWbXBrTjNwRjhzS29LbGVQNElUcEZFOEt1RzcxLTI0YzQ1c1BZekZZNTg?oc=5
- https://news.google.com/rss/articles/CBMid0FVX3lxTE5mUkgtN0I5X2FtclFwMWZkeFd1S3lLdTJXRXhCVGxQN2NjLXBJRzU2QkZXNWR1bDE4cHNlSEFBU0c1Y0FZU0VabWJoMDVsMUp6aEhrSzRLTnNreUMwZHUwUXBheS1qOEpfbThCeTB2MVd1dWJhbUR3?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxOVndXOFJydEpQc01GaS1CQVl3c0Y2QmF4MHZsTzUtUmQ0WWh4WEQ1dTkwLU8xbmpScEpFY2NOSU81TlBfM3ZZb3NCS3U0NVdWcEtRTHVudjRkQTNzOHdjYUtBdGRiVEJUTVNpWE00NDd5V2UycEp6czN3UEVDTVlKOVhhTERMRUpZcy14OVpEYXdDYTQ0My0tbkV2Q1dpNF83MFViaUs5WS1WeUhCa3N6eHp4T19wTncwRURjZnlSNS3SAcYBQVVfeXFMTUdHU095Ty1vaHEyY21ManRLLVFTREx5eUtjSlNGdUQ4c3NiWnVWQ2hqTHJzZmtGeElaaWJ2M3dBTkZmSEtEMXdFZzE3Wm9jUHRiWWs2MEpmcXV5OUVnQkxySHJsVE1MUlRnQTU1RUFWc1kzaUJya0FWUzVLSjJXcFhUYV93VjRFeVRyZmpOUm8yY1lsMDRmRUhuWk5ocWkxblp0YjMwYmFKbUFraDQyeTFEeVRqd3k5LTVWTEdpNWwyRUNMQkdR?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxPR1h5SUU0LXFib0pMaUxjOE9VR0Z1ZDhhWUhycl9YYXFlV2s1Ml80bHhBWm9oRllXTVNGNEoxUkVabW50VjVvaEx1dTgxZUIxdEkyamllVkE5QjM2Qmh1bVJNR3NnZW12YllJNGE5VEZhUDJ3dVFudGVjd2hTSmtBaUVoWnJjNXYzcWxTamxobG5pX3Z4Tlh6VWR2eFpNZkhaWUlYLTkxZFVNYXNKWDBtWnlLV1J5SmR0U3RsOUR3Qk04Z9IBxwFBVV95cUxNeGhLcHdfSmNlRFhESm16X3pkUmVIUEhpZVVsNzRjWWR5UGNsREJnZVU4TGRtVmtyZW5vNV9za054aVAtTHkzaEVfdWp1QmVSV2pPd1R6NVNiZjdHV0RwV182U3JfSldqQ3FSQXFyQlFZVXZET0ctQ0NxRDRibnViZHlpWUNXR1ZBdm9MVU9WeUFfbTdwdktOS3I5WjJjdXFFMUN0cFh6Y2R5U3l0QzNNdExuWkxsUEw5ajJ5eDVmazVha2dOVkpB?oc=5
- https://news.google.com/rss/articles/CBMi6AFBVV95cUxOaGh3SUVLS3MzejhVU085TEIwNFVIUU9laUZ5UWtEY01xcS13RHdyWkRVN3kyaDRRMWVLQzNNUGFoWTZ0enI2Nnp2bnBUTVItUUR0ZXJXbjdfWFo3Tm81a3FScmFHZ0U4eFlUeDZaUnFwRjhKQ0RoLUhNZWdjbTZmTzRMVjU5VzlhQmRUYV9fUGt6YTBiaUNBR1ljUzlvZng3djNzaVgxM3kxaTlrWkcwQmlKdXlxdWhkOTNwTU94VFEwZXFTSVc0Xy1zOVhRUE1jQXc4a2t0S05LdFVndXlXdlphbkxSZENt?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxPdDZsRTMyNjdybTktZEVTZ3JIaGxjeEVhd3VSVGUyc3hZNnlOcm14NWZxcDJuWGtGTFlFeU43WWJnSnNzSDd2ZW1QMWRIR3NPa0RNVlZBTlJWVGRoRXZDM3F0OW1wWEFLbzlZX3dDR0UzNWlHZ19SYWl4ejZLMWxEczR1QXdUaHpFTmlPOENfRHlJMDVrRGJLMkNn?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQZGhWalpQSjhncTE1ZEsyRy1KTHNXQ18yX0FRNlV6ekUyM1l1TzVOYUlfVFNiaFc3a256TFFVY3lwWXo4VGl5UElMalZYb3FMNHRDWjNZQWpBV3p4aVdpUmV4V1VzZlUyM1VHNEdaTlpMY3k2N3lESEpkb1ZVRWVlWkR5QTBLQ1JIYWNTTHRJV3pxanYwTi1NcA?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxPZ1RNTXN0U2dhM3RNaFM3b0lZMkgyVmlLMTRUVVlBOFZxZG93RjJ1aWRtLUJtLVd3dEFXYTdBX0hsYmlRbWpFMXQtRmNIcUV2UDdFcHVCd1lIR28taEhGWjF4d0tEb2ktcWl6ZExHSWROcXpHTEpDUmJkakZCT0ZFSEZ6M3dXUm1QSGVVRVE0M1VVb19QOG1hWnQ3bUpVNzdZQ25HZUZUVDZjOFM1N3poT3N5ejd6cUNoWi00Sg?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxOR0tUOVFtWkpDaFZpM0VXM1dybXlXMF94ZVh5SGYxRE82eUtRNV9qeEtRYnFlZTZXaW9aRHd5SDRSdHAwcDA1VUFxanBwNHBxeDJEUmYxMEkzdWk4aXpKQVVpSEZMLWVZN0pFZl8xTnZJUWt6OGpxc2lVX0RHZUFJQ1VKMU1XdkxjYjF5Q3pLN2NsZklOZHlJ?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxPcWhPMHdtNDFsTEZDUjZNbXJVWVNRSG92al83UEdlSU50dWcwQXRJUHpOUjV6d0dXSTRZcFpzYzZvNjRYdGVtTWdvcDVTMG9aSWp1SzZIU3laWnlraXdZVlA4TUhWaXBXdm5NUUo4M2k2WTdLOFYxMWR6UV9UbEtaT0lCQTQ2ZzhGUlJwVGtTRklvbGsxakl4dkM3ekU5UlR4aV9ZV0YtU2lHcWhjdURqQnVONnZRQXJSbXc5Mlpn?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxQOEdDdXl2bGNjMmg5WEs1T0I2RjE1V1lrdlpTR1hfYmYxa0EwT3NxN1lOUTdmVmpwc0tRRnVZcUI4QUV5dko3RGhnTmxkc1N4d3hFMTQ1UmpkM2xCSVVJUlA1b1NXSnpQUHZpUGFJSU53blZwVjl3QlJCczk2SkpkSmFYOUFycUdUWmQzTmpvZ0ItQ0ZRZ21JVk9MNS1fRWM?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
