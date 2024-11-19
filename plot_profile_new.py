import numpy as np
import matplotlib.pyplot as plt

import locale
locale.setlocale(locale.LC_NUMERIC, "pt_BR.UTF-8")

plt.rcdefaults()
plt.rcParams['axes.formatter.use_locale'] = True


values = np.loadtxt('./atomizador_repar/vel_avg.txt')

zz = np.ndarray(shape=(160,160), buffer=np.array(values[:,0]))
yy = np.ndarray(shape=(160,160), buffer=np.array(values[:,1]))
plot_var = np.ndarray(shape=(160,160), buffer=np.array(values[:,2]))

circle = plt.Circle((0.5,0.5), 0.3207, color='white', fill=False, linewidth=1)
fig, ax = plt.subplots(figsize=(7.5,6))
plot = ax.pcolor(yy, zz, plot_var, edgecolors='k', linewidths=1, cmap='jet')
ax.set_title('Velocidade U do gás [m/s]')
ax.add_patch(circle)
fig.colorbar(plot)
plt.savefig('./atomizador_repar/U_gas.png',
            dpi=1200,
            format='png')


values = np.loadtxt('./atomizador_repar/vel_avg.txt')

zz = np.ndarray(shape=(160,160), buffer=np.array(values[:,0]))
yy = np.ndarray(shape=(160,160), buffer=np.array(values[:,1]))
plot_var = np.ndarray(shape=(160,160), buffer=np.array(values[:,3]))

circle = plt.Circle((0.5,0.5), 0.3207, color='white', fill=False, linewidth=1)
fig, ax = plt.subplots(figsize=(7.5,6))
plot = ax.pcolor(yy, zz, plot_var, edgecolors='k', linewidths=1, cmap='jet')
ax.set_title('Velocidade V do gás [m/s]')
ax.add_patch(circle)
fig.colorbar(plot)
plt.savefig('./atomizador_repar/V_gas.png',
            dpi=1200,
            format='png')


values = np.loadtxt('./atomizador_repar/vel_avg.txt')

zz = np.ndarray(shape=(160,160), buffer=np.array(values[:,0]))
yy = np.ndarray(shape=(160,160), buffer=np.array(values[:,1]))
plot_var = np.ndarray(shape=(160,160), buffer=np.array(values[:,4]))

circle = plt.Circle((0.5,0.5), 0.3207, color='white', fill=False, linewidth=1)
fig, ax = plt.subplots(figsize=(7.5,6))
plot = ax.pcolor(yy, zz, plot_var, edgecolors='k', linewidths=1, cmap='jet')
ax.set_title('Velocidade W do gás [m/s]')
ax.add_patch(circle)
fig.colorbar(plot)
plt.savefig('./atomizador_repar/W_gas.png',
            dpi=1200,
            format='png')


values = np.loadtxt('./atomizador_repar/T_avg.txt')

zz = np.ndarray(shape=(160,160), buffer=np.array(values[:,0]))
yy = np.ndarray(shape=(160,160), buffer=np.array(values[:,1]))
plot_var = np.ndarray(shape=(160,160), buffer=np.array(values[:,2]))-273.15

circle = plt.Circle((0.5,0.5), 0.3207, color='white', fill=False, linewidth=1)
incircle = plt.Circle((0.5,0.5), 0.05, color='gray', fill=False, linewidth=1)
fig, ax = plt.subplots(figsize=(7.5,6))
plot = ax.pcolor(yy, zz, plot_var, edgecolors='k', linewidths=1, cmap='jet')
ax.set_title('Temperatura média do gás [°C]')
ax.add_patch(circle)
# ax.add_patch(incircle)
fig.colorbar(plot)
plt.savefig('./atomizador_repar/T_gas.png',
            dpi=1200,
            format='png')


values = np.loadtxt('./atomizador_repar/T_std.txt')

zz = np.ndarray(shape=(160,160), buffer=np.array(values[:,0]))
yy = np.ndarray(shape=(160,160), buffer=np.array(values[:,1]))
plot_var = np.ndarray(shape=(160,160), buffer=np.array(values[:,2]))

circle = plt.Circle((0.5,0.5), 0.3207, color='white', fill=False, linewidth=1)
incircle = plt.Circle((0.5,0.5), 0.05, color='gray', fill=False, linewidth=1)
fig, ax = plt.subplots(figsize=(7.5,6))
plot = ax.pcolor(yy, zz, plot_var, edgecolors='k', linewidths=1, cmap='jet')
ax.set_title('Desvio padrão da temperatura do gás [°C]')
ax.add_patch(circle)
# ax.add_patch(incircle)
fig.colorbar(plot)
plt.savefig('./atomizador_repar/T-std_gas.png',
            dpi=1200,
            format='png')


values = np.loadtxt('./atomizador_repar/dpm_diam_avg.txt')

zz = np.ndarray(shape=(160,160), buffer=np.array(values[:,0]))
yy = np.ndarray(shape=(160,160), buffer=np.array(values[:,1]))
plot_var = np.ndarray(shape=(160,160), buffer=np.array(values[:,2]))*1000

circle = plt.Circle((0.5,0.5), 0.3207, color='white', fill=False, linewidth=1)
fig, ax = plt.subplots(figsize=(7.5,6))
plot = ax.pcolor(yy, zz, plot_var, edgecolors='k', linewidths=1, cmap='jet')
ax.set_title('Diâmetro médio das gotas [mm]')
ax.add_patch(circle)
fig.colorbar(plot)
plt.savefig('./atomizador_repar/dpm_diam.png',
            dpi=1200,
            format='png')


values = np.loadtxt('./atomizador_repar/dpm_diam_std.txt')

zz = np.ndarray(shape=(160,160), buffer=np.array(values[:,0]))
yy = np.ndarray(shape=(160,160), buffer=np.array(values[:,1]))
plot_var = np.ndarray(shape=(160,160), buffer=np.array(values[:,2]))*1000

circle = plt.Circle((0.5,0.5), 0.3207, color='white', fill=False, linewidth=1)
fig, ax = plt.subplots(figsize=(7.5,6))
plot = ax.pcolor(yy, zz, plot_var, edgecolors='k', linewidths=1, cmap='jet')
ax.set_title('Desvio padrão do diâmetro [mm]')
ax.add_patch(circle)
fig.colorbar(plot)
plt.savefig('./atomizador_repar/dpm_diam-std.png',
            dpi=1200,
            format='png')


values = np.loadtxt('./atomizador_repar/dpm_temp.txt')

zz = np.ndarray(shape=(160,160), buffer=np.array(values[:,0]))
yy = np.ndarray(shape=(160,160), buffer=np.array(values[:,1]))
plot_var = np.ndarray(shape=(160,160), buffer=np.array(values[:,2]))-273.15

circle = plt.Circle((0.5,0.5), 0.3207, color='white', fill=False, linewidth=1)
fig, ax = plt.subplots(figsize=(7.5,6))
plot = ax.pcolor(yy, zz, plot_var, edgecolors='k', linewidths=1, cmap='jet')
ax.set_title('Temperatura média das gotas [°C]')
ax.add_patch(circle)
fig.colorbar(plot)
plt.savefig('./atomizador_repar/dpm_temp.png',
            dpi=1200,
            format='png')


values = np.loadtxt('./atomizador_repar/dpm_temp.txt')

zz = np.ndarray(shape=(160,160), buffer=np.array(values[:,0]))
yy = np.ndarray(shape=(160,160), buffer=np.array(values[:,1]))
plot_var = np.ndarray(shape=(160,160), buffer=np.array(values[:,3]))-273.15

circle = plt.Circle((0.5,0.5), 0.3207, color='white', fill=False, linewidth=1)
fig, ax = plt.subplots(figsize=(7.5,6))
plot = ax.pcolor(yy, zz, plot_var, edgecolors='k', linewidths=1, cmap='jet')
ax.set_title('Desvio padrão da temperatura das gotas [°C]')
ax.add_patch(circle)
fig.colorbar(plot)
plt.savefig('./atomizador_repar/dpm_temp-std.png',
            dpi=1200,
            format='png')


values = np.loadtxt('./atomizador_repar/dpm_vel.txt')

zz = np.ndarray(shape=(160,160), buffer=np.array(values[:,0]))
yy = np.ndarray(shape=(160,160), buffer=np.array(values[:,1]))
plot_var = np.ndarray(shape=(160,160), buffer=np.array(values[:,2]))

circle = plt.Circle((0.5,0.5), 0.3207, color='white', fill=False, linewidth=1)
incircle = plt.Circle((0.5,0.5), 0.07, color='gray', fill=False, linewidth=1)
fig, ax = plt.subplots(figsize=(7.5,6))
plot = ax.pcolor(yy, zz, plot_var, edgecolors='k', linewidths=1, cmap='jet')
ax.set_title('Velocidade média U das gotas [m/s]')
ax.add_patch(circle)
# ax.add_patch(incircle)
fig.colorbar(plot)
plt.savefig('./atomizador_repar/dpm_u.png',
            dpi=1200,
            format='png')


values = np.loadtxt('./atomizador_repar/dpm_u_std.txt')

zz = np.ndarray(shape=(160,160), buffer=np.array(values[:,0]))
yy = np.ndarray(shape=(160,160), buffer=np.array(values[:,1]))
plot_var = np.ndarray(shape=(160,160), buffer=np.array(values[:,2]))

circle = plt.Circle((0.5,0.5), 0.3207, color='white', fill=False, linewidth=1)
fig, ax = plt.subplots(figsize=(7.5,6))
plot = ax.pcolor(yy, zz, plot_var, edgecolors='k', linewidths=1, cmap='jet')
ax.set_title('Desvio padrão da velocidade U das gotas [m/s]')
ax.add_patch(circle)
fig.colorbar(plot)
plt.savefig('./atomizador_repar/dpm_u-std.png',
            dpi=1200,
            format='png')


values = np.loadtxt('./atomizador_repar/dpm_vel.txt')

zz = np.ndarray(shape=(160,160), buffer=np.array(values[:,0]))
yy = np.ndarray(shape=(160,160), buffer=np.array(values[:,1]))
plot_var = np.ndarray(shape=(160,160), buffer=np.array(values[:,3]))

circle = plt.Circle((0.5,0.5), 0.3207, color='white', fill=False, linewidth=1)
fig, ax = plt.subplots(figsize=(7.5,6))
plot = ax.pcolor(yy, zz, plot_var, edgecolors='k', linewidths=1, cmap='jet')
ax.set_title('Velocidade média V das gotas [m/s]')
ax.add_patch(circle)
fig.colorbar(plot)
plt.savefig('./atomizador_repar/dpm_v.png',
            dpi=1200,
            format='png')


values = np.loadtxt('./atomizador_repar/dpm_v_std.txt')

zz = np.ndarray(shape=(160,160), buffer=np.array(values[:,0]))
yy = np.ndarray(shape=(160,160), buffer=np.array(values[:,1]))
plot_var = np.ndarray(shape=(160,160), buffer=np.array(values[:,2]))

circle = plt.Circle((0.5,0.5), 0.3207, color='white', fill=False, linewidth=1)
fig, ax = plt.subplots(figsize=(7.5,6))
plot = ax.pcolor(yy, zz, plot_var, edgecolors='k', linewidths=1, cmap='jet')
ax.set_title('Desvio padrão da velocidade V das gotas [m/s]')
ax.add_patch(circle)
fig.colorbar(plot)
plt.savefig('./atomizador_repar/dpm_v-std.png',
            dpi=1200,
            format='png')


values = np.loadtxt('./atomizador_repar/dpm_vel.txt')

zz = np.ndarray(shape=(160,160), buffer=np.array(values[:,0]))
yy = np.ndarray(shape=(160,160), buffer=np.array(values[:,1]))
plot_var = np.ndarray(shape=(160,160), buffer=np.array(values[:,4]))

circle = plt.Circle((0.5,0.5), 0.3207, color='white', fill=False, linewidth=1)
fig, ax = plt.subplots(figsize=(7.5,6))
plot = ax.pcolor(yy, zz, plot_var, edgecolors='k', linewidths=1, cmap='jet')
ax.set_title('Velocidade média W das gotas [m/s]')
ax.add_patch(circle)
fig.colorbar(plot)
plt.savefig('./atomizador_repar/dpm_w.png',
            dpi=1200,
            format='png')


values = np.loadtxt('./atomizador_repar/dpm_w_std.txt')

zz = np.ndarray(shape=(160,160), buffer=np.array(values[:,0]))
yy = np.ndarray(shape=(160,160), buffer=np.array(values[:,1]))
plot_var = np.ndarray(shape=(160,160), buffer=np.array(values[:,2]))

circle = plt.Circle((0.5,0.5), 0.3207, color='white', fill=False, linewidth=1)
fig, ax = plt.subplots(figsize=(7.5,6))
plot = ax.pcolor(yy, zz, plot_var, edgecolors='k', linewidths=1, cmap='jet')
ax.set_title('Desvio padrão da velocidade W das gotas [m/s]')
ax.add_patch(circle)
fig.colorbar(plot)
plt.savefig('./atomizador_repar/dpm_w-std.png',
            dpi=1200,
            format='png')


values = np.loadtxt('./atomizador_repar/vazao.txt')

zz = np.ndarray(shape=(160,160), buffer=np.array(values[:,0]))
yy = np.ndarray(shape=(160,160), buffer=np.array(values[:,1]))
plot_var = np.ndarray(shape=(160,160), buffer=np.array(values[:,2]))

circle = plt.Circle((0.5,0.5), 0.3207, color='white', fill=False, linewidth=1)
incircle = plt.Circle((0.5,0.5), 0.07, color='gray', fill=False, linewidth=1)
fig, ax = plt.subplots(figsize=(7.5,6))
plot = ax.pcolor(yy, zz, plot_var, edgecolors='k', linewidths=1, cmap='jet')
ax.set_title('Vazão mássica de gotas [-]')
ax.add_patch(circle)
# ax.add_patch(incircle)
fig.colorbar(plot)
plt.savefig('./atomizador_repar/dpm_massflow.png',
            dpi=1200,
            format='png')


values = np.loadtxt('./atomizador_repar/Y_H2O_average.txt')

zz = np.ndarray(shape=(160,160), buffer=np.array(values[:,0]))
yy = np.ndarray(shape=(160,160), buffer=np.array(values[:,1]))
plot_var = np.ndarray(shape=(160,160), buffer=np.array(values[:,2]))

circle = plt.Circle((0.5,0.5), 0.3207, color='white', fill=False, linewidth=1)
fig, ax = plt.subplots(figsize=(7.5,6))
plot = ax.pcolor(yy, zz, plot_var, edgecolors='k', linewidths=1, cmap='jet')
ax.set_title("Fração mássica de vapor d'água no gás [-]")
ax.add_patch(circle)
fig.colorbar(plot)
plt.savefig('./atomizador_repar/Yh2o_gas.png',
            dpi=1200,
            format='png')


####### test

values = np.loadtxt('./atomizador_recap/dpm_vel.txt')

zz = np.ndarray(shape=(160,160), buffer=np.array(values[:,0]))
yy = np.ndarray(shape=(160,160), buffer=np.array(values[:,1]))
plot_var = np.ndarray(shape=(160,160), buffer=np.array(values[:,2]))

circle = plt.Circle((0.5,0.5), 0.3207, color='white', fill=False, linewidth=1)
incircle = plt.Circle((0.5,0.5), 0.07, color='gray', fill=False, linewidth=1)
fig, ax = plt.subplots(figsize=(7.5,6))
plot = ax.pcolor(yy, zz, plot_var, edgecolors='k', linewidths=1, cmap='jet')
ax.set_title('Velocidade média U das gotas [m/s]')
ax.add_patch(circle)
# ax.add_patch(incircle)
fig.colorbar(plot)


values = np.loadtxt('./atomizador_recap/dpm_vel.txt')

zz = np.ndarray(shape=(160,160), buffer=np.array(values[:,0]))
yy = np.ndarray(shape=(160,160), buffer=np.array(values[:,1]))
plot_var = np.ndarray(shape=(160,160), buffer=np.array(values[:,3]))

circle = plt.Circle((0.5,0.5), 0.3207, color='white', fill=False, linewidth=1)
fig, ax = plt.subplots(figsize=(7.5,6))
plot = ax.pcolor(yy, zz, plot_var, edgecolors='k', linewidths=1, cmap='jet')
ax.set_title('Velocidade média V das gotas [m/s]')
ax.add_patch(circle)
fig.colorbar(plot)


values = np.loadtxt('./atomizador_recap/dpm_vel.txt')

zz = np.ndarray(shape=(160,160), buffer=np.array(values[:,0]))
yy = np.ndarray(shape=(160,160), buffer=np.array(values[:,1]))
plot_var = np.ndarray(shape=(160,160), buffer=np.array(values[:,4]))

circle = plt.Circle((0.5,0.5), 0.3207, color='white', fill=False, linewidth=1)
fig, ax = plt.subplots(figsize=(7.5,6))
plot = ax.pcolor(yy, zz, plot_var, edgecolors='k', linewidths=1, cmap='jet')
ax.set_title('Velocidade média W das gotas [m/s]')
ax.add_patch(circle)
fig.colorbar(plot)
