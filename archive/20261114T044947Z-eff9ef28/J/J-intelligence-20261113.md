# J Intelligence Report

- ticker: **J**
- Report as_of: **2026-11-13**
- Market data as_of: **2026-11-13**
- Quant sources: https://finance.yahoo.com/quote/J/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/J/key-statistics/
- AI analysis snapshot as_of: **2026-11-13**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-14T04:58:15.648428+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 11, 'rule': 2, 'ai': 7, 'unknown': 0, 'irrelevant': 2})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **2** exact headline/source/date matches; prior report **20261113T045636Z-34122c9a/J** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 11 unique headlines; 5 named publishers; 0 exact duplicates; 11 HTTPS source links; largest publisher share 63.64%; oldest publication 2026-11-11

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 158.2300 |
| Return 1D (%) | -0.2899 |
| Return 1W (%) | 6.2660 |
| Return 1M (%) | 11.2729 |
| Return YTD (%) | 20.4368 |
| Return 1Y (%) | 4.3837 |
| Annualized volatility (%) | 34.1055 |
| Beta vs SPY | 0.8768 |
| Max drawdown (%) | -30.1809 |
| Sharpe (rf=0) | 0.2984 |
| Downside deviation (rf=0, %) | 25.4459 |
| Sortino (rf=0) | 0.3999 |
| Historical VaR 95% (1D, %) | 3.0531 |
| Historical ES 95% (1D, %) | 5.4729 |
| Correlation vs SPY | 0.3505 |
| Tracking error vs SPY (%) | 31.9859 |
| P/E (trailing) | 52.74 |
| P/B | 5.68 |
| EV/EBITDA | 20.24 |
| Revenue growth (%) | 34.50 |
| Forward P/E (estimate) | 19.21 |
| Gross margin (%) | 22.07 |
| Operating margin (%) | 5.93 |
| Return on equity (%) | 8.00 |
| Free cash flow yield (%) | 3.49 |
| MA50 | 145.0624 |
| Close vs MA50 (%) | 9.0772 |
| MA200 | 134.3315 |
| Close vs MA200 (%) | 17.7907 |
| RSI (14, Wilder) | 62.6330 |
| MACD (12,26) | 3.9940 |
| MACD signal (9) | 3.6132 |
| MACD histogram | 0.3807 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'J': 282, 'SPY': 282}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 158.2300 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.2899 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 6.2660 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 11.2729 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 20.4368 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 4.3837 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 34.1055 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 25.4459 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 0.3999 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.0531 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 5.4729 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.3505 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 31.9859 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.8768 -> Broadly tracks market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -30.1809 -> Deep peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.2984 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 19.2099 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 22.0670 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 5.9290 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 7.9980 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 3.4866 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 52.7433 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 62.6330 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.3807 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 9.0772 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 17.7907 -> Clearly above the moving-average trend level.

## TAILWINDS

### What Jacobs Solutions Shares Major Contract Wins Mean For Shareholders
- Summary: Jacobs wins major contracts, boosting future revenue prospects.
- Date: 2026-11-11 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi2AFBVV95cUxNeUpWeHIxOTRFR0s4TWZfa080U3IzSmZweTZBalUzSHNYSDdkdFo5cG03WW44T21Obm9iOE1mSnhrb3R5RGZBV1JlbWZBWW43bnVsN3d2bjltQ3pOZ3ZvaVlHcVB6MjhTemU1ZHJhVHJtUlM1Q0VmY0dGd1Z5SWhPYU9Jek50VUZyclJqVzFWS1prZFR4eFFzaGJjdUtZeHhjclROeGwtYUN2S2dJTjRQWVNYSFg3SVFWYlc5eUVZM2VFQXVFZWtwWmpqZE1sdHRoVW9UeS1ZdkHSAd4BQVVfeXFMTmV4NjNBOTZkMmZzZm5UcVRiLUNKX05PZ19aZURpWEZoZ2JUV3NqUmtOMXZKZ1JrSzMzcnlFV29LNUp0aGlReVhnUVpmOTE0TVpCX0MwOGZQbEZEQ2loeE5VVk9NRi1tdzBTTHRVaUdkN0htU3YyQUNyNXc3WDVrbEtrSEE1Qm5hMG1IWkdrR2QxZjBLNE5ENDNNZzh2YjN6dlNxUjhKNWZBcjEyc3BReVBDalR1N2FtcVRpckIxLWlMd1JkWV9wV0dMdXNMamF2VElPUEZxUHg1Uk91ZDF3?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Jacobs declares quarterly dividend
- Summary: Jacobs declares quarterly dividend
- Date: 2026-11-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMigwFBVV95cUxQSWllWERLQ1FfQUlYQnVwU3JNZkQ0UjZScU5ycWduRVhrai1fVWpLUS1Vc3ZuSEpNUlg0NHdBWFhiVndhWXBDZFJ2WDYtOE42NHdhSlRGeFkyMDdydWJYT2dkUWFkTGZFckJJNWVfdmZhLUdLYnZMNWlzVzE2TFdZY1FWNA?oc=5>

### Jacobs Solutions Inc. (NYSE:J) Shareholders to Collect $0.36 Quarterly Dividend
- Summary: Jacobs Solutions Inc. (NYSE:J) Shareholders to Collect $0.36 Quarterly Dividend
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0wFBVV95cUxQUGotZVRidnM3N3ZRT3dBSmp0YnE4clJ6VDF2d1plMHRaaHF6eTVoWUprZVRVUUJtb1V2Q19JQ0w1MnVWLWJfYUdaV1UyakpxVFdBUEdud0k4NTBxdHV2ck5Bb19WTGVWcUVlSGpKZFQxblROckExMEN4YWlFLW56bEFVb1JvUHVuOFdKTlJSbUxUTE10NGc1cmNmVnhKcnYyUUVudjZHeGg5U1FPQm92UTdyVmo4TXE2RGJocm9OUTBIZjZWXzN1enBUd29xZFlheEdj?oc=5>

### Jacobs Solutions (J) EVP Allen’s 1,271-unit stock award vests in four equal annual installments.
- Summary: EVP Allen receives 1,271 stock units vesting over four years, enhancing executive ownership.
- Date: 2026-11-13 | Impact: low | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxQTE53QjFFcDlpQndCc0lxTXJDVmFlVVpERHhHc3pwbFlSc1VMQ0tMMjlRNnJrcmNLY1Riem9OT1NtYVdzYjNSMFRLVTNtMWxDOVMwR2NVWnhqMC1UREhjdXd5OWhQUUdpcnRCcExTTUwwckNrbTNhN28wZlZfWVBtUXRMQVNwRENDekJhR2JqMGZ1ZXYySE03OUc5Tk03blFLb09XaC1qVlRGSXpNWEhMVQ?oc=5>

### Jacobs Solutions (J) CFO Venkatesh Nathamuni’s 6,351 stock units vest in four equal annual installments.
- Summary: CFO Nathamuni awarded 6,351 stock units vesting over four years, strengthening executive equity.
- Date: 2026-11-13 | Impact: low | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxObW8xcmVfUWpVYUs1SVVZWFRDYW5SUkNiYjJidVBJeEh6enc3TzI2ZmkwcENfbkFpeXVYa3RwQUNhSjlabWRiN3NpTU5JT0wyXzJBRWMwN2RLdk9tQzl3a3hvWnRIczFJZ1oxU2lUSVZvRy11a1RmcnFNMm0tc1BEWUR3SGxocy0wY3BoWDkyOGNlQWd2c3pmNXdlOFpzZEswVUFsY3RIbEdRV0xydVZONQ?oc=5>

### Jacobs Solutions (J) legal chief receives stock grant vesting in four equal annual installments.
- Summary: Legal chief granted stock units vesting over four years, increasing executive ownership.
- Date: 2026-11-13 | Impact: low | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxQLWltNEMtb3JwSDhXN3VFVy1YVWZheTVHYlZpSEw2MWJTajVZSU5qbXJYTE02ckxXYlJhVGRibzFzelN2Tkp4M1Zyc0ttdmpzOGgyeEpGNG5zdkdYdVVlUzNIbjNINnpDUUh6LS1UenNheFFhbGwyYnl0V0NLdTVRWnpwMXVMeTB5UUpPZTFHRHowRGpjRDZHQndDeTk2T0J1T3gzbVNDRG9nNENvSUVaSw?oc=5>

### Jacobs Solutions (J) CEO receives stock units that vest in four equal annual installments.
- Summary: CEO awarded stock units vesting over four years, boosting executive equity.
- Date: 2026-11-13 | Impact: low | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxNWWl5LTZ3akhfOFlpNkI5cnVmNE80Z1UwaV9JSGVmV3Zsaks0U0VBZ0c0QllzWlprNnZfWVpKVXB4djR1NkItQ1VHSUlDRnp1QTJLb0RRRFZoX2RZSkFZa0ZsVlM2aUtYTlFvYmtONk5QTVNSdkFIVFV2WFFyWlJRbEo0OEw3OE9nN1ZHUkswR2pvdzNPTzlHMXlkRFZ5bW16ODZ3MWR5UHBrMUJzLW5wUw?oc=5>

### President's stock grant at Jacobs Solutions (J) vests in four equal annual installments.
- Summary: President’s stock grant vests over four equal annual installments, providing ongoing incentive alignment.
- Date: 2026-11-13 | Impact: medium | Horizon: short | Confidence: 1
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxQb1JFV2t6WEM2YzZLeURWNHFzLW52NmhOOVB3Z2xqY3NVaG14ZmVTYTVxbFhYQXo5SzNyUWVHcWdRTGF2WVBzc0NlMG5EbmxxZmdzZnBtd0diTXl5TlQ3dmZjRXYycHBIeExISUlpa1N4VVd0UmZkU1cxLXdJa2RPTEhWdFpqa0tDYXc5VE5fWjJOLWhnTXQxaTMyaHBYRlY2STlaNXp2dHpXWC1xeG56Wg?oc=5>

### President Patrick Hill’s stock grant at Jacobs Solutions (J) vests in four equal annual installments.
- Summary: President Patrick Hill’s stock grant vests over four equal annual installments, reinforcing long-term commitment.
- Date: 2026-11-11 | Impact: medium | Horizon: short | Confidence: 1
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxNdXkyZFJNQjdPblhIOHA3Z0I3NWV3YVVrMTJvSjZwNE1JdkJ1eUw4ZURPTm1RamQ3MEczYzd6NXIxblExYXZQNGlubVgtYU1UbW9vRVYwLVVXMU1NbnJMUlBoS3BXd3FFelZwNnVTeGZ2a1hHdmRoRWM4azBHUDRPYTRSMHE5WG5ITXlnRFhhSUxhVk1WdEkzVzJzTDRFSVBWSkNzVVlKVXBPV0IxTkxQcA?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **J** | **52.74** | **5.68** | **20.24** | **34.50** | **18,519,017,472.00 USD** | **4.38** |
| ACM | 24.65 | 4.14 | 12.44 | -14.20 | 9,073,097,728.00 USD | -46.44 |
| FLR | N/A | 2.47 | 11.05 | 10.50 | 6,278,465,024.00 USD | 13.80 |
| KBR | 10.26 | 2.54 | 9.82 | 5.00 | 4,488,218,624.00 USD | -14.30 |

Peers fetched as_of: 2026-11-13; J reuses existing data (market data as_of: 2026-11-13); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-04
- Next expected earnings: 2026-11-23 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-13

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-08-04
- Revenue (latest available single quarter): 4,142,644,000.00 USD; period 2018-06-30/2018-09-28; fiscal year/reporting period 2018/FY
- Net income (latest available single quarter): 136,553,000.00 USD; period 2026-03-28/2026-06-26; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/52988/000162828026052573/jec-20260626.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMi2AFBVV95cUxNeUpWeHIxOTRFR0s4TWZfa080U3IzSmZweTZBalUzSHNYSDdkdFo5cG03WW44T21Obm9iOE1mSnhrb3R5RGZBV1JlbWZBWW43bnVsN3d2bjltQ3pOZ3ZvaVlHcVB6MjhTemU1ZHJhVHJtUlM1Q0VmY0dGd1Z5SWhPYU9Jek50VUZyclJqVzFWS1prZFR4eFFzaGJjdUtZeHhjclROeGwtYUN2S2dJTjRQWVNYSFg3SVFWYlc5eUVZM2VFQXVFZWtwWmpqZE1sdHRoVW9UeS1ZdkHSAd4BQVVfeXFMTmV4NjNBOTZkMmZzZm5UcVRiLUNKX05PZ19aZURpWEZoZ2JUV3NqUmtOMXZKZ1JrSzMzcnlFV29LNUp0aGlReVhnUVpmOTE0TVpCX0MwOGZQbEZEQ2loeE5VVk9NRi1tdzBTTHRVaUdkN0htU3YyQUNyNXc3WDVrbEtrSEE1Qm5hMG1IWkdrR2QxZjBLNE5ENDNNZzh2YjN6dlNxUjhKNWZBcjEyc3BReVBDalR1N2FtcVRpckIxLWlMd1JkWV9wV0dMdXNMamF2VElPUEZxUHg1Uk91ZDF3?oc=5
- https://news.google.com/rss/articles/CBMigwFBVV95cUxQSWllWERLQ1FfQUlYQnVwU3JNZkQ0UjZScU5ycWduRVhrai1fVWpLUS1Vc3ZuSEpNUlg0NHdBWFhiVndhWXBDZFJ2WDYtOE42NHdhSlRGeFkyMDdydWJYT2dkUWFkTGZFckJJNWVfdmZhLUdLYnZMNWlzVzE2TFdZY1FWNA?oc=5
- https://news.google.com/rss/articles/CBMi0wFBVV95cUxQUGotZVRidnM3N3ZRT3dBSmp0YnE4clJ6VDF2d1plMHRaaHF6eTVoWUprZVRVUUJtb1V2Q19JQ0w1MnVWLWJfYUdaV1UyakpxVFdBUEdud0k4NTBxdHV2ck5Bb19WTGVWcUVlSGpKZFQxblROckExMEN4YWlFLW56bEFVb1JvUHVuOFdKTlJSbUxUTE10NGc1cmNmVnhKcnYyUUVudjZHeGg5U1FPQm92UTdyVmo4TXE2RGJocm9OUTBIZjZWXzN1enBUd29xZFlheEdj?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxQTE53QjFFcDlpQndCc0lxTXJDVmFlVVpERHhHc3pwbFlSc1VMQ0tMMjlRNnJrcmNLY1Riem9OT1NtYVdzYjNSMFRLVTNtMWxDOVMwR2NVWnhqMC1UREhjdXd5OWhQUUdpcnRCcExTTUwwckNrbTNhN28wZlZfWVBtUXRMQVNwRENDekJhR2JqMGZ1ZXYySE03OUc5Tk03blFLb09XaC1qVlRGSXpNWEhMVQ?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxObW8xcmVfUWpVYUs1SVVZWFRDYW5SUkNiYjJidVBJeEh6enc3TzI2ZmkwcENfbkFpeXVYa3RwQUNhSjlabWRiN3NpTU5JT0wyXzJBRWMwN2RLdk9tQzl3a3hvWnRIczFJZ1oxU2lUSVZvRy11a1RmcnFNMm0tc1BEWUR3SGxocy0wY3BoWDkyOGNlQWd2c3pmNXdlOFpzZEswVUFsY3RIbEdRV0xydVZONQ?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxQLWltNEMtb3JwSDhXN3VFVy1YVWZheTVHYlZpSEw2MWJTajVZSU5qbXJYTE02ckxXYlJhVGRibzFzelN2Tkp4M1Zyc0ttdmpzOGgyeEpGNG5zdkdYdVVlUzNIbjNINnpDUUh6LS1UenNheFFhbGwyYnl0V0NLdTVRWnpwMXVMeTB5UUpPZTFHRHowRGpjRDZHQndDeTk2T0J1T3gzbVNDRG9nNENvSUVaSw?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxNWWl5LTZ3akhfOFlpNkI5cnVmNE80Z1UwaV9JSGVmV3Zsaks0U0VBZ0c0QllzWlprNnZfWVpKVXB4djR1NkItQ1VHSUlDRnp1QTJLb0RRRFZoX2RZSkFZa0ZsVlM2aUtYTlFvYmtONk5QTVNSdkFIVFV2WFFyWlJRbEo0OEw3OE9nN1ZHUkswR2pvdzNPTzlHMXlkRFZ5bW16ODZ3MWR5UHBrMUJzLW5wUw?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxQb1JFV2t6WEM2YzZLeURWNHFzLW52NmhOOVB3Z2xqY3NVaG14ZmVTYTVxbFhYQXo5SzNyUWVHcWdRTGF2WVBzc0NlMG5EbmxxZmdzZnBtd0diTXl5TlQ3dmZjRXYycHBIeExISUlpa1N4VVd0UmZkU1cxLXdJa2RPTEhWdFpqa0tDYXc5VE5fWjJOLWhnTXQxaTMyaHBYRlY2STlaNXp2dHpXWC1xeG56Wg?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxNdXkyZFJNQjdPblhIOHA3Z0I3NWV3YVVrMTJvSjZwNE1JdkJ1eUw4ZURPTm1RamQ3MEczYzd6NXIxblExYXZQNGlubVgtYU1UbW9vRVYwLVVXMU1NbnJMUlBoS3BXd3FFelZwNnVTeGZ2a1hHdmRoRWM4azBHUDRPYTRSMHE5WG5ITXlnRFhhSUxhVk1WdEkzVzJzTDRFSVBWSkNzVVlKVXBPV0IxTkxQcA?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
