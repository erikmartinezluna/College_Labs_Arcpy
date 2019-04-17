# Title: wk8_1.py
# Description: Takes in a csv file, convert it to a point shapefile, assign it to a proper projection
#           then perform a spatial join of that shapefile to an existing polygon file
# Inputs: bar_input is the csv file, structure_input is the existing polygon file (feature class)
# Outputs: two feature classes, bar_output and structure_output
# Author: Lauren Rogers
# Date: 10/21/2016

import arcpy
import os

#Set up inputs
bar_input = arcpy.GetParameterAsText(0)
structure_input = arcpy.GetParameterAsText(1)

#Set up outputs
bar_output = arcpy.GetParameterAsText(2)
structure_output = arcpy.GetParameterAsText(3)

#Set up environment workspace
ws = os.path.split(bar_output)[0]
arcpy.env.workspace = ws[0]

#Open bar input and read opened file to bar_data
bar_handle = open(bar_input, 'r')
bar_data = bar_handle.read()

#Split the csv into lines
bar_lines = bar_data.split('\n')

#Create a blank point shapefile, Create features requires 3 inputs
#(the workspace, the filename, and the type of shapefile)
arcpy.management.CreateFeatureclass(ws,os.path.split(bar_output)[1],'POINT')

#Add two fields to the shapefile to accomodate Name and Pickleshot data
arcpy.management.AddField(bar_output, 'Name', 'TEXT')
arcpy.management.AddField(bar_output, 'Pickleshot', 'SHORT')

#Create an insert cursor from that blank shapefile
icurs = arcpy.da.InsertCursor(bar_output,['shape@','Name','Pickleshot'])
#Create a point object
pnt = arcpy.Point()

#Use a forloop to iterate each line of the file
i = 1
for item in bar_lines:
    if i ==1:
        i += 1
        continue #This is to skip the first row of the file
    if item == '': #double single quotes
        continue #This is to account for the last empty row of the file
    it_sp = item.split(',') #Splits each item into a list by commas
    #arcpy.AddMessage('x = %10.3f y = %10.3f' % (float(it_sp[4]),float(it_sp[5])))
    pnt.X = long(it_sp[4]) #use float() to change the text to a float data type
    pnt.Y = long(it_sp[5])
    icurs.insertRow([pnt,(it_sp[2]),int(it_sp[3])])

#Delete the cursor object
del icurs #necessary to prevent shapefile corruption

#Assign a spatial reference to this data

#Read the spatial reference that is in structure_input
spatial_ref = arcpy.Describe(structure_input).spatialReference

#Assign the spatial ref to the new point shapefile
arcpy.DefineProjection_management(bar_output,spatial_ref)

#Now create a polyline shapefile from the CSV file, join the pointshapefile to the polygon

#Create blank fieldmappings
fieldmappings = arcpy.FieldMappings()

#Add the bar_output (the point file) to the field mappings
fieldmappings.addTable(bar_output)

#Perform the spatial join
arcpy.SpatialJoin_analysis(structure_input, bar_output, structure_output, 'JOIN_ONE_TO_ONE', 'KEEP_COMMON', fieldmappings)

