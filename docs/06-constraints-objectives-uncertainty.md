# 6. Constraints, Objectives and Uncertainty

[← Problem structure](05-problem-structure.md) · [Next: Time, distribution and model access →](07-time-distribution-and-model-access.md)

## 6.1 Unconstrained optimization

An unconstrained problem has the form

```math
\min_{x\in\mathbb{R}^n} f(x).
```

Every point in the variable domain is formally admissible. The challenge lies in the objective landscape rather than explicit feasibility constraints.

## 6.2 Constrained optimization

A constrained problem may be written as

```math
\begin{aligned}
\min \quad & f(x) \\
\text{s.t.}\quad & g_i(x)\le0, \\
& h_j(x)=0.
\end{aligned}
```

Important concepts and methods include:

- Lagrange multipliers,
- KKT conditions,
- penalty methods,
- barrier methods,
- interior-point methods,
- Augmented Lagrangian methods,
- feasibility restoration.

## 6.3 Hard constraints

A hard constraint must be satisfied.

For example:

```math
x_1+x_2\le100.
```

A solution violating the constraint is infeasible.

Exact mathematical-programming solvers typically preserve or restore feasibility according to the model and numerical tolerances. Heuristics may need explicit feasibility-preserving operators or repair mechanisms.

## 6.4 Soft constraints

A soft constraint may be violated at a cost.

One common penalty formulation is

```math
F(x)=f(x)+\lambda P(x),
```

where `P(x)` measures violation and `λ` controls the penalty strength.

Soft constraints are useful when requirements represent preferences rather than inviolable rules.

## 6.5 Single-objective optimization

A single-objective model optimizes one scalar criterion:

```math
\min f(x).
```

Examples:

- minimize cost,
- minimize distance,
- minimize makespan,
- maximize profit by minimizing negative profit.

Multiple business considerations can still be embedded into one scalar objective through weighting or penalties, but that is a modeling decision.

## 6.6 Multi-objective optimization

A multi-objective problem optimizes several criteria:

```math
\min
\begin{bmatrix}
f_1(x)\\
f_2(x)\\
\vdots\\
f_k(x)
\end{bmatrix}.
```

Typical conflicts include:

- cost vs. service level,
- quality vs. lead time,
- return vs. risk,
- cost vs. carbon emissions.

### Pareto dominance

For minimization, solution `y` dominates `x` if

```math
f_i(y)\le f_i(x), \qquad \forall i,
```

and for at least one objective `j`,

```math
f_j(y)<f_j(x).
```

A Pareto-optimal solution is not dominated by another feasible solution.

The goal is often a **Pareto frontier**, not one universally best solution.

### Common approaches

- Weighted Sum,
- ε-constraint method,
- Goal Programming,
- NSGA-II,
- NSGA-III,
- SPEA2,
- MOEA/D,
- multi-objective PSO.

## 6.7 Deterministic optimization models

A deterministic model assumes model parameters are known constants. For example,

```math
c,\;A,\;b
```

are fixed data.

This use of “deterministic” describes the **model**, not the algorithm.

## 6.8 Stochastic optimization models

A stochastic model represents uncertain quantities as random variables, for example

```math
\xi\sim P.
```

A common objective is

```math
\min_x \mathbb{E}[f(x,\xi)].
```

Major approaches include:

- two-stage stochastic programming,
- multistage stochastic programming,
- Sample Average Approximation,
- chance-constrained programming.

Stochastic Gradient Descent is different: its name primarily describes **algorithmic sampling/randomness**, not necessarily uncertainty in the decision model.

## 6.9 Robust optimization

Robust optimization often assumes uncertain parameters lie in an uncertainty set:

```math
\xi\in U.
```

A simple worst-case formulation is

```math
\min_x \max_{\xi\in U} f(x,\xi).
```

The central distinction from classical stochastic optimization is:

- stochastic optimization uses a probabilistic model or distributional information,
- robust optimization protects against a specified uncertainty set or ambiguity description.

Modern formulations can be more sophisticated, including distributionally robust optimization, but the conceptual difference remains useful.

## 6.10 Fuzzy optimization

Fuzzy optimization represents imprecise goals or parameters using fuzzy sets and membership functions.

Examples of linguistic requirements include:

- “cost should be approximately 100,”
- “delivery time should be as low as reasonably possible,”
- “risk should remain at an acceptable level.”

Fuzzy optimization is conceptually different from probabilistic uncertainty: membership grades express degree of satisfaction or compatibility, not necessarily probability.

## 6.11 Do not confuse model uncertainty with algorithm randomness

Four combinations are possible:

| Model | Algorithm | Possible? |
|---|---|---|
| Deterministic | Deterministic | Yes |
| Deterministic | Stochastic | Yes |
| Stochastic | Deterministic | Yes |
| Stochastic | Stochastic | Yes |

For example, a deterministic TSP instance can be solved by a stochastic Genetic Algorithm. Conversely, a deterministic decomposition algorithm may solve a stochastic-programming reformulation.
