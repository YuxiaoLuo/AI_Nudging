#!/usr/bin/env python3
"""Audit lightweight reference-format consistency in the manuscript bibliography."""

from __future__ import annotations

import argparse
from datetime import date
import re
import sys
from dataclasses import dataclass
from pathlib import Path


REFERENCES_SPLIT = "\n## References\n"
DOI_PREFIX = "https://doi.org/"


@dataclass
class ReferenceEntry:
    raw: str
    authors: str
    year: int | None
    title: str
    journal: str
    doi: str | None
    first_author_key: str


def split_manuscript(text: str) -> tuple[str, str]:
    if REFERENCES_SPLIT not in text:
        raise ValueError("Could not find '## References' section in manuscript.")
    body, references = text.split(REFERENCES_SPLIT, 1)
    return body, references.strip()


def extract_reference_blocks(references: str) -> list[str]:
    return [block.strip() for block in references.split("\n\n") if block.strip()]


def normalize_author_key(text: str) -> str:
    text = text.lower().strip()
    text = text.replace("ä", "a")
    text = text.replace("ö", "o")
    text = text.replace("ü", "u")
    text = text.replace("ß", "ss")
    text = re.sub(r"[^a-zà-ÿ0-9 ]+", "", text)
    text = re.sub(r"\s+", " ", text)
    return text


def parse_entry(block: str) -> ReferenceEntry:
    doi_match = re.search(r"(https://doi\.org/\S+)\s*$", block)
    doi = doi_match.group(1) if doi_match else None
    body = block[: doi_match.start()].strip() if doi_match else block.strip()

    year_match = re.search(r"\((\d{4})\)", body)
    year = int(year_match.group(1)) if year_match else None
    if year_match is None:
        raise ValueError(f"Could not parse year from reference entry: {block}")

    authors = body[: year_match.start()].strip().rstrip(".")
    tail = body[year_match.end() :].strip()
    if tail.startswith("."):
        tail = tail[1:].strip()

    title_match = re.match(r"(.+?[.?!])\s+\*([^*]+)\*\.*\s*$", tail)
    if title_match is None:
        raise ValueError(f"Could not parse title/journal from reference entry: {block}")

    title = title_match.group(1).strip()
    journal = title_match.group(2).strip()
    first_author = authors.split("&", 1)[0].split(",", 1)[0].strip()

    return ReferenceEntry(
        raw=block,
        authors=authors,
        year=year,
        title=title,
        journal=journal,
        doi=doi,
        first_author_key=normalize_author_key(first_author),
    )


def subtitle_case_flag(title: str) -> bool:
    parts = title.split(": ", 1)
    if len(parts) != 2:
        return False
    follow = parts[1]
    first_alpha = next((char for char in follow if char.isalpha()), "")
    return bool(first_alpha and first_alpha.islower())


def markdown_report(
    manuscript_rel: str,
    entries: list[ReferenceEntry],
    warnings: list[str],
    issues: list[str],
    observed_order_matches: bool,
    colon_mixed: bool,
    has_vs_entries: bool,
    has_frontiers_entries: bool,
    colon_case_examples: list[str],
    vs_examples: list[str],
    frontiers_examples: list[str],
) -> str:
    lines = [
        "# Manuscript Reference Format Audit",
        "",
        "## Purpose",
        "This file records the current lightweight formatting state of the manuscript references section. The goal is to separate `structural bibliography consistency` from the narrower set of `target-journal style choices` that still remain.",
        "",
        "## Current audit target",
        "- Source file:",
        f"  - `{manuscript_rel}`",
        "- Audit date:",
        f"  - `{date.today().isoformat()}`",
        "- Audit helper:",
        "  - `replication_package/scripts/check_reference_formatting.py`",
        "",
        "## Current structural status",
        f"- The draft currently contains {len(entries)} reference entries.",
        f"- All {sum(1 for entry in entries if entry.doi)} entries currently use full `https://doi.org/` URLs." if all(entry.doi for entry in entries) else f"- Entries currently using full `https://doi.org/` URLs: {sum(1 for entry in entries if entry.doi)} of {len(entries)}.",
        f"- {'No duplicate DOI URLs are currently flagged.' if not any('Duplicate DOI URL' in issue for issue in issues) else 'At least one duplicate DOI URL is currently flagged.'}",
        f"- {'The first-pass alphabetical ordering issue in the references is not currently flagged.' if observed_order_matches else 'A first-pass alphabetical ordering warning is currently flagged.'}",
    ]

    if issues:
        lines.append("- The current bibliography does not yet pass the lightweight structural-format audit.")
    else:
        lines.append("- The current bibliography therefore passes the lightweight structural-format audit.")

    lines.extend(
        [
            "",
            "## Current warning flags",
            f"- Alphabetical-order warning: `{'yes' if not observed_order_matches else 'no'}`",
            f"- Mixed subtitle capitalization warning: `{'yes' if colon_mixed else 'no'}`",
            f"- `vs.` warning: `{'yes' if has_vs_entries else 'no'}`",
            f"- `Frontiers:` warning: `{'yes' if has_frontiers_entries else 'no'}`",
            "",
            "## Current remaining warnings",
        ]
    )

    if warnings:
        for idx, warning in enumerate(warnings, start=1):
            lines.append(f"{idx}. {warning}")
    else:
        lines.append("- No outlet-specific style warnings are currently flagged.")

    if colon_case_examples or vs_examples or frontiers_examples:
        lines.extend(
            [
                "",
                "## Flagged entries",
            ]
        )
        if colon_case_examples:
            lines.append("- Mixed subtitle-capitalization examples:")
            for title in colon_case_examples:
                lines.append(f"  - `{title}`")
        if vs_examples:
            lines.append("- `vs.` examples:")
            for title in vs_examples:
                lines.append(f"  - `{title}`")
        if frontiers_examples:
            lines.append("- `Frontiers:` examples:")
            for title in frontiers_examples:
                lines.append(f"  - `{title}`")

    if issues:
        lines.extend(
            [
                "",
                "## Current structural issues",
            ]
        )
        for idx, issue in enumerate(issues, start=1):
            lines.append(f"{idx}. {issue}")

    lines.extend(
        [
            "",
            "## Interpretation",
            "- These warnings do **not** indicate citation-list misalignment.",
            "- These warnings do **not** require reopening the manuscript's theory or citation set.",
        ]
    )
    if issues:
        lines.append("- The current issues do indicate that the bibliography still needs a bounded structural cleanup pass before it can be treated as format-clean.")
    else:
        if has_vs_entries or has_frontiers_entries:
            lines.append("- They also do **not** imply uncertainty about the underlying published article titles; in the current manuscript state, the remaining `vs.` and `Frontiers:` flags are source-confirmed title features.")
        lines.append("- They indicate only that the final bibliography pass still needs one explicit target-journal style decision.")

    lines.extend(
        [
            "",
            "## What to do next",
            "- If the target outlet prefers sentence case:",
            "  - normalize all titles and subtitles in one bounded pass while preserving proper nouns and any required article prefixes.",
            "- If the target outlet prefers title case:",
            "  - convert all titles and subtitles in one pass rather than editing only the flagged entries.",
            "- Before making that pass:",
            "  - keep the citation set frozen",
            "  - confirm citation/reference alignment with `manuscript_reference_audit.md`",
            "  - use `manuscript_reference_cleanup_notes.md` to keep the normalization pass bounded",
            "",
            "## Related files",
            "- `manuscript_reference_audit.md`",
            "- `manuscript_reference_cleanup_notes.md`",
            "- `manuscript_citation_crosswalk.md`",
            "- `submission_readiness_checklist.md`",
            "",
            "## Practical use",
            "- Use this file when deciding whether the next bibliography task is `style normalization` versus `PDF retrieval`.",
            "- Refresh this audit after any future reference-list edits that change title wording, ordering, DOI presentation, or validation logic.",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def build_report(manuscript_path: Path, report_path: Path | None = None, repo_root: Path | None = None) -> int:
    text = manuscript_path.read_text()
    _, references = split_manuscript(text)
    blocks = extract_reference_blocks(references)
    entries = [parse_entry(block) for block in blocks]

    issues: list[str] = []
    warnings: list[str] = []

    for entry in entries:
        if entry.doi is None:
            issues.append(f"Missing DOI URL: {entry.authors} ({entry.year}).")
        elif not entry.doi.startswith(DOI_PREFIX):
            issues.append(f"Nonstandard DOI format: {entry.authors} ({entry.year}) -> {entry.doi}")

    seen_dois: dict[str, str] = {}
    for entry in entries:
        if entry.doi is None:
            continue
        if entry.doi in seen_dois:
            issues.append(
                f"Duplicate DOI URL: {entry.doi} appears in both '{seen_dois[entry.doi]}' "
                f"and '{entry.authors} ({entry.year})'."
            )
        else:
            seen_dois[entry.doi] = f"{entry.authors} ({entry.year})"

    observed_order = [(entry.first_author_key, entry.year or 0) for entry in entries]
    expected_order = sorted(observed_order)
    if observed_order != expected_order:
        warnings.append("Reference entries are not in simple first-author alphabetical order.")

    colon_upper = sum(": " in entry.title and not subtitle_case_flag(entry.title) for entry in entries)
    colon_lower = sum(subtitle_case_flag(entry.title) for entry in entries)
    colon_case_examples = [entry.title for entry in entries if ": " in entry.title]
    if colon_upper and colon_lower:
        warnings.append(
            "Mixed subtitle capitalization detected after colons; choose one journal-specific rule in the final style pass."
        )

    vs_entries = [entry for entry in entries if "vs." in entry.title.lower()]
    if vs_entries:
        warnings.append(
            "At least one title uses 'vs.'; in the current manuscript state this abbreviation is treated as source-confirmed, so the remaining question is whether the target outlet keeps it or normalizes it."
        )

    frontiers_entries = [entry for entry in entries if entry.title.startswith("Frontiers:")]
    if frontiers_entries:
        warnings.append(
            "At least one title starts with 'Frontiers:'; in the current manuscript state this prefix is treated as source-confirmed, so the remaining question is whether the target outlet keeps it exactly or normalizes it."
        )

    if report_path is not None:
        if repo_root is None:
            repo_root = manuscript_path.parent
        manuscript_rel = manuscript_path.relative_to(repo_root).as_posix() if manuscript_path.is_relative_to(repo_root) else manuscript_path.as_posix()
        report_path.write_text(
            markdown_report(
                manuscript_rel=manuscript_rel,
                entries=entries,
                warnings=warnings,
                issues=issues,
                observed_order_matches=observed_order == expected_order,
                colon_mixed=bool(colon_upper and colon_lower),
                has_vs_entries=bool(vs_entries),
                has_frontiers_entries=bool(frontiers_entries),
                colon_case_examples=colon_case_examples if colon_upper and colon_lower else [],
                vs_examples=[entry.title for entry in vs_entries],
                frontiers_examples=[entry.title for entry in frontiers_entries],
            )
        )

    print(f"Manuscript: {manuscript_path}")
    print(f"Reference entries: {len(entries)}")
    print(f"Entries with DOI URLs: {sum(1 for entry in entries if entry.doi)}")
    print(f"Alphabetical-order warning: {'yes' if observed_order != expected_order else 'no'}")
    print(f"Mixed subtitle capitalization warning: {'yes' if colon_upper and colon_lower else 'no'}")
    print(f"'vs.' warning: {'yes' if vs_entries else 'no'}")
    print(f"'Frontiers:' warning: {'yes' if frontiers_entries else 'no'}")

    if warnings:
        print("\nWarnings:")
        for warning in warnings:
            print(f"- {warning}")

    if issues:
        print("\nIssues:")
        for issue in issues:
            print(f"- {issue}")

    if colon_upper and colon_lower:
        print("\nMixed subtitle-capitalization examples:")
        for title in colon_case_examples:
            print(f"- {title}")

    if vs_entries:
        print("\n'vs.' examples:")
        for entry in vs_entries:
            print(f"- {entry.title}")

    if frontiers_entries:
        print("\n'Frontiers:' examples:")
        for entry in frontiers_entries:
            print(f"- {entry.title}")

    return 1 if issues else 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "manuscript",
        nargs="?",
        default="manuscript_llm_ai_nudges_draft.md",
        help="Path to the manuscript markdown file.",
    )
    parser.add_argument(
        "--repo-root",
        default=".",
        help="Repository root used when writing a markdown audit report.",
    )
    parser.add_argument(
        "--report-md",
        help="Optional path to write a markdown audit report.",
    )
    args = parser.parse_args()
    try:
        repo_root = Path(args.repo_root).resolve()
        manuscript_path = Path(args.manuscript).resolve()
        report_path = (repo_root / args.report_md).resolve() if args.report_md else None
        return build_report(manuscript_path, report_path=report_path, repo_root=repo_root)
    except Exception as exc:  # pragma: no cover - diagnostic path
        print(f"Error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
