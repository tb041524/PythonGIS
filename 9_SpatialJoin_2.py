# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 15:13:37 2018

@author: cscuser
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 14:46:09 2018

GitHub: Profile: tb041524 

@author: cscuser
"""

#-------
import geopandas as gpd

# https://github.com/geopandas/geopandas/issues/830
# Error using to_crs() -- no such file or directory
import os
os.environ["PROJ_LIB"] = "C:\ProgramData\Miniconda3\envs\py35\Library\share" #windows

pop_fp = "C:/Users/cscuser/Documents/Exercises/L4_data/Vaestotietoruudukko_2015.shp"
point_fp = "C:/Users/cscuser/Documents/Exercises/L4_data/addresses.shp"
pop = gpd.read_file(pop_fp)
points = gpd.read_file(point_fp)
# assert pop.crs == points.crs
points = points.to_crs(crs=pop.crs)
assert pop.crs == points.crs

# %matplotlib inline
import matplotlib.pyplot as plt

# -------

# Make a spatial join
join = gpd.sjoin(addresses, pop, how="inner", op="within")

# Let's check the result
join.head()

# Output path
outfp = "C:/Users/cscuser/Documents/Exercises/L4_data/addresses_pop15_epsg3979.shp"

# Save to disk
join.to_file(outfp)

# PITAA AJAA KERRALLA! eli Run F5 tai Rivit valittuna ja F9 !!!!
# Plot the points with population info
join.plot(column='IKA30_39', cmap="Reds", markersize=70, scheme='quantiles', legend=True);
# Add title
plt.title("Amount of inhabitants living close the the point");
# Remove white space around the figure
plt.tight_layout()
