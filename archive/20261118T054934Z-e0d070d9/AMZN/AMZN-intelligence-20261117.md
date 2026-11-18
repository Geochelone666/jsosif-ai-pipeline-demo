# AMZN Intelligence Report

- ticker: **AMZN**
- Report as_of: **2026-11-17**
- Market data as_of: **2026-11-17**
- Quant sources: https://finance.yahoo.com/quote/AMZN/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AMZN/key-statistics/
- AI analysis snapshot as_of: **2026-11-17**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-18T06:09:04.744513+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 23, 'rule': 3, 'ai': 13, 'unknown': 0, 'irrelevant': 7})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **4** exact headline/source/date matches; prior report **20261117T062519Z-6171f6c2/AMZN** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'low_uncalibrated_model_confidence': 2}
- RSS source audit (metadata only, not article fact-checking): 23 unique headlines; 10 named publishers; 2 exact duplicates; 23 HTTPS source links; largest publisher share 26.09%; oldest publication 2026-11-12

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 257.8900 |
| Return 1D (%) | 0.0543 |
| Return 1W (%) | -4.7920 |
| Return 1M (%) | 3.1560 |
| Return YTD (%) | 11.7278 |
| Return 1Y (%) | 10.7442 |
| Annualized volatility (%) | 34.0233 |
| Beta vs SPY | 1.3235 |
| Max drawdown (%) | -19.6419 |
| Sharpe (rf=0) | 0.4675 |
| Downside deviation (rf=0, %) | 21.0490 |
| Sortino (rf=0) | 0.7556 |
| Historical VaR 95% (1D, %) | 3.0783 |
| Historical ES 95% (1D, %) | 4.0960 |
| Correlation vs SPY | 0.5361 |
| Tracking error vs SPY (%) | 29.0652 |
| P/E (trailing) | 20.83 |
| P/B | 4.54 |
| EV/EBITDA | 16.22 |
| Revenue growth (%) | 12.10 |
| Forward P/E (estimate) | 23.60 |
| Gross margin (%) | 51.37 |
| Operating margin (%) | 13.09 |
| Return on equity (%) | 27.42 |
| Free cash flow yield (%) | -1.25 |
| MA50 | 254.8148 |
| Close vs MA50 (%) | 1.2068 |
| MA200 | 244.7624 |
| Close vs MA200 (%) | 5.3634 |
| RSI (14, Wilder) | 49.7454 |
| MACD (12,26) | 2.4315 |
| MACD signal (9) | 2.1043 |
| MACD histogram | 0.3272 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AMZN': 284, 'SPY': 284}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 257.8900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.0543 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -4.7920 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 3.1560 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 11.7278 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 10.7442 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 34.0233 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 21.0490 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.7556 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.0783 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.0960 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5361 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 29.0652 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.3235 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -19.6419 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.4675 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 23.6032 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 51.3740 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 13.0870 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 27.4160 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: -1.2455 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 20.8312 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 49.7454 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.3272 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 1.2068 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 5.3634 -> Clearly above the moving-average trend level.

## TAILWINDS

### Amazon (AMZN) Is Building Its Own Answer to NVIDIA. Here’s How It’s Going
- Summary: Amazon is developing its own AI hardware to compete with NVIDIA, signaling innovation and potential market expansion.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxPWTZXSmptWXNhdDBlVUZFN2xDRE4xdzI2TDJ2b1NrN0paY0dyY2dUNFBKUUJHdi1zbnVyX0lGYm1teVI4ZEJXZU1sa1IwVjBnbTRld3JZd1FVVE9CYVIzOE9UNDI0Z0Vrb2doRFd4UGdkMUpJMGhjY3NWU1FzUW5IZzBVODBpdHU0NjltYmpPM18tekNTNGVJQ3FWcw?oc=5>

### Amazon makes major investments in renewable energy projects in India (AMZN:NASDAQ)
- Summary: Amazon is investing heavily in renewable energy projects in India, supporting sustainability and reducing operational costs.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxPTkpLSzFzQVZ5V0xHYmhnVE5HSU1fMEZ5SVZjc2ZTLThtWHFfMDI3dWNiNkl5emt2TnhoUVRZd0dzM0ROS2VpWmxpcGw2SC1HQm5CVVNqUUhZRlFjLTFGb0FTN2VKUTMyODd5X3hfVzBjWmxieTB6NjE3c1QwMWVmYU05WnNzR0g3eEctY3RUMENMdERlYVdMUzZERm5wRzVjaDlvMTRxSGljQQ?oc=5>

### Amazon looks to take a bigger bite out of the food delivery market (AMZN:NASDAQ)
- Summary: Amazon plans to expand its food delivery services, aiming to capture a larger share of the market.
- Date: 2026-11-17 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxPOUpacmFTc2V0a2tyZ1AwUjBtUHlLczh1NDc5WnBvSW5vU1owWVlkTXRVdFlTQlBsWXN5NExwRFluS3hWUzMyT0N4VWNIWUF3aVZZZ0xwSGJsT1hNRGhkSk0wbWQtUy1jeUJ1T2VqdFkwRThUcXUtSUZvSm1TN2J5aXBtbTdFVjRZUEk5T1VlMFdITm5jMFphTzhZdTB6NVRfSUlNRWhYUQ?oc=5>

### Amazon Cranks Up Its India Clean Energy Investment With Fresh $7 Billion Bet
- Summary: Amazon is increasing its clean energy investment in India with a new $7 billion commitment.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMizgFBVV95cUxOYTVRLVBIMzJZaVFPWVh6SlFDUXFwcUM3Z0JZVEYyM2ozbWdnUlBpNThUVkI2RnRoQWktUTg1c0tQcUdaM2tBcTR2Vk5rVm1DS1lPRkE5OUJwR0IwMWUwOHBlcng0dUxMcXpNdmF5OGlWRWhBaWpPRDVkbmZIa0ZSdjBIMnpKczZWZlFLUWx4OFY0bTF5YnBxeDZ4WHZHM0h0RXRDU1JIblZmbE5lMG93c0RGOVlmek1vNkFVMWNyY2pFWlNqT1pSWUY0THZsZw?oc=5>

### What Will Drive Amazon.com (NASDAQ:AMZN) Stock Performance Ahead?
- Summary: Analysis of factors likely to influence Amazon's stock performance in the near term.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxOSDU1MmczN0tfVC01aHNRSUN1ejV4R0xYcUpYeUpIdFBrWmFfbE1JVXJuU1haODhnS0NoZWJWeWp3Q2pjMEVxQWpidDJDamVoMkx1NW81SkVTYkZrTWRoWlNaX1pWb21mOVJQQmN6ZDVnTkt3WHZMSDlBQzhOVnhRNmNvWW8yX09GanROOTVtek5XeHFJeERMZllwVUNnb0lCcFRXaHhiTnJNNFdKRnN3YjdkVkI?oc=5>

### Amazon (AMZN) director Brad D. Smith converts a stock award into shares held in trust.
- Summary: Director Brad D. Smith converted a stock award into shares held in trust, increasing his ownership stake.
- Date: 2026-11-17 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxPWjFzaW1wa2JNazMzN2xTU2pQQjVRMTZtZ094aXdMYVIyX0VFU0tZdzFsX3dzd3JKX2daV2hmcnJIV2ptZlRkV3Nxa2R2WFlhaE02RnoxMUpQYmRDeWZ3bWpZS21tZHVFTlIydXNPbjItREp5VUNTV3NYaTRuam1UOEQ0VnUxSEstb1loNDlHSmtENTFUX291RUtZbnNmVW5ic1lyU1BnUkYydElv?oc=5>

### Amazon (AMZN) director Edith W. Cooper holds 10,264 shares after stock award conversion.
- Summary: Director Edith W. Cooper now holds 10,264 shares following a stock award conversion.
- Date: 2026-11-17 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxNUnJyOEI4MXdFUGRmM3BoQl9paTVFZ0p4QnlGUHM1NWJQSENKRXpad3ViblJsdnBSZ0dha0RYTzdRLWhMOVJQeDhKZ3lMVmdvZ1doYnUxNVN2VHFHYXJpTmZPVjlKMXZOSlJIY09CLVBoVV9DcHU1VDNSRVFSQjZlV2JSd09QZHVRaUFyTGhMMzJFTzZYanVNNEc0VGUwOW5vZjVDRnpkeDRHU0Zv?oc=5>

### Amazon (AMZN) director Daniel P. Huttenlocher holds 27,713 shares after stock award conversion.
- Summary: Director Daniel P. Huttenlocher holds 27,713 shares after converting a stock award.
- Date: 2026-11-17 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxNcGV4Nkl3UjNXUl9kaXl1SGhwQTZCNk15Q3BFVG9WZG9zTEVtN3BiZG1ZYW91Y0NRTHVuRlJVenQwRndsamZvS3JVaVh4Mk5SdkVTTW83cTgzR0twR21XT0FFYWNnM0UtUkVPMlpDak1LYlhlSzNSaWhhMVhlVWI5X3lhUWRmQ1hNWWZTUHRJOTdhdm12OG1YT2tiVVFWYnlYeE9tM0xiLXQzS2Ru?oc=5>

### Amazon (AMZN) director holds 55,204 shares after converting a stock award.
- Summary: Director holds 55,204 shares following a stock award conversion, increasing ownership.
- Date: 2026-11-17 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxONk1Vcl95Z3pLck1YMFJsN3JUdTMzWkwyV2dpbmVLV2dSbXp2Y3ExT0hHMktkYnc3YkVYUU8wN2dEZnktNTZacFpkWXZ4WkthbVRMaXctdHRfQVBrYnppVUFCb3JYRGdzVjlaeDlmMHk5anNtNFlVbWJteFFDcXdPWmZZN2R2Y1RQQVlaVDVuT0NoM2gzUk92bzBKMVUxQ2paYndkRU1VN0RkeGpl?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Amazon (AMZN) Has Its First Binding Union Contract In North America
- Summary: Amazon (AMZN) Has Its First Binding Union Contract In North America
- Date: 2026-11-14 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxORjJSY19uVEtwcExrMnJnbUlhRWVRWWF3Mm42VkRLbk5HdGxOeXh1U0VTb1d4dF94dDZXT2tHbDVXSi1JYnVpM0dvaEw1dkVwOFdjRUtyR2lISTF1S1pHNW95R1VXeEtiOFJoZ1FLV0Y2akZ6Z2FPNGk5UHdCUmdOMFN3TGFfVnpwQno5YVVsVktGQk9aQWZLTm0xeWU?oc=5>

### Amazon's AWS Strikes $5B Data Center Deal With Blackstone Digital — A Look At Some Key Highlights
- Summary: Amazon's AWS Strikes $5B Data Center Deal With Blackstone Digital — A Look At Some Key Highlights
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxPcFRWN0I0NVFPbC03RXNNTzdjLTg0RkFSM2dSVDNQOWJUSnA5NVl6SFRmLTRCMEVJVm5HeUFrZkxzb1JkZ21MT1dsb2V6b2RFYzZJR0drS0VpcFdBV1ZBZTBJcEtvT0E3MVZNSDYydWNTUEVRb2M4THo2bFlpdEF5eXU5UGJjSTJCVEFpWkROcjRkNFE?oc=5>

### Amazon Has Quietly Recouped Its Post Q3 Earnings Losses. AMZN Stock Could Hit $300 Next.
- Summary: Amazon Has Quietly Recouped Its Post Q3 Earnings Losses. AMZN Stock Could Hit $300 Next.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiyAFBVV95cUxNVDFMMWpzTHFWNVpraFphOVZad0Rza2psdnFrb3UwU2FES3JEZ2VaNHNudE80T2NOejIwTDJUaXJBMFdFSzNQZjFNYXZmc2tucTlPUXFobVpRLUJva2lGb0ItbVR1SkktLWhuaXRaUDA2VVV5SlJpSE5zaldBd19fSE5LNDFRbWZuLUZNT3l4VkRtTVRjRFIwNy15ZzdNWXZSSkg2TVFtUmN6Y2ZwbF9oaFJoby1ORER1UmRXVkNhQjRVaTF6b3dqMg?oc=5>

### What Could Lift Amazon Stock From Here?
- Summary: Speculative piece on factors that could boost Amazon's stock performance.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.5
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxPdnhpdEhzanE4RkFZb3FsR1hjYl93aktwY3hjV0NCQ1EtQzBBbDRMSzgzYjZoVEdKS2c1ZWU0RTRoMVd5Si1pSlR5R0VaOXQwRVByX1YzdUhLV1djN2ZoSmF1OTAycm5kanF1Y014ZXBSbVp0Q3Nqd0RmWjdJaEFtM3ptUDZsT25temNOTEY3YncxMU1SOHpzSU5fU0JNbjRT?oc=5>

### Amazon (AMZN) executive converts 9,352 stock awards and sells shares under a trading plan.
- Summary: Amazon executive converts awards and sells shares under a trading plan, indicating a stock move.
- Date: 2026-11-17 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxQTWlPWkxpNnZjNVFhSzVOWXFmYjIyQ2dPVGxFWHpINXFucm80WGhTbzdIdS1zYkktdG8zTW9jLWVQNjBXUW5acmd4ekdaa0lialdnTEloNWszOENBWk1qTFdyNlZqT0d0VjFETm1IOHdCTWhYdW5rSVp5bWxaOG9zRjlVemR1M0VTZVE3b19zcXNQTl9BNGRXaUc3aTRIU3FFLTdjRnQxS3hTTHhk?oc=5>

### Anthropic’s New IPO Filing Shows Amazon, Google Will Own Over A Quarter Of The Claude Maker
- Summary: Amazon will own over 25% of Anthropic after its IPO filing, indicating a significant partnership and potential AI collaboration.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxNWnBIQWE0a2JUME11UzNpeTZUa0lqOEg0aFNMT05BV29YVldtdzNISHM1OWtrdHZsYkRHc2xTZmFjekh4dTltVEpROVRsZlFjcW8xR21QZ2t2aXpNcHNpb2QyU0lkdU5aZXV6bFVkdXNES09NRnh2MHJTeER1R2hud3o1UWdkSmR5ZnZoQmpRQjhvQk5nTlZtVnBMS1FGUDA?oc=5>

## RISKS

### Amazon: The Age Of Inference (And Big E-Commerce Profits) (NASDAQ:AMZN)
- Summary: Amazon's inference tech promises growth but may face execution risk.
- Date: 2026-11-16 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxNQnRLX2xlM3NNZ3ctbTl3OF9OdlRwYktiRHBTeUN1bjZNRG0yTFBYaGw5OTdaVXRHcEVrMWt6WlRJWXpLT05xVEJoSFJnUEgxSDg0R1pmYXFMMWlYX2U2QU5kWlZtTUx0eWpWVjFxSnNaNWhRS0tIWUdOUkRkZk5td2dRanFxR1ZyNklUS2hpUXJKS1hT?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AMZN** | **20.83** | **4.54** | **16.22** | **12.10** | **2,788,600,315,904.00 USD** | **10.74** |
| WMT | 46.20 | 10.31 | 24.55 | 5.90 | 1,014,814,212,096.00 USD | 24.91 |
| MSFT | 26.42 | 7.99 | 18.61 | 18.80 | 3,759,436,726,272.00 USD | 0.57 |
| GOOGL | 14.82 | 5.22 | 18.05 | 24.70 | 3,444,778,729,472.00 USD | -1.44 |

Peers fetched as_of: 2026-11-17; AMZN reuses existing data (market data as_of: 2026-11-17); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-29
- Next expected earnings: 2027-02-04 (yfinance; expected dates may change)

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
- Filing date: 2026-10-30
- Revenue (latest available single quarter): 201,944,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 20,685,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMimwFBVV95cUxPWTZXSmptWXNhdDBlVUZFN2xDRE4xdzI2TDJ2b1NrN0paY0dyY2dUNFBKUUJHdi1zbnVyX0lGYm1teVI4ZEJXZU1sa1IwVjBnbTRld3JZd1FVVE9CYVIzOE9UNDI0Z0Vrb2doRFd4UGdkMUpJMGhjY3NWU1FzUW5IZzBVODBpdHU0NjltYmpPM18tekNTNGVJQ3FWcw?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxPTkpLSzFzQVZ5V0xHYmhnVE5HSU1fMEZ5SVZjc2ZTLThtWHFfMDI3dWNiNkl5emt2TnhoUVRZd0dzM0ROS2VpWmxpcGw2SC1HQm5CVVNqUUhZRlFjLTFGb0FTN2VKUTMyODd5X3hfVzBjWmxieTB6NjE3c1QwMWVmYU05WnNzR0g3eEctY3RUMENMdERlYVdMUzZERm5wRzVjaDlvMTRxSGljQQ?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxPOUpacmFTc2V0a2tyZ1AwUjBtUHlLczh1NDc5WnBvSW5vU1owWVlkTXRVdFlTQlBsWXN5NExwRFluS3hWUzMyT0N4VWNIWUF3aVZZZ0xwSGJsT1hNRGhkSk0wbWQtUy1jeUJ1T2VqdFkwRThUcXUtSUZvSm1TN2J5aXBtbTdFVjRZUEk5T1VlMFdITm5jMFphTzhZdTB6NVRfSUlNRWhYUQ?oc=5
- https://news.google.com/rss/articles/CBMizgFBVV95cUxOYTVRLVBIMzJZaVFPWVh6SlFDUXFwcUM3Z0JZVEYyM2ozbWdnUlBpNThUVkI2RnRoQWktUTg1c0tQcUdaM2tBcTR2Vk5rVm1DS1lPRkE5OUJwR0IwMWUwOHBlcng0dUxMcXpNdmF5OGlWRWhBaWpPRDVkbmZIa0ZSdjBIMnpKczZWZlFLUWx4OFY0bTF5YnBxeDZ4WHZHM0h0RXRDU1JIblZmbE5lMG93c0RGOVlmek1vNkFVMWNyY2pFWlNqT1pSWUY0THZsZw?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxOSDU1MmczN0tfVC01aHNRSUN1ejV4R0xYcUpYeUpIdFBrWmFfbE1JVXJuU1haODhnS0NoZWJWeWp3Q2pjMEVxQWpidDJDamVoMkx1NW81SkVTYkZrTWRoWlNaX1pWb21mOVJQQmN6ZDVnTkt3WHZMSDlBQzhOVnhRNmNvWW8yX09GanROOTVtek5XeHFJeERMZllwVUNnb0lCcFRXaHhiTnJNNFdKRnN3YjdkVkI?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxPWjFzaW1wa2JNazMzN2xTU2pQQjVRMTZtZ094aXdMYVIyX0VFU0tZdzFsX3dzd3JKX2daV2hmcnJIV2ptZlRkV3Nxa2R2WFlhaE02RnoxMUpQYmRDeWZ3bWpZS21tZHVFTlIydXNPbjItREp5VUNTV3NYaTRuam1UOEQ0VnUxSEstb1loNDlHSmtENTFUX291RUtZbnNmVW5ic1lyU1BnUkYydElv?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxNUnJyOEI4MXdFUGRmM3BoQl9paTVFZ0p4QnlGUHM1NWJQSENKRXpad3ViblJsdnBSZ0dha0RYTzdRLWhMOVJQeDhKZ3lMVmdvZ1doYnUxNVN2VHFHYXJpTmZPVjlKMXZOSlJIY09CLVBoVV9DcHU1VDNSRVFSQjZlV2JSd09QZHVRaUFyTGhMMzJFTzZYanVNNEc0VGUwOW5vZjVDRnpkeDRHU0Zv?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxNcGV4Nkl3UjNXUl9kaXl1SGhwQTZCNk15Q3BFVG9WZG9zTEVtN3BiZG1ZYW91Y0NRTHVuRlJVenQwRndsamZvS3JVaVh4Mk5SdkVTTW83cTgzR0twR21XT0FFYWNnM0UtUkVPMlpDak1LYlhlSzNSaWhhMVhlVWI5X3lhUWRmQ1hNWWZTUHRJOTdhdm12OG1YT2tiVVFWYnlYeE9tM0xiLXQzS2Ru?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxONk1Vcl95Z3pLck1YMFJsN3JUdTMzWkwyV2dpbmVLV2dSbXp2Y3ExT0hHMktkYnc3YkVYUU8wN2dEZnktNTZacFpkWXZ4WkthbVRMaXctdHRfQVBrYnppVUFCb3JYRGdzVjlaeDlmMHk5anNtNFlVbWJteFFDcXdPWmZZN2R2Y1RQQVlaVDVuT0NoM2gzUk92bzBKMVUxQ2paYndkRU1VN0RkeGpl?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxORjJSY19uVEtwcExrMnJnbUlhRWVRWWF3Mm42VkRLbk5HdGxOeXh1U0VTb1d4dF94dDZXT2tHbDVXSi1JYnVpM0dvaEw1dkVwOFdjRUtyR2lISTF1S1pHNW95R1VXeEtiOFJoZ1FLV0Y2akZ6Z2FPNGk5UHdCUmdOMFN3TGFfVnpwQno5YVVsVktGQk9aQWZLTm0xeWU?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxPcFRWN0I0NVFPbC03RXNNTzdjLTg0RkFSM2dSVDNQOWJUSnA5NVl6SFRmLTRCMEVJVm5HeUFrZkxzb1JkZ21MT1dsb2V6b2RFYzZJR0drS0VpcFdBV1ZBZTBJcEtvT0E3MVZNSDYydWNTUEVRb2M4THo2bFlpdEF5eXU5UGJjSTJCVEFpWkROcjRkNFE?oc=5
- https://news.google.com/rss/articles/CBMiyAFBVV95cUxNVDFMMWpzTHFWNVpraFphOVZad0Rza2psdnFrb3UwU2FES3JEZ2VaNHNudE80T2NOejIwTDJUaXJBMFdFSzNQZjFNYXZmc2tucTlPUXFobVpRLUJva2lGb0ItbVR1SkktLWhuaXRaUDA2VVV5SlJpSE5zaldBd19fSE5LNDFRbWZuLUZNT3l4VkRtTVRjRFIwNy15ZzdNWXZSSkg2TVFtUmN6Y2ZwbF9oaFJoby1ORER1UmRXVkNhQjRVaTF6b3dqMg?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxPdnhpdEhzanE4RkFZb3FsR1hjYl93aktwY3hjV0NCQ1EtQzBBbDRMSzgzYjZoVEdKS2c1ZWU0RTRoMVd5Si1pSlR5R0VaOXQwRVByX1YzdUhLV1djN2ZoSmF1OTAycm5kanF1Y014ZXBSbVp0Q3Nqd0RmWjdJaEFtM3ptUDZsT25temNOTEY3YncxMU1SOHpzSU5fU0JNbjRT?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxQTWlPWkxpNnZjNVFhSzVOWXFmYjIyQ2dPVGxFWHpINXFucm80WGhTbzdIdS1zYkktdG8zTW9jLWVQNjBXUW5acmd4ekdaa0lialdnTEloNWszOENBWk1qTFdyNlZqT0d0VjFETm1IOHdCTWhYdW5rSVp5bWxaOG9zRjlVemR1M0VTZVE3b19zcXNQTl9BNGRXaUc3aTRIU3FFLTdjRnQxS3hTTHhk?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxNWnBIQWE0a2JUME11UzNpeTZUa0lqOEg0aFNMT05BV29YVldtdzNISHM1OWtrdHZsYkRHc2xTZmFjekh4dTltVEpROVRsZlFjcW8xR21QZ2t2aXpNcHNpb2QyU0lkdU5aZXV6bFVkdXNES09NRnh2MHJTeER1R2hud3o1UWdkSmR5ZnZoQmpRQjhvQk5nTlZtVnBMS1FGUDA?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxNQnRLX2xlM3NNZ3ctbTl3OF9OdlRwYktiRHBTeUN1bjZNRG0yTFBYaGw5OTdaVXRHcEVrMWt6WlRJWXpLT05xVEJoSFJnUEgxSDg0R1pmYXFMMWlYX2U2QU5kWlZtTUx0eWpWVjFxSnNaNWhRS0tIWUdOUkRkZk5td2dRanFxR1ZyNklUS2hpUXJKS1hT?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
