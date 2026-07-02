# Appendix B. Full Measurement Instrument

## Purpose
This appendix externalizes the measurement package described in the manuscript into one inspectable instrument file. It is intended as a draft appendix artifact rather than as a final survey-programming export.

## General response format
- Core evaluative items: seven-point Likert-type scale from `1 = strongly disagree` to `7 = strongly agree`
- Purchase-likelihood items: seven-point scale from `1 = very unlikely` to `7 = very likely`
- Unless noted otherwise, higher values should indicate more of the named construct after any prespecified reverse coding

## Primary outcomes

### Purchase likelihood
- Construct role: headline behavioral outcome
- Response format: seven-point unlikely-to-likely scale
- Measurement note:
  - These items are asked after the participant selects one focal product, so they capture willingness to act on that selected option rather than mere completion of the choice task
- Draft items:
  - `I would be likely to purchase the headphone option I selected.`
  - `I would seriously consider buying the headphone option I selected.`
  - `The probability that I would purchase the headphone option I selected is high.`

### Perceived decision quality
- Construct role: headline evaluative outcome
- Response format: seven-point agreement scale
- Measurement note:
  - These items evaluate whether the selected option feels well justified and appropriate, which is analytically distinct from willingness to purchase it
- Draft items:
  - `I made a high-quality decision in this shopping task.`
  - `My final choice seems well justified given the information available.`
  - `The option I selected is an appropriate choice for my needs.`

## Core process measures

### Perceived personalization
- Construct role: benefit-route mechanism
- Response format: seven-point agreement scale
- Draft items:
  - `The guidance felt tailored to my needs.`
  - `The shopping aid took my priorities into account.`
  - `The recommendation felt personalized rather than generic.`
- Source logic:
  - Adapted from the conversational-shopping personalization logic in Chung et al. (2020) and the task-fit logic in Chen et al. (2021)

### Cognitive load
- Construct role: benefit-route mechanism
- Response format: seven-point agreement scale
- Draft items:
  - `It took a lot of mental effort to make this decision.`
  - `Comparing the headphone options felt cognitively demanding.`
  - `This shopping task felt mentally taxing.`
- Reverse coding:
  - All three items are naturally negatively valenced and should be reverse-coded for interpretive consistency after reliability and dimensionality checks so higher retained scores indicate a more favorable process state
- Source logic:
  - Grounded in the decision-aid tradition where guided comparison should reduce effortful processing

### Choice confidence
- Construct role: downstream benefit-route mechanism
- Response format: seven-point agreement scale
- Draft items:
  - `I am confident that I selected the right headphone option.`
  - `I feel certain about the choice I made.`
  - `I have relatively little doubt about the option I selected.`

### Perceived transparency
- Construct role: risk-route mechanism
- Response format: seven-point agreement scale
- Draft items:
  - `I understand why this product was recommended or stood out.`
  - `The basis of the recommendation was clear to me.`
  - `I could reconstruct the main logic behind the recommendation.`
- Source logic:
  - Most directly tied to the explanation-facility and disclosure tradition represented by Wang and Benbasat (2007), Wang et al. (2018), and Wang and Wang (2019)

## Secondary outcomes

### Trust in the shopping aid
- Construct role: auxiliary outcome
- Response format: seven-point agreement scale
- Draft items:
  - `I trust the shopping aid I interacted with.`
  - `The shopping aid seemed reliable.`

### Satisfaction with the guidance process
- Construct role: auxiliary outcome
- Response format: seven-point agreement scale
- Draft items:
  - `I am satisfied with the guidance I received in this shopping task.`
  - `The guidance process worked well for me.`

## Manipulation checks
- Purpose:
  - Verify that the conditions were experienced as intended without replacing the substantive mediator constructs
- Response format: seven-point agreement scale
- Draft items:
  - `The shopping aid felt conversational.`
  - `The guidance adapted to my inputs or needs.`
  - `Artificial intelligence played a meaningful role in the guidance I received.`
  - `The logic behind the recommendation was visibly presented to me.`
- Coding note:
  - The visible-logic item sits near the transparency domain, so it should remain diagnostic rather than be treated as a substitute for perceived transparency in the main model
- Interpretation note:
  - These items are intended for condition validation and robustness context, not for routine post hoc respondent exclusion

## Control variables

### Product-category familiarity
- Purpose:
  - Capture baseline familiarity with wireless over-ear headphones
- Response format: seven-point agreement scale
- Representative item:
  - `I am familiar with wireless over-ear headphones as a product category.`

### Prior use of AI shopping assistants
- Purpose:
  - Capture baseline exposure to AI-assisted shopping tools
- Response format: seven-point agreement scale or short frequency-style adaptation if needed
- Representative item:
  - `I have used AI-based assistants or chatbots for shopping before.`

### General trust in AI
- Purpose:
  - Capture baseline receptivity to AI recommendations
- Response format: seven-point agreement scale
- Representative item:
  - `I generally trust AI systems to provide useful recommendations.`

### Need for cognition
- Purpose:
  - Provide compact dispositional adjustment for effortful engagement
- Response format:
  - Seven-point agreement scale using a short validated subset rather than ad hoc reflective items
- Draft implementation note:
  - Final item selection should use a brief validated subset and stay stable across all confirmatory models

### Shopping involvement
- Purpose:
  - Capture how important or involving the headphone choice feels
- Response format: seven-point agreement scale
- Representative item:
  - `Choosing the right headphones in this scenario feels like an important decision.`

## Data-quality screens

### Attentiveness screen
- Purpose:
  - Identify clearly inattentive respondents
- Draft item style:
  - A direct instruction item that tells the respondent to select a specified response option

### Completion thresholds
- Purpose:
  - Flag implausibly fast or incomplete responses
- Draft implementation note:
  - Thresholds should be defined in advance and treated as prespecified exclusion criteria

### Duplicate-response checks
- Purpose:
  - Remove repeated submissions before outcome analysis

## Coding and retention notes
- Aggregation rule:
  - Multi-item constructs should be aggregated only after basic reliability and dimensionality checks confirm that the retained items behave as intended
- Retention discipline:
  - The project can drop an evidently weak item if doing so preserves the intended construct and is reported transparently, but the measurement package should not expand opportunistically in response to noisy diagnostics
- Sign convention:
  - Final retained construct scores should be aligned so higher values indicate more favorable support, confidence, transparency, trust, satisfaction, and decision quality, with cognitive-load items reverse-coded accordingly
- Confirmatory use:
  - The same compact construct package should be carried across the confirmatory analyses rather than shifting batteries across tables

## What this appendix should eventually report
- Final item wording for each retained construct
- Any reverse-coding direction
- Concise reliability statistics for retained scales
- Brief dimensionality or loading evidence sufficient to show construct separability
- Any clearly reported item deletions made under the disciplined retention rule
- A short note that the forced product choice anchors what respondents evaluate, while purchase likelihood remains the main action-oriented outcome
