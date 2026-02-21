import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 2)

x = np.linspace(-2, 2, 50)
y = np.linspace(-2, 2, 50)


ax[0].plot(x, y)
ax[1].plot(x, y**2)

plt.show()
