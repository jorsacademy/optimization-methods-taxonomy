# 11. Common Confusions and FAQ

[← Classification workflow](10-classification-workflow.md) · [Back to README](../README.md)

## Is every exact method deterministic?

No. Exactness describes the guarantee. Determinism describes whether randomness is used. A randomized search order can still belong to an exact framework if the final algorithm preserves the proof of optimality.

## Is every stochastic method a heuristic?

No. Randomized exact algorithms exist. Randomness can affect computational path without removing the optimality guarantee.

## Is every heuristic stochastic?

No. Greedy construction rules and deterministic local search are common deterministic heuristics.

## Is every metaheuristic stochastic?

No. Many are stochastic in common implementations, but stochasticity is not part of the definition. Tabu Search and Variable Neighborhood Descent can be implemented deterministically.

## Are heuristic and metaheuristic synonyms?

No. A heuristic is often a direct problem-specific solution rule. A metaheuristic is usually a higher-level reusable framework for controlling repeated search, diversification and intensification.

## Is an approximation algorithm just another heuristic?

Not in the technical sense used here. An approximation algorithm comes with a proven bound on solution quality. A generic heuristic usually does not.

## Does “global optimization method” mean it guarantees the global optimum?

Not necessarily. Some global optimization methods are exact and certify a global optimum. Others are global-search-oriented heuristics or metaheuristics that explore broadly without a finite-time certificate.

## Is a local search necessarily heuristic?

In most combinatorial-optimization usage, local search is heuristic. More generally, “local” describes the search mechanism. Under special structural assumptions, locally driven methods may still have global guarantees—for example, convex optimization makes every local minimum global.

## Does Gradient Descent find the global optimum?

Only under suitable assumptions. For a convex objective with appropriate step-size conditions, global convergence results are available. For a nonconvex problem, Gradient Descent may converge to a stationary point or local minimum instead.

## Is Newton's method exact?

Calling Newton's method simply “exact” is usually unhelpful. It is a second-order iterative numerical method. Its convergence behavior depends on smoothness, initialization, curvature and the problem class. The guarantee should be stated rather than compressed into the word exact.

## Is Simplex deterministic?

With fixed pivot and tie-breaking rules, yes. Different pivot rules can follow different paths. Randomized tie-breaking is also possible. The method's LP optimality framework is separate from that implementation detail.

## Does Branch and Bound always return the optimum?

If a correct exact Branch and Bound procedure is allowed to complete under its assumptions, it can certify optimality. In practice, users often stop a solver early because of time limits, node limits or acceptable optimality gaps. In that case, the best incumbent is not necessarily proven optimal.

## Is a deterministic model solved only by deterministic algorithms?

No. A deterministic optimization model can be solved using a stochastic metaheuristic.

## Is stochastic programming the same as using a stochastic algorithm?

No.

- **Stochastic programming**: uncertainty is part of the optimization model.
- **Stochastic algorithm**: randomness is part of the solution procedure.

These can occur independently.

## Is robust optimization the same as stochastic optimization?

No. Stochastic optimization typically uses probability distributions or scenarios with probabilistic meaning. Robust optimization protects against uncertainty described by sets or ambiguity descriptions and often emphasizes worst-case protection.

## Is every linear problem convex?

Yes, standard linear objectives and linear constraint sets are convex. But not every convex problem is linear.

## Is every quadratic problem convex?

No. A quadratic objective is convex when its quadratic matrix is positive semidefinite. Indefinite quadratic forms are nonconvex.

## Is derivative-free the same as black-box?

Not exactly.

- **Derivative-free** means the algorithm does not use derivatives.
- **Black-box** means the analytical structure of the evaluated system is unavailable or intentionally ignored.

A derivative-free method can be applied to an explicit formula, and a black-box optimizer is usually derivative-free because derivatives are unavailable.

## Is Bayesian Optimization a metaheuristic?

It is more precise to call it a **surrogate-based global optimization framework**. It builds a probabilistic or predictive surrogate and chooses new evaluations through an acquisition strategy. It shares some practical goals with metaheuristics but belongs to a different methodological family.

## Is Reinforcement Learning an optimization method?

Reinforcement Learning solves sequential decision problems by learning policies or value functions. It overlaps with Dynamic Programming, stochastic approximation and optimal control, but calling all RL algorithms generic optimization algorithms hides important structure. In this guide, RL appears under dynamic/model-free decision optimization because of that connection.

## Is a population method always better at global search?

No. A population can lose diversity and collapse into one region. Population size alone does not guarantee exploration.

## Is a single-solution method always local?

No. Simulated Annealing, Iterated Local Search and Variable Neighborhood Search maintain one main solution but can produce broad search behavior through stochastic acceptance, perturbation, memory or changing neighborhoods.

## Does using an exact solver inside a heuristic make the whole method exact?

No. The overall method is exact only if the complete outer procedure preserves a valid global optimality proof. Exact subproblem optimization alone is insufficient.

## Do heuristics have no theory at all?

No. A heuristic may have theoretical analysis of runtime, convergence, probabilistic behavior or special-case performance. The key point is that a general optimality or approximation-ratio guarantee is not what defines it.

## What is the safest way to describe an algorithm?

Use multiple labels and state assumptions explicitly:

> guarantee + randomness + search scope + representation + problem class + information used + caveats.

For example:

> “Differential Evolution is a stochastic, population-based, derivative-free evolutionary metaheuristic used primarily for continuous black-box and global-search-oriented optimization; finite runs do not normally certify global optimality.”

That sentence is much more informative than assigning one category.
