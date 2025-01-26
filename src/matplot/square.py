import matplotlib.pyplot as plt
import numpy as np

# 正方形の頂点の座標
square = np.array([[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]])

# プロット
plt.figure()
plt.plot(square[:, 0], square[:, 1], "r-")  # 'r-'は赤色の線を意味します
plt.fill(square[:, 0], square[:, 1], "r", alpha=0.3)  # 正方形を赤色で塗りつぶします
plt.gca().set_aspect("equal")
plt.title("Square")
plt.show()
