from copy import deepcopy
from datetime import datetime, timedelta, timezone
import hashlib
import json
from pathlib import Path
import sys
from types import SimpleNamespace

import pytest

import benchmark_prices as prices
import benchmark_review as review
from shared_research_pack import digest
from universe import SUPPORTED

START = '2025-10-01'
END = '2025-10-08'
NOW = datetime(2025, 10, 10, 12, tzinfo=timezone.utc)


def provider(symbol, start=START, end=END):
    return {'symbol': symbol, 'currency': 'CAD' if symbol.endswith('.TO') else 'USD',
            'exchange_timezone': 'America/New_York', 'exchange_name': 'SYNTHETIC',
            'instrument_type': 'EQUITY' if symbol in SUPPORTED else 'ETF', 'provider_version': 'synthetic-test',
            'observations': [{'observed_on': start, 'value': 100},
                             {'observed_on': end, 'value': 110 if symbol in SUPPORTED else 105}]}


def sample(symbols=('CSCO', 'XLK'), fetcher=provider):
    return prices.capture(list(symbols), start=START, end=END, clock=lambda: NOW, fetcher=fetcher)


def rehash_capture(value):
    value['capture_id'] = digest({k:v for k,v in value.items() if k != 'capture_id'})
    return value


def rehash_review(value):
    value['review_id'] = digest({k:v for k,v in value.items() if k != 'review_id'})
    return value


def pair(value, stock='CSCO', benchmark='XLK'):
    return next(p for g in value['groups'] for p in g['pairs'] if (p['stock'], p['benchmark']) == (stock, benchmark))


def test_capture_calls_each_requested_symbol_once_and_sanitizes_fields():
    calls = []
    def fetch(symbol, start, end):
        calls.append((symbol, start, end))
        return dict(provider(symbol, start, end), private_token='DO-NOT-RETAIN')
    result = sample(('XLK', 'CSCO', 'CSCO'), fetch)
    assert calls == [('CSCO', START, END), ('XLK', START, END)]
    assert 'DO-NOT-RETAIN' not in json.dumps(result)
    assert result == sample()
    assert result['point_in_time_eligible'] is False


def test_failure_isolated_without_exception_details():
    def fetch(symbol, start, end):
        if symbol == 'CSCO': raise RuntimeError('secret-cookie?api_key=PRIVATE')
        return provider(symbol, start, end)
    result = sample(fetcher=fetch)
    assert [r['status'] for r in result['series']] == ['unavailable', 'observed']
    assert result['series'][0]['reason'] == 'PROVIDER_UNAVAILABLE'
    assert 'PRIVATE' not in json.dumps(result)
    assert pair(review.build(result))['result']['reason'] == 'Stock series: PROVIDER_UNAVAILABLE'


@pytest.mark.parametrize('field,value', [
    ('symbol','MSFT'), ('currency',None), ('currency','US$'), ('exchange_timezone','BAD/ZONE'),
    ('exchange_name','<script>'), ('instrument_type','ETF'), ('provider_version', 'secret?token=value'),
    ('observations',None), ('observations',[{'observed_on': START, 'value': 100, 'extra': 'secret'}]),
    ('observations',[{'observed_on': START, 'value': 100}, {'observed_on': START, 'value': 101}]),
    ('observations',[{'observed_on': '2025-09-30', 'value': 100}]),
])
def test_invalid_provider_metadata_is_a_sanitized_gap(field, value):
    result = sample(('CSCO',), lambda s,a,b: dict(provider(s,a,b), **{field:value}))
    assert result['series'][0]['status'] == 'unavailable'
    assert result['series'][0]['reason'] == 'DATA_VALIDATION_ERROR'
    assert result['series'][0]['observations'] == []


@pytest.mark.parametrize('price', [0,-1,True,'100',float('nan'),float('inf'),10**400])
def test_invalid_prices_cannot_enter_capture(price):
    def fetch(s,a,b):
        row = provider(s,a,b); row['observations'][0]['value'] = price
        return row
    assert sample(('CSCO',),fetch)['series'][0]['reason'] == 'DATA_VALIDATION_ERROR'


@pytest.mark.parametrize('rows', [[], [{'observed_on': START,'value':None}]])
def test_absent_and_null_prices_remain_missing(rows):
    value = sample(('CSCO',),lambda s,a,b: dict(provider(s,a,b), observations=rows))
    assert value['series'][0]['status'] == 'missing'
    assert pair(review.build(value))['result']['relative_return_pp'] is None


@pytest.mark.parametrize('start,end', [(END,START),(START,START),('2024-01-01',END),('2025-1-01',END),(START,'2025-10-10')])
def test_invalid_or_unfinished_window_rejected_before_fetch(start,end):
    calls = []
    with pytest.raises(ValueError):
        prices.capture(['CSCO'],start=start,end=end,clock=lambda:NOW,fetcher=lambda *args:calls.append(args))
    assert not calls


def test_exchange_local_day_gate_rejects_unclosed_requested_date():
    # UTC is Oct 10, but New York is still Oct 9; the requested local day is incomplete.
    value = prices.capture(['CSCO'],start=START,end='2025-10-09',fetcher=provider,
                           clock=lambda:datetime(2025,10,10,1,tzinfo=timezone.utc))
    assert value['series'][0]['reason'] == 'DATA_VALIDATION_ERROR'


@pytest.mark.parametrize('symbols', [[],['UNKNOWN'],['CSCO',None],['../CSCO'],'CSCO'])
def test_unknown_symbols_rejected(symbols):
    with pytest.raises(ValueError): sample(symbols) if isinstance(symbols,list) else prices.capture(symbols,start=START,end=END)


def test_naive_clock_and_reversed_capture_time_rejected():
    with pytest.raises(ValueError):
        prices.capture(['CSCO'],start=START,end=END,clock=lambda:NOW.replace(tzinfo=None),fetcher=provider)
    moments = iter([NOW,NOW,NOW-timedelta(seconds=1)])
    with pytest.raises(ValueError):
        prices.capture(['CSCO'],start=START,end=END,clock=lambda:next(moments),fetcher=provider)


@pytest.mark.parametrize('mutation', [
    lambda c:c.update(point_in_time_eligible=True),
    lambda c:c.update(finished_at=(NOW+timedelta(hours=2)).isoformat()),
    lambda c:c['series'].append(deepcopy(c['series'][0])),
    lambda c:c['series'][0].update(retrieved_at=(NOW+timedelta(seconds=1)).isoformat()),
    lambda c:c['series'][0].update(adjustment_basis='raw_close'),
    lambda c:c['series'][0].update(status='missing'),
    lambda c:c['series'][0].update(source_url='https://example.com/?token=PRIVATE'),
    lambda c:c['series'][0]['observations'].reverse(),
])
def test_rehashed_invalid_capture_fails_validation(mutation):
    value = sample(); mutation(value); rehash_capture(value)
    with pytest.raises(ValueError): prices.validate_capture(value)


def test_exact_return_percent_and_percentage_points_with_full_coverage_gaps():
    value = review.build(sample())
    assert value['coverage'] == dict(stocks=50,groups=8,pairs=59,available_pairs=1,missing_pairs=58,captured_series=2)
    result = pair(value)['result']
    assert result['stock_return_pct'] == pytest.approx(10)
    assert result['benchmark_return_pct'] == pytest.approx(5)
    assert result['relative_return_pp'] == pytest.approx(5)
    assert result['currency'] == 'USD'
    assert value['delivery_ready'] is False and value['point_in_time_eligible'] is False
    assert pair(value)['stock_series_id'] == digest(value['capture']['series'][0])
    assert pair(value,'JPM','XLF')['result']['reason'] == 'Stock series was not captured'


def test_consumer_candidates_remain_separate_and_cad_requires_fx_evidence():
    value = review.build(sample(('COST','XLP','XLY','BMO.TO','XLF')))
    assert value['coverage']['available_pairs'] == 2
    assert pair(value,'COST','XLP')['result']['status'] == 'available'
    assert pair(value,'COST','XLY')['result']['status'] == 'available'
    assert pair(value,'BMO.TO','XLF')['result']['reason'] == 'Currency conversion evidence is required'
    assert all(p['benchmark_status']=='proposed' for g in value['groups'] for p in g['pairs'])


def test_matching_nonconfigured_currency_does_not_activate_candidate():
    value = review.build(sample(fetcher=lambda s,a,b: dict(provider(s,a,b),currency='CAD')))
    result = pair(value)['result']
    assert result['status'] == 'missing' and result['relative_return_pp'] is None
    assert result['reason'] == 'Candidate currency differs from configured currency'


@pytest.mark.parametrize('mode',['drop','null','nearby'])
def test_missing_endpoints_are_not_forward_filled(mode):
    def fetch(s,a,b):
        row = provider(s,a,b)
        if s == 'CSCO':
            if mode=='drop': row['observations'].pop()
            if mode=='null': row['observations'][-1]['value'] = None
            if mode=='nearby': row['observations'][-1]['observed_on'] = '2025-10-07'
        return row
    result = pair(review.build(sample(fetcher=fetch)))['result']
    assert result['status']=='missing' and result['reason']=='Exact observation endpoints are unavailable'


@pytest.mark.parametrize('mutation', [
    lambda r:r.update(delivery_ready=True),
    lambda r:r['coverage'].update(available_pairs=59),
    lambda r:pair(r)['result'].update(relative_return_pp=20),
    lambda r:pair(r).update(stock_series_id='0'*64),
    lambda r:r['configuration'][0].update(name='Altered'),
    lambda r:r['groups'].pop(),
])
def test_rehashed_review_cannot_change_derived_returns_or_readiness(mutation):
    value = review.build(sample()); mutation(value); rehash_review(value)
    with pytest.raises(ValueError): review.validate(value)


def test_bundles_roundtrip_deterministically_without_provider_calls(tmp_path,monkeypatch):
    capture = sample()
    prices.write_bundle(capture,tmp_path/'capture')
    monkeypatch.setattr(prices,'fetch_history',lambda *args:pytest.fail('Offline review called provider'))
    value = review.build(prices.load_bundle(tmp_path/'capture'))
    for name in ('first','second'): review.write_bundle(value,tmp_path/name)
    assert review.load_bundle(tmp_path/'first') == value
    assert {p.name:p.read_bytes() for p in (tmp_path/'first').iterdir()} == {p.name:p.read_bytes() for p in (tmp_path/'second').iterdir()}
    text = (tmp_path/'first'/'benchmark-review.md').read_text()
    assert 'Difference (pp)' in text and '1 / 59' in text and 'Consumer ETF blend' in text
    with pytest.raises(FileExistsError): review.write_bundle(value,tmp_path/'first')
    with pytest.raises(FileExistsError): prices.write_bundle(capture,tmp_path/'capture')


@pytest.mark.parametrize('kind',['capture','review'])
def test_checksum_and_symlink_escape_rejected(tmp_path,kind):
    module = prices if kind=='capture' else review
    value = sample() if kind=='capture' else review.build(sample())
    module.write_bundle(value,tmp_path/'bundle')
    filename = 'prices.json' if kind=='capture' else 'benchmark-review.json'
    target = tmp_path/'bundle'/filename
    original = target.read_bytes(); target.write_bytes(original+b' ')
    with pytest.raises(ValueError,match='checksum'): module.load_bundle(tmp_path/'bundle')
    target.unlink(); (tmp_path/'outside.json').write_bytes(original); target.symlink_to(tmp_path/'outside.json')
    with pytest.raises(ValueError): module.load_bundle(tmp_path/'bundle')


def test_rehashed_markdown_cannot_lie_about_results(tmp_path):
    review.write_bundle(review.build(sample()),tmp_path/'review')
    path = tmp_path/'review'/'benchmark-review.md'; path.write_text('All benchmarks approved!')
    manifest_path = tmp_path/'review'/'manifest.json'; manifest = json.loads(manifest_path.read_text())
    manifest['files'][path.name] = hashlib.sha256(path.read_bytes()).hexdigest(); manifest_path.write_text(json.dumps(manifest))
    with pytest.raises(ValueError,match='rendered content'): review.load_bundle(path.parent)


def test_capture_cli_refuses_existing_output_before_network(tmp_path,monkeypatch):
    monkeypatch.setattr(sys,'argv',['benchmark_prices.py','--symbols','CSCO','--start',START,'--end',END,'--output',str(tmp_path)])
    monkeypatch.setattr(prices,'fetch_history',lambda *args:pytest.fail('Network called before destination validation'))
    with pytest.raises(SystemExit) as error: prices.main()
    assert error.value.code == 2


def test_review_cli_cannot_write_inside_capture(tmp_path,monkeypatch):
    prices.write_bundle(sample(),tmp_path/'capture')
    monkeypatch.setattr(sys,'argv',['benchmark_review.py','--capture',str(tmp_path/'capture'),'--output',str(tmp_path/'capture'/'nested')])
    with pytest.raises(SystemExit) as error: review.main()
    assert error.value.code == 2 and not (tmp_path/'capture'/'nested').exists()


def test_provider_adapter_uses_inclusive_window_adjusted_prices_and_local_dates(monkeypatch):
    import pandas as pd
    import yfinance
    calls = []
    class Ticker:
        history_metadata = dict(symbol='CSCO', currency='USD', exchangeTimezoneName='America/New_York',
                                exchangeName='NMS', instrumentType='EQUITY')
        def history(self, **kwargs):
            calls.append(kwargs)
            return pd.DataFrame({'Close':[100,float('nan')]},index=pd.to_datetime(['2025-10-02T01:00Z','2025-10-08T04:00Z']))
    monkeypatch.setattr(yfinance,'Ticker',lambda s:Ticker())
    raw = prices.fetch_history('CSCO',START,END)
    assert calls == [dict(start=START,end='2025-10-09',interval='1d',auto_adjust=True,actions=False,
                          repair=False,keepna=True,timeout=15,raise_errors=True)]
    assert raw['observations'] == [{'observed_on':START,'value':100.0},{'observed_on':END,'value':None}]


def test_provider_adapter_rejects_naive_bar_dates(monkeypatch):
    import pandas as pd
    import yfinance
    ticker = SimpleNamespace(history_metadata={'exchangeTimezoneName':'America/New_York'},
                             history=lambda **kwargs:pd.DataFrame({'Close':[100]},index=pd.to_datetime([START])))
    monkeypatch.setattr(yfinance,'Ticker',lambda s:ticker)
    with pytest.raises(ValueError,match='timezone'): prices.fetch_history('CSCO',START,END)


@pytest.mark.parametrize('module,filename',[(prices,'prices.json'),(review,'benchmark-review.json')])
def test_oversized_inputs_and_repository_output_rejected(tmp_path,monkeypatch,module,filename):
    value = sample() if module is prices else review.build(sample())
    module.write_bundle(value,tmp_path/'bundle')
    monkeypatch.setattr(module,'MAX_BYTES',10)
    with pytest.raises(ValueError,match='size limit'): module.load_bundle(tmp_path/'bundle')
    with pytest.raises(ValueError,match='outside the repository'): module.write_bundle(value,module.ROOT/'unsafe-output')


def test_manifest_cannot_redirect_capture_path(tmp_path):
    prices.write_bundle(sample(),tmp_path/'bundle')
    path = tmp_path/'bundle'/'manifest.json'; value = json.loads(path.read_text())
    value['json'] = '../prices.json'; path.write_text(json.dumps(value))
    with pytest.raises(ValueError,match='manifest'): prices.load_bundle(path.parent)


def test_committed_capture_is_explicitly_synthetic_and_reproducible():
    value = prices.load_bundle(Path(__file__).parent/'fixtures'/'benchmark_prices_synthetic')
    assert value == sample()
    assert value['capture_mode'] == 'injected_fetcher'
    assert all(r['provider_version']=='synthetic-test' for r in value['series'])
    assert review.build(value)['coverage']['available_pairs'] == 1
    assert 'Synthetic/injected fixture' in review.markdown(review.build(value))
