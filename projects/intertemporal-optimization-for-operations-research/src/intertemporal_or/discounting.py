"""Discounting utilities for finite-horizon intertemporal models."""

from __future__ import annotations

from collections.abc import Iterable

import numpy as np


def discount_factor(period: int | np.ndarray, rate: float) -> float | np.ndarray:
    """Return the present-value discount factor 1 / (1 + rate) ** period."""
    if rate <= -1:
        raise ValueError("rate must be greater than -1")
    if np.any(np.asarray(period) < 0):
        raise ValueError("period must be non-negative")
    return 1.0 / (1.0 + rate) ** np.asarray(period)


def present_value(cash_flows: Iterable[float], rate: float) -> float:
    """Compute the present value of period-indexed cash flows."""
    flows = np.asarray(list(cash_flows), dtype=float)
    factors = discount_factor(np.arange(len(flows)), rate)
    return float(np.dot(flows, factors))
