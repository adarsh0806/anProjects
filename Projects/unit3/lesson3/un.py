from bs4 import BeautifulSoup
import requests
import pprint
import pandas as pd
import statsmodels.formula.api as smf
import statsmodels.api as sm
import numpy as np

url = "http://web.archive.org/web/20110514112442/http://unstats.un.org/unsd/demographic/products/socind/education.htm"
r = requests.get(url)
soup = BeautifulSoup(r.content)
# for row in soup('table'):
# 	print row
#7th table
s = soup('table')[6]
'''
Create a table with the 
country name, 
the male school life expectancy, 
the female school life expectancy 
the year of the analysis.
'''
df = pd.DataFrame(columns = ['Name', 'Male SLE', 'Female SLE', 'Year'])
for i in s:
	tcont = s.findAll('tr',{'class':'tcont'})
#pprint.pprint(tcont)
for i in tcont:
	td = i.find('td')
	print td