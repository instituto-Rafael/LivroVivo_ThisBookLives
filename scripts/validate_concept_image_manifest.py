#!/usr/bin/env python3
from __future__ import annotations
import argparse
import json
from pathlib import Path

EXPECTED_IDS = {f"IMG-{i:03d}" for i in range(1, 11)}


def validate(data: dict) -> dict:
    errors = []
    if data.get("schema") != "concept_image_manifest_v1":
        errors.append("invalid schema")
    if data.get("claim_allowed") is not False:
        errors.append("claim_allowed must be false")
    if data.get("scientific_evidence") is not False:
        errors.append("collection cannot be scientific evidence")
    if not str(data.get("rights_state", "")).startswith("TOKEN_VAZIO"):
        errors.append("rights state must remain TOKEN_VAZIO until explicit proof")
    if data.get("publication_state") != "METADATA_ONLY_IMAGES_NOT_COMMITTED":
        errors.append("publication state must remain metadata-only")

    images = data.get("images", [])
    ids = [x.get("id") for x in images if isinstance(x, dict)]
    if set(ids) != EXPECTED_IDS or len(ids) != len(set(ids)):
        errors.append("image ids must be exactly IMG-001..IMG-010")
    hashes = [x.get("sha256") for x in images if isinstance(x, dict)]
    if len(set(hashes)) != 10 or any(
        not isinstance(value, str) or len(value) != 64 for value in hashes
    ):
        errors.append("ten unique sha256 hashes required")

    for item in images:
        if item.get("media_type") != "image/jpeg":
            errors.append(f"{item.get('id')}: detected media type must be image/jpeg")
        if (
            item.get("claim_allowed") is not False
            or item.get("scientific_evidence") is not False
        ):
            errors.append(f"{item.get('id')}: claim/evidence promotion blocked")
        if item.get("repository_path") is not None:
            errors.append(
                f"{item.get('id')}: repository_path must remain null before rights clearance"
            )
        if not str(item.get("rights_state", "")).startswith("TOKEN_VAZIO"):
            errors.append(f"{item.get('id')}: rights must remain TOKEN_VAZIO")
        if (
            item.get("bytes", 0) <= 0
            or item.get("width", 0) <= 0
            or item.get("height", 0) <= 0
        ):
            errors.append(f"{item.get('id')}: invalid media dimensions or size")
        if not item.get("technical_boundary"):
            errors.append(f"{item.get('id')}: missing technical boundary")

    return {
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "image_count": len(images),
        "claim_allowed": False,
        "publication_state": data.get("publication_state"),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="data/media/concept_images_manifest.v1.json")
    parser.add_argument("--write-report")
    args = parser.parse_args()
    data = json.loads(Path(args.input).read_text(encoding="utf-8"))
    report = validate(data)
    output = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.write_report:
        Path(args.write_report).write_text(output, encoding="utf-8")
    print(output, end="")
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
