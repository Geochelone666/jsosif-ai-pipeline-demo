"""Offline RSS boundary and graceful-failure regressions."""
import io
import json
import socket
import urllib.error

import pytest

import ai_extract as ai
import data_utils

EMPTY = b'<rss><channel/></rss>'
NEWS = b'''<rss><channel><item><title>Nvidia stock gains - Example</title>
<link>https://example.com/news</link><pubDate>Fri, 02 Oct 2026 12:00:00 GMT</pubDate>
</item></channel></rss>'''


@pytest.mark.parametrize('exc,category,retryable,attempts', [
    (urllib.error.URLError('DNS unavailable'), 'dns_or_connection', True, 3),
    (ConnectionResetError('reset'), 'dns_or_connection', True, 3),
    (socket.timeout('timed out'), 'timeout', True, 3),
    (urllib.error.URLError(socket.timeout('timed out')), 'timeout', True, 3),
    (urllib.error.HTTPError('https://news.google.com', 503, 'Unavailable', {}, None), 'http_error', True, 3),
    (urllib.error.HTTPError('https://news.google.com', 429, 'Too many requests', {}, None), 'http_error', True, 3),
    (urllib.error.HTTPError('https://news.google.com', 404, 'Not found', {}, None), 'http_error', False, 1),
])
def test_failures(monkeypatch, exc, category, retryable, attempts):
    calls, delays = [], []
    def fail(req, timeout):
        calls.append((req.full_url, timeout))
        raise exc
    monkeypatch.setattr(ai.urllib.request, 'urlopen', fail)
    with pytest.raises(ai.RSSFetchError) as caught:
        ai.fetch_rss('Nvidia stock', max_attempts=3, sleep=delays.append)
    error = caught.value
    assert (error.category, error.retryable, error.attempts) == (category, retryable, attempts)
    assert error.detail == str(exc)
    assert error.__cause__ is exc
    assert len(calls) == attempts
    assert all(timeout == 30 for _, timeout in calls)
    assert delays == ([0.5, 1.0] if retryable else [])


def test_malformed_xml(monkeypatch):
    calls = []
    def respond(*args, **kwargs):
        calls.append(1)
        return io.BytesIO(b'<rss>')
    monkeypatch.setattr(ai.urllib.request, 'urlopen', respond)
    with pytest.raises(ai.RSSFetchError) as caught:
        ai.fetch_rss('test', sleep=lambda _: pytest.fail('must not sleep'))
    assert (caught.value.category, caught.value.retryable, caught.value.attempts) == ('malformed_xml', False, 1)
    assert len(calls) == 1


@pytest.mark.parametrize('xml,count', [(EMPTY, 0), (NEWS, 1)])
def test_success(monkeypatch, xml, count):
    monkeypatch.setattr(ai.urllib.request, 'urlopen', lambda *a, **kw: io.BytesIO(xml))
    items, status = ai.fetch_rss('Nvidia stock', sleep=lambda _: pytest.fail('must not sleep'))
    assert status == dict(stage='rss_fetch', status='ok', category=None, retryable=False,
                          attempts=1, url='https://news.google.com/rss/search?q=Nvidia%20stock&hl=en-US&gl=US&ceid=US:en', items=count)
    assert len(items) == count
    if count:
        assert items[0] == dict(headline='Nvidia stock gains', source='Example',
                               link='https://example.com/news', pubDate='Fri, 02 Oct 2026 12:00:00 GMT')


def test_recovery(monkeypatch):
    calls, delays = [], []
    def respond(*args, **kwargs):
        calls.append(1)
        if len(calls) < 2:
            raise socket.timeout('temporary')
        return io.BytesIO(NEWS)
    monkeypatch.setattr(ai.urllib.request, 'urlopen', respond)
    items, status = ai.fetch_rss('test', sleep=delays.append)
    assert len(items) == 1
    assert status['status'] == 'ok' and status['attempts'] == 2
    assert delays == [0.5]


@pytest.mark.parametrize('failed', [True, False])
def test_main_writes_status(monkeypatch, tmp_path, capsys, failed):
    def respond(*args, **kwargs):
        if failed:
            raise socket.timeout('raw technical timeout')
        return io.BytesIO(EMPTY)
    monkeypatch.setattr(ai.urllib.request, 'urlopen', respond)
    fetch = ai.fetch_rss
    monkeypatch.setattr(ai, 'fetch_rss', lambda *a, **kw: fetch(*a, **kw, sleep=lambda _: None))
    monkeypatch.setattr(data_utils, 'DATA', tmp_path)
    monkeypatch.setattr(data_utils, 'ticker_arg', lambda: 'CNQ.TO')
    monkeypatch.setattr(ai, 'call_gemini', lambda *a: pytest.fail('empty news must not call AI'))
    ai.main()
    data = json.loads((tmp_path / data_utils.ticker_file('CNQ.TO', 'ai-intel.json')).read_text())
    assert json.loads((tmp_path / data_utils.ticker_file('CNQ.TO', 'rss-items.json')).read_text()) == []
    assert data['fetch_status']['status'] == ('failed' if failed else 'ok')
    assert data['fetch_status']['items'] == 0
    stderr = capsys.readouterr().err
    if failed:
        assert data['fetch_status']['attempts'] == 3
        assert data['fetch_status']['category'] == 'timeout'
        assert 'Connection timed out' in data['error'] and '3 attempts' in data['error']
        assert 'quantitative metrics unaffected' in data['error']
        assert 'raw technical timeout' not in data['error']
        assert data['error'] in stderr
    else:
        assert 'error' not in data
        assert stderr == ''


@pytest.mark.parametrize('max_attempts', [1, 2, 4])
def test_attempt_budget(monkeypatch, max_attempts):
    calls, delays = [], []
    def fail(*args, **kwargs):
        calls.append(1)
        raise urllib.error.URLError('offline')
    monkeypatch.setattr(ai.urllib.request, 'urlopen', fail)
    with pytest.raises(ai.RSSFetchError) as caught:
        ai.fetch_rss('test', max_attempts=max_attempts, sleep=delays.append)
    assert caught.value.attempts == len(calls) == max_attempts
    assert delays == [0.5 * 2 ** i for i in range(max_attempts - 1)]


@pytest.mark.parametrize('max_attempts', [0, -1, True, 1.5])
def test_invalid_attempt_budget(monkeypatch, max_attempts):
    monkeypatch.setattr(ai.urllib.request, 'urlopen', lambda *a, **kw: pytest.fail('must not fetch'))
    with pytest.raises(ValueError, match='positive integer'):
        ai.fetch_rss('test', max_attempts=max_attempts)

