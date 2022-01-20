# trace generated using paraview version 5.9.0

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'VisItChomboReader'
# base_dir = "/home/dventuri/st_euler/sp_5x5_CoF_forced_evap/output"
glob.glob(filename)
ns_output_ct000100 = VisItChomboReader(
    FileName=glob.glob("/home/dventuri/st_euler/sp_5x5_CoF_forced_evap/output/ns_output_ct.0001*.hdf5"
)
#https://discourse.paraview.org/t/selecting-multiple-pvtu-files/2537/6
# """
#         f'{base_dir}\s_output_ct.000100000.hdf5',
#         f'{base_dir}\s_output_ct.000100100.hdf5',
#         f'{base_dir}\s_output_ct.000100200.hdf5'
#     """
ns_output_ct000100.MeshStatus = ['Mesh']
ns_output_ct000100.PointArrayStatus = []

# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# Properties modified on ns_output_ct000100
ns_output_ct000100.PointArrayStatus = ['dpm_diam', 'temperature']

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
ns_output_ct000100Display = Show(ns_output_ct000100, renderView1, 'AMRRepresentation')

# trace defaults for the display properties.
ns_output_ct000100Display.Representation = 'Outline'
ns_output_ct000100Display.ColorArrayName = [None, '']
ns_output_ct000100Display.SelectTCoordArray = 'None'
ns_output_ct000100Display.SelectNormalArray = 'None'
ns_output_ct000100Display.SelectTangentArray = 'None'
ns_output_ct000100Display.OSPRayScaleArray = 'dpm_diam'
ns_output_ct000100Display.OSPRayScaleFunction = 'PiecewiseFunction'
ns_output_ct000100Display.SelectOrientationVectors = 'None'
ns_output_ct000100Display.ScaleFactor = 0.10000000000000005
ns_output_ct000100Display.SelectScaleArray = 'None'
ns_output_ct000100Display.GlyphType = 'Arrow'
ns_output_ct000100Display.GlyphTableIndexArray = 'None'
ns_output_ct000100Display.GaussianRadius = 0.005000000000000003
ns_output_ct000100Display.SetScaleArray = ['POINTS', 'dpm_diam']
ns_output_ct000100Display.ScaleTransferFunction = 'PiecewiseFunction'
ns_output_ct000100Display.OpacityArray = ['POINTS', 'dpm_diam']
ns_output_ct000100Display.OpacityTransferFunction = 'PiecewiseFunction'
ns_output_ct000100Display.DataAxesGrid = 'GridAxesRepresentation'
ns_output_ct000100Display.PolarAxes = 'PolarAxesRepresentation'
ns_output_ct000100Display.ScalarOpacityUnitDistance = 0.009086965540189068

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
ns_output_ct000100Display.ScaleTransferFunction.Points = [-0.00012592176034472542, 0.0, 0.5, 0.0, 0.0019275920162844288, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
ns_output_ct000100Display.OpacityTransferFunction.Points = [-0.00012592176034472542, 0.0, 0.5, 0.0, 0.0019275920162844288, 1.0, 0.5, 0.0]

# reset view to fit data
renderView1.ResetCamera()

# get the material library
materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Extract AMR Blocks'
extractAMRBlocks1 = ExtractAMRBlocks(registrationName='ExtractAMRBlocks1', Input=ns_output_ct000100)

# Properties modified on extractAMRBlocks1
extractAMRBlocks1.SelectedDataSets = [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0, 11, 0, 12, 0, 13, 0, 14, 0, 15]

# show data in view
extractAMRBlocks1Display = Show(extractAMRBlocks1, renderView1, 'UniformGridRepresentation')

# trace defaults for the display properties.
extractAMRBlocks1Display.Representation = 'Outline'
extractAMRBlocks1Display.ColorArrayName = [None, '']
extractAMRBlocks1Display.SelectTCoordArray = 'None'
extractAMRBlocks1Display.SelectNormalArray = 'None'
extractAMRBlocks1Display.SelectTangentArray = 'None'
extractAMRBlocks1Display.OSPRayScaleArray = 'dpm_diam'
extractAMRBlocks1Display.OSPRayScaleFunction = 'PiecewiseFunction'
extractAMRBlocks1Display.SelectOrientationVectors = 'None'
extractAMRBlocks1Display.ScaleFactor = 0.10000000000000005
extractAMRBlocks1Display.SelectScaleArray = 'None'
extractAMRBlocks1Display.GlyphType = 'Arrow'
extractAMRBlocks1Display.GlyphTableIndexArray = 'None'
extractAMRBlocks1Display.GaussianRadius = 0.005000000000000003
extractAMRBlocks1Display.SetScaleArray = ['POINTS', 'dpm_diam']
extractAMRBlocks1Display.ScaleTransferFunction = 'PiecewiseFunction'
extractAMRBlocks1Display.OpacityArray = ['POINTS', 'dpm_diam']
extractAMRBlocks1Display.OpacityTransferFunction = 'PiecewiseFunction'
extractAMRBlocks1Display.DataAxesGrid = 'GridAxesRepresentation'
extractAMRBlocks1Display.PolarAxes = 'PolarAxesRepresentation'
extractAMRBlocks1Display.ScalarOpacityUnitDistance = 0.047247039371057765
extractAMRBlocks1Display.OpacityArrayName = ['POINTS', 'dpm_diam']
extractAMRBlocks1Display.SliceFunction = 'Plane'
extractAMRBlocks1Display.Slice = 10

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
extractAMRBlocks1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 0.0015660851738388808, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
extractAMRBlocks1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 0.0015660851738388808, 1.0, 0.5, 0.0]

# init the 'Plane' selected for 'SliceFunction'
extractAMRBlocks1Display.SliceFunction.Origin = [0.25000000000000006, 0.5000000000000002, 0.5000000000000002]

# hide data in view
Hide(ns_output_ct000100, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(extractAMRBlocks1Display, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
extractAMRBlocks1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'vtkBlockColors'
vtkBlockColorsLUT = GetColorTransferFunction('vtkBlockColors')

# get opacity transfer function/opacity map for 'vtkBlockColors'
vtkBlockColorsPWF = GetOpacityTransferFunction('vtkBlockColors')

# create a new 'Temporal Statistics'
temporalStatistics1 = TemporalStatistics(registrationName='TemporalStatistics1', Input=extractAMRBlocks1)

# show data in view
temporalStatistics1Display = Show(temporalStatistics1, renderView1, 'UniformGridRepresentation')

# trace defaults for the display properties.
temporalStatistics1Display.Representation = 'Outline'
temporalStatistics1Display.ColorArrayName = [None, '']
temporalStatistics1Display.SelectTCoordArray = 'None'
temporalStatistics1Display.SelectNormalArray = 'None'
temporalStatistics1Display.SelectTangentArray = 'None'
temporalStatistics1Display.OSPRayScaleArray = 'dpm_diam_average'
temporalStatistics1Display.OSPRayScaleFunction = 'PiecewiseFunction'
temporalStatistics1Display.SelectOrientationVectors = 'None'
temporalStatistics1Display.ScaleFactor = 0.10000000000000005
temporalStatistics1Display.SelectScaleArray = 'None'
temporalStatistics1Display.GlyphType = 'Arrow'
temporalStatistics1Display.GlyphTableIndexArray = 'None'
temporalStatistics1Display.GaussianRadius = 0.005000000000000003
temporalStatistics1Display.SetScaleArray = ['POINTS', 'dpm_diam_average']
temporalStatistics1Display.ScaleTransferFunction = 'PiecewiseFunction'
temporalStatistics1Display.OpacityArray = ['POINTS', 'dpm_diam_average']
temporalStatistics1Display.OpacityTransferFunction = 'PiecewiseFunction'
temporalStatistics1Display.DataAxesGrid = 'GridAxesRepresentation'
temporalStatistics1Display.PolarAxes = 'PolarAxesRepresentation'
temporalStatistics1Display.ScalarOpacityUnitDistance = 0.047247039371057765
temporalStatistics1Display.OpacityArrayName = ['POINTS', 'dpm_diam_average']
temporalStatistics1Display.SliceFunction = 'Plane'
temporalStatistics1Display.Slice = 10

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
temporalStatistics1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 0.0015259095652783283, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
temporalStatistics1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 0.0015259095652783283, 1.0, 0.5, 0.0]

# init the 'Plane' selected for 'SliceFunction'
temporalStatistics1Display.SliceFunction.Origin = [0.25000000000000006, 0.5000000000000002, 0.5000000000000002]

# hide data in view
Hide(extractAMRBlocks1, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(temporalStatistics1Display, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
temporalStatistics1Display.SetScalarBarVisibility(renderView1, True)

# create a new 'Slice'
slice1 = Slice(registrationName='Slice1', Input=temporalStatistics1)
slice1.SliceType = 'Plane'
slice1.HyperTreeGridSlicer = 'Plane'
slice1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Origin = [0.25000000000000006, 0.5000000000000002, 0.5000000000000002]

# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice1.HyperTreeGridSlicer.Origin = [0.25000000000000006, 0.5000000000000002, 0.5000000000000002]

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.4999, 0.5000000000000002, 0.5000000000000002]

# show data in view
slice1Display = Show(slice1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
slice1Display.Representation = 'Surface'
slice1Display.ColorArrayName = [None, '']
slice1Display.SelectTCoordArray = 'None'
slice1Display.SelectNormalArray = 'None'
slice1Display.SelectTangentArray = 'None'
slice1Display.OSPRayScaleArray = 'dpm_diam_average'
slice1Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice1Display.SelectOrientationVectors = 'None'
slice1Display.ScaleFactor = 0.1
slice1Display.SelectScaleArray = 'None'
slice1Display.GlyphType = 'Arrow'
slice1Display.GlyphTableIndexArray = 'None'
slice1Display.GaussianRadius = 0.005
slice1Display.SetScaleArray = ['POINTS', 'dpm_diam_average']
slice1Display.ScaleTransferFunction = 'PiecewiseFunction'
slice1Display.OpacityArray = ['POINTS', 'dpm_diam_average']
slice1Display.OpacityTransferFunction = 'PiecewiseFunction'
slice1Display.DataAxesGrid = 'GridAxesRepresentation'
slice1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
slice1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 0.0014731827857373855, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
slice1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 0.0014731827857373855, 1.0, 0.5, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(slice1Display, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# set scalar coloring
ColorBy(slice1Display, ('POINTS', 'dpm_diam_average'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(vtkBlockColorsLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
slice1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'dpm_diam_average'
dpm_diam_averageLUT = GetColorTransferFunction('dpm_diam_average')

# get opacity transfer function/opacity map for 'dpm_diam_average'
dpm_diam_averagePWF = GetOpacityTransferFunction('dpm_diam_average')

# save data
SaveData(f'{base_dir}/test.csv', proxy=slice1, PointDataArrays=['dpm_diam_average', 'dpm_diam_maximum', 'dpm_diam_minimum', 'dpm_diam_stddev', 'temperature_average', 'temperature_maximum', 'temperature_minimum', 'temperature_stddev'])

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

# get layout
layout1 = GetLayout()

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1554, 796)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [0.25, 0.5, 3.397777478867205]
renderView1.CameraFocalPoint = [0.25, 0.5, 0.5]
renderView1.CameraParallelScale = 0.75

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
