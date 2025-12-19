#Série {0, 1/2, 2/3, 3/4, ..., 1-(1/n), ...}
import matplotlib.pyplot as plt

x = [i for i in range(1, 100)]
y = [1-(1/i) for i in x]

plt.plot(x, y)
#plt.scatter(x, y)
plt.title("Série {0, 1/2, 2/3, 3/4, ..., 1-(1/n), ...}")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()
