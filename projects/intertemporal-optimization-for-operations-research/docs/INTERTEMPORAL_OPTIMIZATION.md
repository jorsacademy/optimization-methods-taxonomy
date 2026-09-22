# Intertemporal Optimization Notes

## 1. What makes an optimization problem intertemporal?

An optimization problem is intertemporal when decisions or states in one period affect the costs, benefits, constraints, or feasible decisions in another period.

Typical coupling mechanisms include:

- inventory carried from one period to the next,
- installed capacity that remains available,
- equipment aging and deterioration,
- cash balances and borrowing,
- backlog accumulation,
- storage of energy or water,
- cumulative emissions,
- learning or information accumulation,
- investment lead times,
- irreversible decisions.

A collection of independent period-by-period models is multi-period in notation but not meaningfully intertemporal unless some cross-period relationship is present.

## 2. State-transition representation

A useful generic representation is

```text
s_(t+1) = f_t(s_t, x_t, w_t)
```

where

- `s_t` is the state,
- `x_t` is the action or decision,
- `w_t` is an exogenous quantity such as demand,
- `f_t` is the transition function.

For inventory,

```text
inventory_t
    = inventory_(t-1)
    + production_t
    - demand_t
```

For cumulative installed capacity,

```text
capacity_t
    = capacity_(t-1)
    + expansion_t
    - retirement_t
```

The state summarizes the relevant consequences of the past for future optimization.

## 3. Discounting

If the per-period discount rate is `r`, the present-value factor for period `t` is

```text
beta_t = 1 / (1 + r)^t
```

and a stream of costs `C_t` has present value

```text
PV = sum_t beta_t C_t
```

Discounting is an economic weighting mechanism. It should not be confused with time coupling.

For example,

```text
minimize sum_t beta_t c_t x_t
```

with completely independent constraints for every `t` is discounted, but each period can still be optimized separately. A transition such as

```text
s_(t+1) = s_t + x_t
```

creates actual coupling.

## 4. Simultaneous optimization versus Bellman recursion

Many deterministic finite-horizon models can be written as one large mathematical program.

For example, production planning can optimize all

```text
production_0, ..., production_T
inventory_0, ..., inventory_T
```

at once.

Dynamic programming instead writes the problem recursively:

```text
V_t(s) = min_x {
    C_t(s, x)
    + beta E[V_(t+1)(S')]
}
```

Both views optimize a trajectory across time. The most useful formulation depends on the structure.

LP/MILP is often attractive when:

- transitions are linear,
- integrality can be handled directly,
- all periods and constraints are naturally modeled together.

Dynamic programming is attractive when:

- the state is compact,
- recursive structure is important,
- decisions adapt to state,
- uncertainty or stochastic control is central.

## 5. Terminal conditions

Finite-horizon optimization can suffer from end effects.

Examples:

- an inventory model may deplete all stock at the final date,
- a maintenance model may postpone necessary maintenance beyond the horizon,
- an investment model may undervalue assets whose benefits continue after the horizon.

Common remedies include:

- terminal inventory targets,
- salvage value,
- terminal value functions,
- minimum final capacity,
- cyclic boundary conditions,
- extending the planning horizon.

A terminal condition is part of the model, not merely a numerical detail.

## 6. Irreversibility and timing

Investment timing is a classic intertemporal decision.

Suppose

```text
K_t = K_(t-1) + y_t
```

with

```text
y_t >= 0
```

and no retirement variable. Then expansion is irreversible during the planning horizon.

The planner must trade off:

- installing capacity early, which may incur cost sooner,
- waiting, which preserves flexibility and may benefit from discounting,
- future feasibility limits, which may require anticipatory investment.

This tension appears in infrastructure, manufacturing, energy, logistics, and workforce planning.

## 7. Deterministic versus stochastic intertemporal optimization

Intertemporal structure does not require uncertainty.

In a deterministic model, the entire future trajectory can be optimized at time 0.

Under uncertainty, a multi-stage model must also respect information availability. Decisions at time `t` may depend only on information observed by time `t`.

This leads to non-anticipativity constraints and scenario-tree formulations.

The distinction is:

```text
intertemporal optimization:
    decisions are linked across time

multi-stage stochastic optimization:
    decisions are linked across time
    + uncertainty is revealed progressively
    + decisions must respect information availability
```

## 8. Rolling horizon

A rolling-horizon policy repeatedly:

1. observes the current state,
2. solves a finite-horizon optimization problem,
3. implements only the first decision,
4. advances time,
5. updates forecasts and state,
6. solves again.

This is common in production, logistics, energy, workforce planning, and model predictive control.

Rolling-horizon optimization is useful operationally, but horizon length and terminal treatment still matter.

## 9. Common Operations Research applications

Intertemporal optimization appears in:

- lot sizing,
- inventory control,
- production planning,
- capacity expansion,
- equipment replacement,
- maintenance,
- fleet renewal,
- energy storage,
- hydro reservoir operation,
- financial planning,
- workforce planning,
- supply-chain design over time,
- decarbonization pathways,
- project investment,
- network expansion.

The mathematical details differ, but the central question is stable:

> How should current actions be chosen when their consequences persist into the future?
