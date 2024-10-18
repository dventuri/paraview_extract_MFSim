### import modules
import numpy as np
import matplotlib.pyplot as plt

base_dir = "./atomizador_repar"
base_fname = f"{base_dir}/dados_atomizador_extract.csv"

n = 80
dx = 0.00625

def sort(data_array):

    ### sort by z first, then y - ascending order
    sorted_data = data_array[np.lexsort((data_array[:,1],data_array[:,0]))]

    return sorted_data

def read_save_data(line: int, filename: str):

    # read first half of the data
    data1 = np.loadtxt(
            base_fname,
            delimiter=',',
            skiprows=1,
            max_rows=12800,
            usecols=(
                line
            )
    )

    # read second half of the data
    data2 = np.loadtxt(
            base_fname,
            delimiter=',',
            skiprows=1+12800,
            usecols=(
                line
            )
    )

    # append y and z locations to each array
    total = len(data1)
    data_new1 = np.zeros((total, 3))
    for i in range(2*n):
        for j in range(n):
            data_new1[n*i + j, 0] = (i+1)*dx
            data_new1[n*i + j, 1] = (j+1)*dx
            data_new1[n*i + j, 2] = data1[n*i + j]
    data_new2 = np.zeros((total, 3))
    for i in range(2*n):
        for j in range(n):
            data_new2[n*i + j, 0] = (i+1)*dx
            data_new2[n*i + j, 1] = (j+1)*dx + 0.5
            data_new2[n*i + j, 2] = data2[n*i + j]

    # concatenate both arrays
    data_new = np.concatenate((data_new1, data_new2), axis=0)
    data_new[:, [1, 0]] = data_new[:, [0, 1]]   # swap y,z columns
    data_sorted = sort(data_new)                # sort
    np.savetxt(f"{base_dir}/{filename}.txt", data_sorted)  # save


read_save_data(1, 'Y_C11H21')
read_save_data(3, 'Y_C2H6')
read_save_data(5, 'Y_C9H19-1')
read_save_data(7, 'Y_H2O_average')
read_save_data(9, 'Y_NC13H28')
read_save_data(11, 'Y_NC6H14')
read_save_data(13, 'Y_NC7H16')
read_save_data(15, 'dpm_diam_avg')
read_save_data(16, 'dpm_diam_std')
read_save_data(19, 'dpm_temp_avg')
read_save_data(20, 'dpm_temp_std')
read_save_data(21, 'dpm_u_avg')
read_save_data(22, 'dpm_u_std')
read_save_data(23, 'dpm_v_avg')
read_save_data(24, 'dpm_v_std')
read_save_data(25, 'dpm_w_avg')
read_save_data(26, 'dpm_w_std')
read_save_data(27, 'T_avg')
read_save_data(28, 'T_std')
read_save_data(29, 'U_avg')
read_save_data(31, 'V_avg')
read_save_data(34, 'W_avg')
read_save_data(33, 'vazao')
