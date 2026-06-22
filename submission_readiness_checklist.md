# Submission Readiness Checklist

## Purpose
This checklist converts the current manuscript package into a pre-submission workflow. It is meant to reduce last-mile confusion once data collection, analysis, and manuscript finishing begin.

## Manuscript core
- [ ] Confirm the target journal and align formatting requirements.
- [ ] Re-read `manuscript_llm_ai_nudges_draft.md` after empirical results are inserted.
- [ ] Verify that the title, abstract, introduction, theory, methods, results, discussion, and conclusion still tell one consistent story.
- [ ] Confirm that the conversational-versus-UI comparison remains the central empirical contrast throughout.
- [ ] Check that all cited works in the text appear in the references section and vice versa.

## Tables
- [ ] Populate `results_table_shells.md` with final estimates or map each shell to the final journal-formatted table file.
- [ ] Confirm that Table 1 reports means, standard deviations, and correlations for the retained constructs.
- [ ] Confirm that Table 2 foregrounds the primary outcomes and the conversational-versus-UI contrast.
- [ ] Confirm that Table 3 cleanly separates mechanism-path estimates and indirect effects.
- [ ] Confirm that Table 4 remains bounded to secondary outcomes and robustness evidence only.

## Figures
- [ ] Review `figures/figure1_conceptual_model.html` for any theory changes after the final results are known.
- [ ] Review `figures/figure2_treatment_materials.html` against the final implemented stimuli.
- [ ] Decide whether a `Figure 3` sample-flow visual is actually needed or whether Appendix C is sufficient.
- [ ] Export any HTML-based figures into the final submission-ready format if the journal does not accept HTML artifacts directly.

## Appendices
- [ ] Confirm Appendix A matches the final implemented treatment materials exactly.
- [ ] Confirm Appendix B matches the final programmed survey and retained item set.
- [ ] Populate Appendix C with realized screening counts and final sample definitions.
- [ ] Populate Appendix D only with bounded supporting evidence and robustness material.

## Replication package
- [ ] Confirm `replication_package/codebook_shell.md` has been converted into a final codebook.
- [ ] Implement the script shells in the final analysis language.
- [ ] Add any shareable raw or processed data objects allowed by policy.
- [ ] Ensure the replication outputs can regenerate the main reported tables and figures.
- [ ] Check that the replication package README still reflects the final folder contents.

## Screening and construct handling
- [ ] Fix the main confirmatory sample definition before interpreting results.
- [ ] Verify that any exclusions were prespecified and consistently applied.
- [ ] Verify the final retained construct items and reverse-coding rules.
- [ ] Check that reliability and construct-separability evidence are adequate for the retained batteries.

## References and source hygiene
- [ ] Use `manuscript_reference_audit.md` to confirm the references list still matches the in-text citation set after any draft changes.
- [ ] Use `manuscript_reference_format_audit.md` to confirm that any remaining warnings are truly outlet-specific rather than structural.
- [ ] Run `replication_package/scripts/check_reference_formatting.py` before the final bounded bibliography cleanup pass.
- [ ] Use `manuscript_reference_cleanup_notes.md` to run one bounded bibliography style-normalization pass once the target journal is fixed.
- [ ] Verify DOI formatting and journal names in the reference list.
- [ ] Use `manuscript_citation_crosswalk.md` to confirm that any citation-role changes are intentional rather than accidental.
- [ ] If authoritative local PDFs are still desired for the two bridge citations, use the fallback routes recorded in `literature/download_log.md` from a different access context rather than restarting discovery work.
- [ ] Remove any placeholder `TBD` text that remains in package files.
- [ ] Check that any later literature additions are reflected in both the manuscript and package files where relevant.

## Final package walk-through
- [ ] Use `replication_package/scripts/run_validation_suite.py` as the default lightweight package audit before the final manual walk-through.
- [ ] If a durable snapshot is useful for handoff or archiving, rerun the suite with `--report-md manuscript_package_validation_report.md`.
- [ ] Use `replication_package/scripts/validation_workflow.md` if you need to rerun or interpret the individual helpers separately.
- [ ] Start from `manuscript_package_index.md` and verify every linked file still exists and is current.
- [ ] Confirm `README.md` still points to the right manuscript entrypoints.
- [ ] Check that the package feels coherent to a new reader rather than only to someone who built it incrementally.

## Sign-off note
- [ ] When the study reaches a true submission-ready state, update `STATUS.md` so the project no longer reads as a packaging build-out phase.
