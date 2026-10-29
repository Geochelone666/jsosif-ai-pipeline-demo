# AMZN Intelligence Report

- ticker: **AMZN**
- Report as_of: **2026-10-28**
- Market data as_of: **2026-10-28**
- Quant sources: https://finance.yahoo.com/quote/AMZN/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AMZN/key-statistics/
- AI analysis snapshot as_of: **2026-10-28**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-29T02:11:22.215033+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 6, 'ai': 13, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **8** exact headline/source/date matches; prior report **20261028T015717Z-533e470c/AMZN** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 8 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 56.0%; oldest publication 2026-10-25

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 254.6000 |
| Return 1D (%) | 0.5927 |
| Return 1W (%) | -2.9615 |
| Return 1M (%) | 3.4329 |
| Return YTD (%) | 10.3024 |
| Return 1Y (%) | 11.0578 |
| Annualized volatility (%) | 34.7529 |
| Beta vs SPY | 1.4751 |
| Max drawdown (%) | -21.7362 |
| Sharpe (rf=0) | 0.4724 |
| Downside deviation (rf=0, %) | 20.9566 |
| Sortino (rf=0) | 0.7833 |
| Historical VaR 95% (1D, %) | 2.9597 |
| Historical ES 95% (1D, %) | 3.9961 |
| Correlation vs SPY | 0.5392 |
| Tracking error vs SPY (%) | 29.8846 |
| P/E (trailing) | 20.37 |
| P/B | 4.98 |
| EV/EBITDA | 17.02 |
| Revenue growth (%) | 19.60 |
| Forward P/E (estimate) | 24.36 |
| Gross margin (%) | 50.77 |
| Operating margin (%) | 13.69 |
| Return on equity (%) | 30.56 |
| Free cash flow yield (%) | 0.12 |
| MA50 | 255.1152 |
| Close vs MA50 (%) | -0.2019 |
| MA200 | 243.3761 |
| Close vs MA200 (%) | 4.6117 |
| RSI (14, Wilder) | 50.1039 |
| MACD (12,26) | -0.3159 |
| MACD signal (9) | 0.1505 |
| MACD histogram | -0.4664 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AMZN': 270, 'SPY': 270}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 254.6000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.5927 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -2.9615 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 3.4329 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 10.3024 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 11.0578 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 34.7529 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 20.9566 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.7833 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.9597 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.9961 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5392 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 29.8846 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.4751 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -21.7362 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.4724 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 24.3634 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 50.7700 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 13.6890 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 30.5580 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 0.1172 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 20.3680 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 50.1039 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.4664 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -0.2019 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 4.6117 -> Slightly above the moving-average trend level.

## TAILWINDS

### Amazon Earnings Preview: Why Wall Street Is Bullish On Cloud Growth
- Summary: Amazon Earnings Preview: Why Wall Street Is Bullish On Cloud Growth
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihwFBVV95cUxPMl9ieEFKdkpVZ3ZKQktnWjdqNG1NOHpaWXJqSnNOemNJRDFNNkN5VllMNmI1Rzc0bmpSV21WR2VCNDZnS1ZaUHl5ejVXVlB3c1RmRHVSSWFURmRVM2ZlX0txWDN0X29PYVM1MmFwRS03OFRBTmdvWlVqZGstbmtWYklvZWhPVlE?oc=5>

### Ahead of Earnings, Is Amazon Stock a Buy, a Sell, or Fairly Valued?
- Summary: Analyst debate suggests potential upside for Amazon stock ahead of earnings.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxOU3ZWanZTdVJOZjZiV21CWVQzeTZYSTZiQkVQS192N2xLNm0tUVFMWmJOeWxQVEctMUpPRmZZTm1NZ1JzUTlEMWNYT1V0S3dwNW9KWUlwQXVVM0VrZ3UyejlDSUgxeGxrcXdtakRWY3ZZZ2JwaUMtUlBoSEt4elV6ZEZWSFhJSEp5dm9yZ1NkWkxDQXNXTWFOQ0dXX3hwbndIY1Fvag?oc=5>

### Morgan Stanley Sees Amazon Stock Surging 100% with AWS Hitting $1 Trillion in Revenue Sooner Than People Think
- Summary: Morgan Stanley forecasts 100% stock surge driven by AWS revenue milestone.
- Date: 2026-10-25 | Impact: high | Horizon: short | Confidence: 0.88
- Sources: <https://news.google.com/rss/articles/CBMi5wFBVV95cUxNRTlMTHZLbXU2X3RFdmhmRlg0RFBMNXNodVhKODRZQ2stU1k4eEd2Q1lHV1Itdm8zajZOOGxpNEpTTnVqUGdQMHlqSzBreUk5M3Jpei1Ma0treWYzVnRPS0drUnk2cXJYa3dlNG9ROXVYbF8ybDJtMTNFMzZ0MC1HRVZCaTd3RDZxMUlfeGRvemJDSXotemd0VUp3QzR0cWV5VGcxcXRXeGdOSzYzVkNwTGk3WUFpbmNCclVYX2p2dDZ1RC10eVRMNUxqb1dGYjcyZ29UM2twOXdYSFQ3R1c3a0JiSG9GbWM?oc=5>

### UBS Sets Bold Amazon Stock Target Ahead of Earnings
- Summary: UBS projects a significant upside for Amazon stock before earnings release.
- Date: 2026-10-26 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxPTWN3cXhlTi1oTDJXY3BIbGZUYl9DV1YzNWZPVmYzZHhZczNlMm1YdnY2bElNNEEtQ2ZtTGFzYi0yOGZpbEVpaU93cEJoaFhrTzdOZ01TQWNVMm54QUM1T0VsZ2h4aXNGeVBWeWNsS1p1U2hRTktmVXdKVGJVWlFKc3pJTXV5dWxLb3FZN09xTE5KdEUtdnc?oc=5>

## HEADWINDS

### Amazon Faces A Big Test As Spending Weighs On Cash Flow (NASDAQ:AMZN)
- Summary: Amazon's increased spending threatens cash flow, posing a short‑term challenge.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQRXRxcWF4Zzk2YVFTZ2lBMmFfYzdZTG9TVnhNaEk3SlBvWlh1R1F4UThUZTFUNVJtcmxkazhGZDY1TWNKYUg3N19fQ3Y4RmJ3ajZ1X1hGdUFSVVB1X2VaaWplNElhMEt1U2Nia2YwclM1c3JKdXdzOGVOTkVEOVB6ajAwaWFTY1BaYmZwQm00YnlYZF96dHRXSS1sTGE?oc=5>

## CATALYSTS

### Amazon (AMZN) Q3 Earnings Preview: AWS Growth Takes Center Stage
- Summary: Amazon (AMZN) Q3 Earnings Preview: AWS Growth Takes Center Stage
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQWmh2NnNFTEwxNmRlRjZvVkJZUjlLRHJhMWprTFpXSXJ5aWZDUVVya1djLTRnNlgxVlZMbGVEZEZ0OEFSVXVUeEsxR1FOeVVzN1A1ZjUwejJfMVZtNC1RN214ZzJmWVdQR3hfY05nOGdycm5TZVpEa2h5ZlhDb2g2M0hhQVlCNktPcHdUNm1MaXV1MVd2cXpJVUZZRW8?oc=5>

### Amazon Stock (AMZN) Ticks Up After Launching $500 Echo Show 16, Alexa Photo Frame, and Speakers to Rival Apple
- Summary: Amazon Stock (AMZN) Ticks Up After Launching $500 Echo Show 16, Alexa Photo Frame, and Speakers to Rival Apple
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0AFBVV95cUxPQTcwa1Vwc01xbU16d0FhUHpzOU5GTDZBOTlhdUZiLXpvUTU0MkpybTlROGFoTk1McTlQMExKVTRnR1FIZUpFRG9yODJJUVdnbHJpcnRtVDVBODdwc2FWVDRvV1BqdDBsdi1CcE53bWNURktBcncwQVo1YWxYNkdkV1VVcGppbjJEd2lCWmszbmNPYlJ3TXRZcndwMGVUV25haEhRMlFGMEp1NVZNTWtrYTJYOVd2dFVHa1MzZ25kLTN1OFpCTEFHeHdOSlQtR1pf?oc=5>

### Amazon Q3 earnings on deck: All eyes on cloud growth, capex (AMZN:NASDAQ)
- Summary: Amazon Q3 earnings on deck: All eyes on cloud growth, capex (AMZN:NASDAQ)
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxPN2JmR0M3VE1qQ3RjcWxUdjVYZ1RyaHZjQVlaNmtyUzFOUTBLVi12bXpXZE1WaVc0MHZ6dWpySU9lUGp0YTcxTHBaejBtSFVMRDAzcUhLellVM28xdERPOFktUll6WHUzSXg5WGR5djlhY19MMmhZekpmV3czblNCMDhScHNFWGdWWlR1NXB6Nm1TcS1nYlV6cVd6UQ?oc=5>

### Amazon (AMZN) Set to Report Q3 Earnings Amid Focus on Cloud Grow
- Summary: Amazon (AMZN) Set to Report Q3 Earnings Amid Focus on Cloud Grow
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxPdzBmSGswYURKY01aMm5MYlROYi1neDNiUy1HcFU1b2JvQUtUQzZjSWtHUmVzSUxoM01DMFQyVUVsOW55TTFKaHFNWmh4cFRMNmhWaXhrdkFWUV81cUVCMFhjY0RrXzlYNEtHa2pVV3dEamFUUHVnY094b3NKMWw2Y0NVdjBsZHZ0WFI2ZDJQcTVhSW9jOGJxZFBuYnFXRmZ2QWthbmJEVHp3WHB1dHh0WElwY0h0SW10U3pz?oc=5>

### Amazon Stock: Wall Street Says AMZN Looks Increasingly Attractive Ahead of Q3 Earnings
- Summary: Amazon Stock: Wall Street Says AMZN Looks Increasingly Attractive Ahead of Q3 Earnings
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxPdXE4U096S21YUzhLNi1VeFEzamhtdWdCdmg0aWgtYnMxUlZBOG90TWZYeERWMVgzSnJCUlJ1allSMmplLTIwOTFxajVxYmpTd2NHdmVFTjd0d2t0cWlPdHE2bl9SMjR3WnlzaXBEMjJWaUV1UnptTWZrTWhxNjItVkhEcEpzV1VKYnNEN0syeFAweVc3VTdsd2dn?oc=5>

### AMZN Stock: 3 Reasons Why Amazon Could Deliver Solid Growth in Q3
- Summary: Three growth drivers cited for Amazon’s Q3 performance.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxOeGJ1SlJUbWhEZEVzQlcxTkl5cTA0WUxLaUhrRWl2X3VEdTdMcm10a29wSGR5bnE3SHM5bUFLeGQ1dDhidG8xbkJhQnJRVlE4b3VURlRHSjdUZHhvR2VDY2V1TURnNjEtTGdCN2M1QXZtd3hmdDFCLVYyUTN3T0YycDYwdmVUSkd1ajJvTjZJYi1fNk1tdElZNmhlMDZheHMya0s0Vi1uQnZkZWpM?oc=5>

### Is Amazon.com (AMZN) Undervalued As Investors Eye Q3 2026 Earnings?
- Summary: Investors question Amazon’s valuation ahead of Q3 2026 earnings.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxNNi1LSUJRazNtYzA3eDZYM3QwOFRlNmNqUHZOYmY4Q0UzYjlkMkFKcWFuMmRKYXhnN0xrdlpVU3VPclRfOGlvWEE4UWFYYUcxV1c2VWRMLXd3ZWxwUGVaNjBpRlRoSzRTU0NZRjcwTk9ScGxqLUlaRnlEd3NkQWd6c0tpdUE2Z2xkQUlrR0lqNW5kV2ZadWlsY1ptQXFmVl96Q09hbQ?oc=5>

### Gear Up for Amazon (AMZN) Q3 Earnings: Wall Street Estimates for Key Metrics
- Summary: Wall Street estimates key metrics for Amazon's Q3 earnings, setting expectations for the upcoming report.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQdGZpTVBwWkxLQzF0RUNxb2U0OHNURGlWSzZNMjVJb0hIeVBocTJZek9JUG5tRDRnVVc4TGRXaGE4bzByUFJoRVRRTWhVemVRbm5pRmVEZ3ltcDZqMVNpRmVHZG1Bck8zdUNHNE9ob1BWN0xwaUVNODJBWFdtU2R5YVlxVWRYT0QybDNkRHNzT1NEN3pCT3R3dg?oc=5>

### Amazon's Q3: What You Need To Know (NASDAQ:AMZN)
- Summary: Key points to consider for Amazon’s Q3 earnings.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMifEFVX3lxTE9tSFU2Z3YzVmJ6ZVRkc3Q2dXF3anpOTTQwRVJYQWJLT1FkcTZlNnFYY3VIOHAwQ3JxVVBsUVdtbXpCUmpGR29NOUwya1AtWkR3NE5uZGg2REc3c3Z5VDY1N2dWS2hLemZULU56aFpHMS0wdV9KUU5nbUpSeXg?oc=5>

### Here’s How Much Traders Expect Amazon Stock to Move After Earnings
- Summary: Analysts forecast post‑earnings price movement for Amazon shares.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivAFBVV95cUxPVlJURXJrUkpQWVZoZ0huRXhQWTFmQ2IySWdjcWVVN29GdkpRMXNYY1JHNEJpUEFJLVNmc3hMUVRCQnRPei00NTE0OUwzWFNqS3NmRW10RVlaSzA1dWJkeDFRUzFEQldXN0ZqdWx0OG82TXZ0b2hPR0RsZ0w2NlRmWVk2bkpZRy05OEhkUnFhM2hyZDVzQ0s4YTRvYXpqeFZONlNaeDVpcWItLUNUNEsyaEt0dVVlVlRqRjV2VA?oc=5>

### Ahead of Amazon Earnings, Here's What Barchart Data Says Comes Next for AMZN Stock
- Summary: Barchart predicts Amazon stock behavior ahead of earnings release.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxNd2xRQ0QxQjVfRFR6MGNuX0JTRll6N0lmb1N6YnJIM1ctcHM1WE0xWFc5QWgwSl9LcXRUMW5VbUNwR3Rael9QdUZyLVgwaEwwSXlXSUYwdmVxSkUxbUhzZno5QTluUjlja0RHVGtvYXNUNENKTldILWRFMXRzQlJZYllrV1FDaDFFSjlrRkc2MjFnejFlYkdoUFQydnNvMVBkc3NXSg?oc=5>

### ETFs Are Net Sellers of Amazon (AMZN) on Oct. 26
- Summary: ETFs sold Amazon shares on Oct. 26, indicating short-term selling pressure.
- Date: 2026-10-28 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxNY0k3YkkwbWVyaGlEWXpVQTh3bWtYNHNqZUg4NzZGWFpLMFVZaVBELVl1VGhud1JCdTROckkyX2ZjS0xEWDN1N0t1dnkwanBUQjVGLTNiNDJqcW9aU1VmdThpcmNTa0w1T096S3ZHRlJGQkF6YXlFXzI3YW9KWFBiZ2R0YUJBUW84T2Q2dkk5WWd1OTdjOGdhdQ?oc=5>

### Amazon tells software engineers to avoid ‘tokenmaxxing’ AI use (AMZN:NASDAQ)
- Summary: Amazon instructs engineers to steer clear of tokenmaxxing AI practices to maintain compliance and performance.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxNOEVHY1dEMFFnV1hYcllZUDliQTY2QkVtb0swTkhlSy0wSVRUVWx2a2NYdmwzSHJVbkJxR1VWbGNJaEZRaWFJWndqX0ViQjNZSEthYjNIUDVaNGs0Si1tdU5NYURJVDlUQTB3c3BVUF9za0ZtQkgyUTRXY1phM2dSUXU1U0VxaTh0Rk5jay13bU5kdWs3dTZCQVdVY2Rtc1E?oc=5>

### FCC Approves $11.5 Billion Amazon Leo Acquisition Of Globalstar
- Summary: FCC approves Amazon Leo’s $11.5B acquisition of Globalstar, expanding Amazon’s satellite services.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxQY2cwSkFkNnpGZURLb3FnYmZzbU5MOHhWN2JPWnlKWVFOdWZvT3FaVHFkNTRLa0FLMExza3hoY3RRM1ZKRXVoZkRQZzdyLXFTXzk2NXhmOXhuSnZSa1ItSHdXd1RnTm5Sc0hCaXgxZE55cmJ3eVdVVWxKMGxZSkI2eFV4WnJZMGRPQVFNVUVmUzZqdkFo?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AMZN** | **20.37** | **4.98** | **17.02** | **19.60** | **2,746,195,378,176.00 USD** | **11.06** |
| WMT | 43.03 | 9.60 | 22.97 | 5.90 | 945,181,032,448.00 USD | 16.09 |
| MSFT | 29.58 | 8.91 | 20.57 | 17.70 | 3,943,039,238,144.00 USD | -1.23 |
| GOOGL | 16.08 | 6.38 | 22.35 | 24.20 | 3,973,383,716,864.00 USD | 21.78 |

Peers fetched as_of: 2026-10-28; AMZN reuses existing data (market data as_of: 2026-10-28); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-07-30
- Next expected earnings: 2026-10-29 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-28

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-07-31
- Revenue (latest available single quarter): 200,606,000,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- Net income (latest available single quarter): 62,647,000,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000026/amzn-20260630.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMihwFBVV95cUxPMl9ieEFKdkpVZ3ZKQktnWjdqNG1NOHpaWXJqSnNOemNJRDFNNkN5VllMNmI1Rzc0bmpSV21WR2VCNDZnS1ZaUHl5ejVXVlB3c1RmRHVSSWFURmRVM2ZlX0txWDN0X29PYVM1MmFwRS03OFRBTmdvWlVqZGstbmtWYklvZWhPVlE?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxOU3ZWanZTdVJOZjZiV21CWVQzeTZYSTZiQkVQS192N2xLNm0tUVFMWmJOeWxQVEctMUpPRmZZTm1NZ1JzUTlEMWNYT1V0S3dwNW9KWUlwQXVVM0VrZ3UyejlDSUgxeGxrcXdtakRWY3ZZZ2JwaUMtUlBoSEt4elV6ZEZWSFhJSEp5dm9yZ1NkWkxDQXNXTWFOQ0dXX3hwbndIY1Fvag?oc=5
- https://news.google.com/rss/articles/CBMi5wFBVV95cUxNRTlMTHZLbXU2X3RFdmhmRlg0RFBMNXNodVhKODRZQ2stU1k4eEd2Q1lHV1Itdm8zajZOOGxpNEpTTnVqUGdQMHlqSzBreUk5M3Jpei1Ma0treWYzVnRPS0drUnk2cXJYa3dlNG9ROXVYbF8ybDJtMTNFMzZ0MC1HRVZCaTd3RDZxMUlfeGRvemJDSXotemd0VUp3QzR0cWV5VGcxcXRXeGdOSzYzVkNwTGk3WUFpbmNCclVYX2p2dDZ1RC10eVRMNUxqb1dGYjcyZ29UM2twOXdYSFQ3R1c3a0JiSG9GbWM?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxPTWN3cXhlTi1oTDJXY3BIbGZUYl9DV1YzNWZPVmYzZHhZczNlMm1YdnY2bElNNEEtQ2ZtTGFzYi0yOGZpbEVpaU93cEJoaFhrTzdOZ01TQWNVMm54QUM1T0VsZ2h4aXNGeVBWeWNsS1p1U2hRTktmVXdKVGJVWlFKc3pJTXV5dWxLb3FZN09xTE5KdEUtdnc?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQRXRxcWF4Zzk2YVFTZ2lBMmFfYzdZTG9TVnhNaEk3SlBvWlh1R1F4UThUZTFUNVJtcmxkazhGZDY1TWNKYUg3N19fQ3Y4RmJ3ajZ1X1hGdUFSVVB1X2VaaWplNElhMEt1U2Nia2YwclM1c3JKdXdzOGVOTkVEOVB6ajAwaWFTY1BaYmZwQm00YnlYZF96dHRXSS1sTGE?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQWmh2NnNFTEwxNmRlRjZvVkJZUjlLRHJhMWprTFpXSXJ5aWZDUVVya1djLTRnNlgxVlZMbGVEZEZ0OEFSVXVUeEsxR1FOeVVzN1A1ZjUwejJfMVZtNC1RN214ZzJmWVdQR3hfY05nOGdycm5TZVpEa2h5ZlhDb2g2M0hhQVlCNktPcHdUNm1MaXV1MVd2cXpJVUZZRW8?oc=5
- https://news.google.com/rss/articles/CBMi0AFBVV95cUxPQTcwa1Vwc01xbU16d0FhUHpzOU5GTDZBOTlhdUZiLXpvUTU0MkpybTlROGFoTk1McTlQMExKVTRnR1FIZUpFRG9yODJJUVdnbHJpcnRtVDVBODdwc2FWVDRvV1BqdDBsdi1CcE53bWNURktBcncwQVo1YWxYNkdkV1VVcGppbjJEd2lCWmszbmNPYlJ3TXRZcndwMGVUV25haEhRMlFGMEp1NVZNTWtrYTJYOVd2dFVHa1MzZ25kLTN1OFpCTEFHeHdOSlQtR1pf?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxPN2JmR0M3VE1qQ3RjcWxUdjVYZ1RyaHZjQVlaNmtyUzFOUTBLVi12bXpXZE1WaVc0MHZ6dWpySU9lUGp0YTcxTHBaejBtSFVMRDAzcUhLellVM28xdERPOFktUll6WHUzSXg5WGR5djlhY19MMmhZekpmV3czblNCMDhScHNFWGdWWlR1NXB6Nm1TcS1nYlV6cVd6UQ?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxPdzBmSGswYURKY01aMm5MYlROYi1neDNiUy1HcFU1b2JvQUtUQzZjSWtHUmVzSUxoM01DMFQyVUVsOW55TTFKaHFNWmh4cFRMNmhWaXhrdkFWUV81cUVCMFhjY0RrXzlYNEtHa2pVV3dEamFUUHVnY094b3NKMWw2Y0NVdjBsZHZ0WFI2ZDJQcTVhSW9jOGJxZFBuYnFXRmZ2QWthbmJEVHp3WHB1dHh0WElwY0h0SW10U3pz?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxPdXE4U096S21YUzhLNi1VeFEzamhtdWdCdmg0aWgtYnMxUlZBOG90TWZYeERWMVgzSnJCUlJ1allSMmplLTIwOTFxajVxYmpTd2NHdmVFTjd0d2t0cWlPdHE2bl9SMjR3WnlzaXBEMjJWaUV1UnptTWZrTWhxNjItVkhEcEpzV1VKYnNEN0syeFAweVc3VTdsd2dn?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxOeGJ1SlJUbWhEZEVzQlcxTkl5cTA0WUxLaUhrRWl2X3VEdTdMcm10a29wSGR5bnE3SHM5bUFLeGQ1dDhidG8xbkJhQnJRVlE4b3VURlRHSjdUZHhvR2VDY2V1TURnNjEtTGdCN2M1QXZtd3hmdDFCLVYyUTN3T0YycDYwdmVUSkd1ajJvTjZJYi1fNk1tdElZNmhlMDZheHMya0s0Vi1uQnZkZWpM?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxNNi1LSUJRazNtYzA3eDZYM3QwOFRlNmNqUHZOYmY4Q0UzYjlkMkFKcWFuMmRKYXhnN0xrdlpVU3VPclRfOGlvWEE4UWFYYUcxV1c2VWRMLXd3ZWxwUGVaNjBpRlRoSzRTU0NZRjcwTk9ScGxqLUlaRnlEd3NkQWd6c0tpdUE2Z2xkQUlrR0lqNW5kV2ZadWlsY1ptQXFmVl96Q09hbQ?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQdGZpTVBwWkxLQzF0RUNxb2U0OHNURGlWSzZNMjVJb0hIeVBocTJZek9JUG5tRDRnVVc4TGRXaGE4bzByUFJoRVRRTWhVemVRbm5pRmVEZ3ltcDZqMVNpRmVHZG1Bck8zdUNHNE9ob1BWN0xwaUVNODJBWFdtU2R5YVlxVWRYT0QybDNkRHNzT1NEN3pCT3R3dg?oc=5
- https://news.google.com/rss/articles/CBMifEFVX3lxTE9tSFU2Z3YzVmJ6ZVRkc3Q2dXF3anpOTTQwRVJYQWJLT1FkcTZlNnFYY3VIOHAwQ3JxVVBsUVdtbXpCUmpGR29NOUwya1AtWkR3NE5uZGg2REc3c3Z5VDY1N2dWS2hLemZULU56aFpHMS0wdV9KUU5nbUpSeXg?oc=5
- https://news.google.com/rss/articles/CBMivAFBVV95cUxPVlJURXJrUkpQWVZoZ0huRXhQWTFmQ2IySWdjcWVVN29GdkpRMXNYY1JHNEJpUEFJLVNmc3hMUVRCQnRPei00NTE0OUwzWFNqS3NmRW10RVlaSzA1dWJkeDFRUzFEQldXN0ZqdWx0OG82TXZ0b2hPR0RsZ0w2NlRmWVk2bkpZRy05OEhkUnFhM2hyZDVzQ0s4YTRvYXpqeFZONlNaeDVpcWItLUNUNEsyaEt0dVVlVlRqRjV2VA?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxNd2xRQ0QxQjVfRFR6MGNuX0JTRll6N0lmb1N6YnJIM1ctcHM1WE0xWFc5QWgwSl9LcXRUMW5VbUNwR3Rael9QdUZyLVgwaEwwSXlXSUYwdmVxSkUxbUhzZno5QTluUjlja0RHVGtvYXNUNENKTldILWRFMXRzQlJZYllrV1FDaDFFSjlrRkc2MjFnejFlYkdoUFQydnNvMVBkc3NXSg?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxNY0k3YkkwbWVyaGlEWXpVQTh3bWtYNHNqZUg4NzZGWFpLMFVZaVBELVl1VGhud1JCdTROckkyX2ZjS0xEWDN1N0t1dnkwanBUQjVGLTNiNDJqcW9aU1VmdThpcmNTa0w1T096S3ZHRlJGQkF6YXlFXzI3YW9KWFBiZ2R0YUJBUW84T2Q2dkk5WWd1OTdjOGdhdQ?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxNOEVHY1dEMFFnV1hYcllZUDliQTY2QkVtb0swTkhlSy0wSVRUVWx2a2NYdmwzSHJVbkJxR1VWbGNJaEZRaWFJWndqX0ViQjNZSEthYjNIUDVaNGs0Si1tdU5NYURJVDlUQTB3c3BVUF9za0ZtQkgyUTRXY1phM2dSUXU1U0VxaTh0Rk5jay13bU5kdWs3dTZCQVdVY2Rtc1E?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxQY2cwSkFkNnpGZURLb3FnYmZzbU5MOHhWN2JPWnlKWVFOdWZvT3FaVHFkNTRLa0FLMExza3hoY3RRM1ZKRXVoZkRQZzdyLXFTXzk2NXhmOXhuSnZSa1ItSHdXd1RnTm5Sc0hCaXgxZE55cmJ3eVdVVWxKMGxZSkI2eFV4WnJZMGRPQVFNVUVmUzZqdkFo?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
