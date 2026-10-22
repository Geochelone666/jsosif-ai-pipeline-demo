"""Offline coverage for the optional FRED macro collector."""
from pathlib import Path
import io
import json
import sys

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import data_utils
import fred


@pytest.fixture
def workspace(tmp_path, monkeypatch):
    monkeypatch.setattr(data_utils, 'DATA', tmp_path)
    monkeypatch.setattr(fred, 'CONFIG_PATH', str(tmp_path / 'missing-fred.json'))
    monkeypatch.setenv('REPORT_AS_OF', '2026-10-08')
    monkeypatch.delenv('FRED_API_KEY', raising=False)
    return tmp_path


def output(workspace):
    return json.loads((workspace / 'fred.json').read_text(encoding='utf-8'))


def test_no_key_makes_no_request(workspace, monkeypatch, capsys):
    monkeypatch.setattr(fred, 'urlopen', lambda *a, **k: pytest.fail('network used'))
    fred.main()
    assert output(workspace) == {'available': False, 'reason': 'no key'}
    assert 'FRED SKIP' in capsys.readouterr().out


@pytest.mark.parametrize('config', ['[]', '{"api_key": null}', '{not json'])
def test_malformed_config_falls_back_to_environment(workspace, monkeypatch, config):
    Path(fred.CONFIG_PATH).write_text(config, encoding='utf-8')
    monkeypatch.setattr(fred, 'urlopen', lambda *a, **k: pytest.fail('network used'))
    fred.main()
    assert output(workspace)['available'] is False


def test_first_numeric_observation_and_failures_hide_key(workspace, monkeypatch, capsys):
    monkeypatch.setenv('FRED_API_KEY', 'secret-test-key')
    requested = []

    def fake_urlopen(url, timeout):
        requested.append(url)
        assert 'observation_end=2026-10-08' in url and timeout == 30
        if 'series_id=NAPM' in url:
            raise OSError('connection refused for ' + url)
        observations = [{'date': '2026-09-01', 'value': '.'},
                        {'date': '2026-08-01', 'value': 'nan'},
                        {'date': '2026-07-01', 'value': '4.1'}]
        return io.BytesIO(json.dumps({'observations': observations}).encode())

    monkeypatch.setattr(fred, 'urlopen', fake_urlopen)
    fred.main()
    result = output(workspace)
    assert result['available'] is True and result['as_of'] == '2026-10-08'
    rows = {row['series_id']: row for row in result['indicators']}
    assert list(rows) == list(fred.SERIES) and len(requested) == 4
    assert rows['UNRATE'] == {'series_id': 'UNRATE', 'name': fred.SERIES['UNRATE'],
                              'value': 4.1, 'date': '2026-07-01'}
    assert rows['NAPM']['value'] is None and rows['NAPM']['date'] is None
    printed = capsys.readouterr().out
    assert 'NAPM unavailable: OSError' in printed and '3/4 values' in printed
    assert 'secret-test-key' not in printed
    assert 'secret-test-key' not in (workspace / 'fred.json').read_text(encoding='utf-8')


def test_config_key_takes_precedence(workspace, monkeypatch):
    Path(fred.CONFIG_PATH).write_text('{"api_key": " team-key "}', encoding='utf-8')
    monkeypatch.setenv('FRED_API_KEY', 'personal-key')
    seen = []
    monkeypatch.setattr(fred, 'urlopen', lambda url, timeout: seen.append(url) or
                        io.BytesIO(b'{"observations": []}'))
    fred.main()
    assert seen and all('api_key=team-key&' in url for url in seen)
    assert all(row['value'] is None for row in output(workspace)['indicators'])
