# Manuscript Package Validation Report

## Purpose
This file records one lightweight validation-suite snapshot for the current manuscript package.

## Snapshot metadata
- Generated at (UTC): `2026-06-23T00:52:25+00:00`
- Repository HEAD at generation: `5818c11dcac60e572808b10bae993adf4b3de571`

## Input fingerprints
- `manuscript_llm_ai_nudges_draft.md`: sha256 `9b68409e8332`
- `README.md`: sha256 `83bf31b0cff2`
- `manuscript_package_index.md`: sha256 `d239a53ff745`
- `submission_readiness_checklist.md`: sha256 `e6f14f2fe552`

## Current validation target
- Repository root: `/Users/yuxiaoluo/.openclaw/workspace/projects/nudging`
- Manuscript: `/Users/yuxiaoluo/.openclaw/workspace/projects/nudging/manuscript_llm_ai_nudges_draft.md`
- Package-facing docs included in link check:
  - `README.md`
  - `manuscript_package_index.md`
  - `submission_readiness_checklist.md`

## Included lightweight checks
- package-link integrity for the main manuscript/package entrypoints
- manuscript citation/reference alignment
- bibliography-format consistency warnings
- source-archive status for cited manuscript references

## Validation results
### package_links
- Status: `PASS`
- Output:
```text
Doc: README.md
Referenced package paths: 22
Missing targets: 0

Doc: manuscript_package_index.md
Referenced package paths: 30
Missing targets: 0

Doc: submission_readiness_checklist.md
Referenced package paths: 20
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
Mixed subtitle capitalization warning: yes
'vs.' warning: yes
'Frontiers:' warning: yes

Warnings:
- Mixed subtitle capitalization detected after colons; choose one journal-specific rule in the final style pass.
- At least one title uses 'vs.'; confirm whether the target outlet keeps abbreviations or spells them out.
- At least one title starts with 'Frontiers:'; confirm whether that prefix is kept exactly in the target style.
```

### source_archive_status
- Status: `PASS`
- Output:
```text
Crosswalk: /Users/yuxiaoluo/.openclaw/workspace/projects/nudging/manuscript_citation_crosswalk.md
Source archive audit: /Users/yuxiaoluo/.openclaw/workspace/projects/nudging/manuscript_source_archive_audit.md
Citations checked: 12
Archived locally: 10
Missing local PDFs: 2

Missing local PDFs:
- Xiao and Benbasat (2007)
- Ebrahimi et al. (2022)
```

## Interpretation note
- Treat `PASS` here as confirmation that the current lightweight checks did not find structural package or bibliography failures.
- Treat any remaining warnings inside the individual outputs as follow-up guidance, not as automatic blockers, unless they contradict the intended submission state.
