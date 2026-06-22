# Manuscript Reference Audit

## Purpose
This file records the current relationship between the manuscript's in-text citations and the draft references section. The goal is to make later reference cleanup faster and to separate `reference-list alignment` from the narrower question of whether every cited paper already has an authoritative local PDF archived.

## Current audit target
- Source file:
  - `manuscript_llm_ai_nudges_draft.md`
- Audit date:
  - `2026-06-22`

## In-text citation set currently used in the draft
The current main-text citation set is:

1. Häubl and Trifts (2000)
2. Senecal and Nantel (2004)
3. Ursu (2018)
4. Wang and Benbasat (2007)
5. Wang et al. (2018)
6. Wang and Wang (2019)
7. Xiao and Benbasat (2007)
8. Luo et al. (2019)
9. Ebrahimi et al. (2022)
10. de Cicco et al. (2022)
11. Chung et al. (2020)
12. Chen et al. (2021)

## References-section alignment
- The current references section in `manuscript_llm_ai_nudges_draft.md` contains entries for all 12 citations currently used in the main text.
- No extra references were found in the draft references section beyond the current in-text citation set.
- No currently used in-text citations were found to be missing from the references section.

## What this audit confirms
- The draft is currently aligned at the level of `in-text citation present` versus `reference entry present`.
- The manuscript therefore does not currently have a citation-list mismatch problem.

## What this audit does not confirm
- This file does not certify that every reference is already in final journal style.
- This file does not certify that every cited work has an authoritative local PDF archived.
- For source-role mapping and local-file status, use:
  - `manuscript_citation_crosswalk.md`

## Remaining cleanup points
- `Xiao and Benbasat (2007)` is bibliographically confirmed in project records, but an authoritative local PDF is still not archived.
- `Ebrahimi et al. (2022)` is bibliographically confirmed in project records, but an authoritative local PDF is still not archived.
- The latest archive attempt on `2026-06-22` indicates that the remaining problem is access or download-route availability from this environment rather than a citation-list mismatch.
- The literature download log now records concrete manual-access routes for both missing PDFs, so later retrieval work no longer has to restart from a blank search.
- If the manuscript later gains or drops citations, this audit should be refreshed rather than assumed to remain valid.

## Practical use
- Use this file before submission-oriented formatting passes on the references section.
- Use this file together with `manuscript_citation_crosswalk.md` when deciding whether the next step is `style cleanup`, `source verification`, or `local-PDF archiving`.
- Use `replication_package/scripts/check_reference_alignment.py` when the draft changes and you want to rerun the alignment check instead of repeating the audit manually.
