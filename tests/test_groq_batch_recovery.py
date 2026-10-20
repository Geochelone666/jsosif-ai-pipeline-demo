"""A failed structured batch can shrink without relaxing identity or quota guards."""
import json

import pytest

import ai_extract
import ai_provider
import data_utils
from groq_provider import GroqError


@pytest.fixture
def transport(tmp_path, monkeypatch):
    monkeypatch.setenv('AI_PROVIDER', 'groq')
    monkeypatch.setattr(data_utils, 'DATA', tmp_path)
    monkeypatch.setattr('time.sleep', lambda seconds: None)


@pytest.mark.parametrize('maximum,calls_expected', [(3, [5, 3, 2, 1]), (2, [5, 3, 2, 1, 2, 1])])
def test_failed_large_batch_shrinks_and_preserves_every_decision(transport, monkeypatch, maximum, calls_expected):
    calls = []

    def generate(prompt, schema):
        headlines = [item['headline'] for item in json.loads(prompt.split('News: ', 1)[1])]
        calls.append(len(headlines))
        assert schema['properties']['ticker']['enum'] == ['V']
        if len(headlines) > maximum:
            raise GroqError('Invalid structured output', status=400, provider_code='json_validate_failed')
        return {'text': json.dumps({'ticker': 'V', **{key: [] for key in ai_extract.KEYS},
                'irrelevant': [{'headline': headline, 'reason': 'No target-company event'} for headline in headlines]})}

    monkeypatch.setattr(ai_provider, 'generate_json', generate)
    result = ai_extract.call_gemini([{'headline': f'Synthetic headline {n}'} for n in range(6)], 'V')
    assert calls == calls_expected
    assert [item['headline'] for item in result['irrelevant']] == [f'Synthetic headline {n}' for n in range(6)]


@pytest.mark.parametrize('status,code,count', [
    (400, 'json_validate_failed', 1),
    (400, 'invalid_request_error', 5),
    (401, 'invalid_api_key', 5),
    (429, 'rate_limit_exceeded', 5),
    (None, None, 5),
])
def test_singleton_and_non_generation_errors_do_not_fan_out(transport, monkeypatch, status, code, count):
    calls = []

    def fail(*args, **kwargs):
        calls.append(True)
        raise GroqError('Synthetic failure', status=status, provider_code=code)

    monkeypatch.setattr(ai_provider, 'generate_json', fail)
    with pytest.raises(GroqError):
        ai_extract.call_gemini([{'headline': f'Headline {n}'} for n in range(count)], 'V')
    assert len(calls) == 1


def test_persistent_generation_failure_stops_at_one_headline(transport, monkeypatch):
    sizes = []

    def fail(prompt, **kwargs):
        sizes.append(len(json.loads(prompt.split('News: ', 1)[1])))
        raise GroqError('Invalid structured output', status=400, provider_code='json_validate_failed')

    monkeypatch.setattr(ai_provider, 'generate_json', fail)
    with pytest.raises(GroqError):
        ai_extract.call_gemini([{'headline': str(n)} for n in range(5)], 'V')
    assert sizes == [5, 3, 2, 1]


def test_recovered_batches_still_reject_a_different_listing(transport, monkeypatch):
    def generate(prompt, **kwargs):
        if len(json.loads(prompt.split('News: ', 1)[1])) == 5:
            raise GroqError('Invalid structured output', status=400, provider_code='json_validate_failed')
        return {'text': json.dumps({'ticker': 'VISA'})}

    monkeypatch.setattr(ai_provider, 'generate_json', generate)
    with pytest.raises(ValueError, match='different ticker'):
        ai_extract.call_gemini([{'headline': str(n)} for n in range(5)], 'V')
