import numpy as np 
import pandas as pd
#In scikit-learn a random split into training and test sets can be quickly computed with 
#the train_test_split helper function.
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import pprint

#read data in
df = pd.read_excel("rollingsales_manhattan.xls", skiprows = 4, nrows = 15)

#split data into training and test sets
dfTrain, dfTest = train_test_split(df, test_size = 0.2)

# true_labels = dfTest[:,8]
# print "true_labels: \n", true_labels

'''
mylist[X:Y]
X is the index of the first element you want.
Y is the index of the first element you don't want.
[start:end:step] # start through not past end, by step
'''
knn_features = ['Area','Type']
l = len(knn_features)

#training data
print "training data: ",dfTrain[:,:l]
#target values
print "target values :",dfTrain[:,l]

#find the best k for KNN
#UNSURE + ERRORS HERE
for k in range(1,20):
	model = KNeighborsClassifier(n_neighbors = k,algorithm = 'auto')
	#fit(X, y) -> Fit the model using X as training data and y as target values
	model.fit(dfTrain[:,:l], dfTrain[:,l])
	#training data is the target values
	expected = dfTest[:,l]
	#target values 
	predicted = model.predict(dfTest[:,:l])
	#misclassification rate
	mr = (predicted != expected).mean()
	print mr
    

