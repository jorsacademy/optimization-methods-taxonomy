import numpy as np
import pytest

from intertemporal_or import (
    discount_factor,
    present_value,
    solve_capacity_expansion,
    solve_equipment_replacement,
    solve_inventory_planning,
)


def test_discounting():
    assert discount_factor(0, 0.10) == pytest.approx(1.0)
    assert discount_factor(2, 0.10) == pytest.approx(1 / 1.1**2)
    assert present_value([100, 100], 0.10) == pytest.approx(190.9090909)


def test_capacity_expansion_sample():
    result = solve_capacity_expansion()
    np.testing.assert_allclose(result.additions, [10, 20, 40, 40, 40])
    np.testing.assert_allclose(result.installed_capacity, [70, 90, 130, 170, 210])
    assert result.discounted_cost == pytest.approx(1024.3844378)


def test_inventory_planning_sample():
    result = solve_inventory_planning()
    np.testing.assert_allclose(result.production, [40, 55, 70, 45, 55])
    np.testing.assert_allclose(result.ending_inventory, [10, 0, 35, 0, 5])
    assert result.discounted_cost == pytest.approx(2058.9752007)


def test_equipment_replacement_sample():
    result = solve_equipment_replacement()
    assert [step.action for step in result.path] == [
        "replace",
        "keep",
        "replace",
        "keep",
        "replace",
        "keep",
    ]
    assert result.discounted_cost == pytest.approx(46.40435936)
