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

# Solving using Nonlinear Programming (Sequential Quadratic Programming)
problem = cp.Problem(objective, constraints)
# problem.solve(solver=cp.SCS, verbose=False)  # Using SCS solver for SQP
problem.solve()  # Using SCS solver for SQP
optimal_value_nlp = problem.value
optimal_x1_nlp = x1.value
optimal_x2_nlp = x2.value

print("Optimal value (Nonlinear Programming):", optimal_value_nlp)
print("Optimal x1 (Nonlinear Programming):", optimal_x1_nlp)
print("Optimal x2 (Nonlinear Programming):", optimal_x2_nlp)






## check time and memory usage
## tramelloc provide (x,y) where x is current memory usage and y is peak memory usage.
import time
import tracemalloc

# record start time
start = time.time()
tracemalloc.start()


end = time.time()
print(tracemalloc.get_traced_memory()) 
# stopping the library
tracemalloc.stop()
print("The time of execution of above program is :", (end-start) * 10**3, "ms")