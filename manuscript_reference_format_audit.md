# Manuscript Reference Format Audit

## Purpose
This file records the current lightweight formatting state of the manuscript references section. The goal is to separate `structural bibliography consistency` from the narrower set of `target-journal style choices` that still remain.

## Current audit target
- Source file:
  - `manuscript_llm_ai_nudges_draft.md`
- Audit date:
  - `2026-06-22`
- Audit helper:
  - `replication_package/scripts/check_reference_formatting.py`

## Current structural status
- The draft currently contains 12 reference entries.
- All 12 entries currently use full `https://doi.org/` URLs.
- No duplicate DOI URLs are currently flagged.
- The first-pass alphabetical ordering issue in the `Wang` entries has already been corrected.
- The current bibliography therefore passes the lightweight structural-format audit.

## Current remaining warnings
The audit currently reports only outlet-specific style warnings:

1. Mixed subtitle capitalization appears after colons across some titles.
2. At least one title currently uses `vs.`.
3. At least one title currently begins with `Frontiers:`.

## Interpretation
- These warnings do **not** indicate citation-list misalignment.
- These warnings do **not** indicate missing DOI URLs.
- These warnings do **not** require reopening the manuscript's theory or citation set.
- They indicate only that the final bibliography pass still needs one explicit target-journal style decision.

## What to do next
- If the target outlet prefers sentence case:
  - normalize all titles and subtitles in one bounded pass while preserving proper nouns and any required article prefixes.
- If the target outlet prefers title case:
  - convert all titles and subtitles in one bounded pass rather than editing only the flagged entries.
- Before making that pass:
  - keep the citation set frozen
  - confirm citation/reference alignment with `manuscript_reference_audit.md`
  - use `manuscript_reference_cleanup_notes.md` to keep the normalization pass bounded

## Related files
- `manuscript_reference_audit.md`
- `manuscript_reference_cleanup_notes.md`
- `manuscript_citation_crosswalk.md`
- `submission_readiness_checklist.md`

## Practical use
- Use this file when deciding whether the next bibliography task is `style normalization` versus `PDF retrieval`.
- Refresh this audit after any future reference-list edits that change title wording, ordering, or DOI presentation.
