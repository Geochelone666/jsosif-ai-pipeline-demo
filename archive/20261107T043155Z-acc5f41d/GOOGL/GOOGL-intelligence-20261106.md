# GOOGL Intelligence Report

- ticker: **GOOGL**
- Report as_of: **2026-11-06**
- Market data as_of: **2026-11-06**
- Quant sources: https://finance.yahoo.com/quote/GOOGL/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/GOOGL/key-statistics/
- AI analysis snapshot as_of: **2026-11-06**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-07T04:47:48.346519+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 2, 'ai': 18, 'unknown': 0, 'irrelevant': 4})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **7** exact headline/source/date matches; prior report **20261106T045829Z-1db1e5a7/GOOGL** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **5**; {'directional_claim_without_event_type': 2, 'low_uncalibrated_model_confidence': 3}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 9 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 41.67%; oldest publication 2026-10-30

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 284.7800 |
| Return 1D (%) | 0.7821 |
| Return 1W (%) | 1.7653 |
| Return 1M (%) | -18.0913 |
| Return YTD (%) | -8.8390 |
| Return 1Y (%) | 0.2706 |
| Annualized volatility (%) | 33.8210 |
| Beta vs SPY | 1.3244 |
| Max drawdown (%) | -30.6204 |
| Sharpe (rf=0) | 0.1775 |
| Downside deviation (rf=0, %) | 23.7787 |
| Sortino (rf=0) | 0.2524 |
| Historical VaR 95% (1D, %) | 2.9365 |
| Historical ES 95% (1D, %) | 4.7232 |
| Correlation vs SPY | 0.5306 |
| Tracking error vs SPY (%) | 29.0023 |
| P/E (trailing) | 14.87 |
| P/B | 5.31 |
| EV/EBITDA | 18.35 |
| Revenue growth (%) | 24.70 |
| Forward P/E (estimate) | 18.45 |
| Gross margin (%) | 60.86 |
| Operating margin (%) | 31.80 |
| Return on equity (%) | 44.29 |
| Free cash flow yield (%) | -0.03 |
| MA50 | 332.9062 |
| Close vs MA50 (%) | -14.4564 |
| MA200 | 339.2164 |
| Close vs MA200 (%) | -16.0477 |
| RSI (14, Wilder) | 29.9216 |
| MACD (12,26) | -16.5704 |
| MACD signal (9) | -12.7763 |
| MACD histogram | -3.7941 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'GOOGL': 277, 'SPY': 277}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 284.7800 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.7821 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 1.7653 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -18.0913 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -8.8390 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 0.2706 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 33.8210 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 23.7787 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.2524 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.9365 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.7232 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5306 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 29.0023 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.3244 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -30.6204 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.1775 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 18.4501 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 60.8570 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 31.8050 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 44.2860 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: -0.0332 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 14.8710 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 29.9216 -> Oversold momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -3.7941 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -14.4564 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -16.0477 -> Clearly below the moving-average trend level.

## TAILWINDS

### Marc Chaikin Sees Alphabet (GOOGL) as a Conglomerate Hiding Three World-Class Businesses
- Summary: Analyst views Alphabet as a conglomerate with hidden top-tier businesses.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxOZGUwTUFsMVZQeEZPSnFCZ3dnMDZNTVNFeGVXelVQN1ZtcFo3SnY2dzdmSHhIM2J2OGgwRXZScGYxajZuSDNQd3ZvTGdrMDU5QWNEdWhXM0hnb1lPMmNoQ3ZST0lTcnVDRllVRnpwWG9VdWxxQ1I5R0w5Q3BsZ0NaMkJ1b0FRc05nZnRWdFRhdFBBYVg3aEkwSWd4NlktZw?oc=5>

### Why Alphabet Stock Popped on Wednesday
- Summary: Analyzes factors contributing to Alphabet's price jump on Wednesday, including earnings expectations and market dynamics.
- Date: 2026-11-04 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiAFBVV95cUxOYlJpNTBiZjlSRFh0LTc3cThFWW5GWXlQUFdTVDJQQkZWYWRwVnYxQXh4T1ZnY1FnM0JxY2Joc2ltWGJlVDJWVmRpWEVySHU5WFpLeFhiRENVVHhOUUI4SjA1SXl2dTBZRGFKVENzZldSLXc3WUR3c05aRXFWeE9URnpsTkp5d1Yy?oc=5>

### Why Is Everyone Talking About Alphabet Stock?
- Summary: General discussion about Alphabet stock popularity.
- Date: 2026-11-06 | Impact: low | Horizon: short | Confidence: 0.5
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxNc2NmMm1pRExrWjZCdzNKc3d5UGgyRGxzaDlueFdIQVdIaWxHWUEzNnFiaVVhcWJjemEzcWR4bktUZldUY1owanRObEt1NG0ydmlabzhMd0pJR0xYTnRDZlVOdG5TaENQWHVwdG9SWk1fTldQRkVxWkhMUUZTWjd2MXVoN3lsTW85TW85aUJvWTQ?oc=5>

### Alphabet: TPU Sales And Gemini Enterprise Are Reshaping The Bull Case (NASDAQ:GOOG)
- Summary: Alphabet’s TPU sales and Gemini Enterprise boost its bullish outlook.
- Date: 2026-11-06 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxPZzRiUEYxbWdqNkNNWWE5VHdpTWQ0S3N4SzdRRlRIZ3Z4eG9FemhrU2dkaWZ1NWg3am5KUkJucGZRbDU4YzRGRDIzb3NnV2daRm9UMXhQblJSa292R2l2dzE5bE5XU09ncHpPanNpTzhHYlVuazBrYk1IcXA4elpsWGdwaUVoUHo1d3FxV2JmVHJPUFlkZnJpMGxiOEZHWkFpbFM0?oc=5>

## HEADWINDS

### GOOGL Stock Is Down 10% YTD. Alphabet’s Historic Selloff Could Be a Buying Opportunity.
- Summary: GOOGL Stock Is Down 10% YTD. Alphabet’s Historic Selloff Could Be a Buying Opportunity.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxNbl9XRDh5Y0hMVXdFZUpUZ3ExTDRzV0Z6dHYtTWhRQVdrU3l1Z085NFRsYkVocDBWX0xfZzltd25VdW5idENwc1hFNXd0SjFiWTRmY3VEcHBzUjFqdmFzcjQ0RkR6WTRfUGJ3SzdvZUN0SGNwVnROdUtzSC1LeEpKeFJRNzJoMEp1cFZweS1SbWNCdw?oc=5>

### GOOGL Q3 deep dive: AI investment drives revenue growth but profit falls short of expectations
- Summary: GOOGL Q3 deep dive: AI investment drives revenue growth but profit falls short of expectations
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxPZURicFRzOTd2YnRheVByVFd3c3h5eDFlbHFPVmV3ZEZPbW1adG1NaElwdU1kcU5RM25tWjBZb1lqMktlTy1JalcxWXY4ek1QUGxrOVVES2RSN0JMcXVMRmxpOVpENlcyeTFHa3I0VUxEb2g2U2tCMjhjZV9McHRocVNDU2pEbTlkUFJfblF2WQ?oc=5>

### Alphabet: Search Disruption Vs. The Rise Of Carbon
- Summary: Search disruption threatens Alphabet amid growing carbon focus.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxPTWFweTVyMV9zZjhXMnVna0dsaWppNUVEMmpCNjlTVjJJcFljd3ExUjZwRlpTT3lrRmxmTGFFYWEyZE1NWUNFQVV1UjJfSTB1enlPUERnYnE5eXM2V2txMUhrdXFUelR6SGFUNndiWjM5WDlVMTFwMV92SW8xLUVRa3Y5cHpxSGpUVlRfYW55OVpBdGM?oc=5>

### Has Alphabet (GOOGL) Fallen Far Enough To Back Its Cash Flow Value?
- Summary: Questioning if Alphabet's valuation supports its cash flow value.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxQckEtTjZnazV2YS1qTjQxNkxzaXZOU2pjYmZ5S29qRzB5QlJ6Y04wcE9MYzE0c250WjQydHNkeUVDS1Q4RGRTaUFrUkphdFVGYWlqcHNibXNkVFo3QUpKVWZKX29LZTF4NE1INVU1ZkVONnQ3MzVzWXhrQzJ2VVBrZUVkTmVRT0VETVdhUnhWZW9uWFhVaThnbkRJeXEyZw?oc=5>

### Why Did Alphabet (GOOGL) Shares Fall After Its $500 Billion Value Wipeout?
- Summary: Shares dropped after a $500B market value wipeout, reflecting investor concerns.
- Date: 2026-11-01 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxQcWljZDdUS0l6cHpEVmtJYWlLNm5IdFN0RnV6ZmhuLThjODQ4aXhiQl95UE1Pa3ptY1pGRUVrQm5EWVh0SzN5aEVaUF9rUjVBU1YyZHhtMlBRem45b01lY3IwdFZkdmNxWU9LcWVEQTZTM2hjcWVrdmJaRDZDaFlzUWFHVlBNNjBSS0tJQ1MyMk8wazVMLVRCTFJB?oc=5>

### Alphabet loses $475 billion in market value, the biggest drop in its history
- Summary: Alphabet's market value fell $475B, the largest decline in its history, indicating significant investor sell‑off and market uncertainty.
- Date: 2026-10-30 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi0wFBVV95cUxOb0pfRGxYakdFTWU5eXlYYTd5cGVuVmpzMDFiMDBuX2ZOQVB5aFV1Qmk1dEhXQWwtSVNtU2ZOSTNfVDMxS2NoMUpTbmJ3a0hYOGtvOGJldXlkU3k2N3djaVhDMUNGN0g5Q1J2SzRXMkhXbzI3MUxqd2t5SEszX0JEZWZPUmRSd3VZQmYyZzZZeDNvY0hKaExMcnNTbHhzeTItckpZaEJmbWxodHVla2FKTTN4cmdFY2VjWk96cjdwLUtjX3FMRmZwLVp3SHJiX2xNajBR?oc=5>

### Good News Or Bad? Wall Street Lowers The Revenue Bar For Google Search
- Summary: Revenue expectations lowered, negative outlook.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxOWXFmV3NncXdwZnhIbTZmUGJOM2hWUkhHeVdySTRlY3hnRjVVMzk5bVYyN2R1Mk8xbm0xanV0TGVxMFN5UW9haTZhcFpaQXpIc2o1SDBqTThOOVlsMmJKMzVxMTBZRXFnVlZLbTREdW1PeTczbV9CQzExZDBSY2dwakh3d0gyQWRCQzVCY0VydFVkajRfbGliejB4aERfbHV3ckJTM3h5aUZlcmFFc3NMS05zdU1vaFlSdXZv?oc=5>

### ETFs Are Net Sellers of Alphabet (GOOGL) on Nov. 2
- Summary: ETF net selling may pressure Alphabet’s share price.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxOSDltbDVtR0dNR2o5Q3RwM18tellmR2N1R0pjeVFnQWtvV2ltSThRNUY2cE9OYng5SDBXWTRMeHpjcXRweHd0emhJZC0xVGJhREVDaE1yV0FoV1U2UFRnMmhkZXdYY0ZaV0lpY3IzeHUwT0ZiQXVEMUdSVHpKazhRaGxtVnI0SFltWmtLWGNVRnc2RG9hM1V1WlBxbkc?oc=5>

### Alphabet Inc Class A Stock (GOOGL) Opened Up by 3.50% on Nov 4: What Signal Does It Send?
- Summary: A 3.5% rise could signal short‑term volatility.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxQVHloOFA4QXZrajc0VXJrRnVCN2FWUlZweFRlendkN3JWN0ZNUkVzRlFOZjJGOUZTSDZNay1iOExXNWFqX1V1QXpCbjdoeHZFRGJUaVU4UzlWUzh0Q1ZYcGczeXFGODZ2S2wwcGpSd0IzNFlzQkVxanZST3lUbmFNNUdpLXhBVjVuaVdTRg?oc=5>

## CATALYSTS

### Alphabet’s drone unit to invest up to $125M in new manufacturing facility (GOOG:NASDAQ)
- Summary: Alphabet’s drone unit plans a $125M investment in a new manufacturing facility.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxPVzBOdjM3UF9HNko3dDdLNERnSW9ZSHl5OFA2NzZKWlRxUFpmZmYyQkhPcXJiUUJxZ2RFQlBJMlMxSTIwM0ZaY1N4N0RfOVYzWE11VUc0WkF5NkFMakQtTjlfeXRBYWpaZmFGdXV5Z3l1VkNyTFE5bXpkN1Y2SWdSV3BwUGFzNy1rNWpuWUFkRUVGU1NGaWhGQnZfaC12NVZ6ckRVMWdZemx0M0FlR0hld0RTRFFwSUhRR1E?oc=5>

### Google's $900 Million SpaceX Bet Is Now Worth $69 Billion. It Added Millions More Shares
- Summary: Alphabet’s $900M bet on SpaceX has grown to $69B, adding shares.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxNTTBzNHd1VVVraFFSd1paMThrLXdqaXlDZFgwVFBOMjhlbWsxUU1nYllKQXItSTl5VjRyYVlEbkVVYlF5czJXNTNSLUZaeXJtVUJrNUJNdV9pam9PWnk4VTA3UEFFQ3lVbTI3UmNFb1ZRYUlXSUZZYWtabnNVZ0NzX2JZNXQ1aE9pUmo5VDYxTQ?oc=5>

### Alphabet: Why The Company Remains A Strong Buy (NASDAQ:GOOG)
- Summary: Analyst view: Alphabet remains a strong buy.
- Date: 2026-11-06 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxQVUlZNTlUUWNRZG9iemNvWnZNLVdCRU9NaEtmeXZaY3NJNVNHbHBYeVRod3hEaFdkdklObXhFOGRoREd1NHVCQTY1TUY5Y1JJZTdtY3FjRWt6S1RyTVlVTlY4UEx1elZ3TFRuNl9FRHM1ZEtCT3lZN0lQdUYzbTJKaHRONjBMeHl5UlBsSXV2TQ?oc=5>

### Google parent reveals $548 million bet on beaten-down chip stock
- Summary: Alphabet’s $548M bet on a chip stock is disclosed.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxQNFdHMFhfc0p5eUg4UWVkYWEwZl96ZTFEeDI3VzJCSUd2ajV0QWhjRkVDVkU5RjJhYjF3cEM5VncwRnFPY0RQbVpsVFZfM2FjN3pCWnFFaE9QdlNUdWV2c0M3dkZRU2tqZFZqQmJaNWF3MmVvcldIbkU3bzVBbXlUQlJiVjF4RElzc2pqQlRtdld4ck9fdTBqYkNxdUZRejg?oc=5>

### Alphabet (GOOGL) Sees $35.0 Million in Net ETF Selling on Wednesday
- Summary: Alphabet’s shares saw $35M net ETF selling on Wednesday.
- Date: 2026-11-06 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMifkFVX3lxTFA3cGhXNVBvV2JpbHBkbXNDX251LU9CcEpSaUJ1cnFxUHlraHRFbDlwN1l5bS1FUHBpQ2dKbXhodEx4Ymo2Yy1vUFVGcTAxNTVFRkxkTml3dHhhM3RfUTJFeU43aW9wTjV0bU5JbF9EV0Q1WldkMEJKYWhZMVk3Zw?oc=5>

### Alphabet (GOOGL) Is Spending $15 Billion On Malaysia Data Centers
- Summary: Alphabet invests $15B in Malaysia data centers, expanding infrastructure.
- Date: 2026-11-04 | Impact: high | Horizon: long | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxOVmZLa0xpaWxxcnJtRTBhMGt4eWpzWEd3NDNvZlNJcWJPeGxmWnNnQ1pLQWNLSENyQ0Uzb3FKS2NyandnbERlQ1A3Y0lCdXpPdm1HeEhlZ2FXTGtiajRiMGlIVXNuVGZ1MUpLYUcxTlVsa2RKZFFYdThQLWxUU2V6T2dtZnpXdUVENGtQcHRJemtpTzZiNFp3NHd6cFJ5RVE?oc=5>

### Alphabet Inc. $GOOGL Stock: Lynx Investment Advisory Trims Stake
- Summary: Lynx Investment Advisory reduced its Alphabet stake, signaling a potential shift in investor confidence.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxNdFZLejBIakEtalo4aEZFTWozUlpwV19sMGNPQ3VoVWdfVW5UcGNKZWZxaHJDSmdfVHY5TVQxTElkdmo1Ml83UDBWZ1F3RWRVbDBKeEJpZHF0QU1GWkJvVERhRnpETTZJbE9YZVpTNWJ3YU9ZYUhjWW1CMkpycUFiLXJ1V3NtN3VrdmpMRUF2U3hFb285QUc4TzNnTFp3VGk1c0xTUkhaRk1md0wxcXlGZlo3SktCVzE4b3J2MnJGcw?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **GOOGL** | **14.87** | **5.31** | **18.35** | **24.70** | **3,501,085,163,520.00 USD** | **0.27** |
| META | 20.82 | 5.73 | 13.70 | 26.10 | 1,560,051,712,000.00 USD | -1.09 |
| MSFT | 27.97 | 8.38 | 19.49 | 18.80 | 3,940,412,817,408.00 USD | 7.62 |
| AMZN | 21.03 | 4.57 | 16.30 | 12.10 | 2,803,846,610,944.00 USD | 6.69 |

Peers fetched as_of: 2026-11-06; GOOGL reuses existing data (market data as_of: 2026-11-06); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-28
- Next expected earnings: 2027-02-03 (yfinance; expected dates may change)

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
- Filing date: 2026-10-29
- Revenue (latest available single quarter): 127,577,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 26,468,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1652044/000165204426000084/goog-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMingFBVV95cUxOZGUwTUFsMVZQeEZPSnFCZ3dnMDZNTVNFeGVXelVQN1ZtcFo3SnY2dzdmSHhIM2J2OGgwRXZScGYxajZuSDNQd3ZvTGdrMDU5QWNEdWhXM0hnb1lPMmNoQ3ZST0lTcnVDRllVRnpwWG9VdWxxQ1I5R0w5Q3BsZ0NaMkJ1b0FRc05nZnRWdFRhdFBBYVg3aEkwSWd4NlktZw?oc=5
- https://news.google.com/rss/articles/CBMiiAFBVV95cUxOYlJpNTBiZjlSRFh0LTc3cThFWW5GWXlQUFdTVDJQQkZWYWRwVnYxQXh4T1ZnY1FnM0JxY2Joc2ltWGJlVDJWVmRpWEVySHU5WFpLeFhiRENVVHhOUUI4SjA1SXl2dTBZRGFKVENzZldSLXc3WUR3c05aRXFWeE9URnpsTkp5d1Yy?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxNc2NmMm1pRExrWjZCdzNKc3d5UGgyRGxzaDlueFdIQVdIaWxHWUEzNnFiaVVhcWJjemEzcWR4bktUZldUY1owanRObEt1NG0ydmlabzhMd0pJR0xYTnRDZlVOdG5TaENQWHVwdG9SWk1fTldQRkVxWkhMUUZTWjd2MXVoN3lsTW85TW85aUJvWTQ?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxPZzRiUEYxbWdqNkNNWWE5VHdpTWQ0S3N4SzdRRlRIZ3Z4eG9FemhrU2dkaWZ1NWg3am5KUkJucGZRbDU4YzRGRDIzb3NnV2daRm9UMXhQblJSa292R2l2dzE5bE5XU09ncHpPanNpTzhHYlVuazBrYk1IcXA4elpsWGdwaUVoUHo1d3FxV2JmVHJPUFlkZnJpMGxiOEZHWkFpbFM0?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxNbl9XRDh5Y0hMVXdFZUpUZ3ExTDRzV0Z6dHYtTWhRQVdrU3l1Z085NFRsYkVocDBWX0xfZzltd25VdW5idENwc1hFNXd0SjFiWTRmY3VEcHBzUjFqdmFzcjQ0RkR6WTRfUGJ3SzdvZUN0SGNwVnROdUtzSC1LeEpKeFJRNzJoMEp1cFZweS1SbWNCdw?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxPZURicFRzOTd2YnRheVByVFd3c3h5eDFlbHFPVmV3ZEZPbW1adG1NaElwdU1kcU5RM25tWjBZb1lqMktlTy1JalcxWXY4ek1QUGxrOVVES2RSN0JMcXVMRmxpOVpENlcyeTFHa3I0VUxEb2g2U2tCMjhjZV9McHRocVNDU2pEbTlkUFJfblF2WQ?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxPTWFweTVyMV9zZjhXMnVna0dsaWppNUVEMmpCNjlTVjJJcFljd3ExUjZwRlpTT3lrRmxmTGFFYWEyZE1NWUNFQVV1UjJfSTB1enlPUERnYnE5eXM2V2txMUhrdXFUelR6SGFUNndiWjM5WDlVMTFwMV92SW8xLUVRa3Y5cHpxSGpUVlRfYW55OVpBdGM?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxQckEtTjZnazV2YS1qTjQxNkxzaXZOU2pjYmZ5S29qRzB5QlJ6Y04wcE9MYzE0c250WjQydHNkeUVDS1Q4RGRTaUFrUkphdFVGYWlqcHNibXNkVFo3QUpKVWZKX29LZTF4NE1INVU1ZkVONnQ3MzVzWXhrQzJ2VVBrZUVkTmVRT0VETVdhUnhWZW9uWFhVaThnbkRJeXEyZw?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxQcWljZDdUS0l6cHpEVmtJYWlLNm5IdFN0RnV6ZmhuLThjODQ4aXhiQl95UE1Pa3ptY1pGRUVrQm5EWVh0SzN5aEVaUF9rUjVBU1YyZHhtMlBRem45b01lY3IwdFZkdmNxWU9LcWVEQTZTM2hjcWVrdmJaRDZDaFlzUWFHVlBNNjBSS0tJQ1MyMk8wazVMLVRCTFJB?oc=5
- https://news.google.com/rss/articles/CBMi0wFBVV95cUxOb0pfRGxYakdFTWU5eXlYYTd5cGVuVmpzMDFiMDBuX2ZOQVB5aFV1Qmk1dEhXQWwtSVNtU2ZOSTNfVDMxS2NoMUpTbmJ3a0hYOGtvOGJldXlkU3k2N3djaVhDMUNGN0g5Q1J2SzRXMkhXbzI3MUxqd2t5SEszX0JEZWZPUmRSd3VZQmYyZzZZeDNvY0hKaExMcnNTbHhzeTItckpZaEJmbWxodHVla2FKTTN4cmdFY2VjWk96cjdwLUtjX3FMRmZwLVp3SHJiX2xNajBR?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxOWXFmV3NncXdwZnhIbTZmUGJOM2hWUkhHeVdySTRlY3hnRjVVMzk5bVYyN2R1Mk8xbm0xanV0TGVxMFN5UW9haTZhcFpaQXpIc2o1SDBqTThOOVlsMmJKMzVxMTBZRXFnVlZLbTREdW1PeTczbV9CQzExZDBSY2dwakh3d0gyQWRCQzVCY0VydFVkajRfbGliejB4aERfbHV3ckJTM3h5aUZlcmFFc3NMS05zdU1vaFlSdXZv?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxOSDltbDVtR0dNR2o5Q3RwM18tellmR2N1R0pjeVFnQWtvV2ltSThRNUY2cE9OYng5SDBXWTRMeHpjcXRweHd0emhJZC0xVGJhREVDaE1yV0FoV1U2UFRnMmhkZXdYY0ZaV0lpY3IzeHUwT0ZiQXVEMUdSVHpKazhRaGxtVnI0SFltWmtLWGNVRnc2RG9hM1V1WlBxbkc?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxQVHloOFA4QXZrajc0VXJrRnVCN2FWUlZweFRlendkN3JWN0ZNUkVzRlFOZjJGOUZTSDZNay1iOExXNWFqX1V1QXpCbjdoeHZFRGJUaVU4UzlWUzh0Q1ZYcGczeXFGODZ2S2wwcGpSd0IzNFlzQkVxanZST3lUbmFNNUdpLXhBVjVuaVdTRg?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxPVzBOdjM3UF9HNko3dDdLNERnSW9ZSHl5OFA2NzZKWlRxUFpmZmYyQkhPcXJiUUJxZ2RFQlBJMlMxSTIwM0ZaY1N4N0RfOVYzWE11VUc0WkF5NkFMakQtTjlfeXRBYWpaZmFGdXV5Z3l1VkNyTFE5bXpkN1Y2SWdSV3BwUGFzNy1rNWpuWUFkRUVGU1NGaWhGQnZfaC12NVZ6ckRVMWdZemx0M0FlR0hld0RTRFFwSUhRR1E?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxNTTBzNHd1VVVraFFSd1paMThrLXdqaXlDZFgwVFBOMjhlbWsxUU1nYllKQXItSTl5VjRyYVlEbkVVYlF5czJXNTNSLUZaeXJtVUJrNUJNdV9pam9PWnk4VTA3UEFFQ3lVbTI3UmNFb1ZRYUlXSUZZYWtabnNVZ0NzX2JZNXQ1aE9pUmo5VDYxTQ?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxQVUlZNTlUUWNRZG9iemNvWnZNLVdCRU9NaEtmeXZaY3NJNVNHbHBYeVRod3hEaFdkdklObXhFOGRoREd1NHVCQTY1TUY5Y1JJZTdtY3FjRWt6S1RyTVlVTlY4UEx1elZ3TFRuNl9FRHM1ZEtCT3lZN0lQdUYzbTJKaHRONjBMeHl5UlBsSXV2TQ?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxQNFdHMFhfc0p5eUg4UWVkYWEwZl96ZTFEeDI3VzJCSUd2ajV0QWhjRkVDVkU5RjJhYjF3cEM5VncwRnFPY0RQbVpsVFZfM2FjN3pCWnFFaE9QdlNUdWV2c0M3dkZRU2tqZFZqQmJaNWF3MmVvcldIbkU3bzVBbXlUQlJiVjF4RElzc2pqQlRtdld4ck9fdTBqYkNxdUZRejg?oc=5
- https://news.google.com/rss/articles/CBMifkFVX3lxTFA3cGhXNVBvV2JpbHBkbXNDX251LU9CcEpSaUJ1cnFxUHlraHRFbDlwN1l5bS1FUHBpQ2dKbXhodEx4Ymo2Yy1vUFVGcTAxNTVFRkxkTml3dHhhM3RfUTJFeU43aW9wTjV0bU5JbF9EV0Q1WldkMEJKYWhZMVk3Zw?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxOVmZLa0xpaWxxcnJtRTBhMGt4eWpzWEd3NDNvZlNJcWJPeGxmWnNnQ1pLQWNLSENyQ0Uzb3FKS2NyandnbERlQ1A3Y0lCdXpPdm1HeEhlZ2FXTGtiajRiMGlIVXNuVGZ1MUpLYUcxTlVsa2RKZFFYdThQLWxUU2V6T2dtZnpXdUVENGtQcHRJemtpTzZiNFp3NHd6cFJ5RVE?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxNdFZLejBIakEtalo4aEZFTWozUlpwV19sMGNPQ3VoVWdfVW5UcGNKZWZxaHJDSmdfVHY5TVQxTElkdmo1Ml83UDBWZ1F3RWRVbDBKeEJpZHF0QU1GWkJvVERhRnpETTZJbE9YZVpTNWJ3YU9ZYUhjWW1CMkpycUFiLXJ1V3NtN3VrdmpMRUF2U3hFb285QUc4TzNnTFp3VGk1c0xTUkhaRk1md0wxcXlGZlo3SktCVzE4b3J2MnJGcw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
