# JSOSIF AI Pipeline Demo —— 教学包（Lucas 专用）

目标：开会前能讲明白架构、每个脚本、关键公式，被问不倒。读完去 GPT 对话里追问也行。

## 1. 架构（一句话 + 一张图）

双 pipeline，汇成一份报告：

```
Market APIs (yfinance) ──→ Python metrics ──┐
                                            ├─→ {TICKER}-intelligence-20261003.md
News RSS ──→ Gemini extract/classify ────────┘
```

- **Quant pipeline**：拿行情，算数。确定性，可复算。
- **AI Research pipeline**：拿新闻，分类。概率性，需人工抽查。
- 两条线在 `regenerate_report.py` 汇合，拼成 Markdown。

## 2. 数据流（每个文件干什么）

| 脚本 | 输入 | 处理 | 输出 |
|---|---|---|---|
| quant.py | yfinance NVDA/SPY 日线 | 算收益、风险、技术指标 | quant.json |
| ai_extract.py | Google News RSS 25 条标题 | 拼 prompt → Gemini 分类 | ai-intel.json |
| comparables.py | yfinance info ×4 | 取估值倍数 | comparables.json |
| earnings.py | yfinance earnings_dates | 取上次/下次财报日 | earnings.json |
| fred.py | FRED API | 取失业率/CPI/联邦基金利率 | fred.json |
| edgar.py | SEC EDGAR API | 取最新 10-Q + 当季营收/净利 | edgar.json |
| regenerate_report.py | 以上所有 JSON | 拼 Markdown | 报告 |

## 3. 关键公式（会算、会讲）

- **收益率**：(末价 − 初价) / 初价。1Y 取一年前最近交易日。
- **年化波动率**：日收益标准差 × √252。
- **Beta**：Cov(NVDA 日收益, SPY 日收益) / Var(SPY 日收益)。1.88 = 比大盘波动大 88%。
- **最大回撤**：从历史最高点跌下来的最大幅度。−20.2% 意味着曾从高点跌掉两成。
- **Sharpe**：(年化收益 − 无风险利率) / 年化波动率。这里 rf=0，所以是 0.76。
- **RSI(14)**：Wilder 平滑，>70 超买、<30 超卖。63 = 偏热但没超买。
- **MACD**：EMA(12) − EMA(26)；signal = MACD 的 EMA(9)；histogram = MACD − signal。正的 histogram = 动量向上。

## 4. 四个坑（亲手验证过，开会可讲）

1. **Gemini 免费档 grounding 不可用**：`google_search` 工具直接 429。 workaround：RSS 抓取 + 纯文本抽取两步法。
2. **Groq ban 机房 IP**：Cloudflare 1010，请求到不了鉴权，不是 key 的问题。
3. **yfinance 是延迟行情**：免费档非实时；基本面是抓取时快照。
4. **AI 输出要人工抽查**：分类的 confidence 是抽取置信度，不是投资成功率。

## 5. 团队可能问的 Q&A

- **数据准不准？** → 免费源，够 demo；生产级要评估。quant 部分可复算验证过，AI 部分要人工抽查。
- **为什么不用付费 API？** → 学生基金零预算，先把免费档榨干。
- **demo 和生产差在哪？** → JSON 文件 vs 真数据库；手动跑 vs 定时 pipeline；3 个 ticker vs 全持仓；无监控告警。
- **代码是你写的吗？** → "AI 辅助写的，细节我还在学。"（标准答案，别硬撑）
- **和 Efficient-Frontier 什么关系？** → 那是组合优化，这个是投研情报，不重叠，是补空白。

## 6. 30 分钟速通计划

1. 读一遍 NVDA 报告（10 分钟）
2. 看 quant.py 的指标计算段（10 分钟）
3. 看 ai_extract.py 的 prompt 拼装（5 分钟）
4. 背下第 4 节四个坑（5 分钟）
