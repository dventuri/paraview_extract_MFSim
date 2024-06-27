import numpy as np
import matplotlib.pyplot as plt


# plt.style.use('singleColumn.mplstyle')
fig, ax = plt.subplots()
ax.set_xlabel(r'$x$ [m]')
ax.set_ylabel(r'$T$ [K]')
# ax.axis([0, 30, 413.15, 418.15])
ax.xaxis.set_major_locator(plt.MultipleLocator(5))
ax.xaxis.set_minor_locator(plt.MultipleLocator(2.5))
# ax.yaxis.set_major_locator(plt.MultipleLocator(0.5))
# ax.yaxis.set_minor_locator(plt.MultipleLocator(.25))

x, y = np.loadtxt("./new_repar_30m/mix_1p_temperature_planes.txt",
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
           label='Mix 1'
           )

x, y = np.loadtxt("./new_repar_30m/mix_10p_temperature_planes.txt",
                   dtype=float,
                   skiprows=0,
                   delimiter=' ',
                   unpack=True)
ax.scatter(x, y,
           s=25,
           c='white',
           marker='s',
           edgecolors='black',
           linewidths=1,
           label='Mix 10'
           )

x, y = np.loadtxt("./new_repar_30m/mix_10preal_temperature_planes.txt",
                   dtype=float,
                   skiprows=0,
                   delimiter=' ',
                   unpack=True)
ax.scatter(x, y,
           s=25,
           c='white',
           marker='v',
           edgecolors='black',
           linewidths=1,
           label='Mix 10R'
           )

x, y = np.loadtxt("./new_repar_30m/mix_40p_temperature_planes.txt",
                   dtype=float,
                   skiprows=0,
                   delimiter=' ',
                   unpack=True)
ax.scatter(x, y,
           s=25,
           c='white',
           marker='P',
           edgecolors='black',
           linewidths=1,
           label='Mix 40'
           )

x, y = np.loadtxt("./new_repar_30m/UL_40p_temperature_planes.txt",
                   dtype=float,
                   skiprows=0,
                   delimiter=' ',
                   unpack=True)
ax.scatter(x, y,
           s=25,
           c='white',
           marker='^',
           edgecolors='black',
           linewidths=1,
           label='UL 40'
           )


# x, y = np.loadtxt("./new_repar_30m/old_temperature_planes.txt",
#                    dtype=float,
#                    skiprows=0,
#                    delimiter=' ',
#                    unpack=True)
# ax.scatter(x, y,
#            s=25,
#            c='white',
#            marker='*',
#            edgecolors='black',
#            linewidths=1,
#            label='Old'
#            )

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
ax.xaxis.set_major_locator(plt.MultipleLocator(5))
ax.xaxis.set_minor_locator(plt.MultipleLocator(2.5))
# ax.yaxis.set_major_locator(plt.MultipleLocator(0.5))
# ax.yaxis.set_minor_locator(plt.MultipleLocator(.25))

x, y = np.loadtxt("./new_repar_30m/mix_1p_u_planes.txt",
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
           label='Mix 1'
           )

x, y = np.loadtxt("./new_repar_30m/mix_10p_u_planes.txt",
                   dtype=float,
                   skiprows=0,
                   delimiter=' ',
                   unpack=True)
ax.scatter(x, y,
           s=25,
           c='white',
           marker='s',
           edgecolors='black',
           linewidths=1,
           label='Mix 10'
           )

x, y = np.loadtxt("./new_repar_30m/mix_10preal_u_planes.txt",
                   dtype=float,
                   skiprows=0,
                   delimiter=' ',
                   unpack=True)
ax.scatter(x, y,
           s=25,
           c='white',
           marker='v',
           edgecolors='black',
           linewidths=1,
           label='Mix 10R'
           )

x, y = np.loadtxt("./new_repar_30m/mix_40p_u_planes.txt",
                   dtype=float,
                   skiprows=0,
                   delimiter=' ',
                   unpack=True)
ax.scatter(x, y,
           s=25,
           c='white',
           marker='P',
           edgecolors='black',
           linewidths=1,
           label='Mix 40'
           )

x, y = np.loadtxt("./new_repar_30m/UL_40p_u_planes.txt",
                   dtype=float,
                   skiprows=0,
                   delimiter=' ',
                   unpack=True)
ax.scatter(x, y,
           s=25,
           c='white',
           marker='^',
           edgecolors='black',
           linewidths=1,
           label='UL 40'
           )

x, y = np.loadtxt("./new_repar_30m/teste_u_planes.txt",
                   dtype=float,
                   skiprows=0,
                   delimiter=' ',
                   unpack=True)
ax.scatter(x, y,
           s=25,
           c='white',
           marker='*',
           edgecolors='black',
           linewidths=1,
           label='Ghost IB'
           )

# x, y = np.loadtxt("./new_repar_30m/old_u_planes.txt",
#                    dtype=float,
#                    skiprows=0,
#                    delimiter=' ',
#                    unpack=True)
# ax.scatter(x, y,
#            s=25,
#            c='white',
#            marker='*',
#            edgecolors='black',
#            linewidths=1,
#            label='Old'
#            )


fig.tight_layout(pad=0.01)
ax.grid(color='lightgrey',ls='-.')
ax.legend(facecolor="white", framealpha=1, frameon=1)
# # plt.savefig('./new_repar_30m/figures/u_planes.png',
# #             dpi=1200,
# #             format='png')



# plt.style.use('singleColumn.mplstyle')
fig, ax = plt.subplots()
ax.set_xlabel(r'$x$ [m]')
ax.set_ylabel(r'$Y_{H2O}$ [m/s]')
# ax.axis([0, 30, 413.15, 418.15])
ax.xaxis.set_major_locator(plt.MultipleLocator(5))
ax.xaxis.set_minor_locator(plt.MultipleLocator(2.5))
# ax.yaxis.set_major_locator(plt.MultipleLocator(0.5))
# ax.yaxis.set_minor_locator(plt.MultipleLocator(.25))

x, y = np.loadtxt("./new_repar_30m/mix_1p_YH2O_planes.txt",
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
           label='Mix 1'
           )

x, y = np.loadtxt("./new_repar_30m/mix_10p_YH2O_planes.txt",
                   dtype=float,
                   skiprows=0,
                   delimiter=' ',
                   unpack=True)
ax.scatter(x, y,
           s=25,
           c='white',
           marker='s',
           edgecolors='black',
           linewidths=1,
           label='Mix 10'
           )

x, y = np.loadtxt("./new_repar_30m/mix_10preal_YH2O_planes.txt",
                   dtype=float,
                   skiprows=0,
                   delimiter=' ',
                   unpack=True)
ax.scatter(x, y,
           s=25,
           c='white',
           marker='v',
           edgecolors='black',
           linewidths=1,
           label='Mix 10R'
           )

x, y = np.loadtxt("./new_repar_30m/mix_40p_YH2O_planes.txt",
                   dtype=float,
                   skiprows=0,
                   delimiter=' ',
                   unpack=True)
ax.scatter(x, y,
           s=25,
           c='white',
           marker='P',
           edgecolors='black',
           linewidths=1,
           label='Mix 40'
           )

x, y = np.loadtxt("./new_repar_30m/UL_40p_YH2O_planes.txt",
                   dtype=float,
                   skiprows=0,
                   delimiter=' ',
                   unpack=True)
ax.scatter(x, y,
           s=25,
           c='white',
           marker='^',
           edgecolors='black',
           linewidths=1,
           label='UL 40'
           )


# x, y = np.loadtxt("./new_repar_30m/old_YH2O_planes.txt",
#                    dtype=float,
#                    skiprows=0,
#                    delimiter=' ',
#                    unpack=True)
# ax.scatter(x, y,
#            s=25,
#            c='white',
#            marker='*',
#            edgecolors='black',
#            linewidths=1,
#            label='Old'
#            )

fig.tight_layout(pad=0.01)
ax.grid(color='lightgrey',ls='-.')
ax.legend(facecolor="white", framealpha=1, frameon=1)
# # plt.savefig('./new_repar_30m/figures/YH2O_planes.png',
# #             dpi=1200,
# #             format='png')
