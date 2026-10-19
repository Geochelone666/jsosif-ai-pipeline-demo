#!/usr/bin/env python3
"""Check frozen snapshot sidecars and repeat builds to detect format or output drift."""
import argparse
import json
from importlib import import_module
from pathlib import Path

try:
    snapshot_contract = import_module(
        f'{__package__}.snapshot_contract' if __package__ else 'snapshot_contract')
except ModuleNotFoundError as exc:
    if exc.name != (f'{__package__}.snapshot_contract' if __package__ else 'snapshot_contract'):
        raise
    snapshot_contract = None

validate_snapshot = getattr(snapshot_contract, 'validate_snapshot', None)

REQUIRED_TOP_LEVEL = ('contract_version', 'identity', 'quant', 'ai_summary',
                      'freshness', 'disclaimer')
REQUIRED_IDENTITY = ('ticker', 'as_of', 'report_stamp')


def check_snapshot_payload(payload) -> list[str]:
    """Return contract errors, retaining basic protection before the shared contract lands."""
    if validate_snapshot is not None:
        return validate_snapshot(payload)
    if not isinstance(payload, dict):
        return ['snapshot must be an object']
    errors = [f'{key}: required field missing' for key in REQUIRED_TOP_LEVEL if key not in payload]
    identity = payload.get('identity')
    if not isinstance(identity, dict):
        errors.append('identity must be an object')
    else:
        for key in REQUIRED_IDENTITY:
            value = identity.get(key)
            if not isinstance(value, str) or not value.strip():
                errors.append(f'identity.{key}: must be a nonempty string')
    disclaimer = payload.get('disclaimer')
    if not isinstance(disclaimer, str) or not disclaimer.strip():
        errors.append('disclaimer: must be a nonempty string')
    return errors


def check_reports_dir(path) -> dict:
    """Validate matching sidecars independently so one corrupt file cannot hide others."""
    path = Path(path)
    result = {'checked': 0, 'passed': 0, 'failed': []}
    if not path.is_dir():
        result['failed'].append({'file': str(path), 'errors': ['reports directory does not exist or is not a directory']})
        return result
    try:
        files = sorted(path.iterdir())
    except OSError as exc:
        result['failed'].append({'file': str(path), 'errors': [str(exc)]})
        return result
    for file in files:
        if not file.match('*-intelligence-*.json') or not file.is_file():
            continue
        result['checked'] += 1
        try:
            payload = json.loads(file.read_text(encoding='utf-8'))
        except (OSError, ValueError) as exc:
            errors = [f'Cannot read snapshot JSON: {exc}']
        else:
            errors = check_snapshot_payload(payload)
        if errors:
            result['failed'].append({'file': str(file), 'errors': errors})
        else:
            result['passed'] += 1
    if not result['checked']:
        result['failed'].append({'file': str(path), 'errors': ['No snapshot sidecars found']})
    return result


def determinism_check(emit_fn, *args, **kwargs) -> bool:
    """Compare two sorted JSON byte strings to catch noise in repeat builds.

    Serialize each result immediately: emitters may reuse a mutable output object.
    Callers provide the emitter and its inputs; no source data is refreshed here.
    """
    first = json.dumps(emit_fn(*args, **kwargs), sort_keys=True).encode('utf-8')
    second = json.dumps(emit_fn(*args, **kwargs), sort_keys=True).encode('utf-8')
    return first == second


def main(argv=None):
    """Print actionable file errors and fail the CLI when a snapshot violates the gate."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('reports_dir', type=Path)
    args = parser.parse_args(argv)
    result = check_reports_dir(args.reports_dir)
    print(f"checked={result['checked']} passed={result['passed']} failed={len(result['failed'])}")
    for failure in result['failed']:
        for error in failure['errors']:
            print(f"{failure['file']}: {error}")
    if result['failed']:
        raise SystemExit(1)
    return 0


if __name__ == '__main__':
    main()
