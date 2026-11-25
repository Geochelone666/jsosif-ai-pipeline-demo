# DIS Intelligence Report

- ticker: **DIS**
- Report as_of: **2026-11-24**
- Market data as_of: **2026-11-24**
- Quant sources: https://finance.yahoo.com/quote/DIS/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/DIS/key-statistics/
- AI analysis snapshot as_of: **2026-11-24**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-25T07:08:35.033181+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 1, 'ai': 16, 'unknown': 0, 'irrelevant': 7})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **10** exact headline/source/date matches; prior report **20261124T081701Z-6c335e3d/DIS** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **0**; {}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 14 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 20.83%; oldest publication 2026-11-17

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 122.5100 |
| Return 1D (%) | 1.8625 |
| Return 1W (%) | 4.7631 |
| Return 1M (%) | 8.8784 |
| Return YTD (%) | 8.5073 |
| Return 1Y (%) | 21.9187 |
| Annualized volatility (%) | 26.4955 |
| Beta vs SPY | 0.5340 |
| Max drawdown (%) | -20.2451 |
| Sharpe (rf=0) | 0.8831 |
| Downside deviation (rf=0, %) | 17.5111 |
| Sortino (rf=0) | 1.3362 |
| Historical VaR 95% (1D, %) | 2.3418 |
| Historical ES 95% (1D, %) | 3.3566 |
| Correlation vs SPY | 0.3014 |
| Tracking error vs SPY (%) | 26.2069 |
| P/E (trailing) | 21.76 |
| P/B | 1.90 |
| EV/EBITDA | 11.42 |
| Revenue growth (%) | 15.50 |
| Forward P/E (estimate) | 14.31 |
| Gross margin (%) | 38.02 |
| Operating margin (%) | 16.57 |
| Return on equity (%) | 9.13 |
| Free cash flow yield (%) | 3.56 |
| MA50 | 111.1420 |
| Close vs MA50 (%) | 10.2284 |
| MA200 | 103.8324 |
| Close vs MA200 (%) | 17.9883 |
| RSI (14, Wilder) | 64.4747 |
| MACD (12,26) | 2.7734 |
| MACD signal (9) | 2.7421 |
| MACD histogram | 0.0313 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'DIS': 289, 'SPY': 289}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 122.5100 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 1.8625 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 4.7631 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 8.8784 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 8.5073 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 21.9187 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 26.4955 -> Moderate annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 17.5111 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.3362 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 2.3418 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 3.3566 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.3014 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 26.2069 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.5340 -> Moves with the market with reduced sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -20.2451 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 0.8831 -> Modest risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 14.3091 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 38.0230 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 16.5650 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 9.1270 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 3.5610 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 21.7602 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 64.4747 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 0.0313 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 10.2284 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 17.9883 -> Clearly above the moving-average trend level.

## TAILWINDS

### Walt Disney (DIS) Beats Q4 Earnings and Revenue Estimates
- Summary: Walt Disney (DIS) Beats Q4 Earnings and Revenue Estimates
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMikwFBVV95cUxQZ2hDaXFGQUsyQkpHOUJ3UWRLRXNxWWdSdmljN0pFOEZxNFZpNzNjSW94bjRwSmFMOHRJSUdqR3RodDBodl9tUFo0Wl9RVVhrVGsyVTdkbHV5alZfeERRdjhRTHhCVkxrbXVWOUFweGpCbGFMeTNNWGtsUDhIeEN1eG14bkF0ME5yTXo2SmtxdWRzNVU?oc=5>

### How Record Earnings Will Impact Disney Stock Investors
- Summary: Record earnings boost Disney stock investors.
- Date: 2026-11-23 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxPeTJaTWxRYWlkUHpsRmlxeFg3QTQyVFZ2VVVCX3NiOVZOYWR5VVM1NkNFSmFIQ1VXeWVUM3R1dkx5dk02ZTFKQ2hPV29NWGNOQXJmdmVuZmstUmt3LUtEWkhZTS1nV0ZXaXc5MTBCLWVYdzdjVDJzZk5sMGljelBxQjhxblp3NUo1SmxZUFNnMGpvTGF3eE85RzMwQzJlbkxKby0wekNTZDdwUnd2S3EyUjBWbnNFMjBNNEHSAb8BQVVfeXFMUHYyTFo4ekswb2NNOEc0VWowbXhDaTN0d1JQMmJtMlhQZWhKdnFVbzdQcy1aTnZmYWZXZXF1MzFkV1cxLVhrUlMtc3lINjNPOHlwUy1vZFh2amNjS3dIRlFuelpGeWJMOU5VU0ZsN0FMSXUtTUZPSEQxOW5ZaU1OMS03N2FzYmdyN0IzRGs3cWsweEs5WDZWT3k0M1RoSHU5ZVJicG9FeVJrOFo0cDAweTZpd296TVlfMkttVmpqUnM?oc=5>

### Disney Stock Hits New Highs After Strong Q4 Earnings: Time to Buy DIS?
- Summary: Strong Q4 earnings push Disney stock to new highs, signaling positive momentum.
- Date: 2026-11-17 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxPejRicWlDWmJXV3lqdXd2SnRSY0l1TGt1OHA3SEJ0THIwOGVhWDFPblRvMUVCSzhHajJCUHhiMFJ4amZPSUQzc1ctd1BZekNhNnRDemRlWTFFZzA1aGlTb093Q1dDczA4aXFFSUJKSWR3UUVFMjQ2ODNKTjlxVENzMGVpYUVLR25nQ2p4MV9qMnBHODhJYUd2bHY1NkF5X0Jw?oc=5>

### Why Walt Disney (DIS) Stock Is Up Today
- Summary: Shares rise today, reflecting positive market sentiment.
- Date: 2026-11-18 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiggFBVV95cUxQZnh2R3I4X0poWVF5Q2tUOU1DMVJyWTktZk5vS3lIUkZtSTVWTlJYV2N3NzJBZUUyTEFoT2JTc0MwV1ktUGlwNWhXaUFoN3Bua3Y4bWpuQUxuUEcyY3pOZ3A3UWRCd3UxSlg4VVhUWnl3VDJPakpqN2hVTVNMMGdtNExB?oc=5>

### Disney's Winning Formula: Blockbusters, Packed Parks and Football
- Summary: Strong business mix drives growth prospects.
- Date: 2026-11-17 | Impact: high | Horizon: medium | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMiuwFBVV95cUxQeDJER3pDY3I3Rk9HWVpKT0kta1NOVTJ1Ym5PQ3NmbmttRnUzMnIzb0dEVmtLVkhWN21qSktYZXI3cDBfUzBET3BkTkdDWlphSFhhQllOQldjUzhzaDdVY3RPRXd2blM1NklLaVRaUjd2V19BVWFiZW1BSEd2eXMxamlCeTE0NXJocGtTekRHVkF3MGNnWDV5SGphYmNnTVlhX2hXLTlHRTNwdGpfRHUteWEzWVZVUzI5dUVv?oc=5>

### Disney Just Raised Its Dividend 33%, Giving Shareholders a Bigger Payday
- Summary: Dividend increase boosts shareholder returns.
- Date: 2026-11-17 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitAFBVV95cUxPaEtxRVYxd3FpdWpqeE1nbFd2by1wdnJoVlhHVE91RWl4UXVQblVuWGRUUmNCVDRyOVdLOTVYU2hUZWk3aENjc3hMQVFmUWhrNnlvaV9nbE80RUJZdmxnTzNHNnFtMXNiV3VnbkgxanMxTldIekRGWGRfbExoSmxIQmRxYnJZWlZOOVRRWkVUSktMdWVZLTBCTEY2TzVrNEt2dkMtT1hqSHRPc1ZYT0FKc2hPTF8?oc=5>

### Walt Disney (DIS) Beats On Earnings And Lifts Dividend, Is The Stock Fully Valued?
- Summary: Earnings beat and dividend lift signal strength.
- Date: 2026-11-19 | Impact: high | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxOSlR6R2lQb1lmNFR6V25TX09faUo4S25sTmFPZld3dXI3YkNlUmxoNW9Nd3BPaG1aa1hjbXB2RW56R1JpZW5laElmU0lfdElmMnEwZWhPTGpNOHVrRXhzVGFjeVg3TXZPMWs2aFJIdTg4c3pTTGREWW9PR0QxQ3VTVlFfTWhMT1hsR1VsaGcwNGJDSW0xcGw5MmhXVTZZWmRzSHNHczVHa05KVV9xMVJISnlXZ3RJTUNNZ3M0OVlQdE3SAcYBQVVfeXFMT1RwQWphbFNyX0dsejdVY3hEc25GWU42WmhhQ3FTTG01N0xwMVZWb0c1cnlGRTYtVGluc2V0am9udzFnWHJVWkFiODU2SEdZYy1OODlYNWk4UXRIeHpYVGRGWnpqd0Rvb1FZTEVWRnU3U2FoVm1Wc2VLczdxOUF2R3daTFkwckdjTUxwT1MzQTgtWnJUSnJfUF9QYXJUUzhTdDZxVm5QSEgzWFN1aFBnTGRJc2V5TXYxSnlHY20tbk1xZVRDRmdB?oc=5>

## HEADWINDS

### Disney Stops Reporting Streaming Profit. Should You Worry?
- Summary: Disney ceases streaming profit reporting.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxNTy1FUDdSVTVGYWN4OHZXTkxUT3NIRm41b2F1LWVIUHNwNFBVd1hJTlpmQUpodjB2ckFPVU5vY196UzJzNHQ5M3VMWWRlLXI5d2F2X2V6YnYzSlBwSS02ejhEd0hDNk1MZ3RWNXg5ajcwTnduNFd6cVpGV3VURVJleUlFdERVZzY5aXNKVnBiYkpfNy1NVE43VXA4RENVUG1mQjIzeC1DN09CeHJ4M1lqSFJsZ096ODg?oc=5>

### Disney: Economic Outlook Clashes With Disney Goals (NYSE:DIS)
- Summary: Economic outlook conflicts with Disney's goals, indicating potential challenges.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxQSnBqVXZUdi1CY0cxV0JwLS1IOTQ3UW5sUjlNUXV3TlpBRzdENkVNdEJsaDVaUGNuWTVPbFh3cWxHNm5BeWMtUjNVSWxkaWQ5ckdQYTZ5eHRjTkc0WF9vTF9jampzMFVsY19OczRWRHFCTzhva1ZnbkxsQlg3LWo0QWN5dUdpRWdvN1NmV1RXaXJ2dmpy?oc=5>

### Disney Wants $3 Billion in Savings, and More Layoffs Are Coming
- Summary: Cost cuts and layoffs signal financial pressure.
- Date: 2026-11-18 | Impact: high | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMiqAFBVV95cUxOdkNjV1FhTlZ1bnVCZ0g2ZnZXY3A4cVRQMjNaUzJpa0o4WWRseVdnOUhDVFcteHg5a29NX0Z1UXNBemhfNUpjdmd5M1AyRm5PR1VjUktvd3RxSHpDLWc3U1p3OWJCYnFfR3JRNUtoeUlUV25QcGhuRm1TOG5LRGs5TXVCT3J3S2EwTDlPdlBZX0tUQnBTQ1gzNWprekZzdFM2TGtHZC05SGo?oc=5>

## CATALYSTS

### DIS: Walt Disney Company filed SEC Form 8-K: Leadership Update, Financial Statements and Exhibits
- Summary: Leadership update and financial statements filed in SEC 8-K.
- Date: 2026-11-23 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMirgFBVV95cUxORll2WnljNW55VXE0NkNxU2VJMERnWDhYaVdQdDZ2T2lxUFpsRDBxOUVNYTlxLWZPQUtPSk1HSW52UFFaS05uZ21QWmxXeEJwVTBiUkxKdkJkUUpoZU5IR1o0NkhfcHNkYV9lYUd5Q25pWWxERk9PeUF1Ylc1MXhjUHR1OEtuOWl4NG00eTdVRjVLc2JyejRzRVVOa0lGVDhPTmpnVlNTanlITm13NkE?oc=5>

### Disney Just Boosted Its Dividend by 33%. That Gives DIS Stock Investors a Real Reason to Stick Around.
- Summary: Disney increased dividend by 33%.
- Date: 2026-11-20 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMi2wFBVV95cUxPSlowejN5VDB0OWxkUnJIMmhHclNmWWNaM3M5SE9FTFJHb09JYnRiQjNZSWxha3JrUUw4SFQ3UXhJQkhBbDJMYkg1dEw2Ym1IdG1tZDIwTWZicVhfLW0zQlVzanVGaUppNm54SlphanNyZ3ZEanhPQ0hhc2Y2Q0lQWGFlUVgtZEhPOXB5ODQ4ejI2QlV3TktSZFZZdVFGV1ZnaURiSU1HdklOc0tpYjBVb1Y0aUV2cjhOeE9SU0R2Zi13czNYemVkSFI3RW0zWnliYUR3MjFJYmp5QUk?oc=5>

### Disney (DIS) Stock Slips As Q4 Earnings Contrast Margin Compression
- Summary: Margin compression in Q4 earnings leads to a stock decline.
- Date: 2026-11-18 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilAFBVV95cUxOZ2VGTzJFbDNmLV9HcDNCekJ4ODh6Q0ZVaXZENUNtR2o5Sm5BamdyQnhJZlpfWG9HeWxCMmp3TlFmQnI4TkZCS0pXVDJqdGlXN2cxSnNidnI4aklkYUo0XzB1MjhhX1M1YmhBYlQ1ckhCd1BmaDIwc3RJYlhuWmZNd3BseV9QYWN3dS1nMURMS0tyRGFo?oc=5>

### Disney (DIS) Stock Looks Fully Priced Following Q4 Earnings Beat
- Summary: Q4 earnings beat, but stock appears fully priced, suggesting limited upside.
- Date: 2026-11-19 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxOQkZvSUplV09USFNrSTY5N05ROUhsRmFmREhnM0NtVjNrclE4ODJibkV3dTU3SDEtaXZESjBUZU5PUVVCd1JBVk4zeGRBbzI5azAtLVc1dmVxZXdRdkc0X3hsTV96ZGpOMlEtSW5YQTZ1ZHRyRGMxTG5tMk5vRjFQMlg0eThCUm5wbGIwSlVxcm1Ea1gycDR5Wg?oc=5>

### Disney quarterly earnings exceed forecasts as streaming profitability improves (DIS:NYSE)
- Summary: Disney reported Q4 earnings surpassing forecasts, driven by improved streaming profitability.
- Date: 2026-11-17 | Impact: high | Horizon: short | Confidence: 1
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxQdFZnYU1KZVJvd0dMR002enhzVDhxYmR2V2E3SDNVRzdJMUV0Z1RWelhXSFVvXzhseEpMcl9hMmU1SWRnZTd3MmJCYm1KWGV6QkNfcVJIbFFoT0dHLXNTcmR5anZXbUtSOTNsQk1UcUZCOVI3Q0hMMTcxT1BFLTdjZW9BWUZ3NjRra2RyLUdOYlpxcENSVVgxb3BldFd3UHBhOFFHX1JhSzVDMEYzeHFPVUVNSEV4WU0?oc=5>

### Disney: One Franchise, Several Ways To Make Money (NYSE:DIS)
- Summary: Disney highlights diversified revenue streams across its franchise portfolio.
- Date: 2026-11-17 | Impact: medium | Horizon: short | Confidence: 1
- Sources: <https://news.google.com/rss/articles/CBMikgFBVV95cUxNdE9hMWU2LUE3aFFJUEtqSjVTWkpnM2VoeVpzY3hZQ2FCcGY1Q3B1TUQ2VUdKNVFUQWNsV0FfbExscmhVTVg1dEVudnFqMHFjMTBqM0hPSU83YW91eVMtay1uTkhUMFVXX2ZIWHoxNmJnekJlZVJNVS1XcjFHeUhZdmQxQkpJaURHdkNYMDA3MGtKQQ?oc=5>

### Disney Q4 Earnings Beat Estimates, Revenues Rise Y/Y
- Summary: Disney's Q4 earnings exceeded estimates with year-over-year revenue growth.
- Date: 2026-11-18 | Impact: high | Horizon: short | Confidence: 1
- Sources: <https://news.google.com/rss/articles/CBMiqwFBVV95cUxNTVU3UmJGMDBGdUNreEFQQUV3MHFqRFZhVW1rbUdDY0J0OWhVeElwSko2MjZaSXhMZkR3ZmxKYWdEakNHMXoxbFkyTm9HMVNtYUM4eVBnM0xGQ0lERmdLQk1wRFlKMU9zREQ2bmQ0dWNxRzlHd1ZNMkVWcWlUSG9uZUdPMGVsRnpJLW0tUmFSRGV4WUM2alhKQUVXYmY2QnJ6bk5JUXRFVlE4cjg?oc=5>

## RISKS

No items in this run

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **DIS** | **21.76** | **1.90** | **11.42** | **15.50** | **209,250,713,600.00 USD** | **21.92** |
| NFLX | 17.01 | 8.25 | 15.73 | 11.80 | 241,739,415,552.00 USD | -44.97 |
| WBD | N/A | 2.36 | 13.79 | -11.20 | 77,595,885,568.00 USD | N/A |
| PSKY | N/A | 0.93 | 7.95 | 0.90 | 10,992,190,464.00 USD | N/A |

Peers fetched as_of: 2026-11-24; DIS reuses existing data (market data as_of: 2026-11-24); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-11-17
- Next expected earnings: 2027-02-01 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-24

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.10 | 2026-10-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 337.48 | 2026-10-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-K
- Filing date: 2026-11-17
- Revenue (latest available single quarter): 25,248,000,000.00 USD; period 2026-03-29/2026-06-27; fiscal year/reporting period 2026/Q3
- Net income (latest available single quarter): 2,638,000,000.00 USD; period 2026-03-29/2026-06-27; fiscal year/reporting period 2026/Q3
- SEC link: https://www.sec.gov/Archives/edgar/data/1744489/000174448926000066/dis-20261003.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMikwFBVV95cUxQZ2hDaXFGQUsyQkpHOUJ3UWRLRXNxWWdSdmljN0pFOEZxNFZpNzNjSW94bjRwSmFMOHRJSUdqR3RodDBodl9tUFo0Wl9RVVhrVGsyVTdkbHV5alZfeERRdjhRTHhCVkxrbXVWOUFweGpCbGFMeTNNWGtsUDhIeEN1eG14bkF0ME5yTXo2SmtxdWRzNVU?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxPeTJaTWxRYWlkUHpsRmlxeFg3QTQyVFZ2VVVCX3NiOVZOYWR5VVM1NkNFSmFIQ1VXeWVUM3R1dkx5dk02ZTFKQ2hPV29NWGNOQXJmdmVuZmstUmt3LUtEWkhZTS1nV0ZXaXc5MTBCLWVYdzdjVDJzZk5sMGljelBxQjhxblp3NUo1SmxZUFNnMGpvTGF3eE85RzMwQzJlbkxKby0wekNTZDdwUnd2S3EyUjBWbnNFMjBNNEHSAb8BQVVfeXFMUHYyTFo4ekswb2NNOEc0VWowbXhDaTN0d1JQMmJtMlhQZWhKdnFVbzdQcy1aTnZmYWZXZXF1MzFkV1cxLVhrUlMtc3lINjNPOHlwUy1vZFh2amNjS3dIRlFuelpGeWJMOU5VU0ZsN0FMSXUtTUZPSEQxOW5ZaU1OMS03N2FzYmdyN0IzRGs3cWsweEs5WDZWT3k0M1RoSHU5ZVJicG9FeVJrOFo0cDAweTZpd296TVlfMkttVmpqUnM?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxPejRicWlDWmJXV3lqdXd2SnRSY0l1TGt1OHA3SEJ0THIwOGVhWDFPblRvMUVCSzhHajJCUHhiMFJ4amZPSUQzc1ctd1BZekNhNnRDemRlWTFFZzA1aGlTb093Q1dDczA4aXFFSUJKSWR3UUVFMjQ2ODNKTjlxVENzMGVpYUVLR25nQ2p4MV9qMnBHODhJYUd2bHY1NkF5X0Jw?oc=5
- https://news.google.com/rss/articles/CBMiggFBVV95cUxQZnh2R3I4X0poWVF5Q2tUOU1DMVJyWTktZk5vS3lIUkZtSTVWTlJYV2N3NzJBZUUyTEFoT2JTc0MwV1ktUGlwNWhXaUFoN3Bua3Y4bWpuQUxuUEcyY3pOZ3A3UWRCd3UxSlg4VVhUWnl3VDJPakpqN2hVTVNMMGdtNExB?oc=5
- https://news.google.com/rss/articles/CBMiuwFBVV95cUxQeDJER3pDY3I3Rk9HWVpKT0kta1NOVTJ1Ym5PQ3NmbmttRnUzMnIzb0dEVmtLVkhWN21qSktYZXI3cDBfUzBET3BkTkdDWlphSFhhQllOQldjUzhzaDdVY3RPRXd2blM1NklLaVRaUjd2V19BVWFiZW1BSEd2eXMxamlCeTE0NXJocGtTekRHVkF3MGNnWDV5SGphYmNnTVlhX2hXLTlHRTNwdGpfRHUteWEzWVZVUzI5dUVv?oc=5
- https://news.google.com/rss/articles/CBMitAFBVV95cUxPaEtxRVYxd3FpdWpqeE1nbFd2by1wdnJoVlhHVE91RWl4UXVQblVuWGRUUmNCVDRyOVdLOTVYU2hUZWk3aENjc3hMQVFmUWhrNnlvaV9nbE80RUJZdmxnTzNHNnFtMXNiV3VnbkgxanMxTldIekRGWGRfbExoSmxIQmRxYnJZWlZOOVRRWkVUSktMdWVZLTBCTEY2TzVrNEt2dkMtT1hqSHRPc1ZYT0FKc2hPTF8?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxOSlR6R2lQb1lmNFR6V25TX09faUo4S25sTmFPZld3dXI3YkNlUmxoNW9Nd3BPaG1aa1hjbXB2RW56R1JpZW5laElmU0lfdElmMnEwZWhPTGpNOHVrRXhzVGFjeVg3TXZPMWs2aFJIdTg4c3pTTGREWW9PR0QxQ3VTVlFfTWhMT1hsR1VsaGcwNGJDSW0xcGw5MmhXVTZZWmRzSHNHczVHa05KVV9xMVJISnlXZ3RJTUNNZ3M0OVlQdE3SAcYBQVVfeXFMT1RwQWphbFNyX0dsejdVY3hEc25GWU42WmhhQ3FTTG01N0xwMVZWb0c1cnlGRTYtVGluc2V0am9udzFnWHJVWkFiODU2SEdZYy1OODlYNWk4UXRIeHpYVGRGWnpqd0Rvb1FZTEVWRnU3U2FoVm1Wc2VLczdxOUF2R3daTFkwckdjTUxwT1MzQTgtWnJUSnJfUF9QYXJUUzhTdDZxVm5QSEgzWFN1aFBnTGRJc2V5TXYxSnlHY20tbk1xZVRDRmdB?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxNTy1FUDdSVTVGYWN4OHZXTkxUT3NIRm41b2F1LWVIUHNwNFBVd1hJTlpmQUpodjB2ckFPVU5vY196UzJzNHQ5M3VMWWRlLXI5d2F2X2V6YnYzSlBwSS02ejhEd0hDNk1MZ3RWNXg5ajcwTnduNFd6cVpGV3VURVJleUlFdERVZzY5aXNKVnBiYkpfNy1NVE43VXA4RENVUG1mQjIzeC1DN09CeHJ4M1lqSFJsZ096ODg?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxQSnBqVXZUdi1CY0cxV0JwLS1IOTQ3UW5sUjlNUXV3TlpBRzdENkVNdEJsaDVaUGNuWTVPbFh3cWxHNm5BeWMtUjNVSWxkaWQ5ckdQYTZ5eHRjTkc0WF9vTF9jampzMFVsY19OczRWRHFCTzhva1ZnbkxsQlg3LWo0QWN5dUdpRWdvN1NmV1RXaXJ2dmpy?oc=5
- https://news.google.com/rss/articles/CBMiqAFBVV95cUxOdkNjV1FhTlZ1bnVCZ0g2ZnZXY3A4cVRQMjNaUzJpa0o4WWRseVdnOUhDVFcteHg5a29NX0Z1UXNBemhfNUpjdmd5M1AyRm5PR1VjUktvd3RxSHpDLWc3U1p3OWJCYnFfR3JRNUtoeUlUV25QcGhuRm1TOG5LRGs5TXVCT3J3S2EwTDlPdlBZX0tUQnBTQ1gzNWprekZzdFM2TGtHZC05SGo?oc=5
- https://news.google.com/rss/articles/CBMirgFBVV95cUxORll2WnljNW55VXE0NkNxU2VJMERnWDhYaVdQdDZ2T2lxUFpsRDBxOUVNYTlxLWZPQUtPSk1HSW52UFFaS05uZ21QWmxXeEJwVTBiUkxKdkJkUUpoZU5IR1o0NkhfcHNkYV9lYUd5Q25pWWxERk9PeUF1Ylc1MXhjUHR1OEtuOWl4NG00eTdVRjVLc2JyejRzRVVOa0lGVDhPTmpnVlNTanlITm13NkE?oc=5
- https://news.google.com/rss/articles/CBMi2wFBVV95cUxPSlowejN5VDB0OWxkUnJIMmhHclNmWWNaM3M5SE9FTFJHb09JYnRiQjNZSWxha3JrUUw4SFQ3UXhJQkhBbDJMYkg1dEw2Ym1IdG1tZDIwTWZicVhfLW0zQlVzanVGaUppNm54SlphanNyZ3ZEanhPQ0hhc2Y2Q0lQWGFlUVgtZEhPOXB5ODQ4ejI2QlV3TktSZFZZdVFGV1ZnaURiSU1HdklOc0tpYjBVb1Y0aUV2cjhOeE9SU0R2Zi13czNYemVkSFI3RW0zWnliYUR3MjFJYmp5QUk?oc=5
- https://news.google.com/rss/articles/CBMilAFBVV95cUxOZ2VGTzJFbDNmLV9HcDNCekJ4ODh6Q0ZVaXZENUNtR2o5Sm5BamdyQnhJZlpfWG9HeWxCMmp3TlFmQnI4TkZCS0pXVDJqdGlXN2cxSnNidnI4aklkYUo0XzB1MjhhX1M1YmhBYlQ1ckhCd1BmaDIwc3RJYlhuWmZNd3BseV9QYWN3dS1nMURMS0tyRGFo?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxOQkZvSUplV09USFNrSTY5N05ROUhsRmFmREhnM0NtVjNrclE4ODJibkV3dTU3SDEtaXZESjBUZU5PUVVCd1JBVk4zeGRBbzI5azAtLVc1dmVxZXdRdkc0X3hsTV96ZGpOMlEtSW5YQTZ1ZHRyRGMxTG5tMk5vRjFQMlg0eThCUm5wbGIwSlVxcm1Ea1gycDR5Wg?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxQdFZnYU1KZVJvd0dMR002enhzVDhxYmR2V2E3SDNVRzdJMUV0Z1RWelhXSFVvXzhseEpMcl9hMmU1SWRnZTd3MmJCYm1KWGV6QkNfcVJIbFFoT0dHLXNTcmR5anZXbUtSOTNsQk1UcUZCOVI3Q0hMMTcxT1BFLTdjZW9BWUZ3NjRra2RyLUdOYlpxcENSVVgxb3BldFd3UHBhOFFHX1JhSzVDMEYzeHFPVUVNSEV4WU0?oc=5
- https://news.google.com/rss/articles/CBMikgFBVV95cUxNdE9hMWU2LUE3aFFJUEtqSjVTWkpnM2VoeVpzY3hZQ2FCcGY1Q3B1TUQ2VUdKNVFUQWNsV0FfbExscmhVTVg1dEVudnFqMHFjMTBqM0hPSU83YW91eVMtay1uTkhUMFVXX2ZIWHoxNmJnekJlZVJNVS1XcjFHeUhZdmQxQkpJaURHdkNYMDA3MGtKQQ?oc=5
- https://news.google.com/rss/articles/CBMiqwFBVV95cUxNTVU3UmJGMDBGdUNreEFQQUV3MHFqRFZhVW1rbUdDY0J0OWhVeElwSko2MjZaSXhMZkR3ZmxKYWdEakNHMXoxbFkyTm9HMVNtYUM4eVBnM0xGQ0lERmdLQk1wRFlKMU9zREQ2bmQ0dWNxRzlHd1ZNMkVWcWlUSG9uZUdPMGVsRnpJLW0tUmFSRGV4WUM2alhKQUVXYmY2QnJ6bk5JUXRFVlE4cjg?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
