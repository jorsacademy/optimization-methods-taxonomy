# 9. Multi-Dimensional Comparison Matrix

[← Hybrid methods](08-hybrid-methods.md) · [Next: Classification workflow →](10-classification-workflow.md)

The table below illustrates why a one-dimensional taxonomy is insufficient. Labels are intentionally qualified where assumptions or implementation choices matter.

| Method | Guarantee class | Randomness | Search scope | Representation / mechanism | Typical domain | Important qualification |
|---|---|---|---|---|---|---|
| Simplex | Exact for LP | Usually deterministic | Global for LP | Basis / vertex transitions | Linear programming | Numerical solvers use tolerances; pivot rule affects path |
| Interior-point methods | Exact-solution framework for convex/LP classes under assumptions | Usually deterministic | Global under appropriate convexity assumptions | Continuous trajectory / barrier system | LP, convex optimization | Convergence theory depends on problem class and method |
| Branch and Bound | Exact when completed correctly | Usually deterministic; can be randomized | Global/systematic | Search tree + bounds | Integer/global optimization | May stop early with a nonzero optimality gap |
| Branch and Cut | Exact when completed correctly | Usually deterministic; implementation-dependent | Global/systematic | Search tree + cutting planes | MILP | Modern solvers also use heuristics internally |
| Dynamic Programming | Exact for the formulated recursion | Usually deterministic | Global over state recursion | Subproblems / states | Discrete and sequential problems | State explosion may dominate complexity |
| Dijkstra | Exact for its shortest-path assumptions | Deterministic with fixed ties | Global for the specified shortest-path problem | Graph frontier | Graph optimization | Requires nonnegative edge weights |
| Gradient Descent | Assumption-dependent convergence | Usually deterministic in full batch | Locally driven | Single solution, first-order | Continuous optimization | Global optimum under suitable convex assumptions; not generally for nonconvex problems |
| SGD | Assumption-dependent convergence | Stochastic | Locally driven | Single solution, sampled first-order | Large-scale learning/optimization | Randomness comes from sampled gradient estimates |
| Hill Climbing | Heuristic | Deterministic or stochastic | Local | Single solution | General/discrete | Strongly neighborhood- and initialization-dependent |
| Nearest Neighbor | Heuristic | Usually deterministic after start/tie rules | Constructive/local decision rule | Single constructive solution | TSP-like routing | Fast but no general optimality guarantee |
| Christofides | Approximation algorithm | Deterministic in standard form | Global construction | Constructive graph algorithm | Metric TSP | Approximation guarantee depends on metric assumptions |
| Simulated Annealing | Metaheuristic | Stochastic | Global-search-oriented | Single solution | General | Finite runs do not normally certify global optimality |
| Tabu Search | Metaheuristic | Deterministic or stochastic | Global-search-oriented | Single solution + memory | Combinatorial optimization | Memory and neighborhood design drive behavior |
| Genetic Algorithm | Metaheuristic | Usually stochastic | Global-search-oriented | Population, evolutionary | General | No general finite-run optimality certificate |
| Particle Swarm Optimization | Metaheuristic | Usually stochastic | Global-search-oriented | Population/swarm | Continuous and adapted variants | Sensitive to parameterization/topology |
| Differential Evolution | Metaheuristic | Stochastic | Global-search-oriented | Population, evolutionary | Continuous/global optimization | Strong derivative-free baseline in many black-box settings |
| Ant Colony Optimization | Metaheuristic | Stochastic | Global-search-oriented | Multi-agent + pheromone model | Combinatorial optimization | Persistent search information is pheromone-based |
| Bayesian Optimization | Surrogate-based approximate optimization | Implementation-dependent | Global-search-oriented | Surrogate + acquisition | Expensive black-box optimization | Best suited when evaluations are costly; dimensionality matters |
| CMA-ES | Metaheuristic / evolutionary strategy | Stochastic | Global-search-oriented | Population + adaptive covariance | Continuous black-box optimization | Derivative-free; evaluation cost can be high |
| NSGA-II | Multi-objective evolutionary metaheuristic | Stochastic | Global-search-oriented | Population + Pareto ranking | Multi-objective optimization | Produces an approximation to the Pareto set/front |
| ADMM | Decomposition/first-order framework | Usually deterministic | Depends on model | Distributed/decomposed iterates | Convex structured optimization | Classical guarantees rely on convexity/regularity assumptions |

## 9.1 Reading the table correctly

The same row contains labels from several independent axes. For example:

### Genetic Algorithm

- **metaheuristic** = guarantee/search-framework classification,
- **stochastic** = randomness classification,
- **global-search-oriented** = search-scope description,
- **population** = representation,
- **evolutionary** = search mechanism.

### Branch and Bound

- **exact** = guarantee classification,
- **usually deterministic** = common implementation behavior,
- **global/systematic** = search scope,
- **search tree + bounds** = representation/mechanism.

This is the intended use of the entire taxonomy.
