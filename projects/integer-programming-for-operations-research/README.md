# Integer Programming for Operations Research

A rigorous, executable introduction to Integer Programming (IP) and its main subtypes for Operations Research.

The repository focuses on mathematical formulation, model interpretation, exact solution methods, modeling patterns, computational behavior, and solution validation. The examples are written in Python and use SciPy's optimization interfaces so that the mathematical structure remains explicit.

## Topics covered

- Linear Programming versus Integer Programming
- Pure Integer Programming
- Binary Integer Programming
- Mixed-Integer Linear Programming (MILP)
- LP relaxation and integrality gaps
- Branch-and-Bound
- Cutting planes and valid inequalities
- Branch-and-Cut concepts
- Big-M and logical linking constraints
- Knapsack models
- Fixed-charge models
- Facility location
- Assignment and parallel-machine scheduling
- Network design
- Multi-objective integer optimization
- Exact methods versus heuristics
- Computational complexity and formulation quality
- Solution validation and common modeling mistakes

## Main notebook

`integer_programming_for_operations_research.ipynb`

The notebook is designed to be read sequentially. Every code example has been executed and checked before publication.

## Requirements

- Python 3.10+
- NumPy
- pandas
- SciPy
- Jupyter

Install the dependencies with:

```bash
pip install -r requirements.txt
```

Then start Jupyter and open the notebook:

```bash
jupyter lab
```

## Solver approach

The notebook uses:

- `scipy.optimize.linprog` for LP relaxations;
- `scipy.optimize.milp` for integer and mixed-integer models;
- a small educational Branch-and-Bound implementation to expose the core algorithmic logic.

The custom Branch-and-Bound implementation is intentionally pedagogical and is not intended to replace production-grade MILP solvers.

## Model classes used in the notebook

### Pure IP

All decision variables are integer-valued.

### Binary IP

All decision variables are restricted to 0 or 1.

### MILP

Integer or binary variables coexist with continuous variables.

The notebook explicitly distinguishes these classes at both the mathematical and implementation levels.

## Validation philosophy

A solver result should not be accepted blindly. The examples demonstrate practices such as:

- checking solver success/status;
- independently recomputing objective values;
- checking constraint feasibility;
- verifying integrality within numerical tolerance;
- validating application-specific invariants.

## Educational scope

All coefficients and datasets are synthetic. The repository is intended for education, academic study, and non-commercial research. It does not provide operational, financial, engineering, or commercial recommendations.

## License

This repository is distributed under the Non-Commercial Source License included in `LICENSE.md`.

Commercial use is prohibited without prior written permission from the copyright holder. This is a source-available license and is not an OSI-approved open-source license.
