from io import BytesIO
import json
from pathlib import Path
import subprocess
import sys

import pytest
from pypdf import PdfReader

import news_evidence
import news_review as news
from report_store import digest as file_digest, read_json, write_json
from shared_research_pack import digest
from snapshot_emit import emit_frozen_snapshot


@pytest.fixture
def archive(tmp_path):
    root = tmp_path / 'store'; folder = Path('archive/synthetic/CSCO')
    entry = {'ticker': 'CSCO', 'report_id': 'synthetic/CSCO', 'as_of': '2026-11-06',
             'generated_at': '2026-11-07T01:00:00+00:00', 'quality': 'ready'}
    snapshot = emit_frozen_snapshot(ticker='CSCO', as_of=entry['as_of'], quant_metrics={'Close': 100},
                                   ai={'status': 'Available'}, freshness={}, disclaimer='Synthetic fixture')
    snapshot['quality'] = 'ready'
    for kind, raw in [('json', json.dumps(snapshot)), ('md', 'fixture'), ('pdf', '%PDF-1.4 fixture')]:
        relative = folder / f'CSCO-intelligence-20261106.{kind}'
        path = root / relative; path.parent.mkdir(parents=True, exist_ok=True); path.write_text(raw)
        entry[kind] = str(relative)
    entry['sha256'] = {k: file_digest(root / entry[k]) for k in ('json', 'md', 'pdf')}
    write_json(root / 'index.json', {'reports': [entry]})
    rows = [{'headline': f'CSCO synthetic story {i}', 'source': 'Synthetic publisher',
             'pubDate': f'Fri, 06 Nov 2026 {i:02}:00:00 GMT', 'link': 'https://example.org/article/' + str(i)} for i in range(10)]
    rows += [{**rows[0], 'pubDate': 'Sat, 07 Nov 2026 00:00:00 GMT'}, {**rows[0], 'pubDate': None}]
    write_json(root / folder / 'sources/csco-rss-items.json', rows)
    return root


def value(root):
    return news.assemble(news_evidence.build(root, as_of='2026-11-06'))


def rehash(value):
    index = value['evidence']
    index['index_id'] = digest({k:v for k,v in index.items() if k != 'index_id'})
    value['review_id'] = digest({k:v for k,v in value.items() if k != 'review_id'})


def test_chronology_excludes_future_and_undated_without_erasing_them(archive):
    result = value(archive)
    articles = {a['id']: a for a in result['evidence']['articles']}
    assert len(result['selected_article_ids']) == 8 and result['summary']['articles'] == 12
    assert result['summary']['future_articles'] == result['summary']['undated_articles'] == 1
    assert [articles[k]['headline'] for k in result['selected_article_ids']] == [f'CSCO synthetic story {i}' for i in range(9, 1, -1)]
    assert result['delivery_ready'] is False
    assert result['report_versions']['CSCO']['snapshot_sha256']
    assert all(a['event_date'] is None for a in articles.values())


def test_pdf_companion_and_manifest_reproduce_and_load_retained_bytes(archive, tmp_path):
    result = value(archive)
    first = news.write_bundle(result, tmp_path / 'first', store=archive)
    second = news.write_bundle(result, tmp_path / 'second', store=archive)
    assert first == second and first['validation']['pages'] == 4
    for kind in ('pdf', 'json'):
        assert (tmp_path / 'first' / first[kind]).read_bytes() == (tmp_path / 'second' / second[kind]).read_bytes()
    loaded = news.load_bundle(tmp_path / 'first')
    assert loaded['review_id'] == result['review_id'] and loaded['report_versions'] == result['report_versions']
    assert loaded['bytes'] == (tmp_path / 'first' / first['pdf']).read_bytes()
    assert news.load_bundle(None) is None
    pdf = PdfReader(BytesIO(loaded['bytes']))
    assert len(pdf.pages) == 4 and 'future' in pdf.pages[0].extract_text()
    assert len(pdf.pages[1]['/Annots']) == 4  # Actual clickable source references.


@pytest.mark.parametrize('field', ['summary', 'selected_article_ids', 'report_versions'])
def test_rehashed_derived_tampering_is_rejected(archive, field):
    result = value(archive)
    result[field] = [] if field == 'selected_article_ids' else {}
    rehash(result)
    with pytest.raises(ValueError, match='differs'): news.validate_review(result)


@pytest.mark.parametrize('field,altered', [('event_date', '2026-12-05'), ('point_in_time_eligible', True),
    ('publication_age', {}), ('url', 'https://example.org/a?secret=key'), ('published_at', '2026-11-06T10:00:00')])
def test_rehashed_false_claims_and_unsafe_metadata_fail(archive, field, altered):
    result = value(archive); result['evidence']['articles'][0][field] = altered; rehash(result)
    with pytest.raises(ValueError): news.validate_review(result)


@pytest.mark.parametrize('change', ['source', 'article', 'count', 'decision', 'missing', 'unknown'])
def test_rehashed_broken_references_and_accounting_fail(archive, change):
    result = value(archive); index = result['evidence']; r = index['reports'][0]
    if change == 'source': r['rss_source_id'] = 'source:' + '0'*64
    elif change == 'article': r['references'][0]['article_id'] = 'article:' + '0'*64
    elif change == 'count': r['raw_rss_rows'] += 1
    elif change == 'decision': r['references'][0]['decision_status'] = 'single_saved_prediction'
    elif change == 'missing': index['missing_reports'] = []
    else: index['private'] = 'unexpected'
    rehash(result)
    with pytest.raises(ValueError): news.validate_review(result)


@pytest.mark.parametrize('kind', ['pdf', 'json'])
def test_bundle_hash_tampering_is_rejected(archive, tmp_path, kind):
    manifest = news.write_bundle(value(archive), tmp_path / 'out', store=archive)
    with (tmp_path / 'out' / manifest[kind]).open('ab') as stream: stream.write(b'tampered')
    with pytest.raises(ValueError, match='checksum'): news.load_bundle(tmp_path / 'out')


@pytest.mark.parametrize('field,altered', [('delivery_ready', True), ('pdf', '../elsewhere.pdf'), ('review_id', '0'*64)])
def test_manifest_promotion_path_escape_and_identity_mismatch_fail(archive, tmp_path, field, altered):
    out = tmp_path / 'out'; manifest = news.write_bundle(value(archive), out, store=archive)
    manifest[field] = altered; write_json(out / 'manifest.json', manifest)
    with pytest.raises(ValueError): news.load_bundle(out)


def test_empty_archive_has_four_pages_and_explicit_missing_coverage(tmp_path):
    root = tmp_path / 'store'; write_json(root / 'index.json', {'reports': []})
    result = value(root); raw = news.render(result)
    assert result['summary']['articles'] == 0 and len(result['evidence']['missing_reports']) == 50
    assert news.inspect_pdf(raw, result)['pages'] == 4
    assert 'No additional eligible dated headlines' in PdfReader(BytesIO(raw)).pages[1].extract_text()


def test_long_untrusted_text_is_shortened_and_escaped_without_extra_pages(archive):
    path = archive / 'archive/synthetic/CSCO/sources/csco-rss-items.json'
    rows = read_json(path)
    for r in rows:
        r['headline'] = '<script><b>news</b></script> ' + 'Long headline words ' * 70
        r['source'] = 'Publisher ' * 25
    write_json(path, rows)
    result = value(archive); raw = news.render(result)
    assert news.inspect_pdf(raw, result)['pages'] == 4
    page = PdfReader(BytesIO(raw)).pages[1].extract_text()
    assert '[shortened]' in page and '<script>' in page
    assert all(len(a['headline']) > 1000 for a in result['evidence']['articles'])


def test_output_and_input_bounds_preserve_existing_paths(archive, tmp_path, monkeypatch):
    result = value(archive); out = tmp_path / 'out'; out.mkdir(); (out / 'user').write_text('keep')
    with pytest.raises(FileExistsError): news.write_bundle(result, out, store=archive)
    assert (out / 'user').read_text() == 'keep'
    with pytest.raises(ValueError, match='outside'): news.write_bundle(result, archive / 'new', store=archive)
    monkeypatch.setattr(news, 'MAX_JSON', 10)
    with pytest.raises(ValueError, match='limit'): news.write_bundle(result, tmp_path / 'too-large', store=archive)
    assert not (tmp_path / 'too-large').exists()


def test_write_failure_never_leaves_completion_manifest(archive, tmp_path, monkeypatch):
    original = Path.open
    def fail(path, *args, **kw):
        if path.name == 'news-review-2026-11-06.json' and args == ('xb',): raise OSError('synthetic disk full')
        return original(path, *args, **kw)
    monkeypatch.setattr(Path, 'open', fail)
    with pytest.raises(OSError): news.write_bundle(value(archive), tmp_path / 'failed', store=archive)
    assert not (tmp_path / 'failed/manifest.json').exists()


def test_cli_builds_draft(archive, tmp_path):
    result = subprocess.run([sys.executable, str(Path(news.__file__)), '--store', str(archive),
        '--as-of', '2026-11-06', '--output', str(tmp_path / 'cli')], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
    assert news.load_bundle(tmp_path / 'cli')['review_id'] == value(archive)['review_id']
