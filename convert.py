### import modules
import numpy as np


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
    'test_5x5.csv',
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
np.savetxt('vel.txt', data_new)

# temperature
data = []
data = np.loadtxt(
    'test_5x5.csv',
    delimiter=',',
    skiprows=1,
    usecols=(
        1,  # y position
        2,  # z position
        31, # temperature_average
        34  # temperature_stddev
    )
)
data_new = []
data_new = sort(data)
np.savetxt('temperature.txt', data_new)

# yk_n2
data = []
data = np.loadtxt(
    'test_5x5.csv',
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
np.savetxt('yk.txt', data_new)

# dpdiam
data = []
data = np.loadtxt(
    'test_5x5.csv',
    delimiter=',',
    skiprows=1,
    usecols=(
        1,  # y position
        2,  # z position
        7, # dpdiam_average
        10  # dpdiam_stddev
    )
)
data_new = []
data_new = sort(data)
np.savetxt('dpdiam.txt', data_new)

# dpvel
data = []
data = np.loadtxt(
    'test_5x5.csv',
    delimiter=',',
    skiprows=1,
    usecols=(
        1,  # y position
        2,  # z position
        19, # dpmu_average
        23, # dpmv_average
        27, # dpmw_average
        22, # dpmu_stddev
        26, # dpmv_stddev
        30  # dpmw_stddev
    )
)
data_new = []
data_new = sort(data)
np.savetxt('dpvel.txt', data_new)

# dpm_mass_flow - PDF
data = []
data = np.loadtxt(
    'test_5x5.csv',
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

np.savetxt('dpm_flow.txt', data_new)
print('add total_mass_flow to first line!!!', total_flow)

### testing fortran array and read function for MFSim
# data_test_fortran = np.concatenate(([[None,None,None]],masked_data),axis=0)
# def find_position(y,z,n=41,d=0.025):
#     j = round(y/d)
#     k = round(z/d)
#     pos = j*n + k + 1
#     return pos
