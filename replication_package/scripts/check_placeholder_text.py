#!/usr/bin/env python3
"""Audit placeholder text in core package docs versus intentional templates."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


PLACEHOLDER_PATTERN = re.compile(r"\bTBD\b")
IGNORE_LINE_PATTERNS = [
    re.compile(r"placeholder `TBD` text"),
    re.compile(r"check_placeholder_text\.py"),
    re.compile(r"unexpected `TBD` placeholders in core package docs"),
]


@dataclass
class FileResult:
    rel_path: str
    count: int
    lines: list[str]


DEFAULT_CORE_DOCS = [
    "README.md",
    "manuscript_package_index.md",
    "manuscript_package_open_items.md",
    "manuscript_llm_ai_nudges_draft.md",
    "submission_readiness_checklist.md",
    "manuscript_asset_plan.md",
    "manuscript_reference_audit.md",
    "manuscript_reference_format_audit.md",
    "manuscript_reference_cleanup_notes.md",
    "manuscript_citation_crosswalk.md",
    "manuscript_source_archive_audit.md",
    "replication_package/README.md",
    "replication_package/scripts/README.md",
]

DEFAULT_TEMPLATE_DOCS = [
    "appendix_c_screening_and_sample_flow.md",
    "appendix_d_supplemental_robustness.md",
    "results_table_shells.md",
    "replication_package/codebook_shell.md",
]


def scan_file(path: Path, repo_root: Path) -> FileResult | None:
    matches: list[str] = []
    for lineno, line in enumerate(path.read_text().splitlines(), start=1):
        if not PLACEHOLDER_PATTERN.search(line):
            continue
        if any(pattern.search(line) for pattern in IGNORE_LINE_PATTERNS):
            continue
        matches.append(f"{lineno}: {line.strip()}")
    if not matches:
        return None
    return FileResult(rel_path=path.relative_to(repo_root).as_posix(), count=len(matches), lines=matches)


def scan_paths(paths: list[str], repo_root: Path) -> list[FileResult]:
    results: list[FileResult] = []
    for rel in paths:
        path = (repo_root / rel).resolve()
        if not path.exists():
            continue
        result = scan_file(path, repo_root)
        if result:
            results.append(result)
    return results


def print_section(title: str, results: list[FileResult]) -> None:
    print(title)
    print(f"Files with placeholders: {len(results)}")
    total = sum(result.count for result in results)
    print(f"Total placeholder hits: {total}")
    if results:
        print()
        for result in results:
            print(f"- {result.rel_path}: {result.count}")
            for line in result.lines:
                print(f"  - {line}")
    print()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=".", help="Repository root.")
    parser.add_argument(
        "--core-doc",
        action="append",
        dest="core_docs",
        help="Core package doc where placeholders should generally not remain. May be repeated.",
    )
    parser.add_argument(
        "--template-doc",
        action="append",
        dest="template_docs",
        help="Template doc where placeholders are expected before data/results exist. May be repeated.",
    )
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    core_docs = args.core_docs or DEFAULT_CORE_DOCS
    template_docs = args.template_docs or DEFAULT_TEMPLATE_DOCS

    unexpected = scan_paths(core_docs, repo_root)
    expected = scan_paths(template_docs, repo_root)

    print_section("Unexpected placeholders in core package docs", unexpected)
    print_section("Expected placeholders in template/result-shell docs", expected)

    return 1 if unexpected else 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # pragma: no cover - diagnostic path
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(2)
