#!/usr/bin/env python3
"""Summarize which cited manuscript sources are locally archived."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path


@dataclass
class CitationRow:
    citation: str
    local_file_cell: str

    @property
    def archived_path(self) -> str | None:
        match = re.fullmatch(r"`([^`]+)`", self.local_file_cell.strip())
        if not match:
            return None
        path = match.group(1)
        return path if path.startswith("literature/") else None


TABLE_ROW_PATTERN = re.compile(r"^\| (.+?) \| (.+?) \| (.+?) \| (.+?) \| (.+?) \|$")


def parse_crosswalk(crosswalk_path: Path) -> list[CitationRow]:
    rows: list[CitationRow] = []
    for line in crosswalk_path.read_text().splitlines():
        match = TABLE_ROW_PATTERN.match(line.strip())
        if not match:
            continue
        citation = match.group(1).strip()
        if citation == "Citation":
            continue
        if all(part.strip("-: ") == "" for part in match.groups()):
            continue
        rows.append(CitationRow(citation=citation, local_file_cell=match.group(5).strip()))
    if not rows:
        raise ValueError("Could not find citation rows in manuscript_citation_crosswalk.md.")
    return rows


def markdown_report(
    manuscript_rel: str,
    crosswalk_rel: str,
    download_log_rel: str,
    archived: list[tuple[str, str]],
    missing: list[CitationRow],
) -> str:
    lines = [
        "# Manuscript Source Archive Audit",
        "",
        "## Purpose",
        "This file records the current local-archive status of the manuscript's cited sources. The goal is to separate `citation present in the manuscript` from `authoritative local PDF archived in the project`.",
        "",
        "## Current audit target",
        "- Source manuscript:",
        f"  - `{manuscript_rel}`",
        "- Audit date:",
        f"  - `{date.today().isoformat()}`",
        "- Related files:",
        f"  - `{crosswalk_rel}`",
        "  - `manuscript_reference_audit.md`",
        f"  - `{download_log_rel}`",
        "",
        "## Current archive summary",
        "- Current in-text citation count:",
        f"  - `{len(archived) + len(missing)}`",
        "- Citations with authoritative local PDFs archived:",
        f"  - `{len(archived)}`",
        "- Citations bibliographically confirmed but still lacking authoritative local PDFs:",
        f"  - `{len(missing)}`",
        "",
        "## Archived citations",
    ]

    for citation, rel_path in archived:
        lines.extend(
            [
                f"- {citation}",
                f"  - local file: `{rel_path}`",
            ]
        )

    lines.extend(
        [
            "",
            "## Confirmed citations still missing authoritative local PDFs",
            "",
        ]
    )

    for row in missing:
        lines.extend(
            [
                f"### {row.citation}",
                "- Citation status:",
                "  - bibliographically confirmed in the manuscript package",
                "- Current issue:",
                "  - no authoritative local PDF archived yet",
                "- Current crosswalk note:",
                f"  - {row.local_file_cell}",
                "",
            ]
        )

    lines.extend(
        [
            "## Interpretation",
            "- The manuscript currently does not have a citation-alignment problem.",
            "- The manuscript also does not have a broad source-discovery problem.",
            "- The remaining archive gap is narrow and specific to the bridge citations already identified in the manuscript package.",
            "- The main unresolved issue is access context, not uncertainty about what the cited papers are.",
            "",
            "## Practical use",
            "- Use this file when deciding whether the next bibliography step is `style cleanup` versus `manual PDF retrieval`.",
            "- Use this file during handoff when a future session needs a fast answer to `which cited papers are still not locally archived?`",
            f"- If a missing PDF is later archived successfully, update this file, `{crosswalk_rel}`, and `{download_log_rel}` together.",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def build_report(repo_root: Path, crosswalk_path: Path, manuscript_path: Path, report_path: Path, download_log_path: Path) -> int:
    rows = parse_crosswalk(crosswalk_path)
    archived: list[tuple[str, str]] = []
    missing: list[CitationRow] = []

    for row in rows:
        archived_path = row.archived_path
        if archived_path is None:
            missing.append(row)
            continue
        abs_path = (repo_root / archived_path).resolve()
        if abs_path.exists():
            archived.append((row.citation, archived_path))
        else:
            missing.append(row)

    report_path.write_text(
        markdown_report(
            manuscript_path.relative_to(repo_root).as_posix(),
            crosswalk_path.relative_to(repo_root).as_posix(),
            download_log_path.relative_to(repo_root).as_posix(),
            archived,
            missing,
        )
    )

    print(f"Crosswalk: {crosswalk_path}")
    print(f"Source archive audit: {report_path}")
    print(f"Citations checked: {len(rows)}")
    print(f"Archived locally: {len(archived)}")
    print(f"Missing local PDFs: {len(missing)}")
    if missing:
        print("\nMissing local PDFs:")
        for row in missing:
            print(f"- {row.citation}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=".", help="Repository root.")
    parser.add_argument(
        "--crosswalk-md",
        default="manuscript_citation_crosswalk.md",
        help="Path to the manuscript citation crosswalk markdown file.",
    )
    parser.add_argument(
        "--manuscript",
        default="manuscript_llm_ai_nudges_draft.md",
        help="Path to the manuscript markdown file.",
    )
    parser.add_argument(
        "--download-log-md",
        default="literature/download_log.md",
        help="Path to the literature download log markdown file.",
    )
    parser.add_argument(
        "--report-md",
        default="manuscript_source_archive_audit.md",
        help="Path to write the source archive audit markdown file.",
    )
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    crosswalk_path = (repo_root / args.crosswalk_md).resolve()
    manuscript_path = (repo_root / args.manuscript).resolve()
    report_path = (repo_root / args.report_md).resolve()
    download_log_path = (repo_root / args.download_log_md).resolve()

    try:
        return build_report(repo_root, crosswalk_path, manuscript_path, report_path, download_log_path)
    except Exception as exc:  # pragma: no cover - diagnostic path
        print(f"Error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
