# 8. Hybrid Methods and Matheuristics

[← Time, distribution and model access](07-time-distribution-and-model-access.md) · [Next: Comparison matrix →](09-comparison-matrix.md)

## 8.1 Why exact and heuristic methods are often combined

The exact/heuristic distinction is conceptually useful, but real optimization systems frequently combine both.

A large mixed-integer problem may contain:

- a tractable exact subproblem,
- a difficult combinatorial master problem,
- neighborhoods that can be searched exactly,
- relaxations that give informative bounds,
- domain-specific construction rules that produce strong incumbents quickly.

A hybrid can exploit each component where it is strongest.

## 8.2 Matheuristics

A **matheuristic** combines mathematical programming with heuristic or metaheuristic search.

Typical patterns include:

- use a MILP solver inside Large Neighborhood Search,
- solve exact subproblems inside a Genetic Algorithm,
- fix part of a solution and optimize the remaining variables exactly,
- use relaxation information to define neighborhoods,
- use heuristic incumbents to accelerate an exact solver.

Representative techniques include:

- Local Branching,
- Relaxation Induced Neighborhood Search (RINS),
- Feasibility Pump,
- fix-and-optimize,
- relax-and-fix,
- Large Neighborhood Search with exact repair/subproblem solving.

## 8.3 Local Branching

Local Branching adds a constraint that restricts the search to a neighborhood around an incumbent, then uses a MILP solver to search that neighborhood exactly or to a controlled tolerance.

The high-level idea is:

```text
incumbent solution
      ↓
define exact mathematical neighborhood
      ↓
solve neighborhood with MILP machinery
      ↓
update incumbent
      ↓
move / enlarge / redefine neighborhood
```

This is a clear example of exact machinery being embedded inside a heuristic search strategy.

## 8.4 Fix-and-optimize

A subset of variables is fixed to incumbent values while another subset is reoptimized.

The neighborhood is therefore induced by the chosen free-variable block.

This can be effective when:

- the full model is too difficult,
- small subproblems are much easier,
- the problem has a meaningful decomposition by time, location, product, vehicle or machine.

## 8.5 Relax-and-fix

Variables are divided into blocks. Some variables are enforced as integer, some are fixed from earlier decisions, and others are temporarily relaxed.

The method progressively constructs a feasible integer solution through a sequence of smaller problems.

It is commonly used as a constructive heuristic for large planning and scheduling models.

## 8.6 Exact subproblem optimization inside a metaheuristic

Suppose a routing metaheuristic chooses a subset of customers to remove and reinsert. Instead of reinserting them greedily, the algorithm may solve the reinsertion subproblem exactly.

This yields the pattern:

```text
metaheuristic chooses where to search
           +
exact solver optimizes inside that neighborhood
```

The overall method is still not automatically exact. Exactness of a subproblem does not imply global exactness of the complete hybrid.

## 8.7 Memetic and hybrid metaheuristics

Hybridization is not limited to mathematical programming.

Examples:

- Genetic Algorithm + local search,
- PSO + gradient refinement,
- ACO + 2-opt,
- GA + Tabu Search,
- evolutionary search + exact repair.

A hybrid should be classified by each component and by the guarantee of the **whole algorithm**, not by the strongest component alone.

## 8.8 A critical rule for classification

If a method contains an exact solver, ask:

> Does the entire outer algorithm preserve a proof of global optimality?

If the answer is no, the overall method should not be called exact merely because one internal subproblem is solved exactly.

Similarly, if an exact solver uses primal heuristics internally, the overall solver can still be exact if the exact search and certification machinery remain valid.

This distinction is essential in modern solver architectures, where exact and heuristic components coexist extensively.
