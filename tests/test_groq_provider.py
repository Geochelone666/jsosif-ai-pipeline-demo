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


def test_pacing_across_midnight_charges_the_new_application_day(setup, monkeypatch):
    from datetime import datetime, timezone
    from report_store import write_json
    clock = {'now': datetime(2026, 10, 19, 23, 59, 59, tzinfo=timezone.utc).timestamp()}
    write_json(setup, {'groq_next_request_at': clock['now'] + 2})
    monkeypatch.setattr(groq.time, 'time', lambda: clock['now'])
    def wait(seconds):
        clock['now'] += seconds
    groq.generate_json('JSON', opener=lambda *a, **kw: response(), sleep=wait)
    ledger = read_json(setup, {})
    assert 'groq:openai/gpt-oss-20b:2026-10-19' not in ledger
    assert ledger['groq:openai/gpt-oss-20b:2026-10-20']['requests'] == 1


def test_response_persistence_error_does_not_repeat_a_successful_http_call(setup, monkeypatch):
    save = groq.reconcile_usage
    saves, calls = [], []
    def write(path, ledger):
        saves.append(True)
        if len(saves) == 1:
            raise OSError('Synthetic disk failure')
        save(path, ledger)
    monkeypatch.setattr(groq, 'reconcile_usage', write)
    def open_request(*args, **kwargs):
        calls.append(True)
        return response()
    with pytest.raises(OSError, match='disk failure'):
        groq.generate_json('JSON', opener=open_request, sleep=lambda _: None)
    assert len(calls) == 1


@pytest.mark.parametrize('payload', [[], {'choices': []}, {'choices': [None]},
                                     {'choices': [{'message': {'content': '{}'}}], 'usage': None}])
def test_malformed_provider_envelopes_have_safe_errors(setup, payload):
    with pytest.raises(groq.GroqError, match='invalid response'):
        groq.generate_json('JSON', opener=lambda *a, **kw: io.BytesIO(json.dumps(payload).encode()),
                           sleep=lambda _: None)


def test_batching_normalizes_provider_payloads_before_merging(tmp_path, monkeypatch):
    import ai_extract
    import ai_provider
    import data_utils
    monkeypatch.setenv('AI_PROVIDER', 'groq')
    monkeypatch.setattr(data_utils, 'DATA', tmp_path)
    monkeypatch.setattr(ai_extract.time, 'sleep', lambda _: None)
    batches = []
    def generate(prompt, **kwargs):
        news = json.loads(prompt.split('News: ', 1)[1])
        batches.append(len(news))
        payload = {'ticker': 'CSCO', 'tailwinds': [], 'headwinds': [], 'risks': [],
                   'catalysts': [dict(headline=item['headline']) for item in news]}
        return {'text': json.dumps([payload]), 'model': 'synthetic'}
    monkeypatch.setattr(ai_provider, 'generate_json', generate)
    result = ai_extract.call_gemini([{'headline': f'Synthetic headline {i}'} for i in range(11)], 'CSCO')
    assert batches == [5, 5, 1]
    assert len(result['catalysts']) == 11


@pytest.mark.parametrize('summary', [None, {}, [], 42, '', '   '])
def test_malformed_ai_summary_remains_unclassified(summary):
    from ai_extract import extract
    headline = 'Will Cisco rise?'
    item = dict(headline=headline, source='Synthetic', link='https://example.com',
                pubDate='Sun, 18 Oct 2026 12:00:00 GMT')
    def generate(*args):
        return {'ticker': 'CSCO', 'tailwinds': [], 'headwinds': [], 'risks': [],
                'catalysts': [dict(headline=headline, summary=summary, impact='low', horizon='short',
                                   confidence=.5, event_type='earnings', sentiment='neutral')]}
    result = extract([item], 'CSCO', generate, as_of='2026-10-18')
    assert result['extraction_stats']['ai'] == 0
    assert result['extraction_stats']['unknown'] == 1


def test_api_requests_identify_the_application(setup):
    def open_request(request, **kwargs):
        assert request.get_header('User-agent') == 'JSOSIF/1.0'
        return response()
    groq.generate_json('JSON', opener=open_request, sleep=lambda _: None)


@pytest.mark.parametrize('body,expected', [
    (b'error code: 1010', 'edge_policy_1010'),
    (b'{"error":{"code":"invalid_api_key","message":"synthetic-secret"}}', 'invalid_api_key'),
    (b'{"error":{"code":"synthetic-secret"}}', None),
])
def test_safe_provider_error_codes_never_copy_arbitrary_response_content(body, expected):
    assert groq.error_code(io.BytesIO(body)) == expected


def test_model_discovery_exposes_only_known_public_candidates(setup):
    def open_request(request, **kwargs):
        assert request.full_url == 'https://api.groq.com/openai/v1/models'
        assert request.get_method() == 'GET'
        return io.BytesIO(json.dumps({'data': [{'id': 'llama-3.3-70b-versatile'},
                                             {'id': 'private-org-model'}]}).encode())
    assert groq.available_models(opener=open_request) == ['llama-3.3-70b-versatile']


def test_minute_token_budget_checks_the_rolling_window_for_unequal_requests():
    caps = {'RPM': 10, 'TPM': 5000}
    events = [{'at': 0, 'tokens': 1000}, {'at': 12, 'tokens': 4000}]
    # Average-rate spacing would allow another 4000 at t=60, exceeding 5000
    # in the interval (0, 60]. The rolling window must wait until t=72.
    at, active = groq.minute_slot(events, 60, 4000, caps)
    assert at == 72 and active == []


def test_minute_request_budget_waits_for_the_oldest_reservation_to_expire():
    events = [{'at': second, 'tokens': 1} for second in range(10)]
    at, active = groq.minute_slot(events, 10, 1, {'RPM': 10, 'TPM': 5000})
    assert at == 60 and len(active) == 9


def test_successful_token_usage_reconciles_the_rolling_window(setup):
    groq.generate_json('JSON', opener=lambda *a, **kw: response(), sleep=lambda _: None)
    assert read_json(setup, {})['groq_recent_requests'][0]['tokens'] == 24


def test_schema_fixes_the_requested_listing_and_accounts_for_schema_tokens(setup):
    from ai_extract import classification_schema
    schema = classification_schema('CNQ.TO')
    def open_request(request, **kwargs):
        body = json.loads(request.data)
        shape = body['response_format']['json_schema']
        assert body['response_format']['type'] == 'json_schema' and shape['strict']
        assert shape['schema']['properties']['ticker']['enum'] == ['CNQ.TO']
        usage = read_json(setup, {})
        expected = len('JSON'.encode()) + 1800 + len(json.dumps(schema, separators=(',', ':')).encode())
        assert usage['groq_recent_requests'][0]['tokens'] == expected
        return response()
    groq.generate_json('JSON', schema=schema, opener=open_request, sleep=lambda _: None)


def test_actual_usage_waits_for_the_next_checkpoint_instead_of_pushing_twice(setup, monkeypatch):
    import report_store
    reservations = []
    monkeypatch.setenv('JSOSIF_PERSIST_API_USAGE', '1')
    monkeypatch.setattr(report_store, 'persist', lambda *a, **kw: reservations.append(read_json(setup, {})))
    groq.generate_json('JSON', opener=lambda *a, **kw: response(), sleep=lambda _: None)
    assert len(reservations) == 1
    assert reservations[0]['groq_recent_requests'][0]['tokens'] > 24
    assert read_json(setup, {})['groq_recent_requests'][0]['tokens'] == 24


def test_explicit_irrelevance_is_audited_without_inventing_company_events():
    from ai_extract import extract
    headline = 'General Mills mentioned in unrelated market roundup'
    item = {'headline': headline, 'pubDate': 'Mon, 19 Oct 2026 12:00:00 GMT', 'source': 'Fixture'}
    def answer(*args):
        return {'ticker': 'GIS', 'tailwinds': [], 'headwinds': [], 'catalysts': [], 'risks': [],
                'irrelevant': [{'headline': headline, 'reason': 'No company-specific development in the headline'}]}
    result = extract([item], 'GIS', answer, as_of='2026-10-19')
    assert result['extraction_stats']['unknown'] == 0
    assert result['extraction_stats']['irrelevant'] == 1
    assert result['irrelevant'][0]['headline'] == headline
    assert all(not result[name] for name in ('tailwinds','headwinds','catalysts','risks'))


def test_structured_provider_failure_metadata_excludes_error_bodies():
    from ai_extract import extract
    item = {'headline': 'Will Cisco rise?', 'pubDate': 'Mon, 19 Oct 2026 12:00:00 GMT'}
    def failed(*args):
        raise groq.GroqError('Groq HTTP 400; check account limits and retry guidance',
                             status=400, provider_code='json_validate_failed')
    result = extract([item], 'CSCO', failed, as_of='2026-10-19')
    assert result['failure'] == {'type': 'provider', 'status': 400, 'code': 'json_validate_failed'}
    assert result['extraction_stats']['unknown'] == 1


def test_measured_portfolio_and_same_day_recovery_fit_default_local_daily_caps(setup, monkeypatch):
    from datetime import datetime, timezone
    clock = {'now': datetime(2026, 10, 20, 12, tzinfo=timezone.utc).timestamp()}
    monkeypatch.setattr(groq.time, 'time', lambda: clock['now'])
    def wait(seconds):
        clock['now'] += seconds
    def completed(*args, **kwargs):
        return io.BytesIO(json.dumps({'choices': [{'message': {'content': '{}'}}],
                                     'usage': {'total_tokens': 1500}}).encode())
    # 62 calls is the observed pending-headline workload. The synthetic 1500-token
    # response makes two such attempts exceed the former daily application cap.
    for _ in range(62 * 2):
        groq.generate_json('JSON', opener=completed, sleep=wait, attempts=1)
    daily = read_json(setup, {})['groq:openai/gpt-oss-20b:2026-10-20']
    assert daily == {'requests': 124, 'tokens': 186000}
