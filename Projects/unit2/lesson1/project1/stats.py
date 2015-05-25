import pandas as pd

data = '''Region, Alcohol, Tobacco
North, 6.47, 4.03
Yorkshire, 6.13, 3.76
Northeast, 6.19, 3.77
East Midlands, 4.89, 3.34
West Midlands, 5.63, 3.47
East Anglia, 4.52, 2.92
Southeast, 5.89, 3.20
Southwest, 4.79, 2.71
Wales, 5.27, 3.53
Scotland, 6.08, 4.51
Northern Ireland, 4.02, 4.56'''

data = data.splitlines()
#data.split('\n')
#print data
data = [i.split(', ') for i in data]
col_names = data[0]
#print "col_names",col_names
data_rows = data[1::]
df = pd.DataFrame(data_rows, columns = col_names)

df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

print "\nThe mean Alcohol consumption is:",df['Alcohol'].mean() 
print "\nThe median Alcohol consumption is:",df['Alcohol'].median()
#stats.mode(df['Alcohol']) 

print "\nThe mean Tobacco consumption is:",df['Tobacco'].mean() 
print "\nThe median Tobacco consumption is:",df['Tobacco'].median() 
#stats.mode(df['Tobacco']) 

max(df['Alcohol']) - min(df['Alcohol'])

print "\nThe standard deviation Alcohol consumption is:",df['Alcohol'].std() 
print "\nThe variance Alcohol consumption is:",df['Alcohol'].var() 


max(df['Tobacco']) - min(df['Tobacco'])

df['Tobacco'].std() 

df['Tobacco'].var() 
































