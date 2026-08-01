#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("validator", ROOT / "scripts" / "validate_living_book_domain_cell.py")
validator = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(validator)


def load(name: str):
    with (ROOT / name).open("r", encoding="utf-8") as handle:
        return json.load(handle)


class LivingBookDomainCellTests(unittest.TestCase):
    def setUp(self):
        self.cell = load("data/living_book/domain_cells/music.v1.json")
        self.ledger = load("data/living_book/ledger/genesis.music.v1.json")

    def resign_cell(self):
        self.cell["integrity"]["digests"] = validator.digests(self.cell["payload"])

    def test_valid_fixture(self):
        self.assertEqual([], validator.validate_cell(self.cell))
        self.assertEqual([], validator.validate_ledger(self.ledger, self.cell))

    def test_ai_cannot_be_final_authority(self):
        self.cell["payload"]["mirrors"]["ai"]["role"] = "FINAL_AUTHORITY"
        self.resign_cell()
        self.assertTrue(any("advisory only" in e for e in validator.validate_cell(self.cell)))

    def test_raw_private_text_fails_closed(self):
        self.cell["payload"]["privacy_security"]["raw_private_text_committed"] = True
        self.resign_cell()
        self.assertTrue(any("raw private text" in e for e in validator.validate_cell(self.cell)))

    def test_claim_promotion_fails_closed(self):
        self.cell["payload"]["governance"]["claim_allowed"] = True
        self.resign_cell()
        self.assertTrue(any("governance claim_allowed" in e for e in validator.validate_cell(self.cell)))

    def test_support_module_cannot_require_programming(self):
        self.cell["payload"]["modules"][2]["required_user_knowledge"] = ["Python"]
        self.resign_cell()
        self.assertTrue(any("technical user knowledge" in e for e in validator.validate_cell(self.cell)))

    def test_forbidden_automatic_execution(self):
        self.cell["payload"]["workflow_proof"]["triggers"].append({"on": "SEED_ADDED", "action": "EXECUTE", "automatic": True})
        self.resign_cell()
        self.assertTrue(any("forbidden automatic trigger" in e for e in validator.validate_cell(self.cell)))

    def test_payload_tamper_breaks_digest(self):
        self.cell["payload"]["domain"]["title"] = "tampered"
        self.assertTrue(any("digest mismatch" in e for e in validator.validate_cell(self.cell)))

    def test_ledger_cannot_point_to_other_object_digest(self):
        self.ledger["body"]["object_digests"]["sha256"] = "0" * 64
        self.ledger["integrity"]["digests"] = validator.digests(self.ledger["body"])
        self.assertTrue(any("object digests mismatch" in e for e in validator.validate_ledger(self.ledger, self.cell)))


if __name__ == "__main__":
    unittest.main()
