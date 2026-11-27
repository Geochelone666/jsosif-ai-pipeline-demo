# AMZN Intelligence Report

- ticker: **AMZN**
- Report as_of: **2026-11-26**
- Market data as_of: **2026-11-25**
- Quant sources: https://finance.yahoo.com/quote/AMZN/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/AMZN/key-statistics/
- AI analysis snapshot as_of: **2026-11-26**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-27T06:44:30.995913+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 7, 'ai': 11, 'unknown': 0, 'irrelevant': 7})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **13** exact headline/source/date matches; prior report **20261126T064454Z-dbdd6f45/AMZN** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'directional_claim_without_event_type': 1}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 13 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 28.0%; oldest publication 2026-11-19

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 244.4300 |
| Return 1D (%) | -3.1155 |
| Return 1W (%) | -8.7062 |
| Return 1M (%) | -1.4395 |
| Return YTD (%) | 5.8964 |
| Return 1Y (%) | 6.4266 |
| Annualized volatility (%) | 34.5066 |
| Beta vs SPY | 1.2417 |
| Max drawdown (%) | -19.6419 |
| Sharpe (rf=0) | 0.3499 |
| Downside deviation (rf=0, %) | 21.4537 |
| Sortino (rf=0) | 0.5628 |
| Historical VaR 95% (1D, %) | 3.2284 |
| Historical ES 95% (1D, %) | 4.1300 |
| Correlation vs SPY | 0.5372 |
| Tracking error vs SPY (%) | 29.3267 |
| P/E (trailing) | 19.76 |
| P/B | 4.31 |
| EV/EBITDA | 15.42 |
| Revenue growth (%) | 12.10 |
| Forward P/E (estimate) | 22.37 |
| Gross margin (%) | 51.37 |
| Operating margin (%) | 13.09 |
| Return on equity (%) | 27.42 |
| Free cash flow yield (%) | -1.31 |
| MA50 | 255.1158 |
| Close vs MA50 (%) | -4.1886 |
| MA200 | 245.7811 |
| Close vs MA200 (%) | -0.5497 |
| RSI (14, Wilder) | 41.9550 |
| MACD (12,26) | -0.9804 |
| MACD signal (9) | 0.9062 |
| MACD histogram | -1.8866 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'AMZN': 290, 'SPY': 290}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 244.4300 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -3.1155 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -8.7062 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -1.4395 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 5.8964 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 6.4266 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 34.5066 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 21.4537 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.5628 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.2284 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.1300 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5372 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 29.3267 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.2417 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -19.6419 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.3499 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 22.3712 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 51.3740 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 13.0870 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 27.4160 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: -1.3141 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 19.7599 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 41.9550 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -1.8866 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -4.1886 -> Slightly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -0.5497 -> Slightly below the moving-average trend level.

## TAILWINDS

### Amazon Stock Pops: What's Going On? - Amazon.com (NASDAQ:AMZN)
- Summary: Amazon Stock Pops: What's Going On? - Amazon.com (NASDAQ:AMZN)
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxPZzNaYkdqazhvS254MUt3MjVTaFcxNzV6Q2NGYlZ2eHdaUm9XS3FyTkR5WkRHX3A1SjBEQ1QtY0djSC1iTUdpRkl2bUZudFRwM2ZUcDV1eHRhRVJObXNpRFBaYjMwZDdnNWhmdkVwZkpCa0xCRWtMNkZpX2xQLXg1eENFUjV6YXROaEQ2SlhJMk9KSVZhUGJKaw?oc=5>

### Amazon Stock Moves Higher: What's Going On?
- Summary: Amazon Stock Moves Higher: What's Going On?
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxOd3EzOU9yRkc4NDAwWmxwN0dpeF9DdHJpNFpmN1hfV2poTUZkY21xcW1jNXAyR1BIU3NDZnpPQ0M3Z2NYMG1xeTAzRXpwTUplOTB5SHZ0R2xtNjNmajRrVWxCTVl0ZGpiUEtnS1FRRFpIMUE2dFlYZUo2WXFEVXNkM1JEYU1DdW5vS05YbXdwcW10dWJwS0ltdDVQd0xBLXVfOENXRUdn?oc=5>

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

### Amazon (AMZN) Stock Trades Below Fair Value As Its 82% Run Continues
- Summary: Amazon (AMZN) Stock Trades Below Fair Value As Its 82% Run Continues
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxQUUtfMDhmNWV5dFk3RkdyTDhlTi1NZ2U1QmVMXzBhWmZwWHlGWktLSk1kbUFJUTVEUjYybDFxT2NJMjFRa2lySmw2bkVSdXFtcnpxaEFsbWF1MEhPX3FVLUxFSXAyTmM4LXJwVUVSS29KTWtxejlYYjZVejNGTW9FbXpmUFBzRE53Yi11TnBUVnAyYTBLNllfQ2E2OA?oc=5>

### Amazon (AMZN) Stock Trades Below Fair Value With AI Cash Flow In Focus
- Summary: Amazon (AMZN) Stock Trades Below Fair Value With AI Cash Flow In Focus
- Date: 2026-11-21 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwwFBVV95cUxNcWlDUlo1X0dLWE1CbGY1dUg4cXRPaDgtRFRHN1JWRGxOTktkbzFRV1VTWnQ1VmMzUDUwTWloa2l5RVdtU0FuZC1kbHR1X2N4bEdHMHg4TEZ2bGV6LTM0d2FvVFg4emU5RjlJbHRXOXhReFBUbEZQREZfeHNFclBlcFNnQzlaLW13czBwbUVSakJrUG14eG9OUS1lY2lFMFBXOGZTZzdNZHFVXy1xQWVidEM5Rm5oYndMVnB3YTFIZkJxdlXSAcgBQVVfeXFMTkQzTnB5bEJNOHNlbjJVOFpVbFVzQXdQb0lxV19wQWp4OE5SU3hSQnFmMWM0dmZvU1hHeWh4cWZ6a1N6WU1EbXFHNW9LOVlXZmFEaDB3M2F3Y3ZrN0dKcklScDBWSEZxUWlmR2xfekdGbEQyN1pVNEdtMkhPOFd2UkZHVHBnalVhZkJublJoQkdueWd0LVMxWFhmWm9NUDJIRjVVUHRZYjJIRlJpUWFUU2NmeGE1bnE3VWJxWHl2cGtOa1JVQ2tQbkY?oc=5>

### Amazon Stock Rises 4% After Announcing Acquisition of AI Startup Decart AI
- Summary: Amazon Stock Rises 4% After Announcing Acquisition of AI Startup Decart AI
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxOeGZMRDlrbE1hb21mc28zX0JxOFNacFNmWVNYZzJ3cnVOeWd0TTdMNlJ0RGNxT1FRSkdvNEdqSi1fN2NueW9yeEdGaUxmNVNyd052SWZoSTl6QTA4WmNIWDQ5eWVDUWl4TW1sYU1PRHV0MU1iNFBJY05DSWNzdTNwbmRaZ0xiR2xpUE8zNnd5R2VNaWpTTFlucWVfR1dYcm1zZUU3WnhKTFI5V2M?oc=5>

### Amazon (NASDAQ:AMZN) Takes Aim at Nvidia With Reported $7.5 Billion AI Technology Deal
- Summary: Amazon (NASDAQ:AMZN) Takes Aim at Nvidia With Reported $7.5 Billion AI Technology Deal
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMib0FVX3lxTE1zdE5xTF90UGhzTWsyQ05ybnVzaElJWW96MmF2QlYzZ01VUWV3MFdac0NsNUx1aEV1UUNCQ0tTc2NHamVoUnQtTVh2U1gzYVNjbXhZOFpxakZycDNkYzFlOHFVWl92Rlg5NHRpa0o2WQ?oc=5>

### Amazon’s CEO, CFO and AWS Chief All Just Sold Amazon Stock
- Summary: Amazon executives sold shares, indicating potential insider confidence shift.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxOZWJNbFNCT21wb3lOdTB0bFhOb0twTjR1ckFOeTZ4UHBiQl9raHZrNkIwbFFNOFlwY0xtcXBFQjNuRUJNM1RPZUJjQ0VNYW43S21zdUU5dEI3Unp3R2cwUzNRaXZPS2pmMXZHamFPdUtNN1FaTmhtYlRUV2FYYjVHb1dDRk95OWEtZGVOX2RoZG9mQkFfUWhqdlUwSmVSbTJpWFE?oc=5>

### Amazon, Meta Reportedly Discuss Restoring Muse Shopping Bot Access As Advertising Concerns Persist
- Summary: Amazon considers reintroducing Muse bot to address ad concerns.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi7wFBVV95cUxPb2NPSzZZQWxaOVJGU3QwSE9ZN2VnajdYNTh6RlF5cXhfeU40SzgzbmEwV19rWXpkcDRMdmhZYUoyZGpNQWg5aGtjd3ViSFV3eVU4V2ZDV1lpMXdFNzMwLWRMRTA1QkRmdzZpd1h4Mm5XVWVoalh0V3c1V1RiOGxvNDloRTh1UjZRYjVxa0VLaHJHdkpaNXYyT05XcV9iZkhWcWN2NTJHdHUtZ3FYNGkzMlc0Zlk1UXFVakdnVU1vVHB3c2JzWWxrNC01RWhIRUZwV3hyN2RpOE1XdUJqNWRBaUtWMHh5clFYWU9fTHFTWQ?oc=5>

### Amazon.com (AMZN) CEO Herrington sold 6,362 shares for $1.62M at an average $255.21 under a 10b5-1 plan
- Summary: CEO Herrington sold shares under a 10b5-1 plan.
- Date: 2026-11-24 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxNamo1WFZUcmZhanZMNVU3OTl2S1R2cl8wUDA5Ym5sNGVjdGhmWUpJbTczdGZMQnhHYmN3U0dxUkpBUDJOTkFacUVpNldvYm9BWmpyVWtTM3JhaVpXOExrX1RhanpXMVg0WUFaQ2g4NGpkbGV1SWtheG95Q2lvVEltYmpqTjg1MlpGa0dfWVk3aFJBamxtbUl6ZXgwQllWZDR3VTFmMWhXQTlSMnVyVjY1SXJIQUQ?oc=5>

## RISKS

### Amazon: Lower Downside Risk, But Not Immune To AI-Trade Related Risks (NASDAQ:AMZN)
- Summary: AI trade risks remain despite lower downside risk.
- Date: 2026-11-25 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxNMmFQakQ2Y2JUb0JLV193UDltcmQ1dUJBeFNjTFlPbXVwem1lRUQ0NHpDeGpaMmNFZVcteF8zTlRyaVVHTWJ3U2FSem5wNXJGSGgyUU01Q0s1bFg2OHVJbGtuQWw5QXhOTmVtLTJ0Q3RlR2VfZ3NLaTBPVGgwS3JTYld2UHV3RUg5UjlxbU1RbjZub0k1MG1NeHdDX2VyelI4TlpBQkJmYzNMd0pn?oc=5>

### FAA probes Amazon delivery drone crash in Michigan near Detroit (AMZN:NASDAQ)
- Summary: FAA investigating Amazon drone crash.
- Date: 2026-11-24 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxOeFVtMWpScDBVZnhzMnVXQWNmcmlWRGtSSUVIeWhvRXloUGVSdE1vSE9lTUNlbVBJR1JtYjhPaVRSeHNOV093NDg0aF9vQ3lPTTdFYmpidm5zbURJNmtFNUJFN1ZISllDeFFBemQ3ZXhDQUhsTFdNYXo5aE9ONTVOVV8zT1M3OHhNZXd5Mm1qRG8xajNPbHNjRGRGVHNmbnFnX0F3?oc=5>

### Amazon: Sacrificing Near-Term Free Cash Flow For A $1 Trillion AWS Payoff (NASDAQ:AMZN)
- Summary: Amazon plans to sacrifice short‑term cash flow for a $1T AWS payoff.
- Date: 2026-11-25 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisgFBVV95cUxNZ3RVcEtJVFhJWFdyNlNnWHZpMzlCcFg0S05INUdXaXV2aVBZQUI5cm9oNkg0OE9mNzVGVTd2WnVtd2pyOEhSM05BaFZkams0QjJ2ZzRZQUNEam8tS0pqZzJPMVNQeE8tdlJuMFJrYXNOQWozR0VqWlNKdENhRURRNEJmclMxaVpqRFJtS05UUV9NVHd0SDlCcHpCalp2SWVmNlJPbmstTExacy1EVjNLNFF3?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **AMZN** | **19.76** | **4.31** | **15.42** | **12.10** | **2,643,055,345,664.00 USD** | **6.43** |
| WMT | 47.80 | 10.67 | 23.02 | 5.20 | 1,046,778,478,592.00 USD | 24.35 |
| MSFT | 25.57 | 7.73 | 18.03 | 18.80 | 3,638,315,450,368.00 USD | 3.56 |
| GOOGL | 14.26 | 5.09 | 17.58 | 24.70 | 3,357,491,331,072.00 USD | -15.34 |

Peers fetched as_of: 2026-11-26; AMZN reuses existing data (market data as_of: 2026-11-25); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-29
- Next expected earnings: 2027-02-04 (yfinance; expected dates may change)

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
- Filing date: 2026-10-30
- Revenue (latest available single quarter): 201,944,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 20,685,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMimAFBVV95cUxPZzNaYkdqazhvS254MUt3MjVTaFcxNzV6Q2NGYlZ2eHdaUm9XS3FyTkR5WkRHX3A1SjBEQ1QtY0djSC1iTUdpRkl2bUZudFRwM2ZUcDV1eHRhRVJObXNpRFBaYjMwZDdnNWhmdkVwZkpCa0xCRWtMNkZpX2xQLXg1eENFUjV6YXROaEQ2SlhJMk9KSVZhUGJKaw?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxOd3EzOU9yRkc4NDAwWmxwN0dpeF9DdHJpNFpmN1hfV2poTUZkY21xcW1jNXAyR1BIU3NDZnpPQ0M3Z2NYMG1xeTAzRXpwTUplOTB5SHZ0R2xtNjNmajRrVWxCTVl0ZGpiUEtnS1FRRFpIMUE2dFlYZUo2WXFEVXNkM1JEYU1DdW5vS05YbXdwcW10dWJwS0ltdDVQd0xBLXVfOENXRUdn?oc=5
- https://news.google.com/rss/articles/CBMihAFBVV95cUxQdWwxTW5IUFNRc01yMjBHeldQeDhUeUJjUC1idHF0bVJmWE04UkJkbWJyT1hiZmppWUd1NGpua1kzZl85bXRIMTFOZVh3VEZaMWl5cktCS1M3VEF3UXpFbjI5b21TWjMyOVZoZUlfQkVSU0tDTGlJNmVHOXRmLXA2clN4eXE?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxQcFhMeDB5S290YzhSLTFMWkpYVjZOeGpvNzdOWVg2TDItUVFxRzVrenN6Y3k3a0RoRUphb2JXeWczR1FZa1pOYTR1ZWNwRlV3Q281SUx6R2FrN3ZMX0gtX2R6dFBJTHd3NjN3ZVpsWDRNbHl6anB1SmVDVEl0Q0pfRi1sTldLeFZIQWV5Wg?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxPYXdObzQzU3p0UjFqbGdjUmE0LUNBcU1iN2xpNTEzRVdKaWtfWEltdnp4RHl0RFY3a2NwWUZlMXF0TUJ2RFlpTFJGS29iV2RwYTluX0RwcDJ0dEJWaEZ1UFFkRTZnOGlrZXFSd2VpU0tPLUdISjBFZGlsZkFzWk9jZ2pSRzZuczhhR0hjUTRn?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxQLXVIRDFZWk96UXRyLWRvTUJxU2ZZMUdvSExoSk9keXF3ZWx4RTdtSDZPMFJjWTUySjZqUC1SZ0llWXNaVFJuMDVKNlNvOFlsRXRiZXM3N2t3RXM0UnZ5RnlPU3N6VnJYY2dRd1djVXhsYVAyRlg0TVJaczBIMkxYdmlJaE1pcnR3MTZ2VUFrTjRxTWE2RUdzdEhVeXlFZ2FBSmoxOVdiTld1ZkF0NDdxaVFR?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxPRmlzcEFyOEU3Y1NsUGtza3NDT0Z5SXpwY01yem96aHdVR3pQbVFUcTNqRTcyLWdYSHdRQkN2WkJGcllBYnA0UTQ3bTlPZjhiYkJpakRlVVVNNGg1RzlwQlhyc1I5WWVldkxpdk5ta0d5cjM3Qnp1dUd1cktDbEpYSUtRVDZpR3RzUU5YTUFlQVZrYlVuQURCaHNEQ2p0anZ5elVKdTVR?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxOTEpCNDRaX2V3M3cydmtwbG5PR25raHVDV2puLTJzNmFLTDI2dUtHYlJRWDl5Q2xqZ3lLSTlqZVVSS2hYY0FnNjdWckZIQmltaDY0NDBFeVBDdVNidjNyVXZlaGJEUmtVMXFvVFhrWnpvZlA1N1JEU1h6b2U1Q0ZsTGNVNnFzYkpQU3pGeE1zSWtiT2I1ZHl2VmxsUXdjN3JlR2JoZWs0VXFHS0ZNYVlCckF3?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxQUUtfMDhmNWV5dFk3RkdyTDhlTi1NZ2U1QmVMXzBhWmZwWHlGWktLSk1kbUFJUTVEUjYybDFxT2NJMjFRa2lySmw2bkVSdXFtcnpxaEFsbWF1MEhPX3FVLUxFSXAyTmM4LXJwVUVSS29KTWtxejlYYjZVejNGTW9FbXpmUFBzRE53Yi11TnBUVnAyYTBLNllfQ2E2OA?oc=5
- https://news.google.com/rss/articles/CBMiwwFBVV95cUxNcWlDUlo1X0dLWE1CbGY1dUg4cXRPaDgtRFRHN1JWRGxOTktkbzFRV1VTWnQ1VmMzUDUwTWloa2l5RVdtU0FuZC1kbHR1X2N4bEdHMHg4TEZ2bGV6LTM0d2FvVFg4emU5RjlJbHRXOXhReFBUbEZQREZfeHNFclBlcFNnQzlaLW13czBwbUVSakJrUG14eG9OUS1lY2lFMFBXOGZTZzdNZHFVXy1xQWVidEM5Rm5oYndMVnB3YTFIZkJxdlXSAcgBQVVfeXFMTkQzTnB5bEJNOHNlbjJVOFpVbFVzQXdQb0lxV19wQWp4OE5SU3hSQnFmMWM0dmZvU1hHeWh4cWZ6a1N6WU1EbXFHNW9LOVlXZmFEaDB3M2F3Y3ZrN0dKcklScDBWSEZxUWlmR2xfekdGbEQyN1pVNEdtMkhPOFd2UkZHVHBnalVhZkJublJoQkdueWd0LVMxWFhmWm9NUDJIRjVVUHRZYjJIRlJpUWFUU2NmeGE1bnE3VWJxWHl2cGtOa1JVQ2tQbkY?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxOeGZMRDlrbE1hb21mc28zX0JxOFNacFNmWVNYZzJ3cnVOeWd0TTdMNlJ0RGNxT1FRSkdvNEdqSi1fN2NueW9yeEdGaUxmNVNyd052SWZoSTl6QTA4WmNIWDQ5eWVDUWl4TW1sYU1PRHV0MU1iNFBJY05DSWNzdTNwbmRaZ0xiR2xpUE8zNnd5R2VNaWpTTFlucWVfR1dYcm1zZUU3WnhKTFI5V2M?oc=5
- https://news.google.com/rss/articles/CBMib0FVX3lxTE1zdE5xTF90UGhzTWsyQ05ybnVzaElJWW96MmF2QlYzZ01VUWV3MFdac0NsNUx1aEV1UUNCQ0tTc2NHamVoUnQtTVh2U1gzYVNjbXhZOFpxakZycDNkYzFlOHFVWl92Rlg5NHRpa0o2WQ?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxOZWJNbFNCT21wb3lOdTB0bFhOb0twTjR1ckFOeTZ4UHBiQl9raHZrNkIwbFFNOFlwY0xtcXBFQjNuRUJNM1RPZUJjQ0VNYW43S21zdUU5dEI3Unp3R2cwUzNRaXZPS2pmMXZHamFPdUtNN1FaTmhtYlRUV2FYYjVHb1dDRk95OWEtZGVOX2RoZG9mQkFfUWhqdlUwSmVSbTJpWFE?oc=5
- https://news.google.com/rss/articles/CBMi7wFBVV95cUxPb2NPSzZZQWxaOVJGU3QwSE9ZN2VnajdYNTh6RlF5cXhfeU40SzgzbmEwV19rWXpkcDRMdmhZYUoyZGpNQWg5aGtjd3ViSFV3eVU4V2ZDV1lpMXdFNzMwLWRMRTA1QkRmdzZpd1h4Mm5XVWVoalh0V3c1V1RiOGxvNDloRTh1UjZRYjVxa0VLaHJHdkpaNXYyT05XcV9iZkhWcWN2NTJHdHUtZ3FYNGkzMlc0Zlk1UXFVakdnVU1vVHB3c2JzWWxrNC01RWhIRUZwV3hyN2RpOE1XdUJqNWRBaUtWMHh5clFYWU9fTHFTWQ?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxNamo1WFZUcmZhanZMNVU3OTl2S1R2cl8wUDA5Ym5sNGVjdGhmWUpJbTczdGZMQnhHYmN3U0dxUkpBUDJOTkFacUVpNldvYm9BWmpyVWtTM3JhaVpXOExrX1RhanpXMVg0WUFaQ2g4NGpkbGV1SWtheG95Q2lvVEltYmpqTjg1MlpGa0dfWVk3aFJBamxtbUl6ZXgwQllWZDR3VTFmMWhXQTlSMnVyVjY1SXJIQUQ?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxNMmFQakQ2Y2JUb0JLV193UDltcmQ1dUJBeFNjTFlPbXVwem1lRUQ0NHpDeGpaMmNFZVcteF8zTlRyaVVHTWJ3U2FSem5wNXJGSGgyUU01Q0s1bFg2OHVJbGtuQWw5QXhOTmVtLTJ0Q3RlR2VfZ3NLaTBPVGgwS3JTYld2UHV3RUg5UjlxbU1RbjZub0k1MG1NeHdDX2VyelI4TlpBQkJmYzNMd0pn?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxOeFVtMWpScDBVZnhzMnVXQWNmcmlWRGtSSUVIeWhvRXloUGVSdE1vSE9lTUNlbVBJR1JtYjhPaVRSeHNOV093NDg0aF9vQ3lPTTdFYmpidm5zbURJNmtFNUJFN1ZISllDeFFBemQ3ZXhDQUhsTFdNYXo5aE9ONTVOVV8zT1M3OHhNZXd5Mm1qRG8xajNPbHNjRGRGVHNmbnFnX0F3?oc=5
- https://news.google.com/rss/articles/CBMisgFBVV95cUxNZ3RVcEtJVFhJWFdyNlNnWHZpMzlCcFg0S05INUdXaXV2aVBZQUI5cm9oNkg0OE9mNzVGVTd2WnVtd2pyOEhSM05BaFZkams0QjJ2ZzRZQUNEam8tS0pqZzJPMVNQeE8tdlJuMFJrYXNOQWozR0VqWlNKdENhRURRNEJmclMxaVpqRFJtS05UUV9NVHd0SDlCcHpCalp2SWVmNlJPbmstTExacy1EVjNLNFF3?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
