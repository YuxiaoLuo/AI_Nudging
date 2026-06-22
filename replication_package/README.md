# Replication Package Manifest

## Purpose
This folder is a draft replication-package scaffold for the nudging manuscript. It turns the manuscript's generic promise of `treatment materials`, `codebook`, and `core analysis scripts` into an explicit package map before data collection and estimation outputs exist.

## Intended package contents

### 1. Treatment materials
- Current linked draft assets:
  - `../appendix_a_stimuli_and_treatment_materials.md`
  - `../figures/figure2_treatment_materials.html`
  - `../figures/figure1_conceptual_model.html`
- Intended final role:
  - show the scenario, product set, treatment wording, and representative interface materials used in Study 1

### 2. Measurement instrument and codebook
- Current linked draft assets:
  - `../appendix_b_measurement_instrument.md`
  - `codebook_shell.md`
- Intended final role:
  - document survey items, variable names, coding conventions, reverse-coding rules, retained scales, and analysis-ready constructs

### 3. Screening and sample-flow logic
- Current linked draft assets:
  - `../appendix_c_screening_and_sample_flow.md`
  - `../appendix_d_supplemental_robustness.md`
- Intended final role:
  - document the main confirmatory sample, exclusion workflow, and bounded robustness variants

### 4. Core analysis scripts
- Current linked draft assets:
  - `scripts/README.md`
  - `scripts/check_reference_alignment.py`
  - `scripts/check_package_links.py`
  - `scripts/check_reference_formatting.py`
  - `scripts/validation_workflow.md`
  - `scripts/01_screening_shell.md`
  - `scripts/02_constructs_shell.md`
  - `scripts/03_main_results_shell.md`
  - `scripts/04_robustness_shell.md`
- Intended final role:
  - generate the confirmatory tables, mechanism-path results, and any bounded supplemental outputs linked to the manuscript

## Suggested final directory structure

```text
replication_package/
  README.md
  codebook_shell.md
  data/
    raw/                 # if sharing is allowed
    processed/
  materials/
    stimuli/
    screenshots/
  scripts/
    01_screening.*
    02_constructs.*
    03_main_results.*
    04_robustness.*
  outputs/
    tables/
    figures/
```

## Current package coverage
- Treatment materials: scaffolded
- Measurement instrument: scaffolded
- Screening logic: scaffolded
- Results table shells: scaffolded in `../results_table_shells.md`
- Core analysis scripts: scaffolded
- Replication directory structure: scaffolded
- Shareable data objects: pending

## Packaging rule
- When a new package-relevant asset is created elsewhere in the repo, add or update its reference here so the replication package remains a useful entrypoint rather than a vague future promise.
