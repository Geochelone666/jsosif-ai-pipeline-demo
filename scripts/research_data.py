"""Deterministic shared research contracts; no provider calls or inferred observations."""
from dataclasses import dataclass
from datetime import date, datetime, timezone
import math
import re
from urllib.parse import urlsplit


@dataclass(frozen=True)
class PriceObservation:
    instrument: str
    observed_on: date
    value: float
    currency: str
    retrieved_at: datetime
    source_url: str
    adjustment_basis: str = 'unspecified'

    def __post_init__(self):
        if (not isinstance(self.instrument,str) or not re.fullmatch(r'[A-Z0-9][A-Z0-9.-]{0,19}',self.instrument) or type(self.observed_on) is not date or
                isinstance(self.value,bool) or not isinstance(self.value,(int,float)) or
                not math.isfinite(self.value) or self.value<=0 or
                not isinstance(self.currency,str) or not re.fullmatch(r'[A-Z]{3}',self.currency) or
                self.adjustment_basis not in ('adjusted_close','raw_close','unspecified') or
                not isinstance(self.retrieved_at,datetime) or self.retrieved_at.utcoffset() is None):
            raise ValueError('Invalid price observation')
        url=urlsplit(self.source_url)
        if url.scheme!='https' or not url.hostname or url.username or url.password or url.query or url.fragment:
            raise ValueError('Expected an attributable HTTPS data source')
        if self.observed_on>self.retrieved_at.astimezone(timezone.utc).date():
            raise ValueError('Observation is future-dated relative to retrieval')


def relative_performance(stock, benchmark, *, start, end):
    """Compare identical endpoints in identical currency, with explicit missing data.

    Prices must share a documented adjustment basis supplied by the adapter.
    This function does not convert currencies, forward-fill or blend ETF proxies.
    """
    if type(start) is not date or type(end) is not date or start>=end:
        raise ValueError('Expected a positive observation window')
    def endpoints(observations):
        if not observations:return None
        if len({r.instrument for r in observations})!=1 or len({r.currency for r in observations})!=1:
            raise ValueError('One instrument/currency is required per series')
        by_date={}
        for row in observations:
            if row.observed_on in by_date:raise ValueError('Duplicate observations require source reconciliation')
            by_date[row.observed_on]=row
        if start not in by_date or end not in by_date:return None
        return by_date[start],by_date[end]
    a,b=endpoints(stock),endpoints(benchmark)
    missing={'status':'missing','stock_return_pct':None,'benchmark_return_pct':None,'relative_return_pp':None,
             'start':start.isoformat(),'end':end.isoformat()}
    if not a or not b:return dict(missing,reason='Exact observation endpoints are unavailable')
    if a[0].currency!=b[0].currency:return dict(missing,reason='Currency conversion evidence is required')
    bases={r.adjustment_basis for r in (*a,*b)}
    if len(bases)!=1 or 'unspecified' in bases:
        return dict(missing,reason='A matching documented price adjustment basis is required')
    first=(a[1].value/a[0].value-1)*100;second=(b[1].value/b[0].value-1)*100
    if not all(math.isfinite(v) for v in (first,second,first-second)):
        return dict(missing,reason='Computed return is not finite')
    return {'status':'available','start':start.isoformat(),'end':end.isoformat(),
            'currency':a[0].currency,'stock_return_pct':first,'benchmark_return_pct':second,
            'relative_return_pp':first-second,'sources':sorted({r.source_url for r in (*a,*b)})}
