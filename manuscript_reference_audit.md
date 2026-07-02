# Manuscript Reference Audit

## Purpose
This file records the current relationship between the manuscript's in-text citations and the draft references section. The goal is to make later reference cleanup faster and to separate `reference-list alignment` from the narrower question of whether every cited paper already has an authoritative local PDF archived.

## Current audit target
- Source file:
  - `manuscript_llm_ai_nudges_draft.md`
- Audit date:
  - `2026-07-02`
- Audit helper:
  - `replication_package/scripts/check_reference_alignment.py`

## In-text citation set currently used in the draft
The current main-text citation set is:

1. Chen et al. (2021)
2. Chung et al. (2020)
3. de Cicco et al. (2022)
4. Ebrahimi et al. (2022)
5. Häubl and Trifts (2000)
6. Luo et al. (2019)
7. Senecal and Nantel (2004)
8. Ursu (2018)
9. Wang and Benbasat (2007)
10. Wang et al. (2018)
11. Wang and Wang (2019)
12. Xiao and Benbasat (2007)

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
  - `manuscript_source_archive_audit.md`

## Practical use
- Use this file before submission-oriented formatting passes on the references section.
- Use this file together with `manuscript_citation_crosswalk.md` when deciding whether the next step is `style cleanup`, `source verification`, or `local-PDF archiving`.
- Refresh this audit after any future manuscript citation changes or reference-list edits, ideally by rerunning `replication_package/scripts/check_reference_alignment.py` with `--report-md manuscript_reference_audit.md`.
