"""Load sector teams from YAML: team key -> {name, email, sectors, role}."""
from pathlib import Path
import re

import yaml


DEFAULT_PATH = Path(__file__).resolve().parents[1] / 'config' / 'recipients.yaml'
EMAIL = re.compile(r"[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+"
                   r"(?:\.[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+)*@"
                   r"[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?"
                   r"(?:\.[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?)+")


class _UniqueLoader(yaml.SafeLoader):
    """Reject duplicate mapping keys before YAML can silently overwrite them."""

    def construct_mapping(self, node, deep=False):
        keys = set()
        for key_node, _ in node.value:
            key = self.construct_object(key_node, deep=deep)
            if not isinstance(key, str):
                raise ValueError(f'mapping keys must be strings at line {key_node.start_mark.line + 1}')
            if key in keys:
                raise ValueError(f'duplicate key {key!r} at line {key_node.start_mark.line + 1}')
            keys.add(key)
        return super().construct_mapping(node, deep=deep)


def validate(config) -> list[str]:
    """Return schema errors; duplicate YAML keys are checked by load_recipients.

    Team keys and display names must be nonblank and unique. Sectors are a
    nonempty list of nonblank strings; role is a nonblank, free-form string.
    Emails must be bare ASCII addresses with a dotted domain (no DNS lookup).
    """
    if not isinstance(config, dict) or not config:
        return ['config must be a nonempty mapping of team names to recipients']
    errors, names = [], set()
    for team, entry in config.items():
        if not isinstance(team, str) or not team.strip():
            errors.append(f'team {team!r}: team name must be a nonempty string')
        if not isinstance(entry, dict):
            errors.append(f'team {team!r}: recipient must be a mapping')
            continue
        for field in ('name', 'role'):
            value = entry.get(field)
            if not isinstance(value, str) or not value.strip():
                errors.append(f'team {team!r}: {field} must be a nonempty string')
        name = entry.get('name')
        if isinstance(name, str) and name.strip():
            if name in names:
                errors.append(f'team {team!r}: duplicate team name {name!r}')
            names.add(name)
        email = entry.get('email')
        if (not isinstance(email, str) or not EMAIL.fullmatch(email)
                or len(email) > 254 or len(email.split('@')[0]) > 64):
            errors.append(f'team {team!r}: email must be a valid bare email address')
        sectors = entry.get('sectors')
        if not isinstance(sectors, list) or not sectors or not all(
                isinstance(sector, str) and sector.strip() for sector in sectors):
            errors.append(f'team {team!r}: sectors must be a nonempty list of nonempty strings')
    return errors


def load_recipients(path=None) -> dict:
    """Read UTF-8 YAML, raising ValueError with a path for missing/invalid config.

    Omitted path uses config/recipients.yaml relative to the repository, not cwd.
    Loading an explicit path has no effect on subsequent default queries.
    """
    path = Path(path) if path is not None else DEFAULT_PATH
    try:
        config = yaml.load(path.read_text(encoding='utf-8'), Loader=_UniqueLoader)
    except (OSError, UnicodeError) as exc:
        raise ValueError(f'Cannot read recipients config {path}: {exc}') from None
    except (yaml.YAMLError, ValueError) as exc:
        raise ValueError(f'Invalid recipients config {path}: {exc}') from None
    errors = validate(config)
    if errors:
        raise ValueError(f'Invalid recipients config {path}:\n' + '\n'.join(errors))
    return config


def recipients_for_sector(sector) -> list[dict]:
    """Return matching recipient records in config order, using exact sector names.

    Read the default configuration on each call; unknown sectors return [].
    """
    return [entry for entry in load_recipients().values() if sector in entry['sectors']]
