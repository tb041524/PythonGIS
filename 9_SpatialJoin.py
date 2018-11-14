# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 14:46:09 2018

@author: cscuser
"""

# https://github.com/geopandas/geopandas/issues/830
import os
os.environ["PROJ_LIB"] = "C:\ProgramData\Miniconda3\envs\py35\Library\share" #windows

import geopandas as gpd

# Filepath
fp = "C:/Users/cscuser/Documents/Exercises/L4_data/Vaestotietoruudukko_2015.shp"

# Read the data
pop = gpd.read_file(fp)

# See the first rows
pop.head()

# Change the name of a column
pop = pop.rename(columns={'ASUKKAITA': 'pop15'})
# See the column names and confirm that we now have a column called 'pop15'
pop.columns
# Columns that will be sected
selected_cols = ['pop15', 'geometry']
# Select those columns
pop = pop[selected_cols]
# Let's see the last 2 rows
pop.head()

# Addresses filpath
addr_fp = "C:/Users/cscuser/Documents/Exercises/L4_data/addresses.shp"
# Read data
addresses = gpd.read_file(addr_fp)
# Check the head of the file
addresses.head()

# Do they match? - We can test that
# assert addresses.crs == pop.crs
# Re-project addresses to the projection of the population layer:
print(pop.crs)
print(addresses.crs)
addresses = addresses.to_crs(pop.crs)

#-------
import geopandas as gpd

# https://github.com/geopandas/geopandas/issues/830
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

# Plot the points with population info
join.plot(column='pop15', cmap="Reds", markersize=70, scheme='quantiles', legend=True);

# Add title
plt.title("Amount of inhabitants living close the the point");

# Remove white space around the figure
plt.tight_layout()
