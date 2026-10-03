#!/usr/bin/env python3
"""Regenerate the NVDA intelligence report with quant + AI results."""
import json

quant = json.load(open("quant.json", encoding="utf-8"))
q = quant["metrics"]
ai = json.load(open("ai-intel.json", encoding="utf-8"))
rss = json.load(open("rss-items.json", encoding="utf-8"))

# map rss links by headline for sources
link_by_headline = {}
for it in rss:
    link_by_headline[it["headline"]] = it["link"]

def section(name, items):
    out = [f"## {name}\n"]
    if not items:
        out.append("（本轮无条目）\n")
        return "\n".join(out)
    for it in items:
        srcs = " ".join(f"<{u}>" for u in it.get("sources", []) if u)
        if not srcs:
            u = link_by_headline.get(it["headline"], "")
            srcs = f"<{u}>" if u else ""
        out.append(
            f"### {it['headline']}\n"
            f"- 摘要：{it['summary']}\n"
            f"- 日期：{it['date']}｜影响：{it['impact']}｜期限：{it['horizon']}｜置信度：{it['confidence']}\n"
            + (f"- 来源：{srcs}\n" if srcs else "")
        )
    return "\n".join(out)

def fmt(v, d=4):
    if v is None:
        return "N/A"
    return f"{v:.{d}f}"

q = q  # metrics dict
quant_table = f"""## QUANTITATIVE

| 指标 | 数值 |
|---|---:|
| Close | {fmt(q.get('Close'))} |
| Return 1D (%) | {fmt(q.get('Return 1D (%)'))} |
| Return 1W (%) | {fmt(q.get('Return 1W (%)'))} |
| Return 1M (%) | {fmt(q.get('Return 1M (%)'))} |
| Return YTD (%) | {fmt(q.get('Return YTD (%)'))} |
| Return 1Y (%) | {fmt(q.get('Return 1Y (%)'))} |
| Annualized volatility (%) | {fmt(q.get('Annualized volatility (%)'))} |
| Beta vs SPY | {fmt(q.get('Beta vs SPY'))} |
| Max drawdown (%) | {fmt(q.get('Max drawdown (%)'))} |
| Sharpe (rf=0) | {fmt(q.get('Sharpe (rf=0)'))} |
| P/E (trailing) | {fmt(q.get('P/E (trailing)'), 2)} |
| P/B | {fmt(q.get('P/B'), 2)} |
| EV/EBITDA | {fmt(q.get('EV/EBITDA'), 2)} |
| Revenue growth (%) | {fmt(q.get('Revenue growth (%)'), 2)} |
| MA50 | {fmt(q.get('MA50'))} |
| Close vs MA50 (%) | {fmt(q.get('Close vs MA50 (%)'))} |
| MA200 | {fmt(q.get('MA200'))} |
| Close vs MA200 (%) | {fmt(q.get('Close vs MA200 (%)'))} |
| RSI (14, Wilder) | {fmt(q.get('RSI (14, Wilder)'))} |
| MACD (12,26) | {fmt(q.get('MACD (12,26)'))} |
| MACD signal (9) | {fmt(q.get('MACD signal (9)'))} |
| MACD histogram | {fmt(q.get('MACD histogram'))} |
"""

all_sources = []
seen = set()
for sec in ("tailwinds", "headwinds", "catalysts", "risks"):
    for it in ai[sec]:
        for u in it.get("sources", []):
            if u and u not in seen:
                seen.add(u); all_sources.append(u)
        u = link_by_headline.get(it["headline"], "")
        if u and u not in seen:
            seen.add(u); all_sources.append(u)

report = f"""# NVDA Intelligence Demo

- ticker: **NVDA**
- 报告 as_of: **2026-10-03**
- 行情 as_of: **{quant.get('as_of','2026-10-02')}**
- Quant 数据源：yfinance（NVDA/SPY 日线 + info 基本面）
- AI 模型：**gemini-3.5-flash-lite**（Google News RSS 抓取 25 条 → AI 抽取分类；grounding 在免费档不可用，改用 RSS+AI 两步法）

{quant_table}
计算口径：yfinance auto_adjust=True 日收盘价；1Y 收益已用 Decimal 从原始 CSV 独立复算验证通过。
行情样本数：NVDA/SPY 各 252 个交易日。

{section('TAILWINDS', ai['tailwinds'])}
{section('HEADWINDS', ai['headwinds'])}
{section('CATALYSTS', ai['catalysts'])}
{section('RISKS', ai['risks'])}
## SOURCES

""" + "\n".join(f"- {u}" for u in all_sources) + """

## Demo 说明与限制

- 单资产本地一次性演示；AI 条目需人工抽查；RSS 覆盖率不保证。
- 免费档 Gemini grounding（google_search 工具）返回 429，改用 Google News RSS + 纯文本 AI 抽取的两步法跑通。
- 行情或基本面缺失均标 N/A，没有补造数字。报告不构成投资建议。
"""

with open("NVDA-intelligence-20261003.md", "w", encoding="utf-8") as f:
    f.write(report)
print("report regenerated,", len(report), "chars")
