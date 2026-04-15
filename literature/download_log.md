# Literature Download / File Log

## Request
Download the most relevant articles into the literature folder and rename them with the format:
`FirstAuthorLastName_AcronymJournalName_SimplifiedTitle`

## What happened
I attempted direct publisher-PDF downloads for several top-journal anchor papers, including papers from Marketing Science, Management Science, Information Systems Research, and European Journal of Information Systems. Those requests returned HTML landing pages rather than usable PDF files, so I removed the bad files instead of leaving misleading fake PDFs in the folder.

## Valid renamed copies created from existing local files
The following files were created as clean renamed copies from papers already present in the workspace literature folder:

- `Michels_EJIS_SalienceTransparencySelfNudging.pdf`
  - source: `Michelsetal_EJIS2023_Salience Transparency & Self-nudging healtyhy food.pdf`

- `Xiao_DSS_BiasedRecommendationAgents.pdf`
  - source: `Xiao&Benbasat_DSS2018_Biased RA.pdf`

- `Pecune_FrontRobotAI_FoodConversationalAgentNudging.pdf`
  - source: `Pecune_2022_food conversational agent and nudging.pdf`

- `Guo_JRetailingConsumerServices_ChatbotPersonasFoodChoice.pdf`
  - source: `Guo&Wan_2025_Chatbot personas and food choice.pdf`


- `Luo_DSS_AINudgingDecisionQuality.pdf`
  - source: `Luo_DSS2026_ai nudging and decision quality.pdf`

## Not successfully downloaded as PDFs in this pass
These were identified as highly relevant, but direct download did not yield valid PDFs with the tools available in this environment:

- Häubl & Trifts (2000), Marketing Science
- Ursu (2018), Marketing Science
- Wang, Xu, & Wang (2018), Management Science
- Wang & Wang (2019), Information Systems Research

## Most relevant missing top-journal PDFs
These are the highest-priority papers that I double-checked and still identified as especially important for the project, but could not download as valid PDFs in this environment.

- Häubl, G., & Trifts, V. (2000). *Consumer Decision Making in Online Shopping Environments: The Effects of Interactive Decision Aids*. Marketing Science.
  - intended filename: `Haubl_MktSci_InteractiveDecisionAids.pdf`
  - why it is relevant:
    - This is a foundational online-shopping paper on interactive decision aids, specifically a recommendation agent and a comparison matrix.
    - The paper shows that stronger digital aids can reduce search effort, improve consideration set quality, and improve purchase decision quality.
    - It matters here because it gives the baseline argument that online choice architecture can shape the **decision process**, not just the final click or purchase.
    - It is especially useful for distinguishing LLM conversational nudges from simple badges: LLM nudges may be framed as a new generation of interactive decision aid, but one that is more adaptive, dialogic, and opaque.

- Ursu, R. M. (2018). *The Power of Rankings: Quantifying the Effect of Rankings on Online Consumer Search and Purchase Decisions*. Marketing Science.
  - intended filename: `Ursu_MktSci_PowerOfRankings.pdf`
  - why it is relevant:
    - This is the clearest top-journal baseline for ranking-based choice architecture in e-commerce-like search settings.
    - The paper shows that rankings affect what consumers search, and attributes much of their effect to lowered search costs rather than deeper changes in utility.
    - It matters because your project needs a strong comparison point for algorithm-generated badges and rankings.
    - It helps support the claim that badge/ranking nudges mainly alter **attention and search order**, whereas LLM conversational nudges may also alter confidence, evaluation, and preference articulation.

- Wang, W., Xu, J. D., & Wang, M. (2018). *Effects of Recommendation Neutrality and Sponsorship Disclosure on Trust vs. Distrust in Online Recommendation Agents: Moderating Role of Explanations for Organic Recommendations*. Management Science.
  - intended filename: `Wang_MgmtSci_RecommendationNeutralitySponsorshipDisclosure.pdf`
  - why it is relevant:
    - This paper directly studies online recommendation agents rather than simple interface cues.
    - It shows that bias, sponsorship disclosure, and explanations shape trust and distrust differently.
    - It matters because LLM shopping assistants will likely be perceived as recommendation agents with even greater agency and opacity than classic recommenders.
    - It is a strong bridge paper from recommendation systems to your core themes of trust, opacity, explanation, and hidden persuasive influence.

- Wang, W., & Wang, M. (2019). *Effects of Sponsorship Disclosure on Perceived Integrity of Biased Recommendation Agents: Psychological Contract Violation and Knowledge-Based Trust Perspectives*. Information Systems Research.
  - intended filename: `Wang_ISR_SponsorshipDisclosurePerceivedIntegrity.pdf`
  - why it is relevant:
    - This paper focuses on perceived integrity, transparency, sponsorship disclosure, and psychological contract violation in biased recommendation agents.
    - It matters because your project likely hinges on a similar issue: conversational AI may be helpful and persuasive, but users may not clearly understand whose interests the system is serving or how its recommendations are produced.
    - The paper is especially valuable if your model includes perceived transparency, integrity, or trust as mediators or tradeoff variables.
    - It provides a rigorous top-journal mechanism for thinking about why opaque recommendation systems can influence user evaluations even when the system appears helpful.

## Removed out-of-scope paper
I double-checked `Ho_2025_System 2 & Confidence.pdf` and confirmed it was misaligned with this project. The local filename was misleading. Embedded PDF metadata showed that it was actually published in *Humanities and Social Sciences Communications*, not in JBR, and it is not part of the UTD24 or ABDC A* business-journal target set. I therefore removed it from the nudging project literature folder and dropped it from the usable anchor set.

## Recommended next step
If you have institutional access through a browser session, the fastest path is to download those missing articles manually or place them in the folder, and I can immediately rename and organize them to match the naming convention.
