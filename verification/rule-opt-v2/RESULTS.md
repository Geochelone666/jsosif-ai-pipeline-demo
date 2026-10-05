# JSOSIF rule-opt-v2 对比报告 — 2026-10-05

仅在本地 `rule-opt-v2` 分支探索；没有 merge、push、Notion 操作或模型/API 调用，也未增加凭据。

## 指标

同一组六家公司缓存新闻：150 条输入，按公司去重后 147 条。

| 指标 | v1 | v2 | 变化 |
|---|---:|---:|---:|
| 规则覆盖率 | 41/147 = 27.89% | 74/147 = 50.34% | +22.45 个百分点 |
| AI 候选标题数 | 106 | 73 | 减少 33 条 |
| 历史 AI 类别一致率 | 11/24 = 45.83% | 21/29 = 72.41% | +26.58 个百分点 |

达成本缓存集的覆盖率 ≥50%、历史 AI 类别一致率 ≥70% 目标。共同可比的 23 条标题，一致数从 11 增至 16（47.83% → 69.57%）；总体一致率的分母也随覆盖率变化。

历史 AI 仅有四类标签，并非人工真值；不代表事件、情绪提取准确率，也不代表新数据上的泛化表现。规则开发和评估使用同一缓存集，属于探索性结果，没有独立留出集；未验证在线 fallback。标题减少不必然减少 API 请求次数（原流程已批处理）。

## 漏判分析与改动

v1 的 106 条漏判包括动词变形（rise/dropped/raised）、财报 beat/miss 句式、评级和目标价调整、机构买卖持仓、中文公司别名，以及事实陈述后附带评论问题的标题。其余大量是价格预测、估值推测、提问或相互冲突的信号。

新增或扩展：
- 公司匹配：ticker、GOOG、Amazon.com、Azure，以及英伟达/輝達、微软、苹果、谷歌、亚马逊、特斯拉；保留英文单词边界，防止 Pineapple 匹配 Apple。
- 事件：并购、spin-off/股票拆分、回购、分红、指引、评级/目标价、机构持仓、明确日历提醒和具体风险；财报 beats/misses estimates、cuts/raises guidance 可直接识别。
- 更具体的公司事件优先于宽泛的 earnings/stock 词汇；产品、回购、拆分等公告作为 catalysts，评级上调/下调保留方向。
- 事实后附带评论问句可识别，但首句预测、条件语气及冲突信号继续回退；修复 competitor stock move 被归给目标公司的问题，以及 falls shy 被当作下跌的问题。
- 机构持仓买卖是中性事件，不直接推断公司前景；摘要仍复制标题，不编造信息。

新增规则命中的事件分布：{'risk': 3, 'analyst': 4, 'market_move': 18, 'calendar': 1, 'ownership': 6, 'product': 1, 'partnership': 1, 'earnings': 3}。
仍回退 73 条的事件分布：{'market_move': 48, 'earnings': 3, 'unknown': 10, 'buyback': 1, 'stock_split': 1, 'workforce': 1, 'analyst': 2, 'product': 6, 'guidance': 1}。逐条 v1/v2 分类、历史标签及剩余 miss 见 `comparison.json`。

| 公司 | v1 命中/总数 | v2 命中/总数 |
|---|---:|---:|
| NVDA | 7/25 | 10/25 |
| MSFT | 5/23 | 11/23 |
| AAPL | 5/25 | 13/25 |
| GOOGL | 8/25 | 10/25 |
| AMZN | 6/24 | 13/24 |
| TSLA | 10/25 | 17/25 |

## Schema 与验证

保留四个分类数组及全部原字段，包括 `extraction_method=rule/ai/unknown`、RSS 元数据、未分类列表和统计。事件词表新增 ownership/calendar/risk；字段结构兼容，但若外部消费者硬编码 event_type 枚举，需要同步新增值。impact/horizon 仍为保守固定默认值。

通过的可复现命令：

```bash
python3 -m unittest -v test_ai_extract test_rule_opt_v2
python3 verification/rule-opt-v2/compare.py
python3 verification/rule-opt-v2/check_reports.py
```

原有 4 项测试全部通过，新增 3 项参数化测试覆盖事件句式、别名、冲突/预测、日期和字段。六家公司仅添加元数据时报告字节一致；v2 输出报告均可渲染，隔离目录中的现有 validate_phase1.py 通过。所有验证离线完成。

## 分支与基线说明

开始时目录没有 `.git`。从远端取回 Git 历史，保留全部本地文件，执行 `git checkout -b rule-opt-v2`。远端 main 与本地已有 v1 有差异，因此本报告明确以冻结的本地 `v1_ai_extract.py` 为基线；12 个新闻/历史 AI fixture 文件也冻结在本目录。main 引用不变。仅暂存本任务的规则、测试及验证文件，其他已有工作区修改未纳入暂存。仓库没有配置 Git 提交身份，commit 未创建；未擅自填写身份。改动保留在 rule-opt-v2 分支工作区，没有 push 或合并，待用户审阅。
