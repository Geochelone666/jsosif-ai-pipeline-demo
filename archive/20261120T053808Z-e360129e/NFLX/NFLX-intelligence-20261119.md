# NFLX Intelligence Report

- ticker: **NFLX**
- Report as_of: **2026-11-19**
- Market data as_of: **2026-11-19**
- Quant sources: https://finance.yahoo.com/quote/NFLX/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/NFLX/key-statistics/
- AI analysis snapshot as_of: **2026-11-19**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-20T05:46:38.316957+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 22, 'rule': 1, 'ai': 8, 'unknown': 0, 'irrelevant': 13})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **8** exact headline/source/date matches; prior report **20261118T054934Z-e0d070d9/NFLX** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'low_uncalibrated_model_confidence': 2}
- RSS source audit (metadata only, not article fact-checking): 22 unique headlines; 8 named publishers; 3 exact duplicates; 22 HTTPS source links; largest publisher share 40.91%; oldest publication 2026-11-13

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 58.4600 |
| Return 1D (%) | -2.2735 |
| Return 1W (%) | -6.7475 |
| Return 1M (%) | -16.3064 |
| Return YTD (%) | -37.6493 |
| Return 1Y (%) | -46.8545 |
| Annualized volatility (%) | 35.9765 |
| Beta vs SPY | 0.3098 |
| Max drawdown (%) | -46.8545 |
| Sharpe (rf=0) | -1.5835 |
| Downside deviation (rf=0, %) | 26.5484 |
| Sortino (rf=0) | -2.1458 |
| Historical VaR 95% (1D, %) | 3.4231 |
| Historical ES 95% (1D, %) | 5.1040 |
| Correlation vs SPY | 0.1197 |
| Tracking error vs SPY (%) | 36.9839 |
| P/E (trailing) | 16.90 |
| P/B | 8.20 |
| EV/EBITDA | 15.63 |
| Revenue growth (%) | 11.80 |
| Forward P/E (estimate) | 15.50 |
| Gross margin (%) | 50.69 |
| Operating margin (%) | 31.30 |
| Return on equity (%) | 53.46 |
| Free cash flow yield (%) | 10.61 |
| MA50 | 67.8176 |
| Close vs MA50 (%) | -13.7982 |
| MA200 | 80.0596 |
| Close vs MA200 (%) | -26.9794 |
| RSI (14, Wilder) | 30.7093 |
| MACD (12,26) | -2.2762 |
| MACD signal (9) | -2.0466 |
| MACD histogram | -0.2296 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'NFLX': 286, 'SPY': 286}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 58.4600 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -2.2735 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -6.7475 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -16.3064 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -37.6493 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -46.8545 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 35.9765 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 26.5484 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -2.1458 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.4231 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.1040 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.1197 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 36.9839 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.3098 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -46.8545 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -1.5835 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 15.5011 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 50.6850 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 31.2960 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 53.4630 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 10.6125 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 16.8960 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 30.7093 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.2296 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -13.7982 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -26.9794 -> Clearly below the moving-average trend level.

## TAILWINDS

### NFLX Stock Edges Higher Overnight: Evercore Swaps Netflix For Spotify On Top Picks List
- Summary: NFLX Stock Edges Higher Overnight: Evercore Swaps Netflix For Spotify On Top Picks List
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxQQ3VZcm5lRlRBZE15a3pBMWxZRHBRVlhhYjQwQU9YWEhQYktpdWNkTngyN3R6VkZQaEZTMEp1OHZLQTJCbml1eElwSDljampSQ3RDMWx4MVZYUjNKRlRqdFpRWTVtU2NNeDYtWDdoenRyaHlOWV9aYlBTYUVHUlRRWTFIUjZST2k0U2ZVSlFIN3NGbk00Vjd4eVByNVFfT00?oc=5>

## HEADWINDS

### Netflix Engagement Growth Is Slowing. Here’s Why I Bought More Anyway.
- Summary: Netflix reports slowing engagement growth, potentially impacting future subscriber growth.
- Date: 2026-11-14 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxNUDg2NjRQTFZaakJxNExNaHliTGJvc3M3TVpZS051aFRuelExOURBOGMydmE0YXlpdTJxVVI2dE5kdjIwaGRKclZxQWU2SFN4YV9FVV9GZTRTRmJ6ODY1N2ZxcTQ3LXNySFNrcE1yT3NMVkIzcVhjaFEtX3dmb2VVUkNOZkFEQ2RGUm9WV1kzSHBSVGV2LUxOTVBXeHRNU0ZvVVBtbA?oc=5>

### Netflix (NASDAQ:NFLX) Stock Price Down 2.3% - Should You Sell?
- Summary: Netflix shares fell 2.3%, prompting investors to consider selling amid market volatility.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxQbnJYNkxHaHh1VFdiVGl1TURPdlRtT2xjNHU3Q1FlbUJsZzBjNXlnT24tcW1HWHd4VzNLeXFoZTZha0RUMS1GbEVRNmZCeXNJcmZpenR5dnJQRFZHNlFfOUhjOUs0dXY5R3p4LW95cDRYQmptb1pkZThFUVB3TWp2S0VWTXU0SEJSNFFQNEEwTGhUMjRsbUNmbHBwd2FaN2llemgwdGFoa0RsQ1oxTDVHQlM1OW9rQQ?oc=5>

## CATALYSTS

### Can Netflix Stock Fall 50%?
- Summary: Questions potential 50% decline in Netflix shares.
- Date: 2026-11-16 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxPWW05ekMtcWpHNzBsWDk3ZElHMUtwbW9LR19UWU9DVjRBanZuT21sTjljQlo5b2JJcWhWQ25LTUtzaEVRQjJhTXZfdWl4WU9Gakp4R2E5X3lLcVRTb3l5aXg2cWVHQ1o5cEsyY0lKaE01SVFHeTJSUlV3MXIyT1Y3bjhHRlRlNjYwUnA1UkU5WEFodw?oc=5>

### Netflix Stock Now Trades at a 70% Discount to Its Peak Valuation, and One Number Is to Blame
- Summary: Shares are 70% below peak, attributed to a single metric.
- Date: 2026-11-16 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxPd3hXU1A4QW5XVDRHeEFOZ0UxYkp1TmU1bERCblNTM0g1c1ZRcm14YWhBRkJDdDE2dHZ3Ty1SQ2dnV0xXTEJYWGQ0cDl2REE2UG9Zb19hWGN5ZHVxQU5DT2pmckZnckxrT1QzcUFCS0taT050S0Zzb1lmNUNQa3E3Zy16Ukplb09USXhNdUFISzB0aEFlbEFr?oc=5>

### Netflix Stock Hits New 52-Week Low: Here's What Investors Need to Know
- Summary: Netflix shares reach a new 52-week low, signaling potential downside risk for investors.
- Date: 2026-11-17 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiyAFBVV95cUxQOUk0TTJyaWQyc1RHT05KNGJzVEhsT05qNWN2V2xtb2NCc2R0czFjbDR1V1hSOTBUcEN2RnYwT25aOWdnQ2xUTnQydmxBV1Juc3RoN0cxSk1mQ08zZWRsdEpVX21INzlpMUtUdHJGTTZiTk9VLUFPVW9BM3pOZW5zMTNUcW1sQ182VEI1UkVfbmtpS25QOExOb2hBZWNRbl9LNlZodXpXRkV2M3N1bkVqOVBBc25hbXBUUnUyOU1rb3VBTmJQMkJkZA?oc=5>

### Netflix is considered the frontrunner to win the 2030 World Cup media rights (NFLX:NASDAQ)
- Summary: Netflix is positioned to secure 2030 World Cup media rights, potentially expanding its sports content portfolio and boosting subscriber growth.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxONUt6c2YwTEJXdjh4UzJCQnZJRlFHRFRveFFkSW8wWExZeWlRVDRmdklsdTA1T3ZaN3BEMXgwemI2b2VIN0dTU3BBbG9lbDN5dFlMcWFaTDdGTUFZR0UxYjdOUzc2R0xOMU9NNVd6SDJONFhUSDZJcVdMY3kxVjB4WmpsS1B2VFRWTmpuNHJHaEk4bEx6TTc4cHhYcUVjalM4QlJYQ1lyUHZuejNJNDNVbmlUbzE?oc=5>

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
| **NFLX** | **16.90** | **8.20** | **15.63** | **11.80** | **240,055,812,096.00 USD** | **-46.85** |
| DIS | 21.36 | 1.87 | 11.25 | 15.50 | 205,390,577,664.00 USD | 16.55 |
| WBD | N/A | 2.36 | 13.79 | -11.20 | 77,595,885,568.00 USD | N/A |
| CMCSA | 7.99 | 0.95 | 5.01 | -6.10 | 88,278,016,000.00 USD | 4.01 |

Peers fetched as_of: 2026-11-19; NFLX reuses existing data (market data as_of: 2026-11-19); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-20
- Next expected earnings: 2027-01-19 (yfinance; expected dates may change)

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
- Filing date: 2026-10-21
- Revenue (latest available single quarter): 12,874,176,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 3,663,927,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1065280/000106528026000291/nflx-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMinwFBVV95cUxQQ3VZcm5lRlRBZE15a3pBMWxZRHBRVlhhYjQwQU9YWEhQYktpdWNkTngyN3R6VkZQaEZTMEp1OHZLQTJCbml1eElwSDljampSQ3RDMWx4MVZYUjNKRlRqdFpRWTVtU2NNeDYtWDdoenRyaHlOWV9aYlBTYUVHUlRRWTFIUjZST2k0U2ZVSlFIN3NGbk00Vjd4eVByNVFfT00?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxNUDg2NjRQTFZaakJxNExNaHliTGJvc3M3TVpZS051aFRuelExOURBOGMydmE0YXlpdTJxVVI2dE5kdjIwaGRKclZxQWU2SFN4YV9FVV9GZTRTRmJ6ODY1N2ZxcTQ3LXNySFNrcE1yT3NMVkIzcVhjaFEtX3dmb2VVUkNOZkFEQ2RGUm9WV1kzSHBSVGV2LUxOTVBXeHRNU0ZvVVBtbA?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxQbnJYNkxHaHh1VFdiVGl1TURPdlRtT2xjNHU3Q1FlbUJsZzBjNXlnT24tcW1HWHd4VzNLeXFoZTZha0RUMS1GbEVRNmZCeXNJcmZpenR5dnJQRFZHNlFfOUhjOUs0dXY5R3p4LW95cDRYQmptb1pkZThFUVB3TWp2S0VWTXU0SEJSNFFQNEEwTGhUMjRsbUNmbHBwd2FaN2llemgwdGFoa0RsQ1oxTDVHQlM1OW9rQQ?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxPWW05ekMtcWpHNzBsWDk3ZElHMUtwbW9LR19UWU9DVjRBanZuT21sTjljQlo5b2JJcWhWQ25LTUtzaEVRQjJhTXZfdWl4WU9Gakp4R2E5X3lLcVRTb3l5aXg2cWVHQ1o5cEsyY0lKaE01SVFHeTJSUlV3MXIyT1Y3bjhHRlRlNjYwUnA1UkU5WEFodw?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxPd3hXU1A4QW5XVDRHeEFOZ0UxYkp1TmU1bERCblNTM0g1c1ZRcm14YWhBRkJDdDE2dHZ3Ty1SQ2dnV0xXTEJYWGQ0cDl2REE2UG9Zb19hWGN5ZHVxQU5DT2pmckZnckxrT1QzcUFCS0taT050S0Zzb1lmNUNQa3E3Zy16Ukplb09USXhNdUFISzB0aEFlbEFr?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxNOWpfV3UtY2xldE5YOWRsRk91THhqckx0ZVpJQU82WkdyQ0RNYUhPSTBZY05oOHBGNVlCTlh3ejZrT2NzcG1WRU93NzJVWFVOSjBrWXR3UDFRSDJmSkRldG96MzQwT1dLTzIwTmxQSk9tOWRRVE1vb2llc0UxUlh0aGJUVU82UXowZlZjTFNpc2p2OXhsaGJKSHpldncyU1BjdGxycC1RTmtHaTA?oc=5
- https://news.google.com/rss/articles/CBMiyAFBVV95cUxQOUk0TTJyaWQyc1RHT05KNGJzVEhsT05qNWN2V2xtb2NCc2R0czFjbDR1V1hSOTBUcEN2RnYwT25aOWdnQ2xUTnQydmxBV1Juc3RoN0cxSk1mQ08zZWRsdEpVX21INzlpMUtUdHJGTTZiTk9VLUFPVW9BM3pOZW5zMTNUcW1sQ182VEI1UkVfbmtpS25QOExOb2hBZWNRbl9LNlZodXpXRkV2M3N1bkVqOVBBc25hbXBUUnUyOU1rb3VBTmJQMkJkZA?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxONUt6c2YwTEJXdjh4UzJCQnZJRlFHRFRveFFkSW8wWExZeWlRVDRmdklsdTA1T3ZaN3BEMXgwemI2b2VIN0dTU3BBbG9lbDN5dFlMcWFaTDdGTUFZR0UxYjdOUzc2R0xOMU9NNVd6SDJONFhUSDZJcVdMY3kxVjB4WmpsS1B2VFRWTmpuNHJHaEk4bEx6TTc4cHhYcUVjalM4QlJYQ1lyUHZuejNJNDNVbmlUbzE?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxPWjJQa19fOGt4UGtqcFJHTzZDWEdmNVJoRmo2N19ZN0lYMllBaVR1LWQxNzQxZjVQamRsTkpPZTVzM04xZHREdmU5ZWtPR3VIeDhNQy05Rm9GeE5WZm03XzBUTlhJUkloTUp1TW9za0MzMEVXYTFyUXBjRkhhUFUwRlRxSVo4ZHhWQkdoOWFXRXEzTlZqSmktUkpCQ2xhQTZLaV80TWlB?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxPdmdOMkF2LUM5SmJFMkluV2l4S2FtS2RadUF5eWFfczJLY3htRWM5ZWo5V09FaDFoRExPVjZnaHF2N2ZSRlZVRGRBUEswUTFHdE45OTVRUUZSa2JMaGtIQzFjdU1OVjNwdElxSmxsUTg5dDRPVmNmcHdlUnEtRUs0RUJ4SGlfdVpQY0oxUlR0OEJSclNxWGVzeUx5ME8xd3M?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
