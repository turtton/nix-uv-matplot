import matplotlib.pyplot as plt
import numpy as np

# 三角形の頂点の座標
triangle = np.array([[0, 0], [1, 0], [0.5, np.sqrt(3) / 2], [0, 0]])

# プロット
plt.figure()
plt.plot(triangle[:, 0], triangle[:, 1], "b-")  # 'b-'は青色の線を意味します
plt.fill(triangle[:, 0], triangle[:, 1], "b", alpha=0.3)  # 三角形を青色で塗りつぶします
plt.gca().set_aspect("equal")  # アスペクト比を1:1に設定します
plt.title("Triangle")
plt.show()
