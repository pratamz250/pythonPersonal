import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

x = np.linspace(-1, 1, 10)
y = np.linspace(-4, 20, 10)

line1, = ax.plot(x, y**3, color="blue", label="line 1")
ax.plot(x+2, np.sqrt(y), color="red", label="line 2")
ax.plot(x, y, color="green", label="line 3")
ax.legend(loc="upper left")

def eventLine1(event):
    if event.key == 'v':
        line1.set_visible(False)
    elif event.key == 'V':
        line1.set_visible(True)
    fig.canvas.draw()

fig.canvas.mpl_connect("key_press_event", eventLine1)

plt.show()
