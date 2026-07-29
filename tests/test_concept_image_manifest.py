import copy
import json
import unittest
from pathlib import Path
from scripts.validate_concept_image_manifest import validate

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads(
    (ROOT / "data/media/concept_images_manifest.v1.json").read_text(encoding="utf-8")
)


class TestManifest(unittest.TestCase):
    def test_canonical(self):
        self.assertEqual(validate(copy.deepcopy(DATA))["status"], "PASS")

    def test_claim_block(self):
        data = copy.deepcopy(DATA)
        data["claim_allowed"] = True
        self.assertEqual(validate(data)["status"], "FAIL")

    def test_rights_cannot_be_inferred(self):
        data = copy.deepcopy(DATA)
        data["rights_state"] = "PUBLIC_DOMAIN"
        self.assertEqual(validate(data)["status"], "FAIL")

    def test_images_cannot_be_published_yet(self):
        data = copy.deepcopy(DATA)
        data["images"][0]["repository_path"] = "assets/a.jpg"
        self.assertEqual(validate(data)["status"], "FAIL")

    def test_image_is_not_evidence(self):
        data = copy.deepcopy(DATA)
        data["images"][0]["scientific_evidence"] = True
        self.assertEqual(validate(data)["status"], "FAIL")

    def test_hash_uniqueness(self):
        data = copy.deepcopy(DATA)
        data["images"][1]["sha256"] = data["images"][0]["sha256"]
        self.assertEqual(validate(data)["status"], "FAIL")

    def test_format_detection(self):
        data = copy.deepcopy(DATA)
        data["images"][0]["media_type"] = "image/png"
        self.assertEqual(validate(data)["status"], "FAIL")


if __name__ == "__main__":
    unittest.main()
