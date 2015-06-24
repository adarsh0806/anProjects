#From Kaggle competition - https://www.kaggle.com/c/sf-crime/data?test.csv.zip
#https://www.kaggle.com/c/digit-recognizer/forums/t/2299/getting-started-python-sample-code-random-forest

##################################### TASK #####################################
#Predict the category of crimes that occurred in San Francisco by the district
#################################################################################

import numpy as np
import pandas as pd
import seaborn as sns
import ggplot
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier

'''
Data fields:
Dates - timestamp of the crime incident
Category - category of the crime incident (only in train.csv). This is the target variable you are going to predict.
Descript - detailed description of the crime incident (only in train.csv)
DayOfWeek - the day of the week
PdDistrict - name of the Police Department District
Resolution - how the crime incident was resolved (only in train.csv)
Address - the approximate street address of the crime incident 
X - Longitude
Y - Latitude

Ones that are needed:
Category -> target variable that needs to be predicted
PdDistrict


Plot Legend

Crime Category:
0 - asault
1 - burglary
2 - drunkenness
3 - larceny/theft
4 - non criminal
5 - other offenses
6 - robbery
7 - suspicious occ
8 - vandalism
9 - vehicle theft
10 - warrants
11 - weapon laws

District:
0 - Bayview
1 - Central
2 - Ingleside
3 - Mission
4 - Northern
5 - Park
6 - Richmond
7 - Southern
8 - Taraval
9 - Tenderloin
'''
#DATA SET - https://www.kaggle.com/c/sf-crime/data
dfTest = pd.read_csv('test.csv', header = 0, nrows = 100)
dfTrain = pd.read_csv('train.csv', header = 0, nrows = 100)

#Cleaning the data
#Drop columns that won't be used
dfTrain = dfTrain.drop(['Dates', 'DayOfWeek', 'Resolution', 'X','Y', 'Address','Descript'], axis = 1)
dfTest = dfTest.drop(['Dates', 'DayOfWeek','X','Y','Address'], axis = 1)

# convert string values to dummy variables
dfTrain['Category'] = pd.Categorical(dfTrain.Category).codes
dfTrain['PdDistrict'] = pd.Categorical(dfTrain.PdDistrict).codes
dfTest['PdDistrict'] = pd.Categorical(dfTest.PdDistrict).codes

#Making prediction of Crime by District using Random Forest ML Algorithm
rforest = RandomForestClassifier(n_estimators = 100)
training_set = dfTrain.ix[:,'Category':]
target = dfTrain['Category']
#Fit the district and the crime category
rforest = rforest.fit(training_set, target)
#Predict the district based on the crime
output = rforest.predict(dfTrain.ix[:,'Category':])
#Make the prediction readable
dfOut = pd.DataFrame(dfTest['PdDistrict'].values, columns = ['PdDistrict'])
dfOut['Category'] = output

#Visualization of the predicted model
plt.figure()
plt.title('Crime Prediction by District')
plt.ylabel('Category of Crime')
plt.xlabel('District in San Francisco')
plt.bar(dfOut['PdDistrict'], dfOut['Category'])
plt.show()

##################################### ANALYSIS #####################################
#Based on the algorithm our prediction of the category of crimes that occurred in 
#San Francisco by the district are:
####################################################################################
'''
Based on the algorithm our prediction of the category of crimes that occurred in San Francisco by the district are:

Bayview 	- 	warrants	
Central 	- 	warrants
Ingleside 	- 	warrants
Mission 	- 	vandalism
Northern 	- 	vehicle theft
Park 		- 	other offenses
Richmond 	- 	warrants
Southern	-	warrants
Taraval		-	weapon laws
Tenderloin	-	non criminal
'''