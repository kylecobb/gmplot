from gmplot import gmplot
import pandas as pd 
import numpy as np
import json 

def getJSON(fileName):
	with open(fileName, 'r') as fn:
		return json.load(fn)	

berrydata = getJSON('./berrydata2.json')

# # Place map by taking the first value of the coordinates list, where the shift starts, and using it as the center of the google map

start_lat = berrydata["berrydata"][0]['lat']
start_lon = berrydata["berrydata"][0]['lon']

gmap = gmplot.GoogleMapPlotter(start_lat, start_lon, 15)

# Draw polygon by creating a blank list to be populated using a for loop scraping the CSV file.  

latplots = []
lonplots = []

for i in berrydata['berrydata']: 
	latplots.append((i['lat']))

for j in berrydata['berrydata']: 
	lonplots.append(j['lon'])

print latplots
print lonplots

gmap.plot(latplots, lonplots, 'white', edge_width=2)


# Scatter points of errors in the field, using error codes highlighted in the CSV 


# error_list = []

# for item in berrydata:
# 	for error in berrydata['berrydata']:
# 			error_list.append(error['error'])

# print error_list

# error_latplots = []
# error_lonplots = []

# for datapoint in error_list: 
# 	if datapoint > 0: 	
# 		error_latplots.append(datapoint)
		
		
# print error_latplots
# print error_lonplots

# gmap.scatter(error_latplots, error_lonplots, '#3B0B39', size=5, marker=False)


# Using the last coordinate to show where we parked the tractor 

parked_lat = berrydata["berrydata"][-1]['lat']
parked_lon = berrydata["berrydata"][-1]['lon']

gmap.marker(parked_lat, parked_lon, 'cornflowerblue')

# Heatmap code can support many gps coordinates

gmap.heatmap(latplots, lonplots)

# gmap.heatmap(error_latplots, error_lonplots)


# Draw
gmap.draw("json_map.html")
