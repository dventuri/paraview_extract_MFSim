import numpy as np
import matplotlib.pyplot as plt

x, y = np.loadtxt("./milena_30m/temperature_mm.txt",
                   dtype=float,
                   skiprows=0,
                   delimiter=' ',
                   unpack=True)

plt.style.use('singleColumn.mplstyle')
fig, ax = plt.subplots()
ax.set_xlabel('Time-step number')
ax.set_ylabel(r'$T$ [K]')
ax.axis([24000, 70000, 416.75, 418.1])
ax.xaxis.set_major_locator(plt.MultipleLocator(10000))
ax.xaxis.set_minor_locator(plt.MultipleLocator(5000))
ax.yaxis.set_major_locator(plt.MultipleLocator(.25))
ax.yaxis.set_minor_locator(plt.MultipleLocator(.125))
ax.scatter(x, y,
           s=25,
           c='white',
           marker='o',
           edgecolors='black',
           linewidths='1')
fig.tight_layout(pad=0.01)
plt.savefig('./milena_30m/figures/temperature_mm.png',
            dpi=1200,
            format='png')


x, y = np.loadtxt("./milena_30m/u_mm.txt",
                   dtype=float,
                   skiprows=0,
                   delimiter=' ',
                   unpack=True)

plt.style.use('singleColumn.mplstyle')
fig, ax = plt.subplots()
ax.set_xlabel('Time-step number')
ax.set_ylabel(r'$u$ [m/s]')
ax.axis([24000, 70000, 13, 17])
ax.xaxis.set_major_locator(plt.MultipleLocator(10000))
ax.xaxis.set_minor_locator(plt.MultipleLocator(5000))
ax.yaxis.set_major_locator(plt.MultipleLocator(.5))
ax.yaxis.set_minor_locator(plt.MultipleLocator(.25))
ax.scatter(x, y,
           s=25,
           c='white',
           marker='o',
           edgecolors='black',
           linewidths='1')
fig.tight_layout(pad=0.01)
plt.savefig('./milena_30m/figures/u_mm.png',
            dpi=1200,
            format='png')


x, y = np.loadtxt("./milena_30m/YH2O_mm.txt",
                   dtype=float,
                   skiprows=0,
                   delimiter=' ',
                   unpack=True)

plt.style.use('singleColumn.mplstyle')
fig, ax = plt.subplots()
ax.set_xlabel('Time-step number')
ax.set_ylabel(r'$Y_{H2O}$ [-]')
ax.axis([24000, 70000, 0.19999, 0.2001])
ax.xaxis.set_major_locator(plt.MultipleLocator(10000))
ax.xaxis.set_minor_locator(plt.MultipleLocator(5000))
ax.yaxis.set_major_locator(plt.MultipleLocator(.00005))
ax.yaxis.set_minor_locator(plt.MultipleLocator(.000025))
ax.scatter(x, y,
           s=25,
           c='white',
           marker='o',
           edgecolors='black',
           linewidths='1')
fig.tight_layout(pad=0.01)
plt.savefig('./milena_30m/figures/YH2O_mm.png',
            dpi=1200,
            format='png')


x, y = np.loadtxt("./milena_30m/dpdiam_mm.txt",
                   dtype=float,
                   skiprows=0,
                   delimiter=' ',
                   unpack=True)

plt.style.use('singleColumn.mplstyle')
fig, ax = plt.subplots()
ax.set_xlabel('Time-step number')
ax.set_ylabel(r'$d_{d}$ [m]')
ax.axis([24000, 70000, 0, 7.5e-6])
ax.xaxis.set_major_locator(plt.MultipleLocator(10000))
ax.xaxis.set_minor_locator(plt.MultipleLocator(5000))
ax.yaxis.set_major_locator(plt.MultipleLocator(1e-6))
ax.yaxis.set_minor_locator(plt.MultipleLocator(5e-7))
ax.scatter(x, y,
           s=25,
           c='white',
           marker='o',
           edgecolors='black',
           linewidths='1')
fig.tight_layout(pad=0.01)
plt.savefig('./milena_30m/figures/dpdiam_mm.png',
            dpi=1200,
            format='png')


x, y = np.loadtxt("./milena_30m/dpmass_mm.txt",
                   dtype=float,
                   skiprows=0,
                   delimiter=' ',
                   unpack=True)

plt.style.use('singleColumn.mplstyle')
fig, ax = plt.subplots()
ax.set_xlabel('Time-step number')
ax.set_ylabel(r'$m_{d}$ [kg]')
ax.axis([24000, 70000, 0, 5e-9])
ax.xaxis.set_major_locator(plt.MultipleLocator(10000))
ax.xaxis.set_minor_locator(plt.MultipleLocator(5000))
ax.yaxis.set_major_locator(plt.MultipleLocator(1e-9))
ax.yaxis.set_minor_locator(plt.MultipleLocator(5e-10))
ax.scatter(x, y,
           s=25,
           c='white',
           marker='o',
           edgecolors='black',
           linewidths='1')
fig.tight_layout(pad=0.01)
plt.savefig('./milena_30m/figures/dpmass_mm.png',
            dpi=1200,
            format='png')


x, y = np.loadtxt("./milena_30m/dpu_mm.txt",
                   dtype=float,
                   skiprows=0,
                   delimiter=' ',
                   unpack=True)

plt.style.use('singleColumn.mplstyle')
fig, ax = plt.subplots()
ax.set_xlabel('Time-step number')
ax.set_ylabel(r'$u_{d}$ [m/s]')
ax.axis([24000, 70000, 0, 0.15])
ax.xaxis.set_major_locator(plt.MultipleLocator(10000))
ax.xaxis.set_minor_locator(plt.MultipleLocator(5000))
ax.yaxis.set_major_locator(plt.MultipleLocator(0.05))
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.025))
ax.scatter(x, y,
           s=25,
           c='white',
           marker='o',
           edgecolors='black',
           linewidths='1')
fig.tight_layout(pad=0.01)
plt.savefig('./milena_30m/figures/dpu_mm.png',
            dpi=1200,
            format='png')
