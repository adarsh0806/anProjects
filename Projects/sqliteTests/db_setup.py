import sqlite3
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
           ('Portland', 2013, 'July ','December',  63),
           ('San Francisco', 2013, 'September', 'December', 64),
           ('Los Angeles', 2013, 'September', 'December',  75))
with con:
	cur = con.cursor()
	# cur.execute("create table weather (city text, year integer, warm_month text, cold_month text, average_high integer)")
	# cur.executemany("INSERT INTO weather VALUES(?,?,?,?,?)", weather)
	# cur.execute("CREATE TABLE cities (name text, state text)")
	# cur.executemany("INSERT INTO cities VALUES(?,?)", cities)
	cur.execute("select warm_month, avg(average_high) from weather group by warm_month")
    
    # select c.name, c.state, w.average_high 
    # from cities c, weather w order by state 
    # inner join weather 
    # on c.name = w.city
    # group by c.state 
    # order by w.average_high DESC

    # SELECT warm_month, AVG(average_high) 
    # FROM weather 
    # GROUP BY warm_month 
    # HAVING AVG(average_high) > 65;

    select distinct c.name, c.state 
    from cities c, weather w
    inner join weather 
    on c.name = w.city and w.warm_month = 'July'
    


    SELECT warm_month, AVG(average_high) 
    FROM weather 
    GROUP BY warm_month 
    HAVING AVG(average_high) > 65;



