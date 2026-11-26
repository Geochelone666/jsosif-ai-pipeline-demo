"""Regression gates for publishing the daily GitHub Pages research archive.

This is a workflow-contract test; live Pages deployment is checked separately.
"""
from pathlib import Path

import yaml


WORKFLOW_PATH = (
    Path(__file__).resolve().parents[1] / ".github/workflows/daily-25-reports.yml"
)


def _workflow():
    return yaml.safe_load(WORKFLOW_PATH.read_text(encoding="utf-8"))


def _step(step_id):
    return next(
        step
        for step in _workflow()["jobs"]["refresh"]["steps"]
        if step.get("id") == step_id
    )


def test_degraded_source_evidence_cannot_publish_pages():
    """Generation or site-build success alone must never authorize release."""
    strict = _step("strict_release")
    assert strict["run"].endswith("--require-ready")
    assert "steps.build.outcome == 'success'" in strict["if"]

    upload = _step("upload")
    assert upload["uses"].startswith("actions/upload-pages-artifact@")
    assert "steps.strict_release.outcome == 'success'" in upload["if"]
    assert "vars.PAGES_DEPLOY_ENABLED == 'true'" in upload["if"]

    deploy = _step("deployment")
    assert deploy["uses"].startswith("actions/deploy-pages@")
    assert "steps.strict_release.outcome == 'success'" in deploy["if"]
    assert "steps.pages_artifact_ready.outcome == 'success'" in deploy["if"]
    assert "vars.PAGES_DEPLOY_ENABLED == 'true'" in deploy["if"]

    steps = _workflow()["jobs"]["refresh"]["steps"]
    assert sum(s.get("uses", "").startswith("actions/deploy-pages@") for s in steps) == 1


def test_pages_artifact_visibility_check_is_bounded_and_run_scoped():
    workflow = _workflow()
    assert workflow["permissions"]["actions"] == "read"
    probe = _step("pages_artifact_ready")
    assert "steps.upload.outcome == 'success'" in probe["if"]
    assert "steps.strict_release.outcome == 'success'" in probe["if"]
    assert probe["env"]["GH_TOKEN"] == "${{ github.token }}"
    assert "repos/$GITHUB_REPOSITORY/actions/runs/$GITHUB_RUN_ID/artifacts" in probe["run"]
    assert '.name == "github-pages"' in probe["run"]
    assert "for attempt in 1 2 3 4 5 6" in probe["run"]
    assert "exit 1" in probe["run"]


def test_backup_survives_strict_failure_but_http_verification_requires_deploy():
    steps = _workflow()["jobs"]["refresh"]["steps"]
    backup = next(s for s in steps if s.get("name") == "Back up the persisted archive and recovery state")
    assert "steps.persist.outcome == 'success'" in backup["if"]
    assert "steps.strict_release" not in backup["if"]

    verify = next(s for s in steps if s.get("name") == "Verify the deployed publication and archived files")
    assert "steps.deployment.outcome == 'success'" in verify["if"]
    assert "--require-ready" in verify["run"]
