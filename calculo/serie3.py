import matplotlib.pyplot as plt
import math

x = list(range(1, 100))
y = [math.sqrt(i) for i in x]

plt.scatter(x, y)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()
