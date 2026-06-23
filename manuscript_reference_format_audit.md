# Manuscript Reference Format Audit

## Purpose
This file records the current lightweight formatting state of the manuscript references section. The goal is to separate `structural bibliography consistency` from the narrower set of `target-journal style choices` that still remain.

## Current audit target
- Source file:
  - `manuscript_llm_ai_nudges_draft.md`
- Audit date:
  - `2026-06-23`
- Audit helper:
  - `replication_package/scripts/check_reference_formatting.py`

## Current structural status
- The draft currently contains 12 reference entries.
- All 12 entries currently use full `https://doi.org/` URLs.
- No duplicate DOI URLs are currently flagged.
- The first-pass alphabetical ordering issue in the references is not currently flagged.
- The current bibliography therefore passes the lightweight structural-format audit.

## Current warning flags
- Alphabetical-order warning: `no`
- Mixed subtitle capitalization warning: `yes`
- `vs.` warning: `yes`
- `Frontiers:` warning: `yes`

## Current remaining warnings
1. Mixed subtitle capitalization detected after colons; choose one journal-specific rule in the final style pass.
2. At least one title uses 'vs.'; confirm whether the target outlet keeps abbreviations or spells them out.
3. At least one title starts with 'Frontiers:'; confirm whether that prefix is kept exactly in the target style.

## Flagged entries
- Mixed subtitle-capitalization examples:
  - `Understanding automated conversational agent as a decision aid: matching agent's conversation with customer's shopping task.`
  - `Effects of personalization and social role in voice shopping: An experimental study on product recommendation by a conversational voice agent.`
  - `Conversational commerce: Do biased choices offered by voice assistants' technology constrain its appropriation?`
  - `The impact of trust and recommendation quality on adopting interactive and non-interactive recommendation agents: A meta-analysis.`
  - `Consumer decision making in online shopping environments: The effects of interactive decision aids.`
  - `Frontiers: Machines vs. humans: The impact of artificial intelligence chatbot disclosure on customer purchases.`
  - `The power of rankings: Quantifying the effect of rankings on online consumer search and purchase decisions.`
  - `Recommendation agents for electronic commerce: Effects of explanation facilities on trusting beliefs.`
  - `Effects of recommendation neutrality and sponsorship disclosure on trust vs. distrust in online recommendation agents: Moderating role of explanations for organic recommendations.`
  - `Effects of sponsorship disclosure on perceived integrity of biased recommendation agents: Psychological contract violation and knowledge-based trust perspectives.`
  - `E-commerce product recommendation agents: Use, characteristics, and impact.`
- `vs.` examples:
  - `Frontiers: Machines vs. humans: The impact of artificial intelligence chatbot disclosure on customer purchases.`
  - `Effects of recommendation neutrality and sponsorship disclosure on trust vs. distrust in online recommendation agents: Moderating role of explanations for organic recommendations.`
- `Frontiers:` examples:
  - `Frontiers: Machines vs. humans: The impact of artificial intelligence chatbot disclosure on customer purchases.`

## Interpretation
- These warnings do **not** indicate citation-list misalignment.
- These warnings do **not** require reopening the manuscript's theory or citation set.
- They indicate only that the final bibliography pass still needs one explicit target-journal style decision.

## What to do next
- If the target outlet prefers sentence case:
  - normalize all titles and subtitles in one bounded pass while preserving proper nouns and any required article prefixes.
- If the target outlet prefers title case:
  - convert all titles and subtitles in one pass rather than editing only the flagged entries.
- Before making that pass:
  - keep the citation set frozen
  - confirm citation/reference alignment with `manuscript_reference_audit.md`
  - use `manuscript_reference_cleanup_notes.md` to keep the normalization pass bounded

## Related files
- `manuscript_reference_audit.md`
- `manuscript_reference_cleanup_notes.md`
- `manuscript_citation_crosswalk.md`
- `submission_readiness_checklist.md`

## Practical use
- Use this file when deciding whether the next bibliography task is `style normalization` versus `PDF retrieval`.
- Refresh this audit after any future reference-list edits that change title wording, ordering, DOI presentation, or validation logic.
