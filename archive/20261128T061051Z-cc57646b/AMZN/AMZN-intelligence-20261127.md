# AMZN Intelligence Report

- ticker: **AMZN**
- Report as_of: **2026-11-27**
- Market data as_of: **2026-11-27**
- Quant sources: https://finance.yahoo.com/quote/AMZN/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AMZN/key-statistics/
- AI analysis snapshot as_of: **2026-11-27**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-28T06:13:51.297926+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 5, 'ai': 15, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **14** exact headline/source/date matches; prior report **20261127T063646Z-c0c26981/AMZN** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **3**; {'directional_claim_without_event_type': 2, 'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 14 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 24.0%; oldest publication 2026-11-20

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 254.1200 |
| Return 1D (%) | 3.9643 |
| Return 1W (%) | 2.9576 |
| Return 1M (%) | 0.4030 |
| Return YTD (%) | 10.0944 |
| Return 1Y (%) | 10.8919 |
| Annualized volatility (%) | 34.7550 |
| Beta vs SPY | 1.2562 |
| Max drawdown (%) | -19.6419 |
| Sharpe (rf=0) | 0.4188 |
| Downside deviation (rf=0, %) | 21.4954 |
| Sortino (rf=0) | 0.6772 |
| Historical VaR 95% (1D, %) | 3.2397 |
| Historical ES 95% (1D, %) | 4.1300 |
| Correlation vs SPY | 0.5430 |
| Tracking error vs SPY (%) | 29.4384 |
| P/E (trailing) | 20.54 |
| P/B | 4.48 |
| EV/EBITDA | 15.99 |
| Revenue growth (%) | 12.10 |
| Forward P/E (estimate) | 23.26 |
| Gross margin (%) | 51.37 |
| Operating margin (%) | 13.09 |
| Return on equity (%) | 27.42 |
| Free cash flow yield (%) | -1.26 |
| MA50 | 255.1744 |
| Close vs MA50 (%) | -0.4132 |
| MA200 | 246.0313 |
| Close vs MA200 (%) | 3.2877 |
| RSI (14, Wilder) | 48.6377 |
| MACD (12,26) | -1.0129 |
| MACD signal (9) | 0.5224 |
| MACD histogram | -1.5353 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AMZN': 291, 'SPY': 291}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 254.1200 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 3.9643 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 2.9576 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 0.4030 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 10.0944 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 10.8919 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 34.7550 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 21.4954 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.6772 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.2397 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.1300 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5430 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 29.4384 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.2562 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -19.6419 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.4188 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 23.2581 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 51.3740 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 13.0870 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 27.4160 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: -1.2640 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 20.5433 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 48.6377 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -1.5353 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -0.4132 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 3.2877 -> Slightly above the moving-average trend level.

## TAILWINDS

### Amazon (NASDAQ:AMZN) Stock Jumps 4% as Thanksgiving Online Spending Hits Record $7.1 Billion
- Summary: Amazon (NASDAQ:AMZN) Stock Jumps 4% as Thanksgiving Online Spending Hits Record $7.1 Billion
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMieEFVX3lxTE52cmVhLUdXcXhuNnU2UXFEYmRzWDlxZDVHeF9majZZS1JvMzRteUN4ZEVfWng5VGtjVjBNN1dZVGFlSmtRY3hNZFkzUFdDMDllUWhnTG14cVFwWHdvSjIwczYya2I3bUhWWjM2QU9qYWhocVhSRnhQeQ?oc=5>

### Amazon Stock Pops: What's Going On? - Amazon.com (NASDAQ:AMZN)
- Summary: Amazon Stock Pops: What's Going On? - Amazon.com (NASDAQ:AMZN)
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxPZzNaYkdqazhvS254MUt3MjVTaFcxNzV6Q2NGYlZ2eHdaUm9XS3FyTkR5WkRHX3A1SjBEQ1QtY0djSC1iTUdpRkl2bUZudFRwM2ZUcDV1eHRhRVJObXNpRFBaYjMwZDdnNWhmdkVwZkpCa0xCRWtMNkZpX2xQLXg1eENFUjV6YXROaEQ2SlhJMk9KSVZhUGJKaw?oc=5>

### Amazon stock declines while higher inflation and Fed signals boost Treasury yields
- Summary: Amazon stock declines while higher inflation and Fed signals boost Treasury yields
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihAFBVV95cUxQdWwxTW5IUFNRc01yMjBHeldQeDhUeUJjUC1idHF0bVJmWE04UkJkbWJyT1hiZmppWUd1NGpua1kzZl85bXRIMTFOZVh3VEZaMWl5cktCS1M3VEF3UXpFbjI5b21TWjMyOVZoZUlfQkVSU0tDTGlJNmVHOXRmLXA2clN4eXE?oc=5>

### Amazon Is The Smartest Way To Own Anthropic (NASDAQ:AMZN)
- Summary: Amazon’s acquisition of Anthropic positions it as a leading AI player.
- Date: 2026-11-25 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxQcFhMeDB5S290YzhSLTFMWkpYVjZOeGpvNzdOWVg2TDItUVFxRzVrenN6Y3k3a0RoRUphb2JXeWczR1FZa1pOYTR1ZWNwRlV3Q281SUx6R2FrN3ZMX0gtX2R6dFBJTHd3NjN3ZVpsWDRNbHl6anB1SmVDVEl0Q0pfRi1sTldLeFZIQWV5Wg?oc=5>

### Amazon: The AI Boom Is Just Getting Started
- Summary: Amazon highlights AI growth potential, signaling future product expansion.
- Date: 2026-11-25 | Impact: high | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxPYXdObzQzU3p0UjFqbGdjUmE0LUNBcU1iN2xpNTEzRVdKaWtfWEltdnp4RHl0RFY3a2NwWUZlMXF0TUJ2RFlpTFJGS29iV2RwYTluX0RwcDJ0dEJWaEZ1UFFkRTZnOGlrZXFSd2VpU0tPLUdISjBFZGlsZkFzWk9jZ2pSRzZuczhhR0hjUTRn?oc=5>

### Amazon Is Reportedly Paying $7.5 Billion for Decart’s AI Chip Software
- Summary: Amazon acquires Decart’s AI chip software for $7.5B, expanding its AI capabilities.
- Date: 2026-11-24 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxQLXVIRDFZWk96UXRyLWRvTUJxU2ZZMUdvSExoSk9keXF3ZWx4RTdtSDZPMFJjWTUySjZqUC1SZ0llWXNaVFJuMDVKNlNvOFlsRXRiZXM3N2t3RXM0UnZ5RnlPU3N6VnJYY2dRd1djVXhsYVAyRlg0TVJaczBIMkxYdmlJaE1pcnR3MTZ2VUFrTjRxTWE2RUdzdEhVeXlFZ2FBSmoxOVdiTld1ZkF0NDdxaVFR?oc=5>

### Can Record Black Friday Spending Lift Amazon Stock?
- Summary: Speculation on Black Friday sales potentially boosting Amazon stock.
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.5
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxNbUkzSDcwQjkwWUZReElhNWZ2TVVRcFAxZHRVZ3lITlppaGwwRllFUzBpRG1wbk9VWHV6bXByTGZzVkVKUERjdnJRNzl6ZjdYa3l2cU9ycXgyOFNwbFpqRVpURldRVlF0aGtRT1c5T2FYM3M2eEJVV0NNLURaYS1zTk50R0cwLWpqeFJsdWMzREYwc0hnQTI5ei1kRkdnQ0k?oc=5>

### Amazon has wall-to-wall free sports coverage on Black Friday (AMZN:NASDAQ) | Seeking Alpha
- Summary: Amazon offers free sports coverage during Black Friday.
- Date: 2026-11-27 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiO0FVX3lxTE84RDNqamVQdnFLT3A3b3NJQVJvQmJaWnM3NVpvSk9RNnp0ekdheDg1MENBUUoydlJJaVA0?oc=5>

### What Amazon.com (AMZN)'s UK Car Marketplace Launch Means For Shareholders
- Summary: Launch of Amazon's UK car marketplace could benefit shareholders.
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxPRHA5dzBQWGtlckZQa1IxS3dzT2YtcmxXNTkxLThhYjk1T2NHRFByMmRSVS10QW43MDNxTktMdkhFX24wcWNlQ1JDNy1XbFNfY0J0dzFpYWZyTk5QNmV0Y2x5aDlzYTFhU0l4V1E5WUlINjFMYVN3ZkRoakJuWVBIQmdKdC00VFJlRmJJb1JUdWI?oc=5>

### Why Is Amazon Stock Surging on Friday?
- Summary: Amazon stock surge observed on Friday.
- Date: 2026-11-26 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxOajFLYlpISU9VMW1QMUhKR1R1dnZaeTE3cXR3Z1RKVTUzM2lyMEhHeWYycGhJVWZReURYU2Y0VEJjNWxUS1ZyT0hNck5LZFNHVmQ4bjAwQ3U2TktWUzFabEY1WkQ2am0wbllnXzFsaXZRX3g0ZHRKdFNYWThMbHVHNkxDUExZU2N4TEUwNUdNcTBuZWI5c0l6NzhhZ2wyVms?oc=5>

### Amazon.com (NASDAQ:AMZN) Stock Jumps 4.2% - Should You Buy?
- Summary: Amazon stock increased 4.2% prompting buy considerations.
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxPc2d0UmVkRGNuOVpaY2lfWkJSRHZZYW51aWRsZkNyOGFUNWk1NzNqS3ZBaDMwOHJ5MmxqcXZ5WWxaaE10ZjN3Tk5RLTZFRjc2Z3FIQTVQV29KcVZORjN6cUJKVFRHZVQ4LVVraXFBazl6dnpRSzNxZUhQenIzX0NVbmVPS1haSF9PSWMtTnItNmVpVTRONzZuOVVqNHpSLTZmeS1kUnpBUTRtT0JKU0pOdQ?oc=5>

## HEADWINDS

### Amazon’s advertising concerns complicate talks with Meta over Muse (AMZN:NASDAQ)
- Summary: Advertising issues hinder Amazon‑Meta Muse negotiations.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxPRmlzcEFyOEU3Y1NsUGtza3NDT0Z5SXpwY01yem96aHdVR3pQbVFUcTNqRTcyLWdYSHdRQkN2WkJGcllBYnA0UTQ3bTlPZjhiYkJpakRlVVVNNGg1RzlwQlhyc1I5WWVldkxpdk5ta0d5cjM3Qnp1dUd1cktDbEpYSUtRVDZpR3RzUU5YTUFlQVZrYlVuQURCaHNEQ2p0anZ5elVKdTVR?oc=5>

### Why Is Amazon Stock Down Today? Shares Fall 5.6% as an AI Selloff Hits Big Tech and the Nasdaq Sinks 3.9%
- Summary: Amazon shares drop due to AI selloff, reflecting market volatility.
- Date: 2026-11-25 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxOTEpCNDRaX2V3M3cydmtwbG5PR25raHVDV2puLTJzNmFLTDI2dUtHYlJRWDl5Q2xqZ3lLSTlqZVVSS2hYY0FnNjdWckZIQmltaDY0NDBFeVBDdVNidjNyVXZlaGJEUmtVMXFvVFhrWnpvZlA1N1JEU1h6b2U1Q0ZsTGNVNnFzYkpQU3pGeE1zSWtiT2I1ZHl2VmxsUXdjN3JlR2JoZWs0VXFHS0ZNYVlCckF3?oc=5>

## CATALYSTS

### Amazon Stock Gets Black Friday Boost As Analysts Size Up Holiday Spending
- Summary: Amazon Stock Gets Black Friday Boost As Analysts Size Up Holiday Spending
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxQTU41NEI0dWtzYjhjT1hRSkFSd1Jkdm1RQV96dkwxZ09QWUlWY21CWFhGbUQxSVUxNXRXbThVcklCeTMzZFRFS0tBbEJHTFlBckpmUWdlcGNBWnp3SW9FcE16UWk1Q3lyNVd3enpFNkE5bmdsWlNIRkxMeUZPYm5PX0R6NDR6TFFuVFJ0Rzg2ci1CcFp5V3FWTmNzRUw5UHJxMGc?oc=5>

### Amazon.com, Inc. $AMZN Stock Purchased by Brighton Jones LLC
- Summary: Amazon.com, Inc. $AMZN Stock Purchased by Brighton Jones LLC
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxQd1EyNlFEWWhwYi1fQnExQkJqZVdVQmRNT3hfNVdyY3d0TzU4ZlpNQ215eEFOV2ptNE1rVk9uay1pSHpDcEo2WWE5Z0hxNkhYSGRKMXpPa0VRZS1LRUROWG01N0JpMVdSMl9VR3dmcTRCQjFKM29KWVFGN1lsVDdnVkpoVzFfaVlaUVJyTE9Dem45UTduR1gtejBWSVpZbl9iQWxYaUdQS3EzQlhvel9xTkNoRzI4eGFH?oc=5>

### Amazon’s CEO, CFO and AWS Chief All Just Sold Amazon Stock
- Summary: Amazon executives sold shares, indicating potential insider confidence shift.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxOZWJNbFNCT21wb3lOdTB0bFhOb0twTjR1ckFOeTZ4UHBiQl9raHZrNkIwbFFNOFlwY0xtcXBFQjNuRUJNM1RPZUJjQ0VNYW43S21zdUU5dEI3Unp3R2cwUzNRaXZPS2pmMXZHamFPdUtNN1FaTmhtYlRUV2FYYjVHb1dDRk95OWEtZGVOX2RoZG9mQkFfUWhqdlUwSmVSbTJpWFE?oc=5>

### Amazon.com (AMZN) CEO Herrington sold 6,362 shares for $1.62M at an average $255.21 under a 10b5-1 plan
- Summary: CEO Herrington sold shares under a 10b5-1 plan.
- Date: 2026-11-24 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxNamo1WFZUcmZhanZMNVU3OTl2S1R2cl8wUDA5Ym5sNGVjdGhmWUpJbTczdGZMQnhHYmN3U0dxUkpBUDJOTkFacUVpNldvYm9BWmpyVWtTM3JhaVpXOExrX1RhanpXMVg0WUFaQ2g4NGpkbGV1SWtheG95Q2lvVEltYmpqTjg1MlpGa0dfWVk3aFJBamxtbUl6ZXgwQllWZDR3VTFmMWhXQTlSMnVyVjY1SXJIQUQ?oc=5>

### Amazon.com (NASDAQ:AMZN) Bounces Back Pre-Market Today After Wednesday's Drop, with the AI Trade Recovering and AWS Concerns Still in Play
- Summary: Amazon’s pre‑market price rebounds after a Wednesday decline, driven by AI trade gains and ongoing AWS concerns.
- Date: 2026-11-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi-wFBVV95cUxOci1QLXJmYkU1QmVGU205alV1QXlfVEV1cnhCYWIzVDZ2cmJEUGJSWGtLaTR1Y1A4RnFTUWpaWkc5NnQ4SmlmQ3puYXZPSENKSld6OTY0TVZVeThhVGRpX1EtNTc4b0IxREIwaEJKd0FzYU9MaDU2RUhabmhfTFBqYi1ZNXItVWFLT1dIRFczTzVDODVkSzgzZ2FWREplS2UzM2loeDJBZ1cwVmRWN2k3QzQwOHdIVk5XNV94R2Y4alpzUmdpSlZzSEZackZ6MHRJeTJ0RWF2M0hDSVdxWV9MdXpYbE1Wd25KeENyaWh4Y3R6WUktcTE0Q0RiOA?oc=5>

## RISKS

### Amazon: Lower Downside Risk, But Not Immune To AI-Trade Related Risks (NASDAQ:AMZN)
- Summary: AI trade risks remain despite lower downside risk.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxNMmFQakQ2Y2JUb0JLV193UDltcmQ1dUJBeFNjTFlPbXVwem1lRUQ0NHpDeGpaMmNFZVcteF8zTlRyaVVHTWJ3U2FSem5wNXJGSGgyUU01Q0s1bFg2OHVJbGtuQWw5QXhOTmVtLTJ0Q3RlR2VfZ3NLaTBPVGgwS3JTYld2UHV3RUg5UjlxbU1RbjZub0k1MG1NeHdDX2VyelI4TlpBQkJmYzNMd0pn?oc=5>

### Amazon: Sacrificing Near-Term Free Cash Flow For A $1 Trillion AWS Payoff (NASDAQ:AMZN)
- Summary: Amazon plans to sacrifice short‑term cash flow for a $1T AWS payoff.
- Date: 2026-11-25 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxNZ3RVcEtJVFhJWFdyNlNnWHZpMzlCcFg0S05INUdXaXV2aVBZQUI5cm9oNkg0OE9mNzVGVTd2WnVtd2pyOEhSM05BaFZkams0QjJ2ZzRZQUNEam8tS0pqZzJPMVNQeE8tdlJuMFJrYXNOQWozR0VqWlNKdENhRURRNEJmclMxaVpqRFJtS05UUV9NVHd0SDlCcHpCalp2SWVmNlJPbmstTExacy1EVjNLNFF3?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AMZN** | **20.54** | **4.48** | **15.99** | **12.10** | **2,747,834,564,608.00 USD** | **10.89** |
| WMT | 48.24 | 10.76 | 23.21 | 5.20 | 1,059,459,104,768.00 USD | 23.05 |
| MSFT | 25.72 | 7.78 | 18.13 | 18.80 | 3,660,000,002,048.00 USD | 2.36 |
| GOOGL | 14.36 | 5.13 | 17.70 | 24.70 | 3,380,358,152,192.00 USD | -13.84 |

Peers fetched as_of: 2026-11-27; AMZN reuses existing data (market data as_of: 2026-11-27); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-29
- Next expected earnings: 2027-02-04 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-27

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-30
- Revenue (latest available single quarter): 201,944,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 20,685,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMieEFVX3lxTE52cmVhLUdXcXhuNnU2UXFEYmRzWDlxZDVHeF9majZZS1JvMzRteUN4ZEVfWng5VGtjVjBNN1dZVGFlSmtRY3hNZFkzUFdDMDllUWhnTG14cVFwWHdvSjIwczYya2I3bUhWWjM2QU9qYWhocVhSRnhQeQ?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxPZzNaYkdqazhvS254MUt3MjVTaFcxNzV6Q2NGYlZ2eHdaUm9XS3FyTkR5WkRHX3A1SjBEQ1QtY0djSC1iTUdpRkl2bUZudFRwM2ZUcDV1eHRhRVJObXNpRFBaYjMwZDdnNWhmdkVwZkpCa0xCRWtMNkZpX2xQLXg1eENFUjV6YXROaEQ2SlhJMk9KSVZhUGJKaw?oc=5
- https://news.google.com/rss/articles/CBMihAFBVV95cUxQdWwxTW5IUFNRc01yMjBHeldQeDhUeUJjUC1idHF0bVJmWE04UkJkbWJyT1hiZmppWUd1NGpua1kzZl85bXRIMTFOZVh3VEZaMWl5cktCS1M3VEF3UXpFbjI5b21TWjMyOVZoZUlfQkVSU0tDTGlJNmVHOXRmLXA2clN4eXE?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxQcFhMeDB5S290YzhSLTFMWkpYVjZOeGpvNzdOWVg2TDItUVFxRzVrenN6Y3k3a0RoRUphb2JXeWczR1FZa1pOYTR1ZWNwRlV3Q281SUx6R2FrN3ZMX0gtX2R6dFBJTHd3NjN3ZVpsWDRNbHl6anB1SmVDVEl0Q0pfRi1sTldLeFZIQWV5Wg?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxPYXdObzQzU3p0UjFqbGdjUmE0LUNBcU1iN2xpNTEzRVdKaWtfWEltdnp4RHl0RFY3a2NwWUZlMXF0TUJ2RFlpTFJGS29iV2RwYTluX0RwcDJ0dEJWaEZ1UFFkRTZnOGlrZXFSd2VpU0tPLUdISjBFZGlsZkFzWk9jZ2pSRzZuczhhR0hjUTRn?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxQLXVIRDFZWk96UXRyLWRvTUJxU2ZZMUdvSExoSk9keXF3ZWx4RTdtSDZPMFJjWTUySjZqUC1SZ0llWXNaVFJuMDVKNlNvOFlsRXRiZXM3N2t3RXM0UnZ5RnlPU3N6VnJYY2dRd1djVXhsYVAyRlg0TVJaczBIMkxYdmlJaE1pcnR3MTZ2VUFrTjRxTWE2RUdzdEhVeXlFZ2FBSmoxOVdiTld1ZkF0NDdxaVFR?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxNbUkzSDcwQjkwWUZReElhNWZ2TVVRcFAxZHRVZ3lITlppaGwwRllFUzBpRG1wbk9VWHV6bXByTGZzVkVKUERjdnJRNzl6ZjdYa3l2cU9ycXgyOFNwbFpqRVpURldRVlF0aGtRT1c5T2FYM3M2eEJVV0NNLURaYS1zTk50R0cwLWpqeFJsdWMzREYwc0hnQTI5ei1kRkdnQ0k?oc=5
- https://news.google.com/rss/articles/CBMiO0FVX3lxTE84RDNqamVQdnFLT3A3b3NJQVJvQmJaWnM3NVpvSk9RNnp0ekdheDg1MENBUUoydlJJaVA0?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxPRHA5dzBQWGtlckZQa1IxS3dzT2YtcmxXNTkxLThhYjk1T2NHRFByMmRSVS10QW43MDNxTktMdkhFX24wcWNlQ1JDNy1XbFNfY0J0dzFpYWZyTk5QNmV0Y2x5aDlzYTFhU0l4V1E5WUlINjFMYVN3ZkRoakJuWVBIQmdKdC00VFJlRmJJb1JUdWI?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxOajFLYlpISU9VMW1QMUhKR1R1dnZaeTE3cXR3Z1RKVTUzM2lyMEhHeWYycGhJVWZReURYU2Y0VEJjNWxUS1ZyT0hNck5LZFNHVmQ4bjAwQ3U2TktWUzFabEY1WkQ2am0wbllnXzFsaXZRX3g0ZHRKdFNYWThMbHVHNkxDUExZU2N4TEUwNUdNcTBuZWI5c0l6NzhhZ2wyVms?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxPc2d0UmVkRGNuOVpaY2lfWkJSRHZZYW51aWRsZkNyOGFUNWk1NzNqS3ZBaDMwOHJ5MmxqcXZ5WWxaaE10ZjN3Tk5RLTZFRjc2Z3FIQTVQV29KcVZORjN6cUJKVFRHZVQ4LVVraXFBazl6dnpRSzNxZUhQenIzX0NVbmVPS1haSF9PSWMtTnItNmVpVTRONzZuOVVqNHpSLTZmeS1kUnpBUTRtT0JKU0pOdQ?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxPRmlzcEFyOEU3Y1NsUGtza3NDT0Z5SXpwY01yem96aHdVR3pQbVFUcTNqRTcyLWdYSHdRQkN2WkJGcllBYnA0UTQ3bTlPZjhiYkJpakRlVVVNNGg1RzlwQlhyc1I5WWVldkxpdk5ta0d5cjM3Qnp1dUd1cktDbEpYSUtRVDZpR3RzUU5YTUFlQVZrYlVuQURCaHNEQ2p0anZ5elVKdTVR?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxOTEpCNDRaX2V3M3cydmtwbG5PR25raHVDV2puLTJzNmFLTDI2dUtHYlJRWDl5Q2xqZ3lLSTlqZVVSS2hYY0FnNjdWckZIQmltaDY0NDBFeVBDdVNidjNyVXZlaGJEUmtVMXFvVFhrWnpvZlA1N1JEU1h6b2U1Q0ZsTGNVNnFzYkpQU3pGeE1zSWtiT2I1ZHl2VmxsUXdjN3JlR2JoZWs0VXFHS0ZNYVlCckF3?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxQTU41NEI0dWtzYjhjT1hRSkFSd1Jkdm1RQV96dkwxZ09QWUlWY21CWFhGbUQxSVUxNXRXbThVcklCeTMzZFRFS0tBbEJHTFlBckpmUWdlcGNBWnp3SW9FcE16UWk1Q3lyNVd3enpFNkE5bmdsWlNIRkxMeUZPYm5PX0R6NDR6TFFuVFJ0Rzg2ci1CcFp5V3FWTmNzRUw5UHJxMGc?oc=5
- https://news.google.com/rss/articles/CBMiuAFBVV95cUxQd1EyNlFEWWhwYi1fQnExQkJqZVdVQmRNT3hfNVdyY3d0TzU4ZlpNQ215eEFOV2ptNE1rVk9uay1pSHpDcEo2WWE5Z0hxNkhYSGRKMXpPa0VRZS1LRUROWG01N0JpMVdSMl9VR3dmcTRCQjFKM29KWVFGN1lsVDdnVkpoVzFfaVlaUVJyTE9Dem45UTduR1gtejBWSVpZbl9iQWxYaUdQS3EzQlhvel9xTkNoRzI4eGFH?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxOZWJNbFNCT21wb3lOdTB0bFhOb0twTjR1ckFOeTZ4UHBiQl9raHZrNkIwbFFNOFlwY0xtcXBFQjNuRUJNM1RPZUJjQ0VNYW43S21zdUU5dEI3Unp3R2cwUzNRaXZPS2pmMXZHamFPdUtNN1FaTmhtYlRUV2FYYjVHb1dDRk95OWEtZGVOX2RoZG9mQkFfUWhqdlUwSmVSbTJpWFE?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxNamo1WFZUcmZhanZMNVU3OTl2S1R2cl8wUDA5Ym5sNGVjdGhmWUpJbTczdGZMQnhHYmN3U0dxUkpBUDJOTkFacUVpNldvYm9BWmpyVWtTM3JhaVpXOExrX1RhanpXMVg0WUFaQ2g4NGpkbGV1SWtheG95Q2lvVEltYmpqTjg1MlpGa0dfWVk3aFJBamxtbUl6ZXgwQllWZDR3VTFmMWhXQTlSMnVyVjY1SXJIQUQ?oc=5
- https://news.google.com/rss/articles/CBMi-wFBVV95cUxOci1QLXJmYkU1QmVGU205alV1QXlfVEV1cnhCYWIzVDZ2cmJEUGJSWGtLaTR1Y1A4RnFTUWpaWkc5NnQ4SmlmQ3puYXZPSENKSld6OTY0TVZVeThhVGRpX1EtNTc4b0IxREIwaEJKd0FzYU9MaDU2RUhabmhfTFBqYi1ZNXItVWFLT1dIRFczTzVDODVkSzgzZ2FWREplS2UzM2loeDJBZ1cwVmRWN2k3QzQwOHdIVk5XNV94R2Y4alpzUmdpSlZzSEZackZ6MHRJeTJ0RWF2M0hDSVdxWV9MdXpYbE1Wd25KeENyaWh4Y3R6WUktcTE0Q0RiOA?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxNMmFQakQ2Y2JUb0JLV193UDltcmQ1dUJBeFNjTFlPbXVwem1lRUQ0NHpDeGpaMmNFZVcteF8zTlRyaVVHTWJ3U2FSem5wNXJGSGgyUU01Q0s1bFg2OHVJbGtuQWw5QXhOTmVtLTJ0Q3RlR2VfZ3NLaTBPVGgwS3JTYld2UHV3RUg5UjlxbU1RbjZub0k1MG1NeHdDX2VyelI4TlpBQkJmYzNMd0pn?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxNZ3RVcEtJVFhJWFdyNlNnWHZpMzlCcFg0S05INUdXaXV2aVBZQUI5cm9oNkg0OE9mNzVGVTd2WnVtd2pyOEhSM05BaFZkams0QjJ2ZzRZQUNEam8tS0pqZzJPMVNQeE8tdlJuMFJrYXNOQWozR0VqWlNKdENhRURRNEJmclMxaVpqRFJtS05UUV9NVHd0SDlCcHpCalp2SWVmNlJPbmstTExacy1EVjNLNFF3?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
