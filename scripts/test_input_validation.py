"""Regression tests for pipeline entry input validation."""
from datetime import date, timedelta
from pathlib import Path
import runpy
import sys

import pytest

from data_utils import as_of_date, ticker_arg, SUPPORTED


INVALID_DATES = ['10/11/2026', '20261011', '', '2026-02-30',
                 '2025-02-29', '2026-1-01', '2026-01-01\n',
                 ' 2026-01-01', '0000-01-01']


@pytest.mark.parametrize('value', INVALID_DATES)
def test_invalid_date(monkeypatch, capsys, value):
    monkeypatch.setenv('REPORT_AS_OF', value)
    with pytest.raises(SystemExit) as exc:
        as_of_date()
    assert exc.value.code != 0
    error = capsys.readouterr().err
    assert 'REPORT_AS_OF' in error
    assert 'YYYY-MM-DD' in error
    assert repr(value) in error
    assert 'Traceback' not in error


def test_future_date(monkeypatch, capsys):
    value = (date.today() + timedelta(days=1)).isoformat()
    monkeypatch.setenv('REPORT_AS_OF', value)
    with pytest.raises(SystemExit) as exc:
        as_of_date()
    assert exc.value.code != 0
    error = capsys.readouterr().err
    assert 'future' in error
    assert 'YYYY-MM-DD' in error
    assert repr(value) in error


@pytest.mark.parametrize('value', ['2024-02-29', '2000-01-01', date.today().isoformat()])
def test_valid_date(monkeypatch, value):
    monkeypatch.setenv('REPORT_AS_OF', value)
    assert as_of_date() == date.fromisoformat(value)


def test_unset_date_defaults_to_today(monkeypatch):
    monkeypatch.delenv('REPORT_AS_OF', raising=False)
    assert as_of_date() == date.today()


@pytest.mark.parametrize('value, expected', [(' cScO ', 'CSCO'), (' cnq.To ', 'CNQ.TO')])
def test_ticker_normalization(monkeypatch, value, expected):
    monkeypatch.setattr(sys, 'argv', ['pipeline', '--ticker', value])
    assert ticker_arg() == expected


def test_default_ticker(monkeypatch):
    monkeypatch.setattr(sys, 'argv', ['pipeline'])
    assert ticker_arg() == SUPPORTED[0]


def test_unknown_ticker(monkeypatch, capsys):
    monkeypatch.setattr(sys, 'argv', ['pipeline', '--ticker', ' unknown '])
    with pytest.raises(SystemExit) as exc:
        ticker_arg()
    assert exc.value.code != 0
    error = capsys.readouterr().err
    assert 'invalid choice' in error
    assert 'UNKNOWN' in error


@pytest.mark.parametrize('script', ['quant.py', 'validate_phase1.py', 'regenerate_report.py'])
@pytest.mark.parametrize('value', INVALID_DATES + [(date.today() + timedelta(days=1)).isoformat()])
def test_entry_rejects_date_before_pipeline_work(monkeypatch, capsys, script, value):
    monkeypatch.setenv('REPORT_AS_OF', value)
    monkeypatch.setattr(sys, 'argv', [script])
    with pytest.raises(SystemExit) as exc:
        runpy.run_path(str(Path(__file__).with_name(script)), run_name='__main__')
    assert exc.value.code != 0
    error = capsys.readouterr().err
    assert 'REPORT_AS_OF' in error
    assert 'YYYY-MM-DD' in error
    assert repr(value) in error
    assert 'Traceback' not in error
