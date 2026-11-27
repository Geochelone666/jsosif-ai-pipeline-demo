from copy import deepcopy
import json
from pathlib import Path
import socket
import subprocess
import sys

import pytest

import news_evidence as news
from report_store import digest as file_digest, read_json, write_json
from snapshot_emit import emit_frozen_snapshot

STORY = {'headline': 'Company schedules results for December 5', 'source': 'Example publisher',
         'pubDate': 'Fri, 06 Nov 2026 23:30:00 -0500',
         'link': 'https://news.google.com/rss/articles/ABC_def-123?oc=5'}


def prediction(story=STORY, **changes):
    return {**{k: story[k] for k in ('headline', 'source', 'pubDate')}, 'url': story['link'],
            'date': '2026-11-06', 'event_type': 'calendar', 'sentiment': 'neutral',
            'extraction_method': 'rule', 'summary': 'Never copy this private narrative', **changes}


@pytest.fixture
def archive(tmp_path):
    root = tmp_path / 'store'
    entries = []
    for ticker in ('CSCO', 'JPM'):
        folder = Path('archive/synthetic') / ticker
        entry = {'ticker': ticker, 'report_id': 'synthetic/' + ticker, 'as_of': '2026-11-06',
                 'generated_at': '2026-11-07T04:00:00Z', 'quality': 'ready'}
        snapshot = emit_frozen_snapshot(ticker=ticker, as_of=entry['as_of'], quant_metrics={'Close': 100},
                                       ai={'status': 'Available'}, freshness={}, disclaimer='Synthetic fixture')
        snapshot['quality'] = 'ready'
        for kind, raw in [('json', json.dumps(snapshot)), ('md', 'fixture'), ('pdf', '%PDF-1.4 fixture')]:
            relative = folder / f'{ticker}-intelligence-20261106.{kind}'
            path = root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(raw)
            entry[kind] = relative.as_posix()
        entry['sha256'] = {kind: file_digest(root / entry[kind]) for kind in ('json', 'md', 'pdf')}
        source_hashes = {}
        for kind in ('quant', 'info', 'ai-intel', 'rss-items', 'comparables', 'earnings', 'edgar', 'fred'):
            path = root / folder / 'sources' / ('fred.json' if kind == 'fred' else ticker.lower() + '-' + kind + '.json')
            data = ([STORY, STORY] if kind == 'rss-items' else
                    {'ticker': ticker, 'as_of': entry['as_of'], 'catalysts': [prediction()],
                     'api_key': 'secret-fixture-value'} if kind == 'ai-intel' else {})
            write_json(path, data)
            source_hashes[kind] = file_digest(path)
        entry['source_sha256'] = source_hashes
        entries.append(entry)
    write_json(root / 'index.json', {'reports': entries, 'private': 'secret-index-value'})
    return root


def edit_source(root, kind, value, ticker='CSCO', *, rehash=True):
    index = read_json(root / 'index.json')
    entry = next(r for r in index['reports'] if r['ticker'] == ticker)
    path = (root / entry['json']).parent / 'sources' / (ticker.lower() + '-' + kind + '.json')
    write_json(path, value)
    if rehash:
        entry['source_sha256'][kind] = file_digest(path)
        write_json(root / 'index.json', index)
    return path


def build(root, as_of='2026-11-13'):
    return news.build(root, as_of=as_of)


def test_exact_cross_report_dedup_preserves_context_and_never_infers_event_date(archive):
    value = build(archive)
    assert len(value['articles']) == 1 and len(value['reports']) == 2
    article = value['articles'][0]
    assert article['published_at'] == '2026-11-07T04:30:00+00:00'
    assert article['event_date'] is None and article['point_in_time_eligible'] is False
    assert article['url'] == STORY['link'].split('?')[0]
    assert article['publication_age']['age_days'] == 6
    for row in value['reports']:
        ref = row['references'][0]
        assert ref['rss_occurrences'] == 2 and ref['future_relative_to_report'] is True
        assert ref['decision_status'] == 'single_saved_prediction'
        assert 'saved_date_not_confirmed_by_utc_publication' in ref['saved_decisions'][0]['review_flags']
        assert row['snapshot_sha256'] and row['sector_ids']
    assert value['reports'][0]['sector_ids'] != value['reports'][1]['sector_ids']
    assert all(s['integrity'] == 'archived_expected_hash' for s in value['sources'])
    assert value['delivery_ready'] is False and len(value['missing_reports']) == 48
    encoded = news.canonical(value)
    assert all(private not in encoded for private in ('secret-fixture-value', 'secret-index-value', 'private narrative', 'oc=5'))


def test_no_title_only_join_or_invented_prediction(archive):
    wrong = prediction(url='https://example.org/different')
    edit_source(archive, 'ai-intel', {'ticker': 'CSCO', 'as_of': '2026-11-06', 'catalysts': [wrong]})
    row = build(archive)['reports'][0]
    assert row['unmatched_decisions'] == 1
    assert row['unmatched_decisions_by_category'] == {'catalysts': 1}
    assert row['references'][0]['decision_status'] == 'missing'
    assert not row['references'][0]['saved_decisions']


@pytest.mark.parametrize('field,value', [('source', 'Other publisher'), ('pubDate', 'Thu, 05 Nov 2026 12:00:00 GMT'),
                                       ('link', 'https://example.org/different'), ('headline', STORY['headline'] + '!')])
def test_similar_stories_remain_distinct(archive, field, value):
    edit_source(archive, 'rss-items', [STORY, {**STORY, field: value}])
    assert len(build(archive)['articles']) == 2


def test_conflicting_predictions_preserved_without_winner_and_duplicates_counted(archive):
    edit_source(archive, 'ai-intel', {'ticker': 'CSCO', 'as_of': '2026-11-06',
        'catalysts': [prediction(), prediction()], 'headwinds': [prediction(sentiment='positive')]})
    ref = build(archive)['reports'][0]['references'][0]
    assert ref['decision_status'] == 'conflicting' and len(ref['saved_decisions']) == 2
    assert ref['saved_decision_occurrences'] == 3
    assert any('positive_sentiment_in_headwinds' in d['review_flags'] for d in ref['saved_decisions'])


@pytest.mark.parametrize('stamp,status', [(None, 'invalid_or_missing'), ('yesterday', 'invalid_or_missing'),
    ('Fri, 06 Nov 2026 23:30:00', 'timezone_missing'), ('Fri, 06 Nov 2026 23:30:00 -0000', 'timezone_missing')])
def test_missing_timezone_or_date_never_borrows_report_date(stamp, status):
    assert news.publication(stamp) == (None, status)


@pytest.mark.parametrize('url', ['http://example.org/x', 'javascript:alert(1)', 'https://user:secret@example.org/x',
    'https://example.org/x?token=secret', 'https://example.org/x#secret', 'https://127.0.0.1/x',
    'https://localhost/x', 'https://app.local/x', 'https://example.org:abc/x',
    'https://example.org/x\n<script>', 'https://news.google.com/rss/articles/id?key=secret',
    'https://news.google.com/private/path', 'https://example.org/x\\evil'])
def test_unsafe_links_not_emitted(url):
    assert news.public_link(url) is None


def test_unsafe_url_remains_exact_identity_only_and_markdown_escapes_headline(archive):
    story = {**STORY, 'headline': '<script>alert(1)</script> [open](javascript:bad) | **text**',
             'link': 'https://example.org/x?api_key=secret-test-value'}
    edit_source(archive, 'rss-items', [story])
    value = build(archive)
    rendered = news.markdown(value)
    assert '<script>' not in rendered and '[open](' not in rendered
    assert 'secret-test-value' not in news.canonical(value) + rendered
    assert any(a['url'] is None for a in value['articles'])


@pytest.mark.parametrize('kind', ['rss-items', 'ai-intel'])
def test_tampered_tracked_sources_fail_closed(archive, kind):
    edit_source(archive, kind, {}, rehash=False)
    with pytest.raises(ValueError, match='integrity'):
        build(archive)


def test_source_race_after_initial_verification_fails(archive, monkeypatch):
    original = news.verified_report_files
    def race(root, entry):
        result = original(root, entry)
        edit_source(root, 'rss-items', [], rehash=False)
        return result
    monkeypatch.setattr(news, 'verified_report_files', race)
    with pytest.raises(ValueError, match='changed after'):
        build(archive)


def test_legacy_sources_are_not_claimed_verified_and_missing_is_explicit(archive):
    index = read_json(archive / 'index.json')
    for entry in index['reports']:
        del entry['source_sha256']
    write_json(archive / 'index.json', index)
    path = (archive / index['reports'][0]['json']).parent / 'sources/csco-ai-intel.json'
    path.unlink()
    value = build(archive)
    assert value['reports'][0]['ai_status'] == 'missing'
    assert all(s['integrity'] == 'observed_hash_only' for s in value['sources'])


def test_wrong_ai_ticker_or_date_does_not_attach_decisions(archive):
    edit_source(archive, 'ai-intel', {'ticker': 'JPM', 'as_of': '2026-11-06', 'catalysts': [prediction()]})
    row = build(archive)['reports'][0]
    assert row['ai_status'] == 'identity_mismatch' and row['references'][0]['decision_status'] == 'missing'


def test_invalid_rss_rows_are_counted_and_invalid_ai_metadata_is_flagged(archive):
    edit_source(archive, 'rss-items', [None, {}, {'headline': []}, STORY])
    edit_source(archive, 'ai-intel', {'ticker': 'CSCO', 'as_of': '2026-11-06',
        'catalysts': [None, prediction(event_type=['invented'], sentiment='certain', extraction_method='human')]})
    row = build(archive)['reports'][0]
    assert row['invalid_rss_rows'] == 3 and row['malformed_decisions'] == 1
    flags = row['references'][0]['saved_decisions'][0]['review_flags']
    assert {'missing_or_invalid_event_type', 'missing_or_invalid_sentiment', 'missing_or_invalid_extraction_method'} <= set(flags)


def test_latest_version_cutoff_and_duplicate_archive_identity(archive):
    assert not build(archive, '2026-11-05')['reports']
    index = read_json(archive / 'index.json')
    replay = deepcopy(index['reports'][0])
    replay.update(report_id='later/CSCO', generated_at='2026-11-08T00:00:00Z')
    index['reports'].append(replay)
    write_json(archive / 'index.json', index)
    assert build(archive)['reports'][0]['report_id'] == 'later/CSCO'
    index['reports'].append(replay)
    write_json(archive / 'index.json', index)
    with pytest.raises(ValueError, match='Ambiguous'):
        build(archive)


def test_determinism_no_network_no_input_changes_and_manifest_checksums(archive, tmp_path, monkeypatch):
    def no_network(*a, **kw):
        raise AssertionError('Network access forbidden')
    monkeypatch.setattr(socket, 'create_connection', no_network)
    before = {p: p.read_bytes() for p in archive.rglob('*') if p.is_file()}
    first = build(archive)
    index = read_json(archive / 'index.json')
    index['reports'].reverse()
    write_json(archive / 'index.json', index)
    assert first == build(archive)
    # Restore the fixture index so the full input immutability assertion is exact.
    (archive / 'index.json').write_bytes(before[archive / 'index.json'])
    for folder in ('out-a', 'out-b'):
        news.write_bundle(first, tmp_path / folder, store=archive)
    a, b = tmp_path / 'out-a', tmp_path / 'out-b'
    assert {p.name: p.read_bytes() for p in a.iterdir()} == {p.name: p.read_bytes() for p in b.iterdir()}
    manifest = read_json(a / 'manifest.json')
    assert all(file_digest(a / name) == sha for name, sha in manifest['sha256'].items())
    assert all(p.read_bytes() == raw for p, raw in before.items())
    with pytest.raises(FileExistsError):
        news.write_bundle(first, a, store=archive)
    with pytest.raises(ValueError, match='outside'):
        news.write_bundle(first, archive / 'out', store=archive)


def test_bounded_source_and_row_counts(archive, monkeypatch):
    monkeypatch.setattr(news, 'MAX_SOURCE_BYTES', 10)
    with pytest.raises(ValueError, match='size limit'):
        build(archive)
    monkeypatch.setattr(news, 'MAX_SOURCE_BYTES', 2 * 1024 * 1024)
    edit_source(archive, 'rss-items', [STORY] * 501)
    with pytest.raises(ValueError, match='Too many'):
        build(archive)


def test_failed_write_never_has_completion_manifest(archive, tmp_path, monkeypatch):
    original = Path.open
    def fail(path, *args, **kw):
        if path.name == 'news-review.md' and args == ('xb',):
            raise OSError('synthetic full disk')
        return original(path, *args, **kw)
    value = build(archive)
    monkeypatch.setattr(Path, 'open', fail)
    with pytest.raises(OSError):
        news.write_bundle(value, tmp_path / 'failed', store=archive)
    assert not (tmp_path / 'failed/manifest.json').exists()


def test_title_only_irrelevant_decisions_stay_unmatched(archive):
    edit_source(archive, 'ai-intel', {'ticker': 'CSCO', 'as_of': '2026-11-06',
                                    'irrelevant': [{'headline': STORY['headline'], 'reason': 'private'}]})
    row = build(archive)['reports'][0]
    assert row['unmatched_decisions_by_category'] == {'irrelevant': 1}
    assert row['references'][0]['decision_status'] == 'missing'


def test_empty_feed_is_distinguished_from_missing_and_malformed(archive):
    edit_source(archive, 'rss-items', [])
    row = build(archive)['reports'][0]
    assert row['rss_status'] == 'available' and row['raw_rss_rows'] == 0
    edit_source(archive, 'rss-items', {'unexpected': []})
    row = build(archive)['reports'][0]
    assert row['rss_status'] == 'invalid_shape' and row['references'] == []


def test_unclassified_and_irrelevant_full_identities_are_retained(archive):
    edit_source(archive, 'ai-intel', {'ticker': 'CSCO', 'as_of': '2026-11-06',
                                    'unclassified': [prediction()], 'irrelevant': [prediction()]})
    ref = build(archive)['reports'][0]['references'][0]
    assert ref['decision_status'] == 'conflicting'
    assert {d['category'] for d in ref['saved_decisions']} == {'irrelevant', 'unclassified'}


def test_future_missing_and_stale_publications_are_not_suppressed(archive):
    edit_source(archive, 'rss-items', [{**STORY, 'pubDate': day} for day in
        ('Sat, 14 Nov 2026 00:00:00 GMT', None, 'Thu, 01 Oct 2026 00:00:00 GMT')])
    labels = {a['publication_age']['label'] for a in build(archive)['articles']}
    assert {'future_dated', 'unknown_publication_date', 'outside_rss_window'} <= labels


def test_output_symlink_into_store_is_rejected(archive, tmp_path):
    alias = tmp_path / 'alias'
    alias.symlink_to(archive, target_is_directory=True)
    with pytest.raises(ValueError, match='outside'):
        news.write_bundle(build(archive), alias / 'output', store=archive)


def test_archive_index_is_bounded(archive, monkeypatch):
    monkeypatch.setattr(news, 'MAX_INDEX_BYTES', 20)
    with pytest.raises(ValueError, match='size limit'):
        build(archive)


def test_cli_builds_explicit_draft_without_mutating_inputs(archive, tmp_path):
    script = Path(news.__file__)
    result = subprocess.run([sys.executable, str(script), '--store', str(archive), '--as-of', '2026-11-13',
                             '--output', str(tmp_path / 'cli')], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
    assert 'retrospective draft only' in result.stdout
    assert read_json(tmp_path / 'cli/manifest.json')['delivery_ready'] is False
