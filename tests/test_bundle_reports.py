from pathlib import Path

import pytest

from bundle_reports import bundle_reports


def test_bundle_copies_files_and_replaces_stale_content(tmp_path):
    reports = tmp_path / 'reports'
    (reports / 'nested').mkdir(parents=True)
    (reports / 'a.md').write_text('a')
    (reports / 'nested' / 'b.md').write_text('b')
    bundle = bundle_reports(reports, tmp_path / 'bundle')
    assert sorted(p.relative_to(bundle).as_posix() for p in Path(bundle).rglob('*') if p.is_file()) == ['a.md', 'nested/b.md']
    (Path(bundle) / 'stale.md').write_text('x')
    assert bundle_reports(reports, tmp_path / 'bundle') == bundle
    assert not (Path(bundle) / 'stale.md').exists()


def test_missing_empty_and_overlapping_directories_are_rejected(tmp_path):
    with pytest.raises(SystemExit):
        bundle_reports(tmp_path / 'missing', tmp_path / 'bundle')
    (tmp_path / 'empty').mkdir()
    with pytest.raises(SystemExit):
        bundle_reports(tmp_path / 'empty', tmp_path / 'bundle')
    reports = tmp_path / 'reports'
    reports.mkdir()
    (reports / 'a.md').write_text('a')
    with pytest.raises(SystemExit):
        bundle_reports(reports, reports)
