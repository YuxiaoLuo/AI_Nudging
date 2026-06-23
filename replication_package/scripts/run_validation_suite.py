#!/usr/bin/env python3
"""Run the current lightweight manuscript/package validation checks in one command."""

from __future__ import annotations

import argparse
import hashlib
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path


@dataclass
class CheckResult:
    name: str
    command: list[str]
    returncode: int
    stdout: str
    stderr: str


def run_check(name: str, command: list[str]) -> CheckResult:
    completed = subprocess.run(command, capture_output=True, text=True)
    return CheckResult(
        name=name,
        command=command,
        returncode=completed.returncode,
        stdout=completed.stdout.strip(),
        stderr=completed.stderr.strip(),
    )


def git_head(repo_root: Path) -> str | None:
    completed = subprocess.run(
        ["git", "-C", str(repo_root), "rev-parse", "HEAD"],
        capture_output=True,
        text=True,
    )
    if completed.returncode != 0:
        return None
    return completed.stdout.strip() or None


def sha256_prefix(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()[:12]


def write_freshness_report(
    repo_root: Path,
    report_path: Path,
    freshness_report_path: Path,
) -> subprocess.CompletedProcess[str]:
    script_dir = repo_root / "replication_package" / "scripts"
    return subprocess.run(
        [
            sys.executable,
            str(script_dir / "check_validation_snapshot_freshness.py"),
            "--repo-root",
            str(repo_root),
            "--report-md",
            str(report_path),
            "--freshness-report-md",
            str(freshness_report_path),
        ],
        capture_output=True,
        text=True,
    )


def markdown_report(
    repo_root: Path,
    manuscript: Path,
    package_docs: list[str],
    bibliography_inputs: list[str],
    validator_scripts: list[str],
    results: list[CheckResult],
) -> str:
    generated_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    head = git_head(repo_root)
    tracked_inputs = [
        manuscript,
        *[(repo_root / doc).resolve() for doc in package_docs],
        *[(repo_root / path).resolve() for path in bibliography_inputs],
    ]
    tracked_validators = [(script_dir := repo_root / "replication_package" / "scripts") / script for script in validator_scripts]

    lines = [
        "# Manuscript Package Validation Report",
        "",
        "## Purpose",
        "This file records one lightweight validation-suite snapshot for the current manuscript package.",
        "",
        "## Snapshot metadata",
        f"- Generated at (UTC): `{generated_at}`",
    ]
    if head:
        lines.append(f"- Repository HEAD at generation: `{head}`")
    lines.extend(
        [
            "",
            "## Input fingerprints",
        ]
    )
    for path in tracked_inputs:
        lines.append(f"- `{path.relative_to(repo_root)}`: sha256 `{sha256_prefix(path)}`")
    lines.extend(
        [
            "",
            "## Validator-script fingerprints",
        ]
    )
    for path in tracked_validators:
        lines.append(f"- `{path.relative_to(repo_root)}`: sha256 `{sha256_prefix(path)}`")
    lines.extend(
            [
                "",
                "## Current validation target",
                f"- Repository root: `{repo_root}`",
                f"- Manuscript: `{manuscript}`",
                "- Package-facing docs included in link check:",
            ]
    )
    lines.extend([f"  - `{doc}`" for doc in package_docs])
    lines.extend(
        [
            "- Bibliography-side files tracked for source-archive freshness:",
        ]
    )
    lines.extend([f"  - `{path}`" for path in bibliography_inputs])
    lines.extend(
        [
            "",
            "## Included lightweight checks",
            "- package-link integrity for the main manuscript/package entrypoints",
            "- manuscript citation/reference alignment",
            "- bibliography-format consistency warnings",
            "- source-archive status for cited manuscript references",
            "- placeholder-text carryover in core handoff docs versus explicit templates",
            "- validator-script drift for the saved package-validation snapshot",
            "",
            "## Validation results",
        ]
    )

    for result in results:
        status = "PASS" if result.returncode == 0 else "FAIL"
        lines.extend(
            [
                f"### {result.name}",
                f"- Status: `{status}`",
            ]
        )
        if result.stdout:
            lines.extend(["- Output:", "```text", result.stdout, "```"])
        if result.stderr:
            lines.extend(["- Stderr:", "```text", result.stderr, "```"])
        lines.append("")

    lines.extend(
        [
            "## Interpretation note",
            "- Treat `PASS` here as confirmation that the current lightweight checks did not find structural package or bibliography failures.",
            "- Treat any remaining warnings inside the individual outputs as follow-up guidance, not as automatic blockers, unless they contradict the intended submission state.",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--repo-root",
        default=".",
        help="Repository root for package-doc path checks.",
    )
    parser.add_argument(
        "--manuscript",
        default="manuscript_llm_ai_nudges_draft.md",
        help="Path to the manuscript markdown file.",
    )
    parser.add_argument(
        "--package-doc",
        action="append",
        dest="package_docs",
        help="Package-facing doc to include in the link check. May be repeated.",
    )
    parser.add_argument(
        "--report-md",
        help="Optional path to write a markdown validation report.",
    )
    parser.add_argument(
        "--freshness-report-md",
        help="Optional path to write a markdown freshness report after the validation report is refreshed.",
    )
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    repo_root = Path(args.repo_root).resolve()
    manuscript = Path(args.manuscript).resolve()
    report_path = Path(args.report_md).resolve() if args.report_md else None
    freshness_report_path = Path(args.freshness_report_md).resolve() if args.freshness_report_md else None
    package_docs = args.package_docs or [
        "README.md",
        "manuscript_package_index.md",
        "submission_readiness_checklist.md",
        "replication_package/README.md",
    ]
    bibliography_inputs = [
        "manuscript_reference_audit.md",
        "manuscript_reference_format_audit.md",
        "manuscript_citation_crosswalk.md",
        "literature/download_log.md",
        "manuscript_source_archive_audit.md",
    ]
    validator_scripts = [
        "run_validation_suite.py",
        "check_validation_snapshot_freshness.py",
        "check_package_links.py",
        "check_reference_alignment.py",
        "check_reference_formatting.py",
        "check_source_archive_status.py",
        "check_placeholder_text.py",
    ]

    if report_path and not report_path.exists():
        report_path.write_text(
            "# Manuscript Package Validation Report\n\n"
            "_This placeholder is overwritten automatically by `run_validation_suite.py`._\n"
        )

    checks = [
        (
            "package_links",
            [
                sys.executable,
                str(script_dir / "check_package_links.py"),
                "--repo-root",
                str(repo_root),
                *package_docs,
            ],
        ),
        (
            "reference_alignment",
            [
                sys.executable,
                str(script_dir / "check_reference_alignment.py"),
                "--repo-root",
                str(repo_root),
                str(manuscript),
                "--report-md",
                str(repo_root / "manuscript_reference_audit.md"),
            ],
        ),
        (
            "reference_formatting",
            [
                sys.executable,
                str(script_dir / "check_reference_formatting.py"),
                "--repo-root",
                str(repo_root),
                str(manuscript),
                "--report-md",
                str(repo_root / "manuscript_reference_format_audit.md"),
            ],
        ),
        (
            "source_archive_status",
            [
                sys.executable,
                str(script_dir / "check_source_archive_status.py"),
                "--repo-root",
                str(repo_root),
            ],
        ),
        (
            "placeholder_text",
            [
                sys.executable,
                str(script_dir / "check_placeholder_text.py"),
                "--repo-root",
                str(repo_root),
            ],
        ),
    ]

    results = [run_check(name, command) for name, command in checks]

    if report_path:
        report_path.write_text(
            markdown_report(
                repo_root,
                manuscript,
                package_docs,
                bibliography_inputs,
                validator_scripts,
                results,
            )
        )
        if freshness_report_path:
            freshness_completed = write_freshness_report(repo_root, report_path, freshness_report_path)
            print("Freshness report refresh:")
            if freshness_completed.stdout.strip():
                print(freshness_completed.stdout.strip())
            if freshness_completed.stderr.strip():
                print(freshness_completed.stderr.strip(), file=sys.stderr)
            print()

    overall_failure = False
    print("Validation suite summary:")
    for result in results:
        status = "PASS" if result.returncode == 0 else "FAIL"
        print(f"- {result.name}: {status}")
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(result.stderr, file=sys.stderr)
        print()
        if result.returncode != 0:
            overall_failure = True

    return 1 if overall_failure else 0


if __name__ == "__main__":
    raise SystemExit(main())
