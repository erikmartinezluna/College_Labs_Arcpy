import arcpy, os, math

ws = arcpy.GetParameterAsText(0)
bands_strings = arcpy.GetParameterAsText(1)

arcpy.env.workspace = ws

bands = bands_strings.split(',')

allRas = arcpy.ListRasters()

uniques = []
procRas = []
outRas = []
arcpy.env.overwriteOutput = True
for item in allRas:
    if uniques.count(item.split('_')[0]) == 0:
        uniques.append(item.split('_')[0])

for unique in uniques:
    myfile = open(os.path.join(ws,unique+'_MTL.txt'),'r')
    myfile_data = myfile.read()
    myfile.close()
    myfile_lines = myfile_data.split('\n')
    for band in bands:
        for thisline in myfile_lines:
            if thisline.count('REFLECTANCE_MULT_BAND_'+band) > 0:
                rasmult = float(thisline.split(' ')[-1])
            elif thisline.count('REFLECTANCE_ADD_BAND_'+band) > 0:
                rasadd = float(thisline.split(' ')[-1])
            elif thisline.count('SUN_ELEVATION') > 0:
                sune = float(thisline.split(' ')[-1])
            else:
                continue
            
        ras = arcpy.sa.Raster(os.path.join(ws,unique+'_B'+band+'.tif'))
        rasRef = (ras*rasmult)+rasadd
        rasSRef = rasRef/math.sin(sune*(3.1415927/180))
        rasSRef.save(os.path.join(ws,unique+'_C'+band+'.tif'))
        procRas.append(os.path.join(ws,unique+'_C'+band+'.tif'))
    arcpy.management.CompositeBands(procRas,os.path.join(ws,unique+'eml.tif'))
    outRas.append(os.path.join(ws,unique+'eml.tif'))
    procRas = []

arcpy.SetParameter(2,';'.join(outRas))
