"""Finite-horizon equipment replacement via backward dynamic programming."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class ReplacementStep:
    period: int
    age: int
    action: str


@dataclass(frozen=True)
class EquipmentReplacementResult:
    value_function: np.ndarray
    policy: np.ndarray
    path: tuple[ReplacementStep, ...]
    discounted_cost: float


def solve_equipment_replacement(
    horizon: int = 6,
    initial_age: int = 2,
    replacement_cost: float = 14.0,
    operating_cost=(3.0, 5.0, 8.0, 12.0, 17.0),
    salvage_value=(8.0, 5.0, 3.0, 1.0, 0.0),
    discount_rate: float = 0.08,
) -> EquipmentReplacementResult:
    """Solve a deterministic replacement problem with Bellman recursion.

    State: machine age at the start of a period.
    Actions: keep or replace.
    Terminal salvage value is credited at the end of the horizon.
    """
    if horizon <= 0:
        raise ValueError("horizon must be positive")
    if discount_rate <= -1:
        raise ValueError("discount_rate must be greater than -1")

    operating_cost = np.asarray(operating_cost, dtype=float)
    salvage_value = np.asarray(salvage_value, dtype=float)
    if len(operating_cost) != len(salvage_value):
        raise ValueError("operating_cost and salvage_value must have equal length")
    if np.any(operating_cost < 0) or np.any(salvage_value < 0):
        raise ValueError("costs and salvage values must be non-negative")

    max_age = len(operating_cost) - 1
    if initial_age < 0 or initial_age > max_age:
        raise ValueError("initial_age is outside the modeled age range")

    beta = 1.0 / (1.0 + discount_rate)
    value = np.zeros((horizon + 1, max_age + 1))
    policy = np.empty((horizon, max_age + 1), dtype=object)

    # End-of-horizon salvage is a negative cost.
    value[horizon, :] = -salvage_value

    for t in range(horizon - 1, -1, -1):
        for age in range(max_age + 1):
            keep_cost = np.inf
            if age < max_age:
                keep_cost = operating_cost[age] + beta * value[t + 1, age + 1]

            replace_cost = (
                replacement_cost
                - salvage_value[age]
                + operating_cost[0]
                + beta * value[t + 1, 1]
            )

            if keep_cost <= replace_cost:
                value[t, age] = keep_cost
                policy[t, age] = "keep"
            else:
                value[t, age] = replace_cost
                policy[t, age] = "replace"

    path = []
    age = initial_age
    for t in range(horizon):
        action = str(policy[t, age])
        path.append(ReplacementStep(period=t, age=age, action=action))
        age = 1 if action == "replace" else age + 1

    return EquipmentReplacementResult(
        value_function=value,
        policy=policy,
        path=tuple(path),
        discounted_cost=float(value[0, initial_age]),
    )
