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

# Define master problem variables
alpha = cp.Variable()
beta = cp.Variable()

# Define master problem objective
objective_master = alpha + beta

# Define master problem constraints
constraints_master = [alpha >= 0, beta >= 0]

# Formulate master problem
problem_master = cp.Problem(cp.Minimize(objective_master), constraints_master)

# Initialize values
epsilon = 1e-6
tolerance = 1e-4
converged = False
iteration = 0

while not converged:
    # Solve master problem
    problem_master.solve()

    # Update subproblem
    x1.value = alpha.value
    x2.value = beta.value

    # Solve subproblem
    problem_sub = cp.Problem(cp.Minimize((x1 - 1)**2 + (x2 - 2)**2),
                             [x1 + x2 >= 3,
                              x1 - x2 <= 1,
                              x1 >= 0,
                              x2 >= 0])
    problem_sub.solve()

    # Update master problem variables with subproblem solution
    alpha.value = x1.value
    beta.value = x2.value

    # Check convergence
    residual = np.abs(problem_sub.value - problem_master.value)
    if residual < tolerance:
        converged = True

    iteration += 1

optimal_value_benders = problem_master.value
optimal_x1_benders = alpha.value
optimal_x2_benders = beta.value

print("Optimal value (Benders Decomposition):", optimal_value_benders)
print("Optimal x1 (Benders Decomposition):", optimal_x1_benders)
print("Optimal x2 (Benders Decomposition):", optimal_x2_benders)