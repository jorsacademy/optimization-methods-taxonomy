# 1. Foundations: How to Think About Optimization Taxonomies

[← Back to README](../README.md) · [Next: Solution guarantees →](02-solution-guarantees.md)

## 1.1 Why a single taxonomy is misleading

A frequent question is whether optimization methods can be divided into two large classes such as:

- exact / deterministic methods, and
- heuristic / metaheuristic methods.

The useful part of that intuition is the contrast between **guaranteed methods** and **methods that search for good solutions without a general optimality guarantee**. The misleading part is combining `exact` with `deterministic`.

These words answer different questions:

- **Exact** asks: *What can the method prove about the final solution?*
- **Deterministic** asks: *If I repeat the algorithm with the same inputs and settings, does the same computational path occur?*
- **Local/global** asks: *How broadly does the algorithm search?*
- **Single-solution/population-based** asks: *How many candidate solutions are explicitly maintained?*

A useful taxonomy therefore behaves more like a **coordinate system** than a tree. Each algorithm receives one label on several axes.

## 1.2 Optimization problem notation

A general constrained minimization problem can be written as

```math
\begin{aligned}
\min_{x \in X} \quad & f(x) \\
\text{s.t.} \quad & g_i(x) \le 0, \quad i=1,\ldots,m, \\
& h_j(x)=0, \quad j=1,\ldots,p.
\end{aligned}
```

where:

- `x` is the decision vector,
- `X` describes the decision domain,
- `f(x)` is the objective function,
- `g_i(x)` are inequality constraints,
- `h_j(x)` are equality constraints.

Different optimization methods exploit different kinds of structure in this problem.

## 1.3 The most important independent axes

### Axis A — solution guarantee

Questions:

- Does the method prove optimality?
- Does it provide a bound on suboptimality?
- Does it simply return the best solution it found?

Typical labels: **exact**, **approximation**, **heuristic**, **metaheuristic**.

### Axis B — randomness

Questions:

- Is random sampling used?
- Is initialization random?
- Are moves, mutations, selections or branching choices probabilistic?

Typical labels: **deterministic**, **stochastic/randomized**.

### Axis C — search scope

Questions:

- Is improvement driven by the neighborhood of a current solution?
- Is the algorithm designed to explore multiple regions of the search space?
- Does it systematically partition the full search space?

Typical labels: **local**, **global**, or **global-search-oriented**.

### Axis D — search representation

Questions:

- Is one incumbent solution updated iteratively?
- Is a set or population of solutions evolved?
- Is the search represented as a tree, graph, frontier or probability model instead?

Typical labels: **single-solution**, **population-based**, **tree-based**, **model-based**, and other structures.

## 1.4 Why “exact = deterministic” is false

Suppose an exact Branch and Bound implementation uses a random rule to select among tied branching candidates. Different runs may traverse the search tree in different orders, but if the method completes correctly it can still prove the same optimum.

Randomness changes the **path**. Exactness concerns the **guarantee**.

Symbolically:

```math
\text{Exact} \not\equiv \text{Deterministic}
```

and similarly:

```math
\text{Stochastic} \not\equiv \text{Heuristic}.
```

## 1.5 A method may have many labels at once

Consider Simulated Annealing:

- metaheuristic,
- usually stochastic,
- single-solution based,
- global-search-oriented,
- derivative-free in its classical form.

Consider Dijkstra's algorithm with nonnegative edge weights:

- exact for the shortest-path problem it solves,
- deterministic under fixed tie-breaking,
- graph algorithm,
- globally solves that specific shortest-path problem,
- not a metaheuristic.

Consider Gradient Descent:

- usually deterministic in full-batch form,
- local/iterative,
- single-solution based,
- first-order,
- globally convergent to a global minimum only under appropriate assumptions such as convexity and suitable step-size conditions.

The name of an algorithm is therefore not enough; **problem assumptions matter**.

## 1.6 Algorithm classification vs. model classification

A second major source of confusion is that some adjectives describe the **model**, while others describe the **algorithm**.

For example:

- A **deterministic optimization model** treats its parameters as known constants.
- A **deterministic algorithm** uses no algorithmic randomness.

These are logically independent. A deterministic algorithm can solve a stochastic-programming reformulation, and a randomized algorithm can solve a deterministic model.

The same separation is useful for other labels:

- `convex` usually describes problem structure,
- `first-order` describes information used by an algorithm,
- `population-based` describes algorithm representation,
- `multi-objective` describes the model's objective structure.

## 1.7 A practical rule

When describing an optimization method, avoid sentences such as:

> “Genetic Algorithm is a stochastic optimization algorithm.”

That statement is not wrong, but it is incomplete. Prefer a structured description:

> “Genetic Algorithm is a population-based evolutionary metaheuristic that usually uses stochastic operators and is designed for broad exploration of the search space.”

The rest of this guide develops the vocabulary needed to make descriptions like this precise.
