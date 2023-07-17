import numpy as np
import matplotlib.pyplot as plt

x, y = np.loadtxt("./milena_30m/temperature_planes.txt",
                   dtype=float,
                   skiprows=0,
                   delimiter=' ',
                   unpack=True)

plt.style.use('singleColumn.mplstyle')
fig, ax = plt.subplots()
ax.set_xlabel(r'$x$ [m]')
ax.set_ylabel(r'$T$ [K]')
ax.axis([0, 30, 416.75, 417.75])
ax.xaxis.set_major_locator(plt.MultipleLocator(5))
ax.xaxis.set_minor_locator(plt.MultipleLocator(2.5))
ax.yaxis.set_major_locator(plt.MultipleLocator(.25))
ax.yaxis.set_minor_locator(plt.MultipleLocator(.125))
ax.scatter(x, y,
           s=25,
           c='white',
           marker='o',
           edgecolors='black',
           linewidths='1')
fig.tight_layout(pad=0.01)
plt.savefig('./milena_30m/figures/temperature_planes.png',
            dpi=1200,
            format='png')


x, y = np.loadtxt("./milena_30m/u_planes.txt",
                   dtype=float,
                   skiprows=0,
                   delimiter=' ',
                   unpack=True)

plt.style.use('singleColumn.mplstyle')
fig, ax = plt.subplots()
ax.set_xlabel(r'$x$ [m]')
ax.set_ylabel(r'$u$ [m/s]')
ax.axis([0, 30, 13, 17])
ax.xaxis.set_major_locator(plt.MultipleLocator(5))
ax.xaxis.set_minor_locator(plt.MultipleLocator(2.5))
ax.yaxis.set_major_locator(plt.MultipleLocator(.5))
ax.yaxis.set_minor_locator(plt.MultipleLocator(.25))
ax.scatter(x, y,
           s=25,
           c='white',
           marker='o',
           edgecolors='black',
           linewidths='1')
fig.tight_layout(pad=0.01)
plt.savefig('./milena_30m/figures/u_planes.png',
            dpi=1200,
            format='png')


x, y = np.loadtxt("./milena_30m/YH2O_planes.txt",
                   dtype=float,
                   skiprows=0,
                   delimiter=' ',
                   unpack=True)

plt.style.use('singleColumn.mplstyle')
fig, ax = plt.subplots()
ax.set_xlabel(r'$x$ [m]')
ax.set_ylabel(r'$Y_{H2O}$ [-]')
ax.axis([0, 30, 0.19985, 0.2001])
ax.xaxis.set_major_locator(plt.MultipleLocator(5))
ax.xaxis.set_minor_locator(plt.MultipleLocator(2.5))
ax.yaxis.set_major_locator(plt.MultipleLocator(.00010))
ax.yaxis.set_minor_locator(plt.MultipleLocator(.000025))
ax.scatter(x, y,
           s=25,
           c='white',
           marker='o',
           edgecolors='black',
           linewidths='1')
ax.hlines(0.2, 0, 30,
          colors='grey',
          linestyles='--')
fig.tight_layout(pad=0.01)
plt.savefig('./milena_30m/figures/YH2O_planes.png',
            dpi=1200,
            format='png')


x, y = np.loadtxt("./milena_30m/dpdiam_planes.txt",
                   dtype=float,
                   skiprows=0,
                   delimiter=' ',
                   unpack=True)

plt.style.use('singleColumn.mplstyle')
fig, ax = plt.subplots()
ax.set_xlabel(r'$x$ [m]')
ax.set_ylabel(r'$d_{d}$ [m]')
ax.axis([0, 30, 0, 5.2e-5])
ax.xaxis.set_major_locator(plt.MultipleLocator(5))
ax.xaxis.set_minor_locator(plt.MultipleLocator(2.5))
ax.yaxis.set_major_locator(plt.MultipleLocator(1e-5))
ax.yaxis.set_minor_locator(plt.MultipleLocator(5e-6))
ax.scatter(x, y,
           s=25,
           c='white',
           marker='o',
           edgecolors='black',
           linewidths='1')
fig.tight_layout(pad=0.01)
plt.savefig('./milena_30m/figures/dpdiam_planes.png',
            dpi=1200,
            format='png')

plt.style.use('singleColumn.mplstyle')
fig, ax = plt.subplots()
ax.set_xlabel(r'$x$ [m]')
ax.set_ylabel(r'$d_{d}$ [m]')
ax.axis([0, 30, 1e-6, 1.e-4])
ax.xaxis.set_major_locator(plt.MultipleLocator(5))
ax.xaxis.set_minor_locator(plt.MultipleLocator(2.5))
ax.scatter(x, y,
           s=25,
           c='white',
           marker='o',
           edgecolors='black',
           linewidths='1')
ax.set_yscale("log")
fig.tight_layout(pad=0.01)
plt.savefig('./milena_30m/figures/dpdiam_log_planes.png',
            dpi=1200,
            format='png')


x, y = np.loadtxt("./milena_30m/dpmass_planes.txt",
                   dtype=float,
                   skiprows=0,
                   delimiter=' ',
                   unpack=True)

plt.style.use('singleColumn.mplstyle')
fig, ax = plt.subplots()
ax.set_xlabel(r'$x$ [m]')
ax.set_ylabel(r'$m_{d}$ [kg]')
ax.axis([0, 30, 0, 3.5e-8])
ax.xaxis.set_major_locator(plt.MultipleLocator(5))
ax.xaxis.set_minor_locator(plt.MultipleLocator(2.5))
ax.yaxis.set_major_locator(plt.MultipleLocator(0.5e-8))
ax.yaxis.set_minor_locator(plt.MultipleLocator(5e-9))
ax.scatter(x, y,
           s=25,
           c='white',
           marker='o',
           edgecolors='black',
           linewidths='1')
fig.tight_layout(pad=0.01)
plt.savefig('./milena_30m/figures/dpmass_planes.png',
            dpi=1200,
            format='png')

plt.style.use('singleColumn.mplstyle')
fig, ax = plt.subplots()
ax.set_xlabel(r'$x$ [m]')
ax.set_ylabel(r'$m_{d}$ [kg]')
ax.axis([0, 30, 1e-9, 5e-8])
ax.xaxis.set_major_locator(plt.MultipleLocator(5))
ax.xaxis.set_minor_locator(plt.MultipleLocator(2.5))
ax.scatter(x, y,
           s=25,
           c='white',
           marker='o',
           edgecolors='black',
           linewidths='1')
ax.set_yscale("log")
fig.tight_layout(pad=0.01)
plt.savefig('./milena_30m/figures/dpmass_log_planes.png',
            dpi=1200,
            format='png')


x, y = np.loadtxt("./milena_30m/dpu_planes.txt",
                   dtype=float,
                   skiprows=0,
                   delimiter=' ',
                   unpack=True)

plt.style.use('singleColumn.mplstyle')
fig, ax = plt.subplots()
ax.set_xlabel(r'$x$ [m]')
ax.set_ylabel(r'$u_{d}$ [m/s]')
ax.axis([0, 30, 0, 1])
ax.xaxis.set_major_locator(plt.MultipleLocator(5))
ax.xaxis.set_minor_locator(plt.MultipleLocator(2.5))
ax.yaxis.set_major_locator(plt.MultipleLocator(0.2))
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.05))
ax.scatter(x, y,
           s=25,
           c='white',
           marker='o',
           edgecolors='black',
           linewidths='1')
fig.tight_layout(pad=0.01)
plt.savefig('./milena_30m/figures/dpu_planes.png',
            dpi=1200,
            format='png')
