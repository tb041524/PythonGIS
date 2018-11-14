# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 10:05:46 2018

@author: cscuser
"""


import rasterio
from rasterio.plot import show
from rasterio.plot import show_hist
import os
import numpy as np
import matplotlib.pyplot as plt

# Oma funktio tiedostossa D_RasterNormalize.py, funktio normalize
from D_RasterNormalize import normalize

# Slash / backslash in Windows (esim. \n... escape characters)
# r: "Don't interpret"
data_dir = r"Exercises"
fp = os.path.join(data_dir, "L5_Data", "Helsinki_masked_p188r018_7t20020529_z34__LV-FIN.tif")

print(fp)
print(os.getcwd())
files = os.listdir(data_dir)
for name in files: print(name)
filename = os.path.basename(fp)

raster = rasterio.open(fp)
show((raster, 1))
show((raster, 3))

# Select lines, F9
fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(10,4), sharey=True )
show((raster, 3), cmap='Reds', ax=ax1)
show((raster, 2), cmap='Greens', ax=ax2)
show((raster, 1), cmap='Blues', ax=ax3)

# Composite image
red = raster.read(3)
green = raster.read(2)
blue = raster.read(1)

# Composite normalized image
redn = normalize(red)
greenn = normalize(green)
bluen = normalize(blue)

print(np.mean(green), np.mean(greenn))
print(np.max(green), np.max(greenn))
print(np.std(green), np.std(greenn))
print(np.std(green)/np.mean(green), np.std(greenn)/np.mean(greenn))

rgb = np.dstack((redn, greenn, bluen))
plt.imshow(rgb)

show_hist(raster, bins=50, lw=0.0, stacked=False, alpha=0.3,
      histtype='stepfilled', title="Histogram")