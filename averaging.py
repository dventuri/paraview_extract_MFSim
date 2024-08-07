# before using in cluster6: ml paraview

# trace generated using paraview version 5.9.0
# modified

### filename and timestep selection
base_dir = "/home/dventuri/st_euler/canal_teste_dpms_medias"
base_fname = f"{base_dir}/output/ns_output_ct.*.hdf5"
timestep_treshold = 500
dx = 0.005

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
    #'temperature', 'Y_H2O',
    'dpm_diam', 'dpm_mass', 'dpm_npart',
    'dpm_u', 'dpm_v', 'dpm_w'
]

# Convert point data to cell data
pointDatatoCellData1 = PointDatatoCellData(Input=db)
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
slice1.SliceType.Origin = [0.999999, 0.05, 0.05]
slice1.Triangulatetheslice = 0

# save data
SaveData(f'./dados_canal_teste.csv',
         proxy=slice1,
         WriteTimeSteps=0,
         ChooseArraysToWrite=0,
         FieldAssociation='Cell Data'
)
