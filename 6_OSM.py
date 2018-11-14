# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 11:19:20 2018

@author: cscuser
"""

import osmnx as ox
import matplotlib.pyplot as plt
# %matplotlib inline
# %matplotlib auto


# Specify the name that is used to seach for the data
place_name = "Kamppi, Helsinki, Finland"

# Specify the name that is used to seach for the data
place_name = "Kamppi, Helsinki, Finland"
# Fetch OSM street network from the location
graph = ox.graph_from_place(place_name)

# Fetch OSM street network from the location
# graphx = ox.graph_from_place(place_name)
graph = ox.graph_from_place(place_name)
type(graph)

fig, ax = ox.plot_graph(graph)

nodes, edges = ox.graph_to_gdfs(graph)

buildings = ox.buildings_from_address(place_name, 1000)
buildings.plot()

footprint = ox.gdf_from_place(place_name)
footprint.plot()

restaurants= ox.pois_from_place(place_name, amenities=['restaurant'])
restaurants.plot()

# Plot all layers together
ax = footprint.plot(facecolor='black')
edges.plot(ax=ax, linewidth=1, edgecolor='#FF0000')
#buildings.plot(ax=ax, facecolor='khaki', alpha=0.7)
#restaurants.plot(ax=ax, color='green', alpha=0.7, markersize=10)
acc.plot(column="nb_pt_r_tt", linewidth=0, legend=True)
plt.tight_layout()

 
# Plot the footprint
# PITAA AJAA KERRALLA! eli Run F5

ax = footprint.plot(facecolor='black')
plt.savefig('foo.png', bbox_inches='tight')
# Plot street edges
edges.plot(ax=ax, linewidth=1, edgecolor='#BC8F8F')
# Plot buildings
buildings.plot(ax=ax, facecolor='khaki', alpha=0.7)
# Plot restaurants
restaurants.plot(ax=ax, color='green', alpha=0.7, markersize=10)
plt.tight_layout()

print(ax)
