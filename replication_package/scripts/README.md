# Core Analysis Script Shells

## Purpose
These files define the intended analysis workflow before a final implementation language is chosen. They are language-agnostic shells, not executable scripts yet.

## Planned workflow
1. `01_screening_shell.md`
   - build the main confirmatory sample from raw responses
2. `02_constructs_shell.md`
   - score retained constructs and document item handling
3. `03_main_results_shell.md`
   - generate the main manuscript tables and mechanism-path results while keeping forced product choice as the task anchor rather than treating it as a substitute outcome
4. `04_robustness_shell.md`
   - run bounded sensitivity and supplemental checks only after the main results are fixed, with trust and satisfaction kept in the secondary layer

## Current helper utility
- Fastest `what should I run?` companion:
  - `validation_workflow.md`
- `check_reference_alignment.py`
  - lightweight local check for whether the manuscript's in-text citations and references section still align
  - useful during package cleanup before a full journal-style bibliography pass
  - default target: `../../manuscript_llm_ai_nudges_draft.md`
  - optional `--report-md` flag writes the current alignment audit into `../../manuscript_reference_audit.md` or another package-facing markdown artifact
- `check_package_links.py`
  - lightweight local check for whether package-doc file references still exist when resolved from each document's own location
  - default docs: `../../README.md`, `../../manuscript_package_index.md`, `../../manuscript_package_open_items.md`, `../../submission_readiness_checklist.md`, `../../replication_package/README.md`, `../../replication_package/codebook_shell.md`, and `../../replication_package/scripts/README.md`
  - useful when package entrypoints are edited and you want to catch stale file pointers quickly
- `check_reference_formatting.py`
  - lightweight local audit for reference-list ordering, DOI URL consistency, and a few bounded style-normalization risks
  - default target: `../../manuscript_llm_ai_nudges_draft.md`
  - in the current manuscript state, the remaining warnings are narrowed to outlet-specific title decisions such as `vs.` wording and the `Frontiers:` prefix rather than broader capitalization drift
  - those remaining title warnings should now be read as `source title confirmed, outlet normalization still pending` rather than as generic title uncertainty
  - useful before the final journal-style bibliography pass so cleanup stays disciplined rather than ad hoc
  - optional `--report-md` flag writes the current audit into `../../manuscript_reference_format_audit.md` or another package-facing markdown artifact
- `check_source_archive_status.py`
  - lightweight local audit for which cited manuscript sources are already archived as authoritative local PDFs versus only bibliographically confirmed
  - default inputs: `../../manuscript_citation_crosswalk.md`, `../../manuscript_llm_ai_nudges_draft.md`, and `../../literature/download_log.md`
  - treats a local file as archived only if it exists and begins with the `%PDF-` signature, so HTML challenge pages saved from vendor routes are not misclassified as valid paper PDFs
  - useful when you want to refresh `../../manuscript_source_archive_audit.md` without maintaining that handoff file manually
- `check_placeholder_text.py`
  - lightweight local audit for distinguishing unexpected `TBD` placeholders in core package docs from intentional placeholders in template appendices and result shells
  - default core docs: main manuscript/package entrypoints, including `../../manuscript_package_open_items.md`, plus the bibliography handoff artifacts
  - default core docs also include `../../replication_package/scripts/README.md`, because it now acts as a package-facing workflow handoff rather than as a disposable internal note
  - default template docs: `../../appendix_c_screening_and_sample_flow.md`, `../../appendix_d_supplemental_robustness.md`, `../../results_table_shells.md`, and `../../replication_package/codebook_shell.md`
  - useful before a handoff or submission-style walk-through when you want to know whether placeholder text remains only where it should
- `run_validation_suite.py`
  - one-command wrapper for the current package-link, citation-alignment, reference-formatting, source-archive-status, and placeholder-text checks
  - refreshes the package-facing bibliography and archive audit artifacts as part of the same run
  - the saved markdown snapshot now begins with a compact orientation summary so later readers can see the current residual counts before scanning the full raw check outputs
  - optional `--freshness-report-md` flag refreshes the package-facing freshness artifact immediately after the saved validation snapshot is rewritten
  - default docs: `../../README.md`, `../../manuscript_package_index.md`, `../../manuscript_package_open_items.md`, `../../submission_readiness_checklist.md`, `../../replication_package/README.md`, `../../replication_package/codebook_shell.md`, and `../../replication_package/scripts/README.md`
  - default freshness-tracked bibliography inputs: `../../manuscript_citation_crosswalk.md`, `../../literature/download_log.md`, and `../../manuscript_source_archive_audit.md`
  - useful when you want one reproducible package-validation pass instead of remembering the helper order manually
  - optional `--report-md` flag writes the suite output into a reusable markdown artifact with generation metadata and input fingerprints
- `check_validation_snapshot_freshness.py`
  - checks whether the saved markdown validation snapshot still matches the current repo head and tracked file fingerprints
  - default report: `../../manuscript_package_validation_report.md`
  - useful when you want to trust the saved snapshot without rerunning the full validation suite
  - treats tracked manuscript/package inputs as the freshness criterion while still surfacing repository-HEAD drift as provenance
  - optional `--freshness-report-md` flag writes that freshness decision into a reusable markdown artifact
- `validation_workflow.md`
  - compact guide for when to run the current lightweight checks, what each one covers, and which file to read first when the question is `what is left?` versus `is the snapshot current?`

## Rule
- When the final analysis language is chosen, each shell should be translated into one real script while preserving the same numbering and responsibility split.
