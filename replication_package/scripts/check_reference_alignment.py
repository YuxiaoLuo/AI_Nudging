#!/usr/bin/env python3
"""Check basic alignment between manuscript citations and the references list."""

from __future__ import annotations

import argparse
from datetime import date
import re
import sys
from pathlib import Path


REFERENCES_SPLIT = "\n## References\n"


def normalize_token(text: str) -> str:
    text = text.lower()
    text = text.replace("&", " and ")
    text = text.replace("’", "'")
    text = text.replace("et al.", "et al")
    text = re.sub(r"\((\d{4})\)", r" \1", text)
    text = re.sub(r"[^a-z0-9à-ÿ ]+", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def split_manuscript(text: str) -> tuple[str, str]:
    if REFERENCES_SPLIT not in text:
        raise ValueError("Could not find '## References' section in manuscript.")
    body, references = text.split(REFERENCES_SPLIT, 1)
    return body, references.strip()


def extract_reference_blocks(references: str) -> list[str]:
    return [block.strip() for block in references.split("\n\n") if block.strip()]


def extract_reference_metadata(block: str) -> tuple[str, int | None, list[str]]:
    year_match = re.search(r"\((\d{4})\)", block)
    year = int(year_match.group(1)) if year_match else None
    author_segment = block.split("(", 1)[0].strip()
    surnames = [
        match.group(1).strip()
        for match in re.finditer(r"([A-Za-zÀ-ÿ' -]+?),\s+[A-Z]", author_segment)
    ]
    return author_segment, year, surnames


def citation_label_from_block(block: str) -> str:
    _, year, surnames = extract_reference_metadata(block)
    if year is None or not surnames:
        return block.split(".", 1)[0].strip()
    if len(surnames) == 1:
        return f"{surnames[0]} ({year})"
    if len(surnames) == 2:
        return f"{surnames[0]} and {surnames[1]} ({year})"
    return f"{surnames[0]} et al. ({year})"


def reference_keys(block: str) -> set[str]:
    _, year, surnames = extract_reference_metadata(block)
    if year is None or not surnames:
        return set()
    year_text = str(year)
    if len(surnames) == 1:
        return {normalize_token(f"{surnames[0]} {year_text}")}
    if len(surnames) == 2:
        left, right = surnames[0], surnames[1]
        return {
            normalize_token(f"{left} and {right} {year_text}"),
            normalize_token(f"{left} & {right} {year_text}"),
        }
    return {normalize_token(f"{surnames[0]} et al. {year_text}")}


def extract_parenthetical_tokens(body: str) -> set[str]:
    tokens: set[str] = set()
    for match in re.finditer(r"\(([^()]*\d{4}[^()]*)\)", body):
        content = match.group(1)
        for part in content.split(";"):
            if not re.search(r"\d{4}", part):
                continue
            if not re.search(r"[A-Za-zÀ-ÿ]", part):
                continue
            cleaned = normalize_token(part)
            if re.search(r"\b\d{4}\b", cleaned) and re.search(r"[a-zà-ÿ]", cleaned):
                tokens.add(cleaned)
    return tokens


def extract_narrative_tokens(body: str) -> set[str]:
    tokens: set[str] = set()
    pattern = re.compile(
        r"\b((?:[A-Z][A-Za-zÀ-ÿ'’-]+|de [A-Z][A-Za-zÀ-ÿ'’-]+)"
        r"(?: and (?:[A-Z][A-Za-zÀ-ÿ'’-]+|de [A-Z][A-Za-zÀ-ÿ'’-]+)| et al\.)?)\s*\((\d{4})\)"
    )
    for match in pattern.finditer(body):
        tokens.add(normalize_token(f"{match.group(1)} {match.group(2)}"))
    return tokens


def markdown_report(
    manuscript_rel: str,
    matched_reference_blocks: list[str],
    uncited_reference_blocks: list[str],
    unmatched_citation_tokens: list[str],
) -> str:
    citation_labels = [citation_label_from_block(block) for block in matched_reference_blocks]
    lines = [
        "# Manuscript Reference Audit",
        "",
        "## Purpose",
        "This file records the current relationship between the manuscript's in-text citations and the draft references section. The goal is to make later reference cleanup faster and to separate `reference-list alignment` from the narrower question of whether every cited paper already has an authoritative local PDF archived.",
        "",
        "## Current audit target",
        "- Source file:",
        f"  - `{manuscript_rel}`",
        "- Audit date:",
        f"  - `{date.today().isoformat()}`",
        "- Audit helper:",
        "  - `replication_package/scripts/check_reference_alignment.py`",
        "",
        "## In-text citation set currently used in the draft",
    ]

    if citation_labels:
        lines.append("The current main-text citation set is:")
        lines.append("")
        for idx, label in enumerate(citation_labels, start=1):
            lines.append(f"{idx}. {label}")
    else:
        lines.append("- No current in-text citations were detected.")

    lines.extend(
        [
            "",
            "## References-section alignment",
            f"- The current references section in `{manuscript_rel}` contains entries for all {len(matched_reference_blocks)} citations currently used in the main text." if not unmatched_citation_tokens else f"- The current references section in `{manuscript_rel}` does not yet cover all citations currently used in the main text.",
            f"- {'No extra references were found in the draft references section beyond the current in-text citation set.' if not uncited_reference_blocks else f'{len(uncited_reference_blocks)} reference entries are currently not matched to any in-text citation token.'}",
            f"- {'No currently used in-text citations were found to be missing from the references section.' if not unmatched_citation_tokens else f'{len(unmatched_citation_tokens)} currently used in-text citation tokens do not yet match any reference entry.'}",
        ]
    )

    if uncited_reference_blocks:
        lines.extend(
            [
                "",
                "## Uncited reference entries",
            ]
        )
        for block in uncited_reference_blocks:
            lines.append(f"- {block}")

    if unmatched_citation_tokens:
        lines.extend(
            [
                "",
                "## In-text citation tokens without matching reference entries",
            ]
        )
        for token in unmatched_citation_tokens:
            lines.append(f"- `{token}`")

    lines.extend(
        [
            "",
            "## What this audit confirms",
            "- The draft is currently aligned at the level of `in-text citation present` versus `reference entry present`." if not uncited_reference_blocks and not unmatched_citation_tokens else "- The audit isolates the current structural citation/reference mismatches that still need repair.",
            "- The manuscript therefore does not currently have a citation-list mismatch problem." if not uncited_reference_blocks and not unmatched_citation_tokens else "- The manuscript should not be treated as citation-list clean until those mismatches are resolved.",
            "",
            "## What this audit does not confirm",
            "- This file does not certify that every reference is already in final journal style.",
            "- This file does not certify that every cited work has an authoritative local PDF archived.",
            "- For source-role mapping and local-file status, use:",
            "  - `manuscript_citation_crosswalk.md`",
            "  - `manuscript_source_archive_audit.md`",
            "",
            "## Practical use",
            "- Use this file before submission-oriented formatting passes on the references section.",
            "- Use this file together with `manuscript_citation_crosswalk.md` when deciding whether the next step is `style cleanup`, `source verification`, or `local-PDF archiving`.",
            "- Refresh this audit after any future manuscript citation changes or reference-list edits, ideally by rerunning `replication_package/scripts/check_reference_alignment.py` with `--report-md manuscript_reference_audit.md`.",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def build_report(manuscript_path: Path, report_path: Path | None = None, repo_root: Path | None = None) -> int:
    text = manuscript_path.read_text()
    body, references = split_manuscript(text)
    reference_blocks = extract_reference_blocks(references)

    ref_to_keys = {block: reference_keys(block) for block in reference_blocks}
    all_reference_keys = set().union(*ref_to_keys.values()) if ref_to_keys else set()

    cited_tokens = extract_parenthetical_tokens(body) | extract_narrative_tokens(body)

    matched_reference_blocks = []
    uncited_reference_blocks = []
    for block, keys in ref_to_keys.items():
        if keys & cited_tokens:
            matched_reference_blocks.append(block)
        else:
            uncited_reference_blocks.append(block)

    unmatched_citation_tokens = sorted(token for token in cited_tokens if token not in all_reference_keys)

    print(f"Manuscript: {manuscript_path}")
    print(f"Reference entries: {len(reference_blocks)}")
    print(f"Distinct citation tokens found: {len(cited_tokens)}")
    print(f"Cited reference entries: {len(matched_reference_blocks)}")
    print(f"Uncited reference entries: {len(uncited_reference_blocks)}")
    print(f"Unmatched citation tokens: {len(unmatched_citation_tokens)}")

    if uncited_reference_blocks:
        print("\nUncited reference entries:")
        for block in uncited_reference_blocks:
            print(f"- {block}")

    if unmatched_citation_tokens:
        print("\nCitation tokens without matching reference keys:")
        for token in unmatched_citation_tokens:
            print(f"- {token}")

    if report_path is not None:
        if repo_root is None:
            repo_root = manuscript_path.parent
        manuscript_rel = manuscript_path.relative_to(repo_root).as_posix() if manuscript_path.is_relative_to(repo_root) else manuscript_path.as_posix()
        report_path.write_text(
            markdown_report(
                manuscript_rel=manuscript_rel,
                matched_reference_blocks=matched_reference_blocks,
                uncited_reference_blocks=uncited_reference_blocks,
                unmatched_citation_tokens=unmatched_citation_tokens,
            )
        )

    return 1 if uncited_reference_blocks or unmatched_citation_tokens else 0


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
