# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 13:08:48 2018

@author: cscuser

Classifying data
Classification based on common classifiers

"""

import geopandas as gpd
import pysal as ps
import matplotlib.pyplot as plt
%matplotlib inline

fp = "Exercises/L3_data/TravelTimes_to_5975375_RailwayStation_Helsinki.geojson"
data =  gpd.read_file(fp)

data = data.loc[data["pt_r_tt"] >= 0]

data.plot(column="pt_r_tt", scheme="Fisher_Jenks", k=9, cmap="RdYlBu", legend=True, linewidth=0)

k = 12
classifier = ps.Natural_Breaks.make(k=k)
print(classifier)
classifications = data[["pt_r_tt"]].apply(classifier)
# classifications.plot()

classifications = classifications.rename(columns={"pt_r_tt": "nb_pt_r_tt"})

data = data.join(classifications)

# Plot
data.plot(column="nb_pt_r_tt", linewidth=0, legend=True)

# Use tight layout
plt.tight_layout()

ax = data.plot(column="nb_pt_r_tt", linewidth=0, legend=True)
class_bins = [10,20,30,40,50,60]
classifier = 

