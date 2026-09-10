---
title: "From open-source game theory to AI moral formalization"
date: 2026-09-10
type: rapid-evidence-map-and-formalization-proposal
tags: [ai-safety, formal-ethics, game-theory, stakeholder-inclusion, lean]
status: initial-research-human-review-needed
---

# 0. Executive summary

**Verdict: there is a credible contribution path, starting with precise definitions, assumption audits, and small checked counterexamples.** The first research question is what connects cooperation between agents to acceptable outcomes for affected people. These are different properties and must be connected explicitly.

The supplied video is commentary by Dr. Samuel Allen Alexander on the Mathematical AI Safety Institute (MAISI). We retrieved its original English automatic SRT with `yt-dlp`, then traced the guide and research-direction page it mentions. The relevant destination is [Open-Source Game Theory](https://mathforaisafety.org/research/open-source-game-theory), within [AI Safety for Mathematicians](https://mathforaisafety.org/), linked from [MAISI](https://maisi.org/).

Five findings drive the decision:

1. The video calls attention to foundational research and disagreement about human values. It does not present a new formal theory of morality or a tested alignment system. See the [timestamp audit](video-analysis.md).
2. Open-source game theory studies interactions in which agents can inspect each other's programs. Source inspection changes strategic possibilities; it does not itself settle the ethical desirability of outcomes. [Critch, Dennis & Russell, 2022](https://arxiv.org/abs/2208.07006).
3. Formal ethics already has substantive work using theorem provers. The project should learn from existing logical encodings instead of inventing a universal morality score. [Singh, 2022](https://arxiv.org/abs/2207.10152); [Parent & Benzmüller, 2024](https://arxiv.org/abs/2308.10686v4).
4. An actionable source-audit candidate concerns the growth condition in the guide's bounded Löb statement. The original theorem includes proof-encoding overhead and a stronger asymptotic relation. The [audit](source-audit.md) records the exact qualification; no external correction has been submitted.
5. The first implementation constructs a two-agent game with an excluded stakeholder. Stable, mutually beneficial coordination can violate a separately specified no-harm constraint. This is a modest formal example of a familiar conceptual limitation, with no novelty claim. See [verification status](verification.md).

**Evidence bands:** high confidence in the retrieved caption provenance, the identified links, and directly inspected source statements; model-internal confidence depends on the recorded checker results; low confidence in transfer to deployed AI because there is no empirical evaluation. These are descriptive bands, not a clinical GRADE assessment. No pooled effect size is appropriate.

**Next actions:** review the meaning of the first model; inspect the source-assumption note; then choose one external contribution target and prepare a narrow patch conforming to its existing definitions and review policy. The independent checks matter more than the number of generated theorems.

# From open-source game theory to AI moral formalization

## 1. Abstract

This rapid evidence map traces a YouTube discussion to its primary institutional and mathematical sources, assesses contribution routes, and starts a reproducible repository. The main conceptual result is a separation between strategic cooperation, verification of a specified property, moral justification, and external validity. The implementation begins with a finite counterexample involving an affected non-player. The source audit identifies a theorem-statement qualification worth checking with maintainers. Limitations include automatic captions, selective literature coverage, no upstream acceptance, and no evidence about deployed-system safety.

## 2. Introduction

An AI can be effective at advancing an objective without that objective representing everyone affected. Multiple AIs can also coordinate successfully while their shared activity imposes costs on others. Consequently, a research program about moral formalization needs to specify whose interests count, how conflicting claims are handled, and what observable or provable property is being asserted.

MAISI describes a program to develop mathematical foundations for AI safety and explicitly recognizes that mathematics must work alongside other safety efforts. Its institutional ambition should be distinguished from completed technical results. [MAISI goals and strategy](https://maisi.org/#goals).

For this project, “moral formalization” means making a normative claim precise enough to expose its assumptions, consequences, conflicts, and counterexamples. It does not mean deriving values without normative premises.

## 3. Method

**Design:** a rapid evidence map plus a bounded software/proof prototype, conducted on 2026-09-10. This was not a preregistered systematic review.

**Acquisition:** use the supplied video ID; inventory platform captions; select original English automatic captions; retrieve source SRT without changing it; retain a SHA-256 hash and metadata; follow the guide link discussed in the captions; inspect cited mathematical sources and relevant repositories.

**Source selection:** prioritize the original caption track, official institutional pages, original research papers, and source repositories. Search engines were discovery aids. Incidental unrelated search results were excluded. Formal and conceptual work was selected for its relevance to cooperation, normative specification, or proof reuse; the project did not screen every paper in these areas.

**Extraction:** separate presenter commentary from text read from a website; record timestamps, theorem locators, versions, formal assumptions, and unresolved gaps. Caption errors in names and overlapping timing windows are preserved in the SRT; interpretation uses independently verified names.

**Validation:** check a small finite game rather than simulating contemporary language models. The [verification record](verification.md) is authoritative about executed commands and proof status. Source-code review and build execution establish different things, and both need to be reported.

**Deviation:** initial web retrieval of YouTube failed. The user-requested `yt-dlp` route succeeded. The guide was initially a search candidate and subsequently confirmed against the caption discussion and canonical site navigation.

## 4. Findings

### 4.1 What the video contributes

The most relevant passage is approximately [16:34–17:25](https://www.youtube.com/watch?v=P6yKoqCxl_0&t=994s): the presenter challenges the treatment of human values as fixed or unanimous, then reads the guide's call to formalize poorly specified concepts. Around [17:38](https://www.youtube.com/watch?v=P6yKoqCxl_0&t=1058s), he notices the open-source game-theory link. He does not work through its theorems in this video. The complete source-specific analysis is [here](video-analysis.md).

The presenter's questions about funding and corporate influence motivate scrutiny but are not evidence identifying the institute's funders or establishing misconduct. Institutional forecasts, risk hypotheses, and mathematical theorems have different evidential status.

### 4.2 What the game-theory page means

Ordinary one-shot games typically specify actions and payoffs. Program games can let one agent condition its action on the other agent's code. FairBot-style constructions make cooperation depend on a proof about the other program. Provability logic enables surprising mutual-cooperation results under the stipulated formal setting. [Bárász et al., 2014, revised 2021](https://arxiv.org/abs/1401.5577v2).

Bounded agents add finite proof-search resources. Claims about them depend on encoding and proof-length conditions. They cannot be obtained simply by assuming an unbounded proof search finishes quickly. [Critch, 2016](https://arxiv.org/abs/1602.04184).

The term “open-source” here refers to program visibility within the model. We did not establish that the guide itself has a public code repository, license, or pull-request intake. External formalization repositories are separate possible destinations.

### 4.3 Four layers that must remain visible

| Layer | Question | A successful check establishes | Remaining gap |
|---|---|---|---|
| Strategic | Will the agents coordinate under these incentives? | An equilibrium or cooperation property in the model | Desirability of that coordination |
| Normative | Which constraints or values are endorsed? | A precise specification and its implications | Justification, disagreement, representation |
| Implementation | Does the program satisfy the specification? | The proved or tested implementation property | Whether the specification captures the intention |
| Empirical | Does the model describe the real setting? | Evidence within the validation design | Transfer, distribution shift, omitted stakeholders |

Our interpretation is that useful progress often comes from connecting two of these layers with explicit assumptions, rather than giving all four the same label.

### 4.4 The first model

Two decision makers choose whether to join a joint action. A third stakeholder is affected but does not choose an action. All numbers below are invented utility units for a mathematical example.

| Agent A | Agent B | A payoff | B payoff | Outsider payoff |
|---|---|---:|---:|---:|
| Abstain | Abstain | 1 | 1 | 0 |
| Join | Abstain | 0 | 2 | -1 |
| Abstain | Join | 2 | 0 | -1 |
| Join | Join | 3 | 3 | -2 |

Both joining is a strict Nash equilibrium: given the other's participation, leaving reduces either agent's payoff from 3 to 2. It also improves both agents' payoff relative to mutual abstention and is Pareto efficient for those two agents. Yet the outsider loses 2 units relative to the abstention baseline. A chosen rule requiring that outsider not be worse off rejects this outcome.

Including the outsider in the payoff vector reveals a tradeoff: mutual joining and mutual abstention are incomparable under stakeholder-wide Pareto dominance. Importantly, adding the outsider does not automatically eliminate Pareto efficiency of the harmful outcome. Pareto efficiency alone does not resolve the normative choice.

This is a coordination game, not the Prisoner's Dilemma, and it does not implement FairBot or program equilibrium. It isolates the distinct inference from good outcomes for participants to good outcomes for all affected people. The formal package and independent finite checker document exactly which versions of these statements are established.

### 4.5 Existing formal ethics and contribution targets

Singh's work encodes a Kantian principle in dyadic deontic logic and Isabelle, illustrating how philosophical interpretation can inform machine-checkable specifications. Parent and Benzmüller use Isabelle/HOL to study conditional obligations and a population-ethics argument. Our assessment of these two papers is at metadata/abstract level; no reproduction of their proofs is claimed. [Singh](https://arxiv.org/abs/2207.10152); [Parent & Benzmüller](https://arxiv.org/abs/2308.10686v4).

For game-theory and logical infrastructure, see the audited repository links in [source-audit.md](source-audit.md). Reuse should depend on reading actual definitions and reproducing a pinned build. A compatible license or welcoming contribution page is not evidence that a proposed patch will be accepted.

## 5. Conclusion

We can begin contributing now through a narrow, reviewable research artifact. The starter example and assumption audit provide such artifacts. The next meaningful milestone is an independently reviewed statement whose interpretation and proof agree, followed by a contribution that fills a documented gap in an existing project.

## 6. Deconstructive analysis: start with the broad claim

Take “cooperative AI is morally aligned” and unpack it. What counts as cooperation? Who are the beneficiaries? Can affected outsiders object? What reference point defines harm? Are outcomes deterministic? Is the system's stated code its actual behavior? Are the utilities proxies? Does the proof assume the desired conclusion through a definition or axiom?

The starter model targets only one of these links: participant benefit does not logically imply a chosen outsider-protection criterion. Its value is that the failed implication becomes inspectable.

## 7. Reconstructive analysis: build from explicit commitments

For each future model, begin with a stakeholder set, actions, outcomes, information available to agents, and a baseline. Then define candidate normative constraints separately from the agents' objectives. Next state one theorem and one stronger claim that should fail. Finally add a proof or checker and a plain-language interpretation.

A no-harm rule, aggregate-welfare rule, consent requirement, and fairness criterion may conflict. Their names do not establish that they are justified or compatible. Keeping them modular makes disagreement visible and allows the consequences of each choice to be examined.

## 8. Middle-out synthesis: a contribution path

| Stage | Deliverable | Completion criterion |
|---|---|---|
| Current | Video/site audit, finite-game example, reproducibility record | Sources traceable; model claims match executed checks |
| Next | Review one theorem-statement qualification | All formal hypotheses traced to the original theorem |
| Next | Small family of stakeholder counterexamples | General assumptions proved; finite examples serve as witnesses |
| Later | Add a consent or representation mechanism | Both protection and incentive compatibility assessed; possible impossibility exposed |
| Later | Adapt one artifact to an existing formalization project | Definitions reused, pinned build reproduced, human review requested |
| Research extension | Validate a behavioral interpretation | Construct definitions and study design specified before data collection |

A psychology contribution would be especially useful at the interpretation layer: distinguish compliance from consent, verbal endorsement from stable preference, confidence from knowledge, and stakeholder representation from simple majority agreement. These are proposed research roles, not claims that clinical constructs already have validated encodings here. Initial examples should use synthetic nonclinical situations.

## 9. Glossary

| Term | Meaning here |
|---|---|
| Formalization | Translation into explicit mathematical or logical definitions and claims |
| Verification | Checking a property relative to specified assumptions |
| Validation | Investigating whether a model represents its intended target |
| Program equilibrium | Equilibrium involving the selection of programs whose behavior can depend on other programs |
| Nash equilibrium | A profile at which no player gains by changing only their own action |
| Pareto dominance | Everyone in the specified comparison set is at least as well off and someone is better off |
| Pareto efficiency | No available outcome Pareto dominates the outcome for the specified comparison set |
| Deontic logic | Logic concerned with obligations, permissions, and prohibitions |
| Externality | An effect on someone not fully represented in the decision makers' objectives |
| Bounded proof search | Search restricted by a specified resource such as proof length |

## 10. Bibliography

The machine-readable bibliography is [references.bib](../references.bib). It includes the original provability/game-theory papers and relevant formal-ethics papers. Source roles, exact locators, version qualifications, and repository pointers appear in [source-audit.md](source-audit.md). The [video analysis](video-analysis.md) supplies caption provenance and timestamp links. No citation count is treated as evidence of a theorem's applicability.

## 11. Metacognitive review: process integrity

**Assessment: a useful rapid map, with incomplete coverage.** A transparent, task-specific process score is 7/10: provenance 2/2; source-to-claim traceability 2/2; breadth/counterevidence 1/2; reproducibility 1/2; independent semantic review 1/2. This is an informal rubric, not AMSTAR-2, and it does not score mathematical truth.

Strengths include obtaining the requested source track, following the actual link chain, recording uncertainty about automatic captions, and checking the guide against its cited paper. Weaknesses include selective searches, no independent screening, no audio verification, and no outside expert review. Some philosophical sources were examined only at abstract level. Agents working on separate subtasks offer additional checking, but do not constitute independent human replication.

PRISMA-style reporting habits are useful for the search log and exclusions; AMSTAR-2 and RoB-2 are not appropriate scoring instruments for this mix of a commentary video, webpages, formal papers, and software. Fixes are to reproduce exact source versions, review definitions with a domain specialist, and expand the literature only around the next chosen theorem rather than declare comprehensive coverage.

## 12. Metacognitive reflection: inference robustness

**Verdict: the local counterexample can refute an unrestricted implication; it cannot estimate the frequency or severity of real AI harms.** Its conclusion is conditional on a chosen game, utility assignments, stakeholder set, and baseline. A finite proof is exact within that specification; that exactness is not a guarantee of construct validity.

There are no comparable effect sizes to pool, so fixed/random effects, Q, tau-squared, I-squared, funnel plots, and Egger tests are not applicable. The appropriate stress tests are changed payoff orderings, alternative baselines, explicit stakeholder participation, and competing normative constraints.

What would change the local conclusion? A model in which every permitted cooperative outcome satisfies the specified outsider constraint, or in which the payoff inequalities needed for equilibrium fail. What would change the project recommendation? An existing identical formal example with stronger documented reuse, an error in the definitions/proof, or a maintainer explaining that the proposed assumption note is already resolved. In any of these cases, reuse or revise rather than claim novelty.

Our main prior is that machine checking is useful; the main bias risk is treating checkability as importance. A second risk is building the easiest theorem instead of the most relevant one. The next stage therefore requires external semantic review and a specific gap statement before broadening the proof library.

## 13. Zotero and Obsidian integration

Import `references.bib` into a Zotero collection named **AI Moral Formalization**. Suggested tags: `topic/open-source-game-theory`, `topic/formal-ethics`, `method/lean`, `method/isabelle`, `claim/conditional-guarantee`, `limitation/stakeholder-exclusion`, and `status/needs-reproduction`. Use actual item types: preprint or conference/journal article as supported by verified metadata; webpage for institutional guides; video recording for the supplied video.

Link the 2014/2021 modal-agent paper, the 2016 bounded theorem, and the 2022 institution-design paper as Related items. In notes explain the relationship as **foundation → bounded extension → further constructions/open problems**. Link the formal-ethics papers as a parallel normative-specification lane rather than treating them as replications of game-theory results.

For each Better Notes source note, use: **claim; exact locator; assumptions; proof/empirical status; counterexample; relationship to this repository; what remains unchecked**. Attach this original report as a project note; retain third-party PDFs and the SRT in your own reference collection according to their source permissions.

This Markdown file can be copied into an Obsidian project folder. Create links to `[[AI cooperation]]`, `[[Normative specification]]`, `[[Stakeholder inclusion]]`, and `[[Verification versus validation]]`. Use citekeys from the imported bibliography; resolve Zotero item links locally after import rather than inventing item IDs. No Zotero library edits have been made during this task.

## 14. Appendix: reproducibility and claim boundaries

- [Video analysis and timestamp provenance](video-analysis.md)
- [Primary-source and repository audit](source-audit.md)
- [Formalization and checker verification](verification.md)
- [Bibliography](../references.bib)

The full source SRT is a separate downloadable artifact. It is excluded from this public repository, along with transient YouTube metadata. This repository contains original analysis and code; it does not redistribute the video's transcript or claim affiliation with MAISI.

Research, writing, and implementation are AI-assisted. The user has not yet independently endorsed every interpretation or reviewed the code. A draft contribution is not an accepted external result.
