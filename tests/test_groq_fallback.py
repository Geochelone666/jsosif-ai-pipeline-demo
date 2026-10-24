"""Backup-model failover is explicit and preserves evidence / provider boundaries."""
import json

import pytest

import ai_extract
import ai_provider
import data_utils
import groq_provider
from groq_provider import GroqError


@pytest.fixture
def configured(monkeypatch):
    monkeypatch.setenv('AI_PROVIDER', 'groq')
    monkeypatch.setenv('GROQ_MODEL', 'openai/gpt-oss-20b')
    monkeypatch.delenv('GROQ_FALLBACK_MODEL', raising=False)


@pytest.mark.parametrize('kind', ['tokens', 'requests'])
def test_opt_in_fallback_uses_another_model_only_after_local_cap(configured, monkeypatch, kind):
    monkeypatch.setenv('GROQ_FALLBACK_MODEL', 'openai/gpt-oss-120b')
    tried = []

    def fake(prompt, model, **kwargs):
        tried.append((model, kwargs))
        if len(tried) == 1:
            raise GroqError('Groq application daily budget exhausted (' + kind + ')',
                            budget_kind=kind)
        return {'model': model, 'text': '{"ticker":"V"}'}

    monkeypatch.setattr(groq_provider, 'generate_json', fake)
    answer = ai_provider.generate_json('synthetic', schema={'type': 'object'})
    assert answer['model'] == 'openai/gpt-oss-120b'
    assert [model for model, _ in tried] == [
        'openai/gpt-oss-20b', 'openai/gpt-oss-120b']
    assert tried[0][1] == tried[1][1]


@pytest.mark.parametrize('failure', [
    GroqError('Provider HTTP 429', status=429),
    GroqError('Permission denied', status=401),
    GroqError('Schema validation', status=400, provider_code='json_validate_failed'),
    GroqError('Connection failed'),
])
def test_remote_errors_never_trigger_model_fallback(configured, monkeypatch, failure):
    monkeypatch.setenv('GROQ_FALLBACK_MODEL', 'openai/gpt-oss-120b')
    calls = []

    def fail(*args, **kwargs):
        calls.append(1)
        raise failure

    monkeypatch.setattr(groq_provider, 'generate_json', fail)
    with pytest.raises(GroqError):
        ai_provider.generate_json('synthetic')
    assert len(calls) == 1


def test_no_fallback_without_explicit_configuration(configured, monkeypatch):
    calls = []

    def fail(*args, **kwargs):
        calls.append(1)
        raise GroqError('daily budget exhausted', budget_kind='tokens')

    monkeypatch.setattr(groq_provider, 'generate_json', fail)
    with pytest.raises(GroqError):
        ai_provider.generate_json('synthetic')
    assert len(calls) == 1


@pytest.mark.parametrize('backup', ['invalid', 'openai/gpt-oss-20b', ''])
def test_invalid_or_same_model_does_not_retry(configured, monkeypatch, backup):
    monkeypatch.setenv('GROQ_FALLBACK_MODEL', backup)
    calls = []

    def fail(*args, **kwargs):
        calls.append(1)
        raise GroqError('daily budget exhausted', budget_kind='tokens')

    monkeypatch.setattr(groq_provider, 'generate_json', fail)
    with pytest.raises(GroqError):
        ai_provider.generate_json('synthetic')
    assert len(calls) == 1


def test_actual_model_provenance_survives_multi_batch_classification(configured, monkeypatch, tmp_path):
    monkeypatch.setattr(data_utils, 'DATA', tmp_path)
    monkeypatch.setattr(ai_extract.time, 'sleep', lambda *args: None)
    calls = []

    def reply(prompt, **kwargs):
        names = [entry['headline'] for entry in json.loads(prompt.split('News: ', 1)[1])]
        calls.append(len(names))
        used = 'openai/gpt-oss-20b' if len(calls) == 1 else 'openai/gpt-oss-120b'
        return {'model': used, 'text': json.dumps({'ticker': 'V',
                **{key: [] for key in ai_extract.KEYS},
                'irrelevant': [{'headline': h, 'reason': 'Not a company event'} for h in names]})}

    monkeypatch.setattr(ai_provider, 'generate_json', reply)
    result = ai_extract.call_gemini(
        [{'headline': f'Broad market question {i}'} for i in range(6)], 'V')
    assert calls == [5, 1]
    assert result['models_used'] == ['openai/gpt-oss-20b', 'openai/gpt-oss-120b']
    assert len(result['irrelevant']) == 6


def test_extracted_model_identity_is_recorded_without_claiming_coverage():
    item = {'headline': 'Broad market discussion'}
    def model_reply(*args):
        return {'ticker': 'V', **{key: [] for key in ai_extract.KEYS},
                'models_used': ['openai/gpt-oss-120b']}
    result = ai_extract.extract([item], 'V', model_reply, as_of='2026-10-23')
    assert result['models_used'] == ['openai/gpt-oss-120b']
    assert result['extraction_stats']['unknown'] == 1
