# AAPL Intelligence Report

- ticker: **AAPL**
- Report as_of: **2026-11-19**
- Market data as_of: **2026-11-19**
- Quant sources: https://finance.yahoo.com/quote/AAPL/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AAPL/key-statistics/
- AI analysis snapshot as_of: **2026-11-19**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-20T05:59:27.963528+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 4, 'ai': 15, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **8** exact headline/source/date matches; prior report **20261119T054856Z-9eb86811/AAPL** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 13 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 24.0%; oldest publication 2026-11-16

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 349.2100 |
| Return 1D (%) | -0.9193 |
| Return 1W (%) | -1.5977 |
| Return 1M (%) | 1.9057 |
| Return YTD (%) | 28.8996 |
| Return 1Y (%) | 30.4835 |
| Annualized volatility (%) | 24.9018 |
| Beta vs SPY | 0.6112 |
| Max drawdown (%) | -13.7985 |
| Sharpe (rf=0) | 1.1977 |
| Downside deviation (rf=0, %) | 16.8979 |
| Sortino (rf=0) | 1.7651 |
| Historical VaR 95% (1D, %) | 2.0034 |
| Historical ES 95% (1D, %) | 3.4742 |
| Correlation vs SPY | 0.3411 |
| Tracking error vs SPY (%) | 24.0239 |
| P/E (trailing) | 39.24 |
| P/B | 45.28 |
| EV/EBITDA | 29.81 |
| Revenue growth (%) | 11.70 |
| Forward P/E (estimate) | 33.03 |
| Gross margin (%) | 48.79 |
| Operating margin (%) | 33.01 |
| Return on equity (%) | 142.26 |
| Free cash flow yield (%) | 2.08 |
| MA50 | 341.3742 |
| Close vs MA50 (%) | 2.2954 |
| MA200 | 302.4477 |
| Close vs MA200 (%) | 15.4613 |
| RSI (14, Wilder) | 53.1560 |
| MACD (12,26) | 3.6123 |
| MACD signal (9) | 3.6629 |
| MACD histogram | -0.0506 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AAPL': 286, 'SPY': 286}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 349.2100 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.9193 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -1.5977 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 1.9057 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 28.8996 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 30.4835 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 24.9018 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 16.8979 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.7651 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.0034 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.4742 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.3411 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 24.0239 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.6112 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -13.7985 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.1977 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 33.0293 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 48.7860 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 33.0100 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 142.2570 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.0820 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 39.2371 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 53.1560 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.0506 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 2.2954 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 15.4613 -> Clearly above the moving-average trend level.

## TAILWINDS

### Apple targets June 2027 unveiling for AI smart glasses: report (AAPL:NASDAQ)
- Summary: Apple plans to unveil AI smart glasses in June 2027.
- Date: 2026-11-16 | Impact: medium | Horizon: long | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxOZEhVR1p4SVhoeEFLSTkwSUVoLW5RRG9JRmZxX1k5NVVpbExYRU1WTGw5clM4d2FKNllFMTlROVlVT25HQmdkRHpVZUJqMWptSlhkSk9RdmF4LTlDMlhQazFDU3ZlelhMRkJPMTJkOEl0UHYxZHpOY3lYSG1lU2piV0tzM2lvZXdmaDJTU0RueExWYmNJWU1uQU4tWW83Q1lZ?oc=5>

### Services Franchise and Installed Base Anchor Apple’s (AAPL) Durable Earnings Growth
- Summary: Apple’s services and installed base support steady earnings growth.
- Date: 2026-11-19 | Impact: high | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxPU05ZM0hXWHV5dklpM3lCUzhua21IQ3JZOHRTNVFTNkI4bEVlTTY1TVhyNWdYUERDMW1VSXRjZkRMOVotU1FTQWo4Z0dWV21QTU5tb3NKSlI2cVFiLWhHNkJHWFpLeHYwd3FKQUgwOU9GdnFMaS1pVHhmUWhSbnh0MDYzbWpOZkxxbGNMLXJuZGYtWW15WEZRTVdGTGU0cE9iY294Q3F0cUtoUQ?oc=5>

### AAPL Stock Posted Best Week In 4 Months Amid Nvidia Disruption: Apple Reportedly Plans Smart Glasses To Rival Meta Next Year
- Summary: Apple plans smart glasses to compete with Meta, boosting product prospects.
- Date: 2026-11-16 | Impact: high | Horizon: long | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxPaTZ2ZWQ2QTBxMk1iWTJ4ZXBGc3hpUDRHMDVVdFdMaGtkWVVkcEtzM2djWFpZQ1ZxTnYtUHFhMHFIbjFSSjhPSXVDWWsxdXlvQzQ1RDliaVNNUzR5QzZLWEl0UW9ROGx5RnZVdko4LWYzbWNqWEJORkJDTEVmY3ZObDgyaHNmZzRHaWpQN2ZCaDFQM05ja21J?oc=5>

### Apple (AAPL) Board Member Sells $31 Million of Company Stock
- Summary: Insider sold $31M shares, indicating potential confidence in company value.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxNd3JDclJKSWdtLU42WGpUckt6cGVnU2pqd2RhUHdrNEVmTHBZZE50QkJacC1LRFc1UUhMUXc4di1SOG1YU214UmkyeG1TWldTczliUlVETVY5UHN3RVB5XzNmYkF6eGNxVXZlVWxTODFZbGdWUVlxbl9PWFJSSDhYTVNJdzdRcUtxVlFyZFFNeEs?oc=5>

### Apple Stock Price Could Reach $765 by 2030, CoinCodex Forecast Shows
- Summary: External forecast projects Apple stock to hit $765 by 2030.
- Date: 2026-11-19 | Impact: low | Horizon: long | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxPQ2I1TjdieTB0dHRkQ2NlckpUT2FSY240RDNPZ3VhUHVEbnZ6czlqbERpRGJlSWV2NFVLbEdsTG4tNTN2OURIaEZOWXRQN0RWdGJLTk5WUUVrSmI5RHZPY0FseGpOQXZTS0taZjl2N2RzNXREc3JMWXZvZVdaWl96RTc3VEdtZjZZa1E?oc=5>

### Apple (AAPL) Stock Price Prediction: Apple Holds Above Key Support as AI Optimism Meets Mixed Positioning
- Summary: Prediction shows Apple stock above support amid AI optimism.
- Date: 2026-11-17 | Impact: low | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxNQzRFdU02UWFvTnB5TklqbXVQUUNwZWhsR1BhZkp2NjJCV2k3OWNXZ1RwRDd4YjE3YTllbmFoYjhjeHRFWVhZbmUweTdIVlZ2VHhiRklQWm1JR21qWC1nRXhkMzlhZjE1WDNqcUNEaE9CbGJJLXZYMzJKVGpHOUM5TWxoaDZtUmpJWEVBTlJ3VHhBazU2cm13?oc=5>

## HEADWINDS

### Atlanta Fed inflation update may deepen policy risk backdrop for Apple shares
- Summary: Fed inflation update could increase policy risk for Apple.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihAFBVV95cUxPVmNReERLS3drZlJOQm5qWmRXTzA4YUQ0bkdPOVRXcVdtNm9GRTdzenlSUVZWM0k4WXJCUThVZjRIZlRlYklMSWgtbHkyR2F2SXlHbzlXY0JuR05XeXRfT2NYSVJmVjJLV0NSbFJfMGwwZXNRMjc3dU5tYUdMQVpkWjFiMHQ?oc=5>

### Apple’s Haven Status Makes It One of Priciest Stocks in Market
- Summary: Apple’s high valuation may deter investors.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxOWFdXODZmaFdpSjdGdFF5Mm5IQVRyZTJUczJ5R08zSGttalFxSFgtdTQxVENCajRVYlJWOG1hUmcwRHpmcHBENVBDNU1NMDgzbDdDZEtLbE5uT0N6bHdnNGdaOUZxbV9ad3FXSVUyVUt1Mld2S0NYaHpDNG1EaUlfSDFJZFZ0R1hmSDl3dmczRkc2RW4xM1VKdHZCY3FWWUJpUkswM2hsRGtCR1VmdWRuMFRaQQ?oc=5>

### How Investors May Respond To Apple (AAPL) Service Outages
- Summary: Service outages could negatively affect investor sentiment.
- Date: 2026-11-19 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxOXy02WGZ5d1JKRjdEUFlEZm92TmEwYy1Kd2F6X0lobUIyd0sxSFJrNlhGR3hOMkxma2ZpQmQ0V3RaUXVnUFNGR3dLc3RzTHFCcEJOaXNsRlVCS2dxZWVwOWExbUFiQi1pYnFuNGZlTzExLWZmNXd2WlJHWkV4WWdtLUFleE5iWTdMeW9wb1d5RTBjbHRXblhqVDY5WkpTUQ?oc=5>

### Apple (AAPL) Must Fight UK Backdoor Order In Public
- Summary: Apple faces a UK legal challenge over a backdoor order.
- Date: 2026-11-19 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxQTDFVZTliM0JEbThicVlKYXE0OFZzd3U3dENPdUVieTJ2dWlvNl82Y2Fpdng0Rmd2V041UnltejdaLTBMS0NpUnc2WlQtdjBGb2RIZmlVQlZKb2ZYWGdmdWZkeWRBUkI4OUY4S2VQVmZPQzJlMWJMdHNuaEpWb00tdHE3LWxfZDJLQXB4ZHRzVWljb0RjTEctQTRGelJ4US1WUmV3aWppYVAwUGs1MnfSAbMBQVVfeXFMTTUwV0ZuTDQtYm9sVWg0NFZCRkNDR2JEYVA5Tmt5SERUZUpwWDdNVVBSb2dGTGpHTjU5UmdUMjFmdjZPSE9UQkFxQlJTTUNLbzYzUXo2Q0UtaVlGc2RuLWJFOWxfWmtCWmdQOHhfeWxMQTgxNmF1N21yYjJQZjdoVnBLNDgwck1zX1M4U3lzTzFhRUY1ZHRZUC1Jd0dvcGZna3c2T3B1Zk5XNFFGLVdVT291aE0?oc=5>

## CATALYSTS

### Apple Nears a Rare Long-Term DRAM Supply Deal With Samsung Electronics. What This Means for AAPL Stock.
- Summary: Apple Nears a Rare Long-Term DRAM Supply Deal With Samsung Electronics. What This Means for AAPL Stock.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxQZTAzU2dvbVdZTzN2Smttc1pjc3lsSW5qWTdldDFETUFxNmx4Y2Z1RkZSNG5EcXR0bFlueDdLY2Y4cWxfdGxiYktmeWVDODhnclQ5eEpWZVZRVHlJZjhkalNMVlk1UUpKaW9IS3NRN3RVcnF1MHhEbnVaZWdQaThJRjdud3VSSGkxREdfWHVTelZxSGdXTXc?oc=5>

### Apple adds face unlock to iPhone Duo in new software beta (AAPL:NASDAQ)
- Summary: Apple adds face unlock to iPhone Duo in new software beta (AAPL:NASDAQ)
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNekw4czk1V0dBR21SMWtoS1ozbkVuWUhPTTR5cEtWTmNTd3JrdHM3UWg5RWItekxCMnJVcUhrZXBDTkJ3aDdPdktucTRUYWtjazFCV1p4a0xyMzBsS3NrMXdvOGlmaEViOGM4MTd4MmZQOW9sN0JTbmQxY3pyRjlTUjk2eXBCa0QwWFR0N1REdHhMMmRfb0x3anhnWQ?oc=5>

### Apple to stand trial in France over iPhone repair restrictions: report (AAPL:NASDAQ)
- Summary: Apple to stand trial in France over iPhone repair restrictions: report (AAPL:NASDAQ)
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxPZ0xRQ0RCX3RmbzdqVjRpTzAwSFZ0bTRGeTlCUzh5QXRpSlZRT0NWT3Y5YmhFU1AtdHA1ZmM1eGxDczBsdVFNUDYyd085VVJPaHFCRGZPZlZMWDZFX3hQM0p4M1UyQlZOYnlfRGY1eFNnbHFDSWdtUkN6TWE2R2VjQjlIZ09GODAxcDBmRVNUVTI1ME9xMks3WUo1U19nZ1I0ZEJQXzJ1R3VkRlU?oc=5>

### Apple (AAPL) Heads To French Trial In June 2027 Over iPhone Repairs
- Summary: Apple (AAPL) Heads To French Trial In June 2027 Over iPhone Repairs
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxNanM1bVhuU1dILWpuWnI0VFNfeTVDOW5ZNnNOdERKalBvSXpaOHdvUWlLUmRpc09ieXRCeUlXcWwwU0N3c0N5NXMtdHBHYUE2ejlLZGNNb180eDh4Y0hfd0Y4QV9zY1JGRFJ4STlKSjhMVWc2bXBvNmJhT2x2VDEtZ3dCNXJHbUNQa2tLX3I5N0Ewdm8zZW5wMVBsai1sOXNWWDFIN014bzA2VUMwNHU2Q2F5OERyVnh1U205d9IBwgFBVV95cUxPNjIydEQzdWR2V2NxRzFGRktPdG5jNkFpTW1UaVJUX2hCLTY1akVCVnpyNGViWW9pdTBXd1JMNHBOLWdILWtIek9sTW0zQW5WcHhKV09CWVRudzlSZ3pSSzRuZC14allOa0ZfaG5UTHVrWU9yOVoxZUVKUVlLb2NOU29RaDh5aTZlSk9Ub1lYSW9sa2ZKYW1vaDNVZlpjNEpMMWxNU0djYjJzVDhqVGpPTGw3VFBIUmZ0bHA1MTgzS1dCdw?oc=5>

### ANT, META Stock Slip After-Hours Amid Reports That Apple Is Working On Its Own AI Agent
- Summary: Apple developing its own AI agent signals product innovation.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMi4AFBVV95cUxQeTJ6NFlTUEVrSzlSZ2Q1UVNDakdTR2NkM3JuSHVVbkFfX3BWNnUyTE9pY1MwbTRDdmpndEoxOHRTeVR1TWdZb05PelJPd1FVVzZzMTdLbVNBeldwb2o0UGZTS0t2dUF0UUswZ3ozTWptalJwM3pRQXlDSXJQNjFnRG1IV1BJSWVHZjRBX2x2MUdHVzN1anNaXzhuWVVGbkVUQ3BpN2lya2x5V2diTHNHekNrTV9Ic0xMVUozS1ZhblgxWjkxdHBqYkFON3I5YWdKZXNjS2JHRk1aMW1ta2xuRA?oc=5>

### Apple Music Radio hits 50M listeners as audio competition intensifies (AAPL:NASDAQ)
- Summary: Apple Music Radio reaches 50M listeners, strengthening audio presence.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxNZG1iYzZKN2piZlZQOUthcnBZb3hYTlpwM3hXRjk4YmU1eWRVQ1o5T1MwVERqRjRXV20wZWUtNVpnN0VITzFrUkI0MzhxbEUxU3RkbzUxaV9BTFdMSFVTOENGdU1ZYTNIMGFfRW5OUkRVamEzeDFzT1V4T0VzWUpNaDVnWTdHYjN6UzVkVEhEX0VJWmdreEJ2YlVTWktZWTRwdk1YWFduRk56TXc?oc=5>

## RISKS

### Apple(AAPL.US) Director Sells US$31.77 Million in Common Stock
- Summary: A director sold $31.77M in Apple shares, possibly signaling insider concerns.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxPcjBvOVFKU0RhSk5mZUNBYUo5Z3lHU3NUdEVOV0NBel8wVkJhX29TY2I3MWhVR3dFclVfM0JLOFNEdXNIblA1VV84b1VxOFlsZnJsaTFBYVlhZnRNeW1weU1fZ3pXYk5MOThWeXZLUGJMNkt5dS14T2JZZGZtbnUtaXNRTHhNbV9HSWo2ei1kRmNUUE00ZnN0emIySVVQVm8?oc=5>

### An Apple (AAPL) director gave away 50,000 shares the same day he sold stock.
- Summary: A director gave away 50,000 shares while selling, raising potential governance concerns.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxPeXo2bXM2UVlsdURDYTdkaUx1U1YyOFBtRzhmSnhYaFdSZVhQR0ZZeGE3cWNaWTU4dWNNdUVSd0FpU1VaYkc5U09iaWhlSmV1ZDRDa19nWWRONklwT1BuSFY0Z2dZeUFkclNQSVlMN3RjOXpfY3BhZUZUUno1RnRBVkxjUk5yX21xOU9WMmtGOVYyRkUzdGhXT2d5TzZQQzZMSzF4NUhB?oc=5>

### Apple (AAPL) Stock Price Prediction: Apple Holds Above Key Support as Analysts Stay Mixed
- Summary: Analysts remain mixed on Apple’s support level, adding uncertainty.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxPRVlfbWZZcDEwUGVTaEJQcjlkSXlfWGd5Y0xwSkhnX2tNT3VQeG00VjZNQmVyVWY5NklHWFVwQ2phWXNZNU1LbXhqMjY0MTl1QVk4YTcyNGxpMzhVNVVITVFXUUxGM256VXdOV0RHRnh0dTJVQkp1NURnNVY4N1p1N21FUkpaOUVLekhVSG04aGpDNDEyV2Jj?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AAPL** | **39.24** | **45.28** | **29.81** | **11.70** | **5,074,783,305,728.00 USD** | **30.48** |
| MSFT | 26.01 | 7.87 | 18.33 | 18.80 | 3,700,472,676,352.00 USD | 3.34 |
| GOOGL | 14.24 | 5.08 | 17.55 | 24.70 | 3,352,081,989,632.00 USD | -6.64 |
| SONY | 20.76 | 2.94 | 0.30 | 10.30 | 158,528,503,808.00 USD | -4.73 |

Peers fetched as_of: 2026-11-19; AAPL reuses existing data (market data as_of: 2026-11-19); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-02
- Next expected earnings: 2027-01-28 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-19

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-K
- Filing date: 2026-11-03
- Revenue (latest available single quarter): 62,900,000,000.00 USD; period 2018-07-01/2018-09-29; fiscal year/reporting period 2018/FY
- Net income (latest available single quarter): 29,789,000,000.00 USD; period 2026-03-29/2026-06-27; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/320193/000032019326000026/aapl-20260926.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMioAFBVV95cUxOZEhVR1p4SVhoeEFLSTkwSUVoLW5RRG9JRmZxX1k5NVVpbExYRU1WTGw5clM4d2FKNllFMTlROVlVT25HQmdkRHpVZUJqMWptSlhkSk9RdmF4LTlDMlhQazFDU3ZlelhMRkJPMTJkOEl0UHYxZHpOY3lYSG1lU2piV0tzM2lvZXdmaDJTU0RueExWYmNJWU1uQU4tWW83Q1lZ?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxPU05ZM0hXWHV5dklpM3lCUzhua21IQ3JZOHRTNVFTNkI4bEVlTTY1TVhyNWdYUERDMW1VSXRjZkRMOVotU1FTQWo4Z0dWV21QTU5tb3NKSlI2cVFiLWhHNkJHWFpLeHYwd3FKQUgwOU9GdnFMaS1pVHhmUWhSbnh0MDYzbWpOZkxxbGNMLXJuZGYtWW15WEZRTVdGTGU0cE9iY294Q3F0cUtoUQ?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxPaTZ2ZWQ2QTBxMk1iWTJ4ZXBGc3hpUDRHMDVVdFdMaGtkWVVkcEtzM2djWFpZQ1ZxTnYtUHFhMHFIbjFSSjhPSXVDWWsxdXlvQzQ1RDliaVNNUzR5QzZLWEl0UW9ROGx5RnZVdko4LWYzbWNqWEJORkJDTEVmY3ZObDgyaHNmZzRHaWpQN2ZCaDFQM05ja21J?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxNd3JDclJKSWdtLU42WGpUckt6cGVnU2pqd2RhUHdrNEVmTHBZZE50QkJacC1LRFc1UUhMUXc4di1SOG1YU214UmkyeG1TWldTczliUlVETVY5UHN3RVB5XzNmYkF6eGNxVXZlVWxTODFZbGdWUVlxbl9PWFJSSDhYTVNJdzdRcUtxVlFyZFFNeEs?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxPQ2I1TjdieTB0dHRkQ2NlckpUT2FSY240RDNPZ3VhUHVEbnZ6czlqbERpRGJlSWV2NFVLbEdsTG4tNTN2OURIaEZOWXRQN0RWdGJLTk5WUUVrSmI5RHZPY0FseGpOQXZTS0taZjl2N2RzNXREc3JMWXZvZVdaWl96RTc3VEdtZjZZa1E?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxNQzRFdU02UWFvTnB5TklqbXVQUUNwZWhsR1BhZkp2NjJCV2k3OWNXZ1RwRDd4YjE3YTllbmFoYjhjeHRFWVhZbmUweTdIVlZ2VHhiRklQWm1JR21qWC1nRXhkMzlhZjE1WDNqcUNEaE9CbGJJLXZYMzJKVGpHOUM5TWxoaDZtUmpJWEVBTlJ3VHhBazU2cm13?oc=5
- https://news.google.com/rss/articles/CBMihAFBVV95cUxPVmNReERLS3drZlJOQm5qWmRXTzA4YUQ0bkdPOVRXcVdtNm9GRTdzenlSUVZWM0k4WXJCUThVZjRIZlRlYklMSWgtbHkyR2F2SXlHbzlXY0JuR05XeXRfT2NYSVJmVjJLV0NSbFJfMGwwZXNRMjc3dU5tYUdMQVpkWjFiMHQ?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxOWFdXODZmaFdpSjdGdFF5Mm5IQVRyZTJUczJ5R08zSGttalFxSFgtdTQxVENCajRVYlJWOG1hUmcwRHpmcHBENVBDNU1NMDgzbDdDZEtLbE5uT0N6bHdnNGdaOUZxbV9ad3FXSVUyVUt1Mld2S0NYaHpDNG1EaUlfSDFJZFZ0R1hmSDl3dmczRkc2RW4xM1VKdHZCY3FWWUJpUkswM2hsRGtCR1VmdWRuMFRaQQ?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxOXy02WGZ5d1JKRjdEUFlEZm92TmEwYy1Kd2F6X0lobUIyd0sxSFJrNlhGR3hOMkxma2ZpQmQ0V3RaUXVnUFNGR3dLc3RzTHFCcEJOaXNsRlVCS2dxZWVwOWExbUFiQi1pYnFuNGZlTzExLWZmNXd2WlJHWkV4WWdtLUFleE5iWTdMeW9wb1d5RTBjbHRXblhqVDY5WkpTUQ?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxQTDFVZTliM0JEbThicVlKYXE0OFZzd3U3dENPdUVieTJ2dWlvNl82Y2Fpdng0Rmd2V041UnltejdaLTBMS0NpUnc2WlQtdjBGb2RIZmlVQlZKb2ZYWGdmdWZkeWRBUkI4OUY4S2VQVmZPQzJlMWJMdHNuaEpWb00tdHE3LWxfZDJLQXB4ZHRzVWljb0RjTEctQTRGelJ4US1WUmV3aWppYVAwUGs1MnfSAbMBQVVfeXFMTTUwV0ZuTDQtYm9sVWg0NFZCRkNDR2JEYVA5Tmt5SERUZUpwWDdNVVBSb2dGTGpHTjU5UmdUMjFmdjZPSE9UQkFxQlJTTUNLbzYzUXo2Q0UtaVlGc2RuLWJFOWxfWmtCWmdQOHhfeWxMQTgxNmF1N21yYjJQZjdoVnBLNDgwck1zX1M4U3lzTzFhRUY1ZHRZUC1Jd0dvcGZna3c2T3B1Zk5XNFFGLVdVT291aE0?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxQZTAzU2dvbVdZTzN2Smttc1pjc3lsSW5qWTdldDFETUFxNmx4Y2Z1RkZSNG5EcXR0bFlueDdLY2Y4cWxfdGxiYktmeWVDODhnclQ5eEpWZVZRVHlJZjhkalNMVlk1UUpKaW9IS3NRN3RVcnF1MHhEbnVaZWdQaThJRjdud3VSSGkxREdfWHVTelZxSGdXTXc?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNekw4czk1V0dBR21SMWtoS1ozbkVuWUhPTTR5cEtWTmNTd3JrdHM3UWg5RWItekxCMnJVcUhrZXBDTkJ3aDdPdktucTRUYWtjazFCV1p4a0xyMzBsS3NrMXdvOGlmaEViOGM4MTd4MmZQOW9sN0JTbmQxY3pyRjlTUjk2eXBCa0QwWFR0N1REdHhMMmRfb0x3anhnWQ?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxPZ0xRQ0RCX3RmbzdqVjRpTzAwSFZ0bTRGeTlCUzh5QXRpSlZRT0NWT3Y5YmhFU1AtdHA1ZmM1eGxDczBsdVFNUDYyd085VVJPaHFCRGZPZlZMWDZFX3hQM0p4M1UyQlZOYnlfRGY1eFNnbHFDSWdtUkN6TWE2R2VjQjlIZ09GODAxcDBmRVNUVTI1ME9xMks3WUo1U19nZ1I0ZEJQXzJ1R3VkRlU?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxNanM1bVhuU1dILWpuWnI0VFNfeTVDOW5ZNnNOdERKalBvSXpaOHdvUWlLUmRpc09ieXRCeUlXcWwwU0N3c0N5NXMtdHBHYUE2ejlLZGNNb180eDh4Y0hfd0Y4QV9zY1JGRFJ4STlKSjhMVWc2bXBvNmJhT2x2VDEtZ3dCNXJHbUNQa2tLX3I5N0Ewdm8zZW5wMVBsai1sOXNWWDFIN014bzA2VUMwNHU2Q2F5OERyVnh1U205d9IBwgFBVV95cUxPNjIydEQzdWR2V2NxRzFGRktPdG5jNkFpTW1UaVJUX2hCLTY1akVCVnpyNGViWW9pdTBXd1JMNHBOLWdILWtIek9sTW0zQW5WcHhKV09CWVRudzlSZ3pSSzRuZC14allOa0ZfaG5UTHVrWU9yOVoxZUVKUVlLb2NOU29RaDh5aTZlSk9Ub1lYSW9sa2ZKYW1vaDNVZlpjNEpMMWxNU0djYjJzVDhqVGpPTGw3VFBIUmZ0bHA1MTgzS1dCdw?oc=5
- https://news.google.com/rss/articles/CBMi4AFBVV95cUxQeTJ6NFlTUEVrSzlSZ2Q1UVNDakdTR2NkM3JuSHVVbkFfX3BWNnUyTE9pY1MwbTRDdmpndEoxOHRTeVR1TWdZb05PelJPd1FVVzZzMTdLbVNBeldwb2o0UGZTS0t2dUF0UUswZ3ozTWptalJwM3pRQXlDSXJQNjFnRG1IV1BJSWVHZjRBX2x2MUdHVzN1anNaXzhuWVVGbkVUQ3BpN2lya2x5V2diTHNHekNrTV9Ic0xMVUozS1ZhblgxWjkxdHBqYkFON3I5YWdKZXNjS2JHRk1aMW1ta2xuRA?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxNZG1iYzZKN2piZlZQOUthcnBZb3hYTlpwM3hXRjk4YmU1eWRVQ1o5T1MwVERqRjRXV20wZWUtNVpnN0VITzFrUkI0MzhxbEUxU3RkbzUxaV9BTFdMSFVTOENGdU1ZYTNIMGFfRW5OUkRVamEzeDFzT1V4T0VzWUpNaDVnWTdHYjN6UzVkVEhEX0VJWmdreEJ2YlVTWktZWTRwdk1YWFduRk56TXc?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxPcjBvOVFKU0RhSk5mZUNBYUo5Z3lHU3NUdEVOV0NBel8wVkJhX29TY2I3MWhVR3dFclVfM0JLOFNEdXNIblA1VV84b1VxOFlsZnJsaTFBYVlhZnRNeW1weU1fZ3pXYk5MOThWeXZLUGJMNkt5dS14T2JZZGZtbnUtaXNRTHhNbV9HSWo2ei1kRmNUUE00ZnN0emIySVVQVm8?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxPeXo2bXM2UVlsdURDYTdkaUx1U1YyOFBtRzhmSnhYaFdSZVhQR0ZZeGE3cWNaWTU4dWNNdUVSd0FpU1VaYkc5U09iaWhlSmV1ZDRDa19nWWRONklwT1BuSFY0Z2dZeUFkclNQSVlMN3RjOXpfY3BhZUZUUno1RnRBVkxjUk5yX21xOU9WMmtGOVYyRkUzdGhXT2d5TzZQQzZMSzF4NUhB?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxPRVlfbWZZcDEwUGVTaEJQcjlkSXlfWGd5Y0xwSkhnX2tNT3VQeG00VjZNQmVyVWY5NklHWFVwQ2phWXNZNU1LbXhqMjY0MTl1QVk4YTcyNGxpMzhVNVVITVFXUUxGM256VXdOV0RHRnh0dTJVQkp1NURnNVY4N1p1N21FUkpaOUVLekhVSG04aGpDNDEyV2Jj?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
