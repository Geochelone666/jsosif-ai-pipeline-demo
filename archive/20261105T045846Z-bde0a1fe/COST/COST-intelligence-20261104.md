# COST Intelligence Report

- ticker: **COST**
- Report as_of: **2026-11-04**
- Market data as_of: **2026-11-04**
- Quant sources: https://finance.yahoo.com/quote/COST/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/COST/key-statistics/
- AI analysis snapshot as_of: **2026-11-04**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-05T05:04:21.646490+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 4, 'ai': 13, 'unknown': 0, 'irrelevant': 8})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **5** exact headline/source/date matches; prior report **20261104T044411Z-6b13f9ec/COST** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'negative_sentiment_in_tailwinds': 1}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 12 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 36.0%; oldest publication 2026-10-29

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 1046.4700 |
| Return 1D (%) | 2.6696 |
| Return 1W (%) | 6.6434 |
| Return 1M (%) | 13.8344 |
| Return YTD (%) | 22.0681 |
| Return 1Y (%) | 11.8951 |
| Annualized volatility (%) | 20.2183 |
| Beta vs SPY | -0.1726 |
| Max drawdown (%) | -18.1993 |
| Sharpe (rf=0) | 0.6590 |
| Downside deviation (rf=0, %) | 13.8328 |
| Sortino (rf=0) | 0.9631 |
| Historical VaR 95% (1D, %) | 2.0802 |
| Historical ES 95% (1D, %) | 2.7374 |
| Correlation vs SPY | -0.1096 |
| Tracking error vs SPY (%) | 25.1101 |
| P/E (trailing) | 49.11 |
| P/B | 12.96 |
| EV/EBITDA | 31.91 |
| Revenue growth (%) | 11.10 |
| Forward P/E (estimate) | 41.81 |
| Gross margin (%) | 12.77 |
| Operating margin (%) | 3.79 |
| Return on equity (%) | 28.40 |
| Free cash flow yield (%) | 1.46 |
| MA50 | 946.5687 |
| Close vs MA50 (%) | 10.5540 |
| MA200 | 969.0733 |
| Close vs MA200 (%) | 7.9867 |
| RSI (14, Wilder) | 69.0312 |
| MACD (12,26) | 23.9138 |
| MACD signal (9) | 20.5797 |
| MACD histogram | 3.3342 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'COST': 275, 'SPY': 275}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 1046.4700 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 2.6696 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 6.6434 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 13.8344 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 22.0681 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 11.8951 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 20.2183 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 13.8328 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.9631 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.0802 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.7374 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.1096 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 25.1101 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.1726 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -18.1993 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.6590 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 41.8123 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 12.7660 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 3.7890 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 28.4020 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.4562 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 49.1070 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 69.0312 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 3.3342 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 10.5540 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 7.9867 -> Clearly above the moving-average trend level.

## TAILWINDS

### Costco Wholesale (NASDAQ:COST) Stock Price Up 2.7% - Here's Why
- Summary: Costco Wholesale (NASDAQ:COST) Stock Price Up 2.7% - Here's Why
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxOdlRWenc0amRmcDVNNV9RNU1UYnY2WUtnSC0tS1FYcGdydm5uWmJWY2RpSG43eVQ5cmFJUHJyS0EzLW1IWDhXRlFlTFVPSnR3SXdRSGNBZDZEcDdWcmNwTk9oTEF2S2VNTzVRbzlkbXhGSWpOOEVaRU43MVdiQ1dHX19Yd05uTkFGWWtpaHNaMGNkNmZRQU40Y0M5VGM1NDFueEZsaVpFaG1kNHIyZmtDNnNzRVFKRDQ?oc=5>

### Why Should Costco Stock Holders Watch This Number?
- Summary: Analysis of key metric influencing Costco stock performance.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMirwFBVV95cUxNM3BldWVTN1JRWnl0aFJPSXhUZlRSbDdhVkhGWEpNSU9hcTdYOTdQRVE2VnlNZ203X0h1RDJkLTNadXdjNU9najZjc21OMEl1Z0FtU3ZsdEZsS3gyOXd2bURqTzRuQThsZ1lQR1B0U1JNOVlKTUZtdy0tdmgtSGpXZWZFS2ttRzc5QVVleTFvcFVvdlcxWjJZcEdWSVMwUkN6cGV3c2NSbFJlTVlRUkVR?oc=5>

### Costco outpaces broad retail again with double-digit sales growth in October (COST:NASDAQ)
- Summary: Costco reports double‑digit sales growth in October, outperforming broader retail.
- Date: 2026-11-04 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxPcWRwUUlPTGctY0RiRE9FVXFGeU1tV0F4WjEzZXFOeGdtZ2tCU1pUZFhLU2dSVEd5UG9MLTFLbzYyZzZZOV9rZFJ4WXYwdU1PSmxGOVlHbjZGVjFCTHF6NE1BSXdsOTEwc21RZ0hoZktOcVZUS3ZXT0E1RklNcHltcjhsU3VoOElWUDFxRVhsZXFRUGJNWGdYeGxYaC0yMk51Zk5jQ0twNklnRGRUSWhpc29rSEk?oc=5>

### ETFs Are Buying Costco (COST) on Monday
- Summary: ETF purchases of Costco shares increase, indicating institutional interest.
- Date: 2026-11-04 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxQTnZMRlhNZDR2OWFRbnFBeG9TcXRsMjk3Y3BpOTREajNxZk90VzI3NGVaa1ZCcFFpTXNOMzFnQXgxR05GdGd1YVhlSUNRQUZYcHlIOWZIMTVOVXczMUw5eURrUkZNMEZtMDI3anJuTk05MWIxNlU5OTZ2eVIwSFFIN0FxV180MTVmVnNLbmFlSkJLanoyNThvMnY3Zw?oc=5>

### ETFs Are Net Sellers of Costco (COST) on Thursday
- Summary: ETFs sold Costco shares, indicating a short-term market move.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxPYTBMbElWV2hVeEZPVl84aG5zNE9vZ01KRzAycGdrclhTaHFLaUw3QU9HVHFNNHJJQ0wyQUtvbUZWTnlNUE43Q1A2WmJZSlRWbk0zUEVsWXpnRGJIM1lKMnlvVFpJb3NxVHk1cTA1Qkprd1dKcU83VUo2WHM2ak9qX3NYOXp3Vjl2TEx0LVZDclp5RkJwZEZUSw?oc=5>

### Costco's digital sales rose 22.5% in October
- Summary: Digital sales up 22.5% in October, boosting revenue growth.
- Date: 2026-11-04 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxQREhtcG53U19CWmVxeUlNdUFhd3FMNVQ2Y3hUVktPM3U2YnBOckc1YWFzd2hnR3gzUmpPLTJXNXpvSWpUQU9WZlFZLW5oUEc1TVZSU3lldE01clhPUWROOThXYTJtU3RKZHBhLW5Jd2p1RmZlVWNYNVJOeEZkdENJanVQb2JmOVhxVFpxUV9tV1hsUjg2NC1JX2tQWU9LdHlZRTlMTng3VE8?oc=5>

## HEADWINDS

### Costco (COST) Stock Looks Stretched As Its 113% Five Year Run Continues
- Summary: Stock appears overvalued, raising concerns about future upside.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi3gFBVV95cUxNcUF0VlFYVmEtam8wSUFGTE5jZVpzcHVVN2xUTV9mOHAxUGh0MmItdkk0a0o1YlZtcGN6UGpTUi00REFHSmZKODA4ZHpPNTBZQUswWGlyU3dPaExkVVNONEowV3YwNlAxMnk0d0lUM0FZd19aeFdKYXFBRDJIR0d2SmE3QkdXOWZNZWJPLVljOUlCTDdNOXVQMHZoWXlBTGhEcmdncUZhOUVONDRHcXB2UDFRSE5XRHpfTzJTb0l0eDF0OE03cVp5eTdCNW1FRzhZQ1pjWkIxR2JVNndSS0HSAeMBQVVfeXFMUGRISkJ5Ri1KbHkzV1F4bndYZENwa3NuNFZ6SndVSnFLTTlneEh5UEdQc2o5S0QxOGZvLUxzTDZxNWtVR2ZETHlRVkVrd1hTTnRlMjB3ZEZad3QwZ1MweWJmMEVFYVBNMVJ5d2liZDYtV19DcXR6dE5lTWZfWTlKd0JtR2VGTDIyNEQ5M1RuUWJGU21yQzVrSHo1N2tnc2JsZ2xTY0l1WkxvaXhlSnlhNkloTG1lc2dJYXJUalhmd1FJb2E1Z1gtY2w2cDFVeXMyRHZ6aXRmS3UyMXZDWmJ1bUdIQk0?oc=5>

### A Third of Costco’s U.S. Sales Growth Is Just Pricier Gas
- Summary: Sales growth driven by higher gas prices, indicating cost pressure.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxNcGloWUk5dHpNWEZvN0liODV3aVFocnN0VkhySWpfTUpBYW5fMFVJbVloVzEyQ3JnaFdaaUVwT3V3dy1ySkZIWmJYNm1HOXIxXzdyY2FPczVnZW50WjFBOVBJekFfWUQzN0pqOTVNdjd0MkM5OGNIam1yeDZWLTBwMFRMN2RmZWZhdGxyVkhBR0JKUQ?oc=5>

## CATALYSTS

### Costco Wholesale Stock Is Trading Over $1,000. Here's Why a Stock Split Still May Not Come in 2027.
- Summary: Costco Wholesale Stock Is Trading Over $1,000. Here's Why a Stock Split Still May Not Come in 2027.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxQTXREUHFXa21EQXYwT3I0VFNEWlhlWWdlMWYxLTZuT2dkNkZNRjBSQ0J2LV9aVnhyWk94RGNVRGQwaWN4S1k4aERNbmROckpoNS1CSUdQSER4MzZVRzIwYURwcDlIUTBhaEROZ0RzMVBQUGw1bHc1VWhXRGktR0t0bTVBemM3eFlBWnZuSTBqQmlJeEZDamJR?oc=5>

### Costco Hasn't Split Its Stock Since 2000. Here's Why 2027 Could Be the Year.
- Summary: Costco Hasn't Split Its Stock Since 2000. Here's Why 2027 Could Be the Year.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxQVFpPakx4Wk9Sa1BTRkFkb1kwMjNGbmRSZVlhZFlaTUpiQUV4ckduZ1JHVTFEWFpoNjBlQkFDenlLMWJEd25xRDVZMnlMMmkzX2xZcnotVWhieGJ0ZmpsaXJ4dE1LSHFoU2prMnU1Q0hkLW8xQUNnZmZYNnNKR1g5TWpOcWR4UTBCMERCd1dIekRJNzQ0Y19z?oc=5>

### Costco (COST) Weighs Special Dividend Amid Strategic Investment Plans for 2027
- Summary: Costco (COST) Weighs Special Dividend Amid Strategic Investment Plans for 2027
- Date: 2026-10-31 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxPNGNwZnR0dTNfNEpGVlVFczFkMllsRGFEX3dGSHowR3k2RlpnT1NJSUxOOVcwSG9zaC0yRGJVX2N2OXY5VlN1R3JtMTJ4MlFZVEhteUlJQnN0TFJ2aDNGazZYTk9BQWp0a3F1ZTVjZjgxLTEyYm5QdmdGY3pYN1NNZzZwRGotcnVFWnFQbWl4YlZmMUZOTlVMS0h0UW1KWmdGdWdpb0R2UzJOYi1wSDZDLWVKN29OUQ?oc=5>

### Costco (COST) Ascends While Market Falls: Some Facts to Note
- Summary: Costco shares rise as broader market declines, indicating relative strength.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxPZW5GXzBSMXFsY2FDcklHbHVQTVB2V1RXeTVkLTZWT3pIbEczTFZta2FUN0wzaDF6clNETEplNHhFTHJHU0RXd0pVSW5EM3FJLW5sTkcwSTczc3RZNVNsSUFOLWx2ei1kSnpuU0Njb2pZLUI1VEFKaHVVeHJkSmo1SHJXQU9UUmlrWldGNEktRTFkMG1sTlFjMnUwZzIwZw?oc=5>

### Earnings beat lifts Costco stock price as bullish trend persists
- Summary: Costco reported earnings that exceeded expectations, driving a positive market reaction and reinforcing bullish sentiment.
- Date: 2026-11-04 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxPaFptTmgyS3dEYnBLZEUwNzRDZWQ1LU1LLTNCMTlkM3pKTU5NM0xjRTM0ZTloMzhXc25YS1YtdUY2TEF0c3hMSXJ5alpyXzZ1WkVuamh0ZkxuWWRVYUt0R0o5WlI0SGI4MEtIV2pjVDllVzFVaHMzbUVIVXZnTF9NcjdxUUw1aXFXT1I4RnFTc0E5VlJX?oc=5>

### Costco’s Capital Preservation Function Will Be on Display Over the Next Few Weeks
- Summary: Costco will showcase its new capital preservation feature in upcoming weeks.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxOdkozemV2R0ZkY1B0bXRyNHJxWGpCaWppdW43VFdIdzV5TXFoX1ZXdzRucFdBVEpqYXNqVHNsaWFaekFLOTh2TEROZzZ2TGhQUUNZamNtdmdQRVM5RExoX1VOSmlQcjliUmdWVVk1MnpacDk5VGtCRGZnWEFyNmRCa29SMHhmd2FpbDJMNnU1NjMzV0FQc1RrQmotek92elVieG9jVU1vOC1UV0lPbVNSci1uTEk2SGhKSFZsTjVJZ0ZYQQ?oc=5>

### Costco (COST) Reports 12.6% October Net Sales Growth, Shares Ris
- Summary: Costco reported a 12.6% increase in October net sales, driving share price rise.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxNNDlHQXVHVU9rUURuNno0VWp3a3J0dVNjNFBVc3BCcFF1TmF2VG50NGlxZUxnQnBiWlpncGNWV1dmYUFWTlA4cFc2WnpKOFdBb2ljYUdON2lRb1p5VlhPYld1eVdDWWlkbUtjWm1FZFVrdWxYZEM3MFpuRW5nQmxIbm8wMjh3MHpBN2tMUnkwLVJ0bVc0RHdVbmpGVTlNQWplWVBR?oc=5>

## RISKS

### Should Medicare Push Require Action From Costco (COST) Investors?
- Summary: Raises potential regulatory pressure from Medicare, posing a risk to investors.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxObWVYZjVuTC1CRk81TnpXTkxvcWtYb1M2ZlZIYlJINm93M1hJakVHOVNQVDhHcXZudWZMak04MV9CZVQ2SEo2YW9KbURPeVpPa3hEaVIxTkU4X0V6MGdaQ0Zpc3JLMnptQ0dLM083OGZ0VlJfNlhYdzkwQkllT1dlMEUtLXoxZmFDSlA3NnVKM0VEZkZwSDFKOEdxZzg?oc=5>

### Nvidia (NVDA), Costco (COST), Nike (NKE) join OKX–ICE tokenized stock objections, bringing total to 50
- Summary: Costco joins 50 companies objecting to OKX–ICE tokenized stocks, raising regulatory concerns.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxNT2JRbThULWtaaVVVeGEyVlZPSTQ0alVKSk1Qc2VKRGppaHVtSFoyM3Uzam1jWE1iVXFsT0dTNmFuTWJhQ3d1ZXZ6dWc3X0RvaVBSeGV5MTNvNm9MdmtyYWVNcmlkRWNMbWttQ2JQTzdEVlZ2SW5UZDRQZnJpOWtsN0V3dmtXaVdTOEZWZm5MeGpoRXZ3NjFHOGZkWEZSc2FObEZFT2hWSk1iYmZJSWxDamlQbWxFN0ppTzRv?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **COST** | **49.11** | **12.96** | **31.91** | **11.10** | **463,721,562,112.00 USD** | **11.90** |
| WMT | 45.16 | 10.44 | 24.84 | 5.90 | 1,027,945,070,592.00 USD | 27.37 |
| TGT | 16.04 | 4.15 | 10.23 | 5.30 | 74,095,804,416.00 USD | 88.60 |
| BJ | 23.95 | 6.38 | 14.44 | 15.70 | 14,008,299,520.00 USD | 22.96 |

Peers fetched as_of: 2026-11-04; COST reuses existing data (market data as_of: 2026-11-04); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-09-24
- Next expected earnings: 2026-12-10 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-04

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
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

- https://news.google.com/rss/articles/CBMitwFBVV95cUxOdlRWenc0amRmcDVNNV9RNU1UYnY2WUtnSC0tS1FYcGdydm5uWmJWY2RpSG43eVQ5cmFJUHJyS0EzLW1IWDhXRlFlTFVPSnR3SXdRSGNBZDZEcDdWcmNwTk9oTEF2S2VNTzVRbzlkbXhGSWpOOEVaRU43MVdiQ1dHX19Yd05uTkFGWWtpaHNaMGNkNmZRQU40Y0M5VGM1NDFueEZsaVpFaG1kNHIyZmtDNnNzRVFKRDQ?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxNM3BldWVTN1JRWnl0aFJPSXhUZlRSbDdhVkhGWEpNSU9hcTdYOTdQRVE2VnlNZ203X0h1RDJkLTNadXdjNU9najZjc21OMEl1Z0FtU3ZsdEZsS3gyOXd2bURqTzRuQThsZ1lQR1B0U1JNOVlKTUZtdy0tdmgtSGpXZWZFS2ttRzc5QVVleTFvcFVvdlcxWjJZcEdWSVMwUkN6cGV3c2NSbFJlTVlRUkVR?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxPcWRwUUlPTGctY0RiRE9FVXFGeU1tV0F4WjEzZXFOeGdtZ2tCU1pUZFhLU2dSVEd5UG9MLTFLbzYyZzZZOV9rZFJ4WXYwdU1PSmxGOVlHbjZGVjFCTHF6NE1BSXdsOTEwc21RZ0hoZktOcVZUS3ZXT0E1RklNcHltcjhsU3VoOElWUDFxRVhsZXFRUGJNWGdYeGxYaC0yMk51Zk5jQ0twNklnRGRUSWhpc29rSEk?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxQTnZMRlhNZDR2OWFRbnFBeG9TcXRsMjk3Y3BpOTREajNxZk90VzI3NGVaa1ZCcFFpTXNOMzFnQXgxR05GdGd1YVhlSUNRQUZYcHlIOWZIMTVOVXczMUw5eURrUkZNMEZtMDI3anJuTk05MWIxNlU5OTZ2eVIwSFFIN0FxV180MTVmVnNLbmFlSkJLanoyNThvMnY3Zw?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxPYTBMbElWV2hVeEZPVl84aG5zNE9vZ01KRzAycGdrclhTaHFLaUw3QU9HVHFNNHJJQ0wyQUtvbUZWTnlNUE43Q1A2WmJZSlRWbk0zUEVsWXpnRGJIM1lKMnlvVFpJb3NxVHk1cTA1Qkprd1dKcU83VUo2WHM2ak9qX3NYOXp3Vjl2TEx0LVZDclp5RkJwZEZUSw?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxQREhtcG53U19CWmVxeUlNdUFhd3FMNVQ2Y3hUVktPM3U2YnBOckc1YWFzd2hnR3gzUmpPLTJXNXpvSWpUQU9WZlFZLW5oUEc1TVZSU3lldE01clhPUWROOThXYTJtU3RKZHBhLW5Jd2p1RmZlVWNYNVJOeEZkdENJanVQb2JmOVhxVFpxUV9tV1hsUjg2NC1JX2tQWU9LdHlZRTlMTng3VE8?oc=5
- https://news.google.com/rss/articles/CBMi3gFBVV95cUxNcUF0VlFYVmEtam8wSUFGTE5jZVpzcHVVN2xUTV9mOHAxUGh0MmItdkk0a0o1YlZtcGN6UGpTUi00REFHSmZKODA4ZHpPNTBZQUswWGlyU3dPaExkVVNONEowV3YwNlAxMnk0d0lUM0FZd19aeFdKYXFBRDJIR0d2SmE3QkdXOWZNZWJPLVljOUlCTDdNOXVQMHZoWXlBTGhEcmdncUZhOUVONDRHcXB2UDFRSE5XRHpfTzJTb0l0eDF0OE03cVp5eTdCNW1FRzhZQ1pjWkIxR2JVNndSS0HSAeMBQVVfeXFMUGRISkJ5Ri1KbHkzV1F4bndYZENwa3NuNFZ6SndVSnFLTTlneEh5UEdQc2o5S0QxOGZvLUxzTDZxNWtVR2ZETHlRVkVrd1hTTnRlMjB3ZEZad3QwZ1MweWJmMEVFYVBNMVJ5d2liZDYtV19DcXR6dE5lTWZfWTlKd0JtR2VGTDIyNEQ5M1RuUWJGU21yQzVrSHo1N2tnc2JsZ2xTY0l1WkxvaXhlSnlhNkloTG1lc2dJYXJUalhmd1FJb2E1Z1gtY2w2cDFVeXMyRHZ6aXRmS3UyMXZDWmJ1bUdIQk0?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxNcGloWUk5dHpNWEZvN0liODV3aVFocnN0VkhySWpfTUpBYW5fMFVJbVloVzEyQ3JnaFdaaUVwT3V3dy1ySkZIWmJYNm1HOXIxXzdyY2FPczVnZW50WjFBOVBJekFfWUQzN0pqOTVNdjd0MkM5OGNIam1yeDZWLTBwMFRMN2RmZWZhdGxyVkhBR0JKUQ?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxQTXREUHFXa21EQXYwT3I0VFNEWlhlWWdlMWYxLTZuT2dkNkZNRjBSQ0J2LV9aVnhyWk94RGNVRGQwaWN4S1k4aERNbmROckpoNS1CSUdQSER4MzZVRzIwYURwcDlIUTBhaEROZ0RzMVBQUGw1bHc1VWhXRGktR0t0bTVBemM3eFlBWnZuSTBqQmlJeEZDamJR?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxQVFpPakx4Wk9Sa1BTRkFkb1kwMjNGbmRSZVlhZFlaTUpiQUV4ckduZ1JHVTFEWFpoNjBlQkFDenlLMWJEd25xRDVZMnlMMmkzX2xZcnotVWhieGJ0ZmpsaXJ4dE1LSHFoU2prMnU1Q0hkLW8xQUNnZmZYNnNKR1g5TWpOcWR4UTBCMERCd1dIekRJNzQ0Y19z?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxPNGNwZnR0dTNfNEpGVlVFczFkMllsRGFEX3dGSHowR3k2RlpnT1NJSUxOOVcwSG9zaC0yRGJVX2N2OXY5VlN1R3JtMTJ4MlFZVEhteUlJQnN0TFJ2aDNGazZYTk9BQWp0a3F1ZTVjZjgxLTEyYm5QdmdGY3pYN1NNZzZwRGotcnVFWnFQbWl4YlZmMUZOTlVMS0h0UW1KWmdGdWdpb0R2UzJOYi1wSDZDLWVKN29OUQ?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxPZW5GXzBSMXFsY2FDcklHbHVQTVB2V1RXeTVkLTZWT3pIbEczTFZta2FUN0wzaDF6clNETEplNHhFTHJHU0RXd0pVSW5EM3FJLW5sTkcwSTczc3RZNVNsSUFOLWx2ei1kSnpuU0Njb2pZLUI1VEFKaHVVeHJkSmo1SHJXQU9UUmlrWldGNEktRTFkMG1sTlFjMnUwZzIwZw?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxPaFptTmgyS3dEYnBLZEUwNzRDZWQ1LU1LLTNCMTlkM3pKTU5NM0xjRTM0ZTloMzhXc25YS1YtdUY2TEF0c3hMSXJ5alpyXzZ1WkVuamh0ZkxuWWRVYUt0R0o5WlI0SGI4MEtIV2pjVDllVzFVaHMzbUVIVXZnTF9NcjdxUUw1aXFXT1I4RnFTc0E5VlJX?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxOdkozemV2R0ZkY1B0bXRyNHJxWGpCaWppdW43VFdIdzV5TXFoX1ZXdzRucFdBVEpqYXNqVHNsaWFaekFLOTh2TEROZzZ2TGhQUUNZamNtdmdQRVM5RExoX1VOSmlQcjliUmdWVVk1MnpacDk5VGtCRGZnWEFyNmRCa29SMHhmd2FpbDJMNnU1NjMzV0FQc1RrQmotek92elVieG9jVU1vOC1UV0lPbVNSci1uTEk2SGhKSFZsTjVJZ0ZYQQ?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxNNDlHQXVHVU9rUURuNno0VWp3a3J0dVNjNFBVc3BCcFF1TmF2VG50NGlxZUxnQnBiWlpncGNWV1dmYUFWTlA4cFc2WnpKOFdBb2ljYUdON2lRb1p5VlhPYld1eVdDWWlkbUtjWm1FZFVrdWxYZEM3MFpuRW5nQmxIbm8wMjh3MHpBN2tMUnkwLVJ0bVc0RHdVbmpGVTlNQWplWVBR?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxObWVYZjVuTC1CRk81TnpXTkxvcWtYb1M2ZlZIYlJINm93M1hJakVHOVNQVDhHcXZudWZMak04MV9CZVQ2SEo2YW9KbURPeVpPa3hEaVIxTkU4X0V6MGdaQ0Zpc3JLMnptQ0dLM083OGZ0VlJfNlhYdzkwQkllT1dlMEUtLXoxZmFDSlA3NnVKM0VEZkZwSDFKOEdxZzg?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxNT2JRbThULWtaaVVVeGEyVlZPSTQ0alVKSk1Qc2VKRGppaHVtSFoyM3Uzam1jWE1iVXFsT0dTNmFuTWJhQ3d1ZXZ6dWc3X0RvaVBSeGV5MTNvNm9MdmtyYWVNcmlkRWNMbWttQ2JQTzdEVlZ2SW5UZDRQZnJpOWtsN0V3dmtXaVdTOEZWZm5MeGpoRXZ3NjFHOGZkWEZSc2FObEZFT2hWSk1iYmZJSWxDamlQbWxFN0ppTzRv?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
