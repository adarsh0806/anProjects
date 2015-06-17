import numpy as np 
import pandas as pd
#In scikit-learn a random split into training and test sets can be quickly computed with 
#the train_test_split helper function.
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import pprint

df = pd.read_excel("rollingsales_manhattan.xls", skiprows = 4, nrows = 15)
#print df.head()
dfTrain, dfTest = train_test_split(df, test_size = 0.2)
print "dfTrain: \n"
pprint.pprint(dfTrain)
print "dfTest: \n"
pprint.pprint(dfTest)
true_labels = dfTest[:,2]
#print "true_labels: \n", true_labels

# for k in range(1,20):
# 	model = KNeighborsClassifier(n_neighbors = 3)
# 	model.fit(dfTrain[:,:2])

'''
mylist[X:Y]
X is the index of the first element you want.
Y is the index of the first element you don't want.

'''

r = []


# print dfTrain[:,:2]
# print "\n\n"
# print dfTrain[:,2]
# print "\n\n"
# print dfTrain
