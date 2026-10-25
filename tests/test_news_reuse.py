"""Exact, integrity-verified news-decision reuse does not silently invent coverage."""
import json
from pathlib import Path

import pytest

from ai_extract import extract
from news_reuse import prior_decisions
from report_store import digest


def rss(title='Will Visa acquire a competitor?', *, link='https://example.test/v'):
    return {'headline': title, 'source': 'Synthetic publisher',
            'link': link, 'pubDate': 'Fri, 23 Oct 2026 12:00:00 GMT'}


def prior_archive(root, monkeypatch, *, date='2026-10-24', ticker='V',
                  category='catalysts', status='ready'):
    from news_reuse import _verified_sources
    folder = root / 'archive' / 'synthetic-run' / ticker
    sources = folder / 'sources'
    sources.mkdir(parents=True, exist_ok=True)
    prefix = ticker.lower()
    news = rss()
    (sources / f'{prefix}-rss-items.json').write_text(json.dumps([news]))
    classified = {
        'headline': news['headline'], 'summary': 'Synthetic headline context.',
        'impact': 'medium', 'horizon': 'short', 'confidence': .75,
        'event_type': 'acquisition', 'sentiment': 'neutral',
        'extraction_method': 'ai',
    }
    ai = {'ticker': ticker, 'as_of': date, 'fetch_status': {'status': 'ok'},
          'extraction_stats': {'unknown': 0},
          'tailwinds': [], 'headwinds': [], 'catalysts': [],
          'risks': [], 'irrelevant': [], 'models_used': ['openai/gpt-oss-20b']}
    ai[category].append(classified)
    (sources / f'{prefix}-ai-intel.json').write_text(json.dumps(ai))
    entry = {
        'report_id': f'synthetic-run/{ticker}', 'ticker': ticker,
        'as_of': date, 'generated_at': date + 'T20:00:00+00:00',
        'quality': status,
        'json': f'archive/synthetic-run/{ticker}/{ticker}-intelligence-20261024.json',
        'source_sha256': {
            'rss-items': digest(sources / f'{prefix}-rss-items.json'),
            'ai-intel': digest(sources / f'{prefix}-ai-intel.json'),
        },
    }
    # The actual report contract is checked in verified_report_files. Separate
    # source-hash checks remain real in these focused tests.
    monkeypatch.setattr('news_reuse.verified_report_files', lambda root, entry: {'json': folder / 'report.json'})
    return entry, folder


def test_prior_verified_ai_result_can_be_reused_without_provider_request(tmp_path, monkeypatch):
    entry, folder = prior_archive(tmp_path, monkeypatch)
    cache = prior_decisions(tmp_path, [entry], 'V', '2026-10-25')
    assert len(cache['items']) == 1
    assert cache['source_models'] == ['openai/gpt-oss-20b']
    def never(*args):
        pytest.fail('Same source headline must not generate a new API call')
    data = extract([rss()], 'V', never, as_of='2026-10-25', cached_decisions=cache)
    assert data['extraction_stats'] == {'unique_headlines': 1, 'rule': 0, 'ai': 1, 'unknown': 0}
    assert data['catalysts'][0]['reuse_origin'] == 'verified_prior_archive'
    assert data['catalysts'][0]['reuse_as_of'] == '2026-10-24'
    assert data['ai_reuse']['reused_headlines'] == 1
    assert not data['unclassified']
    assert 'models_used' not in data  # Previous model was not invoked today.


def test_changed_publication_link_never_reuses_an_old_classification(tmp_path, monkeypatch):
    entry, _ = prior_archive(tmp_path, monkeypatch)
    cache = prior_decisions(tmp_path, [entry], 'V', '2026-10-25')
    changed = rss(link='https://example.test/edited-article')
    data = extract([changed], 'V', as_of='2026-10-25', cached_decisions=cache)
    assert data['extraction_stats']['unknown'] == 1
    assert 'ai_reuse' not in data


def test_tampered_or_undigested_sources_cannot_be_reused(tmp_path, monkeypatch):
    entry, folder = prior_archive(tmp_path, monkeypatch)
    path = folder / 'sources/v-ai-intel.json'
    path.write_text(path.read_text().replace('Synthetic headline context.', 'Altered text'))
    assert prior_decisions(tmp_path, [entry], 'V', '2026-10-25') is None
    entry['source_sha256'] = {}
    assert prior_decisions(tmp_path, [entry], 'V', '2026-10-25') is None


def test_expired_or_degraded_cache_remains_disabled(tmp_path, monkeypatch):
    entry, _ = prior_archive(tmp_path, monkeypatch)
    assert prior_decisions(tmp_path, [entry], 'V', '2026-10-27') is None
    assert prior_decisions(tmp_path, [entry], 'MSFT', '2026-10-25') is None
    entry['quality'] = 'degraded'
    assert prior_decisions(tmp_path, [entry], 'V', '2026-10-25') is None


def test_rule_improvements_override_older_ai_decisions(tmp_path, monkeypatch):
    entry, folder = prior_archive(tmp_path, monkeypatch)
    original = rss('Visa (NYSE:V) Stock Jumps 1.6%')
    ai_path = folder / 'sources/v-ai-intel.json'
    rss_path = folder / 'sources/v-rss-items.json'
    older = json.loads(ai_path.read_text())
    older['catalysts'][0]['headline'] = original['headline']
    rss_path.write_text(json.dumps([original]))
    ai_path.write_text(json.dumps(older))
    entry['source_sha256'] = {
        'rss-items': digest(rss_path), 'ai-intel': digest(ai_path)}
    cache = prior_decisions(tmp_path, [entry], 'V', '2026-10-25')
    assert cache is not None
    data = extract([original], 'V', as_of='2026-10-25', cached_decisions=cache)
    assert data['extraction_stats']['rule'] == 1
    assert data['extraction_stats']['ai'] == 0
    assert data['tailwinds'][0]['extraction_method'] == 'rule'


def test_cache_ignores_invalid_cached_payload_fields():
    news = rss()
    cache = {
        'ticker': 'V', 'source_as_of': '2026-10-24', 'source_report_id': 'x/V',
        'items': [{'headline': news['headline'], 'pubDate': news['pubDate'],
                   'link': news['link'], 'category': 'catalysts',
                   'decision': {'summary': 'Invalid', 'impact': 'extreme', 'horizon': 'short',
                                'confidence': 10, 'event_type': 'acquisition',
                                'sentiment': 'neutral'}}],
    }
    result = extract([news], 'V', as_of='2026-10-25', cached_decisions=cache)
    assert result['extraction_stats']['unknown'] == 1
    assert 'ai_reuse' not in result
