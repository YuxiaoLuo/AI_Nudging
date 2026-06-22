#!/usr/bin/env python3
"""Audit lightweight reference-format consistency in the manuscript bibliography."""

from __future__ import annotations

import argparse
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


def build_report(manuscript_path: Path) -> int:
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
    if colon_upper and colon_lower:
        warnings.append(
            "Mixed subtitle capitalization detected after colons; choose one journal-specific rule in the final style pass."
        )

    vs_entries = [entry for entry in entries if "vs." in entry.title.lower()]
    if vs_entries:
        warnings.append(
            "At least one title uses 'vs.'; confirm whether the target outlet keeps abbreviations or spells them out."
        )

    frontiers_entries = [entry for entry in entries if entry.title.startswith("Frontiers:")]
    if frontiers_entries:
        warnings.append(
            "At least one title starts with 'Frontiers:'; confirm whether that prefix is kept exactly in the target style."
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

    return 1 if issues else 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "manuscript",
        nargs="?",
        default="manuscript_llm_ai_nudges_draft.md",
        help="Path to the manuscript markdown file.",
    )
    args = parser.parse_args()
    try:
        return build_report(Path(args.manuscript))
    except Exception as exc:  # pragma: no cover - diagnostic path
        print(f"Error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
