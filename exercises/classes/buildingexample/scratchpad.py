# this is our implementation code
from shed import Shed

garden_shed = Shed(2) #this is an instance of Shed and inherits the properties of building and shed
garden_shed.upc = "98790987773892"

tool_shed = Shed(3)
garden_shed.upc = "9123455789"

print("The garden shed has " + str(garden_shed.windows) + " windows.")
print("The tool shed has " + str(tool_shed.windows) + " windows.")
print("The garden shed has " + str(garden_shed.doors) + " door.")