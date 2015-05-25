import sqlite3
import pandas as pd 

con = sqlite3.connect('getting_started.db')

cities = (('Las Vegas', 'NV'),
    	  ('Atlanta', 'GA'))
weather = (('Las Vegas', 2013, 'July', 'December'),
    	   ('Atlanta', 2013, 'July', 'January'))


with con:
	cur = con.cursor()
	cur.execute("select * from cities")
	rows = cur.fetchall()
	cols = [desc[0] for desc in cur.description]
	df = pd.DataFrame(rows, columns = cols)
	print df
	# cur.execute("CREATE TABLE cities (name text, state text)")
	# cur.execute("create table weather (city text, year integer, warm_month text, cold_month text)")
	# cur.executemany("INSERT INTO cities VALUES(?,?)", cities)
 #    cur.executemany("INSERT INTO weather VALUES(?,?,?,?)", weather)
 #    cur.execute("INSERT INTO weather VALUES('Washington', 2013, 'July', 'January')")
 #    cur.execute("INSERT INTO weather VALUES('Houston', 2013, 'July', 'January')")
	# # cur.execute('select sqlite_version()')
	# # data = cur.fetchone()
	# # print 'sqlite version', data
	
	# cur.execute("INSERT INTO cities VALUES('Houston', 'TX')")
	# cur.execute("INSERT INTO cities VALUES('Washington', 'DC')")
    
    

