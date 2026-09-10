"""Contrast cases guard against confusing equilibrium, Pareto, and no-harm.

Run with: python3 -m unittest discover -s tests -v
"""

import unittest

from scripts.check_game import (
    BASELINE,
    GAME,
    PACT,
    PROFILES,
    check,
    dominates,
    no_outsider_harm,
    pareto_efficient,
    strict_nash,
)


class ExcludedStakeholderTests(unittest.TestCase):
    def test_exhaustive_counterexample_checks(self):
        self.assertTrue(check()["all_checks_passed"])

    def test_baseline_is_equilibrium_but_not_agent_pareto_efficient(self):
        self.assertTrue(strict_nash(GAME, BASELINE))
        self.assertFalse(pareto_efficient(GAME, BASELINE))
        self.assertTrue(no_outsider_harm(GAME, BASELINE))

    def test_mismatched_profiles_are_not_equilibria(self):
        for profile in ((False, True), (True, False)):
            with self.subTest(profile=profile):
                self.assertFalse(strict_nash(GAME, profile))

    def test_pareto_comparison_is_irreflexive(self):
        for profile in PROFILES:
            self.assertFalse(dominates(GAME, profile, profile, (0, 1)))
            self.assertFalse(dominates(GAME, profile, profile, (0, 1, 2)))

    def test_tied_deviation_breaks_strict_nash(self):
        changed = dict(GAME)
        changed[(False, True)] = (3, 0, -1)
        self.assertFalse(strict_nash(changed, PACT))

    def test_fixing_outsider_payoffs_changes_moral_predicate_not_agent_game(self):
        repaired = {p: (v[0], v[1], 0) for p, v in GAME.items()}
        for profile in PROFILES:
            self.assertEqual(strict_nash(GAME, profile), strict_nash(repaired, profile))
            self.assertEqual(pareto_efficient(GAME, profile), pareto_efficient(repaired, profile))
            self.assertTrue(no_outsider_harm(repaired, profile))
        self.assertTrue(dominates(repaired, PACT, BASELINE, (0, 1, 2)))

    def test_harm_predicate_depends_on_explicit_reference(self):
        self.assertFalse(no_outsider_harm(GAME, PACT, BASELINE))
        self.assertTrue(no_outsider_harm(GAME, PACT, PACT))


if __name__ == "__main__":
    unittest.main()
