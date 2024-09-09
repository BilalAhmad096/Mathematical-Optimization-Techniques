import gurobipy as gp
from gurobipy import GRB

# Data: demand, generation capacity, cost, renewable source availability
demand = [50, 60, 70]
renewable = [30, 40, 20]  # Available renewable energy
gen_capacity = [100, 120, 100]  # Total generation capacity
cost = [5, 6, 7]  # Cost per unit of energy

# Create model
model = gp.Model("smart_grid_optimization")

# Decision variables: amount generated from non-renewable and renewable sources
non_renewable_gen = model.addVars(3, lb=0, name="NonRenewableGen")
renewable_gen = model.addVars(3, lb=0, ub=renewable, name="RenewableGen")

# Constraints: meet demand
for t in range(3):
    model.addConstr(non_renewable_gen[t] + renewable_gen[t] == demand[t], f"Demand_t{t}")

# Objective: minimize cost
model.setObjective(gp.quicksum(cost[t] * non_renewable_gen[t] for t in range(3)), GRB.MINIMIZE)

# Optimize
model.optimize()

# Print results
for v in model.getVars():
    print(f"{v.varName}: {v.x}")
print(f"Objective Value: {model.objVal}")
