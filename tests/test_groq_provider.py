import io
import json
from urllib.error import HTTPError

import pytest
import groq_provider as groq
from report_store import read_json


@pytest.fixture
def setup(monkeypatch, tmp_path):
    monkeypatch.setenv('GROQ_API_KEY', 'synthetic-test-key')
    monkeypatch.setenv('JSOSIF_API_USAGE_PATH', str(tmp_path / 'state/api-usage.json'))
    monkeypatch.delenv('JSOSIF_PERSIST_API_USAGE', raising=False)
    for name in ('RPD', 'RPM', 'TPD', 'TPM'):
        monkeypatch.delenv('GROQ_' + name, raising=False)
    return tmp_path / 'state/api-usage.json'


def response():
    return io.BytesIO(json.dumps({'choices': [{'message': {'content': '{"status":"ok"}'}}],
                                'usage': {'total_tokens': 24}}).encode())


def test_endpoint_contract_and_durable_reservation(setup):
    def open_request(request, timeout):
        assert request.full_url == 'https://api.groq.com/openai/v1/chat/completions'
        assert request.get_header('Authorization') == 'Bearer synthetic-test-key'
        assert timeout == 60
        body = json.loads(request.data)
        assert body['response_format'] == {'type': 'json_object'}
        assert body['max_completion_tokens'] == 1600
        assert any(isinstance(v, dict) and v.get('requests') == 1
                   for v in read_json(setup, {}).values())
        return response()
    assert groq.generate_json('Return JSON', opener=open_request, sleep=lambda _: None)['usage']['total_tokens'] == 24
    assert 'synthetic-test-key' not in setup.read_text()
    assert sum(v['tokens'] for v in read_json(setup, {}).values() if isinstance(v, dict)) == 24


def test_daily_token_cap_blocks_http(setup, monkeypatch):
    monkeypatch.setenv('GROQ_TPD', '1')
    with pytest.raises(groq.GroqError, match='daily budget'):
        groq.generate_json('JSON', opener=lambda *a, **kw: pytest.fail('unexpected HTTP'))


def test_long_server_retry_is_persisted_without_early_retry(setup):
    calls = []
    def fail(request, **kwargs):
        calls.append(request)
        raise HTTPError(request.full_url, 429, 'private response', {'retry-after': '300'}, None)
    with pytest.raises(groq.GroqError, match='HTTP 429'):
        groq.generate_json('JSON', opener=fail, sleep=lambda _: None)
    assert len(calls) == 1
    assert read_json(setup, {})['groq_next_request_at'] > groq.time.time() + 290
    assert 'private response' not in setup.read_text()


def test_auth_failure_not_retried_or_exposed(setup):
    def fail(request, **kwargs):
        raise HTTPError(request.full_url, 401, 'synthetic-test-key', {}, None)
    with pytest.raises(groq.GroqError, match='HTTP 401') as error:
        groq.generate_json('JSON', opener=fail, sleep=lambda _: pytest.fail('retry'))
    assert 'synthetic-test-key' not in str(error.value)


def test_explicit_groq_never_uses_google_key(monkeypatch):
    from ai_provider import generate_json
    monkeypatch.setenv('AI_PROVIDER', 'groq')
    monkeypatch.setenv('GEMINI_API_KEY', 'synthetic-google-key')
    monkeypatch.delenv('GROQ_API_KEY', raising=False)
    monkeypatch.delenv('Grop_ai_API', raising=False)
    with pytest.raises(groq.GroqError, match='not configured'):
        generate_json('JSON')


def test_retry_counts_each_attempt_and_honors_retry_after(setup):
    calls, delays = [], []
    def open_request(request, **kwargs):
        calls.append(request)
        if len(calls) == 1:
            raise HTTPError(request.full_url, 429, 'limited', {'retry-after': '2'}, None)
        return response()
    assert groq.generate_json('JSON', opener=open_request, sleep=delays.append)['text']
    assert len(calls) == 2
    assert 2 in delays
    assert sum(v['requests'] for v in read_json(setup, {}).values() if isinstance(v, dict)) == 2


def test_reservation_push_failure_prevents_http(setup, monkeypatch):
    import report_store
    monkeypatch.setenv('JSOSIF_PERSIST_API_USAGE', '1')
    def fail(*args, **kwargs):
        raise RuntimeError('Persistence failed')
    monkeypatch.setattr(report_store, 'persist', fail)
    with pytest.raises(RuntimeError, match='Persistence failed'):
        groq.generate_json('JSON', opener=lambda *a, **kw: pytest.fail('unexpected HTTP'))


def test_daily_request_cap_prevents_another_attempt(setup, monkeypatch):
    monkeypatch.setenv('GROQ_RPD', '1')
    groq.generate_json('JSON', opener=lambda *a, **kw: response(), sleep=lambda _: None)
    with pytest.raises(groq.GroqError, match='daily budget'):
        groq.generate_json('JSON', opener=lambda *a, **kw: pytest.fail('unexpected HTTP'))
