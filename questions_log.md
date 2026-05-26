# Nudging Project Questions Log

This file records open questions, uncertainties, and decisions encountered while collecting literature and developing the project. The goal is to keep iterating autonomously while preserving a clear handoff trail.

## Open questions

### Scope and positioning
- Should the paper frame LLM conversational nudges primarily as a new form of digital nudging, a new form of recommendation agent, or a new form of conversational choice architecture?
- Is the strongest theoretical contrast against algorithm-generated recommendation badges, against recommendation agents, or against both in a layered comparison?
- Should the paper prioritize e-commerce theory, AI transparency theory, or consumer decision-process theory as its main contribution lane?

### Outcome variables
- What should be the single most important dependent variable: purchase likelihood, decision quality, or confidence?
- Should transparency be modeled as a mediator, a moderator, or a tradeoff variable alongside positive mechanisms like personalization and cognitive-load reduction?
- Does the paper need both behavioral outcomes and perceived outcomes, or should it stay tighter?

### Experiment design
- What product category is best for the shopping experiment?
- Should the experimental treatments simulate a real shopping assistant conversation or a tightly scripted chatbot?
- How much adaptivity is necessary in the LLM condition for the treatment to feel meaningfully different from UI nudges?

### Current design direction
- Headphones currently looks like the strongest first-category candidate because it combines attribute complexity, broad participant familiarity, and meaningful tradeoffs without requiring niche expertise.
- The measure strategy should remain tightly theory-aligned: each key construct should map to a distinct role in the model rather than expanding into a broad, overlapping set of post-task attitudes.
- The control set should remain compact and theory-justified rather than growing into a broad checklist of generic individual-difference variables.
- The first-pass treatment logic should keep the product set constant across conditions and vary only the mode of guidance: conversational assistant, static UI nudge, or no explicit nudge.
- The first-pass analysis strategy should follow the tradeoff model directly, prioritizing condition comparisons plus mediation/path tests over a broad menu of loosely connected regressions.
- Another selective literature pass suggests Luo et al. (2019, Marketing Science) is not just a strong commerce-facing support paper but a likely core anchor for the transparency and disclosure side of the model.
- This additional literature pass did not reveal a clearly superior omitted seminal paper for the current theory frame, which increases confidence in the current compact anchor strategy.
- The treatment should now be implemented as a semi-structured rather than fully open-ended conversation so the conversational condition feels adaptive without creating uncontrolled content variation.
- The current best stimulus structure is a six-product fictional headphone set with one balanced focal option recommended across both the conversational and UI-nudge conditions.
- The methods section can now be drafted with enough specificity to include a panel-based three-condition experiment, a stable shopping scenario, a compact procedure, and candidate scale items without inventing new theory.
- The project now has enough material to sustain an integrated introduction-theory-hypotheses-methods draft rather than only disconnected blueprint sections.
- The empirical section now has a more defendable publication-oriented logic: explicit conversational-versus-UI planned contrasts, staged outcome and process models, a preferred path-model specification, and a simpler fallback regression sequence.
- The integrated draft can now be improved meaningfully through prose cleanup alone; the next writing gain no longer depends on adding many new structural blocks.
- A final narrow pass on the remaining confidence and perceived decision-quality gaps did not reveal a clearly stronger core anchor, so the project does not need another literature-expansion step before manuscript consolidation.
- The formal manuscript file can now absorb more of the concrete empirical specification directly, which reduces the need to keep consulting the blueprint for core study details.
- The methods section of the formal manuscript draft benefits from being broken into more explicit participant, design, and procedure components rather than left as one dense block.
- The manuscript draft also benefits from explicitly carrying the manipulation-check and control rationale, because those details otherwise remain trapped in blueprint notes rather than the paper-facing draft.
- The manuscript draft benefits from carrying its own definition and focal-comparison logic early, because reviewers should not have to infer what exactly counts as the conversational nudge versus the UI-based comparison.

### Literature and paper selection
- Which additional UTD24 or ABDC A* papers best strengthen the bridge from recommendation agents to conversational AI?
- Are there top-journal marketing papers on consumer confidence, transparency, or algorithmic advice in shopping contexts that should be pulled in next?
- Which currently collected papers are useful but should remain supporting rather than anchor references?
- Which current papers are true construct anchors versus merely useful context, so the manuscript does not become citation-heavy but theoretically loose?
- With the PDFs now added, the next question is not whether Wang and Benbasat (2007), Senecal and Nantel (2004), and Yalcin et al. (2022) are usable, but which of them should be elevated from strong support into the smallest defensible core anchor set after close reading.
- How much should top-journal but cross-domain AI-advice papers such as Longoni et al. (2019) be used in the first paper, given their value for boundary conditions but not for direct shopping-theory anchoring?
- After this literature pass, should Xiao and Benbasat (2007), Wang and Benbasat (2008), Wang and Benbasat (2016), and the 2022 JMIS meta-analysis be used primarily to strengthen the recommendation-agent bridge, or should one of them be promoted into the compact core anchor set?
- For the first paper, should Wang and Benbasat (2007) now be explicitly promoted into the compact core anchor set because explanation facilities directly support the transparency mechanism more cleanly than the broader bridge papers do?

### Construct-definition questions
- How should perceived decision quality be distinguished most cleanly from choice confidence so the two do not collapse conceptually?
- Is perceived transparency best defined as understandability of recommendation logic, reconstructability of the recommendation process, or both?
- Which construct definitions need the strongest seminal anchors before measure selection begins?

### Current construct-definition direction
- Perceived personalization should capture whether the guidance feels specifically adapted to the consumer's own needs, goals, and preference structure.
- Cognitive load should capture the mental effort required to process alternatives, compare attributes, and reach a choice.
- Choice confidence should capture subjective certainty that the selected option is the right or appropriate choice.
- Perceived decision quality should capture the broader judgment that the final decision is sound, appropriate, and well justified.

### Current writing direction
- The theoretical background should be organized as a four-step bridge: interface nudges and decision aids, recommendation-agent explanation/disclosure research, conversational AI as adaptive advisory guidance, and then the tradeoff argument around support versus transparency.
- The section should function as a cumulative narrowing argument toward the paper's central question, not as a broad review of adjacent AI-commerce work.
- A useful drafting guardrail is that each paragraph should either establish the baseline, explain advisory/transparency mechanisms, or sharpen the tradeoff claim.
- The core anchor priority list should stay compact: Häubl and Trifts (2000), Senecal and Nantel (2004), and Ursu (2018) for the baseline, then Wang and Benbasat (2007), Wang et al. (2018), Wang and Wang (2019), and likely Luo et al. (2019) for the advisory and transparency bridge.
- A new candidate bridge layer has emerged between the baseline and disclosure papers: Xiao and Benbasat (2007), Wang and Benbasat (2008), Wang and Benbasat (2016), and the 2022 JMIS meta-analysis collectively strengthen the case that interactivity and trust in recommendation agents are already theorized design dimensions rather than entirely new LLM-era phenomena.
- The section should also avoid theoretical overbreadth: depth should come from a disciplined bridge among a few strong anchors rather than an expanding inventory of adjacent literatures.
- The opening paragraph of that section should establish continuity between classic digital guidance tools and advisory-system research before introducing the specific gap around LLM-based conversational assistants, so the paper reads as a reconfiguration of established choice-architecture logic rather than an isolated AI phenomenon paper.
- The next paragraph should explicitly bridge from earlier advisory technologies to conversational AI as a dialogic and adaptive form of choice architecture rather than merely a stronger static nudge.
- The following paragraph should turn that bridge into the paper's core tradeoff question by foregrounding the tension between decision support and inspectability.
- The next paragraph should connect that tradeoff explicitly to the manuscript's benefit and risk pathways so the theoretical background transitions cleanly into the formal model.

## Resolved questions

### Verification workflow
- I should verify metadata, journal fit, and topical alignment before treating a paper as an anchor.
- Misleading local filenames should not be trusted without verification.

### Excluded paper
- `Ho_2025_System 2 & Confidence.pdf` was verified as out of scope for this project and removed from the usable literature set.

### Current first-paper logic
- The current best first-paper framing is a tradeoff model rather than an everything-model.
- Headphones should now be treated as the selected first-paper category rather than only a leading candidate.
- Primary outcomes should remain purchase likelihood and perceived decision quality.
- Trust and satisfaction should remain secondary outcomes unless later evidence shows they need a more central role.
- The core theory should contrast conversational AI with interface-level nudges by emphasizing adaptive dialogue, personalization benefits, and transparency costs.
- The literature base should be organized around a small number of true anchors for each construct rather than continued broad accumulation of adjacent papers.
- Another literature pass suggests the next gain is not a broad search for more conversational-AI papers, but a tighter recommendation-agent bridge built around a few Benbasat-centered RA papers, especially to support the interactivity and trust-attribution logic.
- A plausible next-step decision is to keep Xiao and Benbasat (2007), Wang and Benbasat (2008), Wang and Benbasat (2016), and the 2022 meta-analysis as bridge/support citations while promoting Wang and Benbasat (2007) into the compact core anchor set because it most directly underwrites the transparency and explanation mechanism in the current model.
- The next theory gain should come from cleaner construct definitions, not from adding many more adjacent citations.
- Choice confidence should be treated as certainty in the selected option, whereas perceived decision quality should remain the broader evaluative judgment of whether the final decision was sound and appropriate.
- Perceived transparency should be treated as a combination of understandability and reconstructability of the recommendation basis.
- Scientific manuscript style should now be the default for theory writing, with citation-backed claims integrated directly into the prose rather than left implicit.
- The first experiment should keep the recommended focal product substantively constant across the conversational and UI-nudge conditions so the main manipulation remains the mode of guidance rather than the recommended option itself.
- The first-pass questionnaire should stay compact and construct-disciplined, with perceived decision quality, personalization, cognitive load, confidence, and transparency each measured separately rather than collapsed into a generic post-task attitude battery.
- The next writing gain should come less from adding new blocks and more from smoothing the integrated draft into cleaner manuscript prose and tightening the analysis framing.
- The next likely decision point is whether the remaining confidence and perceived decision-quality literature gaps are serious enough to justify one more narrow source pass before the project shifts primarily into prose cleanup and manuscript consolidation.
- The practical transition point is getting close: once the remaining source-gap decision is made, the project should be ready to move from blueprint refinement into a cleaner manuscript-file workflow.
- That transition point has effectively been reached: the project now has a dedicated manuscript draft file, and the next gains should come from selective migration and refinement rather than more blueprint expansion.
- The next practical manuscript gain is to keep moving only the highest-value remaining design and wording details into the draft while shrinking the blueprint's role as the primary working document.
- The manuscript-draft workflow is now mature enough that many gains come from section-level rewriting and decomposition rather than from adding entirely new conceptual content.
- A useful heuristic now is to move only those remaining blueprint details that materially increase the formal draft's self-sufficiency and review readiness.
- Definition clarity and comparison clarity are part of that heuristic: moving them into the draft is high value because they improve reviewer readability without reopening the model.
- The formal manuscript draft should now carry explicit theory-level definitions for perceived personalization, cognitive load, perceived transparency, choice confidence, and perceived decision quality, rather than leaving those distinctions mainly in blueprint notes.
- The formal manuscript draft should also carry the strongest existing source-backed wording for personalization and cognitive-load support directly in the theory section, while keeping the confidence-versus-decision-quality distinction explicit and disciplined.
- The next methods-level cleanup should fix presentation conventions in advance rather than leaving them implicit, especially by treating the conversational-versus-UI contrast as the central reported comparison and by keeping cognitive-load coding direction consistent across models and tables.
- The manuscript draft should also carry enough concrete manipulation-check, control, and data-quality language that a reviewer can see how the instrument would actually be fielded without needing to consult the blueprint.
- The formal manuscript draft should now also state explicitly that the conversational-versus-UI treatment contrast is meant to isolate mode of guidance while holding recommendation content substantively constant.
- The reassessed compact core anchor set should now be treated as stable: Häubl and Trifts (2000), Senecal and Nantel (2004), and Ursu (2018) for the digital-guidance baseline; Wang and Benbasat (2007), Wang et al. (2018), Wang and Wang (2019), and Luo et al. (2019) for the transparency and disclosure spine; Xiao and Benbasat (2007), Ebrahimi et al. (2022), and Chen et al. (2021) as bridge citations rather than additional core anchors.
- The formal manuscript draft should now also make that hierarchy visible in the prose itself, so core mechanism claims are carried by the compact anchor set while bridge citations remain supportive rather than overloaded.
- The formal manuscript draft should now also carry a representative semi-structured recommendation script and explicit planned-contrast language, because those details materially improve review-facing self-sufficiency without reopening the design.
- The formal manuscript draft should now also carry representative item wording for the primary outcomes, core process measures, and secondary outcomes, because those examples further reduce the blueprint's role in explaining how the instrument would actually look.
- The formal manuscript draft should now also carry a representative visibility-of-logic manipulation-check item and a concrete attentiveness-screen example, which likely closes the last clearly valuable blueprint-to-manuscript migration step for the current draft.
- The next manuscript gains can now come from article-level prose smoothing rather than from missing conceptual or design content, because the formal draft is substantially self-sufficient on theory, treatment, measurement, and analysis detail.
- The next prose-level gains can now come from trimming specification-style qualifiers such as `representative` and `example` where the manuscript already makes the design sufficiently concrete.
- The measures section should now also say directly that construct items are adapted from adjacent decision-aid, recommendation-agent, and conversational-shopping literatures and then normalized to the current shopping context, because that clarifies measurement grounding without forcing premature item-by-item scale finalization.
- Another useful cleanup rule is to state the paper's central contrast once in strong form and then avoid rephrasing it too many times as "not simply a stronger recommendation cue," because repetition weakens the manuscript's front-end economy.
- A related cleanup rule is that the back-end sections should divide labor more clearly: contribution should state what the paper adds, discussion should interpret what the findings would mean, and conclusion should close rather than restate the whole tradeoff argument again.
- The analysis section should now say directly that the post-task constructs must be shown to be empirically distinguishable before the path model is interpreted, especially for confidence versus perceived decision quality and for transparency versus nearby manipulation-check wording.
- The draft should also say directly that manipulation checks mainly establish condition separation and should not become an ad hoc exclusion device after outcomes are observed, except under narrow preregistered criteria.
- The draft should also say directly that prespecified exclusions must be reported as a sample-flow accounting exercise and, when feasible, paired with a light robustness check so screening rules do not look outcome-contingent.
- The draft should also say directly that one clearly defined screened sample anchors the main results, while narrower or alternative screening choices belong in explicitly labeled robustness checks rather than in shifting table-by-table samples.
- The draft should also say directly that the compact control set is for stable baseline adjustment, not for opportunistic covariate searching or table-by-table specification drift.
- The draft should also say directly that the confirmatory workflow itself should be fixed in advance when feasible, so preregistered hypotheses and model sequencing remain clearly distinguishable from secondary robustness or exploratory analyses.
- The draft should also say directly that trust and satisfaction stay secondary in the reporting sequence, so they do not quietly become co-primary outcomes if they generate interesting condition differences.
- The draft should also say directly that the empirical section should foreground estimated magnitudes and uncertainty, including condition means, effect sizes, and confidence intervals, rather than relying mainly on significance phrasing.
- The draft should also say directly that total, indirect, and residual direct effects should be reported separately, and that any remaining direct path after mediation enters should be interpreted cautiously rather than treated as automatically theory-generating.
- The draft should also say directly that missingness should be minimized by survey design, any residual missing data should be reported transparently, and the confirmatory analyses should rely on one prespecified missing-data rule rather than on silently shifting usable samples across models.
- The draft should also say directly that the target sample range is meant to support the planned treatment contrast and process-path estimation, and that the eventual paper should anchor that range in a prespecified sensitivity or power rationale with room for ordinary screening losses.
- The draft should also say directly that random assignment is expected to keep the three conditions approximately balanced and that the final reported paper should show realized cell counts transparently rather than leaving condition sizes implicit.
- The draft should also say directly that pre-treatment characteristics should be shown descriptively by condition, while avoiding a side trip into opportunistic randomization significance tests that do not strengthen the main treatment logic.
- The draft should also say directly that representative treatment materials or screenshots should appear in the eventual paper or appendix, because the conversational-versus-UI contrast is easier to evaluate when readers can inspect the instantiated stimuli.
- The draft should also say directly that the eventual paper should show full item wording, any reverse-coding direction, and concise scale diagnostics for the retained constructs, because measurement transparency matters almost as much as treatment transparency in this design.
- The draft should also say directly that the eventual paper should show construct means, standard deviations, and correlations, because reviewers should not have to reconstruct the descriptive measurement pattern only from path coefficients and prose.
- The draft should also say directly that a compact descriptive table for the retained constructs should appear before or alongside the structural results, so readers can see the empirical pattern at a glance before the full path model.
- The draft should also say directly that tables, figures, and appendices should label confirmatory, robustness, and exploratory results consistently, so the evidentiary hierarchy remains visible throughout the paper.
- The draft should also say directly that confirmatory evidence should appear first in the results narrative, with robustness, secondary, and exploratory material following afterward so the paper's inferential spine is never obscured.
- The draft should also say directly that the final paper should show screening counts and screening-sensitivity checks in a compact table, flowchart, or appendix display, so the data-quality workflow remains inspectable rather than only described narratively.
- The draft should also say directly that, where journal policy and data-sharing constraints allow, the final paper should be paired with a compact replication package containing the treatment materials, codebook, and core analysis scripts.
- Another useful cleanup rule is to convert repeated "eventual paper should" formulations into direct manuscript prose once the underlying design decision is stable, so the draft reads like a paper rather than a blueprint annotated for future revision.
- A related cleanup rule is to trim low-value auxiliary phrasing such as "ideally," "would make it easier," and "would further help" once the substantive reporting expectation is already clear, because those hedges slow the prose without adding design precision.
- Another useful cleanup rule is to vary how the manuscript refers to its core mechanism claim across sections, so the support-inspectability idea remains clear without sounding mechanically repeated in the abstract, introduction, contribution, discussion, and conclusion.
- Another useful cleanup rule is to replace example-style instrument wording with clearer planned battery structure once the constructs are stable, because reviewers should be able to see which measures are intended to be core versus merely illustrative.
- Another useful cleanup rule is to replace remaining optional-sounding phrases like `when feasible`, `for example`, and `can simply` once the preferred design choice is already clear, because those qualifiers weaken the manuscript's sense of design commitment.
- Another useful cleanup rule is to state key construct definitions in compact declarative form once the theory is stable, because burying those distinctions inside longer mechanism paragraphs makes reviewer-facing construct boundaries harder to track.
- Another useful cleanup rule is to remove note-like phrases such as `useful here`, `core theoretical burden`, and `in an important way` once the citation hierarchy is already stable, because those formulations sound like drafting commentary rather than finished theory prose.
- Another useful cleanup rule is to distinguish the roles of behavioral and evaluative outcomes explicitly once the model is stable, because reviewers should not have to infer on their own how purchase likelihood and perceived decision quality differ analytically.
- Another useful cleanup rule is to make the discussion do the interpretive work and the conclusion do the closing work, because repeating the same support-inspectability claim in both sections weakens the back-end economy of the manuscript.
- Another useful cleanup rule is to convert instrument and reporting language from planning mode into settled declarative prose once the battery structure is stable, because lingering phrases like `should`, `best captured`, and similar qualifiers make the design look less committed than it already is.
- Another useful cleanup rule is to convert method-reporting conventions into declarative manuscript prose once the workflow is stable, because repeated `should report` and `should be based on` phrasing makes the empirical section sound like reviewer instructions rather than part of the paper itself.
- Another useful cleanup rule is to convert analysis-plan reporting and interpretation guidance into declarative prose once the empirical sequence is stable, because otherwise the results section sounds like instructions for future write-up rather than part of a finished manuscript.
- Another useful cleanup rule is to remove small conditional phrasings like `can read as follows` or `should be tied` once the corresponding design choice is already fixed, because those fragments make even stable methods prose sound less committed than it is.
- Another useful cleanup rule is to remove lingering phrases like `final paper` once a section already reads as article prose, because that wording quietly reintroduces the sense that the manuscript is still only a plan for a later document.
- Another useful cleanup rule is to make the compact anchor hierarchy visible inside the prose once the literature set is stable, because otherwise the manuscript can cite the right papers while still leaving the reader unsure which citations carry the main bridge, benefit, and opacity logic.
- Another useful cleanup rule is to make the measure-to-literature mapping explicit once the instrument structure is stable, because reviewers often care less about long item lists than about whether each retained battery clearly inherits its logic from the right adjacent research stream.
