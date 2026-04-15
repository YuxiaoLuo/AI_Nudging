# Talking Shoppers Into Buying? Experimental Evidence on LLM-Driven AI Nudges

## 1. Core premise
The integration of LLMs into e-commerce platforms has created a new form of digital choice architecture: conversational AI nudging. Unlike traditional UI nudges such as recommendation badges, product rankings, or highlighted labels, LLM-based assistants influence users through interactive, adaptive, and often opaque dialogue. This project examines whether and how LLM-driven conversational nudges shape purchase decision-making differently from traditional UI-based nudges.

## 2. Problem statement
Digital nudging research has largely focused on interface-level interventions such as defaults, rankings, labels, visual salience, social proof, and recommendation cues. These mechanisms alter choice architecture by changing what users see and how options are presented. Recommendation research has further shown that online recommendations can influence consumer choice, while recommendation-agent research has highlighted the importance of explanations, neutrality, disclosure, and trust. However, LLM-enabled shopping assistants do more than present options. They converse, interpret user needs, generate comparative guidance, personalize recommendations in real time, and steer users through a dynamic exchange.

This shift matters because conversational AI may not simply be a stronger version of existing recommendation cues. It may represent a qualitatively different persuasive mechanism. Compared with static UI nudges, LLM-based nudges can feel more personalized, reduce search effort, guide users through complexity, and increase decision confidence. At the same time, they may reduce transparency because users cannot easily determine why a product is recommended, what logic was used, or whether the platform’s commercial interests shaped the response.

As a result, the central question is not only whether LLM assistants increase purchase likelihood. It is whether conversational AI nudges reshape the decision process itself by changing transparency, cognitive load, confidence, and ultimately perceived decision quality in ways that established interface nudges and prior recommendation mechanisms do not fully explain.

## 3. Potential contribution
This project can contribute by showing that LLM conversational assistants are a distinct form of AI nudge rather than a simple extension of existing digital nudges. It can also identify a central design tradeoff in conversational commerce: greater personalization and reduced cognitive burden may improve decision support and increase purchase, but increased algorithmic opacity may undermine transparent and responsible choice architecture. In that sense, the paper is not just about whether AI nudges work. It is about why conversational AI changes the balance between decision support and inspectability differently from rankings, badges, and classic recommendation agents.

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

## 6. Theoretical logic
### 6.1 Why conversational AI should not be treated as just another interface cue
Prior digital nudging research has largely examined interventions that operate through the interface itself, such as rankings, labels, salience cues, defaults, and recommendation badges. These mechanisms alter consumer behavior primarily by influencing attention allocation, search order, and comparison efficiency (Häubl & Trifts 2000; Ursu 2018). Even when such cues are algorithmically generated, they are encountered as relatively static design features rather than as adaptive advisory processes. Related recommendation research further shows that online product recommendations can influence consumer choice (Senecal & Nantel 2004), while recommendation-agent research demonstrates that explanation facilities, sponsorship disclosure, and perceived neutrality shape trust and evaluation of advisory systems (Wang & Benbasat 2007; Wang et al. 2018; Wang & Wang 2019).

However, these literatures do not fully explain LLM conversational nudges. LLM-based assistants do not merely highlight, rank, or label options. They can solicit preferences, ask follow-up questions, summarize tradeoffs, and adapt guidance across multiple turns. In that sense, they are closer to a hybrid of recommendation agent, decision aid, and conversational advisor than to a conventional interface nudge. Because the mechanism of influence is dialogic rather than purely visual, conversational AI should shape not only what consumers notice, but also how they experience support, effort, certainty, and understanding during the choice process.

### 6.2 Personalization as the core benefit route
A central advantage of conversational AI is its capacity to make guidance feel tailored to the consumer's stated goals, constraints, and preferences. Because the system can gather richer input than a static badge or ranking and respond in natural language, consumers should perceive the recommendation as more individualized and context-sensitive. This matters theoretically because perceived personalization captures more than mere relevance. It reflects the extent to which the consumer experiences the guidance as responsive to their own situation rather than as a generic platform signal. In recommendation settings, such tailoring should make advice feel more useful and easier to act upon.

### 6.3 Cognitive load reduction through structured guidance
Perceived personalization should have downstream consequences for cognitive effort. When consumers face many options, attributes, and tradeoffs, decision making becomes effortful and mentally taxing. Conversational AI may reduce that burden by filtering the option set, structuring comparison, and translating complex information into a more manageable decision narrative. In this way, personalization is not only persuasive. It also functions as a mechanism of decision simplification. This distinguishes conversational guidance from static interface nudges, which may redirect attention but often do less to integrate and interpret tradeoffs on the consumer's behalf. Accordingly, higher perceived personalization should reduce the cognitive load associated with product choice.

### 6.4 Confidence amplification in AI-assisted choice
As cognitive burden declines and guidance feels more tailored, consumers should become more confident in the option they are considering. Confidence is especially relevant in shopping environments characterized by attribute complexity and incomplete consumer knowledge. When the choice process feels manageable and the recommendation appears coherent, consumers should feel more certain that they are arriving at an acceptable decision. At the same time, confidence is not conceptually identical to decision quality. Confidence refers to certainty in the selected option, whereas perceived decision quality captures the broader evaluative judgment that the final decision is sound, appropriate, and well justified. In the present model, confidence is therefore best understood as a downstream consequence of the benefit route rather than as a substitute for evaluative quality.

### 6.5 Transparency as the core risk route
The same properties that make conversational AI helpful may also make it difficult to scrutinize. Unlike UI nudges, which often leave visible traces of how a product is highlighted or ranked, conversational recommendations can obscure the basis of advice. Consumers may not know which attributes were prioritized, how tradeoffs were weighted, whether platform incentives shaped the recommendation, or whether the same advice would have emerged under slightly different prompts. This opacity matters because it reduces the reconstructability of the choice architecture. Prior recommendation-agent research suggests that explanation facilities, sponsorship disclosure, and perceived integrity influence how advisory systems are evaluated (Wang & Benbasat 2007; Wang et al. 2018; Wang & Wang 2019). Building on that logic, perceived transparency in the present project should be understood as the extent to which the recommendation basis feels both understandable and reconstructable after the fact.

### 6.6 The tradeoff at the center of the paper
Taken together, the core theoretical claim is that LLM conversational nudges create a benefit-risk tradeoff. On one side, conversational AI should increase perceived personalization, reduce cognitive load, and raise confidence in choice. On the other side, it should reduce perceived transparency in how recommendations are generated and justified. This combination makes conversational AI more than a stronger recommendation badge. It represents a distinct architecture of influence in which the consumer may feel better supported while simultaneously becoming less able to inspect the basis of that support. The contribution of the paper therefore lies not merely in showing that conversational AI can be effective, but in showing that its effectiveness may be inseparable from a new opacity problem in digital choice architecture.

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
The cleanest first paper is a tradeoff model rather than an everything-model. The main claim should be that, relative to UI nudges and control, LLM conversational nudges reshape consumer choice through two opposing process routes. The value of this structure is that it maps the manuscript onto a compact anchor set rather than requiring a sprawling review: decision-aid and ranking research for the baseline, recommendation-effect research for influence on choice, recommendation-agent explanation and disclosure research for transparency concerns, and conversational decision-aid work for adaptive guidance.

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

## 10. Hypotheses development
The model implies that LLM conversational nudges influence shopping decisions through two competing routes. The first route captures decision-support benefits, beginning with stronger perceived personalization and flowing through lower cognitive load and higher confidence. The second route captures opacity costs, in which conversational guidance reduces perceived transparency and thereby complicates evaluation of the final choice. Consistent with the scientific writing direction of the project, the hypotheses below are stated as theory-linked predictions rather than as isolated causal claims.

### 10.1 LLM conversational nudges and perceived personalization
Compared with UI nudges, conversational AI can ask follow-up questions, incorporate stated preferences, and present advice in language that appears tailored to the shopper's goals. This should make the recommendation process feel more individualized and context-sensitive than a generic badge, ranking, or highlight. Because the consumer experiences the system as responding to their situation rather than merely presenting a static signal, perceived personalization should be higher in the conversational condition.

**H1:** Relative to UI-based nudges and control, LLM conversational nudges increase perceived personalization.

### 10.2 Perceived personalization and cognitive load
When recommendations feel tailored to the consumer's goals, the consumer should expend less effort sorting through irrelevant alternatives and reconciling competing product attributes. Personalized guidance helps simplify the decision environment by narrowing the set of plausible options and making tradeoffs easier to interpret. As a result, stronger perceived personalization should reduce the cognitive load associated with product choice.

**H2:** Greater perceived personalization is associated with lower cognitive load during product choice.

### 10.3 Cognitive load and choice confidence
Lower cognitive burden should make consumers feel more capable of arriving at a satisfactory decision. When the choice process feels manageable rather than overwhelming, consumers can more readily commit to an option and feel assured about the quality of their evaluation. Reduced cognitive load therefore should translate into stronger confidence in the chosen option.

**H3:** Lower cognitive load is associated with higher choice confidence.

### 10.4 Choice confidence and perceived decision quality
Consumers often judge decision quality not only by objective choice outcomes but also by whether the final decision feels justified, well considered, and appropriate for their goals. Confidence serves as an important subjective indicator that the consumer has reached such a decision, but it is not identical to perceived decision quality. A consumer can feel certain about a choice without necessarily believing the decision process was fully sound, and the present model therefore treats confidence as an input into, rather than a substitute for, decision-quality judgments. Accordingly, higher confidence in the chosen option should be associated with higher perceived decision quality.

**H4:** Higher choice confidence is associated with higher perceived decision quality.

### 10.5 LLM conversational nudges and perceived transparency
Although conversational AI can feel helpful and personalized, it can also obscure how recommendations are produced. Unlike UI nudges, which often provide visible signals such as rankings, labels, or badges, conversational advice is generated through a less observable reasoning process. Consumers may therefore find it harder to infer why a product was suggested, what criteria guided the advice, or how platform interests may have influenced the recommendation. Relative to UI nudges and control, conversational nudges should therefore reduce perceived transparency.

**H5:** Relative to UI-based nudges and control, LLM conversational nudges decrease perceived transparency.

### 10.6 Perceived transparency and perceived decision quality
When consumers cannot understand the basis of a recommendation, they may feel less able to evaluate whether the final choice is genuinely well founded. Reduced transparency limits their ability to reconstruct the decision process, assess the appropriateness of the recommendation, and detect possible bias or missing considerations. For that reason, lower perceived transparency should reduce perceived decision quality.

**H6:** Lower perceived transparency is associated with lower perceived decision quality.

### 10.7 LLM conversational nudges and purchase likelihood
Conversational AI may also increase purchase likelihood directly because it reduces friction in the decision process, structures comparison more effectively, and makes the final choice feel more actionable. Even if consumers do not fully understand the basis of the recommendation, the combined effects of guidance fluency, personalization, and confidence may make them more willing to move toward purchase. Thus, compared with UI nudges and control, LLM conversational nudges should increase purchase likelihood.

**H7:** Relative to UI-based nudges and control, LLM conversational nudges increase purchase likelihood.

### 10.8 Joint tradeoff effect on perceived decision quality
Taken together, the model suggests that the effect of conversational AI on decision quality is not unidirectional. On the one hand, conversational nudges can improve perceived decision quality by increasing personalization, reducing cognitive load, and strengthening confidence. On the other hand, they can undermine perceived decision quality by reducing transparency. The overall effect on decision quality therefore should be jointly shaped by these competing benefit and risk paths.

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
This study contributes to research on digital nudging and conversational commerce by theorizing LLM-driven conversational assistants as a distinct form of AI nudge that operates through adaptive dialogue rather than interface placement alone. It further contributes by identifying a core tradeoff in AI-mediated shopping: conversational AI can increase personalization, reduce cognitive burden, and raise purchase support, while simultaneously reducing transparency in how recommendations are generated and justified. By comparing conversational AI nudges directly with traditional UI-based nudges, the study clarifies whether LLM-based assistance is merely a stronger interface cue or a qualitatively different architecture of influence. More broadly, the paper links classic recommendation effects, recommendation-agent explanation research, and newer conversational commerce work into a single theory of conversational AI as choice architecture. This framing also keeps the first paper narrow enough to be credible: it does not need to explain every possible AI-shopping outcome, only why conversational AI changes the balance between support and opacity differently from simpler nudges.

## 13. Immediate next steps
- convert the compact anchor set into a cleaner manuscript-style theoretical background section
- tighten construct definitions for perceived personalization, transparency, confidence, and perceived decision quality
- choose the shopping product category
- draft treatment materials for the three conditions
- specify the measures and analysis plan
