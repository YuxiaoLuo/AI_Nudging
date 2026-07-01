# Manuscript Package Validation Report

## Purpose
This file records one lightweight validation-suite snapshot for the current manuscript package.

## Snapshot metadata
- Generated at (UTC): `2026-07-01T19:52:04+00:00`
- Repository HEAD at generation: `1950706f2e3594d83f9fd7b3a006f1e177446d1e`

## Input fingerprints
- `manuscript_llm_ai_nudges_draft.md`: sha256 `d0841293ab41`
- `README.md`: sha256 `a510f939dd6e`
- `manuscript_package_index.md`: sha256 `391dfcaaaef6`
- `manuscript_package_open_items.md`: sha256 `5b33b6c4f9eb`
- `submission_readiness_checklist.md`: sha256 `1e430fee8624`
- `replication_package/README.md`: sha256 `da6d4ec4db21`
- `manuscript_reference_audit.md`: sha256 `94b8b1b478ec`
- `manuscript_reference_format_audit.md`: sha256 `0766bb2e1503`
- `manuscript_citation_crosswalk.md`: sha256 `8d5476741689`
- `literature/download_log.md`: sha256 `b7bab40dfeb3`
- `manuscript_source_archive_audit.md`: sha256 `9c44ef554e52`

## Validator-script fingerprints
- `replication_package/scripts/run_validation_suite.py`: sha256 `b88a21c811aa`
- `replication_package/scripts/check_validation_snapshot_freshness.py`: sha256 `42bc7bc752dc`
- `replication_package/scripts/check_package_links.py`: sha256 `efc91ccac4f2`
- `replication_package/scripts/check_reference_alignment.py`: sha256 `dd7bbef31ea6`
- `replication_package/scripts/check_reference_formatting.py`: sha256 `b5f349592bf5`
- `replication_package/scripts/check_source_archive_status.py`: sha256 `2fd4f177d359`
- `replication_package/scripts/check_placeholder_text.py`: sha256 `a35d6125add0`

## Current validation target
- Repository root: `/Users/yuxiaoluo/.openclaw/workspace/projects/nudging`
- Manuscript: `/Users/yuxiaoluo/.openclaw/workspace/projects/nudging/manuscript_llm_ai_nudges_draft.md`
- Package-facing docs included in link check:
  - `README.md`
  - `manuscript_package_index.md`
  - `manuscript_package_open_items.md`
  - `submission_readiness_checklist.md`
  - `replication_package/README.md`
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
Referenced package paths: 10
Missing targets: 0

Doc: submission_readiness_checklist.md
Referenced package paths: 23
Missing targets: 0

Doc: replication_package/README.md
Referenced package paths: 24
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
Files with placeholders: 3
Total placeholder hits: 59

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
  - 24: | Shopping aid felt conversational | `TBD` | `TBD` | `TBD` | Descriptive validation |
  - 25: | Guidance adapted to my inputs or needs | `TBD` | `TBD` | `TBD` | Descriptive validation |
  - 26: | AI played a meaningful role in the guidance | `TBD` | `TBD` | `TBD` | Descriptive validation |
  - 27: | Recommendation logic was visibly presented | `TBD` | `TBD` | `TBD` | Diagnostic only |
  - 43: | Perceived personalization | `TBD` | `TBD` | `TBD` |
  - 44: | Cognitive load | `TBD` | `TBD` | `TBD` |
  - 45: | Choice confidence | `TBD` | `TBD` | `TBD` |
  - 46: | Perceived transparency | `TBD` | `TBD` | `TBD` |
  - 47: | Perceived decision quality | `TBD` | `TBD` | `TBD` |
  - 59: | Trust in the shopping aid | `TBD` | `TBD` | `TBD` | `TBD` | Secondary only |
  - 60: | Satisfaction with guidance process | `TBD` | `TBD` | `TBD` | `TBD` | Secondary only |
  - 75: | Main confirmatory sample | `TBD` | `TBD` | `TBD` | Headline reference |
  - 76: | Robustness variant 1 | `TBD` | `TBD` | `TBD` | Narrower screen |
  - 77: | Robustness variant 2 | `TBD` | `TBD` | `TBD` | Sensitivity only |
  - 93: | Staged regression confirmation | `TBD` | `TBD` |
  - 94: | Alternative indirect-effect estimation | `TBD` | `TBD` |
  - 95: | Secondary missing-data handling | `TBD` | `TBD` |
- results_table_shells.md: 25
  - 16: | 1. Purchase likelihood | `TBD` | `TBD` | `--` |  |  |  |  |  |  |  |
  - 17: | 2. Perceived decision quality | `TBD` | `TBD` | `TBD` | `--` |  |  |  |  |  |  |
  - 18: | 3. Perceived personalization | `TBD` | `TBD` | `TBD` | `TBD` | `--` |  |  |  |  |  |
  - 19: | 4. Cognitive load (reverse coded) | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | `--` |  |  |  |  |
  - 20: | 5. Choice confidence | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | `--` |  |  |  |
  - 21: | 6. Perceived transparency | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | `--` |  |  |
  - 22: | 7. Trust | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | `--` |  |
  - 23: | 8. Satisfaction | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | `--` |
  - 39: | Purchase likelihood | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` |
  - 40: | Perceived decision quality | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` |
  - 56: | Perceived personalization | `TBD` | `TBD` | `TBD` | Benefit-route entry |
  - 57: | Perceived transparency | `TBD` | `TBD` | `TBD` | Risk-route entry |
  - 63: | Perceived personalization -> cognitive load (reverse coded) | `TBD` | `TBD` | Support simplification route |
  - 64: | Cognitive load (reverse coded) -> choice confidence | `TBD` | `TBD` | Confidence-building route |
  - 65: | Choice confidence -> perceived decision quality | `TBD` | `TBD` | Positive evaluative route |
  - 66: | Perceived transparency -> perceived decision quality | `TBD` | `TBD` | Inspectability route |
  - 67: | Conversational nudge -> purchase likelihood (direct) | `TBD` | `TBD` | Direct behavioral path |
  - 68: | Conversational nudge -> perceived decision quality (residual direct effect, if retained) | `TBD` | `TBD` | Interpret cautiously |
  - 74: | Conversational nudge -> personalization -> cognitive load -> confidence -> decision quality | `TBD` | `TBD` | Support-route indirect effect |
  - 75: | Conversational nudge -> transparency -> decision quality | `TBD` | `TBD` | Opacity-route indirect effect |
  - 86: | Trust | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | Secondary only |
  - 87: | Satisfaction | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | Secondary only |
  - 93: | Main confirmatory sample | `TBD` | `TBD` | `TBD` | Reference row |
  - 94: | Variant 1 | `TBD` | `TBD` | `TBD` | Narrower screen or coding choice |
  - 95: | Variant 2 | `TBD` | `TBD` | `TBD` | Sensitivity only if needed |
```

## Interpretation note
- Treat `PASS` here as confirmation that the current lightweight checks did not find structural package or bibliography failures.
- Treat any remaining warnings inside the individual outputs as follow-up guidance, not as automatic blockers, unless they contradict the intended submission state.
