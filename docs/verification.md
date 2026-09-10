# Verification record: excluded-stakeholder counterexample

Recorded 2026-09-10. **Python finite checks passed; Lean source is a candidate
pending a successful build on an ordinary Lean runtime or GitHub CI.**

## Claim and assumptions

Two agents choose `abstain` or `join`. An affected outsider has no action in this
game. Outcomes are stipulated welfare coordinates, not measurements:

| Agent 1 | Agent 2 | Agent 1 welfare | Agent 2 welfare | Outsider welfare |
|---|---|---:|---:|---:|
| abstain | abstain | 1 | 1 | 0 |
| join | abstain | 0 | 2 | −1 |
| abstain | join | 2 | 0 | −1 |
| join | join | 3 | 3 | −2 |

The baseline is `abstain/abstain`. The chosen normative predicate is
`outsider welfare at outcome ≥ outsider welfare at baseline`. This rule is an
additional modeling choice. It is not derived from rationality or asserted as a
complete theory of morality. Calling the joint outcome a cooperative pact is a
description of the agents' relationship, not a positive moral evaluation.

The finite checks establish that:

1. `join/join` and the baseline are strict pure Nash equilibria.
2. `join/join` is Pareto efficient among the agents and Pareto dominates their
   baseline payoffs.
3. `join/join` violates the chosen outsider no-harm predicate.
4. Adding the outsider makes the joint pact and baseline Pareto incomparable.
5. The pact remains Pareto efficient even with the outsider included. Merely
   including affected parties in an outcome vector therefore does not enforce
   the no-harm constraint.
6. Only the baseline satisfies the chosen no-harm constraint in this table.

Consequently, the stated game properties do not entail the chosen constraint.
This is a small counterexample formalization and teaching/review artifact, not a
novel discovery about game theory or evidence that any actual AI behaves this
way. The results are about four pure deterministic profiles. They do not assert
mixed-strategy or correlated-equilibrium properties, repeated-game behavior,
logical source-code cooperation, uncertainty, or empirical welfare estimates.

## Executed Python checks

Commands from the repository root:

```sh
python3 scripts/check_game.py
python3 -m unittest discover -s tests -v
```

Results: all nine reported table claims passed; all seven tests passed. Tests
include a safe equilibrium that is inefficient among agents, failed unilateral
profiles, irreflexive Pareto dominance, a tied deviation that invalidates strict
Nash, changing only outsider payoffs while keeping agent equilibrium properties
fixed, and changing the declared no-harm reference.

These checks exhaust the four listed profiles. They do not replace checking the
Lean file, and agreement has not been promoted to a machine-checked theorem.

## Lean status and reproducibility

Files: `AIMoral/ExcludedStakeholder.lean`, `AIMoral.lean`, `lakefile.toml`, and
`lean-toolchain`. The toolchain is pinned to `leanprover/lean4:v4.19.0`. There are
no third-party Lean package dependencies; the file imports `Std`.

Reproduction command with this toolchain installed:

```sh
lake build
```

The intended Lean claims use ordinary `decide`, case analysis, and implication
elimination. There are no `sorry`, `admit`, added axioms, or `native_decide` calls.
Their presence as source text does not establish successful elaboration or proof
checking. A green CI build is the next verification gate.

Local attempt downloaded the official Lean 4.19.0 Linux release. The compiler
failed during runtime startup, before reading project code:

```text
lean --version
error: failed to locate application

lake build
error: could not detect the configuration of the Lake installation
```

Official runtime source performs application-location lookup through
`/proc/<pid>/exe`; this environment does not resolve that lookup for Lean.
Explicit installation-path settings did not resolve startup. A diagnostic
tracing attempt was also unavailable (`PTRACE_TRACEME: Operation not permitted`).
No runtime restrictions were bypassed, and no compiler success is claimed here.

Official provenance: [Lean 4.19.0 release](https://github.com/leanprover/lean4/releases/tag/v4.19.0)
and [Lean 4.19.0 application-path implementation](https://github.com/leanprover/lean4/blob/v4.19.0/src/runtime/io.cpp).

## Review boundaries

**Process integrity:** the chosen table, baseline, formal predicates, executable
checker, and contrast tests are explicit. The Python result is reproducible.
Lean verification remains incomplete until CI is observed to pass. Source and
Python use parallel definitions; no automatic cross-language equivalence proof
is supplied.

**Inference robustness:** the logical non-implication needs only one valid
counterexample. Changing outsider welfare to zero removes the no-harm violation
without changing the agents' game; this is tested. Changing the reference can
also change the predicate. Thus these results establish a distinction between
game properties and an additional normative requirement, not a uniquely correct
choice of moral rule. Meta-analysis quantities such as I² and pooled effect sizes
are inapplicable to this finite mathematical construction.
