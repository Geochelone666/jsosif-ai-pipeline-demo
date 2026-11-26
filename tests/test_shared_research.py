from datetime import date,datetime,timezone
import json
from pathlib import Path
import pytest
from research_data import PriceObservation,relative_performance
from universe import SUPPORTED

A=date(2026,10,1);B=date(2026,10,8)
def row(t,d,value,c='USD'):
 return PriceObservation(t,d,value,c,datetime(2026,10,9,tzinfo=timezone.utc),'https://example.com/observations',adjustment_basis='adjusted_close')

def test_default_eight_teams_cover_the_exact_universe_once():
 data=json.loads((Path(__file__).parents[1]/'config/research_teams.json').read_text())
 assert len(data['teams'])==8
 tickers=[t for g in data['teams'] for t in g['tickers']]
 assert len(tickers)==len(set(tickers)) and set(tickers)==set(SUPPORTED)
 assert all(b['status']=='proposed' for g in data['teams'] for b in g['benchmark_candidates'])
 assert len(next(g for g in data['teams'] if g['id']=='consumer')['benchmark_candidates'])==2

def test_returns_use_same_endpoints_and_expose_sources():
 result=relative_performance([row('CSCO',A,100),row('CSCO',B,110)],
                             [row('XLK',A,100),row('XLK',B,105)],start=A,end=B)
 assert result['status']=='available'
 assert result['relative_return_pp']==pytest.approx(5)
 assert result['sources']==['https://example.com/observations']

def test_currency_mismatch_requires_evidence():
 result=relative_performance([row('BMO.TO',A,100,'CAD'),row('BMO.TO',B,110,'CAD')],
                             [row('XLF',A,100),row('XLF',B,105)],start=A,end=B)
 assert result['status']=='missing' and result['relative_return_pp'] is None

def test_missing_endpoint_is_not_forward_filled():
 result=relative_performance([row('CSCO',A,100)],[row('XLK',A,100),row('XLK',B,105)],start=A,end=B)
 assert result['status']=='missing'

def test_duplicate_observation_fails_instead_of_silently_overwriting():
 with pytest.raises(ValueError,match='Duplicate'):
  relative_performance([row('CSCO',A,100),row('CSCO',A,101)],[],start=A,end=B)

@pytest.mark.parametrize('value',[True,0,-1,float('nan'),float('inf')])
def test_invalid_prices_rejected(value):
 with pytest.raises(ValueError):row('CSCO',A,value)


def test_unknown_adjustment_basis_cannot_claim_comparable_returns():
 from dataclasses import replace
 stock=[replace(row('CSCO',A,100),adjustment_basis='unspecified'),row('CSCO',B,110)]
 result=relative_performance(stock,[row('XLK',A,100),row('XLK',B,105)],start=A,end=B)
 assert result['status']=='missing'


def test_private_query_credentials_cannot_enter_public_source_reference():
 with pytest.raises(ValueError):
  PriceObservation('CSCO',A,100,'USD',datetime(2026,10,9,tzinfo=timezone.utc),
                   'https://example.com/data?api_key=synthetic',adjustment_basis='adjusted_close')
