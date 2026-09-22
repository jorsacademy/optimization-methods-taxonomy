from intertemporal_or import solve_inventory_planning


result = solve_inventory_planning()

print("Period | Production | Ending inventory")
for t, (production, inventory) in enumerate(
    zip(result.production, result.ending_inventory, strict=True)
):
    print(f"{t:>6} | {production:>10.1f} | {inventory:>16.1f}")

print(f"\nDiscounted total cost: {result.discounted_cost:.3f}")
