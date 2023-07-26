### import modules
import numpy as np

base_dir = "./milena_30m"
base_fname = f"{base_dir}/data.csv"

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
        39, # u_average
        43, # v_average
        47  # w_average
    )
)
data_new = []
data_new = sort(data)
np.savetxt(f"{base_dir}/u_avg.txt", data_new)

# temperature
data = []
data = np.loadtxt(
    base_fname,
    delimiter=',',
    skiprows=1,
    usecols=(
        1,  # y position
        2,  # z position
        35, # temperature_average
        38  # temperature_stddev
    )
)
data_new = []
data_new = sort(data)
np.savetxt(f'{base_dir}/temperature_avg.txt', data_new)

# yk_h2o
data = []
data = np.loadtxt(
    base_fname,
    delimiter=',',
    skiprows=1,
    usecols=(
        1,  # y position
        2,  # z position
        3,  # yk_average
        6   # yk_stddev
    )
)
data_new = []
data_new = sort(data)
np.savetxt(f'{base_dir}/ykH2O_avg.txt', data_new)

# density
data = []
data = np.loadtxt(
    base_fname,
    delimiter=',',
    skiprows=1,
    usecols=(
        1,  # y position
        2,  # z position
        11, # rho_average
        14  # rho_stddev
    )
)
data_new = []
data_new = sort(data)
np.savetxt(f'{base_dir}/rho_avg.txt', data_new)

# dpdiam
data = []
data = np.loadtxt(
    base_fname,
    delimiter=',',
    skiprows=1,
    usecols=(
        1,  # y position
        2,  # z position
        15, # dpdiam_average
        18  # dpdiam_stddev
    )
)
data_new = []
data_new = sort(data)
np.savetxt(f'{base_dir}/dpdiam_avg.txt', data_new)

# dpvel
data = []
data = np.loadtxt(
    base_fname,
    delimiter=',',
    skiprows=1,
    usecols=(
        1,  # y position
        2,  # z position
        23, # dpmu_average
        27, # dpmv_average
        31, # dpmw_average
        26, # dpmu_stddev
        30, # dpmv_stddev
        34  # dpmw_stddev
    )
)
data_new = []
data_new = sort(data)
np.savetxt(f'{base_dir}/dpvel_avg.txt', data_new)

# # dpNpart
# data = []
# data = np.loadtxt(
#     base_fname,
#     delimiter=',',
#     skiprows=1,
#     usecols=(
#         1,  # y position
#         2,  # z position
#         15, # dpm_npart_average
#         18  # dpm_npart_stddev
#     )
# )
# data_new = []
# data_new = sort(data)
# np.savetxt(f'{base_dir}/dpNpart_avg.txt', data_new)

# # dpm_mass_flow - PDF
# data = []
# data = np.loadtxt(
#     base_fname,
#     delimiter=',',
#     skiprows=1,
#     usecols=(
#         1,  # y position
#         2,  # z position
#         43  # vazao_average
#     )
# )
# data_new = []
# data_new = sort(data)

# total_flow = data_new[:,2].sum()
# data_new[:,2] = data_new[:,2]/total_flow
# data_new[:,2] = np.cumsum(data_new[:,2])

# np.savetxt(f'{base_dir}/dpm_flow_15.txt', data_new)
# print('add total_mass_flow to first line!!!', total_flow)

### testing fortran array and read function for MFSim
# data_test_fortran = np.concatenate(([[None,None,None]],masked_data),axis=0)
# def find_position(y,z,n=41,d=0.025):
#     j = round(y/d)
#     k = round(z/d)
#     pos = j*n + k + 1
#     return pos
