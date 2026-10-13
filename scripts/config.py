"""Small, strict pipeline configuration: environment > JSON file > defaults."""
from datetime import date
from difflib import get_close_matches
import json
import os
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
# Bounds limit feed size, exponential retry delays, and individual request waits.
REGISTRY = {
    'report_as_of': None,
    'rss_count': (25, 1, 100),
    'rss_max_attempts': (3, 1, 5),
    'rss_timeout': (30, 1, 120),
}


class ConfigError(ValueError):
    """Human-readable configuration errors, collected in key order."""


def load_config(path=None):
    """Load optional JSON; validate effective values and reject unknown file keys.

    An explicit path wins over JSOSIF_CONFIG, then the repository config.json.
    Missing files are allowed, including explicitly selected files.
    """
    path = Path(path if path is not None else os.environ.get('JSOSIF_CONFIG', ROOT / 'config.json'))
    try:
        values = json.loads(path.read_text(encoding='utf-8'))
    except FileNotFoundError:
        values = {}
    except json.JSONDecodeError as exc:
        raise ConfigError(f'Invalid config file {path}: expected valid JSON at line '
                          f'{exc.lineno}, column {exc.colno} (position {exc.pos}): {exc.msg}.') from None
    except (OSError, UnicodeError) as exc:
        raise ConfigError(f'Cannot read config file {path}: expected readable UTF-8 JSON '
                          f'({type(exc).__name__}).') from None
    if not isinstance(values, dict):
        raise ConfigError(f'Invalid config root: got {values!r}; expected a JSON object.')
    today = date.today()
    result, errors = {}, []
    for key in sorted(set(values) | set(REGISTRY)):
        if key not in REGISTRY:
            closest = get_close_matches(key, REGISTRY, n=1, cutoff=0)
            errors.append(f'Invalid config key {key!r}: got {values[key]!r}; expected a known key; '
                          f'did you mean {closest[0]}?')
            continue
        spec = REGISTRY[key]
        default = today.isoformat() if spec is None else spec[0]
        env_name = 'JSOSIF_' + key.upper()
        value = os.environ.get(env_name, values.get(key, default))
        received = value
        if spec is None:
            expected = f'a real calendar date in YYYY-MM-DD format, no later than today ({today})'
            valid = isinstance(value, str) and re.fullmatch(r'[0-9]{4}-[0-9]{2}-[0-9]{2}', value)
            if valid:
                try:
                    valid = date.fromisoformat(value) <= today
                except ValueError:
                    valid = False
        else:
            _, low, high = spec
            expected = f'an integer from {low} to {high} (not a boolean)'
            if env_name in os.environ and re.fullmatch(r'[0-9]+', value):
                # Bound length before conversion so huge inputs remain human errors.
                value = int(value) if len(value) < 10 else None
            valid = type(value) is int and low <= value <= high
        if valid:
            result[key] = value
        else:
            errors.append(f'Invalid config key {key!r}: got {received!r}; expected {expected}.')
    if errors:
        raise ConfigError('\n'.join(errors))
    return result


def startup_config():
    """Fail before pipeline work with a concise diagnostic and exit status 2."""
    import sys
    try:
        return load_config()
    except ConfigError as exc:
        print(str(exc), file=sys.stderr)
        raise SystemExit(2) from None
