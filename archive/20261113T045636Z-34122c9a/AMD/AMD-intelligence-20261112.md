# AMD Intelligence Report

- ticker: **AMD**
- Report as_of: **2026-11-12**
- Market data as_of: **2026-11-12**
- Quant sources: https://finance.yahoo.com/quote/AMD/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AMD/key-statistics/
- AI analysis snapshot as_of: **2026-11-12**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-13T05:03:31.665998+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 6, 'ai': 16, 'unknown': 0, 'irrelevant': 3})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **1** exact headline/source/date matches; prior report **20261112T054014Z-6c47e7f9/AMD** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **4**; {'directional_claim_without_event_type': 1, 'low_uncalibrated_model_confidence': 3}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 20 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 16.0%; oldest publication 2026-11-09

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 585.3000 |
| Return 1D (%) | 5.8600 |
| Return 1W (%) | 44.7329 |
| Return 1M (%) | -1.5044 |
| Return YTD (%) | 173.3003 |
| Return 1Y (%) | 126.0806 |
| Annualized volatility (%) | 72.9889 |
| Beta vs SPY | 3.4203 |
| Max drawdown (%) | -37.7290 |
| Sharpe (rf=0) | 1.4869 |
| Downside deviation (rf=0, %) | 47.1284 |
| Sortino (rf=0) | 2.3028 |
| Historical VaR 95% (1D, %) | 6.3184 |
| Historical ES 95% (1D, %) | 9.4746 |
| Correlation vs SPY | 0.6436 |
| Tracking error vs SPY (%) | 65.0042 |
| P/E (trailing) | 125.06 |
| P/B | 14.04 |
| EV/EBITDA | 85.56 |
| Revenue growth (%) | 44.70 |
| Forward P/E (estimate) | 33.09 |
| Gross margin (%) | 56.00 |
| Operating margin (%) | 17.82 |
| Return on equity (%) | 11.96 |
| Free cash flow yield (%) | 0.77 |
| MA50 | 552.9942 |
| Close vs MA50 (%) | 5.8420 |
| MA200 | 421.7086 |
| Close vs MA200 (%) | 38.7925 |
| RSI (14, Wilder) | 57.4801 |
| MACD (12,26) | -10.1997 |
| MACD signal (9) | -17.7827 |
| MACD histogram | 7.5830 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AMD': 281, 'SPY': 281}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 585.3000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 5.8600 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 44.7329 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -1.5044 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 173.3003 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 126.0806 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 72.9889 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 47.1284 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 2.3028 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 6.3184 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 9.4746 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.6436 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 65.0042 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 3.4203 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -37.7290 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.4869 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 33.0852 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 56.0000 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 17.8210 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 11.9600 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 0.7664 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 125.0641 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 57.4801 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 7.5830 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 5.8420 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 38.7925 -> Clearly above the moving-average trend level.

## TAILWINDS

### AMD Stock Rallies as Jensen Huang Leaves Nvidia - Advanced Micro Devices (NASDAQ:AMD)
- Summary: AMD Stock Rallies as Jensen Huang Leaves Nvidia - Advanced Micro Devices (NASDAQ:AMD)
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxQcmxESl9XeVB0ZHFqWVpNX0RyZlhIMDV2aE1EQ043SUN1MVpQUFpvRzB3MGRNUFZENEhwUmpjOXZMVlZudTNMSGpLWVpoRmhVTl9fU3JYM0tpSFdxa0xZTHdzcWNHdWlFbi13cnREVC1TN3lyM2VJcDI0QlRaSDExbFdxU0pqNkc5RlVXR1lPMXFXTFpPMzhWZjk0dmxmSkxfRFZuY28zYzIxUk1NcnpNbHluVGxXcmVF?oc=5>

### Advanced Micro Devices (NASDAQ:AMD) Stock Price Up 5.9% Following Analyst Upgrade
- Summary: Advanced Micro Devices (NASDAQ:AMD) Stock Price Up 5.9% Following Analyst Upgrade
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0wFBVV95cUxQRmR2dDdxbEc2b2lBT2lGb3pJbk9XZVZ3YzZvc1hoWmpreEtJNmZOcmtfYkI3MmdZUkZyQjBBdjV2a2FXSDhOalRPS0JyT1RiUnc0WHVmbGFxNVV5SDdBSkpmS0g1R2poU3JQWklZQlNNOE5kekljT0xMaFRmUnliMW5qak1ULW9lVE44d3NLamo0U09PcTZXN25yZEtmLUJXYkVZODItWU5lOWpQbXYyXzVDVTVMTmhwY29JUXFwS3BMamt5emphdFhxNFltZFhIdVQ0?oc=5>

### AMD Stock Gets Upgrade. What It Says About the Future of the AI Trade. -- Barrons.com
- Summary: AMD Stock Gets Upgrade. What It Says About the Future of the AI Trade. -- Barrons.com
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxQbFdwblpVLThWUTFCaGZSNFY2c1ZOMGlEdkJUakdnM1BKQlF0WUdHOE5uLVgzd0ZjdVl3UUJWWTc5UHZNTnFyVWItVGlsRkhUTG1scjFXTG1aQ2g2RHotb2dhQUZPVWFfbDZMc3lRZEhSSGhBczI2SDAzNkg4WjRDbHRrdEFDVVJ3WE9mc3hlWWJzRnZ4WDBxSE1NTQ?oc=5>

### AMD Stock Rises On Google Cloud Deal, Wall Street Upgrade
- Summary: AMD Stock Rises On Google Cloud Deal, Wall Street Upgrade
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxNc0pob1FQZVItVXBmSHRhb1kzQkg0T3ZaR1FlT3hqQ3NEUEpPUDZoN19qTHRHZ1R4UHN2dUI3MEg4OVRITGNxc3V3WjRNZTJpQndZbm1SY2J1Wm1SRGZWRVRkQm5HaGZhWlBhbG15dHdYaWc5cUdYZjN5QjBjWk5kVlhDZ0N6WlJzbEdfWUU3QU1FaFhraTVUNzBORFVhOVRG?oc=5>

### Lisa Su Just Delivered Fantastic News for AMD Investors
- Summary: Lisa Su announced positive developments for AMD, boosting investor confidence.
- Date: 2026-11-11 | Impact: high | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxPT2R4dElOVkdNdkU0X3NMQ19nbHVUM1FfNnVnYWRfSGhUY3FWaW0wVFlaQWZlVXVkYU05UWpfekozZWxZaDYzdHc5XzdFdTVmaF9KRklKRHh0UE9mLXhKbXVKQkZsMWo2OGtxai13a0RUaU1MR3hrb1RIUEd2TUc4Mlc1QTZuVmMwaXdZX1dxMUdlaG8tS0hNbUhiNV9JQQ?oc=5>

### Why Are Advanced Micro Devices (AMD) Shares Drawing Fresh AI Attention?
- Summary: AI focus boosts AMD shares, signaling growth potential.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxOeXF3anFkTFY3eHhpbjR3MlQzWFJJUS1PSXJ4VlpJREgzc2FSLWhMS1Z6YjUxbUQ1MDA1aXpJTFM0SkstQlNidnhHaTFmRFlLdjFJZHhhbjQzWFg5Ul80SnEtMlBmNzNtVjRRbllEOV9DbnRZNW9FaEdZQ3hNb2ozX0RvbDBqdGMzOHRSTGN0QUlWY2hrQ01kMDlNaw?oc=5>

### AMD and Broadcom Stock Get a Boost From Nvidia’s Loss
- Summary: Competitor loss lifts AMD and Broadcom stocks.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiggFBVV95cUxOMGJPR1pTTlRRSUZBTFNIZTZCd1JYRHltdEx2N2F3OVpvRzRDbFZ2UWlhR01SLWZadTlKNnRjbi1sQU5RazZKaDdReWZmdHhqOEVuemFRTlQ3dWk5SUt2RnMtTU1CcTlDbGctMWZGLUhNREtPNXNnZXNNRUJwQkpMQTVB?oc=5>

### Why AMD Shares Are Surging and What a $10,000 Investment in the Stock Could Be Worth in 3 Years
- Summary: Share surge suggests strong future returns over 3 years.
- Date: 2026-11-12 | Impact: high | Horizon: long | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi1wFBVV95cUxObzh5UGl4cjhpRTFJdGJCa3h6NlFER25XZE9FeXVrRFA2dW9QZ3B1MkZBN0NEYTU4d2lJRmF2Q1FobHJuVDZlbzJJT2dGQjJOT0M2STF1NDNhaElxS1JQSURMMFFBVXlRdFhwNDJJVFEzNUhibnRTcjA4c0F6WGNSbUZ5bEJNUnp0dnd1YmdzUUxSbDY4Y1JJNXB6ZUw3amQ0WklsVWtTbEJwQUFjd1A0Ukc5ZU5qZ1l4cHhBSjF0RzBPRnZldXhDUkNlZzRMQ0I1Rkp3azlPOA?oc=5>

### Bank of America Revamps AMD Stock Price Target for 2027
- Summary: Revised price target reflects updated outlook.
- Date: 2026-11-12 | Impact: medium | Horizon: long | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxQTlIyR0htNHdHYTZrN01BNGhIVUpXWlFoeUNxdjNXT3ZnM0NtVF9fT3JlOGRLdTN3UnoyTFExVm9WR19IWjFfeTlxZkJWRm0wdUt2SXlvTmxfU1lPOGNqM0dxOHVBdjM0d3JHNVd2RWdEbkNhUXdfZE9tRUVqdGJvOXFOalY4NEQ0d3Z1VHFBUERNZ1hGempiV0xpSEUzazhkY2g4RVlDOEVvWGpmemo0Nm1oSDYzZw?oc=5>

### AMD Stock Is a Buy on the Pullback. Why Its AI Growth Story Still Has Room to Run.
- Summary: Buy recommendation amid AI growth prospects.
- Date: 2026-11-12 | Impact: high | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxQNlpKUmRHV0x3UExHZEE3NVdSTld1bnROU1lMTlRVTHJFWjVSRHBKZndPaGpPc1JPMmtnd3ROWDhLaUtYREhDdzVBazdTbkVoX01ZSGVtN0lpdExJSmZQY2Z3SnhwenJ3Y3RrbmxTYXJmZ1hrNUJkWk41ZTlfSEtvNDM0Q0Q0VHUyZFpyRGREeGRGYWVua1dDZW56WFlQTTR5dldrMU5oZVJsZUFaNDNoaFpMMXBaNkZGa3BDMHM0T1Fydw?oc=5>

### Nvidia Turmoil Lifts AMD, Broadcom on Bets for Business Gains
- Summary: AMD benefits from Nvidia turmoil, boosting its business prospects.
- Date: 2026-11-12 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxQOVNuY1hQVVBKWnpYYldPbW1yYm9Nc3lhMGhyM1E0aTE2ektOem82UkdWZWtQclFUem41QWFpLUZXRnNWQV9YT2J4eUNrZ0Y2Z1JBajBYTlJmWjBHSXBVVFIyNC1jX2FiTnNIenZjSlNQX1lvb1JxVjQtMTZ4TG1BZTc4X3BJTk5SeWpibEwzeWM0VF9rSEs3SHpLcXpYckJmQ0Q4RXN1REVuNDhUS09xYg?oc=5>

### Great News for Nvidia, Micron, Broadcom, and AMD Stock Investors -- Wall Street Made a Mistake
- Summary: Positive market sentiment for AMD stock investors.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxOTl9udEduTFVUMjNKV25nY3F6QUwtRjBiMlpoMnZEUFo5dWlhc1RPNUw2SWNzd0Jzay1CY2tGUlpQSmVGbjBtMjliUnR3R2ZaVTRiSUFPNnZVdEwyNVRYWnExXzhpTk9zZ0NhV3A2aWU1SFlDc3ltaVFlTlpDUlJMRXhoRUhKNHRNTnMwVHhfRksyV2NWZVpFaVJPV0laYkhJUEE?oc=5>

### Why Advanced Micro Devices Stock Popped Today
- Summary: AMD stock experienced a positive price jump today.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxOMWRENGltcGVObDltYWVFeE1hN3NRdXZTNG5LQ29zTHlhQV9WRGsyTWI2SE92VjlFcl9pZkdjQzhSVjl4dFBfNVRWakIycmgxU0hqSGlyNVhtZzlyS2FNa2EyVDljamk1Nk9GbjhZWGI3TjROamJ1WWJSVFNFWjI1MWZqazBFd3NvM0VJU2k4ZTUxaV9XYXNRcVlNYVJ3Zw?oc=5>

### AMD: The Story Is Getting Better And Better
- Summary: Positive outlook on AMD’s performance.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMiigFBVV95cUxOaWJVbkFNSnJYU29BN0M0WkNKUjRzRC1HY0NPQ2FBMlpjR2VfQ2ppcy1zaHlQZlJoX2JoWC02V1R6dkFJOW5vYmRUVW5DSUtzYmtvQXZidEROellnM3VLQW80TUFKWEYwVFN4QnI1QkR5WEZhZkdBSy12X0dleHUtYTBfNHhxT2Jpbnc?oc=5>

### Stock Market Today, Nov. 12: AMD Jumps 5.9% on Bank of America Price Target Hike to $700
- Summary: Price target hike boosts AMD shares.
- Date: 2026-11-12 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi_wFBVV95cUxOY05oeV95cmVQSmtQV0pINnFDNHJhMnQzZGFMZzBoeDNYZm9YYXhwVmV4eUh1ZGNKMnlCTVM1VFJPZkpRZ1gwV2JWTllkd1Z2TFVLNElScUpWdmtyZEdfRWNHU3hzeFZmZWtXNWZhMGs2UW9XNzVsOUl1NU1Fd3Z2eWRBMFc3YTc3ZFRFV3E4ckZhQlBwY0JRUnlGRVhjd0w2RkJULUthdmZ3U011RFlrMXk3TVN4Z3NFS3pwS1U3ZDNhcVhUeFA4ek4wRUtJX3FVRUs4RV9YZVNaZGI0Wml6cUtPTmJIZ2wzZ3dybjUzdEc4ZGhCRGZabzB2YkhHT0E?oc=5>

### Analysts Back AMD Stock Amid Nvidia CEO Scandal
- Summary: Analyst support amid competitor scandal.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiqgFBVV95cUxNSGpfWUhXNXJqUUJyM2dJd1ZRTVM2a05kak9Va2txRVhwWGRQU2RqdmppOXl4ZDJlQmQ3ODBnMmYyRjRmT0dkM05EOHBZYWN5eXg2eDVxVDNGdVZOT05tT180UFdhRVpnVjJJQVdpZS1IVnh4NkNGVFVoZG5PNUQ5T3MtSGdMai1CV1FIWmIxMElYLWtKbUphTEs0Wk1JQzU1SGFjcGw2NmFTUQ?oc=5>

### AMD is Trading at a Premium at 38.39X P/E: Is the Stock Still a Buy?
- Summary: Questioning AMD’s valuation at premium P/E.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMivwFBVV95cUxOVmh4UVRhYmFtUUZfMkN4OFU5RnQybllLVkFiMGgzbUl5RnVnWGh0MEg0dVUxQTBhZE9DTElwUS1nRVA5UHRRVHRUMElMMHMydXRxNkJnOVpRU3B5dVhpTzVXS1lsRFhmeVhnNURwaXZESk1BUk91T1h2TzNxal9Yb2p2S1UyNkwzOTFrZ2NhS0VGRFZVbnBDNDFUNWRtUEQzdlVTaEN5MkNDNGZLUnpFQURkU0FPN3B5WWNNbkpidw?oc=5>

## HEADWINDS

### AMD Swung 17% Down and Back in One Week: Take Profits, or Buy More?
- Summary: AMD's share price volatility may deter investors.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxNRjJGdmlaWU15d0JtaFBXR1d1bWYtYlVPdDdtZTgxSjFrM1U4aHk3WlU0YzJoUVBmMElVUzVSQmF4cDAyNFlZWnNZNkhtM1NDbTZ1U1ZrVDBhQ3c0LXM4dUVQQVR0ZVdVRVRYaW40WUY1T3h4VnhXWW5UaFBtQ0M2VmIzdFRnMHJONGxicHQxMmlHUFZt?oc=5>

### AMD’s stock fades as investors weigh whether Nvidia’s turmoil will mean lasting wins
- Summary: Investors question if Nvidia issues benefit AMD, causing AMD shares to decline.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxQRjNQX1Ntbk1OMGFrQnRHTDh1S291MHRKa2ZIR3RrQUJHT2U1QVZQMC1kSUdOVmgwNVBwNlVlS0x3dUs2SHYyRzltRThVVTltNmVCcm1fTnNob1BTbEkzWWRjeDJCbi1BbDV0ZWoyUFA1Z1ZWSW5CN3VVSU5tX3o1cWYzSi14T2lVQ0FOWnRUejhvNm04aU8wV2VwZ3lnUVV4aUNCM2oxOWFJTExEM1BlWXZhSTQ5X3RqMlVYMHF0ZjhoYW8?oc=5>

## CATALYSTS

### AMD stock jumps 13% after 5-star analyst resets price target
- Summary: AMD stock jumps 13% after 5-star analyst resets price target
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxPYlRIejllVjJBT1VWTzZjVFRYYUtIOUJUS0kyVm02aS02YkhQWVhmM2JmcVJwaVVQbW96aUpZMEpiVnZoclhlS3lqZnF3YnA2NnRWRTQ5TEZiU1Q3eC02dVU4bXZlMXhPTWU1LUE3YWlCNUNuN01Vak5KX05hUVEyMWgyemJLdllOOGNhMTljNDlSTW4zb1Rr?oc=5>

### Advanced Micro Devices' Management Confident About CPU Revenue Doubling in 2027, RBC Says
- Summary: Advanced Micro Devices' Management Confident About CPU Revenue Doubling in 2027, RBC Says
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1wFBVV95cUxQbWx6TEdJdk96MmFJOG1RbHNhV3ZBd2ZJalhvekRkWHctTHFLcXVxODBvbVprazJWazFTem9ib0szNUstTm9Dam5jeDB0dDRVOHVTc2taamNTWnR5VjlxR2N5ZEZWNnA5amd3SkFWM0txWUtfWWt2TjhsSDBsSl9uM1ZRUGluazlCR2FsUTBCRWZ3Z1lROU5PVjRPUDd2clA3LVZkQ2IzUWd2YmY5eDViTDJiMmFuUl9pZktEM1FEWENkWndTZ2lYTlJpcEktakhzRThfME16TQ?oc=5>

### Advanced Micro Devices (AMD) Stock Jumped, What Is Driving Attention Today?
- Summary: AMD shares surged, attracting investor interest.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiiAFBVV95cUxPYXEtam5HVVFWdmhQcWFJbTdUMV93ekYxajZNQkZURnhNeGxaVXA1VVhMb2Q0eW9DakhEcTg5S2NONXNvb2x2MXJRd2xlYjZkd05MdTFJTHRxZ3V5UXc0WGE1aW9yaWo0WExWaXJJQmFQTkZkaFl3YVlwRm56QUJMdXdPWlB5ZkpM?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AMD** | **125.06** | **14.04** | **85.56** | **44.70** | **959,943,081,984.00 USD** | **126.08** |
| NVDA | 21.01 | 17.53 | 19.78 | 105.90 | 4,012,989,743,104.00 USD | -14.04 |
| INTC | N/A | 2.83 | 17.67 | 20.90 | 325,278,007,296.00 USD | 61.52 |
| AVGO | 46.53 | 17.45 | 33.96 | 85.50 | 1,739,319,803,904.00 USD | 3.34 |

Peers fetched as_of: 2026-11-12; AMD reuses existing data (market data as_of: 2026-11-12); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-03
- Next expected earnings: 2027-02-02 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-12

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
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

- https://news.google.com/rss/articles/CBMiuAFBVV95cUxQcmxESl9XeVB0ZHFqWVpNX0RyZlhIMDV2aE1EQ043SUN1MVpQUFpvRzB3MGRNUFZENEhwUmpjOXZMVlZudTNMSGpLWVpoRmhVTl9fU3JYM0tpSFdxa0xZTHdzcWNHdWlFbi13cnREVC1TN3lyM2VJcDI0QlRaSDExbFdxU0pqNkc5RlVXR1lPMXFXTFpPMzhWZjk0dmxmSkxfRFZuY28zYzIxUk1NcnpNbHluVGxXcmVF?oc=5
- https://news.google.com/rss/articles/CBMi0wFBVV95cUxQRmR2dDdxbEc2b2lBT2lGb3pJbk9XZVZ3YzZvc1hoWmpreEtJNmZOcmtfYkI3MmdZUkZyQjBBdjV2a2FXSDhOalRPS0JyT1RiUnc0WHVmbGFxNVV5SDdBSkpmS0g1R2poU3JQWklZQlNNOE5kekljT0xMaFRmUnliMW5qak1ULW9lVE44d3NLamo0U09PcTZXN25yZEtmLUJXYkVZODItWU5lOWpQbXYyXzVDVTVMTmhwY29JUXFwS3BMamt5emphdFhxNFltZFhIdVQ0?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxQbFdwblpVLThWUTFCaGZSNFY2c1ZOMGlEdkJUakdnM1BKQlF0WUdHOE5uLVgzd0ZjdVl3UUJWWTc5UHZNTnFyVWItVGlsRkhUTG1scjFXTG1aQ2g2RHotb2dhQUZPVWFfbDZMc3lRZEhSSGhBczI2SDAzNkg4WjRDbHRrdEFDVVJ3WE9mc3hlWWJzRnZ4WDBxSE1NTQ?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxNc0pob1FQZVItVXBmSHRhb1kzQkg0T3ZaR1FlT3hqQ3NEUEpPUDZoN19qTHRHZ1R4UHN2dUI3MEg4OVRITGNxc3V3WjRNZTJpQndZbm1SY2J1Wm1SRGZWRVRkQm5HaGZhWlBhbG15dHdYaWc5cUdYZjN5QjBjWk5kVlhDZ0N6WlJzbEdfWUU3QU1FaFhraTVUNzBORFVhOVRG?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxPT2R4dElOVkdNdkU0X3NMQ19nbHVUM1FfNnVnYWRfSGhUY3FWaW0wVFlaQWZlVXVkYU05UWpfekozZWxZaDYzdHc5XzdFdTVmaF9KRklKRHh0UE9mLXhKbXVKQkZsMWo2OGtxai13a0RUaU1MR3hrb1RIUEd2TUc4Mlc1QTZuVmMwaXdZX1dxMUdlaG8tS0hNbUhiNV9JQQ?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxOeXF3anFkTFY3eHhpbjR3MlQzWFJJUS1PSXJ4VlpJREgzc2FSLWhMS1Z6YjUxbUQ1MDA1aXpJTFM0SkstQlNidnhHaTFmRFlLdjFJZHhhbjQzWFg5Ul80SnEtMlBmNzNtVjRRbllEOV9DbnRZNW9FaEdZQ3hNb2ozX0RvbDBqdGMzOHRSTGN0QUlWY2hrQ01kMDlNaw?oc=5
- https://news.google.com/rss/articles/CBMiggFBVV95cUxOMGJPR1pTTlRRSUZBTFNIZTZCd1JYRHltdEx2N2F3OVpvRzRDbFZ2UWlhR01SLWZadTlKNnRjbi1sQU5RazZKaDdReWZmdHhqOEVuemFRTlQ3dWk5SUt2RnMtTU1CcTlDbGctMWZGLUhNREtPNXNnZXNNRUJwQkpMQTVB?oc=5
- https://news.google.com/rss/articles/CBMi1wFBVV95cUxObzh5UGl4cjhpRTFJdGJCa3h6NlFER25XZE9FeXVrRFA2dW9QZ3B1MkZBN0NEYTU4d2lJRmF2Q1FobHJuVDZlbzJJT2dGQjJOT0M2STF1NDNhaElxS1JQSURMMFFBVXlRdFhwNDJJVFEzNUhibnRTcjA4c0F6WGNSbUZ5bEJNUnp0dnd1YmdzUUxSbDY4Y1JJNXB6ZUw3amQ0WklsVWtTbEJwQUFjd1A0Ukc5ZU5qZ1l4cHhBSjF0RzBPRnZldXhDUkNlZzRMQ0I1Rkp3azlPOA?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxQTlIyR0htNHdHYTZrN01BNGhIVUpXWlFoeUNxdjNXT3ZnM0NtVF9fT3JlOGRLdTN3UnoyTFExVm9WR19IWjFfeTlxZkJWRm0wdUt2SXlvTmxfU1lPOGNqM0dxOHVBdjM0d3JHNVd2RWdEbkNhUXdfZE9tRUVqdGJvOXFOalY4NEQ0d3Z1VHFBUERNZ1hGempiV0xpSEUzazhkY2g4RVlDOEVvWGpmemo0Nm1oSDYzZw?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxQNlpKUmRHV0x3UExHZEE3NVdSTld1bnROU1lMTlRVTHJFWjVSRHBKZndPaGpPc1JPMmtnd3ROWDhLaUtYREhDdzVBazdTbkVoX01ZSGVtN0lpdExJSmZQY2Z3SnhwenJ3Y3RrbmxTYXJmZ1hrNUJkWk41ZTlfSEtvNDM0Q0Q0VHUyZFpyRGREeGRGYWVua1dDZW56WFlQTTR5dldrMU5oZVJsZUFaNDNoaFpMMXBaNkZGa3BDMHM0T1Fydw?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxQOVNuY1hQVVBKWnpYYldPbW1yYm9Nc3lhMGhyM1E0aTE2ektOem82UkdWZWtQclFUem41QWFpLUZXRnNWQV9YT2J4eUNrZ0Y2Z1JBajBYTlJmWjBHSXBVVFIyNC1jX2FiTnNIenZjSlNQX1lvb1JxVjQtMTZ4TG1BZTc4X3BJTk5SeWpibEwzeWM0VF9rSEs3SHpLcXpYckJmQ0Q4RXN1REVuNDhUS09xYg?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxOTl9udEduTFVUMjNKV25nY3F6QUwtRjBiMlpoMnZEUFo5dWlhc1RPNUw2SWNzd0Jzay1CY2tGUlpQSmVGbjBtMjliUnR3R2ZaVTRiSUFPNnZVdEwyNVRYWnExXzhpTk9zZ0NhV3A2aWU1SFlDc3ltaVFlTlpDUlJMRXhoRUhKNHRNTnMwVHhfRksyV2NWZVpFaVJPV0laYkhJUEE?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxOMWRENGltcGVObDltYWVFeE1hN3NRdXZTNG5LQ29zTHlhQV9WRGsyTWI2SE92VjlFcl9pZkdjQzhSVjl4dFBfNVRWakIycmgxU0hqSGlyNVhtZzlyS2FNa2EyVDljamk1Nk9GbjhZWGI3TjROamJ1WWJSVFNFWjI1MWZqazBFd3NvM0VJU2k4ZTUxaV9XYXNRcVlNYVJ3Zw?oc=5
- https://news.google.com/rss/articles/CBMiigFBVV95cUxOaWJVbkFNSnJYU29BN0M0WkNKUjRzRC1HY0NPQ2FBMlpjR2VfQ2ppcy1zaHlQZlJoX2JoWC02V1R6dkFJOW5vYmRUVW5DSUtzYmtvQXZidEROellnM3VLQW80TUFKWEYwVFN4QnI1QkR5WEZhZkdBSy12X0dleHUtYTBfNHhxT2Jpbnc?oc=5
- https://news.google.com/rss/articles/CBMi_wFBVV95cUxOY05oeV95cmVQSmtQV0pINnFDNHJhMnQzZGFMZzBoeDNYZm9YYXhwVmV4eUh1ZGNKMnlCTVM1VFJPZkpRZ1gwV2JWTllkd1Z2TFVLNElScUpWdmtyZEdfRWNHU3hzeFZmZWtXNWZhMGs2UW9XNzVsOUl1NU1Fd3Z2eWRBMFc3YTc3ZFRFV3E4ckZhQlBwY0JRUnlGRVhjd0w2RkJULUthdmZ3U011RFlrMXk3TVN4Z3NFS3pwS1U3ZDNhcVhUeFA4ek4wRUtJX3FVRUs4RV9YZVNaZGI0Wml6cUtPTmJIZ2wzZ3dybjUzdEc4ZGhCRGZabzB2YkhHT0E?oc=5
- https://news.google.com/rss/articles/CBMiqgFBVV95cUxNSGpfWUhXNXJqUUJyM2dJd1ZRTVM2a05kak9Va2txRVhwWGRQU2RqdmppOXl4ZDJlQmQ3ODBnMmYyRjRmT0dkM05EOHBZYWN5eXg2eDVxVDNGdVZOT05tT180UFdhRVpnVjJJQVdpZS1IVnh4NkNGVFVoZG5PNUQ5T3MtSGdMai1CV1FIWmIxMElYLWtKbUphTEs0Wk1JQzU1SGFjcGw2NmFTUQ?oc=5
- https://news.google.com/rss/articles/CBMivwFBVV95cUxOVmh4UVRhYmFtUUZfMkN4OFU5RnQybllLVkFiMGgzbUl5RnVnWGh0MEg0dVUxQTBhZE9DTElwUS1nRVA5UHRRVHRUMElMMHMydXRxNkJnOVpRU3B5dVhpTzVXS1lsRFhmeVhnNURwaXZESk1BUk91T1h2TzNxal9Yb2p2S1UyNkwzOTFrZ2NhS0VGRFZVbnBDNDFUNWRtUEQzdlVTaEN5MkNDNGZLUnpFQURkU0FPN3B5WWNNbkpidw?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxNRjJGdmlaWU15d0JtaFBXR1d1bWYtYlVPdDdtZTgxSjFrM1U4aHk3WlU0YzJoUVBmMElVUzVSQmF4cDAyNFlZWnNZNkhtM1NDbTZ1U1ZrVDBhQ3c0LXM4dUVQQVR0ZVdVRVRYaW40WUY1T3h4VnhXWW5UaFBtQ0M2VmIzdFRnMHJONGxicHQxMmlHUFZt?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxQRjNQX1Ntbk1OMGFrQnRHTDh1S291MHRKa2ZIR3RrQUJHT2U1QVZQMC1kSUdOVmgwNVBwNlVlS0x3dUs2SHYyRzltRThVVTltNmVCcm1fTnNob1BTbEkzWWRjeDJCbi1BbDV0ZWoyUFA1Z1ZWSW5CN3VVSU5tX3o1cWYzSi14T2lVQ0FOWnRUejhvNm04aU8wV2VwZ3lnUVV4aUNCM2oxOWFJTExEM1BlWXZhSTQ5X3RqMlVYMHF0ZjhoYW8?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxPYlRIejllVjJBT1VWTzZjVFRYYUtIOUJUS0kyVm02aS02YkhQWVhmM2JmcVJwaVVQbW96aUpZMEpiVnZoclhlS3lqZnF3YnA2NnRWRTQ5TEZiU1Q3eC02dVU4bXZlMXhPTWU1LUE3YWlCNUNuN01Vak5KX05hUVEyMWgyemJLdllOOGNhMTljNDlSTW4zb1Rr?oc=5
- https://news.google.com/rss/articles/CBMi1wFBVV95cUxQbWx6TEdJdk96MmFJOG1RbHNhV3ZBd2ZJalhvekRkWHctTHFLcXVxODBvbVprazJWazFTem9ib0szNUstTm9Dam5jeDB0dDRVOHVTc2taamNTWnR5VjlxR2N5ZEZWNnA5amd3SkFWM0txWUtfWWt2TjhsSDBsSl9uM1ZRUGluazlCR2FsUTBCRWZ3Z1lROU5PVjRPUDd2clA3LVZkQ2IzUWd2YmY5eDViTDJiMmFuUl9pZktEM1FEWENkWndTZ2lYTlJpcEktakhzRThfME16TQ?oc=5
- https://news.google.com/rss/articles/CBMiiAFBVV95cUxPYXEtam5HVVFWdmhQcWFJbTdUMV93ekYxajZNQkZURnhNeGxaVXA1VVhMb2Q0eW9DakhEcTg5S2NONXNvb2x2MXJRd2xlYjZkd05MdTFJTHRxZ3V5UXc0WGE1aW9yaWo0WExWaXJJQmFQTkZkaFl3YVlwRm56QUJMdXdPWlB5ZkpM?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
