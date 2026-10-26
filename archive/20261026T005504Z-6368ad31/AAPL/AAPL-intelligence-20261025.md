# AAPL Intelligence Report

- ticker: **AAPL**
- Report as_of: **2026-10-25**
- Market data as_of: **2026-10-23**
- Quant sources: https://finance.yahoo.com/quote/AAPL/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AAPL/key-statistics/
- AI analysis snapshot as_of: **2026-10-25**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-26T01:08:46.300807+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 6, 'ai': 10, 'unknown': 0, 'irrelevant': 8})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **0** exact headline/source/date matches; prior report **N/A** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **3**; {'low_uncalibrated_model_confidence': 2, 'short_term_price_move_in_structural_risks': 1}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 12 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 29.17%; oldest publication 2026-10-19

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 347.7300 |
| Return 1D (%) | -0.1407 |
| Return 1W (%) | 1.2432 |
| Return 1M (%) | 3.1779 |
| Return YTD (%) | 28.2559 |
| Return 1Y (%) | 34.4535 |
| Annualized volatility (%) | 24.0631 |
| Beta vs SPY | 0.5780 |
| Max drawdown (%) | -13.7985 |
| Sharpe (rf=0) | 1.3564 |
| Downside deviation (rf=0, %) | 16.5679 |
| Sortino (rf=0) | 1.9700 |
| Historical VaR 95% (1D, %) | 2.0034 |
| Historical ES 95% (1D, %) | 3.4742 |
| Correlation vs SPY | 0.3062 |
| Tracking error vs SPY (%) | 23.5305 |
| P/E (trailing) | 39.88 |
| P/B | 47.25 |
| EV/EBITDA | 30.34 |
| Revenue growth (%) | 16.40 |
| Forward P/E (estimate) | 36.37 |
| Gross margin (%) | 48.65 |
| Operating margin (%) | 32.62 |
| Return on equity (%) | 148.75 |
| Free cash flow yield (%) | 2.12 |
| MA50 | 329.4668 |
| Close vs MA50 (%) | 5.5433 |
| MA200 | 294.1080 |
| Close vs MA200 (%) | 18.2321 |
| RSI (14, Wilder) | 63.9280 |
| MACD (12,26) | 4.3746 |
| MACD signal (9) | 4.0603 |
| MACD histogram | 0.3143 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AAPL': 267, 'SPY': 267}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 347.7300 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.1407 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 1.2432 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 3.1779 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 28.2559 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 34.4535 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 24.0631 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 16.5679 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.9700 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.0034 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.4742 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.3062 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 23.5305 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.5780 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -13.7985 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.3564 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 36.3655 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 48.6530 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 32.6230 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 148.7510 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.1227 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 39.8767 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 63.9280 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.3143 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 5.5433 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 18.2321 -> Clearly above the moving-average trend level.

## TAILWINDS

### Apple tops Nvidia to become world's most valuable company (AAPL:NASDAQ)
- Summary: Apple surpasses Nvidia, becoming the world's most valuable company, boosting investor confidence and market perception.
- Date: 2026-10-23 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxQXy1LUVY5N2YyajY5UkU5TFllTjZEV21qLWZXUkxiWW9VNGE3LXNFMWhuMFhDVXhHSkwyNVN4OFQxNVdLLWxFaTlrbDl4WW9NeE9yS2VvaUxrMHNyYklERGF2Q2NKLUpjaDQzYlpBMjlja3pHR01ac0hsaHYtb0I3SENoVmNPNVYtM3FvZ0NNZFhBMVlYQldBRld3?oc=5>

### Billionaire Ken Fisher and Jim Cramer Still Like Apple (AAPL). Should You?
- Summary: Prominent investors Ken Fisher and Jim Cramer endorse Apple, signaling strong analyst support.
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxNY3JUbWpTS29yaXBSMVRxZjM0bmttUDZLZzVTWFhjU1hLWHJhWGtEWVl1T1JJUjdEeXZrb05rUFpzWTVMR1JHWjd3TFphWTFlQ25OWWtQSm5Udk42R2NlNnFFcEM3azNRNllGNnQxNWJKb2U1S3I0ZzFfZTkyYkp5UWw2c3ZWa0IydzRKaGpLVEJCbzU5XzJzbzVIUGxyY3M?oc=5>

### Deep Hardware-Software Integration Drives Apple’s (AAPL) Underappreciated AI Advantage
- Summary: Apple's integrated hardware-software design enhances its AI capabilities, strengthening competitive edge.
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxPdVFKSGptT2FQdzNFbzBvTDVGSnF5MkF3UC05Q3FjbjlrVE16UnRKS3VWTzNWUHpOcEU2eTRSemtaT19GMHBWTEV3MzBQYW1rcXdUU041dGFld0ZFUXBldU1Gak1vbEJ4ZlZRQW12NnZHQjJlYVU5QkphTW1tREVpaWdmT2ZVSGlyY2lrS0dMblNYUVRwWjlFRzduWFRZT1k2Umk0UVlIODU4dw?oc=5>

### Prediction: Apple Will Soar After Oct. 28
- Summary: Analysts predict a significant rise in Apple shares post-October 28.
- Date: 2026-10-21 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxQWGZqMXY5QXhtakJNOWFxQlg1VHl0QTlSMnppelN6cXAwVHA2cUFtUl95TkdBS3ZOaURZblI2bGZzeWpRNGVOdjhBV1hFUU92eUpXcHJVZ043NkhqN1FZVlhvVkhFMDM1Q01Hc3ZaR1RkcWQ1NVRxR0VkZDRmYmNrS3pYRld0dkpoV0E?oc=5>

### Apple Stock Could Have Another Major Growth Chapter Ahead
- Summary: Forecasts suggest Apple may enter a new growth phase.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxOcVF1N2VhaVZ5QkExSFUtaHpvTXhjekdWODYtUGFFWm9YcTVyS1lmNjFHaUVaWE9FR0ZrYzJUZ2hwTFduNkxvcDdQVDJiNWNBQVlveGdVVzVSaTgyTGdDdlFZamJ3dWRxLXdlTG00aGtmaXF6eldwRzVZNksyMDRVZmdNYmVYZFkzT1Y4TEloaUZtTDQ3ZGdWcTZWZ3Q?oc=5>

## HEADWINDS

### Apple Stock Downgraded As Analysts Turn Cautious On iPhone Maker
- Summary: Apple Stock Downgraded As Analysts Turn Cautious On iPhone Maker
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxOSzNXYWVVQlFPQUdlNE03Q3FDenFiVUNQTlB4M1RmX05pRzJwQXVrX0ZwUmRMZncxY1hqOWpHUHVmUzFva1cyb3A3bGN6OWZQMW01N2JvLTR6SzN3UTFBdFlES1dIMnpBOWNuZnZ1Y2NMSEFhVW9VQ29VOXc1TzBWRnJhZjBXT0xoWGcxb1hhbGxfSHhyUW1VbmVHZkRSdmVVMWI0Yi1XM0R3SDQ?oc=5>

## CATALYSTS

### Apple (NASDAQ:AAPL) Stock Hits Record US$351.73 as iPhone Duo Production Target Reportedly Jumps 44%
- Summary: Apple (NASDAQ:AAPL) Stock Hits Record US$351.73 as iPhone Duo Production Target Reportedly Jumps 44%
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiekFVX3lxTE42YWZvT3p4TXJERy1HVHRZTTROeWlHWURrY3VnV25CTFpFcTJ4dndMSXR3b3owTW9rTy14eXFTLXNFOGtaV2h3MzFKaFYwMkpJWWV4WnpLaG1iTjI0U0ZMYmtnNTRvUEZIZnhfbnZ3Y01aeHBaUmNlSGJn?oc=5>

### Apple Stock Hits Record High On iPhone Duo Launch
- Summary: Apple Stock Hits Record High On iPhone Duo Launch
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxNdUltNURaQjNjcmctdzRVNGdxX3ZWbmE0ejVOc0c3aXFjQVUzVC14VURDMGRKQzViUzFQdlV1Z3hOQy1sZTJNdkVrWDFxOC0zSXlTalJyQW1TbVdhYVRQRFU3UmxCREFPdWlHbzRxOEg3T1BRMTh5cGxPRk00d3VualFvbnhhOEFaYkIwVTRsRUtNRlZobjdz?oc=5>

### Apple in focus as Wedbush sees 'strong' demand for iPhone Duo (AAPL:NASDAQ)
- Summary: Apple in focus as Wedbush sees 'strong' demand for iPhone Duo (AAPL:NASDAQ)
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxQQTluNzctU0h1eHNIUEl6eHNLdnBRSVRuTk5nMlpLSldGVk9hUXVReEN1TThXOEN5LWdqUnBtWWR0Q0V6QXFvbnl1VXdKSkhpQWthc3RReXJnTkRpWmZEYm02YTJqXzFzMmpPRTJnS3pLa2prLUdvLTVTdnBRYTBReDRXLXNRSUJoMWFISU5wclR5ZXN4Y3pSUXhJSkZZdw?oc=5>

### Apple Inc. $AAPL Stock Sold by Navigate Wealth Management LLC
- Summary: Apple Inc. $AAPL Stock Sold by Navigate Wealth Management LLC
- Date: 2026-10-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxOdC0wckQ0aDVmcXZnX1BPTDFuOVE4QmFOUVFPTFJna0hwRnBKaTFYTUZRYnVqbjljU0dtQkd6YThDTkFXc3Q3TDdsdm5FN2tqbzk0ek5va1hBOW1kTmtfemJueGJvY2xpMVE1WkdKVFlKQnU4d0ZIQWlNWk9BNEZ1UWItZG41a1EtTHAyN2JrWXN1dy04c25Ra1JxR05zQVBQMWVwdHVvRHl1S2ZyVUtsVmtDaUh4QW11ZG5KUQ?oc=5>

### AAPL Stock Hits Record High As Apple Tops Nvidia Market Cap Amid iPhone Duo Debut
- Summary: AAPL Stock Hits Record High As Apple Tops Nvidia Market Cap Amid iPhone Duo Debut
- Date: 2026-10-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi9AFBVV95cUxPTDNJSXExelJGYWlmWmw1OVdUaHdiYlY1c0dpSi1QZjg4UFFkZ2lFSUxwdUZsQTVMSWwtMDREM1YtWlp0MFV1Uy1UMXliLThGU2lkdFFfRWNCTDZTUExSX0Z6SWxxWUdnTnVSM2cxek9uRXVIZTV6WlpOcXdweTJYSUsyZFNnTXBBdWN4MHdhNTVMaXBHUks1TWtsU0cxM2swRHQ0WTRORjYzNkd2TmE2cFYzQ2M4ZmE0czhMNDZBV1R1MG5KTmx4RXRrUXV5UVg5RmFlcXM0c1o3NDhKdWF0a3AyVGdoaGpVWlBQSnlCVW1NbGJz?oc=5>

### Will Apple (AAPL) Change Macs With Its First Touchscreen MacBook Pro?
- Summary: Speculation that Apple may introduce a touchscreen MacBook Pro, potentially expanding its product line.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxObUJBZXJ6TTZfbDg4S0IxTnhqOHRsSlc0QjczUGlrMkZxYWFMWExrTHBrN1hxQXI1STNNX0lyZmwwN3FqaUI1Zm5iQUNsbGJnYlFQN1NGSEkxdFk0ZS1BOHN6akZVVXNEMEk3R2ZrT2VLR3RHODhVQjVqR3ZCVGpBT0FqeVVrTWFoMThkQkp6R3FmVnFpRVk3Ng?oc=5>

### What Is Apple (AAPL) Telling The Market With Its Biggest Smart Home Push?
- Summary: Apple’s major smart home initiative could signal a strategic shift toward home ecosystem services.
- Date: 2026-10-19 | Impact: medium | Horizon: short | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxQYjFEeTJjUEtTNVo1bTNWN2ZKMVVFQllsNVNxcll2RkV4MndkcW0yRk1TaDYzVE5OeFJxWmtkUUpVa1ZwUG5tbEI0T3JRUzNiVkxmaVpvYTlMamVwRHBFMHQ1REUxOFJMcjR0d3VQTEw5NDQ0ZURnM0NjRVFhNXB2SkVpMklreFJXX0NvSDljVktYM2pyZ0d5OUtiYnFmQQ?oc=5>

### How much Apple stock does former CEO Tim Cook actually own?
- Summary: Details on Tim Cook’s current Apple share ownership, indicating personal investment level.
- Date: 2026-10-23 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxQd1Q5cm02a01vTUpTUGtWY1NhZG5KZ05jZm82US1FUmlLOE5qT2s5SEYwbU9ORF9FOVQxUGJFejJXZ2NvSUo2VkxTSENXR0xUYVlDd1NZWWVmOVEwTjQtd1RZRmxnZ08wWWZ5Y19vSVBoY0V6c202Yk9xRVF1MElzRVQ4UWFmaXplZ0wwZDFR?oc=5>

### Apple: Buy-Rated Despite High Valuation, But Limited To A 3% Allocation (NASDAQ:AAPL)
- Summary: Analyst upgrades Apple to buy, citing strong fundamentals but high valuation, limiting allocation to 3%.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxQelFsXzlpdXFxaDNiV2pHejBCZUxLTHU1UDIxOTg5S19mLWt2Z0JDd0FhanFBYkljUGR3azZLbmlHWkRpal9GcDVzWmQ5dnVQQlE0eXZSeXU2b0RYQms3V2VyODdXNmc3Mi0wNEhVZ09sd2RrdjNNenJ0SzdheEJRakQ2NmJvT0lENXp0eXBpVUZlMkVlOHBBSjVDbXpmelczYTlQVG95Q0ZfekxDbEM4VDE4bFVKSnpE?oc=5>

## RISKS

### Apple Stock Price Forecast: AAPL Continues Pullback After Record High, Will It Test $300 Again This Year?
- Summary: Forecast predicts continued pullback from record high, questioning $300 target, indicating potential downside pressure.
- Date: 2026-10-24 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxQYy16c1hoRlNmSWUyZ2FGNV92azg2ckFMLVp4RXdsRG9OSGE0WGVMdHJXZGlLZjNQcWNWQm9mZm9uRE84b0RpM0I4X2o1X0pTQzR0WnpwcTlSR1JHVmhrRng3d21vX0V0ZkJsYTl3dWtnLXhqaTBlS1hVTnp4TFV2dW1EYWg3OGpwQUROMm5Md3BqOEFhbnBpa0owNDF5QkpmVV9TdDdDa1NpdW5rdWlPNzI5eFJMakVWU0RLV3pqQndpQ1k?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AAPL** | **39.88** | **47.25** | **30.34** | **16.40** | **5,074,761,285,632.00 USD** | **34.45** |
| MSFT | 29.22 | 8.81 | 20.32 | 17.70 | 3,894,773,022,720.00 USD | 1.59 |
| GOOGL | 16.07 | 6.29 | 22.02 | 24.20 | 3,916,147,458,048.00 USD | 26.85 |
| SONY | 21.55 | 2.89 | 0.12 | 8.20 | 152,303,173,632.00 USD | -9.16 |

Peers fetched as_of: 2026-10-25; AAPL reuses existing data (market data as_of: 2026-10-23); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-07-30
- Next expected earnings: 2026-11-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-25

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-07-31
- Revenue (latest available single quarter): 62,900,000,000.00 USD; period 2018-07-01/2018-09-29; fiscal year/reporting period 2018/FY
- Net income (latest available single quarter): 29,789,000,000.00 USD; period 2026-03-29/2026-06-27; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/320193/000032019326000020/aapl-20260627.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMimgFBVV95cUxQXy1LUVY5N2YyajY5UkU5TFllTjZEV21qLWZXUkxiWW9VNGE3LXNFMWhuMFhDVXhHSkwyNVN4OFQxNVdLLWxFaTlrbDl4WW9NeE9yS2VvaUxrMHNyYklERGF2Q2NKLUpjaDQzYlpBMjlja3pHR01ac0hsaHYtb0I3SENoVmNPNVYtM3FvZ0NNZFhBMVlYQldBRld3?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxNY3JUbWpTS29yaXBSMVRxZjM0bmttUDZLZzVTWFhjU1hLWHJhWGtEWVl1T1JJUjdEeXZrb05rUFpzWTVMR1JHWjd3TFphWTFlQ25OWWtQSm5Udk42R2NlNnFFcEM3azNRNllGNnQxNWJKb2U1S3I0ZzFfZTkyYkp5UWw2c3ZWa0IydzRKaGpLVEJCbzU5XzJzbzVIUGxyY3M?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxPdVFKSGptT2FQdzNFbzBvTDVGSnF5MkF3UC05Q3FjbjlrVE16UnRKS3VWTzNWUHpOcEU2eTRSemtaT19GMHBWTEV3MzBQYW1rcXdUU041dGFld0ZFUXBldU1Gak1vbEJ4ZlZRQW12NnZHQjJlYVU5QkphTW1tREVpaWdmT2ZVSGlyY2lrS0dMblNYUVRwWjlFRzduWFRZT1k2Umk0UVlIODU4dw?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxQWGZqMXY5QXhtakJNOWFxQlg1VHl0QTlSMnppelN6cXAwVHA2cUFtUl95TkdBS3ZOaURZblI2bGZzeWpRNGVOdjhBV1hFUU92eUpXcHJVZ043NkhqN1FZVlhvVkhFMDM1Q01Hc3ZaR1RkcWQ1NVRxR0VkZDRmYmNrS3pYRld0dkpoV0E?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxOcVF1N2VhaVZ5QkExSFUtaHpvTXhjekdWODYtUGFFWm9YcTVyS1lmNjFHaUVaWE9FR0ZrYzJUZ2hwTFduNkxvcDdQVDJiNWNBQVlveGdVVzVSaTgyTGdDdlFZamJ3dWRxLXdlTG00aGtmaXF6eldwRzVZNksyMDRVZmdNYmVYZFkzT1Y4TEloaUZtTDQ3ZGdWcTZWZ3Q?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxOSzNXYWVVQlFPQUdlNE03Q3FDenFiVUNQTlB4M1RmX05pRzJwQXVrX0ZwUmRMZncxY1hqOWpHUHVmUzFva1cyb3A3bGN6OWZQMW01N2JvLTR6SzN3UTFBdFlES1dIMnpBOWNuZnZ1Y2NMSEFhVW9VQ29VOXc1TzBWRnJhZjBXT0xoWGcxb1hhbGxfSHhyUW1VbmVHZkRSdmVVMWI0Yi1XM0R3SDQ?oc=5
- https://news.google.com/rss/articles/CBMiekFVX3lxTE42YWZvT3p4TXJERy1HVHRZTTROeWlHWURrY3VnV25CTFpFcTJ4dndMSXR3b3owTW9rTy14eXFTLXNFOGtaV2h3MzFKaFYwMkpJWWV4WnpLaG1iTjI0U0ZMYmtnNTRvUEZIZnhfbnZ3Y01aeHBaUmNlSGJn?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxNdUltNURaQjNjcmctdzRVNGdxX3ZWbmE0ejVOc0c3aXFjQVUzVC14VURDMGRKQzViUzFQdlV1Z3hOQy1sZTJNdkVrWDFxOC0zSXlTalJyQW1TbVdhYVRQRFU3UmxCREFPdWlHbzRxOEg3T1BRMTh5cGxPRk00d3VualFvbnhhOEFaYkIwVTRsRUtNRlZobjdz?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxQQTluNzctU0h1eHNIUEl6eHNLdnBRSVRuTk5nMlpLSldGVk9hUXVReEN1TThXOEN5LWdqUnBtWWR0Q0V6QXFvbnl1VXdKSkhpQWthc3RReXJnTkRpWmZEYm02YTJqXzFzMmpPRTJnS3pLa2prLUdvLTVTdnBRYTBReDRXLXNRSUJoMWFISU5wclR5ZXN4Y3pSUXhJSkZZdw?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxOdC0wckQ0aDVmcXZnX1BPTDFuOVE4QmFOUVFPTFJna0hwRnBKaTFYTUZRYnVqbjljU0dtQkd6YThDTkFXc3Q3TDdsdm5FN2tqbzk0ek5va1hBOW1kTmtfemJueGJvY2xpMVE1WkdKVFlKQnU4d0ZIQWlNWk9BNEZ1UWItZG41a1EtTHAyN2JrWXN1dy04c25Ra1JxR05zQVBQMWVwdHVvRHl1S2ZyVUtsVmtDaUh4QW11ZG5KUQ?oc=5
- https://news.google.com/rss/articles/CBMi9AFBVV95cUxPTDNJSXExelJGYWlmWmw1OVdUaHdiYlY1c0dpSi1QZjg4UFFkZ2lFSUxwdUZsQTVMSWwtMDREM1YtWlp0MFV1Uy1UMXliLThGU2lkdFFfRWNCTDZTUExSX0Z6SWxxWUdnTnVSM2cxek9uRXVIZTV6WlpOcXdweTJYSUsyZFNnTXBBdWN4MHdhNTVMaXBHUks1TWtsU0cxM2swRHQ0WTRORjYzNkd2TmE2cFYzQ2M4ZmE0czhMNDZBV1R1MG5KTmx4RXRrUXV5UVg5RmFlcXM0c1o3NDhKdWF0a3AyVGdoaGpVWlBQSnlCVW1NbGJz?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxObUJBZXJ6TTZfbDg4S0IxTnhqOHRsSlc0QjczUGlrMkZxYWFMWExrTHBrN1hxQXI1STNNX0lyZmwwN3FqaUI1Zm5iQUNsbGJnYlFQN1NGSEkxdFk0ZS1BOHN6akZVVXNEMEk3R2ZrT2VLR3RHODhVQjVqR3ZCVGpBT0FqeVVrTWFoMThkQkp6R3FmVnFpRVk3Ng?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxQYjFEeTJjUEtTNVo1bTNWN2ZKMVVFQllsNVNxcll2RkV4MndkcW0yRk1TaDYzVE5OeFJxWmtkUUpVa1ZwUG5tbEI0T3JRUzNiVkxmaVpvYTlMamVwRHBFMHQ1REUxOFJMcjR0d3VQTEw5NDQ0ZURnM0NjRVFhNXB2SkVpMklreFJXX0NvSDljVktYM2pyZ0d5OUtiYnFmQQ?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxQd1Q5cm02a01vTUpTUGtWY1NhZG5KZ05jZm82US1FUmlLOE5qT2s5SEYwbU9ORF9FOVQxUGJFejJXZ2NvSUo2VkxTSENXR0xUYVlDd1NZWWVmOVEwTjQtd1RZRmxnZ08wWWZ5Y19vSVBoY0V6c202Yk9xRVF1MElzRVQ4UWFmaXplZ0wwZDFR?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxQelFsXzlpdXFxaDNiV2pHejBCZUxLTHU1UDIxOTg5S19mLWt2Z0JDd0FhanFBYkljUGR3azZLbmlHWkRpal9GcDVzWmQ5dnVQQlE0eXZSeXU2b0RYQms3V2VyODdXNmc3Mi0wNEhVZ09sd2RrdjNNenJ0SzdheEJRakQ2NmJvT0lENXp0eXBpVUZlMkVlOHBBSjVDbXpmelczYTlQVG95Q0ZfekxDbEM4VDE4bFVKSnpE?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxQYy16c1hoRlNmSWUyZ2FGNV92azg2ckFMLVp4RXdsRG9OSGE0WGVMdHJXZGlLZjNQcWNWQm9mZm9uRE84b0RpM0I4X2o1X0pTQzR0WnpwcTlSR1JHVmhrRng3d21vX0V0ZkJsYTl3dWtnLXhqaTBlS1hVTnp4TFV2dW1EYWg3OGpwQUROMm5Md3BqOEFhbnBpa0owNDF5QkpmVV9TdDdDa1NpdW5rdWlPNzI5eFJMakVWU0RLV3pqQndpQ1k?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
