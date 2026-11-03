# SCHW Intelligence Report

- ticker: **SCHW**
- Report as_of: **2026-11-02**
- Market data as_of: **2026-11-02**
- Quant sources: https://finance.yahoo.com/quote/SCHW/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/SCHW/key-statistics/
- AI analysis snapshot as_of: **2026-11-02**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-03T05:23:48.675288+00:00**
- AI status: **Partial: 1 headline remains unclassified and excluded from research conclusions**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 25, 'rule': 1, 'ai': 5, 'unknown': 1, 'irrelevant': 18})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **4** exact headline/source/date matches; prior report **20261102T041627Z-c84a7052/SCHW** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 25 unique headlines; 8 named publishers; 0 exact duplicates; 25 HTTPS source links; largest publisher share 48.0%; oldest publication 2026-10-28

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 88.7100 |
| Return 1D (%) | 0.7496 |
| Return 1W (%) | -1.1367 |
| Return 1M (%) | -8.2627 |
| Return YTD (%) | -10.3299 |
| Return 1Y (%) | -4.9473 |
| Annualized volatility (%) | 25.5204 |
| Beta vs SPY | 0.4275 |
| Max drawdown (%) | -22.5253 |
| Sharpe (rf=0) | -0.0141 |
| Downside deviation (rf=0, %) | 19.7015 |
| Sortino (rf=0) | -0.0183 |
| Historical VaR 95% (1D, %) | 2.5536 |
| Historical ES 95% (1D, %) | 3.9505 |
| Correlation vs SPY | 0.2148 |
| Tracking error vs SPY (%) | 25.9833 |
| P/E (trailing) | 15.16 |
| P/B | 2.98 |
| EV/EBITDA | N/A |
| Revenue growth (%) | 16.90 |
| Forward P/E (estimate) | 11.37 |
| Gross margin (%) | 97.51 |
| Operating margin (%) | 52.67 |
| Return on equity (%) | 21.12 |
| Free cash flow yield (%) | N/A |
| MA50 | 100.0220 |
| Close vs MA50 (%) | -11.3095 |
| MA200 | 97.1262 |
| Close vs MA200 (%) | -8.6652 |
| RSI (14, Wilder) | 30.9925 |
| MACD (12,26) | -3.1787 |
| MACD signal (9) | -3.1703 |
| MACD histogram | -0.0083 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'SCHW': 273, 'SPY': 273}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 88.7100 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 0.7496 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -1.1367 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -8.2627 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -10.3299 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -4.9473 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 25.5204 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 19.7015 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.0183 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.5536 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.9505 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.2148 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 25.9833 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.4275 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -22.5253 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.0141 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 11.3685 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 97.5060 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 52.6700 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 21.1220 -> Adjusted price rose over this period.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 15.1641 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 30.9925 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -0.0083 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -11.3095 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -8.6652 -> Clearly below the moving-average trend level.

## TAILWINDS

### Charles Schwab (SCHW) Stock Could Be A Bargain Based On Returns
- Summary: Positive analyst view that Schwab stock may be undervalued based on returns.
- Date: 2026-10-31 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxObTFUOFN4cmpuSll5aHAtTm1ZRDU4TUEzRGYtTXBvb1VFQ3YwS1FqUVhZOUp5VEdTbnNLU3lFNVBScm9GZFNRYWp2R1gyVm5HRFNVOVllRjRMUTZrNkZVeUtFQVI3a05pb2dNR1MzanJhNmZIcU16aE8tNUprT3lxWVcyWEhnNktjcEZHSXVOT255WUhqNV9pd3RnRm0?oc=5>

## HEADWINDS

No items in this run

## CATALYSTS

### Charles Schwab (SCHW) Faces 23 Hour Trading Review After Record Revenue Quarter
- Summary: Charles Schwab (SCHW) Faces 23 Hour Trading Review After Record Revenue Quarter
- Date: 2026-10-31 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi3gFBVV95cUxQQ1FQbHMxV0hkbjFnbHdqRjFzSHVCTzg4Smw0MlFpU09Ib19HRDZCTDZwVjZYMGlGUW5Mcy0yZklWcW43eWNBY052R0dSdkZLYVJlSE85NjZ6LWppVmJEaVR5Y3NNSXJBYVlwWlJhYmxMM0ZJNDlDblpCYjVwLXozakJ6cGdNWVcxWWN4RUFWdzZhQUc1dUQ2UU9TNXFHMTZ0VVJXdnpKOGVqcXIzbXYtM2cxXzhuNUsxQkNYTTlaMzdfc1ZOVTNMWlZoNXozMHRTTC0xWFFleTlfQW1GNXfSAeMBQVVfeXFMT2RiMVVCcnViYWROTTFmcVM0cGpoWWVvdHhVN2tsYldVcVJMYnFYb1ltSWpIaWxSa1Nwbjk2T3NXeTJIUzBVN0k1Uk01U0xfbFd1Q1hLSmhvNUxVLXNaSmVWSWpLdlR2Ujd3UmJtSGRNM1FOOEkxX0hGN0xKVFgzSkhBbHlsX0JPbFlXSWtyV29TcnFrYVJpalByYnFzc1Z3cE01YlhmdW9NaVZmZnFqYzdFZnU4ZlNCZHExZ3h1aE41VkxyRmpWRC1oWkM4WFRmQi1iRWxRd2ctbHFHLUYxVUdSSzQ?oc=5>

### Charles Schwab (SCHW) CEO Says Retail Investors Should Have Greater Access to IPOs
- Summary: CEO promotes broader IPO access for retail investors, indicating strategic guidance.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxPX1hrWVJjVW8zYXhqTkRjdm44WTlka0dsTElaMmdibXpUZlRkdE8xcHZPdDY4b0Mwb1BYN1pOZ1NSeVB0Rm5zYllRdTRfZThVTmZ6ZFpPeno3MlpJeVhELW1DSW5TUmowVlg0N0dBMHQ0cE45TTl5V3diMFotVzNSY2x2NWl3RUswNVdZcUNfMHNmQUFDeHJpN0tBWUMxdHFuSTVlZ1VYV2M?oc=5>

### Charles Schwab (SCHW) Expands AI Tools For RIAs, Is The Stock Still 25% Undervalued?
- Summary: Schwab expands AI tools for RIAs, signaling product enhancement.
- Date: 2026-10-31 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxPVmtZQzNUTUxSSDVBZVgwUURWUWREZ2ZNM0owNGdwWHlkYjVOdUZYWFhMQnlBZXVIZTBwQUlDOFc1Rmo1Q29wVWFRaXQtRGVoRV8tYUVCSjlnc3BpMU5Vb19QZERTNERMNEZTa1BtUE51X3JlZUhSOFJSUk9xU3ZLamNwSUZpWjREclIxLUFDc3Z1dGRSSUNsemI3aw?oc=5>

### Mirae Asset Global Investments Co. Ltd. Makes New Investment in The Charles Schwab Corporation $SCHW
- Summary: Mirae Asset invests in Schwab, indicating confidence in the firm.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi7wFBVV95cUxPY0o3cTFzSU1qemozT3M0Rlk3ZzFWd1RLMjByeWs4amxzWmhUZkx5UzNWMlhLdnRzR1d1LUdvNW9mQU9qZ2N1bEdEU3J2OXBna21kUmZicGtaOHlJQVN2eU04T2FyWl9jVVQyZFRqV2QxNjZXMkxRN05sWHBKTDFJajJYTWwzck1FYnhoRXhiOE1rRS05STlqSHN0SHZ0NnB5Nm9ucndtS2dTRks1YURCMU5HN3djdE9rV1JtaXhZWDVkQ3dVSjZLeU1tU2JmbGtRUmdkVTBJOXd6OVFlMEpfMk5PdzhqNnRDXzF5UkxDQQ?oc=5>

### Charles Schwab(SCHW.US) Officer Sells US$18.11 Million in Common Stock
- Summary: Officer sold $18.11M of Schwab shares, indicating personal liquidity move.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxOTk1pamQwVlFrNS1OS2ExNDlMczZKNGh5ZWNHa1N0c19oLXI0N2l3cll0MlU3MTdJd3NpTzFtVXRNYnZ3ZG8zM0hzbkNaS2N2WUY4V0ZjT3F4bUNhZkdkcnl2aFlraC1vZlFZSGw2Qnp3Qy0yWmpnSkFId0dGM2Fwb1E2dllqd3BSaTNtV3dlOVFrMnB6bkpBT0xfVWhKaHlB?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **SCHW** | **15.16** | **2.98** | **N/A** | **16.90** | **153,409,372,160.00 USD** | **-4.95** |
| IBKR | 29.35 | 5.45 | N/A | 13.50 | 127,496,519,680.00 USD | 6.80 |
| HOOD | 39.18 | 7.55 | N/A | 11.80 | 75,497,185,280.00 USD | -42.88 |
| LPLA | 16.27 | 4.02 | N/A | 17.80 | 23,253,846,016.00 USD | -20.57 |

Peers fetched as_of: 2026-11-02; SCHW reuses existing data (market data as_of: 2026-11-02); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-15
- Next expected earnings: 2027-01-21 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-02

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-08-07
- Revenue (latest available single quarter): 7,072,000,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- Net income (latest available single quarter): 2,800,000,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/316709/000031670926000031/schw-20260630.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMinAFBVV95cUxObTFUOFN4cmpuSll5aHAtTm1ZRDU4TUEzRGYtTXBvb1VFQ3YwS1FqUVhZOUp5VEdTbnNLU3lFNVBScm9GZFNRYWp2R1gyVm5HRFNVOVllRjRMUTZrNkZVeUtFQVI3a05pb2dNR1MzanJhNmZIcU16aE8tNUprT3lxWVcyWEhnNktjcEZHSXVOT255WUhqNV9pd3RnRm0?oc=5
- https://news.google.com/rss/articles/CBMi3gFBVV95cUxQQ1FQbHMxV0hkbjFnbHdqRjFzSHVCTzg4Smw0MlFpU09Ib19HRDZCTDZwVjZYMGlGUW5Mcy0yZklWcW43eWNBY052R0dSdkZLYVJlSE85NjZ6LWppVmJEaVR5Y3NNSXJBYVlwWlJhYmxMM0ZJNDlDblpCYjVwLXozakJ6cGdNWVcxWWN4RUFWdzZhQUc1dUQ2UU9TNXFHMTZ0VVJXdnpKOGVqcXIzbXYtM2cxXzhuNUsxQkNYTTlaMzdfc1ZOVTNMWlZoNXozMHRTTC0xWFFleTlfQW1GNXfSAeMBQVVfeXFMT2RiMVVCcnViYWROTTFmcVM0cGpoWWVvdHhVN2tsYldVcVJMYnFYb1ltSWpIaWxSa1Nwbjk2T3NXeTJIUzBVN0k1Uk01U0xfbFd1Q1hLSmhvNUxVLXNaSmVWSWpLdlR2Ujd3UmJtSGRNM1FOOEkxX0hGN0xKVFgzSkhBbHlsX0JPbFlXSWtyV29TcnFrYVJpalByYnFzc1Z3cE01YlhmdW9NaVZmZnFqYzdFZnU4ZlNCZHExZ3h1aE41VkxyRmpWRC1oWkM4WFRmQi1iRWxRd2ctbHFHLUYxVUdSSzQ?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxPX1hrWVJjVW8zYXhqTkRjdm44WTlka0dsTElaMmdibXpUZlRkdE8xcHZPdDY4b0Mwb1BYN1pOZ1NSeVB0Rm5zYllRdTRfZThVTmZ6ZFpPeno3MlpJeVhELW1DSW5TUmowVlg0N0dBMHQ0cE45TTl5V3diMFotVzNSY2x2NWl3RUswNVdZcUNfMHNmQUFDeHJpN0tBWUMxdHFuSTVlZ1VYV2M?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxPVmtZQzNUTUxSSDVBZVgwUURWUWREZ2ZNM0owNGdwWHlkYjVOdUZYWFhMQnlBZXVIZTBwQUlDOFc1Rmo1Q29wVWFRaXQtRGVoRV8tYUVCSjlnc3BpMU5Vb19QZERTNERMNEZTa1BtUE51X3JlZUhSOFJSUk9xU3ZLamNwSUZpWjREclIxLUFDc3Z1dGRSSUNsemI3aw?oc=5
- https://news.google.com/rss/articles/CBMi7wFBVV95cUxPY0o3cTFzSU1qemozT3M0Rlk3ZzFWd1RLMjByeWs4amxzWmhUZkx5UzNWMlhLdnRzR1d1LUdvNW9mQU9qZ2N1bEdEU3J2OXBna21kUmZicGtaOHlJQVN2eU04T2FyWl9jVVQyZFRqV2QxNjZXMkxRN05sWHBKTDFJajJYTWwzck1FYnhoRXhiOE1rRS05STlqSHN0SHZ0NnB5Nm9ucndtS2dTRks1YURCMU5HN3djdE9rV1JtaXhZWDVkQ3dVSjZLeU1tU2JmbGtRUmdkVTBJOXd6OVFlMEpfMk5PdzhqNnRDXzF5UkxDQQ?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxOTk1pamQwVlFrNS1OS2ExNDlMczZKNGh5ZWNHa1N0c19oLXI0N2l3cll0MlU3MTdJd3NpTzFtVXRNYnZ3ZG8zM0hzbkNaS2N2WUY4V0ZjT3F4bUNhZkdkcnl2aFlraC1vZlFZSGw2Qnp3Qy0yWmpnSkFId0dGM2Fwb1E2dllqd3BSaTNtV3dlOVFrMnB6bkpBT0xfVWhKaHlB?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
