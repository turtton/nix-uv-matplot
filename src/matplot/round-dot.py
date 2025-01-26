import numpy as np
import random
import matplotlib.pyplot as plt
from numpy import ndarray
from scipy.optimize import least_squares
from scipy.spatial import ConvexHull


def get_ball(num_points: int, r: float) -> ndarray[tuple[int, ...], np.dtype]:
    point_cloud = []
    for i in range(num_points):
        t = random.random()
        t = np.arcsin(1 - 2 * t)
        u = random.random() * 2 * np.pi - np.pi
        x = np.cos(t) * np.cos(u) * r
        y = np.cos(t) * np.sin(u) * r
        z = np.sin(t) * r
        point_cloud.append([x, y, z])
    return np.array(point_cloud)


# 点群作成
num_points = 1000
r = 0.5
test_data = get_ball(num_points, r)


# 最小二乗法を使用して点群の外側の輪郭に円をフィットさせる
def fit_circle(x: ndarray[tuple[int, ...], np.dtype], y: ndarray[tuple[int, ...], np.dtype]) -> tuple[
    tuple[float, float], float]:
    def calc_R(c):
        return np.sqrt((x - c[0]) ** 2 + (y - c[1]) ** 2)

    def f_2(c):
        Ri = calc_R(c)
        return Ri - Ri.mean()

    center_estimate = np.mean(x), np.mean(y)
    center = least_squares(f_2, center_estimate).x
    radius = calc_R(center).mean()
    return center, radius


# 2次元に投影
test_data_2d = test_data[:, :2]

# ConvexHullを使用して外側の輪郭を計算
hull = ConvexHull(test_data_2d)

hull_points = test_data_2d[hull.vertices]
center, radius = fit_circle(hull_points[:, 0], hull_points[:, 1])

# matplotlibで可視化
fig, ax = plt.subplots(figsize=(8, 8))
ax.scatter(test_data_2d[:, 0], test_data_2d[:, 1], s=1, c="b")

# 外側の輪郭を線で結ぶ
for simplex in hull.simplices:
    ax.plot(test_data_2d[simplex, 0], test_data_2d[simplex, 1], 'r-')

circle = plt.Circle(center, radius, color='g', fill=False, linestyle='--', linewidth=2)
ax.add_patch(circle)

plt.show()
