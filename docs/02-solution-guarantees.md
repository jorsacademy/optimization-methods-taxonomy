# 2. Solution Guarantees: Exact, Approximation, Heuristic and Metaheuristic Methods

[← Foundations](01-foundations.md) · [Next: Randomness and search →](03-randomness-and-search.md)

## 2.1 Exact methods

An **exact method** is designed so that, under its mathematical assumptions and when allowed to terminate normally, it can identify an optimal solution or provide a valid certificate of optimality.

For

```math
\min_{x\in X} f(x),
```

an optimal solution `x^*` satisfies

```math
f(x^*) \le f(x), \qquad \forall x\in X.
```

Exactness is a statement about mathematical guarantees, not about speed. An exact method may be extremely fast on one instance and computationally prohibitive on another.

### Typical exact-method families

#### Linear programming

For a linear program such as

```math
\begin{aligned}
\min \quad & c^T x \\
\text{s.t.}\quad & Ax \le b,
\end{aligned}
```

standard exact-solution algorithm families include:

- Simplex,
- Dual Simplex,
- interior-point methods.

In practical floating-point solvers, “exact” should be read in the optimization sense: the mathematical algorithm targets an optimal solution and solvers terminate within numerical feasibility/optimality tolerances. It does **not** imply symbolic arithmetic or zero numerical error.

#### Mixed-integer and discrete optimization

Important exact frameworks include:

- Branch and Bound,
- Branch and Cut,
- Cutting Plane methods,
- Branch and Price,
- Branch-Cut-and-Price.

Their central strategy is to derive bounds, partition the feasible set, eliminate regions that cannot improve the incumbent, and close the optimality gap.

For a minimization problem, a solver often maintains:

- an **upper bound** from the best feasible incumbent, and
- a **lower bound** from relaxations or node bounds.

When the bounds meet within the chosen tolerance, optimality is certified.

#### Dynamic programming

Dynamic Programming decomposes a problem into overlapping subproblems with an optimal-substructure relationship. A generic Bellman recursion can be written as

```math
V(s)=\min_{a\in A(s)} \left\{c(s,a)+V(T(s,a))\right\}.
```

Applications include:

- knapsack variants,
- shortest-path formulations,
- inventory control,
- resource allocation,
- multistage decision problems.

Dynamic Programming can be exact, but its state space may grow exponentially or combinatorially: the classical **curse of dimensionality**.

#### Specialized graph algorithms

Some algorithms are exact for specific problem classes:

- Dijkstra — shortest path with nonnegative edge weights,
- Bellman–Ford — single-source shortest path with negative edges but no reachable negative cycle,
- Floyd–Warshall — all-pairs shortest paths,
- Kruskal and Prim — minimum spanning tree,
- Edmonds–Karp — maximum flow,
- Hungarian algorithm — assignment problem.

These are not general-purpose exact solvers for arbitrary optimization models; their guarantees rely on the structure of the problem class.

## 2.2 Continuous optimization: why the word “exact” needs care

For continuous numerical optimization, it is often clearer to describe **convergence guarantees** than to label an iterative numerical method simply “exact.”

Examples include:

- Gradient Descent,
- Newton's method,
- Quasi-Newton methods such as BFGS,
- Conjugate Gradient,
- Sequential Quadratic Programming (SQP).

Whether such methods reach a global optimum depends on assumptions:

- convexity or strong convexity,
- differentiability or smoothness,
- constraint qualifications,
- line-search or trust-region conditions,
- initialization and numerical tolerances.

For a convex problem, a suitable method may have a global convergence guarantee to the global optimum. For a nonconvex problem, the same method may converge only to a stationary point or local optimum.

Therefore:

> **Algorithm name + problem assumptions + convergence theorem** is more informative than calling a continuous method “exact” without qualification.

## 2.3 Approximation algorithms

An **approximation algorithm** returns a solution with a proven quality bound relative to the optimum.

For a minimization problem, an `α`-approximation guarantee may take the form

```math
f(x_{alg}) \le \alpha f(x^*), \qquad \alpha \ge 1.
```

If `α = 2`, the algorithm guarantees a solution whose objective value is at most twice the optimum, under the assumptions of the theorem.

Examples include:

- a 2-approximation for Vertex Cover,
- Christofides' algorithm for Metric TSP,
- logarithmic-factor approximations for Set Cover,
- FPTAS constructions for Knapsack variants.

The defining distinction is **not** that an approximation algorithm is always better in practice than a heuristic. It is that it has a **theoretical worst-case quality guarantee**.

### PTAS

A Polynomial-Time Approximation Scheme produces, for every `ε > 0`, a solution satisfying a `(1+ε)`-type guarantee for appropriate minimization problems, while running in polynomial time for each fixed `ε`.

Its dependence on `1/ε` may still be expensive.

### FPTAS

A Fully Polynomial-Time Approximation Scheme is polynomial in both:

- the input size, and
- `1/ε`.

This is a stronger computational guarantee.

## 2.4 Heuristics

A **heuristic** is a problem-solving rule designed to find a good solution efficiently, typically without a general proof of optimality or a worst-case approximation ratio.

Heuristics are often problem-specific.

Examples:

- Nearest Neighbor for TSP,
- greedy assignment rules,
- First Fit / Best Fit in packing,
- scheduling priority rules,
- Savings Algorithm in routing,
- repair procedures,
- constructive insertion rules.

### Example: Nearest Neighbor for TSP

1. Choose a starting city.
2. Move to the nearest unvisited city.
3. Repeat until every city has been visited.
4. Return to the start.

Advantages:

- simple,
- fast,
- scalable,
- useful for generating an initial incumbent.

Limitations:

- locally attractive choices can produce poor global tours,
- result quality depends strongly on instance geometry and starting conditions,
- no general optimality guarantee.

## 2.5 Metaheuristics

A **metaheuristic** is a higher-level search framework that controls how candidate solutions are generated, accepted, diversified and intensified.

A generic pattern is

```text
initial solution(s)
    ↓
candidate generation
    ↓
evaluation
    ↓
acceptance / selection
    ↓
memory / adaptation / diversification
    ↓
stopping rule
```

Typical goals are:

- escape poor local optima,
- explore multiple search regions,
- intensify search near promising solutions,
- balance exploration and exploitation,
- reuse information from previous iterations.

Common metaheuristics include:

- Genetic Algorithm,
- Simulated Annealing,
- Tabu Search,
- Particle Swarm Optimization,
- Ant Colony Optimization,
- Differential Evolution,
- Variable Neighborhood Search,
- GRASP,
- Iterated Local Search,
- Scatter Search,
- Evolution Strategies,
- Memetic Algorithms.

### Heuristic vs. metaheuristic

| Heuristic | Metaheuristic |
|---|---|
| Often problem-specific | Usually a reusable search framework |
| Often expresses a direct construction or improvement rule | Organizes a repeated search process |
| May be a single pass | Usually iterative/adaptive |
| Often emphasizes immediate local decisions | Explicitly manages broader search behavior |
| Example: Nearest Neighbor | Example: Genetic Algorithm |

The boundary is not absolute in every paper. In practice, the most useful distinction is that a metaheuristic is an **algorithmic framework for controlling search**, while a heuristic is often a more direct problem-specific rule.

## 2.6 The relationship among these categories

A practical hierarchy is:

```text
Optimization solution approaches
├── Exact methods
└── Non-exact / approximate approaches
    ├── Approximation algorithms with theoretical quality bounds
    ├── Heuristics
    └── Metaheuristics
```

However, terminology varies by field. In theoretical computer science, “approximation algorithm” has a specific guarantee-oriented meaning. In operations research practice, “approximate methods” may be used more broadly.

The safest habit is to state the guarantee explicitly instead of relying on the label alone.

## 2.7 What to report about guarantees

When presenting an optimization algorithm, state:

- whether global optimality is guaranteed,
- under what assumptions,
- whether termination is finite or asymptotic,
- whether the guarantee concerns a global optimum, local optimum or stationary point,
- whether an approximation ratio exists,
- which feasibility and optimality tolerances are used numerically,
- whether the result is a proof/certificate or only the best incumbent found.

This prevents “found a very good solution” from being confused with “proved optimal.”
