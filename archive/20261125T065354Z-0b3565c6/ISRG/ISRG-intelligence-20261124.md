# ISRG Intelligence Report

- ticker: **ISRG**
- Report as_of: **2026-11-24**
- Market data as_of: **2026-11-24**
- Quant sources: https://finance.yahoo.com/quote/ISRG/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/ISRG/key-statistics/
- AI analysis snapshot as_of: **2026-11-24**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-25T07:10:49.019445+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 14, 'rule': 4, 'ai': 4, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **6** exact headline/source/date matches; prior report **20261124T081701Z-6c335e3d/ISRG** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **3**; {'directional_claim_without_event_type': 3}
- RSS source audit (metadata only, not article fact-checking): 14 unique headlines; 7 named publishers; 1 exact duplicates; 14 HTTPS source links; largest publisher share 21.43%; oldest publication 2026-11-18

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 434.4600 |
| Return 1D (%) | 4.3798 |
| Return 1W (%) | 0.9128 |
| Return 1M (%) | -3.9422 |
| Return YTD (%) | -23.2891 |
| Return 1Y (%) | -23.5751 |
| Annualized volatility (%) | 36.0355 |
| Beta vs SPY | 0.8830 |
| Max drawdown (%) | -43.9960 |
| Sharpe (rf=0) | -0.5672 |
| Downside deviation (rf=0, %) | 26.5437 |
| Sortino (rf=0) | -0.7700 |
| Historical VaR 95% (1D, %) | 3.3061 |
| Historical ES 95% (1D, %) | 5.1297 |
| Correlation vs SPY | 0.3664 |
| Tracking error vs SPY (%) | 33.5746 |
| P/E (trailing) | 52.53 |
| P/B | 9.42 |
| EV/EBITDA | 32.81 |
| Revenue growth (%) | 21.70 |
| Forward P/E (estimate) | 34.84 |
| Gross margin (%) | 66.64 |
| Operating margin (%) | 31.70 |
| Return on equity (%) | 17.93 |
| Free cash flow yield (%) | 2.28 |
| MA50 | 425.4216 |
| Close vs MA50 (%) | 2.1246 |
| MA200 | 427.0336 |
| Close vs MA200 (%) | 1.7391 |
| RSI (14, Wilder) | 51.1680 |
| MACD (12,26) | -2.8675 |
| MACD signal (9) | 1.7920 |
| MACD histogram | -4.6595 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'ISRG': 289, 'SPY': 289}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 434.4600 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 4.3798 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 0.9128 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -3.9422 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -23.2891 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -23.5751 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 36.0355 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 26.5437 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.7700 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.3061 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.1297 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.3664 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 33.5746 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.8830 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -43.9960 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.5672 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 34.8439 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 66.6420 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 31.7020 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 17.9320 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.2807 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 52.5345 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 51.1680 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -4.6595 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 2.1246 -> Slightly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 1.7391 -> Slightly above the moving-average trend level.

## TAILWINDS

### Intuitive Surgical Inc (ISRG) Shares Surge 4.3% -- What GF Score of 92 Tells Investors
- Summary: Intuitive Surgical Inc (ISRG) Shares Surge 4.3% -- What GF Score of 92 Tells Investors
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxOdXN4ZlRxR2pmaGZTNzdyTEJSb0FBQ1hFbFZRd2Vsa3NIclFGN0xweGQ0Z19sdG1TLUItSk5aQnJjWm9Cd2lfRDVoV19jUG1yYmJPclY2R2F5UUQ5WWdjOGxTTE5vVS03R1Z2TmxsRjJmc2NJRzg4WVJiOFQ2bjdGa2t4Qko2aU8xZXdwOURoblRlaUhOa24wa0VtWGcyZVZTZ2RSakRrb0puOHAyZWlDakc3bVRWWEhPZlE?oc=5>

### Intuitive Surgical (ISRG) Stock May Be Near Fair Value Despite 22% Revenue Growth
- Summary: Analysts suggest ISRG stock is close to fair value amid strong revenue growth, indicating potential upside.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxQNm5nT296UEhuUmRBTGluVElaZFFjLThLajVZcHZhRDAzV3hwZG0zakY5SWRGZVVjSFgzWl9LMWtfbHFSODFKOGw2SUZIb1ZBSEp3eWFWZE9fSGhwTGE1TVJvTEltNWtUdWJ5OTBKemlueUpxNEdxR3ZjYkxabVpUc1M1WHg3WVppcVJLLXdyRlV6VDF3N1lYVlFsRkFJQ2s?oc=5>

### Why Is Intuitive Surgical (ISRG) At The Center Of The Robotics Boom?
- Summary: ISRG positioned as a key player in the robotics boom, benefiting from industry momentum.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxPNlM1eFVHd2JZQ2taWXNjSm1tZXlCLXp2V2FYUVExcXM0UktHakxsbG1Hcng1dGNBM1pQTG4taTBxNF9ZY0t1WnVVQ2sxRXE4MmZxbllSa0NGNDUyTTlGcGwyYXNFT0d5LXhzdVg4eTVyYU1DME5yM1JBSFhMelE2R2E2U2d0emNlLUNzWkhlSHRrYWlWZUM5ZVMwTQ?oc=5>

### Why Is Intuitive Surgical (ISRG) Seeing Faster Da Vinci Adoption Worldwide?
- Summary: Rapid global adoption of Da Vinci systems boosts ISRG’s market presence and revenue prospects.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxQN0NlbWFwM3RFV194U2o2bE9kMVRjVWJCVVZQNzAzZGV0cjVwbkhsTmNpNnBzb0V0QWh6SUxkaHk3UTh3QzV5Um9CNF9ETlF5M0pVdVFCVDhCdzBYU2c4TzBINU1HUHhvOTlaNG5LRGUwSVA3bi02VkI2U1dtNV9ZVGdoUUFaM2pWbVVIRms5ZmFWT0RGMXVrZEstZkM3c0ZMVDdTc19La0FacFBGeHZINktQeHYyT1pERHRGYUNrdjZuRjhEZl9rcmptdzdsVFBRb3NlRDd30gHbAUFVX3lxTE9ONF9RTXljS08wWkFRNi1QVEJCOEM1bV9IMFZYcXVrX0lIMEdmQm9KcDVwaURPLXZxeWxpb3lCdllqWHVYcHhmYUdFcmFWRkFXem5aT3ZYcnNjQTd0OGtsUEt5TUlaeGNIWjhmM2hqTXZmdHM3VURoM3VSU291dWhqd3RpazFnV1lQZXNFenpJWUhaQnl5LVRBYXA5TzUtd2s3cWRVUVE0aUVoUVktMVNJWVR6bW5yaXo3U01ycldqTDMxNGgwOThNajg1U0FoYUhOV3k1MkVtRXBYcw?oc=5>

## HEADWINDS

### Intuitive Surgical stock falls as weak momentum weighs on price
- Summary: Intuitive Surgical stock falls as weak momentum weighs on price
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxNTGRnaXJtNDBTeWVDYkNiWWlraHJzV0ZXeGFhbUxsRGgwYmZlanh3c0pqS2oyWGpkVks4VUVEUjJOZGY5LURkeHNIZzJJTDdMckJxekUxMUZIbUZIX01aSUZaSHp6dlFRVHNOc21rTm9DaWFoLUpwd2hLVk1YeUM0Y0JoRkdhYlVTX3ljbk5FeHhaVHRvOFJXdA?oc=5>

## CATALYSTS

### Intuitive Surgical completes record share buyback: ISRG gains momentum
- Summary: Intuitive Surgical completes record share buyback: ISRG gains momentum
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxPMm5nOVNQZml2RnJNbU5SR0E4dzdaMldZcTFKQ0NydnhOb1NuRTIzZ3pEbFhSbGJNcUhSamM3a0lmZ09vLV9QSzlXR01QX01CTElYaGFTWkE0djdzMDh3LUdkeFo2UUhVRGU1NVJiUFF6WXhSdzlHcjRXc0FBSlc0ZmRRT1Q5Ri1lTUdLUTUybG1pbktPQW1IUw?oc=5>

### Intuitive Surgical rises as investors appear to lean on upbeat analyst commentary and durable procedure growth
- Summary: Intuitive Surgical rises as investors appear to lean on upbeat analyst commentary and durable procedure growth
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi2wFBVV95cUxQVDhaRlBvZXRMT1ZOUHluMGNvaVFKczBRVWl3MkdKeWdSOEJNQlBhN3MxdW9Jd2xTREJEdi1YbTNMSE90UjNBU2RTMXo3bjNiMVFvZ1NlT0xMUXRFVDlUejZkMWRHRW5WMk8tSnZrWGVFeTczY0FtbUxRQzFUSXZqYXhZNU9hbGRLbHZkV2tPWUFtT0htNlFLdTlnMGs5OURQbGxoVDZZNmZuTU9nNjUxTThrb3FxbU13MU1UYVhDNXdZNW9PRmMtTkdjbzljaVpzM0ZNYkhLRWNZazA?oc=5>

### Intuitive Surgical (ISRG) Beats In Q3 As Investors Weigh Whether The Story Still Looks Cheap
- Summary: Intuitive Surgical exceeded Q3 earnings expectations, prompting investors to reassess its valuation prospects.
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi1gFBVV95cUxPU0N2enJ1c3lrbHh0WnJzMU9hejgzanRxM01OcnI2OV9FcV9Nc3B0a29aMnAxWjd2VklnMFBvNkd1YkFvMVlpQmtHUjNXUDh2Qnp4RXphTXRjN0IyaWVPYUVvbG9WUVFaYTlIdFBNWkpmYVFhZG5JQ25HN3NVTXNMS2NLU2wxVHk0YXpQRWxRVWhyR0kzeThJSEZCNzY1Sl9qRnBLTVQyblYxRmJzWHp5U3B6SUxnVW9tWWRPYVRucTFCYndiWHRBUEVvbWdxREsxUC1jcExB0gHbAUFVX3lxTE5OWk1maUMxUnhsMkVkRWtfc0VfN09rNDNlRHFiUlZ2R0g1czNfeTZMRlZKNk5YMEhmWm5RYWxwamRqRU5fTm1ndW5LSnBsSldwMC1vRlFiYWZLLXp6NjNjcEw2OXNvNkIyTllPeEpfblRJd3pXeWxqQ3VSYktuSU92WFQ5MDRpM3pFck9mMTVqcnd4WXdxWU1qdXkxRTZ1NnNQeklCYXZGaGFhV0pJOWo3TEJTR0hYOGVDRHNBcDBvLVNEczREZm1aWFlYSl9PSVk2Wkp0eHpDOWh1MA?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **ISRG** | **52.53** | **9.42** | **32.81** | **21.70** | **150,602,825,728.00 USD** | **-23.58** |
| MDT | 23.62 | 2.45 | 14.32 | 13.70 | 122,963,525,632.00 USD | -3.76 |
| SYK | 34.51 | 5.26 | 18.05 | 7.60 | 123,374,338,048.00 USD | -11.49 |
| BSX | 18.62 | 2.50 | 13.57 | 1.40 | 63,979,749,376.00 USD | -54.98 |

Peers fetched as_of: 2026-11-24; ISRG reuses existing data (market data as_of: 2026-11-24); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-20
- Next expected earnings: 2027-01-21 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-24

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-21
- Revenue (latest available single quarter): 3,048,700,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 522,800,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1035267/000103526726000071/isrg-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiugFBVV95cUxOdXN4ZlRxR2pmaGZTNzdyTEJSb0FBQ1hFbFZRd2Vsa3NIclFGN0xweGQ0Z19sdG1TLUItSk5aQnJjWm9Cd2lfRDVoV19jUG1yYmJPclY2R2F5UUQ5WWdjOGxTTE5vVS03R1Z2TmxsRjJmc2NJRzg4WVJiOFQ2bjdGa2t4Qko2aU8xZXdwOURoblRlaUhOa24wa0VtWGcyZVZTZ2RSakRrb0puOHAyZWlDakc3bVRWWEhPZlE?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxQNm5nT296UEhuUmRBTGluVElaZFFjLThLajVZcHZhRDAzV3hwZG0zakY5SWRGZVVjSFgzWl9LMWtfbHFSODFKOGw2SUZIb1ZBSEp3eWFWZE9fSGhwTGE1TVJvTEltNWtUdWJ5OTBKemlueUpxNEdxR3ZjYkxabVpUc1M1WHg3WVppcVJLLXdyRlV6VDF3N1lYVlFsRkFJQ2s?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxPNlM1eFVHd2JZQ2taWXNjSm1tZXlCLXp2V2FYUVExcXM0UktHakxsbG1Hcng1dGNBM1pQTG4taTBxNF9ZY0t1WnVVQ2sxRXE4MmZxbllSa0NGNDUyTTlGcGwyYXNFT0d5LXhzdVg4eTVyYU1DME5yM1JBSFhMelE2R2E2U2d0emNlLUNzWkhlSHRrYWlWZUM5ZVMwTQ?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxQN0NlbWFwM3RFV194U2o2bE9kMVRjVWJCVVZQNzAzZGV0cjVwbkhsTmNpNnBzb0V0QWh6SUxkaHk3UTh3QzV5Um9CNF9ETlF5M0pVdVFCVDhCdzBYU2c4TzBINU1HUHhvOTlaNG5LRGUwSVA3bi02VkI2U1dtNV9ZVGdoUUFaM2pWbVVIRms5ZmFWT0RGMXVrZEstZkM3c0ZMVDdTc19La0FacFBGeHZINktQeHYyT1pERHRGYUNrdjZuRjhEZl9rcmptdzdsVFBRb3NlRDd30gHbAUFVX3lxTE9ONF9RTXljS08wWkFRNi1QVEJCOEM1bV9IMFZYcXVrX0lIMEdmQm9KcDVwaURPLXZxeWxpb3lCdllqWHVYcHhmYUdFcmFWRkFXem5aT3ZYcnNjQTd0OGtsUEt5TUlaeGNIWjhmM2hqTXZmdHM3VURoM3VSU291dWhqd3RpazFnV1lQZXNFenpJWUhaQnl5LVRBYXA5TzUtd2s3cWRVUVE0aUVoUVktMVNJWVR6bW5yaXo3U01ycldqTDMxNGgwOThNajg1U0FoYUhOV3k1MkVtRXBYcw?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxNTGRnaXJtNDBTeWVDYkNiWWlraHJzV0ZXeGFhbUxsRGgwYmZlanh3c0pqS2oyWGpkVks4VUVEUjJOZGY5LURkeHNIZzJJTDdMckJxekUxMUZIbUZIX01aSUZaSHp6dlFRVHNOc21rTm9DaWFoLUpwd2hLVk1YeUM0Y0JoRkdhYlVTX3ljbk5FeHhaVHRvOFJXdA?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxPMm5nOVNQZml2RnJNbU5SR0E4dzdaMldZcTFKQ0NydnhOb1NuRTIzZ3pEbFhSbGJNcUhSamM3a0lmZ09vLV9QSzlXR01QX01CTElYaGFTWkE0djdzMDh3LUdkeFo2UUhVRGU1NVJiUFF6WXhSdzlHcjRXc0FBSlc0ZmRRT1Q5Ri1lTUdLUTUybG1pbktPQW1IUw?oc=5
- https://news.google.com/rss/articles/CBMi2wFBVV95cUxQVDhaRlBvZXRMT1ZOUHluMGNvaVFKczBRVWl3MkdKeWdSOEJNQlBhN3MxdW9Jd2xTREJEdi1YbTNMSE90UjNBU2RTMXo3bjNiMVFvZ1NlT0xMUXRFVDlUejZkMWRHRW5WMk8tSnZrWGVFeTczY0FtbUxRQzFUSXZqYXhZNU9hbGRLbHZkV2tPWUFtT0htNlFLdTlnMGs5OURQbGxoVDZZNmZuTU9nNjUxTThrb3FxbU13MU1UYVhDNXdZNW9PRmMtTkdjbzljaVpzM0ZNYkhLRWNZazA?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxPU0N2enJ1c3lrbHh0WnJzMU9hejgzanRxM01OcnI2OV9FcV9Nc3B0a29aMnAxWjd2VklnMFBvNkd1YkFvMVlpQmtHUjNXUDh2Qnp4RXphTXRjN0IyaWVPYUVvbG9WUVFaYTlIdFBNWkpmYVFhZG5JQ25HN3NVTXNMS2NLU2wxVHk0YXpQRWxRVWhyR0kzeThJSEZCNzY1Sl9qRnBLTVQyblYxRmJzWHp5U3B6SUxnVW9tWWRPYVRucTFCYndiWHRBUEVvbWdxREsxUC1jcExB0gHbAUFVX3lxTE5OWk1maUMxUnhsMkVkRWtfc0VfN09rNDNlRHFiUlZ2R0g1czNfeTZMRlZKNk5YMEhmWm5RYWxwamRqRU5fTm1ndW5LSnBsSldwMC1vRlFiYWZLLXp6NjNjcEw2OXNvNkIyTllPeEpfblRJd3pXeWxqQ3VSYktuSU92WFQ5MDRpM3pFck9mMTVqcnd4WXdxWU1qdXkxRTZ1NnNQeklCYXZGaGFhV0pJOWo3TEJTR0hYOGVDRHNBcDBvLVNEczREZm1aWFlYSl9PSVk2Wkp0eHpDOWh1MA?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
