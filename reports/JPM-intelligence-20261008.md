# JPM Intelligence Demo

- ticker: **JPM**
- Report as_of: **2026-10-08**
- Market data as_of: **2026-10-07**
- Quant sources: https://finance.yahoo.com/quote/JPM/history/, https://finance.yahoo.com/quote/SPY/history/, https://finance.yahoo.com/quote/JPM/key-statistics/
- AI analysis snapshot as_of: **2026-10-03** (retained; this run refreshes market data only)
- Snapshot note: the report-date daily bar may be intraday until the US market closes; its Close field is provisional. News, peers, earnings, EDGAR and macro sections reuse their existing snapshots.
- Market data fetched_at (UTC): **2026-10-08T04:10:57.399472+00:00**
- AI status: **Available**
- AI model: **gemini-3.5-flash-lite** (25 Google News RSS headlines -> AI extraction and classification; free-tier grounding unavailable, using RSS + AI)

## QUANTITATIVE

| Metric | Value |
|---|---:|
| Close | 329.5800 |
| Return 1D (%) | -0.5132 |
| Return 1W (%) | 0.1192 |
| Return 1M (%) | -7.6444 |
| Return YTD (%) | 4.2541 |
| Return 1Y (%) | 9.1773 |
| Annualized volatility (%) | 22.4891 |
| Beta vs SPY | 0.7911 |
| Max drawdown (%) | -15.4717 |
| Sharpe (rf=0) | 0.5044 |
| P/E (trailing) | 14.19 |
| P/B | 2.48 |
| EV/EBITDA | N/A |
| Revenue growth (%) | 30.40 |
| MA50 | 349.0915 |
| Close vs MA50 (%) | -5.5892 |
| MA200 | 318.8990 |
| Close vs MA200 (%) | 3.3493 |
| RSI (14, Wilder) | 33.8112 |
| MACD (12,26) | -5.7058 |
| MACD signal (9) | -4.7812 |
| MACD histogram | -0.9247 |

Methodology: adjusted daily closes (yfinance auto_adjust=True; Stooq fallback if unavailable). 1Y return uses the last trading day on or before the one-year boundary.
Market data sample: {'JPM': 255, 'SPY': 255}.

## TAILWINDS

### JPMorgan Chase (JPM) Stock Gets Fair Value Boost After Analysts Raise Targets
- Summary: JPMorgan Chase (JPM) Stock Gets Fair Value Boost After Analysts Raise Targets
- Date: 2026-08-12 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxQQUJCVENvbkFBUC1kUU5FWUNqbWU4b2F1SmdGeDZIMk5fMWZIZFVkb25aRUJQU3ozbndQMHNwZHNVYUdhRVdraXNtOE1Md0tKOTVmbjhocEJPdDBZQUhnQzdlLTdQZnB1U2I4dElSRUdWLTM2RkVlelFuUDRkdkxQM2RuV3U5OXRHSkE0VEFCYXpOZ3pzTWlXck1B?oc=5>

### JPMorgan Chase (JPM) Stock Is Up, What You Need To Know
- Summary: JPMorgan Chase (JPM) Stock Is Up, What You Need To Know
- Date: 2026-07-14 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxNUnAzZ0gwc19BdUV1aVdrS056bi14RktZREF5aWRrbFFSaXN1aFJVTUh4dlBwR3QxbG9rV3g4ejhYQ0hqZkw4TXBoLUlYZ2ZSeWJ2RnIwSDBWTm83d1h0TE1GbE42Rnpva0lXLVIxMHhEaFViVnB6RmpZb2dPUFJER1BEUEtueDI2VWZPODAxZ2lLdDRBekgzdXB3?oc=5>

### JPMorgan Chase (JPM) Stock Could Be Undervalued Based On Capital Returns
- Summary: JPMorgan Chase stock could be undervalued based on capital returns.
- Date: 2026-09-25 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxPZ19TVk1KSE1WMmxZYVJZUEl3eS1XZkdNckN1QmRQUnYxQXN6OVBVY0gzcnI0Ny1hTHJqT2RKd1FqaHBFa3U3bjEtajlYRTZacFRZTmtTYVZVRVV2OExXbFRDVnYxZngtYmJvd1BFUndjWGhENHVGczlmOUh5QTFlY0hqR0dCVWY5XzBhQmgxS2VhWHRtY0VfTmZwZw?oc=5>

### JPMorgan Chase (JPM) Stock May Trade At A Discount Following Record Dealmaking News
- Summary: JPMorgan Chase stock may trade at a discount following record dealmaking news.
- Date: 2026-09-29 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixgFBVV95cUxOR2tmdmpTSnkwSG53QlpVTEhiUmhqZ1JNUUdiUGhYX2pXLTlCemdTcWllRk91QVBRSEdMdnUyRmhNZWxtV0Q2TlhoMnpxOU91OTAybktFUWJCNFFRMy1saFAtR1VadEpxS05vNF9hV1VHTVROeXdQbHMwT0RBV0JBZkJXU1lKTlZ2OWpFMlZrQnhUOTNfUXNCVUtkcS0ybXdZSS0wRk0xQ05LOXJwTmh5OGZOSjBRYXpzaVB6V2hsZjRtdUt5NVHSAcsBQVVfeXFMUEUzRk93MVNtdEc4V2E5MEoxdjhFc0NDV1FNbDBSOHMwRm9memFxdkcyc0RITGNveGx5a2VSSXNVRHNHZUp0OHBGbzNPazJJejVZUHBCTGdLaGRtbG1qbUJtT0JRQUhJQ3FjLXBlX0oxNUlXRHl2ZWVlSHRXUFBBQXY4U1ItNzZLV2lKc0Q1NUJIQ0NVa1VMemo3bkFOb1dwUld0TzI5ZXp4WklCZWtVa3RqWndXS1lhUWY4dnIzbk1MVGU2ekhBSnFHSFU?oc=5>

### JPMorgan Chase (JPM) Stock Gets Fair Value Bump As Analysts Rework Revenue Outlook
- Summary: JPMorgan Chase stock gets fair value bump as analysts rework revenue outlook.
- Date: 2026-07-02 | Impact: medium | Horizon: medium | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMimgFBVV95cUxQZS1hR2RnSWpLSmd6UTQwSnR5YUFSM250Ri1KWERKbTVqRW4wVUdVREVwZ0Q0SlBiVkNmcjRuazhBNmJJbTE3eEpvNkdXZ2I5V2w1VzZPNjBHUG4yQmpPX1J4YzZacEkwV252d1Z3RmJlSm11N2FoZjF3TnhrQWY4UFRhYnZiTEJOZEZxQWRsZlQzbEZVcjZCSHd3?oc=5>

### JPMorgan Chase (JPM) Could Be 3% Below Fair Value Following Chicago Expansion
- Summary: JPMorgan Chase could be 3% below fair value following its Chicago expansion.
- Date: 2026-08-18 | Impact: low | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMilgFBVV95cUxPQ1l2MlZSNThPX29mT3FXZTluMjcyUGJOUmp0YnNWNlVOSVQ1NVB2QkstdDZxU2xGWjhrZ3hhU09CSXNQUzF2ekNVZlJZQU5XWTIwUjFvSGdiMHBpZHdnNjhqc3RYcC1WMzVaRGxkTnJqNWNrQ3ZYUXI5bWt5RDViaE8tVHlBdWsxclF5OElSbi1rNVFfcEE?oc=5>

## HEADWINDS

### JPMorgan Chase & Co. (JPM) Stock Moves -3.34%: What You Should Know
- Summary: JPMorgan Chase stock moved -3.34%.
- Date: 2026-09-22 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxPbU1qLTdsRmJXSEtMdGNtdEoxeWdBb3JqZDFiLTZ4MmxsTTVLQXVPOGtoZ19UU29WY3VCOVptQ09hSzYxQkhBcmtVeGhyRnFBbG1MNU5keU44ZENjN3JMTlJVOEx3bG5sVG96aGtoN1pKOWRiLXVqY21aa0xMYThSb1BFYnJBaU1MT0tuMnQyRXBDWWJ0b3VN?oc=5>

### JPMorgan Chase & Co. (JPM) Stock Drops Despite Market Gains: Important Facts to Note
- Summary: JPMorgan Chase stock dropped despite market gains.
- Date: 2026-08-19 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMilwFBVV95cUxNNUo4S0xSblFyRTBOMDN4OURpQ1JNUTBFenpnVjNaMVMzMHhURDRQXzd6R2NFRzJjVktaTjRqUmNzLV8xaGNmMU92ejNSY0NjRWhVbUpFdG9tSlJxb0N6aHU3UzFnZWN3ZWtwUDJfQWVTM094N05mZ25mUDlkZEY2N3NEcnp4bnJfUnJkUWl2YkVTODlPRWtJ?oc=5>

### Why JPMorgan Chase Stock Tumbled Today
- Summary: JPMorgan Chase stock tumbled.
- Date: 2026-07-29 | Impact: medium | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxNcGoySGFlSURjVjlFdWxkYzg2akdUWm9qdThEMU00MDBNc09qSXI0Xy1jZ0NxZGlmdFVXMllEUmt5RWN0QUZUak82WjBaMlpXWllyc0wyaUlodkUtaDhNRWlFUjkzbEFhS1phTWNkRmJfbngzZFptb3NrMy1jeTJyRTZQMEJwU05BV1V1cXdlUGZuS3hsTXNKa3dLaWN6Zw?oc=5>

## CATALYSTS

### JPMorgan Chase & Co. $JPM Stock Bought by West Family Investments Inc.
- Summary: JPMorgan Chase & Co. $JPM Stock Bought by West Family Investments Inc.
- Date: 2026-10-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMixAFBVV95cUxQN2dZRFQ5NDRLYmJGQ0xMRHFod2g2SUdMVG1rLU1pV1ZjZlJ2eWFibEl1bW1TTVhnX0hsTF9ycWZBZkFIbENaLUNEUFRudEVQX2l6am1HNzNfOF82bzZjSlNyWEVQdTF3QkhhQjBtMS10eENQVXhSZjY3Vl9OTlJOR1l5Z3RjWGU4cFo2TkxqZkMyWjIwVGllTEdVMTVPS3R3RE43Z1F4azNMMmFvMWxSTnVxY2dEUVd4a1lORVVZaW16WUFD?oc=5>

### JPMorgan Chase & Co. $JPM Stock Bought by RFG Advisory LLC
- Summary: JPMorgan Chase & Co. $JPM Stock Bought by RFG Advisory LLC
- Date: 2026-10-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMitgFBVV95cUxNSndzVTBjdlhPcW9GTElvVTdYVktIcjVDUlZULVRXeThubjdMbHlzWFBtTjJvZU9EeXY0Vjk0U05ua2ZxbUh5cGlpUXd0cDY0MTVkQS00bnFMaTVXc0VDQUgzd2xWb3lvRm5PaWw3ZjRITC1xS09yYkxYdFdpb2pkUUdLNkpsdzBNTk82eXdWd0h1MnNmQnp6N211YnJzS2M1emh2R0JMQnNVZ1h4d1U5WTFtcWN0QQ?oc=5>

### JPMorgan Chase & Co. (NYSE:JPM) Stock Has Average Price Target of $363.29
- Summary: JPMorgan Chase & Co. (NYSE:JPM) Stock Has Average Price Target of $363.29
- Date: 2026-10-02 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMiygFBVV95cUxPeWI4T2lESUNrZTZtRzdiWmlRNjBKcFRTemhWbjdjUC1laTVYRDI1bWtzV0FGLWVPX0p1NjM1VUQzeUNjTjMzYXdmWmRIcmVaTU5jZFFmd2xZNmw0UGxYcWYyYXM2ZVNzOWE4c09zN3ZCbzdhUlNyMVZPYVlxUkV3NW0zMlhtaE96aUhrcnJJQ0lpeHpjOU5Bc19UU3NNdG10MjdORFVVZ1dpU3NKQi10VE9JWVhEMnNNNV9pa1AwUUhYVVAzWFMycG1B?oc=5>

### JPMorgan Chase (JPM) Stock Looks Undervalued Even As Earnings Look Fair
- Summary: JPMorgan Chase (JPM) Stock Looks Undervalued Even As Earnings Look Fair
- Date: 2026-07-29 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimwFBVV95cUxQekE0TUk1aFJUOUZhczFYdHJNOEVJb2ZuMHB6ZFBTZkppOU5vTVVncUFmYi1QNjBmTlFPRXBBX082OEpxOFc3dDNuQkxJdEhkYU1PWmxOVVV0WThNSEE3Y1pmS19kOG9aeXRwMDVIVHNmNzRLMHp4TUJNQ0E4TV84dDBTRm1VbDNRaUFPdDBKSl9SdGZTM3liWUg2bw?oc=5>

### JPMorgan Chase (JPM) Taps Bond Markets, Is The Stock Still Undervalued?
- Summary: JPMorgan Chase taps bond markets.
- Date: 2026-10-01 | Impact: medium | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMimAFBVV95cUxPY19fbTR5d0ZudE96RExhTTY1SXBPUXpPeDRlV0ZBTWxlV2RRYnZjWGdrMkF2QWNrNklOTExieFpVby1HMVc2RGloWWg0ZmxKQ05SR29oTTBHSVZ4ZElTd3l4TXprMG5yODM0dU5wWGQ1V0FuOHVLMDVjX29Ib2xzOWhXb3VkY2NlLWdfWEYyTUplQXRIOTJZWg?oc=5>

### JPMorgan Stock Sits 6% Below Its High After a Record Year. Here’s What Q3 Earnings Must Prove
- Summary: JPMorgan stock sits 6% below its high after a record year, detailing what Q3 earnings must prove.
- Date: 2026-09-28 | Impact: high | Horizon: short | Confidence: 0.9
- Sources: <https://news.google.com/rss/articles/CBMitwFBVV95cUxPT0MxSGV1cE9DaTIwdV9DYnBka0ZXWGhtMi1QWWFESjU3TmFBakhHamNQMkhzTXBfM01ldmZ6MEZxSWIzdzlMbmNCM2U4X1hrb2d2NUxZNEhHMmxSMXVZRy10djFJY0w0R2ZTazVKbVpRcHoySk1ia1RSUm1HOUVQS2IwN2ZKM2tyLW1Tc25Tdml6cGI2YUlmWWVWQ3BTYkJiWElWNVQ4d2tLMTBkUkRCZDk5V21aRlU?oc=5>

## RISKS

### JPMorgan (JPM) Reserves for Losses That Have Not Arrived. What Is the Buffer Really For?
- Summary: JPMorgan reserves for losses that have not arrived.
- Date: 2026-10-02 | Impact: medium | Horizon: medium | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMingFBVV95cUxNNlhGSVlDdEVIcml4T2xBUlktTHhJY29Ud2NmaXpuMUtqVG9KWkc4LXd1Y014VkZTR2E0YXBGZ2s4b0NpQUNtbmVITV9MUHh2ZGduSnRYcERoN3M5YTRJN3ZPOEt4c0FtTmcxbTIxRkRaRGpmdFpZRjgxNm56MUlpc0lLMXliRU54LTBXbFRfa0RqaFVCdmQ0SGdIWmhVdw?oc=5>

### JPMorgan Chase & Co. (NYSE:JPM) Stock Sale Disclosed by Sen. Sheldon Whitehouse
- Summary: JPMorgan Chase stock sale disclosed by Sen. Sheldon Whitehouse.
- Date: 2026-10-03 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi0gFBVV95cUxPbG5CTVlIcGZfc3JzVURpV2luMW53bGdWRnctODNsZUFOX3ROb2p0M29OdUw5cWdDZG13U1pYZW9FS2tGdG92d3Q3RTJnR2RRRk5vaUMwbm51OXlPR28zWUdzSTBUcmVXVWVjT3hoc0ZsVnRjcktaZzhXYmktQnJJaXBEaTE2V3ZQb0IxNjBVNlJjS1FyeE9ZQ0otUFRVdDVLYW1IVG5PdXBlTWxSRFNSaWNoRHJBM0NUNm9mQkNHdnhQRDlRQmUtRGh4LTdxVGl5SUE?oc=5>

### JPMorgan Chase & Co. $JPM Stock Holdings Decreased by Anchor Capital Advisors LLC
- Summary: JPMorgan Chase stock holdings decreased by Anchor Capital Advisors LLC.
- Date: 2026-10-02 | Impact: low | Horizon: short | Confidence: 0.8
- Sources: <https://news.google.com/rss/articles/CBMi1AFBVV95cUxQd25hWktNeS1ldHlhNFNHVWh5VmMyamNMNk1nUVNtQUlHc0lqa0ZMb0V2NVNmZ1gwdzVoWmpaRXhuUHZZUWhkYXJlRWUtdW1naUx5Qm9LemFDQ2dGUXFEc1Bxd2dmUXdBSTNUZkh2elpIYkxHSmFvQ193LXBsRHJVOXZrQzhXNXBSVFowREJsNEVtZDhaS1o0b2ZfSjNzbllXcTdFa1Jtby0wZ29wMnZnUDdscndJYUI4VGU1dkxscjljR0tvRVpzVktBYVRKV0NGSjNabQ?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | Revenue growth (%) | Market cap (USD) | 1Y return (%) |
|---|---:|---:|---:|---:|---:|---:|
| **JPM** | **14.19** | **2.48** | **N/A** | **30.40** | **876,084,985,856.00** | **9.18** |

Peers fetched as_of: 2026-10-08; JPM reuses existing data (market data as_of: 2026-10-07); fundamentals are yfinance info snapshots. 1Y return uses adjusted daily closes relative to the nearest trading day on or before one year earlier; missing values are not interpolated.

## EARNINGS CALENDAR

- Last reported earnings: 2026-07-14
- Next expected earnings: 2026-10-13 (yfinance; expected dates may change)

## MACRO (FRED)

Fetched as_of: 2026-10-03

| Metric | series_id | Latest value | Observation date |
|---|---|---:|---|
| Unemployment Rate (%) | UNRATE | 4.20 | 2026-09-01 |
| Consumer Price Index | CPIAUCSL | 334.13 | 2026-08-01 |
| Federal Funds Effective Rate (%) | FEDFUNDS | 3.75 | 2026-09-01 |

## LATEST FILING (EDGAR)

- Form: 10-Q
- Filing date: 2026-08-06
- Revenue (latest available single quarter): 24,246,000,000.00 USD; period 2014-07-01/2014-09-30; fiscal year/reporting period 2014/Q3
- Net income (latest available single quarter): 21,155,000,000.00 USD; period 2026-04-01/2026-06-30; fiscal year/reporting period 2026/Q2
- SEC link: https://www.sec.gov/Archives/edgar/data/19617/000162828026054343/jpm-20260630.htm

SEC requests use the demo placeholder contact email contact@example.com. Financial values use directly reported periods of approximately three months, without deriving quarters from cumulative values; fiscal year/period labels come from original facts and may refer to later comparative statements.

API documentation: [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html).

## SOURCES

- https://news.google.com/rss/articles/CBMimgFBVV95cUxQQUJCVENvbkFBUC1kUU5FWUNqbWU4b2F1SmdGeDZIMk5fMWZIZFVkb25aRUJQU3ozbndQMHNwZHNVYUdhRVdraXNtOE1Md0tKOTVmbjhocEJPdDBZQUhnQzdlLTdQZnB1U2I4dElSRUdWLTM2RkVlelFuUDRkdkxQM2RuV3U5OXRHSkE0VEFCYXpOZ3pzTWlXck1B?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxNUnAzZ0gwc19BdUV1aVdrS056bi14RktZREF5aWRrbFFSaXN1aFJVTUh4dlBwR3QxbG9rV3g4ejhYQ0hqZkw4TXBoLUlYZ2ZSeWJ2RnIwSDBWTm83d1h0TE1GbE42Rnpva0lXLVIxMHhEaFViVnB6RmpZb2dPUFJER1BEUEtueDI2VWZPODAxZ2lLdDRBekgzdXB3?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxPZ19TVk1KSE1WMmxZYVJZUEl3eS1XZkdNckN1QmRQUnYxQXN6OVBVY0gzcnI0Ny1hTHJqT2RKd1FqaHBFa3U3bjEtajlYRTZacFRZTmtTYVZVRVV2OExXbFRDVnYxZngtYmJvd1BFUndjWGhENHVGczlmOUh5QTFlY0hqR0dCVWY5XzBhQmgxS2VhWHRtY0VfTmZwZw?oc=5
- https://news.google.com/rss/articles/CBMixgFBVV95cUxOR2tmdmpTSnkwSG53QlpVTEhiUmhqZ1JNUUdiUGhYX2pXLTlCemdTcWllRk91QVBRSEdMdnUyRmhNZWxtV0Q2TlhoMnpxOU91OTAybktFUWJCNFFRMy1saFAtR1VadEpxS05vNF9hV1VHTVROeXdQbHMwT0RBV0JBZkJXU1lKTlZ2OWpFMlZrQnhUOTNfUXNCVUtkcS0ybXdZSS0wRk0xQ05LOXJwTmh5OGZOSjBRYXpzaVB6V2hsZjRtdUt5NVHSAcsBQVVfeXFMUEUzRk93MVNtdEc4V2E5MEoxdjhFc0NDV1FNbDBSOHMwRm9memFxdkcyc0RITGNveGx5a2VSSXNVRHNHZUp0OHBGbzNPazJJejVZUHBCTGdLaGRtbG1qbUJtT0JRQUhJQ3FjLXBlX0oxNUlXRHl2ZWVlSHRXUFBBQXY4U1ItNzZLV2lKc0Q1NUJIQ0NVa1VMemo3bkFOb1dwUld0TzI5ZXp4WklCZWtVa3RqWndXS1lhUWY4dnIzbk1MVGU2ekhBSnFHSFU?oc=5
- https://news.google.com/rss/articles/CBMimgFBVV95cUxQZS1hR2RnSWpLSmd6UTQwSnR5YUFSM250Ri1KWERKbTVqRW4wVUdVREVwZ0Q0SlBiVkNmcjRuazhBNmJJbTE3eEpvNkdXZ2I5V2w1VzZPNjBHUG4yQmpPX1J4YzZacEkwV252d1Z3RmJlSm11N2FoZjF3TnhrQWY4UFRhYnZiTEJOZEZxQWRsZlQzbEZVcjZCSHd3?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxPQ1l2MlZSNThPX29mT3FXZTluMjcyUGJOUmp0YnNWNlVOSVQ1NVB2QkstdDZxU2xGWjhrZ3hhU09CSXNQUzF2ekNVZlJZQU5XWTIwUjFvSGdiMHBpZHdnNjhqc3RYcC1WMzVaRGxkTnJqNWNrQ3ZYUXI5bWt5RDViaE8tVHlBdWsxclF5OElSbi1rNVFfcEE?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxPbU1qLTdsRmJXSEtMdGNtdEoxeWdBb3JqZDFiLTZ4MmxsTTVLQXVPOGtoZ19UU29WY3VCOVptQ09hSzYxQkhBcmtVeGhyRnFBbG1MNU5keU44ZENjN3JMTlJVOEx3bG5sVG96aGtoN1pKOWRiLXVqY21aa0xMYThSb1BFYnJBaU1MT0tuMnQyRXBDWWJ0b3VN?oc=5
- https://news.google.com/rss/articles/CBMilwFBVV95cUxNNUo4S0xSblFyRTBOMDN4OURpQ1JNUTBFenpnVjNaMVMzMHhURDRQXzd6R2NFRzJjVktaTjRqUmNzLV8xaGNmMU92ejNSY0NjRWhVbUpFdG9tSlJxb0N6aHU3UzFnZWN3ZWtwUDJfQWVTM094N05mZ25mUDlkZEY2N3NEcnp4bnJfUnJkUWl2YkVTODlPRWtJ?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxNcGoySGFlSURjVjlFdWxkYzg2akdUWm9qdThEMU00MDBNc09qSXI0Xy1jZ0NxZGlmdFVXMllEUmt5RWN0QUZUak82WjBaMlpXWllyc0wyaUlodkUtaDhNRWlFUjkzbEFhS1phTWNkRmJfbngzZFptb3NrMy1jeTJyRTZQMEJwU05BV1V1cXdlUGZuS3hsTXNKa3dLaWN6Zw?oc=5
- https://news.google.com/rss/articles/CBMixAFBVV95cUxQN2dZRFQ5NDRLYmJGQ0xMRHFod2g2SUdMVG1rLU1pV1ZjZlJ2eWFibEl1bW1TTVhnX0hsTF9ycWZBZkFIbENaLUNEUFRudEVQX2l6am1HNzNfOF82bzZjSlNyWEVQdTF3QkhhQjBtMS10eENQVXhSZjY3Vl9OTlJOR1l5Z3RjWGU4cFo2TkxqZkMyWjIwVGllTEdVMTVPS3R3RE43Z1F4azNMMmFvMWxSTnVxY2dEUVd4a1lORVVZaW16WUFD?oc=5
- https://news.google.com/rss/articles/CBMitgFBVV95cUxNSndzVTBjdlhPcW9GTElvVTdYVktIcjVDUlZULVRXeThubjdMbHlzWFBtTjJvZU9EeXY0Vjk0U05ua2ZxbUh5cGlpUXd0cDY0MTVkQS00bnFMaTVXc0VDQUgzd2xWb3lvRm5PaWw3ZjRITC1xS09yYkxYdFdpb2pkUUdLNkpsdzBNTk82eXdWd0h1MnNmQnp6N211YnJzS2M1emh2R0JMQnNVZ1h4d1U5WTFtcWN0QQ?oc=5
- https://news.google.com/rss/articles/CBMiygFBVV95cUxPeWI4T2lESUNrZTZtRzdiWmlRNjBKcFRTemhWbjdjUC1laTVYRDI1bWtzV0FGLWVPX0p1NjM1VUQzeUNjTjMzYXdmWmRIcmVaTU5jZFFmd2xZNmw0UGxYcWYyYXM2ZVNzOWE4c09zN3ZCbzdhUlNyMVZPYVlxUkV3NW0zMlhtaE96aUhrcnJJQ0lpeHpjOU5Bc19UU3NNdG10MjdORFVVZ1dpU3NKQi10VE9JWVhEMnNNNV9pa1AwUUhYVVAzWFMycG1B?oc=5
- https://news.google.com/rss/articles/CBMimwFBVV95cUxQekE0TUk1aFJUOUZhczFYdHJNOEVJb2ZuMHB6ZFBTZkppOU5vTVVncUFmYi1QNjBmTlFPRXBBX082OEpxOFc3dDNuQkxJdEhkYU1PWmxOVVV0WThNSEE3Y1pmS19kOG9aeXRwMDVIVHNmNzRLMHp4TUJNQ0E4TV84dDBTRm1VbDNRaUFPdDBKSl9SdGZTM3liWUg2bw?oc=5
- https://news.google.com/rss/articles/CBMimAFBVV95cUxPY19fbTR5d0ZudE96RExhTTY1SXBPUXpPeDRlV0ZBTWxlV2RRYnZjWGdrMkF2QWNrNklOTExieFpVby1HMVc2RGloWWg0ZmxKQ05SR29oTTBHSVZ4ZElTd3l4TXprMG5yODM0dU5wWGQ1V0FuOHVLMDVjX29Ib2xzOWhXb3VkY2NlLWdfWEYyTUplQXRIOTJZWg?oc=5
- https://news.google.com/rss/articles/CBMitwFBVV95cUxPT0MxSGV1cE9DaTIwdV9DYnBka0ZXWGhtMi1QWWFESjU3TmFBakhHamNQMkhzTXBfM01ldmZ6MEZxSWIzdzlMbmNCM2U4X1hrb2d2NUxZNEhHMmxSMXVZRy10djFJY0w0R2ZTazVKbVpRcHoySk1ia1RSUm1HOUVQS2IwN2ZKM2tyLW1Tc25Tdml6cGI2YUlmWWVWQ3BTYkJiWElWNVQ4d2tLMTBkUkRCZDk5V21aRlU?oc=5
- https://news.google.com/rss/articles/CBMingFBVV95cUxNNlhGSVlDdEVIcml4T2xBUlktTHhJY29Ud2NmaXpuMUtqVG9KWkc4LXd1Y014VkZTR2E0YXBGZ2s4b0NpQUNtbmVITV9MUHh2ZGduSnRYcERoN3M5YTRJN3ZPOEt4c0FtTmcxbTIxRkRaRGpmdFpZRjgxNm56MUlpc0lLMXliRU54LTBXbFRfa0RqaFVCdmQ0SGdIWmhVdw?oc=5
- https://news.google.com/rss/articles/CBMi0gFBVV95cUxPbG5CTVlIcGZfc3JzVURpV2luMW53bGdWRnctODNsZUFOX3ROb2p0M29OdUw5cWdDZG13U1pYZW9FS2tGdG92d3Q3RTJnR2RRRk5vaUMwbm51OXlPR28zWUdzSTBUcmVXVWVjT3hoc0ZsVnRjcktaZzhXYmktQnJJaXBEaTE2V3ZQb0IxNjBVNlJjS1FyeE9ZQ0otUFRVdDVLYW1IVG5PdXBlTWxSRFNSaWNoRHJBM0NUNm9mQkNHdnhQRDlRQmUtRGh4LTdxVGl5SUE?oc=5
- https://news.google.com/rss/articles/CBMi1AFBVV95cUxQd25hWktNeS1ldHlhNFNHVWh5VmMyamNMNk1nUVNtQUlHc0lqa0ZMb0V2NVNmZ1gwdzVoWmpaRXhuUHZZUWhkYXJlRWUtdW1naUx5Qm9LemFDQ2dGUXFEc1Bxd2dmUXdBSTNUZkh2elpIYkxHSmFvQ193LXBsRHJVOXZrQzhXNXBSVFowREJsNEVtZDhaS1o0b2ZfSjNzbllXcTdFa1Jtby0wZ29wMnZnUDdscndJYUI4VGU1dkxscjljR0tvRVpzVktBYVRKV0NGSjNabQ?oc=5

## Demo notes and limitations

- Multi-ticker local demo; AI items require human spot checks; RSS coverage is not guaranteed.
- Free-tier Gemini grounding (google_search tool) returned 429; the demo uses Google News RSS + plain-text AI extraction.
- Missing market data or fundamentals are marked N/A; no numbers are fabricated. This report is not investment advice.
