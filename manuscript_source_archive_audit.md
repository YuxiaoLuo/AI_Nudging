# Manuscript Source Archive Audit

## Purpose
This file records the current local-archive status of the manuscript's cited sources. The goal is to separate `citation present in the manuscript` from `authoritative local PDF archived in the project`.

## Current audit target
- Source manuscript:
  - `manuscript_llm_ai_nudges_draft.md`
- Audit date:
  - `2026-06-23`
- Related files:
  - `manuscript_citation_crosswalk.md`
  - `manuscript_reference_audit.md`
  - `literature/download_log.md`

## Current archive summary
- Current in-text citation count:
  - `12`
- Citations with authoritative local PDFs archived:
  - `10`
- Citations with local files present but not validated as real PDFs:
  - `0`
- Citations bibliographically confirmed but still lacking authoritative local PDFs:
  - `2`

## Archived citations
- Häubl and Trifts (2000)
  - local file: `literature/Haubl_MktSci2000_InteractiveDecisionAids.pdf`
- Senecal and Nantel (2004)
  - local file: `literature/Senecal_JRetailing2004_OnlineProductRecommendationsChoices.pdf`
- Ursu (2018)
  - local file: `literature/Ursu_MktSci2018_PowerOfRankings.pdf`
- Wang and Benbasat (2007)
  - local file: `literature/Wang_JMIS2007_ExplanationFacilitiesTrustingBeliefs.pdf`
- Wang et al. (2018)
  - local file: `literature/Wang_MgmtSci2018_RecommendationNeutralitySponsorshipDisclosure.pdf`
- Wang and Wang (2019)
  - local file: `literature/Wang_ISR2019_SponsorshipDisclosurePerceivedIntegrity.pdf`
- Luo et al. (2019)
  - local file: `literature/Luo_MktSci2019_ChatbotDisclosureCustomerPurchases.pdf`
- Chung et al. (2020)
  - local file: `literature/Chung_CHB2020_PersonalizationSocialRoleVoiceShopping.pdf`
- Chen et al. (2021)
  - local file: `literature/Chen_IntrRes2021_ConversationalAgentDecisionAidShoppingTask.pdf`
- de Cicco et al. (2022)
  - local file: `literature/DeCicco_TFSC2022_BiasedChoicesVoiceAssistantsConversationalCommerce.pdf`

## Local files present but not validated as real PDFs

- None currently flagged.

## Confirmed citations still missing authoritative local PDFs

### Xiao and Benbasat (2007)
- Citation status:
  - bibliographically confirmed in the manuscript package
- Current issue:
  - no authoritative local PDF archived yet
- Current crosswalk note:
  - Exact citation is confirmed in `literature_reading_matrix.md` and `literature/download_log.md`, but no authoritative local PDF is currently present. Direct MISQ and JSTOR PDF routes were rechecked on 2026-06-22 and both returned `403` access blocks from this environment; the download log now records those routes plus a ResearchGate full-text page for later manual retrieval. Nearby `Xiao_*` PDFs should not be treated as verified matches.

### Ebrahimi et al. (2022)
- Citation status:
  - bibliographically confirmed in the manuscript package
- Current issue:
  - no authoritative local PDF archived yet
- Current crosswalk note:
  - Exact citation is confirmed in `literature_reading_matrix.md` and `literature/download_log.md`, but no authoritative local PDF is currently present. A direct Taylor & Francis PDF route and ResearchGate route were rechecked on 2026-06-22 and returned `403` access blocks from this environment; the download log records those routes for later manual retrieval, and `literature/DSS2024_XAI & Decision Making.pdf` should not be treated as a verified substitute.

## Interpretation
- The manuscript currently does not have a citation-alignment problem.
- The manuscript also does not have a broad source-discovery problem.
- The remaining archive gap is narrow and specific to the bridge citations already identified in the manuscript package.
- The main unresolved issue is access context, not uncertainty about what the cited papers are.

## Practical use
- Use this file when deciding whether the next bibliography step is `style cleanup` versus `manual PDF retrieval`.
- Use this file during handoff when a future session needs a fast answer to `which cited papers are still not locally archived?`
- If a missing PDF is later archived successfully, update this file, `manuscript_citation_crosswalk.md`, and `literature/download_log.md` together.
