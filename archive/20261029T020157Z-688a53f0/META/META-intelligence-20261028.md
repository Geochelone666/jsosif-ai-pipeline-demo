# META Intelligence Report

- ticker: **META**
- Report as_of: **2026-10-28**
- Market data as_of: **2026-10-28**
- Quant sources: https://finance.yahoo.com/quote/META/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/META/key-statistics/
- AI analysis snapshot as_of: **2026-10-28**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-10-29T02:20:58.886559+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 8, 'ai': 11, 'unknown': 0, 'irrelevant': 5})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **5** exact headline/source/date matches; prior report **20261028T015717Z-533e470c/META** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'low_uncalibrated_model_confidence': 1}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 15 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 25.0%; oldest publication 2026-10-26

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 612.4900 |
| Return 1D (%) | -1.2416 |
| Return 1W (%) | -12.1903 |
| Return 1M (%) | -14.4113 |
| Return YTD (%) | -6.9723 |
| Return 1Y (%) | -18.2147 |
| Annualized volatility (%) | 42.7411 |
| Beta vs SPY | 1.5040 |
| Max drawdown (%) | -29.9428 |
| Sharpe (rf=0) | -0.2595 |
| Downside deviation (rf=0, %) | 29.7613 |
| Sortino (rf=0) | -0.3727 |
| Historical VaR 95% (1D, %) | 3.7761 |
| Historical ES 95% (1D, %) | 6.2110 |
| Correlation vs SPY | 0.4470 |
| Tracking error vs SPY (%) | 38.7660 |
| P/E (trailing) | 21.16 |
| P/B | 5.75 |
| EV/EBITDA | 13.75 |
| Revenue growth (%) | 26.10 |
| Forward P/E (estimate) | 17.43 |
| Gross margin (%) | 81.03 |
| Operating margin (%) | 35.41 |
| Return on equity (%) | 32.26 |
| Free cash flow yield (%) | 1.06 |
| MA50 | 666.8185 |
| Close vs MA50 (%) | -8.1474 |
| MA200 | 631.2948 |
| Close vs MA200 (%) | -2.9788 |
| RSI (14, Wilder) | 30.6871 |
| MACD (12,26) | -16.0637 |
| MACD signal (9) | 0.3261 |
| MACD histogram | -16.3897 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'META': 270, 'SPY': 270}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 612.4900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: -1.2416 -> Adjusted price fell over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: -12.1903 -> Adjusted price fell over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: -14.4113 -> Adjusted price fell over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: -6.9723 -> Adjusted price fell over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: -18.2147 -> Adjusted price fell over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 42.7411 -> High annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 29.7613 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: -0.3727 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 3.7761 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 6.2110 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.4470 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 38.7660 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 1.5040 -> Amplified market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -29.9428 -> Moderate peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: -0.2595 -> Negative risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 17.4250 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 81.0340 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 35.4140 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 32.2640 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 1.0569 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 21.1568 -> Moderate trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 30.6871 -> Neutral momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: -16.3897 -> Negative momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: -8.1474 -> Clearly below the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: -2.9788 -> Slightly below the moving-average trend level.

## TAILWINDS

### Meta Stock Falls On Plan For $95 Billion Equity Raise. Analysts Are Offering A Positive View.
- Summary: Meta Stock Falls On Plan For $95 Billion Equity Raise. Analysts Are Offering A Positive View.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMigwFBVV95cUxQRVNaVzVKMV9fbDV0TlVybC05NnZsay1zWEc3ZDBtbDVBVWxuYkltbE9DSmRVY2RsR2Z3RTJaREF1MWZ6ZWhfeVdxTHVhdV9PYS1zRG1LVGplM1ViYnBVbEZmUVhoTHh5cFduaWhkbG51SEhVaXd6OVIybjc5ekI4Z1Nrbw?oc=5>

### Meta Will Offer Up to $95 Billion in Stock. What That Means for Its Big AI Push.
- Summary: Meta plans a $95B stock issuance to fund AI initiatives, potentially diluting shares but boosting capital for growth.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMifkFVX3lxTE10bm9vdXZ0RDJuVWNfMGo5bnQtLTJ6b2c3WTlMNExXaEsyOUpiNEd0cGt0YVNldlZHNEtvaThTOXV3LUpBVEFmcmNOOTBSZDNPbTBmNGlFVzgwYkFqQmY2eExVUjR6UEEtNk1hNzdkWEgtTWs2bTZNbGl2a0hOUQ?oc=5>

### Meta Platforms: Muse May Be Metaverse 2.0, But It’s Too Late (NASDAQ:META)
- Summary: Meta’s Muse platform aims to revitalize its metaverse vision, though critics question its timeliness and competitive edge.
- Date: 2026-10-26 | Impact: medium | Horizon: medium | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxQU1U5NGk4c1k0U0Jfa2hBQUZmaVVFcndyNmQ5bUxXdmhVbjBDMWhnNy1SdDFvckd0cmxDOW9LY09hQ3EwTlpHRE9Ha2gwdnBEVHJrUWJJdFdDckk0a0lGeHE2RVFCS09leGI0czFWbHQ1VFc0d2dSR0dDZml0N1F5YXE4QWoxS2xDRlg0RWVQcjNkYzNNSUdMUWgxclJFbUk?oc=5>

## HEADWINDS

### Meta Shares Are Down 12% Since Earnings. Is the Stock a Buy?
- Summary: Meta Shares Are Down 12% Since Earnings. Is the Stock a Buy?
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijwFBVV95cUxPeEFsRjB6d2lwTVZ1UWhyVnhEZmkwRG9rQmo1dVp5d3plSFNEVzZHQllCakFVdXJaM2dQUklnQTEwMHp6MDlud0pmOERnSFVpeEtuMFY1ZjFGMmtkcGFlN2JSUVVMLTBDNEJqazJDUXVRWTBFczdKTXJVVTlXcHk2VHZJUE1aTTVfZm1uM2YzRQ?oc=5>

### Meta Platforms (NASDAQ:META) Stock Falls 1.2% - Here's What Happened
- Summary: Meta Platforms (NASDAQ:META) Stock Falls 1.2% - Here's What Happened
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxPbGF5WlpxNDVQeWZhVktWY0xfSnhWc0VLNE5IN1pHVFFwR2JXcUVFb05PcENMQ2R0SUI4Skk3ci1Va3oyeUNidHdUWGF5NEp3X0s2X2p1WmhZaE4waW52QkFDVWh6SDdKVVF1THBaNUdpVTJ0dWV6NDczbGlEWHppbWw5Y1YzR25Tc09RZ3IyYmFuU3k1QXJGR3EyQTV3SHFCV2k1RUh4bWp4MmQ0dENMY1pQa1pFaFBSVVd1R1h3?oc=5>

### Meta Stock Has Dropped the Day After 3 Straight Earnings Reports. Is It a Buy Now?
- Summary: Meta Stock Has Dropped the Day After 3 Straight Earnings Reports. Is It a Buy Now?
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiwAFBVV95cUxNamJrMEYxSG9NeTJWRVlfMjdWWS1veVlyS19zZlVicFJCVng5WTdmQ2wybEZnVjl2dkJoOTB5U3VROGhENnZITmNobklfdGtFRGlPeWlocUFldUlZbG1TQTRLQnpKVUNVTXNSXzMxdjVPZnhCd2RHLVBBcUptOHpsbnhDSXZENHhBdmFwMHItZjJfYk9xdTBBWDVhbVVBSVczaDNCZF8xMFJGOEtSVVJPa1NhczVld3JRdFNGYmw2Yno?oc=5>

### Meta Stock Sell-Off Looks Like an Overreaction
- Summary: Meta shares fell sharply, seen as overreaction to market fears.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiggFBVV95cUxQcHJtRUdQWm1ocmFuMnFtMTU0Zzc4WE9QTWZVSWllaWVaejhGQW13ZTZRMjZrWmt5Qm1LS1BackpkNXdqT1ozbTlEUzNJUS02X3RhZGs4cjJNT1lyMUhVaVRHX3RFdm1vcFNYSkREUEFNblQwR01KdDFSazNIMDRYUkVB?oc=5>

### Zuckerberg Stock Deal, Meta Restructuring Hit With Challenge (2)
- Summary: Zuckerberg's stock deal faces restructuring challenge.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxPbzRhY1NjSWVPZlI2eHBBdkdfN2JvblJESXFmRUZ3dE5JUkVxUjZZdzY1d2VFWE1YLTlEbFE4ck56Wk1jTTk3U2J1bzdfVmpuWHUzcVZmOElYYWh5M0U4eXBndUNhS2VtaGNEOHhMSTlSWUI1MjJrdDZKM3YtVWthNXlwM2ZzOHZMWmY2YnBOdEYyN0R0bkZQS3NB?oc=5>

## CATALYSTS

### Meta Announces Launch of Offering of Depositary Shares Representing Series A Mandatory Convertible Preferred Stock and Offering of Class A Common Stock in Connection with Forward Sale Agreements
- Summary: Meta Announces Launch of Offering of Depositary Shares Representing Series A Mandatory Convertible Preferred Stock and Offering of Class A Common Stock in Connection with Forward Sale Agreements
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMijANBVV95cUxON0lNaXV6RThzZ0ltRF9MS3VXbHJpTkdETG81Y2toYkd5QXN2NUVhX3BiSnNkVWhhUU1sNzdMV1RIS1lNSm44Z05LdmZiWk42WlB4OGE2YUZZSlRIX3ZQN3ByNUVrYmFBdWFnLVBwUUNqMW14bllLZnV0OTB2WG9CMHlBWXl6SUhZWnYyU1lmdHBNNm41dDVzb2RESnFuNElWallZa2ZMamtpc3lLNms3N2VyOUxpZjl0QlZ6UzRORkpadGJ1bTV0NG5NaERaNDdTc0NFSVExWVREaHFMaGZzOFU5bFZ2anl4aFRHaW5BdjBNbzdKU01NM211OHFubTlGV2stRHJBdlVjYlRSeUVLMnE3TGpNaU9Ya2FScjJyWlBRUnd6Z0xZdUR5djdQb2ZDQkVsZUkzSEw1d1V1SzNIcXBweTBvMVRIRmNTd0JFcWhsMlZhczJlVFkxcnhNMkVER0JqQU10Tm9JQzVZU3BkM1lFWVZEaXVYYnJ2Z3FCQW9DQks4TWZmbUQyWFg?oc=5>

### Meta Loses $400 Billion, Auctions More Stock, But Analysts Still See 1.4x Upside
- Summary: Meta Loses $400 Billion, Auctions More Stock, But Analysts Still See 1.4x Upside
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMinAFBVV95cUxQZDZCVy1CLS1KV1plaWZjVXo4UnZuWWVXbGRQNmtQcTRlM0lIeHBnaE5tVGg2dzN0MFJ2N0tQejFjbklESHhoTS1UX2p4SlUzQWhUZXFZTzJGM2NpTDFGUHJRSXVSS0N3YVpYRG9fUEM5Z2dMQmdYbkV0TEZkYUIxMUtWT2h3eVR6MGhqRFFUeFVqdklVQzd1TzlLeUw?oc=5>

### Meta Launches $35B Stock Offering, Plans Another $60B Program In 2027: Nvidia, AMD, Broadcom Eye Up To $5B Investment
- Summary: Meta Launches $35B Stock Offering, Plans Another $60B Program In 2027: Nvidia, AMD, Broadcom Eye Up To $5B Investment
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxPRUZTaHN0QlFyYk9uM1pRZWtkcWV4T19femtzQ3FwWXpGQnhDZDh0WFdQUU1EREtESlhjeUVKRUpfTkxfUjVhVGFFNFFnSUJ6NEc4RWNoUkJqZ19WdlNUNDZMb3U3N3RKUzZKa24zaTd0dkM0R0VLdThfUThyM1lIU2NOdlRXSHJTVXJyeUxfS1AtUnZqaVotNElVakI2QQ?oc=5>

### Meta Platforms Just Delivered Great News to AI Stock Investors
- Summary: Meta Platforms Just Delivered Great News to AI Stock Investors
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMioAFBVV95cUxNY3RFaF95TzNuUUhqODJYMkJYY0lNRkN1Qm1ydUtDTW40Y0sxUlQ3bXNwMzVVM0NTSTdKZjlqZXBoUjJ4cGs4TjBPSUZjZnhJNkN5eTQwMUtVOThqYVNNY1VCSzZKLUtlWVlsZEJJcTdOVVVoakV5ZmwyVzhIYi1MRHhER3ozS09pVFZGeHdWWkw2N215SHVoYTF1R1VHZ0p3?oc=5>

### Meta’s $25 Billion Stock Sale Ended Five Times Oversubscribed
- Summary: Meta completed a $25B stock sale, oversubscribed five times, signaling strong investor demand.
- Date: 2026-10-27 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMisAFBVV95cUxNdmR1WjllZWo5S013MU1kTmgzNWdZXzd3ejl4bHZFRlR6NUpLbWt5aHdaYkpzc3g4eG55M0Q2UGVHb01oSHBIUWZyY0tzTHNzMlU2clZ6NVFoZmJ3clRtYkZLWHFsWElfRHRibEw0UkZYMUNtQzNQcFVtejBQUjM4QVh6Yk9LdVMzOENZU1U3S0syTWRxSU9zdmFkQUlLY2hVQkFtVlFrN3lseGhEcWNPdA?oc=5>

### Meta eyes record $97.5 billion equity raise to fund AI expansion
- Summary: Meta plans a $97.5B equity raise to fund AI expansion.
- Date: 2026-10-27 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiswFBVV95cUxPclhjOFJvYkM0S0hLUmxaY0l2X3hCdWI0N1prZlo2QXhXdmt5T0pNQVpFODVpYzgycWdZcHM2NkZ2LTdaMEVUVlpTXzVFUzc2ZEdVdlpTeThUVkZtc3V4cEFTelk5bDd2Z0dfRDFsb0dGQ0MxRXhYMExFZTlXVkNjRXF6TDBLalZ5ZTFBbFMyX24wMVBTQW1GQkJNRjNYWTRiVGJJWWdialBfV1oyQUZNN3I4RQ?oc=5>

### Update: Meta Launches $35 Billion Stock, Preferred Offerings; Plans Potential $60 Billion ATM Stock Offering
- Summary: Meta launches $35B stock and preferred offerings, with a potential $60B ATM offering.
- Date: 2026-10-26 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNdllkTUQ0S1ZjSkxCUUNBYmFEUi1OQ0VWV2tsTmR0dzAzdEswdVNxY1g4c2t0aEtKTmdKZmhXX0xyMEFTamlPcE00Z1NYQnVnZTk4V2pzR1prWnBKSGdSNkpLaXpwYXNVVDFxcEZveFFoSUsxVkdNQUpqSlJ1QVJ5aGpnalo2alNBZXpWS1F5OHRXNUFraUUzTlU1NA?oc=5>

### Meta Just Priced a Stock Sale at $625 a Share. I'd Consider Buying at the Same Price.
- Summary: Meta priced a stock sale at $625 per share, suggesting a potential buy opportunity.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMixwFBVV95cUxNdVlzQ3pfeDlpYVJ0TjRSX3padDdtb2NvaWNmOW9HQ0dQQzRubEdVU2E4ZTRhWE9WVGFpYjFweXdpUFd5UV9xNFZvZGdqcDE2Sm5aNGt4cXlTMllQYVBtSXRlQmJneG5JdTJXa0xDX3EtdVhRZTFMN2tFNzNEV19NbXA5REoya1I2Z3o2ZWgtVXBFQ3I3MU9ld0gwV2k1N2pTNy1ITDM4cnp3TEdpME1qbWxVQjdUc0ZKRFl4WlRxNjdzSm9PYlFZ?oc=5>

### Meta Plans up to $95 Billion in Financing to Power Its AI Growth
- Summary: Meta announces $95B financing to boost AI initiatives.
- Date: 2026-10-26 | Impact: low | Horizon: short | Confidence: 0.6
- Sources: <https://news.google.com/rss/articles/CBMivgFBVV95cUxOWWVJZlJtQjJkZTMyWV9zMXNqV3RxZERPOE1CZlliQTVqR3VaTFk5anp5bHViM0pVTlVlc3lmMTU2YzVkb01hRXVsYU9yWUVFWjJxVHlrbW5TRVZoMWw3SzM1VUZ3UmpZN1NRODBhZmpHQXI4OXFCZDI5dWpMOGlTcGlWblREUUhmWHRCLWtZeW9zcnNUMVlRa2JTN0pwZ2dkSXBKQS14emotVmM1LWMtb2RxMEF5Y3RqNHBFZndn?oc=5>

### Meta Is Creating a New Class of Stock. What Shareholders Need to Know
- Summary: Meta announces a new class of stock, affecting shareholder structure and voting rights.
- Date: 2026-10-26 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxPeFFUWkhxYlJNc3labzFqU1hldXAwd3A4VHB0Wl9heUZ4d21vQnc0bWVoSVBwNlZiOERENjBTekYwODFoSk5uRGozUjdRQjdCd0JZLXpLSGplbjIxX1psNXBUY2NPeGZWM2FqemJBdU9LcHE0TTQyS1Q5TkY4OTZuUHUyVHdNRGlqRXZ2V3pvR2ZHaDR0d3pmR3Z5cS05eDFJVDBYcnVn?oc=5>

## RISKS

### Meta’s Pullback Just Changed The AI Risk/Reward (NASDAQ:META)
- Summary: Meta's pullback alters AI risk/reward profile.
- Date: 2026-10-28 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMijgFBVV95cUxOcGprcWFSbjJXN3c1TVdDM2xoZVhnRnVfRURPb0JsM0k4UzdjelprbGllNUp6akd3OFF0a0RQY3V3SDdBZksxWmtodTdpbzQzeWF3TTdfZ1VfOWV6cEFxZUNaa2ZaakVhZEp5V2Y2VUZQX09nOHpvVEhaTHdwWUgwNEpXZWgyWURSYjRIMjJR?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **META** | **21.16** | **5.75** | **13.75** | **26.10** | **1,594,209,206,272.00 USD** | **-18.21** |
| GOOGL | 16.08 | 6.38 | 22.35 | 24.20 | 3,973,383,716,864.00 USD | 21.78 |
| SNAP | N/A | 5.20 | -79.61 | 18.90 | 10,079,538,176.00 USD | -23.00 |
| PINS | 59.77 | 4.09 | 37.18 | 18.20 | 11,847,268,352.00 USD | -36.99 |

Peers fetched as_of: 2026-10-28; META reuses existing data (market data as_of: 2026-10-28); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-10-21
- Next expected earnings: 2027-01-27 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-28

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |
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

- https://news.google.com/rss/articles/CBMigwFBVV95cUxQRVNaVzVKMV9fbDV0TlVybC05NnZsay1zWEc3ZDBtbDVBVWxuYkltbE9DSmRVY2RsR2Z3RTJaREF1MWZ6ZWhfeVdxTHVhdV9PYS1zRG1LVGplM1ViYnBVbEZmUVhoTHh5cFduaWhkbG51SEhVaXd6OVIybjc5ekI4Z1Nrbw?oc=5
- https://news.google.com/rss/articles/CBMifkFVX3lxTE10bm9vdXZ0RDJuVWNfMGo5bnQtLTJ6b2c3WTlMNExXaEsyOUpiNEd0cGt0YVNldlZHNEtvaThTOXV3LUpBVEFmcmNOOTBSZDNPbTBmNGlFVzgwYkFqQmY2eExVUjR6UEEtNk1hNzdkWEgtTWs2bTZNbGl2a0hOUQ?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxQU1U5NGk4c1k0U0Jfa2hBQUZmaVVFcndyNmQ5bUxXdmhVbjBDMWhnNy1SdDFvckd0cmxDOW9LY09hQ3EwTlpHRE9Ha2gwdnBEVHJrUWJJdFdDckk0a0lGeHE2RVFCS09leGI0czFWbHQ1VFc0d2dSR0dDZml0N1F5YXE4QWoxS2xDRlg0RWVQcjNkYzNNSUdMUWgxclJFbUk?oc=5
- https://news.google.com/rss/articles/CBMijwFBVV95cUxPeEFsRjB6d2lwTVZ1UWhyVnhEZmkwRG9rQmo1dVp5d3plSFNEVzZHQllCakFVdXJaM2dQUklnQTEwMHp6MDlud0pmOERnSFVpeEtuMFY1ZjFGMmtkcGFlN2JSUVVMLTBDNEJqazJDUXVRWTBFczdKTXJVVTlXcHk2VHZJUE1aTTVfZm1uM2YzRQ?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxPbGF5WlpxNDVQeWZhVktWY0xfSnhWc0VLNE5IN1pHVFFwR2JXcUVFb05PcENMQ2R0SUI4Skk3ci1Va3oyeUNidHdUWGF5NEp3X0s2X2p1WmhZaE4waW52QkFDVWh6SDdKVVF1THBaNUdpVTJ0dWV6NDczbGlEWHppbWw5Y1YzR25Tc09RZ3IyYmFuU3k1QXJGR3EyQTV3SHFCV2k1RUh4bWp4MmQ0dENMY1pQa1pFaFBSVVd1R1h3?oc=5
- https://news.google.com/rss/articles/CBMiwAFBVV95cUxNamJrMEYxSG9NeTJWRVlfMjdWWS1veVlyS19zZlVicFJCVng5WTdmQ2wybEZnVjl2dkJoOTB5U3VROGhENnZITmNobklfdGtFRGlPeWlocUFldUlZbG1TQTRLQnpKVUNVTXNSXzMxdjVPZnhCd2RHLVBBcUptOHpsbnhDSXZENHhBdmFwMHItZjJfYk9xdTBBWDVhbVVBSVczaDNCZF8xMFJGOEtSVVJPa1NhczVld3JRdFNGYmw2Yno?oc=5
- https://news.google.com/rss/articles/CBMikwFBVV95cUxNeklvb08xd1ZtTzkySTRZbVhLZzY2QzMyRTI4dFk5ZmlYdGx6Z1JsS21pZWl4SEVpTXBPYWJLaU5LYmhVbTFuMUxRR0wwSXhzTlZmWDN2TC1yb3BYRHNJRXVmY0gtNmtNMTVpbU84WXI4S0E4Snc5Vk8wcDBxelZOOG5pTmpfbURqZ0dVczN4OGtreFU?oc=5
- https://news.google.com/rss/articles/CBMiggFBVV95cUxQcHJtRUdQWm1ocmFuMnFtMTU0Zzc4WE9QTWZVSWllaWVaejhGQW13ZTZRMjZrWmt5Qm1LS1BackpkNXdqT1ozbTlEUzNJUS02X3RhZGs4cjJNT1lyMUhVaVRHX3RFdm1vcFNYSkREUEFNblQwR01KdDFSazNIMDRYUkVB?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxPbzRhY1NjSWVPZlI2eHBBdkdfN2JvblJESXFmRUZ3dE5JUkVxUjZZdzY1d2VFWE1YLTlEbFE4ck56Wk1jTTk3U2J1bzdfVmpuWHUzcVZmOElYYWh5M0U4eXBndUNhS2VtaGNEOHhMSTlSWUI1MjJrdDZKM3YtVWthNXlwM2ZzOHZMWmY2YnBOdEYyN0R0bkZQS3NB?oc=5
- https://news.google.com/rss/articles/CBMijANBVV95cUxON0lNaXV6RThzZ0ltRF9MS3VXbHJpTkdETG81Y2toYkd5QXN2NUVhX3BiSnNkVWhhUU1sNzdMV1RIS1lNSm44Z05LdmZiWk42WlB4OGE2YUZZSlRIX3ZQN3ByNUVrYmFBdWFnLVBwUUNqMW14bllLZnV0OTB2WG9CMHlBWXl6SUhZWnYyU1lmdHBNNm41dDVzb2RESnFuNElWallZa2ZMamtpc3lLNms3N2VyOUxpZjl0QlZ6UzRORkpadGJ1bTV0NG5NaERaNDdTc0NFSVExWVREaHFMaGZzOFU5bFZ2anl4aFRHaW5BdjBNbzdKU01NM211OHFubTlGV2stRHJBdlVjYlRSeUVLMnE3TGpNaU9Ya2FScjJyWlBRUnd6Z0xZdUR5djdQb2ZDQkVsZUkzSEw1d1V1SzNIcXBweTBvMVRIRmNTd0JFcWhsMlZhczJlVFkxcnhNMkVER0JqQU10Tm9JQzVZU3BkM1lFWVZEaXVYYnJ2Z3FCQW9DQks4TWZmbUQyWFg?oc=5
- https://news.google.com/rss/articles/CBMinAFBVV95cUxQZDZCVy1CLS1KV1plaWZjVXo4UnZuWWVXbGRQNmtQcTRlM0lIeHBnaE5tVGg2dzN0MFJ2N0tQejFjbklESHhoTS1UX2p4SlUzQWhUZXFZTzJGM2NpTDFGUHJRSXVSS0N3YVpYRG9fUEM5Z2dMQmdYbkV0TEZkYUIxMUtWT2h3eVR6MGhqRFFUeFVqdklVQzd1TzlLeUw?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxPRUZTaHN0QlFyYk9uM1pRZWtkcWV4T19femtzQ3FwWXpGQnhDZDh0WFdQUU1EREtESlhjeUVKRUpfTkxfUjVhVGFFNFFnSUJ6NEc4RWNoUkJqZ19WdlNUNDZMb3U3N3RKUzZKa24zaTd0dkM0R0VLdThfUThyM1lIU2NOdlRXSHJTVXJyeUxfS1AtUnZqaVotNElVakI2QQ?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxNY3RFaF95TzNuUUhqODJYMkJYY0lNRkN1Qm1ydUtDTW40Y0sxUlQ3bXNwMzVVM0NTSTdKZjlqZXBoUjJ4cGs4TjBPSUZjZnhJNkN5eTQwMUtVOThqYVNNY1VCSzZKLUtlWVlsZEJJcTdOVVVoakV5ZmwyVzhIYi1MRHhER3ozS09pVFZGeHdWWkw2N215SHVoYTF1R1VHZ0p3?oc=5
- https://news.google.com/rss/articles/CBMisAFBVV95cUxNdmR1WjllZWo5S013MU1kTmgzNWdZXzd3ejl4bHZFRlR6NUpLbWt5aHdaYkpzc3g4eG55M0Q2UGVHb01oSHBIUWZyY0tzTHNzMlU2clZ6NVFoZmJ3clRtYkZLWHFsWElfRHRibEw0UkZYMUNtQzNQcFVtejBQUjM4QVh6Yk9LdVMzOENZU1U3S0syTWRxSU9zdmFkQUlLY2hVQkFtVlFrN3lseGhEcWNPdA?oc=5
- https://news.google.com/rss/articles/CBMiswFBVV95cUxPclhjOFJvYkM0S0hLUmxaY0l2X3hCdWI0N1prZlo2QXhXdmt5T0pNQVpFODVpYzgycWdZcHM2NkZ2LTdaMEVUVlpTXzVFUzc2ZEdVdlpTeThUVkZtc3V4cEFTelk5bDd2Z0dfRDFsb0dGQ0MxRXhYMExFZTlXVkNjRXF6TDBLalZ5ZTFBbFMyX24wMVBTQW1GQkJNRjNYWTRiVGJJWWdialBfV1oyQUZNN3I4RQ?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNdllkTUQ0S1ZjSkxCUUNBYmFEUi1OQ0VWV2tsTmR0dzAzdEswdVNxY1g4c2t0aEtKTmdKZmhXX0xyMEFTamlPcE00Z1NYQnVnZTk4V2pzR1prWnBKSGdSNkpLaXpwYXNVVDFxcEZveFFoSUsxVkdNQUpqSlJ1QVJ5aGpnalo2alNBZXpWS1F5OHRXNUFraUUzTlU1NA?oc=5
- https://news.google.com/rss/articles/CBMixwFBVV95cUxNdVlzQ3pfeDlpYVJ0TjRSX3padDdtb2NvaWNmOW9HQ0dQQzRubEdVU2E4ZTRhWE9WVGFpYjFweXdpUFd5UV9xNFZvZGdqcDE2Sm5aNGt4cXlTMllQYVBtSXRlQmJneG5JdTJXa0xDX3EtdVhRZTFMN2tFNzNEV19NbXA5REoya1I2Z3o2ZWgtVXBFQ3I3MU9ld0gwV2k1N2pTNy1ITDM4cnp3TEdpME1qbWxVQjdUc0ZKRFl4WlRxNjdzSm9PYlFZ?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxOWWVJZlJtQjJkZTMyWV9zMXNqV3RxZERPOE1CZlliQTVqR3VaTFk5anp5bHViM0pVTlVlc3lmMTU2YzVkb01hRXVsYU9yWUVFWjJxVHlrbW5TRVZoMWw3SzM1VUZ3UmpZN1NRODBhZmpHQXI4OXFCZDI5dWpMOGlTcGlWblREUUhmWHRCLWtZeW9zcnNUMVlRa2JTN0pwZ2dkSXBKQS14emotVmM1LWMtb2RxMEF5Y3RqNHBFZndn?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxPeFFUWkhxYlJNc3labzFqU1hldXAwd3A4VHB0Wl9heUZ4d21vQnc0bWVoSVBwNlZiOERENjBTekYwODFoSk5uRGozUjdRQjdCd0JZLXpLSGplbjIxX1psNXBUY2NPeGZWM2FqemJBdU9LcHE0TTQyS1Q5TkY4OTZuUHUyVHdNRGlqRXZ2V3pvR2ZHaDR0d3pmR3Z5cS05eDFJVDBYcnVn?oc=5
- https://news.google.com/rss/articles/CBMijgFBVV95cUxOcGprcWFSbjJXN3c1TVdDM2xoZVhnRnVfRURPb0JsM0k4UzdjelprbGllNUp6akd3OFF0a0RQY3V3SDdBZksxWmtodTdpbzQzeWF3TTdfZ1VfOWV6cEFxZUNaa2ZaakVhZEp5V2Y2VUZQX09nOHpvVEhaTHdwWUgwNEpXZWgyWURSYjRIMjJR?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
