# before unsing in cluster6: ml gnu python/3.9.0 paraview
# execute in pvpython

### IMPORTS
import glob
import re
from paraview.simple import *


### GLOBAL DEFINITIONS
base_dir = "/home/mmvillar/st_euler/canal_30m_ewf/teste30m"
base_fname = f"{base_dir}/out1/ns_output_ct.*.hdf5"
timestep_treshold = 0


### FUNCTIONS
# sort numerically
def numericalSort(value):
    numbers = re.compile(r'(\d+)')  #regex to match any repeating numerical Unicode character
    parts = numbers.split(value)    #splits the string using "numbers"
    parts = map(int, parts[1::2])   #returns only the numbers converted to ints
    return tuple(parts)

# compare timesteps
def timestep_above(value, threshold):
    parts = numericalSort(value)
    return parts[-2] >= threshold    #uses second to last number (last is 5 for .hdf5)


### FILENAMES
# generate list of filenames to read (numerically sorted and only above timestep threshold)
fnames = sorted(glob.glob(base_fname), key=numericalSort)   #sorts the list of names using the converted numbers
fnames = [fname for fname in fnames if timestep_above(fname, timestep_treshold)]

for count, fname in enumerate(fnames):
    print(len(fnames)-count-1, fname[-10:-5])
