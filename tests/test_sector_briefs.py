import hashlib
import json
from pathlib import Path
import subprocess
import sys

import pytest
from pypdf import PdfReader

from report_store import digest as file_digest, read_json, write_json
from shared_research_pack import build, digest
from snapshot_emit import emit_frozen_snapshot
from sector_briefs import assemble, cell, write_bundle, SECTIONS


@pytest.fixture
def archive(tmp_path):
    root = tmp_path / 'store'
    entries = []
    for ticker in ('CSCO', 'MSFT'):
        base = Path('archive/synthetic') / ticker
        entry = {'ticker': ticker, 'report_id': 'synthetic/' + ticker, 'as_of': '2026-11-06',
                 'generated_at': '2026-11-07T01:00:00+00:00', 'quality': 'ready'}
        snapshot = emit_frozen_snapshot(ticker=ticker, as_of=entry['as_of'],
            quant_metrics={'Close': 100, 'Return 1W (%)': 0}, ai={'status': 'Available'},
            freshness={'market_data_as_of': '2026-11-06'}, disclaimer='Synthetic fixture')
        snapshot['quality'] = 'ready'
        for kind in ('json', 'md', 'pdf'):
            rel = base / f'{ticker}-intelligence-20261106.{kind}'
            path = root / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text({'json': json.dumps(snapshot), 'md': 'Fixture', 'pdf': '%PDF-1.4 fixture'}[kind])
            entry[kind] = str(rel)
        entry['sha256'] = {k: file_digest(root / entry[k]) for k in ('json', 'md', 'pdf')}
        sources = root / base / 'sources'
        write_json(sources / (ticker.lower() + '-info.json'), {'symbol': ticker, 'currency': 'USD',
                   'industry': 'Software', 'private': 'private@example.com'})
        write_json(sources / 'fred.json', {'available': True, 'indicators': [
            {'series_id': 'UNRATE', 'value': 0, 'date': '2026-10-01'}]})
        write_json(sources / (ticker.lower() + '-comparables.json'), {'as_of': '2026-11-06', 'peers': [
            {'ticker': t, 'currency': 'USD', 'pe': v, 'pb': 2, 'mktcap': 100, 'ret_1y': .1}
            for t, v in [('AMD', 10), ('NVDA', None), ('IBM', 0)]]})
        entries.append(entry)
    write_json(root / 'index.json', {'reports': entries})
    return root


def pack_for(root):
    return build(root, as_of='2026-11-06')


def technology(pack):
    return next(b for b in assemble(pack) if b['sector_id'] == 'sector:technology')


def rehash(pack):
    pack['dataset_id'] = digest({k: v for k, v in pack.items() if k != 'dataset_id'})


def test_all_groups_missing_facts_and_source_lineage(archive):
    pack = pack_for(archive)
    briefs = assemble(pack)
    assert len(briefs) == 8 and sum(len(b['stocks']) for b in briefs) == 50
    for brief in briefs:
        assert brief['sections'] == list(SECTIONS)
        assert brief['delivery_ready'] is False and brief['relative_performance'] is None
        assert not brief['events'] and not brief['kpi_observations']
        assert brief['brief_id'] == digest({k: v for k, v in brief.items() if k != 'brief_id'})
        assert set(o['source_id'] for o in brief['observations'] if o['source_id']) <= {s['id'] for s in brief['sources']}
    tech = technology(pack)
    stock = next(s for s in tech['stocks'] if s['ticker'] == 'CSCO')
    assert stock['quality'] == 'ready' and stock['industry'] == 'Software'
    assert [p['ticker'] for p in stock['peers']] == ['AMD', 'IBM', 'NVDA']
    assert cell(tech, stock['peers'][1]['metrics']['peer.pe']) == '0.00'
    assert cell(tech, stock['peers'][2]['metrics']['peer.pe']) == 'N/A'
    assert 'private@example.com' not in json.dumps(briefs)
    assert next(m for m in tech['macro'] if m['subject'] == 'macro:fred:UNRATE')['value'] == 0


def test_permutations_do_not_change_briefs(archive):
    pack = pack_for(archive)
    expected = assemble(pack)
    for key in ('reports', 'entities', 'sources', 'observations', 'relationships', 'sectors'):
        pack[key].reverse()
    rehash(pack)
    actual = assemble(pack)
    # Dataset fingerprints intentionally capture input order; content selection does not.
    for before, after in zip(expected, actual):
        assert {k:v for k,v in before.items() if k not in ('brief_id','dataset_id')} == {
            k:v for k,v in after.items() if k not in ('brief_id','dataset_id')}


def test_old_reports_remain_disclosed_not_current(archive):
    brief = technology(build(archive, as_of='2026-11-26'))
    stock = next(s for s in brief['stocks'] if s['ticker'] == 'CSCO')
    assert stock['report_age_days'] == 20 and stock['in_review_window'] is False
    assert brief['delivery_ready'] is False


def test_conflicting_macro_values_are_not_arbitrarily_selected(archive):
    path = archive / 'archive/synthetic/MSFT/sources/fred.json'
    value = read_json(path); value['indicators'][0]['value'] = 5; write_json(path, value)
    macro = next(m for m in technology(pack_for(archive))['macro'] if m['subject'] == 'macro:fred:UNRATE')
    assert macro['status'] == 'conflicting' and macro['value'] is None and macro['unit'] is None
    assert len(macro['observation_ids']) == 2


def test_peer_candidates_are_capped_and_not_padded(archive):
    path = archive / 'archive/synthetic/CSCO/sources/csco-comparables.json'
    payload = read_json(path)
    payload['peers'] += [{'ticker': t, 'pe': 4} for t in ('V', 'MA', 'GOOGL')]
    write_json(path, payload)
    stock = next(s for s in technology(pack_for(archive))['stocks'] if s['ticker'] == 'CSCO')
    assert stock['peer_count'] == 6 and len(stock['peers']) == 5
    payload['peers'] = payload['peers'][:1]; write_json(path, payload)
    stock = next(s for s in technology(pack_for(archive))['stocks'] if s['ticker'] == 'CSCO')
    assert stock['peer_count'] == 1 and len(stock['peers']) == 1


def test_incomplete_price_is_not_printed_as_established_fact(archive):
    path = archive / 'archive/synthetic/CSCO/sources/csco-info.json'
    write_json(path, {'symbol': 'OTHER', 'currency': 'USD'})
    brief = technology(pack_for(archive))
    stock = next(s for s in brief['stocks'] if s['ticker'] == 'CSCO')
    assert cell(brief, stock['metrics']['stock.Close']) == 'N/A'


def test_evidence_context_cannot_be_reassigned(archive):
    pack = pack_for(archive)
    pack['reports'][0]['as_of'] = '2026-11-05'; rehash(pack)
    with pytest.raises(ValueError, match='context'): assemble(pack)


def test_duplicate_sector_membership_fails(archive):
    pack = pack_for(archive)
    pack['sectors'][0]['tickers'].append('CSCO'); rehash(pack)
    with pytest.raises(ValueError, match='coverage'): assemble(pack)


def test_output_hashes_four_pages_and_reproducibility(archive, tmp_path):
    pack = pack_for(archive)
    a, b = tmp_path / 'first', tmp_path / 'second'
    first, second = write_bundle(pack, a), write_bundle(pack, b)
    assert first == second
    assert len(first['briefs']) == 8
    for entry in first['briefs']:
        for kind in ('pdf', 'json'):
            assert hashlib.sha256((a / entry[kind]).read_bytes()).hexdigest() == entry['sha256'][kind]
            assert (a / entry[kind]).read_bytes() == (b / entry[kind]).read_bytes()
        reader = PdfReader(a / entry['pdf'])
        assert len(reader.pages) == 4
        assert all('Draft - incomplete evidence' in p.extract_text() for p in reader.pages)


def test_existing_directory_and_symlink_are_preserved(archive, tmp_path):
    out = tmp_path / 'user-files'; out.mkdir(); (out / 'important.txt').write_text('keep')
    with pytest.raises(FileExistsError): write_bundle(pack_for(archive), out)
    link = tmp_path / 'link'; link.symlink_to(out, target_is_directory=True)
    with pytest.raises(FileExistsError): write_bundle(pack_for(archive), link)
    assert (out / 'important.txt').read_text() == 'keep' and len(list(out.iterdir())) == 1


def test_failed_render_leaves_no_completed_bundle(archive, tmp_path, monkeypatch):
    import sector_brief_pdf
    def fail(*args): raise ValueError('render failed')
    monkeypatch.setattr(sector_brief_pdf, 'render', fail)
    out = tmp_path / 'failed'
    with pytest.raises(ValueError): write_bundle(pack_for(archive), out)
    assert not (out / 'manifest.json').exists() and list(out.iterdir()) == []


def test_cli_cannot_write_into_archive(archive):
    result = subprocess.run([sys.executable, 'scripts/sector_briefs.py', '--store', str(archive),
        '--as-of', '2026-11-06', '--output', str(archive / 'briefs')], capture_output=True)
    assert result.returncode != 0 and not (archive / 'briefs').exists()


def test_tampered_archive_cannot_create_output(archive, tmp_path):
    entry = read_json(archive / 'index.json')['reports'][0]
    (archive / entry['json']).write_text('{}')
    output = tmp_path / 'output'
    result = subprocess.run([sys.executable, 'scripts/sector_briefs.py', '--store', str(archive),
        '--as-of', '2026-11-06', '--output', str(output)], capture_output=True)
    assert result.returncode != 0 and not output.exists()
