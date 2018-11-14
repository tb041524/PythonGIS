# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 15:04:24 2018

@author: cscuser
"""

import rasterio
import matplotlib.pyplot as plt
import numpy as np

# Specify the path for Landsat TIF on AWS
url = 'http://landsat-pds.s3.amazonaws.com/c1/L8/042/034/LC08_L1TP_042034_20170616_20170629_01_T1/LC08_L1TP_042034_20170616_20170629_01_T1_B4.TIF'

# data stream
src = rasterio.open(url)
print(src.profile)

# List of overviews, 
oviews = src.overviews(1)
oview = oviews[-1]
print(oviews)
print(oview)

# Read the thumbnail
thumbnail = src.read(1, out_shape=(1, int(src.height // oview), int(src.width // oview)))
print('array type: ',type(thumbnail))
print(thumbnail)
show(thumbnail, cmap='terrain')
plt.imshow(thumbnail)

# Convert the values into float
thumbnail = thumbnail.astype('f4')
# Convert 0 values to NaNs
thumbnail[thumbnail==0] = np.nan
show(thumbnail, cmap='terrain')
plt.imshow(thumbnail)

# MLS F9 
plt.imshow(thumbnail)
plt.colorbar()
plt.title('Overview - Band 4 {}'.format(thumbnail.shape))
plt.xlabel('Column #')
plt.ylabel('Row #')
           
window = rasterio.windows.Window(1024, 1024, 1280, 2560)
subset = src.read(1, window=window)
subset = subset.astype('f4')
subset[subset==0] = np.nan
show(subset, cmap='terrain')

# SYKE data
fp = 'http://landsat-pds.s3.amazonaws.com/c1/L8/042/034/LC08_L1TP_042034_20170616_20170629_01_T1/LC08_L1TP_042034_20170616_20170629_01_T1_B4.TIF'

           
# ---- Older version

# See the profile
with rasterio.open(url) as src:        print(src.profile)

%matplotlib inline
# Open the COG
with rasterio.open(url) as src:
    # List of overviews from biggest to smallest
    oviews = src.overviews(1)

    # Retrieve the smallest thumbnail
    oview = oviews[-1]
    print('Decimation factor= {}'.format(oview))
    # NOTE this is using a 'decimated read' (http://rasterio.readthedocs.io/en/latest/topics/resampling.html)
    thumbnail = src.read(1, out_shape=(1, int(src.height // oview), int(src.width // oview)))

print('array type: ',type(thumbnail))
print(thumbnail)

plt.imshow(thumbnail)
plt.colorbar()
plt.title('Overview - Band 4 {}'.format(thumbnail.shape))
plt.xlabel('Column #')
plt.ylabel('Row #')
           
           