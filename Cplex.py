from docplex.mp.model import Model

# Create a new model
model = Model(name="nonlinear_nonconvex")

# Decision variables
x1 = model.continuous_var(name="x1")
x2 = model.continuous_var(name="x2")

# Objective function: Maximize x1 * x2 + x1^2 - x2^2
model.maximize(x1 * x2 + x1**2 - x2**2)

# Constraints
model.add_constraint(x1 + x2 <= 10, "constraint1")
model.add_constraint(x1 >= 0, "nonneg_x1")
model.add_constraint(x2 >= 0, "nonneg_x2")

# Solve the problem
solution = model.solve()

# Output solution
if solution:
    print(f"x1: {solution[x1]}")
    print(f"x2: {solution[x2]}")
    print(f"Objective value: {solution.objective_value}")
else:
    print("No solution found.")
