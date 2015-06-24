#From Kaggle competition - https://www.kaggle.com/c/sf-crime/data?test.csv.zip
#Predict the category of crimes that occurred in San Francisco by the district
#https://www.kaggle.com/c/digit-recognizer/forums/t/2299/getting-started-python-sample-code-random-forest

import numpy as np
import pandas as pd
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


#Random Forest
rforest = RandomForestClassifier(n_estimators = 100)
training_set = dfTrain.ix[:,'Category':]
target = dfTrain['Category']
#Fit the district and the crime category
rforest = rforest.fit(training_set, target)
#Predict the district based on the crime
output = rforest.predict(dfTrain.ix[:,'Category':])
#Make the prediction readable
dfOut = pd.DataFrame(dfTest['PdDistrict'].values, columns = ['District'])
dfOut['Category'] = output

print dfOut.head()


