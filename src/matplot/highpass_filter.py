import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-0.2, 2 * np.pi, 200)
# y(k) - 3/4y(k-1) + 1/8y(k-2) = u(k) - u(k-1) {k>=0}
y = 10*(1/2)**x-9*(1/4)**x

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()
