# Core Analysis Script Shells

## Purpose
These files define the intended analysis workflow before a final implementation language is chosen. They are language-agnostic shells, not executable scripts yet.

## Planned workflow
1. `01_screening_shell.md`
   - build the main confirmatory sample from raw responses
2. `02_constructs_shell.md`
   - score retained constructs and document item handling
3. `03_main_results_shell.md`
   - generate the main manuscript tables and mechanism-path results
4. `04_robustness_shell.md`
   - run bounded sensitivity and supplemental checks only after the main results are fixed

## Current helper utility
- `check_reference_alignment.py`
  - lightweight local check for whether the manuscript's in-text citations and references section still align
  - useful during package cleanup before a full journal-style bibliography pass
  - default target: `../../manuscript_llm_ai_nudges_draft.md`
- `check_package_links.py`
  - lightweight local check for whether repo-relative file references in package docs still exist
  - default docs: `../../README.md` and `../../manuscript_package_index.md`
  - useful when package entrypoints are edited and you want to catch stale file pointers quickly
- `check_reference_formatting.py`
  - lightweight local audit for reference-list ordering, DOI URL consistency, and a few bounded style-normalization risks
  - default target: `../../manuscript_llm_ai_nudges_draft.md`
  - useful before the final journal-style bibliography pass so cleanup stays disciplined rather than ad hoc
- `validation_workflow.md`
  - compact guide for when to run the current lightweight checks and what each one covers

## Rule
- When the final analysis language is chosen, each shell should be translated into one real script while preserving the same numbering and responsibility split.
