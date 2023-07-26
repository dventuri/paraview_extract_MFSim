import numpy as np
import matplotlib.pyplot as plt

# Droplets diameter
values = np.loadtxt('./milena_30m/dpdiam_avg.txt')

yy = np.ndarray(shape=(81,81), buffer=np.array(values[:,0]))
zz = np.ndarray(shape=(81,81), buffer=np.array(values[:,1]))
plot_var = np.ndarray(shape=(81,81), buffer=np.array(values[:,2]))

circle = plt.Circle((0.5,0.5), 0.3207, color='white', fill=False, linewidth=1)
fig, ax = plt.subplots(figsize=(7.5,6))
plot = ax.pcolor(yy, zz, plot_var, edgecolors='k', linewidths=1)
ax.set_title('Droplets diameter (m)')
ax.add_patch(circle)
fig.colorbar(plot)

plt.savefig('./milena_30m/figures/dpdiam_avg.png',
            dpi=300,
            format='png')


# Gas temperature
values = np.loadtxt('./milena_30m/temperature_avg.txt')

yy = np.ndarray(shape=(81,81), buffer=np.array(values[:,0]))
zz = np.ndarray(shape=(81,81), buffer=np.array(values[:,1]))
plot_var = np.ndarray(shape=(81,81), buffer=np.array(values[:,2]))

circle = plt.Circle((0.5,0.5), 0.3207, color='white', fill=False, linewidth=1)
fig, ax = plt.subplots(figsize=(7.5,6))
plot = ax.pcolor(yy, zz, plot_var, edgecolors='k', linewidths=1)
ax.set_title('Gas temperature (K)')
ax.add_patch(circle)
fig.colorbar(plot)

plt.savefig('./milena_30m/figures/temperature_avg.png',
            dpi=300,
            format='png')


# Gas vapor fraction
values = np.loadtxt('./milena_30m/ykH2O_avg.txt')

yy = np.ndarray(shape=(81,81), buffer=np.array(values[:,0]))
zz = np.ndarray(shape=(81,81), buffer=np.array(values[:,1]))
plot_var = np.ndarray(shape=(81,81), buffer=np.array(values[:,2]))

circle = plt.Circle((0.5,0.5), 0.3207, color='white', fill=False, linewidth=1)
fig, ax = plt.subplots(figsize=(7.5,6))
plot = ax.pcolor(yy, zz, plot_var, edgecolors='k', linewidths=1)
ax.set_title('Gas H2O mass fraction')
ax.add_patch(circle)
fig.colorbar(plot)

plt.savefig('./milena_30m/figures/ykH2O_avg.png',
            dpi=300,
            format='png')


# Gas density
values = np.loadtxt('./milena_30m/rho_avg.txt')

yy = np.ndarray(shape=(81,81), buffer=np.array(values[:,0]))
zz = np.ndarray(shape=(81,81), buffer=np.array(values[:,1]))
plot_var = np.ndarray(shape=(81,81), buffer=np.array(values[:,2]))

circle = plt.Circle((0.5,0.5), 0.3207, color='white', fill=False, linewidth=1)
fig, ax = plt.subplots(figsize=(7.5,6))
plot = ax.pcolor(yy, zz, plot_var, edgecolors='k', linewidths=1)
ax.set_title('Gas density (kg/m³)')
ax.add_patch(circle)
fig.colorbar(plot)

plt.savefig('./milena_30m/figures/rho_avg.png',
            dpi=300,
            format='png')


# Gas velocity
values = np.loadtxt('./milena_30m/u_avg.txt')

yy = np.ndarray(shape=(81,81), buffer=np.array(values[:,0]))
zz = np.ndarray(shape=(81,81), buffer=np.array(values[:,1]))
plot_var = np.ndarray(shape=(81,81), buffer=np.array(values[:,2]))

circle = plt.Circle((0.5,0.5), 0.3207, color='white', fill=False, linewidth=1)
fig, ax = plt.subplots(figsize=(7.5,6))
plot = ax.pcolor(yy, zz, plot_var, edgecolors='k', linewidths=1)
ax.set_title('Gas axial velocity (m/s)')
ax.add_patch(circle)
fig.colorbar(plot)

plt.savefig('./milena_30m/figures/u_avg.png',
            dpi=300,
            format='png')


# Droplets velocity
values = np.loadtxt('./milena_30m/dpvel_avg.txt')

yy = np.ndarray(shape=(81,81), buffer=np.array(values[:,0]))
zz = np.ndarray(shape=(81,81), buffer=np.array(values[:,1]))
plot_var = np.ndarray(shape=(81,81), buffer=np.array(values[:,2]))

circle = plt.Circle((0.5,0.5), 0.3207, color='white', fill=False, linewidth=1)
fig, ax = plt.subplots(figsize=(7.5,6))
plot = ax.pcolor(yy, zz, plot_var, edgecolors='k', linewidths=1)
ax.set_title('Droplets axial velocity (m/s)')
ax.add_patch(circle)
fig.colorbar(plot)

plt.savefig('./milena_30m/figures/dpvel_avg.png',
            dpi=300,
            format='png')
