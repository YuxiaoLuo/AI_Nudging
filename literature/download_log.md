# Literature Download / File Log

## Standing rule for future literature review
Every time I do literature review for this project, I should update this file. If I identify relevant articles but cannot download valid PDFs, I should list them here clearly so Rain can review and add them manually.

## Request
Download the most relevant articles into the literature folder and rename them with the format:
`FirstAuthorLastName_AcronymJournalNameYear_SimplifiedTitle`

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

## Previously missing top-journal PDFs now added to the folder
These were previously identified as highly relevant and not retrievable in the earlier pass, but they have now been added to the literature folder:

- `Haubl_MktSci2000_InteractiveDecisionAids.pdf`
- `Ursu_MktSci2018_PowerOfRankings.pdf`
- `Wang_MgmtSci2018_RecommendationNeutralitySponsorshipDisclosure.pdf`
- `Wang_ISR2019_SponsorshipDisclosurePerceivedIntegrity.pdf`

## Previously missing supporting PDFs now added to the folder
These supporting but relevant publications were previously listed as not successfully downloaded, and have now been added to the literature folder:

- `Balakrishnan_AOR2024_ConversationalCommerceAIPoweredDigitalAssistants.pdf`
- `Chen_IntrRes2021_ConversationalAgentDecisionAidShoppingTask.pdf`
- `DeCicco_TFSC2022_BiasedChoicesVoiceAssistantsConversationalCommerce.pdf`
- `Chung_CHB2020_PersonalizationSocialRoleVoiceShopping.pdf`

## Removed out-of-scope paper
I double-checked `Ho_2025_System 2 & Confidence.pdf` and confirmed it was misaligned with this project. The local filename was misleading. Embedded PDF metadata showed that it was actually published in *Humanities and Social Sciences Communications*, not in JBR, and it is not part of the UTD24 or ABDC A* business-journal target set. I therefore removed it from the nudging project literature folder and dropped it from the usable anchor set.

## Additional relevant publications identified after the initial pass
These were identified as meaningfully relevant to the current theory direction and have now been added to the literature folder.

### Standing workflow note
Every time literature review is performed for this project, this file should be updated. Relevant articles that cannot be downloaded as valid PDFs should always be listed here for manual review and addition.

- Balakrishnan, J., & Dwivedi, Y. K. (2024). *Conversational commerce: entering the next stage of AI-powered digital assistants*. Annals of Operations Research.
  - added as: `Balakrishnan_AOR2024_ConversationalCommerceAIPoweredDigitalAssistants.pdf`
  - why it is relevant:
    - Useful high-level framing for conversational commerce as an emerging commerce architecture.
    - Better for motivation and phenomenon framing than for core causal theory.

- Chen, J. V., Le, H. T., & Tran, S. T. T. (2021). *Understanding automated conversational agent as a decision aid: matching agent's conversation with customer's shopping task*. Internet Research.
  - added as: `Chen_IntrRes2021_ConversationalAgentDecisionAidShoppingTask.pdf`
  - why it is relevant:
    - Very close to the project because it explicitly frames the conversational agent as a decision aid.
    - Strong bridge from classic decision-aid literature to conversational shopping support.

- de Cicco, R., Iacobucci, S., & Pagliaro, S. (2022). *Conversational commerce: Do biased choices offered by voice assistants’ technology constrain its appropriation?*. Technological Forecasting and Social Change.
  - added as: `DeCicco_TFSC2022_BiasedChoicesVoiceAssistantsConversationalCommerce.pdf`
  - why it is relevant:
    - Strong support for the risk side of the model, especially bias, constrained choice, and transparency concerns.

- Chung, M., Ko, E., Joung, H., & Kim, S. J. (2020). *Effects of personalization and social role in voice shopping: An experimental study on product recommendation by a conversational voice agent*. Computers in Human Behavior.
  - added as: `Chung_CHB2020_PersonalizationSocialRoleVoiceShopping.pdf`
  - why it is relevant:
    - Strong support for the personalization benefit path in conversational shopping.

## Newly identified relevant articles not yet added in this pass
These look significant and relevant enough to track for manual review or later collection.

### New manual-follow-up candidates from this literature pass
I ran another stricter pass focused on strengthening the recommendation-agent bridge between early decision aids and later disclosure/transparency work. Metadata verification worked, but the direct PDF URLs I tested returned `403` HTML pages rather than valid PDFs, so I did **not** keep any of those files.

- Xiao, B., & Benbasat, I. (2007). *E-Commerce Product Recommendation Agents: Use, Characteristics, and Impact*. MIS Quarterly. https://doi.org/10.2307/25148784
  - why it is relevant:
    - Strong bridge paper for the middle layer of the theory section.
    - Helps define what recommendation agents do before the later transparency and disclosure literature.

- Wang, W., & Benbasat, I. (2008). *Attributions of Trust in Decision Support Technologies: A Study of Recommendation Agents for E-Commerce*. Journal of Management Information Systems. https://doi.org/10.2753/MIS0742-1222240410
  - why it is relevant:
    - Sharpens the trust-attribution logic behind recommendation-agent use.
    - Useful for explaining why conversational AI may change not only usefulness judgments but also the basis of trust.

- Wang, W., & Benbasat, I. (2016). *Empirical Assessment of Alternative Designs for Enhancing Different Types of Trusting Beliefs in Online Recommendation Agents*. Journal of Management Information Systems. https://doi.org/10.1080/07421222.2016.1243949
  - why it is relevant:
    - Supports the argument that design choices in recommendation agents systematically affect trusting beliefs.
    - Useful support for a design-sensitive conversational-AI framing.

- Ebrahimi, S., Ghasemaghaei, M., & Benbasat, I. (2022). *The Impact of Trust and Recommendation Quality on Adopting Interactive and Non-Interactive Recommendation Agents: A Meta-Analysis*. Journal of Management Information Systems. https://doi.org/10.1080/07421222.2022.2096549
  - why it is relevant:
    - Especially useful because it explicitly distinguishes interactive from non-interactive recommendation agents.
    - Strong support for treating conversational AI as more than a stronger static recommender.

### Previously resolved missing set
The five previously missing papers below have now been added to the literature folder:
- `Wang_JMIS2007_ExplanationFacilitiesTrustingBeliefs.pdf`
- `Senecal_JRetailing2004_OnlineProductRecommendationsChoices.pdf`
- `Yalcin_JMR2022_ConsumerReactionsAlgorithmsVersusHumans.pdf`
- `Longoni_JCR2019_ResistanceToMedicalAI.pdf`
- `Luo_MktSci2019_ChatbotDisclosureCustomerPurchases.pdf`

## Recommended next step
Keep using this file to track newly identified but unavailable articles in future literature-review passes.
