"""
CODE FOR FINDING AREA OF A CIRCLE
"""
rad = float(input("Input the radius of the circle: "))   #input for radius which is converted to float type

area = (22/7) * rad * rad                                #area is calculated using formula for area of a circle 

print("Area of the circle with radius {} is: {}".format(rad,area))          #the area of the circle is displayed along with the radius






"""
CODE FOR IDENTIFING THE EXTENSION FOR GIVEN FILENAME
"""

fname = input("Input file name: ")   #input for file name

i=0                                  #iteration variable initialisation

for x in fname:                      #loop to find position from where extension starts
  if x==".":
    var = i
    break
  else:
    i+=1

var = len(fname)                     #variable for length of the filename

ext = fname[i:var]                   #variable to store extension seperately

if ext == ".py":                     #if/else to find the right extension of the file
  print("Extension of this file is: Python")
elif ext == ".c":
   print("Extension of this file is: C")
elif ext == ".cpp":
   print("Extension of this file is: C++")
elif ext == ".html" or ".htm":
   print("Extension of this file is: HTML")
elif ext == ".xlsx":
   print("Extension of this file is: Excel")
else:
  print("Filename unidentified!")