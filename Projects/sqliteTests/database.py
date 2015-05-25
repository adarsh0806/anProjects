import sqlite3
import pandas as pd
con = sqlite3.connect('getting_started.db')
cities = (('Las Vegas', 'NV'),
    	  ('Atlanta', 'GA'),
    	  ('New York City', 'NY'),
    	  ('Boston', 'MA'),
          ('Chicago', 'IL'),
          ('Miami', 'FL'),
          ('Dallas', 'TX'),
          ('Seattle', 'WA'),
          ('Portland', 'OR'),
          ('San Francisco', 'CA'),
          ('Los Angeles', 'CA'))
weather = (('New York City',2013,'July','January',62),
  		   ('Boston',2013,'July','January',59),
           ('Chicago', 2013, 'July', 'January' ,59),
           ('Seattle', 2013,'July', 'January',  61),
     	   ('Miami', 2013, 'August',  'January', 84),
           ('Dallas',2013, 'July', 'January', 77),
           ('Portland', 2013, 'July','December',  63),
           ('San Francisco', 2013, 'September', 'December', 64),
           ('Los Angeles', 2013, 'September', 'December',  75))
with con:
	cur = con.cursor()
	cur.execute("drop table if exists cities")
	cur.execute("drop table if exists weather")
	#DB Setup
	cur.execute("CREATE TABLE weather (city text, year integer, warm_month text, cold_month text, average_high integer)")
	cur.executemany("INSERT INTO weather VALUES(?,?,?,?,?)", weather)
	cur.execute("CREATE TABLE cities (name text, state text)")
	cur.executemany("INSERT INTO cities VALUES(?,?)", cities)
	#Query execution
	cur.execute("select distinct c.name, c.state from cities c, weather w inner join weather on c.name = w.city and w.warm_month = 'July'")
	rows = cur.fetchall()
	cols = [desc[0] for desc in cur.description]
	#Loading into dataframe
	df1 = pd.DataFrame(rows, columns = cols)
	print "The cities that are warmest in July are:" 
	print df1['name']+ ", " +df1['state']+ ";"



