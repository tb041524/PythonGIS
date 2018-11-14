# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 15:25:43 2018

@author: cscuser
"""

# Importoidaan vain nama (luokkia?)
from shapely.geometry import Point, LineString, Polygon

import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

fp = "exercises/L2_data/Europe_borders.shp"

data = gpd.read_file(fp)

print(data.crs)

# data.plot()

geo = data.copy()
geo = geo.to_crs(epsg=3035)

data.plot()
geo.plot()

# Create subplots
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(12,8))
ax1.set_title("WGS84")
ax2.set_title("Lambert Azimuthal")
data.plot(ax=ax1, facecolor='gray')
geo.plot(ax=ax2, facecolor='red')
plt.savefig("projs.png", dpi=300)

outfp = "exercises/L2_data/Europe_borders_3035.gjson"
geo.to_file(outfp, driver="GeoJSON")

# Voi olla tarpeen, jos herjaa ajettava pycrs korjaus/uudelleenasennus?
import pycrs
proj4 = pycrs.parser.from_epsg_code(3035).to_proj4()
proj4
