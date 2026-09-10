import Std

/-!
# Cooperation does not entail protection of excluded stakeholders

A finite counterexample, not a definition or proof of morality. Two agents can
join a pact. The outsider has a welfare coordinate but no move in this game.
`false` means abstain; `true` means join. Welfare numbers and the baseline are
stipulated model assumptions. `NoOutsiderHarm` is an explicit, chosen normative
constraint. Nash and Pareto claims are mathematical properties of the table.

Only pure strategies and the four listed deterministic outcomes are considered.
The project makes no claim about actual AI behavior, subjective experience, or
the universal moral authority of its welfare scale.
-/

namespace AIMoral.ExcludedStakeholder

abbrev Profile := Bool × Bool
abbrev AgentUtility := Profile → Bool → Int

/-- Outcome coordinates: first agent, second agent, excluded outsider. -/
def outcome : Profile → Int × Int × Int
  | (false, false) => (1, 1, 0)
  | (true, false)  => (0, 2, -1)
  | (false, true)  => (2, 0, -1)
  | (true, true)   => (3, 3, -2)

def agents : AgentUtility := fun p who =>
  if who then (outcome p).2.1 else (outcome p).1

def outsider (p : Profile) : Int := (outcome p).2.2

def baseline : Profile := (false, false)
def pact : Profile := (true, true)

/-- Every different unilateral action is strictly worse for its choosing agent. -/
def StrictNash (u : AgentUtility) (p : Profile) : Prop :=
  (∀ a : Bool, a ≠ p.1 → u (a, p.2) false < u p false) ∧
  (∀ b : Bool, b ≠ p.2 → u (p.1, b) true < u p true)

/-- At least one agent improves and neither agent loses; outsider is omitted. -/
def AgentParetoDominates (u : AgentUtility) (q p : Profile) : Prop :=
  (∀ a : Bool, u p a ≤ u q a) ∧ (∃ a : Bool, u p a < u q a)

def AgentParetoEfficient (u : AgentUtility) (p : Profile) : Prop :=
  ∀ q : Profile, ¬ AgentParetoDominates u q p

/-- Pareto comparison with the excluded outsider added to the welfare vector. -/
def StakeholderParetoDominates (q p : Profile) : Prop :=
  (agents p false ≤ agents q false ∧
   agents p true ≤ agents q true ∧ outsider p ≤ outsider q) ∧
  (agents p false < agents q false ∨
   agents p true < agents q true ∨ outsider p < outsider q)

def StakeholderParetoEfficient (p : Profile) : Prop :=
  ∀ q : Profile, ¬ StakeholderParetoDominates q p

/-- Chosen normative rule, relative to a declared baseline, not derived from Nash. -/
def NoOutsiderHarm (reference p : Profile) : Prop :=
  outsider reference ≤ outsider p

theorem pact_strict_nash : StrictNash agents pact := by
  unfold StrictNash
  decide

theorem baseline_strict_nash : StrictNash agents baseline := by
  unfold StrictNash
  decide

theorem pact_agent_pareto_efficient : AgentParetoEfficient agents pact := by
  unfold AgentParetoEfficient AgentParetoDominates
  intro q
  rcases q with ⟨a, b⟩
  cases a <;> cases b <;> decide

theorem pact_dominates_baseline_for_agents :
    AgentParetoDominates agents pact baseline := by
  unfold AgentParetoDominates
  decide

theorem pact_harms_outsider : ¬ NoOutsiderHarm baseline pact := by
  unfold NoOutsiderHarm
  decide

theorem baseline_satisfies_chosen_rule : NoOutsiderHarm baseline baseline := by
  unfold NoOutsiderHarm
  decide

/-- Enlarging the vector reveals the tradeoff; it does not resolve it. -/
theorem baseline_and_pact_stakeholder_incomparable :
    ¬ StakeholderParetoDominates pact baseline ∧
    ¬ StakeholderParetoDominates baseline pact := by
  unfold StakeholderParetoDominates
  decide

/-- Even all-stakeholder Pareto efficiency does not enforce the no-harm rule. -/
theorem pact_still_stakeholder_pareto_efficient :
    StakeholderParetoEfficient pact := by
  unfold StakeholderParetoEfficient StakeholderParetoDominates
  intro q
  rcases q with ⟨a, b⟩
  cases a <;> cases b <;> decide

theorem cooperation_properties_do_not_entail_no_harm :
    ¬ (∀ p : Profile, StrictNash agents p → AgentParetoEfficient agents p →
      NoOutsiderHarm baseline p) := by
  intro claimed
  exact pact_harms_outsider
    (claimed pact pact_strict_nash pact_agent_pareto_efficient)

/-- This finite game has a safe baseline equilibrium, but the rule is additional. -/
theorem chosen_rule_selects_baseline (p : Profile) :
    NoOutsiderHarm baseline p ↔ p = baseline := by
  unfold NoOutsiderHarm
  rcases p with ⟨a, b⟩
  cases a <;> cases b <;> decide

end AIMoral.ExcludedStakeholder
