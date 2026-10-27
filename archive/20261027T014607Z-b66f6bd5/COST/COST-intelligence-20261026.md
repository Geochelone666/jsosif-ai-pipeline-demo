# COST Intelligence Report

- ticker: **COST**
- Report as_of: **2026-10-26**
- Market data as_of: **2026-10-26**
- Quant sources: https://finance.yahoo.com/quote/COST/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/COST/key-statistics/
- AI analysis snapshot as_of: **2026-10-26**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-27T02:00:28.596026+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 23, 'rule': 4, 'ai': 12, 'unknown': 0, 'irrelevant': 7})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **6** exact headline/source/date matches; prior report **20261026T005504Z-6368ad31/COST** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 23 unique headlines; 9 named publishers; 2 exact duplicates; 23 HTTPS source links; largest publisher share 30.43%; oldest publication 2026-10-19

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 1005.1600 |
| Return 1D (%) | 0.1834 |
| Return 1W (%) | 0.9673 |
| Return 1M (%) | 8.9285 |
| Return YTD (%) | 17.0764 |
| Return 1Y (%) | 8.4627 |
| Annualized volatility (%) | 19.8076 |
| Beta vs SPY | -0.1779 |
| Max drawdown (%) | -18.1993 |
| Sharpe (rf=0) | 0.5247 |
| Downside deviation (rf=0, %) | 13.7097 |
| Sortino (rf=0) | 0.7581 |
| Historical VaR 95% (1D, %) | 2.0804 |
| Historical ES 95% (1D, %) | 2.7374 |
| Correlation vs SPY | -0.1142 |
| Tracking error vs SPY (%) | 24.7301 |
| P/E (trailing) | 48.42 |
| P/B | 12.44 |
| EV/EBITDA | 30.62 |
| Revenue growth (%) | 11.10 |
| Forward P/E (estimate) | 40.16 |
| Gross margin (%) | 12.77 |
| Operating margin (%) | 3.79 |
| Return on equity (%) | 28.40 |
| Free cash flow yield (%) | 1.52 |
| MA50 | 939.7460 |
| Close vs MA50 (%) | 6.9608 |
| MA200 | 968.1091 |
| Close vs MA200 (%) | 3.8271 |
| RSI (14, Wilder) | 69.6847 |
| MACD (12,26) | 22.3193 |
| MACD signal (9) | 17.3044 |
| MACD histogram | 5.0149 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'COST': 268, 'SPY': 268}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 1005.1600 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.1834 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 0.9673 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 8.9285 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 17.0764 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 8.4627 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 19.8076 -> Low annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 13.7097 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.7581 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.0804 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.7374 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.1142 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 24.7301 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.1779 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -18.1993 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.5247 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 40.1641 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 12.7660 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 3.7890 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 28.4020 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.5161 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 48.4181 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 69.6847 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 5.0149 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 6.9608 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 3.8271 -> Slightly above the moving-average trend level.

## TAILWINDS

### How AI Product Expansion At Costco (COST) Has Changed Its Investment Story
- Summary: AI product expansion enhances Costco’s value proposition, potentially boosting future earnings.
- Date: 2026-10-26 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi3gFBVV95cUxQeGlXaTBVdTZValYwcy02U0hKWldkVFlnaWo2Qm00TThTQ0puRE5KMktCWHlZVUs1Mk0zdlF6MmIwOC0ydFcwdGVSc1o2OG1OWWZ3Ni1mQUFXQlJFUEVVbGsyY2lNc0pzcUNHTU92WTUwYllMOXlSbXZ4WVJaUlVuVHJqV1dLeXNMMW9hcjVldzJKR0dJeUxRYVVHZXlfQldiUXhmaF8zLU52SVRscF9KczB6eWNvR0dyb3MxQ1dTYXBOcmpRYU9TRnhGYUptNDNjaGl4ZUFTakU3OFBGWlHSAeMBQVVfeXFMTml1ekFjbDg3ZlVUZHFIRWJWQ0tOYnBDVTFtc0Q3di1kRm93ZHhicjlwQmc0elBxZ1RKczBjZE96X1FPejhQZm4zaW4xVGxxU3J5UTVHcG1DSUFZT0VjVnpyRlJLR0ZpMzRhNkFfQWI0TFhwQ2ZvbkpObnpfaGpwWXRfd0JSUHh4MXQ1NnctRXpqRHdFd19KQlFTYTBHSTh1NnhMb3hNTHRaUWQ2ZDJZWUdhNnRUOXNpZTdTd21rQVo2TW1oaFNyaGd6NGhRMTBTQVZVeHdUS00zV2hMamhpdk1fdFE?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Costco's Last Stock Split Was in 2000. Is Its Board Close to Another?
- Summary: Costco's Last Stock Split Was in 2000. Is Its Board Close to Another?
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxOS0hEMnF3U29oM05mVE9xLXJsUVBLVHNjcVZFc0ZJWHdSWXlZdTJVSVlVb3Q0enZsazZTeGxSUFNMaTdfSHJjOGxEWDA3Sll0QUp5ZWd4OVdlcnltM1VHQmFUUURaRVpmMktsU1JfLTd5ckN5R3RNNW0xUGFhZm1tUmliYkZIWG14S2xTVlFmaWZzVkRsLU16M1ln?oc=5>

### Costco Wholesale Corporation $COST Shares Sold by Guardian Investment Management
- Summary: Costco Wholesale Corporation $COST Shares Sold by Guardian Investment Management
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1wFBVV95cUxOMVgtYl9GM1gzX1plUGxFNEZ0a1AtYXlwYjJ0eW5TRzFQX3VrRndaMG0yd0RlZnJfdTM4OTA4R25fTTdxMFN2OFNLdTJvR3JQdEpQd1BVYmVPTTRGM2J4b1djU182UTktRXN2bzlESlVVUDgwa1ZzNkhWUy00T1BHaWR4NGV5VVJMTHZvS1dIMFhyVWNjdnQ0Ul9Yc3dKX2R6ck12QUMtMEFCSWdmSDVsRV9aNXVzVThCVHlHa0poZVFkUVdIUEJtcTdTNGZWQmVhQ3BXd1F2OA?oc=5>

### Costco Wholesale Corporation $COST Shares Bought by Simplicity Wealth LLC
- Summary: Costco Wholesale Corporation $COST Shares Bought by Simplicity Wealth LLC
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizgFBVV95cUxPd0hWcENYbXNEcXZEUThJUnR6eG1jNmt0YWNZQWNtczFYa1pOTVVqbHVYaWtLWE5wdFhDcHpjTVU3VkJjX2ZiMUltTnBEUW9NWmVOQWo1WHMzX3BBbC1ka1pXU0RNd2NrZEdBN0MweU12YnZrdmZvajJqaGlCazJ6MGFDQkxYTGxnbGRQbmY4SS1jdHQ5cVZOSHotSGJSSzV0blVWcEwxT0pUS2g0X1EyNWJTN05uWF91Qkw4bmo2ZWdqclhjWmJZX1BKU1plZw?oc=5>

### Costco Wholesale Corporation $COST Stock: WASHINGTON TRUST Co Increases Position
- Summary: Costco Wholesale Corporation $COST Stock: WASHINGTON TRUST Co Increases Position
- Date: 2026-10-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxOOENZTDdqQ0RTYnltNUZ0SGZVVFVLUE9abFU4RWRIZkJSOW13cFhuSEc0NlllZnZsUFRQYmxzeVdfX1ltdi11X3lRUkRlSU41bm1xcDV5ZmJZZklUR2s3VHdrVkJWNk4wSnFCQXFvOFRFQktOMEdUVGpyeEZGbjJ6ZVFibkNLTjZVQkUtQndGcElrd1VqaWxBc05Sb1BjR3FrZjF5Nm1UbkR1SXhIS1dkazhXV0lDWC04UThpYmlzSDFfSHdiTnZ1aUo0cU93Z0dyUUEtTFd3?oc=5>

### What Could Surprise Costco Stock Investors On The Upside?
- Summary: Speculation on potential positive surprises for Costco investors.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxNdDRfZlZnQmF6elFJUWY0ZGY1UjlaNHcycFU2ZklDMC14cHRHeFlkMG1wVnVlRzB2aHFrUVlsRHBhNXoxYWNUcHlSNDdJTDM2RlZzMVZ4dk45NkNNbnJfRENRSG5ERDZWQlhtdXBiaXpSTVNaZ3Q0Q3E0b1pZY2xMaC1wQ2pUUHFRX2Foa0ZzUzAyS01HNVpvS0FEZEMtaldMUTVWV2hQNWU4dmFTcnZKS1g0OE5ZckFM?oc=5>

### Costco (COST) Stock Looks Expensive Despite Strong Sales Growth
- Summary: Analysts note high valuation amid sales growth, suggesting caution for investors.
- Date: 2026-10-19 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxNQ0JoWGpKMXA0cmxzbnU4MEN4LUJDNnhSRHpyWWdIdmtXeWlyaDVoaGFZQ2gyOVJkSFNGLUJUN1JCUTVzZlRjWWNOSGNtY1NWS1duaGRva1NvRmNuX2lINHdFRmwzWFJPOWNUcktlNkdkRklsamktbmpTN0JOeVpMSTBSNlJjM3d1Q01YZzJmSVFWUFc4cXVndEVVZHV1UDg?oc=5>

### Is Trending Stock Costco Wholesale Corporation (COST) a Buy Now?
- Summary: Opinion piece questioning if Costco is a good buy at current price.
- Date: 2026-10-20 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxQWmJjMXd1OUdua2hta1d5Y2NiSDFHNjNvNkNjZDBwZE5lSk9GLV93TnhQQW5qU1QydHl0SE1BbVVZRWNyVHN2QW04TS1YVnBfTjBwUEdPamtjUVE1MnpEeUhXU3ZieE5LV3kzSExCTUU5al8zbVVyb0JlU1BSUWtqbVBpdlVJTTNpcV95b2tuZGdES3hfMGVKQ2FLdnMyRk5sSEllYXkyYTFrZ0Vt?oc=5>

### Is Costco (COST) a Buy as Wall Street Analysts Look Optimistic?
- Summary: Analysts express optimism, recommending a buy for Costco shares.
- Date: 2026-10-23 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxNckZTVVN0a3JPUC1mckI4OGNvc0hJblRHLWY5dV90N2FCSGdvS1FseUpFaFdQejBhRUkwX09KcGRwOEFEZVRyaVVub3pIYkh2T25LWVdPSVFCTXV2V1huLTNDVGl3SHF0Q2t3bldvcTluYW94YV9WVG5PRmRmRC1uV3lYdHBRRm9udkpwTHhCakQ3VmpnSjFN?oc=5>

### Costco (COST) Advances While Market Declines: Some Information for Investors
- Summary: Costco shares rise despite broader market downturn, indicating resilience.
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxQdllxbjJ5MVp0RzlUZ2xwcEhHUURCbDNab3lqVHlpT0c1b0l5ODJDeHhkUUtHeGNTSGlnc1dBZHMxV0x3UEZBY0xONHBGTDJkVWRiSkNhSk15ZVgwaE9XczhEOVRFU0UybTdQSWtjUlJNcm1ablNab2tMS0k1ZzlTNElVTW5CeWhDeUtHVEN5cnpwTmdTUVhNOVNCZDk3Rnc?oc=5>

### Costco Wholesale Corporation $COST Stock: Sterling Capital Management LLC Decreases Stake
- Summary: Sterling Capital reduces its stake in Costco, potentially signaling a shift in investor confidence.
- Date: 2026-10-25 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi4gFBVV95cUxPRkpYZDdHNjdHVjRlUnNPZ1kxWlh0YXlVbFlXbk1OM3pHdWRqNFZkd01EUDhxTENyRnhNQmtyMzFvUWxzb0tXMU5wSWV3OTJIUWNBekVWR0FBU2VrcFNyLUxVREF5TG42am9OZnFBUVZYSTk4STFoVmM3QWZBTThqbWNMVWJRRW16SE5jQjlMUmZTZlI4R0RjQ2F6bzlPZ044QUJlR0NYTjdCd2YzQmRJaWZJNU0zbEdPUzVzUDBwM2Y2TmotWEtZLWFJZTZSUUdOcGExZkxZVEJPdmI4cFlHVEpn?oc=5>

### 38 ETFs Add to Costco (COST) Holdings on Thursday
- Summary: ETFs increased holdings in Costco, indicating broader institutional interest.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMinAJBVV95cUxPV2tuT18wR2ROVV9aX0pjVmtrY1NjNE93d1FvZlZYTGVfTFRabUF2by1ZYUlJMTVxSFM0NVc1eVVGRmhmU1VyMk84UGh1WTlfRzZqUmtTZEVFTm93V1Jib2J0ZVlTdHhVelRSd19rekxxNkFGS2t4VHBQSV9DV2JGQ2p0WUlGY2RDMkdJTkI4ZGhVVUJLanZfbllOVEJQR1d1aEsyd2xaSW5MQkszNlp0S19STHJ3bEtwWjUtX3BiTE54eGl4M1ZTcy1OM1ZfQ282TEthNEJFM0VpaHVyeUFVN3ZvNVlPQzN1THhMR0xEbFlJNDJCWHl3SF9WdGw1amV5aktmTjdoSVlUWGZRNWxLc1daZlBZWElxc2xtMw?oc=5>

### Costco Wholesale Corporation $COST Shares Newly Purchased by Norris Perne & French LLP MI
- Summary: Shares of Costco purchased by Norris Perne & French LLP MI.
- Date: 2026-10-26 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi4AFBVV95cUxOU2stZWx6VjAwX1JObWlyR1NYcThnWm9sRkRWY2YwZUFYbGJibHF3anM0Z3A4NFFYS2ZxaFNocWk2YjdydF81ZE12Sm1sUmZOa2lCT1FtX05haTFRZzNENjU0aGJSTVJvUFlVVFFNeVZ4RXpBNnd1VXZrYTNxSXoxMHlJcXd5dElzUlVEMkU4LTVZWkItYVNSbXNMNkNNbmtsaTlmeXhTWTFUcm1PSUZyU0xYQktlQmlEcDVxRWRMaXYtRVBQREotQ05XX3RVTDBiZ3F0dkx1S29CM210ekl3SQ?oc=5>

### Costco (COST) director Decker holds 8,798 shares directly after receiving a 266-unit stock grant.
- Summary: Director Decker now directly owns 8,798 shares following a 266-unit stock grant, indicating increased insider ownership.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxQY3pwRnNMY29jVXVlcW5mWFpJWE1oVXRTLXNIXzlTMVdrczZGWGdxUGR1cFUtYUpkY0ZEYnJ0ZHMydjhvNU1OLVdYaW1aTjhvd2M2b2dnVjQ2VncxWHlkcE5aZktHQ0oxVlIycEc5RXREYjlrMTJ0YkdsNFlpM09qdXhuQ1U5TkEyWlRCUmZXVzZTVjFLR2tERkFBNnhpSnBrcU1YS0dQeWZMeUprRUQxUlM0c0tPZ2ZSSTd3?oc=5>

### Costco (Nasdaq: COST) withholds 537 shares for taxes as its accounting chief receives a stock grant.
- Summary: Accounting chief receives a stock grant; 537 shares withheld for taxes, reflecting a new insider ownership stake.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxQNmRIMFZ3TDFkV2RybEZLVlQxVEVjM0NGWTZvOVBPWUJzdGNid2JqY3htR0RYV3pMcHlPZ3JFaEM1M0ktdW5kV013enB2aUhQNXJlZDdSZElZNDVfdHllYmJHVmE3VVdpRlB2OXRuRFl4U25Xb2loQzlPWjB6UlV0M3FhRkxmT0NOWndRZDR1Q1ZiVW1HRGswNGFqSC1icEtOeUplS19Zamg1QzY0eE90a2pjSTRhOUxKS3Fz?oc=5>

### Costco Wholesale Corporation $COST Holdings Increased by Orange Investment Advisors Inc.
- Summary: Orange Investment Advisors Inc. increased its holdings in Costco, signaling a larger institutional stake.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi4AFBVV95cUxOZzFVLWIyampHUS1KYm9URG93SFFmVEtXaE04Y2twemw5Ql9KR3NZNVVIM3ZRSFpDanZ0aTBpUE8ybklZeVlNM2hZSTJfU3I1RUdpVi1vZGJOWXhvRWFDTWlNdGdIY3BNblJHMVo1Z2tpM0xnSFM1MnE0Y3pnVHVHS0tUc2JkTFd1T0hWZEhyaHhjbUZLYmVvUlRBVS1vUFpEUVpKTWxMZVJlcnlQazVuUnNDVlc3WHROYUFsRkU5X19nX3hGTEdNU29hSWQxZHI3d2w0Sm1ySTNpODY3SjBCSg?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **COST** | **48.42** | **12.44** | **30.62** | **11.10** | **445,415,882,752.00 USD** | **8.46** |
| WMT | 43.58 | 9.73 | 23.25 | 5.90 | 957,277,339,648.00 USD | 14.25 |
| TGT | 15.42 | 3.78 | 9.46 | 5.30 | 67,476,692,992.00 USD | 63.96 |
| BJ | 23.27 | 6.12 | 13.94 | 15.70 | 13,434,829,824.00 USD | 15.90 |

Peers fetched as_of: 2026-10-26; COST reuses existing data (market data as_of: 2026-10-26); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-09-24
- Next expected earnings: 2026-12-10 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-26

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

- https://news.google.com/rss/articles/CBMi3gFBVV95cUxQeGlXaTBVdTZValYwcy02U0hKWldkVFlnaWo2Qm00TThTQ0puRE5KMktCWHlZVUs1Mk0zdlF6MmIwOC0ydFcwdGVSc1o2OG1OWWZ3Ni1mQUFXQlJFUEVVbGsyY2lNc0pzcUNHTU92WTUwYllMOXlSbXZ4WVJaUlVuVHJqV1dLeXNMMW9hcjVldzJKR0dJeUxRYVVHZXlfQldiUXhmaF8zLU52SVRscF9KczB6eWNvR0dyb3MxQ1dTYXBOcmpRYU9TRnhGYUptNDNjaGl4ZUFTakU3OFBGWlHSAeMBQVVfeXFMTml1ekFjbDg3ZlVUZHFIRWJWQ0tOYnBDVTFtc0Q3di1kRm93ZHhicjlwQmc0elBxZ1RKczBjZE96X1FPejhQZm4zaW4xVGxxU3J5UTVHcG1DSUFZT0VjVnpyRlJLR0ZpMzRhNkFfQWI0TFhwQ2ZvbkpObnpfaGpwWXRfd0JSUHh4MXQ1NnctRXpqRHdFd19KQlFTYTBHSTh1NnhMb3hNTHRaUWQ2ZDJZWUdhNnRUOXNpZTdTd21rQVo2TW1oaFNyaGd6NGhRMTBTQVZVeHdUS00zV2hMamhpdk1fdFE?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxOS0hEMnF3U29oM05mVE9xLXJsUVBLVHNjcVZFc0ZJWHdSWXlZdTJVSVlVb3Q0enZsazZTeGxSUFNMaTdfSHJjOGxEWDA3Sll0QUp5ZWd4OVdlcnltM1VHQmFUUURaRVpmMktsU1JfLTd5ckN5R3RNNW0xUGFhZm1tUmliYkZIWG14S2xTVlFmaWZzVkRsLU16M1ln?oc=5
- https://news.google.com/rss/articles/CBMi1wFBVV95cUxOMVgtYl9GM1gzX1plUGxFNEZ0a1AtYXlwYjJ0eW5TRzFQX3VrRndaMG0yd0RlZnJfdTM4OTA4R25fTTdxMFN2OFNLdTJvR3JQdEpQd1BVYmVPTTRGM2J4b1djU182UTktRXN2bzlESlVVUDgwa1ZzNkhWUy00T1BHaWR4NGV5VVJMTHZvS1dIMFhyVWNjdnQ0Ul9Yc3dKX2R6ck12QUMtMEFCSWdmSDVsRV9aNXVzVThCVHlHa0poZVFkUVdIUEJtcTdTNGZWQmVhQ3BXd1F2OA?oc=5
- https://news.google.com/rss/articles/CBMizgFBVV95cUxPd0hWcENYbXNEcXZEUThJUnR6eG1jNmt0YWNZQWNtczFYa1pOTVVqbHVYaWtLWE5wdFhDcHpjTVU3VkJjX2ZiMUltTnBEUW9NWmVOQWo1WHMzX3BBbC1ka1pXU0RNd2NrZEdBN0MweU12YnZrdmZvajJqaGlCazJ6MGFDQkxYTGxnbGRQbmY4SS1jdHQ5cVZOSHotSGJSSzV0blVWcEwxT0pUS2g0X1EyNWJTN05uWF91Qkw4bmo2ZWdqclhjWmJZX1BKU1plZw?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxOOENZTDdqQ0RTYnltNUZ0SGZVVFVLUE9abFU4RWRIZkJSOW13cFhuSEc0NlllZnZsUFRQYmxzeVdfX1ltdi11X3lRUkRlSU41bm1xcDV5ZmJZZklUR2s3VHdrVkJWNk4wSnFCQXFvOFRFQktOMEdUVGpyeEZGbjJ6ZVFibkNLTjZVQkUtQndGcElrd1VqaWxBc05Sb1BjR3FrZjF5Nm1UbkR1SXhIS1dkazhXV0lDWC04UThpYmlzSDFfSHdiTnZ1aUo0cU93Z0dyUUEtTFd3?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxNdDRfZlZnQmF6elFJUWY0ZGY1UjlaNHcycFU2ZklDMC14cHRHeFlkMG1wVnVlRzB2aHFrUVlsRHBhNXoxYWNUcHlSNDdJTDM2RlZzMVZ4dk45NkNNbnJfRENRSG5ERDZWQlhtdXBiaXpSTVNaZ3Q0Q3E0b1pZY2xMaC1wQ2pUUHFRX2Foa0ZzUzAyS01HNVpvS0FEZEMtaldMUTVWV2hQNWU4dmFTcnZKS1g0OE5ZckFM?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxNQ0JoWGpKMXA0cmxzbnU4MEN4LUJDNnhSRHpyWWdIdmtXeWlyaDVoaGFZQ2gyOVJkSFNGLUJUN1JCUTVzZlRjWWNOSGNtY1NWS1duaGRva1NvRmNuX2lINHdFRmwzWFJPOWNUcktlNkdkRklsamktbmpTN0JOeVpMSTBSNlJjM3d1Q01YZzJmSVFWUFc4cXVndEVVZHV1UDg?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxQWmJjMXd1OUdua2hta1d5Y2NiSDFHNjNvNkNjZDBwZE5lSk9GLV93TnhQQW5qU1QydHl0SE1BbVVZRWNyVHN2QW04TS1YVnBfTjBwUEdPamtjUVE1MnpEeUhXU3ZieE5LV3kzSExCTUU5al8zbVVyb0JlU1BSUWtqbVBpdlVJTTNpcV95b2tuZGdES3hfMGVKQ2FLdnMyRk5sSEllYXkyYTFrZ0Vt?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxNckZTVVN0a3JPUC1mckI4OGNvc0hJblRHLWY5dV90N2FCSGdvS1FseUpFaFdQejBhRUkwX09KcGRwOEFEZVRyaVVub3pIYkh2T25LWVdPSVFCTXV2V1huLTNDVGl3SHF0Q2t3bldvcTluYW94YV9WVG5PRmRmRC1uV3lYdHBRRm9udkpwTHhCakQ3VmpnSjFN?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxQdllxbjJ5MVp0RzlUZ2xwcEhHUURCbDNab3lqVHlpT0c1b0l5ODJDeHhkUUtHeGNTSGlnc1dBZHMxV0x3UEZBY0xONHBGTDJkVWRiSkNhSk15ZVgwaE9XczhEOVRFU0UybTdQSWtjUlJNcm1ablNab2tMS0k1ZzlTNElVTW5CeWhDeUtHVEN5cnpwTmdTUVhNOVNCZDk3Rnc?oc=5
- https://news.google.com/rss/articles/CBMi4gFBVV95cUxPRkpYZDdHNjdHVjRlUnNPZ1kxWlh0YXlVbFlXbk1OM3pHdWRqNFZkd01EUDhxTENyRnhNQmtyMzFvUWxzb0tXMU5wSWV3OTJIUWNBekVWR0FBU2VrcFNyLUxVREF5TG42am9OZnFBUVZYSTk4STFoVmM3QWZBTThqbWNMVWJRRW16SE5jQjlMUmZTZlI4R0RjQ2F6bzlPZ044QUJlR0NYTjdCd2YzQmRJaWZJNU0zbEdPUzVzUDBwM2Y2TmotWEtZLWFJZTZSUUdOcGExZkxZVEJPdmI4cFlHVEpn?oc=5
- https://news.google.com/rss/articles/CBMinAJBVV95cUxPV2tuT18wR2ROVV9aX0pjVmtrY1NjNE93d1FvZlZYTGVfTFRabUF2by1ZYUlJMTVxSFM0NVc1eVVGRmhmU1VyMk84UGh1WTlfRzZqUmtTZEVFTm93V1Jib2J0ZVlTdHhVelRSd19rekxxNkFGS2t4VHBQSV9DV2JGQ2p0WUlGY2RDMkdJTkI4ZGhVVUJLanZfbllOVEJQR1d1aEsyd2xaSW5MQkszNlp0S19STHJ3bEtwWjUtX3BiTE54eGl4M1ZTcy1OM1ZfQ282TEthNEJFM0VpaHVyeUFVN3ZvNVlPQzN1THhMR0xEbFlJNDJCWHl3SF9WdGw1amV5aktmTjdoSVlUWGZRNWxLc1daZlBZWElxc2xtMw?oc=5
- https://news.google.com/rss/articles/CBMi4AFBVV95cUxOU2stZWx6VjAwX1JObWlyR1NYcThnWm9sRkRWY2YwZUFYbGJibHF3anM0Z3A4NFFYS2ZxaFNocWk2YjdydF81ZE12Sm1sUmZOa2lCT1FtX05haTFRZzNENjU0aGJSTVJvUFlVVFFNeVZ4RXpBNnd1VXZrYTNxSXoxMHlJcXd5dElzUlVEMkU4LTVZWkItYVNSbXNMNkNNbmtsaTlmeXhTWTFUcm1PSUZyU0xYQktlQmlEcDVxRWRMaXYtRVBQREotQ05XX3RVTDBiZ3F0dkx1S29CM210ekl3SQ?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxQY3pwRnNMY29jVXVlcW5mWFpJWE1oVXRTLXNIXzlTMVdrczZGWGdxUGR1cFUtYUpkY0ZEYnJ0ZHMydjhvNU1OLVdYaW1aTjhvd2M2b2dnVjQ2VncxWHlkcE5aZktHQ0oxVlIycEc5RXREYjlrMTJ0YkdsNFlpM09qdXhuQ1U5TkEyWlRCUmZXVzZTVjFLR2tERkFBNnhpSnBrcU1YS0dQeWZMeUprRUQxUlM0c0tPZ2ZSSTd3?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxQNmRIMFZ3TDFkV2RybEZLVlQxVEVjM0NGWTZvOVBPWUJzdGNid2JqY3htR0RYV3pMcHlPZ3JFaEM1M0ktdW5kV013enB2aUhQNXJlZDdSZElZNDVfdHllYmJHVmE3VVdpRlB2OXRuRFl4U25Xb2loQzlPWjB6UlV0M3FhRkxmT0NOWndRZDR1Q1ZiVW1HRGswNGFqSC1icEtOeUplS19Zamg1QzY0eE90a2pjSTRhOUxKS3Fz?oc=5
- https://news.google.com/rss/articles/CBMi4AFBVV95cUxOZzFVLWIyampHUS1KYm9URG93SFFmVEtXaE04Y2twemw5Ql9KR3NZNVVIM3ZRSFpDanZ0aTBpUE8ybklZeVlNM2hZSTJfU3I1RUdpVi1vZGJOWXhvRWFDTWlNdGdIY3BNblJHMVo1Z2tpM0xnSFM1MnE0Y3pnVHVHS0tUc2JkTFd1T0hWZEhyaHhjbUZLYmVvUlRBVS1vUFpEUVpKTWxMZVJlcnlQazVuUnNDVlc3WHROYUFsRkU5X19nX3hGTEdNU29hSWQxZHI3d2w0Sm1ySTNpODY3SjBCSg?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
