#!/usr/bin/env python3
"""Check basic alignment between manuscript citations and the references list."""

from __future__ import annotations

import argparse
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


def build_report(manuscript_path: Path) -> int:
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

    return 1 if uncited_reference_blocks or unmatched_citation_tokens else 0


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
