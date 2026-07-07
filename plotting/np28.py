import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

x = np.linspace(-4, 4, 50)
y = x**2 + 2*x - 3

ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.set_title("Função simples com eventos")
ax.axhline(0, color="black", linestyle="--")
ax.axvline(0, color="black", linestyle="--")

line, = ax.plot(x, y, label="y = x^2 + 2x - 3")
ax.legend(loc="upper left")
def onEvent(event):
    print(f"tecla:{event.key}")
    print(f"eixo:{event.inaxes}")
    print(f"coordx:{event.xdata} | coordy:{event.ydata}")

fig.canvas.mpl_connect("key_press_event", onEvent)

plt.show()
