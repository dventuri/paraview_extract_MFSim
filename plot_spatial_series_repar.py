import numpy as np
import matplotlib.pyplot as plt

import locale
locale.setlocale(locale.LC_NUMERIC, "pt_BR.UTF-8")

plt.rcdefaults()
plt.rcParams['axes.formatter.use_locale'] = True


x, y = np.loadtxt("./repar_keps/repar_temperature_planes.txt",
                   dtype=float,
                   skiprows=0,
                   delimiter=' ',
                   unpack=True)

# plt.style.use('singleColumn.mplstyle')
fig, ax = plt.subplots()
ax.set_xlabel('Comprimento [m]')
ax.set_ylabel('Temperatura do gás [°C]')
ax.axis([0, 16, 130, 145])
ax.xaxis.set_major_locator(plt.MultipleLocator(2))
ax.xaxis.set_minor_locator(plt.MultipleLocator(1))
ax.yaxis.set_major_locator(plt.MultipleLocator(1))
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.5))
ax.plot(x, y-273.15,
        c='black',
        ls='-',
        linewidth=1)#,
        # label='Caso padrão')
fig.tight_layout(pad=0.01)
ax.grid(color='lightgrey',ls='-.')
# ax.legend(facecolor="white", framealpha=1, frameon=1)
plt.savefig('./repar_keps/temperature_planes.png',
            dpi=1200,
            format='png')


x, y = np.loadtxt("./repar_keps/repar_u_planes.txt",
                   dtype=float,
                   skiprows=0,
                   delimiter=' ',
                   unpack=True)

# plt.style.use('singleColumn.mplstyle')
fig, ax = plt.subplots()
ax.set_xlabel(r'$x$ [m]')
ax.set_ylabel(r'$U$ [m/s]')
ax.axis([0, 16, 18, 22])
ax.xaxis.set_major_locator(plt.MultipleLocator(2))
ax.xaxis.set_minor_locator(plt.MultipleLocator(1))
ax.yaxis.set_major_locator(plt.MultipleLocator(0.5))
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.25))
ax.plot(x, y,
        c='black',
        ls='-',
        linewidth=1)#,
        # label='Caso padrão')
fig.tight_layout(pad=0.01)
ax.grid(color='lightgrey',ls='-.')
# ax.legend(facecolor="white", framealpha=1, frameon=1)
plt.savefig('./repar_keps/u_planes.png',
            dpi=1200,
            format='png')


x, y = np.loadtxt("./repar_keps/repar_YH2O_planes.txt",
                   dtype=float,
                   skiprows=0,
                   delimiter=' ',
                   unpack=True)

# plt.style.use('singleColumn.mplstyle')
fig, ax = plt.subplots()
ax.set_xlabel('Comprimento [m]')
ax.set_ylabel("Fração mássica de vapor d'água no gás [%]")
ax.axis([0, 16, 17, 20])
ax.xaxis.set_major_locator(plt.MultipleLocator(2))
ax.xaxis.set_minor_locator(plt.MultipleLocator(1))
ax.yaxis.set_major_locator(plt.MultipleLocator(0.5))
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.25))
ax.plot(x, y*100,
        c='black',
        ls='-',
        linewidth=1)#,
        # label='Caso padrão')
fig.tight_layout(pad=0.01)
ax.grid(color='lightgrey',ls='-.')
# ax.legend(facecolor="white", framealpha=1, frameon=1)
plt.savefig('./repar_keps/YH2O_planes.png',
            dpi=1200,
            format='png')


x, y = np.loadtxt("./repar_keps/repar_rho_planes.txt",
                   dtype=float,
                   skiprows=0,
                   delimiter=' ',
                   unpack=True)

# plt.style.use('singleColumn.mplstyle')
fig, ax = plt.subplots()
ax.set_xlabel(r'$x$ [m]')
ax.set_ylabel('Massa específica do gás [kg/m3]')
ax.axis([0, 16, 2.0, 3.125])
ax.xaxis.set_major_locator(plt.MultipleLocator(2))
ax.xaxis.set_minor_locator(plt.MultipleLocator(1))
ax.yaxis.set_major_locator(plt.MultipleLocator(0.1))
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.05))
ax.plot(x, y,
        c='black',
        ls='-',
        linewidth=1)#,
        # label='Caso padrão')
fig.tight_layout(pad=0.01)
ax.grid(color='lightgrey',ls='-.')
# ax.legend(facecolor="white", framealpha=1, frameon=1)
plt.savefig('./repar_keps/rho_planes.png',
            dpi=1200,
            format='png')
