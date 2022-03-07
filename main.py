# trace generated using paraview version 5.9.0
# modified

### filename and timestep selection
base_dir = "/home/dventuri/st_euler/sp_5x5_CoF_forced_evap/output"
base_fname = f"{base_dir}/ns_output_ct.*.hdf5"
timestep_treshold = 129500

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
fnames = [fname for fname in fnames if timestep_above(fname, 100500)]

# create a new 'VisItChomboReader'
db = VisItChomboReader(FileName=fnames)

# Properties modified on db
db.PointArrayStatus = ['dpm_diam', 'temperature', 'dpm_u', 'dpm_mass']

# create a new 'Calculator'
# vazao de gotas = concentracao de gotas na celula * velocidade (das gotas) * area
#                = dpm_mass/cell_volume * dpm_u * cell area
#                = dpm_mass*dpm_u/0.025
calculator1 = Calculator(registrationName='Calculator1', Input=db)
calculator1.Function = ''
calculator1.ResultArrayName = 'vazao'
calculator1.Function = 'dpm_mass*dpm_npart/0.025'

# create a new 'Extract AMR Blocks'
extractAMRBlocks1 = ExtractAMRBlocks(registrationName='ExtractAMRBlocks1', Input=calculator1)

# Properties modified on extractAMRBlocks1
extractAMRBlocks1.SelectedDataSets = [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0, 11, 0, 12, 0, 13, 0, 14, 0, 15]

# create a new 'Temporal Statistics'
temporalStatistics1 = TemporalStatistics(registrationName='TemporalStatistics1', Input=extractAMRBlocks1)

# create a new 'Slice'
slice1 = Slice(registrationName='Slice1', Input=temporalStatistics1)
slice1.SliceType = 'Plane'
slice1.HyperTreeGridSlicer = 'Plane'
slice1.SliceOffsetValues = [0.0]

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.4999, 0.5, 0.5]

# save data
SaveData(f'{base_dir}/test.csv', proxy=slice1, PointDataArrays=[
    'dpm_diam_average', 'dpm_diam_maximum', 'dpm_diam_minimum', 'dpm_diam_stddev',
    'temperature_average', 'temperature_maximum', 'temperature_minimum', 'temperature_stddev',
    'vazao_average'
])
