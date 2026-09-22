from intertemporal_or import solve_capacity_expansion


result = solve_capacity_expansion()

print("Period | Add capacity | Installed capacity")
for t, (addition, capacity) in enumerate(
    zip(result.additions, result.installed_capacity, strict=True)
):
    print(f"{t:>6} | {addition:>12.1f} | {capacity:>18.1f}")

print(f"\nDiscounted investment cost: {result.discounted_cost:.3f}")
