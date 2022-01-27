### import modules
import numpy as np

### read csv data exported from paraview module
data = np.loadtxt(
    'test.csv',
    delimiter=',',
    skiprows=1,
    usecols=(
        1,  # y position
        2,  # z position
        3,  # dpm_diam_average
        6   # dpm_diam_stddev
    )
)

### sort by z first, then y - ascending order
sorted_data = data[np.lexsort((data[:,1],data[:,0]))]

### creates a bool mask pointing repeating (y,z) lines
row_mask = np.append([True],np.any(np.diff(sorted_data[:,:2],axis=0),1))

### filters data
masked_data = sorted_data[row_mask]

### save data
np.savetxt("vel.txt", masked_data)


### testing fortran array and read function for MFSim
# data_test_fortran = np.concatenate(([[None,None,None]],masked_data),axis=0)
# def find_position(y,z,n=41,d=0.025):
#     j = round(y/d)
#     k = round(z/d)
#     pos = j*n + k + 1
#     return pos
