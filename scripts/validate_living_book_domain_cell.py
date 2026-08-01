#!/usr/bin/env python3
"""Validate RAFAELIA Living Book Domain Cell V1 with Python stdlib only."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

EXPECTED_STATES = [
    "CAPTURED", "CLASSIFIED", "MAPPED", "PROPOSED", "HUMAN_APPROVED",
    "EXECUTED_BOUNDED", "VERIFIED", "RECEIPTED", "INDEXED",
]
RELATION_TYPES = {
    "EXPLAINS", "MEASURES", "VALIDATES", "TRANSLATES_TO_DOMAIN",
    "DEPENDS_ON", "CONTRADICTS", "GOVERNED_BY", "EVIDENCED_BY",
}
FORBIDDEN_AUTOMATIC = {"EXECUTE", "PUBLISH", "DISCLOSE_PRIVATE", "PROMOTE_CLAIM"}


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def digests(value: Any) -> dict[str, str]:
    data = canonical_bytes(value)
    return {
        "sha256": hashlib.sha256(data).hexdigest(),
        "sha3_256": hashlib.sha3_256(data).hexdigest(),
        "blake2b_256": hashlib.blake2b(data, digest_size=32).hexdigest(),
    }


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def validate_cell(cell: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    require(cell.get("schema") == "rafaelia.living-book.domain-cell/v1", "invalid cell schema", errors)
    payload = cell.get("payload")
    require(isinstance(payload, dict), "payload must be an object", errors)
    if not isinstance(payload, dict):
        return errors

    seed = payload.get("seed", {})
    governance = payload.get("governance", {})
    privacy = payload.get("privacy_security", {})
    workflow = payload.get("workflow_proof", {})
    mirrors = payload.get("mirrors", {})

    require(seed.get("source_disclosure") == "NO_RAW_PRIVATE_TEXT", "seed must not disclose raw private text", errors)
    require(seed.get("claim_allowed") is False, "seed claim_allowed must be false", errors)
    require(governance.get("claim_allowed") is False, "governance claim_allowed must be false", errors)
    require(workflow.get("claim_allowed") is False, "workflow claim_allowed must be false", errors)
    require(governance.get("ai_can_approve") is False, "AI cannot approve", errors)
    require(governance.get("approval_binding") == "EXACT_CELL_SHA256", "approval must bind exact cell SHA-256", errors)

    human = mirrors.get("human", {})
    ai = mirrors.get("ai", {})
    require("FINAL" in str(human.get("role", "")), "human mirror must hold final authority", errors)
    require("ONLY" in str(ai.get("role", "")), "AI mirror must be advisory only", errors)
    forbidden = set(ai.get("forbidden", []))
    require({"self_approve", "publish", "disclose_private", "promote_claim", "execute_untrusted", "overwrite_seed"}.issubset(forbidden), "AI forbidden-action set incomplete", errors)

    require(privacy.get("raw_private_text_committed") is False, "raw private text must not be committed", errors)
    require(privacy.get("secrets_allowed") is False, "secrets must be forbidden", errors)
    require(privacy.get("credentials_allowed") is False, "credentials must be forbidden", errors)
    require(privacy.get("untrusted_content_execution") == "FORBIDDEN", "untrusted content execution must be forbidden", errors)
    require(privacy.get("public_export_default") == "DENY", "public export must default deny", errors)

    modules = payload.get("modules", [])
    require(isinstance(modules, list) and bool(modules), "at least one module is required", errors)
    module_ids: set[str] = set()
    if isinstance(modules, list):
        for module in modules:
            module_id = module.get("id")
            require(isinstance(module_id, str) and module_id not in module_ids, f"invalid or duplicate module id: {module_id}", errors)
            if isinstance(module_id, str):
                module_ids.add(module_id)
            require(module.get("required_user_knowledge") == [], f"module {module_id} may not require technical user knowledge", errors)
            if module.get("kind") != "DOMAIN":
                require(module.get("must_translate_to_domain_language") is True, f"support module {module_id} must translate to domain language", errors)

    for relation in payload.get("relations", []):
        require(relation.get("type") in RELATION_TYPES, f"unknown relation type: {relation.get('type')}", errors)
        require(relation.get("from") in module_ids, f"relation source missing: {relation.get('from')}", errors)
        require(relation.get("to") in module_ids, f"relation target missing: {relation.get('to')}", errors)

    require(workflow.get("state_order") == EXPECTED_STATES, "state order changed or incomplete", errors)
    automatic_forbidden = set(workflow.get("automatic_actions_forbidden", []))
    require(FORBIDDEN_AUTOMATIC.issubset(automatic_forbidden), "automatic forbidden-action set incomplete", errors)
    for trigger in workflow.get("triggers", []):
        if trigger.get("automatic") is True:
            require(trigger.get("action") not in FORBIDDEN_AUTOMATIC, f"forbidden automatic trigger: {trigger.get('action')}", errors)

    integrity = cell.get("integrity", {})
    require(integrity.get("canonicalization") == "json-sort-keys-utf8-no-whitespace/v1", "unsupported canonicalization", errors)
    require(integrity.get("digests") == digests(payload), "cell payload triple digest mismatch", errors)
    return errors


def validate_ledger(ledger: dict[str, Any], cell: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    require(ledger.get("schema") == "rafaelia.living-book.ledger-event/v1", "invalid ledger schema", errors)
    require(ledger.get("object_id") == cell.get("cell_id"), "ledger object_id mismatch", errors)
    require(ledger.get("event_type") == "GENESIS_REGISTER", "first event must be GENESIS_REGISTER", errors)
    require(ledger.get("previous_event_sha256") is None, "genesis previous_event_sha256 must be null", errors)
    body = ledger.get("body", {})
    require(body.get("claim_allowed") is False, "ledger claim_allowed must be false", errors)
    require(body.get("source_raw_private_text_stored") is False, "ledger must record no raw private text", errors)
    require(body.get("object_digests") == cell.get("integrity", {}).get("digests"), "ledger object digests mismatch", errors)
    require(ledger.get("integrity", {}).get("digests") == digests(body), "ledger body triple digest mismatch", errors)
    return errors


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"{path}: top-level JSON must be an object")
    return value


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("cell", type=Path)
    parser.add_argument("ledger", type=Path)
    args = parser.parse_args()
    try:
        cell = load_json(args.cell)
        ledger = load_json(args.ledger)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"FAIL: {exc}")
        return 2
    errors = validate_cell(cell) + validate_ledger(ledger, cell)
    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1
    print("PASS: Living Book Domain Cell V1")
    print(json.dumps({"cell_id": cell["cell_id"], "digests": cell["integrity"]["digests"], "claim_allowed": False}, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
