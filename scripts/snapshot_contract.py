"""Shared v1 email snapshot contract, keeping daily payload structure stable.

Identity carries ticker, YYYY-MM-DD as_of and YYYYMMDD report_stamp. Quant
rows carry metric, string-or-None value, ok/missing availability and nullable
reason. AI summaries carry status and a mapping of section names to text.
Freshness records existing timestamps and assumptions, with no_refresh_note
fixed to '邮件生成不刷新任何数据'. Validation must never fetch or refresh data.
"""

CONTRACT_VERSION = '1.0'
REQUIRED_TOP_LEVEL = [
    'contract_version', 'identity', 'quant', 'ai_summary', 'freshness', 'disclaimer']
REQUIRED_IDENTITY = ['ticker', 'as_of', 'report_stamp']
REQUIRED_FRESHNESS = [
    'report_as_of', 'market_data_as_of', 'market_data_fetched_at',
    'ai_snapshot_as_of', 'snapshot_note', 'assumptions_version',
    'assumptions_checked', 'no_refresh_note']
