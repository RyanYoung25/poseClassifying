#!/usr/bin/env python

from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib

#Global random forest classifier object
rfc = None
threshold = .80


def loadClassifier():
    #Update the global rfc with the forest that was pickled
    global rfc

    rfc = joblib.load("./classifier/classifier.pkl")

def classifySample(sample):
    #Take a sample and try to classify it
    # using a random forest
    global rfc
    
    if rfc is None:
        print "Error: Classifier is not loaded"
        return None

    #Calculate the predicted gesture and the probability
    pred = rfc.predict(sample)
    probs = rfc.predict_proba(sample)
    print probs
    maxProb = max(probs[0])
    print maxProb
    #Reject if the probability is less than the threshold
    if maxProb < threshold:
        print "Not a gesture I know"
        return None

    return pred



