# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 09:13:18 2018

TB 2018-11-13

@author: cscuser
"""

# Importoidaan vain nama (luokkia?)
from shapely.geometry import Point, LineString, Polygon

import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

import requests 
import geojson
import pycrs


# fp = "exercises/L2_data/Europe_borders.shp"

url = "http://geo.stat.fi/geoserver/vaestoruutu/wfs"

capabilities_params = dict(service='WFS', request='GetCapabilities')
capabilities = requests.get(url, params=capabilities_params)
print(capabilities.content)
params = dict(service='WFS', version='2.0.0', request='GetFeature', typeName='vaestoruutu:vaki2017_5km', outputFormat='json')

r = requests.get(url, params=params)
print(type(r))
data = gpd.GeoDataFrame.from_features(geojson.loads(r.content))

data.crs = pycrs.parser.from_epsg_code(3067).to_proj4


# -------

import geopandas as gpd
import requests
import geojson

# Specify the url for the backend
url = 'http://geo.stat.fi/geoserver/vaestoruutu/wfs'

# Specify parameters (read data in json format)
params = dict(service='WFS', version='2.0.0', request='GetFeature',
         typeName='vaestoruutu:vaki2017_5km', outputFormat='json')

# Fetch data from WFS using requests
r = requests.get(url, params=params)

# Create GeoDataFrame from geojson
data = gpd.GeoDataFrame.from_features(geojson.loads(r.content))

print(data.crs)

# 
#    Double click variable in the variable explorer
#    Double click the attribute with type core.frame.DataFrame
# data

