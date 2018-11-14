# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 09:14:04 2018

@author: cscuser
"""

import rasterio
import os
import numpy as np

# Slash / backslash in Windows (esim. \n... escape characters)
# r: "Don't interpret"
data_dir = r"Exercises"
fp = os.path.join(data_dir, "L5_Data", "Helsinki_masked_p188r018_7t20020529_z34__LV-FIN.tif")

print(fp)
print(os.getcwd())
files = os.listdir(data_dir)
for name in files: print(name)
# files = os.listdir(fp)
# for name in files: print(name)

raster = rasterio.open(fp)
print(raster.crs)
raster.transform

raster.bounds
raster.driver
raster.nodatavals
raster.meta

band1 = raster.read(1)
band1.dtype
data_type = str(band1.dtype)

# Read all bands
array = raster.read()
stats = []
# Select lines, F9
for band in array: 
    band_stat = {
        'min': band.min(), 
        'max': band.max(), 
        'median': np.median(band), 
        'mean': band.mean(), 
        'std': band.std()
        }

# Read all bands
stats = []
# Select lines, F9
skip = 4
# for: Tuple
for idx, band in enumerate(array): 
    if ( idx < skip ): 
        print(idx)
        band_stat = {
                'min': band.min(), 
                'max': band.max(), 
                'median': np.median(band), 
                'mean': band.mean(),    
                'std': band.std()
                }
        channel_stat = { 'Channel %s' % (idx+1): band_stat }
    
