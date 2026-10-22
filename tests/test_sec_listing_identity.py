"""Exchange-qualified symbols must never resolve to a different US issuer."""
import pytest

import edgar


@pytest.mark.parametrize('symbol,expected', [('MG.TO', '749098'), ('CNQ.TO', '1017413'), ('MG', '1436126')])
def test_verified_dual_listing_alias_preserves_issuer(monkeypatch, symbol, expected):
    monkeypatch.delenv('JSOSIF_SEC_CACHE', raising=False)
    monkeypatch.setattr(edgar, 'fetch', lambda url: {
        '0': {'ticker': 'MG', 'cik_str': 1436126, 'title': 'Mistras Group, Inc.'},
        '1': {'ticker': 'MGA', 'cik_str': 749098, 'title': 'MAGNA INTERNATIONAL INC'},
        '2': {'ticker': 'CNQ', 'cik_str': 1017413, 'title': 'CANADIAN NATURAL RESOURCES Ltd'},
    })
    assert edgar.resolve_cik(symbol) == expected


@pytest.mark.parametrize('symbol', ['JWEL.TO', 'ATD.TO', 'UNVERIFIED.TO', 'MC.PA'])
def test_unverified_foreign_mapping_is_unavailable_without_querying_another_issuer(monkeypatch, symbol):
    def unexpected_fetch(url):
        pytest.fail('Unverified foreign symbols must not query a guessed US issuer')

    monkeypatch.setattr(edgar, 'fetch', unexpected_fetch)
    assert edgar.resolve_cik(symbol) is None


def test_reused_alias_with_a_different_cik_is_not_accepted(monkeypatch):
    monkeypatch.delenv('JSOSIF_SEC_CACHE', raising=False)
    monkeypatch.setattr(edgar, 'fetch', lambda url: {'0': {'ticker': 'MGA', 'cik_str': 1436126}})
    assert edgar.resolve_cik('MG.TO') is None


TICKERS = {'0': {'ticker': 'CSCO', 'cik_str': 858877, 'title': 'CISCO SYSTEMS'}}


@pytest.mark.parametrize('content', ['{"0": {"ticker": "CS', '', '[]'])
def test_corrupt_ticker_cache_is_refetched_and_replaced(monkeypatch, tmp_path, content):
    cache = tmp_path / 'state' / 'sec-tickers.json'
    cache.parent.mkdir()
    cache.write_text(content)
    monkeypatch.setenv('JSOSIF_SEC_CACHE', str(cache))
    calls = []
    monkeypatch.setattr(edgar, 'fetch', lambda url: calls.append(url) or TICKERS)
    assert edgar.resolve_cik('CSCO') == '858877'
    assert len(calls) == 1
    import json
    assert json.loads(cache.read_text()) == TICKERS
    assert not list(cache.parent.glob('*.tmp'))
    # The repaired cache is then used without another request.
    assert edgar.resolve_cik('CSCO') == '858877' and len(calls) == 1
