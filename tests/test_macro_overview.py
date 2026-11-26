import hashlib
import json
from pathlib import Path
import subprocess
import sys

import pytest

from macro_overview import assemble, validate_overview, write_bundle, load_bundle, UNITS, number
from report_store import write_json, read_json
from shared_research_pack import build, Evidence, digest


def rehash(value, key):
    value[key] = digest({k:v for k,v in value.items() if k != key})


@pytest.fixture
def archive(tmp_path):
    root = tmp_path / 'store'; write_json(root / 'index.json', {'reports': []})
    return root


def pack(archive, rows):
    result = build(archive, as_of='2026-11-13')
    evidence = Evidence(); subject = evidence.entity('macro', 'fred:UNRATE', provider='FRED', series_id='UNRATE')
    for i, (day, value, unit) in enumerate(rows):
        source = evidence.provenance('fred', {'sha256': f'{i:064x}', 'integrity': 'synthetic test source'},
                                     url='https://fred.stlouisfed.org/')
        evidence.observation(subject, 'level', value, unit, day, source, '2026-11-13')
    result['entities'] += list(evidence.entities.values())
    result['sources'] += list(evidence.sources.values())
    result['observations'] += list(evidence.observations.values())
    rehash(result, 'dataset_id')
    return result


def unemployment(value):
    return next(r for r in value['series'] if r['subject'] == 'macro:fred:UNRATE')


def test_latest_date_zero_units_age_and_five_series(archive):
    value = assemble(pack(archive, [('2026-11-05', 2, 'percent'), ('2026-11-06', 0, 'percent')]))
    row = unemployment(value)
    assert row['status'] == 'observed' and row['value'] == 0 and row['age_days'] == 7
    assert len(value['series']) == 5 and set(r['subject'] for r in value['series']) == set(UNITS)
    assert value['delivery_ready'] is False and len(row['history']) == 2
    assert all(o['publication_time'] is None and o['point_in_time_eligible'] is False for o in value['observations'])
    assert number(0.000001) != '0' and number(0) == '0'


@pytest.mark.parametrize('rows,status,day', [
    ([('2026-11-05', 2, 'percent'), ('2026-11-06', None, 'percent')], 'missing', '2026-11-06'),
    ([('2026-11-06', 2, 'percent'), ('2026-11-06', None, 'percent')], 'incomplete', '2026-11-06'),
    ([('2026-11-06', 2, 'percent'), ('2026-11-06', 3, 'percent')], 'conflicting', '2026-11-06'),
])
def test_missing_newer_or_conflicting_evidence_never_becomes_an_available_value(archive, rows, status, day):
    row = unemployment(assemble(pack(archive, rows)))
    assert row['status'] == status and row['value'] is None and row['observed_on'] == day
    assert sum(len(r['observation_ids']) for r in row['history']) == len(rows)


def test_equal_copies_do_not_inflate_history_dates(archive):
    row = unemployment(assemble(pack(archive, [('2026-11-06', 0, 'percent')] * 2)))
    assert row['status'] == 'observed' and len(row['history']) == 1
    assert len(row['history'][0]['observation_ids']) == 2


def test_empty_archive_has_explicit_missing_series(archive):
    value = assemble(build(archive, as_of='2026-11-13'))
    assert len(value['series']) == 5 and all(r['status'] == 'missing' for r in value['series'])
    assert value['observations'] == [] and value['report_versions'] == {}


def test_wrong_units_fail_even_with_valid_fingerprints(archive):
    with pytest.raises(ValueError, match='unit'):
        assemble(pack(archive, [('2026-11-06', 2, 'fraction')]))


def test_modified_derived_summary_is_rejected_after_rehash(archive):
    value = assemble(pack(archive, [('2026-11-06', 2, 'percent')]))
    unemployment(value)['value'] = 99; rehash(value, 'overview_id')
    with pytest.raises(ValueError, match='summary'): validate_overview(value)


def test_publication_and_point_in_time_claims_are_rejected(archive):
    value = assemble(pack(archive, [('2026-11-06', 2, 'percent')]))
    observation = value['observations'][0]; observation['point_in_time_eligible'] = True
    observation['id'] = 'observation:' + digest({k:v for k,v in observation.items() if k != 'id'})
    rehash(value, 'overview_id')
    with pytest.raises(ValueError, match='observation'): validate_overview(value)


def test_captured_boc_dates_and_retrieval_are_preserved(archive):
    capture = Path('tests/fixtures/boc_fxusdcad_20261102_20261106.json')
    value = assemble(build(archive, as_of='2026-11-13', boc_capture=capture))
    row = next(r for r in value['series'] if r['subject'] == 'macro:boc:FXUSDCAD')
    assert len(row['history']) == 5 and row['observed_on'] == '2026-11-06' and row['age_days'] == 7
    assert all(r['retrieved_at'].startswith('2026-11-14') for r in value['observations'])


def test_pdf_and_json_are_byte_reproducible_and_round_trip(archive, tmp_path):
    value = assemble(pack(archive, [('2026-11-06', 2, 'percent')]))
    a, b = tmp_path / 'first', tmp_path / 'second'
    first, second = write_bundle(value, a), write_bundle(value, b)
    assert first == second and first['validation']['pages'] == 2
    for kind in ('pdf', 'json'):
        assert (a / first[kind]).read_bytes() == (b / second[kind]).read_bytes()
        assert hashlib.sha256((a / first[kind]).read_bytes()).hexdigest() == first['sha256'][kind]
    loaded = load_bundle(a)
    assert loaded['overview_id'] == value['overview_id'] and loaded['bytes'] == (a / first['pdf']).read_bytes()


@pytest.mark.parametrize('kind', ['pdf', 'json'])
def test_artifact_tampering_fails(archive, tmp_path, kind):
    out = tmp_path / 'output'; manifest = write_bundle(assemble(build(archive, as_of='2026-11-13')), out)
    with (out / manifest[kind]).open('ab') as stream: stream.write(b'changed')
    with pytest.raises(ValueError, match='checksum'): load_bundle(out)


def test_manifest_cannot_promote_draft_or_escape_bundle(archive, tmp_path):
    out = tmp_path / 'output'; manifest = write_bundle(assemble(build(archive, as_of='2026-11-13')), out)
    altered = dict(manifest, delivery_ready=True); write_json(out / 'manifest.json', altered)
    with pytest.raises(ValueError, match='manifest'): load_bundle(out)
    altered = dict(manifest, pdf='../elsewhere.pdf'); write_json(out / 'manifest.json', altered)
    with pytest.raises(ValueError, match='filename'): load_bundle(out)


def test_existing_output_and_archive_are_preserved(archive, tmp_path):
    out = tmp_path / 'output'; out.mkdir(); (out / 'user.txt').write_text('keep')
    value = assemble(build(archive, as_of='2026-11-13'))
    with pytest.raises(FileExistsError): write_bundle(value, out)
    assert (out / 'user.txt').read_text() == 'keep'
    result = subprocess.run([sys.executable, 'scripts/macro_overview.py', '--store', str(archive),
        '--as-of', '2026-11-13', '--output', str(archive / 'output')], capture_output=True)
    assert result.returncode != 0 and not (archive / 'output').exists()
