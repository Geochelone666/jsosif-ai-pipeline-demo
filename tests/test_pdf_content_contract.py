"""Keep the PDF metric table synchronized with the numerical snapshot contract."""
import ast
from pathlib import Path

from fundamental_context import FUNDAMENTAL_KEYS
from risk_extensions import RISK_KEYS


def test_pdf_table_includes_new_risk_and_fundamental_dimensions():
    source = (Path(__file__).resolve().parents[1] / 'scripts/report_pdf.py').read_text()
    tree = ast.parse(source)
    assignments = [
        node for node in tree.body if isinstance(node, ast.Assign) and
        any(isinstance(t, ast.Name) and t.id == 'quant_rows' for t in node.targets)
    ]
    assert len(assignments) == 1
    rows = assignments[0].value.elts
    displayed = {
        row.elts[0].value for row in rows
        if isinstance(row, ast.Tuple) and isinstance(row.elts[0], ast.Constant)
    }
    assert set(RISK_KEYS).issubset(displayed)
    assert set(FUNDAMENTAL_KEYS).issubset(displayed)
    assert len(displayed) == len(rows)


def test_pdf_has_distinct_incomplete_and_quiet_news_explanations():
    source = (Path(__file__).resolve().parents[1] / 'scripts/report_pdf.py').read_text()
    assert 'headlines remain unresolved' in source
    assert 'this does not prove there was no company news' in source
    assert 'No qualified events assigned to this category' in source
