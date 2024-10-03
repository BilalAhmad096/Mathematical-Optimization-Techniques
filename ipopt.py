from pyomo.environ import ConcreteModel, Var, Objective, Constraint, SolverFactory, value

# Create a simple model
model = ConcreteModel()

# Define variables
model.x = Var(initialize=0.5, bounds=(0, 2))  # Variable with bounds
model.y = Var(initialize=1.5, bounds=(0, 2))

# Define an objective function (to be minimized)
model.obj = Objective(expr=(model.x - 1)**2 + (model.y - 1)**2)

# Add a constraint
model.constr = Constraint(expr=model.x + model.y == 1)

# Create IPOPT solver instance
solver = SolverFactory('ipopt')

# Solve the model
result = solver.solve(model, tee=True)

# Display results
model.display()

# Accessing the solution
x_value = value(model.x)
y_value = value(model.y)

print(f"Optimal solution: x = {x_value}, y = {y_value}")
