# 13. Computational Complexity for Optimization

[← Algorithm and method index](12-algorithm-index.md) · [Next: Benchmarking and experimental methodology →](14-benchmarking-experimental-methodology.md)

Optimization methods should not be compared only by whether they are called exact, heuristic, deterministic, or stochastic. A second layer is computational complexity: how the required work grows with instance size and which guarantees remain realistic as the problem scales.

## 13.1 Problem complexity is not algorithm runtime

A problem class and a particular implementation are different objects.

- A complexity class describes a family of decision or optimization problems under a formal computational model.
- An algorithm has a time and memory complexity under stated assumptions.
- A solver implementation adds engineering choices, preprocessing, numerical tolerances, parallelism, and hardware effects.
- Empirical runtime is an observed quantity for a particular benchmark distribution and machine.

Therefore, an observed fast run does not change the worst-case complexity class of the underlying problem.

## 13.2 P, NP, NP-hard, and NP-complete

For decision problems:

- **P** contains problems solvable in polynomial time by a deterministic algorithm.
- **NP** contains problems whose proposed yes-certificates can be verified in polynomial time.
- **NP-complete** problems are both in NP and NP-hard.
- **NP-hard** problems are at least as hard as NP-complete problems under an appropriate reduction; an NP-hard optimization problem does not need to be a decision problem.

For optimization practice, the main lesson is not to use these labels as synonyms for “easy” and “hard.” Instance structure matters. A theoretically difficult family may contain many easy practical instances, while a polynomial-time method can still be too expensive at industrial scale.

## 13.3 Weak and strong polynomiality

Polynomial runtime can depend on different notions of input size. Numerical optimization also has to account for coefficient encoding length, conditioning, and arithmetic precision.

A method described as polynomial should therefore be interpreted with its assumptions. In numerical optimization, iteration complexity and arithmetic complexity are often more informative than one informal statement that an algorithm is “efficient.”

## 13.4 Pseudo-polynomial algorithms

Some algorithms are polynomial in the numeric value of a parameter rather than in the number of bits required to encode that value.

Classical dynamic programming for integer knapsack is the standard example: a formulation indexed by capacity may be practical for moderate capacities but does not imply polynomial complexity in the binary encoding length of the input.

This distinction is important when comparing dynamic programming with MILP, approximation schemes, or heuristics.

## 13.5 Parameterized complexity

A difficult problem can become tractable when one structural parameter is small. Instead of asking only how runtime grows with total input size n, parameterized analysis studies expressions such as

```text
f(k) * poly(n)
```

where k may be treewidth, number of machines, number of complicating constraints, solution size, or another structural quantity.

This viewpoint is useful in Operations Research because industrial instances often have exploitable structure even when the general problem class is NP-hard.

## 13.6 Approximation algorithms

An approximation algorithm is not merely any non-exact method. It has a formal solution-quality guarantee.

For a minimization problem, a multiplicative approximation guarantee may take the form

```text
cost(solution) <= alpha * OPT
```

for alpha >= 1 under stated assumptions.

This differs from:

- a heuristic, which may have no general bound;
- a metaheuristic, which is a reusable search framework rather than a guarantee class;
- a solver stopped early, which may have an instance-specific bound but is not automatically an approximation algorithm.

## 13.7 PTAS and FPTAS

A **PTAS** produces a solution within a requested approximation level for every fixed epsilon, with polynomial dependence on input size for that fixed epsilon.

An **FPTAS** is polynomial in both input size and 1/epsilon.

The distinction matters because two algorithms may offer superficially similar accuracy controls while having very different scaling behavior as the requested tolerance becomes tighter.

## 13.8 Exact optimization and exponential worst cases

Exact optimization does not imply practical impossibility.

Branch-and-Bound, Branch-and-Cut, dynamic programming, and decomposition methods can exploit bounds, relaxations, sparsity, dominance, symmetry, decomposition structure, and good incumbents. Their practical performance is determined by the instance distribution and implementation as well as worst-case theory.

A careful description therefore separates:

```text
worst-case complexity
+ structural assumptions
+ theoretical guarantee
+ practical benchmark behavior
```

## 13.9 Continuous optimization complexity

For continuous optimization, complexity statements usually depend on assumptions such as convexity, smoothness, Lipschitz constants, strong convexity, access to first- or second-order information, and target accuracy.

Examples of useful questions are:

- How many gradient evaluations are required to reach an epsilon-stationary point?
- How does convergence change under strong convexity?
- What is the per-iteration cost of solving a Newton system?
- How does conditioning affect observed convergence?
- Does the method guarantee a global optimum or only stationarity?

Iteration count alone is not enough when per-iteration work differs substantially.

## 13.10 Complexity as one axis of method selection

Complexity theory should inform method selection without replacing empirical validation.

For a real optimization project, ask:

1. What is known about the problem class?
2. Which structural assumptions apply to this instance family?
3. Which guarantees are required?
4. Which dimensions or parameters drive computational growth?
5. What evaluation or runtime budget is available?
6. What does a controlled benchmark show on representative instances?

The correct conclusion is usually multi-dimensional. “Polynomial,” “exact,” “heuristic,” and “fast in our benchmark” answer different questions.
