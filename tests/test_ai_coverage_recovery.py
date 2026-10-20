"""Omitted news gets one bounded retry without hiding unresolved evidence."""
import pytest

from ai_extract import KEYS, extract
from groq_provider import GroqError


def payload(ticker, headlines):
    return {'ticker': ticker, **{key: [] for key in KEYS},
            'irrelevant': [{'headline': h, 'reason': 'No target-company event'} for h in headlines]}


def test_retry_only_missing_inputs_and_keep_accepted_decisions():
    calls = []

    def ai(items, ticker):
        headlines = [item['headline'] for item in items]
        calls.append(headlines)
        return payload(ticker, headlines[:1])

    result = extract([{'headline': 'First unclear story'}, {'headline': 'Second unclear story'}], 'XYL', ai)
    assert calls == [['First unclear story', 'Second unclear story'], ['Second unclear story']]
    assert result['extraction_stats'] == {'unique_headlines': 2, 'rule': 0, 'ai': 0, 'unknown': 0, 'irrelevant': 2}
    assert result['unclassified'] == []
    assert result['ai_coverage_retry'] == {'requested': 1, 'unresolved': 0}


def test_persistent_omission_stops_and_preserves_unknown():
    calls = []

    def ai(items, ticker):
        calls.append(items)
        return payload(ticker, [])

    result = extract([{'headline': 'Unclear story'}], 'AMTM', ai)
    assert len(calls) == 2
    assert result['extraction_stats']['unknown'] == 1
    assert result['ai_coverage_retry']['unresolved'] == 1


@pytest.mark.parametrize('wrong_ticker', [False, True])
def test_retry_failure_preserves_prior_decisions_and_diagnostic(wrong_ticker):
    calls = []

    def ai(items, ticker):
        calls.append(items)
        if len(calls) == 1:
            return payload(ticker, [items[0]['headline']])
        if wrong_ticker:
            return payload('OTHER', [items[0]['headline']])
        raise GroqError('Daily budget exhausted')

    result = extract([{'headline': 'First story'}, {'headline': 'Second story'}], 'XYL', ai)
    assert len(calls) == 2
    assert len(result['irrelevant']) == 1
    assert result['extraction_stats']['unknown'] == 1
    assert 'error' in result and 'failure' in result


def test_provider_error_does_not_trigger_coverage_retry():
    calls = []

    def ai(items, ticker):
        calls.append(items)
        raise GroqError('Rate limited', status=429)

    result = extract([{'headline': 'Unclear story'}], 'XYL', ai)
    assert len(calls) == 1
    assert result['failure']['status'] == 429
