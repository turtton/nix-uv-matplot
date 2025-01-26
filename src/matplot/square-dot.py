import numpy as np
import random
import matplotlib.pyplot as plt
from numpy import ndarray
from scipy.spatial import ConvexHull
from scipy.optimize import minimize

def get_square(num_points: int, side_length: float) -> ndarray:
    point_cloud = []
    for _ in range(num_points):
        x = random.uniform(-side_length / 2, side_length / 2)
        y = random.uniform(-side_length / 2, side_length / 2)
        point_cloud.append([x, y])
    return np.array(point_cloud)

def fit_rectangle(points: ndarray) -> ndarray:
    def rectangle_area(params: tuple[float, float, float, float, float]):
        cx, cy, angle, width, height = params
        theta = np.radians(angle)
        R = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
        rect = np.array([[-width/2, -height/2], [width/2, -height/2], [width/2, height/2], [-width/2, height/2]])
        rect = np.dot(rect, R.T) + [cx, cy]
        hull = ConvexHull(points)
        return np.sum(np.min(np.linalg.norm(points[hull.vertices][:, None] - rect, axis=2), axis=1))

    centroid: ndarray[dict[int, ...], np.dtype] = np.mean(points, axis=0)
    initial_guess = [centroid[0], centroid[1], 0, 1, 1]
    result = minimize(rectangle_area, initial_guess, method='L-BFGS-B')
    cx, cy, angle, width, height = result.x
    theta = np.radians(angle)
    R = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
    rect = np.array([[-width/2, -height/2], [width/2, -height/2], [width/2, height/2], [-width/2, height/2], [-width/2, -height/2]])
    rect = np.dot(rect, R.T) + [cx, cy]
    return rect

num_points = 1000
side_length = 1.0
test_data = get_square(num_points, side_length)

hull = ConvexHull(test_data)

hull_points = test_data[hull.vertices]
rectangle = fit_rectangle(hull_points)

fig, ax = plt.subplots(figsize=(8, 8))
ax.scatter(test_data[:, 0], test_data[:, 1], s=1, c="b")

for simplex in hull.simplices:
    ax.plot(test_data[simplex, 0], test_data[simplex, 1], 'r-')

ax.plot(rectangle[:, 0], rectangle[:, 1], 'g--', linewidth=2)

plt.show()
