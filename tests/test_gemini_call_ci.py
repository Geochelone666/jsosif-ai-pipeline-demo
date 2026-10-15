"""Tests for scripts/gemini_call_ci.py (Gemini REST wrapper for CI)."""

import io
import json
import os
import sys
import urllib.error

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))
import gemini_call_ci as gc


def test_parse_args_prompt_file(tmp_path):
    prompt_file = tmp_path / 'prompt.txt'
    prompt_file.write_text('hello world')
    model, prompt, want_json = gc.parse_args(
        ['--model', 'gemini-3.5-flash-lite', '--json-output',
         '--prompt', '@' + str(prompt_file)])
    assert model == 'gemini-3.5-flash-lite'
    assert prompt == 'hello world'
    assert want_json is True


def test_parse_args_inline_prompt():
    model, prompt, _ = gc.parse_args(
        ['--model', 'm', '--prompt', 'inline text'])
    assert prompt == 'inline text'


def test_main_fail_closed_without_key(monkeypatch, capsys):
    monkeypatch.delenv('GEMINI_API_KEY', raising=False)
    rc = gc.main(['--model', 'm', '--json-output', '--prompt', 'x'])
    assert rc == 2
    assert 'GEMINI_API_KEY' in capsys.readouterr().err


def test_main_usage_without_model(monkeypatch, capsys):
    monkeypatch.setenv('GEMINI_API_KEY', 'dummy')
    rc = gc.main(['--json-output'])
    assert rc == 2


def test_call_gemini_extracts_text(monkeypatch):
    fake_payload = {
        'candidates': [{
            'content': {'parts': [{'text': '{"a": 1}'}, {'text': ' more'}]}
        }]
    }

    class FakeResp:
        def read(self):
            return json.dumps(fake_payload).encode('utf-8')

        def __enter__(self):
            return self

        def __exit__(self, *a):
            return False

    monkeypatch.setattr(
        gc.urllib.request, 'urlopen', lambda req, timeout=None: FakeResp())
    assert gc.call_gemini('key', 'm', 'prompt') == '{"a": 1} more'


def test_call_gemini_http_error(monkeypatch):
    def boom(req, timeout=None):
        raise urllib.error.HTTPError(
            req.full_url, 429, 'Too Many Requests', {},
            io.BytesIO(b'{"error": {"message": "quota"}}'))

    monkeypatch.setattr(gc.urllib.request, 'urlopen', boom)
    with pytest.raises(RuntimeError, match='Gemini HTTP 429'):
        gc.call_gemini('key', 'm', 'prompt')


def test_main_prints_envelope(monkeypatch, capsys):
    monkeypatch.setenv('GEMINI_API_KEY', 'dummy')
    monkeypatch.setattr(gc, 'call_gemini',
                        lambda key, model, prompt, timeout=120: '{"ok": true}')
    rc = gc.main(['--model', 'm', '--json-output', '--prompt', 'hi'])
    assert rc == 0
    # stdout must be the {"text": ...} envelope ai_extract.py parses
    out = json.loads(capsys.readouterr().out)
    assert out == {'text': '{"ok": true}'}
