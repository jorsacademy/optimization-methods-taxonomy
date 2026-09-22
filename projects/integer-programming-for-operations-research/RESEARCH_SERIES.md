# Exact Methods and Mathematical Programming Research Series

This file maps related repositories in the JORS Academy portfolio. It is an index only: every listed repository remains an independent project with its own scope, code, assumptions, and benchmarks.

## Core foundation

- `integer-programming-for-operations-research` — foundational IP/MILP concepts, LP relaxation, branch-and-bound, cutting planes, formulation quality, and validation.

## Decomposition and exact-solver methods

- `benders-decomposition-capacity-planning` — classical Benders decomposition for capacity-planning structure.
- `logic-based-benders-production-scheduling-python` — logic-based Benders for production scheduling; distinct from classical linear Benders because the subproblem logic is problem-specific.
- `column-generation-cutting-stock` — Dantzig-Wolfe/column-generation structure for cutting stock.
- `airline-crew-scheduling-column-generation` — column generation in a crew-scheduling application with a very different pricing problem from cutting stock.
- `lagrangian-relaxation-unit-commitment` — dualizes coupling constraints and solves decomposed unit subproblems.
- `capacitated-vrp-branch-and-cut-python` — exact branch-and-cut for CVRP, emphasizing valid inequalities inside tree search.
- `matrix-free-pdhg-large-scale-linear-programming-python` — first-order large-scale LP optimization rather than tree-based discrete optimization.
- `sddp-multistage-energy-storage` — multistage stochastic decomposition; also cross-listed in the stochastic/robust series.
- `mpi-sppy-multistage-stochastic-planning` — distributed multistage stochastic decomposition; also cross-listed in the stochastic/robust series.

## Classical application models that should remain standalone

- `hungarian-assignment-optimization-python` — specialized polynomial-time assignment structure.
- `bin-packing-optimization-python` — exact MILP plus FFD comparison.
- `bin-packing-milp-pulp-visualization` — compact exact MILP/visualization demonstration.
- `miter-aware-cutting-stock-milp` — cutting-stock formulation with application-specific geometry details.
- `parallel-machine-scheduling-milp-optimization` — scheduling MILP.
- `resource-constrained-project-scheduling-pulp` — project scheduling under resource constraints.
- `fire-station-location-covering-optimization` — covering-style location model.
- `fire-station-location-optimization-pulp` — assignment-style location model with response-time objective.
- `capacitated-facility-location-tabu-search-julia` — facility location solved with a metaheuristic rather than an exact MILP workflow.
- `supply-chain-network-design-pyomo` — multi-echelon facility/network design.

## Modern learning-augmented extension

The following repositories study learned decisions inside or around exact optimization and therefore remain separate from the classical methods above:

- `learning-to-branch-milp`
- `learning-to-branch-mip-gnn-scip-pytorch`
- `learning-to-cut-milp`
- `learning-to-presolve-mip`
- `learning-to-prune-bnb-node-selection`
- `neural-diving-mip-solution-prediction`
- `gnn-guided-generalized-assignment-variable-fixing-pytorch`
- `learning-augmented-mip-solver`
- `learning-to-price-column-generation-cvrptw`
- `reinforcement-learning-benders-decomposition`

These are not duplicates of the classical repositories. They ask a different research question: which solver-internal decisions can be learned without changing the mathematical feasible region or the optimization objective?

## Portfolio rule

Repositories in this series should be merged only when both the mathematical problem and the computational experiment are substantially the same. Sharing a method family such as MILP, Benders, column generation, or branch-and-cut is not by itself a reason to combine repositories.
