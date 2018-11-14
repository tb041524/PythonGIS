# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 10:59:14 2018

geometric_objects.py

Requirements:
    - shapely
    
Notes:
    - note

Created on ...

@author: cscuser
"""

# Importoidaan vain nama (luokkia?)
from shapely.geometry import Point, LineString, Polygon
import geopandas as gpd
import pandas as pd

# Filepath

fp = "exercises/L2_data/DAMSELFISH_distributions.shp"
data = gpd.read_file(fp)
print(type(data))
cols = data.columns
print(cols)

data.plot()

# Output

outfp = "exercises/L2_data/DAMSELFISH_selection.shp"
outfp_gjson = "exercises/L2_data/DAMSELFISH_selection.geojson"

# Select the first rows

selection = data.head(50)
selection.to_file(outfp)
selection.to_file(outfp_gjson, driver='GeoJSON')

dataout = gpd.read_file(outfp)
dataout.plot()
data.plot()

%matplotlib inline
%matplotlib auto

data.plot()


# Ominaisuustietoja, BINOMIAL on yhdem attribuutin nimi
data.columns
data['geometry'].head(50)
data[['geometry', 'BINOMIAL']].head(50)
sel3 = data[['geometry', 'BINOMIAL']].head(50)
sel3

# select rows based on criteria

unique = data['BINOMIAL'].unique()
unique

criteria = 'Stegastes redemptus'
fish_a = data.loc[data['BINOMIAL']==criteria]
fish_a

# PostGIS, SQL - periaate
"""
import psycopg2
import geoalchemy2
conn, cursor = psycopg2.connect()
gpd.read_postgis(sql="SELECT * FROM TABLEX FETCH FIRST 10 ROWS;", con=conn)
"""

# Iterate over GeoDataFrame

i = 0
for index, row in data.iterrows():
    # Calculate the area of each polygon
    poly_area = row['geometry'].area
    # print("---1: ", i, poly_area)
    # print(row['BINOMIAL'])
    res = str(poly_area)
    res = res + '; ' + row['BINOMIAL']
    print("---2: ", i, index, res)
    i += 1
# data.apply()


def calculate_area(row):
    return row['geometry'].area
data['area2'] = data.apply(calculate_area, axis=1)
data['area2']


data['area3'] = data.area
data['centroid'] = data.centroid

print(data['area3'])

# Talletetaan replace cemtroidit shapefileen

geo = data.copy()
geo = geo.set_geometry('centroid')
geo.plot()
# geo = geo.drop('geometry', axis=1)
# Save points
geo.to_file('geo_centroids.gjson', driver='GeoJSON')

mean_area = data['area2'].mean()
min_area = geo['area2'].min()
max_area = geo['area2'].max()
std_area = geo['area2'].std()
median_area = geo['area2'].median()
print(mean_area, min_area, max_area, std_area, median_area)

# Ei toimi
grouped = data.groupby('BINOMIAL')
print(grouped)
