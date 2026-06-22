# 02 Constructs Shell

## Responsibility
Score the retained constructs from the screened sample and document item handling transparently.

## Inputs
- screened dataset from `01_screening`
- final item map from `appendix_b_measurement_instrument.md`
- codebook variable names from `../codebook_shell.md`

## Main steps
1. Restrict to the main confirmatory sample for confirmatory scoring outputs.
2. Reverse code the cognitive-load items under the fixed sign convention.
3. Check that the retained items match the intended construct map.
4. Compute construct scores for:
   - purchase likelihood
   - perceived decision quality
   - perceived personalization
   - cognitive load (reverse coded)
   - choice confidence
   - perceived transparency
   - trust
   - satisfaction
5. Output compact reliability and separability summaries for Appendix D.
6. Output descriptive means, standard deviations, and correlations for Table 1.

## Outputs
- construct-scored analysis dataset
- reliability/separability summary objects
- descriptive table inputs

## Guardrails
- Do not proliferate substitute measures because of noisy diagnostics.
- Record any dropped item decisions explicitly before recomputing the retained construct.
