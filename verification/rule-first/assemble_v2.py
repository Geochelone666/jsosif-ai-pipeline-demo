"""Reuse the original report generator, then append free-source sections."""
import json
import os
import subprocess
import sys
from data_utils import ROOT, number

REPORT = ROOT / 'NVDA-intelligence-20261003.md'

def load(name):
    with (ROOT / name).open(encoding='utf-8') as stream:
        return json.load(stream)

def fmt(value, percent=False):
    value = number(value)
    return 'N/A' if value is None else f'{value * (100 if percent else 1):,.2f}'

def amount(data):
    if data is None:
        return 'N/A'
    return f'{fmt(data.get("value"))} {data.get("unit", "N/A")}; period {data.get("period", "N/A")}; fiscal year/reporting period {data.get("fiscal_year", "N/A")}/{data.get("fiscal_period", "N/A")}'

def main():
    subprocess.run([sys.executable, str(ROOT / 'regenerate_report.py')], cwd=ROOT, check=True)

if __name__ == '__main__':
    main()
