#Title: "Hellow Arc! My name is ..." script
#wk2arc_eg.py
#Description: Short script to say hello to arcgis
#Input: 1 short string (First Name)
#Ouput: No return, but will print to the console
#Author: Erik Martinez Luna
#Date: 9/9/2016

import arcpy
firstvar = arcpy.GetParameterAsText(0)
arcpy.AddMessage("Hello ArcGIS! I'm %s!" %(firstvar))
