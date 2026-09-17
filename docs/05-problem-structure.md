# 5. Problem Domains and Mathematical Structure

[← Representation and metaheuristics](04-search-representation-and-metaheuristics.md) · [Next: Constraints, objectives and uncertainty →](06-constraints-objectives-uncertainty.md)

## 5.1 Continuous optimization

Continuous decision variables satisfy

```math
x_i \in \mathbb{R}.
```

A generic problem is

```math
\min_{x\in\mathbb{R}^n} f(x).
```

Common methods include:

- Gradient Descent,
- Newton methods,
- BFGS and L-BFGS,
- Conjugate Gradient,
- interior-point methods,
- SQP,
- Differential Evolution,
- CMA-ES.

Applications include:

- parameter estimation,
- engineering design,
- portfolio optimization,
- optimal control,
- machine-learning training.

## 5.2 Discrete and integer optimization

Discrete variables take values from a finite or countable set. Common forms are

```math
x_i \in \{0,1\}
```

or

```math
x_i \in \mathbb{Z}.
```

Applications:

- scheduling,
- routing,
- assignment,
- facility location,
- packing,
- network design.

Typical approaches:

- Branch and Bound,
- Branch and Cut,
- Dynamic Programming,
- Cutting Planes,
- local search,
- Tabu Search,
- Genetic Algorithms,
- Ant Colony Optimization.

## 5.3 Mixed-variable optimization

Mixed models contain variables from different domains, for example

```math
x\in\mathbb{R}^n, \qquad y\in\mathbb{Z}^m.
```

Important classes include:

- MILP — Mixed-Integer Linear Programming,
- MINLP — Mixed-Integer Nonlinear Programming,
- MIQP — Mixed-Integer Quadratic Programming,
- mixed-integer convex optimization.

Mixed-variable structure often motivates decomposition, relaxations and hybrid exact–heuristic methods.

## 5.4 Combinatorial optimization

A combinatorial solution is often a:

- permutation,
- subset,
- matching,
- graph structure,
- route,
- schedule,
- assignment.

Examples:

- Traveling Salesperson Problem,
- Vehicle Routing Problem,
- Job Shop Scheduling,
- Graph Coloring,
- Set Cover,
- Maximum Clique,
- Assignment Problem.

The search space can grow as

```math
|X|=n!
```

for permutations or

```math
|X|=2^n
```

for subsets.

This explosive growth is why exact enumeration quickly becomes infeasible and why bounding, decomposition, approximation and heuristic search matter.

## 5.5 Linear optimization

A linear program has a linear objective and linear constraints:

```math
\begin{aligned}
\min \quad & c^T x \\
\text{s.t.}\quad & Ax\le b.
\end{aligned}
```

The feasible region is convex. Any local optimum is therefore global.

Linear structure supports mature algorithms, duality theory and strong optimality certificates.

## 5.6 Nonlinear optimization

A nonlinear program has a nonlinear objective or at least one nonlinear constraint:

```math
\min f(x)
```

subject to

```math
g_i(x)\le 0.
```

Subclasses include:

- convex nonlinear optimization,
- nonconvex optimization,
- quadratic optimization,
- polynomial optimization,
- fractional programming,
- nonsmooth optimization,
- black-box optimization.

The nonlinear label alone says little about computational difficulty; convexity and exploitable structure are often more decisive.

## 5.7 Convex optimization

A function `f` is convex when

```math
f(\lambda x+(1-\lambda)y)
\le
\lambda f(x)+(1-\lambda)f(y),
\qquad 0\le\lambda\le1.
```

If the feasible set is also convex, every local minimum is a global minimum.

Common method families:

- gradient methods,
- interior-point methods,
- proximal methods,
- subgradient methods,
- ADMM for structured problems.

Convexity is one of the most valuable structural properties in optimization because local reasoning can yield global guarantees.

## 5.8 Nonconvex optimization

Nonconvex problems may contain:

- multiple local minima,
- saddle points,
- disconnected feasible regions,
- flat regions,
- difficult nonlinear constraints.

An illustrative nonconvex objective is

```math
f(x)=x^4-3x^2+x.
```

Possible strategies include:

- multi-start,
- Basin Hopping,
- Simulated Annealing,
- evolutionary algorithms,
- deterministic global optimization,
- spatial Branch and Bound.

The important distinction is whether a method merely explores broadly or can actually certify global optimality.

## 5.9 Quadratic optimization

A quadratic objective has the form

```math
\min \frac12 x^TQx+c^Tx.
```

If `Q \succeq 0`, the objective is convex.

Important classes:

- QP,
- QCQP,
- MIQP,
- MIQCP.

Quadratic structure appears in portfolio models, control, machine learning and many engineering problems.

## 5.10 Differentiable optimization

When gradients or Hessians are available,

```math
\nabla f(x), \qquad \nabla^2 f(x),
```

they can guide efficient local search.

Examples:

- Gradient Descent,
- Newton,
- BFGS,
- SQP.

## 5.11 Derivative-free optimization

Derivative-free methods are useful when derivatives are:

- unavailable,
- unreliable,
- discontinuous,
- too expensive,
- hidden behind a simulator.

Examples:

- Nelder–Mead,
- Pattern Search,
- Powell-type methods,
- Bayesian Optimization,
- evolutionary methods,
- CMA-ES.

## 5.12 Zeroth-, first- and second-order information

A clean information-based classification is:

### Zeroth-order

Uses function values such as

```math
f(x).
```

### First-order

Uses gradients. A steepest-descent direction is

```math
d_k=-\nabla f(x_k),
```

with update

```math
x_{k+1}=x_k+\alpha_k d_k.
```

### Second-order

Uses curvature information such as the Hessian:

```math
x_{k+1}
=
x_k-[\nabla^2 f(x_k)]^{-1}\nabla f(x_k).
```

Newton and trust-region Newton methods are canonical examples.

## 5.13 Black-box optimization

In black-box optimization, the internal analytical form may be unavailable. The optimizer can only evaluate

```math
x \mapsto f(x).
```

Possible applications:

- simulation optimization,
- hyperparameter tuning,
- expensive engineering software,
- physical experiments.

Black-box does not necessarily mean stochastic. The black-box function may be deterministic or noisy.
