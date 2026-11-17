# GOOGL Intelligence Report

- ticker: **GOOGL**
- Report as_of: **2026-11-16**
- Market data as_of: **2026-11-16**
- Quant sources: https://finance.yahoo.com/quote/GOOGL/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/GOOGL/key-statistics/
- AI analysis snapshot as_of: **2026-11-16**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-17T06:30:07.684348+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 2, 'ai': 11, 'unknown': 0, 'irrelevant': 12})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **6** exact headline/source/date matches; prior report **20261116T043911Z-b81cfeb4/GOOGL** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 13 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 28.0%; oldest publication 2026-11-12

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 283.7200 |
| Return 1D (%) | -4.0741 |
| Return 1W (%) | -1.5374 |
| Return 1M (%) | -16.6975 |
| Return YTD (%) | -9.1783 |
| Return 1Y (%) | 2.9116 |
| Annualized volatility (%) | 33.6645 |
| Beta vs SPY | 1.3162 |
| Max drawdown (%) | -30.6204 |
| Sharpe (rf=0) | 0.1629 |
| Downside deviation (rf=0, %) | 23.8717 |
| Sortino (rf=0) | 0.2297 |
| Historical VaR 95% (1D, %) | 3.0970 |
| Historical ES 95% (1D, %) | 4.8033 |
| Correlation vs SPY | 0.5383 |
| Tracking error vs SPY (%) | 28.7038 |
| P/E (trailing) | 14.82 |
| P/B | 5.29 |
| EV/EBITDA | 18.28 |
| Revenue growth (%) | 24.70 |
| Forward P/E (estimate) | 18.69 |
| Gross margin (%) | 60.86 |
| Operating margin (%) | 33.32 |
| Return on equity (%) | 44.29 |
| Free cash flow yield (%) | -0.03 |
| MA50 | 327.0910 |
| Close vs MA50 (%) | -13.2596 |
| MA200 | 337.9318 |
| Close vs MA200 (%) | -16.0422 |
| RSI (14, Wilder) | 34.4552 |
| MACD (12,26) | -12.2903 |
| MACD signal (9) | -13.3077 |
| MACD histogram | 1.0174 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'GOOGL': 283, 'SPY': 283}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 283.7200 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -4.0741 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -1.5374 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -16.6975 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -9.1783 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 2.9116 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 33.6645 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 23.8717 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.2297 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.0970 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 4.8033 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5383 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 28.7038 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.3162 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -30.6204 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.1629 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 18.6895 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 60.8570 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 33.3210 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 44.2860 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: -0.0333 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 14.8157 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 34.4552 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 1.0174 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -13.2596 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -16.0422 -> Clearly below the moving-average trend level.

## TAILWINDS

### Alphabet Climbs 3% as NVIDIA’s Leadership Shake-Up Puts Google’s AI Chips in the Spotlight; Microsoft Gains 2%, Amazon Ticks Up
- Summary: Alphabet Climbs 3% as NVIDIA’s Leadership Shake-Up Puts Google’s AI Chips in the Spotlight; Microsoft Gains 2%, Amazon Ticks Up
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxQeUxVUGczQUl6QzBJeEt1N29mdHVLMHBoMUVjWmJjUHhkclB3YVNTSksxN05oZnZrUmlZV0Y5X0xhai1NcFRDZ0hlWl9vWlp2UTdXNTRUSDF0bktKeGFSdGg0WmJScUpHdEFvdUVKVkd3NVcxMHY4MHM4aHkwYURtM1Z0SHJBVkFqMHdWNkJPTWxiN1JXYzJsMy1oeDNYeHNt?oc=5>

### Google Stock (GOOGL) Rises 1.8% as Nvidia CEO Resigns (Nov 12)
- Summary: Google Stock (GOOGL) Rises 1.8% as Nvidia CEO Resigns (Nov 12)
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiggFBVV95cUxNeEs0VHBWRU1Ib2lpY1ViVTVmNTJocFZtdEh2dWIyeWxnSlY0MzE1U3J6LW43dTVRT1RJeFh0Zl9IS19tS19ic3UzR2drcWprN2U0b3labzFFYWtDanB3dzk0T0R0OFlnVkNxWnZBOGxIN29XMDNaVmJibEYxdTY1dzJn?oc=5>

### Alphabet Inc-CL A (NASDAQ:GOOGL): A GARP Screen Standout
- Summary: Alphabet is highlighted as a GARP standout, suggesting attractive valuation and growth prospects.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxPLUtfTkUzNFpRWDJSYjFpS3Bjc0RBbjM0c3RHcTRQODd6STJjMXoxSm9DSzJSM2dmek9SRi1BaDF6WlRURGU2RFBXZ1I0Y2JNaGRRblZyYnlMUkNDRE1odWVxNXZsUWloQTdKZk9ndUM5T004WS1ndldvTWoyMm01Q2hXeXl1OTRhSVFrMVVDSTVJU1QyMnBLTkpPSktrRHl2bGgxVDlOajY?oc=5>

### Alphabet Draws $5 Billion in Orders as AI Frenzy Builds
- Summary: Alphabet secures $5B in orders, boosting AI revenue prospects.
- Date: 2026-11-12 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxOaFJOMTVYNnlES1ZxSXJxcVg1SzFycEdEaDN5OGlKOFFGTHpCTjU3ZVp6NDZPY25yNmRncjlYc01fNWNucGNhU1Ezd0JOMDNrZ3lRdVZzT3BGUm5hMHJDWDdLYzM0THRCUWNYWUFyMFVCYWR0MkpEOGRkbVRBdVhpQWh5d0RfMXhoVHRoQ3NTSWxULV9nVWZtSFRtUQ?oc=5>

## HEADWINDS

### Alphabet GOOG Stock Extends Decline as $200B Infrastructure Spending and Google Anthropic Investment Raise Concerns
- Summary: Stock decline driven by concerns over large infrastructure spend and Anthropic investment.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi7gFBVV95cUxQbEd0QmItd1VBSm5iUmNyUnU4RmRCWHhUczRMQndSaktERGY1WFFjS0NTMG5TbUNjdE1MSnUycHl6STBPT1dKdjZuT3hDYUFDMnFqdmdxU0Q4ZVFNWl91bkJMRHEwMk4xVmg5cjdHUVJlQ1lQZURUUnZQd0dIREtHN3MtYzRBU19DaXlfVVBYWmg1emdBU2pkZVNxTXpmWkhKNGpfNlJ4UERpZXlibndVdExjb1VWWlBlb0J2enk1cWNHc04taTRRMzB2MVFnNzZ0bXBrck4tRHcyT0gtNVBRQTMtdE1LZ3owZmhPSGl3?oc=5>

### GOOGL declines as momentum remains weak and oversold Stoch RSI hints at near-term reaction
- Summary: Stock falls amid weak momentum and oversold technical signals.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxQY2o4YmxBM0VxeFpPa1dPNU9hRUg2ZjYtRjY3YnZCSkdwNDV4M1ZoWDMzWHV5NlRxVjYwRWEyZEpFRTNPYXdrSEp6UDBXa1hOVkZMcVdnczNXdVJhUjNRbTNrRVlpNm0wdDlSdEZVNEN6UUdrZ3JSd1FQTkFJc0I3VjZMLUJxenFHU3ZXdFhfV2o?oc=5>

### Alphabet Stocks Decline 3.1% as $10 Billion Anthropic Buy Lifts Stake Before IPO
- Summary: Alphabet shares fell 3.1% amid Anthropic stake announcement.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi1AFBVV95cUxPRW1mUXB0RVhOTnNkbE5OUHV0YnlQbkhFb0dHenhPM1YzQ0lIWEMzdm5Hc1R1eG5SdkpjV050eVV3ZlF3SThyQl91OENxRWJPaXY0QTRNTEhfM2FJeVJhV3dBWHFsUlc1aERQN0RWMWV6SXVjY2gzNUdmYkRYMzdNbHpoVXpCVkhNYjd2S3g3QmR6UnFiRVc2YVJnLVFXMTNiYi1OQzJJUkhiaWZhMEdKb19JRkJTaXkxaFdBSVlPU1dPNmh1M0JVQndQMXE4V29neWhBbQ?oc=5>

### Alphabet Inc Class A Stock (GOOGL) Moved Down by 3.52% on Nov 16: Facts Behind the Movement
- Summary: Alphabet shares dropped 3.52% on Nov 16, market reaction noted.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMijAFBVV95cUxPTDYzRmlGcFVDdVFkOG1iSE1QVGc5ZkZOclNYNkY2SWhla3hwVTlwd2x2MEY5ZXNIYTNGTGFoaDZVRUVOWTZjc0lUdXdJRmhpc3MzX01fRFA1eTFFLWhVQ2dET21sQVAyUnZvcTY4TjNCVTROSk1zbzQ0ZzZHWHpLOW9hWEpFUUVsRU9DMA?oc=5>

## CATALYSTS

### Alphabet Inc. (GOOGL) is Attracting Investor Attention: Here is What You Should Know
- Summary: Alphabet is drawing investor attention, indicating analyst interest.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxQVTh2bVNCT0xOVGQwaDBMbm80bHdBd2cxRWhmT3d1SXdXS0ExZG0zUEJiTlg3TEVqSUNPYV9yanhqZjEzeVJYNTh6M3VMVjVZVUgyZUhqMlBIOXQ3QWtMWVZsNHAxV3BDY29DTmh4UkhmcDRtWUlQR1h4T05GZ0NIM29FNjUxa3YyenlrOWhCeFBzSC1pYVhQTTJEcTNqdGpLeGo5NklB?oc=5>

### Should You Buy Alphabet Stock Now That Google Will Let Customers Run Its AI Chips in Their Own Data Centers?
- Summary: Alphabet will allow customers to run its AI chips in their own data centers, expanding product offerings.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi5AFBVV95cUxQbVNibFJDOERyT3YyOGk0aFZBeS1DX3RaZFV3SmFlbGlRcnQtUmhBakxZN25HUmhvaHJyeGJFUHpsVnlMd3JwYmVPTnBZbnhaVEJrQzQxZHY2R3dFamd4aUppT2M2bXltOF95d05oSGhxek95RTkzTkxmS1ZwTVdjWG4zX3NtRXRsRjFJZ0dXMmVKNHM4aUlfalhSaV9qazgxd2JZSmZFVl9OU1NubnlEVktReDZwLThiN3BFRXdzR21xNHdpMms1N0hsZ01ZZnd2T3NMeHgtcU9aSVNmS0dHWklGZ3Q?oc=5>

### Sundar Pichai Reported Alphabet's Cloud Revenue Grew 103% Last Quarter While the Gemini App Reached 1 Billion Monthly Users. Is Google Cloud Becoming a Bigger Growth Driver Than Search?
- Summary: Alphabet's cloud revenue surged 103% last quarter, with Gemini app hitting 1B monthly users, indicating potential shift toward cloud as a growth engine.
- Date: 2026-11-14 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxOcnhHbENNM0g3ZVpYcW9xczlBMkpXUzItNWp4WTF4QkJzbjZVbFA3dS04em91RU9EREsyN2ZTdVphSjZTYnFBdmM4YnF0dG5FaHNTNzNHYXJhWF9LM0pua1o3bl9zYjFqODQxU3Y4bzNRTnJYQnRaVkRJamV6NXRINFQ1VDd4Zl9JQmx5TkEwbTcwS2QxTkFWLQ?oc=5>

## RISKS

### Apaloosa adds Oracle, exits Advanced Micro, raises stake in NVIDIA, cuts in Alphabet among Q3 moves
- Summary: Apaloosa reduced its Alphabet stake, signaling potential investor concern.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMi8AFBVV95cUxQRDlpQXliQ1JMWEpKakVSaEhXSkJBUkROUE9LdGp0Qk1RTnZvaDhCMm1HQ2NFZDVGODUwdUR1cktSQmppQk1SZzNBd3dPcVZfb1p5UDFKMmYydi1vOXk1dVN1YjJhUGFRWHRqYkpwd3Y2YmVwb1VYdkViWG4tbmEtcHNDcHl2Nl9qNHNCRGNoLVk4M0JSWnRuVGxFLWNrajM0Ql9LWVdiaFNQTl9LeDhnbGQ5VElRNzJPNVpkZWthOTBQbHBacVZpaXBtWG5oaFJxZnJxcGs3Y2VCcVlja1ZiRUlaUUNCQ0wzQVVOQWhoRFY?oc=5>

### Seth Klarman's Baupost cuts stake in Alphabet, Union Pacific; adds to CME among Q3 moves
- Summary: Major investor reduces Alphabet stake, indicating potential downside pressure.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxNQnd2WHdjX3ZJRFQxRHdmVmFKZ3pkOWRHQ3dFWURoSEJuMGhOdlJ1d1ZoMlY2M2NDcW1vX1E1RXF1Zkl5Mi1idUNpVjVOalZNbzJKUWR4VzgtbEx3TTQ2aldMcDdpN3ZZcHdtLThpdkppbmdUcUtrMGpoNVlCeXJTUy1uS04yQk9MMmFuaUlaSGh2clpyMFZ5RVZITE9DM1ZTaGpWR281VkJhZ3N5QkJfYjQwYlNQS0RUdlJLMUhSRWY?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **GOOGL** | **14.82** | **5.29** | **18.28** | **24.70** | **3,488,053,460,992.00 USD** | **2.91** |
| META | 21.89 | 5.88 | 14.06 | 26.10 | 1,601,254,981,632.00 USD | 3.13 |
| MSFT | 27.03 | 8.18 | 19.04 | 18.80 | 3,846,694,502,400.00 USD | 2.37 |
| AMZN | 20.84 | 4.54 | 16.21 | 12.10 | 2,787,086,172,160.00 USD | 9.83 |

Peers fetched as_of: 2026-11-16; GOOGL reuses existing data (market data as_of: 2026-11-16); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-28
- Next expected earnings: 2027-02-03 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-16

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-29
- Revenue (latest available single quarter): 127,577,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 26,468,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1652044/000165204426000084/goog-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMioAFBVV95cUxQeUxVUGczQUl6QzBJeEt1N29mdHVLMHBoMUVjWmJjUHhkclB3YVNTSksxN05oZnZrUmlZV0Y5X0xhai1NcFRDZ0hlWl9vWlp2UTdXNTRUSDF0bktKeGFSdGg0WmJScUpHdEFvdUVKVkd3NVcxMHY4MHM4aHkwYURtM1Z0SHJBVkFqMHdWNkJPTWxiN1JXYzJsMy1oeDNYeHNt?oc=5
- https://news.google.com/rss/articles/CBMiggFBVV95cUxNeEs0VHBWRU1Ib2lpY1ViVTVmNTJocFZtdEh2dWIyeWxnSlY0MzE1U3J6LW43dTVRT1RJeFh0Zl9IS19tS19ic3UzR2drcWprN2U0b3labzFFYWtDanB3dzk0T0R0OFlnVkNxWnZBOGxIN29XMDNaVmJibEYxdTY1dzJn?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxPLUtfTkUzNFpRWDJSYjFpS3Bjc0RBbjM0c3RHcTRQODd6STJjMXoxSm9DSzJSM2dmek9SRi1BaDF6WlRURGU2RFBXZ1I0Y2JNaGRRblZyYnlMUkNDRE1odWVxNXZsUWloQTdKZk9ndUM5T004WS1ndldvTWoyMm01Q2hXeXl1OTRhSVFrMVVDSTVJU1QyMnBLTkpPSktrRHl2bGgxVDlOajY?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxOaFJOMTVYNnlES1ZxSXJxcVg1SzFycEdEaDN5OGlKOFFGTHpCTjU3ZVp6NDZPY25yNmRncjlYc01fNWNucGNhU1Ezd0JOMDNrZ3lRdVZzT3BGUm5hMHJDWDdLYzM0THRCUWNYWUFyMFVCYWR0MkpEOGRkbVRBdVhpQWh5d0RfMXhoVHRoQ3NTSWxULV9nVWZtSFRtUQ?oc=5
- https://news.google.com/rss/articles/CBMi7gFBVV95cUxQbEd0QmItd1VBSm5iUmNyUnU4RmRCWHhUczRMQndSaktERGY1WFFjS0NTMG5TbUNjdE1MSnUycHl6STBPT1dKdjZuT3hDYUFDMnFqdmdxU0Q4ZVFNWl91bkJMRHEwMk4xVmg5cjdHUVJlQ1lQZURUUnZQd0dIREtHN3MtYzRBU19DaXlfVVBYWmg1emdBU2pkZVNxTXpmWkhKNGpfNlJ4UERpZXlibndVdExjb1VWWlBlb0J2enk1cWNHc04taTRRMzB2MVFnNzZ0bXBrck4tRHcyT0gtNVBRQTMtdE1LZ3owZmhPSGl3?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxQY2o4YmxBM0VxeFpPa1dPNU9hRUg2ZjYtRjY3YnZCSkdwNDV4M1ZoWDMzWHV5NlRxVjYwRWEyZEpFRTNPYXdrSEp6UDBXa1hOVkZMcVdnczNXdVJhUjNRbTNrRVlpNm0wdDlSdEZVNEN6UUdrZ3JSd1FQTkFJc0I3VjZMLUJxenFHU3ZXdFhfV2o?oc=5
- https://news.google.com/rss/articles/CBMi1AFBVV95cUxPRW1mUXB0RVhOTnNkbE5OUHV0YnlQbkhFb0dHenhPM1YzQ0lIWEMzdm5Hc1R1eG5SdkpjV050eVV3ZlF3SThyQl91OENxRWJPaXY0QTRNTEhfM2FJeVJhV3dBWHFsUlc1aERQN0RWMWV6SXVjY2gzNUdmYkRYMzdNbHpoVXpCVkhNYjd2S3g3QmR6UnFiRVc2YVJnLVFXMTNiYi1OQzJJUkhiaWZhMEdKb19JRkJTaXkxaFdBSVlPU1dPNmh1M0JVQndQMXE4V29neWhBbQ?oc=5
- https://news.google.com/rss/articles/CBMijAFBVV95cUxPTDYzRmlGcFVDdVFkOG1iSE1QVGc5ZkZOclNYNkY2SWhla3hwVTlwd2x2MEY5ZXNIYTNGTGFoaDZVRUVOWTZjc0lUdXdJRmhpc3MzX01fRFA1eTFFLWhVQ2dET21sQVAyUnZvcTY4TjNCVTROSk1zbzQ0ZzZHWHpLOW9hWEpFUUVsRU9DMA?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxQVTh2bVNCT0xOVGQwaDBMbm80bHdBd2cxRWhmT3d1SXdXS0ExZG0zUEJiTlg3TEVqSUNPYV9yanhqZjEzeVJYNTh6M3VMVjVZVUgyZUhqMlBIOXQ3QWtMWVZsNHAxV3BDY29DTmh4UkhmcDRtWUlQR1h4T05GZ0NIM29FNjUxa3YyenlrOWhCeFBzSC1pYVhQTTJEcTNqdGpLeGo5NklB?oc=5
- https://news.google.com/rss/articles/CBMi5AFBVV95cUxQbVNibFJDOERyT3YyOGk0aFZBeS1DX3RaZFV3SmFlbGlRcnQtUmhBakxZN25HUmhvaHJyeGJFUHpsVnlMd3JwYmVPTnBZbnhaVEJrQzQxZHY2R3dFamd4aUppT2M2bXltOF95d05oSGhxek95RTkzTkxmS1ZwTVdjWG4zX3NtRXRsRjFJZ0dXMmVKNHM4aUlfalhSaV9qazgxd2JZSmZFVl9OU1NubnlEVktReDZwLThiN3BFRXdzR21xNHdpMms1N0hsZ01ZZnd2T3NMeHgtcU9aSVNmS0dHWklGZ3Q?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxOcnhHbENNM0g3ZVpYcW9xczlBMkpXUzItNWp4WTF4QkJzbjZVbFA3dS04em91RU9EREsyN2ZTdVphSjZTYnFBdmM4YnF0dG5FaHNTNzNHYXJhWF9LM0pua1o3bl9zYjFqODQxU3Y4bzNRTnJYQnRaVkRJamV6NXRINFQ1VDd4Zl9JQmx5TkEwbTcwS2QxTkFWLQ?oc=5
- https://news.google.com/rss/articles/CBMi8AFBVV95cUxQRDlpQXliQ1JMWEpKakVSaEhXSkJBUkROUE9LdGp0Qk1RTnZvaDhCMm1HQ2NFZDVGODUwdUR1cktSQmppQk1SZzNBd3dPcVZfb1p5UDFKMmYydi1vOXk1dVN1YjJhUGFRWHRqYkpwd3Y2YmVwb1VYdkViWG4tbmEtcHNDcHl2Nl9qNHNCRGNoLVk4M0JSWnRuVGxFLWNrajM0Ql9LWVdiaFNQTl9LeDhnbGQ5VElRNzJPNVpkZWthOTBQbHBacVZpaXBtWG5oaFJxZnJxcGs3Y2VCcVlja1ZiRUlaUUNCQ0wzQVVOQWhoRFY?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxNQnd2WHdjX3ZJRFQxRHdmVmFKZ3pkOWRHQ3dFWURoSEJuMGhOdlJ1d1ZoMlY2M2NDcW1vX1E1RXF1Zkl5Mi1idUNpVjVOalZNbzJKUWR4VzgtbEx3TTQ2aldMcDdpN3ZZcHdtLThpdkppbmdUcUtrMGpoNVlCeXJTUy1uS04yQk9MMmFuaUlaSGh2clpyMFZ5RVZITE9DM1ZTaGpWR281VkJhZ3N5QkJfYjQwYlNQS0RUdlJLMUhSRWY?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
