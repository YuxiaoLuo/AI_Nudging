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

## 2026-06-22 bridge-citation archive check
I revisited the two remaining bridge citations that are already used in the manuscript but still lack authoritative local PDFs:

- Xiao, B., & Benbasat, I. (2007). *E-Commerce Product Recommendation Agents: Use, Characteristics, and Impact*. MIS Quarterly. https://doi.org/10.2307/25148784
- Ebrahimi, S., Ghasemaghaei, M., & Benbasat, I. (2022). *The Impact of Trust and Recommendation Quality on Adopting Interactive and Non-Interactive Recommendation Agents: A Meta-Analysis*. Journal of Management Information Systems. https://doi.org/10.1080/07421222.2022.2096549

What I verified:
- Both citations remain bibliographically confirmed in the local project records, including `literature_reading_matrix.md` and the manuscript-side citation files.
- A direct MIS Quarterly PDF route for Xiao and Benbasat (2007) is discoverable on the open web, but requests from this environment returned `403 Forbidden`, so I could not archive a valid PDF.
- The live JMIS article page for Ebrahimi et al. (2022) is reachable, but no directly downloadable PDF was exposed through the page from this environment, and alternate routes tested here also failed to yield a valid PDF.
- ResearchGate and similar alternate-access routes also did not provide a clean downloadable PDF from this environment.

Outcome:
- Keep both papers on the `citation confirmed but local PDF not yet archived` list.
- Do not treat nearby local placeholder files as authoritative substitutes.

Manual-access routes worth keeping for a later retrieval attempt:
- Xiao and Benbasat (2007):
  - MIS Quarterly PDF route surfaced by search: `https://misq.umn.edu/misq/article-pdf/31/1/137/5188/7_xiaobenbasat.pdf`
  - ResearchGate full-text page surfaced by search: `https://www.researchgate.net/publication/220260358_E-Commerce_Product_Recommendation_Agents_Use_Characteristics_and_Impact`
- Ebrahimi et al. (2022):
  - Taylor & Francis PDF route surfaced by search: `https://www.tandfonline.com/doi/pdf/10.1080/07421222.2022.2096549`
  - Taylor & Francis abstract page surfaced by search: `https://www.tandfonline.com/doi/abs/10.1080/07421222.2022.2096549`
  - ResearchGate article page surfaced by search: `https://www.researchgate.net/publication/363016491_The_Impact_of_Trust_and_Recommendation_Quality_on_Adopting_Interactive_and_Non-Interactive_Recommendation_Agents_A_Meta-Analysis`

## 2026-06-22 late-day bridge-citation retrieval recheck
Purpose of this pass:
- Recheck whether the two remaining bridge citations could now be archived as valid PDFs from stronger direct routes than the earlier abstract-page checks.

What I tested:
- Xiao and Benbasat (2007):
  - MIS Quarterly direct PDF route: `https://misq.umn.edu/misq/article-pdf/31/1/137/5188/7_xiaobenbasat.pdf`
  - JSTOR direct PDF route surfaced by web search: `https://www.jstor.org/stable/pdf/25148784.pdf`
- Ebrahimi et al. (2022):
  - Taylor & Francis direct PDF route surfaced by web search: `https://www.tandfonline.com/doi/pdf/10.1080/07421222.2022.2096549`
  - ResearchGate full-text pages for both papers

What happened:
- The MIS Quarterly direct PDF route for Xiao and Benbasat (2007) now resolves to a Cloudflare-protected `403` challenge page from this environment rather than a downloadable PDF.
- The JSTOR direct PDF route for Xiao and Benbasat (2007) also resolves to a `403` access-denied page from this environment.
- The Taylor & Francis direct PDF route for Ebrahimi et al. (2022) resolves to a Cloudflare-protected `403` challenge page from this environment.
- ResearchGate requests for both papers also returned `403` responses from this environment rather than full-text downloads.

Updated judgment:
- The remaining gap is now even more clearly an environment-level access or anti-bot constraint rather than uncertainty about the most relevant PDF endpoints.
- Keep both citations on the `citation confirmed but local PDF not yet archived` list.
- If Rain later wants these files added, the best next move is likely a manual browser/institutional-library retrieval from one of the direct PDF routes above rather than another discovery pass.

## 2026-04-22 request: Marketing Science paper on ChatGPT referrals
Requested paper:
- Kaiser, M., & Schulze, C. (2026). *Frontiers: ChatGPT Referrals to E-Commerce Websites: How Do LLMs Compare Against Traditional Channels?* Marketing Science. DOI: https://doi.org/10.1287/mksc.2025.0489

What I verified:
- OpenAlex lists this article as published in *Marketing Science* on 2026-04-21.
- OpenAlex marks it as closed access with no open-access PDF or repository full text currently available.
- A direct attempt to fetch the publisher PDF returned a Cloudflare challenge HTML page instead of a valid PDF, so I removed the bad file rather than keeping a fake PDF.

Status:
- Not successfully downloaded as a valid PDF in this pass.
- Needs manual access via institution/library, publisher site, or author-shared copy if Rain wants the full text added.

## 2026-05-25 narrow construct-anchor follow-up
Purpose of this pass:
- Check whether the remaining weak constructs in the current manuscript, especially choice confidence and perceived decision quality, require another targeted literature-collection step before the project moves from blueprint refinement into a cleaner manuscript-file workflow.

## 2026-06-23 early-morning bridge-citation PDF endpoint recheck
Purpose of this pass:
- Recheck whether the two remaining missing bridge citations could be archived by hitting their most PDF-like public endpoints with a browser user agent rather than only relying on abstract pages or search snippets.

What I tested:
- Xiao and Benbasat (2007):
  - MIS Quarterly PDF endpoint with browser user agent:
    - `https://misq.umn.edu/misq/article-pdf/31/1/137/5188/7_xiaobenbasat.pdf`
- Ebrahimi et al. (2022):
  - Taylor & Francis PDF endpoint with browser user agent and explicit download parameter:
    - `https://www.tandfonline.com/doi/pdf/10.1080/07421222.2022.2096549?download=true`
- I also rechecked the JMIS mirror page for Ebrahimi et al. (2022):
  - `https://www.jmis-web.org/articles/1583`

What happened:
- Both PDF-looking vendor endpoints returned HTML documents rather than valid PDFs when fetched from this environment, even with a browser user agent.
- The Xiao and Benbasat (2007) MISQ endpoint saved an HTML page beginning with `<!DOCTYP` rather than `%PDF`.
- The Ebrahimi et al. (2022) Taylor & Francis `?download=true` route also saved an HTML page beginning with `<!DOCTYP` rather than `%PDF`.
- The JMIS mirror page for Ebrahimi et al. (2022) remains useful for metadata and abstract verification, but it still does not expose a downloadable PDF route from this environment.

Updated judgment:
- The remaining archive gap is still an access-context problem rather than a source-discovery problem.
- Even the most direct PDF-style endpoints currently reachable from search should not be trusted unless the fetched file is validated as a real PDF.
- Keep both citations on the `bibliographically confirmed but authoritative local PDF not yet archived` list.

## 2026-06-23 browser-header endpoint retry
Purpose of this pass:
- Recheck the same two remaining bridge citations with a narrower `browser-like request` test from the shell, using explicit PDF-friendly `Accept` headers and site referers, to see whether the earlier failures were caused only by missing browser headers.

What I tested:
- Xiao and Benbasat (2007):
  - MIS Quarterly PDF endpoint with browser-style headers:
    - `https://misq.umn.edu/misq/article-pdf/31/1/137/5188/7_xiaobenbasat.pdf`
- Ebrahimi et al. (2022):
  - Taylor & Francis PDF endpoint with browser-style headers:
    - `https://www.tandfonline.com/doi/pdf/10.1080/07421222.2022.2096549?download=true`

What happened:
- Both endpoints again saved HTML documents rather than real PDFs.
- The Xiao fetch produced an HTML file of 5,614 bytes beginning with `<!DOCTYPE html>`.
- The Ebrahimi fetch produced an HTML file of 5,685 bytes beginning with `<!DOCTYPE html>`.
- That means the failure is not just `missing browser headers`; the environment still cannot obtain valid PDFs from those routes.

Updated judgment:
- The remaining archive gap is now even more clearly an access-context issue rather than a malformed-request issue.
- Future retries should avoid repeating the same shell-level header experiment unless the access context changes materially.
- Keep both citations on the `bibliographically confirmed but authoritative local PDF not yet archived` list.

## 2026-07-01 direct-endpoint recheck
Purpose of this pass:
- Recheck whether the two remaining bridge citations could now be archived from the clearest direct PDF endpoints surfaced by current web search, without broadening the literature scope again.

What I tested:
- Xiao and Benbasat (2007):
  - MIS Quarterly direct PDF route surfaced again by search:
    - `https://misq.umn.edu/misq/article-pdf/31/1/137/5188/7_xiaobenbasat.pdf`
- Ebrahimi et al. (2022):
  - Taylor & Francis direct PDF route surfaced again by search:
    - `https://www.tandfonline.com/doi/pdf/10.1080/07421222.2022.2096549`

What happened:
- Both direct endpoints returned `403 Forbidden` from this environment during a fresh shell-level fetch on 2026-07-01.
- No valid `%PDF-` signature was retrievable from either route in this pass.
- This means the two strongest publisher-style routes remain blocked here even when rediscovered through current search, so the retry did not change archive status.

Updated judgment:
- The archive gap still reflects environment-level access constraints rather than uncertainty about the correct papers or likely PDF routes.
- Further retries should focus only on materially different access contexts, such as a manual browser or institutional-library session, rather than repeated shell fetches of the same endpoints.
- Keep both citations on the `bibliographically confirmed but authoritative local PDF not yet archived` list.

## 2026-07-01 repository-route distinction recheck
Purpose of this pass:
- Check whether the two remaining missing bridge citations differ meaningfully in repository or author-hosted access state, rather than treating both as the same generic `publisher blocked` case.

What I verified:
- Xiao and Benbasat (2007):
  - the ResearchGate article page currently exposes a public full-text view and labels the article `PDF Available`
  - the page text shows the article content directly and indicates author-uploaded content by Bo Xiao
  - however, the direct PDF fetch path still did not yield a locally archived file in this environment, so the project still lacks an authoritative local PDF copy
- Ebrahimi et al. (2022):
  - the ResearchGate article page currently shows `Request full-text PDF` and `No full-text available`
  - the page exposes the abstract and metadata, but not a public downloadable full text

Updated judgment:
- The two remaining archive gaps are now more clearly different:
  - Xiao and Benbasat (2007) appears to have a publicly readable repository-hosted full text, but the project still lacks a successfully archived local PDF from this environment
  - Ebrahimi et al. (2022) still has no publicly exposed full-text route visible from the repository page, so the gap remains closer to `metadata confirmed, no OA full text exposed here`
- Keep both citations on the `bibliographically confirmed but authoritative local PDF not yet archived` list.
- If Rain later wants a manual retrieval attempt, Xiao and Benbasat (2007) is now the stronger candidate for a browser-based save or author-page retrieval before trying Ebrahimi et al. (2022) again.

## 2026-07-01 narrow anchor-placement follow-up
Purpose of this pass:
- Resolve one remaining manuscript-facing literature question without reopening broad source collection: whether Yalcin et al. (2022) or Longoni et al. (2019) should now move into the manuscript's compact core anchor set.

What I checked:
- The current `literature_reading_matrix.md` entries for both papers.
- The current `literature_synthesis_memo.md` anchor map and boundary-citation logic.
- The local literature folder to confirm both papers are already archived here as:
  - `Yalcin_JMR2022_ConsumerReactionsAlgorithmsVersusHumans.pdf`
  - `Longoni_JCR2019_ResistanceToMedicalAI.pdf`

What changed:
- No new PDF downloads were needed in this pass.
- The current evidence base is now strong enough to resolve the placement question directly from the project's existing synthesis materials and archived copies.

Updated judgment:
- Keep **Yalcin et al. (2022)** as a supporting citation on reactions to algorithmic decision makers rather than promoting it into the compact core set.
- Keep **Longoni et al. (2019)** as a boundary-condition citation on resistance to AI advice rather than promoting it into the compact core set.
- The reason is not quality; both are useful high-prestige consumer-AI papers. The reason is fit: neither one is centered on shopping guidance, recommendation-agent explanation design, or commerce-facing disclosure in the way the current core anchor set is.
- Promoting either paper into the compact core would widen the manuscript away from the tighter commerce-specific support-versus-transparency argument that currently reads most defensibly.

What I checked:
- A narrow search focused on chatbot or conversational-agent work related to consumer confidence, decision quality, and AI-assisted shopping decisions.

What this pass clarified:
- I did not identify a clearly stronger core anchor that changes the current compact source strategy.
- The best additional candidates I found appear more useful as supporting citations than as core construct anchors.
- This means the current manuscript can keep moving forward without pausing for a larger literature-expansion step.

Relevant candidates identified in this pass:
- Fan, X., Chai, Y., Deng, N., & Dong, X. (2022). *AI is better when I'm sure: The influence of certainty of needs on consumers' acceptance of AI chatbots*. Journal of Business Research. https://doi.org/10.1016/j.jbusres.2022.06.044
  - why it is relevant:
    - Useful support for chatbot effectiveness and the role of consumer need certainty.
    - Not a clean core anchor for choice confidence in the present model because the article centers more on chatbot acceptance and perceived effectiveness than on confidence as the focal post-choice construct.

- Mimoun, M. S. B., Poncin, I., & Garnier, M. (2015). *A valued agent: How ECAs affect website customers' satisfaction and behaviors*. Journal of Retailing and Consumer Services. https://doi.org/10.1016/j.jretconser.2015.05.008
  - why it is relevant:
    - Useful supporting citation because it treats decision quality as one of the consequences of interacting with a conversational agent in an e-commerce environment.
    - Not strong enough to displace the current tighter logic for perceived decision quality, because the paper is not the kind of compact, high-leverage core anchor that would materially restructure the argument.

- Meng, K., & Xiao, J. J. (2026). *Can ChatGPT relate to you? Exploring consumer satisfaction with AI-generated product advice through the lens of consumption values*. Journal of Retailing and Consumer Services. ideas.repec.org record surfaced in search.
  - why it is relevant:
    - Potentially useful contemporary support for AI-generated product advice and consumer evaluation.
    - Not necessary for the current draft's core mechanism claims, and not a decisive anchor for the remaining construct-definition gap.

Bottom-line judgment from this pass:
- No critical literature gap was found that should block the project from shifting into manuscript consolidation and prose cleanup.
- If a later revision still needs more explicit support, the JBR and JRCS papers above can be cited as secondary reinforcement rather than promoted into the compact core anchor set.

## 2026-06-23 late-night open-route recheck for the two remaining bridge PDFs
Purpose of this pass:
- Test whether the two remaining missing bridge citations now have materially different open or repository-hosted routes worth archiving, rather than repeating the same blocked publisher-PDF endpoints.

What I tested:
- Xiao and Benbasat (2007):
  - a CORE-hosted PDF route surfaced by web search:
    - `https://files01.core.ac.uk/download/pdf/16699406.pdf`
- Ebrahimi et al. (2022):
  - OpenAlex metadata lookup for DOI `10.1080/07421222.2022.2096549`
  - targeted web search for alternate public PDF routes

What happened:
- The Xiao CORE-hosted candidate returned `403 Forbidden` from this environment rather than a downloadable PDF.
- The Ebrahimi OpenAlex record confirms the citation metadata cleanly, but reports `is_oa: false`, `oa_url: null`, and `pdf_url: null`, so there is still no registered open-access PDF route.
- The targeted Ebrahimi web search did not surface a cleaner public PDF host than the already-failed Taylor & Francis and ResearchGate-style routes.

Updated judgment:
- The remaining two-PDF archive gap is still an access-context problem, not a discovery problem.
- Xiao and Benbasat (2007) does have at least one non-publisher route discoverable on the open web, but that route is also blocked from this environment and should not be treated as a usable archive source here.
- Ebrahimi et al. (2022) is now even more clearly a `metadata confirmed, no open PDF exposed` case rather than one where another shell-level vendor retry is likely to help.
- Keep both citations on the `bibliographically confirmed but authoritative local PDF not yet archived` list unless the access context changes materially.

## 2026-07-02 targeted archive-note recheck for the two remaining bridge PDFs
Purpose of this pass:
- Test whether the remaining bridge-source gap has changed materially enough to justify another direct archive attempt, rather than assuming the prior blocked routes still describe the current state.

What I checked:
- Xiao and Benbasat (2007):
  - current local archive and crosswalk state only, to decide whether a new shell-level retry was likely to add anything beyond the existing `publicly readable repository full-text view` note
- Ebrahimi et al. (2022):
  - fresh open-web search results for DOI `10.1080/07421222.2022.2096549`
  - whether the live article-page snippets now signal a clearer PDF route than the earlier Taylor & Francis / ResearchGate checks

What happened:
- The Xiao state did not materially change: it remains the stronger manual-retrieval candidate, but the project still has no successfully archived local PDF from this environment.
- The Ebrahimi search results again surfaced the Taylor & Francis PDF route and article page, and the page snippets now make the access-context issue slightly sharper because they explicitly advertise `View PDF` / `Download PDF` while still not yielding a usable public PDF route here.
- No new open-access host or repository mirror surfaced for Ebrahimi beyond the already logged Taylor & Francis and ResearchGate-style routes.

Updated judgment:
- The remaining archive gap is still better understood as `route known, access context blocks retrieval` than as `citation found but full-text route unknown`.
- Xiao and Benbasat (2007) remains the more plausible candidate for a later manual browser save or alternate-environment retrieval.
- Ebrahimi et al. (2022) now looks even less like a discovery problem: the page advertises a PDF route, but the route still appears to be access-gated from this environment rather than absent.

## 2026-07-02 canonical-endpoint retrieval recheck for the two remaining bridge PDFs
Purpose of this pass:
- Re-test the exact canonical publisher-side PDF routes for the two remaining bridge citations so the archive notes reflect current endpoint behavior rather than only search-result snippets or older inferred routes.

What I checked:
- Xiao and Benbasat (2007):
  - exact MIS Quarterly PDF route from current web search:
    - `https://misq.umn.edu/misq/article-pdf/31/1/137/5188/7_xiaobenbasat.pdf`
  - JSTOR PDF route:
    - `https://www.jstor.org/stable/pdf/25148784.pdf`
- Ebrahimi et al. (2022):
  - Taylor & Francis canonical PDF route:
    - `https://www.tandfonline.com/doi/pdf/10.1080/07421222.2022.2096549`
  - Taylor & Francis abstract route:
    - `https://www.tandfonline.com/doi/abs/10.1080/07421222.2022.2096549`

What happened:
- The exact MIS Quarterly Xiao PDF route returned an HTTP `403` Cloudflare challenge page from this environment.
- Saving that MISQ route with browser-style headers still produced an HTML file beginning with `<!DOCTYPE html>` rather than a real `%PDF-` file.
- The JSTOR Xiao PDF route also returned HTTP `403`.
- The Taylor & Francis Ebrahimi PDF route returned HTTP `403` and saved an HTML challenge page rather than a real PDF.
- The Taylor & Francis abstract route also resolved to a `Just a moment...` Cloudflare challenge page rather than a readable article page from this environment.

Updated judgment:
- The two remaining archive gaps are now confirmed at the canonical endpoint level rather than only at the snippet or alternate-route level.
- Xiao and Benbasat (2007) still has the stronger downstream manual-retrieval story because the citation is exact and the ResearchGate record advertises full text, but the canonical MISQ and JSTOR PDF routes remain blocked here.
- Ebrahimi et al. (2022) is now even more clearly an access-context problem: both the canonical Taylor & Francis PDF and abstract routes are challenge-gated from this environment.
- Keep both citations on the `bibliographically confirmed but authoritative local PDF not yet archived` list.

## 2026-07-06 late-night direct-PDF route recheck
Purpose of this pass:
- Recheck the two remaining unresolved bridge PDFs from the current environment using the clearest direct PDF routes surfaced by current web search, and sharpen the manual-retrieval notes if the files still cannot be archived here.

What I tested:
- Xiao and Benbasat (2007):
  - MIS Quarterly direct PDF route:
    - `https://misq.umn.edu/misq/article-pdf/31/1/137/5188/7_xiaobenbasat.pdf`
  - JSTOR direct PDF route surfaced again by search:
    - `https://www.jstor.org/stable/pdf/25148784.pdf`
- Ebrahimi et al. (2022):
  - Taylor & Francis direct PDF route:
    - `https://www.tandfonline.com/doi/pdf/10.1080/07421222.2022.2096549`

What happened:
- The MIS Quarterly Xiao PDF route returned HTTP `403` with a Cloudflare challenge page from this environment.
- The JSTOR Xiao PDF route also returned HTTP `403` from this environment. This route is still worth preserving because it is a stable article-specific PDF endpoint and may be the cleanest browser-side retrieval candidate if access context changes.
- The Taylor & Francis Ebrahimi PDF route again returned HTTP `403` with a Cloudflare challenge page from this environment.

Updated judgment:
- No authoritative local PDF could be archived in this pass.
- Xiao and Benbasat (2007) now has two exact article-specific PDF endpoints logged (`MISQ` and `JSTOR`), which sharpens the later manual-retrieval path even though both are blocked here.
- Ebrahimi et al. (2022) remains an access-context problem rather than a source-discovery problem; the known Taylor & Francis PDF route is exact, but still challenge-gated from this environment.

## 2026-08-30 alternate-route retrieval check
Purpose of this pass:
- Test whether a materially different retrieval route now works for the two remaining bridge citations, rather than repeating only the already-known publisher PDF endpoints.

What I tested:
- Xiao and Benbasat (2007):
  - an older direct ResearchGate PDF path surfaced indirectly through a later citing PDF:
    - `https://www.researchgate.net/profile/Bo_Xiao12/publication/220260358_E-Commerce_Product_Recommendation_Agents_Use_Characteristics_and_Impact/links/0deec53a01d3bd194f000000/E-Commerce-Product-Recommendation-Agents-Use-Characteristics-and-Impact.pdf`
- Ebrahimi et al. (2022):
  - Taylor & Francis PDF route with explicit download parameter:
    - `https://www.tandfonline.com/doi/pdf/10.1080/07421222.2022.2096549?download=true`
  - current ResearchGate article page:
    - `https://www.researchgate.net/publication/363016491_The_Impact_of_Trust_and_Recommendation_Quality_on_Adopting_Interactive_and_Non-Interactive_Recommendation_Agents_A_Meta-Analysis`

What happened:
- The older direct ResearchGate PDF path for Xiao and Benbasat (2007) returned `403 Forbidden` from this environment on 2026-08-30.
- The Taylor & Francis `?download=true` PDF route for Ebrahimi et al. (2022) also returned `403 Forbidden` again from this environment on 2026-08-30.
- The current ResearchGate article page for Ebrahimi et al. (2022) did not expose a retrievable full text in this shell-level context; it served a `ResearchGate - Temporarily Unavailable` HTML page rather than article content or a downloadable PDF.

Updated judgment:
- The remaining gap still reflects access context rather than source discovery.
- Future retries should not repeat shell-level fetches of ResearchGate or the same Taylor & Francis PDF route unless the access context changes materially.
- The next meaningful retrieval attempt should use an authenticated manual browser or institutional-library session, then archive only files that validate as real PDFs.
