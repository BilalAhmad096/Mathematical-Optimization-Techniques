import numpy as np
from scipy.optimize import minimize

# Define the objective function
def objective(vars):
    x1, x2 = vars
    return -(x1 * x2 + x1**2 - x2**2)  # We negate the objective because SciPy minimizes by default

# Define the constraint: x1 + x2 <= 10
def constraint(vars):
    return 10 - (vars[0] + vars[1])

# Set the bounds for the variables: x1, x2 >= 0
bounds = [(0, None), (0, None)]

# Initial guess
x0 = [1, 1]

# Define the constraint dictionary
constraints = [{'type': 'ineq', 'fun': constraint}]

# Solve the problem
solution = minimize(objective, x0, method='SLSQP', bounds=bounds, constraints=constraints)

# Output the solution
if solution.success:
    print(f"x1: {solution.x[0]}")
    print(f"x2: {solution.x[1]}")
    print(f"Objective value: {-solution.fun}")  # Negate again to get the maximized value
else:
    print("No solution found.")
