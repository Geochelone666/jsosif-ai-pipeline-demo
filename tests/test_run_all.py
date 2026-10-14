"""Offline contracts for the three-stage command; no market data or mail IO."""
import argparse
from contextlib import ExitStack
import importlib
from pathlib import Path
import re
import subprocess
import sys
from types import ModuleType
from unittest.mock import patch

import pytest

SCRIPTS = Path(__file__).resolve().parents[1] / 'scripts'
sys.path.insert(0, str(SCRIPTS))


def optional_module(name):
    """Only an absent sibling is skippable; broken imports must fail."""
    if not (SCRIPTS / f'{name}.py').exists():
        pytest.skip(f'{name}.py is still being implemented')
    return importlib.import_module(name)


def invoke(module, argv=()):
    try:
        return module.main(list(argv))
    except SystemExit as exc:
        return exc.code


def events(output):
    return re.findall(r'^STAGE\s+([123])\b[^\n]*?\b(START|DONE)\b', output, re.M)


EXPECTED = [(str(n), event) for n in (1, 2, 3) for event in ('START', 'DONE')]


@pytest.fixture
def flow(tmp_path, monkeypatch):
    runner = optional_module('run_all')
    mail = importlib.import_module('scripts.email_delivery')
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(runner, 'ROOT', tmp_path)
    calls = []
    parsed = []
    failure = {'stage': None}
    artifacts = [tmp_path / 'reports' / 'stage1.marker',
                 tmp_path / 'bundle' / '20261014' / 'stage2.marker',
                 tmp_path / 'preview.eml']

    def stage(number):
        calls.append(number)
        if failure['stage'] == number:
            raise RuntimeError(f'stage {number} injected failure')
        target = artifacts[number - 1]
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(f'stage {number}\n')
        return str(artifacts[1].parent)

    def child(command, *args, **kwargs):
        tokens = [str(token) for token in command]
        assert '--send' not in tokens and '--really-send' not in tokens
        names = {Path(token).name for token in tokens}
        if 'run_phase1.py' in names:
            stage(1)
        elif 'bundle_reports.py' in names:
            stage(2)
        elif 'email_delivery.py' in names:
            stage(3)
        else:
            pytest.fail(f'Unexpected subprocess: {tokens}')
        return subprocess.CompletedProcess(command, 0, stdout='', stderr='')

    original_parse = argparse.ArgumentParser.parse_args

    def parse(parser, *args, **kwargs):
        result = original_parse(parser, *args, **kwargs)
        parsed.append(result)
        return result

    bundler = ModuleType('scripts.bundle_reports')
    bundler.bundle_reports = lambda *a, **k: stage(2)
    with ExitStack() as stack:
        stack.enter_context(patch.dict(sys.modules, {'scripts.bundle_reports': bundler}))
        stack.enter_context(patch.object(mail, 'load_recipients', return_value=['analyst@example.com']))
        stack.enter_context(patch.object(mail, 'build_email'))
        stack.enter_context(patch.object(mail.DryRunBackend, 'deliver', side_effect=lambda *a, **k: stage(3)))
        transport = stack.enter_context(patch.object(mail, 'send'))
        stack.enter_context(patch('subprocess.run', side_effect=child))
        stack.enter_context(patch('subprocess.Popen', side_effect=AssertionError('Unmocked process')))
        stack.enter_context(patch('socket.create_connection', side_effect=AssertionError('Network attempted')))
        stack.enter_context(patch('socket.socket.connect', side_effect=AssertionError('Network attempted')))
        stack.enter_context(patch.object(argparse.ArgumentParser, 'parse_args', parse))
        # Support either an imported bundle function or a subprocess stage.
        if hasattr(runner, 'bundle_reports') and callable(runner.bundle_reports):
            stack.enter_context(patch.object(runner, 'bundle_reports', side_effect=lambda *a, **k: stage(2)))
        yield runner, calls, artifacts, failure, transport, parsed


def test_stage_order(flow, capsys):
    runner, calls, *_ = flow
    assert invoke(runner) in (None, 0)
    assert events(capsys.readouterr().out) == EXPECTED
    assert calls == [1, 2, 3]


def test_repeat_run_is_identical_without_duplicates(flow, capsys, tmp_path):
    runner, calls, *_ = flow
    assert invoke(runner) in (None, 0)
    first_output = capsys.readouterr()
    first = {p.relative_to(tmp_path): p.read_bytes() for p in tmp_path.rglob('*') if p.is_file()}
    assert len(first) == 3
    assert invoke(runner) in (None, 0)
    assert capsys.readouterr() == first_output
    assert {p.relative_to(tmp_path): p.read_bytes() for p in tmp_path.rglob('*') if p.is_file()} == first
    assert calls == [1, 2, 3, 1, 2, 3]


def test_each_stage_leaves_its_artifact(flow):
    runner, _, artifacts, *_ = flow
    assert invoke(runner) in (None, 0)
    for number, artifact in enumerate(artifacts, 1):
        assert artifact.read_text() == f'stage {number}\n'


def test_default_flow_never_enables_send(flow):
    runner, calls, _, _, transport, parsed = flow
    assert invoke(runner) in (None, 0)
    assert calls == [1, 2, 3]
    assert parsed and parsed[0].really_send is False
    transport.assert_not_called()


def test_really_send_option_is_documented(flow, capsys):
    assert invoke(flow[0], ['--help']) == 0
    assert '--really-send' in capsys.readouterr().out
    assert flow[1] == []
    flow[4].assert_not_called()


@pytest.mark.parametrize('number', [1, 2, 3])
def test_failure_names_stage_and_stops(flow, capsys, number):
    runner, calls, artifacts, failure, transport, _ = flow
    failure['stage'] = number
    status = invoke(runner)
    assert status not in (None, 0)
    captured = capsys.readouterr()
    assert re.search(rf'stage\s+{number}\b', captured.out + captured.err, re.I)
    assert events(captured.out) == EXPECTED[:2 * number - 1]
    assert calls == list(range(1, number + 1))
    assert all(not p.exists() for p in artifacts[number - 1:])
    transport.assert_not_called()


@pytest.mark.parametrize('flags', [[], ['--dry-run']])
def test_email_default_and_dry_run_cannot_reach_transport(flags):
    mail = importlib.import_module('scripts.email_delivery')
    with patch.object(mail, 'send') as send, \
            patch.object(mail, 'load_recipients', return_value=['analyst@example.com']), \
            patch.object(mail, 'build_email') as build, \
            patch.object(mail.DryRunBackend, 'deliver') as preview:
        mail.main(['ACN-intelligence-20261014.md', *flags])
        preview.assert_called_once_with(build.return_value)
        send.assert_not_called()


def test_email_transport_spy_detects_explicit_send():
    mail = importlib.import_module('scripts.email_delivery')
    with patch.object(mail, 'send', side_effect=RuntimeError('send sentinel')) as send:
        with pytest.raises(RuntimeError, match='send sentinel'):
            mail.main(['ACN-intelligence-20261014.md', '--send'])
        send.assert_called_once()


def test_bundle_is_dated_and_idempotent(tmp_path, monkeypatch):
    bundle = optional_module('bundle_reports')
    monkeypatch.chdir(tmp_path)
    reports = tmp_path / 'reports'
    reports.mkdir()
    (reports / 'ACN-intelligence-20261014.md').write_text('# ACN\n')
    first = bundle.bundle_reports()
    assert isinstance(first, str)
    target = Path(first)
    assert target.is_dir()
    assert re.search(r'\d{4}-?\d{2}-?\d{2}', target.name)
    before = {p.relative_to(target): p.read_bytes() for p in target.rglob('*') if p.is_file()}
    assert before
    assert bundle.bundle_reports() == first
    assert {p.relative_to(target): p.read_bytes() for p in target.rglob('*') if p.is_file()} == before
    assert len(list((tmp_path / 'bundle').iterdir())) == 1


def test_no_argument_entry_point_defaults_to_no_send(flow):
    runner, calls, _, _, transport, parsed = flow
    with patch.object(sys, 'argv', ['scripts/run_all.py']):
        assert runner.main() in (None, 0)
    assert parsed[0].really_send is False
    assert calls == [1, 2, 3]
    transport.assert_not_called()
