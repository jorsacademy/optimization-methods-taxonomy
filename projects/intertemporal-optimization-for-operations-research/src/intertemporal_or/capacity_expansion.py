"""Finite-horizon capacity expansion with irreversible investment."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from scipy.optimize import linprog

from .discounting import discount_factor


@dataclass(frozen=True)
class CapacityExpansionResult:
    additions: np.ndarray
    installed_capacity: np.ndarray
    discounted_cost: float


def solve_capacity_expansion(
    demand=(70, 90, 120, 170, 210),
    initial_capacity: float = 60.0,
    max_additions=(40, 40, 40, 40, 40),
    capex=(9.0, 8.8, 8.4, 8.0, 7.8),
    discount_rate: float = 0.08,
) -> CapacityExpansionResult:
    """Minimize discounted capacity investment while meeting demand each period.

    Capacity installed in period t remains available in all later periods.
    """
    demand = np.asarray(demand, dtype=float)
    max_additions = np.asarray(max_additions, dtype=float)
    capex = np.asarray(capex, dtype=float)

    if not (len(demand) == len(max_additions) == len(capex)):
        raise ValueError("demand, max_additions, and capex must have equal length")
    if np.any(demand < 0) or np.any(max_additions < 0) or np.any(capex < 0):
        raise ValueError("inputs must be non-negative")
    if initial_capacity < 0:
        raise ValueError("initial_capacity must be non-negative")

    periods = np.arange(len(demand))
    objective = capex * discount_factor(periods, discount_rate)

    # initial_capacity + sum_{k<=t} addition_k >= demand_t
    cumulative_matrix = np.tril(np.ones((len(demand), len(demand))))
    a_ub = -cumulative_matrix
    b_ub = -(demand - initial_capacity)

    result = linprog(
        objective,
        A_ub=a_ub,
        b_ub=b_ub,
        bounds=[(0.0, float(limit)) for limit in max_additions],
        method="highs",
    )
    if not result.success:
        raise RuntimeError(f"capacity expansion model failed: {result.message}")

    additions = np.asarray(result.x, dtype=float)
    installed_capacity = initial_capacity + np.cumsum(additions)

    return CapacityExpansionResult(
        additions=additions,
        installed_capacity=installed_capacity,
        discounted_cost=float(result.fun),
    )
