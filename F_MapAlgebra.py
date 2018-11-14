# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 13:01:58 2018

@author: cscuser
"""

import rasterio
import numpy as np
from rasterio.plot import show
import os
import matplotlib.pyplot as plt
%matplotlib inline

# Data dir
data_dir = "Exercises\L5_data"

# Filepath
fp = os.path.join(data_dir, "Helsinki_masked_p188r018_7t20020529_z34__LV-FIN.tif")

# Open the raster file in read mode
raster = rasterio.open(fp)

# Read red channel (channel number 3)
red = raster.read(3)
# Read NIR channel (channel number 4)
nir = raster.read(4)

# Calculate some stats to check the data
# https://stackoverflow.com/questions/34439/finding-what-methods-a-python-object-has
[method_name for method_name in dir(red)  if callable(getattr(red, method_name))]
print(red.mean())
print(nir.mean())
print(type(nir))


# Visualize
show(nir, cmap='terrain')

red = red.astype('f4')
nir = nir.astype('f4')
nir
np.seterr(divide='ignore', invalid='ignore')

# Calculate NDVI using numpy arrays
ndvi = (nir - red) / (nir + red)
%matplotlib inline
# Plot the NDVI
plt.imshow(ndvi, cmap='terrain_r')
# Add colorbar to show the index
# F5 tai multilineselection
plt.colorbar()

# -----

a = [1,2,3,4]
np.mean(a)
np.mean([1,2,3,4])
type(a)
# https://stackoverflow.com/questions/34439/finding-what-methods-a-python-object-has
[method_name for method_name in dir(red)  if callable(getattr(red, method_name))]
