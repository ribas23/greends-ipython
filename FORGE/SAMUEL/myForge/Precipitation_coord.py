#ass8.py
import netCDF4 as nc
import numpy as np
import myFunctions as mf

ds =nc.Dataset("nome ficheiro")

in_lat = 38.568
in_lon = -9.720

lat_values = ds.variables['lat'][:]
lon_values = ds.variables['lon'][:]
prec_values = ds.variables['WDEP_PREC'][:]
prec = ds.variables['WDEP_PREC']


# closest indexes from lat 38.568, lon -9.720:

lat_index = mf.nearest_index(38.568, lat_values)
lon_index = mf.nearest_index(-9.720, lon_values)

print(lat_index)
print(lon_index)

#Precipitation for lat_index, lon_index
print("A precipitação nas coordenadas %f,%f é:" %(lat_index,lon_index), prec_values[0, lat_index, lon_index], prec.units)