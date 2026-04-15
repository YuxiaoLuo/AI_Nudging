# Talking Shoppers Into Buying? Experimental Evidence on LLM-Driven AI Nudges

## 1. Core premise
The integration of LLMs into e-commerce platforms has created a new form of digital choice architecture: conversational AI nudging. Unlike traditional UI nudges such as recommendation badges, product rankings, or highlighted labels, LLM-based assistants influence users through interactive, adaptive, and often opaque dialogue. This project examines whether and how LLM-driven conversational nudges shape purchase decision-making differently from traditional UI-based nudges.

## 2. Problem statement
Digital nudging research has largely focused on interface-level interventions such as defaults, rankings, labels, visual salience, social proof, and recommendation cues. These mechanisms alter choice architecture by changing what users see and how options are presented. However, LLM-enabled shopping assistants do more than present options. They converse, interpret user needs, generate comparative guidance, personalize recommendations in real time, and steer users through a dynamic exchange.

This shift matters because conversational AI may not simply be a stronger version of existing recommendation cues. It may represent a qualitatively different persuasive mechanism. Compared with static UI nudges, LLM-based nudges can feel more personalized, reduce search effort, guide users through complexity, and increase decision confidence. At the same time, they may reduce transparency because users cannot easily determine why a product is recommended, what logic was used, or whether the platform’s commercial interests shaped the response.

As a result, the central question is not only whether LLM assistants increase purchase likelihood. It is whether conversational AI nudges reshape the decision process itself by changing transparency, trust, cognitive load, confidence, and ultimately decision quality.

## 3. Potential contribution
This project can contribute by showing that LLM conversational assistants are a distinct form of AI nudge rather than a simple extension of existing digital nudges. It can also identify a central design tradeoff in conversational commerce: greater personalization and reduced cognitive burden may improve decision support and increase purchase, but increased algorithmic opacity may undermine transparent and responsible choice architecture.

## 4. Working definition
**LLM-driven conversational AI nudges** are platform-mediated choice interventions delivered through interactive natural-language dialogue, where recommendations, framing, sequencing, and emphasis are generated or adapted by an LLM in ways that steer user decision processes without restricting options.

### Defining features
- conversational rather than purely visual
- interactive rather than one-shot
- adaptive rather than fixed
- algorithmically generated rather than manually scripted in full
- often opaque in underlying recommendation logic

## 5. Focal comparison
### Condition 1: LLM conversational nudge
Participants receive shopping guidance through a chatbot-style assistant that recommends, compares, frames, and steers options in natural language.

### Condition 2: Traditional UI-based nudge
Participants see static or semi-static nudges such as “best seller,” “recommended,” star ratings, or highlighted product placement.

### Condition 3: Control
Participants browse the same product environment without explicit nudging.

## 6. Candidate theoretical logic
### 6.1 Interactivity and adaptivity
Conversational AI can ask, infer, and respond. This allows it to tailor guidance dynamically, which may increase perceived personalization and fit.

### 6.2 Cognitive offloading
By summarizing options and structuring comparisons, LLM nudges may reduce information overload and cognitive effort.

### 6.3 Confidence amplification
Because the system speaks in coherent, human-like recommendations, it may increase users’ confidence in their choices even when the underlying logic is unclear.

### 6.4 Algorithmic opacity
Unlike transparent UI nudges, conversational recommendations often obscure why a product was suggested, what criteria were prioritized, and how platform incentives may shape the response.

### 6.5 Trust and persuasion tension
Users may trust the interaction more because it feels intelligent and personalized, yet this trust may rest on an opaque and potentially biased recommendation process.

## 7. Recommended mechanism model
### Independent variable
Type of nudge:
- LLM conversational nudge
- UI-based nudge
- control

### Core mediators
- perceived personalization
- cognitive load reduction
- perceived transparency
- choice confidence

### Primary dependent variables
- purchase likelihood
- perceived decision quality

### Secondary outcomes
- trust in the recommendation mechanism
- satisfaction with the decision

### Possible moderators
- AI literacy
- need for cognition
- prior trust in AI
- product involvement
- product type, utilitarian versus hedonic

### Recommended model logic
The cleanest first paper is a tradeoff model rather than an everything-model. The main claim should be that, relative to UI nudges and control, LLM conversational nudges reshape consumer choice through two opposing process routes.

**Benefit route:**
- LLM conversational nudges increase perceived personalization.
- Greater personalization reduces cognitive load by narrowing options and structuring comparison.
- Lower cognitive load increases choice confidence and should improve perceived decision quality.
- These same benefits may also increase purchase likelihood.

**Risk route:**
- LLM conversational nudges reduce perceived transparency because the recommendation logic is difficult to reconstruct.
- Lower transparency weakens informed evaluation and may place artificial weight on fluent, confident recommendations.
- Lower transparency may therefore qualify, offset, or suppress gains in decision quality even when purchase likelihood rises.

This model keeps the paper focused. It also makes the causal comparison easier to defend: LLM nudges do not merely increase persuasion. They change the balance between decision support benefits and opacity costs.

## 8. Strong framing options
### Option A: Effects on purchase and decision process
Compare whether LLM nudges increase purchase likelihood more than UI nudges, and test mediation through personalization, cognitive load, and confidence.

### Option B: Transparency tradeoff model
Argue that LLM nudges improve convenience and confidence but reduce transparency, producing a tradeoff between persuasive effectiveness and responsible platform design.

### Option C: Decision quality model
Examine whether LLM nudges increase buying but not necessarily better buying, positioning decision quality as the most important downstream outcome.

## 9. Recommended direction
Option B remains the strongest direction, but it should be sharpened into a more concrete first-paper structure.

### Recommended outcome strategy
Treat the outcomes in two tiers:

**Primary outcomes**
1. **Purchase likelihood** as the persuasion/effectiveness outcome.
2. **Perceived decision quality** as the welfare/quality outcome.

**Process measures**
- perceived personalization
- cognitive load
- perceived transparency
- choice confidence

**Secondary outcomes**
- trust in recommender
- satisfaction

This is cleaner than making trust, confidence, satisfaction, purchase, and decision quality all co-equal endpoints. Confidence works better as a downstream process outcome than as the headline contribution. Trust can be retained as an auxiliary dependent variable or robustness outcome rather than the centerpiece.

### Recommended causal story
- Compared with UI nudges, LLM conversational nudges increase perceived personalization.
- Increased personalization reduces cognitive load.
- Reduced cognitive load increases choice confidence and supports higher perceived decision quality.
- At the same time, LLM conversational nudges reduce perceived transparency.
- Reduced transparency limits users' ability to understand why products are being recommended and may weaken the quality of their final choice evaluation.
- The net result is a tradeoff: stronger purchase support and confidence, but potentially weaker transparency and more ambiguous decision quality.

## 10. Draft hypotheses structure
A defensible first-pass hypothesis set is:

**H1:** LLM conversational nudges increase perceived personalization relative to UI-based nudges and control.

**H2:** Greater perceived personalization is associated with lower cognitive load during product choice.

**H3:** Lower cognitive load is associated with higher choice confidence.

**H4:** Higher choice confidence is associated with higher perceived decision quality.

**H5:** LLM conversational nudges decrease perceived transparency relative to UI-based nudges and control.

**H6:** Lower perceived transparency is associated with lower perceived decision quality.

**H7:** LLM conversational nudges increase purchase likelihood relative to UI-based nudges and control.

**H8:** The effect of LLM conversational nudges on perceived decision quality is jointly shaped by a positive personalization-to-confidence path and a negative transparency path.

This set is compact enough to execute while still preserving the paper's core tradeoff argument.

## 11. Experimental design sketch
### Task
Use a simulated online shopping task in a moderately involving product category with meaningful comparison needs. Good candidates are headphones, skincare, running shoes, or air fryers. Headphones or skincare may be especially useful because consumers can plausibly care about both preference fit and technical tradeoffs.

### Recommended design choice
Use a **three-condition between-subject experiment**:
1. LLM conversational nudge
2. UI-based nudge
3. control

### Procedure
1. Participant receives a shopping scenario with a budget and preference goal.
2. Participant shops in one randomized condition.
3. Participant selects a product or indicates purchase likelihood.
4. Participant completes post-task scales.
5. Participant answers manipulation checks and basic controls.

### Measures
**Primary outcomes**
- purchase likelihood / purchase intention
- perceived decision quality

**Core process measures**
- perceived personalization
- cognitive load / effort
- perceived transparency
- choice confidence

**Secondary outcomes**
- trust in recommender
- satisfaction

### Manipulation checks
- degree of conversational interaction
- perceived adaptivity/personalization of the aid
- perceived AI involvement
- perceived visibility of recommendation logic

### Controls
- product category familiarity
- prior use of AI assistants for shopping
- general trust in AI
- need for cognition
- shopping involvement

## 12. Draft contribution statement
This study contributes to research on digital nudging and conversational commerce by theorizing LLM-driven conversational assistants as a distinct form of AI nudge that operates through adaptive dialogue rather than interface placement alone. It further contributes by identifying a core tradeoff in AI-mediated shopping: conversational AI can increase personalization, reduce cognitive burden, and raise purchase support, while simultaneously reducing transparency in how recommendations are generated and justified. By comparing conversational AI nudges directly with traditional UI-based nudges, the study clarifies whether LLM-based assistance is merely a stronger interface cue or a qualitatively different architecture of influence.

## 13. Immediate next steps
- convert the recommended model into a cleaner theory section
- write a formal hypotheses section from H1 to H8
- choose the shopping product category
- draft treatment materials for the three conditions
- specify the measures and analysis plan
