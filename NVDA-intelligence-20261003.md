# NVDA Intelligence Demo

- ticker: **NVDA**
- 报告 as_of: **2026-10-03**
- 行情 as_of: **2026-10-02**
- Quant 数据源：yfinance（NVDA/SPY 日线 + info 基本面）
- AI 模型：**gemini-3.5-flash-lite**（Google News RSS 抓取 25 条 → AI 抽取分类；grounding 在免费档不可用，改用 RSS+AI 两步法）

## QUANTITATIVE

| 指标 | 数值 |
|---|---:|
| Close | 233.9500 |
| Return 1D (%) | 1.3385 |
| Return 1W (%) | 3.9454 |
| Return 1M (%) | 4.3678 |
| Return YTD (%) | 25.7359 |
| Return 1Y (%) | 24.1519 |
| Annualized volatility (%) | 37.7210 |
| Beta vs SPY | 1.8806 |
| Max drawdown (%) | -20.2144 |
| Sharpe (rf=0) | 0.7633 |
| P/E (trailing) | 29.17 |
| P/B | 24.67 |
| EV/EBITDA | 27.90 |
| Revenue growth (%) | 105.90 |
| MA50 | 218.1191 |
| Close vs MA50 (%) | 7.2579 |
| MA200 | 200.3791 |
| Close vs MA200 (%) | 16.7537 |
| RSI (14, Wilder) | 63.0111 |
| MACD (12,26) | 3.5406 |
| MACD signal (9) | 2.7183 |
| MACD histogram | 0.8223 |

计算口径：yfinance auto_adjust=True 日收盘价；1Y 收益已用 Decimal 从原始 CSV 独立复算验证通过。
行情样本数：NVDA/SPY 各 252 个交易日。

## TAILWINDS

### Nvidia stock hits new all-time high, market cap at $5.7 trillion
- 摘要：Nvidia的股价创下历史新高，市值达到5.7万亿美元，强劲的市场表现彰显了其在AI芯片领域的绝对统治力。
- 日期：2026-10-02｜影响：high｜期限：medium｜置信度：0.95
- 来源：<https://news.google.com/rss/articles/CBMivgFBVV95cUxPRVh0ZkJ2cXBWRFg3bFpiVHphckdSTjlvYi1pTzJWYnhYRFV2c21WSFZWbkozNG00V3pwdWE4dXhqc2VMcmNvdk9aQkxsSVpZV3NjSU9yd05UMjluQXB2LXdwMV9UaDZjZVZDME5ZS2ZURUZkY1oweGdPNzJjam9QM0lTNktKeHZ2aFc0bnQxV2RwVVhENGlGNFFmdjcxUGpJZXZUQnk2aWhZSWpkV25vZmtjNThqLWZqWUg0dUF3?oc=5>

### Nvidia Stock Climbs After Morgan Stanley Names It a 'Top Semiconductor Pick'
- 摘要：摩根士丹利将Nvidia评为顶级半导体首选，指出当前的AI发展趋势完全契合公司的核心优势。
- 日期：2026-10-02｜影响：high｜期限：short｜置信度：0.9
- 来源：<https://news.google.com/rss/articles/CBMioAFBVV95cUxOd05BNkoxZ1c4V0h5cGpUSWNmNS1jQXJaVjhxYzBTQnVSM2cwYTJPclMyNll6TnFxOHJQVjlOUzgxWlVGcGh3N2tBaU5jNWRCV29WaHBHWDNzWGFOdGFQRGVMT2RDbnRhTkRBT0RGakdVakxRTDRGVHZsWHRwek9teHUzcm8wcVBSellUSEZHYXM0NUhtc1NHRVFDdVI4YzQt?oc=5>

### Investor Makes Bold Prediction: NVIDIA Could Deliver “$360 Billion in Free Cash Flow” Next Year
- 摘要：分析师预测Nvidia明年有望产生高达3600亿美元的自由现金流，展现出极其惊人的盈利能力。
- 日期：2026-10-02｜影响：high｜期限：long｜置信度：0.8
- 来源：<https://news.google.com/rss/articles/CBMipAFBVV95cUxNZzhueUxsZnhIMWhoZG10dm9FSzh5UFNDVmIzWnVEUFlFajBOZmhyNzZTNXBNVXVLMy1LdFA4bDRSUEtyVFJiQVZaeVZReVkxSHoxVUVzM0ktOXFWQ1hWNXVBVU9vVzRyVnRsc0h0Z3VieUNycnB5REprXzh3eUpWYVJUcE81dkFIeTFXUUVQcnZnQVZ1dngwWTZmZ1VwN1ItQXByUg?oc=5>

## HEADWINDS

（本轮无条目）

## CATALYSTS

### Stock Market Today, Sept. 30: Nvidia Authorizes $150B Buyback, Lifting Total to $235B
- 摘要：Nvidia宣布增加1500亿美元的股票回购授权，使总额达到2350亿美元，这将为股价提供强有力的支撑。
- 日期：2026-09-30｜影响：high｜期限：medium｜置信度：0.95
- 来源：<https://news.google.com/rss/articles/CBMilgFBVV95cUxOUlUzUXJNRTI3elQwZjlxVFpTa2IwTWtfeFpUQjdlV0gzb1ZndkFkNXhQODVHd2FVM3FwMWJ0VG1nY0UyWmZNNjYtRHNqeXBkTkhGelB5cE13Y1p6T3VtN1lEekdOSm5vVHM2TXByLVYxcVY3T0J4NllCQmJZeVhSNG9YcmwzRlpoMXFnR1MweEMzckNzeWc?oc=5>

### CoreWeave Unleashes Nvidia's Vera Rubin, Analyst Sees Room to Run
- 摘要：CoreWeave开始部署Nvidia的Vera Rubin架构，分析师认为新一代产品将进一步打开成长空间。
- 日期：2026-10-02｜影响：medium｜期限：medium｜置信度：0.85
- 来源：<https://news.google.com/rss/articles/CBMi1gFBVV95cUxPS19TZUtZUnZ5QVZNWUJmWDR6enJJZk5SWWo0dlZFckxfVktDMkNUQVF6UHI0VkQ4eEhwRm9OX1VWbHVORFdOazU2X29Oc0xrS1lXc3pkVlpCa1pObW5xUUJJbEdQMGh1XzVhLTV0S0dqQXdJa3RqSFFvbkI5RGRjMk5LcmZhUlJPMVBYNlUydkZrbU5obHhwZkVBRGpUWC1hdlZKbTN4QWpZX21qalNPRExvSUVLZ081NEk1RkJFZEhSbDdRYjdXRnhOTWZBQ1Z2aEtER2xR?oc=5>

## RISKS

### Nvidia Stock Has Become Deeply Undervalued, But Watch Out For Accounts Receivable (NVDA)
- 摘要：尽管股价被认为具备投资价值，但投资者仍需警惕应收账款相关潜在的财务风险。
- 日期：2026-10-02｜影响：medium｜期限：short｜置信度：0.75
- 来源：<https://news.google.com/rss/articles/CBMivgFBVV95cUxOS19ad1o0b1dUeUtRUldmMlZWQTBha2sxUXMwWGxMU0NjX1dWVjVaZHMyOHlhMmZEdEZ4VktPZDR1cFRYSFZUTVJrNk1xZ2Q0R1BUbDkwbFk2N2Z6OFRhYnFoUEdJaHFaeERpbEFsLVFnTmlkX3h5MlE1cmZyVFZGZnBLeV9qenJfekxLUk9jR19GRDF0cC1vbHAycGZubTA4a2I5VzgzU3Q5QW9MandFcmlWXzBnRnl0bFM0RXFB?oc=5>

### NVDA Stock Eyes Worst First Half Since 2022: Retail Patience Wears Thin As Board Member Trims Stake For Third Time This Year
- 摘要：部分董事会成员今年已多次减持公司股份，引发了散户投资者对估值与持股耐心的担忧。
- 日期：2026-10-02｜影响：low｜期限：short｜置信度：0.7
- 来源：<https://news.google.com/rss/articles/CBMilgJBVV95cUxORzhNMG5sbTZPeXlsLUFWb0xrc05MRGNQcW9aS3VrOTF5RFRYdFRuQkZvRFFFdkdyNzNiaGNodWdJdjJHZE9oYUNnUWxoclN6LTU4YTRIRnR6NnZKRDV5ZVVSWWJPdGNsdFZZM01rZ1V2ajlPcTFHczdBUElKSUtJbEptTFc5V1JKQXZMbHpkeWxDazRpZGc3eHhDVkxuSXN0OE51QmI3bU1FN2pWMEFVODlFT2Q5SVVrXzNQQktFSjR1dkRFWlBpRlF4V2JuZW1rSFZtSU9sWnU5bXBRaDJxbjVGN3M2cGg4dG5SVWY4d2h6SENzbGlkdGk2dUVvWmtDRmZudmVhOHlmeTNGU0F0S2NWNFdSZw?oc=5>

## PEER COMPARABLES

| ticker | P/E | P/B | EV/EBITDA | 营收增长% | 市值 (USD) | 1Y收益% |
|---|---:|---:|---:|---:|---:|---:|
| **NVDA** | **29.17** | **24.67** | **27.90** | **105.90** | **5,649,190,617,088.00** | **24.15** |
| AMD | 160.89 | 15.39 | 107.30 | 50.10 | 1,034,842,210,304.00 | 273.48 |
| AVGO | 45.36 | 17.01 | 33.12 | 85.50 | 1,695,307,005,952.00 | 5.80 |
| MSFT | 28.83 | 8.69 | 20.05 | 17.70 | 3,842,942,959,616.00 | 1.17 |
| TSM | 34.23 | 97.22 | 5.43 | 36.00 | 2,452,061,159,424.00 | 65.83 |

可比公司抓取日期：2026-10-03。NVDA 复用既有数据（行情日期 2026-10-02）；基本面为 yfinance info 快照。1Y 为复权日收盘价相对一年前最近交易日的收益；缺失值不插值。

## EARNINGS CALENDAR

- 上次已发布财报：2026-08-26
- 下次预计财报：2026-11-17（yfinance，预计日期可变动）

## MACRO (FRED)

未配置 FRED key，跳过

## LATEST FILING (EDGAR)

- Form：10-Q
- Filing date：2026-08-26
- Revenue（最新可用单季度）：96,221,000,000.00 USD；期间 2026-04-27/2026-07-26；财年/披露期 2027/Q2
- Net income（最新可用单季度）：59,688,000,000.00 USD；期间 2026-04-27/2026-07-26；财年/披露期 2027/Q2
- SEC 链接：https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm

SEC 请求使用 demo 占位联系邮箱 contact@example.com。财务值只使用直接披露的约三个月期间，不从累计值推算；披露财年/期来自原始 fact，可能对应后续比较报表。

数据接口文档：[SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces)、[FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html)。

## SOURCES

- https://news.google.com/rss/articles/CBMivgFBVV95cUxPRVh0ZkJ2cXBWRFg3bFpiVHphckdSTjlvYi1pTzJWYnhYRFV2c21WSFZWbkozNG00V3pwdWE4dXhqc2VMcmNvdk9aQkxsSVpZV3NjSU9yd05UMjluQXB2LXdwMV9UaDZjZVZDME5ZS2ZURUZkY1oweGdPNzJjam9QM0lTNktKeHZ2aFc0bnQxV2RwVVhENGlGNFFmdjcxUGpJZXZUQnk2aWhZSWpkV25vZmtjNThqLWZqWUg0dUF3?oc=5
- https://news.google.com/rss/articles/CBMioAFBVV95cUxOd05BNkoxZ1c4V0h5cGpUSWNmNS1jQXJaVjhxYzBTQnVSM2cwYTJPclMyNll6TnFxOHJQVjlOUzgxWlVGcGh3N2tBaU5jNWRCV29WaHBHWDNzWGFOdGFQRGVMT2RDbnRhTkRBT0RGakdVakxRTDRGVHZsWHRwek9teHUzcm8wcVBSellUSEZHYXM0NUhtc1NHRVFDdVI4YzQt?oc=5
- https://news.google.com/rss/articles/CBMipAFBVV95cUxNZzhueUxsZnhIMWhoZG10dm9FSzh5UFNDVmIzWnVEUFlFajBOZmhyNzZTNXBNVXVLMy1LdFA4bDRSUEtyVFJiQVZaeVZReVkxSHoxVUVzM0ktOXFWQ1hWNXVBVU9vVzRyVnRsc0h0Z3VieUNycnB5REprXzh3eUpWYVJUcE81dkFIeTFXUUVQcnZnQVZ1dngwWTZmZ1VwN1ItQXByUg?oc=5
- https://news.google.com/rss/articles/CBMilgFBVV95cUxOUlUzUXJNRTI3elQwZjlxVFpTa2IwTWtfeFpUQjdlV0gzb1ZndkFkNXhQODVHd2FVM3FwMWJ0VG1nY0UyWmZNNjYtRHNqeXBkTkhGelB5cE13Y1p6T3VtN1lEekdOSm5vVHM2TXByLVYxcVY3T0J4NllCQmJZeVhSNG9YcmwzRlpoMXFnR1MweEMzckNzeWc?oc=5
- https://news.google.com/rss/articles/CBMi1gFBVV95cUxPS19TZUtZUnZ5QVZNWUJmWDR6enJJZk5SWWo0dlZFckxfVktDMkNUQVF6UHI0VkQ4eEhwRm9OX1VWbHVORFdOazU2X29Oc0xrS1lXc3pkVlpCa1pObW5xUUJJbEdQMGh1XzVhLTV0S0dqQXdJa3RqSFFvbkI5RGRjMk5LcmZhUlJPMVBYNlUydkZrbU5obHhwZkVBRGpUWC1hdlZKbTN4QWpZX21qalNPRExvSUVLZ081NEk1RkJFZEhSbDdRYjdXRnhOTWZBQ1Z2aEtER2xR?oc=5
- https://news.google.com/rss/articles/CBMivgFBVV95cUxOS19ad1o0b1dUeUtRUldmMlZWQTBha2sxUXMwWGxMU0NjX1dWVjVaZHMyOHlhMmZEdEZ4VktPZDR1cFRYSFZUTVJrNk1xZ2Q0R1BUbDkwbFk2N2Z6OFRhYnFoUEdJaHFaeERpbEFsLVFnTmlkX3h5MlE1cmZyVFZGZnBLeV9qenJfekxLUk9jR19GRDF0cC1vbHAycGZubTA4a2I5VzgzU3Q5QW9MandFcmlWXzBnRnl0bFM0RXFB?oc=5
- https://news.google.com/rss/articles/CBMilgJBVV95cUxORzhNMG5sbTZPeXlsLUFWb0xrc05MRGNQcW9aS3VrOTF5RFRYdFRuQkZvRFFFdkdyNzNiaGNodWdJdjJHZE9oYUNnUWxoclN6LTU4YTRIRnR6NnZKRDV5ZVVSWWJPdGNsdFZZM01rZ1V2ajlPcTFHczdBUElKSUtJbEptTFc5V1JKQXZMbHpkeWxDazRpZGc3eHhDVkxuSXN0OE51QmI3bU1FN2pWMEFVODlFT2Q5SVVrXzNQQktFSjR1dkRFWlBpRlF4V2JuZW1rSFZtSU9sWnU5bXBRaDJxbjVGN3M2cGg4dG5SVWY4d2h6SENzbGlkdGk2dUVvWmtDRmZudmVhOHlmeTNGU0F0S2NWNFdSZw?oc=5

## Demo 说明与限制

- 单资产本地一次性演示；AI 条目需人工抽查；RSS 覆盖率不保证。
- 免费档 Gemini grounding（google_search 工具）返回 429，改用 Google News RSS + 纯文本 AI 抽取的两步法跑通。
- 行情或基本面缺失均标 N/A，没有补造数字。报告不构成投资建议。
