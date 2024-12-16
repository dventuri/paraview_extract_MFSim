import numpy as np
import matplotlib.pyplot as plt

import locale
locale.setlocale(locale.LC_NUMERIC, "pt_BR.UTF-8")

plt.rcdefaults()
plt.rcParams['axes.formatter.use_locale'] = True


x, y = np.loadtxt("./repar_30m_keps_np10_coll_coal_ssd_atmz/repar_temperature_planes.txt",
                   dtype=float,
                   skiprows=0,
                   delimiter=' ',
                   unpack=True)

# plt.style.use('singleColumn.mplstyle')
fig, ax = plt.subplots()
ax.set_xlabel('Comprimento [m]')
ax.set_ylabel('Temperatura do gás [°C]')
ax.axis([0, 30, 136, 146])
ax.xaxis.set_major_locator(plt.MultipleLocator(3))
ax.xaxis.set_minor_locator(plt.MultipleLocator(1.5))
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
plt.savefig('./repar_30m_keps_np10_coll_coal_ssd_atmz/temperature_planes.png',
            dpi=1200,
            format='png')


x, y = np.loadtxt("./repar_30m_keps_np10_coll_coal_ssd_atmz/repar_u_planes.txt",
                   dtype=float,
                   skiprows=0,
                   delimiter=' ',
                   unpack=True)

# plt.style.use('singleColumn.mplstyle')
fig, ax = plt.subplots()
ax.set_xlabel(r'$x$ [m]')
ax.set_ylabel(r'$U$ [m/s]')
ax.axis([0, 30, 16, 18])
ax.xaxis.set_major_locator(plt.MultipleLocator(3))
ax.xaxis.set_minor_locator(plt.MultipleLocator(1.5))
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
plt.savefig('./repar_30m_keps_np10_coll_coal_ssd_atmz/u_planes.png',
            dpi=1200,
            format='png')


x, y = np.loadtxt("./repar_30m_keps_np10_coll_coal_ssd_atmz/repar_YH2O_planes.txt",
                   dtype=float,
                   skiprows=0,
                   delimiter=' ',
                   unpack=True)

# plt.style.use('singleColumn.mplstyle')
fig, ax = plt.subplots()
ax.set_xlabel('Comprimento [m]')
ax.set_ylabel("Fração mássica de vapor d'água no gás [%]")
ax.axis([0, 30, 17, 20])
ax.xaxis.set_major_locator(plt.MultipleLocator(3))
ax.xaxis.set_minor_locator(plt.MultipleLocator(1.5))
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
plt.savefig('./repar_30m_keps_np10_coll_coal_ssd_atmz/YH2O_planes.png',
            dpi=1200,
            format='png')


x, y = np.loadtxt("./repar_30m_keps_np10_coll_coal_ssd_atmz/repar_rho_planes.txt",
                   dtype=float,
                   skiprows=0,
                   delimiter=' ',
                   unpack=True)

# plt.style.use('singleColumn.mplstyle')
fig, ax = plt.subplots()
ax.set_xlabel(r'$x$ [m]')
ax.set_ylabel('Massa específica do gás [kg/m3]')
ax.axis([0, 30, 2.0, 3.125])
ax.xaxis.set_major_locator(plt.MultipleLocator(3))
ax.xaxis.set_minor_locator(plt.MultipleLocator(1.5))
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
plt.savefig('./repar_30m_keps_np10_coll_coal_ssd_atmz/rho_planes.png',
            dpi=1200,
            format='png')
