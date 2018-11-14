# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 10:28:26 2018

@author: cscuser
"""

# Import necessary modules
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

from geopandas.tools import geocode

# Filepath
fp = "Exercises/L3_data/addresses.txt"

# Read the data
data = pd.read_csv(fp, sep=';')

dathttps://automating-gis-processes.github.io/CSC/notebooks/L1/geometric-objects.htmla.head()

geo = geocode(data['addr'], provider='nominatim', user_agent='csc_user_ht')
geo.head(2)

join = geo.join(data)
join.head()

joined = join.head()

geo.plot()
joined.plot()

# Adding a background map to plots
# http://geopandas.org/gallery/plotting_basemap_background.html