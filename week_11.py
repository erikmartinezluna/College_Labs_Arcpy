import arcpy
import os

bar_input = arcpy.GetParameterAsText(0)
bar_output = arcpy.GetParameterAsText(1)

pathfile = os.path.split(bar_output)
arcpy.env.workspace = pathfile[0]

bar_handle = open(bar_input, "r")
bar_data = bar_handle.read()
bar_lines = bar_data.split('\n')

arcpy.management.CreateFeatureclass(pathfile[0],os.path.split(bar_output)[1],"POINT")
arcpy.management.AddField(bar_output,"Name","TEXT")
arcpy.management.AddField(bar_output,"PickleShot","Text")

icurs = arcpy.da.InsertCursor(bar_output,["shape@","Name","PickleShot"])

pnt = arcpy.Point()
arcpy.AddMessage("before the loop")

dictPickle = {'0':"No Pickle Shots",'1':"Pickle Shots Bar"}

i = 1
for item in bar_lines:
    arcpy.AddMessage("Enter da loop1")
    if i == 1:
        i = i + 1
        continue 
    if item =='': 
        continue 
    it_sp = item.split(",")
    pnt.X = long(it_sp[4]) 
    pnt.Y = long(it_sp[5])
    icurs.insertRow([pnt,it_sp[2],dictPickle[(it_sp[3])]])

del icurs 

fieldmappings = arcpy.FieldMappings()

fieldmappings.addTable(bar_output)
