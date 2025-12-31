import matplotlib.pyplot as plt

x = [i for i in range(1, 100)]
y = [1/i for i in x]

plt.plot(x, y)
plt.title("Série Harmônica")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()
