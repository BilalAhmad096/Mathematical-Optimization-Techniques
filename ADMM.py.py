import cvxpy as cp
import numpy as np

# Define variables
x1 = cp.Variable()
x2 = cp.Variable()

# Define objective function
objective = cp.Minimize((x1 - 1)**2 + (x2 - 2)**2)

# Define constraints
constraints = [x1 + x2 >= 3,
               x1 - x2 <= 1,
               x1 >= 0,
               x2 >= 0]

# Define auxiliary variables
z1 = cp.Variable()
z2 = cp.Variable()

# Define ADMM objective
objective_admm = (x1 - 1)**2 + (x2 - 2)**2 + cp.sum_squares(z1) + cp.sum_squares(z2)

# Define ADMM constraints
constraints_admm = [x1 + x2 >= 3,
                    x1 - x2 <= 1,
                    z1 == x1,
                    z2 == x2]

# Formulate ADMM problem and solve
problem_admm = cp.Problem(cp.Minimize(objective_admm), constraints_admm)
problem_admm.solve()

# Retrieve optimal values
optimal_value_admm = problem_admm.value
optimal_x1_admm = x1.value
optimal_x2_admm = x2.value

print("Optimal value (ADMM):", optimal_value_admm)
print("Optimal x1 (ADMM):", optimal_x1_admm)
print("Optimal x2 (ADMM):", optimal_x2_admm)