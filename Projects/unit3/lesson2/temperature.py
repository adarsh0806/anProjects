'''
For this assignment, we're going to be collecting the max temperature in 5 major cities 
in the US over the course of a month and find out which city experienced the largest temperature swings.
'''
import pandas as pd
import datetime
import requests
import pprint
import sqlite3 as lite 
#https://api.forecast.io/forecast/APIKEY/LATITUDE,LONGITUDE,TIME

# cities = {  "Atlanta": '33.762909,-84.422675',
#             "Austin": '30.303936,-97.754355',
#             "Boston": '42.331960,-71.020173',
#             "Chicago": '41.837551,-87.681844',
#             "Cleveland": '41.478462,-81.679435',
#             "Denver": '39.761850,-104.881105',
# 			"Las Vegas": '36.229214,-115.26008',
# 			"Los Angeles":'34.019394,-118.410825',
# 			"Miami":'25.775163,-80.208615',
# 			"Minneapolis":  '44.963324,-93.268320',
# 			"Nashville":'36.171800,-86.785002',
# 			"New Orleans":'30.053420,-89.934502',
# 			"New York":'40.663619,-73.938589',
# 			"Philadelphia":'40.009376,-75.133346',
# 			"Phoenix":'33.572154,-112.090132',
# 			"Salt Lake City":'40.778996,-111.932630',
# 			"San Francisco":'37.727239,-123.032229',
# 			"Seattle":'47.620499,-122.350876',
# 			"Washington":'38.904103,-77.017229'
#         }

cities = { "Atlanta": '33.762909,-84.422675',
            "Austin": '30.303936,-97.754355'
         }

#current date
end_date = datetime.datetime.now()
#30 days prior to today
start_date = end_date - datetime.timedelta(days = 7)

print "Start data (7 days ago): ",start_date
#pprint.pprint(r.json())
con = lite.connect('weather3.db')
cur = con.cursor()


create_table_sql = '''
					CREATE TABLE daily_temp ( 
						day_of_reading INT, 
						city REAL,
						max_temp INT
						)'''
insert_data_sql = '''
					INSERT INTO daily_temp (
								day_of_reading,
								city,
								max_temp)
					VALUES (?,?,?)'''

with con:
	cur.execute('DROP TABLE IF EXISTS daily_temp')
	cur.execute(create_table_sql)
	for k,v in cities.iteritems():
		#while start_date < end_date:
			#querying the API
		coord = v
		url = 'https://api.forecast.io/forecast/6c1bacd950587a34d67f233058710c52/' 
		#r = requests.get(url + coord + ',' + start_date.strftime('%Y-%m-%dT12:00:00'))
		r = requests.get(url + coord)
		
		for i in r.json()['daily']['data']:
			maxtemp = i['temperatureMax']
			time_measured = datetime.datetime.fromtimestamp(int(i['time'])).strftime('%Y-%m-%d %H:%M:%S')
			city = k
			cur.execute(insert_data_sql, (time_measured, city, maxtemp))

	
	x = cur.execute("SELECT day_of_reading,city,max_temp FROM daily_temp;")
	temp_list = []
	for row in x:
		print "Day of reading: ", row[0]
		print "City: ", row[1]
		print "Max temperature : ", row[2]
		

con.close()


