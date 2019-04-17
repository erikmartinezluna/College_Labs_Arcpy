#Title: List Arcshape Files
#Description: This script will list the arcgis shapefiles within a given workspace
#Input: The ws location (wk4_data)
#Output: An output text file which will have the shapefiles listed
#Author: Erik Martinez Luna
#Date: 9/23/2016

import arcpy

#Use get parameter as text for the 1st element (0) for the file path to the workspace that is being worked out of the wk4_data

ws = arcpy.GetParameterAsText(0)
fname = arcpy.GetParameterAsText(1)
arcpy.env.workspace = ws

arcpy.AddMessage('This is Erik. Here is my Week 4 Assignment!')

#Get the name of all shapefiles in the workspace directory 
allFeatures = arcpy.ListFeatureClasses()

f_handle = open(fname, 'w')

for item in allFeatures:
    desc = arcpy.Describe(item)
    name = desc.name
    shapetype = desc.shapeType
    coordsys = desc.spatialReference.name
    arcpy.AddMessage('This %s feature is named %s with a coordinate system of %s\n' % (shapetype, name, coordsys))
    f_handle.write('This %s feature is named %s with a coordinate system of %s\n' % (shapetype, name, coordsys))

f_handle.close()
    
    



