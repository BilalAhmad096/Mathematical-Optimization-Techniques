import gurobipy as gp
from gurobipy import GRB

# Data
supply = [20, 30]  # Supply from two factories
demand = [10, 20, 15]  # Demand at three warehouses
costs = [[8, 6, 10], [9, 12, 5]]  # Transport costs from factory i to warehouse j

# Create model
model = gp.Model("supply_chain_optimization")

# Decision variables: units transported from each factory to each warehouse
x = model.addVars(2, 3, lb=0, name="Transport")

# Supply and demand constraints
for i in range(2):
    model.addConstr(sum(x[i, j] for j in range(3)) <= supply[i], f"SupplyFactory{i}")
for j in range(3):
    model.addConstr(sum(x[i, j] for i in range(2)) == demand[j], f"DemandWarehouse{j}")

# Objective: minimize transport cost
model.setObjective(gp.quicksum(costs[i][j] * x[i, j] for i in range(2) for j in range(3)), GRB.MINIMIZE)

# Optimize
model.optimize()

# Print results
for v in model.getVars():
    print(f"{v.varName}: {v.x}")
print(f"Objective Value: {model.objVal}")
