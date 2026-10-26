# TSM Intelligence Report

- ticker: **TSM**
- Report as_of: **2026-10-25**
- Market data as_of: **2026-10-23**
- Quant sources: https://finance.yahoo.com/quote/TSM/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/TSM/key-statistics/
- AI analysis snapshot as_of: **2026-10-25**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-26T01:02:06.637191+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 23, 'rule': 4, 'ai': 13, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **0** exact headline/source/date matches; prior report **N/A** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 23 unique headlines; 5 named publishers; 2 exact duplicates; 23 HTTPS source links; largest publisher share 60.87%; oldest publication 2026-10-18

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 418.5100 |
| Return 1D (%) | 1.4939 |
| Return 1W (%) | 1.4299 |
| Return 1M (%) | -6.2834 |
| Return YTD (%) | 38.8005 |
| Return 1Y (%) | 45.4750 |
| Annualized volatility (%) | 39.1384 |
| Beta vs SPY | 2.1276 |
| Max drawdown (%) | -21.5466 |
| Sharpe (rf=0) | 1.1569 |
| Downside deviation (rf=0, %) | 26.0366 |
| Sortino (rf=0) | 1.7390 |
| Historical VaR 95% (1D, %) | 4.1383 |
| Historical ES 95% (1D, %) | 5.1216 |
| Correlation vs SPY | 0.6929 |
| Tracking error vs SPY (%) | 31.6685 |
| P/E (trailing) | 27.12 |
| P/B | 79.87 |
| EV/EBITDA | 3.92 |
| Revenue growth (%) | 50.90 |
| Forward P/E (estimate) | 17.90 |
| Gross margin (%) | 65.85 |
| Operating margin (%) | 58.66 |
| Return on equity (%) | 41.85 |
| Free cash flow yield (%) | N/A |
| MA50 | 433.6248 |
| Close vs MA50 (%) | -3.4857 |
| MA200 | 396.0506 |
| Close vs MA200 (%) | 5.6708 |
| RSI (14, Wilder) | 41.4593 |
| MACD (12,26) | -5.9456 |
| MACD signal (9) | -1.1273 |
| MACD histogram | -4.8182 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'TSM': 267, 'SPY': 267}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 418.5100 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.4939 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 1.4299 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -6.2834 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 38.8005 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 45.4750 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 39.1384 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 26.0366 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.7390 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 4.1383 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.1216 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6929 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 31.6685 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 2.1276 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -21.5466 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.1569 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 17.8963 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 65.8460 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 58.6550 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 41.8550 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 27.1231 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 41.4593 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -4.8182 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -3.4857 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 5.6708 -> Clearly above the moving-average trend level.

## TAILWINDS

### TSMC Debunks Irrational AI Fears As Pricing Power Expands (Rating Upgrade) (NYSE:TSM)
- Summary: TSMC Debunks Irrational AI Fears As Pricing Power Expands (Rating Upgrade) (NYSE:TSM)
- Date: 2026-10-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxPaVhFdlg4SFFKQ0sxVVcyMnNvdGxFYVNKOVRpMFRXNnhjV0txOGphTHR1Q2N5S0hRbUVoMWhKcE12Qlh4MEFjb2hKWDR0dUREb3Ywb1p4ZWFLcW8tQVRxdC1Xd2ZwVlRQRXpLS1MwUURibmxDYk14Slc3UV83NlNLLUl5ZVJGUUJWa0VKTl9RaFlUR3ZjNGpBSl9JX21kbFo5VVRVaEYzckRGZnVUYVhtVTZ1cw?oc=5>

### Taiwan Semiconductor and ASML Are Incredible, but 1 of These Monopoly Chip Stocks Is Far Safer.
- Summary: TSMC and ASML are highlighted as strong, with TSMC deemed safer among monopoly chip stocks.
- Date: 2026-10-22 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxPRWxEN05udW5ZSU1udEloR0JrcHNjQlJ5bDBpT2gxd28teGhSV0dNWnpMSDUxSW4yTy1PdlRqZGRrYVR1N1dUbzBaOEZ1all3bjVPSVNHMWxsbXk3S3IwNmFnbG5QRkIzTExjcUxNYzIwUThKUUZ5V2Y1UTZsaUF0UTdURFpwejlPdG43TUhsQ2d3NHRoNHR1YlVQcUpvLVFSeDdhblZB?oc=5>

### Taiwan Semiconductor Will Transition Into an Indispensible Utility of Global Computing Within 5 Years
- Summary: TSMC plans to become essential global computing utility within five years, driven by AI and data center demand.
- Date: 2026-10-23 | Impact: high | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi3gFBVV95cUxQblNIRms1YWZKSjN1WENrYkttcUlzeDkwaVkyR0VBSFpDWlFtTktTSU1NNDM4YnJxRzJvTm9pbnEzZFV2UWxlYTRsa3BHMGNPZ1VkMVcyNW0zQm5BellRM0RMczZCZzVpeE5LYVFsVXZjeVVCSzRZWWY2ZU5zeDg4OG5uMC1yWlVidjFRU1VaMlh0T3VnSDNCdm1SbmVST0pRVTc5emJLN2wwU3JhQVM5TjJjdUs4d25QdWR5bjBzaHBGYlY3UTNOYjJWWlJoemxQTHR3XzQyY0NQczJMZFE?oc=5>

### TSMC Explores Rare Earth Alternatives To Protect Chip Production From China Controls
- Summary: TSMC seeks rare earth substitutes to reduce dependence on China, strengthening supply chain resilience.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxOLXZraEZSc3pROFZjRTdkbkpJT0ZlRmY4eTlaVDQ3MFE4dmJ2ZU5LcnBJTTFpX0tDcGNUQTFZYUE1SVJBdzhvblhWSkxCa01LWmxkRF9ERV92NVo3Nk0wNi1mVDNrWlRMTmxRTUN0MlFFemJKRG94MGVlS2VkVlFacGk0YV9jTTNXdS1vM1pHZmRWTk9OZVhORWZjQ3FkU0U?oc=5>

### Moody’s upgrades TSMC rating to Aa2 on booming AI demand and market dominance
- Summary: Moody’s raises TSMC’s rating to Aa2, citing AI demand and market dominance.
- Date: 2026-10-21 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxQLVc5LUhMMkVUc0VSU2ZYUnVDUXQ1a0dPWE90a25OR3ZMdGVjLVNkQWlIN1JPck9mZUdIR1FTNHBQNk1KcV9MUHgyYUlocV82VlI2cGd2Zm5IU0tEZmNLTkNoU0dnVE1tVGpNUDlzVmR3cGZRdy12d2xkZ2lyWmtpRUZMNmxKNnBMTG51dElNVVoxRDh0eXB2dHRMYw?oc=5>

### Taiwan Semiconductor Manufacturing Co. (TSM) is Capturing AI Growth Through Foundry Leadership
- Summary: TSM leverages its foundry expertise to capitalize on AI demand, positioning itself as a key supplier for AI chip manufacturing.
- Date: 2026-10-19 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxQVTkzSUMyTXRiSGo4ckpsd3owdl9idE9CRFBTU3B1RldCNEZERXF6QUc2Z0EzVERadmRod0Z2WWdRR2w1b3pjNEhhRlVINi03ODB6cGc2ei1leDhyQlpXQjk5ZHc0OFlRU0N4a2trd2JidmtzcTVBLWdXNGNRaU9sbHFRM21DNlFEUHpyTVU0bHlOYko1T3dNX2RUUk9nZ0pYenhmRkFuX1o?oc=5>

## HEADWINDS

### Taiwan Semiconductor (TSMC) Posted Record Profit and the Stock Still Fell. Here's What the Market Is Worried About.
- Summary: Taiwan Semiconductor (TSMC) Posted Record Profit and the Stock Still Fell. Here's What the Market Is Worried About.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxPUC14clR2aXF2cVFkUGpJWjYzNEFKYTlWQVBySmdMdUY4Y3QtQmNXbVlaVjVyWEpuNjNzbXlCRER4WVRyeFFwWGFHcXJPOFA3UGc5R1pNb05CX3V6ZkM4VWRibmdaRG9GN3NXbVBDTkZYZ1J2eUJSSkd5OWlza05OSnQ4TUE0VTNyOXhNTGtiSkRxd05xTmhB?oc=5>

### 'Intel Plus Elon' Could Pose Bigger Threat to TSMC Than Musk Alone, Chip Analyst Says
- Summary: Intel and Elon Musk may jointly threaten TSMC's market position.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxQRVh1dTBHazd3OVphVWZlR0s4THJmMDNWRVVkbGE3bURRVXJOUmhxQ2JqaklObk1vTnFySHFsd00xdFpNVzZ3TnkyOVpLbWt5b29zSTdnYnN4UFZRQTRSZGFtbGVJTnVZTHBmUjBkaVVvaFRYSjVGd293SkUtekszdUxVRUZMYnZ5S0sySk1iVzlJY29FUnF1cW1aeXJPdw?oc=5>

### TSMC (TSM) Underperforms in Q3 as Semiconductor ‘Crowded Trade’ Unwinds
- Summary: TSM's Q3 performance lagged due to market saturation, indicating short-term revenue pressure.
- Date: 2026-10-19 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxOREU2WlFUM1d2SmhjR1R5LXlEUmNoZVVrOGt3ZE1aR3A2dlNHaFdYS0RPUTBlUC1SZ3dYaTd2b3E4NUVXUGZrWTd4MlRVZTVOcFREdG9yU05fWTRnblpxb081RnMxd1FBMEZBbW80WlQzSU84VGVRREJkWFV3RngtMk5XRFVESGVnVTFlZS1oSDl6c0RaWDJWS0dlVGhkdFN2UDl3ak9Hdw?oc=5>

## CATALYSTS

### TSMC Stock Just Delivered Another Blowout Quarter. Why It's a Buy for the Next 10 Years.
- Summary: TSMC Stock Just Delivered Another Blowout Quarter. Why It's a Buy for the Next 10 Years.
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxNeWl0cnltZVNtVUxxa3FKQ0NzeUFJYXpPc3loTzVOUTlXRW1LQmhLeDlQVzRycVM1MkdxN0NiNkpxb3BRSXlXSE90UW9HMEE4MFVadEJjTTFlVVRpSnN4OXBUOTMwaC16REZxMDZVVEpmd2duazJZeGQtcGU0eWE0NGd2OGszZkhZZzRqdjJtVmVhc3VTamQyNWlDTDBYTWM?oc=5>

### Taiwan Semiconductor’s (TSM) Profit Rose 69% Last Quarter. Is the Stock Still Cheap?
- Summary: Taiwan Semiconductor’s (TSM) Profit Rose 69% Last Quarter. Is the Stock Still Cheap?
- Date: 2026-10-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxPcXpvWTlBMWF4RXRoZ0lBUk00bzVvSnNsWFJGNEU5eXlRbHdkZlNFM1hRcXhQOXNOZWpab2NmVXpoRWFuMkZOcjE4a3MwUFRtUGpkbWhZTkdBOHhJbnNmcGtiX21xc09lV1FXMmY1VjQ2eXExSHMycktZTU9GZWpqRFRlMk9fWW52Mkc0Z0Eza0JoUXQzWGgwaUI5U0J6TVA2ZVZ3?oc=5>

### Taiwan Semiconductor Is Set to Cash in on AI. Here's What a $5,000 Investment Could Be Worth by 2030.
- Summary: TSM could benefit from AI chip demand, potentially boosting future earnings.
- Date: 2026-10-25 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxPM19uMDhwWHhPdVVRWEVIaGwxUUZYWldnaFVHdDlkMXF4LVBoM0F2YXQzYmptRFRHQlNvejdhNEhsUXdOQkl5RjJMeDN0VlRMSmJzdW1YeWN0UlJKb3pEeVl2SFFFb3BYeVB5TXJfVVEzZmQzcFFUbHBXeXlBb0thUjdpNFl0Sjk1S0ctTW93NXpkWURSa3M4ZDFJdEMyQQ?oc=5>

### This Company Behind the World’s AI Chips Could Be a Huge Winner
- Summary: TSM may become a major AI chip supplier, enhancing its market position.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxQbldrdE92SjNYOC1XekxDRkJsZEJYa0hFNnBjN3NHSncwUnJPR0EwX1F4TmJjNUFTR1BJMFZCWHRteG1nVk13eGpJNUxYeHlSZzVIN0paZW43YWNCc3B2aVVaWTJ4N3k2NU80ZjUwa3ZYRUJxQXItajVaQmFjTXMtX2M1UHBjOFNIMFNPanIwcFhKZk5qZzRFUlQ5V0NGUE5IUi11MEdRN0cyUQ?oc=5>

### Taiwan Semiconductor Manufactur (TSM) Stock Forecasts
- Summary: TSM analysts provide stock price forecasts for the upcoming period.
- Date: 2026-10-23 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxPMzhDdnNLQW1lbnEtSEc2SVU3dUE5Z0xrMTdvTGFMSjVPZVlrM0MzcndTWTkxeGJQQzIzeFVwUmxhMUtWR3VqYXVKSkp4eVpiR1U5b0ZvXzJuWnJ1WFV5NkItdGVxU2owS0NTUXZrQVNfWFFHVnJnWGtPM2VGek5jTEVGWlFlYjFIQXc?oc=5>

### Taiwan Semiconductor Wants In on SpaceX’s Terafab — but Only If It Runs the Fab
- Summary: TSM seeks to operate SpaceX’s Terafab facility, indicating a potential partnership.
- Date: 2026-10-22 | Impact: medium | Horizon: medium | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxPaENoRUttY3IxVVBjeExBSXhaQzRESmVDMXFtNUFDS1RmVUxPQU9lUHQ5cWlPWGNaRzZFOS1PNzBLejRsdTk1OGJBR0RmNDdtQXFqcGRGN1VhSVJLcWJ3cUwyZG55U0lTN3ZmU2xFS2gwYlhaZmxBVENFV29wWHNyNUlHTFNCcWs4TEV2dVRFN09Hc29PSk56aHZUME1JZ291SUlETg?oc=5>

### Taiwan Semiconductor Manufacturing (TSM) Draws Fund Managers Leaving Firms To Invest Personally
- Summary: TSM attracts fund managers who are investing their own money in the company.
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.75
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxQNWwxM1BhNzBha1B4WGV1WDllaDBXMVByYW9peGwxSmE0WWotQ09qQWlhc3RFMS1TTkhIbDBEcXZGZ2FIRXVlX3Q1UkRDUTJXbjlZNFI0YXcwTVV1OWZXVUhBYTk5bnlqWVJXQUlCUzlxSGVPaVg5UFV3WjVzbnZTV0l3VTNmSG1YbXVNNUdtTnB5cVEtWVRJcFlSbTEzTUNIWUpfcWZKMU1tdzd5alE?oc=5>

### What's Going On With Taiwan Semiconductor Stock Friday?
- Summary: Inquiry about TSM stock performance on Friday.
- Date: 2026-10-23 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxQV1hWNFFIMUw3cmE2SlhnZUJYcXgtaGVjYV96SjJDWjBaV1JWUlJxNWw1WGR0VTNreXRaS09MTGxCdWMzc3dfa0tsd09FdE5LeVA0aWdMQmV4eFRqMjNXM21kNmRHVnlFb2Y2OEVjTy1tVVVMVUJ1dkxDaFc0SlhkRmZZMGJNN1hDYl8tSlc5eVkxdDFjQ1d1b19KaUtOc1ZhSjl4bnJZS2o0Q3Vi?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **TSM** | **27.12** | **79.87** | **3.92** | **50.90** | **2,170,591,248,384.00 USD** | **45.47** |
| UMC | 19.08 | 3.47 | -0.33 | 17.00 | 47,374,393,344.00 USD | 155.62 |
| GFS | 34.68 | 2.06 | 11.98 | 5.80 | 24,743,813,120.00 USD | 26.71 |
| INTC | N/A | 5.01 | 28.21 | 25.40 | 459,679,694,848.00 USD | 127.88 |

Peers fetched as_of: 2026-10-25; TSM reuses existing data (market data as_of: 2026-10-23); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-15
- Next expected earnings: 2027-01-14 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-25

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
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

- https://news.google.com/rss/articles/CBMiswFBVV95cUxPaVhFdlg4SFFKQ0sxVVcyMnNvdGxFYVNKOVRpMFRXNnhjV0txOGphTHR1Q2N5S0hRbUVoMWhKcE12Qlh4MEFjb2hKWDR0dUREb3Ywb1p4ZWFLcW8tQVRxdC1Xd2ZwVlRQRXpLS1MwUURibmxDYk14Slc3UV83NlNLLUl5ZVJGUUJWa0VKTl9RaFlUR3ZjNGpBSl9JX21kbFo5VVRVaEYzckRGZnVUYVhtVTZ1cw?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxPRWxEN05udW5ZSU1udEloR0JrcHNjQlJ5bDBpT2gxd28teGhSV0dNWnpMSDUxSW4yTy1PdlRqZGRrYVR1N1dUbzBaOEZ1all3bjVPSVNHMWxsbXk3S3IwNmFnbG5QRkIzTExjcUxNYzIwUThKUUZ5V2Y1UTZsaUF0UTdURFpwejlPdG43TUhsQ2d3NHRoNHR1YlVQcUpvLVFSeDdhblZB?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxNMHlGRTJ0YnlWblZ6Nk1keHVUdG83aGlNRjc3a0t2YTROdTJjdnpGSjdHS3FsUHRteGk4TjQzSTRkNWxCU0N2WG5nLU9UTndaQXNWeFVnVktjVGpRc1FxcTZxSEEtWXVYazB0TGtKc09iZzEzY1pjckFXQ01jNVVkNjJKeXpSaWdyeTY5ZnF1SXRLX1pyd2V1bw?oc=5
- https://news.google.com/rss/articles/CBMi3gFBVV95cUxQblNIRms1YWZKSjN1WENrYkttcUlzeDkwaVkyR0VBSFpDWlFtTktTSU1NNDM4YnJxRzJvTm9pbnEzZFV2UWxlYTRsa3BHMGNPZ1VkMVcyNW0zQm5BellRM0RMczZCZzVpeE5LYVFsVXZjeVVCSzRZWWY2ZU5zeDg4OG5uMC1yWlVidjFRU1VaMlh0T3VnSDNCdm1SbmVST0pRVTc5emJLN2wwU3JhQVM5TjJjdUs4d25QdWR5bjBzaHBGYlY3UTNOYjJWWlJoemxQTHR3XzQyY0NQczJMZFE?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxOLXZraEZSc3pROFZjRTdkbkpJT0ZlRmY4eTlaVDQ3MFE4dmJ2ZU5LcnBJTTFpX0tDcGNUQTFZYUE1SVJBdzhvblhWSkxCa01LWmxkRF9ERV92NVo3Nk0wNi1mVDNrWlRMTmxRTUN0MlFFemJKRG94MGVlS2VkVlFacGk0YV9jTTNXdS1vM1pHZmRWTk9OZVhORWZjQ3FkU0U?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxQLVc5LUhMMkVUc0VSU2ZYUnVDUXQ1a0dPWE90a25OR3ZMdGVjLVNkQWlIN1JPck9mZUdIR1FTNHBQNk1KcV9MUHgyYUlocV82VlI2cGd2Zm5IU0tEZmNLTkNoU0dnVE1tVGpNUDlzVmR3cGZRdy12d2xkZ2lyWmtpRUZMNmxKNnBMTG51dElNVVoxRDh0eXB2dHRMYw?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxQVTkzSUMyTXRiSGo4ckpsd3owdl9idE9CRFBTU3B1RldCNEZERXF6QUc2Z0EzVERadmRod0Z2WWdRR2w1b3pjNEhhRlVINi03ODB6cGc2ei1leDhyQlpXQjk5ZHc0OFlRU0N4a2trd2JidmtzcTVBLWdXNGNRaU9sbHFRM21DNlFEUHpyTVU0bHlOYko1T3dNX2RUUk9nZ0pYenhmRkFuX1o?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxPUC14clR2aXF2cVFkUGpJWjYzNEFKYTlWQVBySmdMdUY4Y3QtQmNXbVlaVjVyWEpuNjNzbXlCRER4WVRyeFFwWGFHcXJPOFA3UGc5R1pNb05CX3V6ZkM4VWRibmdaRG9GN3NXbVBDTkZYZ1J2eUJSSkd5OWlza05OSnQ4TUE0VTNyOXhNTGtiSkRxd05xTmhB?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxQRVh1dTBHazd3OVphVWZlR0s4THJmMDNWRVVkbGE3bURRVXJOUmhxQ2JqaklObk1vTnFySHFsd00xdFpNVzZ3TnkyOVpLbWt5b29zSTdnYnN4UFZRQTRSZGFtbGVJTnVZTHBmUjBkaVVvaFRYSjVGd293SkUtekszdUxVRUZMYnZ5S0sySk1iVzlJY29FUnF1cW1aeXJPdw?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxOREU2WlFUM1d2SmhjR1R5LXlEUmNoZVVrOGt3ZE1aR3A2dlNHaFdYS0RPUTBlUC1SZ3dYaTd2b3E4NUVXUGZrWTd4MlRVZTVOcFREdG9yU05fWTRnblpxb081RnMxd1FBMEZBbW80WlQzSU84VGVRREJkWFV3RngtMk5XRFVESGVnVTFlZS1oSDl6c0RaWDJWS0dlVGhkdFN2UDl3ak9Hdw?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxNeWl0cnltZVNtVUxxa3FKQ0NzeUFJYXpPc3loTzVOUTlXRW1LQmhLeDlQVzRycVM1MkdxN0NiNkpxb3BRSXlXSE90UW9HMEE4MFVadEJjTTFlVVRpSnN4OXBUOTMwaC16REZxMDZVVEpmd2duazJZeGQtcGU0eWE0NGd2OGszZkhZZzRqdjJtVmVhc3VTamQyNWlDTDBYTWM?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxPcXpvWTlBMWF4RXRoZ0lBUk00bzVvSnNsWFJGNEU5eXlRbHdkZlNFM1hRcXhQOXNOZWpab2NmVXpoRWFuMkZOcjE4a3MwUFRtUGpkbWhZTkdBOHhJbnNmcGtiX21xc09lV1FXMmY1VjQ2eXExSHMycktZTU9GZWpqRFRlMk9fWW52Mkc0Z0Eza0JoUXQzWGgwaUI5U0J6TVA2ZVZ3?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxPM19uMDhwWHhPdVVRWEVIaGwxUUZYWldnaFVHdDlkMXF4LVBoM0F2YXQzYmptRFRHQlNvejdhNEhsUXdOQkl5RjJMeDN0VlRMSmJzdW1YeWN0UlJKb3pEeVl2SFFFb3BYeVB5TXJfVVEzZmQzcFFUbHBXeXlBb0thUjdpNFl0Sjk1S0ctTW93NXpkWURSa3M4ZDFJdEMyQQ?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQYmpiWURNZUxWWjYwaFlnNjZWajVPTmhHekpuLS04TmNwRGgzTHlXbmhSZUROQ0R5U1NaUGs0b1NmR0N4VnZHbEFqT3BaNzVzVG9zQ2lkX0hiLU9pMktNQUxTT2Zhd1RRTHN0aU1iRkdmUVhtQy1RT29FVEJFVS0yaW1uNUhPQ0VDTkRaUjhvaGdWMlZZVHZPMw?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxQbldrdE92SjNYOC1XekxDRkJsZEJYa0hFNnBjN3NHSncwUnJPR0EwX1F4TmJjNUFTR1BJMFZCWHRteG1nVk13eGpJNUxYeHlSZzVIN0paZW43YWNCc3B2aVVaWTJ4N3k2NU80ZjUwa3ZYRUJxQXItajVaQmFjTXMtX2M1UHBjOFNIMFNPanIwcFhKZk5qZzRFUlQ5V0NGUE5IUi11MEdRN0cyUQ?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxPMzhDdnNLQW1lbnEtSEc2SVU3dUE5Z0xrMTdvTGFMSjVPZVlrM0MzcndTWTkxeGJQQzIzeFVwUmxhMUtWR3VqYXVKSkp4eVpiR1U5b0ZvXzJuWnJ1WFV5NkItdGVxU2owS0NTUXZrQVNfWFFHVnJnWGtPM2VGek5jTEVGWlFlYjFIQXc?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxPaENoRUttY3IxVVBjeExBSXhaQzRESmVDMXFtNUFDS1RmVUxPQU9lUHQ5cWlPWGNaRzZFOS1PNzBLejRsdTk1OGJBR0RmNDdtQXFqcGRGN1VhSVJLcWJ3cUwyZG55U0lTN3ZmU2xFS2gwYlhaZmxBVENFV29wWHNyNUlHTFNCcWs4TEV2dVRFN09Hc29PSk56aHZUME1JZ291SUlETg?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxQNWwxM1BhNzBha1B4WGV1WDllaDBXMVByYW9peGwxSmE0WWotQ09qQWlhc3RFMS1TTkhIbDBEcXZGZ2FIRXVlX3Q1UkRDUTJXbjlZNFI0YXcwTVV1OWZXVUhBYTk5bnlqWVJXQUlCUzlxSGVPaVg5UFV3WjVzbnZTV0l3VTNmSG1YbXVNNUdtTnB5cVEtWVRJcFlSbTEzTUNIWUpfcWZKMU1tdzd5alE?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxQV1hWNFFIMUw3cmE2SlhnZUJYcXgtaGVjYV96SjJDWjBaV1JWUlJxNWw1WGR0VTNreXRaS09MTGxCdWMzc3dfa0tsd09FdE5LeVA0aWdMQmV4eFRqMjNXM21kNmRHVnlFb2Y2OEVjTy1tVVVMVUJ1dkxDaFc0SlhkRmZZMGJNN1hDYl8tSlc5eVkxdDFjQ1d1b19KaUtOc1ZhSjl4bnJZS2o0Q3Vi?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
