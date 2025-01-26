import matplotlib.pyplot as plt
import matplotlib.patches as patches

# プロット
fig, ax = plt.subplots()
rounded_square = patches.FancyBboxPatch(
    (0.1, 0.1),
    0.8,
    0.8,
    boxstyle="round,pad=0.1,rounding_size=0.2",
    edgecolor="r",
    facecolor="r",
    alpha=0.3,
)
ax.add_patch(rounded_square)
ax.set_aspect("equal")
plt.title("Rounded Square")
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.show()
