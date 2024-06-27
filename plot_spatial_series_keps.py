import numpy as np
import matplotlib.pyplot as plt

x, y = np.loadtxt("./repar_keps/keps_u_planes.txt",
                   dtype=float,
                   skiprows=0,
                   delimiter=' ',
                   unpack=True)

fig, ax = plt.subplots()
ax.set_xlabel(r'$x$ [m]')
ax.set_ylabel(r'$u$ [m/s]')
ax.axis([0, 30, 16, 20])
ax.xaxis.set_major_locator(plt.MultipleLocator(5))
ax.xaxis.set_minor_locator(plt.MultipleLocator(2.5))
ax.yaxis.set_major_locator(plt.MultipleLocator(.5))
ax.yaxis.set_minor_locator(plt.MultipleLocator(.25))
ax.scatter(x, y,
           s=25,
           c='white',
           marker='o',
           edgecolors='black')
ax.grid(color='lightgrey',ls='-.')
ax.legend(facecolor="white", framealpha=1, frameon=1)
fig.tight_layout(pad=0.01)
# plt.savefig('./repar_keps/figures/keps_u_planes.png',
#             dpi=1200,
#             format='png')

R = 0.320675
v2 = 20.14*0.95**2
print(v2)
