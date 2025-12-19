import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
#y = [2, 4, 6, 8, 10]
#ou
y = [2*i for i in x]

#plt.plot(x, y) #plota com linhas
plt.scatter(x, y) #plota com pontos
plt.title("Primeiro exemplo")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()
