import numpy as np

base_dir = "./atomizador_repar"


# Fluid phase velocity

U = np.loadtxt('./atomizador_repar/U_avg.txt')
V = np.loadtxt('./atomizador_repar/V_avg.txt')
W = np.loadtxt('./atomizador_repar/W_avg.txt')

vel = np.empty((len(U),5))
vel[:,:3] = U
vel[:,3] = V[:,2]
vel[:,4] = W[:,2]
np.savetxt(f"{base_dir}/vel_avg.txt", vel)


# Fluid phase temperature

avg = np.loadtxt('./atomizador_repar/T_avg.txt')
std = np.loadtxt('./atomizador_repar/T_std.txt')

avg_std = np.empty((len(avg),4))
avg_std[:,:3] = avg
avg_std[:,3] = std[:,2]
np.savetxt(f"{base_dir}/fluid_T.txt", avg_std)


# dpm_diam

avg = np.loadtxt('./atomizador_repar/dpm_diam_avg.txt')
std = np.loadtxt('./atomizador_repar/dpm_diam_std.txt')

avg_std = np.empty((len(avg),4))
avg_std[:,:3] = avg
avg_std[:,3] = std[:,2]
np.savetxt(f"{base_dir}/dpm_diam.txt", avg_std)


# Dpms velocity

U_avg = np.loadtxt('./atomizador_repar/dpm_u_avg.txt')
U_avg[:,2][U_avg[:,2]<1.0] = 1.0
V_avg = np.loadtxt('./atomizador_repar/dpm_v_avg.txt')
W_avg = np.loadtxt('./atomizador_repar/dpm_w_avg.txt')
U_std = np.loadtxt('./atomizador_repar/dpm_u_std.txt')
V_std = np.loadtxt('./atomizador_repar/dpm_v_std.txt')
W_std = np.loadtxt('./atomizador_repar/dpm_w_std.txt')

vel = np.empty((len(U),8))
vel[:,:3] = U_avg
vel[:,3] = V_avg[:,2]
vel[:,4] = W_avg[:,2]
vel[:,5] = U_std[:,2]
vel[:,6] = V_std[:,2]
vel[:,7] = W_std[:,2]
np.savetxt(f"{base_dir}/dpm_vel.txt", vel)


# Dpms velocity (scaling for recap)

U_avg = np.loadtxt('./atomizador_repar/dpm_u_avg.txt')
scale = 30.70/22.13
U_avg[:,2] = U_avg[:,2]*scale
U_avg[:,2][U_avg[:,2]<1.0] = 1.0
V_avg = np.loadtxt('./atomizador_repar/dpm_v_avg.txt')
W_avg = np.loadtxt('./atomizador_repar/dpm_w_avg.txt')
U_std = np.loadtxt('./atomizador_repar/dpm_u_std.txt')
V_std = np.loadtxt('./atomizador_repar/dpm_v_std.txt')
W_std = np.loadtxt('./atomizador_repar/dpm_w_std.txt')

vel = np.empty((len(U),8))
vel[:,:3] = U_avg
vel[:,3] = V_avg[:,2]
vel[:,4] = W_avg[:,2]
vel[:,5] = U_std[:,2]
vel[:,6] = V_std[:,2]
vel[:,7] = W_std[:,2]
np.savetxt(f"atomizador_recap/dpm_vel.txt", vel)


# dpm_temp

avg = np.loadtxt('./atomizador_repar/dpm_temp_avg.txt')
avg[:,2][avg[:,2]<333.15] = 333.15
std = np.loadtxt('./atomizador_repar/dpm_temp_std.txt')

avg_std = np.empty((len(avg),4))
avg_std[:,:3] = avg
avg_std[:,3] = std[:,2]
np.savetxt(f"{base_dir}/dpm_temp.txt", avg_std)
