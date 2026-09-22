"""Multi-period production and inventory planning with carryover."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from scipy.optimize import linprog

from .discounting import discount_factor


@dataclass(frozen=True)
class InventoryPlanningResult:
    production: np.ndarray
    ending_inventory: np.ndarray
    discounted_cost: float


def solve_inventory_planning(
    demand=(40, 65, 35, 80, 50),
    production_cost=(8.0, 8.5, 7.0, 9.5, 10.0),
    production_capacity=(55, 55, 70, 55, 70),
    holding_cost=(0.6, 0.6, 0.6, 0.6, 0.6),
    initial_inventory: float = 10.0,
    terminal_inventory: float = 5.0,
    discount_rate: float = 0.05,
) -> InventoryPlanningResult:
    """Minimize discounted production and holding cost over a finite horizon."""
    demand = np.asarray(demand, dtype=float)
    production_cost = np.asarray(production_cost, dtype=float)
    production_capacity = np.asarray(production_capacity, dtype=float)
    holding_cost = np.asarray(holding_cost, dtype=float)

    n = len(demand)
    if not (
        len(production_cost)
        == len(production_capacity)
        == len(holding_cost)
        == n
    ):
        raise ValueError("all period-indexed inputs must have equal length")
    if np.any(demand < 0) or np.any(production_capacity < 0):
        raise ValueError("demand and production_capacity must be non-negative")
    if np.any(production_cost < 0) or np.any(holding_cost < 0):
        raise ValueError("cost inputs must be non-negative")
    if initial_inventory < 0 or terminal_inventory < 0:
        raise ValueError("inventory levels must be non-negative")

    factors = discount_factor(np.arange(n), discount_rate)
    objective = np.concatenate(
        [production_cost * factors, holding_cost * factors]
    )

    # Variable order: production[0:n], inventory[0:n].
    a_eq = np.zeros((n + 1, 2 * n))
    b_eq = np.zeros(n + 1)

    for t in range(n):
        a_eq[t, t] = 1.0
        a_eq[t, n + t] = -1.0
        if t == 0:
            b_eq[t] = demand[t] - initial_inventory
        else:
            a_eq[t, n + t - 1] = 1.0
            b_eq[t] = demand[t]

    a_eq[n, 2 * n - 1] = 1.0
    b_eq[n] = terminal_inventory

    bounds = (
        [(0.0, float(production_capacity[t])) for t in range(n)]
        + [(0.0, None)] * n
    )

    result = linprog(
        objective,
        A_eq=a_eq,
        b_eq=b_eq,
        bounds=bounds,
        method="highs",
    )
    if not result.success:
        raise RuntimeError(f"inventory planning model failed: {result.message}")

    return InventoryPlanningResult(
        production=np.asarray(result.x[:n], dtype=float),
        ending_inventory=np.asarray(result.x[n:], dtype=float),
        discounted_cost=float(result.fun),
    )
