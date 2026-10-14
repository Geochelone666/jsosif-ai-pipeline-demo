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


@pytest.mark.parametrize('email', [None, 12, '', 'team@example', 'team@@example.com',
                                  'team @example.com', 'team@example.com\n',
                                  'Team <team@example.com>', '.team@example.com',
                                  'team..tech@example.com', 'team@-example.com'])
def test_invalid_email_formats(recipients, config, email):
    config['technology']['email'] = email
    assert any('email' in error for error in recipients.validate(config))


@pytest.mark.parametrize('sectors', [None, 'technology', {}, [''], [' '], [1],
                                    ['technology', None]])
def test_invalid_sector_types(recipients, config, sectors):
    config['technology']['sectors'] = sectors
    assert any('sectors' in error for error in recipients.validate(config))


@pytest.mark.parametrize('config', [None, {}, [], 'technology', 42,
                                   {'technology': None}, {'': {}}, {1: {}}])
def test_invalid_schema(recipients, config, tmp_path):
    assert recipients.validate(config)
    with pytest.raises(ValueError, match='config'):
        recipients.load_recipients(write_config(tmp_path, config))


@pytest.mark.parametrize('field', ['name', 'email', 'sectors', 'role'])
def test_required_fields(recipients, config, field):
    del config['technology'][field]
    assert any(field in error for error in recipients.validate(config))


def test_duplicate_display_name(recipients, config, tmp_path):
    config['another'] = dict(config['technology'], email='team-another@example.com')
    assert any('duplicate team name' in error for error in recipients.validate(config))
    with pytest.raises(ValueError, match='duplicate team name'):
        recipients.load_recipients(write_config(tmp_path, config))


@pytest.mark.parametrize('content', ['', 'technology: [', 'technology: {}\n---\nenergy: {}',
                                     'technology: !!python/object:builtins.object {}',
                                     'technology: {email: a, email: b}', '? [a, b]\n: {}'])
def test_invalid_yaml(recipients, tmp_path, content):
    path = tmp_path / 'recipients.yaml'
    path.write_text(content, encoding='utf-8')
    with pytest.raises(ValueError) as caught:
        recipients.load_recipients(path)
    assert str(path) in str(caught.value)


def test_read_errors(recipients, tmp_path, monkeypatch):
    path = tmp_path / 'missing.yaml'
    monkeypatch.setattr(recipients, 'DEFAULT_PATH', path)
    with pytest.raises(ValueError, match='Cannot read recipients config') as caught:
        recipients.recipients_for_sector('technology')
    assert str(path) in str(caught.value)
    path.write_bytes(b'\xff')
    with pytest.raises(ValueError, match='Cannot read recipients config'):
        recipients.load_recipients(path)
    with pytest.raises(ValueError, match='Cannot read recipients config'):
        recipients.load_recipients(tmp_path)


def test_example_config_from_other_directory(recipients, tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    config = recipients.load_recipients()
    assert 3 <= len(config) <= 4
    assert recipients.validate(config) == []
    assert all(row['email'].startswith('team-') and row['email'].endswith('@example.com')
               for row in config.values())
    for sector in ('technology', 'healthcare', 'energy'):
        assert recipients.recipients_for_sector(sector)


def test_load_has_no_global_state_and_query_reloads(recipients, config, tmp_path, monkeypatch):
    path = write_config(tmp_path, config)
    monkeypatch.setattr(recipients, 'DEFAULT_PATH', path)
    first = recipients.recipients_for_sector('technology')
    first[0]['sectors'].clear()
    assert recipients.recipients_for_sector('technology') == [config['technology']]
    other = tmp_path / 'other'
    other.mkdir()
    changed = {'energy': dict(config['technology'], sectors=['energy'])}
    recipients.load_recipients(str(write_config(other, changed)))
    assert recipients.recipients_for_sector('technology') == [config['technology']]
    write_config(tmp_path, changed)
    assert recipients.recipients_for_sector('technology') == []
    assert recipients.recipients_for_sector('energy') == [changed['energy']]


def test_collects_errors_without_mutation(recipients, config):
    from copy import deepcopy
    config['technology'].update(email='invalid', sectors=[], role=' ')
    before = deepcopy(config)
    errors = recipients.validate(config)
    assert len(errors) == 3
    assert all('technology' in error for error in errors)
    assert config == before
