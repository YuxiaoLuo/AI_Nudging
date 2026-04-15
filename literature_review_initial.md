# Initial Literature Review Notes: LLM Conversational Nudges vs. Algorithmic Recommendation Badges

## 1. Why LLM conversational nudges are different from recommendation badges

### Recommendation badges and rankings
Recommendation badges, rankings, and similar interface cues work mainly through **salience, ordering, and heuristic signaling**. They are typically embedded in the interface as visual markers such as “Best Seller,” “Top Pick,” “Recommended,” or ranked product ordering. These mechanisms influence what consumers notice first, what they search next, and sometimes which options they consider. In this sense, they are classic forms of digital choice architecture.

### LLM conversational nudges
LLM-driven conversational nudges operate differently. Instead of merely highlighting or ranking products, they can:
- interpret user goals in natural language
- guide the user through a sequence of questions and comparisons
- adapt recommendations across turns
- frame reasons for a choice
- selectively emphasize product attributes
- potentially reshape preferences during the interaction

This makes conversational nudges more than a visual salience cue. They are closer to a hybrid of recommendation agent, advisor, and persuasive interface. Their influence is dynamic, iterative, and often more opaque.

### Preliminary differentiating dimensions
1. **Mode of delivery**
   - Badge: interface-level visual cue
   - LLM nudge: conversational guidance delivered through dialogue

2. **Temporal structure**
   - Badge: usually one-shot exposure at a page or product-list level
   - LLM nudge: multi-turn, sequential, path-dependent interaction

3. **Adaptivity**
   - Badge: generally fixed for a given context
   - LLM nudge: adaptive to user inputs and evolving stated preferences

4. **Perceived agency**
   - Badge: low social presence
   - LLM nudge: higher agency, anthropomorphism, and perceived intelligence

5. **Mechanism transparency**
   - Badge: users often infer a simple cue even if underlying logic is hidden
   - LLM nudge: recommendation logic is much harder to reconstruct

6. **Potential influence scope**
   - Badge: affects attention, search, and consideration
   - LLM nudge: may affect attention, search, confidence, trust, preference formation, and final choice justification

## 2. Early anchor papers from target journal pools

### UTD24 / closely relevant top journals

1. **Häubl, G., & Trifts, V. (2000). Consumer Decision Making in Online Shopping Environments: The Effects of Interactive Decision Aids. Marketing Science.**
   - Link: https://pubsonline.informs.org/doi/10.1287/mksc.19.1.4.15178
   - Why it matters: foundational paper showing how interactive decision aids change search effort, consideration set quality, and purchase decision quality in online shopping.
   - Relevance here: excellent anchor for arguing that conversational AI nudges are not merely display cues but a stronger form of interactive decision aid.

2. **Ursu, R. M. (2018). The Power of Rankings: Quantifying the Effect of Rankings on Online Consumer Search and Purchase Decisions. Marketing Science.**
   - Link: https://pubsonline.informs.org/doi/10.1287/mksc.2017.1072
   - Why it matters: shows that rankings affect search behavior and lower search costs.
   - Relevance here: strong anchor for the badge/ranking side of the comparison. Helps show that traditional recommendation cues influence search, whereas LLM conversational nudges may additionally shape confidence, trust, and preference articulation.

3. **Compiani, G., Lewis, G., Peng, S., & Wang, P. (2023). Online Search and Optimal Product Rankings: An Empirical Framework. Marketing Science.**
   - Link: https://pubsonline.informs.org/doi/10.1287/mksc.2022.0071
   - Why it matters: frames rankings as a platform design problem balancing consumer surplus and platform goals.
   - Relevance here: useful for discussing platform incentives and responsible design in LLM-mediated shopping.

4. **Wang, W., Xu, J. D., & Wang, M. (2018). Effects of Recommendation Neutrality and Sponsorship Disclosure on Trust vs. Distrust in Online Recommendation Agents: Moderating Role of Explanations for Organic Recommendations. Management Science.**
   - Link: https://pubsonline.informs.org/doi/10.1287/mnsc.2017.2906
   - Why it matters: directly studies biased recommendation agents, trust/distrust, sponsorship disclosure, and explanations.
   - Relevance here: extremely important for your project because it gives a top-journal bridge from recommendation agents to transparency, trust, and hidden influence, all of which matter even more for LLM nudges.

5. **Wang, W., & Wang, M. (2019). Effects of Sponsorship Disclosure on Perceived Integrity of Biased Recommendation Agents: Psychological Contract Violation and Knowledge-Based Trust Perspectives. Information Systems Research.**
   - Link: https://pubsonline.informs.org/doi/10.1287/isre.2018.0811
   - Why it matters: shows that disclosure can improve perceived transparency and integrity, with psychological contract violation as a core mechanism.
   - Relevance here: highly relevant for theorizing opacity and integrity perceptions of conversational AI recommendations.

6. **Kaliyamurthy, A. K., & Schau, H. J. (2025). How Algorithms Constrain Consumer Experience. Journal of Consumer Research.**
   - Link: https://academic.oup.com/jcr/article-abstract/52/4/826/8101497
   - Why it matters: conceptualizes how algorithms constrain consumer experience through algorithmic logics.
   - Relevance here: valuable high-level consumer theory anchor on how algorithmic systems shape experience beyond choice outcomes.

### ABDC A* / strong adjacent business journals

7. **Aksoy, L., Bloom, P. N., Lurie, N. H., & Cooil, B. (2006). Should Recommendation Agents Think Like People? Journal of Service Research.**
   - Link: https://journals.sagepub.com/doi/10.1177/1094670506286326
   - Why it matters: shows that recommendation-agent similarity to consumer decision strategy affects choice quality.
   - Relevance here: useful for arguing that conversational AI may feel closer to a human-like advisor than a badge or ranking cue.

8. **Huseynov, F., Huseynov, S. Y., & Özkan, S. (2016). The influence of knowledge-based e-commerce product recommender agents on online consumer decision-making. Journal of Information Technology.**
   - Link: https://journals.sagepub.com/doi/10.1177/0266666914528929
   - Why it matters: shows recommender agents can reduce effort and improve decision outcomes.
   - Relevance here: useful adjacent evidence that more agentic recommendation tools do more than highlight options.

## 3. Emerging gap statement
The current literature gives you strong pieces on:
- rankings and recommendation badges affecting search and consideration
- recommendation agents influencing trust, integrity, and disclosure effects
- interactive decision aids improving efficiency and decision quality
- algorithmic systems shaping consumer experience more broadly

But the gap is still clear:
**We do not yet have strong business-journal evidence that compares LLM-based conversational nudges against traditional UI-based recommendation cues as distinct forms of choice architecture in e-commerce.**

That is the paper’s sweet spot.

## 4. How this can shape the paper
A stronger paper may position the comparison like this:
- **Badges/rankings** primarily alter what is salient and what gets searched.
- **Recommendation agents** assist evaluation and can raise trust/transparency issues.
- **LLM conversational nudges** add a new layer: dynamic, adaptive, language-based steering that can influence not only search and evaluation but also confidence, perceived personalization, trust, and possibly preference formation itself.

## 5. Recommended next literature review steps
1. Build a reading matrix with columns for:
   - citation
   - journal
   - context
   - focal technology
   - theory
   - method
   - key dependent variables
   - key findings
   - direct relevance to this project

2. Expand the review in these business-journal directions:
   - conversational commerce
   - chatbot persuasion and trust in shopping
   - AI transparency and explainability in consumer contexts
   - decision quality and cognitive load in online shopping

3. Separate the literature into two comparison baselines:
   - UI-based nudges / rankings / badges
   - agentic or conversational recommendation systems

4. Use the distinction above to sharpen the paper’s contribution claim.
