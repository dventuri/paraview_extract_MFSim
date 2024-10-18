import numpy as np
import matplotlib.pyplot as plt


values = np.loadtxt('./atomizador_repar/U_avg.txt')

zz = np.ndarray(shape=(160,160), buffer=np.array(values[:,0]))
yy = np.ndarray(shape=(160,160), buffer=np.array(values[:,1]))
plot_var = np.ndarray(shape=(160,160), buffer=np.array(values[:,2]))

circle = plt.Circle((0.5,0.5), 0.3207, color='white', fill=False, linewidth=1)
fig, ax = plt.subplots(figsize=(7.5,6))
plot = ax.pcolor(yy, zz, plot_var, edgecolors='k', linewidths=1, cmap='jet')
ax.set_title('Fluid velocity (U) [m/s]')
ax.add_patch(circle)
fig.colorbar(plot)


values = np.loadtxt('./atomizador_repar/V_avg.txt')

zz = np.ndarray(shape=(160,160), buffer=np.array(values[:,0]))
yy = np.ndarray(shape=(160,160), buffer=np.array(values[:,1]))
plot_var = np.ndarray(shape=(160,160), buffer=np.array(values[:,2]))

circle = plt.Circle((0.5,0.5), 0.3207, color='white', fill=False, linewidth=1)
fig, ax = plt.subplots(figsize=(7.5,6))
plot = ax.pcolor(yy, zz, plot_var, edgecolors='k', linewidths=1, cmap='jet')
ax.set_title('Fluid velocity (V) [m/s]')
ax.add_patch(circle)
fig.colorbar(plot)


values = np.loadtxt('./atomizador_repar/W_avg.txt')

zz = np.ndarray(shape=(160,160), buffer=np.array(values[:,0]))
yy = np.ndarray(shape=(160,160), buffer=np.array(values[:,1]))
plot_var = np.ndarray(shape=(160,160), buffer=np.array(values[:,2]))

circle = plt.Circle((0.5,0.5), 0.3207, color='white', fill=False, linewidth=1)
fig, ax = plt.subplots(figsize=(7.5,6))
plot = ax.pcolor(yy, zz, plot_var, edgecolors='k', linewidths=1, cmap='jet')
ax.set_title('Fluid velocity (W) [m/s]')
ax.add_patch(circle)
fig.colorbar(plot)


values = np.loadtxt('./atomizador_repar/T_avg.txt')

zz = np.ndarray(shape=(160,160), buffer=np.array(values[:,0]))
yy = np.ndarray(shape=(160,160), buffer=np.array(values[:,1]))
plot_var = np.ndarray(shape=(160,160), buffer=np.array(values[:,2]))

circle = plt.Circle((0.5,0.5), 0.3207, color='white', fill=False, linewidth=1)
incircle = plt.Circle((0.5,0.5), 0.05, color='gray', fill=False, linewidth=1)
fig, ax = plt.subplots(figsize=(7.5,6))
plot = ax.pcolor(yy, zz, plot_var, edgecolors='k', linewidths=1, cmap='jet')
ax.set_title('Fluid avg. temperature [K]')
ax.add_patch(circle)
ax.add_patch(incircle)
fig.colorbar(plot)


values = np.loadtxt('./atomizador_repar/T_std.txt')

zz = np.ndarray(shape=(160,160), buffer=np.array(values[:,0]))
yy = np.ndarray(shape=(160,160), buffer=np.array(values[:,1]))
plot_var = np.ndarray(shape=(160,160), buffer=np.array(values[:,2]))

circle = plt.Circle((0.5,0.5), 0.3207, color='white', fill=False, linewidth=1)
incircle = plt.Circle((0.5,0.5), 0.05, color='gray', fill=False, linewidth=1)
fig, ax = plt.subplots(figsize=(7.5,6))
plot = ax.pcolor(yy, zz, plot_var, edgecolors='k', linewidths=1, cmap='jet')
ax.set_title('Fluid std. temperature [K]')
ax.add_patch(circle)
ax.add_patch(incircle)
fig.colorbar(plot)


values = np.loadtxt('./atomizador_repar/dpm_diam_avg.txt')

zz = np.ndarray(shape=(160,160), buffer=np.array(values[:,0]))
yy = np.ndarray(shape=(160,160), buffer=np.array(values[:,1]))
plot_var = np.ndarray(shape=(160,160), buffer=np.array(values[:,2]))

circle = plt.Circle((0.5,0.5), 0.3207, color='white', fill=False, linewidth=1)
fig, ax = plt.subplots(figsize=(7.5,6))
plot = ax.pcolor(yy, zz, plot_var, edgecolors='k', linewidths=1, cmap='jet')
ax.set_title('Droplet avg. diameter [m]')
ax.add_patch(circle)
fig.colorbar(plot)


values = np.loadtxt('./atomizador_repar/dpm_diam_std.txt')

zz = np.ndarray(shape=(160,160), buffer=np.array(values[:,0]))
yy = np.ndarray(shape=(160,160), buffer=np.array(values[:,1]))
plot_var = np.ndarray(shape=(160,160), buffer=np.array(values[:,2]))

circle = plt.Circle((0.5,0.5), 0.3207, color='white', fill=False, linewidth=1)
fig, ax = plt.subplots(figsize=(7.5,6))
plot = ax.pcolor(yy, zz, plot_var, edgecolors='k', linewidths=1, cmap='jet')
ax.set_title('Droplet std. diameter [m]')
ax.add_patch(circle)
fig.colorbar(plot)


values = np.loadtxt('./atomizador_repar/dpm_temp_avg.txt')

zz = np.ndarray(shape=(160,160), buffer=np.array(values[:,0]))
yy = np.ndarray(shape=(160,160), buffer=np.array(values[:,1]))
plot_var = np.ndarray(shape=(160,160), buffer=np.array(values[:,2]))

circle = plt.Circle((0.5,0.5), 0.3207, color='white', fill=False, linewidth=1)
fig, ax = plt.subplots(figsize=(7.5,6))
plot = ax.pcolor(yy, zz, plot_var, edgecolors='k', linewidths=1, cmap='jet')
ax.set_title('Droplet avg. temperature [K]')
ax.add_patch(circle)
fig.colorbar(plot)


values = np.loadtxt('./atomizador_repar/dpm_temp_std.txt')

zz = np.ndarray(shape=(160,160), buffer=np.array(values[:,0]))
yy = np.ndarray(shape=(160,160), buffer=np.array(values[:,1]))
plot_var = np.ndarray(shape=(160,160), buffer=np.array(values[:,2]))

circle = plt.Circle((0.5,0.5), 0.3207, color='white', fill=False, linewidth=1)
fig, ax = plt.subplots(figsize=(7.5,6))
plot = ax.pcolor(yy, zz, plot_var, edgecolors='k', linewidths=1, cmap='jet')
ax.set_title('Droplet std. temperature [K]')
ax.add_patch(circle)
fig.colorbar(plot)


values = np.loadtxt('./atomizador_repar/dpm_u_avg.txt')

zz = np.ndarray(shape=(160,160), buffer=np.array(values[:,0]))
yy = np.ndarray(shape=(160,160), buffer=np.array(values[:,1]))
plot_var = np.ndarray(shape=(160,160), buffer=np.array(values[:,2]))

circle = plt.Circle((0.5,0.5), 0.3207, color='white', fill=False, linewidth=1)
fig, ax = plt.subplots(figsize=(7.5,6))
plot = ax.pcolor(yy, zz, plot_var, edgecolors='k', linewidths=1, cmap='jet')
ax.set_title('Droplet avg. velocity (U) [m/s]')
ax.add_patch(circle)
fig.colorbar(plot)


values = np.loadtxt('./atomizador_repar/dpm_u_std.txt')

zz = np.ndarray(shape=(160,160), buffer=np.array(values[:,0]))
yy = np.ndarray(shape=(160,160), buffer=np.array(values[:,1]))
plot_var = np.ndarray(shape=(160,160), buffer=np.array(values[:,2]))

circle = plt.Circle((0.5,0.5), 0.3207, color='white', fill=False, linewidth=1)
fig, ax = plt.subplots(figsize=(7.5,6))
plot = ax.pcolor(yy, zz, plot_var, edgecolors='k', linewidths=1, cmap='jet')
ax.set_title('Droplet std. velocity (U) [m/s]')
ax.add_patch(circle)
fig.colorbar(plot)


values = np.loadtxt('./atomizador_repar/dpm_v_avg.txt')

zz = np.ndarray(shape=(160,160), buffer=np.array(values[:,0]))
yy = np.ndarray(shape=(160,160), buffer=np.array(values[:,1]))
plot_var = np.ndarray(shape=(160,160), buffer=np.array(values[:,2]))

circle = plt.Circle((0.5,0.5), 0.3207, color='white', fill=False, linewidth=1)
fig, ax = plt.subplots(figsize=(7.5,6))
plot = ax.pcolor(yy, zz, plot_var, edgecolors='k', linewidths=1, cmap='jet')
ax.set_title('Droplet avg. velocity (V) [m/s]')
ax.add_patch(circle)
fig.colorbar(plot)


values = np.loadtxt('./atomizador_repar/dpm_v_std.txt')

zz = np.ndarray(shape=(160,160), buffer=np.array(values[:,0]))
yy = np.ndarray(shape=(160,160), buffer=np.array(values[:,1]))
plot_var = np.ndarray(shape=(160,160), buffer=np.array(values[:,2]))

circle = plt.Circle((0.5,0.5), 0.3207, color='white', fill=False, linewidth=1)
fig, ax = plt.subplots(figsize=(7.5,6))
plot = ax.pcolor(yy, zz, plot_var, edgecolors='k', linewidths=1, cmap='jet')
ax.set_title('Droplet std. velocity (V) [m/s]')
ax.add_patch(circle)
fig.colorbar(plot)


values = np.loadtxt('./atomizador_repar/dpm_w_avg.txt')

zz = np.ndarray(shape=(160,160), buffer=np.array(values[:,0]))
yy = np.ndarray(shape=(160,160), buffer=np.array(values[:,1]))
plot_var = np.ndarray(shape=(160,160), buffer=np.array(values[:,2]))

circle = plt.Circle((0.5,0.5), 0.3207, color='white', fill=False, linewidth=1)
fig, ax = plt.subplots(figsize=(7.5,6))
plot = ax.pcolor(yy, zz, plot_var, edgecolors='k', linewidths=1, cmap='jet')
ax.set_title('Droplet avg. velocity (W) [m/s]')
ax.add_patch(circle)
fig.colorbar(plot)


values = np.loadtxt('./atomizador_repar/dpm_w_std.txt')

zz = np.ndarray(shape=(160,160), buffer=np.array(values[:,0]))
yy = np.ndarray(shape=(160,160), buffer=np.array(values[:,1]))
plot_var = np.ndarray(shape=(160,160), buffer=np.array(values[:,2]))

circle = plt.Circle((0.5,0.5), 0.3207, color='white', fill=False, linewidth=1)
fig, ax = plt.subplots(figsize=(7.5,6))
plot = ax.pcolor(yy, zz, plot_var, edgecolors='k', linewidths=1, cmap='jet')
ax.set_title('Droplet std. velocity (W) [m/s]')
ax.add_patch(circle)
fig.colorbar(plot)


values = np.loadtxt('./atomizador_repar/vazao.txt')

zz = np.ndarray(shape=(160,160), buffer=np.array(values[:,0]))
yy = np.ndarray(shape=(160,160), buffer=np.array(values[:,1]))
plot_var = np.ndarray(shape=(160,160), buffer=np.array(values[:,2]))

circle = plt.Circle((0.5,0.5), 0.3207, color='white', fill=False, linewidth=1)
incircle = plt.Circle((0.5,0.5), 0.06, color='gray', fill=False, linewidth=1)
fig, ax = plt.subplots(figsize=(7.5,6))
plot = ax.pcolor(yy, zz, plot_var, edgecolors='k', linewidths=1, cmap='jet')
ax.set_title('Droplet mass flow [-]')
ax.add_patch(circle)
ax.add_patch(incircle)
fig.colorbar(plot)
