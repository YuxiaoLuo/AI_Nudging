# Validation Workflow

## Purpose
This file explains how to use the current lightweight package-validation helpers before the final empirical scripts exist. The goal is to preserve a repeatable verification routine for package integrity and bibliography alignment.

## Fast decision paths
- If the question is `what is still unresolved in the package?`
  - read `manuscript_package_open_items.md` first, then return here only if you need the specific helper sequence
- If the question is `is the saved package snapshot still current?`
  - read `manuscript_package_validation_freshness.md` first, then use `check_validation_snapshot_freshness.py` only if you need to regenerate or verify that decision
- If the question is `which lightweight check should I run next?`
  - use the numbered sections below, starting from the narrowest helper that matches the question rather than rerunning every check by default
- If the question is `I just want one current package-state baseline`
  - run `run_validation_suite.py` with `--report-md manuscript_package_validation_report.md --freshness-report-md manuscript_package_validation_freshness.md`

## Current runnable checks

### 0. Full lightweight validation suite
- Script:
  - `run_validation_suite.py`
- Default purpose:
  - run the package-link, citation-alignment, reference-formatting, source-archive-status, and placeholder-text helpers in one reproducible pass
- Typical use:
  - before a package handoff, after several documentation edits, or whenever you want a compact current-state audit without manually sequencing the helpers
- Default package docs covered by the link check inside the suite:
  - `README.md`
  - `manuscript_package_index.md`
  - `manuscript_package_open_items.md`
  - `submission_readiness_checklist.md`
  - `replication_package/README.md`
- Default bibliography-side files fingerprinted in the saved report:
  - `manuscript_reference_audit.md`
  - `manuscript_reference_format_audit.md`
  - `manuscript_citation_crosswalk.md`
  - `literature/download_log.md`
  - `manuscript_source_archive_audit.md`
- Package-facing audit artifacts refreshed by the suite:
  - `manuscript_reference_audit.md`
  - `manuscript_reference_format_audit.md`
  - `manuscript_source_archive_audit.md`
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

- Saved report behavior:
  - the generated validation snapshot now starts with a compact `Quick orientation` block that surfaces the current residual counts for links, citation alignment, bibliography-style flags, missing local PDFs, and unexpected core-doc placeholders before the longer raw helper outputs

- Report + freshness example:

```bash
python3 replication_package/scripts/run_validation_suite.py \
  --repo-root . \
  --report-md manuscript_package_validation_report.md \
  --freshness-report-md manuscript_package_validation_freshness.md
```

- Post-commit nuance:
  - if you commit package-facing changes after writing the saved snapshot, the snapshot's own `Repository HEAD at generation` metadata can lag behind the latest repo head even when the tracked package fingerprints still match
  - in that case, rerun only `check_validation_snapshot_freshness.py --repo-root . --report-md manuscript_package_validation_report.md --freshness-report-md manuscript_package_validation_freshness.md` if you want the saved freshness artifact to record `CURRENT with HEAD drift noted`

### 1. Package entrypoint link check
- Script:
  - `check_package_links.py`
- Default purpose:
  - confirm that repo-relative file references in package-facing docs still resolve
- Typical use:
  - after editing package entrypoints or adding new manuscript-facing assets
- Default doc coverage includes:
  - `README.md`
  - `manuscript_package_index.md`
  - `manuscript_package_open_items.md`
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
  Basic run:

```bash
python3 replication_package/scripts/check_reference_alignment.py manuscript_llm_ai_nudges_draft.md
```

- Report example:

```bash
python3 replication_package/scripts/check_reference_alignment.py \
  --repo-root . \
  manuscript_llm_ai_nudges_draft.md \
  --report-md manuscript_reference_audit.md
```

### 3. Reference-format consistency audit
- Script:
  - `check_reference_formatting.py`
- Default purpose:
  - flag bounded reference-list cleanup risks such as nonuniform DOI presentation, alphabetical-order drift, and any remaining outlet-specific title-style decisions
- Typical use:
  - before or during the final bibliography normalization pass once the citation set is frozen
- Current manuscript state:
  - the structural checks pass, and the remaining warnings are limited to the narrower `vs.` and `Frontiers:` title cases rather than broader capitalization drift
  - those title features are now treated as source-confirmed in the local package docs, so the helper's remaining warnings should be read as `outlet normalization still pending`, not `bibliographic title uncertain`
- Example:
  Basic run:

```bash
python3 replication_package/scripts/check_reference_formatting.py manuscript_llm_ai_nudges_draft.md
```

- Report example:

```bash
python3 replication_package/scripts/check_reference_formatting.py \
  --repo-root . \
  manuscript_llm_ai_nudges_draft.md \
  --report-md manuscript_reference_format_audit.md
```

### 4. Source-archive status audit
- Script:
  - `check_source_archive_status.py`
- Default purpose:
  - regenerate a compact audit showing which cited manuscript sources are already archived locally versus still missing authoritative local PDFs
- Typical use:
  - after literature-retrieval work, after citation-crosswalk updates, or before a package handoff that needs clear source-archive status
- Current validation rule:
  - a local file only counts as archived if it exists and begins with the `%PDF-` signature; vendor challenge pages saved as `.pdf` files are treated as invalid rather than as real archived sources
- Example:

```bash
python3 replication_package/scripts/check_source_archive_status.py --repo-root .
```

### 5. Placeholder-text audit
- Script:
  - `check_placeholder_text.py`
- Default purpose:
  - distinguish unexpected `TBD` placeholders in core handoff docs from intentional placeholders that still belong in templates and result shells
- Typical use:
  - before a package handoff, before a submission-style walk-through, or after creating new package-facing docs that should not contain placeholder carryover
- Default core-doc coverage includes:
  - the front-door package docs such as `README.md`, `manuscript_package_index.md`, and `manuscript_package_open_items.md`
- Example:

```bash
python3 replication_package/scripts/check_placeholder_text.py --repo-root .
```

## Recommended order during package cleanup
1. Use `run_validation_suite.py` when you want one reproducible pass across the current lightweight checks.
2. Use its `--report-md` flag when you want the current validation state preserved as a handoff artifact rather than left only in terminal output.
   The saved report also records generation time, repository head, and input file fingerprints so later sessions can judge whether the snapshot is stale.
3. Use the suite's `--freshness-report-md` flag when you want the saved validation snapshot and its freshness decision refreshed together in one pass.
4. Use `check_validation_snapshot_freshness.py` separately when you want to test whether the saved snapshot is still trustworthy before deciding to rerun the full suite.
   Treat the tracked manuscript and package-doc fingerprints as the actual freshness criterion, while reading any repository-HEAD drift as provenance about changes made after the snapshot was written.
   After a commit that advances repo HEAD without changing the tracked package fingerprints further, this standalone freshness refresh is the right way to preserve an accurate saved handoff signal without rerunning the full suite.
   If useful, write that decision to disk with `--freshness-report-md manuscript_package_validation_freshness.md`.
5. Run `check_package_links.py` separately only when you are editing package-facing docs and want a faster targeted recheck.
6. Run `check_reference_alignment.py` separately only when you changed citations or the references section and do not need the full suite.
7. Run `check_reference_formatting.py` separately when the citation set is stable and the next step is bounded bibliography cleanup rather than theory expansion.
8. Run `check_source_archive_status.py` separately when the question is no longer `are the citations aligned?` but `which cited sources are still not locally archived?`
9. Run `check_placeholder_text.py` when you want to confirm that remaining `TBD` text is confined to explicit templates rather than leaking into the core manuscript/package handoff docs.
10. If the citation, formatting, and archive-status checks pass, use:
   - `manuscript_reference_audit.md`
   - `manuscript_source_archive_audit.md`
   - `manuscript_reference_cleanup_notes.md`
   - `manuscript_citation_crosswalk.md`
   to decide whether the next step is style cleanup, citation-role review, or PDF retrieval.
11. If the package-link and placeholder checks pass, do the final walk-through items in `submission_readiness_checklist.md`.

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
