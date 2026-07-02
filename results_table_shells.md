# Results Table Shells

## Purpose
This file converts the manuscript's promised main-text results tables into concrete shells that can later be populated with estimates. The goal is to keep the confirmatory evidence hierarchy explicit before data collection and analysis outputs exist.

## Table 1. Descriptive statistics and correlations

### Purpose
- Report construct means, standard deviations, and correlations before or alongside the structural results
- Give readers a compact view of the support-route and transparency-route variables before the path estimates

### Shell

| Variable | Mean | SD | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1. Purchase likelihood | `TBD` | `TBD` | `--` |  |  |  |  |  |  |  |
| 2. Perceived decision quality | `TBD` | `TBD` | `TBD` | `--` |  |  |  |  |  |  |
| 3. Perceived personalization | `TBD` | `TBD` | `TBD` | `TBD` | `--` |  |  |  |  |  |
| 4. Cognitive load (reverse coded) | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | `--` |  |  |  |  |
| 5. Choice confidence | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | `--` |  |  |  |
| 6. Perceived transparency | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | `--` |  |  |
| 7. Trust | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | `--` |  |
| 8. Satisfaction | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | `--` |

### Notes
- Keep the confirmatory core constructs visually central even if trust and satisfaction remain in the same table
- Treat `purchase likelihood` as the main action-oriented outcome and `perceived decision quality` as the evaluative tradeoff endpoint when discussing the correlation pattern
- Add significance markers only if the target journal expects them

## Table 2. Headline treatment effects on primary outcomes

### Purpose
- Keep the central conversational-versus-UI comparison visible
- Present both purchase likelihood and perceived decision quality as the headline outcomes

### Shell

| Outcome | Conversational mean (SD) | UI-based nudge mean (SD) | Control mean (SD) | Conversational vs. UI estimate | Conversational vs. control estimate | 95% CI | Effect size | Covariates included? |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Purchase likelihood | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` |
| Perceived decision quality | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` |

### Notes
- The conversational-versus-UI comparison should remain visibly central rather than being buried inside an omnibus test
- Read the purchase-likelihood row as the headline willingness-to-act outcome, not as a substitute for the fuller decision-quality mechanism test
- If the main text keeps only one effect-size column, retain the conversational-versus-UI effect size first

## Table 3. Mechanism-path results

### Purpose
- Report the support and inspectability pathways in the order implied by the theory
- Distinguish total effects, indirect effects, and any residual direct effects clearly

### Shell A. Condition-to-mechanism contrasts

| Dependent variable | Conversational vs. UI estimate | Conversational vs. control estimate | 95% CI | Note |
|---|---:|---:|---:|---|
| Perceived personalization | `TBD` | `TBD` | `TBD` | Benefit-route entry |
| Perceived transparency | `TBD` | `TBD` | `TBD` | Risk-route entry |

### Shell B. Path estimates

| Path | Estimate | 95% CI | Interpretation note |
|---|---:|---:|---|
| Perceived personalization -> cognitive load (reverse coded) | `TBD` | `TBD` | Support simplification route |
| Cognitive load (reverse coded) -> choice confidence | `TBD` | `TBD` | Confidence-building route |
| Choice confidence -> perceived decision quality | `TBD` | `TBD` | Positive evaluative route |
| Perceived transparency -> perceived decision quality | `TBD` | `TBD` | Inspectability route |
| Conversational nudge -> purchase likelihood (direct) | `TBD` | `TBD` | Direct behavioral path |
| Conversational nudge -> perceived decision quality (residual direct effect, if retained) | `TBD` | `TBD` | Interpret cautiously |

### Shell C. Indirect effects

| Indirect effect | Estimate | 95% CI | Note |
|---|---:|---:|---|
| Conversational nudge -> personalization -> cognitive load -> confidence -> decision quality | `TBD` | `TBD` | Support-route indirect effect |
| Conversational nudge -> transparency -> decision quality | `TBD` | `TBD` | Inspectability-route indirect effect |

### Notes
- Keep the mechanism table disciplined: the fuller mediated tradeoff is evaluated through perceived decision quality, not by forcing the same chain to account for every purchase-likelihood movement
- If a direct conversational-nudge effect on purchase likelihood remains, report it as a behavioral consequence of guidance fluency and reduced friction rather than as proof that decision quality improved

## Table 4. Secondary outcomes and compact robustness checks

### Purpose
- Keep secondary outcomes and bounded robustness evidence visible without letting them displace the confirmatory core

### Shell A. Secondary outcomes

| Outcome | Conversational mean (SD) | UI-based nudge mean (SD) | Control mean (SD) | Conversational vs. UI estimate | 95% CI | Note |
|---|---:|---:|---:|---:|---:|---|
| Trust | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | Secondary only |
| Satisfaction | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | Secondary only |

### Shell B. Compact robustness checks

| Robustness variant | N | Purchase-likelihood conclusion preserved? | Decision-quality conclusion preserved? | Note |
|---|---:|---|---|---|
| Main confirmatory sample | `TBD` | `TBD` | `TBD` | Reference row |
| Variant 1 | `TBD` | `TBD` | `TBD` | Narrower screen or coding choice |
| Variant 2 | `TBD` | `TBD` | `TBD` | Sensitivity only if needed |

### Notes
- Preserve the same inferential split here: robustness should show whether the purchase-likelihood conclusion and the decision-quality conclusion each remain stable, not collapse them into one generic `main effect preserved` statement

## Usage notes
- These shells are not a substitute for the appendices; they are the planned main-text table layer
- If a target journal later forces a different table merge or split, revise this file first so the package still has one explicit reporting map
