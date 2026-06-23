# Validation Workflow

## Purpose
This file explains how to use the current lightweight package-validation helpers before the final empirical scripts exist. The goal is to preserve a repeatable verification routine for package integrity and bibliography alignment.

## Current runnable checks

### 0. Full lightweight validation suite
- Script:
  - `run_validation_suite.py`
- Default purpose:
  - run the package-link, citation-alignment, reference-formatting, and source-archive-status helpers in one reproducible pass
- Typical use:
  - before a package handoff, after several documentation edits, or whenever you want a compact current-state audit without manually sequencing the helpers
- Default package docs covered by the link check inside the suite:
  - `README.md`
  - `manuscript_package_index.md`
  - `submission_readiness_checklist.md`
  - `replication_package/README.md`
- Example:

```bash
python3 replication_package/scripts/run_validation_suite.py --repo-root .
```

- Report example:

```bash
python3 replication_package/scripts/run_validation_suite.py \
  --repo-root . \
  --report-md manuscript_package_validation_report.md
```

### 1. Package entrypoint link check
- Script:
  - `check_package_links.py`
- Default purpose:
  - confirm that repo-relative file references in package-facing docs still resolve
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

### 4. Source-archive status audit
- Script:
  - `check_source_archive_status.py`
- Default purpose:
  - regenerate a compact audit showing which cited manuscript sources are already archived locally versus still missing authoritative local PDFs
- Typical use:
  - after literature-retrieval work, after citation-crosswalk updates, or before a package handoff that needs clear source-archive status
- Example:

```bash
python3 replication_package/scripts/check_source_archive_status.py --repo-root .
```

## Recommended order during package cleanup
1. Use `run_validation_suite.py` when you want one reproducible pass across the current lightweight checks.
2. Use its `--report-md` flag when you want the current validation state preserved as a handoff artifact rather than left only in terminal output.
   The saved report also records generation time, repository head, and input file fingerprints so later sessions can judge whether the snapshot is stale.
3. Use `check_validation_snapshot_freshness.py` when you want to test whether the saved snapshot is still trustworthy before deciding to rerun the full suite.
   Treat the tracked manuscript and package-doc fingerprints as the actual freshness criterion, while reading any repository-HEAD drift as provenance about changes made after the snapshot was written.
   If useful, write that decision to disk with `--freshness-report-md manuscript_package_validation_freshness.md`.
4. Run `check_package_links.py` separately only when you are editing package-facing docs and want a faster targeted recheck.
5. Run `check_reference_alignment.py` separately only when you changed citations or the references section and do not need the full suite.
6. Run `check_reference_formatting.py` separately when the citation set is stable and the next step is bounded bibliography cleanup rather than theory expansion.
7. Run `check_source_archive_status.py` separately when the question is no longer `are the citations aligned?` but `which cited sources are still not locally archived?`
8. If the citation, formatting, and archive-status checks pass, use:
   - `manuscript_reference_audit.md`
   - `manuscript_source_archive_audit.md`
   - `manuscript_reference_cleanup_notes.md`
   - `manuscript_citation_crosswalk.md`
   to decide whether the next step is style cleanup, citation-role review, or PDF retrieval.
9. If the package-link check passes, do the final walk-through items in `submission_readiness_checklist.md`.

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
