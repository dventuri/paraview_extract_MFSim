import numpy as np
import matplotlib.pyplot as plt

values = np.loadtxt('vel.txt')

yy = np.ndarray(shape=(41,41), buffer=np.array(values[:,0]))
zz = np.ndarray(shape=(41,41), buffer=np.array(values[:,1]))
plot_var = np.ndarray(shape=(41,41), buffer=np.array(values[:,2]))

circle = plt.Circle((0.5,0.5), 0.3207, color='white', fill=False, linewidth=1)
fig, ax = plt.subplots(figsize=(6,6))
ax.pcolor(yy, zz, plot_var, edgecolors='k', linewidths=1)
ax.add_patch(circle)
