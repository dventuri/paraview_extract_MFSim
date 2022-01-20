# trace generated using paraview version 5.9.0
# modified

import glob
import re

#### import the simple module from the paraview
from paraview.simple import *

### function to sort numerically
numbers = re.compile(r'(\d+)')
def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts

### base folder and filename
base_dir = "/home/dventuri/st_euler/sp_5x5_CoF_forced_evap/output"
filename = f"{base_dir}/ns_output_ct.0001*.hdf5"

#print(sorted(glob.glob(filename), key=numericalSort))
# create a new 'VisItChomboReader'
db = VisItChomboReader(FileName=sorted(glob.glob(filename)))

# Properties modified on db
db.PointArrayStatus = ['dpm_diam', 'temperature']

# create a new 'Extract AMR Blocks'
extractAMRBlocks1 = ExtractAMRBlocks(registrationName='ExtractAMRBlocks1', Input=db)

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
slice1.SliceType.Origin = [0.4999, 0.5000000000000002, 0.5000000000000002]

# show data in view
#slice1Display = Show(slice1, renderView1, 'GeometryRepresentation')

# update the view to ensure updated data information
#renderView1.Update()

# save data
SaveData(f'{base_dir}/test.csv', proxy=slice1, PointDataArrays=['dpm_diam_average', 'dpm_diam_maximum', 'dpm_diam_minimum', 'dpm_diam_stddev', 'temperature_average', 'temperature_maximum', 'temperature_minimum', 'temperature_stddev'])
