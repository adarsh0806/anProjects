# we will be using the diamonds data from ggplot
# pandas
# scikit-learn for random forest
import numpy as np
import pandas as pd
import ggplot
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics

'''
https://www.youtube.com/watch?v=loNcrMjYh64
'''
#load and view the diamonds data
df = ggplot.diamonds

#histogram with a line marking $12,000
plt.figure()
plt.hist(df['price'])
plt.axvline(x=12000)
#plt.show()

# build a TRUE/FALSE variable indicating if the price is above
# our threshold
df['expensive'] = 0
df.ix[df['price'] >= 12000, 'expensive'] = 1

# get rid of the price column
df.drop(['price'], axis = 1, inplace = True)

# scikit-learn can't handle strings, so we need to create dummie variables for cut, color, clarity
dfcut = pd.get_dummies(df.cut)
dfcolor = pd.get_dummies(df.color)
dfclarity = pd.get_dummies(df.clarity)

# reorder the columns so that when we grab our train / test we don't include the Expense column
cols = df.columns.tolist()
#last element
# print cols[-1:]
#all but the last element
# print cols[:-1]
cols = cols[-1:] + cols[:-1]
df.drop(['cut','color','clarity'], axis = 1, inplace = True)
# print df.head()
df = pd.merge(df, dfcut, left_index = True, right_index = True)
df = pd.merge(df, dfcolor, left_index = True, right_index = True)
df = pd.merge(df, dfclarity, left_index = True, right_index = True)
print df.head()

#split train and test
#define the training set 
df['is_train'] = np.random.uniform(0,1, len(df)) <= .75
train, test = df[df['is_train'] == True], df[df['is_train'] == False]

#build the forest
#A random forest is a meta estimator that fits a number of decision tree classifiers on 
#various sub-samples of the dataset and use averaging to improve the predictive accuracy 
#and control over-fitting.
#everything except the first column 'carat' is a feature
features = df.columns[1:]
#n_jobs = The number of jobs to run in parallel for both fit and predict
clf = RandomForestClassifier(n_jobs = 2)
y, _ = pd.factorize(train['expensive'])
#train[features] is the training input samples
#y is the target values
#Build a forest of trees from the training set (X, y)
clf.fit(train[features], y)

#make predictions
expected = y
#predict(X)-> Predict class for X
#The predicted class of an input sample is computed as the majority prediction of the 
#trees in the forest.
predicted = clf.predict(train[features])

#view the predictions
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))



