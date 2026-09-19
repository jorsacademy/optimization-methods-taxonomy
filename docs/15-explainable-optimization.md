# 15. Explainable Optimization

[← Benchmarking and experimental methodology](14-benchmarking-experimental-methodology.md) · [Back to README](../README.md)

Explainable optimization asks how to communicate why an optimization system produced a particular decision, which constraints or trade-offs drove it, and how that decision would change under alternative assumptions.

This is different from explaining a predictive model. In optimization, the explanation may come from the mathematical model, dual information, alternative optima, sensitivity analysis, counterfactual solves, or inverse optimization.

## 15.1 Start with the decision model

A useful explanation identifies:

- decision variables,
- objective terms,
- active constraints,
- data and parameters,
- uncertainty assumptions,
- solver status and optimality information.

Without these elements, an explanation risks becoming a narrative detached from the actual optimization model.

## 15.2 Binding constraints

A binding constraint has little or no slack at the reported solution. Binding constraints often help explain why a decision cannot be improved in an intuitive direction.

However, binding does not automatically mean “important.” Degeneracy, redundant constraints, scaling, and alternative optima can complicate interpretation.

Use binding status as evidence, not as a complete causal explanation.

## 15.3 Dual values and shadow prices

For suitable continuous optimization models, dual values quantify a local marginal relationship between a constraint bound and the optimal objective under the assumptions of sensitivity analysis.

A shadow price should be described with its validity range and model context. It is not a universal causal effect.

For mixed-integer models, LP-relaxation duals can still be diagnostically useful, but they should not be presented as if the integer value function were locally smooth.

## 15.4 Reduced costs

Reduced costs can explain why a variable remains at a bound in an LP solution and how its objective coefficient would need to change before the current basis loses optimality.

Again, the interpretation is local to the mathematical-programming model and its assumptions.

## 15.5 Sensitivity analysis

Classical sensitivity questions include:

- How much can an objective coefficient change before the current solution structure changes?
- How much can a right-hand side change?
- Which constraints have the largest marginal values?
- How stable is the decision under parameter perturbation?

For nonlinear, mixed-integer, stochastic, or black-box models, these questions may require repeated re-optimization rather than a single solver sensitivity report.

## 15.6 Alternative optima and near-optimal solutions

A single optimum can hide flexibility.

Decision makers often need to know:

- Are there multiple optimal solutions?
- Which variables can change with negligible objective degradation?
- Which decisions are structurally fixed across near-optimal solutions?
- What trade-offs become available within a tolerance of the optimum?

Near-optimal solution analysis can be more actionable than explaining only one incumbent.

## 15.7 Counterfactual optimization

A counterfactual explanation asks what model change would be required to make a different decision optimal or feasible.

Examples:

- How much additional capacity would allow one more production order?
- What cost reduction would make supplier B enter the optimal allocation?
- How much must a service-level requirement be relaxed to remove overtime?
- What budget increase would make a preferred project portfolio feasible?

Counterfactuals should be solved as explicit optimization problems when possible rather than guessed from informal reasoning.

## 15.8 Inverse optimization

Inverse optimization starts from observed or desired decisions and infers objective parameters, costs, preferences, or other model components that make those decisions optimal or approximately optimal.

This supports a different type of explanation:

```text
forward optimization:
parameters -> optimal decision

inverse optimization:
observed decision -> plausible parameters/preferences
```

It can help reveal which implied priorities are consistent with a decision, subject to identifiability and modeling assumptions.

## 15.9 Explanations for stochastic and robust optimization

Under uncertainty, explanations should identify the risk model.

Useful questions include:

- Which scenarios drive the decision?
- What is the value of added robustness?
- Which uncertainty-set dimensions are active?
- How does a chance-constraint confidence level affect cost?
- What is the cost of robustness relative to a nominal solution?
- Which recourse actions absorb uncertainty?

Do not describe a robust decision simply as “safer” without quantifying the uncertainty model and the trade-off paid for robustness.

## 15.10 Multi-objective explanations

For multi-objective optimization, the central explanation is the trade-off.

Report:

- objective definitions and units,
- Pareto dominance,
- reference or aspiration points,
- marginal trade-offs where meaningful,
- why a selected Pareto solution was chosen.

The optimizer can generate alternatives, but the final preference among nondominated solutions belongs to the decision process rather than to Pareto optimality itself.

## 15.11 Learned and hybrid optimization systems

When machine learning participates in optimization, separate explanations into layers:

1. **prediction layer** — what the learned model predicts;
2. **optimization layer** — how objectives and constraints convert predictions into decisions;
3. **decision-quality layer** — how sensitive the final decision is to prediction errors.

A feature that strongly affects a predictor does not necessarily strongly affect the optimized decision. Conversely, a small predictive error near a decision threshold can cause a large downstream change.

## 15.12 A practical explanation template

For an optimization result, provide:

```text
Decision:
    what was selected or allocated?

Objective:
    what quantity was optimized?

Feasibility:
    which constraints are satisfied and which are binding?

Trade-offs:
    what was sacrificed to improve the objective?

Sensitivity:
    which parameters would change the decision?

Alternatives:
    are there near-optimal or Pareto alternatives?

Uncertainty:
    what uncertainty/risk assumptions were used?

Guarantee:
    optimal, bounded-gap, heuristic, or approximate?

Evidence:
    which solver outputs or re-optimization experiments support the explanation?
```

Explainability is strongest when it is generated from the same mathematical model and validation pipeline that produced the decision.
