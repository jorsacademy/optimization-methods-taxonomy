# 4. Search Representation and Metaheuristic Families

[← Randomness and search](03-randomness-and-search.md) · [Next: Problem structure →](05-problem-structure.md)

## 4.1 Single-solution methods

A single-solution method keeps one principal incumbent or current solution:

```math
x^{(t)} \rightarrow x^{(t+1)}.
```

Examples:

- Hill Climbing,
- Simulated Annealing,
- Tabu Search,
- Iterated Local Search,
- Variable Neighborhood Search,
- local improvement phases inside GRASP.

Advantages:

- lower memory requirements,
- often simpler state management,
- strong local refinement,
- easy integration with problem-specific neighborhoods.

Limitations:

- only one search region is represented explicitly at a time,
- diversity can be difficult to maintain,
- escape mechanisms are needed for difficult local optima.

## 4.2 Population-based methods

A population-based method maintains a set of candidate solutions:

```math
P^{(t)} = \{x_1^{(t)},x_2^{(t)},\ldots,x_n^{(t)}\}.
```

Examples:

- Genetic Algorithm,
- Differential Evolution,
- Particle Swarm Optimization,
- Evolution Strategies,
- Artificial Bee Colony,
- Scatter Search,
- many multi-objective evolutionary algorithms.

Ant Colony Optimization is also naturally multi-agent/population-oriented, although its persistent search state is often represented through pheromone information rather than only a population of retained solutions.

Advantages:

- multiple search regions can be represented simultaneously,
- diversity mechanisms are easier to express,
- naturally compatible with Pareto-based multi-objective search.

Limitations:

- more objective evaluations per iteration,
- larger memory/computational cost,
- population collapse or premature convergence remains possible.

## 4.3 Representation is not the same as stochasticity

Population-based methods are often stochastic, but that is not a definition. One could design deterministic selection, crossover, mutation or update rules.

Single-solution methods can also be stochastic: Simulated Annealing is the standard example.

Hence:

```text
single-solution ≠ deterministic
population-based ≠ stochastic
```

## 4.4 Evolutionary algorithms

Evolutionary algorithms imitate abstract mechanisms of evolution.

Typical operators:

- selection,
- recombination / crossover,
- mutation,
- elitism,
- replacement.

Representative methods:

- Genetic Algorithm,
- Evolution Strategies,
- Differential Evolution,
- Genetic Programming.

They are usually:

- population-based,
- stochastic,
- derivative-free,
- global-search-oriented.

But those are typical properties, not universal definitions.

## 4.5 Swarm intelligence

Swarm algorithms model collective behavior among multiple agents.

Examples:

- Particle Swarm Optimization,
- Ant Colony Optimization,
- Artificial Bee Colony,
- Firefly Algorithm.

Different swarm algorithms communicate information differently:

- PSO shares information through personal/global best states,
- ACO shares indirect information through pheromone trails,
- bee-inspired methods often divide search roles among agent types.

The biological metaphor is less important than the underlying search mechanism.

## 4.6 Physics-inspired methods

Examples include:

- Simulated Annealing,
- Gravitational Search,
- Electromagnetism-like Optimization.

The important analytical question is not what natural process inspired the name, but:

- how new candidates are generated,
- how acceptance works,
- how parameters change over time,
- what convergence statements, if any, can be made.

## 4.7 Memory-based methods

Tabu Search is the canonical example.

It uses memory structures such as a tabu list to restrict recently used moves or attributes. Typical components include:

- short-term memory,
- aspiration criteria,
- intensification,
- diversification.

This distinguishes it from memoryless local improvement.

## 4.8 Neighborhood-changing methods

Variable Neighborhood Search (VNS) systematically changes neighborhood structures.

Variable Neighborhood Descent (VND) typically applies several local-search neighborhoods in a deterministic descent framework.

The central principle is:

> a solution that is locally optimal under one neighborhood may not be locally optimal under another.

## 4.9 Multi-start and perturbation methods

Examples:

- Multi-start Local Search,
- GRASP,
- Iterated Local Search.

A common pattern is:

```text
construct / initialize
        ↓
local improvement
        ↓
restart or perturb
        ↓
local improvement
        ↓
repeat
```

They transform a local optimizer into a broader search strategy.

## 4.10 Memetic algorithms

A Memetic Algorithm usually combines an evolutionary population mechanism with strong local improvement:

```math
\text{Evolutionary search} + \text{Local search}.
```

The evolutionary component provides diversification; the local search intensifies around promising individuals.

## 4.11 Why “nature-inspired” is not a useful primary taxonomy

Algorithms are sometimes grouped by metaphor: evolutionary, swarm, physics, biology, chemistry and so on. This can be useful historically, but it is usually weaker than classifying them by computational mechanism.

For serious analysis, prioritize:

- guarantee,
- representation,
- neighborhood/operator design,
- use of memory,
- randomness,
- exploration/exploitation strategy,
- parameter adaptation,
- evaluation cost,
- stopping rule.

Those properties determine behavior more directly than the metaphor in the algorithm's name.
