from intertemporal_or import solve_equipment_replacement


result = solve_equipment_replacement()

print("Period | Age | Action")
for step in result.path:
    print(f"{step.period:>6} | {step.age:>3} | {step.action}")

print(f"\nDiscounted lifecycle cost: {result.discounted_cost:.3f}")
