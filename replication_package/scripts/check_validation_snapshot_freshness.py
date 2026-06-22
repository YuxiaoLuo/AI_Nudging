#!/usr/bin/env python3
"""Check whether a saved validation snapshot still matches the current package state."""

from __future__ import annotations

import argparse
import hashlib
import re
import subprocess
import sys
from pathlib import Path


HEAD_PATTERN = re.compile(r"^- Repository HEAD at generation: `([^`]+)`$", re.MULTILINE)
FINGERPRINT_PATTERN = re.compile(r"^- `([^`]+)`: sha256 `([^`]+)`$", re.MULTILINE)


def sha256_prefix(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()[:12]


def git_head(repo_root: Path) -> str | None:
    completed = subprocess.run(
        ["git", "-C", str(repo_root), "rev-parse", "HEAD"],
        capture_output=True,
        text=True,
    )
    if completed.returncode != 0:
        return None
    return completed.stdout.strip() or None


def parse_report(report_path: Path) -> tuple[str | None, list[tuple[str, str]]]:
    text = report_path.read_text()
    head_match = HEAD_PATTERN.search(text)
    saved_head = head_match.group(1) if head_match else None
    fingerprints = FINGERPRINT_PATTERN.findall(text)
    if not fingerprints:
        raise ValueError("No input fingerprints found in validation snapshot.")
    return saved_head, fingerprints


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--repo-root",
        default=".",
        help="Repository root containing the saved validation snapshot.",
    )
    parser.add_argument(
        "--report-md",
        default="manuscript_package_validation_report.md",
        help="Path to the saved validation snapshot markdown file.",
    )
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    report_path = Path(args.report_md).resolve()
    saved_head, fingerprints = parse_report(report_path)
    current_head = git_head(repo_root)

    stale = False
    print(f"Report: {report_path}")
    if saved_head:
        print(f"Saved HEAD: {saved_head}")
    if current_head:
        print(f"Current HEAD: {current_head}")
        if saved_head and saved_head != current_head:
            print("- Repository HEAD differs from the saved snapshot.")
            stale = True

    print("\nTracked input comparison:")
    for rel_path, saved_hash in fingerprints:
        abs_path = (repo_root / rel_path).resolve()
        if not abs_path.exists():
            print(f"- {rel_path}: MISSING (saved sha256 {saved_hash})")
            stale = True
            continue
        current_hash = sha256_prefix(abs_path)
        status = "MATCH" if current_hash == saved_hash else "CHANGED"
        print(f"- {rel_path}: {status} (saved {saved_hash}, current {current_hash})")
        if current_hash != saved_hash:
            stale = True

    if stale:
        print("\nSnapshot freshness: STALE")
        return 1

    print("\nSnapshot freshness: CURRENT")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # pragma: no cover - diagnostic path
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(2)
