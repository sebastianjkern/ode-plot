import matplotlib.pyplot as plt
import numpy as np
import math

mesh_width = 0.5
dir_field_x_template = np.linspace(-mesh_width / 2, mesh_width / 2, 100)
xlims = [-5, 5]
ylims = [-5, 5]

def dydx(x, y):
    return math.cos(x-y)

plt.figure(figsize=(7, 6))
plt.xlim(xlims)
plt.ylim(ylims)
plt.axvline(0, c="black")
plt.axhline(0, c="black")

for x in np.arange(xlims[0], xlims[1], mesh_width):
    for y in np.arange(ylims[0], ylims[1], mesh_width):
        curr_slope = dydx(x, y)
        curr_intercept = y - curr_slope * x
        dir_field_xs = dir_field_x_template + x
        dir_field_ys = [curr_slope * dfx + curr_intercept for dfx in dir_field_xs]
        plt.plot(dir_field_xs, dir_field_ys, color="red")
plt.xlabel("x")
plt.ylabel("y")
plt.title("dy/dx")
plt.show()
