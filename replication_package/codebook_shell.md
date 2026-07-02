# Codebook Shell

## Purpose
This file is a draft codebook scaffold for the nudging study. It is meant to become the replication package's variable-level reference once the survey is programmed and the analysis dataset is defined.

## Study-level metadata
- Study label: `Study 1 - LLM conversational nudges`
- Design: three-condition between-subject online experiment
- Conditions:
  - `1 = conversational_nudge`
  - `2 = ui_nudge`
  - `3 = control`

## Variable dictionary template

| Variable name | Label | Type | Values / coding | Source | Notes |
|---|---|---|---|---|---|
| `participant_id` | Participant identifier | ID | `TBD` | Platform export | De-identify if shared |
| `condition` | Experimental condition | Categorical | `1, 2, 3` | Random assignment | Keep stable across all scripts |
| `choice_product` | Chosen headphone option | Categorical | `TBD` | Shopping task | Anchors which product the participant later evaluates; not the headline action outcome by itself |
| `purchase_1` | Purchase likelihood item 1 | Numeric | `1-7` | Instrument | `TBD` |
| `purchase_2` | Purchase likelihood item 2 | Numeric | `1-7` | Instrument | `TBD` |
| `purchase_3` | Purchase likelihood item 3 | Numeric | `1-7` | Instrument | `TBD` |
| `decision_quality_1` | Decision quality item 1 | Numeric | `1-7` | Instrument | `TBD` |
| `decision_quality_2` | Decision quality item 2 | Numeric | `1-7` | Instrument | `TBD` |
| `decision_quality_3` | Decision quality item 3 | Numeric | `1-7` | Instrument | `TBD` |
| `personalization_1` | Personalization item 1 | Numeric | `1-7` | Instrument | `TBD` |
| `personalization_2` | Personalization item 2 | Numeric | `1-7` | Instrument | `TBD` |
| `personalization_3` | Personalization item 3 | Numeric | `1-7` | Instrument | `TBD` |
| `cogload_1` | Cognitive load item 1 | Numeric | `1-7` | Instrument | Reverse code for construct score |
| `cogload_2` | Cognitive load item 2 | Numeric | `1-7` | Instrument | Reverse code for construct score |
| `cogload_3` | Cognitive load item 3 | Numeric | `1-7` | Instrument | Reverse code for construct score |
| `confidence_1` | Choice confidence item 1 | Numeric | `1-7` | Instrument | `TBD` |
| `confidence_2` | Choice confidence item 2 | Numeric | `1-7` | Instrument | `TBD` |
| `confidence_3` | Choice confidence item 3 | Numeric | `1-7` | Instrument | `TBD` |
| `transparency_1` | Transparency item 1 | Numeric | `1-7` | Instrument | `TBD` |
| `transparency_2` | Transparency item 2 | Numeric | `1-7` | Instrument | `TBD` |
| `transparency_3` | Transparency item 3 | Numeric | `1-7` | Instrument | `TBD` |
| `trust_1` | Trust item 1 | Numeric | `1-7` | Instrument | Secondary outcome |
| `trust_2` | Trust item 2 | Numeric | `1-7` | Instrument | Secondary outcome |
| `satisfaction_1` | Satisfaction item 1 | Numeric | `1-7` | Instrument | Secondary outcome |
| `satisfaction_2` | Satisfaction item 2 | Numeric | `1-7` | Instrument | Secondary outcome |
| `mc_conversational` | Manipulation check: conversational | Numeric | `1-7` | Instrument | Diagnostic only |
| `mc_adaptive` | Manipulation check: adaptive | Numeric | `1-7` | Instrument | Diagnostic only |
| `mc_ai_role` | Manipulation check: AI role | Numeric | `1-7` | Instrument | Diagnostic only |
| `mc_visible_logic` | Manipulation check: visible logic | Numeric | `1-7` | Instrument | Diagnostic only |
| `control_familiarity` | Product-category familiarity | Numeric | `1-7` | Instrument | Covariate |
| `control_ai_use` | Prior AI-shopping use | Numeric | `TBD` | Instrument | Covariate |
| `control_ai_trust` | General trust in AI | Numeric | `1-7` | Instrument | Covariate |
| `control_nfc_*` | Need for cognition subset items | Numeric | `1-7` | Instrument | Replace `*` with final suffixes |
| `control_involvement` | Shopping involvement | Numeric | `1-7` | Instrument | Covariate |
| `attention_check` | Direct attentiveness item | Numeric | `TBD` | Instrument | Screening only |
| `completion_time` | Completion duration | Numeric | `TBD` | Platform export | Screening only |
| `duplicate_flag` | Duplicate-response flag | Binary | `0/1` | Screening workflow | Screening only |
| `included_main_sample` | Included in confirmatory sample | Binary | `0/1` | Screening workflow | Main sample indicator |

## Construct-score section
Use this section later to define the final retained constructs after reliability and dimensionality checks.

Interpretation rule:
- `choice_product` records task completion at the product-selection stage.
- `purchase_likelihood` captures willingness to act on that selected product and remains the headline action-oriented outcome.
- `decision_quality` captures whether the selected choice is experienced as sound and well justified.

| Construct score | Component items | Reverse coded? | Aggregation rule | Final retained? |
|---|---|---|---|---|
| `purchase_likelihood` | `TBD` | No | `TBD` | `TBD` |
| `decision_quality` | `TBD` | No | `TBD` | `TBD` |
| `personalization` | `TBD` | No | `TBD` | `TBD` |
| `cognitive_load_rc` | `TBD` | Yes | `TBD` | `TBD` |
| `choice_confidence` | `TBD` | No | `TBD` | `TBD` |
| `perceived_transparency` | `TBD` | No | `TBD` | `TBD` |
| `trust` | `TBD` | No | `TBD` | `TBD` |
| `satisfaction` | `TBD` | No | `TBD` | `TBD` |

## Screening flags section
Use this section later to document the exact exclusion logic that produced the main confirmatory sample.

| Flag | Definition | Values | Used in main sample? |
|---|---|---|---|
| `flag_incomplete` | `TBD` | `0/1` | `TBD` |
| `flag_duplicate` | `TBD` | `0/1` | `TBD` |
| `flag_low_effort` | `TBD` | `0/1` | `TBD` |
| `flag_attention_fail` | `TBD` | `0/1` | `TBD` |
| `flag_other_prespecified` | `TBD` | `0/1` | `TBD` |

## Maintenance rule
- Keep this file aligned with `appendix_b_measurement_instrument.md` and `appendix_c_screening_and_sample_flow.md`
- If a final variable name changes, update it here before using it in analysis scripts so the replication package retains one stable reference
