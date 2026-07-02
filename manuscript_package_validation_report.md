# Manuscript Package Validation Report

## Purpose
This file records one lightweight validation-suite snapshot for the current manuscript package.

## Snapshot metadata
- Generated at (UTC): `2026-07-02T05:21:50+00:00`
- Repository HEAD at generation: `5e51afac38de7a135dcd4162203adebc3115cd6c`

## Input fingerprints
- `manuscript_llm_ai_nudges_draft.md`: sha256 `b60106712260`
- `README.md`: sha256 `549e7274f3db`
- `manuscript_package_index.md`: sha256 `b06fae90caf8`
- `manuscript_package_open_items.md`: sha256 `b1dfbbdd8714`
- `submission_readiness_checklist.md`: sha256 `7dedc4e3a101`
- `replication_package/README.md`: sha256 `da6d4ec4db21`
- `replication_package/codebook_shell.md`: sha256 `7e487e4f937e`
- `replication_package/scripts/README.md`: sha256 `8bd4a5a362eb`
- `manuscript_reference_audit.md`: sha256 `7cb087c771bf`
- `manuscript_reference_format_audit.md`: sha256 `55cc1df64a17`
- `manuscript_citation_crosswalk.md`: sha256 `8d5476741689`
- `literature/download_log.md`: sha256 `3023cdbc3584`
- `manuscript_source_archive_audit.md`: sha256 `36ed8ce1feea`

## Validator-script fingerprints
- `replication_package/scripts/run_validation_suite.py`: sha256 `9085031993bb`
- `replication_package/scripts/check_validation_snapshot_freshness.py`: sha256 `42bc7bc752dc`
- `replication_package/scripts/check_package_links.py`: sha256 `915ab5083d37`
- `replication_package/scripts/check_reference_alignment.py`: sha256 `dd7bbef31ea6`
- `replication_package/scripts/check_reference_formatting.py`: sha256 `b5f349592bf5`
- `replication_package/scripts/check_source_archive_status.py`: sha256 `2fd4f177d359`
- `replication_package/scripts/check_placeholder_text.py`: sha256 `8c439584c1da`

## Current validation target
- Repository root: `/Users/yuxiaoluo/.openclaw/workspace/projects/nudging`
- Manuscript: `/Users/yuxiaoluo/.openclaw/workspace/projects/nudging/manuscript_llm_ai_nudges_draft.md`
- Package-facing docs included in link check:
  - `README.md`
  - `manuscript_package_index.md`
  - `manuscript_package_open_items.md`
  - `submission_readiness_checklist.md`
  - `replication_package/README.md`
  - `replication_package/codebook_shell.md`
  - `replication_package/scripts/README.md`
- Bibliography-side files tracked for source-archive freshness:
  - `manuscript_reference_audit.md`
  - `manuscript_reference_format_audit.md`
  - `manuscript_citation_crosswalk.md`
  - `literature/download_log.md`
  - `manuscript_source_archive_audit.md`

## Included lightweight checks
- package-link integrity for the main manuscript/package entrypoints
- manuscript citation/reference alignment
- bibliography-format consistency warnings
- source-archive status for cited manuscript references
- placeholder-text carryover in core handoff docs versus explicit templates
- validator-script drift for the saved package-validation snapshot

## Quick orientation
- Read `manuscript_package_open_items.md` first if you want the fastest statement of residual package work.
- Read `manuscript_package_validation_freshness.md` if your first question is whether this saved snapshot is still current.
- Current lightweight snapshot highlights:
  - Package links currently missing: `0`
  - Citation alignment residuals: `0` unmatched tokens, `0` uncited reference entries
  - Remaining bibliography-style flags: `vs.` = `yes`, `Frontiers:` = `yes`
  - Cited sources still lacking authoritative local PDFs: `2`
    - Xiao and Benbasat (2007)
    - Ebrahimi et al. (2022)
  - Current archive-gap diagnosis:
    - Xiao and Benbasat (2007): publicly readable repository full text, but no archived local PDF here
    - Ebrahimi et al. (2022): request-only repository page, with no public full text exposed
  - Unexpected placeholder hits in core package docs: `0`

## Validation results
### package_links
- Status: `PASS`
- Output:
```text
Doc: README.md
Referenced package paths: 23
Missing targets: 0

Doc: manuscript_package_index.md
Referenced package paths: 33
Missing targets: 0

Doc: manuscript_package_open_items.md
Referenced package paths: 11
Missing targets: 0

Doc: submission_readiness_checklist.md
Referenced package paths: 23
Missing targets: 0

Doc: replication_package/README.md
Referenced package paths: 24
Missing targets: 0

Doc: replication_package/codebook_shell.md
Referenced package paths: 2
Missing targets: 0

Doc: replication_package/scripts/README.md
Referenced package paths: 29
Missing targets: 0
```

### reference_alignment
- Status: `PASS`
- Output:
```text
Manuscript: /Users/yuxiaoluo/.openclaw/workspace/projects/nudging/manuscript_llm_ai_nudges_draft.md
Reference entries: 12
Distinct citation tokens found: 12
Cited reference entries: 12
Uncited reference entries: 0
Unmatched citation tokens: 0
```

### reference_formatting
- Status: `PASS`
- Output:
```text
Manuscript: /Users/yuxiaoluo/.openclaw/workspace/projects/nudging/manuscript_llm_ai_nudges_draft.md
Reference entries: 12
Entries with DOI URLs: 12
Alphabetical-order warning: no
Mixed subtitle capitalization warning: no
'vs.' warning: yes
'Frontiers:' warning: yes

Warnings:
- At least one title uses 'vs.'; in the current manuscript state this abbreviation is treated as source-confirmed, so the remaining question is whether the target outlet keeps it or normalizes it.
- At least one title starts with 'Frontiers:'; in the current manuscript state this prefix is treated as source-confirmed, so the remaining question is whether the target outlet keeps it exactly or normalizes it.

'vs.' examples:
- Frontiers: machines vs. humans: the impact of artificial intelligence chatbot disclosure on customer purchases.
- Effects of recommendation neutrality and sponsorship disclosure on trust vs. distrust in online recommendation agents: moderating role of explanations for organic recommendations.

'Frontiers:' examples:
- Frontiers: machines vs. humans: the impact of artificial intelligence chatbot disclosure on customer purchases.
```

### source_archive_status
- Status: `PASS`
- Output:
```text
Crosswalk: /Users/yuxiaoluo/.openclaw/workspace/projects/nudging/manuscript_citation_crosswalk.md
Source archive audit: /Users/yuxiaoluo/.openclaw/workspace/projects/nudging/manuscript_source_archive_audit.md
Citations checked: 12
Archived locally: 10
Invalid local PDFs: 0
Missing local PDFs: 2

Missing local PDFs:
- Xiao and Benbasat (2007)
- Ebrahimi et al. (2022)
```

### placeholder_text
- Status: `PASS`
- Output:
```text
Unexpected placeholders in core package docs
Files with placeholders: 0
Total placeholder hits: 0

Expected placeholders in template/result-shell docs
Files with placeholders: 4
Total placeholder hits: 92

- appendix_c_screening_and_sample_flow.md: 17
  - 67: | Responses collected | `TBD` | `TBD` | `TBD` | `TBD` | Raw total before exclusions |
  - 68: | Removed: incomplete responses | `TBD` | `TBD` | `TBD` | `TBD` | Core-post-task incompletion |
  - 69: | Removed: duplicate responses | `TBD` | `TBD` | `TBD` | `TBD` | Prespecified duplicate rule |
  - 70: | Removed: minimum-effort / implausibly fast responses | `TBD` | `TBD` | `TBD` | `TBD` | Completion-threshold screen |
  - 71: | Removed: attentiveness failures | `TBD` | `TBD` | `TBD` | `TBD` | Direct instruction item |
  - 72: | Removed: other prespecified disqualifications | `TBD` | `TBD` | `TBD` | `TBD` | Only if applicable |
  - 73: | Final analyzable sample | `TBD` | `TBD` | `TBD` | `TBD` | Main confirmatory sample |
  - 78: `We collected [TBD] responses. Prespecified quality screening removed [TBD] incomplete responses, [TBD] duplicate submissions, [TBD] implausibly fast or minimum-effort responses, and [TBD] attentiveness-screen failures, leaving a final analyzable sample of [TBD] participants ([TBD] conversational, [TBD] UI-based nudge, [TBD] control). These rules were fixed before outcome analysis and applied consistently across conditions.`
  - 93: | Main confirmatory sample | `TBD` | `TBD` | `TBD` | `TBD` | Baseline screened sample | Headline evidence |
  - 94: | Robustness variant 1 | `TBD` | `TBD` | `TBD` | `TBD` | Narrower threshold or coding rule | Robustness only |
  - 95: | Robustness variant 2 | `TBD` | `TBD` | `TBD` | `TBD` | Additional sensitivity restriction | Robustness only |
  - 111: | Product-category familiarity | `TBD` | `TBD` | `TBD` | Descriptive only |
  - 112: | Prior AI-shopping use | `TBD` | `TBD` | `TBD` | Descriptive only |
  - 113: | General trust in AI | `TBD` | `TBD` | `TBD` | Descriptive only |
  - 114: | Need for cognition subset | `TBD` | `TBD` | `TBD` | Descriptive only |
  - 115: | Shopping involvement | `TBD` | `TBD` | `TBD` | Descriptive only |
  - 127: `Residual item missingness on the retained core constructs was [TBD]. The confirmatory analyses were estimated on a [TBD] sample under one consistent missing-data rule. Any alternative missing-data handling, if used, is reported only as a secondary robustness check.`
- appendix_d_supplemental_robustness.md: 17
  - 27: | Shopping aid felt conversational | `TBD` | `TBD` | `TBD` | Descriptive validation |
  - 28: | Guidance adapted to my inputs or needs | `TBD` | `TBD` | `TBD` | Descriptive validation |
  - 29: | AI played a meaningful role in the guidance | `TBD` | `TBD` | `TBD` | Descriptive validation |
  - 30: | Recommendation logic was visibly presented | `TBD` | `TBD` | `TBD` | Diagnostic only |
  - 46: | Perceived personalization | `TBD` | `TBD` | `TBD` |
  - 47: | Cognitive load | `TBD` | `TBD` | `TBD` |
  - 48: | Choice confidence | `TBD` | `TBD` | `TBD` |
  - 49: | Perceived transparency | `TBD` | `TBD` | `TBD` |
  - 50: | Perceived decision quality | `TBD` | `TBD` | `TBD` |
  - 62: | Trust in the shopping aid | `TBD` | `TBD` | `TBD` | `TBD` | Secondary only |
  - 63: | Satisfaction with guidance process | `TBD` | `TBD` | `TBD` | `TBD` | Secondary only |
  - 78: | Main confirmatory sample | `TBD` | `TBD` | `TBD` | Headline reference |
  - 79: | Robustness variant 1 | `TBD` | `TBD` | `TBD` | Narrower screen |
  - 80: | Robustness variant 2 | `TBD` | `TBD` | `TBD` | Sensitivity only |
  - 99: | Staged regression confirmation | `TBD` | `TBD` |
  - 100: | Alternative indirect-effect estimation | `TBD` | `TBD` |
  - 101: | Secondary missing-data handling | `TBD` | `TBD` |
- results_table_shells.md: 25
  - 16: | 1. Purchase likelihood | `TBD` | `TBD` | `--` |  |  |  |  |  |  |  |
  - 17: | 2. Perceived decision quality | `TBD` | `TBD` | `TBD` | `--` |  |  |  |  |  |  |
  - 18: | 3. Perceived personalization | `TBD` | `TBD` | `TBD` | `TBD` | `--` |  |  |  |  |  |
  - 19: | 4. Cognitive load (reverse coded) | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | `--` |  |  |  |  |
  - 20: | 5. Choice confidence | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | `--` |  |  |  |
  - 21: | 6. Perceived transparency | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | `--` |  |  |
  - 22: | 7. Trust | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | `--` |  |
  - 23: | 8. Satisfaction | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | `--` |
  - 40: | Purchase likelihood | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` |
  - 41: | Perceived decision quality | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` |
  - 58: | Perceived personalization | `TBD` | `TBD` | `TBD` | Benefit-route entry |
  - 59: | Perceived transparency | `TBD` | `TBD` | `TBD` | Risk-route entry |
  - 65: | Perceived personalization -> cognitive load (reverse coded) | `TBD` | `TBD` | Support simplification route |
  - 66: | Cognitive load (reverse coded) -> choice confidence | `TBD` | `TBD` | Confidence-building route |
  - 67: | Choice confidence -> perceived decision quality | `TBD` | `TBD` | Positive evaluative route |
  - 68: | Perceived transparency -> perceived decision quality | `TBD` | `TBD` | Inspectability route |
  - 69: | Conversational nudge -> purchase likelihood (direct) | `TBD` | `TBD` | Direct behavioral path |
  - 70: | Conversational nudge -> perceived decision quality (residual direct effect, if retained) | `TBD` | `TBD` | Interpret cautiously |
  - 76: | Conversational nudge -> personalization -> cognitive load -> confidence -> decision quality | `TBD` | `TBD` | Support-route indirect effect |
  - 77: | Conversational nudge -> transparency -> decision quality | `TBD` | `TBD` | Opacity-route indirect effect |
  - 92: | Trust | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | Secondary only |
  - 93: | Satisfaction | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | Secondary only |
  - 99: | Main confirmatory sample | `TBD` | `TBD` | `TBD` | Reference row |
  - 100: | Variant 1 | `TBD` | `TBD` | `TBD` | Narrower screen or coding choice |
  - 101: | Variant 2 | `TBD` | `TBD` | `TBD` | Sensitivity only if needed |
- replication_package/codebook_shell.md: 33
  - 18: | `participant_id` | Participant identifier | ID | `TBD` | Platform export | De-identify if shared |
  - 20: | `choice_product` | Chosen headphone option | Categorical | `TBD` | Shopping task | Anchors which product the participant later evaluates; not the headline action outcome by itself |
  - 21: | `purchase_1` | Purchase likelihood item 1 | Numeric | `1-7` | Instrument | `TBD` |
  - 22: | `purchase_2` | Purchase likelihood item 2 | Numeric | `1-7` | Instrument | `TBD` |
  - 23: | `purchase_3` | Purchase likelihood item 3 | Numeric | `1-7` | Instrument | `TBD` |
  - 24: | `decision_quality_1` | Decision quality item 1 | Numeric | `1-7` | Instrument | `TBD` |
  - 25: | `decision_quality_2` | Decision quality item 2 | Numeric | `1-7` | Instrument | `TBD` |
  - 26: | `decision_quality_3` | Decision quality item 3 | Numeric | `1-7` | Instrument | `TBD` |
  - 27: | `personalization_1` | Personalization item 1 | Numeric | `1-7` | Instrument | `TBD` |
  - 28: | `personalization_2` | Personalization item 2 | Numeric | `1-7` | Instrument | `TBD` |
  - 29: | `personalization_3` | Personalization item 3 | Numeric | `1-7` | Instrument | `TBD` |
  - 33: | `confidence_1` | Choice confidence item 1 | Numeric | `1-7` | Instrument | `TBD` |
  - 34: | `confidence_2` | Choice confidence item 2 | Numeric | `1-7` | Instrument | `TBD` |
  - 35: | `confidence_3` | Choice confidence item 3 | Numeric | `1-7` | Instrument | `TBD` |
  - 36: | `transparency_1` | Transparency item 1 | Numeric | `1-7` | Instrument | `TBD` |
  - 37: | `transparency_2` | Transparency item 2 | Numeric | `1-7` | Instrument | `TBD` |
  - 38: | `transparency_3` | Transparency item 3 | Numeric | `1-7` | Instrument | `TBD` |
  - 48: | `control_ai_use` | Prior AI-shopping use | Numeric | `TBD` | Instrument | Covariate |
  - 52: | `attention_check` | Direct attentiveness item | Numeric | `TBD` | Instrument | Screening only |
  - 53: | `completion_time` | Completion duration | Numeric | `TBD` | Platform export | Screening only |
  - 67: | `purchase_likelihood` | `TBD` | No | `TBD` | `TBD` |
  - 68: | `decision_quality` | `TBD` | No | `TBD` | `TBD` |
  - 69: | `personalization` | `TBD` | No | `TBD` | `TBD` |
  - 70: | `cognitive_load_rc` | `TBD` | Yes | `TBD` | `TBD` |
  - 71: | `choice_confidence` | `TBD` | No | `TBD` | `TBD` |
  - 72: | `perceived_transparency` | `TBD` | No | `TBD` | `TBD` |
  - 73: | `trust` | `TBD` | No | `TBD` | `TBD` |
  - 74: | `satisfaction` | `TBD` | No | `TBD` | `TBD` |
  - 85: | `flag_incomplete` | `TBD` | `0/1` | `TBD` |
  - 86: | `flag_duplicate` | `TBD` | `0/1` | `TBD` |
  - 87: | `flag_low_effort` | `TBD` | `0/1` | `TBD` |
  - 88: | `flag_attention_fail` | `TBD` | `0/1` | `TBD` |
  - 89: | `flag_other_prespecified` | `TBD` | `0/1` | `TBD` |
```

## Interpretation note
- Treat `PASS` here as confirmation that the current lightweight checks did not find structural package or bibliography failures.
- Treat any remaining warnings inside the individual outputs as follow-up guidance, not as automatic blockers, unless they contradict the intended submission state.
