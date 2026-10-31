# COST Intelligence Report

- ticker: **COST**
- Report as_of: **2026-10-30**
- Market data as_of: **2026-10-30**
- Quant sources: https://finance.yahoo.com/quote/COST/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/COST/key-statistics/
- AI analysis snapshot as_of: **2026-10-30**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-31T02:16:19.223712+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 5, 'ai': 13, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **8** exact headline/source/date matches; prior report **20261030T021807Z-b9de7146/COST** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 9 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 37.5%; oldest publication 2026-10-23

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 1012.2800 |
| Return 1D (%) | 1.7766 |
| Return 1W (%) | 1.0422 |
| Return 1M (%) | 11.3624 |
| Return YTD (%) | 18.0799 |
| Return 1Y (%) | 10.8143 |
| Annualized volatility (%) | 19.8874 |
| Beta vs SPY | -0.1976 |
| Max drawdown (%) | -18.1993 |
| Sharpe (rf=0) | 0.6176 |
| Downside deviation (rf=0, %) | 13.7040 |
| Sortino (rf=0) | 0.8963 |
| Historical VaR 95% (1D, %) | 2.0766 |
| Historical ES 95% (1D, %) | 2.7374 |
| Correlation vs SPY | -0.1271 |
| Tracking error vs SPY (%) | 24.9741 |
| P/E (trailing) | 48.76 |
| P/B | 12.53 |
| EV/EBITDA | 30.84 |
| Revenue growth (%) | 11.10 |
| Forward P/E (estimate) | 40.45 |
| Gross margin (%) | 12.77 |
| Operating margin (%) | 3.79 |
| Return on equity (%) | 28.40 |
| Free cash flow yield (%) | 1.51 |
| MA50 | 941.9411 |
| Close vs MA50 (%) | 7.4674 |
| MA200 | 967.8804 |
| Close vs MA200 (%) | 4.5873 |
| RSI (14, Wilder) | 66.8749 |
| MACD (12,26) | 19.2825 |
| MACD signal (9) | 18.5329 |
| MACD histogram | 0.7496 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'COST': 272, 'SPY': 272}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 1012.2800 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.7766 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 1.0422 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 11.3624 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 18.0799 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 10.8143 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 19.8874 -> Low annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 13.7040 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.8963 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.0766 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.7374 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: -0.1271 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 24.9741 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: -0.1976 -> Inverse market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -18.1993 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.6176 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 40.4486 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 12.7660 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 3.7890 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 28.4020 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.5054 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 48.7611 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 66.8749 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.7496 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 7.4674 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 4.5873 -> Slightly above the moving-average trend level.

## TAILWINDS

### What Did It Take To Hold Costco Stock?
- Summary: Discusses criteria and benefits of holding Costco shares.
- Date: 2026-10-29 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxPalAyLXZfMkVNejRscjhNSnZsWEJrRkMxYmdpNklzeHRJQ3dtOUFneV9QSzRGbGdLM0NhUjRGYVFlZ2pxZG9hMkxSUzB1RndyeXBrU2NsSDdWWUJlaEVrczE4NHY3MXk3emJkVjNJSW9kM0d6ZUxqQkFPR1BpM0lvcVVYc0o3eklreURwbjYtQlJnVlNZOURUbnQ2WFpzblE?oc=5>

### Costco (COST) Stock Price Forecast: June Sales Up 10.6% But Stock Fell After Hours - Short to $899?
- Summary: Forecasts price movement after sales increase and after-hours decline.
- Date: 2026-10-28 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizgFBVV95cUxNRzZhVEh2RktiaUpZMldjMmJiUmx5V3lBdUhhVUdxVHlYYlViT3RCeHF5N0lmVmZ2aEhpdkFCb2pwWmpXZWg4YUZ1ejJHaHRIckVDSWtsQlpLbTBzTk1FVDUwOE85SFZHSVVuS2dvWEVMeVU5TGU0b0lHZHpvM3M0ZmxoYzJIRWpEdDBDS2dzbndXOUFNc0U0eC1NX0ZqenhfTHZVNEZTV3pVQ2lqYUZkbzZzQlZfODZ5TjBGUnhlaWVBd0VaNzBwY01uNE8yZw?oc=5>

### Costco Stock’s Long-Term Upside Could Come From These 3 Competitive Advantages
- Summary: Highlights three competitive advantages that could drive long-term upside for Costco.
- Date: 2026-10-29 | Impact: medium | Horizon: long | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxNTHFpYjU3dTdiUWpzY3F6dkdiQWp1TWtDaXlUeGtGVHVrcm03dmpyV3JGWmJWM1pTSGpKQVBYVkVLRHJsNmNPQ0Z3bU9jTnI5dDhCRk80a3ZaTHhWbFYyNFh1a0NCdDJyZ0VhbXRISmlxdzZETzBTR3c5c3VRNVhYRjZCdnRiYmNCaUNVdXJUNTlpb0pSR3EwNHFqeEZzbU1tQm1yNjByVjZqcnFYRDR4ZS1jMFprX0dDZllVSjZn?oc=5>

### $100 Invested In Costco Wholesale 5 Years Ago Would Be Worth This Much Today
- Summary: Shows historical growth, indicating strong past performance for Costco.
- Date: 2026-10-30 | Impact: high | Horizon: long | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxPSnZtZ01JVzBUMGVqTkVteV9Wcm02aXdRaVZVSXFPYVRrZWE1amFwaVJDSTBMVFZ5M1IzUnFnTUVtRzk0LTJ5LTBqeXhLaEJfY3dIVW02eDhnVHFhWWt5c1NZTlk2Z0pGZ0NoQlctSGdDNFBpUklnSHZlc1Q0SVNDWHJLYnUzQXNfREg3X0VnUzF5RHVtdUM1dTVVa1EtRHdqcWhWMEptdVAyVGZFenBucEhn?oc=5>

### Costco Wholesale (NASDAQ:COST) Stock Jumps 1.6% - Time to Buy?
- Summary: Reports a 1.6% stock jump, suggesting short-term positive momentum.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxOSnZEcUhGbkJ6aTBnZGExenFFT1Bvc2F0TC0yMXdnOTI2YnpvRGlvb1Vfa3BzY0l0MnJmZXVsWWlzWXlkY0o5V1lXa0dzN25YNng3M3RwYnY0S05mdXJFd3g0d0J3aGR4cTNybkYxTHBBOV9yVERpb3JZejF4M2FTR3BWX01ORl9qTWRUa1htbV95SkhvblBXM19ScmVTbVJSaHNCbXZzMF9OZ0FBcTRZSjRkZ2M2Zw?oc=5>

## HEADWINDS

### Costco Wholesale (NASDAQ:COST) Stock Price Down 1.3% - Here's What Happened
- Summary: Costco Wholesale (NASDAQ:COST) Stock Price Down 1.3% - Here's What Happened
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxPdWZyVXhSQTVhT2RKYjREUUliYTJzZFFuVTg2bnlMa091Y08xSW5Xdk5ITS1IWE42a0JIbmk2RkhPNjNoMWVyMXhBYjJZbmY5U0xSZXVzSmc5d2pkQ1B2dDZPMUFlRXVGMFp6RXBsUm1oaG10eEx6UmE3VWhIYnlfR1R1dDIwNmZHdk16X01wN2VtSlZQLVhyYW9ub1VGSHItTjBqYnZmMVRMazFVcUdvNTZyd0ptbDlhcWVqOVVpQ3E3SHVZRnFz?oc=5>

### Costco Stock's Valuation Remains A Head Scratcher (NASDAQ:COST)
- Summary: Valuation concerns for Costco stock.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxNVUx6T3FXRUEwZ09IbGJBMm54Qk5jcDJJS1J2d3ZyMjFEazhIUDNMLXBkQkozTzFieW1pXzUwZ2NwdEd5QmY2S1VQeVRwNHJJNWJDcnpLbV9SNWJSeWRaRVVfQ3B5TmI1SlJBSzJGNUZsV3dDM3JSczEwX3Foc1hweUZzTUduaXRsdTkwUlQ0ZnBtNmdxblc4WVlFZlFjb2s?oc=5>

### Is Now a Good Time to Buy Costco Stock?
- Summary: Questions the timing of buying Costco shares, reflecting uncertainty.
- Date: 2026-10-29 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxNVkJKZEZjSGdScklXYVpwM29ad3VuSzFPTGNZZXdKSzdDbC1wWGhLbldrWng3aGpiUWR3bjlTbzlXaDhjVzRhS1J5VHZCSGljaHNyTE1JZEw2c1hVdzVqdl9zbUlXa0R6ZDJHLU03SldzWVdEYXlUWE9ZZWo4b185M1NDWXJxb1lHMjItQU43bHlhaTg?oc=5>

## CATALYSTS

### Costco Stock (COST) Ticks Up as the FTC Launches Pricing Probe into Rivals Walmart and Target
- Summary: Costco Stock (COST) Ticks Up as the FTC Launches Pricing Probe into Rivals Walmart and Target
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxQM3BKWGNiOU5HQXVsMEY4QXFFY1FfYWRmZU5vVE9DX19qWHhVSEtPNmZlX215YmJFM3dpTy1OV3RIVXUwaWI2a0NObDYzNThiZGtpNnVwdV9TRmtKSEhSQTdHV2I4QWUxaDRYMU1nenB2OEtFUkloX2NkZFo3VVBUZUl2eUxYbVd1azRRUTNBQVRmUXBaNGFPaDZkUDlvLTBGYmpvbUR3Sk1raUFxcXVzVmhxZ3lqOFU?oc=5>

### Costco Wholesale Corporation $COST Stock Sold by Convergence Financial LLC
- Summary: Costco Wholesale Corporation $COST Stock Sold by Convergence Financial LLC
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizwFBVV95cUxNY0szdGEtT29jZXJ6LXdMYm1EQ1ZHZ1ZpQU1NYlAwOXBPY2tSOEdCdl85WHg2Z3d2UWd1b01XNGVvazVnYUY5NndtLXZ0TWx2NTJsRmVPVHZkMHRENWFoUHZpR0pQMnpVb2RXdUwwaUItRzRVTXZzOTJUWU43alJ3bmdZZjFzd3duemJTS0lBSmxVOE5mY1AzZHZMNDNpU1A0OVdaOW55ZzNjV0F1M3pjVTZVV0JmVkszTlNNc3BPSGRZUldpczFkWFludGFPNDA?oc=5>

### Costco Wholesale Corporation $COST Stock Sold by Arrow Financial Corp
- Summary: Costco Wholesale Corporation $COST Stock Sold by Arrow Financial Corp
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiyAFBVV95cUxQandzT2stU29id0NTanZKTnNlRHNzRko3cjBDclVPSW1pbncxTUNvQUpZSE5RT0FjX2hWejQ0Vk1IaDdUakRMcFhobldzYk5wTHlDSDlxaS12eUFHTVRiVlZnZFlLNU5uYUtRXzl5QlBNRU1BaEdueWdJS2tZdnM5X3RIQ2NINGxJcXRDdXVSRF9MTnBnZ0NKME1jSDMtbmNvbFFyZG81ZUtwY2dDbUdYa3ZzX1lBMVBRbHUtMFRCYktEX2ZFekxIUA?oc=5>

### Costco Wholesale Corporation $COST Stock: LaFleur & Godfrey LLC Increases Position
- Summary: Costco Wholesale Corporation $COST Stock: LaFleur & Godfrey LLC Increases Position
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxPY2ttWTF0eDdlTTV6d0JFMnE5NkE4dk42LVlFU1plUW1oZ0lKUGg0NW5qdW1xSk82QkdwbC1vQVljdEh6SU8zcjFuSTF2ZUZlNHU1aGwtd1FpQ1NqNlgyQkxoSElRLVd4Y1JYcmozQkhfQ2dRbzVfX0JnNTFRa3V3NkJMdjkwMWVQOU5RT3R4VTU2MzYtQnp3bGZ3Vm5wYlpMZ1RaRjA0bGotRVM5ZExPOGk2ZzNWT21kbGVhTU9tdUNZZnlKRWNNREw3VmFOQUpxYlNfSnhB?oc=5>

### Costco (COST) Ascends While Market Falls: Some Facts to Note
- Summary: Costco shares rise as broader market declines, indicating relative strength.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxPZW5GXzBSMXFsY2FDcklHbHVQTVB2V1RXeTVkLTZWT3pIbEczTFZta2FUN0wzaDF6clNETEplNHhFTHJHU0RXd0pVSW5EM3FJLW5sTkcwSTczc3RZNVNsSUFOLWx2ei1kSnpuU0Njb2pZLUI1VEFKaHVVeHJkSmo1SHJXQU9UUmlrWldGNEktRTFkMG1sTlFjMnUwZzIwZw?oc=5>

### Costco: Special Dividend Prospects Meet Expensive Valuations And Mixed Macros
- Summary: Costco may issue a special dividend amid high valuations and mixed macro conditions.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxNNGdpY0ZkVGVjN2FlRXZRZzFUOExtYWZCMnBIaFE2UEtPNFczZEJqaF96TWJNTEF0WWVwSGZoQ005NnAwTmNtbHhMSWFGb1F4YlR2UDBHZ0lBUzkwX0NDRTFacmVJT0hBdlppeWdzeEFtN2RoQjVTLXFxc3dXa1Q4LWZRRUFvdmFORkFERXdpS0V2eGJKdnVoaGFtdG40dUE1U0NKME9JelpsT1A3RHkwbHpfb04wbWlp?oc=5>

### Costco Wholesale Corporation $COST Stock: China Universal Asset Management Co. Ltd. Boosts Holdings
- Summary: China Universal Asset Management Co. Ltd. increased its holdings in Costco.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi7AFBVV95cUxQblVPODFTZXRrS1JMYTJjU3F5cGxuQUxqYUl0SHRKSDlaTXFzQWVaVnhNaDdvbFNIeF8wMGhCakVPVTgtVC1maExNZE1adjBPT3hyTklhTHo4XzZ2SFVDZUt0cktTeEgxSUtiR294WjhKNEdRYUdKcEJsd1czMmo4RnVjUXRzRV9OWWt6d1doZHhQRFh1eU9ueWJIR1lOamwtWWJUOGRJTk40dTM0VlB4UkJKWEc2SWJTY1pDU0tLdTFXRjhnRnMybUp1SkM2Ul9FNFdvdTNkbXQxSFlVSlhQV1VQemhRWklQYXh2ag?oc=5>

### 2,595 Costco Wholesale Corporation $COST Shares Sold by Everett Harris & Co. CA
- Summary: Everett Harris & Co. CA sold 2,595 Costco shares.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi0AFBVV95cUxQU2xfQ1NtcnhpYldyN1NFOXlPUmRHSFpRQ1pMMGpMcWRpVnlSdzJUdHZoNGVteHZvQ214WVhNaUMtVGo4Q2Z5RlNObXRHbFphcm9SWXZhRUVYQUFUU3BRenRPZ3ExYjk0cUlielRYc2dwQjlENHVET2JnSndaOGxfdXJlMUdMNmZsUVo2akZremNCTGlIbmdfR1VvUW5wMXg2cThzWXZRX0UwTHY4Skpka0o0dzM2Um9yMTlEbEVIMGd4N3pzOGVIeDd5Zk5QNnJL?oc=5>

### Costco Wholesale (NASDAQ:COST) Stock Sale Reported by Rep. Pete Sessions
- Summary: Rep. Pete Sessions reported a sale of Costco stock.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMizAFBVV95cUxQNzZ2WmZpSHY2bXc5S05GWnBaVlItSzNhT1Bjb1IwUHNvVHFacERWQTQwbF93MFpSSUZ1N3FLdHZSaXZ5X0xIOENKVWFKZzdCdHVBQVU3NVRiQ2N4YXp2S0NZRkoxeDBoY1drbVRpakFkdVQzWEpQbXlBLWtWWWp2WUN6bUxlUjNkaVcxbHIyaUl5ZG96SXdZOGdGeUtaTDRSeHhUVmNVazFvZkZkb1R1czV2c05mSnZaRzMycFZFYUI3WkIxTU9QNTlTRkI?oc=5>

## RISKS

### Should Medicare Push Require Action From Costco (COST) Investors?
- Summary: Raises potential regulatory pressure from Medicare, posing a risk to investors.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxObWVYZjVuTC1CRk81TnpXTkxvcWtYb1M2ZlZIYlJINm93M1hJakVHOVNQVDhHcXZudWZMak04MV9CZVQ2SEo2YW9KbURPeVpPa3hEaVIxTkU4X0V6MGdaQ0Zpc3JLMnptQ0dLM083OGZ0VlJfNlhYdzkwQkllT1dlMEUtLXoxZmFDSlA3NnVKM0VEZkZwSDFKOEdxZzg?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **COST** | **48.76** | **12.53** | **30.84** | **11.10** | **448,570,982,400.00 USD** | **10.81** |
| WMT | 44.75 | 9.99 | 23.82 | 5.90 | 982,902,374,400.00 USD | 21.83 |
| TGT | 16.03 | 3.93 | 9.77 | 5.30 | 70,134,333,440.00 USD | 72.87 |
| BJ | 23.48 | 6.18 | 14.04 | 15.70 | 13,556,091,904.00 USD | 19.86 |

Peers fetched as_of: 2026-10-30; COST reuses existing data (market data as_of: 2026-10-30); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-09-24
- Next expected earnings: 2026-12-10 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-30

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

- https://news.google.com/rss/articles/CBMinwFBVV95cUxPalAyLXZfMkVNejRscjhNSnZsWEJrRkMxYmdpNklzeHRJQ3dtOUFneV9QSzRGbGdLM0NhUjRGYVFlZ2pxZG9hMkxSUzB1RndyeXBrU2NsSDdWWUJlaEVrczE4NHY3MXk3emJkVjNJSW9kM0d6ZUxqQkFPR1BpM0lvcVVYc0o3eklreURwbjYtQlJnVlNZOURUbnQ2WFpzblE?oc=5
- https://news.google.com/rss/articles/CBMizgFBVV95cUxNRzZhVEh2RktiaUpZMldjMmJiUmx5V3lBdUhhVUdxVHlYYlViT3RCeHF5N0lmVmZ2aEhpdkFCb2pwWmpXZWg4YUZ1ejJHaHRIckVDSWtsQlpLbTBzTk1FVDUwOE85SFZHSVVuS2dvWEVMeVU5TGU0b0lHZHpvM3M0ZmxoYzJIRWpEdDBDS2dzbndXOUFNc0U0eC1NX0ZqenhfTHZVNEZTV3pVQ2lqYUZkbzZzQlZfODZ5TjBGUnhlaWVBd0VaNzBwY01uNE8yZw?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxNTHFpYjU3dTdiUWpzY3F6dkdiQWp1TWtDaXlUeGtGVHVrcm03dmpyV3JGWmJWM1pTSGpKQVBYVkVLRHJsNmNPQ0Z3bU9jTnI5dDhCRk80a3ZaTHhWbFYyNFh1a0NCdDJyZ0VhbXRISmlxdzZETzBTR3c5c3VRNVhYRjZCdnRiYmNCaUNVdXJUNTlpb0pSR3EwNHFqeEZzbU1tQm1yNjByVjZqcnFYRDR4ZS1jMFprX0dDZllVSjZn?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxPSnZtZ01JVzBUMGVqTkVteV9Wcm02aXdRaVZVSXFPYVRrZWE1amFwaVJDSTBMVFZ5M1IzUnFnTUVtRzk0LTJ5LTBqeXhLaEJfY3dIVW02eDhnVHFhWWt5c1NZTlk2Z0pGZ0NoQlctSGdDNFBpUklnSHZlc1Q0SVNDWHJLYnUzQXNfREg3X0VnUzF5RHVtdUM1dTVVa1EtRHdqcWhWMEptdVAyVGZFenBucEhn?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxOSnZEcUhGbkJ6aTBnZGExenFFT1Bvc2F0TC0yMXdnOTI2YnpvRGlvb1Vfa3BzY0l0MnJmZXVsWWlzWXlkY0o5V1lXa0dzN25YNng3M3RwYnY0S05mdXJFd3g0d0J3aGR4cTNybkYxTHBBOV9yVERpb3JZejF4M2FTR3BWX01ORl9qTWRUa1htbV95SkhvblBXM19ScmVTbVJSaHNCbXZzMF9OZ0FBcTRZSjRkZ2M2Zw?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxPdWZyVXhSQTVhT2RKYjREUUliYTJzZFFuVTg2bnlMa091Y08xSW5Xdk5ITS1IWE42a0JIbmk2RkhPNjNoMWVyMXhBYjJZbmY5U0xSZXVzSmc5d2pkQ1B2dDZPMUFlRXVGMFp6RXBsUm1oaG10eEx6UmE3VWhIYnlfR1R1dDIwNmZHdk16X01wN2VtSlZQLVhyYW9ub1VGSHItTjBqYnZmMVRMazFVcUdvNTZyd0ptbDlhcWVqOVVpQ3E3SHVZRnFz?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxNVUx6T3FXRUEwZ09IbGJBMm54Qk5jcDJJS1J2d3ZyMjFEazhIUDNMLXBkQkozTzFieW1pXzUwZ2NwdEd5QmY2S1VQeVRwNHJJNWJDcnpLbV9SNWJSeWRaRVVfQ3B5TmI1SlJBSzJGNUZsV3dDM3JSczEwX3Foc1hweUZzTUduaXRsdTkwUlQ0ZnBtNmdxblc4WVlFZlFjb2s?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxNVkJKZEZjSGdScklXYVpwM29ad3VuSzFPTGNZZXdKSzdDbC1wWGhLbldrWng3aGpiUWR3bjlTbzlXaDhjVzRhS1J5VHZCSGljaHNyTE1JZEw2c1hVdzVqdl9zbUlXa0R6ZDJHLU03SldzWVdEYXlUWE9ZZWo4b185M1NDWXJxb1lHMjItQU43bHlhaTg?oc=5
- https://news.google.com/rss/articles/CBMiiAFBVV95cUxOVW0zdGcxM1BXSWJOTlB1UlJkRTY4eXRqZFNyUW5tUDdUN04tWHpwZXdZQi10MjhqZFFEeXBXZmd2VGYtaFBDMU82Z0M5Qlk2TFB1bktVUGlsenJoVWRKeWZfaU5hbTRuVnBCUHluc1BZcFFaMFNwVVNjZUhPbF9zblo2TTAxdjZL?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxQM3BKWGNiOU5HQXVsMEY4QXFFY1FfYWRmZU5vVE9DX19qWHhVSEtPNmZlX215YmJFM3dpTy1OV3RIVXUwaWI2a0NObDYzNThiZGtpNnVwdV9TRmtKSEhSQTdHV2I4QWUxaDRYMU1nenB2OEtFUkloX2NkZFo3VVBUZUl2eUxYbVd1azRRUTNBQVRmUXBaNGFPaDZkUDlvLTBGYmpvbUR3Sk1raUFxcXVzVmhxZ3lqOFU?oc=5
- https://news.google.com/rss/articles/CBMizwFBVV95cUxNY0szdGEtT29jZXJ6LXdMYm1EQ1ZHZ1ZpQU1NYlAwOXBPY2tSOEdCdl85WHg2Z3d2UWd1b01XNGVvazVnYUY5NndtLXZ0TWx2NTJsRmVPVHZkMHRENWFoUHZpR0pQMnpVb2RXdUwwaUItRzRVTXZzOTJUWU43alJ3bmdZZjFzd3duemJTS0lBSmxVOE5mY1AzZHZMNDNpU1A0OVdaOW55ZzNjV0F1M3pjVTZVV0JmVkszTlNNc3BPSGRZUldpczFkWFludGFPNDA?oc=5
- https://news.google.com/rss/articles/CBMiyAFBVV95cUxQandzT2stU29id0NTanZKTnNlRHNzRko3cjBDclVPSW1pbncxTUNvQUpZSE5RT0FjX2hWejQ0Vk1IaDdUakRMcFhobldzYk5wTHlDSDlxaS12eUFHTVRiVlZnZFlLNU5uYUtRXzl5QlBNRU1BaEdueWdJS2tZdnM5X3RIQ2NINGxJcXRDdXVSRF9MTnBnZ0NKME1jSDMtbmNvbFFyZG81ZUtwY2dDbUdYa3ZzX1lBMVBRbHUtMFRCYktEX2ZFekxIUA?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxPY2ttWTF0eDdlTTV6d0JFMnE5NkE4dk42LVlFU1plUW1oZ0lKUGg0NW5qdW1xSk82QkdwbC1vQVljdEh6SU8zcjFuSTF2ZUZlNHU1aGwtd1FpQ1NqNlgyQkxoSElRLVd4Y1JYcmozQkhfQ2dRbzVfX0JnNTFRa3V3NkJMdjkwMWVQOU5RT3R4VTU2MzYtQnp3bGZ3Vm5wYlpMZ1RaRjA0bGotRVM5ZExPOGk2ZzNWT21kbGVhTU9tdUNZZnlKRWNNREw3VmFOQUpxYlNfSnhB?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxPZW5GXzBSMXFsY2FDcklHbHVQTVB2V1RXeTVkLTZWT3pIbEczTFZta2FUN0wzaDF6clNETEplNHhFTHJHU0RXd0pVSW5EM3FJLW5sTkcwSTczc3RZNVNsSUFOLWx2ei1kSnpuU0Njb2pZLUI1VEFKaHVVeHJkSmo1SHJXQU9UUmlrWldGNEktRTFkMG1sTlFjMnUwZzIwZw?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxNNGdpY0ZkVGVjN2FlRXZRZzFUOExtYWZCMnBIaFE2UEtPNFczZEJqaF96TWJNTEF0WWVwSGZoQ005NnAwTmNtbHhMSWFGb1F4YlR2UDBHZ0lBUzkwX0NDRTFacmVJT0hBdlppeWdzeEFtN2RoQjVTLXFxc3dXa1Q4LWZRRUFvdmFORkFERXdpS0V2eGJKdnVoaGFtdG40dUE1U0NKME9JelpsT1A3RHkwbHpfb04wbWlp?oc=5
- https://news.google.com/rss/articles/CBMi7AFBVV95cUxQblVPODFTZXRrS1JMYTJjU3F5cGxuQUxqYUl0SHRKSDlaTXFzQWVaVnhNaDdvbFNIeF8wMGhCakVPVTgtVC1maExNZE1adjBPT3hyTklhTHo4XzZ2SFVDZUt0cktTeEgxSUtiR294WjhKNEdRYUdKcEJsd1czMmo4RnVjUXRzRV9OWWt6d1doZHhQRFh1eU9ueWJIR1lOamwtWWJUOGRJTk40dTM0VlB4UkJKWEc2SWJTY1pDU0tLdTFXRjhnRnMybUp1SkM2Ul9FNFdvdTNkbXQxSFlVSlhQV1VQemhRWklQYXh2ag?oc=5
- https://news.google.com/rss/articles/CBMi0AFBVV95cUxQU2xfQ1NtcnhpYldyN1NFOXlPUmRHSFpRQ1pMMGpMcWRpVnlSdzJUdHZoNGVteHZvQ214WVhNaUMtVGo4Q2Z5RlNObXRHbFphcm9SWXZhRUVYQUFUU3BRenRPZ3ExYjk0cUlielRYc2dwQjlENHVET2JnSndaOGxfdXJlMUdMNmZsUVo2akZremNCTGlIbmdfR1VvUW5wMXg2cThzWXZRX0UwTHY4Skpka0o0dzM2Um9yMTlEbEVIMGd4N3pzOGVIeDd5Zk5QNnJL?oc=5
- https://news.google.com/rss/articles/CBMizAFBVV95cUxQNzZ2WmZpSHY2bXc5S05GWnBaVlItSzNhT1Bjb1IwUHNvVHFacERWQTQwbF93MFpSSUZ1N3FLdHZSaXZ5X0xIOENKVWFKZzdCdHVBQVU3NVRiQ2N4YXp2S0NZRkoxeDBoY1drbVRpakFkdVQzWEpQbXlBLWtWWWp2WUN6bUxlUjNkaVcxbHIyaUl5ZG96SXdZOGdGeUtaTDRSeHhUVmNVazFvZkZkb1R1czV2c05mSnZaRzMycFZFYUI3WkIxTU9QNTlTRkI?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxObWVYZjVuTC1CRk81TnpXTkxvcWtYb1M2ZlZIYlJINm93M1hJakVHOVNQVDhHcXZudWZMak04MV9CZVQ2SEo2YW9KbURPeVpPa3hEaVIxTkU4X0V6MGdaQ0Zpc3JLMnptQ0dLM083OGZ0VlJfNlhYdzkwQkllT1dlMEUtLXoxZmFDSlA3NnVKM0VEZkZwSDFKOEdxZzg?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
