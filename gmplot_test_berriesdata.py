from gmplot import gmplot
import pandas as pd 
import numpy as np


# column_names = ['timestamp', 'latitude', 'longitude', 'total_berries', 'total_rpc', 'rpc_drop']
# names=column_names

df2 = pd.read_csv('berry.csv', names=['timestamp', 'latitude', 'longitude', 'work_cell', 'total_rpc', 'rpc_drop', 'errorcode'], na_values=['NaN','#N/A'], skip_blank_lines=True)

df = df2.dropna(subset=['longitude'])

# print df

# lat_float = pd.Series(df['latitude'], dtype='float')
# lon_float = pd.Series(df['longitude'], dtype='float')

# # Place map by taking the first value of the coordinates list, where the shift starts, and using it as the center of the google map

start_lat = df['latitude'].iloc[0]
start_lon = df['longitude'].iloc[0]

gmap = gmplot.GoogleMapPlotter(start_lat, start_lon, 15)

# Draw polygon by creating a blank list to be populated using a for loop scraping the CSV file.  

latplots = []
lonplots = []

for i in df['latitude']: 
	latplots.append(i)

for j in df['longitude']: 
	lonplots.append(j)

print latplots
print lonplots

gmap.plot(latplots, lonplots, 'white', edge_width=2)


# Scatter points of errors in the field, using error codes highlighted in the CSV 

error_latplots = [] 
error_lonplots = []

error_latitude = df.loc[df['errorcode'] >0,'latitude']
error_longitude = df.loc[df['errorcode'] >0,'longitude']

for a in error_latitude:
	error_latplots.append(a)

for b in error_longitude:
	error_lonplots.append(b)

print error_latplots
print error_lonplots

gmap.scatter(error_latplots, error_lonplots, '#3B0B39', size=5, marker=False)


# Using the last coordinate to show where we parked the tractor 

parked_lat = df['latitude'].iloc[-1]
parked_lon = df['longitude'].iloc[-1]

gmap.marker(parked_lat, parked_lon, 'cornflowerblue')

# Heatmap code can support many gps coordinates

gmap.heatmap(latplots, lonplots)

# gmap.heatmap(error_latplots, error_lonplots)


# Draw
gmap.draw("my_berry_map_data.html")
