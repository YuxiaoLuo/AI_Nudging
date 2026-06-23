# Manuscript Package Validation Freshness Report

## Purpose
This file records whether the saved manuscript-package validation snapshot still matches the current repository state.

## Freshness metadata
- Generated at (UTC): `2026-06-23T15:22:39+00:00`
- Repository root: `/Users/yuxiaoluo/.openclaw/workspace/projects/nudging`
- Validation snapshot checked: `/Users/yuxiaoluo/.openclaw/workspace/projects/nudging/manuscript_package_validation_report.md`
- Saved snapshot HEAD: `20a171f52104ab247e966144403116a5f7b92af3`
- Current repository HEAD: `af971ce3919fa473b98e63c7687813f99f43f1fe`
- Repository HEAD drift since snapshot: `YES`

## Tracked fingerprint comparison
- `manuscript_llm_ai_nudges_draft.md`: `MATCH` (saved `c2774c9f0090`, current `c2774c9f0090`)
- `README.md`: `MATCH` (saved `57fc50feedfb`, current `57fc50feedfb`)
- `manuscript_package_index.md`: `MATCH` (saved `98c9b30fefa7`, current `98c9b30fefa7`)
- `manuscript_package_open_items.md`: `MATCH` (saved `4a071a3d02d4`, current `4a071a3d02d4`)
- `submission_readiness_checklist.md`: `CHANGED` (saved `c5f1a8547cf9`, current `285df2653e9b`)
- `replication_package/README.md`: `MATCH` (saved `da6d4ec4db21`, current `da6d4ec4db21`)
- `manuscript_reference_audit.md`: `MATCH` (saved `f2ea9930a433`, current `f2ea9930a433`)
- `manuscript_reference_format_audit.md`: `MATCH` (saved `3b2eae652354`, current `3b2eae652354`)
- `manuscript_citation_crosswalk.md`: `MATCH` (saved `c1f019b33366`, current `c1f019b33366`)
- `literature/download_log.md`: `MATCH` (saved `6184e6252288`, current `6184e6252288`)
- `manuscript_source_archive_audit.md`: `MATCH` (saved `b7bd4c564cb2`, current `b7bd4c564cb2`)
- `replication_package/scripts/run_validation_suite.py`: `MATCH` (saved `4fae2c5ea230`, current `4fae2c5ea230`)
- `replication_package/scripts/check_validation_snapshot_freshness.py`: `MATCH` (saved `c62456750aff`, current `c62456750aff`)
- `replication_package/scripts/check_package_links.py`: `MATCH` (saved `efc91ccac4f2`, current `efc91ccac4f2`)
- `replication_package/scripts/check_reference_alignment.py`: `MATCH` (saved `dd7bbef31ea6`, current `dd7bbef31ea6`)
- `replication_package/scripts/check_reference_formatting.py`: `MATCH` (saved `b5f349592bf5`, current `b5f349592bf5`)
- `replication_package/scripts/check_source_archive_status.py`: `MATCH` (saved `2fd4f177d359`, current `2fd4f177d359`)
- `replication_package/scripts/check_placeholder_text.py`: `MATCH` (saved `a35d6125add0`, current `a35d6125add0`)

## Result
- Snapshot freshness: `STALE`
- Action: rerun `replication_package/scripts/run_validation_suite.py --report-md manuscript_package_validation_report.md` before relying on the saved snapshot.
