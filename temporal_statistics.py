# before unsing in cluster6: ml gnu python/3.9.0 paraview
# execute in pvpython

### IMPORTS
import glob
import re
from paraview.simple import *


### GLOBAL DEFINITIONS
base_dir = "/home/mmvillar/st_euler/canal_30m_ewf/teste30m"
base_fname = f"{base_dir}/out1/ns_output_ct.*.hdf5"
timestep_treshold = 30000


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

# convert python annotation strings to numerical values
def annotate2value(annotation_string):
    value = float(annotation_string[1:-1])  #remove brackets "[...]"
    return value


### FILENAMES
# generate list of filenames to read (numerically sorted and only above timestep threshold)
fnames = sorted(glob.glob(base_fname), key=numericalSort)   #sorts the list of names using the converted numbers
fnames = [fname for fname in fnames if timestep_above(fname, timestep_treshold)]


### ITERATE OVER ALL FILES TO GET STATISTICS

for ts in range(len(fnames)-1):
    # create a new 'VisItChomboReader'
    db = VisItChomboReader(FileName=fnames[-2-ts:]) # reversed loop
                                                    # from last ts alone,
                                                    # to last plus previous
    print("Reading databases from ", fnames[-2-ts][-10:-5], "to ", fnames[-1][-10:-5])

    # Properties modified on db
    db.PointArrayStatus = [
        'u', 'Y_H2O', 'temperature',
        'dpm_diam', 'dpm_mass', 'dpm_u'
    ]

    # create a new 'Temporal Statistics'
    temporalStatistics1 = TemporalStatistics(Input=db)

    # Slice
    slice1 = Slice(Input=temporalStatistics1)
    slice1.SliceType = 'Plane'
    slice1.SliceType.Origin = [29.999999, 0.5, 0.5]

    # Integrate Variables
    integrateVariables1 = IntegrateVariables(Input=slice1)

    # Annotation
    pythonAnnotation1 = PythonAnnotation(Input=integrateVariables1)
    pythonAnnotation1.ArrayAssociation = 'Cell Data'
    pythonAnnotation1.Expression = 'Area'
    pythonAnnotation1.UpdatePipeline()
    string = FetchData(pythonAnnotation1)[0].GetRowData().GetAbstractArray(0).GetValue(0)
    AreaSquare = annotate2value(string)

    # Clip
    clip1 = Clip(Input=slice1)
    clip1.ClipType = 'Cylinder'
    clip1.ClipType.Axis = [1.0, 0.0, 0.0]
    clip1.ClipType.Radius = 0.3207

    # Integrate Variables
    integrateVariables2 = IntegrateVariables(Input=clip1)

    # Annotation
    pythonAnnotation2 = PythonAnnotation(Input=integrateVariables2)
    pythonAnnotation2.ArrayAssociation = 'Cell Data'
    pythonAnnotation2.Expression = 'Area'
    pythonAnnotation2.UpdatePipeline()
    string = FetchData(pythonAnnotation2)[0].GetRowData().GetAbstractArray(0).GetValue(0)
    AreaCirc = annotate2value(string)

    pythonAnnotation2.ArrayAssociation = 'Point Data'
    pythonAnnotation2.Expression = 'u_average'
    pythonAnnotation2.UpdatePipeline()
    string = FetchData(pythonAnnotation2)[0].GetRowData().GetAbstractArray(0).GetValue(0)
    mean_u = annotate2value(string)*AreaSquare/AreaCirc
    pythonAnnotation2.Expression = 'Y_H2O_average'
    pythonAnnotation2.UpdatePipeline()
    string = FetchData(pythonAnnotation2)[0].GetRowData().GetAbstractArray(0).GetValue(0)
    mean_YH2O = annotate2value(string)*AreaSquare/AreaCirc
    pythonAnnotation2.Expression = 'temperature_average'
    pythonAnnotation2.UpdatePipeline()
    string = FetchData(pythonAnnotation2)[0].GetRowData().GetAbstractArray(0).GetValue(0)
    mean_T = annotate2value(string)*AreaSquare/AreaCirc
    pythonAnnotation2.Expression = 'dpm_diam_average'
    pythonAnnotation2.UpdatePipeline()
    string = FetchData(pythonAnnotation2)[0].GetRowData().GetAbstractArray(0).GetValue(0)
    mean_dpdiam = annotate2value(string)*AreaSquare/AreaCirc
    pythonAnnotation2.Expression = 'dpm_mass_average'
    pythonAnnotation2.UpdatePipeline()
    string = FetchData(pythonAnnotation2)[0].GetRowData().GetAbstractArray(0).GetValue(0)
    mean_dpmass = annotate2value(string)*AreaSquare/AreaCirc
    pythonAnnotation2.Expression = 'dpm_u_average'
    pythonAnnotation2.UpdatePipeline()
    string = FetchData(pythonAnnotation2)[0].GetRowData().GetAbstractArray(0).GetValue(0)
    mean_dpu = annotate2value(string)*AreaSquare/AreaCirc

    # Destroy objects
    Delete(pythonAnnotation2)
    del pythonAnnotation2
    Delete(integrateVariables2)
    del integrateVariables2
    Delete(clip1)
    del clip1
    Delete(pythonAnnotation1)
    del pythonAnnotation1
    Delete(integrateVariables1)
    del integrateVariables1
    Delete(slice1)
    del slice1
    Delete(temporalStatistics1)
    del temporalStatistics1
    Delete(db)
    del db

    ### save data
    print("Saving data")
    with open('u_avg.txt','a') as f:
        f.write(f"{fnames[-2-ts][-10:-5]} {mean_u}\n")

    with open('YH2O_avg.txt','a') as f:
        f.write(f"{fnames[-2-ts][-10:-5]} {mean_YH2O}\n")

    with open('temperature_avg.txt','a') as f:
        f.write(f"{fnames[-2-ts][-10:-5]} {mean_T}\n")

    with open('dpdiam_avg.txt','a') as f:
        f.write(f"{fnames[-2-ts][-10:-5]} {mean_dpdiam}\n")

    with open('dpmass_avg.txt','a') as f:
        f.write(f"{fnames[-2-ts][-10:-5]} {mean_dpmass}\n")

    with open('dpu_avg.txt','a') as f:
        f.write(f"{fnames[-2-ts][-10:-5]} {mean_dpu}\n")
