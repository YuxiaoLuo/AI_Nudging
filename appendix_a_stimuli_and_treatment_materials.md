# Appendix A. Full Stimuli and Treatment Materials

## Purpose
This appendix consolidates the study stimuli and treatment logic into one inspectable file. It is intended as a draft appendix artifact that matches the current manuscript design rather than as a final survey-platform export.

## Shopping scenario
Participants read the following scenario before entering the shopping environment:

`You need a pair of wireless over-ear headphones for commuting, work, and casual listening. Your budget cap is $180. Please review the available options and select the product you would choose.`

## Product set
The study uses six fictional but plausible headphone options to reduce brand-specific confounds while keeping the task realistic. The same product set appears in all three conditions.

### Shared attribute columns
- price
- battery life
- weight
- active noise cancellation
- microphone quality
- comfort rating
- user rating

### Product profiles

#### Auralite A1
- Positioning: value-focused option
- Approximate price: `$89`
- Key profile:
  - lower price point
  - weaker active noise cancellation
  - weaker call quality

#### Auralite B3
- Positioning: battery-life option
- Approximate price: `$149`
- Key profile:
  - `50` hours of playback
  - moderate comfort

#### NordSound C5
- Positioning: noise-cancellation option
- Approximate price: `$179`
- Key profile:
  - strongest commuting-oriented noise cancellation
  - heavier frame

#### NordSound D2
- Positioning: call-quality option
- Approximate price: `$159`
- Key profile:
  - strongest microphone score
  - average battery life

#### VeroWave H4
- Positioning: comfort-focused option
- Approximate price: `$169`
- Key profile:
  - best comfort rating
  - low weight
  - only midrange microphone quality

#### VeroWave M6
- Positioning: balanced focal option
- Approximate price: `$139`
- Key profile:
  - solid but non-dominant performance across sound quality, comfort, battery life, microphone quality, and active noise cancellation
- Design role:
  - remains the focal recommendation in both treatment conditions so substantive recommendation content is held constant while the mode of guidance changes

## Condition structure
The experiment varies only the mode of guidance while holding the scenario, product set, and focal recommendation constant across the two treatment conditions.

### Condition 1. Conversational-nudge condition
- Interface logic:
  - a semi-structured shopping assistant appears alongside or above the same six-product set
- Functional role:
  - asks a short sequence of preference questions
  - recommends `VeroWave M6`
  - briefly compares `VeroWave M6` with `NordSound C5` and `Auralite B3`
- Core design intent:
  - make the guidance feel adaptive and advisory while preserving stable treatment content

### Condition 2. UI-based nudge condition
- Interface logic:
  - the same focal option, `VeroWave M6`, is positioned first
  - `VeroWave M6` carries a `Best Match` badge
  - a short static recommendation note accompanies the focal option
- Example recommendation note:
  - `Balanced choice for commuting, work, and everyday listening`
- Core design intent:
  - present guidance as a static interface cue rather than an adaptive exchange

### Condition 3. Control condition
- Interface logic:
  - participants see the same six products without explicit recommendation cues
- Core design intent:
  - preserve the shopping environment while removing guided recommendation signals

## Conversational assistant sequence
The conversational treatment remains semi-structured rather than fully open ended. The assistant asks brief questions that create the impression of adaptivity without introducing uncontrolled content variation.

### Assistant question 1
`Which headphone attribute matters most to you: sound quality, comfort, battery life, call quality, or noise cancellation?`

### Assistant question 2
`What will be your main use context most of the time?`

### Assistant question 3
`Is staying comfortably under budget more important than maximizing one feature?`

## Conversational recommendation script
After the short preference exchange, the assistant delivers the following recommendation:

`Based on what you said, I would lean toward the VeroWave M6. It stays comfortably under your budget, performs well across sound, comfort, and battery life, and looks like the most balanced fit for commuting and daily use. If your top priority were maximum noise cancellation, the NordSound C5 would be stronger, but it is heavier and costs more. If battery life mattered above everything else, the Auralite B3 would be a better fit, but it gives up some overall balance.`

## UI-based nudge wording
The UI-based treatment presents the same focal product without dialogue.

### Badge
`Best Match`

### Static recommendation note
`Balanced choice for commuting, work, and everyday listening`

## Shared treatment guardrails
- The same six products appear in every condition
- The same focal recommendation, `VeroWave M6`, anchors both treatment conditions
- The conversational treatment differs from the UI treatment in guidance mode rather than recommendation content
- The control condition preserves the same shopping environment without explicit recommendation cues

## What this appendix should eventually include in final form
- the exact scenario text shown to participants
- the full product-display grid as rendered in the study
- a representative screenshot or clean mockup of the conversational condition
- a representative screenshot or clean mockup of the UI-based condition
- any final formatting details needed to match the survey or experimental interface
