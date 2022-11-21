import numpy as np
import matplotlib.pyplot as plt

values = np.loadtxt('./30m_cont/dpdiam_20.txt')

yy = np.ndarray(shape=(81,81), buffer=np.array(values[:,0]))
zz = np.ndarray(shape=(81,81), buffer=np.array(values[:,1]))
plot_var = np.ndarray(shape=(81,81), buffer=np.array(values[:,2]))

circle = plt.Circle((0.5,0.5), 0.3207, color='white', fill=False, linewidth=1)
fig, ax = plt.subplots(figsize=(7.5,6))
plot = ax.pcolor(yy, zz, plot_var, edgecolors='k', linewidths=1)
ax.add_patch(circle)
fig.colorbar(plot)
