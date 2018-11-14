# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 11:33:58 2018

@author: cscuser
"""

import numpy as np
import json

def get_features(gdf):
    """
    GeodataFrame to rasterio
    """
    features =  return [json.loads(gdf.to_json())['features'][0]['geometry']]
    return features
