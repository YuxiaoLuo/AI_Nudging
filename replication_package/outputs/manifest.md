# Outputs Manifest

## Purpose
This file links the current manuscript-facing output assets into the replication-package outputs layer before executable scripts start generating final release files.

## Current source assets

### Table-source asset
- `../../results_table_shells.md`
- Current role:
  - authoritative shell for the four planned main-text results tables

### Figure-source assets
- `../../figures/figure1_conceptual_model.html`
- `../../figures/figure2_treatment_materials.html`
- Current role:
  - current manuscript-facing figure drafts

## Intended future generated outputs

### `tables/`
- populated versions of the manuscript's main tables
- any appendix tables generated directly from analysis scripts

### `figures/`
- exported submission-ready figure files
- any generated supplementary figures used in the replication package

## Maintenance rule
- If a generated table or figure becomes the new authoritative output, place it in the appropriate subfolder here or update this manifest so the replication package still points to the latest release-ready version.
