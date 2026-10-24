"""Explicit model-scoped quota telemetry and pacing regression."""
import json
from datetime import datetime, timezone

import ai_extract
import ai_provider
import data_utils
import refresh_reports
from report_store import write_json


def test_groq_preflight_reports_tokens_and_requests_separately(tmp_path, monkeypatch):
    monkeypatch.setenv('AI_PROVIDER', 'groq')
    monkeypatch.setenv('GROQ_API_KEY', 'synthetic')
    monkeypatch.setenv('GROQ_MODEL', 'openai/gpt-oss-20b')
    for key in ('GROQ_RPD', 'GROQ_RPM', 'GROQ_TPM', 'GROQ_TPD'):
        monkeypatch.delenv(key, raising=False)
    write_json(tmp_path / 'state/api-usage.json', {
        'groq:openai/gpt-oss-20b:2026-10-24': {'requests': 164, 'tokens': 196829},
        'groq:openai/gpt-oss-120b:2026-10-24': {'requests': 42, 'tokens': 100000},
    })
    chosen, plan = refresh_reports.ai_budget(
        ['V', 'VRTX'], {'reports': []}, tmp_path,
        datetime(2026, 10, 24, 4, tzinfo=timezone.utc))
    assert chosen == ['V', 'VRTX']
    assert plan['model'] == 'openai/gpt-oss-20b'
    assert plan['request_cap'] == 1000
    assert plan['token_cap'] == 200000
    assert plan['remaining_requests'] == 836
    assert plan['remaining_tokens'] == 3171
    assert plan['quota_day_utc'] == '2026-10-24'


def test_groq_requests_do_not_use_a_second_legacy_sleep(tmp_path, monkeypatch):
    monkeypatch.setenv('AI_PROVIDER', 'groq')
    monkeypatch.setattr(data_utils, 'DATA', tmp_path)
    monkeypatch.setattr(ai_extract.time, 'sleep',
                        lambda seconds: (_ for _ in ()).throw(AssertionError('double throttle')))
    calls = []
    def generate(prompt, **kwargs):
        calls.append(prompt)
        return {'text': json.dumps({'ticker': 'V',
                **{key: [] for key in ai_extract.KEYS},
                'irrelevant': [{'headline': 'Question about Visa', 'reason': 'No factual event'}]})}
    monkeypatch.setattr(ai_provider, 'generate_json', generate)
    result = ai_extract.call_gemini([{'headline': 'Question about Visa'}], 'V')
    assert len(calls) == 1
    assert result['irrelevant'][0]['headline'] == 'Question about Visa'
    assert not (tmp_path / '.last-ai-call').exists()
