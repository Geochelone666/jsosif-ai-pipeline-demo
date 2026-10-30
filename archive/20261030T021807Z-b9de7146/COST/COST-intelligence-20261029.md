# COST Intelligence Report

- ticker: **COST**
- Report as_of: **2026-10-29**
- Market data as_of: **2026-10-29**
- Quant sources: https://finance.yahoo.com/quote/COST/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/COST/key-statistics/
- AI analysis snapshot as_of: **2026-10-29**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-30T02:22:01.297398+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 21, 'rule': 6, 'ai': 8, 'unknown': 0, 'irrelevant': 7})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **6** exact headline/source/date matches; prior report **20261029T020157Z-688a53f0/COST** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 21 unique headlines; 10 named publishers; 4 exact duplicates; 21 HTTPS source links; largest publisher share 23.81%; oldest publication 2026-10-22

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 996.0800 |
| Return 1D (%) | 1.3585 |
| Return 1W (%) | -2.1734 |
| Return 1M (%) | 7.7321 |
| Return YTD (%) | 16.0188 |
| Return 1Y (%) | 9.8060 |
| Annualized volatility (%) | 19.8278 |
| Beta vs SPY | -0.1861 |
| Max drawdown (%) | -18.1993 |
| Sharpe (rf=0) | 0.5726 |
| Downside deviation (rf=0, %) | 13.7040 |
| Sortino (rf=0) | 0.8284 |
| Historical VaR 95% (1D, %) | 2.0766 |
| Historical ES 95% (1D, %) | 2.7374 |
| Correlation vs SPY | -0.1193 |
| Tracking error vs SPY (%) | 24.7957 |
| P/E (trailing) | 47.98 |
| P/B | 12.33 |
| EV/EBITDA | 30.33 |
| Revenue growth (%) | 11.10 |
| Forward P/E (estimate) | 39.80 |
| Gross margin (%) | 12.77 |
| Operating margin (%) | 3.79 |
| Return on equity (%) | 28.40 |
| Free cash flow yield (%) | 1.53 |
| MA50 | 941.7280 |
| Close vs MA50 (%) | 5.7715 |
| MA200 | 968.9761 |
| Close vs MA200 (%) | 2.7972 |
| RSI (14, Wilder) | 61.8808 |
| MACD (12,26) | 18.6155 |
| MACD signal (9) | 18.3727 |
| MACD histogram | 0.2428 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'COST': 271, 'SPY': 271}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 996.0800 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.3585 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -2.1734 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 7.7321 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 16.0188 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 9.8060 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 19.8278 -> Low annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 13.7040 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.8284 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.0766 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.7374 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.1193 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 24.7957 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.1861 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -18.1993 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.5726 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 39.8013 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 12.7660 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 3.7890 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 28.4020 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.5299 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 47.9807 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 61.8808 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.2428 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 5.7715 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 2.7972 -> Slightly above the moving-average trend level.

## TAILWINDS

### Costco Wholesale (NASDAQ:COST) Shares Climb 1.4% - Here's Why
- Summary: Costco Wholesale (NASDAQ:COST) Shares Climb 1.4% - Here's Why
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxPMVJKZXpVRDhNY3gtN3N6SnBzeHFwdTh2bFdGcWNEaWY0MkdxdlN6cWlIcFVPX3l6ZVpHcngyX1dxekxvYVFpdjRnVGdIZUZHSjFfb3J2VVcyak1FYkhDQ1RrbGhXbGk4cjNfcW9GeTNTY0g5c3BIV29DQ3BiU25hcU1LYWI5SVRobjlSQlpuN19Zdzc0cW9XTWdHcTRKUFUtaEJwbm44UW1rZlFuNTF3MDdyRUI?oc=5>

### Costco Stock’s Long-Term Upside Could Come From These 3 Competitive Advantages
- Summary: Highlights Costco's competitive strengths that may drive future growth.
- Date: 2026-10-29 | Impact: low | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxNTHFpYjU3dTdiUWpzY3F6dkdiQWp1TWtDaXlUeGtGVHVrcm03dmpyV3JGWmJWM1pTSGpKQVBYVkVLRHJsNmNPQ0Z3bU9jTnI5dDhCRk80a3ZaTHhWbFYyNFh1a0NCdDJyZ0VhbXRISmlxdzZETzBTR3c5c3VRNVhYRjZCdnRiYmNCaUNVdXJUNTlpb0pSR3EwNHFqeEZzbU1tQm1yNjByVjZqcnFYRDR4ZS1jMFprX0dDZllVSjZn?oc=5>

### Own Costco Stock by Oct. 30 to Qualify for Its Nov. 13 Dividend. Here's How Many Shares You'd Need for $1,000 in Yearly Dividends.
- Summary: Explains dividend eligibility and share requirement for $1,000 annual dividends.
- Date: 2026-10-27 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxNeXBxZmdCWExtY2pyVTB0YU9PSGl0WXpWT0pkMl9Fb3QyVDZmMmdtWThGMVlQMUppamk5R0t2TUVuM2FJU00xVC1yUzN2QUx5RzhkWmF3a1lXdXpWVjl6UkNBLXFtYkVEc1BtMW9GajdFUkpyaGdZZ1FlSUQ4U1lBSl9xd3BGbnU2d3ZtbHU3bjFyM3Vtam1N?oc=5>

### Is Now a Good Time to Buy Costco Stock?
- Summary: Presents analysis on current buying opportunity for Costco shares.
- Date: 2026-10-29 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxNVkJKZEZjSGdScklXYVpwM29ad3VuSzFPTGNZZXdKSzdDbC1wWGhLbldrWng3aGpiUWR3bjlTbzlXaDhjVzRhS1J5VHZCSGljaHNyTE1JZEw2c1hVdzVqdl9zbUlXa0R6ZDJHLU03SldzWVdEYXlUWE9ZZWo4b185M1NDWXJxb1lHMjItQU43bHlhaTg?oc=5>

### What Did It Take To Hold Costco Stock?
- Summary: Discusses criteria and benefits of holding Costco shares.
- Date: 2026-10-29 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxPalAyLXZfMkVNejRscjhNSnZsWEJrRkMxYmdpNklzeHRJQ3dtOUFneV9QSzRGbGdLM0NhUjRGYVFlZ2pxZG9hMkxSUzB1RndyeXBrU2NsSDdWWUJlaEVrczE4NHY3MXk3emJkVjNJSW9kM0d6ZUxqQkFPR1BpM0lvcVVYc0o3eklreURwbjYtQlJnVlNZOURUbnQ2WFpzblE?oc=5>

### Costco (COST) Stock Price Forecast: June Sales Up 10.6% But Stock Fell After Hours - Short to $899?
- Summary: Forecasts price movement after sales increase and after-hours decline.
- Date: 2026-10-28 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizgFBVV95cUxNRzZhVEh2RktiaUpZMldjMmJiUmx5V3lBdUhhVUdxVHlYYlViT3RCeHF5N0lmVmZ2aEhpdkFCb2pwWmpXZWg4YUZ1ejJHaHRIckVDSWtsQlpLbTBzTk1FVDUwOE85SFZHSVVuS2dvWEVMeVU5TGU0b0lHZHpvM3M0ZmxoYzJIRWpEdDBDS2dzbndXOUFNc0U0eC1NX0ZqenhfTHZVNEZTV3pVQ2lqYUZkbzZzQlZfODZ5TjBGUnhlaWVBd0VaNzBwY01uNE8yZw?oc=5>

## HEADWINDS

### Costco Stock's Valuation Remains A Head Scratcher (NASDAQ:COST)
- Summary: Valuation concerns for Costco stock.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxNVUx6T3FXRUEwZ09IbGJBMm54Qk5jcDJJS1J2d3ZyMjFEazhIUDNMLXBkQkozTzFieW1pXzUwZ2NwdEd5QmY2S1VQeVRwNHJJNWJDcnpLbV9SNWJSeWRaRVVfQ3B5TmI1SlJBSzJGNUZsV3dDM3JSczEwX3Foc1hweUZzTUduaXRsdTkwUlQ0ZnBtNmdxblc4WVlFZlFjb2s?oc=5>

## CATALYSTS

### Costco Stock (COST) Ticks Up as the FTC Launches Pricing Probe into Rivals Walmart and Target
- Summary: Costco Stock (COST) Ticks Up as the FTC Launches Pricing Probe into Rivals Walmart and Target
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxQM3BKWGNiOU5HQXVsMEY4QXFFY1FfYWRmZU5vVE9DX19qWHhVSEtPNmZlX215YmJFM3dpTy1OV3RIVXUwaWI2a0NObDYzNThiZGtpNnVwdV9TRmtKSEhSQTdHV2I4QWUxaDRYMU1nenB2OEtFUkloX2NkZFo3VVBUZUl2eUxYbVd1azRRUTNBQVRmUXBaNGFPaDZkUDlvLTBGYmpvbUR3Sk1raUFxcXVzVmhxZ3lqOFU?oc=5>

### Costco's Last Stock Split Was in 2000. Is Its Board Close to Another?
- Summary: Costco's Last Stock Split Was in 2000. Is Its Board Close to Another?
- Date: 2026-10-22 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxOS0hEMnF3U29oM05mVE9xLXJsUVBLVHNjcVZFc0ZJWHdSWXlZdTJVSVlVb3Q0enZsazZTeGxSUFNMaTdfSHJjOGxEWDA3Sll0QUp5ZWd4OVdlcnltM1VHQmFUUURaRVpmMktsU1JfLTd5ckN5R3RNNW0xUGFhZm1tUmliYkZIWG14S2xTVlFmaWZzVkRsLU16M1ln?oc=5>

### Costco Wholesale Corporation $COST Stock: LaFleur & Godfrey LLC Increases Position
- Summary: Costco Wholesale Corporation $COST Stock: LaFleur & Godfrey LLC Increases Position
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxPY2ttWTF0eDdlTTV6d0JFMnE5NkE4dk42LVlFU1plUW1oZ0lKUGg0NW5qdW1xSk82QkdwbC1vQVljdEh6SU8zcjFuSTF2ZUZlNHU1aGwtd1FpQ1NqNlgyQkxoSElRLVd4Y1JYcmozQkhfQ2dRbzVfX0JnNTFRa3V3NkJMdjkwMWVQOU5RT3R4VTU2MzYtQnp3bGZ3Vm5wYlpMZ1RaRjA0bGotRVM5ZExPOGk2ZzNWT21kbGVhTU9tdUNZZnlKRWNNREw3VmFOQUpxYlNfSnhB?oc=5>

### Costco Wholesale Corporation $COST Stock Sold by Convergence Financial LLC
- Summary: Costco Wholesale Corporation $COST Stock Sold by Convergence Financial LLC
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizwFBVV95cUxNY0szdGEtT29jZXJ6LXdMYm1EQ1ZHZ1ZpQU1NYlAwOXBPY2tSOEdCdl85WHg2Z3d2UWd1b01XNGVvazVnYUY5NndtLXZ0TWx2NTJsRmVPVHZkMHRENWFoUHZpR0pQMnpVb2RXdUwwaUItRzRVTXZzOTJUWU43alJ3bmdZZjFzd3duemJTS0lBSmxVOE5mY1AzZHZMNDNpU1A0OVdaOW55ZzNjV0F1M3pjVTZVV0JmVkszTlNNc3BPSGRZUldpczFkWFludGFPNDA?oc=5>

### Costco Wholesale Corporation $COST Stock Sold by Arrow Financial Corp
- Summary: Costco Wholesale Corporation $COST Stock Sold by Arrow Financial Corp
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiyAFBVV95cUxQandzT2stU29id0NTanZKTnNlRHNzRko3cjBDclVPSW1pbncxTUNvQUpZSE5RT0FjX2hWejQ0Vk1IaDdUakRMcFhobldzYk5wTHlDSDlxaS12eUFHTVRiVlZnZFlLNU5uYUtRXzl5QlBNRU1BaEdueWdJS2tZdnM5X3RIQ2NINGxJcXRDdXVSRF9MTnBnZ0NKME1jSDMtbmNvbFFyZG81ZUtwY2dDbUdYa3ZzX1lBMVBRbHUtMFRCYktEX2ZFekxIUA?oc=5>

### Costco: Special Dividend Prospects Meet Expensive Valuations And Mixed Macros
- Summary: Costco may issue a special dividend amid high valuations and mixed macro conditions.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxNNGdpY0ZkVGVjN2FlRXZRZzFUOExtYWZCMnBIaFE2UEtPNFczZEJqaF96TWJNTEF0WWVwSGZoQ005NnAwTmNtbHhMSWFGb1F4YlR2UDBHZ0lBUzkwX0NDRTFacmVJT0hBdlppeWdzeEFtN2RoQjVTLXFxc3dXa1Q4LWZRRUFvdmFORkFERXdpS0V2eGJKdnVoaGFtdG40dUE1U0NKME9JelpsT1A3RHkwbHpfb04wbWlp?oc=5>

### Costco (COST) Ascends While Market Falls: Some Facts to Note
- Summary: Costco shares rise as broader market declines, indicating relative strength.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxPZW5GXzBSMXFsY2FDcklHbHVQTVB2V1RXeTVkLTZWT3pIbEczTFZta2FUN0wzaDF6clNETEplNHhFTHJHU0RXd0pVSW5EM3FJLW5sTkcwSTczc3RZNVNsSUFOLWx2ei1kSnpuU0Njb2pZLUI1VEFKaHVVeHJkSmo1SHJXQU9UUmlrWldGNEktRTFkMG1sTlFjMnUwZzIwZw?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **COST** | **47.98** | **12.33** | **30.33** | **11.10** | **441,392,300,032.00 USD** | **9.81** |
| WMT | 43.93 | 9.80 | 23.42 | 5.90 | 964,917,067,776.00 USD | 19.34 |
| TGT | 15.77 | 3.87 | 9.63 | 5.30 | 68,971,331,584.00 USD | 67.84 |
| BJ | 23.07 | 6.07 | 13.84 | 15.70 | 13,314,831,360.00 USD | 17.24 |

Peers fetched as_of: 2026-10-29; COST reuses existing data (market data as_of: 2026-10-29); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-09-24
- Next expected earnings: 2026-12-10 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-29

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

- https://news.google.com/rss/articles/CBMitAFBVV95cUxPMVJKZXpVRDhNY3gtN3N6SnBzeHFwdTh2bFdGcWNEaWY0MkdxdlN6cWlIcFVPX3l6ZVpHcngyX1dxekxvYVFpdjRnVGdIZUZHSjFfb3J2VVcyak1FYkhDQ1RrbGhXbGk4cjNfcW9GeTNTY0g5c3BIV29DQ3BiU25hcU1LYWI5SVRobjlSQlpuN19Zdzc0cW9XTWdHcTRKUFUtaEJwbm44UW1rZlFuNTF3MDdyRUI?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxNTHFpYjU3dTdiUWpzY3F6dkdiQWp1TWtDaXlUeGtGVHVrcm03dmpyV3JGWmJWM1pTSGpKQVBYVkVLRHJsNmNPQ0Z3bU9jTnI5dDhCRk80a3ZaTHhWbFYyNFh1a0NCdDJyZ0VhbXRISmlxdzZETzBTR3c5c3VRNVhYRjZCdnRiYmNCaUNVdXJUNTlpb0pSR3EwNHFqeEZzbU1tQm1yNjByVjZqcnFYRDR4ZS1jMFprX0dDZllVSjZn?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxOTGFqR2ZFQzl2ajZwNWVNRHdaVmlyZk1SdWt6MXlDdmFGM0lBQ0JUZjVyb3ZhV0VhR0lueHE1c0dSbG5XNFFMZ0c4VWpUa19vRGFtX05ReW1vRUdKUHhTT2lqOGVpZF8zZmhvWVFDbHJEX2ZNODBQcm5NVnM3MnhIbV9YYnhHT2VCVmMwZTMwTW5TWkxLZTJvZGlR?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxNeXBxZmdCWExtY2pyVTB0YU9PSGl0WXpWT0pkMl9Fb3QyVDZmMmdtWThGMVlQMUppamk5R0t2TUVuM2FJU00xVC1yUzN2QUx5RzhkWmF3a1lXdXpWVjl6UkNBLXFtYkVEc1BtMW9GajdFUkpyaGdZZ1FlSUQ4U1lBSl9xd3BGbnU2d3ZtbHU3bjFyM3Vtam1N?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxNVkJKZEZjSGdScklXYVpwM29ad3VuSzFPTGNZZXdKSzdDbC1wWGhLbldrWng3aGpiUWR3bjlTbzlXaDhjVzRhS1J5VHZCSGljaHNyTE1JZEw2c1hVdzVqdl9zbUlXa0R6ZDJHLU03SldzWVdEYXlUWE9ZZWo4b185M1NDWXJxb1lHMjItQU43bHlhaTg?oc=5
- https://news.google.com/rss/articles/CBMiiAFBVV95cUxOVW0zdGcxM1BXSWJOTlB1UlJkRTY4eXRqZFNyUW5tUDdUN04tWHpwZXdZQi10MjhqZFFEeXBXZmd2VGYtaFBDMU82Z0M5Qlk2TFB1bktVUGlsenJoVWRKeWZfaU5hbTRuVnBCUHluc1BZcFFaMFNwVVNjZUhPbF9zblo2TTAxdjZL?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxPalAyLXZfMkVNejRscjhNSnZsWEJrRkMxYmdpNklzeHRJQ3dtOUFneV9QSzRGbGdLM0NhUjRGYVFlZ2pxZG9hMkxSUzB1RndyeXBrU2NsSDdWWUJlaEVrczE4NHY3MXk3emJkVjNJSW9kM0d6ZUxqQkFPR1BpM0lvcVVYc0o3eklreURwbjYtQlJnVlNZOURUbnQ2WFpzblE?oc=5
- https://news.google.com/rss/articles/CBMizgFBVV95cUxNRzZhVEh2RktiaUpZMldjMmJiUmx5V3lBdUhhVUdxVHlYYlViT3RCeHF5N0lmVmZ2aEhpdkFCb2pwWmpXZWg4YUZ1ejJHaHRIckVDSWtsQlpLbTBzTk1FVDUwOE85SFZHSVVuS2dvWEVMeVU5TGU0b0lHZHpvM3M0ZmxoYzJIRWpEdDBDS2dzbndXOUFNc0U0eC1NX0ZqenhfTHZVNEZTV3pVQ2lqYUZkbzZzQlZfODZ5TjBGUnhlaWVBd0VaNzBwY01uNE8yZw?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxNVUx6T3FXRUEwZ09IbGJBMm54Qk5jcDJJS1J2d3ZyMjFEazhIUDNMLXBkQkozTzFieW1pXzUwZ2NwdEd5QmY2S1VQeVRwNHJJNWJDcnpLbV9SNWJSeWRaRVVfQ3B5TmI1SlJBSzJGNUZsV3dDM3JSczEwX3Foc1hweUZzTUduaXRsdTkwUlQ0ZnBtNmdxblc4WVlFZlFjb2s?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxQM3BKWGNiOU5HQXVsMEY4QXFFY1FfYWRmZU5vVE9DX19qWHhVSEtPNmZlX215YmJFM3dpTy1OV3RIVXUwaWI2a0NObDYzNThiZGtpNnVwdV9TRmtKSEhSQTdHV2I4QWUxaDRYMU1nenB2OEtFUkloX2NkZFo3VVBUZUl2eUxYbVd1azRRUTNBQVRmUXBaNGFPaDZkUDlvLTBGYmpvbUR3Sk1raUFxcXVzVmhxZ3lqOFU?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxOS0hEMnF3U29oM05mVE9xLXJsUVBLVHNjcVZFc0ZJWHdSWXlZdTJVSVlVb3Q0enZsazZTeGxSUFNMaTdfSHJjOGxEWDA3Sll0QUp5ZWd4OVdlcnltM1VHQmFUUURaRVpmMktsU1JfLTd5ckN5R3RNNW0xUGFhZm1tUmliYkZIWG14S2xTVlFmaWZzVkRsLU16M1ln?oc=5
- https://news.google.com/rss/articles/CBMirwFBVV95cUxPTFdZUHotUjFWa1VCNldNUmh5djd3TXBGNGx5aW1kQ0FnNE1TVy05V3JBU2VibXVURG95ZVJHV1Z5MkVSdDIwdWRvV2prWGRnOExZRHZhNEY0RG5tVzg5VHVsaDM0VWY3YVh5UmlrZVBlWFJsb3k5WXppbW44eWRwXzZHWU5WZE9UX0h1VlprWU85dGk3V0hXdVpzZDZ4OGYwQ25jZ0NTTHp1NTIzQ1hj?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxPY2ttWTF0eDdlTTV6d0JFMnE5NkE4dk42LVlFU1plUW1oZ0lKUGg0NW5qdW1xSk82QkdwbC1vQVljdEh6SU8zcjFuSTF2ZUZlNHU1aGwtd1FpQ1NqNlgyQkxoSElRLVd4Y1JYcmozQkhfQ2dRbzVfX0JnNTFRa3V3NkJMdjkwMWVQOU5RT3R4VTU2MzYtQnp3bGZ3Vm5wYlpMZ1RaRjA0bGotRVM5ZExPOGk2ZzNWT21kbGVhTU9tdUNZZnlKRWNNREw3VmFOQUpxYlNfSnhB?oc=5
- https://news.google.com/rss/articles/CBMizwFBVV95cUxNY0szdGEtT29jZXJ6LXdMYm1EQ1ZHZ1ZpQU1NYlAwOXBPY2tSOEdCdl85WHg2Z3d2UWd1b01XNGVvazVnYUY5NndtLXZ0TWx2NTJsRmVPVHZkMHRENWFoUHZpR0pQMnpVb2RXdUwwaUItRzRVTXZzOTJUWU43alJ3bmdZZjFzd3duemJTS0lBSmxVOE5mY1AzZHZMNDNpU1A0OVdaOW55ZzNjV0F1M3pjVTZVV0JmVkszTlNNc3BPSGRZUldpczFkWFludGFPNDA?oc=5
- https://news.google.com/rss/articles/CBMiyAFBVV95cUxQandzT2stU29id0NTanZKTnNlRHNzRko3cjBDclVPSW1pbncxTUNvQUpZSE5RT0FjX2hWejQ0Vk1IaDdUakRMcFhobldzYk5wTHlDSDlxaS12eUFHTVRiVlZnZFlLNU5uYUtRXzl5QlBNRU1BaEdueWdJS2tZdnM5X3RIQ2NINGxJcXRDdXVSRF9MTnBnZ0NKME1jSDMtbmNvbFFyZG81ZUtwY2dDbUdYa3ZzX1lBMVBRbHUtMFRCYktEX2ZFekxIUA?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxNNGdpY0ZkVGVjN2FlRXZRZzFUOExtYWZCMnBIaFE2UEtPNFczZEJqaF96TWJNTEF0WWVwSGZoQ005NnAwTmNtbHhMSWFGb1F4YlR2UDBHZ0lBUzkwX0NDRTFacmVJT0hBdlppeWdzeEFtN2RoQjVTLXFxc3dXa1Q4LWZRRUFvdmFORkFERXdpS0V2eGJKdnVoaGFtdG40dUE1U0NKME9JelpsT1A3RHkwbHpfb04wbWlp?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxPZW5GXzBSMXFsY2FDcklHbHVQTVB2V1RXeTVkLTZWT3pIbEczTFZta2FUN0wzaDF6clNETEplNHhFTHJHU0RXd0pVSW5EM3FJLW5sTkcwSTczc3RZNVNsSUFOLWx2ei1kSnpuU0Njb2pZLUI1VEFKaHVVeHJkSmo1SHJXQU9UUmlrWldGNEktRTFkMG1sTlFjMnUwZzIwZw?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
