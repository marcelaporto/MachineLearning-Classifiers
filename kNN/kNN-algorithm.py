
## HANDLE DATA
#  load our data file
# split the data into a training dataset and a test dataset
# training dataset: kNN can use to make predictions
# test dataset: used to evaluate the accuracy of the model.

# loadDataset loads a CSV with the provided filename and splits it randomly into train and test datasets using the provided split ratio.
import csv
import random
def loadDataset(filename, split, trainingSet=[] , testSet=[]):
	with open(filename, 'rb') as csvfile:
	    lines = csv.reader(csvfile)
	    dataset = list(lines)
            # print dataset
	    for x in range(len(dataset)-1):
	        for y in range(4):
	            dataset[x][y] = float(dataset[x][y])
	        if random.random() < split:
	            trainingSet.append(dataset[x])
	        else:
	            testSet.append(dataset[x])

## SIMILARITIES
# In order to make predictions we need to calculate the similarity between any two given data instances.
# We'll use the Euclidean distance measure.
# Additionally, we want to control which fields to include in the distance calculation. Specifically, we only want to include the first 4 attributes. One approach is to limit the euclidean distance to a fixed length, ignoring the final dimension

import math
def euclideanDistance(instance1, instance2, length):
	distance = 0
	for x in range(length):
		distance += pow((instance1[x] - instance2[x]), 2)
	return math.sqrt(distance)

## NEIGHBORS

# Now that we have a similarity measure, we can use it collect the k most similar instances for a given unseen instance.
# getNeighbors returns k most similar neighbors from the training set for a given test instance (using the already defined euclideanDistance function)

import operator
def getNeighbors(trainingSet, testInstance, k):
	distances = []
	length = len(testInstance)-1
	for x in range(len(trainingSet)):
		dist = euclideanDistance(testInstance, trainingSet[x], length)
		distances.append((trainingSet[x], dist))
	distances.sort(key=operator.itemgetter(1))
	neighbors = []
	for x in range(k):
		neighbors.append(distances[x][0])
	return neighbors


### DRIVER CODE ###

## HANDLE DATA
trainingSet=[]
testSet=[]
loadDataset('iris.data', 0.66, trainingSet, testSet)
print 'Train: ' + repr(len(trainingSet))
print 'Test: ' + repr(len(testSet))

## SIMILARITIES

data1 = [2, 2, 2, 'a']
data2 = [4, 4, 4, 'b']
distance = euclideanDistance(data1, data2, 3)
print 'Distance: ' + repr(distance)
