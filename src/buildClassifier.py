#!/usr/bin/env python

from sklearn.ensemble import RandomForestClassifier
from AngleCalculator import generateAngles
from MakeData import returnLine
import copy
import cPickle
#Author: Ryan Young

#An array of all the files containing data and an array of the labels for each file 
labels = ["Disco", "ChickenDance", "WalkLikeAnEgyptian", "YMCA"]
sub1 = ["../data/PositionsDisco.log", "../data/PositionsChkn.log", "../data/PositionsEgy.log", "../data/Positionsymca.log"]
sub2 = ["../data/TestDisco.log", "../data/TestChkn.log", "../data/TestEgy.log", "../data/TestYMCA.log"]
sub3 = ["../data/JDisco.log", "../data/JChkn.log", "../data/JEgy.log", "../data/JYMCA.log"]


def generateAllAngleTrainingData():
    '''
    This function creates one large TrainingData object 
    containing data from all three participants but uses
    calculated angles as the features for each data sample.
    '''

    #Maybe TODO: Make this so it's easier to add lists of data. 
    trainingData = []
    trainingLabels = []
    index = 0

    for i in xrange(len(labels)):
        #Open the file
        fIn = open(sub1[i], 'r')
        f2In = open(sub2[i], 'r')
        f3In = open(sub3[i], 'r')

        #For each line of the files calculate the 
        # angles inbetween joints and use the resulting 
        # array as the feature vector. Add that to the trainingData.
        for line in fIn:
            features = generateAngles(line)
            trainingData.append(features)
            trainingLabels.append(labels[index])
        fIn.close()

        for line in f2In:
            features = generateAngles(line)
            trainingData.append(features)
            trainingLabels.append(labels[index])
        f2In.close()

        for line in f3In:
            features = generateAngles(line)
            trainingData.append(features)
            trainingLabels.append(labels[index])
        f3In.close()

        index += 1

    #Return the data object
    return trainingData, trainingLabels


def CreateRandomForestClassifier():
    #Train the classifier
    XTrain, yTrain = generateAllAngleTrainingData()
    rfc = RandomForestClassifier(n_estimators=100)
    rfc = rfc.fit(XTrain, yTrain)

    print "Pickling the classifier in classifier.pkl"
    f = open("classifier.pkl", 'wb')

    #Pickle the classifier
    cPickle.dump(rfc, f)
    f.close()


if __name__ == '__main__':
    CreateRandomForestClassifier()
