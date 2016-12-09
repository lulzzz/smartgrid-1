from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element

import xml.etree.ElementTree as etree

#Step 1: Parse through the XML file
tree=etree.parse('home.xml')
root=tree.getroot()

#Step 2: Edit the Current Consumption
y=root.find("CurrentConsumption") #find the element of current consumption
y.text='50' #change it to 72
tree.write(open('home.xml','w')) #write to the XML file

#Step 3: Change the current consumption to a float to process
f=float(y.text)

#Step 4: Confirm that current consumption is a float by adding 10 and printing the result
z=10+f
print z
