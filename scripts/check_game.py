#!/usr/bin/env python3
"""Exhaustively check the four pure outcomes of the excluded-stakeholder game.

This dependency-free executable checks finite table properties. It is separate
from, and is not a substitute for, Lean's proof checking. The welfare table and
no-harm baseline are modeling/normative choices, not discovered moral facts.
"""

from __future__ import annotations

import json
from itertools import product
from typing import Mapping

Profile = tuple[bool, bool]
Outcome = tuple[int, int, int]
PROFILES: tuple[Profile, ...] = tuple(product((False, True), repeat=2))
BASELINE: Profile = (False, False)
PACT: Profile = (True, True)
GAME: dict[Profile, Outcome] = {
    (False, False): (1, 1, 0),
    (True, False): (0, 2, -1),
    (False, True): (2, 0, -1),
    (True, True): (3, 3, -2),
}


def strict_nash(game: Mapping[Profile, Outcome], profile: Profile) -> bool:
    for agent in range(2):
        deviation = list(profile)
        deviation[agent] = not deviation[agent]
        if game[tuple(deviation)][agent] >= game[profile][agent]:
            return False
    return True


def dominates(
    game: Mapping[Profile, Outcome],
    candidate: Profile,
    reference: Profile,
    stakeholders: tuple[int, ...] = (0, 1),
) -> bool:
    return all(game[candidate][i] >= game[reference][i] for i in stakeholders) and any(
        game[candidate][i] > game[reference][i] for i in stakeholders
    )


def pareto_efficient(
    game: Mapping[Profile, Outcome],
    profile: Profile,
    stakeholders: tuple[int, ...] = (0, 1),
) -> bool:
    return not any(dominates(game, other, profile, stakeholders) for other in PROFILES)


def no_outsider_harm(
    game: Mapping[Profile, Outcome], profile: Profile, reference: Profile = BASELINE
) -> bool:
    return game[profile][2] >= game[reference][2]


def label(profile: Profile) -> str:
    return "/".join("join" if action else "abstain" for action in profile)


def check() -> dict:
    checks = {
        "pact_is_strict_nash": strict_nash(GAME, PACT),
        "baseline_is_strict_nash": strict_nash(GAME, BASELINE),
        "pact_is_agent_pareto_efficient": pareto_efficient(GAME, PACT),
        "pact_dominates_baseline_for_agents": dominates(GAME, PACT, BASELINE),
        "pact_violates_chosen_no_harm_rule": not no_outsider_harm(GAME, PACT),
        "pact_does_not_dominate_baseline_for_all": not dominates(
            GAME, PACT, BASELINE, (0, 1, 2)
        ),
        "baseline_does_not_dominate_pact_for_all": not dominates(
            GAME, BASELINE, PACT, (0, 1, 2)
        ),
        "pact_remains_pareto_efficient_for_all": pareto_efficient(
            GAME, PACT, (0, 1, 2)
        ),
        "chosen_no_harm_rule_selects_baseline": tuple(
            p for p in PROFILES if no_outsider_harm(GAME, p)
        ) == (BASELINE,),
    }
    return {
        "scope": "Four deterministic pure profiles; stipulated welfare and baseline.",
        "all_checks_passed": all(checks.values()),
        "checks": checks,
        "outcomes": [
            {
                "profile": label(p),
                "welfare": GAME[p],
                "strict_nash": strict_nash(GAME, p),
                "agent_pareto_efficient": pareto_efficient(GAME, p),
                "stakeholder_pareto_efficient": pareto_efficient(GAME, p, (0, 1, 2)),
                "no_outsider_harm_vs_baseline": no_outsider_harm(GAME, p),
            }
            for p in PROFILES
        ],
    }


if __name__ == "__main__":
    report = check()
    print(json.dumps(report, indent=2))
    raise SystemExit(0 if report["all_checks_passed"] else 1)
