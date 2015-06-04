import requests
import pprint
#Getting Data into a DataFrame
from pandas.io.json import json_normalize
import matplotlib.pyplot as plt
import pandas as pd

r = requests.get('http://www.citibikenyc.com/stations/json')
#pprint.pprint(r.json())
#pprint.pprint(r.json()['stationBeanList'])
#get a list of the keys in the json file

key_list = []
for station in r.json()['stationBeanList']:
	for key in station.keys():
		if key not in key_list:
			key_list.append(key)
pprint.pprint(key_list)

#Getting Data into a DataFrame
df = json_normalize(r.json()['stationBeanList'])
#print df
#Checking the range of values
df['availableBikes'].hist()
#plt.show()
df['totalDocks'].hist()
#plt.show()
#checking which stations are in service and which aren't
count_nis = 0
count_is = 0
for val in df['statusValue']:
	if val == 'Not In Service':
		count_nis += 1
	else:
		count_is += 1
print "Number of Stations not in service: ", count_nis
print "Number of Stations in service: ", count_is
#mean and median number bikes in dock
print "Mean number of available Bikes: ",df['availableBikes'].mean()
print "Median number of available Bikes: ",df['availableBikes'].median()
#change in mean/median when when we do not consider the not in service stations
total_bikes_is = 0
total_bikes = 0
for i in df['availableBikes']:
	total_bikes = int(i) + total_bikes
print "Total number of bikes amongst all stations: ", total_bikes

#error here, wrong calculation
# for val in df['statusValue']:
# 	if val == 'In Service':
# 		for i in df['availableBikes']:
# 			total_bikes_is = int(i) + total_bikes_is
mean_bikes_in_service = df[(df['statusValue'] == 'In Service')]['availableBikes'].mean()
median_bikes_in_service = df[(df['statusValue'] == 'In Service')]['availableBikes'].median()

print "Mean of bikes amongst stations only in service: ",mean_bikes_in_service
print "Median of bikes amongst stations only in service: ",median_bikes_in_service



