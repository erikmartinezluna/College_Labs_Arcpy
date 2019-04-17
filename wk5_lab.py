#Title: Create Raster Objects
#Description: 
#Input: 
#Output: 
#Author: Erik Martinez Luna
#Date: 9/30/2016


import arcpy, os

inras = arcpy.GetParameterAsText(0)
outshape = arcpy.GetParameterAsText(1)

ws = os.path.split(outshape)
arcpy.env.workspace = ws[0]

ras1 = arcpy.sa.Raster(inras)

arcpy.AddMessage('Raster Mean: %3.3f' % (ras1.mean))
arcpy.AddMessage('Raster Max: %3.3f' % (ras1.maximum))
arcpy.AddMessage('Raster Min: %3.3f' % (ras1.minimum))
arcpy.AddMessage('Raster StdDev: %3.3f' % (ras1.standardDeviation))

ras2 = ras1 > 3.0

ras3 = arcpy.sa.Shrink(ras2,1,1)

ras4 = arcpy.sa.Expand(ras3,1,1)

arcpy.conversion.RasterToPolygon(ras4,outshape,'NO_SIMPLIFY')

uCurs = arcpy.da.UpdateCursor(outshape,['shape@'])

i = 0

for item in uCurs:
    if item[0].area > 500 or item[0].area < 100:
        uCurs.deleteRow()
        i += 1
del uCurs

arcpy.AddMessage('%d features are deleted!' % (i))


