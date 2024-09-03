import gurobipy as gp
from gurobipy import GRB

# Create a Gurobi model
model = gp.Model("Nonlinear_Programming")

# Define variables
x1 = model.addVar(name="x1", lb=0)  # Adding lb=0 since x1 >= 0
x2 = model.addVar(name="x2", lb=0)  # Adding lb=0 since x2 >= 0

# Update the model to integrate new variables
model.update()

# Define the objective function: Minimize (x1 - 1)^2 + (x2 - 2)^2
objective = (x1 - 1)**2 + (x2 - 2)**2
model.setObjective(objective, GRB.MINIMIZE)

# Define constraints
model.addConstr(x1 + x2 >= 3, "c1")
model.addConstr(x1 - x2 <= 1, "c2")

# Optimize the model
model.optimize()

# Retrieve the results
if model.status == GRB.OPTIMAL:
    optimal_value_nlp = model.objVal
    optimal_x1_nlp = x1.x
    optimal_x2_nlp = x2.x
    
    print("Optimal value (Nonlinear Programming with Gurobi):", optimal_value_nlp)
    print("Optimal x1 (Nonlinear Programming with Gurobi):", optimal_x1_nlp)
    print("Optimal x2 (Nonlinear Programming with Gurobi):", optimal_x2_nlp)
else:
    print("Optimal solution not found.")

