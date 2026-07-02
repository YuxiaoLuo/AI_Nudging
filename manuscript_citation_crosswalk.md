# Manuscript Citation Crosswalk

## Purpose
This file maps the manuscript's current citations to their argumentative roles, likely priority level, and local source files. The goal is to make later citation verification, reference cleanup, and theory calibration faster without reopening the paper's broader framing.

## Use rule
- Treat `core anchor` papers as the smallest defensible source set carrying the manuscript's main argument.
- Treat `bridge/support` papers as sources that strengthen transitions, construct definitions, or adjacent empirical support without needing to carry the whole framing.
- If a future draft adds a citation to the main text, record its role here once that citation becomes more than incidental.

## Crosswalk

| Citation | Current manuscript role | Priority | Main section(s) served | Local file |
| --- | --- | --- | --- | --- |
| Häubl and Trifts (2000) | Establishes the classic digital-guidance baseline through interactive decision aids and comparison support. | Core anchor | Introduction; Theoretical Background; benefit-route setup | `literature/Haubl_MktSci2000_InteractiveDecisionAids.pdf` |
| Senecal and Nantel (2004) | Establishes that online product recommendations directly influence consumer choice in e-commerce settings. | Core anchor | Introduction; Theoretical Background | `literature/Senecal_JRetailing2004_OnlineProductRecommendationsChoices.pdf` |
| Ursu (2018) | Establishes that rankings and interface-level guidance shape search and purchase behavior even when the choice set is unchanged. | Core anchor | Introduction; Theoretical Background | `literature/Ursu_MktSci2018_PowerOfRankings.pdf` |
| Xiao and Benbasat (2007) | Bridges from simple recommendation outputs to recommendation agents as decision-support technologies. | Bridge/support | Introduction; Theoretical Background | Exact citation is confirmed in `literature_reading_matrix.md` and `literature/download_log.md`, but no authoritative local PDF is currently present. The MISQ and JSTOR PDF routes returned `403` access blocks on 2026-06-22, a 2026-06-23 browser-header retry against the MISQ PDF endpoint still saved an HTML document beginning with `<!DOCTYPE html>` rather than a real PDF, and a later CORE-hosted route also returned `403 Forbidden` from this environment. A 2026-07-01 repository recheck further clarified that the ResearchGate page currently exposes a publicly readable full-text view and labels the article `PDF Available`, but the project still does not have a successfully archived local PDF copy from this environment. Nearby `Xiao_*` PDFs should not be treated as verified matches. |
| Wang and Benbasat (2007) | Core explanation-facility anchor showing why transparency and trusting-belief logic matter for advisory systems. | Core anchor | Introduction; Theoretical Background; transparency mechanism | `literature/Wang_JMIS2007_ExplanationFacilitiesTrustingBeliefs.pdf` |
| Wang et al. (2018) | Shows that neutrality, sponsorship, and explanations shape trust-versus-distrust responses to recommendation agents. | Core anchor | Introduction; Theoretical Background; transparency mechanism | `literature/Wang_MgmtSci2018_RecommendationNeutralitySponsorshipDisclosure.pdf` |
| Wang and Wang (2019) | Supports the claim that disclosure changes perceived integrity in commercially biased recommendation settings. | Core anchor | Introduction; Theoretical Background; transparency mechanism | `literature/Wang_ISR2019_SponsorshipDisclosurePerceivedIntegrity.pdf` |
| Luo et al. (2019) | Commerce-facing AI-chatbot disclosure anchor tying recommendation transparency and disclosure choices to purchases. | Core anchor | Introduction; Theoretical Background; transparency mechanism; Contribution | `literature/Luo_MktSci2019_ChatbotDisclosureCustomerPurchases.pdf` |
| Ebrahimi et al. (2022) | Supports the claim that interactivity is itself a meaningful recommendation-system design dimension rather than a superficial interface flourish. | Bridge/support | Theoretical Background | Exact citation is confirmed in `literature_reading_matrix.md` and `literature/download_log.md`, but no authoritative local PDF is currently present. The direct Taylor & Francis PDF route and ResearchGate route returned `403` access blocks on 2026-06-22, and a 2026-06-23 browser-header retry against the Taylor & Francis PDF endpoint still saved an HTML document beginning with `<!DOCTYPE html>` rather than a real PDF. A later metadata recheck via OpenAlex also exposed no open-access PDF route for this DOI. A 2026-07-01 repository recheck further clarified that the ResearchGate page currently shows `Request full-text PDF` and `No full-text available`, so no public repository-hosted full text is exposed there either. A 2026-07-02 open-web recheck sharpened the diagnosis slightly further: current Taylor & Francis search snippets explicitly advertise `View PDF` / `Download PDF`, but no usable public PDF route emerged from this environment, so the gap now looks more like access-gated retrieval than route discovery. The download log records those routes for later manual retrieval, and `literature/DSS2024_XAI & Decision Making.pdf` should not be treated as a verified substitute. |
| Chung et al. (2020) | Supports the personalization logic in conversational or voice-shopping settings. | Bridge/support | Theoretical Background; benefit-route setup; measures logic | `literature/Chung_CHB2020_PersonalizationSocialRoleVoiceShopping.pdf` |
| Chen et al. (2021) | Direct conversational-shopping decision-aid anchor for personalization and task-support logic. | Core anchor | Abstract; Theoretical Background; benefit-route setup; measures logic | `literature/Chen_IntrRes2021_ConversationalAgentDecisionAidShoppingTask.pdf` |
| de Cicco et al. (2022) | Supports the idea that conversational-commerce guidance can create concern around bias, appropriation, and inspectability. | Bridge/support | Theoretical Background; transparency mechanism | `literature/DeCicco_TFSC2022_BiasedChoicesVoiceAssistantsConversationalCommerce.pdf` |

## Role summary by argument layer

### 1. Baseline digital-guidance layer
- Häubl and Trifts (2000)
- Senecal and Nantel (2004)
- Ursu (2018)

These papers justify the paper's opening move that digital choice architecture already shapes search, comparison, and choice before conversational AI is introduced.

### 2. Recommendation-agent and explanation bridge
- Xiao and Benbasat (2007)
- Wang and Benbasat (2007)
- Wang et al. (2018)
- Wang and Wang (2019)

These papers justify the move from interface nudges to advisory technologies whose explanations, neutrality, and disclosures change how guidance is evaluated.

### 3. Conversational-shopping and personalization layer
- Chung et al. (2020)
- Chen et al. (2021)

These papers justify the claim that conversational guidance can feel more tailored and decision-supportive than static interface cues.

### 4. Transparency-risk and commerce-facing AI layer
- Luo et al. (2019)
- de Cicco et al. (2022)

These papers justify the claim that AI-mediated shopping guidance can increase support while weakening inspectability, especially when disclosure and recommendation logic are not fully visible.

## Current verification notes
- The baseline and transparency-side anchors have clean local file matches.
- The manuscript's current `Xiao and Benbasat (2007)` and `Ebrahimi et al. (2022)` bridge citations are now confirmed at the metadata level through the project's reading matrix and download log, so the citations themselves are not in doubt.
- Those two bridge citations still lack authoritative local PDFs, so future citation-verification work should distinguish between `citation confirmed` and `local file archived`.
- The latest archive attempts on `2026-06-22`, `2026-06-23`, and `2026-07-01` suggest the remaining gap is still about access context rather than bibliographic uncertainty, but the two cases are now more clearly distinct: Xiao and Benbasat (2007) has a publicly readable repository-hosted full-text page, whereas Ebrahimi et al. (2022) still does not expose public full text there.
- The nearby `Xiao_*` PDFs and `DSS2024_XAI & Decision Making.pdf` should not be treated as authoritative substitutes unless they are checked against the exact cited papers.

## Likely next use
- Use this file when cleaning the references section against the main-text citations.
- Use this file when deciding which citations truly need line-level verification before submission.
- Use this file when a later draft adds or removes citations, so the anchor hierarchy remains explicit rather than implicit.
