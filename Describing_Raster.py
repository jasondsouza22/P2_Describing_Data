import arcpy

raster_path = r"D:\Second Year\Sem 3\Programming_for_GIS_III\P2_Describing_Data\Practical_2_ProProject\ASTGTMV003_N19E072_dem.tif"

desc_obj = arcpy.Describe(raster_path)

dataset_type = desc_obj.datasetType
print(dataset_type)

#The number of bands in the raster dataset
print(desc_obj.bandCount)

#Raster dataset format (Possible value are Grid, ERDAS IMAGINE, TIFF
print(desc_obj.format)

#
print(desc_obj.pixelType)