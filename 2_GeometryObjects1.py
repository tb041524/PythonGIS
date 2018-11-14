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

# PISTE

# Create point objects with a constructor
point1 = Point(2.2, 4.2)
point2 = Point(7.2, -25.1)
point3 = Point(9.26, -2.456)
point3D = Point(9.26, -2.4, 0.57)

print(point3D)
print("point3D:", type(point3D))

point_coords = point1.centroid
print(point_coords)


point_coords = point1.coords
print(point_coords)
xy = point1.xy
print(xy)

x = point1.x
y = point1.y
print(x,y )

point_dist = point1.distance(point2)
print(point_dist)

point_buffer = point1.buffer(20)

# VIIVA

line1 = LineString( [point1, point2, point3] )
print(line1)

line2 = LineString( [ (2.2, 7.3), (2.4, 4.5), (2.5, 7.8)  ] )
print(line2)
# Coordinates
lxy = line1.xy
print(lxy)
lxy = line2.xy
print(lxy)
print(line1.xy[0], line1.xy[1])

l_length = line1.length
print(l_length)
print(l_length, line1.centroid)
centroid1 = line1.centroid

# POLYGON

poly1 = Polygon( [ (1.0,1.0), (2.0,2.0), (3.0,1.0) ] )
print(poly1)

# Pisteita kayttaen - List of coordinates
point_list = [point1, point2, point3, Point(6,7) ]

# List comprehension
poly2 = Polygon( [ [ p.x, p.y ] for p in point_list ] )

poly_type = poly1.geom_type
print(poly_type)

poly_area = poly2.area
print(poly_area)
poly_centroid = poly2.centroid
print(poly_centroid)
poly_bbox = poly2.bounds
print(poly_bbox)

from shapely.geometry import box
bbox = box(*poly_bbox)

poly_exterior = poly1.exterior
poly_ext_len = poly1.exterior.length

hole = [[ (0.2,0.2), (0.3,0.5), (0.6,0.6), (0.4,0.4)  ]]
world_exterior = [ (0,0), (0,1), (1,1), (1,0)]
wpoly = Polygon(shell=world_exterior, holes= hole)




print("end")

