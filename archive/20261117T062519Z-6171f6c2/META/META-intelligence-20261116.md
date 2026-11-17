# META Intelligence Report

- ticker: **META**
- Report as_of: **2026-11-16**
- Market data as_of: **2026-11-16**
- Quant sources: https://finance.yahoo.com/quote/META/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/META/key-statistics/
- AI analysis snapshot as_of: **2026-11-16**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-17T06:32:55.903551+00:00**
- AI status: **Partial: 5 headlines remain unclassified and excluded from research conclusions**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 4, 'ai': 9, 'unknown': 5, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **3** exact headline/source/date matches; prior report **20261116T043911Z-b81cfeb4/META** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 13 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 20.83%; oldest publication 2026-11-12

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 626.4100 |
| Return 1D (%) | -2.3812 |
| Return 1W (%) | -2.3325 |
| Return 1M (%) | -11.6899 |
| Return YTD (%) | -4.8580 |
| Return 1Y (%) | 3.1298 |
| Annualized volatility (%) | 41.7881 |
| Beta vs SPY | 1.3697 |
| Max drawdown (%) | -28.7332 |
| Sharpe (rf=0) | 0.3106 |
| Downside deviation (rf=0, %) | 27.5594 |
| Sortino (rf=0) | 0.4710 |
| Historical VaR 95% (1D, %) | 3.7819 |
| Historical ES 95% (1D, %) | 5.6434 |
| Correlation vs SPY | 0.4512 |
| Tracking error vs SPY (%) | 37.6374 |
| P/E (trailing) | 21.89 |
| P/B | 5.88 |
| EV/EBITDA | 14.06 |
| Revenue growth (%) | 26.10 |
| Forward P/E (estimate) | 17.56 |
| Gross margin (%) | 81.03 |
| Operating margin (%) | 37.78 |
| Return on equity (%) | 32.26 |
| Free cash flow yield (%) | 1.05 |
| MA50 | 679.9057 |
| Close vs MA50 (%) | -7.8681 |
| MA200 | 629.5824 |
| Close vs MA200 (%) | -0.5039 |
| RSI (14, Wilder) | 43.8812 |
| MACD (12,26) | -14.6386 |
| MACD signal (9) | -16.9869 |
| MACD histogram | 2.3482 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'META': 283, 'SPY': 283}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 626.4100 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -2.3812 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -2.3325 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -11.6899 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -4.8580 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 3.1298 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 41.7881 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 27.5594 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.4710 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.7819 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.6434 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4512 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 37.6374 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.3697 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -28.7332 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.3106 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 17.5587 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 81.0340 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 37.7770 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 32.2640 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.0522 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 21.8948 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 43.8812 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 2.3482 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -7.8681 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -0.5039 -> Slightly below the moving-average trend level.

## TAILWINDS

### Will ETF Buying Change Meta Stock Narrative
- Summary: ETF buying could shift Meta’s stock narrative, potentially boosting investor interest.
- Date: 2026-11-14 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxNUnhObF9vcWxydnRua1J4T2hsVjhTOExiYjFWYUJhTmxGazE1ZS1zTzVBN3JuUTkwaHVKM3h0bm95ZXU4NlBLQkFmbkk1cnlYVTBlc1F4Rk9VaVV4cnhtd1Y1QnVETzNjbkZvM3FObVc5Y182VjVjc1B4SXBIbjAwSUp3WUZlVXpqOHpFbkkxT2pqbGhKQWxEMw?oc=5>

### 55 ETFs Add to Meta Platforms (META) on Nov. 11
- Summary: Fifty-five ETFs added Meta shares, indicating institutional support.
- Date: 2026-11-13 | Impact: low | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxQZkc4MEpkMmtxWldrMnI5ZUdHVjMyb1ZBU3duZklHdnBQekw0VnYzR0hoZWRMV3EtOUdScmpzd2E1ZEYxcjNfR3NKNWR6R3JzZWJtWE5SbG4ydTcxSzZRN3lXMmFHV01JaU1SSDNXVF8yRnM3U1VJS2RQYllEd0p3cGNTWV9jc3JTcjRpQkVla0ZLMUd3V1E?oc=5>

### Meta (META) Stock May Be 48% Undervalued Despite EU Feature Crackdown
- Summary: Analysts suggest Meta’s stock is undervalued, indicating potential upside.
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiygFBVV95cUxQQ2ZvRzd0MHA5b0Q3MGJndVB4VlprV3czaDVCbFBfSnEyaUhsRzZTak5kTWZlVUswS21OOXBCUDJ3bkdWQlM5dmZ6a2lzaWxNbldBb3JUUTFXVDlNTDhWbDY0YS14N3pBN3cyU1duRlpDLXBKd2szdF9EQldoRzBsaW80bkpFU1ZrUVh5Tmh4a3VxeE1mMExvQ0t4MDJhTnRna2NlSE1tNTY5YVNMX29Hd2lhWW9YV3dyQmFRR1BDRGtDQjV1LXVlREJn0gHPAUFVX3lxTE9sM1BvZjUzX1YwSmhkd3I0eDZOMEFqdTUzeWVJX2p5Q1ZUd25ObWlfaWZDalhhZzJ3ekxraWdSZEQ5Rk1BMGFZTE5leU9Qb09TWWxieGM5VElzYm1fTk5fUUR3X0JOSTZENnBBTTBZX012NmpIcWFaTkxuX21wTEY4a0V3dElvMXdhNzI5RmMtd2dHRm9aNzZ4QmtOODZmUWFSbTNKVzN1NzVmOGtpMWROdTR3RWdOWXY5SGlWMFFQbmR3aTY1OXA4M2FyVm11Zw?oc=5>

## HEADWINDS

### Meta Stocks Fall 2.5% After Italy Fines Facebook 805 Million Over Photo Access
- Summary: Meta Stocks Fall 2.5% After Italy Fines Facebook 805 Million Over Photo Access
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0wFBVV95cUxON2RHX0dtc09zZU9JbXRhSnVETUpuZ1BaMlI1V0dwR0dKYWpnbjZPX0hfenlOa0pXNzVZSUc3YVItbFFhcWdueWYwN2R5U255cnpyNmtWODZjQ04zd1BPVWJlUEZCU1BsX2s4V1o4QnNqSFVmR1F2ekZQNGZPS3V2bUk2anV0eGgybXR3M0pzaEVNM1pseDFfSk1ldHlaall3Tno0NTJKWVhPLThUem5IVTR6LTdXdVptbjRub2I0S05JZjN6eVJBZVVza0dnS1RHTVFZ?oc=5>

### Meta shares slide over 2% on Monday: here's why
- Summary: Meta shares slide over 2% on Monday: here's why
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxQblZDamRhVTZpZGRtX3V1Y3Fvdlp5REFGWTVyWGg4ODRzN3ZyTVpqbFlEc2o4VFJWUy1NQVJhSWh1Wmdyc3dQME1INXFDaFhtWkVKaUZMTUFaWUQ0UE5CNC1hYXJTNmVhZi1sZmFzU1NLWXF6T1dWR0Fubm5JM2hYczhNcXlKQVppelQtVjNTbmVRRjNIc0lVeWt5X1FQbGFGdGJlTg?oc=5>

### As Meta Platforms Continues To Weaken, A Bearish Trade May Be In Order
- Summary: Meta shares weakening, suggesting bearish sentiment.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxPeXYtc0wwTWRuR29fdGRXZE83a0JHb3Y2Q2Y4b3NPOXVZSjM3TEc5VzJhTkFBN1dHekhaUm9XOWdrbWl2OUx5eWRraVVIWm02YjhQV2M3MWpLbk5ld1c5TG1rRGE5Sm1Td0dMWFQ0b2dMYVp2Wko5SmxEMGEtSDFJWldKXzFEV3hjOTNtQkVFeVRpSjEzOFE?oc=5>

### Meta Platforms (NASDAQ:META) Stock Falls 2.4% - Time to Sell?
- Summary: Meta stock declined 2.4%, prompting sell considerations.
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxPZTBFcHlIZkRlVXFFelNrbVNIc1ZEWWwyMUNSLXJsVC1qcDI2Qmt6NERxWjU0S2hmOEhMZlprZnpSR0RSY09hVEl1TTFKSHo2Mm9sWEVrYllxZkJXTzdQbzRBTkU0V3lSSzBiVmlqQTQ5c0pZMDFWZ2JfWWFld2xNd2w5WjhmNGoyelJUNU5DYXVNWVlVN2JiQk5tUTY0Rk41WTVWS1lmcE1NNm1uVUZsZWNzUGM?oc=5>

### Italy orders Meta to pay $887M over Facebook's photo access practices (META:NASDAQ)
- Summary: Italian court orders Meta to pay $887M for alleged photo access violations.
- Date: 2026-11-16 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxOSG5zRHF0OVdkUDhfQms2XzFzWGcxbEtjZFhMUURua1Vhd2g5ZnZhZlVubGpmaklZMFNvVXp2OTlZN015QjZmUnZmSlU0TW9xTUtCNGR3cmg4Z1owV0tMTlBCdnBlQWRPV2FxakRJeWxlancyQ2EwLWdVOVpfNG8zMGQwLTFPbndtbTRXenhCb3VZQjVoS2VNUExFVFlJTDdsZE9HQXZuRHU?oc=5>

## CATALYSTS

### Meta Plunged After Earnings in 2025 Too. Here’s What Buyers Got a Year Later
- Summary: Meta Plunged After Earnings in 2025 Too. Here’s What Buyers Got a Year Later
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxPY1U3di1QYW5mN3NoYXJWUUdqVHVDSHNOV3hnbTVNZE9zQmE5YjZSMXp0SW9BWjJORjNfakJibjZDa01zWmFzajZHUDdpc1U4UmJmeEpucTFrcnRsWGtOaE1DOGNTaEhzR0lrSFdkY3o2QTdlSTNBTWh2SWN4el9ZQ1Z1Ukg2a3dPNTVSdzVkZEc3RGdGRm5JdDdjSVRLVmNRQ1AtTHNHVUQ2ZlBGdlNCa0VfWTZhVEtjR0E?oc=5>

### Meta Platforms, Inc. $META Stock: Walter Public Investments Inc. Reduces Stake
- Summary: Meta Platforms, Inc. $META Stock: Walter Public Investments Inc. Reduces Stake
- Date: 2026-11-16 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizwFBVV95cUxQWHZsUjF3cGx4NEpEZm9xLTdXRUY5U08tem5ueUFoTFoxc1A0c1hIVnd2UHZXMTFOb0ZpNnJaZUljZHB4MXpzbTFMbXJxOU8yYk1Ma3l0WmtVX3lmb1JpcW5iUHVNdjZOMWVVc0QzZ1d6U2NtN2c3OUJKOTJQUzFRVmM4M0JVYms1UDZCbGgwd3Ata25zTTYxX3VHc0dPWGRMeWg1b0RGTG1mRXBBaTdOdl9BMktVNjdraWNnUlh1WUoyako4WTgtWHlTRHRlWjA?oc=5>

## RISKS

### Meta (META) Faces $880 Million Italy Fine Over User Photo Access
- Summary: Meta fined $880M in Italy for user photo access violations, posing regulatory and financial risk.
- Date: 2026-11-15 | Impact: high | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxOTUdFQ3JuakFLZUxCSzVwSDIzRmcxR0lVX1V0Tks5eVdXNkRKM21EaWh5dXh6T2lzTnQtWkNjLThJTC1oeElFU2wyLXNGM3dzMGhGd2RULXQ2TEhkaUJVU284Wk9YeXNkdmJ2cDdsSHB5ZGd6VjBybXRkU1JiR0xOZE82ZVB0bVl5NzY5OUFjN2s4QQ?oc=5>

### Meta Platforms, Inc. $META Stock Holdings Decreased by Philadelphia Trust Co.
- Summary: Philadelphia Trust Co. reduced its Meta holdings, potentially signaling investor concern.
- Date: 2026-11-16 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMizwFBVV95cUxONHVwSUYwUS1RUEdpVDI1Wm9HUEYtSUdLY1dPc0UtOUNqYnNKLXF4dWVxUXlvcGs2eWFBdmduNFFad2x3Tk9ZOWFCU0tjNHFVQUxLQnBmbmVOVy1xREMzYmdWa094R01QdlRzOVJaRUJxOURIajJ1Z3pHZUs2S1JWTWxJTnBYMExkMktlc3lDejJ1Z2psOU5oNFlIZ0huNFZUYVVyR1FnTEdYSTdhMUZTVTRHaXNDajU3enptWTlCbXpud1FvNUQ4dVFkLWhsNjQ?oc=5>

### Meta Platforms, Inc. $META Stock: Vestor Capital LLC Decreases Holdings
- Summary: Vestor Capital LLC cut its Meta stake, indicating possible negative sentiment.
- Date: 2026-11-16 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxQUWwtZ09XMDFuUHhtVGFDQVk2dGpBNkJTeEVMendyT29kR3lCa19vZEtMc0pXcUhSeHE2RGRqWXNvSXY3WnFKaWlQVjNCcGU4TzlmMWt4NDJPbmdzajBpdE5nNEdLTWxvaV9HWjg4eUJtNURzNG5tZlBPWjg1WnFLc2F5cDQ1LTlJaWJKV1RSZjlJeGxnUi15Vy1sd2R1cjdfQjBrZEVUbElNLUFTc0xoV08tamc3NldjZjl6VHk5cFk5aUc5Y0Rr?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **META** | **21.89** | **5.88** | **14.06** | **26.10** | **1,601,254,981,632.00 USD** | **3.13** |
| GOOGL | 14.82 | 5.29 | 18.28 | 24.70 | 3,488,053,460,992.00 USD | 2.91 |
| SNAP | N/A | 3.92 | 53.56 | 14.30 | 8,788,276,224.00 USD | -40.61 |
| PINS | 76.75 | 3.40 | 34.75 | 11.90 | 10,564,014,080.00 USD | -30.80 |

Peers fetched as_of: 2026-11-16; META reuses existing data (market data as_of: 2026-11-16); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-21
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

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
- Filing date: 2026-10-22
- Revenue (latest available single quarter): 13,727,000,000.00 USD; period 2018-07-01/2018-09-30; fiscal year/reporting period 2018/Q3
- Net income (latest available single quarter): 9,860,000,000.00 USD; period 2026-07-01/2026-09-30; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMimAFBVV95cUxNUnhObF9vcWxydnRua1J4T2hsVjhTOExiYjFWYUJhTmxGazE1ZS1zTzVBN3JuUTkwaHVKM3h0bm95ZXU4NlBLQkFmbkk1cnlYVTBlc1F4Rk9VaVV4cnhtd1Y1QnVETzNjbkZvM3FObVc5Y182VjVjc1B4SXBIbjAwSUp3WUZlVXpqOHpFbkkxT2pqbGhKQWxEMw?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxQZkc4MEpkMmtxWldrMnI5ZUdHVjMyb1ZBU3duZklHdnBQekw0VnYzR0hoZWRMV3EtOUdScmpzd2E1ZEYxcjNfR3NKNWR6R3JzZWJtWE5SbG4ydTcxSzZRN3lXMmFHV01JaU1SSDNXVF8yRnM3U1VJS2RQYllEd0p3cGNTWV9jc3JTcjRpQkVla0ZLMUd3V1E?oc=5
- https://news.google.com/rss/articles/CBMiygFBVV95cUxQQ2ZvRzd0MHA5b0Q3MGJndVB4VlprV3czaDVCbFBfSnEyaUhsRzZTak5kTWZlVUswS21OOXBCUDJ3bkdWQlM5dmZ6a2lzaWxNbldBb3JUUTFXVDlNTDhWbDY0YS14N3pBN3cyU1duRlpDLXBKd2szdF9EQldoRzBsaW80bkpFU1ZrUVh5Tmh4a3VxeE1mMExvQ0t4MDJhTnRna2NlSE1tNTY5YVNMX29Hd2lhWW9YV3dyQmFRR1BDRGtDQjV1LXVlREJn0gHPAUFVX3lxTE9sM1BvZjUzX1YwSmhkd3I0eDZOMEFqdTUzeWVJX2p5Q1ZUd25ObWlfaWZDalhhZzJ3ekxraWdSZEQ5Rk1BMGFZTE5leU9Qb09TWWxieGM5VElzYm1fTk5fUUR3X0JOSTZENnBBTTBZX012NmpIcWFaTkxuX21wTEY4a0V3dElvMXdhNzI5RmMtd2dHRm9aNzZ4QmtOODZmUWFSbTNKVzN1NzVmOGtpMWROdTR3RWdOWXY5SGlWMFFQbmR3aTY1OXA4M2FyVm11Zw?oc=5
- https://news.google.com/rss/articles/CBMi0wFBVV95cUxON2RHX0dtc09zZU9JbXRhSnVETUpuZ1BaMlI1V0dwR0dKYWpnbjZPX0hfenlOa0pXNzVZSUc3YVItbFFhcWdueWYwN2R5U255cnpyNmtWODZjQ04zd1BPVWJlUEZCU1BsX2s4V1o4QnNqSFVmR1F2ekZQNGZPS3V2bUk2anV0eGgybXR3M0pzaEVNM1pseDFfSk1ldHlaall3Tno0NTJKWVhPLThUem5IVTR6LTdXdVptbjRub2I0S05JZjN6eVJBZVVza0dnS1RHTVFZ?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxQblZDamRhVTZpZGRtX3V1Y3Fvdlp5REFGWTVyWGg4ODRzN3ZyTVpqbFlEc2o4VFJWUy1NQVJhSWh1Wmdyc3dQME1INXFDaFhtWkVKaUZMTUFaWUQ0UE5CNC1hYXJTNmVhZi1sZmFzU1NLWXF6T1dWR0Fubm5JM2hYczhNcXlKQVppelQtVjNTbmVRRjNIc0lVeWt5X1FQbGFGdGJlTg?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxPeXYtc0wwTWRuR29fdGRXZE83a0JHb3Y2Q2Y4b3NPOXVZSjM3TEc5VzJhTkFBN1dHekhaUm9XOWdrbWl2OUx5eWRraVVIWm02YjhQV2M3MWpLbk5ld1c5TG1rRGE5Sm1Td0dMWFQ0b2dMYVp2Wko5SmxEMGEtSDFJWldKXzFEV3hjOTNtQkVFeVRpSjEzOFE?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxPZTBFcHlIZkRlVXFFelNrbVNIc1ZEWWwyMUNSLXJsVC1qcDI2Qmt6NERxWjU0S2hmOEhMZlprZnpSR0RSY09hVEl1TTFKSHo2Mm9sWEVrYllxZkJXTzdQbzRBTkU0V3lSSzBiVmlqQTQ5c0pZMDFWZ2JfWWFld2xNd2w5WjhmNGoyelJUNU5DYXVNWVlVN2JiQk5tUTY0Rk41WTVWS1lmcE1NNm1uVUZsZWNzUGM?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxOSG5zRHF0OVdkUDhfQms2XzFzWGcxbEtjZFhMUURua1Vhd2g5ZnZhZlVubGpmaklZMFNvVXp2OTlZN015QjZmUnZmSlU0TW9xTUtCNGR3cmg4Z1owV0tMTlBCdnBlQWRPV2FxakRJeWxlancyQ2EwLWdVOVpfNG8zMGQwLTFPbndtbTRXenhCb3VZQjVoS2VNUExFVFlJTDdsZE9HQXZuRHU?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxPY1U3di1QYW5mN3NoYXJWUUdqVHVDSHNOV3hnbTVNZE9zQmE5YjZSMXp0SW9BWjJORjNfakJibjZDa01zWmFzajZHUDdpc1U4UmJmeEpucTFrcnRsWGtOaE1DOGNTaEhzR0lrSFdkY3o2QTdlSTNBTWh2SWN4el9ZQ1Z1Ukg2a3dPNTVSdzVkZEc3RGdGRm5JdDdjSVRLVmNRQ1AtTHNHVUQ2ZlBGdlNCa0VfWTZhVEtjR0E?oc=5
- https://news.google.com/rss/articles/CBMizwFBVV95cUxQWHZsUjF3cGx4NEpEZm9xLTdXRUY5U08tem5ueUFoTFoxc1A0c1hIVnd2UHZXMTFOb0ZpNnJaZUljZHB4MXpzbTFMbXJxOU8yYk1Ma3l0WmtVX3lmb1JpcW5iUHVNdjZOMWVVc0QzZ1d6U2NtN2c3OUJKOTJQUzFRVmM4M0JVYms1UDZCbGgwd3Ata25zTTYxX3VHc0dPWGRMeWg1b0RGTG1mRXBBaTdOdl9BMktVNjdraWNnUlh1WUoyako4WTgtWHlTRHRlWjA?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxOTUdFQ3JuakFLZUxCSzVwSDIzRmcxR0lVX1V0Tks5eVdXNkRKM21EaWh5dXh6T2lzTnQtWkNjLThJTC1oeElFU2wyLXNGM3dzMGhGd2RULXQ2TEhkaUJVU284Wk9YeXNkdmJ2cDdsSHB5ZGd6VjBybXRkU1JiR0xOZE82ZVB0bVl5NzY5OUFjN2s4QQ?oc=5
- https://news.google.com/rss/articles/CBMizwFBVV95cUxONHVwSUYwUS1RUEdpVDI1Wm9HUEYtSUdLY1dPc0UtOUNqYnNKLXF4dWVxUXlvcGs2eWFBdmduNFFad2x3Tk9ZOWFCU0tjNHFVQUxLQnBmbmVOVy1xREMzYmdWa094R01QdlRzOVJaRUJxOURIajJ1Z3pHZUs2S1JWTWxJTnBYMExkMktlc3lDejJ1Z2psOU5oNFlIZ0huNFZUYVVyR1FnTEdYSTdhMUZTVTRHaXNDajU3enptWTlCbXpud1FvNUQ4dVFkLWhsNjQ?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxQUWwtZ09XMDFuUHhtVGFDQVk2dGpBNkJTeEVMendyT29kR3lCa19vZEtMc0pXcUhSeHE2RGRqWXNvSXY3WnFKaWlQVjNCcGU4TzlmMWt4NDJPbmdzajBpdE5nNEdLTWxvaV9HWjg4eUJtNURzNG5tZlBPWjg1WnFLc2F5cDQ1LTlJaWJKV1RSZjlJeGxnUi15Vy1sd2R1cjdfQjBrZEVUbElNLUFTc0xoV08tamc3NldjZjl6VHk5cFk5aUc5Y0Rr?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
