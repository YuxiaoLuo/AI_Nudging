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

### Literature and paper selection
- Which additional UTD24 or ABDC A* papers best strengthen the bridge from recommendation agents to conversational AI?
- Are there top-journal marketing papers on consumer confidence, transparency, or algorithmic advice in shopping contexts that should be pulled in next?
- Which currently collected papers are useful but should remain supporting rather than anchor references?
- Which current papers are true construct anchors versus merely useful context, so the manuscript does not become citation-heavy but theoretically loose?
- With the PDFs now added, the next question is not whether Wang and Benbasat (2007), Senecal and Nantel (2004), and Yalcin et al. (2022) are usable, but which of them should be elevated from strong support into the smallest defensible core anchor set after close reading.
- How much should top-journal but cross-domain AI-advice papers such as Longoni et al. (2019) be used in the first paper, given their value for boundary conditions but not for direct shopping-theory anchoring?

### Construct-definition questions
- How should perceived decision quality be distinguished most cleanly from choice confidence so the two do not collapse conceptually?
- Is perceived transparency best defined as understandability of recommendation logic, reconstructability of the recommendation process, or both?
- Which construct definitions need the strongest seminal anchors before measure selection begins?

## Resolved questions

### Verification workflow
- I should verify metadata, journal fit, and topical alignment before treating a paper as an anchor.
- Misleading local filenames should not be trusted without verification.

### Excluded paper
- `Ho_2025_System 2 & Confidence.pdf` was verified as out of scope for this project and removed from the usable literature set.

### Current first-paper logic
- The current best first-paper framing is a tradeoff model rather than an everything-model.
- Primary outcomes should remain purchase likelihood and perceived decision quality.
- Trust and satisfaction should remain secondary outcomes unless later evidence shows they need a more central role.
- The core theory should contrast conversational AI with interface-level nudges by emphasizing adaptive dialogue, personalization benefits, and transparency costs.
- The literature base should be organized around a small number of true anchors for each construct rather than continued broad accumulation of adjacent papers.
- The next theory gain should come from cleaner construct definitions, not from adding many more adjacent citations.
- Choice confidence should be treated as certainty in the selected option, whereas perceived decision quality should remain the broader evaluative judgment of whether the final decision was sound and appropriate.
- Perceived transparency should be treated as a combination of understandability and reconstructability of the recommendation basis.
- Scientific manuscript style should now be the default for theory writing, with citation-backed claims integrated directly into the prose rather than left implicit.
