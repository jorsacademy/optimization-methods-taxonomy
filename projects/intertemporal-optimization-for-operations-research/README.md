# Intertemporal Optimization for Operations Research

Educational Python models for optimization problems in which **today's decisions change tomorrow's feasible set, costs, or state**.

Intertemporal optimization is broader than simply repeating a static model over several periods. The essential feature is **coupling across time**: capacity installed now remains available later, inventory carried today becomes tomorrow's initial stock, equipment ages, cash flows are discounted, and terminal conditions influence earlier decisions.

This repository develops those ideas through compact Operations Research examples using linear programming and dynamic programming.

## Topics

- multi-period optimization
- intertemporal trade-offs
- present value and discounting
- state transitions
- inventory carryover
- irreversible investment
- capacity expansion
- terminal conditions
- finite-horizon optimization
- Bellman recursion
- equipment replacement
- shadow value of future resources
- time coupling in LP models

## Core idea

A generic finite-horizon model can be written as

```text
minimize    sum_t beta^t C_t(x_t, s_t)

subject to  s_(t+1) = f_t(s_t, x_t)
            x_t in X_t(s_t)
```

where

- `t` is the time period,
- `s_t` is the state inherited from previous decisions,
- `x_t` is the current decision,
- `C_t` is the period cost,
- `beta = 1 / (1 + r)` is a discount factor,
- `f_t` links one period to the next.

Without the transition equation or another cross-period constraint, the model would decompose into independent static problems.

## Examples

### 1. Irreversible capacity expansion

A planner must install enough capacity to meet demand in every period. New capacity survives for all later periods, but there is a maximum amount that can be installed in any one period.

```text
K_t = K_(t-1) + y_t

K_t >= demand_t

0 <= y_t <= max_addition_t
```

The objective minimizes discounted investment expenditure:

```text
minimize  sum_t beta^t capex_t y_t
```

The sample optimum is

| Period | Capacity added | Installed capacity | Demand |
|---:|---:|---:|---:|
| 0 | 10 | 70 | 70 |
| 1 | 20 | 90 | 90 |
| 2 | 40 | 130 | 120 |
| 3 | 40 | 170 | 170 |
| 4 | 40 | 210 | 210 |

The model installs **more capacity than immediately required in period 2** because future demand cannot be served otherwise under the per-period expansion limit. This is a direct intertemporal effect.

Run:

```bash
python examples/run_capacity_expansion.py
```

### 2. Production and inventory carryover

Production in one period can satisfy demand in a later period by carrying inventory:

```text
I_t = I_(t-1) + q_t - d_t
```

The objective includes discounted production and holding costs:

```text
minimize  sum_t beta^t (
    production_cost_t * q_t
    + holding_cost_t * I_t
)
```

Sample optimum:

| Period | Production | Ending inventory |
|---:|---:|---:|
| 0 | 40 | 10 |
| 1 | 55 | 0 |
| 2 | 70 | 35 |
| 3 | 45 | 0 |
| 4 | 55 | 5 |

Period 2 has relatively low production cost, so the model produces ahead and carries inventory into a more expensive future period.

Run:

```bash
python examples/run_inventory_planning.py
```

### 3. Equipment replacement by dynamic programming

The state is machine age. Each period the planner chooses to either

- `keep` the machine and let it age, or
- `replace` it and reset its effective age.

The Bellman recursion is

```text
V_t(age) = min {
    keep_cost(age) + beta * V_(t+1)(age + 1),
    replacement_cost - salvage(age)
        + operating_cost(0)
        + beta * V_(t+1)(1)
}
```

Terminal salvage value is explicitly included, which prevents the final-period decision from being treated as if the planning horizon had no economic boundary.

For the default instance and initial machine age 2, the optimal path is

```text
replace -> keep -> replace -> keep -> replace -> keep
```

Run:

```bash
python examples/run_equipment_replacement.py
```

## Discounting utilities

The package also contains small helpers for present-value calculations:

```python
from intertemporal_or import discount_factor, present_value

beta_3 = discount_factor(3, rate=0.08)
pv = present_value([100, 100, 100], rate=0.08)
```

For a constant per-period discount rate `r`,

```text
beta_t = 1 / (1 + r)^t
```

Discounting changes the relative attractiveness of costs and benefits at different dates, but it does **not** by itself create intertemporal coupling. Coupling comes from state transitions, carryover, irreversible decisions, shared resources, or similar links across periods.

## Repository structure

```text
.
├── README.md
├── LICENSE
├── requirements.txt
├── pyproject.toml
├── docs/
│   └── INTERTEMPORAL_OPTIMIZATION.md
├── examples/
│   ├── run_capacity_expansion.py
│   ├── run_inventory_planning.py
│   └── run_equipment_replacement.py
├── src/
│   └── intertemporal_or/
│       ├── __init__.py
│       ├── discounting.py
│       ├── capacity_expansion.py
│       ├── inventory_planning.py
│       └── equipment_replacement.py
├── tests/
│   └── test_models.py
└── .github/
    └── workflows/
        └── tests.yml
```

## Installation

Create and activate a virtual environment.

```bash
python -m venv .venv
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

Install the project:

```bash
pip install -e .
```

For tests:

```bash
pip install pytest
```

or install the pinned teaching dependencies:

```bash
pip install -r requirements.txt
```

## Run the examples

```bash
python examples/run_capacity_expansion.py
python examples/run_inventory_planning.py
python examples/run_equipment_replacement.py
```

## Tests

```bash
pytest
```

The regression tests verify the discounting utilities and the optimal solutions of all three sample models.

## Modeling lessons

The examples emphasize several points that recur in Operations Research.

1. **Future constraints can change current decisions.**  
   Capacity expansion limits can force investment before the capacity is immediately needed.

2. **A state variable transfers consequences across time.**  
   Inventory, installed capacity, machine age, cash balance, backlog, and resource condition are common examples.

3. **Terminal conditions matter.**  
   A finite-horizon model without a sensible terminal condition can create artificial end effects.

4. **Discounting and physical carryover are different mechanisms.**  
   Discounting changes valuation across time; transition equations change feasibility across time.

5. **LP and dynamic programming describe the same broad idea from different angles.**  
   LP is natural when the entire trajectory can be optimized simultaneously. Dynamic programming is natural when decisions are organized recursively around state transitions.

## Extensions

Natural extensions include

- stochastic multi-stage optimization,
- scenario trees and non-anticipativity,
- rolling-horizon reoptimization,
- capacity retirement and depreciation,
- cash-flow constraints,
- backlog and service levels,
- energy storage,
- reservoir management,
- maintenance scheduling,
- replacement with multiple asset types,
- intertemporal emissions constraints,
- mixed-integer investment timing,
- approximate dynamic programming.

## Relationship to sequential decision making

Intertemporal optimization and sequential decision making overlap, but they are not identical.

A deterministic multi-period LP can be intertemporal even if all future information is known at time 0. Sequential decision models become especially important when information arrives over time and later actions adapt to observations.

This repository focuses on the **time-coupled optimization structure** itself. Stochastic control, MDPs, reinforcement learning, and learning under uncertainty are natural next steps.

## License

This repository is released under a custom **Non-Commercial Software License**. Personal, educational, academic, and other non-commercial use is permitted. Commercial use requires prior written permission.

This license is intentionally not an OSI-approved open-source license.
