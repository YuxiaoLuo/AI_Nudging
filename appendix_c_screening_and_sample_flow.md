# Appendix C. Screening and Sample-Flow Details

## Purpose
This appendix externalizes the screening and sample-flow logic already promised in the manuscript into one inspectable template. It is intended as a draft appendix artifact that can later be populated with realized counts once data collection is complete.

## Reporting principles
- Report the sample flow transparently from raw collection through final analyzable sample
- Keep one clearly defined primary screened sample for the headline analyses
- Label any narrower or alternative screening definitions explicitly as robustness variants rather than folding them into the main evidentiary frame
- Preserve the same condition labels throughout:
  - conversational nudge
  - UI-based nudge
  - control

## Planned sample-size frame
- Target completed responses:
  - roughly `450` to `600`
- Intended analyzable cell size after ordinary quality screening:
  - roughly `150` to `200` per condition
- Design note:
  - recruitment should be set high enough to preserve adequate post-screening cell sizes for the planned conversational-versus-UI contrast and the main process-path analyses

## Prespecified quality checks

### 1. Incomplete responses
- Rule:
  - remove responses that do not reach the end of the core post-task instrument or that leave required central outcome/process sections unusably incomplete
- What to report:
  - number removed overall
  - number removed by condition if random assignment occurred before attrition

### 2. Duplicate responses
- Rule:
  - remove repeated submissions under the prespecified duplication protocol
- What to report:
  - how duplicates were identified
  - number of records removed
  - which retained record was kept when duplicates were resolved

### 3. Minimum-effort or implausibly fast responses
- Rule:
  - remove responses that fail prespecified completion-threshold standards or otherwise clearly indicate low-effort completion under the study's preregistered logic
- What to report:
  - threshold definition
  - number removed overall
  - whether the threshold was fixed before outcome analysis

### 4. Direct attentiveness-screen failures
- Rule:
  - remove responses that fail the direct attentiveness item if the exclusion rule is prespecified in the final protocol
- What to report:
  - exact attentiveness criterion
  - number removed

### 5. Other prespecified disqualifications
- Rule:
  - include only if the final protocol defines additional up-front exclusions, such as platform-side invalidation or unusable technical completion
- What to report:
  - criterion name
  - rationale
  - number removed

## Primary sample-flow table template

| Stage | Overall N | Conversational nudge | UI-based nudge | Control | Notes |
|---|---:|---:|---:|---:|---|
| Responses collected | `TBD` | `TBD` | `TBD` | `TBD` | Raw total before exclusions |
| Removed: incomplete responses | `TBD` | `TBD` | `TBD` | `TBD` | Core-post-task incompletion |
| Removed: duplicate responses | `TBD` | `TBD` | `TBD` | `TBD` | Prespecified duplicate rule |
| Removed: minimum-effort / implausibly fast responses | `TBD` | `TBD` | `TBD` | `TBD` | Completion-threshold screen |
| Removed: attentiveness failures | `TBD` | `TBD` | `TBD` | `TBD` | Direct instruction item |
| Removed: other prespecified disqualifications | `TBD` | `TBD` | `TBD` | `TBD` | Only if applicable |
| Final analyzable sample | `TBD` | `TBD` | `TBD` | `TBD` | Main confirmatory sample |

## Screening-rule narrative template
Use a short prose block alongside the table that follows this logic:

`We collected [TBD] responses. Prespecified quality screening removed [TBD] incomplete responses, [TBD] duplicate submissions, [TBD] implausibly fast or minimum-effort responses, and [TBD] attentiveness-screen failures, leaving a final analyzable sample of [TBD] participants ([TBD] conversational, [TBD] UI-based nudge, [TBD] control). These rules were fixed before outcome analysis and applied consistently across conditions.`

## Main-sample definition
- Name:
  - primary screened sample
- Definition:
  - the one sample carried through the headline outcome tests and the confirmatory process/path analyses
- Reporting rule:
  - use this same sample definition across the main results unless a clearly labeled model-specific exception is unavoidable and justified

## Alternative-screening robustness template
If secondary analyses use a narrower sample or alternative coding rule, present them in a compact supplemental table rather than blending them into the main sample definition.

| Variant | N | Conversational nudge | UI-based nudge | Control | Difference from main sample | Intended role |
|---|---:|---:|---:|---:|---|---|
| Main confirmatory sample | `TBD` | `TBD` | `TBD` | `TBD` | Baseline screened sample | Headline evidence |
| Robustness variant 1 | `TBD` | `TBD` | `TBD` | `TBD` | Narrower threshold or coding rule | Robustness only |
| Robustness variant 2 | `TBD` | `TBD` | `TBD` | `TBD` | Additional sensitivity restriction | Robustness only |

## Condition-balance reporting template
The manuscript specifies descriptive balance reporting by condition rather than opportunistic randomization significance testing. This appendix can house a compact descriptive table if needed.

Suggested variables:
- product-category familiarity
- prior use of AI shopping assistants
- general trust in AI
- need for cognition subset score
- shopping involvement

Suggested table structure:

| Variable | Conversational nudge mean (SD) | UI-based nudge mean (SD) | Control mean (SD) | Notes |
|---|---:|---:|---:|---|
| Product-category familiarity | `TBD` | `TBD` | `TBD` | Descriptive only |
| Prior AI-shopping use | `TBD` | `TBD` | `TBD` | Descriptive only |
| General trust in AI | `TBD` | `TBD` | `TBD` | Descriptive only |
| Need for cognition subset | `TBD` | `TBD` | `TBD` | Descriptive only |
| Shopping involvement | `TBD` | `TBD` | `TBD` | Descriptive only |

## Missing-data reporting template
- Core rule:
  - report any residual item missingness transparently rather than absorbing it silently into shifting model samples
- What to document:
  - proportion of missingness on core retained constructs
  - whether the confirmatory analyses use a complete-case sample
  - whether any secondary remedy was used only because the observed missingness pattern made it necessary

Suggested short reporting block:

`Residual item missingness on the retained core constructs was [TBD]. The confirmatory analyses were estimated on a [TBD] sample under one consistent missing-data rule. Any alternative missing-data handling, if used, is reported only as a secondary robustness check.`

## What this appendix should eventually contain in final form
- realized counts at each screening stage
- final analyzable sample overall and by condition
- exact threshold definitions used in the final preregistered workflow
- any bounded robustness variants of the screening logic
- descriptive balance information by condition if the main text keeps that summary very compact
