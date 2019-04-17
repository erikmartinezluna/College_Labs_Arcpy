#Title: wk3_csv_1.py
#Description: Read and Print CSV
#Input: A CSV file 
#Output: No return. Print CSV file contents to the console 
#Author: Erik Martinez Luna
#Date: 9/16/2016

#Import ArcPy Library
import arcpy

#Read in parameter
infile = arcpy.GetParameterAsText(0)

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
