#!/usr/bin/env python3
"""Check whether a saved validation snapshot still matches the current package state."""

from __future__ import annotations

import argparse
import hashlib
import re
import subprocess
import sys
from datetime import datetime, timezone
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
        raise ValueError("No fingerprints found in validation snapshot.")
    return saved_head, fingerprints


def markdown_report(
    report_path: Path,
    repo_root: Path,
    saved_head: str | None,
    current_head: str | None,
    comparisons: list[tuple[str, str, str, str | None]],
    stale: bool,
    head_drift: bool,
) -> str:
    generated_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    lines = [
        "# Manuscript Package Validation Freshness Report",
        "",
        "## Purpose",
        "This file records whether the saved manuscript-package validation snapshot still matches the current repository state.",
        "",
        "## Freshness metadata",
        f"- Generated at (UTC): `{generated_at}`",
        f"- Repository root: `{repo_root}`",
        f"- Validation snapshot checked: `{report_path}`",
    ]
    if saved_head:
        lines.append(f"- Saved snapshot HEAD: `{saved_head}`")
    if current_head:
        lines.append(f"- Repository HEAD when this freshness check ran: `{current_head}`")
    lines.append(f"- Repository HEAD drift since snapshot: `{'YES' if head_drift else 'NO'}`")
    lines.extend(
        [
            "",
            "## Tracked fingerprint comparison",
        ]
    )
    for rel_path, status, saved_hash, current_hash in comparisons:
        if current_hash is None:
            lines.append(f"- `{rel_path}`: `{status}` (saved `{saved_hash}`, current file missing)")
        else:
            lines.append(f"- `{rel_path}`: `{status}` (saved `{saved_hash}`, current `{current_hash}`)")
    lines.extend(
        [
            "",
            "## Result",
            f"- Snapshot freshness: `{'CURRENT' if not stale else 'STALE'}`",
        ]
    )
    if stale:
        lines.append("- Action: rerun `replication_package/scripts/run_validation_suite.py --report-md manuscript_package_validation_report.md` before relying on the saved snapshot.")
    else:
        lines.append("- Action: the saved validation snapshot is currently trustworthy for package handoff and quick orientation.")
        if head_drift:
            lines.append("- Note: repository HEAD changed after the snapshot was written, but the tracked fingerprints still match.")
            lines.append("- Interpretation: the head shown above records the repo state when this freshness check ran; if this file is later committed, that commit alone does not require another refresh unless tracked package inputs changed again.")
    return "\n".join(lines).rstrip() + "\n"


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
    parser.add_argument(
        "--freshness-report-md",
        help="Optional path to write a markdown freshness report.",
    )
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    report_path = Path(args.report_md).resolve()
    freshness_report_path = Path(args.freshness_report_md).resolve() if args.freshness_report_md else None
    saved_head, fingerprints = parse_report(report_path)
    current_head = git_head(repo_root)

    stale = False
    head_drift = False
    comparisons: list[tuple[str, str, str, str | None]] = []
    print(f"Report: {report_path}")
    if saved_head:
        print(f"Saved HEAD: {saved_head}")
    if current_head:
        print(f"Current HEAD: {current_head}")
        if saved_head and saved_head != current_head:
            print("- Repository HEAD differs from the saved snapshot.")
            head_drift = True

    print("\nTracked fingerprint comparison:")
    for rel_path, saved_hash in fingerprints:
        abs_path = (repo_root / rel_path).resolve()
        if not abs_path.exists():
            print(f"- {rel_path}: MISSING (saved sha256 {saved_hash})")
            stale = True
            comparisons.append((rel_path, "MISSING", saved_hash, None))
            continue
        current_hash = sha256_prefix(abs_path)
        status = "MATCH" if current_hash == saved_hash else "CHANGED"
        print(f"- {rel_path}: {status} (saved {saved_hash}, current {current_hash})")
        if current_hash != saved_hash:
            stale = True
        comparisons.append((rel_path, status, saved_hash, current_hash))

    if freshness_report_path:
        freshness_report_path.write_text(
            markdown_report(report_path, repo_root, saved_head, current_head, comparisons, stale, head_drift)
        )

    if stale:
        print("\nSnapshot freshness: STALE")
        return 1

    if head_drift:
        print("\nSnapshot freshness: CURRENT (tracked inputs match; HEAD drift noted)")
        return 0

    print("\nSnapshot freshness: CURRENT")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # pragma: no cover - diagnostic path
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(2)
