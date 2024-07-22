### import modules
import numpy as np

base_dir = "./canal_teste"
base_fname = f"{base_dir}/dados_canal_teste.csv"

# Function: sort array in correct order and save to file
def sort(data_array):

    ### sort by z first, then y - ascending order
    sorted_data = data_array[np.lexsort((data_array[:,1],data_array[:,0]))]

    ### creates a bool mask pointing repeating (y,z) lines
    row_mask = np.append([True],np.any(np.diff(sorted_data[:,:2],axis=0),1))

    ### filters data
    new_data = sorted_data[row_mask]

    return new_data


### read csv data exported from paraview module


# u, v and w fluid velocity
data = []
data = np.loadtxt(
    base_fname,
    delimiter=',',
    skiprows=1,
    usecols=(
        1,  # y position
        2,  # z position
        35, # u_average
        39, # v_average
        47  # w_average
    )
)
data_new = []
data_new = sort(data)
np.savetxt(f"{base_dir}/vel.txt", data_new)


# # temperature
# data = []
# data = np.loadtxt(
#     base_fname,
#     delimiter=',',
#     skiprows=1,
#     usecols=(
#         1,  # y position
#         2,  # z position
#         39, # temperature_average
#         42  # temperature_stddev
#     )
# )
# data_new = []
# data_new = sort(data)
# np.savetxt(f'{base_dir}/temperature.txt', data_new)


# # yk_h2o
# data = []
# data = np.loadtxt(
#     base_fname,
#     delimiter=',',
#     skiprows=1,
#     usecols=(
#         1,  # y position
#         2,  # z position
#         3,  # yk_average
#         6   # yk_stddev
#     )
# )
# data_new = []
# data_new = sort(data)
# np.savetxt(f'{base_dir}/yH2O.txt', data_new)


# dpm_Dmass
data = []
data = np.loadtxt(
    base_fname,
    delimiter=',',
    skiprows=1,
    usecols=(
        1,  # y position
        2,  # z position
        3,  # dpm_Dmass_average
        6   # dpm_Dmass_stddev
    )
)
data_new = []
data_new = sort(data)
np.savetxt(f'{base_dir}/dpm_Dmass.txt', data_new)


# dpm_Dnpart
data = []
data = np.loadtxt(
    base_fname,
    delimiter=',',
    skiprows=1,
    usecols=(
        1,  # y position
        2,  # z position
        7,  # dpm_Dnpart_average
        10  # dpm_Dnpart_stddev
    )
)
data_new = []
data_new = sort(data)
np.savetxt(f'{base_dir}/dpm_Dnpart.txt', data_new)


# dpm_diam
data = []
data = np.loadtxt(
    base_fname,
    delimiter=',',
    skiprows=1,
    usecols=(
        1,  # y position
        2,  # z position
        11, # dpm_diam_average
        14  # dpm_diam_stddev
    )
)
data_new = []
data_new = sort(data)
np.savetxt(f'{base_dir}/dpm_diam.txt', data_new)


# dpm_mass
data = []
data = np.loadtxt(
    base_fname,
    delimiter=',',
    skiprows=1,
    usecols=(
        1,  # y position
        2,  # z position
        15, # dpm_mass_average
        18  # dpm_mass_stddev
    )
)
data_new = []
data_new = sort(data)
np.savetxt(f'{base_dir}/dpm_mass.txt', data_new)


# dpm_npart
data = []
data = np.loadtxt(
    base_fname,
    delimiter=',',
    skiprows=1,
    usecols=(
        1,  # y position
        2,  # z position
        19, # dpm_npart_average
        22  # dpm_npart_stddev
    )
)
data_new = []
data_new = sort(data)
np.savetxt(f'{base_dir}/dpm_npart.txt', data_new)


# dpm_vel
data = []
data = np.loadtxt(
    base_fname,
    delimiter=',',
    skiprows=1,
    usecols=(
        1,  # y position
        2,  # z position
        23, # dpm_u_average
        27, # dpm_v_average
        31, # dpm_w_average
        26, # dpm_u_stddev
        30, # dpm_v_stddev
        34  # dpm_w_stddev
    )
)
data_new = []
data_new = sort(data)
np.savetxt(f'{base_dir}/dpm_vel.txt', data_new)


# dpm_mass_flow - PDF
data = []
data = np.loadtxt(
    base_fname,
    delimiter=',',
    skiprows=1,
    usecols=(
        1,  # y position
        2,  # z position
        43  # vazao_average
    )
)
data_new = []
data_new = sort(data)

total_flow = data_new[:,2].sum()
data_new[:,2] = data_new[:,2]/total_flow
data_new[:,2] = np.cumsum(data_new[:,2])

np.savetxt(f'{base_dir}/dpm_flow.txt', data_new)
print('add total_mass_flow to first line!!!', total_flow)


# massa de gotas reais injetadas
# num_gotas_por_dt = 10
# diam_gotas = 0.8E-3
# vol_1gota = np.pi/6*diam_gotas**3
# vol_gotas_por_dt = num_gotas_por_dt*vol_1gota
# rho_gotas = 1000
# massa_gotas_por_dt = vol_gotas_por_dt*rho_gotas
# dt = 1E-4
# massa_gotas_por_s = massa_gotas_por_dt/dt
# print('massa de gotas reais injetadas', massa_gotas_por_s)
print('massa de gotas reais injetadas', 0.01)
