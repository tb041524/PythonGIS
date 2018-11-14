# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 13:22:29 2018

@author: cscuser
"""

import rasterio
from rasterio.merge import merge
from rasterio.plot import show
import matplotlib.pyplot as plt
import glob
import os
%matplotlib inline

# File and folder paths
dirpath = "Exercises\L5_data"
out_fp = os.path.join(dirpath, "Helsinki_DEM2x2m_Mosaic.tif")

# Make a search criteria to select the DEM files
search_criteria = "L*.tif"
q = os.path.join(dirpath, search_criteria)
print(q)
# glob function can be used to list files from a directory with specific criteria
dem_fps = glob.glob(q)
# Files that were found:
dem_fps

src_files_to_mosaic = [ rasterio.open(fp) for fp in dem_fps  ]
src_files_to_mosaic
show(src_files_to_mosaic[0], cmap='terrain')
show(src_files_to_mosaic[1], cmap='terrain')
show(src_files_to_mosaic[2], cmap='terrain')

mosaic, out_trans = merge(datasets = src_files_to_mosaic)
show(mosaic, cmap='terrain')

out_meta = src_files_to_mosaic[0].meta.copy()
out_meta
# Update metadata:  dimensions, crs
out_meta.update({"driver": "GTiff",
                 "height": mosaic.shape[1],
                 "width": mosaic.shape[2],
                 "transform": out_trans,
                 "crs": "+proj=utm +zone=35 +ellps=GRS80 +units=m +no_defs "
                 }
                )
out_meta

# Write the mosaic raster to disk
with rasterio.open(out_fp, "w", **out_meta) as dest:    dest.write(mosaic)


# ----

# Eitoimi, proj? - Toimii
m = rasterio.open(out_fp)
plt.imshow(m.read(1), cmap='terrain')
# Add colorbar to show the index
# F5 tai multilineselection
plt.colorbar()
