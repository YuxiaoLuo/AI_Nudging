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
- [ ] Confirm that Table 1 reports means, standard deviations, and correlations for the retained constructs, while keeping purchase likelihood visible as the action-oriented outcome and perceived decision quality as the evaluative endpoint.
- [ ] Confirm that Table 2 foregrounds the primary outcomes and the conversational-versus-UI contrast, with purchase likelihood read as willingness to act rather than as a substitute for the fuller mechanism test.
- [ ] Confirm that Table 3 cleanly separates mechanism-path estimates and indirect effects, and that the fuller support-versus-inspectability tradeoff is evaluated through perceived decision quality rather than forced onto every purchase-likelihood movement.
- [ ] Confirm that Table 4 remains bounded to secondary outcomes and robustness evidence only.

## Figures
- [ ] Review `figures/figure1_conceptual_model.html` for any theory changes after the final results are known.
- [ ] Review `figures/figure2_treatment_materials.html` against the final implemented stimuli.
- [ ] Decide whether a `Figure 3` sample-flow visual is actually needed or whether Appendix C is sufficient.
- [ ] Export any HTML-based figures into the final submission-ready format if the journal does not accept HTML artifacts directly.

## Appendices
- [ ] Confirm Appendix A matches the final implemented treatment materials exactly.
- [ ] Confirm Appendix B matches the final programmed survey and retained item set, including the distinction between forced product choice as the task anchor and purchase likelihood as the action-oriented outcome.
- [ ] Populate Appendix C with realized screening counts and final sample definitions.
- [ ] Populate Appendix D only with bounded supporting evidence and robustness material, preserving separate robustness interpretations for purchase likelihood and perceived decision quality.

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
- [ ] Read `manuscript_package_open_items.md` first if the goal is to see the current residual package issues without reconstructing them from multiple audits.
- [ ] Use `manuscript_reference_audit.md` to confirm the references list still matches the in-text citation set after any draft changes.
- [ ] If the saved reference-alignment audit may be stale, regenerate it with `replication_package/scripts/check_reference_alignment.py --repo-root . manuscript_llm_ai_nudges_draft.md --report-md manuscript_reference_audit.md`.
- [ ] Use `manuscript_source_archive_audit.md` to confirm which cited papers are already locally archived versus still waiting on manual retrieval.
- [ ] Use `manuscript_reference_format_audit.md` to confirm that any remaining warnings are truly outlet-specific rather than structural.
- [ ] Run `replication_package/scripts/check_reference_formatting.py` before the final bounded bibliography cleanup pass.
- [ ] If the saved reference-format audit may be stale, regenerate it with `replication_package/scripts/check_reference_formatting.py --repo-root . manuscript_llm_ai_nudges_draft.md --report-md manuscript_reference_format_audit.md`.
- [ ] Use `manuscript_reference_cleanup_notes.md` to run one bounded bibliography style-normalization pass once the target journal is fixed.
- [ ] Treat the remaining working-draft bibliography decisions as narrow by default: mainly `vs.` wording and whether `Frontiers:` should remain exactly as written in the Luo et al. (2019) title.
- [ ] Before changing either flagged title feature, decide explicitly whether the target outlet preserves source-title wording or normalizes it, and then apply that rule consistently across the whole references list.
- [ ] Verify DOI formatting and journal names in the reference list.
- [ ] Use `manuscript_citation_crosswalk.md` to confirm that any citation-role changes are intentional rather than accidental.
- [ ] If one of the two bridge PDFs is later archived manually, update `manuscript_source_archive_audit.md`, `manuscript_citation_crosswalk.md`, and `literature/download_log.md` together.
- [ ] If authoritative local PDFs are still desired for the two bridge citations, use the fallback routes recorded in `literature/download_log.md` from a different access context rather than restarting discovery work.
- [ ] Remove any placeholder `TBD` text that remains in package files.
- [ ] Use `replication_package/scripts/check_placeholder_text.py` to confirm that any remaining `TBD` text is confined to explicit templates or result shells rather than core handoff docs.
- [ ] Check that any later literature additions are reflected in both the manuscript and package files where relevant.

## Final package walk-through
- [ ] Use `replication_package/scripts/run_validation_suite.py` as the default lightweight package audit before the final manual walk-through.
- [ ] Treat that suite run as the default way to refresh `manuscript_reference_audit.md`, `manuscript_reference_format_audit.md`, and `manuscript_source_archive_audit.md` together before relying on the saved package state.
- [ ] If you want both saved package artifacts refreshed in one step, run the suite with `--report-md manuscript_package_validation_report.md --freshness-report-md manuscript_package_validation_freshness.md`.
- [ ] If a durable snapshot is useful for handoff or archiving, rerun the suite with `--report-md manuscript_package_validation_report.md`.
- [ ] If using the saved validation snapshot, confirm that its generation metadata and input fingerprints still correspond to the current draft and package-facing docs.
- [ ] Use `replication_package/scripts/check_validation_snapshot_freshness.py` if you want to verify the saved snapshot before deciding whether a full rerun is necessary.
- [ ] If a saved freshness decision would help handoff, write it with `--freshness-report-md manuscript_package_validation_freshness.md`.
- [ ] If repo HEAD has advanced after the saved snapshot was written but the tracked package fingerprints may still match, refresh only `manuscript_package_validation_freshness.md` before assuming the saved snapshot is stale.
- [ ] If the only later HEAD movement is the commit that saves `manuscript_package_validation_freshness.md` itself, do not refresh again just to chase that self-created commit.
- [ ] If the freshness check reports that any tracked manuscript or package fingerprint changed, treat the saved snapshot as genuinely stale and rerun the full suite rather than refreshing only the freshness artifact.
- [ ] Use `replication_package/scripts/validation_workflow.md` if you need to rerun or interpret the individual helpers separately.
- [ ] Start from `manuscript_package_index.md` and verify every linked file still exists and is current.
- [ ] Confirm `README.md` still points to the right manuscript entrypoints.
- [ ] Check that the package feels coherent to a new reader rather than only to someone who built it incrementally.

## Sign-off note
- [ ] When the study reaches a true submission-ready state, update `STATUS.md` so the project no longer reads as a packaging build-out phase.
