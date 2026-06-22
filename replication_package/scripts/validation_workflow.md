# Validation Workflow

## Purpose
This file explains how to use the current lightweight package-validation helpers before the final empirical scripts exist. The goal is to preserve a repeatable verification routine for package integrity and bibliography alignment.

## Current runnable checks

### 1. Package entrypoint link check
- Script:
  - `check_package_links.py`
- Default purpose:
  - confirm that repo-relative file references in `README.md` and `manuscript_package_index.md` still resolve
- Typical use:
  - after editing package entrypoints or adding new manuscript-facing assets
- Example:

```bash
python3 replication_package/scripts/check_package_links.py --repo-root . README.md manuscript_package_index.md
```

### 2. Manuscript citation/reference alignment check
- Script:
  - `check_reference_alignment.py`
- Default purpose:
  - confirm that the manuscript's in-text citations and references section still align at a basic structural level
- Typical use:
  - after editing the manuscript draft or references section
- Example:

```bash
python3 replication_package/scripts/check_reference_alignment.py manuscript_llm_ai_nudges_draft.md
```

### 3. Reference-format consistency audit
- Script:
  - `check_reference_formatting.py`
- Default purpose:
  - flag bounded reference-list cleanup risks such as nonuniform DOI presentation, alphabetical-order drift, and mixed subtitle-capitalization conventions
- Typical use:
  - before or during the final bibliography normalization pass once the citation set is frozen
- Example:

```bash
python3 replication_package/scripts/check_reference_formatting.py manuscript_llm_ai_nudges_draft.md
```

## Recommended order during package cleanup
1. Run `check_package_links.py` after updating `README.md`, `manuscript_package_index.md`, or other package-facing docs.
2. Run `check_reference_alignment.py` after changing the manuscript draft's citations or references.
3. Run `check_reference_formatting.py` when the citation set is stable and the next step is bounded bibliography cleanup rather than theory expansion.
4. If the citation and formatting checks pass, use:
   - `manuscript_reference_audit.md`
   - `manuscript_reference_cleanup_notes.md`
   - `manuscript_citation_crosswalk.md`
   to decide whether the next step is style cleanup, citation-role review, or PDF retrieval.
5. If the package-link check passes, do the final walk-through items in `submission_readiness_checklist.md`.

## Current scope limits
- These helpers do not validate journal-style bibliography formatting.
- These helpers do not choose a target outlet's final citation style for you.
- These helpers do not validate substantive theory consistency.
- These helpers do not validate empirical results, construct scoring, or robustness outputs.
- These helpers are narrow pre-analysis package checks, not replacements for the future full analysis scripts.

## Maintenance rule
- When a new lightweight validation helper is added, document:
  - what it checks
  - when to run it
  - what it does not check
in this file so the verification workflow remains understandable to a future session.
