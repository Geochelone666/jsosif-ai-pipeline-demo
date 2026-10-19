"""Plain-English, deterministic readings of report metrics (percent units)."""
import math

# All band thresholds are judgment choices for this research report, not investment advice.
ZERO = 0
RSI_OVERSOLD = 30
RSI_OVERBOUGHT = 70
BETA_LOW = 0.3
BETA_MARKET_LOW = 0.8
BETA_AMPLIFIED = 1.3
SHARPE_STRONG = 1
VOLATILITY_LOW = 20
VOLATILITY_HIGH = 40
DRAWDOWN_SHALLOW = 10
DRAWDOWN_DEEP = 30
TREND_STRONG = 5
PE_LOW = 15
PE_HIGH = 30

METRICS = {
    'Close': {'label': 'Close', 'meaning': 'The latest adjusted closing price is measured in the quoted currency.'},
    **{f'Return {period} (%)': {
        'label': f'Return {period} (%)',
        'meaning': f'The adjusted closing price change over {meaning} is measured as a percentage.'
    } for period, meaning in [('1D', 'one trading day'), ('1W', 'one week'),
                              ('1M', 'one month'), ('YTD', 'the year to date'),
                              ('1Y', 'one year')]},
    'Annualized volatility (%)': {'label': 'Annualized volatility (%)', 'meaning': 'The variability of daily returns is scaled to one year as a percentage.'},
    'Beta vs SPY': {'label': 'Beta vs SPY', 'meaning': 'Beta estimates how sensitively returns move with the SPY market benchmark.'},
    'Max drawdown (%)': {'label': 'Max drawdown (%)', 'meaning': 'The largest peak-to-trough price decline in the sampled history is measured as a percentage.'},
    'Sharpe (rf=0)': {'label': 'Sharpe (rf=0)', 'meaning': 'Sharpe measures annualized return per unit of volatility using a zero risk-free rate.'},
    'P/E (trailing)': {'label': 'P/E (trailing)', 'meaning': 'The share price is divided by trailing earnings per share.'},
    'RSI (14, Wilder)': {'label': 'RSI (14, Wilder)', 'meaning': 'The 14-period relative strength index compares recent gains with losses on a 0 to 100 scale.'},
    'MACD histogram': {'label': 'MACD histogram', 'meaning': 'The difference between MACD and its signal line measures their momentum gap in price units.'},
    **{f'Close vs MA{days} (%)': {
        'label': f'Close vs MA{days} (%)',
        'meaning': f'The closing price distance from its {days}-day moving average is measured as a percentage.'
    } for days in (50, 200)},
}


def _finite(value):
    try:
        return not isinstance(value, (bool, str)) and math.isfinite(value)
    except (TypeError, ValueError, OverflowError):
        return False


def interpret(key, value) -> str:
    """Read a metric using fixed bands; unknown or unavailable values stay neutral."""
    if not _finite(value):
        return 'No finite value is available.'
    if key == 'RSI (14, Wilder)':
        if value < RSI_OVERSOLD:
            return 'Oversold momentum reading.'
        if value > RSI_OVERBOUGHT:
            return 'Overbought momentum reading.'
        return 'Neutral momentum reading.'
    if key == 'Beta vs SPY':
        if value < ZERO:
            return 'Inverse market sensitivity.'
        if value < BETA_LOW:
            return 'Low market sensitivity.'
        if value < BETA_MARKET_LOW:
            return 'Moves with the market with reduced sensitivity.'
        if value <= BETA_AMPLIFIED:
            return 'Broadly tracks market sensitivity.'
        return 'Amplified market sensitivity.'
    if key == 'Sharpe (rf=0)':
        if value < ZERO:
            return 'Negative risk-adjusted return.'
        if value <= SHARPE_STRONG:
            return 'Modest risk-adjusted return.'
        return 'Strong risk-adjusted return.'
    if key == 'Annualized volatility (%)':
        if value < VOLATILITY_LOW:
            return 'Low annualized volatility.'
        if value <= VOLATILITY_HIGH:
            return 'Moderate annualized volatility.'
        return 'High annualized volatility.'
    if key == 'Max drawdown (%)':
        magnitude = abs(value)
        if magnitude < DRAWDOWN_SHALLOW:
            return 'Shallow peak-to-trough loss magnitude.'
        if magnitude <= DRAWDOWN_DEEP:
            return 'Moderate peak-to-trough loss magnitude.'
        return 'Deep peak-to-trough loss magnitude.'
    if key in ('Close vs MA50 (%)', 'Close vs MA200 (%)'):
        if value == ZERO:
            return 'At the moving-average trend level.'
        direction = 'above' if value > ZERO else 'below'
        strength = 'Clearly' if abs(value) >= TREND_STRONG else 'Slightly'
        return f'{strength} {direction} the moving-average trend level.'
    if key == 'MACD histogram':
        if value == ZERO:
            return 'Neutral momentum: MACD equals its signal line.'
        direction = 'Positive' if value > ZERO else 'Negative'
        return f'{direction} momentum relative to the MACD signal line.'
    if key == 'P/E (trailing)':
        if value <= ZERO:
            return 'Non-positive P/E is not a meaningful positive-earnings multiple.'
        if value < PE_LOW:
            return 'Low trailing earnings multiple under the research bands.'
        if value <= PE_HIGH:
            return 'Moderate trailing earnings multiple under the research bands.'
        return 'High trailing earnings multiple under the research bands.'
    if key.startswith('Return ') and key in METRICS:
        if value == ZERO:
            return 'Unchanged adjusted price over this period.'
        direction = 'rose' if value > ZERO else 'fell'
        return f'Adjusted price {direction} over this period.'
    if key == 'Close':
        return 'Price level only; it does not by itself indicate valuation.'
    return 'No interpretation rule is available for this metric.'


def _display(value):
    """Render a value the same way the report's quantitative table does: 4 decimals."""
    if isinstance(value, float):
        return f"{value:.4f}"
    return str(value)


def build_interpretation_section(metrics: dict) -> str:
    """Render only known metrics with finite numeric values, in registry order."""
    bullets = []
    for key, entry in METRICS.items():
        value = metrics.get(key)
        if _finite(value):
            bullets.append(f"- **{entry['label']}**: {entry['meaning']} "
                           f"This value: {_display(value)} -> {interpret(key, value)}")
    if not bullets:
        return ''
    return ('## HOW TO READ THE QUANTITATIVE SECTION\n\n'
            'These rule-based bands are judgment choices for this research report, '
            'not investment advice.\n\n' + '\n'.join(bullets) + '\n\n')
