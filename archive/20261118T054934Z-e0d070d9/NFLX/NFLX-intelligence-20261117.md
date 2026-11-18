# NFLX Intelligence Report

- ticker: **NFLX**
- Report as_of: **2026-11-17**
- Market data as_of: **2026-11-17**
- Quant sources: https://finance.yahoo.com/quote/NFLX/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NFLX/key-statistics/
- AI analysis snapshot as_of: **2026-11-17**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-18T05:58:39.956023+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 3, 'ai': 13, 'unknown': 0, 'irrelevant': 8})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **12** exact headline/source/date matches; prior report **20261117T062519Z-6171f6c2/NFLX** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 11 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 50.0%; oldest publication 2026-11-11

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 59.6800 |
| Return 1D (%) | -1.7613 |
| Return 1W (%) | -5.6592 |
| Return 1M (%) | -15.3835 |
| Return YTD (%) | -36.3481 |
| Return 1Y (%) | -45.8881 |
| Annualized volatility (%) | 36.2603 |
| Beta vs SPY | 0.2708 |
| Max drawdown (%) | -47.6904 |
| Sharpe (rf=0) | -1.5185 |
| Downside deviation (rf=0, %) | 26.6933 |
| Sortino (rf=0) | -2.0627 |
| Historical VaR 95% (1D, %) | 3.4403 |
| Historical ES 95% (1D, %) | 5.1152 |
| Correlation vs SPY | 0.1029 |
| Tracking error vs SPY (%) | 37.4416 |
| P/E (trailing) | 17.55 |
| P/B | 8.37 |
| EV/EBITDA | 15.94 |
| Revenue growth (%) | 11.80 |
| Forward P/E (estimate) | 15.82 |
| Gross margin (%) | 50.69 |
| Operating margin (%) | 31.30 |
| Return on equity (%) | 53.46 |
| Free cash flow yield (%) | 10.40 |
| MA50 | 68.4928 |
| Close vs MA50 (%) | -12.8668 |
| MA200 | 80.2687 |
| Close vs MA200 (%) | -25.6498 |
| RSI (14, Wilder) | 32.9830 |
| MACD (12,26) | -2.0401 |
| MACD signal (9) | -1.9551 |
| MACD histogram | -0.0850 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NFLX': 284, 'SPY': 284}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 59.6800 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.7613 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -5.6592 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -15.3835 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -36.3481 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -45.8881 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 36.2603 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 26.6933 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -2.0627 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.4403 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.1152 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.1029 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 37.4416 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.2708 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -47.6904 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -1.5185 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 15.8246 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 50.6850 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 31.2960 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 53.4630 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 10.3955 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 17.5529 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 32.9830 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.0850 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -12.8668 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -25.6498 -> Clearly below the moving-average trend level.

## TAILWINDS

### NFLX Stock Edges Higher Overnight: Evercore Swaps Netflix For Spotify On Top Picks List
- Summary: NFLX Stock Edges Higher Overnight: Evercore Swaps Netflix For Spotify On Top Picks List
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxQQ3VZcm5lRlRBZE15a3pBMWxZRHBRVlhhYjQwQU9YWEhQYktpdWNkTngyN3R6VkZQaEZTMEp1OHZLQTJCbml1eElwSDljampSQ3RDMWx4MVZYUjNKRlRqdFpRWTVtU2NNeDYtWDdoenRyaHlOWV9aYlBTYUVHUlRRWTFIUjZST2k0U2ZVSlFIN3NGbk00Vjd4eVByNVFfT00?oc=5>

### Billionaire investor Bill Ackman on why he's staying bullish on Netflix
- Summary: Ackman remains bullish, indicating strong support for Netflix’s future prospects.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMizwFBVV95cUxPN2FXdVM4Rlh5TzBFZjVTOHRLS05zTmJhd1FvRm5kMXRGZUY3RV9Sd3hRUHZKMUV3eGlURzFwclBueGRlRlhhVmRUTWhJNGFObVByaGpMcWwzZHJydU9Hc3VmVDFYOVNUT2dKdDNjc0h4ZXZkT3lWZTlVRUlrSkZjX3pPUmdWckNUeEt2dVY3TmphMHI4YUFTelgxa2xZcWJBZ3dBME9DcVZOM3pRTGlFcmpyZWZIVE5KY3ROcXNGbWlPclFUTjJHMjYwWDloN0U?oc=5>

### Netflix (NASDAQ: NFLX) Stock Trades At A Decade-Low Valuation As Its Advertising Business Holds The Key To A Potential Rebound
- Summary: Low valuation and a growing advertising business suggest a potential rebound for Netflix.
- Date: 2026-11-13 | Impact: medium | Horizon: medium | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiggJBVV95cUxNZV9WTjdQZmFwMWNGZWNtd29sOElEaHVLTDB0MlJuamJVdVQzT0l6TmVhbnVkc2gxUE9xMFBnOG1FZEFBNG85d0RDY0lOVWdjaC1MN3RVdXJRdWd4enRvUGFRYmJ4TE9vWV9wTldScFV6OEE0ZzJyWnJFRXZZZkpxU1NsQjRrQ2xBU0RYcEJWbUpjM1pjd0FmYmxKZXlvbmZGVENjYzQ0Q0R3OWJWQzhlYTdWbmhrVTFlZTdJX2pmQzFLaHJyVmVheXd4alRsQzBINF9uTlNPNVVzZVNOWjdWWVRXZEV4c2I5bC15UTZIenhzYjN6N3M1aHlTVGtFWFZqUEE?oc=5>

## HEADWINDS

### Netflix (NASDAQ:NFLX) Stock Price Down 2.9% - What's Next?
- Summary: Netflix (NASDAQ:NFLX) Stock Price Down 2.9% - What's Next?
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxQRTBpV1JIUGU2aXI3T2FBelhEaTA3dmxtZDNlNkZueDdlaHQ4YzltZWhVRHhTYXY0OTVad1NidG9kNDMwbE96cTlOVVhXbWZHa2ItUGJKSk42Tk1ESVZDOHBpTjc3dlVnckh3clpwY01XMTIwc0JFajRLYlFld0lfeTNJSkhPWFQ5VGVQVzVSQlQ2aWE3R2xxbk1wUDJkeXZMc1hVeVlGV2ROZW5CZDNN?oc=5>

### Netflix (NFLX) Stock May Be a ‘Loser’ This Year, But You Can Still Scalp Profits From It
- Summary: Shares may underperform this year, but short-term trading opportunities remain.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixgFBVV95cUxQaF9lS2lHZnpDYmpGM3FsQXdWZmJGV29qb05VNGJXQkR0SVhQV2JaLUNFWjFpb3VjTDFHeXFJUHhNZkd3b0U4Rk5TcXBZOWZVRF9GZFFTd3dwSEJhMmdjbzV6MFg3dEtwQWtTS1ZXLXU3UmQ4YXB2aFAzUFBiTHdfd1VhZ1Q2ZGlyeVpjQUlPbXJkVEtkUm5uMTlacklKaWlENDdGWXJyXzdYbTJ5c0NvamlGS01SdzQzNkR0SmIycmlaUzJHN2c?oc=5>

## CATALYSTS

### Netflix (NFLX) Stock Hits One-Year Low as Buybacks Outpace Free Cash Flow
- Summary: Netflix (NFLX) Stock Hits One-Year Low as Buybacks Outpace Free Cash Flow
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxPZXVSVEFNQk1oMVNZREhhVllKUVZubmd6Zll3TVotS1NNdTRraHAtSk5YZUlEV1lua3JldGd0UjkxUWNXOXo2aE1rY2JZRlJWVU9ZZkl3MloyVWhDU2hzU2ViQnh4bnBLcUFHOFpadmtoUW5VaEVFdjlrdDJjNDJMaUVtMmMwRWMwNEF5NHRsVVYya3ctMDFfckRBUQ?oc=5>

### Netflix Stock Now Trades at a 70% Discount to Its Peak Valuation, and One Number Is to Blame
- Summary: Shares are 70% below peak, attributed to a single metric.
- Date: 2026-11-16 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxPd3hXU1A4QW5XVDRHeEFOZ0UxYkp1TmU1bERCblNTM0g1c1ZRcm14YWhBRkJDdDE2dHZ3Ty1SQ2dnV0xXTEJYWGQ0cDl2REE2UG9Zb19hWGN5ZHVxQU5DT2pmckZnckxrT1QzcUFCS0taT050S0Zzb1lmNUNQa3E3Zy16Ukplb09USXhNdUFISzB0aEFlbEFr?oc=5>

### Should Netflix (NFLX) Investors Rethink Its Outlook After Bill Ackman’s Fresh Backing?
- Summary: Bill Ackman’s new support may shift investor sentiment toward Netflix.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxQUDBZc0M0UWw0WE5Wb2R0UXpESl9BRDJjZnZqWEh4R2lTVmdtM0ZaTGxKRmd4dHR6Nk9hMmdkNWhaaGtCWjJMQktaU3hySWU4TUpLYmV4eDZvTW5Id0hrNlNhTTM1OHpTWG5GLWpFajRuT1VQZkxIVVZpWGdncW9xb25nVWdJVzdjZDNaZUZhWC1SdnJMcnc2NjhMMEZET25zZW5xZlJn?oc=5>

### Can Netflix Stock Fall 50%?
- Summary: Questions potential 50% decline in Netflix shares.
- Date: 2026-11-16 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxPWW05ekMtcWpHNzBsWDk3ZElHMUtwbW9LR19UWU9DVjRBanZuT21sTjljQlo5b2JJcWhWQ25LTUtzaEVRQjJhTXZfdWl4WU9Gakp4R2E5X3lLcVRTb3l5aXg2cWVHQ1o5cEsyY0lKaE01SVFHeTJSUlV3MXIyT1Y3bjhHRlRlNjYwUnA1UkU5WEFodw?oc=5>

### Netflix Lowers 2026 Ad Revenue Forecast: Time to Hold the Stock?
- Summary: Reduced 2026 ad revenue outlook may affect stock valuation.
- Date: 2026-11-16 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxPd0NyZTVEaFVjdnl1b0k2VzdTMnotSjBXMk9ZZVZmSDdtUHJWMVJZZkphTnA2WElubUxLZmRERC1vYUY1cUFfOTNJYUo0RExvMFNGUFhtNXVQR0FBZkZhczdNNzU0dmI5ZDdjbTltUHE0RkN6N1FLcmRIOGFNR1dJLXB5UVRXU2p3X09yRUwzR05hQ2pMc3FneE15RUVoMXEtLUZtSXhTdDhhOGF2cExlOGlTcktaVlFTYmc?oc=5>

### Netflix Stock Has Been Cut in Half Since Its 2025 Peak. History Says What Came After Its Last 5 Drops Like This.
- Summary: Netflix shares have dropped significantly since 2025 peak, reflecting a steep decline in investor confidence.
- Date: 2026-11-14 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxOQ296RXdJRWNIbGJvU2V5UEdiMGUzVi15ekw0QnNIb0g0c2F0WWFTa1JHSlFEOGxtZ2hDb1d6eWtwWU1OcjdTUWVmSjFYMVF2ekthWmZ2aGhoMVZOa3k5QktkZWl3S3JiV1JhOFBRTHRUd2xJMjFWbVpjdHliaUZtXzI4cURGUDQ0bFFGMEc1aEEzeGNpRUU0TQ?oc=5>

### Netflix Stock Hits New 52-Week Low: Here's What Investors Need to Know
- Summary: Netflix shares reach a new 52-week low, signaling potential downside risk for investors.
- Date: 2026-11-17 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiyAFBVV95cUxQOUk0TTJyaWQyc1RHT05KNGJzVEhsT05qNWN2V2xtb2NCc2R0czFjbDR1V1hSOTBUcEN2RnYwT25aOWdnQ2xUTnQydmxBV1Juc3RoN0cxSk1mQ08zZWRsdEpVX21INzlpMUtUdHJGTTZiTk9VLUFPVW9BM3pOZW5zMTNUcW1sQ182VEI1UkVfbmtpS25QOExOb2hBZWNRbl9LNlZodXpXRkV2M3N1bkVqOVBBc25hbXBUUnUyOU1rb3VBTmJQMkJkZA?oc=5>

### Netflix stock analysis: what next for this fallen angel?
- Summary: Analysis suggests Netflix may continue to struggle, with potential further declines in stock value.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxNUEhsY1BkSjBrVDZzaVkxbS1jdmU1TjBScGhFQ3dWRUpxYmNITnJRVF9ublI4X1dZcnRtOFdocVN3U1ktS1ZVakpUZ0pjMFhNWjJiRGp0aFg2c1pHc3FHMGVsU0psb1JXNFFtWEZkalFqMk42eDdBbHFXN24xQzJlRkFoZHFvOWFUNGNfeWIyTnpLNGhZ?oc=5>

### Netflix (NFLX) Price Prediction: Bearish trend meets near-term support as analyst targets stay above spot
- Summary: Bearish trend persists for Netflix, though analysts maintain support levels above current price.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxOM2d4TnV3cVN5Z2NCYzZ3dWotMUNwYks5ZXVjaUk2VWZPQm1CYTBCVlczRUNkU0J2TWJYNEp0SV9ob2ExaXd3YUw1bDYzaW9Ed2doWHl1Wm43b3V5R3I5WVBrQVc3WFRpMGpPMHNpbVBUR3RsMXRydVprTzRreXpxeFFjdVBtSWlWTVU2djRkY3lmMnVENUV2TVZ1N3NYZw?oc=5>

## RISKS

### What Could Surprise Netflix Stock Investors On The Upside?
- Summary: Potential upside factors could alter expectations for Netflix stock.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxPWjJQa19fOGt4UGtqcFJHTzZDWEdmNVJoRmo2N19ZN0lYMllBaVR1LWQxNzQxZjVQamRsTkpPZTVzM04xZHREdmU5ZWtPR3VIeDhNQy05Rm9GeE5WZm03XzBUTlhJUkloTUp1TW9za0MzMEVXYTFyUXBjRkhhUFUwRlRxSVo4ZHhWQkdoOWFXRXEzTlZqSmktUkpCQ2xhQTZLaV80TWlB?oc=5>

### Netflix Stock Outlook: Is Wall Street Bullish or Bearish?
- Summary: Analysts debate bullish versus bearish outlook for Netflix.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxPdmdOMkF2LUM5SmJFMkluV2l4S2FtS2RadUF5eWFfczJLY3htRWM5ZWo5V09FaDFoRExPVjZnaHF2N2ZSRlZVRGRBUEswUTFHdE45OTVRUUZSa2JMaGtIQzFjdU1OVjNwdElxSmxsUTg5dDRPVmNmcHdlUnEtRUs0RUJ4SGlfdVpQY0oxUlR0OEJSclNxWGVzeUx5ME8xd3M?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **NFLX** | **17.55** | **8.37** | **15.94** | **11.80** | **245,065,531,392.00 USD** | **-45.89** |
| DIS | 20.77 | 1.84 | 11.91 | 6.80 | 201,918,758,912.00 USD | 12.25 |
| WBD | N/A | 2.36 | 13.79 | -11.20 | 77,595,885,568.00 USD | N/A |
| CMCSA | 8.11 | 0.97 | 5.06 | -6.10 | 89,875,963,904.00 USD | 4.53 |

Peers fetched as_of: 2026-11-17; NFLX reuses existing data (market data as_of: 2026-11-17); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-20
- Next expected earnings: 2027-01-19 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-17

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-21
- Revenue (latest available single quarter): 12,874,176,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 3,663,927,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1065280/000106528026000291/nflx-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMinwFBVV95cUxQQ3VZcm5lRlRBZE15a3pBMWxZRHBRVlhhYjQwQU9YWEhQYktpdWNkTngyN3R6VkZQaEZTMEp1OHZLQTJCbml1eElwSDljampSQ3RDMWx4MVZYUjNKRlRqdFpRWTVtU2NNeDYtWDdoenRyaHlOWV9aYlBTYUVHUlRRWTFIUjZST2k0U2ZVSlFIN3NGbk00Vjd4eVByNVFfT00?oc=5
- https://news.google.com/rss/articles/CBMizwFBVV95cUxPN2FXdVM4Rlh5TzBFZjVTOHRLS05zTmJhd1FvRm5kMXRGZUY3RV9Sd3hRUHZKMUV3eGlURzFwclBueGRlRlhhVmRUTWhJNGFObVByaGpMcWwzZHJydU9Hc3VmVDFYOVNUT2dKdDNjc0h4ZXZkT3lWZTlVRUlrSkZjX3pPUmdWckNUeEt2dVY3TmphMHI4YUFTelgxa2xZcWJBZ3dBME9DcVZOM3pRTGlFcmpyZWZIVE5KY3ROcXNGbWlPclFUTjJHMjYwWDloN0U?oc=5
- https://news.google.com/rss/articles/CBMiggJBVV95cUxNZV9WTjdQZmFwMWNGZWNtd29sOElEaHVLTDB0MlJuamJVdVQzT0l6TmVhbnVkc2gxUE9xMFBnOG1FZEFBNG85d0RDY0lOVWdjaC1MN3RVdXJRdWd4enRvUGFRYmJ4TE9vWV9wTldScFV6OEE0ZzJyWnJFRXZZZkpxU1NsQjRrQ2xBU0RYcEJWbUpjM1pjd0FmYmxKZXlvbmZGVENjYzQ0Q0R3OWJWQzhlYTdWbmhrVTFlZTdJX2pmQzFLaHJyVmVheXd4alRsQzBINF9uTlNPNVVzZVNOWjdWWVRXZEV4c2I5bC15UTZIenhzYjN6N3M1aHlTVGtFWFZqUEE?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxQRTBpV1JIUGU2aXI3T2FBelhEaTA3dmxtZDNlNkZueDdlaHQ4YzltZWhVRHhTYXY0OTVad1NidG9kNDMwbE96cTlOVVhXbWZHa2ItUGJKSk42Tk1ESVZDOHBpTjc3dlVnckh3clpwY01XMTIwc0JFajRLYlFld0lfeTNJSkhPWFQ5VGVQVzVSQlQ2aWE3R2xxbk1wUDJkeXZMc1hVeVlGV2ROZW5CZDNN?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxQaF9lS2lHZnpDYmpGM3FsQXdWZmJGV29qb05VNGJXQkR0SVhQV2JaLUNFWjFpb3VjTDFHeXFJUHhNZkd3b0U4Rk5TcXBZOWZVRF9GZFFTd3dwSEJhMmdjbzV6MFg3dEtwQWtTS1ZXLXU3UmQ4YXB2aFAzUFBiTHdfd1VhZ1Q2ZGlyeVpjQUlPbXJkVEtkUm5uMTlacklKaWlENDdGWXJyXzdYbTJ5c0NvamlGS01SdzQzNkR0SmIycmlaUzJHN2c?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxPZXVSVEFNQk1oMVNZREhhVllKUVZubmd6Zll3TVotS1NNdTRraHAtSk5YZUlEV1lua3JldGd0UjkxUWNXOXo2aE1rY2JZRlJWVU9ZZkl3MloyVWhDU2hzU2ViQnh4bnBLcUFHOFpadmtoUW5VaEVFdjlrdDJjNDJMaUVtMmMwRWMwNEF5NHRsVVYya3ctMDFfckRBUQ?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxPd3hXU1A4QW5XVDRHeEFOZ0UxYkp1TmU1bERCblNTM0g1c1ZRcm14YWhBRkJDdDE2dHZ3Ty1SQ2dnV0xXTEJYWGQ0cDl2REE2UG9Zb19hWGN5ZHVxQU5DT2pmckZnckxrT1QzcUFCS0taT050S0Zzb1lmNUNQa3E3Zy16Ukplb09USXhNdUFISzB0aEFlbEFr?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxQUDBZc0M0UWw0WE5Wb2R0UXpESl9BRDJjZnZqWEh4R2lTVmdtM0ZaTGxKRmd4dHR6Nk9hMmdkNWhaaGtCWjJMQktaU3hySWU4TUpLYmV4eDZvTW5Id0hrNlNhTTM1OHpTWG5GLWpFajRuT1VQZkxIVVZpWGdncW9xb25nVWdJVzdjZDNaZUZhWC1SdnJMcnc2NjhMMEZET25zZW5xZlJn?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxPWW05ekMtcWpHNzBsWDk3ZElHMUtwbW9LR19UWU9DVjRBanZuT21sTjljQlo5b2JJcWhWQ25LTUtzaEVRQjJhTXZfdWl4WU9Gakp4R2E5X3lLcVRTb3l5aXg2cWVHQ1o5cEsyY0lKaE01SVFHeTJSUlV3MXIyT1Y3bjhHRlRlNjYwUnA1UkU5WEFodw?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxPd0NyZTVEaFVjdnl1b0k2VzdTMnotSjBXMk9ZZVZmSDdtUHJWMVJZZkphTnA2WElubUxLZmRERC1vYUY1cUFfOTNJYUo0RExvMFNGUFhtNXVQR0FBZkZhczdNNzU0dmI5ZDdjbTltUHE0RkN6N1FLcmRIOGFNR1dJLXB5UVRXU2p3X09yRUwzR05hQ2pMc3FneE15RUVoMXEtLUZtSXhTdDhhOGF2cExlOGlTcktaVlFTYmc?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxOQ296RXdJRWNIbGJvU2V5UEdiMGUzVi15ekw0QnNIb0g0c2F0WWFTa1JHSlFEOGxtZ2hDb1d6eWtwWU1OcjdTUWVmSjFYMVF2ekthWmZ2aGhoMVZOa3k5QktkZWl3S3JiV1JhOFBRTHRUd2xJMjFWbVpjdHliaUZtXzI4cURGUDQ0bFFGMEc1aEEzeGNpRUU0TQ?oc=5
- https://news.google.com/rss/articles/CBMi6AFBVV95cUxNSlZxdEt3TEpUczA4YVRHTUllS08yalltOGJPYUpuVHpQZzBTX2lDZWxzYjVMdTdydWdubzJjTHcyTFAxOWstS2FsLUxhVnJkLUxwSTVKOXBnTnJRdi1rZTJJYWVIWnhHYWc2WDB4UkVkcWhwc3VpbjhBWGptdU1mS29TdWxuMm5ZeHN6QkpyTkpzMjZCTW5XUVFQNDZmTVkwaE9KMFd4cVdFd2dmbGZzbWg0OHh1aEo3b0FsZVBWNVhMTW5TY1FiVDU5QV9KR1I3dXh3c2Z4aEZqbkJ2ekdiTE1EalZFZ2Mt?oc=5
- https://news.google.com/rss/articles/CBMiyAFBVV95cUxQOUk0TTJyaWQyc1RHT05KNGJzVEhsT05qNWN2V2xtb2NCc2R0czFjbDR1V1hSOTBUcEN2RnYwT25aOWdnQ2xUTnQydmxBV1Juc3RoN0cxSk1mQ08zZWRsdEpVX21INzlpMUtUdHJGTTZiTk9VLUFPVW9BM3pOZW5zMTNUcW1sQ182VEI1UkVfbmtpS25QOExOb2hBZWNRbl9LNlZodXpXRkV2M3N1bkVqOVBBc25hbXBUUnUyOU1rb3VBTmJQMkJkZA?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxNUEhsY1BkSjBrVDZzaVkxbS1jdmU1TjBScGhFQ3dWRUpxYmNITnJRVF9ublI4X1dZcnRtOFdocVN3U1ktS1ZVakpUZ0pjMFhNWjJiRGp0aFg2c1pHc3FHMGVsU0psb1JXNFFtWEZkalFqMk42eDdBbHFXN24xQzJlRkFoZHFvOWFUNGNfeWIyTnpLNGhZ?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxOM2d4TnV3cVN5Z2NCYzZ3dWotMUNwYks5ZXVjaUk2VWZPQm1CYTBCVlczRUNkU0J2TWJYNEp0SV9ob2ExaXd3YUw1bDYzaW9Ed2doWHl1Wm43b3V5R3I5WVBrQVc3WFRpMGpPMHNpbVBUR3RsMXRydVprTzRreXpxeFFjdVBtSWlWTVU2djRkY3lmMnVENUV2TVZ1N3NYZw?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxPWjJQa19fOGt4UGtqcFJHTzZDWEdmNVJoRmo2N19ZN0lYMllBaVR1LWQxNzQxZjVQamRsTkpPZTVzM04xZHREdmU5ZWtPR3VIeDhNQy05Rm9GeE5WZm03XzBUTlhJUkloTUp1TW9za0MzMEVXYTFyUXBjRkhhUFUwRlRxSVo4ZHhWQkdoOWFXRXEzTlZqSmktUkpCQ2xhQTZLaV80TWlB?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxPdmdOMkF2LUM5SmJFMkluV2l4S2FtS2RadUF5eWFfczJLY3htRWM5ZWo5V09FaDFoRExPVjZnaHF2N2ZSRlZVRGRBUEswUTFHdE45OTVRUUZSa2JMaGtIQzFjdU1OVjNwdElxSmxsUTg5dDRPVmNmcHdlUnEtRUs0RUJ4SGlfdVpQY0oxUlR0OEJSclNxWGVzeUx5ME8xd3M?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
