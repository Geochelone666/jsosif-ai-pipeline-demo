# MU Intelligence Report

- ticker: **MU**
- Report as_of: **2026-11-11**
- Market data as_of: **2026-11-11**
- Quant sources: https://finance.yahoo.com/quote/MU/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/MU/key-statistics/
- AI analysis snapshot as_of: **2026-11-11**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-12T05:42:45.508205+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 23, 'rule': 0, 'ai': 14, 'unknown': 0, 'irrelevant': 9})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **5** exact headline/source/date matches; prior report **20261111T043601Z-d14951e6/MU** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'directional_claim_without_event_type': 1}
- RSS source audit (metadata only, not article fact-checking): 23 unique headlines; 10 named publishers; 2 exact duplicates; 23 HTTPS source links; largest publisher share 30.43%; oldest publication 2026-11-09

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 811.3000 |
| Return 1D (%) | 11.8865 |
| Return 1W (%) | 2.0208 |
| Return 1M (%) | -21.1441 |
| Return YTD (%) | 184.4656 |
| Return 1Y (%) | 236.8676 |
| Annualized volatility (%) | 84.2843 |
| Beta vs SPY | 3.3964 |
| Max drawdown (%) | -45.8952 |
| Sharpe (rf=0) | 1.8662 |
| Downside deviation (rf=0, %) | 52.5275 |
| Sortino (rf=0) | 2.9945 |
| Historical VaR 95% (1D, %) | 7.0090 |
| Historical ES 95% (1D, %) | 10.3312 |
| Correlation vs SPY | 0.5532 |
| Tracking error vs SPY (%) | 77.5371 |
| P/E (trailing) | 10.91 |
| P/B | 6.63 |
| EV/EBITDA | 8.08 |
| Revenue growth (%) | 379.30 |
| Forward P/E (estimate) | 3.90 |
| Gross margin (%) | 80.72 |
| Operating margin (%) | 74.59 |
| Return on equity (%) | 88.26 |
| Free cash flow yield (%) | 3.17 |
| MA50 | 950.4332 |
| Close vs MA50 (%) | -14.6389 |
| MA200 | 761.8851 |
| Close vs MA200 (%) | 6.4859 |
| RSI (14, Wilder) | 45.1022 |
| MACD (12,26) | -61.9354 |
| MACD signal (9) | -52.1696 |
| MACD histogram | -9.7658 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'MU': 280, 'SPY': 280}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 811.3000 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 11.8865 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 2.0208 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -21.1441 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 184.4656 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 236.8676 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 84.2843 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 52.5275 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 2.9945 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 7.0090 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 10.3312 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.5532 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 77.5371 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 3.3964 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -45.8952 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.8662 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 3.9050 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 80.7160 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 74.5860 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 88.2600 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 3.1746 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 10.9148 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 45.1022 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -9.7658 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -14.6389 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 6.4859 -> Clearly above the moving-average trend level.

## TAILWINDS

### I Still Think Micron Stock Is a Buy. Here's the Price at Which I'd Sell It.
- Summary: Analyst expresses bullish view and target sell price for Micron shares.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxNY2stTE5ZNjFmLXlvbkxTMFNzZXduV1BwdDdRRmV6YnBPa2xlWTZqUjhaNmoxb0J0MG10THZQSXBDWEVUWkgwdVpUVE9Zd3dDYlh5aWVrUkZiS3E4LURZbV9xMS1pSlpVU1ZjVnpUbXNIelR6aldwWlVYdFBpWnNkbHplTUFLeEtpNkFmQTkzN1hMN3hwd0lnX0dYang5a3FzQ256SzNELWpwTDhzNl81Vk5oX2ZDbDA?oc=5>

### Micron Technology Inc Stock (MU) Moved Up by 5.73% on Nov 9: What Investors Need To Know
- Summary: Micron shares rose 5.73% on Nov 9, prompting investors to review the stock’s recent performance and potential catalysts for the uptick.
- Date: 2026-11-09 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiAFBVV95cUxQbXA3S3lxWkhQTUNQYmpqd1JSUFNUelRadTUtQzJLYWJmX0FTS3pGalBEWGFTWHNQMG5jVmZhQkRnenVrQ1E5ZThQUXRydkxzSnoxR25zN2kyZTdxdU5oYUFVY1MxRUtXdXViX05fQmNQQ2NmTV9NcXlVcWVCaGExSEV4VkJ1U20z?oc=5>

### Memory Stocks Surge, Micron Jumps 11% as Morgan Stanley Says Valuation Pullback Improves Memory Stocks' Risk-Reward
- Summary: Micron shares rise 11% amid positive valuation outlook from Morgan Stanley.
- Date: 2026-11-11 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi3wFBVV95cUxPdkViZFRjOXNrTkdFZHRYWVRfUFo5TXFGTDUzQVV1LTJLVU5MSkdEalBhOVM3eE5EVnNSQnRpR3NaTmc4aGhSTTdkTmVtMkhOZmlPUmRKMnIwRnlCc1ZtR1c1THk3Szk2MnF1a0lpOWtqZWp5N280cE1GMkpiWnhTVFd6b1hicGNZME1XNTJOWndpSHZXc1JPeFl4RktPbEV4azlVaU9yZUE2UGVmMnY0NnEyaExoV2lESndJdW5PblRfZFZOSVVwQTNac1VuUEhQZTBYV3dXY1llZXJ3WGFF?oc=5>

### Micron: Buy The Panic, Not The AI Doomsday Story
- Summary: Analyst urges buying Micron amid AI hype, citing undervaluation and strong fundamentals.
- Date: 2026-11-11 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMikAFBVV95cUxPWDlaR1RRb0hFQ3BxNzV5aHpUaEdpdkI5cEhfcmhINVVDSmpzdGlLbWk3UFlIcEtlSVFCWXhDV2ZBbEdKai0tNE8wM3JieDZJcUlETWZwdVltbF8zc0JSMkk1bEQwSzhOSllQaktucEYyOEVPaG1iWU12Z08wWnJLdUtQN3N4RUs3a1JVVWZxVC0?oc=5>

### Micron Is Rebounding. Goldman Prefers These Memory Stocks.
- Summary: Micron’s stock rebounds, attracting Goldman’s preference for memory stocks, indicating positive market sentiment.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMifkFVX3lxTFB2bWhjUktMQU1qZzVGbWF5ZE9XNmdGVmtUVU5EMUozbl9pNlJRZnJjOWl6N2ZLLUEwQVMyWEZpa19RT1NLMXZzbVZxTTlGd2lKMDNLa3FKSUUwQi1EQllKbndwY20zMUF3Q0tkeHFXSnUwQllJdGhiRjJKY3I2dw?oc=5>

### Why Micron Technology Stock Gained On Monday
- Summary: Micron’s shares gained on Monday, reflecting favorable market conditions.
- Date: 2026-11-09 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxNb1hrRzc0OGpMSFBjQ0lmcVpCY3YwMGZ2dFhHSXRaWHU4b0xubTNHaE8yUzBxT3BBQk5xcnZrSHY0QWpKVUdzb1lUMFRldWpSLVpEbFg2QXZRM0ZtN0tKczJnaFJDanlKZmROQWN5SzdnNUU4VEVpamI3WWFLdkpTQmVrQUk4QUpGWXQzUXM4eWtSVG5zU2prOER0TVNXeThH?oc=5>

### Micron Technology climbs 13% as one-month slide reverses (MU:NASDAQ)
- Summary: Micron’s stock climbs 13%, reversing a one-month decline, signaling strong investor confidence.
- Date: 2026-11-11 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxPSExVYU1oeW91UFFKa2VQNUx1ekRnOGFlVThvR3lGTmtxZnhQSXRsaHl4eG1YV2VGTkdxN0pZOWJmQnl5WTVXWDBaYy1IYjc4cTJ1MDZHVXAtbnZtRF96eXZfSnFVNWVwNl9iYlo1bXBjeV9XcHZmNGotRlJNNEt4al9wSWw0bTFGQXZUMGFfQXprVHhyeFNWM0lEdWJvUUFTRTM0?oc=5>

### Micron Stock Is Down 40% From Its Peak After the Sell-Off. History Says This Is What Happens Next.
- Summary: Micron’s shares fell 40% post sell-off, suggesting a potential rebound per historical patterns.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxOc3hPSUpZNHRWLXNkRFpvYzl2YWZ4RDVWeThpUkVLX0Z3aUdmc01GTktyNWw4MHpNWHZaU04tVTkxeG5VLTd2Um1qZGJ5QzFWNzN1MHdZaERSdGRieTdwOGI3djlfVXEyY2hYMTZRT1JFTkZXdFBXZ3dONE9oOTVuRGdYbmZfS2xGbEl2VGlHTlRsQlpm?oc=5>

### Why Micron Stock Popped Today
- Summary: Micron’s stock experienced a pop today, indicating positive market reaction.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMifEFVX3lxTFAyOUM1OGJlREtsc0h4T2phU0UyamlOdnRSUXRMdzFJWVhzRm9ZMDJTeUo3VXBlZVo1YXdBazFzeWgyRUNpRFRIaHhvOXBGeVdqMWZqby15LXZMZVNZTlhYaW1MSUtWZlhYdGwwRzRELU96RXR4Vk8zZmRRb2s?oc=5>

### Micron: Strong Buy Even Under Severe Cyclical Pessimism (NASDAQ:MU)
- Summary: Analyst upgrades Micron to strong buy amid market pessimism, citing resilient fundamentals.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxQWFJLdzdhVVoxMkFta2xWNU9IcjB5b29aanZIMkpHZHo3clZwYWpsTXdxOG5rZDItZzUtRkh0VDVibktvMDRxV3V4ZUI1NmJWNmNaQmJmS3kyWDdyYzNyeGN5XzdKMXdaeUVUcXlmMEVsX2RMUjFJZ2xySEh3M3loOXZrV2RieHFYNXVGbVRhNFc0UGw5R1ZzM01aQQ?oc=5>

### Micron: HBM Repricing Strengthens The Buy Case After The Selloff (NASDAQ:MU)
- Summary: Analyst notes HBM repricing boosts buy case post selloff, supporting positive outlook.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipwFBVV95cUxNNm9rUDU1R28zR2NubWRaeWdaYUl6dG4wWW9CTWpoNlNpUEtWRDAyUHVJRGdEeFVqa3FHNTJISkc4TGxLR3Nsc2YweC1aT1BKcEdhYjlLR09CRXFoRjJyRzZqSEkxV01BTFBrOERCWHBoODVocXItcGlJWjl4d1V2NmVvMHhJQ1BpVUNrVFlYejMyTUhTNDNiWmMtRTZyMExuVU94bGJUQQ?oc=5>

## HEADWINDS

### Micron Technology Stocks Slip 1.27% as Hot CPI Overshadows $1 Billion Anthropic Bet
- Summary: Micron shares fall 1.27% due to inflation concerns outweighing AI investment.
- Date: 2026-11-10 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxPb3ltSGpYNHg5X1N1VW5PMEJtTk5Ba0hkakhXWjdXOFRvVnp3aGxROFgyWHRheFZxMG1MY1YtT3RXN25hcTgwT2xaUEphbjJrVWI1UHgzZ1VxN1FLNXdjYm1yZTJtT2hjdjJRVDVtR01BT0c3R0RqanFYd1BQdnlRdm1KdktwZ0tOMmNxRndoRWVLSFhlci1MQWNCYU8?oc=5>

## CATALYSTS

### Micron Technology (MU) Commits $1 Billion To Landmark AI Infrastructure IPO
- Summary: Micron invests $1B in AI infrastructure IPO, signaling growth.
- Date: 2026-11-11 | Impact: high | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxORC1PS1FreEtDdjc3c0lRUTVvazRVVzBFVkNXYzNMMDBXRGV0R2Nfc1V5cjFlcnh6cHRhanE0a0dUbjByaGNBWExfcmpibDlYc1NoU3VYcjd2SzYzQ0hlcnh6WER0eXZUbHJQRUZ5WG5LS0NTRWxtTG1jcnJnMlVuOFJqaU1TbHg1dTFLLXdJQ21acXZ0MG5IMFZR?oc=5>

### Micron Technology (MU) Could Be 42% Undervalued Despite Board Retirement News
- Summary: Analysts suggest Micron may be undervalued despite board changes.
- Date: 2026-11-11 | Impact: medium | Horizon: medium | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxQd0FwdWhPal9UUHpiMk44MFFyUlpwbzBaZFl5VEFLTm5uZjRuTndoRkFZYmZtMm41M0x2SEVaNVdMcVpHdHBndVByeFpDTk1xOTVGcGkzY2Q2UXozRWtiWVZpY3pDNlVBd3p2aHR4VHVoSzF5ZlkzVWlDQ0FKNXFpMWk0eUJVMDRFa1FGQXAwaDAwMDhSYUJwejBR?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **MU** | **10.91** | **6.63** | **8.08** | **379.30** | **917,923,627,008.00 USD** | **236.87** |
| WDC | 11.02 | 12.53 | 18.52 | 55.50 | 117,279,219,712.00 USD | 84.65 |
| STX | 26.30 | 36.70 | 21.83 | 61.00 | 126,653,448,192.00 USD | 92.70 |
| NXPI | 20.57 | 5.62 | 13.99 | 19.30 | 67,930,804,224.00 USD | 35.20 |

Peers fetched as_of: 2026-11-11; MU reuses existing data (market data as_of: 2026-11-11); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-09-30
- Next expected earnings: 2026-12-23 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-11

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-K
- Filing date: 2026-10-09
- Revenue (latest available single quarter): 8,440,000,000.00 USD; period 2018-06-01/2018-08-30; fiscal year/reporting period 2018/FY
- Net income (latest available single quarter): 28,243,000,000.00 USD; period 2026-02-27/2026-05-28; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/723125/000072312526000023/mu-20260903.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMitwFBVV95cUxNY2stTE5ZNjFmLXlvbkxTMFNzZXduV1BwdDdRRmV6YnBPa2xlWTZqUjhaNmoxb0J0MG10THZQSXBDWEVUWkgwdVpUVE9Zd3dDYlh5aWVrUkZiS3E4LURZbV9xMS1pSlpVU1ZjVnpUbXNIelR6aldwWlVYdFBpWnNkbHplTUFLeEtpNkFmQTkzN1hMN3hwd0lnX0dYang5a3FzQ256SzNELWpwTDhzNl81Vk5oX2ZDbDA?oc=5
- https://news.google.com/rss/articles/CBMiiAFBVV95cUxQbXA3S3lxWkhQTUNQYmpqd1JSUFNUelRadTUtQzJLYWJmX0FTS3pGalBEWGFTWHNQMG5jVmZhQkRnenVrQ1E5ZThQUXRydkxzSnoxR25zN2kyZTdxdU5oYUFVY1MxRUtXdXViX05fQmNQQ2NmTV9NcXlVcWVCaGExSEV4VkJ1U20z?oc=5
- https://news.google.com/rss/articles/CBMi3wFBVV95cUxPdkViZFRjOXNrTkdFZHRYWVRfUFo5TXFGTDUzQVV1LTJLVU5MSkdEalBhOVM3eE5EVnNSQnRpR3NaTmc4aGhSTTdkTmVtMkhOZmlPUmRKMnIwRnlCc1ZtR1c1THk3Szk2MnF1a0lpOWtqZWp5N280cE1GMkpiWnhTVFd6b1hicGNZME1XNTJOWndpSHZXc1JPeFl4RktPbEV4azlVaU9yZUE2UGVmMnY0NnEyaExoV2lESndJdW5PblRfZFZOSVVwQTNac1VuUEhQZTBYV3dXY1llZXJ3WGFF?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxPWDlaR1RRb0hFQ3BxNzV5aHpUaEdpdkI5cEhfcmhINVVDSmpzdGlLbWk3UFlIcEtlSVFCWXhDV2ZBbEdKai0tNE8wM3JieDZJcUlETWZwdVltbF8zc0JSMkk1bEQwSzhOSllQaktucEYyOEVPaG1iWU12Z08wWnJLdUtQN3N4RUs3a1JVVWZxVC0?oc=5
- https://news.google.com/rss/articles/CBMifkFVX3lxTFB2bWhjUktMQU1qZzVGbWF5ZE9XNmdGVmtUVU5EMUozbl9pNlJRZnJjOWl6N2ZLLUEwQVMyWEZpa19RT1NLMXZzbVZxTTlGd2lKMDNLa3FKSUUwQi1EQllKbndwY20zMUF3Q0tkeHFXSnUwQllJdGhiRjJKY3I2dw?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxNb1hrRzc0OGpMSFBjQ0lmcVpCY3YwMGZ2dFhHSXRaWHU4b0xubTNHaE8yUzBxT3BBQk5xcnZrSHY0QWpKVUdzb1lUMFRldWpSLVpEbFg2QXZRM0ZtN0tKczJnaFJDanlKZmROQWN5SzdnNUU4VEVpamI3WWFLdkpTQmVrQUk4QUpGWXQzUXM4eWtSVG5zU2prOER0TVNXeThH?oc=5
- https://news.google.com/rss/articles/CBMikAFBVV95cUxPVE1LVjVKalFkQlVCVFVaU0Z6OWtfYW1ES0lMZmI5c1NPN213eFo3cXhqdWNiX2txVFpBc1FyUTk1ZV8wZ0pGWlV3NHB6X213a1BCODJYWUV4SExXMU1yOFQ1YV9VZF9qZGF2NDlQMkpnSDV4OFV2aFczUWF5QWdUR1pZVU9RTlJUc0Z6VEUyNFc?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxPSExVYU1oeW91UFFKa2VQNUx1ekRnOGFlVThvR3lGTmtxZnhQSXRsaHl4eG1YV2VGTkdxN0pZOWJmQnl5WTVXWDBaYy1IYjc4cTJ1MDZHVXAtbnZtRF96eXZfSnFVNWVwNl9iYlo1bXBjeV9XcHZmNGotRlJNNEt4al9wSWw0bTFGQXZUMGFfQXprVHhyeFNWM0lEdWJvUUFTRTM0?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxOc3hPSUpZNHRWLXNkRFpvYzl2YWZ4RDVWeThpUkVLX0Z3aUdmc01GTktyNWw4MHpNWHZaU04tVTkxeG5VLTd2Um1qZGJ5QzFWNzN1MHdZaERSdGRieTdwOGI3djlfVXEyY2hYMTZRT1JFTkZXdFBXZ3dONE9oOTVuRGdYbmZfS2xGbEl2VGlHTlRsQlpm?oc=5
- https://news.google.com/rss/articles/CBMifEFVX3lxTFAyOUM1OGJlREtsc0h4T2phU0UyamlOdnRSUXRMdzFJWVhzRm9ZMDJTeUo3VXBlZVo1YXdBazFzeWgyRUNpRFRIaHhvOXBGeVdqMWZqby15LXZMZVNZTlhYaW1MSUtWZlhYdGwwRzRELU96RXR4Vk8zZmRRb2s?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxQWFJLdzdhVVoxMkFta2xWNU9IcjB5b29aanZIMkpHZHo3clZwYWpsTXdxOG5rZDItZzUtRkh0VDVibktvMDRxV3V4ZUI1NmJWNmNaQmJmS3kyWDdyYzNyeGN5XzdKMXdaeUVUcXlmMEVsX2RMUjFJZ2xySEh3M3loOXZrV2RieHFYNXVGbVRhNFc0UGw5R1ZzM01aQQ?oc=5
- https://news.google.com/rss/articles/CBMipwFBVV95cUxNNm9rUDU1R28zR2NubWRaeWdaYUl6dG4wWW9CTWpoNlNpUEtWRDAyUHVJRGdEeFVqa3FHNTJISkc4TGxLR3Nsc2YweC1aT1BKcEdhYjlLR09CRXFoRjJyRzZqSEkxV01BTFBrOERCWHBoODVocXItcGlJWjl4d1V2NmVvMHhJQ1BpVUNrVFlYejMyTUhTNDNiWmMtRTZyMExuVU94bGJUQQ?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxPb3ltSGpYNHg5X1N1VW5PMEJtTk5Ba0hkakhXWjdXOFRvVnp3aGxROFgyWHRheFZxMG1MY1YtT3RXN25hcTgwT2xaUEphbjJrVWI1UHgzZ1VxN1FLNXdjYm1yZTJtT2hjdjJRVDVtR01BT0c3R0RqanFYd1BQdnlRdm1KdktwZ0tOMmNxRndoRWVLSFhlci1MQWNCYU8?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxORC1PS1FreEtDdjc3c0lRUTVvazRVVzBFVkNXYzNMMDBXRGV0R2Nfc1V5cjFlcnh6cHRhanE0a0dUbjByaGNBWExfcmpibDlYc1NoU3VYcjd2SzYzQ0hlcnh6WER0eXZUbHJQRUZ5WG5LS0NTRWxtTG1jcnJnMlVuOFJqaU1TbHg1dTFLLXdJQ21acXZ0MG5IMFZR?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxQd0FwdWhPal9UUHpiMk44MFFyUlpwbzBaZFl5VEFLTm5uZjRuTndoRkFZYmZtMm41M0x2SEVaNVdMcVpHdHBndVByeFpDTk1xOTVGcGkzY2Q2UXozRWtiWVZpY3pDNlVBd3p2aHR4VHVoSzF5ZlkzVWlDQ0FKNXFpMWk0eUJVMDRFa1FGQXAwaDAwMDhSYUJwejBR?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
