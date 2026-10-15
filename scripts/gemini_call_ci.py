#!/usr/bin/env python3
"""Gemini REST wrapper for GitHub Actions CI.

ai_extract.py invokes a CLI entrypoint as::

    <GEMINI_CLI> --model <model> --json-output --prompt @<prompt-file>

On developer machines GEMINI_CLI points at a local gemini-call.py; on the
GitHub runner there is no local CLI, so this script fills that role using the
Gemini REST API (stdlib only — no extra dependencies beyond requirements.txt).

It reads the API key from GEMINI_API_KEY (fail-closed when unset) and prints
``{"text": "<model output>"}`` to stdout, which is the envelope shape
ai_extract.py parses.

Usage (set by the weekly workflow):
    GEMINI_CLI=${{ github.workspace }}/scripts/gemini_call_ci.py
    GEMINI_API_KEY=${{ secrets.GEMINI_API_KEY }}
"""

import json
import os
import sys
import urllib.request
import urllib.error

API_BASE = 'https://generativelanguage.googleapis.com/v1beta'


def parse_args(argv):
    """Parse the subset of flags ai_extract.py passes."""
    model, prompt, want_json = None, None, False
    i = 0
    while i < len(argv):
        arg = argv[i]
        if arg == '--model' and i + 1 < len(argv):
            model = argv[i + 1]
            i += 2
        elif arg == '--prompt' and i + 1 < len(argv):
            prompt = argv[i + 1]
            i += 2
        elif arg == '--json-output':
            want_json = True
            i += 1
        else:
            i += 1
    if prompt and prompt.startswith('@'):
        with open(prompt[1:], 'r', encoding='utf-8') as fh:
            prompt = fh.read()
    return model, prompt, want_json


def call_gemini(api_key, model, prompt, timeout=120):
    """POST to generateContent; return the model's text output."""
    url = f'{API_BASE}/models/{model}:generateContent?key={api_key}'
    body = json.dumps({'contents': [{'parts': [{'text': prompt}]}]}).encode('utf-8')
    req = urllib.request.Request(
        url, data=body,
        headers={'Content-Type': 'application/json', 'User-Agent': 'jsosif-ci/1.0'},
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            payload = json.loads(resp.read().decode('utf-8'))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode('utf-8', 'replace')[:500]
        raise RuntimeError(f'Gemini HTTP {exc.code}: {detail}')
    except OSError as exc:
        raise RuntimeError(f'Gemini request failed: {exc}')
    try:
        parts = payload['candidates'][0]['content']['parts']
        return ''.join(p.get('text', '') for p in parts)
    except (KeyError, IndexError, TypeError) as exc:
        raise RuntimeError(
            f'Gemini response missing text: {str(payload)[:300]} ({exc})')


def main(argv):
    api_key = os.environ.get('GEMINI_API_KEY', '').strip()
    if not api_key:
        print('GEMINI_API_KEY is not set; refusing to run (fail-closed).',
              file=sys.stderr)
        return 2
    model, prompt, _want_json = parse_args(argv)
    if not model or not prompt:
        print('usage: gemini_call_ci.py --model <model> --json-output '
              '--prompt @<file>', file=sys.stderr)
        return 2
    try:
        text = call_gemini(api_key, model, prompt)
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    # Envelope shape ai_extract.py expects: {"text": "<inner JSON>"}
    print(json.dumps({'text': text}))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
