# BRK-B Intelligence Report

- ticker: **BRK-B**
- Report as_of: **2026-11-04**
- Market data as_of: **2026-11-04**
- Quant sources: https://finance.yahoo.com/quote/BRK-B/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/BRK-B/key-statistics/
- AI analysis snapshot as_of: **2026-11-04**
- Snapshot note: report rendering uses saved source snapshots with separate observation dates. The daily price bar may be provisional before the listing market closes. Check source dates and availability.
- Market data fetched_at (UTC): **2026-11-05T05:00:07.962267+00:00**
- AI status: **Available**
- AI model (configured): **openai/gpt-oss-20b** (RSS headlines; rule and AI item counts: {'unique_headlines': 24, 'rule': 4, 'ai': 14, 'unknown': 0, 'irrelevant': 6})
- AI model(s) actually used: **openai/gpt-oss-20b**
- Verified recent classification reuse: **9** exact headline/source/date matches; prior report **20261104T044411Z-6b13f9ec/BRK-B** (reused decisions are not new model calls).
- News classification review flags (heuristic, not confirmed errors): **1**; {'directional_claim_without_event_type': 1}
- RSS source audit (metadata only, not article fact-checking): 24 unique headlines; 11 named publishers; 1 exact duplicates; 24 HTTPS source links; largest publisher share 50.0%; oldest publication 2026-10-29

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 579.0900 |
| Return 1D (%) | 3.9528 |
| Return 1W (%) | 7.1714 |
| Return 1M (%) | 15.2074 |
| Return YTD (%) | 15.2074 |
| Return 1Y (%) | 18.7487 |
| Annualized volatility (%) | 15.1203 |
| Beta vs SPY | 0.0112 |
| Max drawdown (%) | -9.4218 |
| Sharpe (rf=0) | 1.2167 |
| Downside deviation (rf=0, %) | 10.0127 |
| Sortino (rf=0) | 1.8374 |
| Historical VaR 95% (1D, %) | 1.4122 |
| Historical ES 95% (1D, %) | 2.0016 |
| Correlation vs SPY | 0.0095 |
| Tracking error vs SPY (%) | 19.7425 |
| P/E (trailing) | 14.01 |
| P/B | 0.00 |
| EV/EBITDA | -1.79 |
| Revenue growth (%) | 10.00 |
| Forward P/E (estimate) | 25.82 |
| Gross margin (%) | 30.33 |
| Operating margin (%) | 32.56 |
| Return on equity (%) | 12.12 |
| Free cash flow yield (%) | 5.81 |
| MA50 | 518.8682 |
| Close vs MA50 (%) | 11.6064 |
| MA200 | 496.8484 |
| Close vs MA200 (%) | 16.5526 |
| RSI (14, Wilder) | 82.7009 |
| MACD (12,26) | 12.7939 |
| MACD signal (9) | 9.9844 |
| MACD histogram | 2.8095 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'BRK-B': 275, 'SPY': 275}.
Fundamental context (yfinance company info snapshot): forward P/E is an estimate; gross/operating margins and return on equity are provider-reported fractional ratios converted to percentages. Free cash flow yield is computed only when financial and listing currencies are explicitly equal. Vendor fundamentals can be stale and may use different fiscal periods.
Additional risk measures use a trailing calendar year of observed daily adjusted closes: downside deviation and Sortino use a zero target and sqrt(252) scaling (minimum 20 daily returns); historical one-day 95% VaR/ES use the empirical 5th percentile and tail average (minimum 100 daily returns); correlation and tracking error align asset/SPY return end dates (minimum 20 pairs). Values are historical, not forecasts. SPY comparisons are in each listing's native currency, without FX conversion.

## HOW TO READ THE QUANTITATIVE SECTION

These rule-based bands are judgment choices for this research report, not investment advice.

- **Close**: The latest adjusted closing price is measured in the quoted currency. This value: 579.0900 -> Price level only; it does not by itself indicate valuation.
- **Return 1D (%)**: The adjusted closing price change over one trading day is measured as a percentage. This value: 3.9528 -> Adjusted price rose over this period.
- **Return 1W (%)**: The adjusted closing price change over one week is measured as a percentage. This value: 7.1714 -> Adjusted price rose over this period.
- **Return 1M (%)**: The adjusted closing price change over one month is measured as a percentage. This value: 15.2074 -> Adjusted price rose over this period.
- **Return YTD (%)**: The adjusted closing price change over the year to date is measured as a percentage. This value: 15.2074 -> Adjusted price rose over this period.
- **Return 1Y (%)**: The adjusted closing price change over one year is measured as a percentage. This value: 18.7487 -> Adjusted price rose over this period.
- **Annualized volatility (%)**: The variability of daily returns is scaled to one year as a percentage. This value: 15.1203 -> Low annualized volatility.
- **Downside deviation (rf=0, %)**: Root-mean-square downside daily return below zero, annualized with 252 trading days; historical, not predictive. This value: 10.0127 -> No interpretation rule is available for this metric.
- **Sortino (rf=0)**: Mean daily return divided by zero-target downside deviation, scaled by sqrt(252); undefined when downside deviation is zero. This value: 1.8374 -> No interpretation rule is available for this metric.
- **Historical VaR 95% (1D, %)**: Observed daily loss at the empirical fifth-percentile return, floored at zero; not a maximum loss. This value: 1.4122 -> No interpretation rule is available for this metric.
- **Historical ES 95% (1D, %)**: Average observed loss in returns at or below the empirical fifth percentile, floored at zero. This value: 2.0016 -> No interpretation rule is available for this metric.
- **Correlation vs SPY**: Pearson correlation of date-aligned daily asset/SPY returns in the sample; native-currency returns are not converted. This value: 0.0095 -> No interpretation rule is available for this metric.
- **Tracking error vs SPY (%)**: Annualized sample standard deviation of date-aligned daily asset-minus-SPY returns, in percentage points. This value: 19.7425 -> No interpretation rule is available for this metric.
- **Beta vs SPY**: Beta estimates how sensitively returns move with the SPY market benchmark. This value: 0.0112 -> Low market sensitivity.
- **Max drawdown (%)**: The largest peak-to-trough price decline in the sampled history is measured as a percentage. This value: -9.4218 -> Shallow peak-to-trough loss magnitude.
- **Sharpe (rf=0)**: Sharpe measures annualized return per unit of volatility using a zero risk-free rate. This value: 1.2167 -> Strong risk-adjusted return.
- **Forward P/E (estimate)**: Vendor estimate of price relative to expected future earnings; estimates can change. This value: 25.8160 -> No interpretation rule is available for this metric.
- **Gross margin (%)**: Gross profit divided by revenue, using the vendor-provided ratio; periods may differ. This value: 30.3320 -> No interpretation rule is available for this metric.
- **Operating margin (%)**: Operating income divided by revenue, using the vendor-provided ratio. This value: 32.5610 -> No interpretation rule is available for this metric.
- **Return on equity (%)**: Vendor-reported profit relative to shareholder equity; leverage can affect the ratio. This value: 12.1200 -> Adjusted price rose over this period.
- **Free cash flow yield (%)**: Free cash flow divided by market capitalization, only when both reported currencies match. This value: 5.8060 -> No interpretation rule is available for this metric.
- **P/E (trailing)**: The share price is divided by trailing earnings per share. This value: 14.0114 -> Low trailing earnings multiple under the research bands.
- **RSI (14, Wilder)**: The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale. This value: 82.7009 -> Overbought momentum reading.
- **MACD histogram**: The difference between MACD and its signal line measures their momentum gap in price units. This value: 2.8095 -> Positive momentum relative to the MACD signal line.
- **Close vs MA50 (%)**: The closing price distance from its 50-day moving average is measured as a percentage. This value: 11.6064 -> Clearly above the moving-average trend level.
- **Close vs MA200 (%)**: The closing price distance from its 200-day moving average is measured as a percentage. This value: 16.5526 -> Clearly above the moving-average trend level.

## TAILWINDS

### Berkshire Hathaway Shares Are Up 11% This Year. Is the Stock a Buy Ahead of Earnings?
- Summary: Berkshire Hathaway Shares Are Up 11% This Year. Is the Stock a Buy Ahead of Earnings?
- Date: 2026-11-03 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMirAFBVV95cUxQRm5DaTN3NmRadmh5LVczYXBueVBlUnhtaDZrQ2FGRGtmS0J1WnRkOWcwQ1FmT1pLN0dwQUV2ajRWZENUTGRFRmRBMEpJdjBMbUVmcnB0ZGxRWTNDRWV6RlItbjBfWndhNWVhVVZuWkxWdUY5RnZmU3h5dVlfaXItdEs4NDN5RVdnTFF6RnNBWXZMTExSRUoyS3B6UTNiSE9qbWx2X3VHNVZYRENl?oc=5>

### Berkshire Hathaway Inc (BRK.B) Shares Surge 4.0% -- What GF Scor
- Summary: Berkshire Hathaway Inc (BRK.B) Shares Surge 4.0% -- What GF Scor
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxOc0w4a19pY1htemludV9nRkY5RnVOcmNxRUoxQzdOakxSUnpYYzFNQU42M29VUjh5ODk3MTZueVpEMUtuZEs4Y3pySnM4TXFUeWxqTzgtQzYxMnFwRmh3S3dKYTlHblJ2em5FNkVlTkZ4TEYyOUI3SGRLenZod3hpSGM3b3d4NW9jZjZnTWctUjZrWjQ4N0dzOVlLeHBuV1pOSlhPTlNWREI3cmUxMzZaM0cta1g4d25kVHc?oc=5>

### History Says Berkshire Hathaway Stock Rewards Patience: It Rose in 50 of the Last 61 Years
- Summary: Long‑term performance data confirms Berkshire’s consistent growth over six decades.
- Date: 2026-11-02 | Impact: medium | Horizon: long | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxPWEpBZDRaVGZiU1gyRXdOQ0IwYkFINklhcXpIT1RNVmNHWnFWY2VWNkNFc0N4NDZrSTdmQTREQVFReTJlaV84VUlDOFFIY25hLW1yaGFtamJnQTQyVkxoUkp4ZlN0aGExeTdKLTZNOXNqUUdOTnctQ0dTZldSaFNiY281RTlUY05HRTQtUjBnU0ZKVmpzRzA0M181N3I4VDJHLUY2bA?oc=5>

### Berkshire Hathaway (BRK.B) Gains Momentum As Valuation Still Looks In Focus
- Summary: Berkshire’s valuation remains attractive, driving momentum in its stock.
- Date: 2026-10-29 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxNS3EtUEZPZUlYeU9nbjVBS2NfYmlVVTlnOWtCWXhEcjF1cjVOMlZyU1RmOXNHNE15cE5BVVMxNjBDNHduMHF3eEtmZEpvbjJENkUtSjk4aVJmT3RYR0ZmQllZUE5iNXpPejkxdVUzNVlCRlQyNFRlVFh3Mk9LYUR0RDRCX1lSbXhFcDk4Z3dQY3hteFdXMDVlQXo1aw?oc=5>

### Greg Abel Just Plowed Another $27 Million Into One of Berkshire Hathaway's Top 20 Holdings That's Up 62% This Year and Has a 3.3% Dividend Yield
- Summary: Berkshire invested $27M in a top holding, boosting its portfolio and dividend yield.
- Date: 2026-11-04 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxOU2tOd3N5X3FjMmlCY21JSTVGc2tvcUZYVkFDaFFRUGFtV1YwTU1NQVdjQXNzajBid2p1Q3dhNTBHT044WUozUWdxSGlLZE1BZ3o0bGNocVlOTll1REprREZzUXU2NjQwcEhtZ1pjaUZ3QnhKb0pJcmU4bnVYN0hpMDBMdjVWZ1kxSlBfX1lhR3VBeV9jUloyM05B?oc=5>

### Berkshire Hathaway Inc Stock (BRKb) Moved Up by 3.29% on Nov 4: Key Drivers Unveiled
- Summary: Berkshire Hathaway’s stock rose 3.29% on Nov 4, driven by key market factors.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.95
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxNc25UQUFicDNuQlhrOENfcjlPa0U0dlFOanFxWS11by1FYWhfMExVUG9tblZMczhOVlprdnllOG11YXN5a0N3ZjBGa2V2Zm5xUW56Rk1NaVZBSDRiMXRONzN5NlRYZHN5SEFjWEVVQ2lxWTFhUmRjTndrdVpOb2JxV1J1RktBRDZzcW53?oc=5>

### Coca-Cola Pays Warren Buffett’s Berkshire $848 Million a Year as Jim Cramer Says Buy KO Stock
- Summary: Coca-Cola’s annual $848M payment to Berkshire is a significant dividend income source.
- Date: 2026-11-04 | Impact: medium | Horizon: long | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxPVk1GSW5iNFZuTDhuQW1OR1o1Sk83b1ZtWUVvNmdaaFBqa3A1dzBLTTJPOEhJNFo2dk9yLU9fUGRJcmhHTVJ1QkxUVkl5SGlOcDNkaVI1Sm1abXlRbnBFcTNvTjNOTHQtSlEyS1ZIcFVienR4WGczVE9uSUNqc1JtU1h4d0JwRF9DVU5JUWVJTWNyZU51RU1acnl3?oc=5>

### Here's How Warren Buffett's Berkshire Hathaway Stock Did in Every S&P 500 Down Year Since 2000
- Summary: Historical performance shows Berkshire’s resilience during S&P 500 downturns.
- Date: 2026-11-02 | Impact: low | Horizon: long | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi2AFBVV95cUxQd0x4OEg0ZlFpTFNaQkllVGZ0bVNlRnkyYm5uUGZBNHB6NkpOblBoOFJXMFNCMmNPbFd1OVQ3dzFjc1kyNXl3azNkUWllazVGVnZZWlVWM01mTUZDTU4yd0M4SFo0TW9NYjZxS3RMX2djRTJQUG96V0p0V1RQdTRyYmZxN1FveGppRm1OUUNtclhJT3U3TDZ2MjFDUTh2NGVpWjI3LXExT3IwNG9BMHdMZjFCMy1JMW5teURDMXdETGRENFlWc29vZWYtX1NEYW9ReVFQYnIxdnk?oc=5>

### Berkshire Hathaway Inc Stock (BRKa) Moved Up by 3.17% on Nov 4: Facts Behind the Movement
- Summary: Shares of Berkshire Hathaway rose 3.17% on Nov 4, reflecting positive market sentiment and potential investor confidence.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiwFBVV95cUxPaVVMTm9fT1JpVVZzSW9xcVdiX01USUthUFZqNTJ6dEx1Q2JzaF8zOHFZWlFZQlRlY3RTRkVPTXB3X0JScGYzVjNtVHRQZk5TYW5TZ1lxZ3VGdnNMQWltVDBERFlpd1otZk1jd2VOZ0liY1FmUnh6U0YxYVFJWUxfUXV0T1NqRFNnR1BV?oc=5>

## HEADWINDS

### Berkshire Hathaway’s Alphabet Loss Exposes Weak Stock-Picking Record
- Summary: Loss on Alphabet highlights poor stock selection, affecting returns.
- Date: 2026-11-02 | Impact: high | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxQdzg5Z0JmTGJKTXNlaWROTlRkLW5FYkxFN1pNT0dBcE85d1Y5akRqOFBfeWc5MU4xcFAxOU9oWnFIYm40ejNnRkNxUkJsbnVxR2RYb0ZUdzFGZmFNTDB6TDYwOURHbmxZaTJGeU41VXBtWG0yTExhYU1JTlJvQzVORU5KU0lNdzYwQmdsaDVBMGNWMkdNY0dMNTktMA?oc=5>

### 1 of Greg Abel's Favorite Stocks and a Top 5 Berkshire Hathaway Holding Just Suffered a Devastating Decline
- Summary: A Berkshire holding dropped sharply, impacting portfolio performance.
- Date: 2026-11-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxPTGI0X1ZyaHhPM3BJeFBlRmtFZzBuTm9sbXRLdy1aU1BvQXFUOFZCVG1KWTRoNy1pR1N3dV8waExaeEdNRFVWZ3ZPZHRGdUdrQ1FxbWFGNnF1VzlJVlQtVjRidncwYjB3emk2c3FkR2VYM2tSLW5kWXNlcURwMHViZF93MV9GRDNJOGhMTV9OU0lxT3IwcUZueg?oc=5>

## CATALYSTS

### Berkshire Hathaway Earnings Put BRKU in the Limelight
- Summary: Berkshire Hathaway Earnings Put BRKU in the Limelight
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiiAFBVV95cUxPOVRqbHA4czI5ZUF1Z0x4enZnbG8zeVNOWG05Z3NRTF9laERKY1BPWUU4WXA5YjFmY2lrQjlROVRtbkpNU2ZjamlVUTM5UDBINEx6LXlRR2hHUEJjc0VxYkRwVzFzZ1BPVXJrMC1FYzN3ZVpEOWRjUUhGZDVoUTlFZzdYTGJCaUxD?oc=5>

### Berkshire Hathaway Inc. Information Regarding Third Quarter Earnings Release
- Summary: Berkshire Hathaway Inc. Information Regarding Third Quarter Earnings Release
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiugFBVV95cUxQSGVMbmpySUUyTklwZDduTmhYampZU2JnR2U1R05RY1IzMUxmUV9uUUZnTEVBemxxQXUxcXZ6d2ZOV2hNSmpuV0xMSXlRNjk4ZXZ4N1ZFaHlpdUFKaWdGZGxIemFSbFNxVC1NLUhDX0JVTEJjUzdkRURzaEIzbHJIWFVIRFF6UnlDRDZqaHNmMEpNRVk4aEFXaTNuWFJUSmtLSFVQNHBmdnZ4emFnUVRXbjUtM0Q4RzlRcVE?oc=5>

### Learn Why The Bull Case For Berkshire Hathaway (BRK.A) Could Change Following Tech Stake Increase
- Summary: Stake increase may alter Berkshire’s valuation outlook.
- Date: 2026-10-31 | Impact: medium | Horizon: short | Confidence: 0.7
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxPbGJfQ2ljcFBDUl81N0lUbjlOTE1nSmhsS1dNQnBZOWt0OXlHZ2J5SGNZQW15bDVSYmU1cjQ2b2dqUTlTdk15QjJ3SWlJV2EwU19xSVZ4OW9YOWJTMzRjaldoci1CUzUtcXdoUHROUUl5bnk4VGpXRHNLNHY0TGgwTlZsenhtcEx3djJQaHpaSGR2UFBTZnhjLVl3?oc=5>

### Warren Buffett's 3 Longest-Held Stocks Average a 3,757% Gain and Collectively Deliver $1.53 Billion in Annual Dividend Income for Berkshire Hathaway
- Summary: Three long-held stocks generate $1.53B in dividends for Berkshire.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMi5gFBVV95cUxOTjVjOWhwZDZXRVRtTjVrcms1YWdnX0IwQnJIbFRFMkRrMWhZR1h3Z1BlQU1HQUZVNmZYelBqZkFYVWFRdEpVNUEyN2Q0OVFoLUVNLTZVb3d3a0lZcUg2YWJFRkNEN21HdjRIdnpvMWduWXhpa0QtN2QtYnZ2bFBrR01qN0FBNWZxdmNKaE1MNHRMQU01M1ZrOTlaOHFNTFZYSDBWWHJVQ2tZamZRNFpoYmRxTG9pVktfTzBvTHNmUmRwZW9adEtGa2pWa0V2MS1vRGJVaEZRQ3dyN0xWblk1LTNEbU9MZw?oc=5>

### Berkshire Hathaway Is Buying More Sirius XM. Here’s What It May See
- Summary: Berkshire Hathaway is increasing its stake in Sirius XM, potentially expanding its media portfolio.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMipAFBVV95cUxNNmFRR3dWNThYNkVNZUl0SnhGS3JaQ3J3Q2hsN2pseHlNRDJVWTV1dEs1MHRBQUtVNDNJZjg1aHNJTDNfcFhQX2dUcTc1VF9kTFJwbzBWdm1Sd0p0WnRTbTFpZDBEV2dseEhxdVJsZjJyTFBnNHZFN3JGc2U3dVJDTkdkMVBtamNKWENuQmhUdm9UUVB0cDFkQkNnQ0JmMzdmUVRjaA?oc=5>

### 2 Berkshire Hathaway Holdings to Buy After Record Third Quarters
- Summary: Berkshire Hathaway plans to acquire two holdings following record third-quarter performance.
- Date: 2026-11-04 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMinwFBVV95cUxQUzc5U0lRWFB3UWhTdEEzazg2SU5tekdwVTNXWTY1M3MyM0lWbXhiUFpBVUF2MUtBcEFVblN6a3pENzcybFJyNGhWcnZXTU91aHhtZS04QklkelJjZ09qS01RQjFhNUQxQmZNWVI2UUUwei13VzVkM3RGX0ZRUVhEelZBTDg0QkNyamJMVkd2WEM2TUU0dkZfeE1Fd05xeGc?oc=5>

## RISKS

### Analysts Estimate Berkshire Hathaway B (BRK.B) to Report a Decline in Earnings: What to Look Out for
- Summary: Forecasts predict a drop in Berkshire’s earnings, potentially affecting investor sentiment.
- Date: 2026-10-30 | Impact: medium | Horizon: short | Confidence: 0.85
- Sources: <https://news.google.com/rss/articles/CBMipgFBVV95cUxNYXlWNjd6V2dkUmdRRHBUMjRSR09JclBRdm9fZGVLcE1iSnZET293bFBLVnJJdm9YNkxtZnJDSnVRVWxZRzhGazJvdnhHbFFtUk95dVJPNDN5YWs3RkRSN1R5MnRXb2lWa2JsNVFjbzJ4QlJ2N1BxelBXM1JSYTRYcjBma19pTktRZmlzR213alhsNXh2b3h4MDh2bXVRUjRMTGU4TTZn?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (listing currency) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **BRK-B** | **14.01** | **0.00** | **-1.79** | **10.00** | **1,239,663,640,576.00 USD** | **18.75** |
| MKL | 13.51 | 1.29 | 8.00 | -11.20 | 23,902,416,896.00 USD | -1.38 |
| FFH.TO | 9.78 | 1.56 | 7.94 | -0.50 | 61,624,901,632.00 CAD | 23.70 |
| L | 15.21 | 1.24 | 8.75 | 1.90 | 22,582,491,136.00 USD | 11.22 |

Peers fetched as_of: 2026-11-04; BRK-B reuses existing data (market data as_of: 2026-11-04); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-08-08
- Next expected earnings: 2026-11-07 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-11-04

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index (1982–1984=100) | CPIAUCSL | 336.30 | 2026-09-01 |
| Federal funds rate (%) | FEDFUNDS | 3.88 | 2026-10-01 |
| ISM Manufacturing PMI | NAPM | N/A | N/A |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-08-10
- Revenue (latest available single quarter): 101,808,000,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- Net income (latest available single quarter): 25,667,000,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/1067983/000119312526341032/brka-20260630.htm

SEC requests use the configured organization and contact identity; unavailable source data is shown as N/A. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMirAFBVV95cUxQRm5DaTN3NmRadmh5LVczYXBueVBlUnhtaDZrQ2FGRGtmS0J1WnRkOWcwQ1FmT1pLN0dwQUV2ajRWZENUTGRFRmRBMEpJdjBMbUVmcnB0ZGxRWTNDRWV6RlItbjBfWndhNWVhVVZuWkxWdUY5RnZmU3h5dVlfaXItdEs4NDN5RVdnTFF6RnNBWXZMTExSRUoyS3B6UTNiSE9qbWx2X3VHNVZYRENl?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxOc0w4a19pY1htemludV9nRkY5RnVOcmNxRUoxQzdOakxSUnpYYzFNQU42M29VUjh5ODk3MTZueVpEMUtuZEs4Y3pySnM4TXFUeWxqTzgtQzYxMnFwRmh3S3dKYTlHblJ2em5FNkVlTkZ4TEYyOUI3SGRLenZod3hpSGM3b3d4NW9jZjZnTWctUjZrWjQ4N0dzOVlLeHBuV1pOSlhPTlNWREI3cmUxMzZaM0cta1g4d25kVHc?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxPWEpBZDRaVGZiU1gyRXdOQ0IwYkFINklhcXpIT1RNVmNHWnFWY2VWNkNFc0N4NDZrSTdmQTREQVFReTJlaV84VUlDOFFIY25hLW1yaGFtamJnQTQyVkxoUkp4ZlN0aGExeTdKLTZNOXNqUUdOTnctQ0dTZldSaFNiY281RTlUY05HRTQtUjBnU0ZKVmpzRzA0M181N3I4VDJHLUY2bA?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxNS3EtUEZPZUlYeU9nbjVBS2NfYmlVVTlnOWtCWXhEcjF1cjVOMlZyU1RmOXNHNE15cE5BVVMxNjBDNHduMHF3eEtmZEpvbjJENkUtSjk4aVJmT3RYR0ZmQllZUE5iNXpPejkxdVUzNVlCRlQyNFRlVFh3Mk9LYUR0RDRCX1lSbXhFcDk4Z3dQY3hteFdXMDVlQXo1aw?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxOU2tOd3N5X3FjMmlCY21JSTVGc2tvcUZYVkFDaFFRUGFtV1YwTU1NQVdjQXNzajBid2p1Q3dhNTBHT044WUozUWdxSGlLZE1BZ3o0bGNocVlOTll1REprREZzUXU2NjQwcEhtZ1pjaUZ3QnhKb0pJcmU4bnVYN0hpMDBMdjVWZ1kxSlBfX1lhR3VBeV9jUloyM05B?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxNc25UQUFicDNuQlhrOENfcjlPa0U0dlFOanFxWS11by1FYWhfMExVUG9tblZMczhOVlprdnllOG11YXN5a0N3ZjBGa2V2Zm5xUW56Rk1NaVZBSDRiMXRONzN5NlRYZHN5SEFjWEVVQ2lxWTFhUmRjTndrdVpOb2JxV1J1RktBRDZzcW53?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxPVk1GSW5iNFZuTDhuQW1OR1o1Sk83b1ZtWUVvNmdaaFBqa3A1dzBLTTJPOEhJNFo2dk9yLU9fUGRJcmhHTVJ1QkxUVkl5SGlOcDNkaVI1Sm1abXlRbnBFcTNvTjNOTHQtSlEyS1ZIcFVienR4WGczVE9uSUNqc1JtU1h4d0JwRF9DVU5JUWVJTWNyZU51RU1acnl3?oc=5
- https://news.google.com/rss/articles/CBMi2AFBVV95cUxQd0x4OEg0ZlFpTFNaQkllVGZ0bVNlRnkyYm5uUGZBNHB6NkpOblBoOFJXMFNCMmNPbFd1OVQ3dzFjc1kyNXl3azNkUWllazVGVnZZWlVWM01mTUZDTU4yd0M4SFo0TW9NYjZxS3RMX2djRTJQUG96V0p0V1RQdTRyYmZxN1FveGppRm1OUUNtclhJT3U3TDZ2MjFDUTh2NGVpWjI3LXExT3IwNG9BMHdMZjFCMy1JMW5teURDMXdETGRENFlWc29vZWYtX1NEYW9ReVFQYnIxdnk?oc=5
- https://news.google.com/rss/articles/CBMiiwFBVV95cUxPaVVMTm9fT1JpVVZzSW9xcVdiX01USUthUFZqNTJ6dEx1Q2JzaF8zOHFZWlFZQlRlY3RTRkVPTXB3X0JScGYzVjNtVHRQZk5TYW5TZ1lxZ3VGdnNMQWltVDBERFlpd1otZk1jd2VOZ0liY1FmUnh6U0YxYVFJWUxfUXV0T1NqRFNnR1BV?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxQdzg5Z0JmTGJKTXNlaWROTlRkLW5FYkxFN1pNT0dBcE85d1Y5akRqOFBfeWc5MU4xcFAxOU9oWnFIYm40ejNnRkNxUkJsbnVxR2RYb0ZUdzFGZmFNTDB6TDYwOURHbmxZaTJGeU41VXBtWG0yTExhYU1JTlJvQzVORU5KU0lNdzYwQmdsaDVBMGNWMkdNY0dMNTktMA?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxPTGI0X1ZyaHhPM3BJeFBlRmtFZzBuTm9sbXRLdy1aU1BvQXFUOFZCVG1KWTRoNy1pR1N3dV8waExaeEdNRFVWZ3ZPZHRGdUdrQ1FxbWFGNnF1VzlJVlQtVjRidncwYjB3emk2c3FkR2VYM2tSLW5kWXNlcURwMHViZF93MV9GRDNJOGhMTV9OU0lxT3IwcUZueg?oc=5
- https://news.google.com/rss/articles/CBMiiAFBVV95cUxPOVRqbHA4czI5ZUF1Z0x4enZnbG8zeVNOWG05Z3NRTF9laERKY1BPWUU4WXA5YjFmY2lrQjlROVRtbkpNU2ZjamlVUTM5UDBINEx6LXlRR2hHUEJjc0VxYkRwVzFzZ1BPVXJrMC1FYzN3ZVpEOWRjUUhGZDVoUTlFZzdYTGJCaUxD?oc=5
- https://news.google.com/rss/articles/CBMiugFBVV95cUxQSGVMbmpySUUyTklwZDduTmhYampZU2JnR2U1R05RY1IzMUxmUV9uUUZnTEVBemxxQXUxcXZ6d2ZOV2hNSmpuV0xMSXlRNjk4ZXZ4N1ZFaHlpdUFKaWdGZGxIemFSbFNxVC1NLUhDX0JVTEJjUzdkRURzaEIzbHJIWFVIRFF6UnlDRDZqaHNmMEpNRVk4aEFXaTNuWFJUSmtLSFVQNHBmdnZ4emFnUVRXbjUtM0Q4RzlRcVE?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxPbGJfQ2ljcFBDUl81N0lUbjlOTE1nSmhsS1dNQnBZOWt0OXlHZ2J5SGNZQW15bDVSYmU1cjQ2b2dqUTlTdk15QjJ3SWlJV2EwU19xSVZ4OW9YOWJTMzRjaldoci1CUzUtcXdoUHROUUl5bnk4VGpXRHNLNHY0TGgwTlZsenhtcEx3djJQaHpaSGR2UFBTZnhjLVl3?oc=5
- https://news.google.com/rss/articles/CBMi5gFBVV95cUxOTjVjOWhwZDZXRVRtTjVrcms1YWdnX0IwQnJIbFRFMkRrMWhZR1h3Z1BlQU1HQUZVNmZYelBqZkFYVWFRdEpVNUEyN2Q0OVFoLUVNLTZVb3d3a0lZcUg2YWJFRkNEN21HdjRIdnpvMWduWXhpa0QtN2QtYnZ2bFBrR01qN0FBNWZxdmNKaE1MNHRMQU01M1ZrOTlaOHFNTFZYSDBWWHJVQ2tZamZRNFpoYmRxTG9pVktfTzBvTHNmUmRwZW9adEtGa2pWa0V2MS1vRGJVaEZRQ3dyN0xWblk1LTNEbU9MZw?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxNNmFRR3dWNThYNkVNZUl0SnhGS3JaQ3J3Q2hsN2pseHlNRDJVWTV1dEs1MHRBQUtVNDNJZjg1aHNJTDNfcFhQX2dUcTc1VF9kTFJwbzBWdm1Sd0p0WnRTbTFpZDBEV2dseEhxdVJsZjJyTFBnNHZFN3JGc2U3dVJDTkdkMVBtamNKWENuQmhUdm9UUVB0cDFkQkNnQ0JmMzdmUVRjaA?oc=5
- https://news.google.com/rss/articles/CBMinwFBVV95cUxQUzc5U0lRWFB3UWhTdEEzazg2SU5tekdwVTNXWTY1M3MyM0lWbXhiUFpBVUF2MUtBcEFVblN6a3pENzcybFJyNGhWcnZXTU91aHhtZS04QklkelJjZ09qS01RQjFhNUQxQmZNWVI2UUUwei13VzVkM3RGX0ZRUVhEelZBTDg0QkNyamJMVkd2WEM2TUU0dkZfeE1Fd05xeGc?oc=5
- https://news.google.com/rss/articles/CBMipgFBVV95cUxNYXlWNjd6V2dkUmdRRHBUMjRSR09JclBRdm9fZGVLcE1iSnZET293bFBLVnJJdm9YNkxtZnJDSnVRVWxZRzhGazJvdnhHbFFtUk95dVJPNDN5YWs3RkRSN1R5MnRXb2lWa2JsNVFjbzJ4QlJ2N1BxelBXM1JSYTRYcjBma19pTktRZmlzR213alhsNXh2b3h4MDh2bXVRUjRMTGU4TTZn?oc=5

## Research notes and limitations

- Daily multi-source research; AI items require human spot checks; RSS coverage is not guaranteed.
- News classifications use source headlines, with rule-based extraction and the configured AI provider when its daily budget is available.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
