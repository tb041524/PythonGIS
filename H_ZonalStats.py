# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 13:53:32 2018

@author: cscuser
"""

import rasterio
from rasterio.plot import show
from rasterstats import zonal_stats
import osmnx as ox
import geopandas as gpd
import os
import matplotlib.pyplot as plt
%matplotlib inline

# File path
data_dir = "Exercises\L5_data"
dem_fp = os.path.join(data_dir, "Helsinki_DEM2x2m_Mosaic.tif")

# Read the Digital Elevation Model for Helsinki
dem = rasterio.open(dem_fp)
dem
show(dem)
show(dem, cmap='terrain')

# See Nominativ OSM
# https://nominatim.openstreetmap.org/


kallio_q = "Kallio, Helsinki, Finland"
pihlajamaki_q = "Pihlajamäki, Malmi, Helsinki, Finland"
lauttasaari_q = "Lauttasaari, Helsinki, Finland"
pitajanmaki_q = "Pitäjänmäki, Helsinki, Finland"
tapiola_q =  = "Tapiola, Espoo, Finland"

# Retrieve the geometries of those areas using osmnx
kallio = ox.gdf_from_place(kallio_q)
pihlajamaki = ox.gdf_from_place(pihlajamaki_q)
lauttasaari = ox.gdf_from_place(lauttasaari_q)
pitajanmaki = ox.gdf_from_place(pitajanmaki_q)
tapiola = ox.gdf_from_place(tapiola_q)

# Reproject to same coordinate system as the
kallio = kallio.to_crs(crs=dem.crs)
pihlajamaki = pihlajamaki.to_crs(crs=dem.crs)
lauttasaari = lauttasaari.to_crs(crs=dem.crs)
pitajanmaki = pitajanmaki.to_crs(crs=dem.crs)
tapiola = tapiola.to_crs(crs=dem.crs)

print(type(kallio))
type(kallio)
kallio.plot()
pihlajamaki.plot()
lauttasaari.plot()
pitajanmaki.plot()

# Plot the Polygons on top of the DEM
# MultiLineSelection - F9
ax = kallio.plot(facecolor='None', edgecolor='red', linewidth=2)
ax = pihlajamaki.plot(ax=ax, facecolor='None', edgecolor='blue', linewidth=2)
ax = lauttasaari.plot(ax=ax, facecolor='None', edgecolor='orange', linewidth=2)
ax = pitajanmaki.plot(ax=ax, facecolor='None', edgecolor='orange', linewidth=2)
# Plot DEM
show((dem, 1), ax=ax)

# Read the raster values
array = dem.read(1)
# Get the affine
affine = dem.transform
print(affine)

# Calculate zonal statistics for Kallio (korkeus mp)
zs_kallio = zonal_stats(kallio, array, affine=affine, stats=['min', 'max', 'mean', 'median', 'majority'])
# Calculate zonal statistics for Pihlajamäki
zs_pihla = zonal_stats(pihlajamaki, array, affine=affine, stats=['min', 'max', 'mean', 'median', 'majority'])
zs_lautta = zonal_stats(lauttasaari, array, affine=affine, stats=['min', 'max', 'mean', 'median', 'majority'])
zs_pitaja = zonal_stats(pitajanmaki, array, affine=affine, stats=['min', 'max', 'mean', 'median', 'majority'])
zs_tapiola = zonal_stats(tapiola, array, affine=affine, stats=['min', 'max', 'mean', 'median', 'majority'])

print(zs_kallio)
print(zs_pihla)
print(zs_lautta)
print(zs_pitaja)
# print(zs_tapiola)

if (zs_kallio[0]['max'] >  zs_pihla[0]['max'] ):
    print('kallio')
else:
    print('pihla')
    

print(zs_kallio)
print(zs_kallio[0])
zs_kallio.append('abc')
print(zs_kallio)
print(zs_kallio[1])

