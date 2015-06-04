# UNDERLYING MISSION
# The goal is determine the station with the most change in that hour
import time
from dateutil.parser import parse
import collections
import sqlite3 as lite
import requests
'''
 downloads the data, parses the result, and then uploads the data to the database
'''

#connect to the database
con = lite.connect('citi_bike.db')
cur = con.cursor()

#download the data
r = requests.get('http://www.citibikenyc.com/stations/json')
#parse to get the execution time
exec_time = parse(r.json()['executionTime'])

#Insert the data into the database table available_bikes
cur.execute('INSERT INTO available_bikes (execution_time) VALUES (?)', (exec_time.strftime('%s'),))
con.commit()

#create dict id_bikes which has key = station_id, value = number of available bikes in that station
id_bikes = collections.defaultdict(int)
for station in r.json()['stationBeanList']:
	id_bikes[station['id']] = station['available_bikes']

#update the id_bikes dict to set the key = value pair set up 
for k,v in id_bikes.iteritems():
	cur.execute("UPDATE available_bikes SET _" +str(k)+ " = " +str(v)+ " WHERE execution_time = " +exec_time.strftime('%s') + ";") 
con.commit()
time.sleep(60)

con.close()