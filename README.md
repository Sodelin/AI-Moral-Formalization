# AI Moral Formalization

A research workspace for making claims about AI cooperation, moral constraints,
and affected stakeholders precise enough to inspect and check.

The starting question is: **what additional assumptions connect successful
cooperation between agents to acceptable outcomes for everyone affected?**

We separate four tasks:

1. **Normative specification:** choose and explain the values or constraints.
2. **Mathematical modeling:** define agents, outcomes, information, and payoffs.
3. **Verification:** prove exactly what follows from those definitions.
4. **External validation:** assess whether the model represents the intended situation.

A checked theorem establishes a consequence of its assumptions. The choice of
those assumptions, their moral justification, and their real-world adequacy
remain separate research questions.

Initial work will combine a source audit of open-source game theory with a
small, reproducible formal example. No solution to AI alignment, moral
philosophy, or an open game-theory problem is claimed.

## Contribution expectations

- Cite the primary source and the exact theorem or claim being formalized.
- Label empirical assumptions, normative choices, and mathematical definitions.
- Report proof status and dependencies; do not present candidate proofs as checked.
- Include counterexamples to stronger claims when they clarify scope.
- Disclose AI assistance and retain human review of semantics and interpretation.
- Keep raw third-party video transcripts and transient metadata out of this repository.

Initial research and implementation are AI-assisted and require human review.

## Initial research package

- [Investigation and contribution plan](docs/investigation.md): video/site findings, scope, and next steps.
- [Video analysis](docs/video-analysis.md): original-caption provenance and timestamped claims.
- [Source audit](docs/source-audit.md): original theorem assumptions, an unposted correction draft, and existing formalization projects.
- [Verification record](docs/verification.md): finite counterexample, proof status, and limitations.
- [Lean model](AIMoral/ExcludedStakeholder.lean): explicit separation of strategic properties from a chosen outsider-protection constraint.
- [Bibliography](references.bib): importable into Zotero, with source-role notes.

The model is a four-profile coordination game with an excluded stakeholder. It
is a foundational counterexample, not a new program-equilibrium result. See the
verification record for the latest checked status.

To reproduce with the pinned Lean toolchain and Python 3.10 or newer:

```sh
lake build --wfail
lake env lean scripts/Audit.lean
python3 scripts/check_game.py
python3 -m unittest discover -s tests -v
```
