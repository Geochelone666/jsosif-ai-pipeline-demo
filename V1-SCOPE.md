# jsosif-ai-pipeline v1 范围（pilot-ready）

制定：2026-10-13 18:05 EDT。目标：2026-10-16（周五）前达到 v1，Lucas 当天 transfer 到团队 GitHub。
背景：2026-10-13 基金团队演示反馈——定位收敛为"analyst 研究前的 standardized snapshot"，
推送从 Telegram 改邮件，开始往内部 pilot 推进。

## v1 定义：pilot 可用

### P0（必须有，否则不算 v1）
1. **邮件推送通道**：pipeline 跑完后把 standardized snapshot 通过邮件发出，替代 Telegram。
   - 每 holding 一份标准化快照（现有 regenerate_report.py 的报告为基础）。
   - 发送后端可插拔；首版用 Lucas Gmail（connector 已接），收件人由配置文件管理。
   - 首次发送前必须 Lucas 逐封确认（draft 审阅），pilot 稳定后再谈自动发送。
2. **快照格式冻结**：邮件里的 snapshot 结构固定（quant 指标 + AI 摘要 + 假设/数据新鲜度声明），
   团队看到的格式每天一致。
3. **可审计性**（Round 7 正在做）：failure modes → explicit contracts → auditable outputs，
   7 个 jsosif 站点（S01/S02/S03/S08/S11/S20/S21）即 v1 质量门。

### P1（有则更好）
4. 一键跑全流程：`run_phase1.py → 报告 → 打包 → 发邮件` 一条命令。
5. 收件人分组（sector teams）配置。
6. 发送记录台账（发了什么、给谁、何时）。

### 不做（v1 明确排除）
- 不碰投资判断逻辑；不替代 analyst 看 10-K/10-Q（团队共识）。
- 不自动发送：所有对外邮件先经 Lucas 确认。
- 不迁 org：周五 transfer 由 Lucas 本人操作；Muse 对 org 只读。

## 节奏
- 每天至少一次实质更新（代码/测试/文档），commit 像人一样自然间隔。
- 每次更新附"教学注记"：改了什么、为什么这么改（Lucas 要学 dev workflow）。
- 每日 driver：cron `jsosif-v1-daily` 每天 09:00 EDT 检查进度并派发当日任务。

## 待 Lucas 决策
- [ ] 邮件发送账号：先用 Lucas 个人 Gmail pilot，还是等团队邮箱？
- [ ] 首批收件人名单（Joseph 邮箱也待提供）。
- [ ] 周五 transfer 的目标位置（org 名 / 新 repo 名）。

- 2026-10-13T22:03:09+00:00 — P0-1 progress: offline email rendering implemented with configurable recipients, plain text/HTML MIME, graceful missing-section handling and a dry-run backend; send remains blocked pending Lucas explicit approval. Teaching note: rendering and transport are separated so every message can be reviewed before sending.
