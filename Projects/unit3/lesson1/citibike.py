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














