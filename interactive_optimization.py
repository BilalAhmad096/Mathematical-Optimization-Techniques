import gurobipy as gp
from gurobipy import GRB

def run_linear_optimization():
    # User input
    num_vars = int(input("Enter number of variables: "))
    
    # Create model
    model = gp.Model("user_optimization")
    
    # Decision variables
    variables = model.addVars(num_vars, lb=-GRB.INFINITY, ub=GRB.INFINITY, name="Vars")

    # Objective coefficients
    obj_coefs = [float(input(f"Enter objective coefficient for variable {i}: ")) for i in range(num_vars)]
    
    # Objective: maximize linear objective
    model.setObjective(sum(obj_coefs[i] * variables[i] for i in range(num_vars)), GRB.MAXIMIZE)

    # Constraints: user-defined (simple demo)
    for i in range(num_vars):
        lb = float(input(f"Enter lower bound for variable {i}: "))
        ub = float(input(f"Enter upper bound for variable {i}: "))
        model.addConstr(variables[i] >= lb, f"LB_Var{i}")
        model.addConstr(variables[i] <= ub, f"UB_Var{i}")
    
    # Optimize
    model.optimize()

    # Print results
    for v in model.getVars():
        print(f"{v.varName}: {v.x}")
    print(f"Objective Value: {model.objVal}")

# Call the function
run_linear_optimization()