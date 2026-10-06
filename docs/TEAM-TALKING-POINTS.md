# JSOSIF 双 Pipeline 方向讨论 — 发言提纲（一页纸）

## 架构（画白板/投屏）

```
JSOSIF Holdings
  ├─ Quant pipeline:      Market APIs (yfinance) → Python metrics → Intelligence DB
  └─ AI Research pipeline: News RSS → Gemini extract/classify → Intelligence DB
                                                              ↓
                                                          Dashboard (新增 Intelligence 页)
```

## 五段话（中英对照，英文可直接念）

1. **现状**：我有个量化看板 MVP（私有仓），synthetic 持仓，performance / attribution / risk 页面现成的。
   *"I built a quant dashboard MVP in a private repo — performance, attribution, risk pages, all working."*

2. **想做的方向**：双 pipeline——量化算数，AI 负责搜集整理信息，汇入 Intelligence DB，dashboard 加一个 Intelligence 页面。
   *"I want to expand it into dual pipelines: quant for numbers, AI for research, merged into an intelligence database with a new dashboard page."*

3. **已验证的**：NVDA 单资产 demo 端到端跑通（报告可投屏）。趟过的坑：免费档 Gemini grounding 直接 429，只能用 RSS+AI 两步法；Groq 把我们这类机器 IP ban 了。
   *"Single-asset NVDA demo works end-to-end. Two lessons: free-tier Gemini grounding returns 429, so I used RSS + AI extraction instead; Groq bans datacenter IPs."*

4. **开放问题**（抛给他们）：Intelligence DB 用 SQLite 还是 Postgres？定时刷新怎么做？多资产怎么扩展？免费 quota 怎么管？
   *"Open questions for the team: SQLite vs Postgres for the intel DB? How to schedule refreshes? How to scale to multi-asset? How to manage free-tier quotas?"*

5. **分工**：谁想认领哪个模块？
   *"Who wants to own which module?"*

## 可能被问到的问题（诚实回答）

- **数据准不准？** → 免费源（yfinance / RSS / SEC EDGAR），AI 条目需人工抽查。demo 阶段够用，生产级要再评估。
- **demo 代码是你写的吗？** → "AI 辅助写的，细节我还在学"——不丢人，别硬撑。
- **为什么不用付费 API？** → 学生基金零预算，先把免费档榨干，瓶颈列出来再谈要不要花钱。
- **和现有 dashboard 什么关系？** → 现有页面不动，Intelligence 是新增页面；quant 页面就是 pipeline 的底座。

## 心态

不是汇报成果，是拉人一起设计。目标：走出会议室时，架构方向有人点头、模块有人认领。
