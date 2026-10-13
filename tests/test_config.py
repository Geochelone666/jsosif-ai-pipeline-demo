"""Offline configuration boundaries and startup regression tests."""
from datetime import date, timedelta
import json
from pathlib import Path
import sys

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import config
import run_phase1


@pytest.fixture(autouse=True)
def isolated(monkeypatch, tmp_path):
    monkeypatch.delenv('JSOSIF_CONFIG', raising=False)
    for key in config.REGISTRY:
        monkeypatch.delenv('JSOSIF_' + key.upper(), raising=False)
    monkeypatch.setattr(config, 'ROOT', tmp_path)


def write_config(tmp_path, values):
    path = tmp_path / 'config.json'
    path.write_text(json.dumps(values), encoding='utf-8')
    return path


def test_missing_defaults(tmp_path):
    expected = dict(report_as_of=date.today().isoformat(), rss_count=25,
                    rss_max_attempts=3, rss_timeout=30)
    assert config.load_config() == expected
    assert config.load_config(tmp_path / 'missing.json') == expected


@pytest.mark.parametrize('key', ['rss_count', 'rss_max_attempts', 'rss_timeout'])
@pytest.mark.parametrize('kind', ['bool', 'string', 'float', 'null', 'low', 'high'])
def test_integer_violations(tmp_path, key, kind):
    _, low, high = config.REGISTRY[key]
    value = {'bool': True, 'string': '3', 'float': 3.0, 'null': None,
             'low': low - 1, 'high': high + 1}[kind]
    with pytest.raises(config.ConfigError) as caught:
        config.load_config(write_config(tmp_path, {key: value}))
    assert key in str(caught.value)
    assert repr(value) in str(caught.value)
    assert 'expected an integer' in str(caught.value)


@pytest.mark.parametrize('value', ['2020-1-01', '2020-02-30', '', None, 20200101,
                                  (date.today() + timedelta(days=1)).isoformat()])
def test_date_invalid(tmp_path, value):
    with pytest.raises(config.ConfigError, match='report_as_of.*expected a real calendar date'):
        config.load_config(write_config(tmp_path, {'report_as_of': value}))


def test_valid_boundaries(tmp_path):
    for index in (1, 2):
        values = {key: spec[index] for key, spec in config.REGISTRY.items() if spec}
        values['report_as_of'] = '2020-02-29'
        assert config.load_config(write_config(tmp_path, values)) == values


def test_unknown_suggestion(tmp_path):
    with pytest.raises(config.ConfigError, match='did you mean rss_count'):
        config.load_config(write_config(tmp_path, {'rss_cout': 10}))


def test_env_wins(monkeypatch, tmp_path):
    write_config(tmp_path, {'rss_count': False, 'report_as_of': 'bad'})
    monkeypatch.setenv('JSOSIF_RSS_COUNT', '42')
    monkeypatch.setenv('JSOSIF_REPORT_AS_OF', '2020-01-01')
    result = config.load_config()
    assert result['rss_count'] == 42
    assert result['report_as_of'] == '2020-01-01'


@pytest.mark.parametrize('value', ['true', '3.5', '-1', '', '9' * 20])
def test_invalid_env(monkeypatch, value):
    monkeypatch.setenv('JSOSIF_RSS_COUNT', value)
    with pytest.raises(config.ConfigError, match='rss_count'):
        config.load_config()


def test_path_precedence(monkeypatch, tmp_path):
    default = write_config(tmp_path, {'rss_count': 10})
    selected = tmp_path / 'selected.json'
    selected.write_text('{"rss_count": 11}')
    monkeypatch.setenv('JSOSIF_CONFIG', str(selected))
    assert config.load_config()['rss_count'] == 11
    assert config.load_config(default)['rss_count'] == 10
    monkeypatch.setenv('JSOSIF_CONFIG', str(tmp_path / 'absent'))
    assert config.load_config()['rss_count'] == 25


def test_malformed_json(tmp_path):
    path = tmp_path / 'config.json'
    path.write_text('{\n"rss_count": }')
    with pytest.raises(config.ConfigError) as caught:
        config.load_config(path)
    assert str(path) in str(caught.value)
    assert 'line 2, column 14 (position 15)' in str(caught.value)


@pytest.mark.parametrize('value', [[], None, 12])
def test_object_required(tmp_path, value):
    with pytest.raises(config.ConfigError, match='expected a JSON object'):
        config.load_config(write_config(tmp_path, value))


def test_errors_sorted_and_complete(tmp_path):
    values = dict(rss_timeout=0, rss_max_attempts=False, rss_count=101,
                  report_as_of='bad', rss_cout=3)
    messages = []
    for payload in (values, dict(reversed(list(values.items())))):
        with pytest.raises(config.ConfigError) as caught:
            config.load_config(write_config(tmp_path, payload))
        messages.append(str(caught.value))
    assert messages[0] == messages[1]
    assert [line.split("'")[1] for line in messages[0].splitlines()] == sorted(values)


def test_startup_fails_before_work(tmp_path, monkeypatch, capsys):
    write_config(tmp_path, {'rss_count': 0})
    monkeypatch.setattr(run_phase1.subprocess, 'run', lambda *a, **k: pytest.fail('child started'))
    with pytest.raises(SystemExit) as caught:
        run_phase1.main()
    assert caught.value.code == 2
    assert 'rss_count' in capsys.readouterr().err


def test_startup_passes_normalized_settings(tmp_path, monkeypatch):
    write_config(tmp_path, {'report_as_of': '2020-01-01', 'rss_count': 12})
    monkeypatch.setattr(run_phase1, 'SUPPORTED', ['CSCO'])
    calls = []
    monkeypatch.setattr(run_phase1.subprocess, 'run', lambda *a, **k: calls.append(k))
    run_phase1.main()
    assert len(calls) == 6
    assert all(c['env']['REPORT_AS_OF'] == '2020-01-01' and
               c['env']['JSOSIF_RSS_COUNT'] == '12' for c in calls)


def test_rss_main_consumes_settings(monkeypatch):
    import ai_extract
    import data_utils
    monkeypatch.setenv('JSOSIF_RSS_COUNT', '12')
    monkeypatch.setenv('JSOSIF_RSS_MAX_ATTEMPTS', '2')
    monkeypatch.setenv('JSOSIF_RSS_TIMEOUT', '7')
    monkeypatch.setattr(data_utils, 'ticker_arg', lambda: 'CSCO')
    monkeypatch.setattr(data_utils, 'save', lambda *args: None)
    calls = []
    def fetch(*args, **kwargs):
        calls.append((args, kwargs))
        return [], {}
    monkeypatch.setattr(ai_extract, 'fetch_rss', fetch)
    monkeypatch.setattr(ai_extract, 'extract', lambda *args: {'extraction_stats': {}})
    ai_extract.main()
    assert calls[0][0][1] == 12
    assert calls[0][1] == {'max_attempts': 2, 'timeout': 7}
