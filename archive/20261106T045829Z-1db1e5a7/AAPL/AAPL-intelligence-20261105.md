# AAPL Intelligence Report

- ticker: **AAPL**
- Report as_of: **2026-11-05**
- Market data as_of: **2026-11-05**
- Quant sources: https://finance.yahoo.com/quote/AAPL/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AAPL/key-statistics/
- AI analysis snapshot as_of: **2026-11-05**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-06T05:11:49.888846+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 7, 'ai': 13, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **8** exact headline/source/date matches; prior report **20261105T045846Z-bde0a1fe/AAPL** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **3**; {'low_uncalibrated_model_confidence': 3}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 10 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 40.0%; oldest publication 2026-10-29

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 344.1700 |
| Return 1D (%) | -1.5279 |
| Return 1W (%) | -1.3585 |
| Return 1M (%) | 3.3885 |
| Return YTD (%) | 26.9429 |
| Return 1Y (%) | 27.8749 |
| Annualized volatility (%) | 24.8362 |
| Beta vs SPY | 0.5911 |
| Max drawdown (%) | -13.7985 |
| Sharpe (rf=0) | 1.1185 |
| Downside deviation (rf=0, %) | 16.9425 |
| Sortino (rf=0) | 1.6397 |
| Historical VaR 95% (1D, %) | 2.0034 |
| Historical ES 95% (1D, %) | 3.4742 |
| Correlation vs SPY | 0.3235 |
| Tracking error vs SPY (%) | 24.1490 |
| P/E (trailing) | 38.33 |
| P/B | 44.62 |
| EV/EBITDA | 29.39 |
| Revenue growth (%) | 11.70 |
| Forward P/E (estimate) | 32.32 |
| Gross margin (%) | 48.79 |
| Operating margin (%) | 31.13 |
| Return on equity (%) | 142.26 |
| Free cash flow yield (%) | 2.11 |
| MA50 | 335.4580 |
| Close vs MA50 (%) | 2.5971 |
| MA200 | 298.0619 |
| Close vs MA200 (%) | 15.4693 |
| RSI (14, Wilder) | 53.0079 |
| MACD (12,26) | 2.2944 |
| MACD signal (9) | 3.0301 |
| MACD histogram | -0.7356 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AAPL': 276, 'SPY': 276}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 344.1700 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.5279 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -1.3585 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 3.3885 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 26.9429 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 27.8749 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 24.8362 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 16.9425 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.6397 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.0034 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.4742 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.3235 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 24.1490 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.5911 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -13.7985 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.1185 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 32.3220 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 48.7860 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 31.1250 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 142.2570 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.1125 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 38.3263 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 53.0079 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.7356 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 2.5971 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 15.4693 -> Clearly above the moving-average trend level.

## TAILWINDS

### Apple’s (NASDAQ:AAPL) Q3 CY2026 sales beat estimates
- Summary: Apple’s (NASDAQ:AAPL) Q3 CY2026 sales beat estimates
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxQSE5CdzZJSUNib0pJNnlFaWpqQjJfUkIxME9lNGdYZmZMWk5aTFotTldPY09Db2lNNEFKSzZqZl93YThIM0VZZjV0aFJaN2lPTDY5UEUyLVNPTlNyeGF6cGFEd05XZkVCRm9zYTNwSEEyazBYOW5veHhHWm9BOGllNkw2XzhPRk5WWEJaS3ZBclJoLXVaLTVV?oc=5>

### Apple (AAPL) Q4 Earnings and Revenues Beat Estimates
- Summary: Apple (AAPL) Q4 Earnings and Revenues Beat Estimates
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihwFBVV95cUxObmE4VGQ2bWZvZWdNcDN5QnU2TW56V05vX2VJMXZiQzYxQWNmVkNsSFh4Y1d5ODUyZG9rS1BLeVZIdDhoZG05Ml91Q0tYczBDSGsyMk9VTEl2b29ERE1iMnBYelhMczd4Y2pGV2RkdndMdFFLYTVZQ0hEV1JycnhnLUNWOFU4c00?oc=5>

### Why the Democrat blue wave could be a good thing for Apple stock
- Summary: Political shift may boost Apple’s market prospects.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxNbzZxNU01Z0RMd3lqLXNsQ2o3cEVfZ18xcWhydHlsZHVMY3UtNFliYzBnNEMtdXBnMzhLdENvcGctdXJMV1hYTmtVMlZIM0NVc0l2VWV5M3BLdUtoXy1NVEphRnowV05yQWgwYTZfYTgyZGRBaGlESUF1c3RVMUw1OTBkNG9GdHZFTFBqSEFmQVhTN2kwWFc4X01iZHhRWGY5MWhqMlk1dVhnTkFmWG0wY1hJbVJHMGNpaUNrMl9uMHZoZHZ1b21B?oc=5>

## HEADWINDS

### Apple (AAPL) Stock Faces Pressure Despite Strong Q4 Earnings and Climate Goals
- Summary: Apple (AAPL) Stock Faces Pressure Despite Strong Q4 Earnings and Climate Goals
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxNMUh0UW9DdHJ4YUZBdWNKNjBzeGRfMUgyZ2JFSHY2RnR3eGs1YTJGQWJsd0J2ZDVHaGpBbXhhdzl0c2FpR0R1UnhPd2gwZlVqZjFzVDBRM3ZDOGk0a1dnS0JFV2NYZjI3VWJIMWJZZWpiajNWanpKUC1hWEFObGd3VjF1R2Q1b3V5SzhYVzBHYkZ4bzh6SDBMTGEyclFzYWp0MmpNdURR?oc=5>

### Apple Q4: Record Earnings, Broken Expectations - I'm Downgrading (NASDAQ:AAPL)
- Summary: Apple Q4: Record Earnings, Broken Expectations - I'm Downgrading (NASDAQ:AAPL)
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxQbG1zaWF3ZE1pMWwzdVROMDlDUGVnaXRpMG1YRDZaTUtTSHQ2ak0wdHVqRXRnNWZfYzNEVVJZM2pRdFphcDB4TGdxa3dfZEpPVk9mMXl1TlY1VEtzb205WHZ1MGJmQTF4cm5GWnAybVB3VG1Vdks4VUNBVmgtTlVxUS15MVp4dGdTNF9hX1F1RUdRZXlTMXo5TmFFRE4wcGlyOFE?oc=5>

### Should Apple (AAPL) Stock Worry About Ternus’ First Call And Rising Chip Costs?
- Summary: Rising chip costs and Ternus first call may pressure Apple’s margins.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxNMXVISmxvelljSS1JeS1CU1Z0QUhWNnk5bzhWdTFZVUxwc0wza1BXWHVkbjU2TGlEYjVDNDZYV05pMURCNlpGT01yUmxMTmtfWWRQMWFNNlRfNEpLMV84WENXcjVETzJZQkRYaFZuM3ozVy1OZEJjcU9qRm9OU3I2akx3dlB3NVhsMmtSSEV5ckpMQTZueDhZc19n?oc=5>

### Stock Market Today, Nov. 2: Apple Stock Slides Ahead of Earnings, but Its Latest Results Tell a Different Story
- Summary: Apple shares fell before earnings, but recent results suggest a different outlook.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxPMmVyaDFCbFUzN2owbVpab2hVYmNHTU5MMWVSQkhqV3l2TDFIaE5KaEdYSGJ5N2dTLXphVFBhN1dCQVI5NzRfcFdNZlB3dzJBZ2VmTFVwRGNnUlVHYnM5WEJfT3Juc0pab21qcGpSWXpjSkNGYWM2eGd5U25tTHAybXo4MGdrRFJyWGRIdV9jbE5ZUkE?oc=5>

### Apple 2027 Growth Outlook Faces Scrutiny — Analysts See iPhone Upside, Flag Services Slowdown And Margin Risks
- Summary: Analysts question Apple’s 2027 outlook, citing services slowdown and margin risks.
- Date: 2026-11-03 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxNWW01ZUZ0UlRKbVl5cTRyS2tXUmc2S0Q2ampkSnpGX2NBdGtOdjBycnV3V2pYUWYzZ0Fmel9SNjdYTm9KejVCQlowQk9Gb1RWNmFCZVBfUjNjVGlEaGViNnp1TmVVdlNpVUVVNXlWa0VMN21mVWRseFBaMGtfOEhjMHpTTTZOQXVVdTQ3UEduaVpzOXNMenJVc1dubmM?oc=5>

### Apple (NASDAQ:AAPL) Stock Slides Despite US$114.5 Billion Revenue Beat: What Went Wrong?
- Summary: Apple shares fell despite strong revenue, indicating market concerns.
- Date: 2026-11-03 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMigAFBVV95cUxPVDJEM1V3RE91VEdDRFFTZE9OXy1qVEpHMXlNeWJlbG9oQzNLRFl0cy01MXNXZXM2Z3BwM1FKdnFRNkFUX1NKSlJRR1RCXzdOXzB3X2dETTFPVlNMN0R0NDAzVDZ4UlZDQXhYYWx2R0RGd0V3aU5OSmd4b2tIdkdCMw?oc=5>

## CATALYSTS

### Apple (AAPL) Stock Faces Q4 Earnings Margin Squeeze
- Summary: Apple (AAPL) Stock Faces Q4 Earnings Margin Squeeze
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxOdDdteU5mbzM5MUZVUnZKLWJkdUNXX3JKVlhQVXMtRFdhWExJb2s1Q1Y4VDNrMVRZQ1JnYTVfaHpCeEhrZFpWbVQySDZUM3k1V3RtdXJuNmRuVHpxRDFIdWU3VWY5VURSeDZackdpRFZaRHFYb3FnalBHaWRLWUxXcFNMYmRfU3M0bWRGTi1YUG1Pdkxt?oc=5>

### Apple Earnings Put New CEO John Ternus in Focus
- Summary: Apple Earnings Put New CEO John Ternus in Focus
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxOZ19raXctR0QzMVNDanBoa0VPSkdlQmp4Y1RScDl0S0dNQ1ZxWmZwUTcyRGUzbDNTYVZzMkpwVWRlbkVscTNJQ0FjeHB6STN6WnhZZnVmdl9FUFhQaUYtWXJ2NXRrTGhtNUxqQzVTOFNqYXh2NDRSdWtlVDRWUS1KaW1Gd05OcG1UT1BYOGZVRnZDSDZlLVpR?oc=5>

### Apple heads into earnings with highest P/E ratio since 2007 (AAPL:NASDAQ)
- Summary: Apple heads into earnings with highest P/E ratio since 2007 (AAPL:NASDAQ)
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxQLWlSMjdTcU9XRm0zWldMT1VpbktwV1ZFTFMwUHZUa0FVd0hVSHF2WW95Slh3eDRvbnlrQlpsUWxZMmpDc0xEc1F5UG8wT0NvbHRIaHJ5Tll3eFBFRFhNRGlCc09Md3lidmw1M1hCY3hucVFvTU5ZTlRPb3JjRzZDWHNHVzluZDdjaTVKVDdOM1RvQ0hTVC1RQnFhbnpjQQ?oc=5>

### Buy Apple Stock (AAPL) After Earnings, Says Bank of America
- Summary: Bank of America recommends buying Apple shares post-earnings, citing positive outlook.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxQWG5CZ1FMYVVJRG8wWElvdkZOQnBGZjc4NlczM2Fkamk0WFloUGttdXZrQ1Q0cmNkSjlTV3U5UGdEMmwzSE5ua2o0bFp3TzdBTkNwQnl2aFdrWDR1YmVqel9xdVRDdUZIYkg0Q3djLVRTY0RpUjliWGctRnBJT0hmcW4yRktaNjdVTllaYkZtRQ?oc=5>

### Apple's Q4 Earnings Loom: Buy or Sell AAPL Stock Ahead of Results?
- Summary: Apple is preparing for Q4 earnings release, prompting investors to decide on buying or selling.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxOMHN2dUpzWHQ5Zzh6ZGVBSWZsSUk5Wnozek5sbmNZQjhWYTVIQlRJZUdBT2xhU2xDZ2Jsb1dIbkkzNWtacTNRTXl6NVpwVENHdHgycTA2YmJsbXFHZmVpSnQxcTl3eVNXY045NUgwSlE4UnpLYzR4QTJOV0JrUGNGelR0TGpPTTlaQmNrVGY3eU03TXExdEtF?oc=5>

### Apple (AAPL) Stock Could Be 30% Overvalued Despite Record iPhone Sales
- Summary: Apple’s stock may be overvalued by 30% despite strong iPhone sales.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxObHl6UFg0RmRmWXdsZHllLVp6VWs5WHcxWTlraVhPR3hfdGtPMnJnTEkwZUxZakktLUNWU19hMS1aZnRhQjk4eERNN3RIbGZxM3pCVHotUjhwbmwyVUViTVctbFU3X1Nxb3JReE9aTm5JbTBXZWhyeU5zci1PTXV1REJJYjYtOFN4TEoweUc5Qi1GWU9W?oc=5>

### The Open Question Under Apple Stock’s Price
- Summary: Uncertainty remains about Apple’s stock valuation.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxPV1RBeXktRnlQOE41Vzk4bVVyLUZfc1NDRXJnSUVmbzhMTjBvejVHUEg0R1hzbzdXZEVreFI0S3d1TE90NjFGMEFEY0w1QWpocDQwX0taeUNFS056VUNHOEF2ai0wY29qekhmNEd2X1BGd1c1TElMSzJhS0lpQjlLWGdmbHR1cXR2RThqM0FrZUtfczZaM3MzdzhWUEw3WklnWXZod3dn?oc=5>

### Apple Stock: Sell - The Premium Without The Growth (NASDAQ:AAPL)
- Summary: Analyst recommends selling Apple stock due to lack of growth.
- Date: 2026-11-05 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxPTnBacUN1bkpIOUlpeW51dlp2dnZraUR6Y0VjbWxRWERtVUIyMDd4UXhxdkJ6Yi10Uy1hWU5UVWNLaGdvVW1xVG80SXEtbTZ1dnVrRFk1aGdfZEt2U1RURWZ3dVI0aVg4aV9TZURmNk1fYU9qZkR1b2tPdHp6aFB6YjBSbDFjc1ViZkE?oc=5>

### Apple taps bond market in seven-part offering (AAPL:NASDAQ)
- Summary: Apple issues bonds in a seven-part offering.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.5
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxQdzY5d2J6UmJEV09UN3hLTmViam1qWGJPM2xYMFhFNU9tUzhZdDV2Y3lEajV6NmpHSk5yRzd0VFpjSTktWTltZkR4THpHS01HRnY0eHhGX2M4a0RPN0ZXbGVTbEkzWjFPem1MVVFtTi1pRm9tNUdycFBsN3hSNDVYSTE1V0FHaGpJYk1r?oc=5>

### Apple: Demand Is Not The Problem (NASDAQ:AAPL)
- Summary: Apple states demand is not an issue.
- Date: 2026-11-05 | Impact: low | Horizon: short | Confidence: 0.5
- Sources: <https://news.google.com/rss/articles/CBMifEFVX3lxTE84QXgzWUhYbkxQQVhtODEtYlE0T3lXTXUycjFnX2xrTWs3bGU4X0VHbnE2eGxjWVNnaTcwTE9fOHV2YjFKcWdSRkVtMUZnYXFGUHNXUjIxT2gtOHU0S0xFMFoxR1pWTTY3cGtBbEpFZ2JwcGZLTVBJbUVTTl8?oc=5>

## RISKS

### Apple: The Midterms Won’t Save It (NASDAQ:AAPL)
- Summary: Political uncertainty from upcoming midterms could negatively affect Apple’s performance.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMifEFVX3lxTFB6RkNJaloxY2pfNWF6c1djdVBGV2pSUFBfNmdmRk5FNGtYODBRald2T1RjeWdET051NkRwUlB5SDdHU2ZqOWU5M19ZQ19sa1JPaUh6ZEFjZTdFT1p6UXVuTUpqV0NDelBldzFTR0s1aHdlVlJqVDRZOHVnRU4?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AAPL** | **38.33** | **44.62** | **29.39** | **11.70** | **5,001,541,320,704.00 USD** | **27.87** |
| MSFT | 29.00 | 8.46 | 19.69 | 18.80 | 3,979,920,277,504.00 USD | 6.54 |
| GOOGL | 15.09 | 5.27 | 18.20 | 24.70 | 3,473,915,510,784.00 USD | -0.35 |
| SONY | 20.55 | 3.17 | 0.12 | 8.20 | 160,829,358,080.00 USD | -1.92 |

Peers fetched as_of: 2026-11-05; AAPL reuses existing data (market data as_of: 2026-11-05); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-02
- Next expected earnings: 2027-01-28 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-05

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-K
- Filing date: 2026-11-03
- Revenue (latest available single quarter): 62,900,000,000.00 USD; period 2018-07-01/2018-09-29; fiscal year/reporting period 2018/FY
- Net income (latest available single quarter): 29,789,000,000.00 USD; period 2026-03-29/2026-06-27; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/320193/000032019326000026/aapl-20260926.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMilwFBVV95cUxQSE5CdzZJSUNib0pJNnlFaWpqQjJfUkIxME9lNGdYZmZMWk5aTFotTldPY09Db2lNNEFKSzZqZl93YThIM0VZZjV0aFJaN2lPTDY5UEUyLVNPTlNyeGF6cGFEd05XZkVCRm9zYTNwSEEyazBYOW5veHhHWm9BOGllNkw2XzhPRk5WWEJaS3ZBclJoLXVaLTVV?oc=5
- https://news.google.com/rss/articles/CBMihwFBVV95cUxObmE4VGQ2bWZvZWdNcDN5QnU2TW56V05vX2VJMXZiQzYxQWNmVkNsSFh4Y1d5ODUyZG9rS1BLeVZIdDhoZG05Ml91Q0tYczBDSGsyMk9VTEl2b29ERE1iMnBYelhMczd4Y2pGV2RkdndMdFFLYTVZQ0hEV1JycnhnLUNWOFU4c00?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxNbzZxNU01Z0RMd3lqLXNsQ2o3cEVfZ18xcWhydHlsZHVMY3UtNFliYzBnNEMtdXBnMzhLdENvcGctdXJMV1hYTmtVMlZIM0NVc0l2VWV5M3BLdUtoXy1NVEphRnowV05yQWgwYTZfYTgyZGRBaGlESUF1c3RVMUw1OTBkNG9GdHZFTFBqSEFmQVhTN2kwWFc4X01iZHhRWGY5MWhqMlk1dVhnTkFmWG0wY1hJbVJHMGNpaUNrMl9uMHZoZHZ1b21B?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxNMUh0UW9DdHJ4YUZBdWNKNjBzeGRfMUgyZ2JFSHY2RnR3eGs1YTJGQWJsd0J2ZDVHaGpBbXhhdzl0c2FpR0R1UnhPd2gwZlVqZjFzVDBRM3ZDOGk0a1dnS0JFV2NYZjI3VWJIMWJZZWpiajNWanpKUC1hWEFObGd3VjF1R2Q1b3V5SzhYVzBHYkZ4bzh6SDBMTGEyclFzYWp0MmpNdURR?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxQbG1zaWF3ZE1pMWwzdVROMDlDUGVnaXRpMG1YRDZaTUtTSHQ2ak0wdHVqRXRnNWZfYzNEVVJZM2pRdFphcDB4TGdxa3dfZEpPVk9mMXl1TlY1VEtzb205WHZ1MGJmQTF4cm5GWnAybVB3VG1Vdks4VUNBVmgtTlVxUS15MVp4dGdTNF9hX1F1RUdRZXlTMXo5TmFFRE4wcGlyOFE?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxNMXVISmxvelljSS1JeS1CU1Z0QUhWNnk5bzhWdTFZVUxwc0wza1BXWHVkbjU2TGlEYjVDNDZYV05pMURCNlpGT01yUmxMTmtfWWRQMWFNNlRfNEpLMV84WENXcjVETzJZQkRYaFZuM3ozVy1OZEJjcU9qRm9OU3I2akx3dlB3NVhsMmtSSEV5ckpMQTZueDhZc19n?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxPMmVyaDFCbFUzN2owbVpab2hVYmNHTU5MMWVSQkhqV3l2TDFIaE5KaEdYSGJ5N2dTLXphVFBhN1dCQVI5NzRfcFdNZlB3dzJBZ2VmTFVwRGNnUlVHYnM5WEJfT3Juc0pab21qcGpSWXpjSkNGYWM2eGd5U25tTHAybXo4MGdrRFJyWGRIdV9jbE5ZUkE?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxNWW01ZUZ0UlRKbVl5cTRyS2tXUmc2S0Q2ampkSnpGX2NBdGtOdjBycnV3V2pYUWYzZ0Fmel9SNjdYTm9KejVCQlowQk9Gb1RWNmFCZVBfUjNjVGlEaGViNnp1TmVVdlNpVUVVNXlWa0VMN21mVWRseFBaMGtfOEhjMHpTTTZOQXVVdTQ3UEduaVpzOXNMenJVc1dubmM?oc=5
- https://news.google.com/rss/articles/CBMigAFBVV95cUxPVDJEM1V3RE91VEdDRFFTZE9OXy1qVEpHMXlNeWJlbG9oQzNLRFl0cy01MXNXZXM2Z3BwM1FKdnFRNkFUX1NKSlJRR1RCXzdOXzB3X2dETTFPVlNMN0R0NDAzVDZ4UlZDQXhYYWx2R0RGd0V3aU5OSmd4b2tIdkdCMw?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxOdDdteU5mbzM5MUZVUnZKLWJkdUNXX3JKVlhQVXMtRFdhWExJb2s1Q1Y4VDNrMVRZQ1JnYTVfaHpCeEhrZFpWbVQySDZUM3k1V3RtdXJuNmRuVHpxRDFIdWU3VWY5VURSeDZackdpRFZaRHFYb3FnalBHaWRLWUxXcFNMYmRfU3M0bWRGTi1YUG1Pdkxt?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxOZ19raXctR0QzMVNDanBoa0VPSkdlQmp4Y1RScDl0S0dNQ1ZxWmZwUTcyRGUzbDNTYVZzMkpwVWRlbkVscTNJQ0FjeHB6STN6WnhZZnVmdl9FUFhQaUYtWXJ2NXRrTGhtNUxqQzVTOFNqYXh2NDRSdWtlVDRWUS1KaW1Gd05OcG1UT1BYOGZVRnZDSDZlLVpR?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxQLWlSMjdTcU9XRm0zWldMT1VpbktwV1ZFTFMwUHZUa0FVd0hVSHF2WW95Slh3eDRvbnlrQlpsUWxZMmpDc0xEc1F5UG8wT0NvbHRIaHJ5Tll3eFBFRFhNRGlCc09Md3lidmw1M1hCY3hucVFvTU5ZTlRPb3JjRzZDWHNHVzluZDdjaTVKVDdOM1RvQ0hTVC1RQnFhbnpjQQ?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxQWG5CZ1FMYVVJRG8wWElvdkZOQnBGZjc4NlczM2Fkamk0WFloUGttdXZrQ1Q0cmNkSjlTV3U5UGdEMmwzSE5ua2o0bFp3TzdBTkNwQnl2aFdrWDR1YmVqel9xdVRDdUZIYkg0Q3djLVRTY0RpUjliWGctRnBJT0hmcW4yRktaNjdVTllaYkZtRQ?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxOMHN2dUpzWHQ5Zzh6ZGVBSWZsSUk5Wnozek5sbmNZQjhWYTVIQlRJZUdBT2xhU2xDZ2Jsb1dIbkkzNWtacTNRTXl6NVpwVENHdHgycTA2YmJsbXFHZmVpSnQxcTl3eVNXY045NUgwSlE4UnpLYzR4QTJOV0JrUGNGelR0TGpPTTlaQmNrVGY3eU03TXExdEtF?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxObHl6UFg0RmRmWXdsZHllLVp6VWs5WHcxWTlraVhPR3hfdGtPMnJnTEkwZUxZakktLUNWU19hMS1aZnRhQjk4eERNN3RIbGZxM3pCVHotUjhwbmwyVUViTVctbFU3X1Nxb3JReE9aTm5JbTBXZWhyeU5zci1PTXV1REJJYjYtOFN4TEoweUc5Qi1GWU9W?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxPV1RBeXktRnlQOE41Vzk4bVVyLUZfc1NDRXJnSUVmbzhMTjBvejVHUEg0R1hzbzdXZEVreFI0S3d1TE90NjFGMEFEY0w1QWpocDQwX0taeUNFS056VUNHOEF2ai0wY29qekhmNEd2X1BGd1c1TElMSzJhS0lpQjlLWGdmbHR1cXR2RThqM0FrZUtfczZaM3MzdzhWUEw3WklnWXZod3dn?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxPTnBacUN1bkpIOUlpeW51dlp2dnZraUR6Y0VjbWxRWERtVUIyMDd4UXhxdkJ6Yi10Uy1hWU5UVWNLaGdvVW1xVG80SXEtbTZ1dnVrRFk1aGdfZEt2U1RURWZ3dVI0aVg4aV9TZURmNk1fYU9qZkR1b2tPdHp6aFB6YjBSbDFjc1ViZkE?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxQdzY5d2J6UmJEV09UN3hLTmViam1qWGJPM2xYMFhFNU9tUzhZdDV2Y3lEajV6NmpHSk5yRzd0VFpjSTktWTltZkR4THpHS01HRnY0eHhGX2M4a0RPN0ZXbGVTbEkzWjFPem1MVVFtTi1pRm9tNUdycFBsN3hSNDVYSTE1V0FHaGpJYk1r?oc=5
- https://news.google.com/rss/articles/CBMifEFVX3lxTE84QXgzWUhYbkxQQVhtODEtYlE0T3lXTXUycjFnX2xrTWs3bGU4X0VHbnE2eGxjWVNnaTcwTE9fOHV2YjFKcWdSRkVtMUZnYXFGUHNXUjIxT2gtOHU0S0xFMFoxR1pWTTY3cGtBbEpFZ2JwcGZLTVBJbUVTTl8?oc=5
- https://news.google.com/rss/articles/CBMifEFVX3lxTFB6RkNJaloxY2pfNWF6c1djdVBGV2pSUFBfNmdmRk5FNGtYODBRald2T1RjeWdET051NkRwUlB5SDdHU2ZqOWU5M19ZQ19sa1JPaUh6ZEFjZTdFT1p6UXVuTUpqV0NDelBldzFTR0s1aHdlVlJqVDRZOHVnRU4?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
