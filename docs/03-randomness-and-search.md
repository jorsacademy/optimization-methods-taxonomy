# 3. Randomness, Local/Global Search, Exploration and Exploitation

[← Solution guarantees](02-solution-guarantees.md) · [Next: Representation and metaheuristics →](04-search-representation-and-metaheuristics.md)

## 3.1 Deterministic algorithms

A deterministic algorithm follows the same computational logic for the same input, initial state and parameterization, assuming deterministic tie-breaking and execution.

Conceptually:

```math
(x^{(0)},\theta) \longrightarrow x^{(1)} \longrightarrow \cdots \longrightarrow x^{(T)}.
```

With all conditions fixed, repeated runs reproduce the same path and result.

Examples can include:

- Simplex with a fixed pivot rule,
- Dijkstra with fixed tie-breaking,
- full-batch Gradient Descent,
- deterministic greedy algorithms,
- deterministic local search,
- Branch and Bound with fixed branching/node-selection rules,
- Hungarian algorithm.

Deterministic does **not** imply:

- exact,
- globally optimal,
- polynomial-time,
- fast,
- robust to initialization.

A deterministic local-search method can repeatedly converge to the same poor local optimum.

## 3.2 Stochastic or randomized algorithms

A stochastic algorithm uses randomness in at least part of its search process.

A transition may be written abstractly as

```math
x^{(t+1)} \sim P(\cdot \mid x^{(t)}).
```

Different runs can therefore produce different trajectories and solutions.

Examples:

- Genetic Algorithm,
- Simulated Annealing,
- Differential Evolution,
- Particle Swarm Optimization,
- Ant Colony Optimization,
- Random Search,
- Stochastic Gradient Descent,
- randomized rounding.

### Why randomness is useful

Randomness can help:

- escape local optima,
- maintain diversity,
- explore disconnected or irregular regions,
- reduce sensitivity to a single deterministic path,
- sample large spaces that cannot be enumerated.

### Why randomness creates evaluation requirements

A single stochastic run is rarely enough to characterize performance. Report, when relevant:

- number of independent runs,
- random seeds,
- mean,
- median,
- standard deviation or another dispersion measure,
- best and worst values,
- runtime or evaluation budget,
- success rate or target-hit rate,
- stopping criteria.

Avoid reporting only the best run unless the experimental protocol explicitly justifies it.

## 3.3 Randomized exact methods

Randomness and exactness are compatible.

An exact framework may use random choices for:

- branching order,
- tie-breaking,
- cut selection,
- primal heuristic timing,
- restarts,
- initialization.

If the exact framework still explores or bounds the search space correctly and eventually proves optimality, randomness changes the computational route, not the guarantee.

This is the clearest counterexample to the mistaken identity:

```math
\text{Exact} = \text{Deterministic}.
```

They are independent properties.

## 3.4 Local search

Let `N(x)` denote a neighborhood of solution `x`:

```math
N(x)=\{y : y \text{ is considered a neighbor of } x\}.
```

A local minimum relative to that neighborhood satisfies

```math
f(x^*) \le f(y), \qquad \forall y\in N(x^*).
```

This does not imply that `x^*` is globally optimal over the entire feasible set.

Common local or locally driven methods include:

- Hill Climbing,
- local search,
- 2-opt and 3-opt,
- Coordinate Descent,
- Gradient Descent,
- Newton-type methods,
- Hooke–Jeeves,
- Nelder–Mead.

Whether a continuous local method finds a global optimum depends strongly on problem structure. For convex optimization, every local minimum is global. For nonconvex optimization, local behavior can be genuinely limiting.

## 3.5 Global search

A global optimization method attempts to reason about or explore the broader feasible region rather than only a single local neighborhood.

A global minimizer satisfies

```math
f(x^*) \le f(x), \qquad \forall x\in X.
```

But the phrase **global search** is ambiguous unless the guarantee is stated.

### Exact global methods

Examples:

- spatial Branch and Bound,
- deterministic global optimization with valid relaxations,
- interval methods under suitable assumptions.

These can provide global-optimality certificates.

### Global-search-oriented metaheuristics

Examples:

- Simulated Annealing,
- Genetic Algorithm,
- Differential Evolution,
- Particle Swarm Optimization,
- Basin Hopping,
- multi-start methods.

These are designed to explore multiple basins or regions, but a finite run generally does not certify the global optimum.

Therefore:

> **global-search behavior ≠ global-optimum guarantee**.

## 3.6 Exploration and exploitation

Metaheuristics are often understood through the balance between two behaviors.

### Exploitation / intensification

Search deeply around known promising regions.

Examples:

- local improvement,
- elite preservation,
- neighborhood search around an incumbent,
- gradient-based refinement,
- path relinking toward high-quality solutions.

Too much exploitation can cause premature convergence or repeated trapping in one basin.

### Exploration / diversification

Search new or under-explored regions.

Examples:

- mutation,
- randomized restart,
- large neighborhood moves,
- diversity-preserving selection,
- migration among subpopulations,
- perturbation mechanisms.

Too much exploration can prevent the algorithm from sufficiently refining good regions.

The design problem is therefore a balance:

```math
\text{Exploration} \longleftrightarrow \text{Exploitation}.
```

## 3.7 Local/global and exploration/exploitation are related, but not identical

A method may be locally driven yet achieve broad search through restarts, memory or perturbations. Variable Neighborhood Search, Iterated Local Search and multi-start local search are examples of this pattern.

Conversely, a population-based method may still lose diversity and behave almost locally after premature convergence.

So classification should describe both:

- the **mechanics of individual moves**, and
- the **overall search behavior** created by the full algorithm.
