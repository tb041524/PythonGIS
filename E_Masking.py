# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 11:09:36 2018

Sekava, ei toim

@author: cscuser
"""

import rasterio
from rasterio.plot import show
from rasterio.mask import mask
from shapely.geometry import box
import geopandas as gpd
import pycrs
import os
os.environ["PROJ_LIB"] = "C:\ProgramData\Miniconda3\envs\py35\Library\share" #windows

data_dir = r"Exercises"
fp = os.path.join(data_dir, "L5_Data", "Helsinki_masked_p188r018_7t20020529_z34__LV-FIN.tif")
print(fp)
print(os.getcwd())
files = os.listdir(data_dir)
for name in files: print(name)
filename = os.path.basename(fp)

out_tif = os.path.join(data_dir, "Helsinki_masked.tif")
raster = rasterio.open(fp)
show((raster, 4), cmap='terrain')

minx, miny = 24.60, 60.00
maxx, maxy = 25.22, 60.35

bbox = box(minx, miny, maxx, maxy)
print(bbox)

crs_code = pycrs.parser.from_epsg_code(4326).to_proj4()
geo = gpd.GeoDataFrame( {'geometry': bbox}, index=[0], crs=crs_code)
# geo = gpd.GeoDataFrame( {'geometry': bbox}, index=[0], crs=from_epsg_code(4326))
print(geo)
print(geo.crs)

# projection to the same as raster
geo = geo.to_crs(crs=raster.crs)
print(raster.crs)
print(geo.crs)


epsg_code = int(data.crs.data['init'][5:])
print(epsg_code)
out_meta.update({"driver": "GTiff",
                 "height": out_img.shape[1],
                 "width": out_img.shape[2],
                 "transform": out_transform,
                 "crs": pycrs.parser.from_epsg_code(epsg_code).to_proj4()}
                         )

# convert  GDF to geom feat dict
from raster_tools import  get_features
coords = get_features(geo)
print(coords)

out_img, out_transform = mask(dataset=raster, shapes=coords, crop=True)
