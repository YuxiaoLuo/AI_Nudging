# Manuscript Package Validation Report

## Purpose
This file records one lightweight validation-suite snapshot for the current manuscript package.

## Snapshot metadata
- Generated at (UTC): `2026-06-22T21:53:15+00:00`
- Repository HEAD at generation: `1055c96ac0c864aa02690ced9d2a29ac6b0e109a`

## Input fingerprints
- `manuscript_llm_ai_nudges_draft.md`: sha256 `9b68409e8332`
- `README.md`: sha256 `a42b2c896673`
- `manuscript_package_index.md`: sha256 `7c57222f1e3f`
- `submission_readiness_checklist.md`: sha256 `ec2ba1a8d220`

## Current validation target
- Repository root: `/Users/yuxiaoluo/.openclaw/workspace/projects/nudging`
- Manuscript: `/Users/yuxiaoluo/.openclaw/workspace/projects/nudging/manuscript_llm_ai_nudges_draft.md`
- Package-facing docs included in link check:
  - `README.md`
  - `manuscript_package_index.md`
  - `submission_readiness_checklist.md`

## Validation results
### package_links
- Status: `PASS`
- Output:
```text
Doc: README.md
Referenced package paths: 20
Missing targets: 0

Doc: manuscript_package_index.md
Referenced package paths: 27
Missing targets: 0

Doc: submission_readiness_checklist.md
Referenced package paths: 17
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

## Interpretation note
- Treat `PASS` here as confirmation that the current lightweight checks did not find structural package or bibliography failures.
- Treat any remaining warnings inside the individual outputs as follow-up guidance, not as automatic blockers, unless they contradict the intended submission state.
