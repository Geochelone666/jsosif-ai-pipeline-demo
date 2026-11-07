# AMD Intelligence Report

- ticker: **AMD**
- Report as_of: **2026-11-06**
- Market data as_of: **2026-11-06**
- Quant sources: https://finance.yahoo.com/quote/AMD/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AMD/key-statistics/
- AI analysis snapshot as_of: **2026-11-06**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-07T04:36:45.061507+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 4, 'ai': 14, 'unknown': 0, 'irrelevant': 7})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **4** exact headline/source/date matches; prior report **20261106T045829Z-1db1e5a7/AMD** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 18 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 24.0%; oldest publication 2026-11-03

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 449.0400 |
| Return 1D (%) | 11.0386 |
| Return 1W (%) | -11.0460 |
| Return 1M (%) | -30.8552 |
| Return YTD (%) | 109.6750 |
| Return 1Y (%) | 88.9104 |
| Annualized volatility (%) | 72.0180 |
| Beta vs SPY | 3.3469 |
| Max drawdown (%) | -37.7290 |
| Sharpe (rf=0) | 1.2467 |
| Downside deviation (rf=0, %) | 47.2356 |
| Sortino (rf=0) | 1.9008 |
| Historical VaR 95% (1D, %) | 6.3184 |
| Historical ES 95% (1D, %) | 9.4746 |
| Correlation vs SPY | 0.6297 |
| Tracking error vs SPY (%) | 64.3521 |
| P/E (trailing) | 95.95 |
| P/B | 10.77 |
| EV/EBITDA | 65.50 |
| Revenue growth (%) | 44.70 |
| Forward P/E (estimate) | 26.00 |
| Gross margin (%) | 56.00 |
| Operating margin (%) | 21.17 |
| Return on equity (%) | 11.96 |
| Free cash flow yield (%) | 1.00 |
| MA50 | 546.8138 |
| Close vs MA50 (%) | -17.8806 |
| MA200 | 415.9775 |
| Close vs MA200 (%) | 7.9481 |
| RSI (14, Wilder) | 38.4071 |
| MACD (12,26) | -30.2042 |
| MACD signal (9) | -17.4482 |
| MACD histogram | -12.7559 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AMD': 277, 'SPY': 277}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 449.0400 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 11.0386 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -11.0460 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -30.8552 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 109.6750 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 88.9104 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 72.0180 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 47.2356 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.9008 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 6.3184 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 9.4746 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6297 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 64.3521 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 3.3469 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -37.7290 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.2467 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 26.0017 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 56.0000 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 21.1710 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 11.9600 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 0.9990 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 95.9487 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 38.4071 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -12.7559 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -17.8806 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 7.9481 -> Clearly above the moving-average trend level.

## TAILWINDS

### AMD shares rise as AI-driven data-center strength fuels growth outlook
- Summary: AMD shares rise as AI-driven data-center strength fuels growth outlook
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxOT1otSGFrSy03TGU4SkFJWHJ0SlJER0pMU0FvV3RIZm1udEtsLTlqazJwbzFEX1lNR3NGYWdNRnRBMDc1ZEk0elNtb2xHcXFFOEFqSnVsWkVRSTBpeHBPUEwtNDZtSUxuZUpKSnM1aXFlX2VUczJlNWRFSXM3MGxmRXAyYkt0dUloMlhaYVJZUVhqNmU2cGVpNkJaMXY3Sm5Qck04ZjNtbHdBSC02Q3hxd3BR?oc=5>

### Advanced Micro Devices (NASDAQ:AMD) Stock Jumps 11% - Here's Why
- Summary: Advanced Micro Devices (NASDAQ:AMD) Stock Jumps 11% - Here's Why
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxNWDNFTnhjZXZBMG9SeVBNemhLMTNoRUZhcW5yZm9iRnhJdExncG5COXBCX2dQakpxQ1NudzNsX1RjazBWMzR2dEc5ejg2REV1dXBMSWR6emRYdWZwSl95Zm1BWFc1WDFCU3pPcGJMUG5MSlpnblhVQzlHTURPNDB4MXBIRHZmSkNvMzN3c1lOUzQyQWVwek50Wm84U3BuSGZmQVd2SUl3QnRKdXViRUpJaTBsTW9OUXVaNGc?oc=5>

### AMD Posts Beat-And-Raise Report On Record AI Data-Center Sales
- Summary: AMD exceeded earnings expectations with record AI data‑center sales, boosting investor confidence.
- Date: 2026-11-03 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMieEFVX3lxTE1XUlpyMXlqcVpLcWt5MHZGLWJZd1FXVDlUTDlMTUhrMjVuOGNtMmhDUmFsang0MVN4RmRTR0o3TFk2Zndka1ZkWWp1QzViaEhkbmcxdXpZejRKWEV2enFDb3NZNmNzb3R5STEtclNmZk1DOUxQemZWQQ?oc=5>

### Nvidia, AMD and other chip stocks rebound — but is relief from the ‘violent’ selloff only temporary?
- Summary: Chip stocks, including AMD, recover after a sharp selloff, raising questions about the durability of the rebound.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxOS05rMlNIQXZwWGRFbUlERjJ6bXlobEFuV19nckJuSlpWZlpKYmJvd1c0Z0FiOGtqc0FaeTItWDBsUkZJY044ZnV0emk5dlBjcVFtNkxBM2xGbzhmRi1adk9XNXpIZVpYNXRubUcwOVNYcHZJVjFzMEducG1pMXFscE9rX0xJazdhaHh0UDZUN3gzZ19aRm4xOG1acE5ONXBVeUVKM1dBb0ZYRjdrUGZNTzBhaEs?oc=5>

### AMD Jumps 8%, Intel and NVIDIA Climb 5% as Chip Stocks Rebound From Worst Sell-Off Since 2020
- Summary: AMD shares rise 8% amid broader chip market rebound.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMizwFBVV95cUxPa01iWmYtRkh1S3plOXhjRGlOVGg1RzZfUS1yRzA3REs1MTFmb0NYQWJRYmNWSlRVYjlnV1hnMm5IT0d6YXFrUDRhWG94UG81TEJ0OVAwSzJ3TzRha3hESW5hSS1hXzA0cm9VV0ZVV1NoZFdSTGdDc3lTaG1wOEV2YkdUYjFkclpkbk1sQmkzYXBHNHBIUkdXb2NEMkkwcWNya2t5WkdXZWtFN2ZBWDFiZlkwd3VXd0ozcExtZ29kZGQzOWl3YWg1YmM0dkVZSTQ?oc=5>

## HEADWINDS

### Advanced Micro Devices Inc (AMD) Stock Down 17.3% but Still Over
- Summary: Advanced Micro Devices Inc (AMD) Stock Down 17.3% but Still Over
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxPTW5ETEI2UEhtLVdUOXhRcFZ3TWtyS21vMWVkY0NoWExTZTMwekxlNXA3WlFIWFk3UkppcU54NjZpYnlaWjJ3MUJjY21FUWNHX0hVSW5TOEU3cmJ0WjJPeVBGdGxUY2Q4UnR4R3pBb093MW9SenFxNk5pYjdWaGJrdjFKNnR5UnByd1RMcUV3Y0ZBTWVwMHN1U05VZEp2cTdqMFpkaVQzVDVMemJFSUpvN2tzdU5ZX3Nkam1IZg?oc=5>

### From Micron to AMD, AI Stocks Crater — And Citi Just Flagged an 'Exponential' New Threat to Data Centers
- Summary: AI stocks, including AMD, are falling amid new data center threat.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi5wFBVV95cUxQRkV2Q0JEVWZCanEzeGZEVUlScFB2eVl5Qjk3anBUSWRGZ0RCYjNfdC1iU0t3OVNsbk84WXByVWRPcmx0ZXFFdE1udGNEVGZXS1RfUlBZU0xDX2dOU2VDVUVsaHRsWTd2aHRXTWtHYzRTckVxSUFzM2V1b3VHUEItRld4aFpldUQ4ZDN0bnhjTjVzeHFIOXhQRTM0NUFpRmJiYmd2QVRsVFBKNVQ1c1Z5Q2tQcGxIQUkwU1M0SGlnV1ZYVXVRVWswb2ZLMktNa25BU0EtYnFGNk92TXRDRnhLQnhpeVFUeFU?oc=5>

### AMD Sinks 13%, Bloom Energy Down 18% as Midterm “Seismic Shift” Deepens Chip Sell-Off
- Summary: AMD shares fall 13% in a sharp sell‑off.
- Date: 2026-11-05 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxPRTZXR01GeWlxZ1I0cnJmWU1hczF5OHBwWVRMS012eVhVOFpkd1dYNkE1WWlERVVDbUhpMzgxT0MwMFc1S2xxN1VzbF9Ea1hseHZJNzRHcmdONXFxTk9HcERpclF1RzNxRlhYZmRaRVVZYlNzU01xNnc2LTN1WjJqUElyNmJUVzdid3lmVElhNklpTFVoTWRLcDllbVczRzlPb2trbFBxQ3A1dw?oc=5>

## CATALYSTS

### AMD's data center revenue nearly doubles in Q3 and CEO Su expects growth to accelerate
- Summary: AMD's data center revenue nearly doubles in Q3 and CEO Su expects growth to accelerate
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMieEFVX3lxTFBfVXVMaFFzOXpSSmhDS2xlZWZLZDk0V2w5MHpTSnZ3d2c5bkMzRDhwbzhURWpMMVcwX3ZiME8ybmU4UHR1ekdtVlUwRTYxcTI0T1dadVhheUQ0LVVpWnRqYjdmeDkxMGJKQXBkNUtpaEVKZVlXNEhYRdIBfkFVX3lxTFAwT0pLTUtFX3FhLU4tWFFuU3JjMXF4NWxpWFNVZEoxeTdqMVc2d201ZHRMdXV4cEg4VGNnd0RDRmhKbnNYZndMa1hhMzZ3Y0lUdk82SUprYVVibVZQT19vR05WaGZKZlBzcDFLZWNzczZkb0pDN180UTZ5MTRuUQ?oc=5>

### AMD: Great Q3 Earnings, But 70% Downside Is Not Unrealistic (NASDAQ:AMD)
- Summary: AMD posts solid Q3 earnings but warns of significant downside risk, tempering upside expectations.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxQNWl1ZUdmNk5CdDA0RWxldDBCbE1mTFY1NUQ0YklGWE1zY3h2SE4td2piY2lSTjJJZm4yMkxQMXVCX1BMRlFMdW9XdHRNSk43ZmtJdnFlX2hxVDhteXdoNVZNS0lkeEV0ZHo0cVlGMVRZejNXUkNtcHFla1RtaHNTbHNtX291eGJ0Q0EzaG1oZXJScWNsUnFUcTFGRXptbVpfd0pzLUVYVHY?oc=5>

### AMD Stock Recovers After CEO Lisa Su Calls the Market ‘Short-Sighted’
- Summary: CEO Lisa Su’s comment boosts confidence in AMD.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxPZG13NC1RU29GekRtM2U4TjNJMVVLSTBZREVvNDRDcy1vWDFLYmhRc2x3VUNpWFRQQ1NESV9EVWs0QWxybWc4aWFKNG9RSmVxWGpHczNQTWo3Ukp2NVVuVWtpcFZQS3BOMDdidmJWa0NjRFR1eDlpTGw5M3pBbUlEWVJzN1owc0VPTm9kSk9vSFkxODBkYTBQcDRTaFVEQQ?oc=5>

### AMD Stock Soars After Thursday's Rout. AI Fears Take a Back Seat
- Summary: AMD shares jumped sharply after a market rout, with AI concerns easing.
- Date: 2026-11-06 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxOUDJ0QVZaRGdFaUdBLXh0MURVcVhPX0ZfQjhWenFaYXJYeG9kcTNQanVOaUxSYU9jeHVxeGVyMmIzSjlUNnJnTWhVS3oteDdVb0ZQdTUyeDVGT2tUR2hxUWRDWUpVcExJVnd3WjU0bEpnbHIxSjRNcjh6cnRpZFZqc1hhZzVvc2hCbnFOci1raGpRalgxUDF1djNOOA?oc=5>

### AMD Tumbles 13%, NVIDIA Slides 7% as AI Regulation Fears Hit Chip Stocks; Intel Sinks 8%
- Summary: AMD shares fell 13% amid AI regulation fears affecting the chip sector.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxPdzNfN2w5ZVNDUjNHZUxyd0tWZG42ajdJbzg0NkU0NHN3UDN5NG5jWVZrUHhqd1JHMVhVMkpXQ2NDYjcxcDREQ0liOWJ4TEFySkpOV3lJSnJQZGtmeUJRX2dBMExXYU0zNFpnMGdhdllkVHlkcmgwTlFILXdfeTMtcjl4YThqSURBdExta09XQXhYb0x5Uldj?oc=5>

### Advanced Micro Devices, Inc. (AMD) Stock Forecasts
- Summary: Analysts provide future price projections for AMD shares.
- Date: 2026-11-04 | Impact: low | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiAFBVV95cUxQMm9ZXzA5b0RjSFRWTFV1b2E2NHNPUzJ0Z2NseFlrZzhjY1U2WEtOeXBaNUpBN0V1RG5HX3RZcXNMaC1yNHJUMEctcENMc2pmbnNndnN5VDUwNnFtU2NpUmxZUmpfMmtpcXd5YWRZeU9yeWdYMGxDYlpsR255OVZtdDYzMlFyYUZ5?oc=5>

### Is Advanced Micro Devices (AMD) Fully Priced After Record AI Growth?
- Summary: Questioning whether AMD’s valuation reflects its AI-driven growth.
- Date: 2026-11-05 | Impact: low | Horizon: medium | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxNN1ZjcDRNUjdDUkxUMDRadUlJckxJZ0RNVW9ZWnZRNHNhQm5qZU9qdEFJQ1dKZmJFMk1GMy14TGpmZWRHcEJETnFwZVJHcE1lWG5lV21Za2s4aVc2Nm9ZSjdiN1lLZFFaR2xHWGtBQUF4Vkt1X2Y2VV9qWXp5MWx3dm15MEJXazZPQXNHRm9DVXNlU3h6S0dxQlBER29qUQ?oc=5>

### What Just Happened To AMD Stock?
- Summary: Exploring recent price movements of AMD shares.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxPUTRETjN2U3Q4TzFMLVlDX0hNTlBTZDhQN3FnX0xYUnJCSmlkNW1BVmpjdGF6aEdHM191YVhMWm1SS3BlbWd0bVZwVmVBRU1JSjFaeWd4OFdkSDVNTjhwVmRuY3F6TTFaVnN6c1pZdm5fV2dTa0prQWVBbk5uVnN3RzRqeXdvVmU4a1ppQ09zcldMWllSOEE?oc=5>

### Stock Market Today, Nov. 6: AMD Surges 11% on Record Quarterly Revenue and Stronger Growth Outlook
- Summary: AMD's record quarterly revenue and optimistic growth outlook drove a 11% stock surge, signaling strong earnings performance.
- Date: 2026-11-06 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMi6wFBVV95cUxOSGNRQWt0a2psYzBKVk1LaGVQZXFTcHRXNWZKVWVacVB5eE1xcjFOeXZxSERaVWd6SmpkN0R4RmNJSmpjbk5Paml1WEJCbHFqRkVVc29HR1dYV0s1dENnQzdBYUJmU1dEYTZpZm11cC05Mi04Y05KdFlzdnZXLVd5YnJKUnRXaGJLNTJCcGJTbVhQZWhWM1JwUDg5amhGZ1JTY2tIYzU3OGhYRnF6eHExdEZXREJVSFZzRldZWG5SNXR4UkdJcEN5Y0F4UWEzSjM1MXFrN3NyZ0NMbW5nNzl0VTQ0WG9lQWRGQ0Z3?oc=5>

### Is AMD Stock a Buy After the Spectacular Investor Update?
- Summary: Investor update highlights positive outlook, suggesting AMD may be a buy, reflecting favorable guidance and market sentiment.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi1wFBVV95cUxQcllpZm9XWl9qOG5CdGRXaEZ1UHZyMGtiM2xHNDZJSXZUV0JpMDVUZWtCbXNxY2Y2RmN2WEZMTWVsdEx1SEdwbUhMQ3hyNkY3c3F2ZGtqR1lIUG12Rm9TbDF6X3VSQUlsSW8wdVRPUmEzMkpCaUVNOFNKQUJZNFJ3dVU3bUQzaTEtZFdCMVJ3WlFOcGJWcTd0NXliOXc0WVZZeHBndFQ0ZXpXVzA2SUFBOXRidHZmbGh5NzdRbUhtMzUwZ1Q5ZFBGQkthaG9zaXdVVE01elh4Yw?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AMD** | **95.95** | **10.77** | **65.50** | **44.70** | **736,464,797,696.00 USD** | **88.91** |
| NVDA | 23.60 | 19.68 | 22.23 | 105.90 | 4,506,795,900,928.00 USD | -0.53 |
| INTC | N/A | 2.60 | 16.30 | 20.90 | 299,128,193,024.00 USD | 51.13 |
| AVGO | 37.22 | 14.06 | 27.50 | 85.50 | 1,401,967,345,664.00 USD | -16.79 |

Peers fetched as_of: 2026-11-06; AMD reuses existing data (market data as_of: 2026-11-06); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-03
- Next expected earnings: 2027-02-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-06

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
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
- https://news.google.com/rss/articles/CBMiugFBVV95cUxNWDNFTnhjZXZBMG9SeVBNemhLMTNoRUZhcW5yZm9iRnhJdExncG5COXBCX2dQakpxQ1NudzNsX1RjazBWMzR2dEc5ejg2REV1dXBMSWR6emRYdWZwSl95Zm1BWFc1WDFCU3pPcGJMUG5MSlpnblhVQzlHTURPNDB4MXBIRHZmSkNvMzN3c1lOUzQyQWVwek50Wm84U3BuSGZmQVd2SUl3QnRKdXViRUpJaTBsTW9OUXVaNGc?oc=5
- https://news.google.com/rss/articles/CBMieEFVX3lxTE1XUlpyMXlqcVpLcWt5MHZGLWJZd1FXVDlUTDlMTUhrMjVuOGNtMmhDUmFsang0MVN4RmRTR0o3TFk2Zndka1ZkWWp1QzViaEhkbmcxdXpZejRKWEV2enFDb3NZNmNzb3R5STEtclNmZk1DOUxQemZWQQ?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxOS05rMlNIQXZwWGRFbUlERjJ6bXlobEFuV19nckJuSlpWZlpKYmJvd1c0Z0FiOGtqc0FaeTItWDBsUkZJY044ZnV0emk5dlBjcVFtNkxBM2xGbzhmRi1adk9XNXpIZVpYNXRubUcwOVNYcHZJVjFzMEducG1pMXFscE9rX0xJazdhaHh0UDZUN3gzZ19aRm4xOG1acE5ONXBVeUVKM1dBb0ZYRjdrUGZNTzBhaEs?oc=5
- https://news.google.com/rss/articles/CBMizwFBVV95cUxPa01iWmYtRkh1S3plOXhjRGlOVGg1RzZfUS1yRzA3REs1MTFmb0NYQWJRYmNWSlRVYjlnV1hnMm5IT0d6YXFrUDRhWG94UG81TEJ0OVAwSzJ3TzRha3hESW5hSS1hXzA0cm9VV0ZVV1NoZFdSTGdDc3lTaG1wOEV2YkdUYjFkclpkbk1sQmkzYXBHNHBIUkdXb2NEMkkwcWNya2t5WkdXZWtFN2ZBWDFiZlkwd3VXd0ozcExtZ29kZGQzOWl3YWg1YmM0dkVZSTQ?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxPTW5ETEI2UEhtLVdUOXhRcFZ3TWtyS21vMWVkY0NoWExTZTMwekxlNXA3WlFIWFk3UkppcU54NjZpYnlaWjJ3MUJjY21FUWNHX0hVSW5TOEU3cmJ0WjJPeVBGdGxUY2Q4UnR4R3pBb093MW9SenFxNk5pYjdWaGJrdjFKNnR5UnByd1RMcUV3Y0ZBTWVwMHN1U05VZEp2cTdqMFpkaVQzVDVMemJFSUpvN2tzdU5ZX3Nkam1IZg?oc=5
- https://news.google.com/rss/articles/CBMi5wFBVV95cUxQRkV2Q0JEVWZCanEzeGZEVUlScFB2eVl5Qjk3anBUSWRGZ0RCYjNfdC1iU0t3OVNsbk84WXByVWRPcmx0ZXFFdE1udGNEVGZXS1RfUlBZU0xDX2dOU2VDVUVsaHRsWTd2aHRXTWtHYzRTckVxSUFzM2V1b3VHUEItRld4aFpldUQ4ZDN0bnhjTjVzeHFIOXhQRTM0NUFpRmJiYmd2QVRsVFBKNVQ1c1Z5Q2tQcGxIQUkwU1M0SGlnV1ZYVXVRVWswb2ZLMktNa25BU0EtYnFGNk92TXRDRnhLQnhpeVFUeFU?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxPRTZXR01GeWlxZ1I0cnJmWU1hczF5OHBwWVRMS012eVhVOFpkd1dYNkE1WWlERVVDbUhpMzgxT0MwMFc1S2xxN1VzbF9Ea1hseHZJNzRHcmdONXFxTk9HcERpclF1RzNxRlhYZmRaRVVZYlNzU01xNnc2LTN1WjJqUElyNmJUVzdid3lmVElhNklpTFVoTWRLcDllbVczRzlPb2trbFBxQ3A1dw?oc=5
- https://news.google.com/rss/articles/CBMieEFVX3lxTFBfVXVMaFFzOXpSSmhDS2xlZWZLZDk0V2w5MHpTSnZ3d2c5bkMzRDhwbzhURWpMMVcwX3ZiME8ybmU4UHR1ekdtVlUwRTYxcTI0T1dadVhheUQ0LVVpWnRqYjdmeDkxMGJKQXBkNUtpaEVKZVlXNEhYRdIBfkFVX3lxTFAwT0pLTUtFX3FhLU4tWFFuU3JjMXF4NWxpWFNVZEoxeTdqMVc2d201ZHRMdXV4cEg4VGNnd0RDRmhKbnNYZndMa1hhMzZ3Y0lUdk82SUprYVVibVZQT19vR05WaGZKZlBzcDFLZWNzczZkb0pDN180UTZ5MTRuUQ?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxQNWl1ZUdmNk5CdDA0RWxldDBCbE1mTFY1NUQ0YklGWE1zY3h2SE4td2piY2lSTjJJZm4yMkxQMXVCX1BMRlFMdW9XdHRNSk43ZmtJdnFlX2hxVDhteXdoNVZNS0lkeEV0ZHo0cVlGMVRZejNXUkNtcHFla1RtaHNTbHNtX291eGJ0Q0EzaG1oZXJScWNsUnFUcTFGRXptbVpfd0pzLUVYVHY?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxPZG13NC1RU29GekRtM2U4TjNJMVVLSTBZREVvNDRDcy1vWDFLYmhRc2x3VUNpWFRQQ1NESV9EVWs0QWxybWc4aWFKNG9RSmVxWGpHczNQTWo3Ukp2NVVuVWtpcFZQS3BOMDdidmJWa0NjRFR1eDlpTGw5M3pBbUlEWVJzN1owc0VPTm9kSk9vSFkxODBkYTBQcDRTaFVEQQ?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxOUDJ0QVZaRGdFaUdBLXh0MURVcVhPX0ZfQjhWenFaYXJYeG9kcTNQanVOaUxSYU9jeHVxeGVyMmIzSjlUNnJnTWhVS3oteDdVb0ZQdTUyeDVGT2tUR2hxUWRDWUpVcExJVnd3WjU0bEpnbHIxSjRNcjh6cnRpZFZqc1hhZzVvc2hCbnFOci1raGpRalgxUDF1djNOOA?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxPdzNfN2w5ZVNDUjNHZUxyd0tWZG42ajdJbzg0NkU0NHN3UDN5NG5jWVZrUHhqd1JHMVhVMkpXQ2NDYjcxcDREQ0liOWJ4TEFySkpOV3lJSnJQZGtmeUJRX2dBMExXYU0zNFpnMGdhdllkVHlkcmgwTlFILXdfeTMtcjl4YThqSURBdExta09XQXhYb0x5Uldj?oc=5
- https://news.google.com/rss/articles/CBMiiAFBVV95cUxQMm9ZXzA5b0RjSFRWTFV1b2E2NHNPUzJ0Z2NseFlrZzhjY1U2WEtOeXBaNUpBN0V1RG5HX3RZcXNMaC1yNHJUMEctcENMc2pmbnNndnN5VDUwNnFtU2NpUmxZUmpfMmtpcXd5YWRZeU9yeWdYMGxDYlpsR255OVZtdDYzMlFyYUZ5?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxNN1ZjcDRNUjdDUkxUMDRadUlJckxJZ0RNVW9ZWnZRNHNhQm5qZU9qdEFJQ1dKZmJFMk1GMy14TGpmZWRHcEJETnFwZVJHcE1lWG5lV21Za2s4aVc2Nm9ZSjdiN1lLZFFaR2xHWGtBQUF4Vkt1X2Y2VV9qWXp5MWx3dm15MEJXazZPQXNHRm9DVXNlU3h6S0dxQlBER29qUQ?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxPUTRETjN2U3Q4TzFMLVlDX0hNTlBTZDhQN3FnX0xYUnJCSmlkNW1BVmpjdGF6aEdHM191YVhMWm1SS3BlbWd0bVZwVmVBRU1JSjFaeWd4OFdkSDVNTjhwVmRuY3F6TTFaVnN6c1pZdm5fV2dTa0prQWVBbk5uVnN3RzRqeXdvVmU4a1ppQ09zcldMWllSOEE?oc=5
- https://news.google.com/rss/articles/CBMi6wFBVV95cUxOSGNRQWt0a2psYzBKVk1LaGVQZXFTcHRXNWZKVWVacVB5eE1xcjFOeXZxSERaVWd6SmpkN0R4RmNJSmpjbk5Paml1WEJCbHFqRkVVc29HR1dYV0s1dENnQzdBYUJmU1dEYTZpZm11cC05Mi04Y05KdFlzdnZXLVd5YnJKUnRXaGJLNTJCcGJTbVhQZWhWM1JwUDg5amhGZ1JTY2tIYzU3OGhYRnF6eHExdEZXREJVSFZzRldZWG5SNXR4UkdJcEN5Y0F4UWEzSjM1MXFrN3NyZ0NMbW5nNzl0VTQ0WG9lQWRGQ0Z3?oc=5
- https://news.google.com/rss/articles/CBMi1wFBVV95cUxQcllpZm9XWl9qOG5CdGRXaEZ1UHZyMGtiM2xHNDZJSXZUV0JpMDVUZWtCbXNxY2Y2RmN2WEZMTWVsdEx1SEdwbUhMQ3hyNkY3c3F2ZGtqR1lIUG12Rm9TbDF6X3VSQUlsSW8wdVRPUmEzMkpCaUVNOFNKQUJZNFJ3dVU3bUQzaTEtZFdCMVJ3WlFOcGJWcTd0NXliOXc0WVZZeHBndFQ0ZXpXVzA2SUFBOXRidHZmbGh5NzdRbUhtMzUwZ1Q5ZFBGQkthaG9zaXdVVE01elh4Yw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
