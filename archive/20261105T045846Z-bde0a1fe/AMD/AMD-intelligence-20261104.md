# AMD Intelligence Report

- ticker: **AMD**
- Report as_of: **2026-11-04**
- Market data as_of: **2026-11-04**
- Quant sources: https://finance.yahoo.com/quote/AMD/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AMD/key-statistics/
- AI analysis snapshot as_of: **2026-11-04**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-05T05:25:21.918338+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 8, 'ai': 14, 'unknown': 0, 'irrelevant': 2})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **3** exact headline/source/date matches; prior report **20261104T044411Z-6b13f9ec/AMD** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 22 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 8.33%; oldest publication 2026-11-02

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 488.7800 |
| Return 1D (%) | 1.0085 |
| Return 1W (%) | -15.5003 |
| Return 1M (%) | -22.8944 |
| Return YTD (%) | 128.2312 |
| Return 1Y (%) | 95.4729 |
| Annualized volatility (%) | 69.4399 |
| Beta vs SPY | 3.2864 |
| Max drawdown (%) | -28.1143 |
| Sharpe (rf=0) | 1.3142 |
| Downside deviation (rf=0, %) | 44.5536 |
| Sortino (rf=0) | 2.0483 |
| Historical VaR 95% (1D, %) | 6.3184 |
| Historical ES 95% (1D, %) | 8.7057 |
| Correlation vs SPY | 0.6076 |
| Tracking error vs SPY (%) | 62.4761 |
| P/E (trailing) | 123.43 |
| P/B | 12.65 |
| EV/EBITDA | 81.69 |
| Revenue growth (%) | 50.10 |
| Forward P/E (estimate) | 30.04 |
| Gross margin (%) | 55.72 |
| Operating margin (%) | 17.25 |
| Return on equity (%) | 10.20 |
| Free cash flow yield (%) | 1.11 |
| MA50 | 548.8970 |
| Close vs MA50 (%) | -10.9523 |
| MA200 | 414.2279 |
| Close vs MA200 (%) | 17.9978 |
| RSI (14, Wilder) | 39.4932 |
| MACD (12,26) | -19.9162 |
| MACD signal (9) | -10.8592 |
| MACD histogram | -9.0570 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AMD': 275, 'SPY': 275}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 488.7800 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.0085 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -15.5003 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -22.8944 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 128.2312 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 95.4729 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 69.4399 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 44.5536 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 2.0483 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 6.3184 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 8.7057 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6076 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 62.4761 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 3.2864 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -28.1143 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.3142 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 30.0421 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 55.7240 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 17.2500 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 10.1960 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.1081 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 123.4293 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 39.4932 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -9.0570 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -10.9523 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 17.9978 -> Clearly above the moving-average trend level.

## TAILWINDS

### AMD shares rise as AI-driven data-center strength fuels growth outlook
- Summary: AMD shares rise as AI-driven data-center strength fuels growth outlook
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxOT1otSGFrSy03TGU4SkFJWHJ0SlJER0pMU0FvV3RIZm1udEtsLTlqazJwbzFEX1lNR3NGYWdNRnRBMDc1ZEk0elNtb2xHcXFFOEFqSnVsWkVRSTBpeHBPUEwtNDZtSUxuZUpKSnM1aXFlX2VUczJlNWRFSXM3MGxmRXAyYkt0dUloMlhaYVJZUVhqNmU2cGVpNkJaMXY3Sm5Qck04ZjNtbHdBSC02Q3hxd3BR?oc=5>

### AMD Stock Jumps on Big Earnings Beat
- Summary: AMD Stock Jumps on Big Earnings Beat
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMidEFVX3lxTE9mcnlEQzhqWExyWFlMNDhsWkRvc2VrVmtkR2tqUXJzQWZBWGh2UzMySGZqUjhEN3dQcFhEWGpUczZnUHJ3WFB4cEJOUDhIMHlwaGxpRGI4YmlUclBaVkVBWHFoNmhBckFUU1ctUllKaF96bTB6?oc=5>

### AMD Stock Pops on $17B Q4 Revenue Guide. Traders Shouldn't Overlook a $3B Inventory Gamble and Collapsing Free Cash Flow.
- Summary: AMD Stock Pops on $17B Q4 Revenue Guide. Traders Shouldn't Overlook a $3B Inventory Gamble and Collapsing Free Cash Flow.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi8wFBVV95cUxNRThLTzdDblZFVl9UR0FwWUxGaEJjV3IydzZ2b0JldC1fd0JiMkY2UlNBVUZ5YU01cUdGdnY5eU9TWmhZOElTVU1ocHlISERaRVplVFBvWHBQYk9tcHVOR3pFeVdkU18yX0lITHB2eGFxWXZyUS1hbkVtQmhSMHlRSm5IU3pybG1UZVJUY1FNOXg4RGFwckg1SmM1c0xNZTVwUEd6QzRBOXExMEQ5eUdFemdGVWI5T1BvNlpnS21Ba1VYUGlIcTRJRTlPbHpUV3ZOa0h2RFc5Um5GTUF0N3YzdkwxcXpwZ2ZPSmpxaFZmRmhmWms?oc=5>

### AMD gains 4% as revenue guidance top estimates amid strong AI chip demand
- Summary: AMD gains 4% as revenue guidance top estimates amid strong AI chip demand
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxQRG43Ym5NZlcwNFlXa3FGTTAyazdIZkh0Wjk4M00xNHhSXzh1ajRhbE45cG40U2RBNHZydEJ6Y3NrY0tsS3ZyQ3hqTW9XU2Nab3NiWTVzVk5EVUktZW5RU3pObXdCTmRSVk9WM2ZYWVBtdWl0RHZHeVowVHFsYzdZYVdiYmUxS0xORGIyTTdXNUdIOWp4TlVlVk5Da2V0ZFpOR2JBaWs1VVhaOVhBOWxGSVAwbTJjUXdBeDVEM3lydVRMdlFycktj?oc=5>

### AMD Stock Surges After Hours As Q3 Sales Surge 45% On AI Boom, And Expectations For 80% Revenue Jump In 2027
- Summary: AMD Stock Surges After Hours As Q3 Sales Surge 45% On AI Boom, And Expectations For 80% Revenue Jump In 2027
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxOeWo2RGNLM050TUp5amI0MHZ0VmpiR1d0bG05S3BlSkUyY2QwdDRwNGw5VzFoaDJ3Rm42bk5NbGpWSGNQdGg3aHJwZFRKNTQ1RWFkeGs2Zjd1ZVRxMVo4R2JTUDV1U0k5UWFjRW5QVzIyTFNfYmdMSUNKUjkySm1XM0gwNEt5ejQwSi1md2lfbGM5ZjFQNFZveWppUUlzb2FhSFRKLVZKM3RyeDJQMXNaTGZlOG1lN3M?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### AMD's data center revenue nearly doubles in Q3 and CEO Su expects growth to accelerate
- Summary: AMD's data center revenue nearly doubles in Q3 and CEO Su expects growth to accelerate
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMieEFVX3lxTFBfVXVMaFFzOXpSSmhDS2xlZWZLZDk0V2w5MHpTSnZ3d2c5bkMzRDhwbzhURWpMMVcwX3ZiME8ybmU4UHR1ekdtVlUwRTYxcTI0T1dadVhheUQ0LVVpWnRqYjdmeDkxMGJKQXBkNUtpaEVKZVlXNEhYRdIBfkFVX3lxTFAwT0pLTUtFX3FhLU4tWFFuU3JjMXF4NWxpWFNVZEoxeTdqMVc2d201ZHRMdXV4cEg4VGNnd0RDRmhKbnNYZndMa1hhMzZ3Y0lUdk82SUprYVVibVZQT19vR05WaGZKZlBzcDFLZWNzczZkb0pDN180UTZ5MTRuUQ?oc=5>

### Advanced Micro Devices (NASDAQ:AMD) Stock Gets Price Target Bump from JPMorgan Chase & Co.
- Summary: Advanced Micro Devices (NASDAQ:AMD) Stock Gets Price Target Bump from JPMorgan Chase & Co.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi4AFBVV95cUxQQ0Zvem5TVGpTVGhITm1qNEhVci10cGZPck4zZ2U0UTdKM3JfcDYzVDBtMjlSalR6ajFvV2xrdUpWMVNRSlhKSlhiaU93MXdWV29wN3VtWmdPUk9PS2RCRFBid2RfMVp1OU1iZ2YtQ1dQcmdHWkJ5X1NDTFVHNUhjaGoyLTZLc2dFczRyc2h0T3ZXczV2cEtPY1RSMUZocVFCZkZFOUwyZkV2VjZpNHJpUm9MODAtYlNHUU02VjcyMVZ1Y1lGVUtNSHJqcm5KMGdWQ1pISzA0SXA3Wm8xcGZfNw?oc=5>

### AMD chips in to market boost as it doubles data centre revenue
- Summary: AMD chips in to market boost as it doubles data centre revenue
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizAFBVV95cUxOOTNIY1JLQjkyaHNzaG1qcmZjc1l0ajdMVTJYS1pVcjFGeVdNYVVidENJbFUxekJXU2ZZQmRsTUY0ejJqUV9MamRtdHNTWkgta1o0RDFLOGtwV2g1T3I4YjJOS0JjN2pHcE1zcHpHbTcteHlwbkgtTG9LUURYc3NWNTNXVTh0OUtuczVZdkNqNFNmWmMwOXEyVGVVWHhCdk5Vd0x4Y1RkMVpPQUpwNHU3SnhxWGdhWUpxVnVsMGtpYms3ekFTUXYxUGRMQzk?oc=5>

### Here’s How Much Traders Expect AMD Stock to Move After Earnings
- Summary: Traders forecast AMD stock movement post-earnings.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxOUzk2TFExUnNScHk1cVdXaHlHMGUxWGhoQVlIWDY3MnE3NnctbVhnYUtERlZFTEw1bjFuVmo5TkRVZC11WWhncHFWb3IybUF3ZjYyWU1kRmlYWTVoOENVaVNHVmY3aVhNZU00VFJfX0VHem1ZRU1mYURPMUxBQVVzZkxKQnVZdW5PR2FoMm1PZnZCeDlTUDQwTTJR?oc=5>

### AMD Forecast Exceeds Estimates After AI Chip Demand Soars
- Summary: AMD's forecast surpassed estimates amid rising AI chip demand.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxQYURlOUxxRUMybEdmbkJoTHZiZEVTTUtCN0gyZ1RsV0s3YlEteXR1NFZIWDNwXzJKTUdCRUpJY0RWNlRqVC02M0VaMFgtY0piUFNGSkhKQmZ3bTVwMHFERHN6ZExPSnVFbWdBWDYxQnNnX0RJRnF6QVlld0FBeDhySGlrUEZ4bEtmWkkybFFVRU9EcnhRd2F5c1M1eGc2OFk5VG95X0dUa1dWUGhPZzJJ?oc=5>

### Ahead of Advanced Micro Devices Earnings, Here’s What Barchart Data Says Comes Next for AMD Stock
- Summary: Barchart data predicts next moves for AMD ahead of earnings.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxQbXJodzQtaWtBSi1tRFpVZ1VyQ0tObE5BOU5uY2htQU4ya0Fncm1ITE5xYXhoNlp5NUlwTGIxQ0ZfejExYzZvMXJYSUg0bUo4bE1fU3lOSTgyeS11U0YzRTZEODZncjVvTmtjeTdwWHJSMVVNY2E1QTlSbTdJMnpfZV92NUhSSEM4eGNjN0JyenFCWEo2OURpNmt6Z1AwaXhqMFVEVWgxa2NTbUJkSU92V3ZRVEVUeGgxaXhma2N6aXFXWjRyaGNTbkVWT1hkT3VuZzBYWlV3?oc=5>

### Stock Market Mostly Higher On Election Day, But Apple, Shopify Slide; AMD Jumps Late
- Summary: AMD shares rise late in a market that was mostly higher on Election Day.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxPNWp4aG5EV1lESkNTbGR1eElCYVFlUmNELVBSZE5nUmxDenoxRzVzQnZDY3hRczFrdUNwa0pxZHZXT0ZTWWhmbzAtSWNYdEFNTnpMaWFyZWlpanlISHZ1cXpNXzJ6ci1OeUc0bWN5VHlvMmVnQzFVckVCV1ZvU2tEMXdLbkpfSVdGZ0p6aHBnSFRYaGtEcXctYkdPN2YwT08xa0tKbldNaVhtaVBkc2ZmZmd4RzJaajkxMjVDaQ?oc=5>

### AMD Beats Wall Street Expectations as It Pivots to Data-Center First Status
- Summary: AMD exceeded earnings expectations by shifting focus to data‑center products.
- Date: 2026-11-03 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxQTS1ackJyUFczU0ZLRnVmUkF2M2M2MUtueVFjd3ZpOEVkSlJQRWY3eUFNa2g2MVlHOTJDZTROanJCRkMzN0k0S0s2WWh6c2VMVW84VklCRmNBdW5CcmlMYzFXX2RpNmp2UDNPbjNWOFZRMVJUYWtyQkcxX0NPTE1FZU1TXzQ4d2VmaXZkNEVRNTRsQUVPTlUtcXIxRUg5endOZVZyT29sYmtEbmhCQ2pxUA?oc=5>

### AMD Stock Rebounds. Is Its AI Edge Built to Last?
- Summary: AMD shares rebound, raising questions about the durability of its AI advantage.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxQa2QyOEhVWC1zVkxzSm02XzRfaDBwOC1DeHZ2ckl5WHlMXy1BOGpqeUNJUVlKckVOZlcyUHIxeGotbWhsS0xsdXNBeXVQWC12YnVUWEI2LTdiUnhtSkp3aUN0OXdHNGJXTkVaOGYwblVJaHF0NlpwQjRDLVhPS2trcDRnWVVmbzdFT0dCUFRsNEh2azNa?oc=5>

### The Case For AMD And SOXX: Semis Are In Bear Territory, AMD Says Demand Is Fine (AMD)
- Summary: AMD maintains demand outlook despite bear market, suggesting guidance optimism.
- Date: 2026-11-04 | Impact: medium | Horizon: medium | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxOaElQbi1TTUZudW1qNGtHSmNZam12a0ZfeHQwSXlIWHBDSTcyQ1BwdTlBOHVxX2ZkdWFhMExKa3AyZUNuRDZxWV9uaFNZdmJ5VERCUWUyay1JVEtzT1FGc2xnbDgtb19DVFYzTUt3MDZLMW1LVlBwZ04zQ01rM3R6bHdxQ2JtQ1dHbDliNi00ZThQYnlwTlFRTEFfT3ZEYXFqS3RBMG9KbnFWSHYtOUZrTE1LLThMajFQV1E?oc=5>

### Goldman Sachs’ $675 Target Says AMD’s Selloff Went Too Far
- Summary: Analyst downgrade to $675 indicates selloff was excessive, negative outlook.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxPbDhyT0VfMURCOV9YSG9tQWp5UjdfZGF6WGlVbExrQmNZdDZEcHRyR0ZDcTd0WkJsZlp3NDEwYTdDSkdQaVRIeGc3alY0UUd5UEh2S1N0M1Q5c185cUVyR2RXNDFqYjRxZUpzV096Ykd6a0psTTJPQ09USmI5ZU90WTE3OWhrbUExemc?oc=5>

### Intel Drops 5%, NVIDIA Retreats 2% After AMD Earnings Beat and Strong 2027 Outlook as Intel Falls 3%; AMD Stock Goes Nowhere
- Summary: AMD beat earnings and projected strong 2027 outlook, but its stock remained flat amid broader market moves.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMi9gFBVV95cUxPVnlhSjhhcGtkM1VvZ1BqMEVhR0d0QWNlaXNfYXNBS3ItR3dIX0k5SS1mQjlqUFBTM0tqa1F6SExNWndUeC1VSzZDNmtwYjVzb0piU3c4MFdlQ0MwdUZBVHVRbTZaT0QwX3llODFMc1A0M1pyLXNJRkJ5MkZRXzJCWUJYUG1RSm9ySVZfb2lhRGtzQVV5ZHBHWk1MQlJRcHZkaGJjNnNEZWpWUDZsbkxJSVZpUWw3Z3FrUEF0cG9hclZwdE1YTHYtNlFndW5pNWRiajlJUTVIcXNNeU93NWJPSWZFSTdUblp4cXVfRUpZM2FIZXV3T3c?oc=5>

### AMD Is Growing Twice as Fast as Intel - Intel (NASDAQ:INTC), Advanced Micro Devices (NASDAQ:AMD)
- Summary: AMD’s growth rate is double that of Intel, highlighting competitive advantage.
- Date: 2026-11-04 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihwFBVV95cUxNcFczQjMxNWtVcDIxRGMtUmlOOHhoQlJadWRIVTZQc2g5RFlkYTZjdE9sajFXQTVKakEyRk9MM083SjFqV0V4Tm51YzBuRHNxQzVLT19zdjd4OHQzTmoydnJSVUNzT0dtQ2FKbUFtWWlld09ScEJCMVJEN0pVVWlyQTQ5WDZ6RXM?oc=5>

### Advanced Micro Devices (NASDAQ:AMD) Q3 2026 Earnings: Data Center Nearly Doubles and Guidance Tops Consensus
- Summary: Q3 earnings show data center revenue nearly doubled; guidance exceeds consensus expectations.
- Date: 2026-11-03 | Impact: high | Horizon: short | Confidence: 0.97
- Sources: <https://news.google.com/rss/articles/CBMi6wFBVV95cUxNV0swN190MXdjV0QxZWoxR3I2ZTJMVXJCNVFNWk56UDBRVlFRaDZ6YnV6blEyd2RXb2NJRTNpSWd2Q2tqX3VSSU8yT0tlX3kyZ3NQYlVIVjBITEVmQ3NfbThNdlg2cHdqVnFTbDc1WDBjclZvNDc1MXZvd2dqdXVsNHhrYjc3MGtpaURFa3Q0QldlTHBvcWZqSC1ER29jRnd5RzFpeGoxZ1ZXRmplbl9mSl9xbDZkQ1hWWWI1NUNVeHBneDBqVFQxUmNUVzZYeUZ1N3kySWNVdlBoZFJHTThrZW5xSmhGd1ZZelNv?oc=5>

### AMD Earnings: Strong Data Center Outlook Points to Upside for Stock
- Summary: Strong data center outlook suggests potential upside for AMD shares.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxOaEkyb2htSzVuS3VET3VLa1NHd0dYOThyQ19XdU5yQm43VzZOS1VnMHctbjhLZWlPZTQ1dFktWk1zX0NYWnJzenJXVGpDcGFUanR4ZUR5Rnd1VENMMGRnRTd0SVBKTDVTQ0g4SE5ubDVpWmFPOHhDZEZ5RFV1aFdkQmtFUGF0SGdTX2YyYnlsMHlHZWNLMXY1YVJB?oc=5>

### ‘There’s a Cheaper Option,’ Says Top Investor About AMD Stock
- Summary: Top investor views AMD stock as a cheaper alternative, implying potential value.
- Date: 2026-11-04 | Impact: low | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxOUGk0dVRzMks1Uy1PRzFLS2hmOFI5VHdaLWgwZGdNNHdhb2FnN0VZSFRBaXFOeXdHeW9BdGxJZFgyR3pFdkJZelNTMUdnYktGMmM2MlJNZWFkbzFQSktOWjdCc2lsdWt6WUx3ZkluSTE1U2tZV3pDZFRlQS1nVUlWUVZEcFBvQlItOUowdThGel9zVkRfMXlwLUlIZw?oc=5>

### Advanced Micro Devices (AMD): AI Data Center Sales Jump 107% as Helios Racks Roll Out
- Summary: AMD reports a 107% increase in AI data center sales with Helios rack deployments, signaling strong demand and revenue growth.
- Date: 2026-11-04 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxPR2pidFhaWmRFZ2Y3Nzg3SFB1YUIxRExMcFY1Z1RTc0NDOWVMUGh5MHBrb2xNNnd6bVBNSlRMNXE3YlpaeUtfMkZ2c2NNT1E5b0lsaVZHaml1RjdyQ3k3bnJ5SElZYmRJNEhqU2hhaUsydWVvNUVrdzhwTTlxT2pVSzFmMUlyakFDWDNSYU9Od2FDQWJlUnJsZA?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AMD** | **123.43** | **12.65** | **81.69** | **50.10** | **797,921,116,160.00 USD** | **95.47** |
| NVDA | 25.30 | 21.10 | 23.85 | 105.90 | 4,832,539,181,056.00 USD | 0.97 |
| INTC | N/A | 2.69 | 16.85 | 20.90 | 309,705,048,064.00 USD | 57.36 |
| AVGO | 42.44 | 15.59 | 30.41 | 85.50 | 1,553,721,065,472.00 USD | -6.83 |

Peers fetched as_of: 2026-11-04; AMD reuses existing data (market data as_of: 2026-11-04); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-03
- Next expected earnings: 2027-02-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-04

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-04
- Revenue (latest available single quarter): 1,584,000,000.00 USD; period 2017-07-02/2017-09-30; fiscal year/reporting period 2018/Q3
- Net income (latest available single quarter): 2,428,000,000.00 USD; period 2026-06-28/2026-09-26; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/2488/000000248826000191/amd-20260926.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMisgFBVV95cUxOT1otSGFrSy03TGU4SkFJWHJ0SlJER0pMU0FvV3RIZm1udEtsLTlqazJwbzFEX1lNR3NGYWdNRnRBMDc1ZEk0elNtb2xHcXFFOEFqSnVsWkVRSTBpeHBPUEwtNDZtSUxuZUpKSnM1aXFlX2VUczJlNWRFSXM3MGxmRXAyYkt0dUloMlhaYVJZUVhqNmU2cGVpNkJaMXY3Sm5Qck04ZjNtbHdBSC02Q3hxd3BR?oc=5
- https://news.google.com/rss/articles/CBMidEFVX3lxTE9mcnlEQzhqWExyWFlMNDhsWkRvc2VrVmtkR2tqUXJzQWZBWGh2UzMySGZqUjhEN3dQcFhEWGpUczZnUHJ3WFB4cEJOUDhIMHlwaGxpRGI4YmlUclBaVkVBWHFoNmhBckFUU1ctUllKaF96bTB6?oc=5
- https://news.google.com/rss/articles/CBMi8wFBVV95cUxNRThLTzdDblZFVl9UR0FwWUxGaEJjV3IydzZ2b0JldC1fd0JiMkY2UlNBVUZ5YU01cUdGdnY5eU9TWmhZOElTVU1ocHlISERaRVplVFBvWHBQYk9tcHVOR3pFeVdkU18yX0lITHB2eGFxWXZyUS1hbkVtQmhSMHlRSm5IU3pybG1UZVJUY1FNOXg4RGFwckg1SmM1c0xNZTVwUEd6QzRBOXExMEQ5eUdFemdGVWI5T1BvNlpnS21Ba1VYUGlIcTRJRTlPbHpUV3ZOa0h2RFc5Um5GTUF0N3YzdkwxcXpwZ2ZPSmpxaFZmRmhmWms?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxQRG43Ym5NZlcwNFlXa3FGTTAyazdIZkh0Wjk4M00xNHhSXzh1ajRhbE45cG40U2RBNHZydEJ6Y3NrY0tsS3ZyQ3hqTW9XU2Nab3NiWTVzVk5EVUktZW5RU3pObXdCTmRSVk9WM2ZYWVBtdWl0RHZHeVowVHFsYzdZYVdiYmUxS0xORGIyTTdXNUdIOWp4TlVlVk5Da2V0ZFpOR2JBaWs1VVhaOVhBOWxGSVAwbTJjUXdBeDVEM3lydVRMdlFycktj?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxOeWo2RGNLM050TUp5amI0MHZ0VmpiR1d0bG05S3BlSkUyY2QwdDRwNGw5VzFoaDJ3Rm42bk5NbGpWSGNQdGg3aHJwZFRKNTQ1RWFkeGs2Zjd1ZVRxMVo4R2JTUDV1U0k5UWFjRW5QVzIyTFNfYmdMSUNKUjkySm1XM0gwNEt5ejQwSi1md2lfbGM5ZjFQNFZveWppUUlzb2FhSFRKLVZKM3RyeDJQMXNaTGZlOG1lN3M?oc=5
- https://news.google.com/rss/articles/CBMieEFVX3lxTFBfVXVMaFFzOXpSSmhDS2xlZWZLZDk0V2w5MHpTSnZ3d2c5bkMzRDhwbzhURWpMMVcwX3ZiME8ybmU4UHR1ekdtVlUwRTYxcTI0T1dadVhheUQ0LVVpWnRqYjdmeDkxMGJKQXBkNUtpaEVKZVlXNEhYRdIBfkFVX3lxTFAwT0pLTUtFX3FhLU4tWFFuU3JjMXF4NWxpWFNVZEoxeTdqMVc2d201ZHRMdXV4cEg4VGNnd0RDRmhKbnNYZndMa1hhMzZ3Y0lUdk82SUprYVVibVZQT19vR05WaGZKZlBzcDFLZWNzczZkb0pDN180UTZ5MTRuUQ?oc=5
- https://news.google.com/rss/articles/CBMi4AFBVV95cUxQQ0Zvem5TVGpTVGhITm1qNEhVci10cGZPck4zZ2U0UTdKM3JfcDYzVDBtMjlSalR6ajFvV2xrdUpWMVNRSlhKSlhiaU93MXdWV29wN3VtWmdPUk9PS2RCRFBid2RfMVp1OU1iZ2YtQ1dQcmdHWkJ5X1NDTFVHNUhjaGoyLTZLc2dFczRyc2h0T3ZXczV2cEtPY1RSMUZocVFCZkZFOUwyZkV2VjZpNHJpUm9MODAtYlNHUU02VjcyMVZ1Y1lGVUtNSHJqcm5KMGdWQ1pISzA0SXA3Wm8xcGZfNw?oc=5
- https://news.google.com/rss/articles/CBMizAFBVV95cUxOOTNIY1JLQjkyaHNzaG1qcmZjc1l0ajdMVTJYS1pVcjFGeVdNYVVidENJbFUxekJXU2ZZQmRsTUY0ejJqUV9MamRtdHNTWkgta1o0RDFLOGtwV2g1T3I4YjJOS0JjN2pHcE1zcHpHbTcteHlwbkgtTG9LUURYc3NWNTNXVTh0OUtuczVZdkNqNFNmWmMwOXEyVGVVWHhCdk5Vd0x4Y1RkMVpPQUpwNHU3SnhxWGdhWUpxVnVsMGtpYms3ekFTUXYxUGRMQzk?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxOUzk2TFExUnNScHk1cVdXaHlHMGUxWGhoQVlIWDY3MnE3NnctbVhnYUtERlZFTEw1bjFuVmo5TkRVZC11WWhncHFWb3IybUF3ZjYyWU1kRmlYWTVoOENVaVNHVmY3aVhNZU00VFJfX0VHem1ZRU1mYURPMUxBQVVzZkxKQnVZdW5PR2FoMm1PZnZCeDlTUDQwTTJR?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxQYURlOUxxRUMybEdmbkJoTHZiZEVTTUtCN0gyZ1RsV0s3YlEteXR1NFZIWDNwXzJKTUdCRUpJY0RWNlRqVC02M0VaMFgtY0piUFNGSkhKQmZ3bTVwMHFERHN6ZExPSnVFbWdBWDYxQnNnX0RJRnF6QVlld0FBeDhySGlrUEZ4bEtmWkkybFFVRU9EcnhRd2F5c1M1eGc2OFk5VG95X0dUa1dWUGhPZzJJ?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxQbXJodzQtaWtBSi1tRFpVZ1VyQ0tObE5BOU5uY2htQU4ya0Fncm1ITE5xYXhoNlp5NUlwTGIxQ0ZfejExYzZvMXJYSUg0bUo4bE1fU3lOSTgyeS11U0YzRTZEODZncjVvTmtjeTdwWHJSMVVNY2E1QTlSbTdJMnpfZV92NUhSSEM4eGNjN0JyenFCWEo2OURpNmt6Z1AwaXhqMFVEVWgxa2NTbUJkSU92V3ZRVEVUeGgxaXhma2N6aXFXWjRyaGNTbkVWT1hkT3VuZzBYWlV3?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxPNWp4aG5EV1lESkNTbGR1eElCYVFlUmNELVBSZE5nUmxDenoxRzVzQnZDY3hRczFrdUNwa0pxZHZXT0ZTWWhmbzAtSWNYdEFNTnpMaWFyZWlpanlISHZ1cXpNXzJ6ci1OeUc0bWN5VHlvMmVnQzFVckVCV1ZvU2tEMXdLbkpfSVdGZ0p6aHBnSFRYaGtEcXctYkdPN2YwT08xa0tKbldNaVhtaVBkc2ZmZmd4RzJaajkxMjVDaQ?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxQTS1ackJyUFczU0ZLRnVmUkF2M2M2MUtueVFjd3ZpOEVkSlJQRWY3eUFNa2g2MVlHOTJDZTROanJCRkMzN0k0S0s2WWh6c2VMVW84VklCRmNBdW5CcmlMYzFXX2RpNmp2UDNPbjNWOFZRMVJUYWtyQkcxX0NPTE1FZU1TXzQ4d2VmaXZkNEVRNTRsQUVPTlUtcXIxRUg5endOZVZyT29sYmtEbmhCQ2pxUA?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxQa2QyOEhVWC1zVkxzSm02XzRfaDBwOC1DeHZ2ckl5WHlMXy1BOGpqeUNJUVlKckVOZlcyUHIxeGotbWhsS0xsdXNBeXVQWC12YnVUWEI2LTdiUnhtSkp3aUN0OXdHNGJXTkVaOGYwblVJaHF0NlpwQjRDLVhPS2trcDRnWVVmbzdFT0dCUFRsNEh2azNa?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxOaElQbi1TTUZudW1qNGtHSmNZam12a0ZfeHQwSXlIWHBDSTcyQ1BwdTlBOHVxX2ZkdWFhMExKa3AyZUNuRDZxWV9uaFNZdmJ5VERCUWUyay1JVEtzT1FGc2xnbDgtb19DVFYzTUt3MDZLMW1LVlBwZ04zQ01rM3R6bHdxQ2JtQ1dHbDliNi00ZThQYnlwTlFRTEFfT3ZEYXFqS3RBMG9KbnFWSHYtOUZrTE1LLThMajFQV1E?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxPbDhyT0VfMURCOV9YSG9tQWp5UjdfZGF6WGlVbExrQmNZdDZEcHRyR0ZDcTd0WkJsZlp3NDEwYTdDSkdQaVRIeGc3alY0UUd5UEh2S1N0M1Q5c185cUVyR2RXNDFqYjRxZUpzV096Ykd6a0psTTJPQ09USmI5ZU90WTE3OWhrbUExemc?oc=5
- https://news.google.com/rss/articles/CBMi9gFBVV95cUxPVnlhSjhhcGtkM1VvZ1BqMEVhR0d0QWNlaXNfYXNBS3ItR3dIX0k5SS1mQjlqUFBTM0tqa1F6SExNWndUeC1VSzZDNmtwYjVzb0piU3c4MFdlQ0MwdUZBVHVRbTZaT0QwX3llODFMc1A0M1pyLXNJRkJ5MkZRXzJCWUJYUG1RSm9ySVZfb2lhRGtzQVV5ZHBHWk1MQlJRcHZkaGJjNnNEZWpWUDZsbkxJSVZpUWw3Z3FrUEF0cG9hclZwdE1YTHYtNlFndW5pNWRiajlJUTVIcXNNeU93NWJPSWZFSTdUblp4cXVfRUpZM2FIZXV3T3c?oc=5
- https://news.google.com/rss/articles/CBMihwFBVV95cUxNcFczQjMxNWtVcDIxRGMtUmlOOHhoQlJadWRIVTZQc2g5RFlkYTZjdE9sajFXQTVKakEyRk9MM083SjFqV0V4Tm51YzBuRHNxQzVLT19zdjd4OHQzTmoydnJSVUNzT0dtQ2FKbUFtWWlld09ScEJCMVJEN0pVVWlyQTQ5WDZ6RXM?oc=5
- https://news.google.com/rss/articles/CBMi6wFBVV95cUxNV0swN190MXdjV0QxZWoxR3I2ZTJMVXJCNVFNWk56UDBRVlFRaDZ6YnV6blEyd2RXb2NJRTNpSWd2Q2tqX3VSSU8yT0tlX3kyZ3NQYlVIVjBITEVmQ3NfbThNdlg2cHdqVnFTbDc1WDBjclZvNDc1MXZvd2dqdXVsNHhrYjc3MGtpaURFa3Q0QldlTHBvcWZqSC1ER29jRnd5RzFpeGoxZ1ZXRmplbl9mSl9xbDZkQ1hWWWI1NUNVeHBneDBqVFQxUmNUVzZYeUZ1N3kySWNVdlBoZFJHTThrZW5xSmhGd1ZZelNv?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxOaEkyb2htSzVuS3VET3VLa1NHd0dYOThyQ19XdU5yQm43VzZOS1VnMHctbjhLZWlPZTQ1dFktWk1zX0NYWnJzenJXVGpDcGFUanR4ZUR5Rnd1VENMMGRnRTd0SVBKTDVTQ0g4SE5ubDVpWmFPOHhDZEZ5RFV1aFdkQmtFUGF0SGdTX2YyYnlsMHlHZWNLMXY1YVJB?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxPdUdGaXRMT19sZ0xxbk1fVnV6Qlg2MUNPRndSWmJwU2o2ZThDczhEd2gzZi1XSHpMOWt1NEU5eENBTWJLM0dweTNDUERJR01HdVB4WWx3WUNiSnNkQ05UYkxXVWwtSjhMejF0WEowdXN4U3I3cDJsSl9yUkZDcThBTWJUNFlaZ2RSRUNlajZZMjlvVDVWOHFLMW10UXdId3QwckdxQ2p3?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxOUGk0dVRzMks1Uy1PRzFLS2hmOFI5VHdaLWgwZGdNNHdhb2FnN0VZSFRBaXFOeXdHeW9BdGxJZFgyR3pFdkJZelNTMUdnYktGMmM2MlJNZWFkbzFQSktOWjdCc2lsdWt6WUx3ZkluSTE1U2tZV3pDZFRlQS1nVUlWUVZEcFBvQlItOUowdThGel9zVkRfMXlwLUlIZw?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxPR2pidFhaWmRFZ2Y3Nzg3SFB1YUIxRExMcFY1Z1RTc0NDOWVMUGh5MHBrb2xNNnd6bVBNSlRMNXE3YlpaeUtfMkZ2c2NNT1E5b0lsaVZHaml1RjdyQ3k3bnJ5SElZYmRJNEhqU2hhaUsydWVvNUVrdzhwTTlxT2pVSzFmMUlyakFDWDNSYU9Od2FDQWJlUnJsZA?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
