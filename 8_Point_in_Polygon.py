# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 13:51:16 2018



@author: cscuser
"""

import geopandas as gpd
# %matplotlib inline
import matplotlib.pyplot as plt
gpd.io.file.fiona.drvsupport.supported_drivers['KML'] = 'rw'

fp = "c:/users/cscuser/documents/exercises/L4_data/PKS_suuralue.kml"
fpa = "c:/users/cscuser/documents/exercises/L4_data/addresses.shp"

polys = gpd.read_file(fp, driver='KML')
data = gpd.read_file(fpa)

polys.plot()

# Select 'Eteläinen' district (Southern)
southern = polys.loc[polys['Name']=='Eteläinen']
southern.reset_index(drop=True, inplace=True)

# Create plot
# PITAA AJAA KERRALLA! eli Run F5
ax = polys.plot(facecolor='gray');
print(ax)
southern.plot(ax=ax1, facecolor='red');
data.plot(ax=ax, color='blue', markersize=5);
plt.tight_layout()

southern.plot(ax=ax, facecolor='red');
