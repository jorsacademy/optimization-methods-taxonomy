# 14. Benchmarking and Experimental Methodology

[← Computational complexity](13-computational-complexity.md) · [Next: Explainable optimization →](15-explainable-optimization.md)

Optimization experiments are easy to bias unintentionally. A credible comparison requires the problem instances, budgets, stopping rules, randomness, solver settings, and evaluation metrics to be controlled explicitly.

## 14.1 Define the experimental question first

A benchmark should answer a precise question, for example:

- Which method reaches the lowest objective value under the same evaluation budget?
- Which exact solver configuration minimizes time to a certified optimum?
- Which heuristic produces the best feasible solution within 60 seconds?
- Which algorithm scales better as instance size grows?
- Which method is more robust across heterogeneous instance families?

Different questions require different metrics. A single runtime or objective value rarely answers all of them.

## 14.2 Match the budget to the algorithm class

Fairness requires comparable resource constraints.

Possible budgets include:

- wall-clock time,
- CPU time,
- number of objective evaluations,
- number of simulation replications,
- number of gradient evaluations,
- solver node limit,
- memory limit,
- communication rounds in distributed optimization.

For black-box optimization, objective evaluations are often the scarce resource. For mathematical programming, time plus optimality gap may be more informative.

Do not compare one method after convergence with another stopped after an arbitrary fixed number of iterations unless iteration cost is genuinely comparable.

## 14.3 Separate tuning from final evaluation

Hyperparameter selection on the test instances leaks information.

Use a structure such as:

```text
training / calibration instances
        ↓
validation / tuning instances
        ↓
freeze method and hyperparameters
        ↓
test instances
```

For synthetic benchmark generators, use disjoint random-seed ranges or independently generated instance sets.

## 14.4 Control randomness

Stochastic algorithms require repeated runs.

Record at least:

- algorithm seed,
- instance seed,
- simulation seed when relevant,
- number of independent repetitions,
- initialization policy.

Common random numbers can reduce variance in simulation-based comparisons when candidate methods can legitimately be evaluated under matched random streams. They should be documented because they change the dependence structure of the observations.

## 14.5 Report more than the mean

For repeated experiments, useful summaries include:

- mean,
- median,
- standard deviation,
- interquartile range,
- selected quantiles,
- confidence intervals,
- number of failures or infeasible outputs.

Optimization results are often skewed or heavy-tailed. Median and quantiles can reveal behavior hidden by a mean.

## 14.6 Objective quality metrics

For minimization with a known reference optimum, an absolute gap is

```text
gap_abs = value - optimum
```

and a relative gap can be reported with an explicitly defined denominator.

For exact solvers, use the solver's primal and dual bounds consistently and state whether the gap is absolute or relative.

For stochastic objectives, distinguish:

- objective estimate used during search,
- independent validation estimate,
- uncertainty of the validation estimate.

## 14.7 Feasibility is a first-class metric

A low objective value is meaningless when constraints are violated.

Report, where applicable:

- feasible-run rate,
- maximum violation,
- total violation,
- integrality violation,
- repair frequency,
- post-repair objective.

For multi-objective methods, verify feasibility before computing Pareto quality indicators.

## 14.8 Convergence curves

A convergence plot should use a meaningful x-axis:

- time,
- evaluations,
- iterations only when iteration cost is comparable,
- solver nodes,
- communication rounds.

For stochastic methods, plot an aggregate trajectory over repeated runs and communicate dispersion rather than presenting one favorable seed.

## 14.9 Performance profiles

When comparing solvers over many heterogeneous instances, performance profiles summarize how often each method is within a factor of the best observed performance on each instance.

They are useful because raw runtime averages can be dominated by a few difficult cases. The benchmark should still document timeout handling and the treatment of unsolved instances.

## 14.10 Statistical comparison

Statistical tests should follow the experimental design.

For paired results on the same instances, paired analyses are usually more informative than treating observations as independent. Across multiple algorithms and benchmark instances, rank-based procedures such as Friedman-style comparisons may be useful, followed by an appropriate multiple-comparison procedure when needed.

The test name is less important than the following principles:

- preserve pairing,
- avoid pseudo-replication,
- report effect sizes or practical differences,
- disclose the number of instances and repetitions,
- do not convert a p-value into a statement about practical importance.

## 14.11 Timeouts and failures

A benchmark must define what happens when a method:

- times out,
- runs out of memory,
- fails numerically,
- returns infeasible output,
- cannot produce a certificate.

Do not silently drop failures. Penalized runtime measures such as PAR-style scores can be useful when solver reliability is part of the question, but the penalty convention must be stated.

## 14.12 Reproducibility checklist

A high-quality optimization repository should make the following discoverable:

```text
instance generator / data source
software versions
hardware description
random seeds
solver parameters
stopping criteria
resource budgets
metric definitions
validation procedure
raw or machine-readable results
scripts that regenerate tables/figures
```

## 14.13 Recommended benchmark table

A compact benchmark report can use columns such as:

| Field | Meaning |
|---|---|
| Instance | Problem identifier |
| Method | Algorithm or solver |
| Feasible | Whether constraints are satisfied |
| Objective | Best validated objective |
| Gap | Gap to reference bound/optimum if available |
| Runtime | Measured resource time |
| Evaluations | Expensive objective calls if relevant |
| Seed | Repetition identifier |
| Status | Optimal, feasible, timeout, failed, etc. |

The central rule is simple: comparisons should preserve the decision problem while changing only the method or configuration being studied.
