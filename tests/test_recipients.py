"""Contracts for sector team recipient configuration."""
import importlib
from pathlib import Path
import sys

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))


@pytest.fixture
def recipients():
    return importlib.import_module('recipients')


@pytest.fixture
def config():
    return {'technology': dict(name='Technology Team', email='team-tech@example.com',
                               sectors=['technology', 'energy'], role='analyst')}


def write_config(tmp_path, config):
    import yaml
    path = tmp_path / 'recipients.yaml'
    path.write_text(yaml.safe_dump(config), encoding='utf-8')
    return path


def test_load(recipients, config, tmp_path):
    assert recipients.validate(config) == []
    assert recipients.load_recipients(write_config(tmp_path, config)) == config


@pytest.mark.parametrize('field, value', [('email', 'invalid'), ('sectors', [])])
def test_invalid_fields(recipients, config, tmp_path, field, value):
    config['technology'][field] = value
    assert any(field in error for error in recipients.validate(config))
    with pytest.raises(ValueError, match=field):
        recipients.load_recipients(write_config(tmp_path, config))


def test_duplicate_team_key(recipients, config, tmp_path):
    path = write_config(tmp_path, config)
    path.write_text(path.read_text() * 2, encoding='utf-8')
    with pytest.raises(ValueError, match='duplicate.*technology'):
        recipients.load_recipients(path)


def test_sector_query(recipients, config, tmp_path, monkeypatch):
    config['healthcare'] = dict(name='Healthcare Team', email='team-health@example.com',
                                sectors=['healthcare', 'energy'], role='analyst')
    monkeypatch.setattr(recipients, 'DEFAULT_PATH', write_config(tmp_path, config))
    assert recipients.recipients_for_sector('technology') == [config['technology']]
    assert recipients.recipients_for_sector('healthcare') == [config['healthcare']]
    assert sorted(row['name'] for row in recipients.recipients_for_sector('energy')) == [
        'Healthcare Team', 'Technology Team']
    assert recipients.recipients_for_sector('unknown') == []
