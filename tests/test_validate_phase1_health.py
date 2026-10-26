"""_health summary for scripts/validate_phase1.py (Round 14 S06).

validate_phase1.py is a top-level script: importing it would run the full
validation (reading reports, writing INDEX.md). So these tests exec only the
pure build_health prefix (imports + function, before the AS_OF line), which
is exactly the code the script itself uses to build the _health entry.
"""

from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "validate_phase1.py"


def _build_health():
    import sys
    # The script runs with scripts/ on sys.path (script directory); mirror that.
    scripts_dir = str(SCRIPT.parent)
    if scripts_dir not in sys.path:
        sys.path.insert(0, scripts_dir)
    source = SCRIPT.read_text()
    prefix = source.split("AS_OF =")[0]
    namespace = {}
    exec(compile(prefix, str(SCRIPT), "exec"), namespace)
    return namespace["build_health"]


def test_pass_example():
    build_health = _build_health()
    results = {
        "NVDA": {"sections_passed": True, "quant_matches_json": True,
                 "ai_items": "3", "market_errors": [], "ai_error": None},
        "independent_NVDA_1Y": {"passed": True, "return_pct": "12.5"},
    }
    health = build_health(results)
    assert health["status"] == "pass"
    assert health == {
        "status": "pass", "total": 2, "passed": 2, "failed": 0, "skipped": 0,
        "items": {"NVDA": "pass", "independent_NVDA_1Y": "pass"},
    }


def test_fail_and_skip_examples():
    build_health = _build_health()
    results = {
        "NVDA": {"sections_passed": True, "quant_matches_json": True,
                 "ai_items": "N/A", "market_errors": [], "ai_error": "quota"},
        "MSFT": None,
        "independent_MSFT_1Y": {"passed": False, "return_pct": "0"},
    }
    health = build_health(results)
    assert health["status"] == "fail"
    assert health["passed"] == 0 and health["failed"] == 2 and health["skipped"] == 1
    assert health["items"] == {
        "NVDA": "fail", "MSFT": "skip", "independent_MSFT_1Y": "fail",
    }


def test_health_key_itself_is_not_counted():
    build_health = _build_health()
    results = {"NVDA": {"sections_passed": True, "quant_matches_json": True,
                         "market_errors": [], "ai_error": None},
               "_health": {"status": "pass"}}
    assert build_health(results)["total"] == 1
