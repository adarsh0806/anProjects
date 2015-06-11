'''
Label all the members of the test set and then use the misclassification rate to see how 
well you did.
'''
from sklearn.neighbors import KNeighborsClassifier
# fitting the model
model = KNeighborsClassifier(n_neighbors = 3)
model.fit(dfTrain[:,:2], dfTrain[:,2])
# we'll loop through and see what the misclassification rate
# is for different values of k
for k in range(1,20):
	model = KNeighborsClassifier(n_neighbors = k)
	model.fit(dfTrain[:,:2], dfTrain[:,2])
	#make predictions
	expected = dfTest[:,2]
	predicted = model.predict(dfTest)
	#misclassification rate
	error_rate = (predicted != expected).mean()
	print('%d:, %.2f' % (k, error_rate))


#applying k = 5 to the person who needs to be classified as with k = 5 we have the lowest
#misclassification rate
model = KNeighborsClassifier(n_neighbors = 5)
model.fit(dfTrain[:,:2], dfTrain[:,2])
predicted = model.predict([57,37])
print predicted