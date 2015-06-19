'''
http://stackoverflow.com/questions/10059594/a-simple-explanation-of-naive-bayes-classification
'''
#This program implements Naive Bayes to predict the onset of Diabetes
'''
Sample from the csv data we will be analyzing
6,148,72,35,0,33.6,0.627,50,1
1,85,66,29,0,26.6,0.351,31,0
8,183,64,0,0,23.3,0.672,32,1
1,89,66,23,94,28.1,0.167,21,0
0,137,40,35,168,43.1,2.288,33,1
'''
import csv
import random
import math
#STEP 1 
#Handle Data: Load the data from CSV file and split it into training and test datasets.
def loadCsv(fiename):
	lines = csv.reader(open(filename, 'rb'))
	dataset = list(lines)
	for i in range(len(dataset)):
		dataset[i] = [float(x) for x in dataset[i]]
	return dataset

#split the data into training(that NB will use to make predictions) 
#and test dataset(that will be used to evaluate the accuracy of the model)
def splitDataset(dataset, splitRatio):
	trainSize = int(len(dataset)*splitRatio)
	print "trainSize = ",trainSize
	trainSet = []
	data = list(dataset)

	while len(trainSet) < trainSize:
		print "data = ",data
		#choose random value from the dataset at index position = index
		index = random.randrange(len(data))
		print "index = ",index
		# append the value chosen at that index into the training set
		# and pop it from the dataset
		trainSet.append(data.pop(index))
		print "trainSet = ",trainSet
		print "data after pop = ",data
	return [trainSet, data]

#STEP 2 - SUMMARIZE DATA
#summarize the properties in the training dataset so that we can 
#calculate probabilities and make predictions.
'''
Separate Data By Class
Calculate Mean
Calculate Standard Deviation
Summarize Dataset
Summarize Attributes By Class
'''
#creating a map of each class value to a list of instances that belong
#to that class and
#sort the entire dataset of instances into the appropriate lists
def separateByClass(dataset):
	separated = {}
	for i in range(len(dataset)):
		vector = dataset[i]
		#vector[-1] or the last element is the class
		#if the last element(class) is not present as a key in the dict
		if vector[-1] not in separated:
			#add it to the dict with empty values
			separated[vector[-1]] = []
			#print separated
		#append the values of the list with the class value specified
		separated[vector[-1]].append(vector)
		#print separated
	return separated

#calculating the mean and std dev
def mean(numbers):
	return sum(numbers)/float(len(numbers))

def stdev(numbers):
	avg = mean(numbers)
	variance = sum([pow(x-avg,2) for x in numbers])/float(len(numbers)-1)
	return math.sqrt(variance)

#Summarize the dataset
#For a given list of instances (for a class value) we can calculate the mean 
#and the standard deviation for each attribute
def summarize(dataset):
	'''
	The zip function groups the values for each attribute across our 
	data instances into their own lists so that we can compute the 
	mean and standard deviation values for the attribute.
	'''
	summaries = [(mean(attribute),stdev(attribute)) for attribute in zip(*dataset)]
	del summaries[-1]
	return summaries

#Summarize Attributes By Class
def summarizeByClass(dataset):
	separated = separateByClass(dataset)
	summaries = {}
	for classvalue, instances in separated.iteritems():
		print "classvalue = ",classvalue
		print "instances = ",instances
		summaries[classvalue] = summarize(instances)
	return summaries


#STEP 3: MAKE PREDICTION - make predictions using the summaries prepared from our training data








filename = 'pima.csv'
#dataset = loadCsv(filename)
dataset = [[1,20,1], [2,21,0], [3,22,1], [4,22,0]]
summary = summarizeByClass(dataset)
#67% of data used for training and 33% for testing
splitRatio = 0.67
print "Loaded file {0} with {1} rows.".format(filename, len(dataset))
train, test = splitDataset(dataset,splitRatio)
print "Split {0} rows into training set with \n\n{1} \n\nand test with \n\n{2}".format(len(dataset), train, test)
separated = separateByClass(dataset)
print "Separated instances by class: {0}".format(separated)

print "Summary by attribute: ",summarize(dataset)
print "Summary by class value \n", summarizeByClass(dataset)
