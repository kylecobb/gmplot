import json
from pandas.io.json import json_normalize
from gmplot import gmplot
import pandas as pd 
import numpy as np


def getJSON(fileName):
	with open(fileName, 'r') as fn:
		return json.load(fn)	

berrydata = getJSON('./berrydata2.json')

berrydatadict = berrydata["berrydata"]

dfberry = json_normalize(berrydatadict)

df = dfberry.dropna(subset=['lon'])

# # Place map by taking the first value of the coordinates list, where the shift starts, and using it as the center of the google map

start_lat = df['lat'].iloc[0]
start_lon = df['lon'].iloc[0]

gmap = gmplot.GoogleMapPlotter(start_lat, start_lon, 15)

# Draw polygon by creating a blank list to be populated using a for loop scraping the CSV file.  

latplots = []
lonplots = []

for i in df['lat']: 
	latplots.append(i)

for j in df['lon']: 
	lonplots.append(j)

print latplots
print lonplots

gmap.plot(latplots, lonplots, 'white', edge_width=2)


# Scatter points of errors in the field, using error codes highlighted in the CSV 

error_latplots = [] 
error_lonplots = []

error_latitude = df.loc[df['error'] >0,'lat']
error_longitude = df.loc[df['error'] >0,'lon']

for a in error_latitude:
	error_latplots.append(a)

for b in error_longitude:
	error_lonplots.append(b)

print error_latplots
print error_lonplots

gmap.scatter(error_latplots, error_lonplots, '#3B0B39', size=5, marker=False)


# Using the last coordinate to show where we parked the tractor 

parked_lat = df['lat'].iloc[-1]
parked_lon = df['lon'].iloc[-1]

gmap.marker(parked_lat, parked_lon, 'cornflowerblue')

# Heatmap code can support many gps coordinates

gmap.heatmap(latplots, lonplots)

# gmap.heatmap(error_latplots, error_lonplots)


# Draw
gmap.draw("my_berry_map_data.html")
