import re
import glob
import sys
sys.path.append("/home/diego/Software/VisIt/visit2.12.1/src/lib/site-packages/")

from visit import *
Launch(vdir="/home/diego/Software/VisIt/visit2.12.1/src/bin")


numbers = re.compile(r'(\d+)')
def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts


input_folder = "/home/diego/run/paper01/mathisen_2008/"
output_folder = input_folder+"results/data/"

cases = [
         'case01',
         'case02',
         'case03',
         'case04',
         'case05',
         'case09',
         'case10'
         ]

sims = [
        '1way_ke',
#        '2way_ke',
#        '4way_ke'
       ]

variables = [
             'w_particle_average',
             'w_average',
             'p_concentration',
             'w_particle_rms'
             ]

l1 = [(0.0, -0.042/2, 2.0),
      (0.0, 0.042/2, 2.0)]
locations = [l1]


for case in cases:

    for sim in sims:

        filename = input_folder+case+"/"+sim+'/01_VISIT/'+sim+'_*_average.case'
        for db in sorted(glob.glob(filename), key=numericalSort):
            print "Current File Being Processed is: " + db

            aux = [int(x) for x in numbers.findall(db)]
            timestep = str(aux[-1]).zfill(6)

            OpenDatabase(db)

            for variable in variables:

                i = 0

                for location in locations:

                    i+=1

                    LineoutAtts = LineoutAttributes()
                    LineoutAtts.point1 = location[0]
                    LineoutAtts.point2 = location[1]
                    LineoutAtts.samplingOn = 1
                    LineoutAtts.numberOfSamplePoints = 1000

                    AddPlot("Curve", "operators/Lineout/"+variable)
                    SetOperatorOptions(LineoutAtts, 1)
                    DrawPlots()
                    e = ExportDBAttributes()
                    e.filename = sim+'_'+case+'_'+timestep+'_'+variable
                    e.dirname = output_folder
                    e.db_type = "Curve2D"
                    ExportDatabase(e)

                    DeleteAllPlots()

            CloseDatabase(db)
