import numpy as np
import matplotlib.pyplot as plt

x, y = np.loadtxt("./milena_30m/temperature_ts.txt",
                   dtype=float,
                   skiprows=0,
                   delimiter=' ',
                   unpack=True)

plt.style.use('singleColumn.mplstyle')
fig, ax = plt.subplots()
ax.set_xlabel('Time-step number')
ax.set_ylabel(r'$T$ [K]')
ax.axis([0.0, 70000, 416.75, 418.1])
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
# plt.savefig('velFluid_twoPhaseValidation.pdf',
#             format='pdf')
# plt.savefig('velFluid_twoPhaseValidation.tiff',
#             dpi=1000,
#             format='tiff')


x, y = np.loadtxt("./milena_30m/u_ts.txt",
                   dtype=float,
                   skiprows=0,
                   delimiter=' ',
                   unpack=True)

plt.style.use('singleColumn.mplstyle')
fig, ax = plt.subplots()
ax.set_xlabel('Time-step number')
ax.set_ylabel(r'$u$ [m/s]')
ax.axis([0.0, 70000, 13, 17])
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
# plt.savefig('velFluid_twoPhaseValidation.pdf',
#             format='pdf')
# plt.savefig('velFluid_twoPhaseValidation.tiff',
#             dpi=1000,
#             format='tiff')


x, y = np.loadtxt("./milena_30m/YH2O_ts.txt",
                   dtype=float,
                   skiprows=0,
                   delimiter=' ',
                   unpack=True)

plt.style.use('singleColumn.mplstyle')
fig, ax = plt.subplots()
ax.set_xlabel('Time-step number')
ax.set_ylabel(r'$Y_{H2O}$ [-]')
ax.axis([0.0, 70000, 0.19999, 0.2001])
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
# plt.savefig('velFluid_twoPhaseValidation.pdf',
#             format='pdf')
# plt.savefig('velFluid_twoPhaseValidation.tiff',
#             dpi=1000,
#             format='tiff')


x, y = np.loadtxt("./milena_30m/dpdiam_ts.txt",
                   dtype=float,
                   skiprows=0,
                   delimiter=' ',
                   unpack=True)

plt.style.use('singleColumn.mplstyle')
fig, ax = plt.subplots()
ax.set_xlabel('Time-step number')
ax.set_ylabel(r'$d_{d}$ [m]')
ax.axis([0.0, 70000, 0, 7.5e-6])
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
# plt.savefig('velFluid_twoPhaseValidation.pdf',
#             format='pdf')
# plt.savefig('velFluid_twoPhaseValidation.tiff',
#             dpi=1000,
#             format='tiff')


x, y = np.loadtxt("./milena_30m/dpmass_ts.txt",
                   dtype=float,
                   skiprows=0,
                   delimiter=' ',
                   unpack=True)

plt.style.use('singleColumn.mplstyle')
fig, ax = plt.subplots()
ax.set_xlabel('Time-step number')
ax.set_ylabel(r'$m_{d}$ [kg]')
ax.axis([0.0, 70000, 0, 5e-9])
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
# plt.savefig('velFluid_twoPhaseValidation.pdf',
#             format='pdf')
# plt.savefig('velFluid_twoPhaseValidation.tiff',
#             dpi=1000,
#             format='tiff')


x, y = np.loadtxt("./milena_30m/dpu_ts.txt",
                   dtype=float,
                   skiprows=0,
                   delimiter=' ',
                   unpack=True)

plt.style.use('singleColumn.mplstyle')
fig, ax = plt.subplots()
ax.set_xlabel('Time-step number')
ax.set_ylabel(r'$u_{d}$ [m/s]')
ax.axis([0.0, 70000, 0, 0.15])
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
# plt.savefig('velFluid_twoPhaseValidation.pdf',
#             format='pdf')
# plt.savefig('velFluid_twoPhaseValidation.tiff',
#             dpi=1000,
#             format='tiff')
