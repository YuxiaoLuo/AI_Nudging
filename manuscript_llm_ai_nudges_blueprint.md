# Talking Shoppers Into Buying? Experimental Evidence on LLM-Driven AI Nudges

## 1. Core premise
The integration of LLMs into e-commerce platforms has created a new form of digital choice architecture: conversational AI nudging. Unlike traditional UI nudges such as recommendation badges, product rankings, or highlighted labels, LLM-based assistants influence users through interactive, adaptive, and often opaque dialogue. This project examines whether and how LLM-driven conversational nudges shape purchase decision-making differently from traditional UI-based nudges.

## 2. Problem statement and research motivation
Digital nudging research has largely focused on interface-level interventions such as defaults, rankings, labels, visual salience, social proof, and recommendation cues. These mechanisms alter choice architecture by changing what users see and how options are presented. Recommendation research has further shown that online recommendations can influence consumer choice, while recommendation-agent research has highlighted the importance of explanations, neutrality, disclosure, and trust. However, LLM-enabled shopping assistants do more than present options. They converse, interpret user needs, generate comparative guidance, personalize recommendations in real time, and steer users through a dynamic exchange.

This shift matters because conversational AI may not simply be a stronger version of existing recommendation cues. It may represent a qualitatively different persuasive mechanism. Compared with static UI nudges, LLM-based nudges can feel more personalized, reduce search effort, guide users through complexity, and increase decision confidence. At the same time, they may reduce transparency because users cannot easily determine why a product is recommended, what logic was used, or whether the platform’s commercial interests shaped the response.

As a result, the central question is not only whether LLM assistants increase purchase likelihood. It is whether conversational AI nudges reshape the decision process itself by changing transparency, cognitive load, confidence, and ultimately perceived decision quality in ways that established interface nudges and prior recommendation mechanisms do not fully explain.

## 3. Potential contribution
This project can contribute by showing that LLM conversational assistants are a distinct form of AI nudge rather than a simple extension of existing digital nudges. It can also identify a central design tradeoff in conversational commerce: greater personalization and reduced cognitive burden may improve decision support and increase purchase, but increased algorithmic opacity may undermine transparent and responsible choice architecture. In that sense, the paper is not just about whether AI nudges work. It is about why conversational AI changes the balance between decision support and inspectability differently from rankings, badges, and classic recommendation agents.

Taken together, this framing suggests a contribution to both digital-nudging and conversational-commerce research. The paper positions conversational AI as a form of choice architecture whose distinctive value lies in adaptive dialogue, but whose distinctive risk lies in reduced inspectability of the recommendation process. The resulting contribution is therefore not a generic claim that AI improves shopping, but a more specific claim that conversational AI changes the mechanism of influence and thereby introduces a new tradeoff between decision support and transparency.

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
Prior digital nudging research has largely examined interventions that operate through the interface itself, such as rankings, labels, salience cues, defaults, and recommendation badges. These mechanisms alter consumer behavior primarily by influencing attention allocation, search order, and comparison efficiency (Häubl & Trifts 2000; Ursu 2018). Even when such cues are algorithmically generated, they are typically encountered as relatively static design features rather than as adaptive advisory processes. Related recommendation research further shows that online product recommendations can directly influence consumer choice (Senecal & Nantel 2004), establishing that digital guidance can move behavior even before a more agentic advisory layer is introduced.

A useful bridge emerges from the recommendation-agent literature. Xiao and Benbasat (2007) synthesize recommendation agents as decision-support technologies that differ in the way they gather preference input, structure product information, and shape consumer choice processes. This framing is important because it clarifies that advisory design, not only recommendation output, matters for how consumers use and evaluate digital guidance. Wang and Benbasat (2007) further show that explanation facilities influence trusting beliefs in recommendation agents, while later work shows that trust also depends on how consumers attribute competence and integrity to the advisory technology itself and on whether the agent appears neutral or commercially biased (Wang & Benbasat 2008; Wang et al. 2018; Wang & Wang 2019). More recent evidence also suggests that interactivity is itself a meaningful design dimension in recommendation systems rather than a superficial interface variation, because interactive and non-interactive recommendation agents differ in how trust and recommendation quality shape adoption (Ebrahimi et al. 2022).

However, these literatures still do not fully explain LLM conversational nudges. LLM-based assistants do not merely highlight, rank, or label options, and they do not only instantiate a bounded recommendation agent that offers fixed explanations. They can solicit preferences, ask follow-up questions, summarize tradeoffs, and adapt guidance across multiple turns. In that sense, they are closer to a hybrid of recommendation agent, decision aid, and conversational advisor than to a conventional interface nudge. Because the mechanism of influence is dialogic rather than purely visual, conversational AI should shape not only what consumers notice, but also how they experience support, effort, certainty, and understanding during the choice process.

### 6.2 Personalization as the core benefit route
A central advantage of conversational AI is its capacity to make guidance feel tailored to the consumer's stated goals, constraints, and preferences. Because the system can gather richer input than a static badge or ranking and respond in natural language, consumers should perceive the recommendation as more individualized and context-sensitive. This matters theoretically because perceived personalization captures more than mere relevance. It reflects the extent to which the consumer experiences the guidance as responsive to their own situation rather than as a generic platform signal. Existing conversational-shopping work is consistent with this expectation. Chung et al. (2020) show that personalization meaningfully shapes consumer responses to voice-shopping recommendations, while Chen et al. (2021) frame the conversational agent as a decision aid whose effectiveness depends on how well its interaction fits the shopper's task. Taken together, these studies support defining perceived personalization in the present paper as the consumer's perception that the recommendation guidance is specifically adapted to their own needs, goals, and preference structure rather than offered as a generic platform suggestion.

### 6.3 Cognitive load reduction through structured guidance
Perceived personalization should have downstream consequences for cognitive effort. When consumers face many options, attributes, and tradeoffs, decision making becomes effortful and mentally taxing. Conversational AI may reduce that burden by filtering the option set, structuring comparison, and translating complex information into a more manageable decision narrative. In this way, personalization is not only persuasive. It also functions as a mechanism of decision simplification. This distinguishes conversational guidance from static interface nudges, which may redirect attention but often do less to integrate and interpret tradeoffs on the consumer's behalf. Prior shopping research on interactive decision aids provides a useful baseline for this claim. Häubl and Trifts (2000) show that decision-aid tools can improve the efficiency of product search and comparison, and Chen et al. (2021) suggest that conversational assistance can play a similar task-support role in shopping settings. Accordingly, higher perceived personalization should reduce the cognitive load associated with product choice. Here, cognitive load should be understood as the mental effort required to process alternatives, compare product attributes, and reach a choice in the shopping task.

### 6.4 Confidence amplification in AI-assisted choice
As cognitive burden declines and guidance feels more tailored, consumers should become more confident in the option they are considering. Confidence is especially relevant in shopping environments characterized by attribute complexity and incomplete consumer knowledge. When the choice process feels manageable and the recommendation appears coherent, consumers should feel more certain that they are arriving at an acceptable decision. At the same time, confidence is not conceptually identical to decision quality. Confidence refers to certainty in the selected option, whereas perceived decision quality captures the broader evaluative judgment that the final decision is sound, appropriate, and well justified. In the present model, confidence is therefore best understood as a downstream consequence of the benefit route rather than as a substitute for evaluative quality. More specifically, choice confidence should be defined as the consumer's subjective certainty that the selected option is the right or appropriate choice among the considered alternatives. Because the current literature base offers stronger support for the decision-aid and personalization mechanisms than for a single canonical confidence anchor in commerce, the present paper should keep this construct definition disciplined and avoid overclaiming beyond the process logic already established.

### 6.5 Transparency as the core risk route
The same properties that make conversational AI helpful may also make it difficult to scrutinize. Unlike UI nudges, which often leave visible traces of how a product is highlighted or ranked, conversational recommendations can obscure the basis of advice. Consumers may not know which attributes were prioritized, how tradeoffs were weighted, whether platform incentives shaped the recommendation, or whether the same advice would have emerged under slightly different prompts. This opacity matters because it reduces the reconstructability of the choice architecture. Prior recommendation-agent research suggests that explanation facilities, sponsorship disclosure, and perceived integrity influence how advisory systems are evaluated (Wang & Benbasat 2007; Wang et al. 2018; Wang & Wang 2019). Luo et al. (2019) further shows in a commerce setting that disclosure about chatbot use changes customer responses, which makes transparency concerns especially salient for AI-mediated shopping interactions. Building on that logic, perceived transparency in the present project should be understood as the extent to which the recommendation basis feels both understandable and reconstructable after the fact. Perceived decision quality, in turn, should be defined as the consumer's judgment that the final decision is sound, appropriate, and well justified given the available information and the decision context.

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
Use a simulated online shopping task in a moderately involving product category with meaningful comparison needs. Good candidates are headphones, skincare, running shoes, or air fryers. At this stage, headphones appears to be the strongest candidate because the category combines attribute complexity, relatively broad consumer familiarity, and plausible tradeoffs among price, sound quality, comfort, battery life, and brand.

### Recommended design choice
Use a **three-condition between-subject experiment**:
1. LLM conversational nudge
2. UI-based nudge
3. control

At this point, the design logic is sufficiently stable that the next productive step is no longer broad conceptual expansion, but translation into concrete treatment materials and an analysis plan.

### Procedure
1. Participant receives a shopping scenario with a budget and preference goal.
2. Participant shops in one randomized condition.
3. Participant selects a product or indicates purchase likelihood.
4. Participant completes post-task scales.
5. Participant answers manipulation checks and basic controls.

### First-pass treatment-material direction
For the headphones version of the study, the three conditions should differ in the mode of guidance rather than in the underlying product set. In the LLM conversational-nudge condition, participants should interact with a chatbot-style assistant that asks a small number of preference-elicitation questions and then recommends a focal product with brief comparative reasoning. In the UI-based nudge condition, participants should see the same product environment but with static interface cues such as recommendation badges, ranking emphasis, or highlighted placement. In the control condition, participants should see the same products without explicit nudging cues. This structure should help isolate the effect of conversational guidance relative to static nudges while holding the core decision environment as constant as possible.

A concrete first-pass implementation should use a product set of roughly six to eight headphone options spanning recognizable but non-dominant tradeoffs: for example, one model emphasizing sound quality, one emphasizing battery life, one emphasizing comfort, one emphasizing noise cancellation, one emphasizing value, and one balanced midrange option. Each option should present the same core attributes across conditions, such as price, battery life, weight, noise cancellation, microphone quality, comfort rating, and brand. The conversational condition should ask participants two or three short preference questions, then recommend one focal option and briefly compare it against one or two alternatives. The UI-nudge condition should instead highlight that same focal option through badges such as “Recommended for you” or “Best Match,” plus a small amount of static comparative emphasis. The control condition should present the same product grid and attribute information without recommendation cues.

A usable first-pass shopping scenario could ask participants to imagine that they need a pair of wireless over-ear headphones for frequent daily use, with a budget cap such as $180 and a goal of finding the best overall fit for commuting, work, and casual listening. This scenario is broad enough to be realistic for a general participant pool while still making attribute tradeoffs consequential. The conversational script should remain deliberately short. A first assistant turn could ask what matters most among sound quality, comfort, battery life, and noise cancellation. A second turn could ask whether the participant prioritizes work calls, travel, exercise, or general everyday use. A third turn, if needed, could clarify price sensitivity. The assistant would then recommend the focal option and justify it in two or three sentences, explicitly referencing the participant's stated priorities. To preserve comparability across conditions, the recommended focal option and the core comparative claims should remain constant, with only the delivery mode changing.

### Concrete first-pass headphone stimulus set
To reduce brand confounds and keep the first study implementable, the stimulus set should use fictional but plausible headphone brands. A compact six-option set is likely sufficient because it creates real comparison pressure without producing an unwieldy shopping screen. One clean structure is to include one option emphasizing battery life, one emphasizing comfort, one emphasizing active noise cancellation, one emphasizing call quality, one emphasizing low price, and one balanced midrange option. The balanced midrange option should be the focal product recommended in both the conversational and UI-nudge conditions so that the substantive recommendation remains constant across treatments.

A first-pass product table could be structured as follows. `Auralite A1` emphasizes value at roughly $89 but offers weaker noise cancellation and call quality. `Auralite B3` emphasizes battery life at roughly $149 with 50 hours of playback but only moderate comfort. `NordSound C5` emphasizes noise cancellation at roughly $179 with strong commuting performance but higher weight. `NordSound D2` emphasizes call quality at roughly $159 with the strongest microphone score but only average battery life. `VeroWave H4` emphasizes comfort at roughly $169 with the best comfort rating and low weight but only midrange microphone quality. `VeroWave M6` should function as the balanced focal option at roughly $139, offering solid but non-dominant scores across sound quality, comfort, battery life, microphone quality, and noise cancellation. This profile makes the focal recommendation defensible without making it objectively superior on every attribute.

The same attribute columns should be displayed in every condition: price, battery life, weight, active noise cancellation, microphone quality, comfort rating, and user rating. Keeping those attributes constant matters because the theory is about the mode of guidance, not about access to different product information. If later implementation needs simplification, user rating can be removed first so the design does not become overloaded with peripheral cues.

### First-pass condition implementation details
The conversational condition should feel adaptive without becoming so open-ended that treatment content varies uncontrollably. The cleanest first implementation is a semi-structured three-turn exchange. Turn 1: the assistant asks which matters most among sound quality, comfort, battery life, and noise cancellation. Turn 2: the assistant asks about primary use context such as commuting, work calls, travel, or general daily listening. Turn 3: the assistant asks whether staying under budget is more important than getting the strongest feature set. After those inputs, the assistant recommends `VeroWave M6` and compares it briefly with two alternatives, for example noting that `NordSound C5` has stronger noise cancellation but is heavier and more expensive, while `Auralite B3` offers more battery life but less balanced overall performance.

A usable first recommendation script could read as follows: "Based on what you said, I would lean toward the VeroWave M6. It stays comfortably under your budget, performs well across sound, comfort, and battery life, and looks like the most balanced fit for commuting and daily use. If your top priority were maximum noise cancellation, the NordSound C5 would be stronger, but it is heavier and costs more. If battery life mattered above everything else, the Auralite B3 would be a better fit, but it gives up some overall balance." This script is concrete enough to build stimuli from, while still leaving room for wording refinement later.

The UI-based nudge condition should recommend the same focal product without dialogue. The simplest implementation is to place a `Best Match` badge on `VeroWave M6`, position it first in the grid, and add one short static note such as `Balanced choice for commuting, work, and everyday listening`. A secondary visual cue such as `Recommended for you` can be added if needed, but the condition should avoid explanatory depth that starts to mimic the conversational treatment. The control condition should present the same six products in the same layout and attribute table but without badges, highlighted placement, or advisory language.

### First-pass analysis strategy direction
The analysis strategy should match the paper's tradeoff logic rather than defaulting to a diffuse set of outcome tests. At a first pass, the core analysis should compare the three experimental conditions on purchase likelihood and perceived decision quality while also testing whether the conversational condition operates through the proposed benefit and risk routes. In practical terms, that means estimating the effect of condition on perceived personalization and perceived transparency, then testing whether personalization predicts lower cognitive load and higher confidence, and whether transparency predicts perceived decision quality. A path-model or structural-equation-style analysis may ultimately fit the theory best, although simpler regression-based mediation checks could be used in an initial version if they preserve the model's logic.

A compact first-pass specification could proceed in three layers. First, estimate omnibus condition effects on the two headline outcomes, purchase likelihood and perceived decision quality, using the three-condition design with control variables included only as theory-justified covariates. Second, test the benefit path by estimating whether the conversational condition increases perceived personalization relative to the other conditions, whether personalization predicts lower cognitive load, and whether lower cognitive load predicts higher confidence. Third, test the risk path by estimating whether the conversational condition lowers perceived transparency and whether transparency predicts perceived decision quality net of the benefit-path variables. If sample size permits, these relations should be estimated in a single structural path model with dummy-coded experimental conditions. If sample size is tighter, the same logic can be implemented through staged regression models and indirect-effect estimation, with special emphasis on preserving the tradeoff interpretation rather than maximizing model complexity.

### First-pass methods and estimation note
The current design is now concrete enough to support a compact methods section. Participants should be randomly assigned to one of the three conditions after reading the shopping scenario. All participants should see the same six headphone options and the same attribute information, then indicate which product they would choose and how likely they would be to purchase it. The post-task survey should then measure perceived personalization, cognitive load, choice confidence, perceived transparency, perceived decision quality, and the smaller set of secondary responses retained for robustness checks.

The most defensible first empirical specification is a dummy-coded condition model with control as the omitted category and a planned conversational-versus-UI contrast reported explicitly. The paper should not rely only on an omnibus ANOVA-style narrative because the theory makes directional claims about the conversational condition relative to both alternatives. For the process model, the cleanest first path structure is: conversational condition -> perceived personalization -> lower cognitive load -> higher confidence, alongside conversational condition -> lower perceived transparency -> lower perceived decision quality. Purchase likelihood can be modeled as a downstream headline outcome predicted directly by condition and, in supplementary analyses, indirectly by the benefit-path variables. Perceived decision quality should be modeled as the main evaluative outcome shaped jointly by confidence and transparency.

If sample size is strong enough, a single path model with bootstrapped indirect effects would best preserve the tradeoff logic. If sample size is more modest, the paper can still remain coherent by estimating three staged models: first, condition effects on headline outcomes; second, condition effects on personalization and transparency; third, regression or mediation models linking personalization to cognitive load and confidence and linking transparency to perceived decision quality. Either way, the analysis write-up should stay disciplined: the goal is to test the support-versus-opacity tradeoff, not to run every possible condition comparison or exploratory moderator.

### Publication-ready analysis specification draft
The analysis section should state the planned contrasts and model sequence explicitly rather than describing them only at a conceptual level. The most useful coding scheme is to treat the control condition as the omitted reference group and estimate two dummy variables, one for the conversational condition and one for the UI-nudge condition. This makes it possible to report both treatment-versus-control comparisons directly while also testing the more theory-critical conversational-versus-UI contrast through a planned linear restriction. Because the paper's core claim is about whether conversational guidance differs from static nudging rather than merely whether any intervention differs from no intervention, this planned contrast should be treated as central rather than supplemental.

For the headline outcomes, the first model layer should estimate condition effects on purchase likelihood and perceived decision quality with the compact control set entered only as theory-justified covariates. This provides the cleanest first answer to whether conversational AI changes consumer responses at the outcome level. The second model layer should estimate condition effects on perceived personalization and perceived transparency, because these are the first-stage variables that distinguish the benefit and risk routes. The third model layer should estimate whether perceived personalization predicts lower cognitive load, whether lower cognitive load predicts higher confidence, and whether confidence and transparency jointly predict perceived decision quality. In the write-up, these models should be presented as a cumulative sequence rather than as isolated regressions.

If the final sample size and data quality are strong enough, the preferred estimation strategy should be a single structural path model with bootstrapped indirect effects. In that specification, the conversational and UI dummy variables should predict perceived personalization and perceived transparency; perceived personalization should predict cognitive load; cognitive load should predict confidence; confidence and transparency should predict perceived decision quality; and purchase likelihood should be modeled as an outcome of condition, with an optional supplementary extension allowing indirect association through the benefit-route variables. The value of this structure is that it keeps the empirical specification aligned with the paper's theoretical tradeoff rather than fragmenting the model into disconnected tests.

If the sample does not support a stable path model, the fallback analysis should still preserve the same logic. First, estimate OLS models for purchase likelihood and perceived decision quality. Second, estimate OLS models for perceived personalization and perceived transparency. Third, estimate regression-based indirect effects for the benefit path, moving from conversational condition to perceived personalization, then to cognitive load, then to confidence. Fourth, estimate the transparency path by testing whether lower transparency predicts lower perceived decision quality net of confidence and the control variables. This fallback sequence is analytically simpler, but it still preserves the substantive claim that conversational AI produces a positive support path and a negative opacity path.

Two presentational choices should also be fixed in advance. First, cognitive-load items should either be reverse-coded so that higher scores consistently indicate a more favorable decision process or retained in the original direction with negative coefficients interpreted explicitly; the paper should not switch conventions across models. Second, the results tables should separate headline outcome tests from process-path tests so the paper does not read like a broad exploratory model search. This will help keep the empirical contribution disciplined and publication-oriented.

### Why headphones is currently the best first-category option
A first paper should use a category that is sufficiently consequential to make advice meaningful, but not so specialized that participants struggle to evaluate the products at all. Headphones meets that requirement well. The category commonly involves multiple attributes, meaningful tradeoffs, and frequent use of recommendation support in actual online shopping. It should therefore make it easier to observe differences between conversational guidance and static nudges while keeping the decision task understandable for a broad participant pool. Compared with skincare, headphones involves less idiosyncratic bodily risk and fewer product-fit contingencies that could blur the interpretation of transparency and confidence effects. Compared with running shoes, headphones also make it easier to display multiple comparable attributes in a compact product grid without forcing participants to rely heavily on prior fit experience. Relative to air fryers, headphones likely generate stronger consumer familiarity with recommendation aids and more plausible use of conversational comparison support. For a first paper, this combination makes headphones the cleanest current category for observing the tradeoff between decision support and inspectability.

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

### Preliminary measure logic
At this stage, the measure strategy should remain aligned with the theory rather than expanding into a broad inventory of attitudes. Purchase likelihood should capture the consumer's willingness to move toward buying the focal product. Perceived decision quality should capture whether the final choice feels sound, appropriate, and well justified. Perceived personalization should capture the extent to which the guidance feels tailored to the consumer's preferences and goals. Cognitive load should capture the amount of mental effort required to make the choice. Perceived transparency should capture whether the recommendation basis feels understandable and reconstructable. Choice confidence should capture certainty in the selected option. Keeping the measures tied this closely to the construct definitions should help preserve alignment between the theory, hypotheses, and eventual empirical implementation.

### Manipulation checks
- degree of conversational interaction
- perceived adaptivity/personalization of the aid
- perceived AI involvement
- perceived visibility of recommendation logic

### Preliminary manipulation-check logic
The manipulation checks should verify that the three conditions differ in the intended way without collapsing into the substantive mediators themselves. The key purpose is to confirm that the LLM condition is experienced as more conversational and adaptive than the UI-based nudge condition, and that both differ from control in the expected direction. Checks on perceived AI involvement and visibility of recommendation logic are also useful because they can confirm that participants recognized the intervention as algorithmically generated while still perceiving differences in how observable the recommendation process was.

### Controls
- product category familiarity
- prior use of AI assistants for shopping
- general trust in AI
- need for cognition
- shopping involvement

### Preliminary control-variable logic
The control set should remain theoretically justified and restrained rather than expanding into a long omnibus list. Product category familiarity is important because consumers with stronger prior knowledge may experience lower cognitive load and less dependence on external guidance. Prior use of AI assistants for shopping and general trust in AI are useful because they may shape baseline receptivity to conversational recommendations. Need for cognition is relevant because consumers who enjoy effortful thinking may respond differently to simplified guidance. Shopping involvement should also be retained because a more involving purchase context may intensify attention to both personalization benefits and transparency concerns. Keeping the control set compact and theory-linked should make the design easier to defend empirically.

## 12. Draft contribution statement
This study contributes to research on digital nudging and conversational commerce by theorizing LLM-driven conversational assistants as a distinct form of AI nudge that operates through adaptive dialogue rather than interface placement alone. It further contributes by identifying a core tradeoff in AI-mediated shopping: conversational AI can increase personalization, reduce cognitive burden, and raise purchase support, while simultaneously reducing transparency in how recommendations are generated and justified. By comparing conversational AI nudges directly with traditional UI-based nudges, the study clarifies whether LLM-based assistance is merely a stronger interface cue or a qualitatively different architecture of influence. More broadly, the paper links classic recommendation effects, recommendation-agent explanation research, and newer conversational commerce work into a single theory of conversational AI as choice architecture.

The theoretical contribution is therefore twofold. First, the paper reconceptualizes conversational AI as a distinctive form of digital choice architecture whose influence is enacted through adaptive dialogue rather than static interface placement. Second, it identifies a mechanism-level tradeoff in which the same properties that make conversational AI feel useful and personalized may also make the recommendation process less transparent and less inspectable. This framing keeps the first paper narrow enough to be credible. The goal is not to explain every possible AI-shopping outcome, but to explain why conversational AI changes the balance between decision support and opacity differently from simpler nudges.

## 13. Immediate next steps
- convert the compact anchor set into a cleaner manuscript-style theoretical background section
- decide whether the new recommendation-agent bridge papers remain support citations or whether one should be elevated into the compact core anchor set
- harmonize the opening, theory, and hypotheses into one fully consistent scientific manuscript voice
- draft first-pass treatment materials for the three conditions using headphones as the lead category
- specify the analysis strategy for testing the tradeoff model
- continue selective literature collection only when it sharpens a construct anchor or a key comparison

## 14. First-pass theoretical background draft direction
A cleaner manuscript-style theoretical background should likely unfold in four steps. First, it should establish that digital choice architecture in online shopping has traditionally operated through rankings, labels, and interactive decision aids that shape search, comparison, and consideration (for example, Häubl and Trifts 2000; Ursu 2018; Senecal and Nantel 2004). Second, it should show that recommendation-agent research moved beyond simple salience effects by introducing questions of explanation, neutrality, sponsorship disclosure, and trusting beliefs (for example, Wang and Benbasat 2007; Wang et al. 2018; Wang and Wang 2019). Third, it should explain that conversational agents and AI shopping assistants transform this advisory logic into a more dialogic and adaptive form of guidance, making the recommendation process feel more personalized while also making the underlying logic more difficult to inspect. Fourth, it should use that bridge to motivate the paper's core tradeoff argument: conversational AI is not just a stronger nudge, but a different form of choice architecture that can simultaneously improve decision support and reduce transparency.

This four-step structure would help the manuscript avoid reading like a list of adjacent literatures. Instead, it would produce a cumulative theoretical bridge from interface nudges, to recommendation agents, to conversational AI as dialogic choice architecture.

### 14.0 Background section purpose note
The theoretical background should do more than summarize adjacent streams. Its purpose is to establish a cumulative argument in which each literature explains part of the phenomenon but leaves unresolved how LLM-based conversational shopping assistants alter the mechanism of influence. The section should therefore read as a progressive narrowing toward the paper's central question, not as a broad review of everything related to AI in commerce.

### 14.0a Background section scope guardrail
A useful guardrail for drafting is that every paragraph in the section should either establish the baseline from which conversational AI departs, explain the advisory and transparency mechanisms that become relevant once recommendations are more agentic, or sharpen the paper's specific tradeoff claim. If a citation or paragraph does not help perform one of those functions, it likely belongs in peripheral context rather than the core theoretical background.

### 14.0b Background section anchor priorities
Given the current literature set, the strongest anchors for the core theoretical background should remain compact. The baseline digital-guidance portion should lean primarily on Häubl and Trifts (2000), Senecal and Nantel (2004), and Ursu (2018). The advisory and transparency bridge should lean primarily on Wang and Benbasat (2007), Wang et al. (2018), Wang and Wang (2019), and likely Luo et al. (2019). At this stage, Wang and Benbasat (2007) appears to be the clearest bridge paper to elevate into the compact core anchor set because explanation facilities bear most directly on the manuscript's transparency mechanism. By contrast, Xiao and Benbasat (2007), Wang and Benbasat (2008), Wang and Benbasat (2016), and the 2022 interactive-versus-non-interactive recommendation-agent meta-analysis are currently best treated as supporting bridge citations unless later drafting reveals that one of them is carrying more core theoretical weight than expected.

A useful implication of this anchor strategy is that the section should avoid introducing too many parallel literatures at once. Theoretical breadth should come from a disciplined bridge among a few strong anchors, not from assembling a long inventory of adjacent AI, service, or consumer-behavior references.

### 14.1 Background section opening paragraph draft
Online shopping platforms have long shaped consumer choice through digital choice architecture such as rankings, recommendation cues, and interactive decision aids. Prior research shows that these mechanisms can alter search effort, comparison processes, and purchase behavior by changing what consumers notice and how they evaluate options (Häubl & Trifts 2000; Senecal & Nantel 2004; Ursu 2018). A second stream of research on recommendation agents extends this logic by showing that advisory technologies are evaluated not only in terms of usefulness, but also in terms of explanations, neutrality, sponsorship disclosure, and trusting beliefs (Wang & Benbasat 2007; Wang et al. 2018; Wang & Wang 2019). Together, these literatures establish that digital guidance tools can meaningfully shape online decisions, but they do not fully explain the distinctive form of influence introduced by LLM-based conversational shopping assistants.

This opening move is important because it keeps the paper anchored in well-established digital-guidance and recommendation literatures before introducing conversational AI. Doing so helps frame the project as an extension and reconfiguration of known choice-architecture mechanisms rather than as a stand-alone AI phenomenon paper.

### 14.2 Background section bridge paragraph draft
LLM-based shopping assistants extend earlier advisory technologies in one important way: they move recommendation support from visible interface structure into adaptive dialogue. Rather than merely highlighting options or presenting explanations for a preconfigured recommendation, conversational assistants can solicit preferences, reformulate tradeoffs, and deliver guidance through sequential natural-language interaction. This shift matters because it changes not only the surface format of the nudge, but also the mechanism through which influence occurs. The recommendation can feel more responsive and personalized, yet also become harder for consumers to inspect after the fact. As a result, conversational AI should be understood not simply as a stronger badge or smarter recommendation agent, but as a more dialogic form of choice architecture whose benefits and risks must be theorized together.

### 14.3 Background section tradeoff-transition paragraph draft
This reconceptualization creates the central theoretical opening for the paper. If conversational AI changes choice architecture through adaptive dialogue, then its consequences should not be assessed only in terms of whether it increases purchase likelihood. The same features that make conversational guidance feel helpful, namely responsiveness, personalization, and reduced decision friction, may also make the recommendation process less transparent and less reconstructable to the consumer. In that sense, conversational AI introduces a sharper tension between decision support and inspectability than earlier interface nudges or even more bounded recommendation agents. The relevant theoretical question is therefore whether LLM-based nudges improve the shopping process by making decisions easier and more confidence-inducing, while simultaneously weakening consumers' ability to understand how those decisions are being shaped.

### 14.4 Background section model-link paragraph draft
This theoretical tension leads directly to the paper's model. On the benefit side, conversational AI should increase perceived personalization because its guidance can be experienced as more responsive to the shopper's stated goals and constraints. That stronger personalization should reduce cognitive load by simplifying comparison and narrowing the choice set, which in turn should increase confidence in the selected option. On the risk side, the same conversational and adaptive qualities should reduce perceived transparency because the basis of the recommendation is less visible and less easily reconstructed. The core prediction of the paper is therefore not that conversational AI is uniformly better or worse than UI-based nudges, but that it changes the consumer decision process through a pair of competing pathways whose joint consequences shape purchase likelihood and perceived decision quality.

## 15. First-pass construct-anchor map
To stabilize the theory section, each core construct should now be tied to a smallest defensible anchor set rather than supported by broad adjacent citations. The goal of this map is not to finalize measurement yet, but to identify which sources should carry the definitional and causal burden in the next writing pass.

### 15.1 Perceived personalization
Perceived personalization should be anchored primarily in conversational-shopping and adaptive-guidance work rather than in broad personalization literatures. The strongest currently available support appears to come from Chung et al. (2020), which directly studies personalization in voice-shopping recommendations, and Chen et al. (2021), which frames the conversational agent as a decision aid whose fit with the shopping task matters for user evaluation. These sources are not enough to make a sweeping general personalization theory claim, but they are well aligned with the present commerce setting and should be sufficient for a focused first-paper definition: perceived personalization is the extent to which the recommendation guidance is experienced as tailored to the consumer's own goals, preferences, and constraints.

### 15.2 Cognitive load
Cognitive-load logic should be anchored less as an isolated psychology construct and more as a consequence of guided comparison in digital shopping environments. Häubl and Trifts (2000) is the cleanest current baseline because it shows how interactive decision aids can improve the efficiency of product search and comparison, which gives the manuscript a commerce-native basis for arguing that structured guidance reduces mental effort. Chen et al. (2021) can then serve as a conversational bridge by suggesting that matched conversational assistance functions as a decision aid rather than merely as an attention cue. In the next draft, cognitive load should therefore be defined in task-specific terms as the mental effort required to process alternatives, compare attributes, and reach a choice in the shopping task.

### 15.3 Choice confidence
Choice confidence should be treated as a downstream subjective state that emerges when the choice environment feels manageable and the recommendation appears coherent. The current literature set does not yet contain a perfect headline confidence anchor from a top commerce journal, so the manuscript should avoid overclaiming here. For now, confidence should be positioned as a theoretically necessary process outcome within the benefit route, supported indirectly by decision-aid logic and by the conversational-assistance framing in Chen et al. (2021) and Chung et al. (2020). This is a place where later measure selection may require an additional source-backed pass, but the conceptual distinction should already remain firm: confidence is certainty in the selected option, not the broader judgment that the decision process was normatively sound.

### 15.4 Perceived transparency
Perceived transparency should be anchored in recommendation-agent explanation and disclosure research rather than in generic AI ethics discussions. Wang and Benbasat (2007) provides the clearest explanation-based starting point because it shows that explanation facilities affect trusting beliefs in recommendation agents. Wang et al. (2018) and Wang and Wang (2019) then sharpen the disclosure, neutrality, and integrity side of the argument, while Luo et al. (2019) provides an especially relevant commerce-facing anchor showing that chatbot disclosure changes customer responses in a shopping context. Together, these sources justify defining perceived transparency as the extent to which the recommendation basis feels understandable and reconstructable to the consumer.

### 15.5 Perceived decision quality
Perceived decision quality should remain tightly separated from both confidence and purchase likelihood. The current literature set gives stronger support for decision support and transparency mechanisms than for a single canonical decision-quality anchor, so the manuscript should define this construct carefully and modestly: perceived decision quality is the consumer's judgment that the final choice is sound, appropriate, and well justified given the available information and the shopping context. In the next pass, this construct should be supported primarily by the paper's internal logic linking confidence and transparency to evaluative judgment, rather than by forcing an overly broad citation net.

### 15.6 Implication for the next manuscript pass
The practical implication is that the next writing gain should come from tightening these construct paragraphs directly inside the theory section rather than continuing broad article collection. If another literature pass is done, it should be narrowly targeted at only two remaining weak spots: a better source-backed confidence anchor and, if possible, a stronger commerce-facing decision-quality anchor.

## 16. First-pass methods section draft

### 16.1 Design overview
The first study can be designed as a three-condition between-subject online experiment comparing an LLM conversational nudge, a traditional UI-based nudge, and a no-nudge control condition. The design holds the shopping assortment constant across conditions and varies only the mode through which recommendation guidance is delivered. This structure is important because the theory concerns whether conversational guidance changes the decision process differently from static interface nudges, not whether participants respond differently to different product sets.

### 16.2 Participants and setting
Participants should be adult consumers recruited from a general online panel such as Prolific or CloudResearch. The study does not require category expertise, but participants should be comfortable making ordinary online shopping decisions in English. A first-pass target sample of roughly 450 to 600 completed responses is likely defensible because it would provide approximately 150 to 200 participants per condition, which is a more credible range for detecting condition differences and estimating the proposed process paths than a small-N pilot-style design. The study should exclude duplicate, incomplete, and low-effort responses through prespecified quality checks rather than ad hoc trimming.

### 16.3 Shopping scenario and stimuli
Participants should be asked to imagine that they need a pair of wireless over-ear headphones for frequent daily use, with a budget cap of $180 and a goal of finding the best overall fit for commuting, work, and casual listening. All participants should evaluate the same six fictional headphone options. The options should differ in meaningful but non-dominant ways on price, battery life, weight, active noise cancellation, microphone quality, comfort rating, and user rating. The key focal option, `VeroWave M6`, should be positioned as a balanced midrange alternative that performs solidly across the core attributes without being the best product on every dimension.

In the conversational-nudge condition, participants should interact with a semi-structured assistant that asks a short sequence of preference questions and then recommends `VeroWave M6` with brief comparative reasoning. In the UI-based nudge condition, participants should see the same focal option highlighted through static cues such as first position, a `Best Match` badge, and a short recommendation note. In the control condition, participants should see the same product grid without explicit recommendation cues. This implementation keeps the substantive recommendation as constant as possible while manipulating the mode of guidance.

### 16.4 Procedure
The first-pass procedure can be written compactly in manuscript style. Participants first read the shopping scenario and are then randomly assigned to one of the three shopping conditions. They review the headphone options, interact with the conversational assistant or UI cues as applicable, and then indicate which product they would choose. After making that selection, participants report purchase likelihood and complete the post-task scales for perceived personalization, cognitive load, choice confidence, perceived transparency, perceived decision quality, and the secondary evaluation variables retained for robustness checks. The survey should conclude with manipulation checks, control variables, and a small number of data-quality screens.

### 16.5 Outcome structure
The empirical structure should remain tightly matched to the theory. Purchase likelihood and perceived decision quality should function as the headline dependent variables. Perceived personalization, cognitive load, choice confidence, and perceived transparency should function as the primary process variables. Trust in the recommender and satisfaction with the shopping aid can remain secondary responses for descriptive completeness and robustness checks, but they should not displace the paper's central tradeoff model.

## 17. First-pass questionnaire candidates

### 17.1 Response format
Unless a borrowed validated scale later suggests otherwise, the first-pass questionnaire can use seven-point Likert-type response formats anchored from strongly disagree to strongly agree for evaluative items, plus a seven-point unlikely-to-likely format for purchase likelihood. This is adequate for blueprint purposes and can later be refined during scale selection and pretesting.

### 17.2 Purchase likelihood
Candidate items:
- I would be likely to purchase the headphone option I selected.
- If I were actually shopping for headphones, I would seriously consider buying the option I selected.
- The probability that I would purchase the option I selected is high.

### 17.3 Perceived decision quality
Candidate items:
- I feel that I made a high-quality decision in this shopping task.
- My final choice seems well justified given the information available.
- I believe the option I selected is an appropriate choice for my needs.
- I feel that I arrived at a sound overall decision.

### 17.4 Perceived personalization
Candidate items:
- The guidance I received felt tailored to my needs and preferences.
- The shopping aid took my priorities into account.
- The recommendation felt personalized rather than generic.

### 17.5 Cognitive load
Candidate items:
- It took a lot of mental effort to make this decision.
- Comparing the headphone options felt cognitively demanding.
- This shopping task felt mentally taxing.

One reverse-direction note is necessary here: if these items are retained in this wording, higher scores indicate greater cognitive load, so the analysis plan should either reverse-code for interpretive clarity or keep the negative direction explicit in the model write-up.

### 17.6 Choice confidence
Candidate items:
- I am confident that I selected the right headphone option.
- I feel certain about the choice I made.
- I have little doubt that my selected option fits my needs well.

### 17.7 Perceived transparency
Candidate items:
- I understand why this product was recommended or stood out.
- The basis of the recommendation was clear to me.
- I could reconstruct the main logic behind the recommendation.
- It was easy to tell what information drove the guidance I received.

### 17.8 Secondary outcomes
Trust candidate items:
- I trust the shopping aid I interacted with.
- The shopping aid seemed reliable.
- I would feel comfortable relying on this type of aid again.

Satisfaction candidate items:
- I am satisfied with the guidance I received in this shopping task.
- The shopping aid improved my shopping experience.
- The guidance process worked well for me.

### 17.9 Manipulation checks
Candidate items:
- The shopping aid felt conversational.
- The guidance adapted to my inputs or needs.
- Artificial intelligence played a meaningful role in the guidance I received.
- The logic behind the recommendation was visibly presented to me.

The final item should be handled carefully because it sits near the transparency construct. It is acceptable as a manipulation-oriented perception check at this stage, but the eventual instrument should avoid making manipulation checks redundant with the core mediator.

### 17.10 Controls
Compact first-pass control candidates:
- product category familiarity: "I am familiar with wireless over-ear headphones as a product category."
- prior AI shopping use: "I have used AI-based assistants or chatbots for shopping before."
- general trust in AI: "I generally trust AI systems to provide useful recommendations."
- need for cognition: use a short validated subset later rather than inventing ad hoc items
- shopping involvement: "Choosing the right headphones in this scenario feels like an important decision."

## 18. Immediate drafting implications
The manuscript is now close to having a complete first-pass empirical core. The next highest-leverage writing move should be to convert Sections 2, 6, 10, 16, and 17 into a more continuous paper-like draft so that the project has a coherent introduction-theory-hypotheses-methods arc rather than a strong but still modular blueprint.

## 19. Working manuscript pass

### 19.1 Introduction
Online shopping platforms increasingly embed large language models into recommendation and assistance interfaces, creating a new form of digital choice architecture in which consumers are guided through interactive conversation rather than static interface cues alone. Prior research shows that digital nudges such as rankings, labels, and recommendation cues can meaningfully alter search, comparison, and purchase behavior, while recommendation-agent research shows that explanations, neutrality, and disclosure shape how advisory technologies are evaluated (Häubl & Trifts 2000; Senecal & Nantel 2004; Ursu 2018; Wang & Benbasat 2007; Wang et al. 2018; Wang & Wang 2019). Yet LLM-based shopping assistants do more than highlight products or present a recommendation. They can solicit preferences, summarize tradeoffs, personalize guidance in real time, and steer users through a dynamic exchange that may feel both more helpful and less inspectable than traditional interface nudges.

This shift creates an important theoretical gap. Existing digital-nudging and recommendation literatures provide a strong baseline for understanding interface-level influence and advisory-system design, but they do not fully explain whether conversational AI operates as merely a stronger recommendation cue or as a qualitatively different architecture of influence. Compared with static UI nudges, conversational AI may improve decision support by making guidance feel more personalized, reducing cognitive burden, and increasing confidence in the final choice. At the same time, conversational guidance may reduce transparency because consumers cannot easily determine why a recommendation was produced, how tradeoffs were weighted, or whether commercial priorities shaped the advice. The relevant question is therefore not only whether conversational AI increases purchase likelihood, but whether it changes the consumer decision process itself in ways that create a tradeoff between decision support and inspectability.

This paper addresses that question by theorizing LLM conversational assistants as a distinct form of AI nudge in online shopping. We argue that conversational AI changes choice architecture through adaptive dialogue rather than interface placement alone and that this shift produces two competing process routes. On the benefit side, conversational guidance should increase perceived personalization, reduce cognitive load, and strengthen choice confidence. On the risk side, it should reduce perceived transparency in the recommendation process. We test this argument in a three-condition experiment comparing an LLM conversational nudge, a traditional UI-based nudge, and a no-nudge control condition. In doing so, the paper contributes to digital-nudging and conversational-commerce research by showing that the distinctive issue raised by conversational AI is not simply stronger persuasive effectiveness, but a new balance between support and opacity in digital choice architecture.

### 19.2 Theoretical background
Research on digital choice architecture has long shown that relatively simple interface structures can shape consumer behavior by altering attention allocation, search order, and comparison efficiency. Rankings, labels, recommendation cues, and interactive decision aids can reduce search costs and guide consumers toward focal options, even when the underlying alternatives remain unchanged (Häubl & Trifts 2000; Senecal & Nantel 2004; Ursu 2018). A related stream on recommendation agents extends this logic by showing that advisory technologies are evaluated not only on usefulness, but also on the explanations they provide, the neutrality they signal, and the integrity they appear to embody (Xiao & Benbasat 2007; Wang & Benbasat 2007; Wang et al. 2018; Wang & Wang 2019). These literatures establish that digital guidance can influence both what consumers choose and how they interpret the technologies assisting them.

LLM-based conversational assistants extend this established logic in an important way. Rather than merely signaling a recommended option or displaying a preconfigured explanation, they move recommendation support into adaptive, sequential dialogue. Conversational assistants can ask follow-up questions, incorporate user-stated priorities, reformulate tradeoffs in natural language, and present a recommendation as if it were the result of an ongoing advisory exchange. This makes the shopping aid more responsive to the user, but it may also make the basis of the recommendation harder to reconstruct after the fact. For that reason, conversational AI should be understood not simply as a stronger badge or smarter recommender, but as a more dialogic form of choice architecture whose benefits and risks must be theorized jointly.

The central benefit route begins with perceived personalization. Because a conversational assistant can gather richer preference input and present advice in language that appears tailored to the shopper's goals, consumers should experience the guidance as more individualized than static UI nudges. Greater perceived personalization should, in turn, reduce cognitive load by narrowing the set of plausible options and making attribute tradeoffs easier to process. As the task feels more manageable, consumers should become more confident in the choice they make. This route implies that conversational AI can improve the felt quality of shopping support not merely by increasing salience, but by changing how consumers experience the task of evaluating alternatives.

The central risk route concerns transparency. The same adaptive and fluent qualities that make conversational guidance feel useful may also reduce the visibility of how recommendations are produced. Unlike a static badge or ranking, conversational advice does not necessarily reveal which attributes were prioritized, how the recommendation was derived, or whether commercial motives shaped the guidance. Prior recommendation-agent and disclosure research suggests that such opacity matters because explanation, neutrality, and perceived integrity shape how consumers evaluate advisory technologies (Wang & Benbasat 2007; Wang et al. 2018; Wang & Wang 2019; Luo et al. 2019). The resulting theoretical prediction is therefore a tradeoff: conversational AI may improve purchase support and subjective confidence while also weakening consumers' ability to inspect and evaluate the basis of the recommendation.

### 19.3 Hypotheses and model
The research model follows directly from this tradeoff logic. Relative to UI-based nudges and control, LLM conversational nudges should increase perceived personalization because the guidance is experienced as more responsive to the shopper's stated goals and constraints. Greater perceived personalization should lower cognitive load, and lower cognitive load should increase choice confidence. Confidence, in turn, should support higher perceived decision quality because consumers often evaluate their decisions partly through whether the final choice feels justified and well grounded. At the same time, conversational nudges should reduce perceived transparency because the recommendation process is less visible and less easily reconstructed than in a static interface condition. Lower transparency should weaken perceived decision quality by making it harder for consumers to judge whether the recommendation was well founded. Conversational AI may nevertheless increase purchase likelihood directly because a more fluent and structured decision process can reduce friction and make purchase action more likely even when transparency is imperfect.

Taken together, these predictions imply that the effect of conversational AI on decision quality is not uniformly positive or negative. Rather, it should be shaped jointly by a positive personalization-to-confidence route and a negative transparency route. The core theoretical claim is therefore that LLM conversational nudges do not merely intensify existing interface effects. They reconfigure digital choice architecture by combining stronger decision support with lower inspectability.

### 19.4 Method
To test this argument, the first study can use a three-condition between-subject online experiment comparing an LLM conversational nudge, a traditional UI-based nudge, and a no-nudge control condition. Participants should be adult consumers recruited from a general online panel and randomly assigned to one of the three shopping environments. All participants should read the same scenario: they need a pair of wireless over-ear headphones for commuting, work, and casual listening and have a budget cap of $180. They should then evaluate the same six fictional headphone options, which vary on price, battery life, weight, active noise cancellation, microphone quality, comfort rating, and user rating.

The conversational-nudge condition should present a semi-structured assistant that asks a short sequence of preference questions and then recommends the balanced focal option, `VeroWave M6`, with brief comparative reasoning. The UI-based nudge condition should present the same focal option with static interface cues such as a `Best Match` badge, first-position placement, and a short recommendation note. The control condition should present the same product set without explicit recommendation cues. Holding the assortment constant while varying only the mode of guidance helps isolate whether conversational assistance changes the consumer decision process differently from a traditional UI nudge.

After reviewing the shopping environment, participants should indicate which option they would choose and report purchase likelihood. They should then complete post-task measures for perceived personalization, cognitive load, choice confidence, perceived transparency, and perceived decision quality, followed by secondary items on trust and satisfaction, manipulation checks, and a compact set of control variables. The empirical analysis should focus on two headline dependent variables, purchase likelihood and perceived decision quality, while testing whether the conversational condition operates through the proposed benefit and risk routes. The clearest first empirical specification is a dummy-coded condition model with an explicit conversational-versus-UI contrast and a path structure in which conversational guidance increases personalization, lowers cognitive load, and raises confidence while simultaneously decreasing perceived transparency.

The analysis should proceed in a staged but theory-aligned way. The first stage should test whether the conversational condition differs from both the control and UI-nudge conditions on the headline outcomes, purchase likelihood and perceived decision quality. The second stage should test whether the conversational condition increases perceived personalization and decreases perceived transparency relative to the comparison conditions. The third stage should test whether personalization predicts lower cognitive load, whether lower cognitive load predicts higher confidence, and whether transparency and confidence jointly predict perceived decision quality. If feasible, these relations should be estimated in a single bootstrapped path model with planned conversational-versus-UI contrasts reported explicitly. If not, the paper should preserve the same logic through staged regression and indirect-effect analyses rather than broadening the empirical design into an unfocused set of tests. This sequencing keeps the empirical section aligned with the paper's theoretical claim that conversational AI generates a support route and an opacity route at the same time.

### 19.5 Contribution
This working manuscript pass clarifies the paper's intended contribution more sharply than the earlier blueprint format. The paper contributes first by conceptualizing LLM-based conversational shopping assistants as a distinct form of AI nudge whose influence is enacted through adaptive dialogue rather than interface placement alone. It contributes second by identifying a mechanism-level tradeoff in which the same properties that make conversational AI feel useful and personalized may also reduce transparency in the recommendation process. More broadly, the paper links classic research on digital guidance and recommendation systems to newer conversational-AI contexts without treating AI shopping assistants as an isolated phenomenon disconnected from prior theory.

The empirical contribution also depends on matching the estimation strategy to the theoretical claim. For that reason, the study should not be framed as a simple omnibus comparison across three conditions. Instead, the analysis should foreground the theoretically central contrast between conversational guidance and static UI nudging while still retaining the no-nudge control as a baseline. The preferred interpretation is that conversational AI should outperform the UI nudge on the benefit route, underperform it on transparency, and produce a joint tradeoff in perceived decision quality. Presenting the results in that sequence will help the empirical section read as a theory test rather than as a broad set of condition comparisons.
