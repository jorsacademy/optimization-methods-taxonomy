"""Small educational models for intertemporal optimization in Operations Research."""

from .capacity_expansion import CapacityExpansionResult, solve_capacity_expansion
from .discounting import discount_factor, present_value
from .equipment_replacement import EquipmentReplacementResult, solve_equipment_replacement
from .inventory_planning import InventoryPlanningResult, solve_inventory_planning

__all__ = [
    "CapacityExpansionResult",
    "EquipmentReplacementResult",
    "InventoryPlanningResult",
    "discount_factor",
    "present_value",
    "solve_capacity_expansion",
    "solve_equipment_replacement",
    "solve_inventory_planning",
]
