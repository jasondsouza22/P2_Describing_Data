import arcpy
import os

# Path to the file gdb
file_GDB_path =r"D:\Second Year\Sem 3\Programming_for_GIS_III\P2_Describing_Data\Practical_2_ProProject\02_Describing_Data.gdb"

majorAttraction_fc_name = "MajorAttractions"
freeways_fc_name = "Freeways"

majorAttraction_fc_full_path = os.path.join(file_GDB_path, majorAttraction_fc_name)
freeways_fc_full_path = os.path.join(file_GDB_path, freeways_fc_name)

print(majorAttraction_fc_full_path)
print(freeways_fc_full_path)

# Creating a Describe object
majorAttractions_desc_obj = arcpy.Describe(majorAttraction_fc_full_path)
freeways_desc_obj = arcpy.Describe(freeways_fc_full_path)


# Printing the type of shape
print("The type of shape is a {}".format(majorAttractions_desc_obj.shapeType))
print("The type of shape is a {}".format(freeways_desc_obj.shapeType))