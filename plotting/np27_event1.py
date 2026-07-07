import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

x = np.linspace(-2, 2, 200)
y = x**2

line, = ax.plot(x, y)

def onEvent(event):
    if event.key == 'r':
        line.set_color('red')
    elif event.key == 'b':
        line.set_color('blue')
    fig.canvas.draw()

fig.canvas.mpl_connect("key_press_event", onEvent)

plt.show()
