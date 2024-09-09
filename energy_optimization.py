import gurobipy as gp
from gurobipy import GRB

# Create model
model = gp.Model("energy_optimization")

# Decision variables: power generated, power stored
power_gen = model.addVar(lb=0, ub=100, name="PowerGenerated")
power_store = model.addVar(lb=0, ub=50, name="PowerStored")

# Parameters
demand = 50  # Required power demand

# Constraints
model.addConstr(power_gen + power_store <= 100, "SupplyLimit")  # Total power limit
model.addConstr(power_gen >= demand, "DemandConstraint")  # Ensure demand is met

# Objective: minimize generation costs (quadratic cost function)
model.setObjective(0.5 * power_gen * power_gen + 10 * power_store, GRB.MINIMIZE)

# Optimize
model.optimize()

# Print results
for v in model.getVars():
    print(f"{v.varName}: {v.x}")
print(f"Objective Value: {model.objVal}")
