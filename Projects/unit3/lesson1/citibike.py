import sqlite3 as lite 
import requests
# a package with datetime objects
import time
# a package for parsing a string into a Python datetime object
from dateutil.parser import parse 
import collections
import pprint
#Getting Data into a DataFrame
from pandas.io.json import json_normalize
import matplotlib.pyplot as plt
import pandas as pd
from time import sleep
import datetime


con = lite.connect('citi_bike.db')
cur = con.cursor()
r = requests.get('http://www.citibikenyc.com/stations/json')
key_list = []
for station in r.json()['stationBeanList']:
    for key in station.keys():
        if key not in key_list:
            key_list.append(key)
pprint.pprint(key_list)
'''
We wont be using the following fields:
u'availableDocks',
u'statusKey',
u'statusValue',
u'lastCommunicationTime',
u'landMark'
'''

#Getting Data into a DataFrame
df = json_normalize(r.json()['stationBeanList'])
#with keyword as a context manager. 
#At the end of the indented code block, the transaction will commit (be saved) to the database.
create_table_sql = '''CREATE TABLE citibike_reference (
                                        id INT PRIMARY KEY,
                                        totalDocks INT,
                                        city TEXT,
                                        altitude INT, 
                                        stAddress2 TEXT,
                                        longitude NUMERIC,
                                        postalCode TEXT,
                                        testStation TEXT,
                                        stAddress1 TEXT,
                                        stationName TEXT,
                                        landMark TEXT,
                                        latitude NUMERIC,
                                        location TEXT)'''
insert_table_sql = '''INSERT INTO citibike_reference (
                                    id, 
                                    totalDocks, 
                                    city, 
                                    altitude, 
                                    stAddress2, 
                                    longitude, 
                                    postalCode, 
                                    testStation, 
                                    stAddress1, 
                                    stationName, 
                                    landMark, 
                                    latitude, 
                                    location) 
                        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)'''
#Create the table                       
with con:
    cur.execute('DROP TABLE IF EXISTS citibike_reference')
    cur.execute(create_table_sql)

#a prepared SQL statement we're going to execute over and over again
#for loop to populate values in the database
with con:
    for station in r.json()['stationBeanList']:
        #id, totalDocks, city, altitude, stAddress2, longitude, postalCode, testStation, stAddress1, stationName, landMark, latitude, location)
        cur.execute(insert_table_sql,(station['id'],station['totalDocks'],station['city'],station['altitude'],station['stAddress2'],station['longitude'],station['postalCode'],station['testStation'],station['stAddress1'],station['stationName'],station['landMark'],station['latitude'],station['location']))

station_ids = df['id'].tolist()
#DEBUG
#print station_ids[0]
#add the '_' to the station name and also add the data type for SQLite
station_ids = ['_' + str(x) + ' INT' for x in station_ids]
#DEBUG
#print station_ids[0]
#create the table of available bikes
#in this case, we're concatentating the string and joining all the station ids 
#(now with '_' and 'INT' added)
with con:
    cur.execute('DROP TABLE IF EXISTS available_bikes')
    cur.execute("CREATE TABLE available_bikes ( execution_time INT, " +  ", ".join(station_ids) + ");")

#take the string and parse it into a Python datetime object
exec_time = parse(r.json()['executionTime'])
#DEBUG
#print exec_time
# create an entry for the execution time
#The function strftime() formats the time. It's alternate is strptime(), which is used to parse a string into the proper time format
with con:
    con.execute('INSERT INTO available_bikes (execution_time) VALUES (?)', (exec_time.strftime('%s'),))
# iterate through the stations in the "stationBeanList"
# defaultdict to store available bikes by station
id_bikes = collections.defaultdict(int)
#loop through the stations in the station list
for station in r.json()['stationBeanList']:
    id_bikes[station['id']] = station['availableBikes']
#DEBUG
#pprint.pprint(id_bikes)

#Now update the values in the defaultdict in the database as the column name can't start with a number
with con:
    for k,v in id_bikes.iteritems():
        #strftime() is formatting the time into what's called Unix time, or Epoch time. It's the number of seconds since 1 January 1970 00:00:00 UTC.
        cur.execute("UPDATE available_bikes SET _" + str(k) + " = " + str(v) + " WHERE execution_time =" + exec_time.strftime('%s') + ";")


#Challenges
#The code then needs to sleep for a minute and then perform the same task
#sleep(60)
#The code only needs to run for an hour. If it's sleeping every minute, the code only needs to loop 60 times

#Analyzing the result
df1 = pd.read_sql_query("SELECT * FROM available_bikes ORDER BY execution_time LIMIT 1", con, index_col = 'execution_time')
pprint.pprint(df1)


'''
Aim: To collect and store the change for each station every minute.
The goal is to record the number of bikes available every minute for an hour across all of 
New York City in order to see which station or set of stations is the most active in New York City 
for that hour. 

Activity is defined as the total number of bicycles taken out or returned in an hour. 
So if 2 bikes are brought in and 4 bikes are taken out, that station has an activity level of 6.

Collect the information(availableBikes) for each station after a repeated interval of 60 seconds. 
How to calculate the activity?
'''

#Process each column to calculate the change at each minute
hour_change = collections.defaultdict(int)
# print df1.columns
# print "df1.index: ",list(df1.index)
for col in df1.columns:
    station_vals = df1[col].tolist() #available bikes per station
    station_ids = col[1:] #trim the "_"
    station_change = 0
    print "station_vals = ",station_vals
    #The enumerate() function returns not only the item in the list but also the index of the item
    for k,v in enumerate(station_vals):
        #k = index of the station
        #v = bikes available
        # print "k = ",k
        # print "len(station_vals) - 1 = ",len(station_vals) - 1
        if k < len(station_vals) - 1:
            station_change += abs(station_vals[k] - station_vals[k+1])
            print "station_change :",station_change
    #station id converted back to integer
    hour_change[int(station_ids)] = station_change   
   
#print hour_change

def key_with_max_val(dic):
    k = list(dic.keys())
    v = list(dic.values())
    return k[v.index(max(v))]

max_station = key_with_max_val(hour_change)

print "max_station: ",max_station

#query sqlite for the reference information
#find the information about the station that has the maximum activity
cur.execute("SELECT id, stationname, latitude, longitude FROM citibike_reference WHERE id = ?", (max_station,))
data = cur.fetchone()
print data

print "The most active station is station id %s at %s latitude: %s longitude: %s " % data
print "With " + str(hour_change[379]) + " bicycles coming and going in the hour between " + datetime.datetime.fromtimestamp(int(df.index[0])).strftime('%Y-%m-%dT%H:%M:%S') + " and " + datetime.datetime.fromtimestamp(int(df.index[-1])).strftime('%Y-%m-%dT%H:%M:%S')

#Visually representing the data
plt.bar(hour_change.keys(), hour_change.values())
plt.show()

