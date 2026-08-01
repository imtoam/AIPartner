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
        "Protocol version: 0.5.0",
        "Framework invariant:",
        "Establish language without creating a language questionnaire",
        "Keep human views subordinate to project truth",
        "Use external reference material without confusing it with the target",
        "There is no `approved` state.",
        "project-overview.html",
    ),
    "PROJECT_WORKFLOW.md": (
        "Framework invariant:",
        "WF-CORE: Core feature delivery",
        "WF-COMMUNICATION: Language, terminology, and translation",
        "WF-STRUCTURE: Repository structure",
        "WF-VCS: Version control",
        "WF-DOCS: Documentation and work tracking",
        "WF-VIEWS: Human-readable project views",
        "WF-DOD: Definition of Done",
        "WF-PLANNING: Multi-level planning",
        "WF-DRIFT: Architecture and governance drift control",
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
        "### 9.4 Phase delivery plan",
        "### 9.12 Human-view registry",
        "project-overview.html",
        "## 11. Minimal greenfield starting set",
    ),
    "project_profile.example.yaml": (
        'schema_version: "0.5.0"',
        "communication:",
        "human_interface:",
        "reference_adoptions:",
        "framework_retained:",
        "unresolved_decisions:",
        'path: "project-overview.html"',
    ),
    "index.html": (
        'name="aipartner-page-role" content="human-start-guide"',
        'id="begin"',
        "Protocol 0.5",
        "Language and terminology",
        "START_HERE.md",
    ),
    "README.md": (
        "START_HERE.md",
        "AGENTS.md",
        "PROJECT_WORKFLOW.md",
        "Protocol version: 0.5.0",
    ),
    "framework_manifest.json": (
        '"schema_version": 1',
        '"protocol_version": "0.5.0"',
        '"files"',
    ),
    "tools/render_project_overview.py": (
        "Render project-overview.html from declared AIPartner project sources",
        'name="aipartner-derived-view" content="true"',
        "os.replace",
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


def child_block(lines: list[str], section: str, child: str) -> list[str]:
    """Return a four-space child mapping inside a top-level section."""
    section_lines = block(lines, section, indent=0)
    prefix = f"  {child}:"
    start = None
    for index, line in enumerate(section_lines):
        if line.startswith(prefix):
            start = index
            break
    if start is None:
        return []
    collected = [section_lines[start]]
    for line in section_lines[start + 1 :]:
        if not line.strip():
            collected.append(line)
            continue
        current_indent = len(line) - len(line.lstrip(" "))
        if current_indent <= 2:
            break
        collected.append(line)
    return collected


def validate_required_modules(lines: list[str], report: Report) -> None:
    required_roles = {"ROLE-CORE", "ROLE-PARTNER"}
    required_workflows = {
        "WF-CORE",
        "WF-COMMUNICATION",
        "WF-STRUCTURE",
        "WF-VCS",
        "WF-DOCS",
        "WF-VIEWS",
        "WF-DOD",
    }
    for section, required in (
        ("role_modules", required_roles),
        ("workflow_modules", required_workflows),
    ):
        for module_id in sorted(required):
            module = child_block(lines, section, module_id)
            state = field(module, "state", minimum_indent=4)
            if state != "active":
                report.error(f"Required module {module_id} must be active, found: {state or '(missing)'}")
            else:
                report.ok(f"Required module {module_id} is active")


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


def validate_communication(
    root: Path, lines: list[str], status: str, report: Report
) -> None:
    communication = block(lines, "communication")
    required = (
        "conversation_language",
        "engineering_language_of_record",
        "code_identifier_language",
        "source_evidence_policy",
        "derived_content_language",
    )
    missing = [name for name in required if not field(communication, name, minimum_indent=2)]
    if missing:
        report.error("Communication contract is missing: " + ", ".join(missing))

    locales = list_values(communication, "human_view_locales", indent=2)
    if not locales:
        report.error("Communication contract requires at least one human_view_locale")

    source_policy = field(communication, "source_evidence_policy", minimum_indent=2)
    if source_policy not in {"preserve_original", "project_defined", "no_external_source"}:
        report.error(f"Invalid source_evidence_policy: {source_policy or '(missing)'}")

    translation = block(communication, "translation", indent=2)
    translation_mode = field(translation, "mode", minimum_indent=4)
    if translation_mode not in {"none", "presentation_only", "versioned_derived", "project_defined"}:
        report.error(f"Invalid translation mode: {translation_mode or '(missing)'}")
    if field(translation, "may_replace_source_evidence", minimum_indent=4).lower() != "false":
        report.error("Translation may_replace_source_evidence must be false")
    if field(translation, "preserves_typed_values", minimum_indent=4).lower() != "true":
        report.error("Translation preserves_typed_values must be true")

    terminology = block(communication, "terminology", indent=2)
    terminology_mode = field(terminology, "mode", minimum_indent=4)
    terminology_source = field(terminology, "source", minimum_indent=4)
    if terminology_mode not in {"inline_conventions", "registry", "deferred"}:
        report.error(f"Invalid terminology mode: {terminology_mode or '(missing)'}")
    if terminology_mode == "registry":
        if not terminology_source:
            report.error("Terminology registry mode requires terminology.source")
        elif status in POST_MATERIALIZATION_STATES and not (root / terminology_source).is_file():
            report.error(f"Terminology registry does not exist: {terminology_source}")
    elif terminology_source:
        report.error("terminology.source must be empty unless terminology mode is registry")


def validate_human_interface(
    root: Path,
    lines: list[str],
    status: str,
    open_blockers: list[dict[str, str]],
    report: Report,
) -> None:
    interface = block(lines, "human_interface")
    interface_mode = field(interface, "mode", minimum_indent=2)
    bind_scope = field(interface, "bind_scope", minimum_indent=2)
    exposure_approval = field(interface, "exposure_approval_ref", minimum_indent=2)
    writeback = field(interface, "writeback", minimum_indent=2)
    writeback_approval = field(interface, "writeback_approval_ref", minimum_indent=2)
    registry_path = field(interface, "view_registry_path", minimum_indent=2)

    if interface_mode not in {"static_html", "local_http", "hybrid"}:
        report.error(f"Invalid human-interface mode: {interface_mode or '(missing)'}")
    if bind_scope not in {"none", "loopback", "approved_network"}:
        report.error(f"Invalid human-interface bind_scope: {bind_scope or '(missing)'}")
    if interface_mode == "static_html" and bind_scope != "none":
        report.error("static_html human interface requires bind_scope none")
    if interface_mode in {"local_http", "hybrid"} and bind_scope not in {"loopback", "approved_network"}:
        report.error(f"{interface_mode} human interface requires loopback or approved_network bind scope")
    if bind_scope == "approved_network" and not exposure_approval:
        report.error("approved_network bind scope requires exposure_approval_ref")

    if writeback not in {"disabled", "proposal_only", "approved_writeback"}:
        report.error(f"Invalid human-interface writeback mode: {writeback or '(missing)'}")
    if writeback != "disabled" and not writeback_approval:
        report.error(f"Human-interface writeback mode {writeback} requires approval evidence")

    if registry_path and status in POST_MATERIALIZATION_STATES and not (root / registry_path).is_file():
        report.error(f"Human-view registry does not exist: {registry_path}")

    overview = block(interface, "overview", indent=2)
    overview_path = field(overview, "path", minimum_indent=4)
    view_id = field(overview, "view_id", minimum_indent=4)
    page_role = field(overview, "page_role", minimum_indent=4)
    locale = field(overview, "locale", minimum_indent=4)
    generator_command = field(overview, "generator_command", minimum_indent=4)
    sources = list_values(overview, "sources", indent=4)
    communication = block(lines, "communication")
    allowed_locales = list_values(communication, "human_view_locales", indent=2)

    if overview_path == "index.html":
        report.error("index.html must remain the human start guide; use project-overview.html")
    if view_id != "project-overview" or page_role != "project-overview":
        report.error("Default overview requires view_id and page_role project-overview")
    if not locale or locale not in allowed_locales:
        report.error(f"Overview locale {locale or '(missing)'} is not an approved human-view locale")
    if not sources:
        report.error("Default overview requires declared sources")
    if not generator_command:
        report.error("Default overview requires generator_command")

    if status not in POST_MATERIALIZATION_STATES:
        return

    overview_file = root / overview_path if overview_path else None
    if overview_file is None or not overview_file.is_file():
        report.error(f"Human project overview does not exist: {overview_path or '(missing)'}")
        return

    overview_text = overview_file.read_text(encoding="utf-8")
    required_markers = (
        'name="aipartner-page-role" content="project-overview"',
        'name="aipartner-view-id" content="project-overview"',
        f'name="aipartner-view-locale" content="{locale}"',
        'name="aipartner-derived-view" content="true"',
    )
    for marker in required_markers:
        if marker not in overview_text:
            report.error(f"{overview_path} lacks required view marker: {marker}")
    if "href=" not in overview_text:
        report.error(f"{overview_path} contains no clickable document links")
    if status and status not in overview_text:
        report.error(f"{overview_path} does not display initialization status {status}")
    for metadata_name in (
        "aipartner-source-version",
        "aipartner-generated-on",
        "aipartner-view-freshness",
    ):
        pattern = rf'name="{metadata_name}" content="[^\"]+"'
        if not re.search(pattern, overview_text):
            report.error(f"{overview_path} lacks non-empty metadata {metadata_name}")
    for source in sources:
        if source and not (root / source).exists():
            report.error(f"Human-view source does not exist: {source}")
        if source and source not in overview_text:
            report.error(f"{overview_path} does not identify source {source}")
    for item in open_blockers:
        item_id = item.get("id", "")
        if item_id and item_id not in overview_text:
            report.error(f"{overview_path} hides blocking decision {item_id}")


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
        "communication",
        "reference_adoptions",
        "role_modules",
        "workflow_modules",
        "version_control",
        "authority",
        "work_identity",
        "first_work",
        "structure",
        "unresolved_decisions",
        "human_interface",
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
    if version != "0.5.0":
        report.error(f"Unsupported project profile schema_version: {version or '(missing)'}")

    initialization = block(lines, "initialization")
    status = field(initialization, "status", minimum_indent=2)
    mode = field(initialization, "mode", minimum_indent=2)
    if status not in ALLOWED_STATES:
        report.error(f"Invalid initialization status: {status or '(missing)'}")
    if mode != "greenfield":
        report.error(f"Protocol 0.5 supports only greenfield mode, found: {mode or '(missing)'}")

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

    validate_required_modules(lines, report)
    validate_communication(root, lines, status, report)
    validate_human_interface(root, lines, status, open_blockers, report)

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
    complexity_level = field(version_control, "complexity_level", minimum_indent=2)
    complexity_activation = field(
        version_control, "complexity_activation_condition", minimum_indent=2
    )
    complexity_retirement = field(
        version_control, "complexity_retirement_condition", minimum_indent=2
    )
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

    allowed_complexity = {
        "single_writer_default_branch",
        "review_branch",
        "multiwriter_worktrees",
        "integration_branch",
        "deferred",
    }
    if complexity_level not in allowed_complexity:
        report.error(f"Invalid Git complexity_level: {complexity_level or '(missing)'}")
    elif complexity_level not in {"single_writer_default_branch", "deferred"}:
        missing_conditions = []
        if not complexity_activation:
            missing_conditions.append("complexity_activation_condition")
        if not complexity_retirement:
            missing_conditions.append("complexity_retirement_condition")
        if missing_conditions:
            report.error(
                f"Git complexity level {complexity_level} requires: "
                + ", ".join(missing_conditions)
            )

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
        "tools/render_project_overview.py",
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
