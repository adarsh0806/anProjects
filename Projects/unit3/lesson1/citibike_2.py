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
print r.json()

