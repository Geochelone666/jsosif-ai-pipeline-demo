"""Review artifacts must stay offline and make blocked drafts unmistakable."""
import json
from pathlib import Path
import re
import socket
import sys

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import build_review_bundle as review
import email_delivery
import snapshot_contract as contract


@pytest.fixture
def repo(tmp_path, monkeypatch):
    monkeypatch.setattr(review, 'ROOT', tmp_path)
    reports = tmp_path / 'reports'
    reports.mkdir()
    for ticker in ('ZZZ', 'AAA'):
        (reports / f'{ticker}-intelligence-20261008.md').write_text(
            f'# Demo\n- ticker: **{ticker}**\n- Report as_of: **2026-10-08**\n'
            '## QUANTITATIVE\n| Metric | Value |\n|---|---|\n| Close | 12 |\n'
            '## TAILWINDS\nExisting evidence\n', encoding='utf-8')
    (tmp_path / 'recipients.json').write_text('{"recipients": ["lucas@example.com"]}')
    return tmp_path


def run(repo):
    review.main(['--out', str(repo / 'review')])
    out = repo / 'review'
    return out, json.loads((out / 'manifest.json').read_text())


def test_render_and_index(repo):
    out, manifest = run(repo)
    assert [item['ticker'] for item in manifest] == ['AAA', 'ZZZ']
    index = (out / 'index.html').read_text()
    for item in manifest:
        ticker = item['ticker']
        assert item['validation_errors'] == []
        assert item['files'] == [f'{ticker}.txt', f'{ticker}.html']
        assert index.count(f'<td>{ticker}</td>') == 1
        assert item['subject'] in index
        assert 'lucas@example.com' in index
        for suffix in ('txt', 'html'):
            content = (out / f'{ticker}.{suffix}').read_text()
            assert 'Not investment advice' in content
            assert f'Contract version: {contract.CONTRACT_VERSION}' in content
    for link in re.findall(r'href="([^"]+)"', index):
        assert (out / link).is_file()
    assert f'Contract version: {contract.CONTRACT_VERSION}' in (out / 'REVIEW-CHECKLIST.md').read_text()
    first = (out / 'manifest.json').read_bytes()
    run(repo)
    assert first == (out / 'manifest.json').read_bytes()


def test_blocked_draft(repo, monkeypatch):
    original = contract.validate_snapshot
    monkeypatch.setattr(contract, 'validate_snapshot', lambda p:
                        ['bad quant'] if p['identity']['ticker'] == 'AAA' else original(p))
    out, manifest = run(repo)
    assert manifest[0]['validation_errors'] == ['bad quant']
    assert manifest[0]['files'] == []
    assert not (out / 'AAA.txt').exists()
    for name in ('index.html', 'REVIEW-CHECKLIST.md'):
        text = (out / name).read_text()
        assert 'BLOCKED' in text and 'bad quant' in text and 'AAA' in text
    assert 'href="AAA.' not in (out / 'index.html').read_text()


@pytest.mark.parametrize('problem', ['missing', 'zero', 'invalid', 'unwritable'])
def test_cli_errors(repo, problem):
    if problem == 'missing':
        (repo / 'recipients.json').unlink()
    elif problem == 'zero':
        for path in (repo / 'reports').iterdir():
            path.unlink()
    elif problem == 'invalid':
        (repo / 'recipients.json').write_text('{')
    else:
        (repo / 'review').write_text('not a directory')
    with pytest.raises(SystemExit) as exc:
        run(repo)
    assert exc.value.code != 0


def test_all_blocked_has_manifest(repo, monkeypatch):
    monkeypatch.setattr(contract, 'validate_snapshot', lambda p: ['invalid'])
    with pytest.raises(SystemExit):
        run(repo)
    assert all(row['validation_errors'] for row in json.loads(
        (repo / 'review/manifest.json').read_text()))


def test_freeze_drift_blocks(repo, monkeypatch):
    monkeypatch.setattr(review.freeze, 'determinism_check', lambda *a, **k: False)
    with pytest.raises(SystemExit):
        run(repo)
    assert 'drift' in (repo / 'review/manifest.json').read_text()


def test_frozen_sidecar_is_validated(repo):
    (repo / 'reports/AAA-intelligence-20261008.json').write_text('{"contract_version": "broken"}')
    _, manifest = run(repo)
    assert manifest[0]['validation_errors']
    assert not manifest[0]['files']


def test_no_network_and_pending_recipients(repo, monkeypatch):
    def forbidden(*args, **kwargs):
        pytest.fail('real transport reached')
    monkeypatch.setattr(socket, 'socket', forbidden)
    monkeypatch.setattr(email_delivery, 'send', forbidden)
    (repo / 'recipients.json').write_text('{"recipients": []}')
    out, manifest = run(repo)
    assert all(item['recipients'] == [] for item in manifest)
    text = (out / 'REVIEW-CHECKLIST.md').read_text()
    for phrase in ('Joseph', 'send-from', 'Sending is blocked', 'recipient', 'freshness'):
        assert phrase in text


def test_staging_failure_publishes_nothing(repo, monkeypatch):
    original = Path.write_text
    def fail(path, *args, **kwargs):
        if path.name == 'REVIEW-CHECKLIST.md':
            raise OSError('disk full')
        return original(path, *args, **kwargs)
    monkeypatch.setattr(Path, 'write_text', fail)
    with pytest.raises(SystemExit):
        run(repo)
    assert not (repo / 'review').exists()


def test_sector_filters_holdings_and_team_recipients(repo):
    data = repo / 'data'
    data.mkdir()
    for ticker, sector in [('aaa', 'technology'), ('zzz', 'energy')]:
        (data / f'{ticker}-info.json').write_text(json.dumps({'sectorKey': sector}))
    config = repo / 'teams.yaml'
    config.write_text('tech:\n  name: Tech\n  email: tech@example.com\n  sectors: [technology]\n  role: analyst\nenergy:\n  name: Energy\n  email: energy@example.com\n  sectors: [energy]\n  role: analyst\n')
    review.main(['--recipients', str(config), '--sector', 'technology', '--out', str(repo / 'review')])
    manifest = json.loads((repo / 'review/manifest.json').read_text())
    assert [row['ticker'] for row in manifest] == ['AAA']
    assert manifest[0]['recipients'] == ['tech@example.com']


def test_frozen_sidecar_drift(repo):
    path = repo / 'reports/AAA-intelligence-20261008.md'
    payload = review.snapshot_payload(path)
    payload['quant'][0]['value'] = '999'
    path.with_suffix('.json').write_text(json.dumps(payload))
    _, manifest = run(repo)
    assert any('drift' in error for error in manifest[0]['validation_errors'])


def test_valid_frozen_sidecar(repo):
    path = repo / 'reports/AAA-intelligence-20261008.md'
    path.with_suffix('.json').write_text(json.dumps(review.snapshot_payload(path)))
    _, manifest = run(repo)
    assert manifest[0]['validation_errors'] == []


def test_default_email_still_rejects_empty_recipients(repo):
    with pytest.raises(ValueError):
        email_delivery.build_email([repo / 'reports/AAA-intelligence-20261008.md'], [])


def test_rerun_removes_previously_clean_blocked_draft(repo, monkeypatch):
    run(repo)
    original = contract.validate_snapshot
    monkeypatch.setattr(contract, 'validate_snapshot', lambda p:
                        ['new failure'] if p['identity']['ticker'] == 'AAA' else original(p))
    out, _ = run(repo)
    assert not (out / 'AAA.html').exists()
    assert not (out / 'AAA.txt').exists()


def test_latest_report_only(repo):
    old = repo / 'reports/AAA-intelligence-20261008.md'
    (repo / 'reports/AAA-intelligence-20261009.md').write_text(
        old.read_text().replace('2026-10-08', '2026-10-09'))
    _, manifest = run(repo)
    assert len(manifest) == 2
    assert '2026-10-09 AAA' in manifest[0]['subject']


def test_sector_falls_back_to_tracked_map_without_pipeline_data(repo):
    (repo / 'data').mkdir()
    (repo / 'data' / 'zzz-info.json').write_text(json.dumps({'sectorKey': 'energy'}))
    (repo / 'config').mkdir(exist_ok=True)
    (repo / 'config' / 'sectors.json').write_text(json.dumps({'sectors': {'AAA': 'technology'}}))
    config = repo / 'teams.yaml'
    config.write_text('tech:\n  name: Tech\n  email: tech@example.com\n  sectors: [technology]\n  role: analyst\n')
    review.main(['--recipients', str(config), '--sector', 'technology', '--out', str(repo / 'review')])
    manifest = json.loads((repo / 'review/manifest.json').read_text())
    assert [row['ticker'] for row in manifest] == ['AAA']


def test_sector_without_any_data_is_a_clear_error(repo, capsys):
    config = repo / 'teams.yaml'
    config.write_text('tech:\n  name: Tech\n  email: tech@example.com\n  sectors: [technology]\n  role: analyst\n')
    with pytest.raises(SystemExit):
        review.main(['--recipients', str(config), '--sector', 'technology', '--out', str(repo / 'review')])
    assert 'config/sectors.json' in capsys.readouterr().err


def test_tracked_sector_map_covers_committed_reports():
    root = Path(__file__).resolve().parents[1]
    sectors = json.loads((root / 'config' / 'sectors.json').read_text())['sectors']
    tickers = {path.name.split('-intelligence-')[0] for path in (root / 'reports').glob('*-intelligence-*.md')}
    assert tickers <= set(sectors)
