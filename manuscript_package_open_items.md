# Manuscript Package Open Items

## Purpose
This file gives a fast, package-facing summary of what is still unresolved in the current manuscript package. The goal is to let a future session, coauthor, or reviewer-facing cleanup pass see the residual work immediately without rereading several audit files first.

## Current status snapshot
- Validation state:
  - the lightweight package checks currently pass across the main package entrypoints, the replication manifest, the codebook shell, and the scripts-layer workflow README
- Citation alignment:
  - no current citation-to-reference mismatch is flagged
- Package links:
  - no current broken package-doc links are flagged
- Placeholder carryover in core package docs:
  - none currently flagged

## Remaining bibliography style decisions
These are now narrow outlet-style decisions rather than broad cleanup problems.
The flagged title features have also been checked against authoritative publication metadata, so what remains is normalization choice rather than title-verification uncertainty.

1. Decide whether `vs.` should remain abbreviated or be spelled out in the final reference style.
   - Current affected titles:
     - `Frontiers: machines vs. humans: the impact of artificial intelligence chatbot disclosure on customer purchases.`
     - `Effects of recommendation neutrality and sponsorship disclosure on trust vs. distrust in online recommendation agents: moderating role of explanations for organic recommendations.`
2. Decide whether the `Frontiers:` prefix in Luo et al. (2019) should remain exactly as written in the final reference list.
   - Current affected title:
     - `Frontiers: machines vs. humans: the impact of artificial intelligence chatbot disclosure on customer purchases.`
Current decision rule:
- treat both `vs.` and `Frontiers:` as source-confirmed title features by default
- change them only if the target outlet's written style guidance or exemplar references clearly normalize them

## Remaining source-archive gaps
These are access-context issues, not source-discovery problems.

1. `Xiao and Benbasat (2007)`
   - citation is bibliographically confirmed
   - authoritative local PDF is still missing
   - the ResearchGate page appears to expose a publicly readable full-text view, but the exact MIS Quarterly and JSTOR PDF routes still returned challenge or access-block HTML from this environment on 2026-07-02, so the project still does not have a successfully archived local PDF copy
2. `Ebrahimi et al. (2022)`
   - citation is bibliographically confirmed
   - authoritative local PDF is still missing
   - current Taylor & Francis search snippets explicitly advertise `View PDF` / `Download PDF`, but the canonical Taylor & Francis PDF and abstract routes still resolved to challenge HTML from this environment on 2026-07-02, and a 2026-08-30 retry with the `?download=true` variant still returned `403 Forbidden`, so the remaining gap looks like access-gated retrieval rather than route discovery

Current rule:
- treat a file as `archived locally` only if it exists and validates as a real PDF, not merely because a vendor URL ended in `.pdf`
- do not repeat shell-level fetches of the same ResearchGate or publisher PDF routes unless the access context changes materially; the next meaningful attempt is an authenticated manual browser or institutional-library session

## Expected non-blocking placeholders
The validation suite still finds intentional to-be-determined placeholders in template or results-shell assets, but not in the core package handoff docs.

Current expected placeholder locations:
- `appendix_c_screening_and_sample_flow.md`
- `appendix_d_supplemental_robustness.md`
- `results_table_shells.md`
- `replication_package/codebook_shell.md`

## Where to act next
- For final reference-style decisions:
  - `manuscript_reference_format_audit.md`
  - `manuscript_reference_cleanup_notes.md`
- For missing bridge PDFs:
  - `manuscript_source_archive_audit.md`
  - `literature/download_log.md`
- For full package revalidation:
  - `manuscript_package_validation_report.md`
  - `manuscript_package_validation_freshness.md`
  - `replication_package/scripts/run_validation_suite.py`

## Practical use
- Read this file first if the question is `what is actually left to clean up?`
- Update this file whenever one of the current residual issues disappears or a new package-facing unresolved item emerges.
