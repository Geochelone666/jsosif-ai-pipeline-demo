# AMD Intelligence Report

- ticker: **AMD**
- Report as_of: **2026-11-09**
- Market data as_of: **2026-11-09**
- Quant sources: https://finance.yahoo.com/quote/AMD/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AMD/key-statistics/
- AI analysis snapshot as_of: **2026-11-09**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-10T05:55:50.957808+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 7, 'ai': 9, 'unknown': 0, 'irrelevant': 9})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **2** exact headline/source/date matches; prior report **20261109T043242Z-c8e908de/AMD** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 14 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 24.0%; oldest publication 2026-11-04

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 508.5800 |
| Return 1D (%) | 13.2594 |
| Return 1W (%) | 8.9410 |
| Return 1M (%) | -16.3657 |
| Return YTD (%) | 137.4766 |
| Return 1Y (%) | 117.7700 |
| Annualized volatility (%) | 73.1698 |
| Beta vs SPY | 3.4196 |
| Max drawdown (%) | -37.7290 |
| Sharpe (rf=0) | 1.3772 |
| Downside deviation (rf=0, %) | 47.2973 |
| Sortino (rf=0) | 2.1305 |
| Historical VaR 95% (1D, %) | 6.3376 |
| Historical ES 95% (1D, %) | 9.4746 |
| Correlation vs SPY | 0.6399 |
| Tracking error vs SPY (%) | 65.2624 |
| P/E (trailing) | 108.67 |
| P/B | 12.20 |
| EV/EBITDA | 74.27 |
| Revenue growth (%) | 44.70 |
| Forward P/E (estimate) | 28.81 |
| Gross margin (%) | 56.00 |
| Operating margin (%) | 21.17 |
| Return on equity (%) | 11.96 |
| Free cash flow yield (%) | 0.88 |
| MA50 | 547.6738 |
| Close vs MA50 (%) | -7.1382 |
| MA200 | 417.2220 |
| Close vs MA200 (%) | 21.8967 |
| RSI (14, Wilder) | 47.6712 |
| MACD (12,26) | -26.9474 |
| MACD signal (9) | -19.3481 |
| MACD histogram | -7.5993 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AMD': 278, 'SPY': 278}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 508.5800 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 13.2594 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 8.9410 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -16.3657 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 137.4766 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 117.7700 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 73.1698 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 47.2973 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 2.1305 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 6.3376 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 9.4746 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6399 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 65.2624 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 3.4196 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -37.7290 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.3772 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 28.8103 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 56.0000 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 21.1710 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 11.9600 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 0.8820 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 108.6709 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 47.6712 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -7.5993 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -7.1382 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 21.8967 -> Clearly above the moving-average trend level.

## TAILWINDS

### Advanced Micro Devices soars 13% on Google Cloud deal, tech rally (AMD:NASDAQ)
- Summary: Advanced Micro Devices soars 13% on Google Cloud deal, tech rally (AMD:NASDAQ)
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxNbWlsWGwzaEFUQkppQnFleUFqeldtRmJNaVctS3luSE5XS0QyZUVPTi1rMkM2T29HMG9EWVBvTDB4cDN0dlpQX2JWZG9DdGl3blRuNEJJb1diS2k3bFlubzg5OWdqLTREZHgzWUl5eWtpQU55TFpaanJkS0Y1UG1tR1BQUmxzeDUwWHY1RWFUZlU0Z0RxMktwOS01cHBOTmRIcTdF?oc=5>

### Advanced Micro Devices (NASDAQ:AMD) Shares Up 13.3% - Here's What Happened
- Summary: Advanced Micro Devices (NASDAQ:AMD) Shares Up 13.3% - Here's What Happened
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixgFBVV95cUxOSGNhdHRDWVJTZ3hNZFVuTHlPdXdqSGZZcDRJNnZoQlJ2MWsydWNibVowMkRkNDltWEdjN3pmUlRBNHBkTGdJS1EwVVRObjVNcFBHLXFOWDhIeFR4WlR5bUV1ZVJDM3lCRWNCdTZtYXZHOE9tVDU4RWJEYnI1Wk5Tc0J3QktsVHFVNmt4NklPSEFTOC1RaTNsbkliYXM5T2w5LXd3RDUyTTRwU21NVWhpV1NtQ2QyM09YWm9IZlZxTWo2eU9xZEE?oc=5>

### AMD Stock Rises On Google Cloud Deal, Wall Street Upgrade
- Summary: AMD Stock Rises On Google Cloud Deal, Wall Street Upgrade
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxNc0pob1FQZVItVXBmSHRhb1kzQkg0T3ZaR1FlT3hqQ3NEUEpPUDZoN19qTHRHZ1R4UHN2dUI3MEg4OVRITGNxc3V3WjRNZTJpQndZbm1SY2J1Wm1SRGZWRVRkQm5HaGZhWlBhbG15dHdYaWc5cUdYZjN5QjBjWk5kVlhDZ0N6WlJzbEdfWUU3QU1FaFhraTVUNzBORFVhOVRG?oc=5>

### Advanced Micro Devices Stock Pops on Oppenheimer Upgrade
- Summary: Advanced Micro Devices Stock Pops on Oppenheimer Upgrade
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxPblVKQTdzS3pVSWRRMHp0SUhjTnFPWFl6bWRMS1QtcVBleURPeGlRMlBsejNVYnBYQlVPMnp2bE94aUFybFVPSlZfbzQzV0RwQWRnc0p4LU5jeFB4MTZRRWIzbGJ3Z25kY2M5Q3V6WUMzNHQ4MmY1R0JVS2djMUR2V3ItQ2ZuTE5leGVkTW5YcXljLUpvTGsxYU5PQWI1OXhvVFI5MHQyRGpPaGRjdEhoelBYa3dQdw?oc=5>

### AMD Soars 12% on “Undeniable” Data Center Success per Oppenheimer Upgrade
- Summary: AMD Soars 12% on “Undeniable” Data Center Success per Oppenheimer Upgrade
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxQMUVCMkhJekg0eE5fVEVhaXlCNEdqUHgxZHB6SlRQSmxYNGxUTzBfajFpLVQ2c1hpc0V6RVFiQnc5Q05OaGR2cVdGVzg1MUlUcFQ1NWlSTTFKbDhrWlJadDZ5dlVlYXQ0ZFpoWjRtNnRnY3lWQ0RPVGNHWmRMbEt5d29FVkFGSkFsV2tweGQ1LUJ5YXFCS29qUg?oc=5>

### AMD Stocks Jump 9.50% After Oppenheimer Upgrade Sets $600 Target
- Summary: AMD Stocks Jump 9.50% After Oppenheimer Upgrade Sets $600 Target
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMieEFVX3lxTE01cm9PLTQxUjBBdmFmTEk1LURPcWJyRUVqRWtQakFWVDlDbkt1cHE1SHZla3NBS3ZqYkdBRFFqclhqY2FjYjRzTXlRTlFlVy1kb0JqRVFyVVI4V2FQMTNxdzA3eDc5dk5OWjkycWQxVnV1a3FGWWpYNA?oc=5>

### 53 ETFs Add to Advanced Micro Devices (AMD) on Nov. 4
- Summary: ETF additions signal institutional confidence and potential liquidity boost.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxOLTJJcVJGQUh6QzJQOEF0WnNKb09adzIwUDAyQWR5emxKZjNaMmZmTFhkTmJiOUFiQnMtc3hucWpRQksxX3FCQzdtSm1ablVJUzhRYjkwd0VvdVRRR2h2VUdVd0JJVTA5dGdUWmM4WHRqTER0WHl2aFRQcWxRM05hRk1oSUNmZDVmd1hBaGZfbU44ODBNdWc?oc=5>

### Stock Market Today, Nov. 9: AMD Jumps on Oppenheimer Upgrade and Google Cloud Chip Selection
- Summary: AMD shares rise after Oppenheimer upgrade and Google Cloud chip selection.
- Date: 2026-11-09 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi5AFBVV95cUxQM2lSUmJqV2lOZUhtVVBfd2pWSmllT0Q0SlYwdkkyUFFINU8zMWNKc2dTM0lOMmgxbEVXYWJ2SnVnTnN4T0U5aXVPbFVwU0xreEphclFTT1psSDRuYWVTTjVqUnlCZnFxdnVPRF9Wd1NwWlpNM05KZ3BVb2dKSTZsM2FtN2JZNW5qcDZZVnluWkxuMHByM3ppTGg1QTZ1dGpvLXlhT0pERkZCV2xmYUQ0NzdsMk9mWC1sZnhxNzFTZks0ZVlWZlBZSWxMVlpqMDhMTGlUc3A5Q2xHWmFKZ21PV3JPNVY?oc=5>

## HEADWINDS

### Advanced Micro Devices (AMD) Recently Crashed Out of the $1 Trillion Club. Should You Buy the Dip?
- Summary: AMD loses $1 trillion market cap, indicating a negative market move.
- Date: 2026-11-07 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxOeEpRMjVrSzZYZENMSFgxdHVucTIxajJzb0xQVXptZGVjRUh3eEMxUEU4MDVpUFJEMnBSYnU5UFhOYXI2SHFjdHQ0NW9QdDczV2MtVlczVzZCbEE0RDN5R0l3NnhkbE40bkJUR3FZSXpZMmVTQ0VPRHNFR3lWcW9mQ2FxTlJpQl9pZ01YTGV2RzlXNVdoVHFV?oc=5>

## CATALYSTS

### Advanced Micro Devices (AMD) Stock Fair Value Edges Higher On AI Optimism And Valuation Debate
- Summary: Advanced Micro Devices (AMD) Stock Fair Value Edges Higher On AI Optimism And Valuation Debate
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxOX1l0LWJQM0UweGdsZExDZWdodmZTNTBreS03LVp0UDE5aG0zM3QwSTA3Tk9zWTFoYjlVbzZMZGZsQV9pckhBLXZ0UUg5R3dtQlFTd2w2UlF3clZDMGw2blhaZUFXbzFuUmM0cmpCTC12UTZXYnJ4ZmxIdlR2eHFHSkZoNXhSS1hEVC1Ec0pMQ2Q1TVp2VXE5c1dhWDVRQQ?oc=5>

### Is Advanced Micro Devices (AMD) Fully Priced After Record AI Growth?
- Summary: Questioning whether AMD’s valuation reflects its AI-driven growth.
- Date: 2026-11-05 | Impact: low | Horizon: medium | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxNN1ZjcDRNUjdDUkxUMDRadUlJckxJZ0RNVW9ZWnZRNHNhQm5qZU9qdEFJQ1dKZmJFMk1GMy14TGpmZWRHcEJETnFwZVJHcE1lWG5lV21Za2s4aVc2Nm9ZSjdiN1lLZFFaR2xHWGtBQUF4Vkt1X2Y2VV9qWXp5MWx3dm15MEJXazZPQXNHRm9DVXNlU3h6S0dxQlBER29qUQ?oc=5>

### AMD Stock Guided for 80% Growth Next Year. Why Isn’t the Market Impressed?
- Summary: AMD forecasts 80% growth next year, sparking market curiosity.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxPeDc1VTVKZVNIem9oYUVEQTdhM1NUT3d2Q25QMmJxVkVlbFNYNF9aWTVxdnZydHI4a2R3VUNGUlFNeTFDV2FsSnU5QkpiTkpZMFRXNWNiUElhQWJGNGE4Z3dKRFhsV2tlZUVFaGQwRE5FODE4VnNrVXRVX1JIOXBjeEJpd1QtbE8xUGRTTng3b0lmZmpRbU5jLUdGNnpvZEc4TmRRRTd6c25oSDZsX0ZqWVRJVnE?oc=5>

### Oppenheimer lifts AMD to Outperform, sees data center sales more than doubling
- Summary: Analyst upgrade to Outperform, forecasts data center sales to more than double.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxOcUhWZTduUS1BUGpNZzFCOVotLVVnSnFEa2JkTFc3VGFhdWVLWUtTOEM5MGFhVnJ5cFlkYzRqX0xGN1ExUzVoTV9tN0lJaXRIVTVjNmpmSDNfbTFydWxTN0d2LU40SnNHR3VWZnZ5aTBwcTdLWHl4WjE1SXRpempYZG9Vcnhqb1NmeDJJWmFEZl9nekViWF9FWnZHQzUzdkVjZUV4aA?oc=5>

### AMD stock today surges 12% after Oppenheimer upgrades Advanced Micro Devices, while Nvidia slides amid boa
- Summary: Oppenheimer upgrade triggers 12% surge in AMD shares.
- Date: 2026-11-09 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiqwJBVV95cUxOT0J5VldKa1YwcjhxRVRVby03N21NQjZIODltalA3cXphYmR6VmVLYnBsdmhfX2pCTVhPcjkxSnV5MkR2cEMyMGNfcmg1UU5hbzJabnJ0dWg3TWtBM29FRGVNN1ZwQTkzRURQUDhCM0NkVDJPejJKMmhQcGtNak5UaWFlRkxFdlhpOVdfQ1ZLQnR2MTBBTkVXaEZ2Z1h3bGtWZFN2R3FtT0pzQTc0LXM5T0YxUnNSaHhPQlBURWNPbHk5aEFfZWt2MDVxc3g5NzY0Z2ZuNjBkak5mN0Z4VkNDLWpWUVFLbEstZDI1QW5XMGtXcVVCZngycVZTbnQ1WVpvZ3gwRlZ2Wjk2VWgydEFWRVdqY2RwR1Y3ZFFYUVJSUVlnWU1wanAzTW1YWdIBsAJBVV95cUxPYlhnaHRFQTdsY0JKdll3YjFmWUE3VXpWaXd1QWVCUGEzXy1ZeDdCUF8teDJVVkZUcHBIZkNzWVVVUlp0amJ2YVBhSmUzV004WVBXNHh0ZWNZaEFvUk9IVmxDNks5ZW1SaEFXS21MdkYtdklBaWlqOVJCbjBrQThJQU5fdFpaQ2k1TFdtektYMUtRZnh6SVE4V1lhMzdvRHctMlYxaXFranVJMmk5OUhwLTFUSE4tU1JUYzhvaW1EOVV3Q0xUbDJNVkszZ3ZEQTF5ZWJJZDFSVmxsa1RMMVdyVUQwdGxyOElYOVBsVzBVeURhZER2RWJGdWt2SlBES3NmX2lxNkcxWHF1cXpxOVIySWt6MnRXQjZtMUJWSjJMRklKd2s4WmJxc1VrT3NzWGlK?oc=5>

### AMD: I'm Buying The Dip Again (NASDAQ:AMD)
- Summary: AMD announces purchase of its own shares to support the stock.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMid0FVX3lxTE15VEpYVldrWVhqanZDbkhNWGllNl9rYk9SeVkzUDdKdC14R2k3VVFGNTRhM3NROTVJUjlwb25iQU9XTGJnRjc0Ny1SeDlPWVM0dnNFbzZTWU0tdWdIT1pYZ2FQOHVvSnNsV1pMcVk1Rl90UUVoTTVZ?oc=5>

## RISKS

### Something Doesn't Add Up With AMD (NASDAQ:AMD)
- Summary: Analysis questions AMD's performance consistency.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMifkFVX3lxTE5ZdDNOZklySDFyVWtwWGxfbW9tSzFNNjhnTDdUVFdwcVFlQ3JTTHhBWWRLR3d4bjBIR09JV1NGckxFb1BvTnc1YXVuWC1Rb0RfQ3RybXNYVVVkR2Y5M3hQek9ZMENpXzQ4dDJ1cVdvU2ZSN05pVXV0OUtwOURNUQ?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AMD** | **108.67** | **12.20** | **74.27** | **44.70** | **834,115,600,384.00 USD** | **117.77** |
| NVDA | 22.59 | 18.84 | 21.28 | 105.90 | 4,314,344,194,048.00 USD | -4.81 |
| INTC | N/A | 2.74 | 17.16 | 20.90 | 315,551,547,392.00 USD | 55.70 |
| AVGO | 40.80 | 15.30 | 29.86 | 85.50 | 1,525,079,343,104.00 USD | -7.89 |

Peers fetched as_of: 2026-11-09; AMD reuses existing data (market data as_of: 2026-11-09); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-03
- Next expected earnings: 2027-02-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-09

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-11-04
- Revenue (latest available single quarter): 1,584,000,000.00 USD; period 2017-07-02/2017-09-30; fiscal year/reporting period 2018/Q3
- Net income (latest available single quarter): 2,428,000,000.00 USD; period 2026-06-28/2026-09-26; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/2488/000000248826000191/amd-20260926.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiowFBVV95cUxNbWlsWGwzaEFUQkppQnFleUFqeldtRmJNaVctS3luSE5XS0QyZUVPTi1rMkM2T29HMG9EWVBvTDB4cDN0dlpQX2JWZG9DdGl3blRuNEJJb1diS2k3bFlubzg5OWdqLTREZHgzWUl5eWtpQU55TFpaanJkS0Y1UG1tR1BQUmxzeDUwWHY1RWFUZlU0Z0RxMktwOS01cHBOTmRIcTdF?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxOSGNhdHRDWVJTZ3hNZFVuTHlPdXdqSGZZcDRJNnZoQlJ2MWsydWNibVowMkRkNDltWEdjN3pmUlRBNHBkTGdJS1EwVVRObjVNcFBHLXFOWDhIeFR4WlR5bUV1ZVJDM3lCRWNCdTZtYXZHOE9tVDU4RWJEYnI1Wk5Tc0J3QktsVHFVNmt4NklPSEFTOC1RaTNsbkliYXM5T2w5LXd3RDUyTTRwU21NVWhpV1NtQ2QyM09YWm9IZlZxTWo2eU9xZEE?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxNc0pob1FQZVItVXBmSHRhb1kzQkg0T3ZaR1FlT3hqQ3NEUEpPUDZoN19qTHRHZ1R4UHN2dUI3MEg4OVRITGNxc3V3WjRNZTJpQndZbm1SY2J1Wm1SRGZWRVRkQm5HaGZhWlBhbG15dHdYaWc5cUdYZjN5QjBjWk5kVlhDZ0N6WlJzbEdfWUU3QU1FaFhraTVUNzBORFVhOVRG?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxPblVKQTdzS3pVSWRRMHp0SUhjTnFPWFl6bWRMS1QtcVBleURPeGlRMlBsejNVYnBYQlVPMnp2bE94aUFybFVPSlZfbzQzV0RwQWRnc0p4LU5jeFB4MTZRRWIzbGJ3Z25kY2M5Q3V6WUMzNHQ4MmY1R0JVS2djMUR2V3ItQ2ZuTE5leGVkTW5YcXljLUpvTGsxYU5PQWI1OXhvVFI5MHQyRGpPaGRjdEhoelBYa3dQdw?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxQMUVCMkhJekg0eE5fVEVhaXlCNEdqUHgxZHB6SlRQSmxYNGxUTzBfajFpLVQ2c1hpc0V6RVFiQnc5Q05OaGR2cVdGVzg1MUlUcFQ1NWlSTTFKbDhrWlJadDZ5dlVlYXQ0ZFpoWjRtNnRnY3lWQ0RPVGNHWmRMbEt5d29FVkFGSkFsV2tweGQ1LUJ5YXFCS29qUg?oc=5
- https://news.google.com/rss/articles/CBMieEFVX3lxTE01cm9PLTQxUjBBdmFmTEk1LURPcWJyRUVqRWtQakFWVDlDbkt1cHE1SHZla3NBS3ZqYkdBRFFqclhqY2FjYjRzTXlRTlFlVy1kb0JqRVFyVVI4V2FQMTNxdzA3eDc5dk5OWjkycWQxVnV1a3FGWWpYNA?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxOLTJJcVJGQUh6QzJQOEF0WnNKb09adzIwUDAyQWR5emxKZjNaMmZmTFhkTmJiOUFiQnMtc3hucWpRQksxX3FCQzdtSm1ablVJUzhRYjkwd0VvdVRRR2h2VUdVd0JJVTA5dGdUWmM4WHRqTER0WHl2aFRQcWxRM05hRk1oSUNmZDVmd1hBaGZfbU44ODBNdWc?oc=5
- https://news.google.com/rss/articles/CBMi5AFBVV95cUxQM2lSUmJqV2lOZUhtVVBfd2pWSmllT0Q0SlYwdkkyUFFINU8zMWNKc2dTM0lOMmgxbEVXYWJ2SnVnTnN4T0U5aXVPbFVwU0xreEphclFTT1psSDRuYWVTTjVqUnlCZnFxdnVPRF9Wd1NwWlpNM05KZ3BVb2dKSTZsM2FtN2JZNW5qcDZZVnluWkxuMHByM3ppTGg1QTZ1dGpvLXlhT0pERkZCV2xmYUQ0NzdsMk9mWC1sZnhxNzFTZks0ZVlWZlBZSWxMVlpqMDhMTGlUc3A5Q2xHWmFKZ21PV3JPNVY?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxOeEpRMjVrSzZYZENMSFgxdHVucTIxajJzb0xQVXptZGVjRUh3eEMxUEU4MDVpUFJEMnBSYnU5UFhOYXI2SHFjdHQ0NW9QdDczV2MtVlczVzZCbEE0RDN5R0l3NnhkbE40bkJUR3FZSXpZMmVTQ0VPRHNFR3lWcW9mQ2FxTlJpQl9pZ01YTGV2RzlXNVdoVHFV?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxOX1l0LWJQM0UweGdsZExDZWdodmZTNTBreS03LVp0UDE5aG0zM3QwSTA3Tk9zWTFoYjlVbzZMZGZsQV9pckhBLXZ0UUg5R3dtQlFTd2w2UlF3clZDMGw2blhaZUFXbzFuUmM0cmpCTC12UTZXYnJ4ZmxIdlR2eHFHSkZoNXhSS1hEVC1Ec0pMQ2Q1TVp2VXE5c1dhWDVRQQ?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxNN1ZjcDRNUjdDUkxUMDRadUlJckxJZ0RNVW9ZWnZRNHNhQm5qZU9qdEFJQ1dKZmJFMk1GMy14TGpmZWRHcEJETnFwZVJHcE1lWG5lV21Za2s4aVc2Nm9ZSjdiN1lLZFFaR2xHWGtBQUF4Vkt1X2Y2VV9qWXp5MWx3dm15MEJXazZPQXNHRm9DVXNlU3h6S0dxQlBER29qUQ?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxPeDc1VTVKZVNIem9oYUVEQTdhM1NUT3d2Q25QMmJxVkVlbFNYNF9aWTVxdnZydHI4a2R3VUNGUlFNeTFDV2FsSnU5QkpiTkpZMFRXNWNiUElhQWJGNGE4Z3dKRFhsV2tlZUVFaGQwRE5FODE4VnNrVXRVX1JIOXBjeEJpd1QtbE8xUGRTTng3b0lmZmpRbU5jLUdGNnpvZEc4TmRRRTd6c25oSDZsX0ZqWVRJVnE?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxOcUhWZTduUS1BUGpNZzFCOVotLVVnSnFEa2JkTFc3VGFhdWVLWUtTOEM5MGFhVnJ5cFlkYzRqX0xGN1ExUzVoTV9tN0lJaXRIVTVjNmpmSDNfbTFydWxTN0d2LU40SnNHR3VWZnZ5aTBwcTdLWHl4WjE1SXRpempYZG9Vcnhqb1NmeDJJWmFEZl9nekViWF9FWnZHQzUzdkVjZUV4aA?oc=5
- https://news.google.com/rss/articles/CBMiqwJBVV95cUxOT0J5VldKa1YwcjhxRVRVby03N21NQjZIODltalA3cXphYmR6VmVLYnBsdmhfX2pCTVhPcjkxSnV5MkR2cEMyMGNfcmg1UU5hbzJabnJ0dWg3TWtBM29FRGVNN1ZwQTkzRURQUDhCM0NkVDJPejJKMmhQcGtNak5UaWFlRkxFdlhpOVdfQ1ZLQnR2MTBBTkVXaEZ2Z1h3bGtWZFN2R3FtT0pzQTc0LXM5T0YxUnNSaHhPQlBURWNPbHk5aEFfZWt2MDVxc3g5NzY0Z2ZuNjBkak5mN0Z4VkNDLWpWUVFLbEstZDI1QW5XMGtXcVVCZngycVZTbnQ1WVpvZ3gwRlZ2Wjk2VWgydEFWRVdqY2RwR1Y3ZFFYUVJSUVlnWU1wanAzTW1YWdIBsAJBVV95cUxPYlhnaHRFQTdsY0JKdll3YjFmWUE3VXpWaXd1QWVCUGEzXy1ZeDdCUF8teDJVVkZUcHBIZkNzWVVVUlp0amJ2YVBhSmUzV004WVBXNHh0ZWNZaEFvUk9IVmxDNks5ZW1SaEFXS21MdkYtdklBaWlqOVJCbjBrQThJQU5fdFpaQ2k1TFdtektYMUtRZnh6SVE4V1lhMzdvRHctMlYxaXFranVJMmk5OUhwLTFUSE4tU1JUYzhvaW1EOVV3Q0xUbDJNVkszZ3ZEQTF5ZWJJZDFSVmxsa1RMMVdyVUQwdGxyOElYOVBsVzBVeURhZER2RWJGdWt2SlBES3NmX2lxNkcxWHF1cXpxOVIySWt6MnRXQjZtMUJWSjJMRklKd2s4WmJxc1VrT3NzWGlK?oc=5
- https://news.google.com/rss/articles/CBMid0FVX3lxTE15VEpYVldrWVhqanZDbkhNWGllNl9rYk9SeVkzUDdKdC14R2k3VVFGNTRhM3NROTVJUjlwb25iQU9XTGJnRjc0Ny1SeDlPWVM0dnNFbzZTWU0tdWdIT1pYZ2FQOHVvSnNsV1pMcVk1Rl90UUVoTTVZ?oc=5
- https://news.google.com/rss/articles/CBMifkFVX3lxTE5ZdDNOZklySDFyVWtwWGxfbW9tSzFNNjhnTDdUVFdwcVFlQ3JTTHhBWWRLR3d4bjBIR09JV1NGckxFb1BvTnc1YXVuWC1Rb0RfQ3RybXNYVVVkR2Y5M3hQek9ZMENpXzQ4dDJ1cVdvU2ZSN05pVXV0OUtwOURNUQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
