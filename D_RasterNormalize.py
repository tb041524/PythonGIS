# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 10:28:52 2018

@author: cscuser
"""

import numpy as np

def normalize(array):
    """
    Normalizes numpy arrays into scale 0.0 ... 1.0
    """
    array_min, array_max = array.min(), array.max()
    return((array - array_min) / (array_max - array_min) )
