#!/usr/bin/env python3
# AIPartner framework file · protocol 0.9.0 · source: https://github.com/imtoam/AIPartner · licence: CC BY-SA 4.0
"""Render project-overview.html from declared AIPartner project sources.

The renderer uses only the Python standard library. It fails before replacing the output when a
declared source is missing and writes the completed page atomically. The page is a derived view;
it never updates project_profile.yaml or another authoritative source.
"""

from __future__ import annotations

import html
import os
import re
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

try:
    from delivery_receipt import DELIVERY_CHECK_ORDER, evaluate_delivery_receipt
except ModuleNotFoundError:
    from tools.delivery_receipt import DELIVERY_CHECK_ORDER, evaluate_delivery_receipt


PERSPECTIVES = (
    ("management", "Management consultation", "perspective-management"),
    ("business", "Business and domain operations", "perspective-business"),
    ("operations", "System operations", "perspective-operations"),
    ("architecture_delivery", "Architecture and delivery", "perspective-architecture-delivery"),
)

PERSPECTIVE_STATES = {
    "active",
    "not_yet_available",
    "not_applicable",
    "blocked",
    "degraded",
}


def scalar(raw: str) -> str:
    value = raw.strip()
    if " #" in value:
        value = value.split(" #", 1)[0].rstrip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        return value[1:-1]
    return value


def top_block(lines: list[str], key: str) -> list[str]:
    start = next((i for i, line in enumerate(lines) if line == f"{key}:"), None)
    if start is None:
        return []
    result = [lines[start]]
    for line in lines[start + 1 :]:
        if line and not line.startswith(" "):
            break
        result.append(line)
    return result


def child_block(lines: list[str], key: str, indent: int) -> list[str]:
    prefix = " " * indent + key + ":"
    start = next((i for i, line in enumerate(lines) if line.startswith(prefix)), None)
    if start is None:
        return []
    result = [lines[start]]
    for line in lines[start + 1 :]:
        if not line.strip():
            result.append(line)
            continue
        current = len(line) - len(line.lstrip(" "))
        if current <= indent:
            break
        result.append(line)
    return result


def field(lines: list[str], key: str, minimum_indent: int = 0) -> str:
    pattern = re.compile(rf"^\s{{{minimum_indent},}}{re.escape(key)}:\s*(.*?)\s*$")
    for line in lines:
        match = pattern.match(line)
        if match:
            return scalar(match.group(1))
    return ""


def list_values(lines: list[str], key: str, indent: int) -> list[str]:
    values: list[str] = []
    for line in child_block(lines, key, indent)[1:]:
        match = re.match(r"^\s+-\s*(.*?)\s*$", line)
        if match:
            values.append(scalar(match.group(1)))
    return values


def unresolved(lines: list[str]) -> list[dict[str, str]]:
    result: list[dict[str, str]] = []
    current: dict[str, str] | None = None
    for line in top_block(lines, "unresolved_decisions")[1:]:
        start = re.match(r"^\s{2}- id:\s*(.*?)\s*$", line)
        if start:
            if current:
                result.append(current)
            current = {"id": scalar(start.group(1))}
            continue
        if current is None:
            continue
        item = re.match(r"^\s{4}([a-zA-Z_]+):\s*(.*?)\s*$", line)
        if item:
            current[item.group(1)] = scalar(item.group(2))
    if current:
        result.append(current)
    return result


def git_version(root: Path) -> str:
    result = subprocess.run(
        ["git", "-C", str(root), "rev-parse", "--short", "HEAD"],
        capture_output=True,
        text=True,
        check=False,
    )
    return result.stdout.strip() if result.returncode == 0 else "unversioned"


def markdown_to_html(text: str) -> str:
    """Render a deliberately small, safe Markdown subset for project-control documents."""
    output: list[str] = []
    paragraph: list[str] = []
    list_kind = ""
    in_code = False
    code_lines: list[str] = []

    def flush_paragraph() -> None:
        if paragraph:
            output.append(f"<p>{html.escape(' '.join(paragraph))}</p>")
            paragraph.clear()

    def close_list() -> None:
        nonlocal list_kind
        if list_kind:
            output.append(f"</{list_kind}>")
            list_kind = ""

    for raw in text.splitlines():
        line = raw.rstrip()
        if line.startswith("```"):
            flush_paragraph()
            close_list()
            if in_code:
                output.append("<pre><code>" + html.escape("\n".join(code_lines)) + "</code></pre>")
                code_lines.clear()
                in_code = False
            else:
                in_code = True
            continue
        if in_code:
            code_lines.append(line)
            continue
        heading = re.match(r"^(#{1,4})\s+(.+)$", line)
        if heading:
            flush_paragraph()
            close_list()
            level = len(heading.group(1)) + 1
            output.append(f"<h{level}>{html.escape(heading.group(2))}</h{level}>")
            continue
        bullet = re.match(r"^\s*[-*]\s+(.+)$", line)
        numbered = re.match(r"^\s*\d+[.)]\s+(.+)$", line)
        if bullet or numbered:
            flush_paragraph()
            wanted = "ul" if bullet else "ol"
            if list_kind != wanted:
                close_list()
                output.append(f"<{wanted}>")
                list_kind = wanted
            item = bullet.group(1) if bullet else numbered.group(1)
            output.append(f"<li>{html.escape(item)}</li>")
            continue
        if not line.strip():
            flush_paragraph()
            close_list()
            continue
        paragraph.append(line.strip())

    flush_paragraph()
    close_list()
    if in_code:
        output.append("<pre><code>" + html.escape("\n".join(code_lines)) + "</code></pre>")
    return "\n".join(output)


def render(root: Path) -> Path:
    profile_path = root / "project_profile.yaml"
    if not profile_path.is_file():
        raise ValueError("project_profile.yaml does not exist")
    lines = profile_path.read_text(encoding="utf-8").splitlines()
    project = top_block(lines, "project")
    initialization = top_block(lines, "initialization")
    delivery = top_block(lines, "delivery_control")
    interface = top_block(lines, "human_interface")
    overview = child_block(interface, "overview", 2)
    perspective_root = child_block(interface, "perspectives", 2)

    project_name = field(project, "name", 2) or "Unnamed project"
    status = field(initialization, "status", 2) or "unknown"
    output_relative = field(overview, "path", 4)
    view_id = field(overview, "view_id", 4)
    page_role = field(overview, "page_role", 4)
    locale = field(overview, "locale", 4)
    sources = list_values(overview, "sources", 4)
    if output_relative != "project-overview.html":
        raise ValueError("default overview path must be project-overview.html")
    if view_id != "project-overview" or page_role != "project-overview":
        raise ValueError("default overview view_id and page_role must be project-overview")
    if not locale:
        raise ValueError("default overview locale is missing")
    if not sources:
        raise ValueError("default overview has no declared sources")

    delivery_state = field(delivery, "state", 2)
    delivery_source = field(delivery, "coordination_source", 2)
    delivery_command = field(delivery, "validation_command", 2)
    delivery_validator_path = field(delivery, "validator_path", 2)
    delivery_receipt_path = field(delivery, "receipt_path", 2)
    delivery_group_format = field(delivery, "delivery_group_id_format", 2)
    delivery_check_order = field(delivery, "check_order", 2)
    delivery_trigger = field(delivery, "trigger", 2)
    if delivery_state not in {"inactive", "active"}:
        raise ValueError(f"invalid delivery-control state: {delivery_state or '(missing)'}")
    if delivery_group_format != "DG-NNN" or delivery_check_order != DELIVERY_CHECK_ORDER:
        raise ValueError("delivery-control identity or check-order contract is invalid")
    if delivery_state == "active":
        if not all(
            (
                delivery_source,
                delivery_command,
                delivery_validator_path,
                delivery_receipt_path,
            )
        ):
            raise ValueError(
                "active delivery control requires source, validator, command, and receipt paths"
            )
        if delivery_source not in sources:
            raise ValueError(
                "active delivery coordination source is absent from overview.sources: "
                + delivery_source
            )
        delivery_validation_state, delivery_receipt, delivery_issues = evaluate_delivery_receipt(
            root,
            coordination_source=delivery_source,
            validation_command=delivery_command,
            validator_path=delivery_validator_path,
            receipt_path=delivery_receipt_path,
        )
    elif not delivery_trigger:
        raise ValueError("inactive delivery control requires an activation trigger")
    else:
        if delivery_source or delivery_command or delivery_validator_path or delivery_receipt_path:
            raise ValueError(
                "inactive delivery control must not declare source, validator, command, or receipt"
            )
        delivery_validation_state = "inactive"
        delivery_receipt = {}
        delivery_issues = []

    perspective_contracts: list[dict[str, object]] = []
    for perspective_id, title, html_id in PERSPECTIVES:
        perspective = child_block(perspective_root, perspective_id, 4)
        audience = field(perspective, "audience", 6)
        purpose = field(perspective, "purpose", 6)
        owner = field(perspective, "owner", 6)
        source_state = field(perspective, "source_state", 6)
        state_reason = field(perspective, "state_reason", 6)
        perspective_sources = list_values(perspective, "sources", 6)
        activation_trigger = field(perspective, "activation_trigger", 6)
        if not perspective:
            raise ValueError(f"required human-interface perspective is missing: {perspective_id}")
        if not audience or not purpose or not owner or not state_reason:
            raise ValueError(
                f"perspective {perspective_id} requires audience, purpose, owner, and state_reason"
            )
        if source_state not in PERSPECTIVE_STATES:
            raise ValueError(
                f"perspective {perspective_id} has invalid source_state: "
                f"{source_state or '(missing)'}"
            )
        if source_state == "active" and not perspective_sources:
            raise ValueError(f"active perspective {perspective_id} requires declared sources")
        if source_state != "active" and not activation_trigger:
            raise ValueError(
                f"inactive perspective {perspective_id} requires an activation or recovery trigger"
            )
        undeclared = [source for source in perspective_sources if source not in sources]
        if undeclared:
            raise ValueError(
                f"perspective {perspective_id} uses sources absent from overview.sources: "
                + ", ".join(undeclared)
            )
        perspective_contracts.append(
            {
                "id": perspective_id,
                "title": title,
                "html_id": html_id,
                "audience": audience,
                "purpose": purpose,
                "owner": owner,
                "source_state": source_state,
                "state_reason": state_reason,
                "sources": perspective_sources,
                "activation_trigger": activation_trigger,
            }
        )

    missing = [source for source in sources if not (root / source).is_file()]
    if missing:
        raise ValueError("declared overview sources are missing: " + ", ".join(missing))

    generated_on = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    version = git_version(root)
    source_links = "\n".join(
        f'<li><a href="{html.escape(source, quote=True)}">{html.escape(source)}</a></li>'
        for source in sources
    )
    open_items = [item for item in unresolved(lines) if item.get("status", "").lower() == "open"]
    if open_items:
        decisions = "\n".join(
            "<article class=\"decision\">"
            f"<strong>{html.escape(item.get('id', '(missing ID)'))}</strong>"
            f"<p>{html.escape(item.get('question', 'Unspecified question'))}</p>"
            f"<span>Owner: {html.escape(item.get('owner', 'unassigned'))}</span>"
            "</article>"
            for item in open_items
        )
    else:
        decisions = '<p class="empty">No open decisions are recorded.</p>'

    if delivery_state == "active":
        delivery_source_html = (
            f'<a href="{html.escape(delivery_source, quote=True)}">'
            f"{html.escape(delivery_source)}</a>"
        )
        delivery_validator_html = (
            f'<a href="{html.escape(delivery_validator_path, quote=True)}">'
            f"{html.escape(delivery_validator_path)}</a>"
        )
        if (root / delivery_receipt_path).is_file():
            delivery_receipt_html = (
                f'<a href="{html.escape(delivery_receipt_path, quote=True)}">'
                f"{html.escape(delivery_receipt_path)}</a>"
            )
        else:
            delivery_receipt_html = f"<code>{html.escape(delivery_receipt_path)}</code>"
        if delivery_issues:
            delivery_issue_html = "<ul>" + "".join(
                f"<li>{html.escape(category)}: {html.escape(issue)}</li>"
                for category, issue in delivery_issues
            ) + "</ul>"
        else:
            delivery_issue_html = '<p class="empty">No receipt discrepancies detected.</p>'
        validated_on = delivery_receipt.get("validated_on")
        source_digest = delivery_receipt.get("coordination_source_sha256")
        validator_digest = delivery_receipt.get("validator_sha256")
        readiness = (
            "Implementation gate passed."
            if delivery_validation_state == "pass"
            else "Implementation is blocked until a current pass receipt exists."
        )
        delivery_detail = (
            f"<p><strong>Coordination source:</strong> {delivery_source_html}</p>"
            f"<p><strong>Validator:</strong> {delivery_validator_html}</p>"
            f"<p><strong>Validation command:</strong> <code>{html.escape(delivery_command)}</code></p>"
            f"<p><strong>Receipt:</strong> {delivery_receipt_html}</p>"
            f"<p><strong>Validated on:</strong> {html.escape(str(validated_on or 'not_available'))}</p>"
            f"<p><strong>Source digest:</strong> <code>{html.escape(str(source_digest or 'not_available'))}</code></p>"
            f"<p><strong>Validator digest:</strong> <code>{html.escape(str(validator_digest or 'not_available'))}</code></p>"
            f'<p class="readiness readiness-{html.escape(delivery_validation_state, quote=True)}">'
            f"{html.escape(readiness)}</p>{delivery_issue_html}"
        )
    else:
        delivery_detail = (
            '<p class="empty">Grouped delivery is not active.</p>'
            f"<p><strong>Activation trigger:</strong> {html.escape(delivery_trigger)}</p>"
        )
    delivery_gate_html = (
        '<div id="delivery-sequence-gate" class="delivery-gate">'
        '<h3>Delivery sequence gate</h3>'
        f'<p><strong>Configuration state:</strong> {html.escape(delivery_state)}</p>'
        f'<p><strong>Validation state:</strong> {html.escape(delivery_validation_state)}</p>'
        f'<p><strong>Group ID format:</strong> {html.escape(delivery_group_format)}</p>'
        f'<p><strong>Required check order:</strong> <code>{html.escape(delivery_check_order)}</code></p>'
        f"{delivery_detail}</div>"
    )

    perspective_sections: list[str] = []
    for contract in perspective_contracts:
        perspective_sources = contract["sources"]
        assert isinstance(perspective_sources, list)
        if perspective_sources:
            perspective_links = "".join(
                f'<li><a href="{html.escape(source, quote=True)}">{html.escape(source)}</a></li>'
                for source in perspective_sources
            )
            source_contract = f"<ul>{perspective_links}</ul>"
        else:
            source_contract = (
                '<p class="empty">No authoritative source is active yet. This is an explicit '
                "source state, not a healthy or empty result.</p>"
            )
        trigger = str(contract["activation_trigger"])
        trigger_html = (
            '<p class="trigger"><strong>Activation / recovery trigger:</strong> '
            f"{html.escape(trigger)}</p>"
            if trigger
            else ""
        )
        decision_html = (
            '<div class="management-decisions"><h3>Decisions requiring attention</h3>'
            f'<div class="grid">{decisions}</div></div>'
            if contract["id"] == "management"
            else ""
        )
        delivery_html = (
            delivery_gate_html if contract["id"] == "architecture_delivery" else ""
        )
        perspective_sections.append(
            f'<section id="{contract["html_id"]}" class="perspective">'
            '<div class="perspective-heading">'
            f'<div><p class="audience">For {html.escape(str(contract["audience"]))}</p>'
            f'<h2>{html.escape(str(contract["title"]))}</h2></div>'
            f'<span class="state state-{html.escape(str(contract["source_state"]), quote=True)}">'
            f'{html.escape(str(contract["source_state"]))}</span></div>'
            f'<p>{html.escape(str(contract["purpose"]))}</p>'
            f'<p><strong>Accountable owner:</strong> {html.escape(str(contract["owner"]))}</p>'
            f'<p><strong>State reason:</strong> {html.escape(str(contract["state_reason"]))}</p>'
            '<h3>Declared sources</h3>'
            f"{source_contract}{trigger_html}{decision_html}{delivery_html}</section>"
        )

    source_sections = []
    for source in sources:
        if not source.endswith(".md"):
            continue
        source_text = (root / source).read_text(encoding="utf-8")
        source_sections.append(
            f'<section class="source"><p class="source-path">{html.escape(source)}</p>'
            f"{markdown_to_html(source_text)}</section>"
        )

    document = f"""<!doctype html>
<html lang="{html.escape(locale, quote=True)}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="aipartner-page-role" content="project-overview">
  <meta name="aipartner-view-id" content="project-overview">
  <meta name="aipartner-view-locale" content="{html.escape(locale, quote=True)}">
  <meta name="aipartner-derived-view" content="true">
  <meta name="aipartner-source-version" content="{html.escape(version, quote=True)}">
  <meta name="aipartner-generated-on" content="{html.escape(generated_on, quote=True)}">
  <meta name="aipartner-view-freshness" content="current">
  <title>{html.escape(project_name)} / Project overview</title>
  <style>
    :root {{ color-scheme: light; --ink:#172022; --muted:#607074; --paper:#f4f1e9;
      --card:#fffdf8; --line:#d7d2c5; --accent:#0d685f; --warn:#9b4d18; }}
    * {{ box-sizing:border-box; }} body {{ margin:0; background:var(--paper); color:var(--ink);
      font:16px/1.55 system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif; }}
    header,main,footer {{ width:min(1120px,calc(100% - 32px)); margin:auto; }}
    header {{ padding:64px 0 30px; }} h1 {{ font-size:clamp(2rem,6vw,4.6rem); line-height:1; margin:.2em 0; }}
    .eyebrow,.source-path {{ color:var(--accent); font-weight:700; letter-spacing:.08em; text-transform:uppercase; }}
    .status {{ display:inline-block; border:1px solid var(--accent); border-radius:999px; padding:5px 12px; }}
    .notice {{ border-left:5px solid var(--warn); background:var(--card); padding:18px 22px; margin:22px 0; }}
    .grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(260px,1fr)); gap:18px; }}
    section,.decision {{ background:var(--card); border:1px solid var(--line); border-radius:16px; padding:24px; margin:18px 0; }}
    .decision {{ margin:0; }} a {{ color:var(--accent); }} pre {{ overflow:auto; background:#172022; color:#f7f4eb; padding:16px; border-radius:10px; }}
    .control-grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(300px,1fr)); gap:18px; }}
    .control-grid .perspective {{ margin:0; }} .perspective-heading {{ display:flex; gap:18px;
      align-items:flex-start; justify-content:space-between; }} .audience {{ color:var(--muted); margin:0; }}
    .state {{ border:1px solid var(--line); border-radius:999px; padding:5px 10px; font-size:.8rem;
      font-weight:750; white-space:nowrap; }} .state-active {{ color:var(--accent); border-color:var(--accent); }}
    .state-blocked,.state-degraded {{ color:var(--warn); border-color:var(--warn); }}
    .trigger {{ border-top:1px solid var(--line); margin-top:18px; padding-top:14px; }}
    .management-decisions {{ border-top:1px solid var(--line); margin-top:22px; padding-top:10px; }}
    .delivery-gate {{ border-top:1px solid var(--line); margin-top:22px; padding-top:10px; }}
    .readiness {{ border-left:4px solid var(--warn); padding:10px 14px; }}
    .readiness-pass {{ border-color:var(--accent); }}
    footer {{ color:var(--muted); padding:32px 0 56px; }}
  </style>
</head>
<body>
  <header>
    <p class="eyebrow">AIPartner derived project view</p>
    <h1>{html.escape(project_name)}</h1>
    <p class="status">Initialization status: {html.escape(status)}</p>
    <div class="notice">This page is generated from declared sources. It is not an independent
      source of project truth. Source errors must be corrected in their owning files.</div>
  </header>
  <main>
    <section>
      <h2>View provenance</h2>
      <p>Generated: {html.escape(generated_on)} · Source version: {html.escape(version)} ·
        Locale: {html.escape(locale)} · Freshness: current</p>
      <ul>{source_links}</ul>
    </section>
    <section>
      <h2>Human control surface</h2>
      <p>Humans govern direction, architecture, scope, progress, cadence, and risk through four
        stable perspectives. Missing runtime or domain evidence is shown explicitly.</p>
    </section>
    <div class="control-grid">{''.join(perspective_sections)}</div>
    {''.join(source_sections)}
  </main>
  <footer>Generated by tools/render_project_overview.py from AIPartner project sources.</footer>
</body>
</html>
"""

    output_path = root / output_relative
    output_path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(
        prefix=f".{output_path.name}.", suffix=".tmp", dir=output_path.parent
    )
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
            handle.write(document)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary_name, output_path)
    except Exception:
        try:
            os.unlink(temporary_name)
        except FileNotFoundError:
            pass
        raise
    return output_path


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    try:
        output = render(root)
    except (OSError, ValueError) as error:
        print(f"ERROR {error}", file=sys.stderr)
        return 1
    print(f"Rendered {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
