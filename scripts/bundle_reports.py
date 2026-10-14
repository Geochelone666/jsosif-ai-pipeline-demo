"""Package generated report artifacts into a daily directory."""

from datetime import date
from pathlib import Path
import shutil


def bundle_reports(reports_dir="reports", bundle_root="bundle"):
    """Collect reports into a dated bundle directory; return its path as a str.

    Re-running replaces the day's contents, including any stale files.
    """
    source = Path(reports_dir)
    destination = Path(bundle_root) / date.today().isoformat()
    if not source.is_dir():
        raise SystemExit(f"Reports directory is missing or not a directory: {source}")
    source_path = source.resolve()
    destination_path = destination.resolve()
    if (source_path == destination_path
            or source_path in destination_path.parents
            or destination_path in source_path.parents):
        raise SystemExit("Reports and dated bundle directories must not overlap")

    files = sorted(path for path in source.rglob("*") if path.is_file())
    if not files:
        raise SystemExit(f"Reports directory contains no files: {source}")

    if destination.is_symlink() or destination.is_file():
        destination.unlink()
    elif destination.exists():
        shutil.rmtree(destination)
    destination.mkdir(parents=True)
    for path in files:
        target = destination / path.relative_to(source)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, target)

    print(f"BUNDLED {len(files)} files -> {destination}")
    return str(destination)


if __name__ == "__main__":
    from tempfile import TemporaryDirectory

    with TemporaryDirectory() as temporary:
        root = Path(temporary)
        reports = root / "reports"
        reports.mkdir()
        (reports / "completeness-matrix.md").write_text("fixture\n")
        bundle = Path(bundle_reports(reports, root / "bundle"))
        first = {p.relative_to(bundle): p.read_bytes()
                 for p in bundle.rglob("*") if p.is_file()}
        (bundle / "stale.md").write_text("stale\n")
        assert bundle_reports(reports, root / "bundle") == str(bundle)
        second = {p.relative_to(bundle): p.read_bytes()
                  for p in bundle.rglob("*") if p.is_file()}
        assert first == second
