# 12. Algorithm and Method Index

[← Common confusions](11-common-confusions.md) · [Back to README](../README.md)

This appendix collects the named methods used throughout the guide and gives a compact classification. It is an index, not a substitute for the assumptions and qualifications explained in the main chapters.

## Exact mathematical-programming and discrete-optimization methods

### Simplex

A basis-based algorithm for linear programming. It is an exact LP solution framework in the optimization sense and is deterministic when pivoting and tie-breaking rules are fixed.

### Dual Simplex

A Simplex variant that maintains dual feasibility while working toward primal feasibility. Widely used inside LP/MILP solvers, particularly after model modifications or branching decisions.

### Interior-Point Methods

Barrier-based numerical methods for linear and convex optimization. Their convergence and optimality guarantees depend on the problem class and method assumptions; practical solvers use numerical tolerances.

### Branch and Bound

An exact search framework that partitions the feasible region and uses bounds to prune regions that cannot improve the incumbent. Common in integer, mixed-integer and global optimization.

### Branch and Cut

Branch and Bound augmented with valid inequalities generated during the search. A foundation of modern MILP solving.

### Cutting Plane Methods

Iteratively add valid constraints that remove infeasible or nonintegral relaxation solutions without excluding valid target solutions.

### Branch and Price

Branch and Bound combined with column generation. Useful when the natural formulation has an enormous number of variables.

### Branch-Cut-and-Price

A solver framework combining branching, cutting planes and column generation.

### Dynamic Programming

An exact method when a valid Bellman recursion covers the required state space. Powerful for sequential or decomposable problems but vulnerable to state-space explosion.

## Graph and network algorithms

### Dijkstra

Exact single-source shortest-path algorithm for graphs with nonnegative edge weights.

### Bellman–Ford

Exact single-source shortest-path algorithm that permits negative edge weights, provided no reachable negative cycle invalidates the finite shortest-path solution.

### Floyd–Warshall

Dynamic-programming algorithm for all-pairs shortest paths.

### Kruskal

Greedy exact algorithm for a minimum spanning tree.

### Prim

Greedy exact algorithm for a minimum spanning tree.

### Ford–Fulkerson

Augmenting-path framework for maximum flow. Termination details depend on capacity assumptions and path selection.

### Edmonds–Karp

A polynomial-time implementation of the augmenting-path idea using breadth-first search.

### Hungarian Algorithm

Exact algorithm for the assignment problem.

## Approximation algorithms and schemes

### Vertex Cover 2-Approximation

A standard example of an approximation algorithm with a proven factor-2 worst-case bound.

### Christofides' Algorithm

A polynomial-time approximation algorithm for Metric TSP with a proven worst-case guarantee under the metric assumptions.

### Set Cover Approximation

Greedy Set Cover has a logarithmic-type approximation guarantee.

### PTAS

A Polynomial-Time Approximation Scheme provides a `(1+ε)`-type approximation for every fixed `ε>0` for problem classes admitting such a scheme.

### FPTAS

A Fully Polynomial-Time Approximation Scheme is polynomial in both input size and `1/ε`.

## Constructive heuristics and local improvement

### Nearest Neighbor

A constructive TSP heuristic that repeatedly visits the nearest unvisited city. Fast and simple, but without a general optimality guarantee.

### Greedy Assignment / Placement Rules

Problem-specific heuristics that make the locally preferred feasible choice at each construction step.

### First Fit and Best Fit

Classical packing heuristics that place items according to the first or best available feasible location under the chosen ordering.

### Savings Algorithm

A constructive routing heuristic, commonly associated with vehicle-routing route merging based on calculated savings.

### Hill Climbing

A local-search heuristic that repeatedly accepts improving moves. It can be deterministic or randomized depending on move selection.

### Local Search

A broad family that improves a current solution using a defined neighborhood. The neighborhood and acceptance rule determine behavior.

### 2-opt and 3-opt

Route-improvement neighborhoods that replace two or three edges, respectively. Common in TSP and routing heuristics.

## Continuous numerical optimization

### Gradient Descent

First-order iterative method. Global-optimum convergence requires suitable assumptions such as convexity and an appropriate step-size rule; in nonconvex settings it is generally a local/stationarity-oriented method.

### Stochastic Gradient Descent (SGD)

A stochastic first-order method based on sampled or noisy gradient estimates. The word stochastic describes the algorithmic gradient estimate and should not be confused with a stochastic optimization model.

### Coordinate Descent

Updates one coordinate or block of coordinates at a time. Guarantees depend on convexity, smoothness and update rules.

### Newton's Method

Second-order method using Hessian information. It can converge very rapidly near a suitable solution but its global behavior depends on problem structure and globalization mechanisms.

### BFGS and L-BFGS

Quasi-Newton methods that approximate second-order information. L-BFGS uses limited memory and is common in large-scale smooth optimization.

### Conjugate Gradient

A major method for quadratic systems and related optimization problems. Its precise role and guarantees depend on the formulation.

### Sequential Quadratic Programming (SQP)

A framework for constrained nonlinear optimization using a sequence of quadratic subproblems.

### Nelder–Mead

Derivative-free direct-search method based on a simplex of points. Common for low-dimensional black-box optimization but without a general global-optimum guarantee.

### Hooke–Jeeves / Pattern Search

Derivative-free search based on exploratory and pattern moves or structured polling directions.

### Powell-Type Methods

Derivative-free methods for continuous optimization using directional searches without requiring explicit gradients.

## Single-solution metaheuristics

### Simulated Annealing

Usually stochastic. Accepts some worsening moves according to a temperature-dependent probability to reduce local trapping. It is single-solution and global-search-oriented.

### Tabu Search

Memory-based metaheuristic using tabu restrictions, aspiration and diversification/intensification mechanisms. It may be deterministic or stochastic.

### Iterated Local Search (ILS)

Alternates local optimization with perturbation and re-optimization to move among attraction basins.

### Variable Neighborhood Search (VNS)

Systematically changes neighborhoods to escape local optima and explore different structures.

### Variable Neighborhood Descent (VND)

Uses multiple neighborhoods in a descent framework, often deterministically.

### GRASP

Greedy Randomized Adaptive Search Procedure. Repeatedly constructs randomized greedy solutions and applies local improvement.

### Multi-Start Local Search

Runs a local optimizer from multiple starting points to broaden coverage of the search space.

### Basin Hopping

Combines perturbations with local minimization and accepts/rejects transitions among basins.

## Evolutionary and population-based metaheuristics

### Genetic Algorithm (GA)

Population-based evolutionary metaheuristic using selection, crossover and mutation. Usually stochastic and derivative-free.

### Evolution Strategy (ES)

Evolutionary optimization family with strong emphasis on mutation, selection and adaptation of strategy parameters.

### Differential Evolution (DE)

Population-based stochastic evolutionary method, especially prominent in continuous derivative-free optimization.

### Genetic Programming (GP)

Evolutionary search over program structures or symbolic expressions rather than only fixed-length numeric vectors.

### Memetic Algorithm

Hybrid evolutionary method that combines population-based search with local improvement.

### Scatter Search

Population/reference-set metaheuristic that systematically combines strategically selected solutions.

### CMA-ES

Covariance Matrix Adaptation Evolution Strategy. A stochastic derivative-free method for continuous black-box optimization that adapts a multivariate search distribution.

## Swarm-intelligence methods

### Particle Swarm Optimization (PSO)

Population/swarm metaheuristic whose particles update positions using individual and shared search information. Usually stochastic.

### Ant Colony Optimization (ACO)

Multi-agent metaheuristic in which artificial ants construct solutions and communicate indirectly through pheromone information.

### Artificial Bee Colony (ABC)

Swarm-inspired population method using multiple search roles to explore and exploit candidate regions.

### Firefly Algorithm

Population-based stochastic metaheuristic using attraction relationships among candidate solutions.

## Other nature- or process-inspired metaheuristics

### Harmony Search

Population-based metaheuristic inspired by musical improvisation. It generates candidates from a harmony memory using memory consideration and randomization mechanisms.

### Gravitational Search

Population-based metaheuristic inspired by gravitational interaction among candidate agents.

### Electromagnetism-Like Optimization

Population-based search inspired by attraction and repulsion among charged particles.

The metaphor is secondary; these methods should still be analyzed by representation, randomness, operators, guarantee and evaluation cost.

## Multi-objective methods

### Weighted Sum

Scalarizes multiple objectives into one weighted objective. Simple but may fail to recover some nonconvex portions of a Pareto frontier.

### ε-Constraint Method

Optimizes one objective while converting other objectives into bounded constraints. A classical mathematical-programming approach to multi-objective optimization.

### Goal Programming

Models deviations from target or aspiration levels and minimizes selected deviation measures.

### NSGA-II

Stochastic population-based evolutionary metaheuristic using nondominated sorting and diversity preservation.

### NSGA-III

Multi-objective evolutionary algorithm designed especially for many-objective problems using reference directions/points.

### SPEA2

Strength Pareto Evolutionary Algorithm 2, a population-based multi-objective evolutionary method using dominance and density information.

### MOEA/D

Multi-Objective Evolutionary Algorithm based on Decomposition. Converts a multi-objective problem into interacting scalar subproblems.

### Multi-Objective PSO

PSO variants adapted to maintain and explore a set of nondominated trade-off solutions.

## Uncertainty, sequential and distributed optimization

### Two-Stage Stochastic Programming

Decisions are split into first-stage decisions made before uncertainty is revealed and recourse decisions made afterward.

### Multistage Stochastic Programming

Extends stochastic decision-making across multiple information-revelation stages.

### Sample Average Approximation (SAA)

Approximates stochastic expectations using a finite sampled scenario set and solves the resulting deterministic sample problem.

### Chance-Constrained Programming

Requires constraints to hold with a specified probability level under an uncertainty model.

### Robust Optimization

Optimizes against uncertainty sets or related ambiguity descriptions rather than relying only on one nominal parameter realization.

### Model Predictive Control (MPC)

Repeatedly solves a finite-horizon optimization problem as the system evolves, applies a near-term control action and then re-optimizes with updated state information.

### Approximate Dynamic Programming (ADP)

Uses approximations of value functions, policies or related dynamic-programming components to address large state spaces.

### Reinforcement Learning (RL)

A broad family of sequential decision-learning methods related to stochastic control and Dynamic Programming. It should not be reduced to a generic optimization label.

### ADMM

Alternating Direction Method of Multipliers. A decomposition framework widely used for structured convex optimization and distributed computation under appropriate assumptions.

### Dual Decomposition

Decomposes structured problems through dual variables associated with coupling constraints.

### Consensus Optimization

Distributed optimization in which agents coordinate toward agreement on shared variables or decisions.

### Distributed Gradient Descent

First-order optimization distributed across multiple agents or compute nodes with communication/consensus steps.

### Federated Optimization

Distributed learning/optimization across data-holding clients, often designed to limit direct sharing of raw local data.

## Surrogate and black-box optimization

### Bayesian Optimization

Surrogate-based global optimization framework for expensive objectives. It alternates between fitting a predictive model and selecting new evaluations with an acquisition function.

### Gaussian-Process Surrogates

Probabilistic surrogate models commonly used in Bayesian Optimization, especially for relatively low-dimensional expensive functions.

### Random-Forest Surrogates

Tree-ensemble surrogates useful for nonlinear and mixed-structure response modeling in some black-box settings.

### Neural-Network Surrogates

Flexible learned approximations suitable when sufficient evaluation data are available.

### Polynomial Response Surfaces

Classical low-order surrogate models used in response-surface methodology.

### Radial Basis Function Surrogates

Interpolation/approximation models frequently used in derivative-free and expensive black-box optimization.

## Hybrid and matheuristic methods

### Local Branching

Defines a mathematical neighborhood around an incumbent and searches it using mixed-integer programming machinery.

### Relaxation Induced Neighborhood Search (RINS)

Uses information from an incumbent and a relaxation solution to define a restricted neighborhood for exact or bounded optimization.

### Feasibility Pump

A heuristic for mixed-integer programming that alternates between relaxation information and integer-oriented projections/rounding to seek feasibility.

### Fix-and-Optimize

Fixes part of an incumbent solution while reoptimizing a selected variable block.

### Relax-and-Fix

Partitions integer variables into blocks and progressively enforces integrality/fixing decisions while temporarily relaxing later blocks.

### Large Neighborhood Search (LNS)

Destroys part of a solution and repairs/reoptimizes the resulting large neighborhood. The repair step may be heuristic or exact.

## Final reminder

No method in this index should be classified from one adjective alone. A complete description asks, at minimum:

```text
guarantee
+ randomness
+ search scope
+ representation
+ problem structure
+ information used
+ assumptions
```

That multi-axis description is the central principle of this repository.
