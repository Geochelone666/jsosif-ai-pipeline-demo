# VRTX Intelligence Report

- ticker: **VRTX**
- Report as_of: **2026-11-26**
- Market data as_of: **2026-11-25**
- Quant sources: https://finance.yahoo.com/quote/VRTX/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/VRTX/key-statistics/
- AI analysis snapshot as_of: **2026-11-26**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-27T06:41:32.929268+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 2, 'ai': 13, 'unknown': 0, 'irrelevant': 10})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **15** exact headline/source/date matches; prior report **20261126T064454Z-dbdd6f45/VRTX** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 12 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 24.0%; oldest publication 2026-11-19

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 564.1200 |
| Return 1D (%) | 0.0355 |
| Return 1W (%) | 5.1580 |
| Return 1M (%) | 7.6709 |
| Return YTD (%) | 24.4309 |
| Return 1Y (%) | 31.2456 |
| Annualized volatility (%) | 30.2462 |
| Beta vs SPY | 0.4971 |
| Max drawdown (%) | -15.2113 |
| Sharpe (rf=0) | 1.0521 |
| Downside deviation (rf=0, %) | 18.2260 |
| Sortino (rf=0) | 1.7460 |
| Historical VaR 95% (1D, %) | 2.8866 |
| Historical ES 95% (1D, %) | 3.4662 |
| Correlation vs SPY | 0.2454 |
| Tracking error vs SPY (%) | 30.2679 |
| P/E (trailing) | 36.30 |
| P/B | 6.84 |
| EV/EBITDA | 28.07 |
| Revenue growth (%) | 11.80 |
| Forward P/E (estimate) | 28.32 |
| Gross margin (%) | 54.81 |
| Operating margin (%) | 37.79 |
| Return on equity (%) | 20.80 |
| Free cash flow yield (%) | 1.63 |
| MA50 | 525.1106 |
| Close vs MA50 (%) | 7.4288 |
| MA200 | 486.1503 |
| Close vs MA200 (%) | 16.0382 |
| RSI (14, Wilder) | 62.2263 |
| MACD (12,26) | 5.6669 |
| MACD signal (9) | 4.5964 |
| MACD histogram | 1.0705 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'VRTX': 290, 'SPY': 290}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 564.1200 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.0355 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 5.1580 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 7.6709 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 24.4309 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 31.2456 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 30.2462 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 18.2260 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.7460 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.8866 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.4662 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2454 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 30.2679 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.4971 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -15.2113 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.0521 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 28.3233 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 54.8090 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 37.7920 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 20.8020 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.6345 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 36.3012 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 62.2263 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 1.0705 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 7.4288 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 16.0382 -> Clearly above the moving-average trend level.

## TAILWINDS

### Vertex Pharmaceuticals Inc Stock (VRTX) Moved Up by 4.43% on Nov 24: Facts Behind the Movement
- Summary: Vertex Pharmaceuticals Inc Stock (VRTX) Moved Up by 4.43% on Nov 24: Facts Behind the Movement
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxPMjdZYjNsbWhQU2JCdlBFdG9Mb3VmcFplcDUyUTIxNUN6UVV0YnN5VTd5M3RsZGYyWERRMl9iY3N2T3RQZkFXNHhCbE1kTHE1cUZ0S0h6d0N3S1NUdUFFOHZ4QjBPb3g3VXFXUzVOUTBLa0JVZ2VfWkJuX2VGVndHUWZPMjh3OXAzTmUw?oc=5>

### Vertex Pharmaceuticals (VRTX) Extends Drug Discovery Collaboration For Four Years
- Summary: Vertex renews drug discovery partnership for four years.
- Date: 2026-11-25 | Impact: high | Horizon: medium | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxNSTVKNF96UXZGaHNTMDBlNzBfcEMtQnVvVXE5R1JHU09qQ245SXB1SmJVbEVkWXh6LVNoQVJZSElWTVdyNzRoRjBMUjlOczY4c3N0LUV4RU1VR29lU2hzN1EyNkkweGRuV3FZalN2ZjZJSmljR2NKWDJGb25mcGM1ajFWa1lYMXA1QWdha2F5T0kyX1J5dlNsZktpNU1vRHpad1dz?oc=5>

### Vertex Pharmaceuticals (VRTX) Climbed, What Is Behind The Latest Attention?
- Summary: Vertex shares rise, attracting investor interest. Analysts highlight strong pipeline and recent earnings beat.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi8gFBVV95cUxNb2pBMVVaSFViWFYxYUViYTBva2RhblpWeTFkVGFlOXhaTDdQWlJCS2N6TFJpUFNsbE8xNGYtaFJGdm9zNVlZbWQ5anRtR0VzQXpRY3I3Z2dndDNMSUQxT19RQkkybTVkYm9pTHRKeW1uTTBlLXZGaDd0bWctZGRNcDQ0MW1peDVlZXNjV0VOMTdSUEVRU2Zaazg3cmlvV3dSeEVKNEVrbGNsVko2dC1rb2RLNHh5eTYtWHNoS1FCVlllN0ZvQ0IwOWlHR0lUQWxWRWVaWnd6cVlnUlduUGtfYnhORE5pTEozXzAtMlNWYkdDZ9IB8gFBVV95cUxNb2pBMVVaSFViWFYxYUViYTBva2RhblpWeTFkVGFlOXhaTDdQWlJCS2N6TFJpUFNsbE8xNGYtaFJGdm9zNVlZbWQ5anRtR0VzQXpRY3I3Z2dndDNMSUQxT19RQkkybTVkYm9pTHRKeW1uTTBlLXZGaDd0bWctZGRNcDQ0MW1peDVlZXNjV0VOMTdSUEVRU2Zaazg3cmlvV3dSeEVKNEVrbGNsVko2dC1rb2RLNHh5eTYtWHNoS1FCVlllN0ZvQ0IwOWlHR0lUQWxWRWVaWnd6cVlnUlduUGtfYnhORE5pTEozXzAtMlNWYkdDZw?oc=5>

## HEADWINDS

### Vertex Pharmaceuticals Inc Stock (VRTX) Moved Down by 3.17% on Nov 19: Facts Behind the Movement
- Summary: Vertex Pharmaceuticals Inc Stock (VRTX) Moved Down by 3.17% on Nov 19: Facts Behind the Movement
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxPXzRaYklKVEs1eVpxTGJpcW85U1hXczc1MlNLblFqWDY5cXNJQXB2MEo3S1RRakxNTjJtRk1mSklyN3NxN2dtQjJwQVRhZ3ZBSmczR05pVUw5ZUt4NF9yU2RoVEhPd241VUlSMWcxMU1sQWFBbzZwYkEzTjJ0WTdnRkVfdkZvcEdvSVFN?oc=5>

### Vertex Announces Extension of PDUFA Target Action Date by up to...
- Summary: Vertex extends PDUFA target action date, delaying approval.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxNYzVITm1kd3RhNDc3TmtpMFhUWkdfOTVndkdhRS1Mb041NDlRR280dUp0a2s0Q3o4cGN5dWp1ZnFpQWJCbm5GMGdOejNhRWdMa2RsLTd5YWRLWG83VE9xYzBvaDFhN1FMbk5ibVdaQndVa1hiZWFsR3NWZ3VNSjY0LURZQ2JVNzVLWDFQYUtyeWpBdDZ0ZFNQVy1SZEZ4bldWYkp5bFpR?oc=5>

### Vertex Stock Drops After Hours on FDA PDUFA Delay - Vertex Pharmaceuticals (NASDAQ:VRTX)
- Summary: FDA PDUFA delay causes after-hours stock drop.
- Date: 2026-11-25 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxQd19CWE90RHNQVkxkNUdRZFpaZlg5NWpucHhfS0hlSmxkY1RvYVZ0TVd0MGNXWmw2X0tZVWczdjd4Q3BJcTdaZ1FJc0FMT0k3WnRhUjBBV01PbmliQ3hTM3pvek9KSThOczY3TFpwQ1FSVGRKTFRrZHFIeWRjSERFX0dGMXRxbWxfOHN6U2xSbVk5OXVkM0xxZ3o0Nm5rY2lUUEk0bExsMnhwSXFPQ3NWSEpDYUxCVVdhVXc?oc=5>

### VRTX Tumbles After-Hours As FDA Delays Kidney Drug Decision; Rival VERA Surges
- Summary: FDA delay on kidney drug causes VRTX after-hours tumble.
- Date: 2026-11-25 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi7gFBVV95cUxPYkdUakREcnpSY0pFX09pZkRjZUJmdjE5VXRLel9uRDlZQUt1OVgyUlJUcnBqRVdudzUtT05lcFZhb0tfZGlUNEtMcUpiY3NVQ0VudHVOM1Z2Z0dJSTRlU05EX2dtUTdjLVBxbzN0VG1xaUNXR0RMblRkalNJcHJpZzJHTVZvaXVya19DWDJ4VlRJV0hDZGJaVVhVSWpacmhsd1RVZ24tMGd5V245b2Q1VHpBeWZ1cUc4WUJ2TkkyempXQk4yVFFzdDBqaGxMYnEtME1GRHBCLTRvT2JjeDRmdzhkZVd0aV8tcl9tdXdn?oc=5>

### Vertex (VERX) Stock Looks Reasonable On A 34% Three Year Slide
- Summary: Vertex stock has declined 34% over three years, raising concerns about valuation and growth prospects.
- Date: 2026-11-26 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxOdktVOUE5NGpyQW1nV0xLUjkyZUZYQnpxZU5ubmZpUEJHLTk1YVJ1aUwwUXExNkhEaDZQWXV5MUl4bVczbmM2Q2V5MmRCLXpvbk9nXzEwMzhDYm95TkQ2Z3NUcndzbGZLVmtkeEpSV0N1dzJkRGFqWmlGRGZzQVJYcWdlbkFHNTNiRHh4Zk5PRXdQWExUX05mY0dPZzJKazdy?oc=5>

## CATALYSTS

### Vertex Shares Have The Bull Case Changed After Drug Discovery Deal Renewal
- Summary: Shares react positively to renewed partnership.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxOOFJUdVRmNzJpV09mNTg2cW9BSHZrajA4c3BNR2RIODNqMGVORDBIRjFkVlFoZVFyWlpsOE10U1ZqOE5FXzgyWDBpVl9iemRfUVlCNzItZEhySkRiWW1rRk4yRmFTdDB4SWxYU2huTEFraTVXVEtJUWdYeWFqZDY0NmNYekp3V3hsTGZkY0VoWVhmbko3XzZF?oc=5>

### Vertex Pharmaceuticals Rises as Investors Position for Key FDA Decision
- Summary: Investors anticipate FDA decision, driving stock up.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxPNTV3RlVEOEpYSUVEcUFXZE9NZXVTRjVmZFBGTjVRajdrLUZvVndpcUxldHVHM2hiaF9EZ1VDdURyVTdsa0wwS3hQUjFJd3FaeHJCTWttMFJJZ1J6UmV6cFFUM1FWVEJYb2Y3M2tEaE9aZDJiN1h0NTZ4Q21WT3pTa3JmRUlLQmVUSFRTSjVMZ0stOXAySHdFVWhWbFAxYzNrMmhhQVo4SQ?oc=5>

### Vertex Pharmaceuticals: Look For Povetacicept Approval In 2 Weeks As Next Catalyst
- Summary: Povetacicept expected FDA approval within two weeks, potentially boosting Vertex’s pipeline momentum.
- Date: 2026-11-20 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxNd3g5ZUlkYjdveC1zQUZ0cW5Bb3dUUXBfdlNxTFEzd2hKYm9HRWpBNGZlYXpoaFUwWFVha0VSdFdqQm1uMUp5WGw0OVg0LTBYYmtOUDg5RVpTMHkzbndsc0FCd1BzWFdIdUcweEszLXVwUGtpVTc0Y0E2RER5OWhHcWpZT29lWGZnSEJnNl9tOTlEd3M5OFR3UnNWRzZZN1ViWTBhcW1tWEwwYWNUc1EzS01TaVBqYXUxd1NPM0NDQQ?oc=5>

### Will Genomics Deal Extension Change Vertex Pharmaceuticals (VRTX) Narrative
- Summary: Potential deal extension could alter company outlook.
- Date: 2026-11-24 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi7AFBVV95cUxPaHB6WEIzekctQmp6Qmk0WFlCQUNoNFRtYUticEIzSWJDYVlVTDNwb3RRSTZhNUZ2X0gtRE9tR29jNGsxeFpSaV9YczBKQ3o0ME1LSmNSWFRlUzUtS0djLVVodUVWaWt0bnU5SnR1NUVUZkU0cDNKUjJNLTlIRElibXc3TTAyeXNzWF9KRTRFMmtXdGRnSC1fOGRtNG1PZ3I4WEVGQTdOUzhxMXBJYnRRc1ROcUdVOXU2cXEzaWl5V1FneFpJUWY4dTNuTFF4Z3F6Wjd0dVlxTUNSU0x2V3dlbGJIUmtHMlROaFZTONIB8gFBVV95cUxOamxzYXdDZ2dsVkdmMERUSjdwZUNZcVo1VV9YMnlWT1lvZ2dOc3Z2U2NUb1poVS1WcWF6RnJYaGRlZDBLTDFzZEtrSXliUHZNQU80cWdNNW0zTldLdzZtLW1OTEFPaDlLLWZuMVpHaTcxdEJ1cUNaQ2hDZnBFN3JDZlRMYVZlNVo0R1cwRFQ4WXZITVBaU1lzVFZDYnhlQjItX0tELTJSNE5mdjBxUFNEajJ4ZFp2azRXbWdxZk1ZQ1E0N1MxekZvRkZjNVhzV2xXWmZtSFh3X2lKdE5IWnc2U1VuRUcwSEw2d0hlRVpnLTBBQQ?oc=5>

### A stock option exercise supplied the shares a Vertex Pharmaceuticals (VRTX) officer proposes to sell.
- Summary: Officer plans to sell shares after option exercise.
- Date: 2026-11-25 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxQeUFjTDdEbDFjNHRuQkJrQ01tbmtDY2x0SElRRldweTNyeENXYy1uWjJXTU9PYm05V2N5Zm54dUY1UXRBUHlRMUFuQXZIQ0lKRDBFME84TmVHYWxnOXh2RkJQN0xjTmJOR1Q1OHUzdlZweUVWdHBpbU1DSWxIMUM1VVdidUM5eFZZcHUwZmV4Q1NCUmloOW9xSFU0ZFJpTjJBN3lQOEtyUTU4dw?oc=5>

### Vertex Pharmaceuticals Incorporated (VRTX) CF Dominance and Pipeline Strengthen Investment Outlook
- Summary: Positive outlook on CF pipeline strengthens investment view.
- Date: 2026-11-26 | Impact: medium | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxQZGFMeFZzY0t2YUVwN3FIdTMwQ1NEbGFzLVR3aDJqX0h0ZUYxUVFTQUZ4R1pIdEZwTlhXTHlmdnQwNzFGSWFvNVJrQlpHWE43VUFhMGRmQndDT1U0QUhOWXpJVThNOS1zbTZ1cDlmOWp6VDRUQklxcm12QXduel9mX3JBVndMOS01dnBhN2Y0aTRieVQ2empaSUZLcUJoSWdlWUFSMUY3bw?oc=5>

## RISKS

### VRTX Down as FDA Extends Review Timeline for Povetacicept BLA
- Summary: FDA review extension delays product launch, increasing risk.
- Date: 2026-11-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxNOUNqVFZuZ1ptX3NGT1NHNXctTHlaUHdVUDkzUTJqZ2VadnlLTm5ocGNrTnJ3TXJfS3Y5RTRRSXpleHI2Tlg4dUJhVi04MWZZZXhEd1ZMSXotNnRhSG5HX0l5Y3J0NmhOV3FDamw5eDNSZDEwcFBLM3hzTG1qU0JkU1UzRkdKVWl3ZWtlNEtqdFdhVXRTbk9ZMHRRZ2xjZGhNcVpMcmdRb3VJcU9kYXVpQ2JrdUdOUEEx?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **VRTX** | **36.30** | **6.84** | **28.07** | **11.80** | **143,025,668,096.00 USD** | **31.25** |
| REGN | 21.70 | 2.94 | 16.28 | 36.30 | 101,572,345,856.00 USD | 25.32 |
| BIIB | 113.18 | 2.04 | 13.67 | 10.60 | 38,646,120,448.00 USD | 43.68 |
| AMGN | 27.20 | 17.68 | 16.71 | 8.50 | 253,817,307,136.00 USD | 41.19 |

Peers fetched as_of: 2026-11-26; VRTX reuses existing data (market data as_of: 2026-11-25); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-02
- Next expected earnings: 2027-02-11 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-26

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-03
- Revenue (latest available single quarter): 640,799,000.00 USD; period 2018-01-01/2018-03-31; fiscal year/reporting period 2018/Q1
- Net income (latest available single quarter): 653,600,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/875320/000087532026000291/vrtx-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiiwFBVV95cUxPMjdZYjNsbWhQU2JCdlBFdG9Mb3VmcFplcDUyUTIxNUN6UVV0YnN5VTd5M3RsZGYyWERRMl9iY3N2T3RQZkFXNHhCbE1kTHE1cUZ0S0h6d0N3S1NUdUFFOHZ4QjBPb3g3VXFXUzVOUTBLa0JVZ2VfWkJuX2VGVndHUWZPMjh3OXAzTmUw?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxNSTVKNF96UXZGaHNTMDBlNzBfcEMtQnVvVXE5R1JHU09qQ245SXB1SmJVbEVkWXh6LVNoQVJZSElWTVdyNzRoRjBMUjlOczY4c3N0LUV4RU1VR29lU2hzN1EyNkkweGRuV3FZalN2ZjZJSmljR2NKWDJGb25mcGM1ajFWa1lYMXA1QWdha2F5T0kyX1J5dlNsZktpNU1vRHpad1dz?oc=5
- https://news.google.com/rss/articles/CBMi8gFBVV95cUxNb2pBMVVaSFViWFYxYUViYTBva2RhblpWeTFkVGFlOXhaTDdQWlJCS2N6TFJpUFNsbE8xNGYtaFJGdm9zNVlZbWQ5anRtR0VzQXpRY3I3Z2dndDNMSUQxT19RQkkybTVkYm9pTHRKeW1uTTBlLXZGaDd0bWctZGRNcDQ0MW1peDVlZXNjV0VOMTdSUEVRU2Zaazg3cmlvV3dSeEVKNEVrbGNsVko2dC1rb2RLNHh5eTYtWHNoS1FCVlllN0ZvQ0IwOWlHR0lUQWxWRWVaWnd6cVlnUlduUGtfYnhORE5pTEozXzAtMlNWYkdDZ9IB8gFBVV95cUxNb2pBMVVaSFViWFYxYUViYTBva2RhblpWeTFkVGFlOXhaTDdQWlJCS2N6TFJpUFNsbE8xNGYtaFJGdm9zNVlZbWQ5anRtR0VzQXpRY3I3Z2dndDNMSUQxT19RQkkybTVkYm9pTHRKeW1uTTBlLXZGaDd0bWctZGRNcDQ0MW1peDVlZXNjV0VOMTdSUEVRU2Zaazg3cmlvV3dSeEVKNEVrbGNsVko2dC1rb2RLNHh5eTYtWHNoS1FCVlllN0ZvQ0IwOWlHR0lUQWxWRWVaWnd6cVlnUlduUGtfYnhORE5pTEozXzAtMlNWYkdDZw?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxPXzRaYklKVEs1eVpxTGJpcW85U1hXczc1MlNLblFqWDY5cXNJQXB2MEo3S1RRakxNTjJtRk1mSklyN3NxN2dtQjJwQVRhZ3ZBSmczR05pVUw5ZUt4NF9yU2RoVEhPd241VUlSMWcxMU1sQWFBbzZwYkEzTjJ0WTdnRkVfdkZvcEdvSVFN?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxNYzVITm1kd3RhNDc3TmtpMFhUWkdfOTVndkdhRS1Mb041NDlRR280dUp0a2s0Q3o4cGN5dWp1ZnFpQWJCbm5GMGdOejNhRWdMa2RsLTd5YWRLWG83VE9xYzBvaDFhN1FMbk5ibVdaQndVa1hiZWFsR3NWZ3VNSjY0LURZQ2JVNzVLWDFQYUtyeWpBdDZ0ZFNQVy1SZEZ4bldWYkp5bFpR?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxQd19CWE90RHNQVkxkNUdRZFpaZlg5NWpucHhfS0hlSmxkY1RvYVZ0TVd0MGNXWmw2X0tZVWczdjd4Q3BJcTdaZ1FJc0FMT0k3WnRhUjBBV01PbmliQ3hTM3pvek9KSThOczY3TFpwQ1FSVGRKTFRrZHFIeWRjSERFX0dGMXRxbWxfOHN6U2xSbVk5OXVkM0xxZ3o0Nm5rY2lUUEk0bExsMnhwSXFPQ3NWSEpDYUxCVVdhVXc?oc=5
- https://news.google.com/rss/articles/CBMi7gFBVV95cUxPYkdUakREcnpSY0pFX09pZkRjZUJmdjE5VXRLel9uRDlZQUt1OVgyUlJUcnBqRVdudzUtT05lcFZhb0tfZGlUNEtMcUpiY3NVQ0VudHVOM1Z2Z0dJSTRlU05EX2dtUTdjLVBxbzN0VG1xaUNXR0RMblRkalNJcHJpZzJHTVZvaXVya19DWDJ4VlRJV0hDZGJaVVhVSWpacmhsd1RVZ24tMGd5V245b2Q1VHpBeWZ1cUc4WUJ2TkkyempXQk4yVFFzdDBqaGxMYnEtME1GRHBCLTRvT2JjeDRmdzhkZVd0aV8tcl9tdXdn?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxOdktVOUE5NGpyQW1nV0xLUjkyZUZYQnpxZU5ubmZpUEJHLTk1YVJ1aUwwUXExNkhEaDZQWXV5MUl4bVczbmM2Q2V5MmRCLXpvbk9nXzEwMzhDYm95TkQ2Z3NUcndzbGZLVmtkeEpSV0N1dzJkRGFqWmlGRGZzQVJYcWdlbkFHNTNiRHh4Zk5PRXdQWExUX05mY0dPZzJKazdy?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxOOFJUdVRmNzJpV09mNTg2cW9BSHZrajA4c3BNR2RIODNqMGVORDBIRjFkVlFoZVFyWlpsOE10U1ZqOE5FXzgyWDBpVl9iemRfUVlCNzItZEhySkRiWW1rRk4yRmFTdDB4SWxYU2huTEFraTVXVEtJUWdYeWFqZDY0NmNYekp3V3hsTGZkY0VoWVhmbko3XzZF?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxPNTV3RlVEOEpYSUVEcUFXZE9NZXVTRjVmZFBGTjVRajdrLUZvVndpcUxldHVHM2hiaF9EZ1VDdURyVTdsa0wwS3hQUjFJd3FaeHJCTWttMFJJZ1J6UmV6cFFUM1FWVEJYb2Y3M2tEaE9aZDJiN1h0NTZ4Q21WT3pTa3JmRUlLQmVUSFRTSjVMZ0stOXAySHdFVWhWbFAxYzNrMmhhQVo4SQ?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxNd3g5ZUlkYjdveC1zQUZ0cW5Bb3dUUXBfdlNxTFEzd2hKYm9HRWpBNGZlYXpoaFUwWFVha0VSdFdqQm1uMUp5WGw0OVg0LTBYYmtOUDg5RVpTMHkzbndsc0FCd1BzWFdIdUcweEszLXVwUGtpVTc0Y0E2RER5OWhHcWpZT29lWGZnSEJnNl9tOTlEd3M5OFR3UnNWRzZZN1ViWTBhcW1tWEwwYWNUc1EzS01TaVBqYXUxd1NPM0NDQQ?oc=5
- https://news.google.com/rss/articles/CBMi7AFBVV95cUxPaHB6WEIzekctQmp6Qmk0WFlCQUNoNFRtYUticEIzSWJDYVlVTDNwb3RRSTZhNUZ2X0gtRE9tR29jNGsxeFpSaV9YczBKQ3o0ME1LSmNSWFRlUzUtS0djLVVodUVWaWt0bnU5SnR1NUVUZkU0cDNKUjJNLTlIRElibXc3TTAyeXNzWF9KRTRFMmtXdGRnSC1fOGRtNG1PZ3I4WEVGQTdOUzhxMXBJYnRRc1ROcUdVOXU2cXEzaWl5V1FneFpJUWY4dTNuTFF4Z3F6Wjd0dVlxTUNSU0x2V3dlbGJIUmtHMlROaFZTONIB8gFBVV95cUxOamxzYXdDZ2dsVkdmMERUSjdwZUNZcVo1VV9YMnlWT1lvZ2dOc3Z2U2NUb1poVS1WcWF6RnJYaGRlZDBLTDFzZEtrSXliUHZNQU80cWdNNW0zTldLdzZtLW1OTEFPaDlLLWZuMVpHaTcxdEJ1cUNaQ2hDZnBFN3JDZlRMYVZlNVo0R1cwRFQ4WXZITVBaU1lzVFZDYnhlQjItX0tELTJSNE5mdjBxUFNEajJ4ZFp2azRXbWdxZk1ZQ1E0N1MxekZvRkZjNVhzV2xXWmZtSFh3X2lKdE5IWnc2U1VuRUcwSEw2d0hlRVpnLTBBQQ?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxQeUFjTDdEbDFjNHRuQkJrQ01tbmtDY2x0SElRRldweTNyeENXYy1uWjJXTU9PYm05V2N5Zm54dUY1UXRBUHlRMUFuQXZIQ0lKRDBFME84TmVHYWxnOXh2RkJQN0xjTmJOR1Q1OHUzdlZweUVWdHBpbU1DSWxIMUM1VVdidUM5eFZZcHUwZmV4Q1NCUmloOW9xSFU0ZFJpTjJBN3lQOEtyUTU4dw?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxQZGFMeFZzY0t2YUVwN3FIdTMwQ1NEbGFzLVR3aDJqX0h0ZUYxUVFTQUZ4R1pIdEZwTlhXTHlmdnQwNzFGSWFvNVJrQlpHWE43VUFhMGRmQndDT1U0QUhOWXpJVThNOS1zbTZ1cDlmOWp6VDRUQklxcm12QXduel9mX3JBVndMOS01dnBhN2Y0aTRieVQ2empaSUZLcUJoSWdlWUFSMUY3bw?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxNOUNqVFZuZ1ptX3NGT1NHNXctTHlaUHdVUDkzUTJqZ2VadnlLTm5ocGNrTnJ3TXJfS3Y5RTRRSXpleHI2Tlg4dUJhVi04MWZZZXhEd1ZMSXotNnRhSG5HX0l5Y3J0NmhOV3FDamw5eDNSZDEwcFBLM3hzTG1qU0JkU1UzRkdKVWl3ZWtlNEtqdFdhVXRTbk9ZMHRRZ2xjZGhNcVpMcmdRb3VJcU9kYXVpQ2JrdUdOUEEx?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
