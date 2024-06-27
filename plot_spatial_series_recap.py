import numpy as np
import matplotlib.pyplot as plt


# plt.style.use('singleColumn.mplstyle')
fig, ax = plt.subplots()
ax.set_xlabel(r'$x$ [m]')
ax.set_ylabel(r'$T$ [K]')
# ax.axis([0, 30, 413.15, 418.15])
# ax.xaxis.set_major_locator(plt.MultipleLocator(5))
# ax.xaxis.set_minor_locator(plt.MultipleLocator(2.5))
# ax.yaxis.set_major_locator(plt.MultipleLocator(0.5))
# ax.yaxis.set_minor_locator(plt.MultipleLocator(.25))

x, y = np.loadtxt("./recap_14m/recap_temperature_planes.txt",
                   dtype=float,
                   skiprows=0,
                   delimiter=' ',
                   unpack=True)
ax.scatter(x, y,
           s=25,
           c='white',
           marker='o',
           edgecolors='black',
           linewidths=1,
           label='Recap 14m'
           )

fig.tight_layout(pad=0.01)
ax.grid(color='lightgrey',ls='-.')
ax.legend(facecolor="white", framealpha=1, frameon=1)
# # plt.savefig('./new_repar_30m/figures/temperature_planes.png',
# #             dpi=1200,
# #             format='png')


# plt.style.use('singleColumn.mplstyle')
fig, ax = plt.subplots()
ax.set_xlabel(r'$x$ [m]')
ax.set_ylabel(r'$U$ [m/s]')
# ax.axis([0, 30, 413.15, 418.15])
# ax.xaxis.set_major_locator(plt.MultipleLocator(5))
# ax.xaxis.set_minor_locator(plt.MultipleLocator(2.5))
# ax.yaxis.set_major_locator(plt.MultipleLocator(0.5))
# ax.yaxis.set_minor_locator(plt.MultipleLocator(.25))

x, y = np.loadtxt("./recap_14m/recap_u_planes.txt",
                   dtype=float,
                   skiprows=0,
                   delimiter=' ',
                   unpack=True)
ax.scatter(x, y,
           s=25,
           c='white',
           marker='o',
           edgecolors='black',
           linewidths=1,
           label='Recap 14m'
           )

fig.tight_layout(pad=0.01)
ax.grid(color='lightgrey',ls='-.')
ax.legend(facecolor="white", framealpha=1, frameon=1)
# # plt.savefig('./new_repar_30m/figures/u_planes.png',
# #             dpi=1200,
# #             format='png')


# plt.style.use('singleColumn.mplstyle')
fig, ax = plt.subplots()
ax.set_xlabel(r'$x$ [m]')
ax.set_ylabel(r'$Y_{H2O}$ [-]')
# ax.axis([0, 30, 413.15, 418.15])
# ax.xaxis.set_major_locator(plt.MultipleLocator(5))
# ax.xaxis.set_minor_locator(plt.MultipleLocator(2.5))
# ax.yaxis.set_major_locator(plt.MultipleLocator(0.5))
# ax.yaxis.set_minor_locator(plt.MultipleLocator(.25))

x, y = np.loadtxt("./recap_14m/recap_YH2O_planes.txt",
                   dtype=float,
                   skiprows=0,
                   delimiter=' ',
                   unpack=True)
ax.scatter(x, y,
           s=25,
           c='white',
           marker='o',
           edgecolors='black',
           linewidths=1,
           label='Recap 14m'
           )

fig.tight_layout(pad=0.01)
ax.grid(color='lightgrey',ls='-.')
ax.legend(facecolor="white", framealpha=1, frameon=1)
# # plt.savefig('./new_repar_30m/figures/YH2O_planes.png',
# #             dpi=1200,
# #             format='png')
