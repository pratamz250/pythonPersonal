import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 2, subplot_kw={'projection': '3d'})

x = np.linspace(-2, 2, 50)
y = np.linspace(-2, 2, 50)

X, Y = np.meshgrid(x, y)

Z1 = X**2 + Y**2 - 1
Z2 = X**2 - Y**2 - 1

ax[0].plot_surface(X, Y, Z1, cmap='viridis')
ax[1].plot_surface(X, Y, Z2, cmap='plasma')

plt.show()
