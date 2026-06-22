# Manuscript Reference Cleanup Notes

## Purpose
This file captures the most likely reference-style cleanup tasks remaining in the current manuscript draft. The goal is to make the eventual bibliography-normalization pass fast and disciplined rather than ad hoc.

## Current source
- Draft:
  - `manuscript_llm_ai_nudges_draft.md`
- Related bibliography assets:
  - `manuscript_citation_crosswalk.md`
  - `manuscript_reference_audit.md`

## Current reference count
- The draft currently contains 12 references.
- The current references section matches the in-text citation set exactly.

## Cleanup principle
- Do not change the substantive citation set during a style-only pass unless the main text changes.
- Treat this file as a normalization checklist, not as a prompt to reopen theory scope.
- Keep bibliography cleanup separate from local-PDF retrieval status.

## Likely style-normalization items

### 1. Title capitalization should be normalized consistently
The current list mixes sentence-style capitalization with title fragments that may need a journal-specific treatment later.

Examples to recheck in one pass:
- `Frontiers: Machines vs. humans: The impact of artificial intelligence chatbot disclosure on customer purchases.`
- `E-commerce product recommendation agents: Use, characteristics, and impact.`
- `The impact of trust and recommendation quality on adopting interactive and non-interactive recommendation agents: A meta-analysis.`

Practical note:
- If the target outlet wants sentence case, keep the current lowercase style but make sure subtitles and proper nouns are handled consistently.
- If the target outlet wants title case, convert all titles in one pass rather than piecemeal.

### 2. Journal-style conventions should be applied uniformly once the target outlet is fixed
The current entries are serviceable working references, but a final pass should apply one journal style to:
- article title capitalization
- treatment of subtitles after colons
- use of `vs.` versus spelled-out forms if the outlet has a house style
- punctuation around DOI placement

### 3. Author-name formatting should be checked for consistency, not rewritten prematurely
The current list already uses a consistent initials-based pattern, but a final style pass should verify:
- spacing between initials
- treatment of multi-initial authors such as `J. V.` and `S. T. T.`
- alphabetization behavior for `de Cicco`

### 4. Alphabetical ordering should be rechecked after any future bibliography edits
The current order is broadly alphabetical, but a final pass should verify the exact placement logic for:
- `de Cicco`
- repeated first authors such as `Wang`

### 5. DOI presentation should remain uniform
The current working format is clean and consistent:
- all entries use full `https://doi.org/` links

Final pass reminder:
- preserve one DOI format across all entries
- avoid mixing naked DOIs, `doi:` prefixes, and full URLs

## Entry-specific notes

### Luo et al. (2019)
- Current working title includes `Frontiers:` as part of the article title.
- Final style pass should confirm whether the target outlet style keeps that prefix exactly as written in the reference list.

### Xiao and Benbasat (2007)
- Bibliographic entry is already present and aligned with the main text.
- Remaining issue is not reference-list alignment but lack of an authoritative local PDF archive.

### Ebrahimi et al. (2022)
- Bibliographic entry is already present and aligned with the main text.
- Remaining issue is not reference-list alignment but lack of an authoritative local PDF archive.

## Suggested final-pass sequence
1. Freeze the manuscript's in-text citation set.
2. Use `manuscript_reference_audit.md` to confirm the references list still matches the text.
3. Apply one journal-specific bibliography style to all 12 entries in one pass.
4. Recheck alphabetical order after any edits.
5. Keep local-PDF retrieval as a separate task, using `manuscript_citation_crosswalk.md` and `literature/download_log.md`.

## Why this file exists
- The bibliography is now stable enough that the remaining work is mostly normalization, not discovery.
- Capturing that explicitly reduces the risk of future low-yield editing or repeated manual inspection of the same 12 entries.
