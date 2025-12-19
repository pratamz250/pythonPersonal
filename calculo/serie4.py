#Série ((n+1)/(n-1))^n
import matplotlib.pyplot as plt

x = list(range(2, 100))
y = list(((i+1)/(i-1))**i for i in x)

plt.plot(x, y)
plt.title("Série ((n+1)/(n-1))^n")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()
