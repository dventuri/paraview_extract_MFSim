# before using in cluster6: ml gnu python/3.9.0 paraview

# trace generated using paraview version 5.9.0
# modified

### filename and timestep selection
base_dir = "/home/mmvillar/st_euler/canal_30m"
base_fname = f"{base_dir}/output/ns_output_ct.*.hdf5"
timestep_treshold = 38500

#imports
import glob
import re
from paraview.simple import *   # import the simple module from the paraview

### function to sort numerically
def numericalSort(value):
    numbers = re.compile(r'(\d+)')  #regex to match any repeating numerical Unicode character
    parts = numbers.split(value)    #splits the string using "numbers"
    parts = map(int, parts[1::2])   #returns only the numbers converted to ints
    return tuple(parts)

### function to compare timesteps
def timestep_above(value, threshold):
    parts = numericalSort(value)
    return parts[-2] >= threshold    #uses second to last number (last is 5 for .hdf5)

# generate list o filenames to read (numerically sorted and only above timestep threshold)
fnames = sorted(glob.glob(base_fname), key=numericalSort)   #sorts the list of names using the converted numbers
fnames = [fname for fname in fnames if timestep_above(fname, timestep_treshold)]

# create a new 'VisItChomboReader'
db = VisItChomboReader(FileName=fnames)

# Properties modified on db
db.PointArrayStatus = [
    'u', 'v', 'w',
    'temperature', 'Y_N2', 'Y_H2O',
    'dpm_diam', 'dpm_mass', 'dpm_npart',
    'dpm_u', 'dpm_v', 'dpm_w'
]

# create a new 'Calculator'
# vazao de gotas = concentracao de gotas na celula * velocidade (das gotas) * area
#                = dpm_mass/cell_volume * dpm_u * cell area
#                = dpm_mass*dpm_u/0.025
calculator1 = Calculator(registrationName='Calculator1', Input=db)
calculator1.Function = ''
calculator1.ResultArrayName = 'vazao'
calculator1.Function = 'dpm_mass*dpm_npart/0.025'

# create a new 'Temporal Statistics'
temporalStatistics1 = TemporalStatistics(registrationName='TemporalStatistics1', Input=calculator1)

# create a new 'Slice'
slice1 = Slice(registrationName='Slice1', Input=temporalStatistics1)
slice1.SliceType = 'Plane'
slice1.HyperTreeGridSlicer = 'Plane'
slice1.SliceOffsetValues = [0.0]

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [29.9999, 0.5, 0.5]

# save data
SaveData(f'{base_dir}/paraview/test.csv', proxy=slice1, PointDataArrays=[
    'u_average', 'v_average', 'w_average',
    'temperature_average', 'temperature_stddev',
    'Y_N2_average', 'Y_N2_stddev',
    'Y_H2O_average', 'Y_H2O_stddev',
    'dpm_diam_average', 'dpm_diam_stddev',
    'dpm_u_average', 'dpm_u_stddev', 'dpm_v_average', 'dpm_v_stddev', 'dpm_w_average', 'dpm_w_stddev',
    'vazao_average'
])
