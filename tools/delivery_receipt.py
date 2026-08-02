#!/usr/bin/env python3
# AIPartner framework file · protocol 0.9.0 · source: https://github.com/imtoam/AIPartner · licence: CC BY-SA 4.0
"""Shared validation for the delivery-sequence receipt contract."""

from __future__ import annotations

import hashlib
import json
import re
from datetime import datetime
from pathlib import Path


DELIVERY_CHECK_ORDER = "delivery_group -> group_order -> dependencies -> approval/exact scope"
DELIVERY_CHECK_STEPS = [
    "delivery_group",
    "group_order",
    "dependencies",
    "approval/exact scope",
]


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def evaluate_delivery_receipt(
    root: Path,
    *,
    coordination_source: str,
    validation_command: str,
    validator_path: str,
    receipt_path: str,
) -> tuple[str, dict[str, object], list[tuple[str, str]]]:
    """Return validation state, parsed receipt, and categorized issues.

    Issue categories are ``invalid``, ``stale``, and ``failed``. The returned state is one of
    ``pass``, ``missing``, ``invalid``, ``stale``, or ``failed``.
    """

    receipt_file = root / receipt_path if receipt_path else None
    if receipt_file is None or not receipt_file.is_file():
        return "missing", {}, [("failed", f"receipt does not exist: {receipt_path or '(missing)'}")]

    try:
        loaded = json.loads(receipt_file.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as error:
        return "invalid", {}, [("invalid", f"cannot read receipt: {error}")]
    if not isinstance(loaded, dict):
        return "invalid", {}, [("invalid", "receipt must be a JSON object")]

    receipt: dict[str, object] = loaded
    issues: list[tuple[str, str]] = []

    if receipt.get("schema_version") != 1:
        issues.append(("invalid", "schema_version must be 1"))
    result = receipt.get("result")
    if result not in {"pass", "fail"}:
        issues.append(("invalid", "result must be pass or fail"))
    elif result != "pass":
        issues.append(("failed", "result is not pass"))

    validated_on = receipt.get("validated_on")
    if not isinstance(validated_on, str) or not validated_on:
        issues.append(("invalid", "validated_on is missing"))
    else:
        try:
            timestamp = datetime.fromisoformat(validated_on.replace("Z", "+00:00"))
            if timestamp.tzinfo is None:
                raise ValueError("timezone missing")
        except ValueError:
            issues.append(("invalid", "validated_on must be a timezone-aware ISO timestamp"))

    contract_values = {
        "coordination_source": coordination_source,
        "validator_path": validator_path,
        "validation_command": validation_command,
        "check_order": DELIVERY_CHECK_ORDER,
    }
    for name, expected in contract_values.items():
        if receipt.get(name) != expected:
            issues.append(("stale", f"{name} does not match project_profile"))
    if receipt.get("checked_steps") != DELIVERY_CHECK_STEPS:
        issues.append(("stale", "checked_steps do not match the mandatory order"))

    errors = receipt.get("errors")
    if not isinstance(errors, list):
        issues.append(("invalid", "errors must be an array"))
    elif result == "pass" and errors:
        issues.append(("failed", "pass receipt contains errors"))

    bound_files = (
        ("coordination_source", coordination_source, "coordination_source_sha256"),
        ("validator", validator_path, "validator_sha256"),
    )
    for label, relative, digest_field in bound_files:
        target = root / relative if relative else None
        if target is None or not target.is_file():
            issues.append(("stale", f"bound {label} file is missing"))
        elif receipt.get(digest_field) != file_sha256(target):
            issues.append(("stale", f"{digest_field} is stale"))

    items = receipt.get("items")
    if not isinstance(items, list) or not items:
        issues.append(("invalid", "items must be a non-empty array"))
        items = []
    work_ids: set[str] = set()
    group_orders: dict[str, int] = {}
    order_groups: dict[int, str] = {}
    for index, item in enumerate(items):
        prefix = f"items[{index}]"
        if not isinstance(item, dict):
            issues.append(("invalid", f"{prefix} must be an object"))
            continue
        work_id = item.get("work_id")
        if not isinstance(work_id, str) or not work_id:
            issues.append(("invalid", f"{prefix}.work_id is missing"))
        elif work_id in work_ids:
            issues.append(("invalid", f"duplicate work_id: {work_id}"))
        else:
            work_ids.add(work_id)

        group_id = item.get("delivery_group")
        if not isinstance(group_id, str) or not re.fullmatch(r"DG-\d{3}", group_id):
            issues.append(("invalid", f"{prefix}.delivery_group must match DG-NNN"))
        group_order = item.get("group_order")
        if isinstance(group_order, bool) or not isinstance(group_order, int) or group_order <= 0:
            issues.append(("invalid", f"{prefix}.group_order must be a positive integer"))
        elif isinstance(group_id, str):
            if group_id in group_orders and group_orders[group_id] != group_order:
                issues.append(("invalid", f"group {group_id} has inconsistent group_order"))
            if group_order in order_groups and order_groups[group_order] != group_id:
                issues.append(("invalid", f"group_order {group_order} is assigned to several groups"))
            group_orders[group_id] = group_order
            order_groups[group_order] = group_id

        dependencies = item.get("dependencies")
        if not isinstance(dependencies, list) or not all(
            isinstance(value, str) for value in dependencies
        ):
            issues.append(("invalid", f"{prefix}.dependencies must be an array of IDs"))

        scope_owner = item.get("scope_owner")
        scope_owner_path = root / scope_owner if isinstance(scope_owner, str) else None
        if scope_owner_path is None or not scope_owner_path.is_file():
            issues.append(("stale", f"{prefix}.scope_owner is missing"))
        elif item.get("scope_owner_sha256") != file_sha256(scope_owner_path):
            issues.append(("stale", f"{prefix}.scope_owner_sha256 is stale"))

        scope_revision = item.get("scope_revision")
        if not isinstance(scope_revision, str) or not scope_revision:
            issues.append(("invalid", f"{prefix}.scope_revision is missing"))
        if item.get("approval_state") != "approved":
            issues.append(("failed", f"{prefix}.approval_state is not approved"))
        if not item.get("approval_evidence_ref"):
            issues.append(("failed", f"{prefix}.approval_evidence_ref is missing"))
        if item.get("approved_scope_revision") != scope_revision:
            issues.append(("failed", f"{prefix}.approved_scope_revision does not match"))

    categories = {category for category, _ in issues}
    if "invalid" in categories:
        state = "invalid"
    elif "stale" in categories:
        state = "stale"
    elif "failed" in categories:
        state = "failed"
    else:
        state = "pass"
    return state, receipt, issues
