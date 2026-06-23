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
- The current references also have uniform full DOI URLs, and the simple alphabetical-order drift in the `Wang` entries has now been corrected.
- The earlier mixed subtitle-capitalization drift has now been cleaned up in the working draft, so the remaining style questions are narrower than before.

## Cleanup principle
- Do not change the substantive citation set during a style-only pass unless the main text changes.
- Treat this file as a normalization checklist, not as a prompt to reopen theory scope.
- Keep bibliography cleanup separate from local-PDF retrieval status.

## Likely style-normalization items

### 1. Journal-style conventions should be applied uniformly once the target outlet is fixed
The current entries are serviceable working references, but a final pass should apply one journal style to:
- article title capitalization
- use of `vs.` versus spelled-out forms if the outlet has a house style
- punctuation around DOI placement
- any house-style treatment of branded or prefixed article titles such as `Frontiers:`

### 2. Remaining title-level decisions are now narrow and explicit
The current draft already uses a cleaner sentence-case baseline, so the main unresolved title-level issues are now limited to a small bounded set:

- whether `vs.` should remain abbreviated or be spelled out
- whether the article-title prefix `Frontiers:` should remain exactly as written in the final reference list
- whether any target journal prefers a different capitalization rule for that prefixed title

Current examples to confirm in the final pass:
- `Frontiers: machines vs. humans: the impact of artificial intelligence chatbot disclosure on customer purchases.`
- `Effects of recommendation neutrality and sponsorship disclosure on trust vs. distrust in online recommendation agents: moderating role of explanations for organic recommendations.`

### 3. Author-name formatting should be checked for consistency, not rewritten prematurely
The current list already uses a consistent initials-based pattern, but a final style pass should verify:
- spacing between initials
- treatment of multi-initial authors such as `J. V.` and `S. T. T.`
- alphabetization behavior for `de Cicco`

### 4. Alphabetical ordering should be rechecked after any future bibliography edits
The current order is now clean at a first-pass level, but any later bibliography edits should still verify the exact placement logic for:
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
- Final style pass should confirm whether the target outlet style keeps that prefix exactly as written in the reference list, and whether `vs.` remains abbreviated in that title.

### Xiao and Benbasat (2007)
- Bibliographic entry is already present and aligned with the main text.
- Remaining issue is not reference-list alignment but lack of an authoritative local PDF archive.

### Ebrahimi et al. (2022)
- Bibliographic entry is already present and aligned with the main text.
- Remaining issue is not reference-list alignment but lack of an authoritative local PDF archive.

## Suggested final-pass sequence
1. Freeze the manuscript's in-text citation set.
2. Use `manuscript_reference_audit.md` to confirm the references list still matches the text.
3. Resolve the remaining `vs.` and `Frontiers:` title-style choices in one bounded pass once the outlet is fixed.
4. Recheck alphabetical order after any edits.
5. Keep local-PDF retrieval as a separate task, using `manuscript_citation_crosswalk.md` and `literature/download_log.md`.

## Why this file exists
- The bibliography is now stable enough that the remaining work is mostly normalization, not discovery.
- Capturing that explicitly reduces the risk of future low-yield editing or repeated manual inspection of the same 12 entries.
