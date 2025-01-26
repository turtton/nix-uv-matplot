import matplotlib.pyplot as plt
import numpy as np
from numpy import ndarray

triangle = np.array([[0, 0], [1, 0], [1, 1]])
triangle2 = np.array([[0, 0], [0, 1], [1, 1]])


def draw(error_list: ndarray[tuple[int, ...], np.dtype], color: str) -> None:
    plt.plot(error_list[:, 0], error_list[:, 1], f"{color}-")
    plt.fill(error_list[:, 0], error_list[:, 1], color, alpha=0.3)


# プロット
plt.figure()
draw(triangle, "r")
draw(triangle2, "b")
plt.gca().set_aspect("equal")
plt.title("Square")
plt.show()
