# CSCO Intelligence Report

- ticker: **CSCO**
- Report as_of: **2026-11-10**
- Market data as_of: **2026-11-10**
- Quant sources: https://finance.yahoo.com/quote/CSCO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/CSCO/key-statistics/
- AI analysis snapshot as_of: **2026-11-10**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-11T04:37:35.062643+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 23, 'rule': 4, 'ai': 12, 'unknown': 0, 'irrelevant': 7})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **12** exact headline/source/date matches; prior report **20261110T055129Z-abd33250/CSCO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **2**; {'low_uncalibrated_model_confidence': 1, 'short_term_price_move_in_structural_risks': 1}
- RSS source audit (metadata only, not article fact-checking): 23 unique headlines; 13 named publishers; 2 exact duplicates; 23 HTTPS source links; largest publisher share 43.48%; oldest publication 2026-11-04

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 98.1500 |
| Return 1D (%) | -0.5068 |
| Return 1W (%) | -4.6810 |
| Return 1M (%) | -17.0960 |
| Return YTD (%) | 29.7768 |
| Return 1Y (%) | 38.6698 |
| Annualized volatility (%) | 36.8150 |
| Beta vs SPY | 1.2383 |
| Max drawdown (%) | -27.2567 |
| Sharpe (rf=0) | 1.0762 |
| Downside deviation (rf=0, %) | 25.4333 |
| Sortino (rf=0) | 1.5578 |
| Historical VaR 95% (1D, %) | 3.0714 |
| Historical ES 95% (1D, %) | 5.3408 |
| Correlation vs SPY | 0.4598 |
| Tracking error vs SPY (%) | 32.8540 |
| P/E (trailing) | 29.47 |
| P/B | 7.70 |
| EV/EBITDA | 21.58 |
| Revenue growth (%) | 17.60 |
| Forward P/E (estimate) | 17.45 |
| Gross margin (%) | 64.52 |
| Operating margin (%) | 27.72 |
| Return on equity (%) | 27.32 |
| Free cash flow yield (%) | 2.89 |
| MA50 | 108.1597 |
| Close vs MA50 (%) | -9.2546 |
| MA200 | 101.4144 |
| Close vs MA200 (%) | -3.2189 |
| RSI (14, Wilder) | 38.0072 |
| MACD (12,26) | -3.3963 |
| MACD signal (9) | -2.3098 |
| MACD histogram | -1.0865 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'CSCO': 279, 'SPY': 279}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 98.1500 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.5068 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -4.6810 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -17.0960 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 29.7768 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 38.6698 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 36.8150 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 25.4333 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.5578 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.0714 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.3408 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4598 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 32.8540 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.2383 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -27.2567 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.0762 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 17.4521 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 64.5240 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 27.7190 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 27.3190 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.8898 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 29.4745 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 38.0072 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -1.0865 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -9.2546 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -3.2189 -> Slightly below the moving-average trend level.

## TAILWINDS

### Cisco Systems Inc (CSCO) Stock Up 5.1% but GF Value Says Overval
- Summary: Cisco Systems Inc (CSCO) Stock Up 5.1% but GF Value Says Overval
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiuAFBVV95cUxQdXlQLXVlWi1HdHF5OUF6SllhRXBWc19HWUdiY2luV05BRXdkaHBfYTh5QmRrX25kZ3p4QlZYa29PVHdLc2lpNWxrMExCUnZQQVhia3pKUE54RjVtZWhxXzFuNVJFX2tueDNYSmk4TmZmaDQxMDF1c1U0NzFtRFIwQnlZTjlocElyQk1hQ0xJZ1V0ZzN6TzVBVmRQOTVOWEdQZzZ5cS1Za2JwUEZJa3ZwOVRRN3lLZVJ1?oc=5>

### Cisco Systems (CSCO) Could Be 15% Undervalued As AI Earnings Focus Builds
- Summary: Investors see Cisco undervalued amid AI earnings focus, suggesting potential upside.
- Date: 2026-11-09 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxNaUZoNjY4Sy13SHlPSFN1Mno0cWtaWFVDMDhDWm90TDRVcmpTSGc3dzh3M09GZ1g0bGRDdnpGVHk0WFlDUFc0WDNkaW9DYy11b2dhV2RuUEVOTTJpa3F2ZUhOdTVFaTJyUnZvWjY0Nmp1eTBWOWdldWJqOU1heXF0MlJvcUR4T1BLTDEwdXo0OEdsbXJJOGdZ?oc=5>

### What Could Lift Cisco Stock?
- Summary: Speculation on factors that could boost Cisco's stock.
- Date: 2026-11-05 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxNd2JhNnJ3MTU4TTV4XzZWdUZVSFdZZWJGTW8xNXlZTGdYWEY5VG9jVmx2NTV5blFTUkU0R0gyMS1SLW9Dd095djJSWXVTQ0xCYURmR2R2c2JpLVhZZEQ3S09RamFPem5PbVVBVzdzNHZULWFJazB3Y0lQeXJnMS0yVGRKY05oUUpGNnBEZi01b3plUQ?oc=5>

### Cisco Systems Stock Outlook: Is Wall Street Bullish or Bearish?
- Summary: Questioning market sentiment toward Cisco's future performance.
- Date: 2026-11-04 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxNNmxUZjJVSDRsTWZrakJ0REVoVTJocTBrYlRaemh4MkV4Sk1DY0hETHFKYmJsNmxrd2VrZnJ2R1JEczV1VHVHaDhoNHM0Vl9feXY1UkFhWm9Qa01ySHVGaEhlWlUzY3ZzRmprcVRCZXFTd3k4V1RtbUE0SHJxUVBULUF6OGIydDBUZHBra2xZT2hfWTd0dGlRZ29pdUZJQQ?oc=5>

### 60 ETFs Add to Cisco (CSCO) Holdings on Nov. 6
- Summary: Fifty‑six ETFs increased Cisco holdings, indicating broader institutional support.
- Date: 2026-11-10 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxNLU8yTTBOZmdNWEVjd3BiajlPNEVEVTRqUElzRTR6UHFidEFMTmFlZFZRVldOM0RLbFM2dEN3dldoTGFLUFF2bHkxd1h5T1RTZm1NOFl5YXY3V1J1enRJSGUxRFl4dEstTzZ4am1LSGhGaU8tWm1tNHBrNzNzelJxNEhNVUJWNlRtUl96Nl8zOGM?oc=5>

## HEADWINDS

### Morgan Stanley Downgrades Cisco On AI Impacting Gross Margins
- Summary: Downgrade citing AI pressure on Cisco's margins.
- Date: 2026-11-05 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxNenlRbU9KcTNickNGZy1DQ1dLTGlwb2FtaEhBZzlyRjBORUlwOWwxUEpCaG9Fbm10TGF5ZFk4RmNqQkZtQWYtbEFXR2FYUXlkNFVlaVpoOWpQVm1IempVdUVhb3ZLMjNkaE9OVEJjQlVsWnE3WnFLdEx6bDhjRlh4amY0YW5zWGs5YnJyLVhR?oc=5>

### Cisco (CSCO) Stock: $93.85, Down 1.95% Nov 6
- Summary: Stock fell 1.95% on Nov 6, indicating short-term downside pressure.
- Date: 2026-11-09 | Impact: low | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxOUUljLXJPM294NmduSEczbTNIMS1DZzRDQ3NoeThJVV8tbmJkTXBITFNNMVBpcGprVy01U01lRXBVQTBObVM5X2xyaVA3Y0FUY0dnTGhhdTNPQ3dyU0NseUtyMDI0NmlNQ1NLOXFiNUZnTWhsZjA0VmJTdFpFYnljbmFKN0d0RmFYM1B3cHhmYWltbTUtbU9nQUZvd05BUzZJbkE?oc=5>

### ETFs Are Net Sellers of Cisco Systems (CSCO) on Nov. 5
- Summary: ETFs sold Cisco shares, indicating negative market sentiment.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxQQmtjOTdBRE5SeER0WU80VFd4bDRZd2R6Z2hfSVFnR2JjTWVYWG5aQ0FBdDE1b1dFQVhaV1V1bVRadTN4TXluTkY4TTQ2NzE2ZkZhcTE1anQtcmdWc1ppTTUzOF9CWVVtT0FIOGVkcTVycFdIeC1hRDd3MmRVY3VGeWU4eFlZNUVKWHFsaElUbzFhdGs0MHhtS0djVQ?oc=5>

## CATALYSTS

### Cisco Q1 Earnings – Here’s What Analysts Expect from CSCO Stock amid AI Trade Concerns
- Summary: Cisco Q1 Earnings – Here’s What Analysts Expect from CSCO Stock amid AI Trade Concerns
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxNX05KdjBPVURfSHJqN3hQb0p4LURJX1NzWDFkeEJZNEFsM3FObmxWWms1Z0FGUFp4Ti1FZzZXRXpMM21aNE50bFoyTFhtOFRseEZ2X09IQ2RlYlZOQWRFYm5CaUd0dXJGalJXUC1rUGJMTEx5Q0dlbzJNSm5PRXNqSGczOU8zbmJ2aXVfMGNtVlVBMENEZnJXOE11cVBubnlmNl9wRklGU291VW5ZUVFTcnZiSQ?oc=5>

### Cisco Systems Has Suffered $145 Billion Wipeout. Will Earnings Change This?
- Summary: Cisco Systems Has Suffered $145 Billion Wipeout. Will Earnings Change This?
- Date: 2026-11-08 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0AFBVV95cUxOYW1LNThidjEtdnVGeXpMdVRUMUhaT1I0aUl6cElGM3B5SFFuNHZfV3BtRDJwVk9wY1lPZkpEVWJqTE5CMlJwa3l5TEVkd2dLNUM0NURCajRHMzB2V1E5WTFHaDlOak40YWx5ODhxZkh6ci1EM0dyUGl1VlctdTJoREFXQUxjdTB4eXJwYXVOU2E1TXZKSi16N2l0WlByX2RlMXVTUms5UkE2ZUNGU29acTM3cHRCdjJzaENkSWN0R3E5blZ3N1ROMzlybXNROEc2?oc=5>

### Cisco Stock Faces a Massive Earnings Test -- Options Traders Expect 8% Swing
- Summary: Cisco Stock Faces a Massive Earnings Test -- Options Traders Expect 8% Swing
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiogFBVV95cUxQZmRiT3c1SEVleXM2VW5od1pHeHFIZFFmc2M1S19mV2RjRVcwTHRXWnBEa2pVYjhMQVZrQVV4ZU5yMjVibUE2STcwX2F0dEpxblNoVDZMM3JTWUtZdVI1bWZWWlR4cUFJZ3JkSEJ0c3FUZXpfQVhIZGJUN3lFa0lEandLMUZIbTFPRU1lc1V4OElTT011TDBZTVNxN3NHbFNqUUE?oc=5>

### 1 Options Trade to Bet on Cisco Stock Ahead of Earnings on November 12 — and Get a Shot at a 128.57% Maximum Payout
- Summary: Options trade signals investor interest ahead of earnings, potentially influencing volatility.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi7AFBVV95cUxNS0hqbXdISTAwWng4ZjEtWW52V1RiZnRiYnVxWXB1X1JpZ19kMktObE4wU3dYOXpRamFQcXNRVTh1VkU0MG5uNnRCS0c1a2hSNE1rUHg0eTdxNnJOcHVmTzB1X0Q2ZkdLa19BSDMwTlp3dkhuZFFXdFd4MWRDYU1pcHI0LURWWERpNUNDaGpWbEt4STZMd3BQOE9CWWo4NXM3N00wVHdiTnptWWFubE5DMnpFMmxSbk9ZMzF5aDdFZ1huQmNHZzdzNjlVWnp1cU1hMlpCQWxEQWJMVm4yQmZTZkJHUmpUd1FNSnRtbA?oc=5>

### How Investors Are Reacting To Cisco Stock After Analyst Downgrade
- Summary: Investors react negatively to Cisco downgrade, impacting short-term sentiment.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxNc3plRmFVemkybDMwNkhvQ3BDSVphWjdfb1VGbng1cTg0akFrVzh1akR4R1FUdVFRZ3RyY2ZPTE9pN2VEMDF5VXB1UDVfNFROZjNPakYxa2F5cWtHeWg5SGNMUll0S042WUpwR2Fra0tRNTl5Qnd5OGZYeXdvNmx3NjNJd3dUS2dDdjVTNkN2QUZkMThFTXJmSDBLeWpFMHlkby1qTWpB?oc=5>

### What Analyst Projections for Key Metrics Reveal About Cisco (CSCO) Q1 Earnings
- Summary: Analyst forecasts for Cisco’s Q1 earnings indicate potential upside, suggesting stronger revenue and earnings than expected.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxNVkQtSVE2N2xBbTB6MGJZY1FMMURxeW55NW03eHR0YXNkSnBWUVg5Z08zWmppNHFlOW5pdExRajd4YnQ4YXpYSjhBVlo0QjhNQnZhNjdNd1BFVHhSYVFHeU1FNWQ0Rnh1QVZOWXlxb1RPVmhGSjZVcXY5cC1XaDdrYVNNN2xJUFZPMElnWWM2R1dXWjE0SUttNXZHcm4yRUV6SVQ5WHR3?oc=5>

### Morgan Stanley resets Cisco stock price target before earnings
- Summary: Morgan Stanley adjusts Cisco price target ahead of earnings, neutral impact.
- Date: 2026-11-06 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxPSDdLTmFtNnZ6YWJfQkxDNzNEQndNQTR0NVVlSlU5a1NNQWZaWjB3cl9FVUw4Q3hZeExiUEV4YmZMYjF6YTJTeEN0SDJTNnZHN1huV04tZUprUnF0eXA2MXNzQ0lXVGRuY2lKcGxXM2doRkpqcG1Zb2lxWUFzbExUSHEzbFZmWTM1bFdteDJPbk5qWnhZTUF5NXVVUnB2WkdzblRKNVYyUjdlSVZyak9rcUFucw?oc=5>

## RISKS

### How Low Can Cisco Stock Go?
- Summary: Speculation on Cisco stock’s lower bound raises concerns about potential downside risk.
- Date: 2026-11-04 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMihwFBVV95cUxPNHJjVFhEbG1IQmplZ3pOVFNXbzVtY01oT0ZCdm53QVAwV19kV2dVbi1HVVQyYWxReTNmQ2xIUEZwdFoxcVBvSWJBbjRPaERhbjVTNnFmY0ZUM3Q4U0RYZTVEQlhZbW44ZVhKVFNZQTNWT0t6SjVENlY4alYtUDZCWnYyQ0dqQzQ?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **CSCO** | **29.47** | **7.70** | **21.58** | **17.60** | **386,964,914,176.00 USD** | **38.67** |
| ANET | 49.60 | 14.21 | 41.36 | 58.50 | 233,754,705,920.00 USD | 34.80 |
| FFIV | 25.34 | 4.50 | 17.99 | 13.30 | 18,026,698,752.00 USD | 31.79 |
| HPE | 24.71 | 2.40 | 11.29 | 33.70 | 63,625,388,032.00 USD | 104.33 |

Peers fetched as_of: 2026-11-10; CSCO reuses existing data (market data as_of: 2026-11-10); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-12
- Next expected earnings: 2026-11-12 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-10

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-K
- Filing date: 2026-09-02
- Revenue (latest available single quarter): 12,844,000,000.00 USD; period 2018-04-29/2018-07-28; fiscal year/reporting period 2018/FY
- Net income (latest available single quarter): 3,373,000,000.00 USD; period 2026-01-25/2026-04-25; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/858877/000085887726000132/csco-20260725.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMiuAFBVV95cUxQdXlQLXVlWi1HdHF5OUF6SllhRXBWc19HWUdiY2luV05BRXdkaHBfYTh5QmRrX25kZ3p4QlZYa29PVHdLc2lpNWxrMExCUnZQQVhia3pKUE54RjVtZWhxXzFuNVJFX2tueDNYSmk4TmZmaDQxMDF1c1U0NzFtRFIwQnlZTjlocElyQk1hQ0xJZ1V0ZzN6TzVBVmRQOTVOWEdQZzZ5cS1Za2JwUEZJa3ZwOVRRN3lLZVJ1?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxNaUZoNjY4Sy13SHlPSFN1Mno0cWtaWFVDMDhDWm90TDRVcmpTSGc3dzh3M09GZ1g0bGRDdnpGVHk0WFlDUFc0WDNkaW9DYy11b2dhV2RuUEVOTTJpa3F2ZUhOdTVFaTJyUnZvWjY0Nmp1eTBWOWdldWJqOU1heXF0MlJvcUR4T1BLTDEwdXo0OEdsbXJJOGdZ?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxNd2JhNnJ3MTU4TTV4XzZWdUZVSFdZZWJGTW8xNXlZTGdYWEY5VG9jVmx2NTV5blFTUkU0R0gyMS1SLW9Dd095djJSWXVTQ0xCYURmR2R2c2JpLVhZZEQ3S09RamFPem5PbVVBVzdzNHZULWFJazB3Y0lQeXJnMS0yVGRKY05oUUpGNnBEZi01b3plUQ?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxNNmxUZjJVSDRsTWZrakJ0REVoVTJocTBrYlRaemh4MkV4Sk1DY0hETHFKYmJsNmxrd2VrZnJ2R1JEczV1VHVHaDhoNHM0Vl9feXY1UkFhWm9Qa01ySHVGaEhlWlUzY3ZzRmprcVRCZXFTd3k4V1RtbUE0SHJxUVBULUF6OGIydDBUZHBra2xZT2hfWTd0dGlRZ29pdUZJQQ?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxNLU8yTTBOZmdNWEVjd3BiajlPNEVEVTRqUElzRTR6UHFidEFMTmFlZFZRVldOM0RLbFM2dEN3dldoTGFLUFF2bHkxd1h5T1RTZm1NOFl5YXY3V1J1enRJSGUxRFl4dEstTzZ4am1LSGhGaU8tWm1tNHBrNzNzelJxNEhNVUJWNlRtUl96Nl8zOGM?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxNenlRbU9KcTNickNGZy1DQ1dLTGlwb2FtaEhBZzlyRjBORUlwOWwxUEpCaG9Fbm10TGF5ZFk4RmNqQkZtQWYtbEFXR2FYUXlkNFVlaVpoOWpQVm1IempVdUVhb3ZLMjNkaE9OVEJjQlVsWnE3WnFLdEx6bDhjRlh4amY0YW5zWGs5YnJyLVhR?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxOUUljLXJPM294NmduSEczbTNIMS1DZzRDQ3NoeThJVV8tbmJkTXBITFNNMVBpcGprVy01U01lRXBVQTBObVM5X2xyaVA3Y0FUY0dnTGhhdTNPQ3dyU0NseUtyMDI0NmlNQ1NLOXFiNUZnTWhsZjA0VmJTdFpFYnljbmFKN0d0RmFYM1B3cHhmYWltbTUtbU9nQUZvd05BUzZJbkE?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxQQmtjOTdBRE5SeER0WU80VFd4bDRZd2R6Z2hfSVFnR2JjTWVYWG5aQ0FBdDE1b1dFQVhaV1V1bVRadTN4TXluTkY4TTQ2NzE2ZkZhcTE1anQtcmdWc1ppTTUzOF9CWVVtT0FIOGVkcTVycFdIeC1hRDd3MmRVY3VGeWU4eFlZNUVKWHFsaElUbzFhdGs0MHhtS0djVQ?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxNX05KdjBPVURfSHJqN3hQb0p4LURJX1NzWDFkeEJZNEFsM3FObmxWWms1Z0FGUFp4Ti1FZzZXRXpMM21aNE50bFoyTFhtOFRseEZ2X09IQ2RlYlZOQWRFYm5CaUd0dXJGalJXUC1rUGJMTEx5Q0dlbzJNSm5PRXNqSGczOU8zbmJ2aXVfMGNtVlVBMENEZnJXOE11cVBubnlmNl9wRklGU291VW5ZUVFTcnZiSQ?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxOajdxTFFHUlRraWFsc0pSekZYRktYRFZVRnVEZDZWc0p0clZaRUNYMjFaMjVHVU9UQzZ0X1cwcE9hWFBLWjBuSGdiSFZ4dmMtcklIUG1YVzgyU19mVm13UnA2OXdZTVNlY2JDVGZMREVfUlVfTGtscTRLVlFhN1hBR2YyejZTLWhsakJSWktCZ09wQ0ZrbV9RVmZseGNZdG8?oc=5
- https://news.google.com/rss/articles/CBMi0AFBVV95cUxOYW1LNThidjEtdnVGeXpMdVRUMUhaT1I0aUl6cElGM3B5SFFuNHZfV3BtRDJwVk9wY1lPZkpEVWJqTE5CMlJwa3l5TEVkd2dLNUM0NURCajRHMzB2V1E5WTFHaDlOak40YWx5ODhxZkh6ci1EM0dyUGl1VlctdTJoREFXQUxjdTB4eXJwYXVOU2E1TXZKSi16N2l0WlByX2RlMXVTUms5UkE2ZUNGU29acTM3cHRCdjJzaENkSWN0R3E5blZ3N1ROMzlybXNROEc2?oc=5
- https://news.google.com/rss/articles/CBMiogFBVV95cUxQZmRiT3c1SEVleXM2VW5od1pHeHFIZFFmc2M1S19mV2RjRVcwTHRXWnBEa2pVYjhMQVZrQVV4ZU5yMjVibUE2STcwX2F0dEpxblNoVDZMM3JTWUtZdVI1bWZWWlR4cUFJZ3JkSEJ0c3FUZXpfQVhIZGJUN3lFa0lEandLMUZIbTFPRU1lc1V4OElTT011TDBZTVNxN3NHbFNqUUE?oc=5
- https://news.google.com/rss/articles/CBMi7AFBVV95cUxNS0hqbXdISTAwWng4ZjEtWW52V1RiZnRiYnVxWXB1X1JpZ19kMktObE4wU3dYOXpRamFQcXNRVTh1VkU0MG5uNnRCS0c1a2hSNE1rUHg0eTdxNnJOcHVmTzB1X0Q2ZkdLa19BSDMwTlp3dkhuZFFXdFd4MWRDYU1pcHI0LURWWERpNUNDaGpWbEt4STZMd3BQOE9CWWo4NXM3N00wVHdiTnptWWFubE5DMnpFMmxSbk9ZMzF5aDdFZ1huQmNHZzdzNjlVWnp1cU1hMlpCQWxEQWJMVm4yQmZTZkJHUmpUd1FNSnRtbA?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxNc3plRmFVemkybDMwNkhvQ3BDSVphWjdfb1VGbng1cTg0akFrVzh1akR4R1FUdVFRZ3RyY2ZPTE9pN2VEMDF5VXB1UDVfNFROZjNPakYxa2F5cWtHeWg5SGNMUll0S042WUpwR2Fra0tRNTl5Qnd5OGZYeXdvNmx3NjNJd3dUS2dDdjVTNkN2QUZkMThFTXJmSDBLeWpFMHlkby1qTWpB?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxNVkQtSVE2N2xBbTB6MGJZY1FMMURxeW55NW03eHR0YXNkSnBWUVg5Z08zWmppNHFlOW5pdExRajd4YnQ4YXpYSjhBVlo0QjhNQnZhNjdNd1BFVHhSYVFHeU1FNWQ0Rnh1QVZOWXlxb1RPVmhGSjZVcXY5cC1XaDdrYVNNN2xJUFZPMElnWWM2R1dXWjE0SUttNXZHcm4yRUV6SVQ5WHR3?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxPSDdLTmFtNnZ6YWJfQkxDNzNEQndNQTR0NVVlSlU5a1NNQWZaWjB3cl9FVUw4Q3hZeExiUEV4YmZMYjF6YTJTeEN0SDJTNnZHN1huV04tZUprUnF0eXA2MXNzQ0lXVGRuY2lKcGxXM2doRkpqcG1Zb2lxWUFzbExUSHEzbFZmWTM1bFdteDJPbk5qWnhZTUF5NXVVUnB2WkdzblRKNVYyUjdlSVZyak9rcUFucw?oc=5
- https://news.google.com/rss/articles/CBMihwFBVV95cUxPNHJjVFhEbG1IQmplZ3pOVFNXbzVtY01oT0ZCdm53QVAwV19kV2dVbi1HVVQyYWxReTNmQ2xIUEZwdFoxcVBvSWJBbjRPaERhbjVTNnFmY0ZUM3Q4U0RYZTVEQlhZbW44ZVhKVFNZQTNWT0t6SjVENlY4alYtUDZCWnYyQ0dqQzQ?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
