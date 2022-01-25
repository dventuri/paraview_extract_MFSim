import numpy as np

data = np.loadtxt('test.csv',delimiter=',',skiprows=1,usecols=(1,2,3))

sorted_data = data[np.lexsort((data[:,1],data[:,0]))]

row_mask = np.append([True],np.any(np.diff(sorted_data[:,:2],axis=0),1))

masked_data = sorted_data[row_mask]

data_test_fortran = np.concatenate(([[None,None,None]],masked_data),axis=0)

def find_position(y,z,n=41,d=0.025):
    j = round(y/d)
    k = round(z/d)
    pos = j*n + k + 1
    return pos
