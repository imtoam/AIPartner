#!/usr/bin/env python3
"""Validate AIPartner framework integrity and initialized project contracts.

The validator intentionally uses only the Python standard library. It checks the stable subset of
the project_profile.yaml contract without attempting to be a general YAML parser.
"""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path


ALLOWED_STATES = {
    "uninitialized",
    "interviewing",
    "draft",
    "proposed",
    "needs_user_decision",
    "approved_pending_materialization",
    "materialized",
    "verification_failed",
    "blocked_by_environment",
    "verified",
    "complete",
}

POST_APPROVAL_STATES = {
    "approved_pending_materialization",
    "materialized",
    "verification_failed",
    "blocked_by_environment",
    "verified",
    "complete",
}

POST_MATERIALIZATION_STATES = {
    "materialized",
    "verification_failed",
    "blocked_by_environment",
    "verified",
    "complete",
}

FRAMEWORK_FILES = {
    "AGENTS.md": (
        "Framework invariant:",
        "ROLE-CORE: Core roles and working rules",
        "ROLE-PARTNER: The partnership",
        "ROLE-REVIEW: Independent peer review",
        "ROLE-MULTIWRITER: Multiple project writers and worktrees",
        "BEGIN PROJECT CONFIG: ROLE MODULE ACTIVATION",
        "BEGIN PROJECT CONFIG: TEAM FACTS",
    ),
    "START_HERE.md": (
        "Protocol version: 0.4.0",
        "Framework invariant:",
        "Use external reference material without confusing it with the target",
        "There is no `approved` state.",
        "project-overview.html",
    ),
    "PROJECT_WORKFLOW.md": (
        "Framework invariant:",
        "WF-CORE: Core feature delivery",
        "WF-STRUCTURE: Repository structure",
        "WF-VCS: Version control",
        "WF-DOCS: Documentation and work tracking",
        "WF-DOD: Definition of Done",
        "WF-PLANNING: Multi-level planning",
        "WF-DATA: Authoritative and non-cleanable data",
        "WF-OPS: Unattended operation",
        "WF-RECOVERY: Backup and recovery",
        "WF-HIGH-IMPACT: High-impact changes",
        "BEGIN PROJECT CONFIG: WORKFLOW MODULE ACTIVATION",
        "BEGIN PROJECT CONFIG: PROJECT FACTS",
    ),
    "PROJECT_STRUCTURE_REFERENCE.md": (
        "Framework invariant:",
        "## 4. Git and version-control reference",
        "framework_retained",
        "project-overview.html",
        "## 11. Minimal greenfield starting set",
    ),
    "project_profile.example.yaml": (
        'schema_version: "0.4.0"',
        "reference_adoptions:",
        "framework_retained:",
        "unresolved_decisions:",
        'path: "project-overview.html"',
    ),
    "index.html": (
        'name="aipartner-page-role" content="human-start-guide"',
        'id="begin"',
        "START_HERE.md",
    ),
    "README.md": (
        "START_HERE.md",
        "AGENTS.md",
        "PROJECT_WORKFLOW.md",
    ),
    "framework_manifest.json": (
        '"schema_version": 1',
        '"files"',
    ),
}


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.passes: list[str] = []

    def ok(self, message: str) -> None:
        self.passes.append(message)

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)


def scalar_value(raw: str) -> str:
    value = raw.strip()
    if " #" in value:
        value = value.split(" #", 1)[0].rstrip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        return value[1:-1]
    return value


def block(lines: list[str], key: str, indent: int = 0) -> list[str]:
    prefix = " " * indent + key + ":"
    start = None
    for index, line in enumerate(lines):
        if line.startswith(prefix) and len(line) > indent + len(key):
            start = index
            break
    if start is None:
        return []

    collected = [lines[start]]
    for line in lines[start + 1 :]:
        if not line.strip():
            collected.append(line)
            continue
        current_indent = len(line) - len(line.lstrip(" "))
        if current_indent <= indent:
            break
        collected.append(line)
    return collected


def field(lines: list[str], key: str, minimum_indent: int = 0) -> str:
    pattern = re.compile(rf"^\s{{{minimum_indent},}}{re.escape(key)}:\s*(.*?)\s*$")
    for line in lines:
        match = pattern.match(line)
        if match:
            return scalar_value(match.group(1))
    return ""


def path_entries(lines: list[str], category: str) -> list[str]:
    category_block = block(lines, category, indent=2)
    results = []
    for line in category_block:
        match = re.match(r"^\s+- path:\s*(.*?)\s*$", line)
        if match:
            results.append(scalar_value(match.group(1)))
    return results


def unresolved_entries(lines: list[str]) -> list[dict[str, str]]:
    unresolved = block(lines, "unresolved_decisions", indent=0)
    entries: list[dict[str, str]] = []
    current: dict[str, str] | None = None
    for line in unresolved[1:]:
        start = re.match(r"^\s{2}- id:\s*(.*?)\s*$", line)
        if start:
            if current:
                entries.append(current)
            current = {"id": scalar_value(start.group(1))}
            continue
        if current is None:
            continue
        item = re.match(r"^\s{4}([a-zA-Z_]+):\s*(.*?)\s*$", line)
        if item:
            current[item.group(1)] = scalar_value(item.group(2))
    if current:
        entries.append(current)
    return entries


def list_values(lines: list[str], key: str, indent: int) -> list[str]:
    values = []
    for line in block(lines, key, indent=indent)[1:]:
        match = re.match(r"^\s+-\s*(.*?)\s*$", line)
        if match:
            values.append(scalar_value(match.group(1)))
    return values


def git_repository_exists(root: Path) -> bool:
    result = subprocess.run(
        ["git", "-C", str(root), "rev-parse", "--is-inside-work-tree"],
        capture_output=True,
        text=True,
        check=False,
    )
    return result.returncode == 0 and result.stdout.strip() == "true"


def normalized_framework_text(text: str) -> str:
    pattern = re.compile(
        r"<!-- BEGIN PROJECT CONFIG: ([^>]+) -->.*?"
        r"<!-- END PROJECT CONFIG: \1 -->",
        re.DOTALL,
    )
    return pattern.sub(
        lambda match: (
            f"<!-- BEGIN PROJECT CONFIG: {match.group(1)} -->\n"
            f"<!-- MANAGED PROJECT CONFIG OMITTED -->\n"
            f"<!-- END PROJECT CONFIG: {match.group(1)} -->"
        ),
        text,
    )


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def validate_manifest(root: Path, report: Report) -> None:
    manifest_path = root / "framework_manifest.json"
    if not manifest_path.is_file():
        return
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as error:
        report.error(f"Cannot read framework_manifest.json: {error}")
        return

    for relative, contract in manifest.get("files", {}).items():
        target = root / relative
        if not target.is_file():
            report.error(f"Manifest target is missing: {relative}")
            continue
        text = target.read_text(encoding="utf-8")
        mode = contract.get("mode")
        if mode == "managed_blocks":
            text = normalized_framework_text(text)
        elif mode != "immutable":
            report.error(f"Unknown manifest mode for {relative}: {mode}")
            continue
        actual = sha256_text(text)
        expected = contract.get("sha256", "")
        if actual != expected:
            report.error(
                f"Framework integrity mismatch: {relative} ({mode}); "
                "restore the template rule or approve a framework-version update"
            )
        else:
            report.ok(f"{relative} matches the {mode} framework contract")


def validate_framework(root: Path, report: Report) -> None:
    for relative, required_fragments in FRAMEWORK_FILES.items():
        target = root / relative
        if not target.is_file():
            report.error(f"Missing retained framework file: {relative}")
            continue
        text = target.read_text(encoding="utf-8")
        missing = [fragment for fragment in required_fragments if fragment not in text]
        if missing:
            report.error(f"{relative} lost required framework content: {', '.join(missing)}")
        else:
            report.ok(f"{relative} retains required framework content")
    validate_manifest(root, report)


def validate_profile(root: Path, report: Report) -> None:
    profile_path = root / "project_profile.yaml"
    if not profile_path.exists():
        report.ok("No project_profile.yaml: retained framework validated in uninitialized state")
        return

    lines = profile_path.read_text(encoding="utf-8").splitlines()
    required_sections = {
        "schema_version",
        "template",
        "input",
        "initialization",
        "project",
        "reference_adoptions",
        "role_modules",
        "workflow_modules",
        "version_control",
        "authority",
        "work_identity",
        "first_work",
        "structure",
        "unresolved_decisions",
        "human_overview",
        "verification",
    }
    present = {
        match.group(1)
        for line in lines
        if (match := re.match(r"^([a-zA-Z_]+):(?:\s|$)", line))
    }
    missing = sorted(required_sections - present)
    if missing:
        report.error(f"project_profile.yaml is missing required sections: {', '.join(missing)}")
    else:
        report.ok("project_profile.yaml contains all required top-level sections")

    version = field(lines, "schema_version")
    if version != "0.4.0":
        report.error(f"Unsupported project profile schema_version: {version or '(missing)'}")

    initialization = block(lines, "initialization")
    status = field(initialization, "status", minimum_indent=2)
    mode = field(initialization, "mode", minimum_indent=2)
    if status not in ALLOWED_STATES:
        report.error(f"Invalid initialization status: {status or '(missing)'}")
    if mode != "greenfield":
        report.error(f"Protocol 0.4 supports only greenfield mode, found: {mode or '(missing)'}")

    approval = block(initialization, "approval", indent=2)
    approval_state = field(approval, "state", minimum_indent=4)
    approval_evidence = field(approval, "evidence_ref", minimum_indent=4)
    if status in POST_APPROVAL_STATES:
        if approval_state != "approved":
            report.error(f"State {status} requires approval.state approved")
        if not approval_evidence:
            report.error(f"State {status} requires approval.evidence_ref")

    unresolved = unresolved_entries(lines)
    open_blockers = [
        item
        for item in unresolved
        if item.get("blocking", "").lower() == "true" and item.get("status", "").lower() == "open"
    ]
    if open_blockers and status in POST_APPROVAL_STATES:
        ids = ", ".join(item.get("id", "(missing ID)") for item in open_blockers)
        report.error(f"State {status} is forbidden while blocking decisions are open: {ids}")
    elif open_blockers:
        report.warn(
            "Open blocking decisions correctly prevent completion: "
            + ", ".join(item.get("id", "(missing ID)") for item in open_blockers)
        )

    first_work = block(lines, "first_work")
    if any(re.match(r"^\s+status:", line) for line in first_work):
        report.error("first_work must not duplicate mutable work status")

    project = block(lines, "project")
    current_work_source = field(project, "current_work_source", minimum_indent=2)
    if status in POST_MATERIALIZATION_STATES and current_work_source:
        if not (root / current_work_source).exists():
            report.error(f"Current work source does not exist: {current_work_source}")

    version_control = block(lines, "version_control")
    vcs_mode = field(version_control, "mode", minimum_indent=2)
    allowed_vcs = {
        "local_git",
        "remote_single_writer",
        "protected_collaboration",
        "integration_branch",
        "deferred",
    }
    if vcs_mode not in allowed_vcs:
        report.error(f"Invalid or missing version-control mode: {vcs_mode or '(missing)'}")
    elif vcs_mode == "deferred":
        deferral = block(version_control, "deferral", indent=2)
        required = ("reason", "accepted_risk", "trigger", "approval_evidence_ref")
        missing_deferral = [name for name in required if not field(deferral, name, 4)]
        if missing_deferral:
            report.error(
                "Deferred Git requires reason, risk, trigger, and approval evidence; missing: "
                + ", ".join(missing_deferral)
            )
    elif not git_repository_exists(root):
        report.error(f"Version-control mode {vcs_mode} requires an actual Git repository")
    else:
        report.ok(f"Git repository exists for version-control mode {vcs_mode}")

    retained = path_entries(lines, "framework_retained")
    selected = path_entries(lines, "selected_now")
    deferred = path_entries(lines, "deferred_until_trigger")
    required_retained = {
        "AGENTS.md",
        "START_HERE.md",
        "PROJECT_WORKFLOW.md",
        "PROJECT_STRUCTURE_REFERENCE.md",
        "project_profile.example.yaml",
        "index.html",
        "README.md",
        "LICENSE",
        "tools/validate_initialization.py",
        "framework_manifest.json",
        "introduction/",
    }
    missing_retained = sorted(required_retained - set(retained))
    if missing_retained:
        report.error(
            "framework_retained is missing required paths: " + ", ".join(missing_retained)
        )
    for relative in retained + selected:
        if relative and not (root / relative).exists():
            report.error(f"Classified materialized path does not exist: {relative}")
    for relative in deferred:
        if relative and (root / relative).exists() and relative not in retained:
            report.error(f"Deferred path was materialized: {relative}")

    overview = block(lines, "human_overview")
    overview_path = field(overview, "path", minimum_indent=2)
    if overview_path == "index.html":
        report.error("index.html must remain the human start guide; use project-overview.html")
    if status in POST_MATERIALIZATION_STATES:
        overview_file = root / overview_path if overview_path else None
        if overview_file is None or not overview_file.is_file():
            report.error(f"Human project overview does not exist: {overview_path or '(missing)'}")
        else:
            overview_text = overview_file.read_text(encoding="utf-8")
            if 'name="aipartner-page-role" content="project-overview"' not in overview_text:
                report.error(f"{overview_path} lacks the project-overview page-role marker")
            if "href=" not in overview_text:
                report.error(f"{overview_path} contains no clickable document links")
            if status and status not in overview_text:
                report.error(f"{overview_path} does not display initialization status {status}")
            generated_on = field(overview, "generated_on", minimum_indent=2)
            if not generated_on:
                report.error(f"{overview_path} has no recorded generation time")
            for source in list_values(overview, "sources", indent=2):
                if source and source not in overview_text:
                    report.error(f"{overview_path} does not identify source {source}")
            for item in open_blockers:
                item_id = item.get("id", "")
                if item_id and item_id not in overview_text:
                    report.error(f"{overview_path} hides blocking decision {item_id}")

    if status == "complete":
        verification = block(lines, "verification")
        if field(verification, "result", minimum_indent=2) != "pass":
            report.error("Complete initialization requires verification.result pass")


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    report = Report()
    validate_framework(root, report)
    validate_profile(root, report)

    print(f"AIPartner initialization validation: {root}")
    for message in report.passes:
        print(f"PASS  {message}")
    for message in report.warnings:
        print(f"WARN  {message}")
    for message in report.errors:
        print(f"ERROR {message}")
    print(
        f"SUMMARY errors={len(report.errors)} warnings={len(report.warnings)} "
        f"passes={len(report.passes)}"
    )
    return 1 if report.errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
