import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

x = np.linspace(-9, 1, 50)
y = np.tan((np.sqrt(x) + 2*x)/(np.cos(x - 1) - 3*x**2))

line, = ax.plot(x, y)
def onEvent(event):
    if event.key == 'r':
        line.set_color("red")
    elif event.key == 'b':
        line.set_color("blue")
    elif event.key == 'p':
        line.set_color("pink")
    else:
        line.set_color("brown")
        print(f"tecla:{event.key}")
    fig.canvas.draw()

fig.canvas.mpl_connect("key_press_event", onEvent)

plt.show()
