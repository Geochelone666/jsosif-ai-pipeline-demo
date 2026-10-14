"""Shared v1 email snapshot contract, keeping daily payload structure stable.

Identity carries ticker, YYYY-MM-DD as_of and YYYYMMDD report_stamp. Quant
rows carry metric, string-or-None value, ok/missing availability and nullable
reason. AI summaries carry status and a mapping of section names to text.
Freshness records existing timestamps and assumptions, with no_refresh_note
fixed to '邮件生成不刷新任何数据'. Validation must never fetch or refresh data.
"""
from datetime import date
import re

CONTRACT_VERSION = '1.0'
REQUIRED_TOP_LEVEL = [
    'contract_version', 'identity', 'quant', 'ai_summary', 'freshness', 'disclaimer']
REQUIRED_IDENTITY = ['ticker', 'as_of', 'report_stamp']
REQUIRED_FRESHNESS = [
    'report_as_of', 'market_data_as_of', 'market_data_fetched_at',
    'ai_snapshot_as_of', 'snapshot_note', 'assumptions_version',
    'assumptions_checked', 'no_refresh_note']


def _nonblank(value):
    return isinstance(value, str) and bool(value.strip())


def _required(mapping, fields, path, errors):
    for field in fields:
        if field not in mapping:
            errors.append(f'{path}.{field} is required')


def validate_snapshot(payload) -> list[str]:
    """Return field-specific v1 schema errors so malformed emails can be blocked.

    This is a pure structural check: it neither changes the payload nor refreshes
    data. Extra keys are allowed; timestamps other than identity.as_of remain
    strings because absent source dates can be represented by explanatory text.
    """
    if not isinstance(payload, dict):
        return ['snapshot must be a dict']
    errors = []
    _required(payload, REQUIRED_TOP_LEVEL, 'snapshot', errors)
    if payload.get('contract_version') != CONTRACT_VERSION:
        errors.append(f'contract_version must equal {CONTRACT_VERSION!r}')

    identity = payload.get('identity')
    if not isinstance(identity, dict):
        errors.append('identity must be a dict')
    else:
        _required(identity, REQUIRED_IDENTITY, 'identity', errors)
        for field in REQUIRED_IDENTITY:
            if not _nonblank(identity.get(field)):
                errors.append(f'identity.{field} must be a nonempty string')
        as_of = identity.get('as_of')
        try:
            if not isinstance(as_of, str) or not re.fullmatch(r'[0-9]{4}-[0-9]{2}-[0-9]{2}', as_of):
                raise ValueError
            date.fromisoformat(as_of)
        except ValueError:
            errors.append('identity.as_of must be a valid YYYY-MM-DD date')

    quant = payload.get('quant')
    if not isinstance(quant, list) or not quant:
        errors.append('quant must be a nonempty list')
    else:
        for index, row in enumerate(quant):
            path = f'quant[{index}]'
            if not isinstance(row, dict):
                errors.append(f'{path} must be a dict')
                continue
            _required(row, ('metric', 'value', 'availability', 'reason'), path, errors)
            if not _nonblank(row.get('metric')):
                errors.append(f'{path}.metric must be a nonempty string')
            for field in ('value', 'reason'):
                if row.get(field) is not None and not isinstance(row[field], str):
                    errors.append(f'{path}.{field} must be a string or None')
            if row.get('availability') not in ('ok', 'missing'):
                errors.append(f'{path}.availability must be ok or missing')
            if row.get('availability') == 'missing' and not _nonblank(row.get('reason')):
                errors.append(f'{path}.reason must be a nonempty string when availability is missing')

    summary = payload.get('ai_summary')
    if not isinstance(summary, dict):
        errors.append('ai_summary must be a dict')
    else:
        if not _nonblank(summary.get('status')):
            errors.append('ai_summary.status must be a nonempty string')
        sections = summary.get('sections')
        if not isinstance(sections, dict):
            errors.append('ai_summary.sections must be a dict')
        elif not all(isinstance(key, str) and isinstance(value, str)
                     for key, value in sections.items()):
            errors.append('ai_summary.sections must map string names to string text')

    freshness = payload.get('freshness')
    if not isinstance(freshness, dict):
        errors.append('freshness must be a dict')
    else:
        _required(freshness, REQUIRED_FRESHNESS, 'freshness', errors)
        for field in REQUIRED_FRESHNESS:
            expected = dict if field == 'assumptions_checked' else str
            if not isinstance(freshness.get(field), expected):
                errors.append(f'freshness.{field} must be a {expected.__name__}')
        if freshness.get('no_refresh_note') != '邮件生成不刷新任何数据':
            errors.append('freshness.no_refresh_note must equal 邮件生成不刷新任何数据')

    if not _nonblank(payload.get('disclaimer')):
        errors.append('disclaimer must be a nonempty string')
    return errors
