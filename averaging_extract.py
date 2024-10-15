# before using in cluster6: ml paraview

# trace generated using paraview version 5.9.0
# modified

### filename and timestep selection
base_dir = "/home/dventuri/run/injetor_m/case1"
base_fname = f"{base_dir}/output_t11/ns_output_ct.*.hdf5"
timestep_treshold = 40000
dx = 0.00625

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
    'temperature', 'Y_H2O', 'Y_C11H21',
    'Y_C2H6', 'Y_C9H19-1', 'Y_NC13H28',
    'Y_NC6H14', 'Y_NC7H16',
    'dpm_diam', 'dpm_mass', 'dpm_npart',
    'dpm_u', 'dpm_v', 'dpm_w', 'dpm_temp'
]

# Extract only base level (lbot)
extractAMRBlocks1 = ExtractAMRBlocks(Input=db)
extractAMRBlocks1.SelectedDataSets = [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0, 11, 0, 12, 0, 13, 0, 14, 0, 15, 0, 16, 0, 17, 0, 18, 0, 19, 0, 20, 0, 21, 0, 22, 0, 23, 0, 24, 0, 25, 0, 26, 0, 27, 0, 28, 0, 29, 0, 30, 0, 31, 0, 32, 0, 33, 0, 34, 0, 35, 0, 36, 0, 37, 0, 38, 0, 39, 0, 40, 0, 41, 0, 42, 0, 43, 0, 44, 0, 45, 0, 46, 0, 47, 0, 48, 0, 49, 0, 50, 0, 51, 0, 52, 0, 53, 0, 54, 0, 55, 0, 56, 0, 57, 0, 58, 0, 59, 0, 60, 0, 61, 0, 62, 0, 63]

# Convert point data to cell data
pointDatatoCellData1 = PointDatatoCellData(Input=extractAMRBlocks1)
pointDatatoCellData1.ProcessAllArrays = 1
pointDatatoCellData1.PassPointData = 0
pointDatatoCellData1.CategoricalData = 0

# create a new 'Temporal Statistics'
temporalStatistics1 = TemporalStatistics(Input=pointDatatoCellData1)
temporalStatistics1.ComputeAverage = 1
temporalStatistics1.ComputeMinimum = 0
temporalStatistics1.ComputeMaximum = 0
temporalStatistics1.ComputeStandardDeviation = 1

# create a new 'Calculator'
calculator1 = Calculator(Input=temporalStatistics1)
calculator1.AttributeType = 'Cell Data'
calculator1.ResultArrayName = 'vazao'
calculator1.Function = 'dpm_npart_average*dpm_mass_average*dpm_u_average/'+str(dx)

# create a new 'Slice'
slice1 = Slice(Input=calculator1)
slice1.SliceType = 'Plane'
slice1.HyperTreeGridSlicer = 'Plane'
slice1.SliceOffsetValues = [0.0]

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.499999, 0.5, 0.5]
slice1.Triangulatetheslice = 0

# save data
SaveData(f'./dados_atomizador_extract.csv',
         proxy=slice1,
         WriteTimeSteps=0,
         ChooseArraysToWrite=0,
         FieldAssociation='Cell Data'
)
