# 01 Screening Shell

## Responsibility
Create the main confirmatory sample from the raw survey export using only prespecified quality rules.

## Inputs
- raw response export
- duplicate-response identifiers
- completion-time fields
- attentiveness item
- any platform-side status flags

## Main steps
1. Load raw responses.
2. Preserve the original raw row count.
3. Flag incomplete responses under the prespecified completion rule.
4. Flag duplicate submissions under the prespecified duplicate rule.
5. Flag implausibly fast or low-effort responses under the prespecified threshold.
6. Flag attentiveness failures if the exclusion rule is part of the final protocol.
7. Create `included_main_sample` as the confirmatory sample indicator.
8. Produce the counts needed for `appendix_c_screening_and_sample_flow.md`.

## Outputs
- processed dataset with screening flags
- sample-flow counts by condition
- final main-sample indicator

## Guardrails
- Do not create outcome-contingent exclusions.
- Keep all flags in the dataset even when excluded rows are dropped from later analysis files.
