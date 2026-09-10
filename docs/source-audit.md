---
title: Source audit and contribution map
date: 2026-09-10
status: exploratory-source-audit
tags: [ai-moral-formalization, open-source-game-theory, source-fidelity, construct-validity]
---

# Source audit and contribution map

The strongest immediate contribution is a small, reproducible formal model with explicit interpretation limits, accompanied by a correction-ready audit of the assumptions behind proof-based cooperation. A proof that agents cooperate establishes a behavioral property under a model. It does not establish that their objectives, beneficiaries, or effects are morally acceptable.

The transcript investigation accompanying this audit confirmed the connection between the supplied YouTube video and the research guide below. The external issue text below is an unposted draft.

## Primary source ledger

| Key | Primary source and inspection | What it supports | What it does not establish |
|---|---|---|---|
| `Barasz2014Robust` | [Barasz et al. (2014), Robust Cooperation in the Prisoner's Dilemma](https://arxiv.org/abs/1401.5577), author abstract inspected | Modal agents can cooperate without exact code equality while avoiding unilateral exploitation in their modeled game. | General ethical goodness, deployability of unbounded modal agents, or safety of contemporary language models. |
| `Critch2016Bounded` | [Critch (2016), Parametric Bounded Löb's Theorem](https://arxiv.org/pdf/1602.04184), v5, theorem and definitions inspected | Bounded proof-based cooperation under explicit formal-system and resource-growth assumptions. | A practical small threshold or replacement of proof length by arbitrary wall-clock budgets. |
| `Critch2022Institutions` | [Critch, Dennis, and Russell (2022), Cooperative and uncooperative institution designs](https://arxiv.org/abs/2208.07006), author abstract inspected | An open-source game-theory research program with counterintuitive institutional interactions and ten posed problems. | That every problem remains open today; that “cooperate” means morally permissible. |
| `Singh2022Kantian` | [Singh (2022), Automated Kantian Ethics: A Faithful Implementation](https://arxiv.org/abs/2207.10152), abstract and linked project README inspected | A concrete Isabelle implementation of a Kantian formalization using dyadic deontic logic, with theory-oriented tests. | Agreement among ethical traditions, proof that Kantian ethics is correct, or empirical validity in a population. |
| `MathAISafetyOpenSource` | [AI-Safety for Mathematicians, Open-Source Game Theory](https://mathforaisafety.org/research/open-source-game-theory), full rendered page inspected; video connection confirmed by the accompanying transcript investigation | Accessible route into FairBot/DUPOC, CUPOD, bounded self-play results, and a candidate open problem. | An exact substitute for the papers' theorem hypotheses. |
| `AISafetyAtlas2026` | [AI Safety Formalization Atlas](https://github.com/mbrcic/ai-safety-formalization-atlas), README, contribution guide, toolchain, license, and head commit inspected | A plausible contribution destination that separates encoded proofs from their AI interpretations. | Independent reproduction of its theorem library or guaranteed acceptance of a proposed contribution. |
| `ParentBenzmuller2024Normative` | [Parent and Benzmüller (2024), Normative Conditional Reasoning as a Fragment of HOL](https://arxiv.org/abs/2308.10686v4), v4 metadata and abstract inspected | Isabelle/HOL mechanization of conditional obligations and an encoded population-ethics argument; a useful example of examining an ethical argument's assumptions. | A resolution of population ethics or a full replication by this project. |
| `Olson2026FULL` | [Olson (2026), Formalizing Kantian Ethics: Formula of the Universal Law Logic](https://arxiv.org/abs/2604.14254), metadata and abstract inspected | A recent primary research lead on formalizing purposes, agency, and universalization through quantified modal logic. | A verified software dependency, comprehensive performance evidence, or an independently audited proof. |

## Bounded Löb: a precise assumption discrepancy

The website describes the required growth as “growing asymptotically at least like log(k).” That wording can be read as allowing any function in Ω(log k). Its cited source states a stronger, proof-system-dependent condition.

In [Critch 2016 v5](https://arxiv.org/pdf/1602.04184), §5, Theorem 3, printed page 9 (PDF page index 8), the condition is

\[
f(k)\succ E\mathcal O(\lg k).
\]

Here `E` is the proof-expansion function from Definition 2 on the same page. The strict asymptotic relation is defined in §2.5, printed page 7: `a ≺ b` means every fixed natural multiple of `a(n)` is eventually smaller than `b(n)`. Even when `E` is linear, an arbitrary Ω(log k) bound does not express this hypothesis. The source also specifies representability, numeral encoding, and abbreviation assumptions in §2.2.

This is a fidelity concern about the webpage's wording. It is not a counterexample to the original theorem, and this audit has not proved the weakest possible growth hypothesis.

### Unposted upstream issue draft

**Suggested title:** Clarify the growth hypothesis in the bounded Löb theorem statement

The Open-Source Game Theory page's bounded Löb statement appears to omit proof-expansion overhead and strict domination. Could it state the cited paper's `f(k) ≻ E O(log k)` hypothesis, or explicitly mark the displayed statement as an informal summary? The relevant locators and notation are recorded immediately above. A short accompanying note could distinguish proof-length bounds from elapsed proof-search time. This would help readers translating the theorem into a proof assistant preserve its assumptions.

## Existing formalization projects

These are inspected leads, not independently reproduced dependencies. Commit references identify the inspected repository state; file reads made against `main` should be repeated at the stated pin before vendoring or depending on them.

| Project | Inspected revision | Toolchain and license | Useful next step |
|---|---|---|---|
| [AI Safety Formalization Atlas](https://github.com/mbrcic/ai-safety-formalization-atlas/tree/a65e32f8047584686320a3013720624b5efa39ee) | `a65e32f8047584686320a3013720624b5efa39ee` | `leanprover/lean4:v4.33.0`; Apache-2.0 LICENSE read | Check existing logic, social-choice, and preference interfaces before proposing new primitives. Its README lists `AISafetyAtlas.Logic.loeb`; that declaration's implementation was not inspected here. |
| [FormalizedFormalLogic / ProvabilityLogic](https://github.com/FormalizedFormalLogic/ProvabilityLogic/tree/f599cb1f775316de053d01f539dbfcbc525078a7) | `f599cb1f775316de053d01f539dbfcbc525078a7` | `leanprover/lean4:v4.33.1`; Apache-2.0 LICENSE read | Inspect reusable provability foundations and contribution conventions before attempting a new formalization. |
| [Automated Kantian Ethics](https://github.com/lsingh123/automatedkantianethics/tree/ea6936cd1599476e0985d14dcd0ec7f82d2a61a5) | `ea6936cd1599476e0985d14dcd0ec7f82d2a61a5` | Isabelle; version not established. No repository license found in inspected top-level listing; GitHub license metadata was null. | Study definitions and test design. Resolve reuse terms before copying implementation. README points to cleaned theory files under `paper/`; build not run. |

The Atlas accepts source checks and precise statements as well as proofs. Its [contribution guide](https://github.com/mbrcic/ai-safety-formalization-atlas/blob/a65e32f8047584686320a3013720624b5efa39ee/CONTRIBUTING.md) asks for a proposal before changes to formalization coverage or public interfaces, plus build, validation, and axiom checks for Lean work. Its threshold for a retained example is substantive use, not a renamed theorem. ProvabilityLogic's [guide](https://github.com/FormalizedFormalLogic/ProvabilityLogic/blob/f599cb1f775316de053d01f539dbfcbc525078a7/CONTRIBUTING.md) requires successful builds without residual proof holes, bibliography/import maintenance when relevant, and disclosure of AI assistance.

No upstream issue, comment, pull request, or message was sent in this audit.

## A bounded contribution with construct validity

**Proposed research unit:** cooperation can improve both modeled players' payoffs while reducing an affected non-player's welfare. This is a foundational counterexample and interpretation test, not a claim of new mathematical discovery.

A useful finite coordination model has two players who can join a pact or abstain, plus a stakeholder who cannot act. The local module `AIMoral/ExcludedStakeholder.lean` assigns both-join payoff `(3,3,-2)`, first-only payoff `(0,2,-1)`, second-only payoff `(2,0,-1)`, and both-abstain payoff `(1,1,0)`. Relative to abstention, the pact improves each player's payoff by 2 while the outsider loses 2. Comparing the outsider against its own baseline avoids assuming that the three welfare coordinates share an interpersonal scale.

Prove separately:

1. Joining together is a strict Nash equilibrium and improves the two players' payoffs relative to abstention.
2. The pact violates the chosen outsider no-harm predicate relative to the baseline.
3. Even stakeholder-inclusive Pareto efficiency does not imply that no-harm predicate: the model permits tradeoffs that Pareto comparisons cannot resolve.

This is a coordination game, not a Prisoner's Dilemma. Its role is to test an overbroad ethical interpretation of cooperation or equilibrium, not to reproduce FairBot. Any claim about program equilibrium needs a separate program-game model and proof. Do not transfer a modal-agent result onto this matrix by terminology alone. The project README records compilation and validation status for the local module; this source audit does not certify that status independently.

Nolan's psychology contribution can concentrate on whether the formal predicates measure their intended constructs. A review sheet should record who is affected, who can consent, what “harm” measures, which baseline is used, and whether identical behavior has different consequences under changed context. Keep participant agreement, theory coherence, and predictive validation as distinct outcomes. A mathematically checked case can still encode the wrong construct.

## 11. Process-integrity assessment

**Verdict: adequate for choosing an initial project; incomplete for systematic coverage.** This is a targeted source audit, not a registered systematic review. Search followed the website to original papers and inspected candidate repository metadata directly. The bounded Löb discrepancy was checked at the theorem and definition level. Other paper coverage is principally abstract-level. External repository builds, comprehensive code search, and exhaustive novelty checks were not performed. A numeric AMSTAR-2 or RoB-2 score would be inappropriate for this mixed mathematical/software source set.

The main corrective actions are to preserve the video's verified source mapping, reproduce selected external dependencies at immutable pins, and review exact theorem-to-model correspondence before making upstream claims. The separate local starter has now passed CI, as recorded in [verification.md](verification.md); the external repositories have not been built here.

## 12. Inference-robustness assessment

**Verdict: the narrow distinction between cooperation and stakeholder-inclusive benefit is robust; practical alignment claims remain unestablished.** The example is sensitive to its welfare definitions and baseline, which must stay visible. Changing outsider harm to a gain removes that counterexample but leaves the general need to model outsiders intact. Proving a global safety claim would require stronger assumptions about objectives, observations, deployment, and the formalization-to-system relationship.

There are no pooled empirical effects, trial samples, or meta-analysis. Q, τ², I², funnel plots, and Egger tests are not applicable. Mathematical robustness here means checking quantifiers, non-vacuity, semantic interpretation, and alternative models. What would change the project choice is an existing maintained formalization of the same stakeholder result with a usable interface, or a more useful bounded problem confirmed by an upstream maintainer.

## Reference integration

Import `../references.bib` into Zotero. Preserve the citation keys when exporting with Better BibTeX. In Obsidian, use notes keyed to `@Critch2016Bounded` and `@Singh2022Kantian`, with relationships `formalizes`, `extends`, `applies`, and `limits-interpretation-of`. Attach this audit as a synthesis note rather than treating it as a primary research paper. No Zotero collection was modified by this audit.
