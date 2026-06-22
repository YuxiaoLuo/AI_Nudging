# Manuscript Asset Plan: LLM Conversational Nudges

## Purpose
This file converts the manuscript's current reporting commitments into a concrete packaging plan. The goal is to make the paper easier to execute as a submission-shaped package without reopening the core theory or methods framing.

## Package entrypoint
- Current package index:
  - `manuscript_package_index.md`
- Citation verification map:
  - `manuscript_citation_crosswalk.md`
- Reference-list alignment audit:
  - `manuscript_reference_audit.md`
- Reference-style cleanup notes:
  - `manuscript_reference_cleanup_notes.md`
- Submission workflow:
  - `submission_readiness_checklist.md`

## Main-text tables

### Table 1. Descriptive statistics and correlations
- Status: required by current manuscript text
- Draft asset: `results_table_shells.md`
- Purpose:
  - Report construct means, standard deviations, and correlations before or alongside the structural results.
  - Give readers a compact view of the support-route and transparency-route variables before the path estimates.
- Likely contents:
  - purchase likelihood
  - perceived decision quality
  - perceived personalization
  - cognitive load
  - choice confidence
  - perceived transparency
  - trust
  - satisfaction
- Notes:
  - Keep the confirmatory core constructs visually prominent even if secondary outcomes are retained in the same table.

### Table 2. Headline treatment effects on primary outcomes
- Status: strongly implied by the current results plan
- Draft asset: `results_table_shells.md`
- Purpose:
  - Present the conversational-versus-UI and conversational-versus-control contrasts on purchase likelihood and perceived decision quality.
  - Keep the paper's central comparison visible rather than burying it inside omnibus treatment tests.
- Likely contents:
  - condition means
  - planned contrasts
  - confidence intervals
  - effect sizes where appropriate
  - stable covariate specification indicator

### Table 3. Mechanism-path results
- Status: required by the current theory-aligned analysis sequence
- Draft asset: `results_table_shells.md`
- Purpose:
  - Report the staged support and opacity pathway evidence.
  - Show whether conversational guidance increases personalization, reduces cognitive load, increases confidence, and decreases transparency in the expected pattern.
- Likely contents:
  - path coefficients
  - indirect effects
  - confidence intervals
  - any residual direct effect reported separately and interpreted cautiously

### Table 4. Secondary outcomes and compact robustness checks
- Status: optional but likely useful
- Draft asset: `results_table_shells.md`
- Purpose:
  - Keep trust, satisfaction, and limited robustness evidence visible without letting them compete with the paper's headline tests.
- Likely contents:
  - trust and satisfaction contrasts
  - brief alternative-screening or alternative-coding checks if used
- Guardrail:
  - This table should remain clearly secondary and should not expand into a generic appendix-in-disguise.

## Figures

### Figure 1. Conceptual model
- Status: required
- Draft asset: `figures/figure1_conceptual_model.html`
- Purpose:
  - Visualize the core tradeoff model linking conversational guidance to the benefit route and the transparency-risk route.
- Core paths:
  - conversational AI nudge -> perceived personalization
  - perceived personalization -> lower cognitive load
  - lower cognitive load -> higher choice confidence
  - choice confidence -> perceived decision quality
  - conversational AI nudge -> lower perceived transparency
  - lower perceived transparency -> lower perceived decision quality
  - conversational AI nudge -> higher purchase likelihood

### Figure 2. Representative treatment materials
- Status: explicitly committed in the manuscript
- Draft asset: `figures/figure2_treatment_materials.html`
- Purpose:
  - Show representative screenshots or visual excerpts from the conversational and UI-based nudge conditions.
- Minimum contents:
  - conversational assistant view
  - UI-based badge or highlighted-placement view
- Guardrail:
  - Use representative materials, not every screen. The figure should clarify the treatment contrast quickly.

### Figure 3. Sample-flow visualization
- Status: optional because the manuscript allows either table, appendix flowchart, or short robustness display
- Purpose:
  - Make the screening pipeline inspectable if the final write-up benefits from a visual flow rather than a text-only description.
- Use only if:
  - the exclusions are numerous enough that prose or a compact appendix table would feel opaque

## Appendices

### Appendix A. Full stimuli and treatment materials
- Status: effectively required if space permits
- Draft asset: `appendix_a_stimuli_and_treatment_materials.md`
- Purpose:
  - Preserve the exact wording and presentation logic for the conversational and UI conditions.
- Include:
  - shopping scenario
  - product grid
  - assistant prompt or scripted exchange
  - UI badge or recommendation wording

### Appendix B. Full measurement instrument
- Status: explicitly committed in the manuscript
- Draft asset: `appendix_b_measurement_instrument.md`
- Purpose:
  - Provide full item wording, reverse-coding direction, and concise scale diagnostics for retained constructs.
- Include:
  - all construct items
  - manipulation checks
  - control items
  - coding notes

### Appendix C. Screening and sample-flow details
- Status: likely required for empirical credibility
- Draft asset: `appendix_c_screening_and_sample_flow.md`
- Purpose:
  - Show how many responses were removed under each prespecified quality rule and what analyzable sample remained.
- Include:
  - initial collected sample
  - exclusions by rule
  - final sample by condition
  - any alternate-screening variants used for robustness

### Appendix D. Supplemental robustness and secondary analyses
- Status: optional but likely useful
- Draft asset: `appendix_d_supplemental_robustness.md`
- Purpose:
  - Keep confirmatory and secondary evidence clearly separated.
- Include only:
  - robustness checks that materially defend the main findings
  - limited secondary-outcome detail not needed in the main text

## Replication package components
- Status: conditional on journal policy and data-sharing constraints, but already anticipated in the manuscript
- Draft assets:
  - `replication_package/README.md`
  - `replication_package/codebook_shell.md`
  - `replication_package/scripts/README.md`
  - `replication_package/scripts/01_screening_shell.md`
  - `replication_package/scripts/02_constructs_shell.md`
  - `replication_package/scripts/03_main_results_shell.md`
  - `replication_package/scripts/04_robustness_shell.md`
  - `replication_package/data/README.md`
  - `replication_package/materials/README.md`
  - `replication_package/materials/manifest.md`
  - `replication_package/outputs/README.md`
  - `replication_package/outputs/manifest.md`
- Minimum package:
  - treatment materials
  - codebook
  - core analysis scripts
- Nice-to-have:
  - mock data dictionary
  - table/figure generation scripts mapped to manuscript assets

## Priority order
1. Figure 1 conceptual model
2. Figure 2 representative treatment materials
3. Table 1 descriptive statistics and correlations
4. Table 2 headline treatment effects
5. Table 3 mechanism-path results
6. Appendix B full measurement instrument
7. Appendix C screening and sample-flow details
8. Appendix A full stimuli
9. Table 4 or Appendix D for bounded secondary evidence

## Practical use
- Treat this file as the packaging checklist for future heartbeats.
- Add asset filenames here once draft tables, figures, or appendices are actually created.
- If the manuscript's reporting promises change, update this file rather than rediscovering the commitments from the prose each time.
- Use the citation crosswalk during reference cleanup so the anchor hierarchy and local-file matches do not have to be reconstructed from scratch.
- Use the reference audit to distinguish citation-list alignment work from local-PDF archiving work.
- Use the reference cleanup notes to separate style normalization from citation verification and source retrieval.
