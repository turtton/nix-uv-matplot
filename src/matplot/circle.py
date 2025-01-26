import matplotlib.pyplot as plt
import numpy as np

n = np.linspace(0, 2 * np.pi, 200)
x = np.cos(n)
y = np.sin(n)

fig, ax = plt.subplots()
ax.plot(x, y)
plt.gca().set_aspect("equal")
plt.show()
