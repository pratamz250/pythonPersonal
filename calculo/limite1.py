#Analisando o limite 1/n com n tentendo ao infinito

import matplotlib.pyplot as plt

x = list(range(1, 100))
y = list(1/i for i in x)

plt.plot(x, y)
plt.title("lim 1/n com n->oo")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()
