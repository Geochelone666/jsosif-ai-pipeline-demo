"""Regression coverage for plain-English metric readings and report placement."""
import ast
from pathlib import Path
import sys

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from metric_interpretation import METRICS, build_interpretation_section, interpret


@pytest.mark.parametrize('key,value,expected', [
    ('RSI (14, Wilder)', 29.9, 'Oversold momentum'),
    ('RSI (14, Wilder)', 30, 'Neutral momentum'),
    ('RSI (14, Wilder)', 70, 'Neutral momentum'),
    ('RSI (14, Wilder)', 70.1, 'Overbought momentum'),
    ('Beta vs SPY', 0, 'Low market sensitivity'),
    ('Beta vs SPY', -1.5, 'Inverse market sensitivity'),
    ('Beta vs SPY', 0.3, 'reduced sensitivity'),
    ('Beta vs SPY', 0.8, 'tracks market sensitivity'),
    ('Beta vs SPY', 1.3, 'tracks market sensitivity'),
    ('Beta vs SPY', 1.31, 'Amplified market sensitivity'),
    ('Sharpe (rf=0)', -0.01, 'Negative risk-adjusted return'),
    ('Sharpe (rf=0)', 0, 'Modest risk-adjusted return'),
    ('Sharpe (rf=0)', 1, 'Modest risk-adjusted return'),
    ('Sharpe (rf=0)', 1.5, 'Strong risk-adjusted return'),
    ('Annualized volatility (%)', 19.9, 'Low annualized volatility'),
    ('Annualized volatility (%)', 20, 'Moderate annualized volatility'),
    ('Annualized volatility (%)', 40, 'Moderate annualized volatility'),
    ('Annualized volatility (%)', 40.1, 'High annualized volatility'),
    ('Max drawdown (%)', -9.9, 'Shallow'),
    ('Max drawdown (%)', -10, 'Moderate'),
    ('Max drawdown (%)', -30, 'Moderate'),
    ('Max drawdown (%)', -30.1, 'Deep'),
    ('Close vs MA50 (%)', 0, 'At the moving-average'),
    ('Close vs MA50 (%)', 4.9, 'Slightly above'),
    ('Close vs MA50 (%)', 5, 'Clearly above'),
    ('Close vs MA200 (%)', -4.9, 'Slightly below'),
    ('Close vs MA200 (%)', -5, 'Clearly below'),
    ('MACD histogram', -0.01, 'Negative momentum'),
    ('MACD histogram', 0, 'Neutral momentum'),
    ('MACD histogram', 0.01, 'Positive momentum'),
    ('P/E (trailing)', 0, 'Non-positive P/E'),
    ('P/E (trailing)', 14.9, 'Low trailing'),
    ('P/E (trailing)', 15, 'Moderate trailing'),
    ('P/E (trailing)', 30, 'Moderate trailing'),
    ('P/E (trailing)', 30.1, 'High trailing'),
    ('Return 1D (%)', -1, 'price fell'),
    ('Return 1Y (%)', 0, 'Unchanged adjusted price'),
    ('Return YTD (%)', 1, 'price rose'),
    ('Close', 196.64, 'Price level only'),
])
def test_bands_and_determinism(key, value, expected):
    reading = interpret(key, value)
    assert expected in reading
    assert interpret(key, value) == reading


@pytest.mark.parametrize('invalid', [None, float('nan'), float('inf'),
                                     -float('inf'), 'N/A', {}, True])
def test_partial_metrics(invalid):
    section = build_interpretation_section({'Close': 100, 'Beta vs SPY': invalid})
    assert '**Close**' in section
    assert '**Beta vs SPY**' not in section
    assert '**RSI (14, Wilder)**' not in section
    assert build_interpretation_section({'Beta vs SPY': invalid}) == ''


def test_section_structure():
    assert len(METRICS) >= 12
    metrics = dict.fromkeys(METRICS, 1.5)
    section = build_interpretation_section(metrics)
    assert section.startswith('## HOW TO READ THE QUANTITATIVE SECTION\n\n')
    bullets = [line for line in section.splitlines() if line.startswith('- ')]
    assert len(bullets) == len(METRICS)
    for (key, entry), bullet in zip(METRICS.items(), bullets):
        assert f"**{entry['label']}**: {entry['meaning']}" in bullet
        assert f'This value: 1.5000 -> {interpret(key, 1.5)}' in bullet
    assert build_interpretation_section({}) == ''
    assert build_interpretation_section({'unknown': 10}) == ''


@pytest.mark.parametrize('metrics', [{}, {'RSI (14, Wilder)': 57.07}])
def test_report_template_placement(metrics):
    # Evaluate the real report template in isolation, without snapshot or network I/O.
    script = Path(__file__).resolve().parents[1] / 'scripts' / 'regenerate_report.py'
    tree = ast.parse(script.read_text())
    assignment = next(node for node in tree.body if isinstance(node, ast.Assign)
                      and any(isinstance(t, ast.Name) and t.id == 'report'
                              for t in node.targets))
    context = dict(TICKER='ACN', AS_OF='2026-10-08', quant={}, q=metrics,
                   ai={k: [] for k in ('tailwinds', 'headwinds', 'catalysts', 'risks')},
                   quant_table='## QUANTITATIVE\n', all_sources=[], ai_status='Available',
                   section=lambda name, items: f'## {name}\n',
                   build_interpretation_section=build_interpretation_section)
    exec(compile(ast.Module(body=[assignment], type_ignores=[]), str(script), 'exec'), context)
    report = context['report']
    header = '## HOW TO READ THE QUANTITATIVE SECTION'
    if metrics:
        assert report.index('Methodology:') < report.index(header) < report.index('## TAILWINDS')
        assert 'This value: 57.0700 -> Neutral momentum reading.' in report
    else:
        assert header not in report
