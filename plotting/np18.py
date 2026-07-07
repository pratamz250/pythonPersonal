import numpy as np

x = np.linspace(0, 4, 10)
print(x)
print("\n\n")

mask = x > 2
print(x[mask])
