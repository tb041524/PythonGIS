# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 15:19:06 2018

@author: cscuser
"""

from shapely.geometry import Point, MultiPoint
from shapely.ops import nearest_points
import geopandas as gpd


def nearest(row, geom_union, df1, df2, geom1_col='geometry', geom2_col='geometry', src_column=None):
    """
    Find the nearest point and return the corresponding value from specified column.
    geom_union : shapely.MultiPoint
    df1 : Source ? 
    df2 : From ? 
    Suoritus: Valitse koko funktio ja F9
    """

    # Find the geometry that is closest
    # [1] -- Closest than itself
    nearest = df2[geom2_col] == nearest_points(row[geom1_col],geom_union)[1]

    # Get the corresponding value from df2 (matching is based on the geometry)
    value = df2[nearest][src_column].get_values()[0]

    return value


#
    
fp1 = "C:/Users/cscuser/Documents/Exercises/L4_data/PKS_suuralue.kml"
fp2 = "C:/Users/cscuser/Documents/Exercises/L4_data/addresses.shp"

gpd.io.file.fiona.drvsupport.supported_drivers['KML'] = 'rw'

polys = gpd.read_file(fp1)
src_points = gpd.read_file(fp2)

polys.plot()
src_points.plot()

unary_union =  src_points.unary_union
print(unary_union)

polys['centroid'] = polys.centroid


polys['nearest_id'] = polys.apply(nearest, geom_union=unary_union, 
     df1=polys, df2=src_points, geom1_col='centroid', src_column='id', axis=1)

polys['nearest_iidee'] = polys.apply(nearest, geom_union=unary_union, 
     df1=polys, df2=src_points, geom1_col='centroid', src_column='id', axis=1)
