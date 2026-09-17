# 7. Time, Computational Distribution and Model Access

[← Constraints, objectives and uncertainty](06-constraints-objectives-uncertainty.md) · [Next: Hybrid methods →](08-hybrid-methods.md)

## 7.1 Static optimization

In a static optimization problem, the data are treated as fixed during the solve. The model is solved as one decision problem.

Examples include many planning, design and allocation models built from a snapshot of data.

## 7.2 Dynamic optimization

Dynamic optimization includes an evolving state such as

```math
x_{t+1}=F(x_t,u_t)
```

and an objective over time:

```math
\min \sum_{t=0}^{T} c(x_t,u_t).
```

Relevant approaches include:

- Dynamic Programming,
- optimal control,
- Model Predictive Control,
- Approximate Dynamic Programming,
- Reinforcement Learning.

Dynamic optimization is about temporal coupling in decisions and state, not simply “an algorithm that runs iteratively.”

## 7.3 Online optimization

In online optimization, decisions are made before all future information is known. New information arrives sequentially.

Examples:

- online scheduling,
- real-time pricing,
- traffic routing,
- ad allocation,
- server resource allocation.

Performance may be evaluated using concepts such as regret, competitive ratio, service level, or realized operational cost depending on the field.

## 7.4 Real-time optimization

Real-time optimization imposes a strict computational deadline. A solution that arrives too late can be operationally useless even if it is mathematically superior.

Applications include:

- autonomous control,
- power-grid control,
- industrial process control,
- emergency routing.

This creates a direct trade-off between:

- solution quality,
- robustness,
- computational budget,
- response time.

## 7.5 Centralized optimization

A centralized architecture sends the full decision problem to a central optimizer.

Advantages:

- access to global information,
- easier coordination,
- potentially stronger system-wide optimization.

Limitations:

- communication burden,
- scalability constraints,
- single point of failure,
- privacy or data-governance concerns.

## 7.6 Distributed optimization

A distributed problem may decompose as

```math
\min \sum_{i=1}^{N} f_i(x_i)
```

possibly with coupling or consensus constraints.

Methods include:

- ADMM,
- dual decomposition,
- consensus optimization,
- distributed gradient methods,
- federated optimization variants.

“Distributed” describes computational organization, not whether the method is exact, heuristic, deterministic or stochastic.

## 7.7 Model-based methods

A model-based optimizer has access to an explicit mathematical or dynamical description.

For example,

```math
x_{t+1}=Ax_t+Bu_t.
```

It can exploit known equations, constraints, derivatives or structure.

## 7.8 Model-free methods

A model-free approach does not rely on a known explicit model of system dynamics.

Examples may include:

- model-free Reinforcement Learning,
- black-box search,
- evolutionary optimization,
- bandit optimization.

The phrase “model-free” is context-dependent. An evolutionary algorithm may still use explicit constraints and objective evaluations even though it does not require derivatives or system equations.

## 7.9 Surrogate-based methods

When the true objective is expensive, a surrogate model approximates it:

```math
\hat f(x) \approx f(x).
```

Possible surrogate models:

- Gaussian Processes,
- Random Forests,
- Neural Networks,
- polynomial response surfaces,
- radial basis functions.

Bayesian Optimization is a prominent surrogate-based framework. It alternates between:

1. fitting/updating a surrogate,
2. using an acquisition function to choose informative candidate points,
3. evaluating the expensive objective,
4. updating the model.

Surrogate-based does not automatically imply stochastic; the surrogate, acquisition function and optimizer may each be deterministic or stochastic.
