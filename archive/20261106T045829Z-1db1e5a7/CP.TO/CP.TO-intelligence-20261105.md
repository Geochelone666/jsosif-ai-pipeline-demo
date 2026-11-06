# CP.TO Intelligence Report

- ticker: **CP.TO**
- Report as_of: **2026-11-05**
- Market data as_of: **2026-11-05**
- Quant sources: https://finance.yahoo.com/quote/CP.TO/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/CP.TO/key-statistics/
- AI analysis snapshot as_of: **2026-11-05**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-06T05:18:01.453167+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 11, 'rule': 3, 'ai': 6, 'unknown': 0, 'irrelevant': 2})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **5** exact headline/source/date matches; prior report **20261105T045846Z-bde0a1fe/CP.TO** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 11 unique headlines; 6 named publishers; 0 exact duplicates; 11 HTTPS source links; largest publisher share 27.27%; oldest publication 2026-11-02

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 131.3700 |
| Return 1D (%) | -0.2354 |
| Return 1W (%) | 6.2005 |
| Return 1M (%) | 7.2583 |
| Return YTD (%) | 30.8431 |
| Return 1Y (%) | 33.4480 |
| Annualized volatility (%) | 22.1534 |
| Beta vs SPY | 0.3641 |
| Max drawdown (%) | -11.9692 |
| Sharpe (rf=0) | 1.4186 |
| Downside deviation (rf=0, %) | 14.5297 |
| Sortino (rf=0) | 2.1629 |
| Historical VaR 95% (1D, %) | 1.8654 |
| Historical ES 95% (1D, %) | 2.9512 |
| Correlation vs SPY | 0.2227 |
| Tracking error vs SPY (%) | 23.4405 |
| P/E (trailing) | 30.27 |
| P/B | 2.50 |
| EV/EBITDA | 16.65 |
| Revenue growth (%) | 15.20 |
| Forward P/E (estimate) | 22.27 |
| Gross margin (%) | 52.76 |
| Operating margin (%) | 38.56 |
| Return on equity (%) | 8.27 |
| Free cash flow yield (%) | 2.40 |
| MA50 | 124.4011 |
| Close vs MA50 (%) | 5.6020 |
| MA200 | 119.5693 |
| Close vs MA200 (%) | 9.8693 |
| RSI (14, Wilder) | 65.6854 |
| MACD (12,26) | 1.6472 |
| MACD signal (9) | 0.8439 |
| MACD histogram | 0.8033 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'CP.TO': 275, 'SPY': 276}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 131.3700 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -0.2354 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 6.2005 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 7.2583 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 30.8431 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 33.4480 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 22.1534 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 14.5297 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 2.1629 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.8654 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.9512 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2227 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 23.4405 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.3641 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -11.9692 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.4186 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 22.2714 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 52.7640 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 38.5640 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 8.2680 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 2.3983 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 30.2696 -> High trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 65.6854 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.8033 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 5.6020 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 9.8693 -> Clearly above the moving-average trend level.

## TAILWINDS

### Canadian Pacific Kansas City stock gains about 2.5% after stronger Q3 revenue and ongoing Kansas City Southern integration
- Summary: Canadian Pacific Kansas City stock gains about 2.5% after stronger Q3 revenue and ongoing Kansas City Southern integration
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxQMHlkV1cxRWxGWjhGbEI3WTRka05OczJNdGhQZ0xLQjFYa3JlX0Zka3A5Sm50VDFqZlBESl8wbDB1ZzAtNm1CTkV0Rnk4c1RBa0JJY19mZUp2YzE5cVVIa0NULTc2Q0lzOEpJTklfZWY2NEo1bGdpUHpIOEpyOWJDUlE3b1czTU5Rc2l1TEFlalBuN0hNa0NB?oc=5>

## HEADWINDS

### Canadian Pacific Kansas City stock faces fuel pressure after Q3 growth
- Summary: Canadian Pacific Kansas City stock faces fuel pressure after Q3 growth
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMizgFBVV95cUxPZFVEdjVCRUc3eE1iUGJZUHhjczZib05WR2N6cWthQldvOHBvNzliWHBnVm10amNQTjlkZk9QV3pyV0g3N0I5UE9vWXctaDJ2OV9GVm02RHdZM05XaHg0TVVOUWFmdXp6ZkpPbVdTaHRkX2pSLUlhVUpQSW1Yc0x4U1NtbHlBdEMwZnVSMDkycF90enphc1I3eDRESEswem9NZWw0LWNtUHJQX3gwT0xUTjM5VFNxXzQ2ODU3ZGFxYmdfYWYwYzEtbFNjeFhaZw?oc=5>

### Can CPKC (TSX:CP) Maintain Third-Quarter Momentum Amid Higher Operating Expenses?
- Summary: Higher operating expenses may dampen momentum, posing a risk to performance.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxPaUx6d0ZKcFZ1YXM4TGlJc3VQN2RlODVZNDV2TFdDMTJ0eFZuSHJZaGF4dm51NWxXeEJJWGhGUE9IcFpPbGtCa0RKQnVDYmU0SmdKbWk4a1pjUFhENUlRRWNqZ1JDeFJleTFDd1ZRS0Jvc2Y3U1Q1MmhtenhYT0Nja2lfbmZ6NVVJalBMV2NrVjRNQklCQnUwX3J1U2RnbmNpa081NWRDUjRNcUw4clVnQ1FjQTlDTUNaZERvd2JR?oc=5>

## CATALYSTS

### Canadian Pacific Kansas City stock posts 15% Q3 revenue growth
- Summary: Canadian Pacific Kansas City stock posts 15% Q3 revenue growth
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwgFBVV95cUxOVm1IazNZZkJ2MWJoRkJwOEdEbXNOSHlVN1d5OUR1YmR6cktiT3J4Ni1EMEFyeHBrZFNUWGxuOGNQNHhHOGhpLUd1M0VmT09tWlBJYmZtLVg5V0M4N2dMa1ZmSEZTa2xTZV9WaWh6Nkk3WUtROEpSR3hTWkZjZkZRXzNlRWRQMnJWWFZuVGhtYkFXRDJsUUR2THdueDBxS3dyQmdjUnFWSkxkVDBqLTU4UnVwbUFCczJVQml2MkYzUGsyUQ?oc=5>

### CPKC sets new October grain records in Canada, U.S.
- Summary: CPKC achieves record grain volumes in Oct, boosting freight revenue.
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiowFBVV95cUxPRFRrc1l2VmxuUmo1SnRQZ21Da1RGbEtaVElXZlI4a0g3Y19IS2NSMG9sQUp1dmpPYXl5aU1mMnY3a3pjdF9SQ1NpQl9rSm9pVXVzaTE4S0luSjFmRzdiQ29YSklPNVl1VXdGMVFZa0pRNlBjRUlRSzNEWnNYWXMyeVlpeEFvcTFmdl9aU19KYm5QRG9ZbXk5TXItNUNjVkxWaE1F?oc=5>

### Canadian Pacific Kansas City stock: Revenue rises 15 percent amid fuel pressure
- Summary: Revenue up 15% despite fuel cost pressures, indicating operational resilience.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi2AFBVV95cUxNa1ZSdUZKSmVtTlZycDlFdWFIN0tocnpSN2t2Z3JMM0R5Tm0xMjBndUtHM2ZySUFUZVpCRkh5ZFNnMUVRaFZuR0QzMi1YNFAtTjc5SFRsem5XaHgxWm85NzNnaXVJUUg5N29UelE1NF9EVF9aRXBKczZ4VndHeXNwTjJHRkdoVWJ1MkQ0dWxxVktDRUtDSW9EQW9fVFY2YmYyNzEzaERCeUo3ZWFYay11S0FMRlZQNXVwWHl2RmE3QzRtMEp5T0F6UjZSWVJKMzdFd0NicHhrT2c?oc=5>

### Is CPKC (TSX:CP) Making Its Cross-Border Rail Network Work Better?
- Summary: Analysis of cross-border network efficiency and its effect on service quality.
- Date: 2026-11-03 | Impact: low | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxPTndiZl9iV2M3d21PSWZtU0ZVQ3JSUUhhZ2FCRjR2akNTZzZjbXdseGpfMy1qOGpobjhDQnN1UERKdXNvRE4tcVgyeFJFTjFZTG5wS29XSGhKWFpCdy1PVE4zanRlSkZFdFJjamp0YklDWTdwWTJyZ3dnYTdJZkJsV1cxNllNVXBqQm9LVHhuYzRyVnk0Y1BORTRhd2JmQ2VkTUtNcWNmckF3M2tN?oc=5>

### CPKC EVP and CFO Nadeem Velani; SVP, Accounting, Planning and Procurement Ian Gray to address 2026 Scotiabank Transportation & Industrials Conference
- Summary: CPKC executives to speak at 2026 Scotiabank conference, highlighting company strategy and market outlook.
- Date: 2026-11-02 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxNQmVZN01MR2plblJ0Z0IzUlpjTEdHWm1ITE1MVkpxdERBSFFzWjJUWWktWVRUVWotOEZCWk1rSFVsSkduZ1luTTduZlF6RW95aWppbUVDMVhQMlZTMjNvTllhLWp4eVpuOGZxZU5HRkZqTkJSNDN6Z2ltTV9GTWhzVi1qSjczNnh3V0k2VHEzcjJBZGRybkE?oc=5>

### Why CPKC (TSX:CP) Is in Focus as Freight Trends Guide the Open?
- Summary: Article discusses how freight trends are shaping CPKC’s strategic focus and market positioning.
- Date: 2026-11-03 | Impact: low | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxNT0ZqTVc5OEktOC1fS1JnUHVselU0UmNrY21PYjVZSEFPRWFVRkhBNmFoLThhWmVKVTdRM3htb0s3RkZUbzhHNFhEWmRaWWRnTzVZV2NjbzRhTzRsZWdOWkFvTF8ySVRmaFEwdWR0a2F2bEhod0dRLXZwcDhBRHJuT2JrajN4ZzNhc1NNYnBSRGg4REFSVENsOGs1SDlpZy1WR0hRckhR?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **CP.TO** | **30.27** | **2.50** | **16.65** | **15.20** | **114,233,401,344.00 CAD** | **33.45** |
| CNR.TO | 22.27 | 4.85 | 13.78 | 14.60 | 106,290,823,168.00 CAD | 33.93 |
| UNP | 23.24 | 8.04 | 15.44 | 15.30 | 177,004,806,144.00 USD | 39.95 |
| NSC | 28.86 | 4.42 | 15.45 | 13.60 | 73,955,041,280.00 USD | 19.33 |

Peers fetched as_of: 2026-11-05; CP.TO reuses existing data (market data as_of: 2026-11-05); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-28
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-05

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-10-29
- Revenue (latest available single quarter): N/A
- Net income (latest available single quarter): N/A
- SEC link: https://www.sec.gov/Archives/edgar/data/16875/000001687526000033/cp-20260930.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMilwFBVV95cUxQMHlkV1cxRWxGWjhGbEI3WTRka05OczJNdGhQZ0xLQjFYa3JlX0Zka3A5Sm50VDFqZlBESl8wbDB1ZzAtNm1CTkV0Rnk4c1RBa0JJY19mZUp2YzE5cVVIa0NULTc2Q0lzOEpJTklfZWY2NEo1bGdpUHpIOEpyOWJDUlE3b1czTU5Rc2l1TEFlalBuN0hNa0NB?oc=5
- https://news.google.com/rss/articles/CBMizgFBVV95cUxPZFVEdjVCRUc3eE1iUGJZUHhjczZib05WR2N6cWthQldvOHBvNzliWHBnVm10amNQTjlkZk9QV3pyV0g3N0I5UE9vWXctaDJ2OV9GVm02RHdZM05XaHg0TVVOUWFmdXp6ZkpPbVdTaHRkX2pSLUlhVUpQSW1Yc0x4U1NtbHlBdEMwZnVSMDkycF90enphc1I3eDRESEswem9NZWw0LWNtUHJQX3gwT0xUTjM5VFNxXzQ2ODU3ZGFxYmdfYWYwYzEtbFNjeFhaZw?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxPaUx6d0ZKcFZ1YXM4TGlJc3VQN2RlODVZNDV2TFdDMTJ0eFZuSHJZaGF4dm51NWxXeEJJWGhGUE9IcFpPbGtCa0RKQnVDYmU0SmdKbWk4a1pjUFhENUlRRWNqZ1JDeFJleTFDd1ZRS0Jvc2Y3U1Q1MmhtenhYT0Nja2lfbmZ6NVVJalBMV2NrVjRNQklCQnUwX3J1U2RnbmNpa081NWRDUjRNcUw4clVnQ1FjQTlDTUNaZERvd2JR?oc=5
- https://news.google.com/rss/articles/CBMiwgFBVV95cUxOVm1IazNZZkJ2MWJoRkJwOEdEbXNOSHlVN1d5OUR1YmR6cktiT3J4Ni1EMEFyeHBrZFNUWGxuOGNQNHhHOGhpLUd1M0VmT09tWlBJYmZtLVg5V0M4N2dMa1ZmSEZTa2xTZV9WaWh6Nkk3WUtROEpSR3hTWkZjZkZRXzNlRWRQMnJWWFZuVGhtYkFXRDJsUUR2THdueDBxS3dyQmdjUnFWSkxkVDBqLTU4UnVwbUFCczJVQml2MkYzUGsyUQ?oc=5
- https://news.google.com/rss/articles/CBMiowFBVV95cUxPRFRrc1l2VmxuUmo1SnRQZ21Da1RGbEtaVElXZlI4a0g3Y19IS2NSMG9sQUp1dmpPYXl5aU1mMnY3a3pjdF9SQ1NpQl9rSm9pVXVzaTE4S0luSjFmRzdiQ29YSklPNVl1VXdGMVFZa0pRNlBjRUlRSzNEWnNYWXMyeVlpeEFvcTFmdl9aU19KYm5QRG9ZbXk5TXItNUNjVkxWaE1F?oc=5
- https://news.google.com/rss/articles/CBMi2AFBVV95cUxNa1ZSdUZKSmVtTlZycDlFdWFIN0tocnpSN2t2Z3JMM0R5Tm0xMjBndUtHM2ZySUFUZVpCRkh5ZFNnMUVRaFZuR0QzMi1YNFAtTjc5SFRsem5XaHgxWm85NzNnaXVJUUg5N29UelE1NF9EVF9aRXBKczZ4VndHeXNwTjJHRkdoVWJ1MkQ0dWxxVktDRUtDSW9EQW9fVFY2YmYyNzEzaERCeUo3ZWFYay11S0FMRlZQNXVwWHl2RmE3QzRtMEp5T0F6UjZSWVJKMzdFd0NicHhrT2c?oc=5
- https://news.google.com/rss/articles/CBMirAFBVV95cUxPTndiZl9iV2M3d21PSWZtU0ZVQ3JSUUhhZ2FCRjR2akNTZzZjbXdseGpfMy1qOGpobjhDQnN1UERKdXNvRE4tcVgyeFJFTjFZTG5wS29XSGhKWFpCdy1PVE4zanRlSkZFdFJjamp0YklDWTdwWTJyZ3dnYTdJZkJsV1cxNllNVXBqQm9LVHhuYzRyVnk0Y1BORTRhd2JmQ2VkTUtNcWNmckF3M2tN?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxNQmVZN01MR2plblJ0Z0IzUlpjTEdHWm1ITE1MVkpxdERBSFFzWjJUWWktWVRUVWotOEZCWk1rSFVsSkduZ1luTTduZlF6RW95aWppbUVDMVhQMlZTMjNvTllhLWp4eVpuOGZxZU5HRkZqTkJSNDN6Z2ltTV9GTWhzVi1qSjczNnh3V0k2VHEzcjJBZGRybkE?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxNT0ZqTVc5OEktOC1fS1JnUHVselU0UmNrY21PYjVZSEFPRWFVRkhBNmFoLThhWmVKVTdRM3htb0s3RkZUbzhHNFhEWmRaWWRnTzVZV2NjbzRhTzRsZWdOWkFvTF8ySVRmaFEwdWR0a2F2bEhod0dRLXZwcDhBRHJuT2JrajN4ZzNhc1NNYnBSRGg4REFSVENsOGs1SDlpZy1WR0hRckhR?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
