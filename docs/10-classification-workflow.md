# 10. How to Classify Any Optimization Algorithm

[← Comparison matrix](09-comparison-matrix.md) · [Next: Common confusions →](11-common-confusions.md)

Use this workflow when encountering an unfamiliar optimization method.

## Step 1 — Identify the optimization problem being solved

Ask:

- What are the decision variables?
- Are they continuous, integer, binary, permutations, subsets or mixed?
- What is the objective?
- What are the constraints?
- Is the model linear, nonlinear, convex or nonconvex?
- Is the objective deterministic, noisy or stochastic?

Do not classify the algorithm before understanding the problem class. Guarantees are often problem-dependent.

## Step 2 — Ask what guarantee the method provides

Possible answers:

- global optimality certificate,
- local optimality/stationarity guarantee,
- approximation ratio,
- asymptotic convergence under assumptions,
- no formal solution-quality guarantee.

This determines whether words such as **exact**, **approximation**, **heuristic** or **metaheuristic** are appropriate.

## Step 3 — Separate finite-time guarantees from asymptotic statements

These are not equivalent.

An algorithm may have a theorem saying that, under idealized conditions, it converges to a global optimum as iterations approach infinity. That is different from producing a finite-time certificate that the current solution is globally optimal.

Always ask:

- Is the statement finite-time or asymptotic?
- Is it deterministic or probabilistic?
- Does it hold for every instance or under specific assumptions?

## Step 4 — Determine whether the algorithm uses randomness

Look for:

- random initialization,
- probabilistic transitions,
- mutation,
- sampling,
- randomized rounding,
- randomized tie-breaking,
- Monte Carlo estimates.

If randomness is present, classify the algorithm as stochastic/randomized on this axis.

Do not infer “heuristic” from this fact alone.

## Step 5 — Identify the search representation

Ask what state the algorithm maintains:

- one incumbent solution,
- a population,
- a search tree,
- a frontier/priority queue,
- a probability distribution,
- a surrogate model,
- dual variables and decomposed subproblems.

This often explains the method better than its metaphorical name.

## Step 6 — Determine local vs. global behavior

Ask:

- Does each iteration examine only a neighborhood?
- Are there restarts or perturbations?
- Is the whole feasible region partitioned or bounded systematically?
- Is diversity explicitly maintained?
- Is the method designed to visit multiple basins?

Use **global-search-oriented** when a heuristic explores broadly but does not prove global optimality.

Reserve **globally optimal** for a guarantee, not for a search aspiration.

## Step 7 — Identify information requirements

Does the method use:

- only objective values,
- gradients,
- Hessians,
- constraint Jacobians,
- relaxations,
- bounds,
- simulations,
- surrogate predictions?

This yields labels such as:

- zeroth-order,
- first-order,
- second-order,
- derivative-free,
- model-based,
- surrogate-based.

## Step 8 — Classify the model separately

Independently record whether the optimization model is:

- deterministic or stochastic,
- robust,
- fuzzy,
- single- or multi-objective,
- static, dynamic or online,
- centralized or distributed.

Never merge model attributes with algorithm attributes.

## Step 9 — State implementation-dependent properties explicitly

Some properties are not inherent to the method family.

For example:

- Tabu Search may be deterministic or stochastic.
- Branch and Bound may use randomized branching.
- Bayesian Optimization may use deterministic or stochastic acquisition optimization.
- Hill Climbing may use deterministic best-improvement or randomized move selection.

Prefer “usually,” “in the standard implementation,” or “implementation-dependent” when needed.

## Step 10 — Write the final classification as a sentence

### Example: Simulated Annealing

> Simulated Annealing is a single-solution, usually stochastic metaheuristic that accepts some worsening moves according to a temperature-controlled rule in order to reduce local trapping and encourage broader search. A finite run normally does not certify global optimality.

### Example: Branch and Cut

> Branch and Cut is an exact mixed-integer optimization framework that combines Branch and Bound with dynamically generated valid inequalities. It is usually deterministic at the conceptual level, although solver implementations may use randomized or adaptive components. If terminated before closing the optimality gap, the incumbent is not yet a proved optimum.

### Example: NSGA-II

> NSGA-II is a stochastic, population-based evolutionary metaheuristic for multi-objective optimization. It uses nondominated sorting and diversity preservation to approximate a Pareto front rather than returning one universally best solution.

## A reusable classification template

Copy this template when documenting a method:

```text
Method:
Problem class:
Guarantee:
Randomness:
Search scope:
Representation:
Information used:
Constraint handling:
Single- or multi-objective:
Model uncertainty:
Typical strengths:
Typical limitations:
Important assumptions / caveats:
```

If these fields are filled carefully, most common taxonomy mistakes disappear.
