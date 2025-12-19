#Série: {1, 1/2, 1/3, 1/4, ..., 1/n, ...}
import subprocess
import matplotlib.pyplot as plt

#Escrever no arquivo
with open("dados.txt", "a") as arquivo:
    for i in range(1, 100):
        n = 1/i
        arquivo.write(str(n) + "\n")
        #print(n)

#Plotar com Matplotlib
x = [i for i in range(1, 100)]
y = [1/i for i in x]

plt.scatter(x, y)
plt.title("Série {1, 1/2, 1/3, ..., 1/n, ...}")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()

subprocess.run(["xdg-open", "dados.txt"])
