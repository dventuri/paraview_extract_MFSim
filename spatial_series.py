# before using in cluster6: ml paraview
# execute in pvpython

### IMPORTS
import glob
import re
import numpy as np
from paraview.simple import *


### GLOBAL DEFINITIONS
base_dir = "/home/dventuri/run/recap_14m_keps_np10_coll_coal_ssd_atmzrepar"
# base_dir = "/home/dventuri/run/repar_30m_keps_np10_coll_coal_ssd_atmz"
base_fname = f"{base_dir}/output/ns_output_ct.*.hdf5"
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

# convert python annotation strings to numerical values
def annotate2value(annotation_string):
    value = float(annotation_string[1:-1])  #remove brackets "[...]"
    return value


### FILENAMES
# generate list of filenames to read (numerically sorted and only above timestep threshold)
fnames = sorted(glob.glob(base_fname), key=numericalSort)   #sorts the list of names using the converted numbers
fnames = [fname for fname in fnames if timestep_above(fname, timestep_treshold)]


### PARAVIEW

# create a new 'VisItChomboReader'
db = VisItChomboReader(FileName=fnames[-1]) #use only last timestep
print("Reading timestep ", fnames[-1][-10:-5])

# Properties modified on db
db.PointArrayStatus = ['u', 'Y_H2O', 'temperature', 'density']

xs = np.linspace(0.1, 13.9, 139)  # 0.1m
# xs = np.linspace(0.1, 29.9, 150)    # 0.2m
for count, x in enumerate(xs):

    print('Plane at x = ', round(x,2), ' m')

    # Slice
    slice1 = Slice(Input=db)
    slice1.SliceType = 'Plane'
    slice1.SliceType.Origin = [x, 0.5, 0.5]

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
    clip1.ClipType.Radius = 0.295275
    # clip1.ClipType.Radius = 0.32065

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
    pythonAnnotation2.Expression = 'u'
    pythonAnnotation2.UpdatePipeline()
    string = FetchData(pythonAnnotation2)[0].GetRowData().GetAbstractArray(0).GetValue(0)
    area_u = annotate2value(string)*AreaSquare/AreaCirc
    pythonAnnotation2.Expression = 'Y_H2O'
    pythonAnnotation2.UpdatePipeline()
    string = FetchData(pythonAnnotation2)[0].GetRowData().GetAbstractArray(0).GetValue(0)
    area_YH2O = annotate2value(string)*AreaSquare/AreaCirc
    pythonAnnotation2.Expression = 'temperature'
    pythonAnnotation2.UpdatePipeline()
    string = FetchData(pythonAnnotation2)[0].GetRowData().GetAbstractArray(0).GetValue(0)
    area_T = annotate2value(string)*AreaSquare/AreaCirc
    pythonAnnotation2.Expression = 'density'
    pythonAnnotation2.UpdatePipeline()
    string = FetchData(pythonAnnotation2)[0].GetRowData().GetAbstractArray(0).GetValue(0)
    area_rho = annotate2value(string)*AreaSquare/AreaCirc

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

    ### save data recap
    print("Saving data")
    with open('/home/dventuri/repos/paraview_extract_MFSim/recap_14m_keps_np10_coll_coal_ssd_atmzrepar/recap_u_planes.txt','a') as f:
        f.write(f"{round(x,2)} {area_u}\n")

    with open('/home/dventuri/repos/paraview_extract_MFSim/recap_14m_keps_np10_coll_coal_ssd_atmzrepar/recap_YH2O_planes.txt','a') as f:
        f.write(f"{round(x,2)} {area_YH2O}\n")

    with open('/home/dventuri/repos/paraview_extract_MFSim/recap_14m_keps_np10_coll_coal_ssd_atmzrepar/recap_temperature_planes.txt','a') as f:
        f.write(f"{round(x,2)} {area_T}\n")

    with open('/home/dventuri/repos/paraview_extract_MFSim/recap_14m_keps_np10_coll_coal_ssd_atmzrepar/recap_rho_planes.txt','a') as f:
        f.write(f"{round(x,2)} {area_rho}\n")

    ### save data repar
    # print("Saving data")
    # with open('/home/dventuri/repos/paraview_extract_MFSim/repar_30m_keps_np10_coll_coal_ssd_atmz/repar_u_planes.txt','a') as f:
    #     f.write(f"{round(x,2)} {area_u}\n")

    # with open('/home/dventuri/repos/paraview_extract_MFSim/repar_30m_keps_np10_coll_coal_ssd_atmz/repar_YH2O_planes.txt','a') as f:
    #     f.write(f"{round(x,2)} {area_YH2O}\n")

    # with open('/home/dventuri/repos/paraview_extract_MFSim/repar_30m_keps_np10_coll_coal_ssd_atmz/repar_temperature_planes.txt','a') as f:
    #     f.write(f"{round(x,2)} {area_T}\n")

    # with open('/home/dventuri/repos/paraview_extract_MFSim/repar_30m_keps_np10_coll_coal_ssd_atmz/repar_rho_planes.txt','a') as f:
    #     f.write(f"{round(x,2)} {area_rho}\n")
