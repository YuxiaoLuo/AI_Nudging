#!/usr/bin/env python3
"""Run the current lightweight manuscript/package validation checks in one command."""

from __future__ import annotations

import argparse
import subprocess
import sys
from dataclasses import dataclass
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
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    repo_root = Path(args.repo_root).resolve()
    manuscript = Path(args.manuscript).resolve()
    package_docs = args.package_docs or [
        "README.md",
        "manuscript_package_index.md",
        "submission_readiness_checklist.md",
    ]

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
                str(manuscript),
            ],
        ),
        (
            "reference_formatting",
            [
                sys.executable,
                str(script_dir / "check_reference_formatting.py"),
                str(manuscript),
            ],
        ),
    ]

    results = [run_check(name, command) for name, command in checks]

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
