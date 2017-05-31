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
	    for x in range(len(dataset)-1):
	        for y in range(4):
	            dataset[x][y] = float(dataset[x][y])
	        if random.random() < split:
	            trainingSet.append(dataset[x])
	        else:
	            testSet.append(dataset[x])

## DRIVER CODE ##

trainingSet=[]
testSet=[]
loadDataset('iris.data', 0.66, trainingSet, testSet)
print 'Train: ' + repr(len(trainingSet))
print 'Test: ' + repr(len(testSet))
