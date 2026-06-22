#!/usr/bin/env python3
"""Check whether repo-relative file references in package docs exist on disk."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


PATH_PATTERN = re.compile(
    r"(?<![A-Za-z0-9_/.-])([A-Za-z0-9_./-]+\.(?:md|html|py))(?![A-Za-z0-9_/.-])"
)


def extract_paths(text: str) -> list[str]:
    seen: list[str] = []
    for match in PATH_PATTERN.finditer(text):
        path = match.group(1)
        if path not in seen:
            seen.append(path)
    return seen


def check_doc(doc_path: Path, repo_root: Path) -> tuple[list[str], list[str]]:
    text = doc_path.read_text()
    found = extract_paths(text)
    missing: list[str] = []
    for rel in found:
        if not (repo_root / rel).exists():
            missing.append(rel)
    return found, missing


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--repo-root",
        default=".",
        help="Repository root containing the package docs.",
    )
    parser.add_argument(
        "docs",
        nargs="*",
        help="Package docs to check. Defaults to README.md and manuscript_package_index.md.",
    )
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    docs = args.docs or ["README.md", "manuscript_package_index.md"]
    missing_total = 0

    for doc in docs:
        doc_path = (repo_root / doc).resolve()
        if not doc_path.exists():
            print(f"ERROR: doc not found: {doc}")
            missing_total += 1
            continue

        found, missing = check_doc(doc_path, repo_root)
        print(f"Doc: {doc}")
        print(f"Referenced package paths: {len(found)}")
        print(f"Missing targets: {len(missing)}")
        if missing:
            for rel in missing:
                print(f"- {rel}")
        print()
        missing_total += len(missing)

    return 1 if missing_total else 0


if __name__ == "__main__":
    raise SystemExit(main())
