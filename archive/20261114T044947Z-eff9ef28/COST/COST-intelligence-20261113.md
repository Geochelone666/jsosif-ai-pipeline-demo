# COST Intelligence Report

- ticker: **COST**
- Report as_of: **2026-11-13**
- Market data as_of: **2026-11-13**
- Quant sources: https://finance.yahoo.com/quote/COST/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/COST/key-statistics/
- AI analysis snapshot as_of: **2026-11-13**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-14T04:53:11.335521+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 10, 'ai': 9, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **6** exact headline/source/date matches; prior report **20261113T045636Z-34122c9a/COST** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 11 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 60.0%; oldest publication 2026-11-10

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 1106.2100 |
| Return 1D (%) | 1.2818 |
| Return 1W (%) | 4.9973 |
| Return 1M (%) | 16.0497 |
| Return YTD (%) | 29.0366 |
| Return 1Y (%) | 20.2852 |
| Annualized volatility (%) | 20.3911 |
| Beta vs SPY | -0.1622 |
| Max drawdown (%) | -18.1993 |
| Sharpe (rf=0) | 1.0113 |
| Downside deviation (rf=0, %) | 13.7877 |
| Sortino (rf=0) | 1.4956 |
| Historical VaR 95% (1D, %) | 2.0802 |
| Historical ES 95% (1D, %) | 2.7374 |
| Correlation vs SPY | -0.1085 |
| Tracking error vs SPY (%) | 25.7290 |
| P/E (trailing) | 52.60 |
| P/B | 13.70 |
| EV/EBITDA | 33.77 |
| Revenue growth (%) | 11.10 |
| Forward P/E (estimate) | 44.18 |
| Gross margin (%) | 12.77 |
| Operating margin (%) | 3.80 |
| Return on equity (%) | 28.40 |
| Free cash flow yield (%) | 1.38 |
| MA50 | 966.0330 |
| Close vs MA50 (%) | 14.5106 |
| MA200 | 972.9408 |
| Close vs MA200 (%) | 13.6976 |
| RSI (14, Wilder) | 76.1417 |
| MACD (12,26) | 35.3469 |
| MACD signal (9) | 29.4528 |
| MACD histogram | 5.8942 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'COST': 282, 'SPY': 282}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 1106.2100 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.2818 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 4.9973 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 16.0497 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 29.0366 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 20.2852 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 20.3911 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 13.7877 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.4956 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.0802 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.7374 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.1085 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 25.7290 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.1622 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -18.1993 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.0113 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 44.1777 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 12.7660 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 3.7970 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 28.4020 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.3776 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 52.6015 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 76.1417 -> Overbought momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 5.8942 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 14.5106 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 13.6976 -> Clearly above the moving-average trend level.

## TAILWINDS

### Costco’s $30-per-share special dividend means just 3 shares could cover your $65 membership. But there’s a catch
- Summary: Costco’s $30 special dividend could offset membership costs for a few shares, offering a financial benefit to shareholders.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxQNU1XWlFxZWMyYTg0NHd3by15cjhlX3FBQXhnaFpiT2JXRXR2VVRLQmZsbUJVN2Fmd3lJMTdpRUhQNUpNcC1uLUUtYUlnS00yQVZhSVFDWHgtbm9oajE4ZlktcHFvQWZJRVlZZ1hNYmxsQmZaMHFOdHVxZUhIVkN1RmhkY05KaVRsb0lNdFdCVUNkSWI4QmNn?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### COST Stock Rises Overnight: Costco’s $30 Special Dividend Has Retail Celebrating ‘Santa Coming Early’
- Summary: COST Stock Rises Overnight: Costco’s $30 Special Dividend Has Retail Celebrating ‘Santa Coming Early’
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxPYU03ekRHaEc0TWl0STFiVExmZnBzd0xRTXdpa2ctc05XeS1qRWlvb3J1NFdaMHVFc2lsLVNkeG1meGZSZTN6MUlLeTRNZFI3c19JeEhWbTlFdFV3MkxJWkt3a05iWVp3ZnZYanZXSTNWV21pLVZ6NTFrT3ZFYmZSOEVFN2pONzdlNHdSOHFYQTJJVzkxeWZQYmZjSlpJMmc?oc=5>

### Costco Stock (COST): Mizuho Raises Price Target on Special Dividend and $4B Buyback Plans
- Summary: Costco Stock (COST): Mizuho Raises Price Target on Special Dividend and $4B Buyback Plans
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxQa291TURNOHhHbFAyQXc4VlJYMW5pLWlYTjlVSHhIYnUxdU91bVBiTTZmMkNyYjBsbXBaY25QTFpUUE15X3MtcTFIUUFWd2lPU05EcXhicnZDeHdDaUVxaE90TWlGa0c3ZlU4LUk5THQ3dXdQYncxaXdOQlBETnE1NlpZQUdNdUUzV1JUelJYenRjcm9uVXI4eWRXcWdiajQ3YUptNVNPSGRPck8zWGFXdE1n?oc=5>

### Costco Just Declared a $30 Special Dividend. Is It Reason Enough to Buy the Stock Before Nov. 24?
- Summary: Costco Just Declared a $30 Special Dividend. Is It Reason Enough to Buy the Stock Before Nov. 24?
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxONmlOcVI4ZEp0c2tIcG1nTjBhLTRhNG5reW9UMTR3dkhaWFViS2FYUTgyZy05RDNNUElHQ0dsMjZuUVpXX3ZGZGhzSkF3MWlqaWpyWVJZM3BJSkVIcTVEY25ULTZUb0lVWmRSMC1SVmY0cnJmU0lCbkVONEk1ZXBSbXFsVVZuUi15allxR012c0x2MVlOT1k1a1JKNUNfSEgwYVlteHdYbnV0RExPVmJfTklkbmppRWthVHl2SjJOWWZuOFhWMTJfNkpIRWtCbEVEMV9OVzd3?oc=5>

### Costco Stock Nears All-Time Peak Amid Dividend, Buyback Buzz
- Summary: Costco Stock Nears All-Time Peak Amid Dividend, Buyback Buzz
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxQaDhILTlrOW5MYlAwM2NmT090b2FrVWRpQnhZQXFsMW9BOWVNLUdXbFowdEg1eFFETEZLTUVxQldTTWhGNTJiNUdKbzJ5OHNvVEFOanhIN2FLXzdKTFljb0NIY3g4ZGZGOV9fQ2xEa0Q3WXZPX0QydmdpV3NYQm1qakhtUXZhdXlEazBjMXVUWThxOEJDZXRkVW9CZC11SXN2anh0RXpwb0dhMUp5MkozNmJzNXFxampRVEE?oc=5>

### COST Stock Alert: What to Know as Costco Issues $30 Special Dividend
- Summary: COST Stock Alert: What to Know as Costco Issues $30 Special Dividend
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxPd040dEdhY1J1bGdUTE5jakswU0d5VTR3cTF6cmVKVGFiQ0o0OG0taVdmMm15ZGQ5dFEzTEJfS3BoWU1wVDZsVUROdUZhSDFzOENDUEhVRTBYQzc5RXdvVENKd3lrY21Rejg2NENfaFNpUDk3RmNSOGhsWE9mNG9GTDhMempQVklNcUxIaDl0UnRCdkhIaDQwYk1uazZ2dXVNblJ0X3FrTXBiYUczRGJr?oc=5>

### Costco gains after announcing its first special dividend in almost three years (COST:NASDAQ)
- Summary: Costco gains after announcing its first special dividend in almost three years (COST:NASDAQ)
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxNNzNkc1pDQ3duTWpMajdNcDBRV3NEdnhlb1FRY3lvWC02WGtWVWpCdXRxV0JDWnFleUxaUktzMHpmWkZIclRPNWE5Vl9ySDg5aFhlalp6R1gzc2RCaG5hc0tMQUl4MWl0aDN4a3hGS2xSblVyOHplMjExSlhDTWd0cWhEMm5yZmt3N2tJdjZWenhzNm5pd1F3ZEtkdkw3ZU1ndXNySFUxRmFwR2QwVDY0bklYdExpMzg?oc=5>

### Costco (COST) Declares $30 Special Dividend And Reauthorizes $4 Billion Buyback
- Summary: Costco (COST) Declares $30 Special Dividend And Reauthorizes $4 Billion Buyback
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNVk1SbzRkY0hkTVlRbk9LWHduY2lLZnJjeUIxU3NvbWVNLWhVZFFJMjNJYUNlSF92N2p5YTY5RFFocmVYSGdKakNybjRTeVZZd250OGg0aWNVVmR6UzFhVHpXRnhVREVmbHJ0RXBVZU5HUVRWelYyRUFxOVhHeHN1QXAxUGxYRVZJSW93OEhjSnJ0V3BGMm9OeURlbk8?oc=5>

### Costco Wholesale Corporation Declares $30 Special Cash Dividend and Reauthorizes Stock Repurchase Program
- Summary: Costco Wholesale Corporation Declares $30 Special Cash Dividend and Reauthorizes Stock Repurchase Program
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxNU2VSTlhQZTRsaGYwMGR4UFF3MTJGVUhHMG84dEdxUWVTM0dFeEJ1UDFsX25sbVJCUzZ2TTFhT2Jpck5uX29OekdvejhHREpJQk5uRnFmR2xOazV4SjJLdFlvc0JRWGQyQVJsZHkyOWRkem80TzZ1X3A2QUlBZldXQ2dYS0xXNERZOEJtSy16b1M5RDZucDNxOGJ2S2NYbl9zZ3VXdmRPYnE?oc=5>

### Costco Stocks Rise 1.62% After Record $30 Special Dividend Worth $13.3 Billion
- Summary: Costco Stocks Rise 1.62% After Record $30 Special Dividend Worth $13.3 Billion
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxNNDhKRGlWaVlleFYxdl9yZTJBTGc5Z0plWEp0Zy1sOTdiNGNneDd6bWkxOEtWRUtBN250aU1Ta2FZcEg3WFRNMXl5b1ZDN1NTLU03R3ZSckgxb1BFelRFUGtLMlFrVThxeFRFNUQxdDRNTkJGdFNuSi11WEdiNjh4QWxWbEwzOF9fZXliazd0RXh2Zw?oc=5>

### COST Stock Draws Street Attention After $30 Cash Dividend – Mizuho Highlights Significantly Higher Payout, Bernstein Eyes Q4 Trends
- Summary: COST Stock Draws Street Attention After $30 Cash Dividend – Mizuho Highlights Significantly Higher Payout, Bernstein Eyes Q4 Trends
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxQM1NLVHZLbFU0ZmtaeFVRcGpvMGtoVjFrWkczdXYxSDFmemkzTllHUzR5ek9ZSUNNdlFxdG0zQmZEdllkTlQ0TEpMUlVwcGY2UnB1eEliM2c1NThhSDl1aUhYV0xZU0tmTDFnYkJ4QzY3c05GMlF1clZPQk9mNndsd0NHM1BGMmhQdHl1aXZYREJqcExOS3NGSUtOMUEtUzA?oc=5>

### Costco Stock Rises Near 52-Week High: What's Going On?
- Summary: Costco shares climb near 52‑week high, indicating positive market sentiment.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxPb3I3SVB4UDlwc2lJVk1CSW9XUGJDQWZJSzQ0a3ZHMjBUdEVJMmJGRG5hZHNBM1piRGVIR29Vd3Fobjg1amJsMzZxaUF3Y2tuQmNzZ0dITHBxNmd5b2RFUzNzYV9Xc2ZXenJIbXFBWjdieEZfOW5UVzY3NE1DSUJ6OFVFTUZUeVJjOHluSURpclRtRGx3TTQxdWVLaF81cVJuUk1ac2R4QlZuS2ktRExva253?oc=5>

### ETFs Bought $69.5 Million of Costco (COST) on Friday
- Summary: ETFs purchased $69.5M of Costco shares, indicating institutional interest.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxPUE1WSmdhN1FQOHVaQ0hTbFN0NTZia3BpQTRPX3FrMEtYYkljb2g4QTdDRU5WM2tkdXp2a0oxME1yXzhZYkRIdmUtNnZQUU5weFZTR0ZQMTFRX2RmLWdFM3VRRjFoY0tkaXlMYVROWjBqZWQxMmw2emRvdk53a251dFNWWFRtR2lXck9kRTgwRy01UUk?oc=5>

### What Costco Wholesale Holders Bought Into
- Summary: Article details the holdings of Costco shareholders.
- Date: 2026-11-12 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNLUFoMFA3dXFHeTA3SjFMNmp6dE9tMkNtb3BWY1JxMkx0dFBxRU9rNVNKTEN1UV9JVjVJZGVleTQ3YzZ5MjVJUGVLNUg2ZUNENk1BOHpYUkhiWDhOYUNrNnpibnFwRlI4XzdTOVBVbmpKaHByRWlNVUhSSTFMR3J6NkVVVGlreWk3dTQweEM0WG5zSk50Z1R5bkg1QTM?oc=5>

### Costco (COST) Surpasses Market Returns: Some Facts Worth Knowing
- Summary: Costco outperformed market returns, indicating strong performance.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxPYVNac1hIUHdZQ1YtZ3JyVC1ONzNNanhheDg5dzNla3pjeUVGYnNvZXpUbHB1SGxhZG9mdTlQekFmN1NoMW1wR0hHUTd6ZHpYYmUtNHVaTUZmVlVSUmV0a1ZhUzNrVExiR0VaMk1rR2pYdDctQXRIUExuTXl0U3RuaHRTME03THRLN0FkUWVn?oc=5>

### Costco Just Sent Shareholders a $13 Billion Signal It Has More Cash Than It Can Use. Here’s What 200 Shares Collect
- Summary: Costco signals excess cash, hinting at future dividend or buyback.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxQSURnd0R2Y3Mza0tyVW9PZGxLdVJzQ2V3ZGE5TDRCSW1WYzRXZUV5b1JpTmpBdXpmZDVqaWNXaDJXU2NtSXJzU3hBNnlEZ0NXcHJzckFMYVRTbjdxaXo3NVVlN0c0MkhtNGNHMFRMdUlTaE9JTjBIcXZ3ekVITzYyWUNsNTFwa29rUnZDY04zNzUtMzBmVFhqSWdESkh5dw?oc=5>

### Did Record Special Dividend Just Shift Costco Wholesale's (COST) Investment Narrative?
- Summary: Costco announced a record special dividend, potentially altering investor perception of the company.
- Date: 2026-11-13 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiiAFBVV95cUxPMDdPeHZmZUlhTThJV29KWVROTUNlc3RSZ1hWb3NEYjlOWlI5Nlk3QWYwS2dLd3ZXNTJFdzgwNWVTRkpKNkhBZGFjWVBoXy1sLXBybkRuSGRVZl84LUdnUERuUFVSa3hsT2g1OVN0YnZMTklHTE03eWJLbGNhdXdTOTVLcjRWbWNz?oc=5>

### Costco Has Charged $1.50 for Its Hot Dog Since the 1980s; Now It’s Paying Shareholders $13.3 Billion
- Summary: Costco's special dividend totals $13.3 billion, marking a significant payout to shareholders.
- Date: 2026-11-11 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxONGVVZUNGcmlfZGJsMUhaNkxMVzJaVnF1aFNGZ1BzVEcwY3NnV2wweXNyZXhYa2w0ZURFU0hCN0tpbzMzUHA0UGtRSWlnRGVSaXg5YVdVUlZkNWc1Vk91YlBuQzVqQ1dHaHlWLURHX040YmMtSDN0Q0k0QTdxQThKZ24zamRfaUJLMFhBZzVaaS16dw?oc=5>

### Does Costco's Special Dividend Offer Enough Reason to Buy the Stock?
- Summary: The special dividend raises questions about its attractiveness for investors.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxOeTdtbDRIRDdBamhHeEh5UG5CRG1xR3lGRXRZbFhVTEZUbU9OOWVpSmhSUUNEdmw5dE1JSFg0ZE5fSHdQUU4wd2c0WE5qNWxodTZIUjZ6U2h5Z0kwS01ZNUdoR0pCRndoSGJrNTZldzVsR2lDdHdmUmRnNi1LQkw4b1AtMFM4N2ZqM0RiSkZvRERZcjdFUWgycDhta0VndERBNUtyRnhVdjAyZVR1WmRYMG0yMVllbTBqUm1IR3JFTFc?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **COST** | **52.60** | **13.70** | **33.77** | **11.10** | **490,194,108,416.00 USD** | **20.29** |
| WMT | 45.75 | 10.36 | 24.65 | 5.90 | 1,019,350,286,336.00 USD | 25.97 |
| TGT | 16.71 | 4.11 | 10.14 | 5.30 | 73,346,203,648.00 USD | 84.36 |
| BJ | 24.14 | 6.35 | 14.37 | 15.70 | 13,937,562,624.00 USD | 17.40 |

Peers fetched as_of: 2026-11-13; COST reuses existing data (market data as_of: 2026-11-13); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-09-24
- Next expected earnings: 2026-12-10 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-13

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
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

- https://news.google.com/rss/articles/CBMilwFBVV95cUxQNU1XWlFxZWMyYTg0NHd3by15cjhlX3FBQXhnaFpiT2JXRXR2VVRLQmZsbUJVN2Fmd3lJMTdpRUhQNUpNcC1uLUUtYUlnS00yQVZhSVFDWHgtbm9oajE4ZlktcHFvQWZJRVlZZ1hNYmxsQmZaMHFOdHVxZUhIVkN1RmhkY05KaVRsb0lNdFdCVUNkSWI4QmNn?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxPYU03ekRHaEc0TWl0STFiVExmZnBzd0xRTXdpa2ctc05XeS1qRWlvb3J1NFdaMHVFc2lsLVNkeG1meGZSZTN6MUlLeTRNZFI3c19JeEhWbTlFdFV3MkxJWkt3a05iWVp3ZnZYanZXSTNWV21pLVZ6NTFrT3ZFYmZSOEVFN2pONzdlNHdSOHFYQTJJVzkxeWZQYmZjSlpJMmc?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxQa291TURNOHhHbFAyQXc4VlJYMW5pLWlYTjlVSHhIYnUxdU91bVBiTTZmMkNyYjBsbXBaY25QTFpUUE15X3MtcTFIUUFWd2lPU05EcXhicnZDeHdDaUVxaE90TWlGa0c3ZlU4LUk5THQ3dXdQYncxaXdOQlBETnE1NlpZQUdNdUUzV1JUelJYenRjcm9uVXI4eWRXcWdiajQ3YUptNVNPSGRPck8zWGFXdE1n?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxONmlOcVI4ZEp0c2tIcG1nTjBhLTRhNG5reW9UMTR3dkhaWFViS2FYUTgyZy05RDNNUElHQ0dsMjZuUVpXX3ZGZGhzSkF3MWlqaWpyWVJZM3BJSkVIcTVEY25ULTZUb0lVWmRSMC1SVmY0cnJmU0lCbkVONEk1ZXBSbXFsVVZuUi15allxR012c0x2MVlOT1k1a1JKNUNfSEgwYVlteHdYbnV0RExPVmJfTklkbmppRWthVHl2SjJOWWZuOFhWMTJfNkpIRWtCbEVEMV9OVzd3?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxQaDhILTlrOW5MYlAwM2NmT090b2FrVWRpQnhZQXFsMW9BOWVNLUdXbFowdEg1eFFETEZLTUVxQldTTWhGNTJiNUdKbzJ5OHNvVEFOanhIN2FLXzdKTFljb0NIY3g4ZGZGOV9fQ2xEa0Q3WXZPX0QydmdpV3NYQm1qakhtUXZhdXlEazBjMXVUWThxOEJDZXRkVW9CZC11SXN2anh0RXpwb0dhMUp5MkozNmJzNXFxampRVEE?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxPd040dEdhY1J1bGdUTE5jakswU0d5VTR3cTF6cmVKVGFiQ0o0OG0taVdmMm15ZGQ5dFEzTEJfS3BoWU1wVDZsVUROdUZhSDFzOENDUEhVRTBYQzc5RXdvVENKd3lrY21Rejg2NENfaFNpUDk3RmNSOGhsWE9mNG9GTDhMempQVklNcUxIaDl0UnRCdkhIaDQwYk1uazZ2dXVNblJ0X3FrTXBiYUczRGJr?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxNNzNkc1pDQ3duTWpMajdNcDBRV3NEdnhlb1FRY3lvWC02WGtWVWpCdXRxV0JDWnFleUxaUktzMHpmWkZIclRPNWE5Vl9ySDg5aFhlalp6R1gzc2RCaG5hc0tMQUl4MWl0aDN4a3hGS2xSblVyOHplMjExSlhDTWd0cWhEMm5yZmt3N2tJdjZWenhzNm5pd1F3ZEtkdkw3ZU1ndXNySFUxRmFwR2QwVDY0bklYdExpMzg?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNVk1SbzRkY0hkTVlRbk9LWHduY2lLZnJjeUIxU3NvbWVNLWhVZFFJMjNJYUNlSF92N2p5YTY5RFFocmVYSGdKakNybjRTeVZZd250OGg0aWNVVmR6UzFhVHpXRnhVREVmbHJ0RXBVZU5HUVRWelYyRUFxOVhHeHN1QXAxUGxYRVZJSW93OEhjSnJ0V3BGMm9OeURlbk8?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxNU2VSTlhQZTRsaGYwMGR4UFF3MTJGVUhHMG84dEdxUWVTM0dFeEJ1UDFsX25sbVJCUzZ2TTFhT2Jpck5uX29OekdvejhHREpJQk5uRnFmR2xOazV4SjJLdFlvc0JRWGQyQVJsZHkyOWRkem80TzZ1X3A2QUlBZldXQ2dYS0xXNERZOEJtSy16b1M5RDZucDNxOGJ2S2NYbl9zZ3VXdmRPYnE?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxNNDhKRGlWaVlleFYxdl9yZTJBTGc5Z0plWEp0Zy1sOTdiNGNneDd6bWkxOEtWRUtBN250aU1Ta2FZcEg3WFRNMXl5b1ZDN1NTLU03R3ZSckgxb1BFelRFUGtLMlFrVThxeFRFNUQxdDRNTkJGdFNuSi11WEdiNjh4QWxWbEwzOF9fZXliazd0RXh2Zw?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxQM1NLVHZLbFU0ZmtaeFVRcGpvMGtoVjFrWkczdXYxSDFmemkzTllHUzR5ek9ZSUNNdlFxdG0zQmZEdllkTlQ0TEpMUlVwcGY2UnB1eEliM2c1NThhSDl1aUhYV0xZU0tmTDFnYkJ4QzY3c05GMlF1clZPQk9mNndsd0NHM1BGMmhQdHl1aXZYREJqcExOS3NGSUtOMUEtUzA?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxPb3I3SVB4UDlwc2lJVk1CSW9XUGJDQWZJSzQ0a3ZHMjBUdEVJMmJGRG5hZHNBM1piRGVIR29Vd3Fobjg1amJsMzZxaUF3Y2tuQmNzZ0dITHBxNmd5b2RFUzNzYV9Xc2ZXenJIbXFBWjdieEZfOW5UVzY3NE1DSUJ6OFVFTUZUeVJjOHluSURpclRtRGx3TTQxdWVLaF81cVJuUk1ac2R4QlZuS2ktRExva253?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxPUE1WSmdhN1FQOHVaQ0hTbFN0NTZia3BpQTRPX3FrMEtYYkljb2g4QTdDRU5WM2tkdXp2a0oxME1yXzhZYkRIdmUtNnZQUU5weFZTR0ZQMTFRX2RmLWdFM3VRRjFoY0tkaXlMYVROWjBqZWQxMmw2emRvdk53a251dFNWWFRtR2lXck9kRTgwRy01UUk?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNLUFoMFA3dXFHeTA3SjFMNmp6dE9tMkNtb3BWY1JxMkx0dFBxRU9rNVNKTEN1UV9JVjVJZGVleTQ3YzZ5MjVJUGVLNUg2ZUNENk1BOHpYUkhiWDhOYUNrNnpibnFwRlI4XzdTOVBVbmpKaHByRWlNVUhSSTFMR3J6NkVVVGlreWk3dTQweEM0WG5zSk50Z1R5bkg1QTM?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxPYVNac1hIUHdZQ1YtZ3JyVC1ONzNNanhheDg5dzNla3pjeUVGYnNvZXpUbHB1SGxhZG9mdTlQekFmN1NoMW1wR0hHUTd6ZHpYYmUtNHVaTUZmVlVSUmV0a1ZhUzNrVExiR0VaMk1rR2pYdDctQXRIUExuTXl0U3RuaHRTME03THRLN0FkUWVn?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxQSURnd0R2Y3Mza0tyVW9PZGxLdVJzQ2V3ZGE5TDRCSW1WYzRXZUV5b1JpTmpBdXpmZDVqaWNXaDJXU2NtSXJzU3hBNnlEZ0NXcHJzckFMYVRTbjdxaXo3NVVlN0c0MkhtNGNHMFRMdUlTaE9JTjBIcXZ3ekVITzYyWUNsNTFwa29rUnZDY04zNzUtMzBmVFhqSWdESkh5dw?oc=5
- https://news.google.com/rss/articles/CBMiiAFBVV95cUxPMDdPeHZmZUlhTThJV29KWVROTUNlc3RSZ1hWb3NEYjlOWlI5Nlk3QWYwS2dLd3ZXNTJFdzgwNWVTRkpKNkhBZGFjWVBoXy1sLXBybkRuSGRVZl84LUdnUERuUFVSa3hsT2g1OVN0YnZMTklHTE03eWJLbGNhdXdTOTVLcjRWbWNz?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxONGVVZUNGcmlfZGJsMUhaNkxMVzJaVnF1aFNGZ1BzVEcwY3NnV2wweXNyZXhYa2w0ZURFU0hCN0tpbzMzUHA0UGtRSWlnRGVSaXg5YVdVUlZkNWc1Vk91YlBuQzVqQ1dHaHlWLURHX040YmMtSDN0Q0k0QTdxQThKZ24zamRfaUJLMFhBZzVaaS16dw?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxOeTdtbDRIRDdBamhHeEh5UG5CRG1xR3lGRXRZbFhVTEZUbU9OOWVpSmhSUUNEdmw5dE1JSFg0ZE5fSHdQUU4wd2c0WE5qNWxodTZIUjZ6U2h5Z0kwS01ZNUdoR0pCRndoSGJrNTZldzVsR2lDdHdmUmRnNi1LQkw4b1AtMFM4N2ZqM0RiSkZvRERZcjdFUWgycDhta0VndERBNUtyRnhVdjAyZVR1WmRYMG0yMVllbTBqUm1IR3JFTFc?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
