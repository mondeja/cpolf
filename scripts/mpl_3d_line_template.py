"""
Need imagemagick, numpy and matplotlib installed.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

TITLE = None
SAVE = True
OUTPUT_FILE = 'output.gif'

fig = plt.figure(figsize=[7.68, 5.76])
ax = plt.axes(projection='3d')

# main line
xrange = np.linspace(0, 10, 10)
yrange = np.linspace(0, 10, 10)
zrange = np.linspace(0, 10, 10)
ax.plot3D(xrange, yrange, zrange, 'k')

# guide line to 0.5
_red_guide_x = np.linspace(0, 4.9, 10)
_red_guide_y = np.linspace(0, 4.9, 10)
_red_guide_z = np.linspace(0.5, 5.5, 10)
ax.plot3D(_red_guide_x, _red_guide_y, _red_guide_z, 'r--')

# central point (0.5)
ax.plot3D([5], [5], [5], markerfacecolor='r', markeredgecolor='r', marker='o', markersize=3)
ax.text(4.7, 4.7, 5.7, "0.5", color='red')

# p0
ax.plot3D([0], [0], [0], markerfacecolor='b', markeredgecolor='b', marker='o', markersize=2.5)
ax.text(.6, .6, -.3, "0, 0, 0", color='blue')
# p1
ax.plot3D([10], [10], [10], markerfacecolor='b', markeredgecolor='b', marker='o', markersize=2.5)
ax.text(10, 10, 10.8, "10, 10, 10", color='blue')

# result
ax.text(5, 5, 3, '5, 5, 5', color="g")

# limits
ax.set_ylim(0, 10)
ax.set_xlim(0, 10)
ax.set_zlim(0, 10)

# styles
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
if TITLE:
    ax.set_title(TITLE)

ax.xaxis.label.set_color('chocolate')
ax.yaxis.label.set_color('chocolate')
ax.zaxis.label.set_color('chocolate')

ax.tick_params(colors='rebeccapurple')
for spine in ax.spines.values():
    spine.set_color("rebeccapurple")

if SAVE:

    def update(i, fig, ax):
        ax.view_init(elev=20., azim=i)
        return fig, ax
     
    anim = FuncAnimation(fig, update, frames=np.arange(0, 360, 2), repeat=True, fargs=(fig, ax))
    anim.save(OUTPUT_FILE, dpi=100, writer='imagemagick', fps=24)
else:
    plt.show()