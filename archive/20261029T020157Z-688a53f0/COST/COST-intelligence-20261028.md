# COST Intelligence Report

- ticker: **COST**
- Report as_of: **2026-10-28**
- Market data as_of: **2026-10-28**
- Quant sources: https://finance.yahoo.com/quote/COST/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/COST/key-statistics/
- AI analysis snapshot as_of: **2026-10-28**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-29T02:14:44.754207+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 23, 'rule': 5, 'ai': 12, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **8** exact headline/source/date matches; prior report **20261028T015717Z-533e470c/COST** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 23 unique headlines; 9 named publishers; 2 exact duplicates; 23 HTTPS source links; largest publisher share 26.09%; oldest publication 2026-10-22

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 982.7300 |
| Return 1D (%) | -0.9475 |
| Return 1W (%) | -1.5606 |
| Return 1M (%) | 6.4805 |
| Return YTD (%) | 14.4638 |
| Return 1Y (%) | 6.9581 |
| Annualized volatility (%) | 19.8272 |
| Beta vs SPY | -0.1827 |
| Max drawdown (%) | -18.1993 |
| Sharpe (rf=0) | 0.4395 |
| Downside deviation (rf=0, %) | 13.7630 |
| Sortino (rf=0) | 0.6331 |
| Historical VaR 95% (1D, %) | 2.0766 |
| Historical ES 95% (1D, %) | 2.7374 |
| Correlation vs SPY | -0.1171 |
| Tracking error vs SPY (%) | 24.7678 |
| P/E (trailing) | 47.80 |
| P/B | 12.17 |
| EV/EBITDA | 29.92 |
| Revenue growth (%) | 11.10 |
| Forward P/E (estimate) | 39.27 |
| Gross margin (%) | 12.77 |
| Operating margin (%) | 3.79 |
| Return on equity (%) | 28.40 |
| Free cash flow yield (%) | 1.55 |
| MA50 | 940.9462 |
| Close vs MA50 (%) | 4.4406 |
| MA200 | 968.6846 |
| Close vs MA200 (%) | 1.4499 |
| RSI (14, Wilder) | 57.3795 |
| MACD (12,26) | 19.2587 |
| MACD signal (9) | 18.3120 |
| MACD histogram | 0.9467 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'COST': 270, 'SPY': 270}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 982.7300 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.9475 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -1.5606 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 6.4805 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 14.4638 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 6.9581 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 19.8272 -> Low annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 13.7630 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.6331 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.0766 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.7374 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.1171 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 24.7678 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.1827 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -18.1993 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.4395 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 39.2679 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 12.7660 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 3.7890 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 28.4020 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.5507 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 47.7982 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 57.3795 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.9467 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 4.4406 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 1.4499 -> Slightly above the moving-average trend level.

## TAILWINDS

### Own Costco Stock by Oct. 30 to Qualify for Its Nov. 13 Dividend. Here's How Many Shares You'd Need for $1,000 in Yearly Dividends.
- Summary: Dividend qualification details for Costco shareholders.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxNeXBxZmdCWExtY2pyVTB0YU9PSGl0WXpWT0pkMl9Fb3QyVDZmMmdtWThGMVlQMUppamk5R0t2TUVuM2FJU00xVC1yUzN2QUx5RzhkWmF3a1lXdXpWVjl6UkNBLXFtYkVEc1BtMW9GajdFUkpyaGdZZ1FlSUQ4U1lBSl9xd3BGbnU2d3ZtbHU3bjFyM3Vtam1N?oc=5>

## HEADWINDS

### Costco Wholesale (NASDAQ:COST) Stock Price Down 1.3% - Here's What Happened
- Summary: Costco Wholesale (NASDAQ:COST) Stock Price Down 1.3% - Here's What Happened
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxPdWZyVXhSQTVhT2RKYjREUUliYTJzZFFuVTg2bnlMa091Y08xSW5Xdk5ITS1IWE42a0JIbmk2RkhPNjNoMWVyMXhBYjJZbmY5U0xSZXVzSmc5d2pkQ1B2dDZPMUFlRXVGMFp6RXBsUm1oaG10eEx6UmE3VWhIYnlfR1R1dDIwNmZHdk16X01wN2VtSlZQLVhyYW9ub1VGSHItTjBqYnZmMVRMazFVcUdvNTZyd0ptbDlhcWVqOVVpQ3E3SHVZRnFz?oc=5>

### Costco Stock's Valuation Remains A Head Scratcher (NASDAQ:COST)
- Summary: Valuation concerns for Costco stock.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxNVUx6T3FXRUEwZ09IbGJBMm54Qk5jcDJJS1J2d3ZyMjFEazhIUDNMLXBkQkozTzFieW1pXzUwZ2NwdEd5QmY2S1VQeVRwNHJJNWJDcnpLbV9SNWJSeWRaRVVfQ3B5TmI1SlJBSzJGNUZsV3dDM3JSczEwX3Foc1hweUZzTUduaXRsdTkwUlQ0ZnBtNmdxblc4WVlFZlFjb2s?oc=5>

### Costco (COST) Sees $96.9 Million in Net ETF Selling on Oct. 26
- Summary: Significant net ETF selling of Costco shares.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxNcWVKSE1FcGpZWWFEVWpBTUcwdzdUV2NSdXVtUjNQRU5KcjlGWFhrazUtYk9JZnhidGRCY3Vwc2gzWWpScWQyd1pGQVI3OURCREJySEZfQ3NlRUZXRHFzQUZac1NVTi1hRjB5VTNZVjNIRC1yNEsxVG9hLWxCOFZlaGZDOFpRaG9XNXcxZThnYw?oc=5>

## CATALYSTS

### Costco's Last Stock Split Was in 2000. Is Its Board Close to Another?
- Summary: Costco's Last Stock Split Was in 2000. Is Its Board Close to Another?
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxOS0hEMnF3U29oM05mVE9xLXJsUVBLVHNjcVZFc0ZJWHdSWXlZdTJVSVlVb3Q0enZsazZTeGxSUFNMaTdfSHJjOGxEWDA3Sll0QUp5ZWd4OVdlcnltM1VHQmFUUURaRVpmMktsU1JfLTd5ckN5R3RNNW0xUGFhZm1tUmliYkZIWG14S2xTVlFmaWZzVkRsLU16M1ln?oc=5>

### Costco Wholesale Corporation $COST Stock Sold by Fishman Jay A Ltd. MI
- Summary: Costco Wholesale Corporation $COST Stock Sold by Fishman Jay A Ltd. MI
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiyAFBVV95cUxNRVE1cGxvQVlBNFJxbzZEVjg2RkYzXzQ4Wmd0UW0tR0lmMVcyMlpjYlpTVFBmMGVodzNQWHdhN3c1VE91Ym9udTJzSVR1dnU2dUlUaVM0MlFIVHJRMG52cGFZaFVCMURQcUcwbWNUQk02d1NHYXQ0am1RdHNlQXhzYWhwMjJUa01YRTRNdTBtbUN4OEJwRTlhXy1GSXFjMjhJZUJ4WGpOc0NtNFJJb2o0WFoybFFYVDVIazVLTHlTZ01peUJmLU53Uw?oc=5>

### Costco Wholesale Corporation $COST Shares Sold by Penobscot Investment Management Company Inc.
- Summary: Costco Wholesale Corporation $COST Shares Sold by Penobscot Investment Management Company Inc.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi6AFBVV95cUxPZXFyem1BOUpUUzI1SWxLU1JrREtJS2U4SU84MGpBZFRESWJSdnJQMHRsTlg0T01aR2s1ZkhQSTZFeVhfMTdoUlZOYUJjaVkwUEYtcWN2YktqLWw0ejROYU94aFExa3pfNVpvYU1NRWF3bE05b2pBaVlybG5LeWZIMXFMbTR3R3dUdThPbXk0MUR4ek9UZzh5WWl3S1hzTndLcHpGOTBFMzlYYlJ2WmNvUHluX0EtaXdSZXJIOWtoSXVDQ1h6aUZTei14MnBPdTlEb3B0M1U5RXR4MEczT3JEcWhoSUJvX0lI?oc=5>

### Costco Turned $1,000 Into $8,018 in Ten Years While the S&P 500 Delivered $3,564
- Summary: Costco Turned $1,000 Into $8,018 in Ten Years While the S&P 500 Delivered $3,564
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxPZjNwWWRaUlV3MXFMSWJUX0hhdEtFZDZ1VkJ5MjRYcmRjS0pWZl9ZVzBQTWxhRHZPX3NKQ3hKcmswbFBmODVxaDh3UDZrc3lPa2x6NlQza2Y2TDdBOFVNMWpmNUoyZ1NFOUpRUFVUd3RXV1BYVEtzT3RKazZfd1MzZzY0bmhoZkdpMEZ5RmpQbUgwMlktMDhSVC1lRjEtemRfc2JtbEVSSWtUSVpDdVNEbkhsQzZ1Qkd1?oc=5>

### What Could Surprise Costco Stock Investors On The Upside?
- Summary: Speculation on potential positive surprises for Costco investors.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxNdDRfZlZnQmF6elFJUWY0ZGY1UjlaNHcycFU2ZklDMC14cHRHeFlkMG1wVnVlRzB2aHFrUVlsRHBhNXoxYWNUcHlSNDdJTDM2RlZzMVZ4dk45NkNNbnJfRENRSG5ERDZWQlhtdXBiaXpSTVNaZ3Q0Q3E0b1pZY2xMaC1wQ2pUUHFRX2Foa0ZzUzAyS01HNVpvS0FEZEMtaldMUTVWV2hQNWU4dmFTcnZKS1g0OE5ZckFM?oc=5>

### ETFs Are Net Sellers of Costco (COST) on Oct. 23
- Summary: ETFs sold Costco shares, indicating a short-term negative market sentiment.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQbkMwdHNwLXFCLWJQOFFkeTZHZS1zZWgzX1NnN3IwN0d1dm9hckZwdFpDYXA1bjdiUWNudlo4N2VlQXFUNmVWb252NlJEeEtJd0swWV9ER3hmcmlaVEgyZzFiTVNwV05KTUltdkN2TXBia0NfX3pDQ0hHV0F5LWhoQ0xKb1dIZ0RtRFlBa19tTktKUDIyVVlIRw?oc=5>

### Costco: Special Dividend Prospects Meet Expensive Valuations And Mixed Macros
- Summary: Costco may issue a special dividend amid high valuations and mixed macro conditions.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxNNGdpY0ZkVGVjN2FlRXZRZzFUOExtYWZCMnBIaFE2UEtPNFczZEJqaF96TWJNTEF0WWVwSGZoQ005NnAwTmNtbHhMSWFGb1F4YlR2UDBHZ0lBUzkwX0NDRTFacmVJT0hBdlppeWdzeEFtN2RoQjVTLXFxc3dXa1Q4LWZRRUFvdmFORkFERXdpS0V2eGJKdnVoaGFtdG40dUE1U0NKME9JelpsT1A3RHkwbHpfb04wbWlp?oc=5>

### Is Costco (COST) a Buy as Wall Street Analysts Look Optimistic?
- Summary: Analysts express optimism, recommending a buy for Costco shares.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxNckZTVVN0a3JPUC1mckI4OGNvc0hJblRHLWY5dV90N2FCSGdvS1FseUpFaFdQejBhRUkwX09KcGRwOEFEZVRyaVVub3pIYkh2T25LWVdPSVFCTXV2V1huLTNDVGl3SHF0Q2t3bldvcTluYW94YV9WVG5PRmRmRC1uV3lYdHBRRm9udkpwTHhCakQ3VmpnSjFN?oc=5>

### Costco (COST) Advances While Market Declines: Some Information for Investors
- Summary: Costco shares rise despite broader market downturn, indicating resilience.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxQdllxbjJ5MVp0RzlUZ2xwcEhHUURCbDNab3lqVHlpT0c1b0l5ODJDeHhkUUtHeGNTSGlnc1dBZHMxV0x3UEZBY0xONHBGTDJkVWRiSkNhSk15ZVgwaE9XczhEOVRFU0UybTdQSWtjUlJNcm1ablNab2tMS0k1ZzlTNElVTW5CeWhDeUtHVEN5cnpwTmdTUVhNOVNCZDk3Rnc?oc=5>

### 38 ETFs Add to Costco (COST) Holdings on Thursday
- Summary: ETFs increased holdings in Costco, indicating broader institutional interest.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMinAJBVV95cUxPV2tuT18wR2ROVV9aX0pjVmtrY1NjNE93d1FvZlZYTGVfTFRabUF2by1ZYUlJMTVxSFM0NVc1eVVGRmhmU1VyMk84UGh1WTlfRzZqUmtTZEVFTm93V1Jib2J0ZVlTdHhVelRSd19rekxxNkFGS2t4VHBQSV9DV2JGQ2p0WUlGY2RDMkdJTkI4ZGhVVUJLanZfbllOVEJQR1d1aEsyd2xaSW5MQkszNlp0S19STHJ3bEtwWjUtX3BiTE54eGl4M1ZTcy1OM1ZfQ282TEthNEJFM0VpaHVyeUFVN3ZvNVlPQzN1THhMR0xEbFlJNDJCWHl3SF9WdGw1amV5aktmTjdoSVlUWGZRNWxLc1daZlBZWElxc2xtMw?oc=5>

### Costco Wholesale Corporation $COST Stock: Generali Asset Management SPA SGR Grows Stake
- Summary: Generali Asset Management increases its stake in Costco, indicating confidence in the company’s prospects.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi3wFBVV95cUxQT1QwbEI4cFRpMDFWem9ZRXZQMG50S0hHTnowdnZ1VEw4OXpMd2c4dldlajdfMFBLalRHMTVBTDN0dXJPU1l3WVJHQVV6bmQ4QVR4dWlzdE5TOHQwOWtJNDloUkNITTJDZjdqMDlrZE5SRmp4aFlCT2ppQUJwOUo2WFVnMGZ6ckUzSUhTOUV3b1diRjZHNnRlTGpkYWpYakRRVjNoSWgyZ0M5bF9ERzFMeEh0eG1USWoxZ2tDNXhvalV5bDRSRTZlX1ZyOXd1SC04WGszMmFDU0pWSmt5clV3?oc=5>

### Costco Wholesale Corporation $COST Holdings Raised by Oppenheimer & Co. Inc.
- Summary: Oppenheimer & Co. raises its holdings in Costco, reflecting bullish sentiment.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMizAFBVV95cUxPc0MxdlJGcEpqclpBMjg2eTJMNGRZNDNuNWVSQlNzc2piYW1ESUtsUFcxNHpNeThKeHV6Ul9XOGMyLU8wdmZFbkd5UnhTRmhDRllQVktkSmVJRFhZYnNlZDh4WDBkQ3VuWHR0ZnM1UjFmaFU1VVBzcFRKcW0zcUlnNmRrRXlPRkdPM3ZwMjdxMzVGaHBSWW9iRzgteGd4eHRVbDJiRE5hdkp6ckZra3ZwOTNLS0RCTmFMY1lCZms2T3lHem9YVHBxcFhMQjM?oc=5>

### Verdence Capital Advisors LLC Purchases 3,206 Shares of Costco Wholesale Corporation $COST
- Summary: Verdence Capital acquires 3,206 Costco shares, signaling investment interest.
- Date: 2026-10-28 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi4wFBVV95cUxNQ0k5dHo5V0xPQXhodWFhR0VaWFZLY2JVZDF0NGtxR2h1MHdOZkRIQllkZ0xxWjdQaHpsY0RJeXJaTTN0LXhaT0VBenNBdkdjZV90UFl0akFnVjdHX2g0clByU2NidVpqMFpoUmFyTUphbFY2ak9CbXpBRGh6ZEVRNmZhS3d3Qmg2cXktNTdJRWZLeDlmUEdOSHkyeWxaSVlTNV9kaU5iaUFNOEhsMzgwZE1JMW56T3Z4SEZ6TG1rNk05WDhKRXljWFExcUl4eDNNUmNTbG9BYS0tMFZSclJJdWliVQ?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **COST** | **47.80** | **12.17** | **29.92** | **11.10** | **435,476,496,384.00 USD** | **6.96** |
| WMT | 43.03 | 9.60 | 22.97 | 5.90 | 945,181,032,448.00 USD | 16.09 |
| TGT | 15.37 | 3.79 | 9.48 | 5.30 | 67,672,043,520.00 USD | 59.60 |
| BJ | 22.63 | 5.95 | 13.62 | 15.70 | 13,065,991,168.00 USD | 11.92 |

Peers fetched as_of: 2026-10-28; COST reuses existing data (market data as_of: 2026-10-28); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-09-24
- Next expected earnings: 2026-12-10 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-28

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-K
- Filing date: 2026-10-07
- Revenue (latest available single quarter): 69,597,000,000.00 USD; period 2025-11-24/2026-02-15; fiscal year/reporting period 2026/Q2
- Net income (latest available single quarter): 2,192,000,000.00 USD; period 2026-02-16/2026-05-10; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/909832/000090983226000093/cost-20260830.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMilwFBVV95cUxNeXBxZmdCWExtY2pyVTB0YU9PSGl0WXpWT0pkMl9Fb3QyVDZmMmdtWThGMVlQMUppamk5R0t2TUVuM2FJU00xVC1yUzN2QUx5RzhkWmF3a1lXdXpWVjl6UkNBLXFtYkVEc1BtMW9GajdFUkpyaGdZZ1FlSUQ4U1lBSl9xd3BGbnU2d3ZtbHU3bjFyM3Vtam1N?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxQVk9ISkVyVk5VdFFMQ1VoVUN1Qm8xQmE5dHBsNlBqQmZLc0doUnNnWVUwa3I2QXoxSWVOejNIQmY2djVHa2JIVXlpNkVhRlZQV1Q3OXBWbFdldzg5ckJyNEVIZkdWTm5kc19wV2J0WGNnSVF0eGVUQThqZmpZa0ZOd2g2emk5REFjODRpQlRERXplZw?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxPdWZyVXhSQTVhT2RKYjREUUliYTJzZFFuVTg2bnlMa091Y08xSW5Xdk5ITS1IWE42a0JIbmk2RkhPNjNoMWVyMXhBYjJZbmY5U0xSZXVzSmc5d2pkQ1B2dDZPMUFlRXVGMFp6RXBsUm1oaG10eEx6UmE3VWhIYnlfR1R1dDIwNmZHdk16X01wN2VtSlZQLVhyYW9ub1VGSHItTjBqYnZmMVRMazFVcUdvNTZyd0ptbDlhcWVqOVVpQ3E3SHVZRnFz?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxNVUx6T3FXRUEwZ09IbGJBMm54Qk5jcDJJS1J2d3ZyMjFEazhIUDNMLXBkQkozTzFieW1pXzUwZ2NwdEd5QmY2S1VQeVRwNHJJNWJDcnpLbV9SNWJSeWRaRVVfQ3B5TmI1SlJBSzJGNUZsV3dDM3JSczEwX3Foc1hweUZzTUduaXRsdTkwUlQ0ZnBtNmdxblc4WVlFZlFjb2s?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxNcWVKSE1FcGpZWWFEVWpBTUcwdzdUV2NSdXVtUjNQRU5KcjlGWFhrazUtYk9JZnhidGRCY3Vwc2gzWWpScWQyd1pGQVI3OURCREJySEZfQ3NlRUZXRHFzQUZac1NVTi1hRjB5VTNZVjNIRC1yNEsxVG9hLWxCOFZlaGZDOFpRaG9XNXcxZThnYw?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxOS0hEMnF3U29oM05mVE9xLXJsUVBLVHNjcVZFc0ZJWHdSWXlZdTJVSVlVb3Q0enZsazZTeGxSUFNMaTdfSHJjOGxEWDA3Sll0QUp5ZWd4OVdlcnltM1VHQmFUUURaRVpmMktsU1JfLTd5ckN5R3RNNW0xUGFhZm1tUmliYkZIWG14S2xTVlFmaWZzVkRsLU16M1ln?oc=5
- https://news.google.com/rss/articles/CBMiyAFBVV95cUxNRVE1cGxvQVlBNFJxbzZEVjg2RkYzXzQ4Wmd0UW0tR0lmMVcyMlpjYlpTVFBmMGVodzNQWHdhN3c1VE91Ym9udTJzSVR1dnU2dUlUaVM0MlFIVHJRMG52cGFZaFVCMURQcUcwbWNUQk02d1NHYXQ0am1RdHNlQXhzYWhwMjJUa01YRTRNdTBtbUN4OEJwRTlhXy1GSXFjMjhJZUJ4WGpOc0NtNFJJb2o0WFoybFFYVDVIazVLTHlTZ01peUJmLU53Uw?oc=5
- https://news.google.com/rss/articles/CBMi6AFBVV95cUxPZXFyem1BOUpUUzI1SWxLU1JrREtJS2U4SU84MGpBZFRESWJSdnJQMHRsTlg0T01aR2s1ZkhQSTZFeVhfMTdoUlZOYUJjaVkwUEYtcWN2YktqLWw0ejROYU94aFExa3pfNVpvYU1NRWF3bE05b2pBaVlybG5LeWZIMXFMbTR3R3dUdThPbXk0MUR4ek9UZzh5WWl3S1hzTndLcHpGOTBFMzlYYlJ2WmNvUHluX0EtaXdSZXJIOWtoSXVDQ1h6aUZTei14MnBPdTlEb3B0M1U5RXR4MEczT3JEcWhoSUJvX0lI?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxPZjNwWWRaUlV3MXFMSWJUX0hhdEtFZDZ1VkJ5MjRYcmRjS0pWZl9ZVzBQTWxhRHZPX3NKQ3hKcmswbFBmODVxaDh3UDZrc3lPa2x6NlQza2Y2TDdBOFVNMWpmNUoyZ1NFOUpRUFVUd3RXV1BYVEtzT3RKazZfd1MzZzY0bmhoZkdpMEZ5RmpQbUgwMlktMDhSVC1lRjEtemRfc2JtbEVSSWtUSVpDdVNEbkhsQzZ1Qkd1?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxNdDRfZlZnQmF6elFJUWY0ZGY1UjlaNHcycFU2ZklDMC14cHRHeFlkMG1wVnVlRzB2aHFrUVlsRHBhNXoxYWNUcHlSNDdJTDM2RlZzMVZ4dk45NkNNbnJfRENRSG5ERDZWQlhtdXBiaXpSTVNaZ3Q0Q3E0b1pZY2xMaC1wQ2pUUHFRX2Foa0ZzUzAyS01HNVpvS0FEZEMtaldMUTVWV2hQNWU4dmFTcnZKS1g0OE5ZckFM?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQbkMwdHNwLXFCLWJQOFFkeTZHZS1zZWgzX1NnN3IwN0d1dm9hckZwdFpDYXA1bjdiUWNudlo4N2VlQXFUNmVWb252NlJEeEtJd0swWV9ER3hmcmlaVEgyZzFiTVNwV05KTUltdkN2TXBia0NfX3pDQ0hHV0F5LWhoQ0xKb1dIZ0RtRFlBa19tTktKUDIyVVlIRw?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxNNGdpY0ZkVGVjN2FlRXZRZzFUOExtYWZCMnBIaFE2UEtPNFczZEJqaF96TWJNTEF0WWVwSGZoQ005NnAwTmNtbHhMSWFGb1F4YlR2UDBHZ0lBUzkwX0NDRTFacmVJT0hBdlppeWdzeEFtN2RoQjVTLXFxc3dXa1Q4LWZRRUFvdmFORkFERXdpS0V2eGJKdnVoaGFtdG40dUE1U0NKME9JelpsT1A3RHkwbHpfb04wbWlp?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxNckZTVVN0a3JPUC1mckI4OGNvc0hJblRHLWY5dV90N2FCSGdvS1FseUpFaFdQejBhRUkwX09KcGRwOEFEZVRyaVVub3pIYkh2T25LWVdPSVFCTXV2V1huLTNDVGl3SHF0Q2t3bldvcTluYW94YV9WVG5PRmRmRC1uV3lYdHBRRm9udkpwTHhCakQ3VmpnSjFN?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxQdllxbjJ5MVp0RzlUZ2xwcEhHUURCbDNab3lqVHlpT0c1b0l5ODJDeHhkUUtHeGNTSGlnc1dBZHMxV0x3UEZBY0xONHBGTDJkVWRiSkNhSk15ZVgwaE9XczhEOVRFU0UybTdQSWtjUlJNcm1ablNab2tMS0k1ZzlTNElVTW5CeWhDeUtHVEN5cnpwTmdTUVhNOVNCZDk3Rnc?oc=5
- https://news.google.com/rss/articles/CBMinAJBVV95cUxPV2tuT18wR2ROVV9aX0pjVmtrY1NjNE93d1FvZlZYTGVfTFRabUF2by1ZYUlJMTVxSFM0NVc1eVVGRmhmU1VyMk84UGh1WTlfRzZqUmtTZEVFTm93V1Jib2J0ZVlTdHhVelRSd19rekxxNkFGS2t4VHBQSV9DV2JGQ2p0WUlGY2RDMkdJTkI4ZGhVVUJLanZfbllOVEJQR1d1aEsyd2xaSW5MQkszNlp0S19STHJ3bEtwWjUtX3BiTE54eGl4M1ZTcy1OM1ZfQ282TEthNEJFM0VpaHVyeUFVN3ZvNVlPQzN1THhMR0xEbFlJNDJCWHl3SF9WdGw1amV5aktmTjdoSVlUWGZRNWxLc1daZlBZWElxc2xtMw?oc=5
- https://news.google.com/rss/articles/CBMi3wFBVV95cUxQT1QwbEI4cFRpMDFWem9ZRXZQMG50S0hHTnowdnZ1VEw4OXpMd2c4dldlajdfMFBLalRHMTVBTDN0dXJPU1l3WVJHQVV6bmQ4QVR4dWlzdE5TOHQwOWtJNDloUkNITTJDZjdqMDlrZE5SRmp4aFlCT2ppQUJwOUo2WFVnMGZ6ckUzSUhTOUV3b1diRjZHNnRlTGpkYWpYakRRVjNoSWgyZ0M5bF9ERzFMeEh0eG1USWoxZ2tDNXhvalV5bDRSRTZlX1ZyOXd1SC04WGszMmFDU0pWSmt5clV3?oc=5
- https://news.google.com/rss/articles/CBMizAFBVV95cUxPc0MxdlJGcEpqclpBMjg2eTJMNGRZNDNuNWVSQlNzc2piYW1ESUtsUFcxNHpNeThKeHV6Ul9XOGMyLU8wdmZFbkd5UnhTRmhDRllQVktkSmVJRFhZYnNlZDh4WDBkQ3VuWHR0ZnM1UjFmaFU1VVBzcFRKcW0zcUlnNmRrRXlPRkdPM3ZwMjdxMzVGaHBSWW9iRzgteGd4eHRVbDJiRE5hdkp6ckZra3ZwOTNLS0RCTmFMY1lCZms2T3lHem9YVHBxcFhMQjM?oc=5
- https://news.google.com/rss/articles/CBMi4wFBVV95cUxNQ0k5dHo5V0xPQXhodWFhR0VaWFZLY2JVZDF0NGtxR2h1MHdOZkRIQllkZ0xxWjdQaHpsY0RJeXJaTTN0LXhaT0VBenNBdkdjZV90UFl0akFnVjdHX2g0clByU2NidVpqMFpoUmFyTUphbFY2ak9CbXpBRGh6ZEVRNmZhS3d3Qmg2cXktNTdJRWZLeDlmUEdOSHkyeWxaSVlTNV9kaU5iaUFNOEhsMzgwZE1JMW56T3Z4SEZ6TG1rNk05WDhKRXljWFExcUl4eDNNUmNTbG9BYS0tMFZSclJJdWliVQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
