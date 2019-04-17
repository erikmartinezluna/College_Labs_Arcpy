#Title: wk3_csv_2.py
#Description: Convert CSV content to points
#Input: A CSV file 
#Output: Point ShapeFile 
#Author: Erik Martinez Luna
#Date: 9/16/2016

#Import ArcPy Library
import arcpy, os

#Read in parameter
infile = arcpy.GetParameterAsText(0)
outshape = arcpy.GetParameterAsText(1)
ws = os.path.split(outshape)[0] #gets the path without the filename

#Open CSV file
infile_handle = open(infile, 'r')

#Read CSV file
infile_data = infile_handle.read()

#Split the CSV into lines
infile_lines = infile_data.split('\n')

#For loop will iterate through the list of lines in "infile_lines"
#Splitting each line into by commas
#For loop will then print the contents 

i = 1 #Counter

arcpy.management.CreateFeatureclass(ws,os.path.split(outshape)[1],'POLYLINE')

#Creates an insert cursor from the blank shapefile
icurs = arcpy.da.InsertCursor(outshape,['shape@'])

pnt = arcpy.Point()
ary = arcpy.Array()

for item in infile_lines:
    #Skip the first line 
    if i == 1:
        i = i + 1
        continue #This is to skip the first row in the file
    #End if the last row is empty
    if item == '':
        continue
    it_sp = item.split(',') #splits each item into strings by the commas
    arcpy.AddMessage('x = %3.3f y = %3.3f' % (float(it_sp[0]), float(it_sp[1])))

    pnt.X = float(it_sp[0]) #Use float() to change the txt to a float data type
    pnt.Y = float(it_sp[1])
    ary.add(pnt)

ply = arcpy.Polyline(ary)
icurs.insertRow([ply])


del icurs # this is necessary to prevent shapefile corruption
    






